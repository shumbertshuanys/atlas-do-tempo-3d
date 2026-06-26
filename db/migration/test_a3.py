#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A3 · D-A3.3 (artefato falsificável / PG1)
test_a3.py — prova que o ENVELOPE MomentResult (forma β) respeita o contrato §8
e o gating por construção (Etapa 11 §6.3 [NORMATIVO] + Playbook §8 + Art.6/§9):

  * a porta PÚBLICA (core.f_momento_publico) NUNCA devolve não-fato: todo item
    tem isFact=true, selo='público', reviewStatus='approved'; nada pending/
    legal-review/rejected/seeded (A3-T2 — espelha A4-T1..T4, mas no envelope);
  * a leitura factual NUNCA é "texto pelado": todo item carrega as chaves §8
    não-nulas (A3-T3) — incl. attributionRef.provenanceRef ([N1], A3-T5);
  * incerteza nunca 'omitir' (A3-T4); paleo em tempo profundo = reconstrução,
    nunca fato documentado/medição direta (A3-T6);
  * selo×is_fact coerentes: seeded→nunca fato; pending→em-revisão; corpus+
    approved→fato (A3-T7);
  * ClaimSet só vaza pela pública se o HOST for público (A3-T8); pesos
    assimétricos + fronteira escrita à mão, sem falsa equivalência (A3-T9);
  * items(pública) ⊆ items(curatorial); lente sem match → array vazio, não erro
    (A3-T10).

Forma β: cada função devolve UMA linha (RETURNS core.t_momento). A3-T1 falha se
virar SETOF ou faltar chave. Conecta como 'atlas' (dono) — o portão por grant
(papéis atlas_public/atlas_curatorial) é provado pela suíte HTTP, não aqui.

