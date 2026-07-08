# -*- coding: utf-8 -*-
"""
Medição — o artefato do Chat 5 (PG1). Deriva do manifesto (§1.6, §8) o
número-decisor: MINUTOS HUMANOS POR ITEM APROVADO, por tier (média e mediana,
com n). itens/hora = 60 ÷ média (derivado); claims/hora (normalização por
tamanho); taxa de devolução; defeitos críticos por categoria; custo de máquina
(informativo, NÃO entra no número humano).

Anti-Goodhart (Art.13): este número existe para decidir a economia do produto
e melhorar o rascunho da IA — NUNCA é meta de produtividade do revisor, nunca
se encurta o checklist para elevá-lo.

Custo por tier (§1.5):
  Tier 0 por item aprovado = Σ tempos de TODOS os papéis, TODAS as passadas até
    `aprovado` (retrabalho conta).
  Tier 1 por item aprovado = (Σ tempos dos pacotes amostrados + tempo de
    montagem/decisão do lote) ÷ itens aprovados do lote.
"""
import statistics

import manifesto as M


def _media(xs):
    return round(statistics.mean(xs), 2) if xs else None


def _mediana(xs):
    return round(statistics.median(xs), 2) if xs else None


def _n_claims_por_pacote(eventos):
    """n_claims declarado no evento pacote_gerado, por pacote (§1.1)."""
    out = {}
    for ev in eventos:
        if ev["evento"] == "pacote_gerado" and ev.get("pacote"):
            out[ev["pacote"]] = ev.get("n_claims", 0)
    return out


def _desfecho_final(eventos):
    """Último desfecho registrado por pacote (aprovado/devolvido/rejeitado)."""
    out = {}
    for ev in eventos:
        if ev["evento"] == "pacote_decidido" and ev.get("desfecho"):
            out[ev["pacote"]] = ev["desfecho"]
    return out


def _lotes(eventos):
    """Mapa lote_id -> {ids, semente, amostra, decidido, segundos_overhead}."""
    lotes = {}
    montados = {}
    for ev in eventos:
        if ev["evento"] == "lote_montado":
            lid = ev.get("lote")
            lotes[lid] = {"ids": ev.get("ids", []), "semente": ev.get("semente"),
                          "amostra": ev.get("amostra", []), "decidido": None,
                          "segundos_overhead": 0.0}
            montados[lid] = M._t(ev)
        elif ev["evento"] == "lote_decidido":
            lid = ev.get("lote")
            if lid in lotes:
                lotes[lid]["decidido"] = ev.get("desfecho")
    return lotes


def gerar_report(eventos=None):
    """Constrói o dict do report de medição a partir do manifesto."""
    eventos = eventos if eventos is not None else M.ler()
    amostras = M.amostras_de_revisao(eventos)
    completas = [a for a in amostras if a["completa"]]
    descartadas = len(amostras) - len(completas)
    nclaims = _n_claims_por_pacote(eventos)
    desfecho = _desfecho_final(eventos)

    # tempo humano total por pacote (Σ passadas, todos os papéis) — segundos
    seg_por_pacote = {}
    for a in completas:
        seg_por_pacote.setdefault(a["pacote"], 0.0)
        seg_por_pacote[a["pacote"]] += a["segundos"]

    # ---- Tier 0: custo por item aprovado = Σ tempos até aprovado (por pacote)
    t0_aprovados = [p for p, d in desfecho.items() if d == "aprovado"
                    and any(x["pacote"] == p and x["tier"] == "T0" for x in completas)]
    t0_min = [seg_por_pacote.get(p, 0.0) / 60.0 for p in t0_aprovados]
    t0_claims = sum(nclaims.get(p, 0) for p in t0_aprovados)
    t0_min_total = sum(t0_min)

    # ---- Tier 1: por lote — (Σ amostrados + overhead do lote) ÷ aprovados do lote
    lotes = _lotes(eventos)
    t1_por_item = []      # minutos/item aprovado, um valor por item aprovado do lote
    t1_claims_total = 0
    t1_min_total = 0.0
    t1_itens_aprovados = 0
    lotes_detalhe = []
    for lid, lo in lotes.items():
        amostrados = lo["amostra"] or []
        seg_amostra = sum(seg_por_pacote.get(p, 0.0) for p in amostrados)
        # itens aprovados do lote: se o lote foi 'aprovado', todos os ids contam;
        # se 'devolvido', 0 (o tempo acumula na coorte até a aprovação — §1.5).
        aprovados_lote = lo["ids"] if lo.get("decidido") == "aprovado" else []
        n_ap = len(aprovados_lote)
        min_lote = (seg_amostra + lo["segundos_overhead"]) / 60.0
        t1_min_total += min_lote
        if n_ap:
            por_item = min_lote / n_ap
            t1_por_item.extend([por_item] * n_ap)
            t1_itens_aprovados += n_ap
            t1_claims_total += sum(nclaims.get(p, 0) for p in aprovados_lote)
        lotes_detalhe.append({"lote": lid, "n_ids": len(lo["ids"]),
                              "n_amostrados": len(amostrados), "semente": lo["semente"],
                              "desfecho": lo.get("decidido"), "min_lote": round(min_lote, 2),
                              "itens_aprovados": n_ap})

    # ---- taxa de devolução (por tier), defeitos, custo de máquina
    devolvidos = [p for p, d in desfecho.items() if d == "devolvido"]
    total_decididos = len(desfecho)
    ms_maquina = sum(ev.get("ms_maquina", 0) for ev in eventos if ev["evento"] == "pacote_gerado")

    def bloco(minutos_por_item, claims_total, min_total, n_itens):
        return {
            "n_itens_aprovados": n_itens,
            "min_por_item_media": _media(minutos_por_item),
            "min_por_item_mediana": _mediana(minutos_por_item),
            "itens_por_hora": round(60.0 / _media(minutos_por_item), 2)
                              if minutos_por_item and _media(minutos_por_item) else None,
            "claims_por_hora": round(claims_total / (min_total / 60.0), 2)
                               if min_total > 0 else None,
        }

    return {
        "gerado_em": M.agora_iso(),
        "hash_manifesto": M.hash_manifesto(),
        "n_eventos": len(eventos),
        "amostras_completas": len(completas),
        "amostras_descartadas": descartadas,
        "numero_decisor": "minutos humanos por item aprovado, por tier",
        "anti_goodhart": ("o número decide a economia do produto e melhora o rascunho da IA; "
                          "nunca é meta de produtividade do revisor, nunca encurta o checklist (Art.13)"),
        "tier_0": bloco(t0_min, t0_claims, t0_min_total, len(t0_aprovados)),
        "tier_1": bloco(t1_por_item, t1_claims_total, t1_min_total, t1_itens_aprovados),
        "lotes": lotes_detalhe,
        "taxa_devolucao": {
            "devolvidos": len(devolvidos), "total_decididos": total_decididos,
            "taxa": round(len(devolvidos) / total_decididos, 3) if total_decididos else None,
        },
        "custo_maquina_ms_informativo": ms_maquina,
    }
