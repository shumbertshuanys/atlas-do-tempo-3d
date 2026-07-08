# -*- coding: utf-8 -*-
"""
Ids já existentes no corpus — para o check de colisão de id (§4.6): "inexistente
no corpus (ITENS/carga promovida) e nos pacotes abertos".

Sem tocar o banco (o laço opera antes/à margem do core): a verdade dos ids do
corpus é o REPO (R1). Extraímos:
  - ids de item da carga-base (db/migration/migrate.py, lista ITENS) por regex
    sobre o arquivo — fica em sincronia com o arquivo real, sem importar migrate
    (que exige env/psycopg2);
  - ids de item já promovidos por este laço (ingestao/carga-promovida.jsonl).

Escopo v0: checamos colisão de IDS DE ITEM (o que os pacotes geram). Ids
derivados (claim:/prov:/src:/geom:/rel:/cset:) nascem da promoção e não colidem
com propostas de item.
"""
import json
import os
import re

_AQUI = os.path.dirname(os.path.abspath(__file__))
_MIGRATE = os.path.join(_AQUI, "..", "db", "migration", "migrate.py")
CARGA_PROMOVIDA = os.path.join(_AQUI, "carga-promovida.jsonl")

# casa id="..." dentro dos dicts de ITENS em migrate.py
_ID_EM_MIGRATE = re.compile(r'\bid\s*=\s*"([a-z]+:[a-z0-9\-]+)"')


def ids_base():
    """Ids de item da carga-base (migrate.py ITENS)."""
    if not os.path.exists(_MIGRATE):
        return set()
    with open(_MIGRATE, encoding="utf-8") as f:
        txt = f.read()
    # a lista ITENS vai do 'ITENS = [' até o fechamento antes de 'CLAIMSETS'.
    ini = txt.find("ITENS = [")
    fim = txt.find("CLAIMSETS", ini) if ini >= 0 else -1
    trecho = txt[ini:fim] if ini >= 0 and fim > ini else txt
    return set(_ID_EM_MIGRATE.findall(trecho))


def ids_promovidos():
    """Ids de item já materializados por este laço."""
    ids = set()
    if not os.path.exists(CARGA_PROMOVIDA):
        return ids
    with open(CARGA_PROMOVIDA, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            reg = json.loads(linha)
            item = reg.get("item", {})
            if item.get("id"):
                ids.add(item["id"])
    return ids


def ids_corpus():
    """União dos ids já existentes no corpus (base + promovidos)."""
    return ids_base() | ids_promovidos()
