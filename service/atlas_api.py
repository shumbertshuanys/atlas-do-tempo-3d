#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A3 · D-A3.4
atlas_api.py — SERVIÇO FINO SÓ-LEITURA (2 endpoints, 2 papéis de banco).

Fronteira HTTP mínima sobre o envelope MomentResult (011). NÃO monta o envelope:
serializa o que o banco devolve (Etapa 11 §6.3 [NORMATIVO] — leitura factual não
é "texto pelado"; o gating e os campos §8 já vêm do autoritativo).

Desenho (D-A3.4/D-A3.5):
  * GET /momento/publico    → conecta como atlas_public (EXECUTE só na pública).
  * GET /momento/curatorial → exige header de auth; conecta como atlas_curatorial.
  * Qualquer método de ESCRITA (POST/PUT/PATCH/DELETE) → 405. Não há rota de
    escrita; o serviço não possui credencial de escrita no banco (ambos os papéis
    são leitura-via-função). O portão é o GRANT, não um `if` aqui.

Stdlib apenas (http.server + psycopg2, já dependência). Bind 127.0.0.1.
Config por ambiente: ATLAS_PG_HOST/PORT/DB, ATLAS_PUBLIC_PW, ATLAS_CURATORIAL_PW,
ATLAS_CURATORIAL_TOKEN, ATLAS_API_HOST/PORT.
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import psycopg2

# Config 12-factor (Opção A): host/porta/db NÃO são segredo (default ok); as
# credenciais e o token são OBRIGATÓRIOS — o serviço RECUSA subir sem eles,
# erra ALTO e não faz fallback silencioso (§5.6 do plano; guarda PG1).
PG_HOST = os.environ.get("ATLAS_PG_HOST", "localhost")
PG_PORT = os.environ.get("ATLAS_PG_PORT", "5432")
PG_DB = os.environ.get("ATLAS_PG_DB", "atlas")


def _require(name):
    v = os.environ.get(name)
    if not v:
        sys.stderr.write(
            "ERRO: variável de ambiente obrigatória %s ausente.\n"
            "O serviço NÃO sobe sem ela (12-factor; sem fallback silencioso).\n"
            "Defina-a no .env (veja .env.example) ou exporte no ambiente.\n" % name)
        sys.exit(2)
    return v


PUBLIC_PW = _require("ATLAS_PUBLIC_PASSWORD")
CURATORIAL_PW = _require("ATLAS_CURATORIAL_PASSWORD")
CURATORIAL_TOKEN = _require("ATLAS_CURATORIAL_TOKEN")
API_HOST = os.environ.get("ATLAS_API_HOST", "127.0.0.1")
API_PORT = int(os.environ.get("ATLAS_API_PORT", "8765"))

# DSNs por PAPEL — o serviço só tem credencial de LEITURA-via-função.
# Nenhum DSN aqui é capaz de escrever (os papéis não têm grant de escrita).
DSN_PUBLIC = "host=%s port=%s dbname=%s user=atlas_public password=%s" % (
    PG_HOST, PG_PORT, PG_DB, PUBLIC_PW)
DSN_CURATORIAL = "host=%s port=%s dbname=%s user=atlas_curatorial password=%s" % (
    PG_HOST, PG_PORT, PG_DB, CURATORIAL_PW)


def _float(qs, key, default):
    try:
        return float(qs.get(key, [default])[0])
    except (TypeError, ValueError):
        return default


def _lenses(qs):
    raw = qs.get("lenses", [None])[0]
    if not raw:
        return None
    return [s for s in raw.split(",") if s]


def fetch_envelope(dsn, fn, start, end, lenses):
    """Chama a função-porta e devolve o envelope JSON (to_jsonb no banco).
    Propaga psycopg2.Error (ex.: permission denied) para o chamador tratar."""
    conn = psycopg2.connect(dsn)
    try:
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor()
        cur.execute("SELECT to_jsonb(m) FROM %s(%%s,%%s,%%s) m" % fn, (start, end, lenses))
        row = cur.fetchone()
        cur.close()
        return row[0] if row else None
    finally:
        conn.close()


class Handler(BaseHTTPRequestHandler):
    server_version = "AtlasReadOnly/1.0"

    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # silencioso (teste captura via HTTP)
        pass

    def do_GET(self):
        u = urlparse(self.path)
        qs = parse_qs(u.query)
        if u.path == "/health":
            return self._send(200, {"status": "ok", "mode": "read-only"})

        if u.path == "/momento/publico":
            start = _float(qs, "start", -1e12)
            end = _float(qs, "end", 1e12)
            try:
                env = fetch_envelope(DSN_PUBLIC, "core.f_momento_publico", start, end, _lenses(qs))
                return self._send(200, env)
            except psycopg2.Error as ex:
                return self._send(500, {"error": "db", "detail": str(ex).strip()})

        if u.path == "/momento/curatorial":
            token = self.headers.get("X-Atlas-Auth")
            if token != CURATORIAL_TOKEN:
                return self._send(401, {"error": "auth",
                                        "detail": "porta curatorial exige X-Atlas-Auth válido"})
            start = _float(qs, "start", -1e12)
            end = _float(qs, "end", 1e12)
            try:
                env = fetch_envelope(DSN_CURATORIAL, "core.f_momento_curatorial", start, end, _lenses(qs))
                return self._send(200, env)
            except psycopg2.Error as ex:
                # se o portão por grant negar EXECUTE, isto não deveria acontecer
                # para atlas_curatorial; vira 403 explícito por clareza.
                return self._send(403, {"error": "forbidden", "detail": str(ex).strip()})

        return self._send(404, {"error": "not_found", "path": u.path})

    # Sem rotas de escrita: qualquer método mutante é 405 (sem caminho de escrita).
    def _deny_write(self):
        self.send_response(405)
        self.send_header("Allow", "GET")
        self.send_header("Content-Length", "0")
        self.end_headers()

    do_POST = _deny_write
    do_PUT = _deny_write
    do_PATCH = _deny_write
    do_DELETE = _deny_write


def main():
    httpd = ThreadingHTTPServer((API_HOST, API_PORT), Handler)
    print("atlas_api (read-only) em http://%s:%d — GET /momento/publico|/momento/curatorial" % (
        API_HOST, API_PORT), flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == "__main__":
    main()
