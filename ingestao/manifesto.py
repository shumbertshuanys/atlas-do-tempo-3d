# -*- coding: utf-8 -*-
"""
Manifesto append-only da ingestão (spec §1.5) — a ÚNICA fonte de tempo é o
timestamp gerado por esta ferramenta no momento do evento. Auto-relato é
inadmissível (PG1: evidência, não afirmação).

Cada evento é uma linha JSON em ingestao/manifest.jsonl. Nunca se reescreve
uma linha; só se acrescenta. O tempo (`t`) é ISO-8601 UTC gerado aqui.

Eventos (§1.5): pacote_gerado · validacao · triagem_confirmada ·
sessao_inicio/fim · pacote_aberto · pacote_decidido · pausa_inicio/fim ·
lote_montado · lote_decidido · promovido.
"""
import json
import os
from datetime import datetime, timezone

_AQUI = os.path.dirname(os.path.abspath(__file__))
MANIFESTO = os.path.join(_AQUI, "manifest.jsonl")


def agora_iso():
    """Timestamp de FERRAMENTA (UTC, ISO-8601). Fonte de tempo canônica."""
    return datetime.now(timezone.utc).isoformat()


def registrar(evento, caminho=None, **campos):
    """Acrescenta um evento ao manifesto (append-only). Retorna o registro."""
    caminho = caminho or MANIFESTO
    reg = {"evento": evento, "t": agora_iso()}
    reg.update({k: v for k, v in campos.items() if v is not None})
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "a", encoding="utf-8") as fp:
        fp.write(json.dumps(reg, ensure_ascii=False) + "\n")
    return reg


def ler(caminho=None):
    """Lê os eventos do manifesto em ordem de append."""
    caminho = caminho or MANIFESTO
    if not os.path.exists(caminho):
        return []
    out = []
    with open(caminho, encoding="utf-8") as fp:
        for linha in fp:
            linha = linha.strip()
            if linha:
                out.append(json.loads(linha))
    return out


def _t(reg):
    return datetime.fromisoformat(reg["t"])


def _pausas_no_intervalo(eventos, ini, fim):
    """Segundos de pausa (pausa_inicio→pausa_fim) contidos em [ini,fim]."""
    total = 0.0
    aberta = None
    for ev in eventos:
        if ev["evento"] == "pausa_inicio" and ini <= _t(ev) <= fim:
            aberta = _t(ev)
        elif ev["evento"] == "pausa_fim" and aberta is not None:
            fim_p = min(_t(ev), fim)
            total += max(0.0, (fim_p - aberta).total_seconds())
            aberta = None
    return total


def amostras_de_revisao(eventos):
    """Reconstrói as amostras de tempo humano de revisão a partir do log.

    Cada par (pacote_aberto → próximo pacote_decidido do MESMO pacote e papel)
    é uma passada. segundos = (decidido − aberto) − pausas contidas.
    pacote_aberto sem pacote_decidido correspondente ⇒ amostra INCOMPLETA
    (registrada, mas DESCARTADA da estatística — §1.5).

    Retorna lista de dicts: {pacote, papel, ator, tier, desfecho, segundos,
    completa}.
    """
    amostras = []
    abertos = {}  # (pacote, papel) -> evento de abertura pendente
    for ev in eventos:
        tipo = ev["evento"]
        if tipo == "pacote_aberto":
            chave = (ev.get("pacote"), ev.get("papel"))
            # abertura nova sobrepõe abertura pendente sem decisão: a anterior
            # vira amostra incompleta (descartada da estatística).
            if chave in abertos:
                ant = abertos[chave]
                amostras.append({"pacote": ant.get("pacote"), "papel": ant.get("papel"),
                                 "ator": ant.get("ator"), "tier": ant.get("tier"),
                                 "desfecho": None, "segundos": None, "completa": False})
            abertos[chave] = ev
        elif tipo == "pacote_decidido":
            chave = (ev.get("pacote"), ev.get("papel"))
            ab = abertos.pop(chave, None)
            if ab is None:
                continue  # decisão sem abertura correspondente: ignorada
            ini, fim = _t(ab), _t(ev)
            seg = (fim - ini).total_seconds() - _pausas_no_intervalo(eventos, ini, fim)
            amostras.append({"pacote": ev.get("pacote"), "papel": ab.get("papel"),
                             "ator": ab.get("ator") or ev.get("ator"),
                             "tier": ab.get("tier") or ev.get("tier"),
                             "desfecho": ev.get("desfecho"),
                             "segundos": max(0.0, seg), "completa": True})
    # aberturas que nunca decidiram: incompletas (descartadas da estatística)
    for ab in abertos.values():
        amostras.append({"pacote": ab.get("pacote"), "papel": ab.get("papel"),
                         "ator": ab.get("ator"), "tier": ab.get("tier"),
                         "desfecho": None, "segundos": None, "completa": False})
    return amostras


def hash_manifesto(caminho=None):
    """Hash do conteúdo do manifesto (para carimbar o report — §8)."""
    import hashlib
    caminho = caminho or MANIFESTO
    if not os.path.exists(caminho):
        return None
    with open(caminho, "rb") as fp:
        return hashlib.sha256(fp.read()).hexdigest()
