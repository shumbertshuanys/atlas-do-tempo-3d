#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suíte do laço de ingestão (PG1 — artefatos falsificáveis). Padrão de verify.py:
script plano, sem pytest; imprime relatório e sai != 0 em falha. Gera
ingestao/reports/test_laco_report.json.

Inclui os DOIS testes negativos obrigatórios (spec §10.4):
  · LACO-T2: rascunho com review_status presente REPROVA a validação;
  · LACO-T10: promover pacote NÃO-aprovado FALHA.
"""
import copy
import json
import os
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_AQUI, ".."))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import manifesto as M
import medicao
import promocao
import triagem
import validacao

resultados = []


def reg(tid, descr, passou, detalhe=""):
    resultados.append({"id": tid, "descricao": descr, "passou": bool(passou), "detalhe": detalhe})
    print(("[ok]  " if passou else "[FAIL]") + f" {tid}: {descr}" + (f" — {detalhe}" if detalhe else ""))


def pacote_valido_t1():
    return {
        "pacote_id": "pkg-teste-001",
        "item": {
            "id": "evt:teste-efemeride-1906", "item_type": "Event", "domain": "historia",
            "layer": "Ciência e técnica", "title": "Efeméride de teste",
            "canonical_start": -94.2, "canonical_end": -94.2, "canonical_scalar": -94.2,
            "source_time_basis": "gregorianCE", "display_time": "1906",
            "time_precision": "dia", "time_uncertainty": "data exata",
            "is_global": False, "anachronism_note": None,
            "geo": {"lat": 48.86, "lng": 2.25, "place": "Paris",
                    "is_paleo": False, "is_reconstruction": False, "modern_correspondence": None},
        },
        "claims": [{"local_id": "c1", "statement": "Statement sustentado pela fonte.",
                    "claim_type": "fato-documentado", "confidence": "alta",
                    "evidence_level": "documental", "uncertainty_profile": "data exata",
                    "bindings": [{"source_local_id": "s1", "locator": "p. 123"}]}],
        "sources": [{"local_id": "s1", "title": "Fonte autoritativa A", "authority_tier": "A",
                     "license": "domínio público", "uri": "https://exemplo.org", "is_aggregator": False}],
        "relations": [], "claim_set": None, "pg5": "público", "tier_proposto": "T1",
        "pessoa_viva_citada": False, "contem_dado_menor": False,
    }


# --------------------------------------------------------------------------
# LACO-T1 — pacote válido T1 passa a validação.
# --------------------------------------------------------------------------
ok, falhas = validacao.validate_pacote(pacote_valido_t1(), corpus_ids=set(), open_ids=set())
reg("LACO-T1", "pacote T1 bem-formado passa a validação", ok, "falhas=%s" % falhas)

# --------------------------------------------------------------------------
# LACO-T2 (NEGATIVO §10.4) — review_status no rascunho REPROVA a validação.
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["item"]["review_status"] = "approved"
ok, falhas = validacao.validate_pacote(p, set(), set())
tem_proibido = any("campo-proibido" in x and "review_status" in x for x in falhas)
reg("LACO-T2", "NEGATIVO: rascunho com review_status reprova validação (§3.1/§10.4)",
    (not ok) and tem_proibido, "ok=%s; falhas=%s" % (ok, falhas))

# provenance_status e per_asset_source_confirmed também são proibidos:
for campo in ("provenance_status", "per_asset_source_confirmed"):
    q = pacote_valido_t1(); q["claims"][0][campo] = True
    ok2, f2 = validacao.validate_pacote(q, set(), set())
    reg("LACO-T2." + campo, "NEGATIVO: %s no rascunho reprova validação" % campo,
        (not ok2) and any("campo-proibido" in x and campo in x for x in f2), "falhas=%s" % f2)

# --------------------------------------------------------------------------
# LACO-T3 — [N1]: claim sem localizador reprova.
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["claims"][0]["bindings"][0]["locator"] = "   "
ok, falhas = validacao.validate_pacote(p, set(), set())
reg("LACO-T3", "[N1]: binding com localizador vazio reprova (§4.3)",
    (not ok) and any("localizador VAZIO" in x for x in falhas), "falhas=%s" % falhas)

# --------------------------------------------------------------------------
# LACO-T4 — eixo 3Z: start > end reprova; scalar fora do intervalo reprova.
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["item"]["canonical_start"] = 5.0; p["item"]["canonical_end"] = -5.0
ok, falhas = validacao.validate_pacote(p, set(), set())
c1 = (not ok) and any("canonical_start" in x and ">" in x for x in falhas)
p = pacote_valido_t1(); p["item"]["canonical_scalar"] = 999.0
ok2, f2 = validacao.validate_pacote(p, set(), set())
c2 = (not ok2) and any("fora de" in x for x in f2)
reg("LACO-T4", "3Z: start>end e scalar fora do intervalo reprovam (§4.4)", c1 and c2)

# --------------------------------------------------------------------------
# LACO-T5 — geo: paleo sem reconstrução reprova (espelha CHECK do banco).
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["item"]["geo"]["is_paleo"] = True; p["item"]["geo"]["is_reconstruction"] = False
ok, falhas = validacao.validate_pacote(p, set(), set())
reg("LACO-T5", "geo: paleo ⇒ reconstrução (§4.5)",
    (not ok) and any("paleo" in x.lower() and "reconstru" in x.lower() for x in falhas), "falhas=%s" % falhas)

# --------------------------------------------------------------------------
# LACO-T6 — colisão de id com o corpus reprova; padrão inválido reprova.
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["item"]["id"] = "evt:ja-existe"
ok, falhas = validacao.validate_pacote(p, corpus_ids={"evt:ja-existe"}, open_ids=set())
c1 = (not ok) and any("colide com id já existente" in x for x in falhas)
p = pacote_valido_t1(); p["item"]["id"] = "ID_Invalido"
ok2, f2 = validacao.validate_pacote(p, set(), set())
c2 = (not ok2) and any("fora do padrão" in x for x in f2)
reg("LACO-T6", "id: colisão com corpus e padrão inválido reprovam (§4.6)", c1 and c2)

# --------------------------------------------------------------------------
# LACO-T7 — número seco e agregador (Art.5).
# --------------------------------------------------------------------------
p = pacote_valido_t1(); p["item"]["time_precision"] = "século"; p["item"]["time_uncertainty"] = ""
ok, falhas = validacao.validate_pacote(p, set(), set())
c1 = (not ok) and any("número seco" in x for x in falhas)
p = pacote_valido_t1(); p["sources"][0]["is_aggregator"] = True
ok2, f2 = validacao.validate_pacote(p, set(), set())
c2 = (not ok2) and any("agregador" in x for x in f2)
reg("LACO-T7", "3Z número-seco reprova; agregador como fonte reprova (§4.4/Art.5)", c1 and c2)

# --------------------------------------------------------------------------
# LACO-T8 — triagem: elegível T1; PG5≠público→T0; claim_type fraco→T0.
# --------------------------------------------------------------------------
tier, motivos = triagem.triar(pacote_valido_t1())
c1 = tier == "T1" and motivos == []
p = pacote_valido_t1(); p["pg5"] = "mediado"
c2 = triagem.triar(p)[0] == "T0"
p = pacote_valido_t1(); p["claims"][0]["claim_type"] = "interpretação"
c3 = triagem.triar(p)[0] == "T0"
p = pacote_valido_t1(); p["sources"][0]["authority_tier"] = "B"
c4 = triagem.triar(p)[0] == "T0"
reg("LACO-T8", "triagem conservadora: T1 só quando TODAS; senão T0 (§5)", c1 and c2 and c3 and c4,
    "T1=%s motivos=%s" % (tier, motivos))

# --------------------------------------------------------------------------
# LACO-T9 — ClaimSet: resolution não-vazia reprova; ClaimSet ⇒ tier T0.
# --------------------------------------------------------------------------
p = pacote_valido_t1()
p["claim_set"] = {"tema": "debate", "resolution": "já preenchida (indevido)",
                  "members": [{"statement": "leitura A", "weight": 0.7, "stance": "a"},
                              {"statement": "leitura B", "weight": 0.3, "stance": "b"}]}
ok, falhas = validacao.validate_pacote(p, set(), set())  # tier_proposto ainda T1 → deve reprovar em 2 frentes
c1 = (not ok) and any("resolution deve ser VAZIA" in x for x in falhas)
c2 = any("ClaimSet proposto exige tier T0" in x for x in falhas)
c3 = triagem.triar(p)[0] == "T0"
reg("LACO-T9", "ClaimSet: resolution vazia no rascunho + tier T0 obrigatório (§3.2/§5)",
    c1 and c2 and c3, "falhas=%s" % falhas)

# --------------------------------------------------------------------------
# LACO-T10 (NEGATIVO §10.4) — promover não-aprovado FALHA; aprovado promove;
#            PG5 sensível T0 → 'pending' (decisão do dono, D-20260708).
# --------------------------------------------------------------------------
import tempfile
tmp = tempfile.mkdtemp(prefix="laco-test-")
manifesto_tmp = os.path.join(tmp, "manifest.jsonl")
carga_tmp = os.path.join(tmp, "carga.jsonl")

pkg = pacote_valido_t1()
# 10a — sem nenhum desfecho: promoção recusada
recusou = False
try:
    promocao.promover(pkg, "T1", "dono", eventos=[], carga=carga_tmp, manifesto_caminho=manifesto_tmp)
except promocao.PromocaoRecusada:
    recusou = True
# 10b — desfecho 'devolvido': promoção recusada
evs_dev = [{"evento": "pacote_decidido", "t": M.agora_iso(), "pacote": pkg["pacote_id"], "desfecho": "devolvido"}]
recusou_dev = False
try:
    promocao.promover(pkg, "T1", "dono", eventos=evs_dev, carga=carga_tmp, manifesto_caminho=manifesto_tmp)
except promocao.PromocaoRecusada:
    recusou_dev = True
# 10c — desfecho 'aprovado': promove e grava review_status=approved (T1)
evs_ap = [{"evento": "pacote_decidido", "t": M.agora_iso(), "pacote": pkg["pacote_id"], "desfecho": "aprovado"}]
reg_ap = promocao.promover(pkg, "T1", "dono", eventos=evs_ap, carga=carga_tmp, manifesto_caminho=manifesto_tmp)
c_ap = (reg_ap["review_status"] == "approved" and reg_ap["provenance_status"] == "corpus"
        and os.path.exists(carga_tmp))
# 10d — T0 sensível (mediado) aprovado → 'pending'
pkg2 = pacote_valido_t1(); pkg2["pacote_id"] = "pkg-teste-sens"; pkg2["pg5"] = "mediado"; pkg2["item"]["id"] = "evt:sensivel"
evs_ap2 = [{"evento": "pacote_decidido", "t": M.agora_iso(), "pacote": pkg2["pacote_id"], "desfecho": "aprovado"}]
reg_pend = promocao.promover(pkg2, "T0", "dono", eventos=evs_ap2, carga=carga_tmp, manifesto_caminho=manifesto_tmp)
c_pend = reg_pend["review_status"] == "pending" and reg_pend["per_asset_source_confirmed"] is False
reg("LACO-T10", "NEGATIVO: promover não-aprovado FALHA; aprovado promove; sensível→pending (§7/§10.4)",
    recusou and recusou_dev and c_ap and c_pend,
    "recusa_sem=%s recusa_dev=%s approved=%s pending=%s" % (recusou, recusou_dev, c_ap, c_pend))

# --------------------------------------------------------------------------
# LACO-T11 — cronometria: intervalos, pausa subtraída, incompleta descartada.
# --------------------------------------------------------------------------
def ev(evento, t, **kw):
    d = {"evento": evento, "t": "2026-07-08T12:%02d:%02d+00:00" % (t // 60, t % 60)}
    d.update(kw); return d

eventos = [
    ev("pacote_aberto", 0, pacote="A", papel="cientifica", ator="dono", tier="T0"),
    ev("pausa_inicio", 60, pacote="A", papel="cientifica"),
    ev("pausa_fim", 120, pacote="A", papel="cientifica"),          # 60s de pausa
    ev("pacote_decidido", 300, pacote="A", papel="cientifica", desfecho="aprovado"),  # 300-0-60=240s
    ev("pacote_aberto", 400, pacote="B", papel="cientifica", ator="dono", tier="T0"),  # sem decisão → descartada
]
amostras = M.amostras_de_revisao(eventos)
completa = [a for a in amostras if a["completa"]]
incompleta = [a for a in amostras if not a["completa"]]
c1 = len(completa) == 1 and abs(completa[0]["segundos"] - 240.0) < 0.01
c2 = len(incompleta) == 1 and incompleta[0]["pacote"] == "B"
reg("LACO-T11", "cronometria: decidido−aberto−pausas; aberto-sem-decisão descartado (§1.5)",
    c1 and c2, "segundos=%s incompletas=%d" % (completa[0]["segundos"] if completa else None, len(incompleta)))

# --------------------------------------------------------------------------
# LACO-T12 — medição: report deriva minutos/item por tier a partir do log.
# --------------------------------------------------------------------------
eventos_m = [
    ev("pacote_gerado", 0, pacote="A", n_claims=2),
    ev("triagem_confirmada", 1, pacote="A", tier="T0"),
    ev("pacote_aberto", 10, pacote="A", papel="cientifica", tier="T0"),
    ev("pacote_decidido", 130, pacote="A", papel="cientifica", tier="T0", desfecho="aprovado"),  # 120s=2min
]
rep = medicao.gerar_report(eventos_m)
c1 = rep["tier_0"]["n_itens_aprovados"] == 1
c2 = abs(rep["tier_0"]["min_por_item_media"] - 2.0) < 0.01
c3 = abs(rep["tier_0"]["itens_por_hora"] - 30.0) < 0.01  # 60/2
reg("LACO-T12", "medição: minutos/item e itens/hora por tier (§1.6/§8)",
    c1 and c2 and c3, "t0=%s" % rep["tier_0"])

# --------------------------------------------------------------------------
# Encerramento
# --------------------------------------------------------------------------
passaram = sum(1 for r in resultados if r["passou"])
report = {"total": len(resultados), "passaram": passaram,
          "falharam": len(resultados) - passaram, "testes": resultados}
out_dir = os.path.join(_AQUI, "..", "reports")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "test_laco_report.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print("\n%d/%d testes passaram." % (passaram, len(resultados)))
if report["falharam"]:
    sys.exit(1)
