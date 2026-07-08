#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI do laço de ingestão assistida (spec docs/ingestao/spec-laco-ingestao.md).
Sub-comandos (§10.1): rascunhar · validar · triar · lote · revisar · promover ·
medir. Opera sobre ingestao/ + manifesto append-only. NÃO toca o Postgres nem
o DDL/read-layer (miolo provado).

Uso:
  python ingestao/laco.py rascunhar [--todos]
  python ingestao/laco.py validar   [--todos | <pacote>]
  python ingestao/laco.py triar      [--todos | <pacote>]
  python ingestao/laco.py triar --confirmar <pacote> --tier T0|T1 --ator X [--justificativa ...]
  python ingestao/laco.py lote montar  --ids a,b,c --semente N [--amostra-pct 100] --ator X
  python ingestao/laco.py lote decidir <lote> --desfecho aprovado|devolvido --ator X
  python ingestao/laco.py revisar <pacote> --papel P --ator X          # interativo (cronômetro)
  python ingestao/laco.py revisar <pacote> --papel P --ator X --abrir  # stepwise: abre
  python ingestao/laco.py revisar <pacote> --papel P --decidir aprovado|devolvido|rejeitado
  python ingestao/laco.py promover <pacote> --ator X
  python ingestao/laco.py medir [--out ingestao/reports/medicao-ingestao.json]
