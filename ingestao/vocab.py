# -*- coding: utf-8 -*-
"""
Vocabulários FECHADOS do laço de ingestão — espelham 1:1 o DDL provado
(db/ddl/001-esquema-reificado.sql). Fonte única aqui para o validador (§4.1).

NÃO alterar estes conjuntos para "abrir" um rascunho: se o DDL não aceita, o
rascunho não pode existir. Mudança de vocabulário é mudança de esquema — fora
do escopo deste laço (spec §0 não-objetivos). Se o DDL mudar, este arquivo
diverge e a suíte do laço (test_laco) acusa.
"""
import re

# knowledge_item.item_type — 6 valores (DDL linha 79)
ITEM_TYPES = frozenset({"Event", "Process", "Concept", "State", "Species", "Entity"})

# claim.claim_type — taxonomia de 10 (DDL linha 113)
CLAIM_TYPES = frozenset({
    "fato-documentado", "inferência-científica", "proxy", "reconstrução-modelada",
    "estimativa", "hipótese", "interpretação", "medição-direta",
    "representação-artística", "aproximação-didática",
})

# claim.confidence — 5 valores (DDL linha 116)
CONFIDENCES = frozenset({"alta", "média-alta", "média", "média-baixa", "baixa"})

# source.authority_tier — A|B|C (DDL linha 50); NULL só existe para demonstração,
# que este laço NUNCA cria (§3.4). Todo pacote deve propor A/B/C.
AUTHORITY_TIERS = frozenset({"A", "B", "C"})

# source_time_basis — conjunto fechado v0 (DDL comentário linha 87).
TIME_BASES = frozenset({"gregorianCE", "Ma", "Ga", "scenarioYear"})

# tag de sensibilidade PG5 proposta (spec §1.1)
PG5_VALUES = frozenset({"público", "mediado", "legal-review"})

# tier proposto/confirmado
TIERS = frozenset({"T0", "T1"})

# precisões que dispensam incerteza (§4.4 "nunca número seco quando há incerteza"):
# só a precisão exata de data documentada não exige perfil de incerteza.
PRECISOES_EXATAS = frozenset({"data exata", "exata"})

# Campos que a IA estruturalmente NÃO escreve (§3.1): não existem no formato de
# rascunho; se aparecerem em qualquer nível, a validação REPROVA (§4.2, teste
# negativo §10.4). São gravados só na promoção humana (§7).
CAMPOS_PROIBIDOS = frozenset({
    "review_status", "provenance_status", "per_asset_source_confirmed",
})

# padrão de id (§4.6) — igual ao usado no corpus
ID_PADRAO = re.compile(r"^[a-z]+:[a-z0-9\-]+$")