Janelas canônicas: 1789=[-212,-210]; GOE≈-2,4e9; K-Pg=[-66.05e6,-65.95e6].
"""
import json
import os
import sys
import psycopg2

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DSN = "host=localhost dbname=atlas user=atlas password=%s" % os.environ["ATLAS_DB_PASSWORD"]
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "out")

JANELAS = {
    "1789 (intervalo do ano)": (-212.0, -210.0),
    "GOE ~2,4 Ga": (-2.4e9, -2.4e9),
    "K-Pg ~66 Ma": (-66.05e6, -65.95e6),
}

# Chaves §8 que TODO item carrega, não-nulas (contrato §5.2; campos firmes).
CHAVES_8 = ["itemId", "title", "itemType", "epistemicType", "confidenceLevel",
            "selo", "isFact", "reviewStatus", "geometryRegime",
            "reconstructionFlag", "uncertaintyDisplayPolicy"]
POLITICAS_VALIDAS = {"sempreRotular", "rótuloCompacto", "aparatoCompleto"}

# Colunas esperadas do envelope (forma β) — A3-T1.
COLUNAS_ENVELOPE = ["porta", "query", "normalized_time_range", "normalized_spatial_scope",
                    "items", "states", "claim_sets", "uncertainty_profiles",
                    "anachronism_warnings", "equivalence_warnings", "publicability_status",
                    "gating_reason", "gating_type", "hidden_summary",
                    "navigation_suggestions", "generated_scene_candidate"]

testes = []


def reg(tid, descr, passou, detalhe):
    testes.append({"id": tid, "descricao": descr, "passou": bool(passou), "detalhe": detalhe})


def asjson(v):
    """psycopg2 devolve jsonb já parseado; tolera string por robustez."""
    return json.loads(v) if isinstance(v, str) else v


conn = psycopg2.connect(DSN)
conn.autocommit = False
cur = conn.cursor()


def envelope(porta, s, e, lenses=None):
    """Devolve (dict_por_coluna, n_linhas). porta ∈ {'publico','curatorial'}."""
    fn = "core.f_momento_publico" if porta == "publico" else "core.f_momento_curatorial"
    cur.execute("SELECT * FROM %s(%%s,%%s,%%s)" % fn, (s, e, lenses))
    cols = [d[0] for d in cur.description]
    linhas = cur.fetchall()
    if not linhas:
        return {c: None for c in cols}, 0
    return dict(zip(cols, linhas[0])), len(linhas)


def items_de(porta, s, e, lenses=None):
    env, _ = envelope(porta, s, e, lenses)
    return asjson(env["items"]) or []


# ---------------------------------------------------------------------------
# A3-T1 — estrutural: 1 linha, escalares + arrays JSONB esperados (forma β).
# Falha se virar SETOF (n_linhas != 1) ou faltar coluna.
# ---------------------------------------------------------------------------
env, n = envelope("publico", -66.05e6, -65.95e6)
faltando = [c for c in COLUNAS_ENVELOPE if c not in env]
arrays_ok = all(isinstance(asjson(env[c]), list)
                for c in ["items", "states", "claim_sets", "uncertainty_profiles",
                          "anachronism_warnings", "equivalence_warnings", "navigation_suggestions"])
reg("A3-T1", "função devolve 1 linha: escalares tipados + arrays JSONB esperados",
    n == 1 and not faltando and arrays_ok,
    "linhas=%d (esperado 1); colunas faltando=%s; arrays_ok=%s." % (n, faltando, arrays_ok))

# ---------------------------------------------------------------------------
# A3-T2 — público nunca devolve não-fato (em toda janela).
# ---------------------------------------------------------------------------
viola_total = 0
n_itens_pub = 0
for nome, (s, e) in JANELAS.items():
    its = items_de("publico", s, e)
    n_itens_pub += len(its)
    viola_total += sum(1 for it in its
                       if it.get("isFact") is not True
                       or it.get("selo") != "público"
                       or it.get("reviewStatus") != "approved")
reg("A3-T2", "público: todo item isFact=true, selo='público', approved; nada pending/legal/rejected/seeded",
    viola_total == 0,
    "%d itens públicos somados nas janelas; violações (não-fato vazado): %d." % (n_itens_pub, viola_total))

# ---------------------------------------------------------------------------
# A3-T3 — cada item carrega as chaves §8 não-nulas (ambas as portas).
# ---------------------------------------------------------------------------
def faltas_8(its):
    f = []
    for it in its:
        for k in CHAVES_8:
            if k not in it or it[k] is None:
                f.append("%s.%s" % (it.get("itemId", "?"), k))
        # attributionRef.provenanceRef presente e não-nulo
        ar = it.get("attributionRef") or {}
        if not ar.get("provenanceRef"):
            f.append("%s.attributionRef.provenanceRef" % it.get("itemId", "?"))
    return f

f_pub = faltas_8(items_de("publico", -66.05e6, -65.95e6))
f_cur = faltas_8(items_de("curatorial", -66.05e6, -65.95e6))
reg("A3-T3", "cada item tem todas as chaves §8 não-nulas (pública e curatorial)",
    not f_pub and not f_cur,
    "faltas pública=%s; faltas curatorial=%s." % (f_pub or "nenhuma", f_cur or "nenhuma"))

# ---------------------------------------------------------------------------
# A3-T4 — uncertaintyDisplayPolicy em enum válido; nunca 'omitir' (ambas).
# ---------------------------------------------------------------------------
ruins = []
for porta in ("publico", "curatorial"):
    for nome, (s, e) in JANELAS.items():
        for it in items_de(porta, s, e):
            pol = it.get("uncertaintyDisplayPolicy")
            if pol not in POLITICAS_VALIDAS:
                ruins.append("%s:%s=%r" % (porta, it.get("itemId"), pol))
reg("A3-T4", "uncertaintyDisplayPolicy sempre em enum válido (nunca 'omitir')",
    not ruins, "fora do enum: %s." % (ruins or "nenhum"))

# ---------------------------------------------------------------------------
# A3-T5 — [N1]: todo item tem attributionRef.provenanceRef (ambas as portas).
# ---------------------------------------------------------------------------
sem_prov = []
for porta in ("publico", "curatorial"):
    for nome, (s, e) in JANELAS.items():
        for it in items_de(porta, s, e):
            if not (it.get("attributionRef") or {}).get("provenanceRef"):
                sem_prov.append("%s:%s" % (porta, it.get("itemId")))
reg("A3-T5", "[N1] todo item afirmativo tem attributionRef.provenanceRef",
    not sem_prov, "itens sem proveniência: %s." % (sem_prov or "nenhum"))

# ---------------------------------------------------------------------------
# A3-T6 — curatorial em tempo profundo: item paleo com reconstructionFlag=true e
# epistemicType ∉ {fato-documentado, medição-direta}. (paleomapa nunca fato.)
# ---------------------------------------------------------------------------
its_cur_kpg = items_de("curatorial", -66.05e6, -65.95e6)
recon = [it for it in its_cur_kpg if it.get("reconstructionFlag") is True]
recon_como_fato = [it["itemId"] for it in recon
                   if it.get("epistemicType") in ("fato-documentado", "medição-direta")]
reg("A3-T6", "tempo profundo: item reconstruído presente; nenhum como fato-documentado/medição-direta",
    len(recon) >= 1 and not recon_como_fato,
    "itens reconstrução=%d; reconstrução-como-fato=%s." % (len(recon), recon_como_fato or "nenhum"))

# ---------------------------------------------------------------------------
# A3-T7 — curatorial: selo×isFact coerentes. seeded→'demonstração'/isFact=false;
# pending→'em-revisão'/isFact=false; corpus+approved→'fato'/isFact=true.
# Usa 1789 (tem seeded approved + pending + corpus approved simultâneos).
# ---------------------------------------------------------------------------
its_cur_1789 = items_de("curatorial", -212.0, -210.0)
incoerentes = []
for it in its_cur_1789:
    selo, fato = it.get("selo"), it.get("isFact")
    ok = ((selo == "fato" and fato is True)
          or (selo in ("demonstração", "em-revisão") and fato is False))
    if not ok:
        incoerentes.append("%s(selo=%s,isFact=%s)" % (it.get("itemId"), selo, fato))
tem_demo = any(it.get("selo") == "demonstração" and it.get("isFact") is False for it in its_cur_1789)
reg("A3-T7", "curatorial: seeded='demonstração'/¬fato; pending='em-revisão'/¬fato; corpus-approved='fato'",
    not incoerentes and tem_demo,
    "incoerências=%s; há 'demonstração' (seeded) is_fact=false: %s." % (incoerentes or "nenhuma", tem_demo))

# ---------------------------------------------------------------------------
# A3-T8 — gating por HOST na pública: todo claimSet exibido tem host em items[];
# e um ClaimSet de host NÃO-público (rev-francesa em 1789) NÃO vaza.
# (Carga real: só kpg-causa tem host público — ver nota de descoberta.)
# ---------------------------------------------------------------------------
its_pub_kpg = items_de("publico", -66.05e6, -65.95e6)
ids_pub_kpg = {it["itemId"] for it in its_pub_kpg}
env_kpg, _ = envelope("publico", -66.05e6, -65.95e6)
cs_pub_kpg = asjson(env_kpg["claim_sets"])
host_fora = [c["claimSetId"] for c in cs_pub_kpg if c.get("host") not in ids_pub_kpg]

env_1789, _ = envelope("publico", -212.0, -210.0)
cs_pub_1789 = asjson(env_1789["claim_sets"])
ids_pub_1789 = {it["itemId"] for it in items_de("publico", -212.0, -210.0)}
revfrancesa_vazou = "evt:estados-gerais-1789" in ids_pub_1789 or any(
    c.get("claimSetId") == "cset:rev-francesa" for c in cs_pub_1789)

reg("A3-T8", "pública: todo claimSet tem host em items[]; claimSet de host não-público não vaza (1789)",
    len(cs_pub_kpg) >= 1 and not host_fora and not revfrancesa_vazou and len(cs_pub_1789) == 0,
    "K-Pg claimSets=%d, hosts fora de items=%s; 1789 claimSets=%d, rev-francesa vazou=%s." % (
        len(cs_pub_kpg), host_fora or "nenhum", len(cs_pub_1789), revfrancesa_vazou))

# ---------------------------------------------------------------------------
# A3-T9 — ClaimSet: pesos assimétricos + fronteira escrita à mão presente;
# sem falsa equivalência (pesos não achatados/simétricos).
# ---------------------------------------------------------------------------
problemas = []
checados = 0
for porta in ("publico", "curatorial"):
    for nome, (s, e) in JANELAS.items():
        env_x, _ = envelope(porta, s, e)
        for c in asjson(env_x["claim_sets"]):
            checados += 1
            pesos = [m.get("weight") for m in c.get("members", []) if m.get("weight") is not None]
            if len(pesos) < 2 or max(pesos) == min(pesos):
                problemas.append("%s:pesos-simétricos/insuficientes" % c.get("claimSetId"))
            if not (c.get("resolutionBoundary") or "").strip():
                problemas.append("%s:sem-fronteira" % c.get("claimSetId"))
reg("A3-T9", "ClaimSet: pesos assimétricos + fronteira (resolution) presente; sem falsa equivalência",
    checados >= 1 and not problemas,
    "claimSets checados=%d; problemas=%s." % (checados, problemas or "nenhum"))

# ---------------------------------------------------------------------------
# A3-T10 — items(pública) ⊆ items(curatorial) (mesma janela); lente sem match →
# array vazio, sem exceção.
# ---------------------------------------------------------------------------
ids_pub = {it["itemId"] for it in items_de("publico", -66.05e6, -65.95e6)}
ids_cur = {it["itemId"] for it in items_de("curatorial", -66.05e6, -65.95e6)}
subconjunto = ids_pub.issubset(ids_cur)
try:
    vazio = items_de("publico", -2.4e9, -2.4e9, ["historia"])  # não há história no GOE
    vazio_ok = (vazio == [])
    err = None
except psycopg2.Error as ex:
    vazio_ok, err = False, str(ex)
reg("A3-T10", "items(pública) ⊆ items(curatorial); lente sem match → array vazio (não erro)",
    subconjunto and vazio_ok,
    "pública=%d ⊆ curatorial=%d: %s; lente-vazia ok: %s%s." % (
        len(ids_pub), len(ids_cur), subconjunto, vazio_ok,
        "" if not err else " (erro: %s)" % err))

# ---------------------------------------------------------------------------
# Encerramento
# ---------------------------------------------------------------------------
conn.rollback()
cur.close()
conn.close()

passaram = sum(1 for t in testes if t["passou"])
report = {
    "total": len(testes),
    "passaram": passaram,
    "falharam": len(testes) - passaram,
    "janelas_canonicas": {k: list(v) for k, v in JANELAS.items()},
    "testes": testes,
}
os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "test_a3_report.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(json.dumps(report, ensure_ascii=False, indent=2))
if report["falharam"] != 0:
    sys.exit(1)