"""
import argparse
import glob
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import corpus
import manifesto as M
import medicao
import promocao
import triagem
import validacao

AQUI = os.path.dirname(os.path.abspath(__file__))
RASCUNHOS = os.path.join(AQUI, "rascunhos")
REPORTS = os.path.join(AQUI, "reports")
THROTTLE = 30  # intake throttling (Art.13 / spec §2): teto de pacotes em-revisão

CHECKLIST_61 = """  Checklist integral §6.1 — por claim/relação:
   (1) a fonte ABRE e SUSTENTA o statement no localizador citado;
   (2) authority_tier correto;  (3) claim_type = o MAIS FRACO compatível (nunca promovido);
   (4) confidence/evidence_level coerentes;  (5) tempo (3Z, precisão, incerteza) correto;
   (6) geo/correspondência moderna corretos;  (7) PG5 correta;
   (8) licença da fonte compatível com o uso;  (9) relação: direção e tipo sustentados;
   (10) ClaimSet: resolution escrita À MÃO, pesos assimétricos conferidos (sem falsa equivalência)."""


# ------------------------------------------------------------------ utilidades
def caminho_pacote(pid):
    return os.path.join(RASCUNHOS, pid + ".json")


def carregar(pid):
    with open(caminho_pacote(pid), encoding="utf-8") as f:
        return json.load(f)


def todos_rascunhos():
    out = {}
    for p in sorted(glob.glob(os.path.join(RASCUNHOS, "*.json"))):
        pid = os.path.splitext(os.path.basename(p))[0]
        with open(p, encoding="utf-8") as f:
            out[pid] = json.load(f)
    return out


def open_ids_exceto(pid, drafts):
    ids = set()
    for k, pkg in drafts.items():
        if k == pid:
            continue
        iid = (pkg.get("item") or {}).get("id")
        if iid:
            ids.add(iid)
    return ids


def _ultimo_tier_confirmado(pid, eventos):
    tier = None
    for ev in eventos:
        if ev["evento"] == "triagem_confirmada" and ev.get("pacote") == pid:
            tier = ev.get("tier")
    return tier


def _em_revisao(eventos):
    """Pacotes triados mas ainda sem desfecho — carga de revisão (throttling)."""
    triados, decididos = set(), set()
    for ev in eventos:
        if ev["evento"] == "triagem_confirmada":
            triados.add(ev.get("pacote"))
        elif ev["evento"] == "pacote_decidido":
            decididos.add(ev.get("pacote"))
    return triados - decididos


# ------------------------------------------------------------------ comandos
def cmd_rascunhar(a):
    """Registra no laço os rascunhos-arquivo ainda não registrados (a 'IA' os
    produz como JSON; aqui entram no manifesto com pacote_gerado). Respeita o
    intake throttling (§2)."""
    eventos = M.ler()
    ja = {ev.get("pacote") for ev in eventos if ev["evento"] == "pacote_gerado"}
    drafts = todos_rascunhos()
    novos = [pid for pid in drafts if pid not in ja]
    if not novos:
        print("nada a registrar (todos os rascunhos já estão no manifesto)."); return 0
    carga = len(_em_revisao(eventos))
    registrados = 0
    for pid in novos:
        if carga >= THROTTLE:
            print(f"THROTTLING (§2): {carga} pacotes em-revisão ≥ {THROTTLE}; "
                  f"a geração pausa. Restam {len(novos)-registrados} rascunhos não registrados.")
            break
        pkg = drafts[pid]
        M.registrar("pacote_gerado", pacote=pid,
                    n_claims=len(pkg.get("claims") or []),
                    n_fontes=len(pkg.get("sources") or []),
                    n_relacoes=len(pkg.get("relations") or []),
                    ms_maquina=pkg.get("ms_maquina", 0),
                    tier_proposto=pkg.get("tier_proposto"))
        registrados += 1
        print(f"registrado: {pid} (claims={len(pkg.get('claims') or [])})")
    print(f"{registrados} rascunho(s) registrado(s).")
    return 0


def _validar_um(pid, pkg, corpus_ids, drafts):
    ok, falhas = validacao.validate_pacote(pkg, corpus_ids, open_ids_exceto(pid, drafts))
    M.registrar("validacao", pacote=pid, resultado=("pass" if ok else "fail"),
                n_falhas=len(falhas))
    if ok:
        print(f"[pass] {pid}")
    else:
        print(f"[fail] {pid} — {len(falhas)} falha(s):")
        for x in falhas:
            print(f"        · {x}")
    return ok


def cmd_validar(a):
    drafts = todos_rascunhos()
    corpus_ids = corpus.ids_corpus()
    alvos = list(drafts) if a.todos or not a.pacote else [a.pacote]
    todos_ok = True
    for pid in alvos:
        if pid not in drafts:
            print(f"pacote inexistente: {pid}"); todos_ok = False; continue
        todos_ok &= _validar_um(pid, drafts[pid], corpus_ids, drafts)
    return 0 if todos_ok else 1


def cmd_triar(a):
    drafts = todos_rascunhos()
    if a.confirmar:
        pid = a.confirmar
        if pid not in drafts:
            print(f"pacote inexistente: {pid}"); return 1
        pkg = drafts[pid]
        tier_calc, motivos = triagem.triar(pkg)
        proposto = pkg.get("tier_proposto")
        # afrouxar T0→T1 exige justificativa (§2 tabela de atores)
        if a.tier == "T1" and tier_calc == "T0" and not a.justificativa:
            print(f"RECUSADO: afrouxar para T1 contra a triagem (motivos: {motivos}) "
                  f"exige --justificativa (§5).")
            return 1
        M.registrar("triagem_confirmada", pacote=pid, tier=a.tier, ator=a.ator,
                    tier_proposto=proposto, tier_calculado=tier_calc,
                    justificativa=a.justificativa)
        print(f"triagem confirmada: {pid} → {a.tier} (proposto={proposto}, calculado={tier_calc}).")
        return 0
    # modo relatório: propõe/mostra a triagem calculada
    alvos = list(drafts) if a.todos or not a.pacote else [a.pacote]
    for pid in alvos:
        if pid not in drafts:
            print(f"pacote inexistente: {pid}"); continue
        tier_calc, motivos = triagem.triar(drafts[pid])
        marca = "T1-elegível" if tier_calc == "T1" else "T0"
        print(f"{pid}: {marca}" + ("" if tier_calc == "T1" else f"  ← {motivos}"))
    return 0


def cmd_lote(a):
    eventos = M.ler()
    if a.acao == "montar":
        ids = [x.strip() for x in a.ids.split(",") if x.strip()]
        if not (10 <= len(ids) <= 25):
            print(f"RECUSADO: lote T1 deve ter 10–25 pacotes (§6.3); recebidos {len(ids)}.")
            return 1
        pct = a.amostra_pct
        n = len(ids) if pct >= 100 else max(5, math.ceil(len(ids) * pct / 100.0))
        n = min(n, len(ids))
        rng = random.Random(a.semente)
        amostra = sorted(rng.sample(ids, n))
        lote_id = a.lote or ("lote-%d" % (1 + sum(1 for ev in eventos if ev["evento"] == "lote_montado")))
        M.registrar("lote_montado", lote=lote_id, ids=ids, semente=a.semente,
                    amostra=amostra, amostra_pct=pct, ator=a.ator)
        print(f"lote {lote_id} montado: {len(ids)} pacotes; amostra ({pct}%, semente {a.semente}) "
              f"= {len(amostra)}: {amostra}")
        return 0
    if a.acao == "decidir":
        M.registrar("lote_decidido", lote=a.lote_id, desfecho=a.desfecho, ator=a.ator)
        print(f"lote {a.lote_id} decidido: {a.desfecho}.")
        if a.desfecho == "devolvido":
            print("  (1 defeito crítico em qualquer amostrado ⇒ lote INTEIRO devolvido — Art.13)")
        return 0
    return 1


def cmd_revisar(a):
    pid = a.pacote
    if not os.path.exists(caminho_pacote(pid)):
        print(f"pacote inexistente: {pid}"); return 1
    tier = _ultimo_tier_confirmado(pid, M.ler())
    # modo stepwise por flags (testável / não-interativo)
    if a.abrir:
        M.registrar("pacote_aberto", pacote=pid, papel=a.papel, ator=a.ator, tier=tier)
        print(f"aberto {pid} (papel={a.papel}). Cronômetro correndo. "
              f"Decida com: revisar {pid} --papel {a.papel} --decidir <desfecho>.")
        return 0
    if a.decidir:
        M.registrar("pacote_decidido", pacote=pid, papel=a.papel, ator=a.ator,
                    tier=tier, desfecho=a.decidir, motivo=a.motivo)
        print(f"decidido {pid}: {a.decidir}" + (f" ({a.motivo})" if a.motivo else ""))
        return 0
    if a.pausa_inicio:
        M.registrar("pausa_inicio", pacote=pid, papel=a.papel, ator=a.ator); print("pausa iniciada."); return 0
    if a.pausa_fim:
        M.registrar("pausa_fim", pacote=pid, papel=a.papel, ator=a.ator); print("pausa encerrada."); return 0
    # modo interativo (cronômetro): abre, mostra o checklist, lê a decisão
    return _revisar_interativo(pid, a.papel, a.ator, tier)


def _revisar_interativo(pid, papel, ator, tier):
    pkg = carregar(pid)
    M.registrar("pacote_aberto", pacote=pid, papel=papel, ator=ator, tier=tier)
    print(f"\n=== REVISÃO {pid}  ·  papel={papel}  ·  tier={tier}  ·  ator={ator} ===")
    print(json.dumps(pkg, ensure_ascii=False, indent=2))
    print(CHECKLIST_61)
    print("\nComandos: [a]provado  [d]evolvido  [r]ejeitado  [p]ausa/retoma  [q]sai-sem-decidir")
    pausado = False
    while True:
        try:
            c = input("decisão> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nsaída sem decisão — amostra de tempo DESCARTADA (§1.5)."); return 0
        if c in ("p",):
            if not pausado:
                M.registrar("pausa_inicio", pacote=pid, papel=papel, ator=ator); pausado = True; print("… pausado")
            else:
                M.registrar("pausa_fim", pacote=pid, papel=papel, ator=ator); pausado = False; print("… retomado")
        elif c in ("a", "d", "r"):
            if pausado:
                M.registrar("pausa_fim", pacote=pid, papel=papel, ator=ator); pausado = False
            desf = {"a": "aprovado", "d": "devolvido", "r": "rejeitado"}[c]
            motivo = input("motivo (tipado, opcional)> ").strip() or None
            M.registrar("pacote_decidido", pacote=pid, papel=papel, ator=ator, tier=tier,
                        desfecho=desf, motivo=motivo)
            print(f"decidido: {desf}."); return 0
        elif c in ("q",):
            print("saída sem decisão — amostra de tempo DESCARTADA (§1.5)."); return 0
        else:
            print("comando inválido.")


def cmd_promover(a):
    pid = a.pacote
    if not os.path.exists(caminho_pacote(pid)):
        print(f"pacote inexistente: {pid}"); return 1
    pkg = carregar(pid)
    eventos = M.ler()
    tier = a.tier or _ultimo_tier_confirmado(pid, eventos) or "T0"
    try:
        reg = promocao.promover(pkg, tier, a.ator, eventos=eventos,
                                commit_hash=a.commit)
    except promocao.PromocaoRecusada as ex:
        print(f"RECUSADO: {ex}"); return 1
    print(f"promovido {pid} → carga-promovida.jsonl (review_status={reg['review_status']}, tier={tier}).")
    if reg["review_status"] == "pending":
        print("  PG5 sensível sem papel competente designado ⇒ entra 'pending' na fila viva "
              "(docs/fila-revisao-claimsets-sensiveis.md); Art.6: não é fato para o público.")
    print("  Lembrete R6: regenere reports + pinos (verify/test_a4) + README no MESMO commit.")
    return 0


def cmd_medir(a):
    rep = medicao.gerar_report()
    out = a.out or os.path.join(REPORTS, "medicao-ingestao.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=2)
    print(json.dumps(rep, ensure_ascii=False, indent=2))
    print(f"\nreport gravado em {out}")
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="laco", description="Laço de ingestão assistida (v0).")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("rascunhar").add_argument("--todos", action="store_true")

    v = sub.add_parser("validar"); v.add_argument("pacote", nargs="?"); v.add_argument("--todos", action="store_true")

    t = sub.add_parser("triar")
    t.add_argument("pacote", nargs="?"); t.add_argument("--todos", action="store_true")
    t.add_argument("--confirmar"); t.add_argument("--tier", choices=["T0", "T1"])
    t.add_argument("--ator", default="dono"); t.add_argument("--justificativa")

    lo = sub.add_parser("lote"); losub = lo.add_subparsers(dest="acao", required=True)
    lm = losub.add_parser("montar")
    lm.add_argument("--ids", required=True); lm.add_argument("--semente", type=int, required=True)
    lm.add_argument("--amostra-pct", dest="amostra_pct", type=int, default=100)
    lm.add_argument("--lote"); lm.add_argument("--ator", default="dono")
    ld = losub.add_parser("decidir")
    ld.add_argument("lote_id"); ld.add_argument("--desfecho", choices=["aprovado", "devolvido"], required=True)
    ld.add_argument("--ator", default="dono")

    r = sub.add_parser("revisar")
    r.add_argument("pacote"); r.add_argument("--papel", required=True); r.add_argument("--ator", default="dono")
    r.add_argument("--abrir", action="store_true")
    r.add_argument("--decidir", choices=["aprovado", "devolvido", "rejeitado"])
    r.add_argument("--motivo"); r.add_argument("--pausa-inicio", dest="pausa_inicio", action="store_true")
    r.add_argument("--pausa-fim", dest="pausa_fim", action="store_true")

    pr = sub.add_parser("promover")
    pr.add_argument("pacote"); pr.add_argument("--ator", default="dono")
    pr.add_argument("--tier", choices=["T0", "T1"]); pr.add_argument("--commit")

    sub.add_parser("medir").add_argument("--out")
    return p


DISPATCH = {"rascunhar": cmd_rascunhar, "validar": cmd_validar, "triar": cmd_triar,
            "lote": cmd_lote, "revisar": cmd_revisar, "promover": cmd_promover, "medir": cmd_medir}


def main(argv=None):
    a = build_parser().parse_args(argv)
    return DISPATCH[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
