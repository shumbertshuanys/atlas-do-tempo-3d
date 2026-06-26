#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A3 · D-A3.4/D-A3.5 (artefato falsificável / PG1)
test_a3_http.py — prova o PORTÃO POR GRANT e a fronteira HTTP só-leitura:

  * A3-HTTP-1 (NEGATIVO, deve falhar): atlas_public chamando f_momento_curatorial
    → permission denied. Se suceder, alguém afrouxou o grant (R-A3.7).  ← artefato-chave
  * A3-HTTP-2 (positivo): atlas_public chama f_momento_publico → envelope.
  * A3-HTTP-3 (positivo): GET /momento/publico → JSON com items[] §8; nenhum isFact=false.
  * A3-HTTP-4 (negativo): método de escrita → 405; e o papel mais privilegiado do
    serviço (atlas_curatorial) NÃO consegue escrever (sem credencial de escrita).
  * A3-HTTP-5: GET /momento/curatorial sem token → 401; com token → envelope curatorial.

Requer 020-papeis-leitura.sql aplicado (papéis atlas_public/atlas_curatorial).
Sobe o serviço (service/atlas_api.py) como subprocesso em porta de teste.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

import psycopg2

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT_DIR = os.path.join(REPO, "out")
SERVICE = os.path.join(REPO, "service", "atlas_api.py")

PORT = int(os.environ.get("ATLAS_TEST_PORT", "8799"))
TOKEN = "token-teste-curatorial"
BASE = "http://127.0.0.1:%d" % PORT

DSN_PUBLIC = "host=localhost dbname=atlas user=atlas_public password=%s" % os.environ["ATLAS_PUBLIC_PASSWORD"]
DSN_CURATORIAL = "host=localhost dbname=atlas user=atlas_curatorial password=%s" % os.environ["ATLAS_CURATORIAL_PASSWORD"]

KPG = (-66.05e6, -65.95e6)
CHAVES_8 = ["itemId", "title", "itemType", "epistemicType", "confidenceLevel",
            "selo", "isFact", "reviewStatus", "geometryRegime",
            "reconstructionFlag", "uncertaintyDisplayPolicy"]

testes = []


def reg(tid, descr, passou, detalhe):
    testes.append({"id": tid, "descricao": descr, "passou": bool(passou), "detalhe": detalhe})


