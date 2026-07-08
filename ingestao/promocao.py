# -*- coding: utf-8 -*-
"""
Promoção ao corpus — git primeiro; banco derivado (spec §7, R1).

Só pacote `aprovado` promove, por comando humano com identidade registrada.
A promoção MATERIALIZA NO REPOSITÓRIO um registro de carga (linha em
ingestao/carga-promovida.jsonl) que o caminho de migração consome ao lado de
ITENS — de modo que `down -v` + bootstrap reproduz o corpus com os promovidos.
Promover só no banco vivo é proibido (R1).

review_status gravado (§7 + decisão de abertura do dono, D-20260708):
  - 'approved'  quando todos os papéis competentes aprovaram:
       Tier 1, ou Tier 0 com PG5 = 'público'.
  - 'pending'   Tier 0 com PG5 ∈ {'mediado','legal-review'} ENQUANTO não houver
       papel competente designado (designação = entrada no DECISOES.md). Entram
       gateados e juntam-se à fila viva (docs/fila-revisao-claimsets-sensiveis.md).
       Art.6 garante: 'pending' não existe como fato para o público.

provenance_status é SEMPRE 'corpus' (§3.4): este laço NÃO cria seeded-demo.

A IA NUNCA passa por aqui: promover é ato humano. E promover pacote
não-`aprovado` FALHA (teste negativo obrigatório §10.4).
"""
import json
import os

import manifesto as M

_AQUI = os.path.dirname(os.path.abspath(__file__))
CARGA_PROMOVIDA = os.path.join(_AQUI, "carga-promovida.jsonl")


class PromocaoRecusada(Exception):
    """Levantada quando se tenta promover um pacote que não está `aprovado`."""


def desfecho_atual(pacote, eventos):
    """Último desfecho registrado para o pacote no manifesto (ou None)."""
    d = None
    for ev in eventos:
        if ev["evento"] == "pacote_decidido" and ev.get("pacote") == pacote:
            d = ev.get("desfecho")
    return d


def review_status_para(pkg, tier_confirmado):
    """Mapa §7 de PG5×tier → review_status na promoção."""
    pg5 = pkg.get("pg5")
    if tier_confirmado == "T1":
        return "approved"
    # Tier 0:
    if pg5 == "público":
        return "approved"
    # PG5 ∈ {mediado, legal-review}: sem papel competente designado ⇒ pending
    return "pending"


def montar_registro(pkg, tier_confirmado, ator):
    """Constrói o registro de carga materializado (não escreve nada)."""
    rev = review_status_para(pkg, tier_confirmado)
    return {
        "pacote_id": pkg.get("pacote_id"),
        "promotor": ator,
        "tier": tier_confirmado,
        "review_status": rev,                 # ATO HUMANO — nasce aqui, não no rascunho
        "provenance_status": "corpus",        # §3.4: nunca seeded-demo
        "per_asset_source_confirmed": (rev == "approved"),
        "pg5": pkg.get("pg5"),
        "item": pkg["item"],
        "claims": pkg["claims"],
        "sources": pkg["sources"],
        "relations": pkg.get("relations") or [],
        "claim_set": pkg.get("claim_set"),
    }


def promover(pkg, tier_confirmado, ator, eventos=None,
             carga=None, manifesto_caminho=None, commit_hash=None):
    """Promove um pacote APROVADO. Recusa qualquer outro desfecho.

    Retorna o registro materializado. Efeitos: acrescenta a linha em `carga`
    e registra o evento 'promovido' no manifesto.
    """
    carga = carga or CARGA_PROMOVIDA
    eventos = eventos if eventos is not None else M.ler(manifesto_caminho)
    pacote_id = pkg.get("pacote_id")

    d = desfecho_atual(pacote_id, eventos)
    if d != "aprovado":
        raise PromocaoRecusada(
            f"promoção recusada: pacote {pacote_id!r} está {d!r}, não 'aprovado' "
            f"(§7 — só pacote aprovado promove; teste negativo §10.4)")

    reg = montar_registro(pkg, tier_confirmado, ator)
    os.makedirs(os.path.dirname(carga), exist_ok=True)
    with open(carga, "a", encoding="utf-8") as fp:
        fp.write(json.dumps(reg, ensure_ascii=False) + "\n")

    M.registrar("promovido", caminho=manifesto_caminho, pacote=pacote_id,
                ator=ator, tier=tier_confirmado, review_status=reg["review_status"],
                commit_hash=commit_hash)
    return reg
