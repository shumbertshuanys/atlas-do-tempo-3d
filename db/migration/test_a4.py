#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A4 · Fatia 3 (artefato falsificável / PG1)
test_a4.py — prova que a CAMADA DE LEITURA GATEADA respeita Art.6/§9:
  * a consulta PÚBLICA nunca devolve pending / legal-review / rejected / seeded
    como fato — em nenhum instante, nem como intervalo;
  * teste DINÂMICO: um item legal-review e um seeded-demo, ambos temporalmente
    simultâneos ao instante consultado, NÃO vazam ao público (o legal-review
    some inclusive da curatorial; o seeded aparece à curadoria apenas com selo
    'demonstração', is_fact=false);
  * o portão §9.2 (fonte-por-asset) separa corpus-approved-publicável (11) de
    corpus-approved-com-fonte-pendente (gated out) — F2 operando;
  * semântica de interseção 3Z correta (tempo profundo não vaza para 1789);
  * lente sem correspondência devolve vazio (D-A3.5: o cliente exibe "nada
    conhecido por estas lentes" — é informação, não erro).

Instantes canônicos: 1789 = -211 (intervalo do ano [-212,-210]);
GOE ≈ -2,4e9; K-Pg ≈ -6,6e7.
"""
import json
import os
import sys
import psycopg2

# saída em UTF-8 mesmo em consoles legados (ex.: cp1252 no Windows) — o relatório
# contém '⊂'/'⟂'. Não muda o conteúdo, só o encoding do stdout.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DSN = "host=localhost dbname=atlas user=atlas password=%s" % os.environ["ATLAS_DB_PASSWORD"]

# diretório de saída relativo ao próprio script (db/migration -> raiz/out),
# independente do diretório de trabalho e do SO.
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "out")

INSTANTES = {
    "1789 (intervalo do ano)": (-212.0, -210.0),
    "GOE ~2,4 Ga": (-2.4e9, -2.4e9),
    "K-Pg ~66 Ma": (-6.6e7, -6.6e7),
    "todo o eixo": (-1e12, 1e12),
}

PROIBIDO_NO_PUBLICO = ("pending", "legal-review", "rejected")

testes = []


def reg(tid, descr, passou, detalhe):
    testes.append({"id": tid, "descricao": descr, "passou": bool(passou), "detalhe": detalhe})


conn = psycopg2.connect(DSN)
conn.autocommit = False
cur = conn.cursor()


def rows_publica(s, e, lenses=None):
    cur.execute(
        "SELECT id, provenance_status, review_status, selo, is_fact "
        "FROM core.f_simultaneidade_publica(%s,%s,%s)", (s, e, lenses))
    return cur.fetchall()


def rows_curatorial(s, e, lenses=None):
    cur.execute(
        "SELECT id, provenance_status, review_status, selo, is_fact "
        "FROM core.f_simultaneidade_curatorial(%s,%s,%s)", (s, e, lenses))
    return cur.fetchall()


# ---------------------------------------------------------------------------
# A4-T1..T4 — a consulta pública só devolve FATO PÚBLICO em cada instante.
# ---------------------------------------------------------------------------
for nome, (s, e) in INSTANTES.items():
    rs = rows_publica(s, e)
    viola = [r for r in rs
             if r[1] != "corpus" or r[2] != "approved"
             or r[3] != "público" or r[4] is not True]
    tid = "A4-T%d" % (len(testes) + 1)
    reg(tid, "público em [%s]: toda linha é corpus+approved+selo público+is_fact" % nome,
        len(viola) == 0,
        "%d linhas; violações (não-fato vazado): %d." % (len(rs), len(viola)))

# ---------------------------------------------------------------------------
# A4-T5 — total público no eixo inteiro = 27 (11 originais + 5 cósmicos, Frente A
# + 11 T1 do laço de ingestão, lote-medicao-01).
# ---------------------------------------------------------------------------
tot_pub = len(rows_publica(-1e12, 1e12))
reg("A4-T5", "total público no eixo inteiro é 27",
    tot_pub == 27, "obtido: %d." % tot_pub)

# ---------------------------------------------------------------------------
# A4-T6 — §9.2 (F2): público ⊂ curatorial-fato, e a diferença são exatamente
# os corpus-approved com fonte-por-asset NÃO confirmada (gated out do público).
# ---------------------------------------------------------------------------
pub_ids = {r[0] for r in rows_publica(-1e12, 1e12)}
cur.execute("SELECT id FROM core.f_simultaneidade_curatorial(-1e12,1e12) WHERE is_fact")
fato_ids = {r[0] for r in cur.fetchall()}
cur.execute("""SELECT id FROM core.knowledge_item
               WHERE review_status='approved' AND provenance_status='corpus'
                 AND per_asset_source_confirmed = false
                 AND ingestion_decision <> 'blocked'""")
corpus_approved_src_pendente = {r[0] for r in cur.fetchall()}
subconjunto = pub_ids.issubset(fato_ids)
diferenca_ok = (fato_ids - pub_ids) == corpus_approved_src_pendente
reg("A4-T6", "público ⊂ curatorial-fato; diferença = corpus-approved com fonte-por-asset pendente",
    subconjunto and diferenca_ok,
    "público=%d ⊂ fato=%d: %s; |fato\\público|=%d == src-pendente=%d: %s." % (
        len(pub_ids), len(fato_ids), subconjunto,
        len(fato_ids - pub_ids), len(corpus_approved_src_pendente), diferenca_ok))

# ---------------------------------------------------------------------------
# A4-T7 — DINÂMICO: legal-review simultâneo a 1789 NÃO vaza (nem público, nem
# curatorial), embora EXISTA na base (o portão filtra exibição, não dados).
# ---------------------------------------------------------------------------
cur.execute("SAVEPOINT leak")
try:
    cur.execute("INSERT INTO core.entity_node(uri,entity_kind) VALUES ('item:_leak_legal','item')")
    cur.execute("""
        INSERT INTO core.knowledge_item(
            id,item_type,domain,title,canonical_start,canonical_end,canonical_scalar,
            source_time_basis,display_time,review_status,provenance_status,
            per_asset_source_confirmed,ingestion_decision,is_global)
        VALUES ('item:_leak_legal','Event','historia','(teste) episódio sensível 1789',
            -211.0,-211.0,-211.0,'gregorianCE','1789','legal-review','corpus',
            true,'admitido',false)
    """)
    na_base = cur.execute("SELECT 1") or True
    cur.execute("SELECT count(*) FROM core.knowledge_item WHERE id='item:_leak_legal'")
    existe = cur.fetchone()[0]
    pub_leak = [r for r in rows_publica(-212.0, -210.0) if r[0] == 'item:_leak_legal']
    cur_leak = [r for r in rows_curatorial(-212.0, -210.0) if r[0] == 'item:_leak_legal']
    cur.execute("ROLLBACK TO SAVEPOINT leak")
    reg("A4-T7", "legal-review simultâneo existe na base mas não vaza (público e curatorial vazios)",
        existe == 1 and len(pub_leak) == 0 and len(cur_leak) == 0,
        "existe na base: %d; no público: %d; na curatorial: %d." % (existe, len(pub_leak), len(cur_leak)))
except psycopg2.Error as ex:
    cur.execute("ROLLBACK TO SAVEPOINT leak")
    reg("A4-T7", "legal-review simultâneo existe na base mas não vaza", False, "erro: %s" % ex)

# ---------------------------------------------------------------------------
# A4-T8 — DINÂMICO: seeded-demo APPROVED simultâneo ao GOE NÃO vaza ao público,
# mas aparece à curadoria como 'demonstração' (is_fact=false).
# ---------------------------------------------------------------------------
cur.execute("SAVEPOINT seed")
try:
    cur.execute("INSERT INTO core.entity_node(uri,entity_kind) VALUES ('item:_leak_seed','item')")
    cur.execute("""
        INSERT INTO core.knowledge_item(
            id,item_type,domain,title,canonical_start,canonical_end,canonical_scalar,
            source_time_basis,display_time,review_status,provenance_status,
            per_asset_source_confirmed,ingestion_decision,is_global)
        VALUES ('item:_leak_seed','State','geologia','(teste) estado semeado GOE',
            -2.4e9,-2.4e9,-2.4e9,'Ga','~2,4 Ga','approved','seeded-demo',
            false,'admitido',false)
    """)
    pub_seed = [r for r in rows_publica(-2.4e9, -2.4e9) if r[0] == 'item:_leak_seed']
    cur_seed = [r for r in rows_curatorial(-2.4e9, -2.4e9) if r[0] == 'item:_leak_seed']
    cur.execute("ROLLBACK TO SAVEPOINT seed")
    selo_ok = (len(cur_seed) == 1 and cur_seed[0][3] == 'demonstração' and cur_seed[0][4] is False)
    reg("A4-T8", "seeded-demo simultâneo não vaza ao público; curadoria vê 'demonstração' (is_fact=false)",
        len(pub_seed) == 0 and selo_ok,
        "no público: %d; na curatorial: %d (selo=%s, is_fact=%s)." % (
            len(pub_seed), len(cur_seed),
            cur_seed[0][3] if cur_seed else "-", cur_seed[0][4] if cur_seed else "-"))
except psycopg2.Error as ex:
    cur.execute("ROLLBACK TO SAVEPOINT seed")
    reg("A4-T8", "seeded-demo simultâneo não vaza ao público", False, "erro: %s" % ex)

# ---------------------------------------------------------------------------
# A4-T9 — interseção 3Z correta: nenhum item de 1789 aparece numa consulta de
# tempo profundo (e vice-versa). Tempo não "vaza" entre regimes.
# ---------------------------------------------------------------------------
deep = rows_curatorial(-2.4e9, -2.4e9)
tem_historico_no_profundo = any(r[0].startswith(("evt:posse", "concept:iluminismo")) for r in deep)
hist = rows_curatorial(-212.0, -210.0)
tem_profundo_no_historico = any(r[0] in ("entity:cianobacterias", "proc:fotossintese-oxigenica") for r in hist)
reg("A4-T9", "interseção temporal 3Z não mistura regimes (1789 ⟂ tempo profundo)",
    (not tem_historico_no_profundo) and (not tem_profundo_no_historico),
    "histórico no profundo: %s; profundo no histórico: %s." % (
        tem_historico_no_profundo, tem_profundo_no_historico))

# ---------------------------------------------------------------------------
# A4-T10 — lente sem correspondência devolve vazio (D-A3.5: informação, não erro).
# ---------------------------------------------------------------------------
vazio = rows_publica(-2.4e9, -2.4e9, ["historia"])   # não há história no GOE
reg("A4-T10", "lente sem correspondência devolve conjunto vazio (D-A3.5)",
    len(vazio) == 0, "linhas: %d (esperado 0)." % len(vazio))

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
    "instantes_canonicos": {k: list(v) for k, v in INSTANTES.items()},
    "testes": testes,
}
os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "test_a4_report.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(json.dumps(report, ensure_ascii=False, indent=2))
if report["falharam"] != 0:
    sys.exit(1)