def http_get(path, headers=None):
    req = urllib.request.Request(BASE + path, headers=headers or {}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            body = json.loads(body)
        except ValueError:
            pass
        return e.code, body


def http_method(path, method):
    req = urllib.request.Request(BASE + path, method=method, data=b"" if method != "GET" else None)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


# --- sobe o serviço ---------------------------------------------------------
env = dict(os.environ)
env["ATLAS_API_PORT"] = str(PORT)
env["ATLAS_CURATORIAL_TOKEN"] = TOKEN
proc = subprocess.Popen([sys.executable, SERVICE], env=env,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    # espera /health
    pronto = False
    for _ in range(50):
        try:
            st, _body = http_get("/health")
            if st == 200:
                pronto = True
                break
        except Exception:
            pass
        time.sleep(0.2)
    if not pronto:
        reg("A3-HTTP-0", "serviço sobe e responde /health", False, "serviço não respondeu em ~10s")

    # --- A3-HTTP-1 (negativo, deve falhar): atlas_public → curatorial = denied ---
    negado = False
    detalhe1 = ""
    try:
        c = psycopg2.connect(DSN_PUBLIC)
        c.set_session(readonly=True, autocommit=True)
        cu = c.cursor()
        try:
            cu.execute("SELECT core.f_momento_curatorial(%s,%s,%s)", (KPG[0], KPG[1], None))
            cu.fetchone()
            detalhe1 = "ERRO: atlas_public executou a curatorial (grant afrouxado!)"
        except psycopg2.errors.InsufficientPrivilege as ex:
            negado = True
            detalhe1 = "permission denied (esperado): %s" % str(ex).strip().splitlines()[0]
        finally:
            c.close()
    except psycopg2.Error as ex:
        detalhe1 = "erro de conexão: %s" % ex
    reg("A3-HTTP-1", "atlas_public NÃO pode executar f_momento_curatorial (portão por grant)",
        negado, detalhe1)

    # --- A3-HTTP-2 (positivo): atlas_public → pública = ok ----------------------
    ok2 = False
    detalhe2 = ""
    try:
        c = psycopg2.connect(DSN_PUBLIC)
        c.set_session(readonly=True, autocommit=True)
        cu = c.cursor()
        cu.execute("SELECT to_jsonb(m) FROM core.f_momento_publico(%s,%s,%s) m", (KPG[0], KPG[1], None))
        env2 = cu.fetchone()[0]
        c.close()
        ok2 = (isinstance(env2, dict) and env2.get("porta") == "publica"
               and isinstance(env2.get("items"), list) and len(env2["items"]) >= 1)
        detalhe2 = "porta=%s, n_items=%d" % (env2.get("porta"), len(env2.get("items", [])))
    except psycopg2.Error as ex:
        detalhe2 = "ERRO: grant apertado demais quebrou o legítimo: %s" % ex
    reg("A3-HTTP-2", "atlas_public executa f_momento_publico com sucesso (envelope)", ok2, detalhe2)

    # --- A3-HTTP-3 (positivo): GET público → items §8; nenhum isFact=false ------
    st3, env3 = http_get("/momento/publico?start=%s&end=%s" % KPG)
    its3 = env3.get("items", []) if isinstance(env3, dict) else []
    faltas = [("%s.%s" % (it.get("itemId"), k)) for it in its3 for k in CHAVES_8
              if k not in it or it[k] is None]
    nao_fato = [it.get("itemId") for it in its3 if it.get("isFact") is not True]
    reg("A3-HTTP-3", "GET público → JSON com items[] §8; nenhum isFact=false",
        st3 == 200 and its3 and not faltas and not nao_fato,
        "status=%s, n_items=%d, faltas§8=%s, isFact=false=%s." % (
            st3, len(its3), faltas or "nenhuma", nao_fato or "nenhum"))

    # --- A3-HTTP-4 (negativo): escrita → 405; e papel sem credencial de escrita -
    st_post = http_method("/momento/publico", "POST")
    st_put = http_method("/momento/publico", "PUT")
    st_del = http_method("/momento/publico", "DELETE")
    metodos_405 = (st_post == 405 and st_put == 405 and st_del == 405)
    # papel mais privilegiado do serviço NÃO escreve:
    sem_escrita = False
    detalhe_w = ""
    try:
        c = psycopg2.connect(DSN_CURATORIAL)
        c.set_session(autocommit=True)
        cu = c.cursor()
        try:
            cu.execute("INSERT INTO core.entity_node(uri,entity_kind) VALUES ('item:_w_probe','item')")
            detalhe_w = "ERRO: atlas_curatorial conseguiu INSERT (tem credencial de escrita!)"
        except psycopg2.errors.InsufficientPrivilege as ex:
            sem_escrita = True
            detalhe_w = "INSERT negado (esperado): %s" % str(ex).strip().splitlines()[0]
        finally:
            c.close()
    except psycopg2.Error as ex:
        detalhe_w = "erro: %s" % ex
    reg("A3-HTTP-4", "escrita HTTP → 405; serviço sem credencial de escrita no banco",
        metodos_405 and sem_escrita,
        "POST/PUT/DELETE=%s/%s/%s (esperado 405); %s" % (st_post, st_put, st_del, detalhe_w))

    # --- A3-HTTP-5: curatorial sem token → 401; com token → envelope ------------
    st_sem, _b = http_get("/momento/curatorial?start=%s&end=%s" % KPG)
    st_com, env5 = http_get("/momento/curatorial?start=%s&end=%s" % KPG,
                            headers={"X-Atlas-Auth": TOKEN})
    com_ok = (st_com == 200 and isinstance(env5, dict) and env5.get("porta") == "curatorial"
              and isinstance(env5.get("items"), list))
    reg("A3-HTTP-5", "curatorial sem token → 401; com token → envelope curatorial",
        st_sem in (401, 403) and com_ok,
        "sem token=%s (esperado 401/403); com token=%s, porta=%s." % (
            st_sem, st_com, env5.get("porta") if isinstance(env5, dict) else "-"))

finally:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()

passaram = sum(1 for t in testes if t["passou"])
report = {
    "total": len(testes),
    "passaram": passaram,
    "falharam": len(testes) - passaram,
    "porta_teste": PORT,
    "testes": testes,
}
os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "test_a3_http_report.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print(json.dumps(report, ensure_ascii=False, indent=2))
if report["falharam"] != 0:
    sys.exit(1)
