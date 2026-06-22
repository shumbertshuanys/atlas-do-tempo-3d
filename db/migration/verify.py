#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A4 · Fatia 1
verify.py — reproduz os 10 testes FALSIFICÁVEIS (T1–T10) dos invariantes
constitucionais sobre o banco reconstruído. É o GATE de avanço: só se 10/10
verde a camada de leitura gateada (Fatia 2+) prossegue.

Espelha verification_report.json do A3 (mesmos ids, invariantes e expectativas).
Cada teste é isolado por SAVEPOINT (negativos) ou conexão própria (T6), de modo
que um caso jamais contamina o seguinte. Os testes NEGATIVOS (T1/T9) provam a
imposição estrutural: a violação é IMPOSSÍVEL de inserir (CHECK), não "barrada
por boa vontade do código".
"""
import json
import os
import sys
import psycopg2

# saída em UTF-8 mesmo em consoles legados (ex.: cp1252 no Windows) — o relatório
# contém '∩'/'⊂'. Não muda o conteúdo, só o encoding do stdout.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DSN = "host=localhost dbname=atlas user=atlas password=atlas"

# diretório de saída relativo ao próprio script (db/migration -> raiz/out),
# independente do diretório de trabalho e do SO.
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "out")

resultados = []


def reg(tid, inv, tipo, esperado, passou, detalhe):
    resultados.append({
        "id": tid,
        "invariante": inv,
        "tipo": tipo,
        "esperado": esperado,
        "passou": bool(passou),
        "detalhe": detalhe,
    })


conn = psycopg2.connect(DSN)
conn.autocommit = False
cur = conn.cursor()


def sp(name):
    cur.execute("SAVEPOINT %s" % name)


def rb(name):
    cur.execute("ROLLBACK TO SAVEPOINT %s" % name)


def one(q, args=None):
    cur.execute(q, args or ())
    return cur.fetchone()[0]


# ---------------------------------------------------------------------------
# T1 — [N1] negativo: aresta afirmativa SEM proveniência é rejeitada (CHECK)
# ---------------------------------------------------------------------------
sp("t1")
try:
    cur.execute("INSERT INTO core.entity_node(uri, entity_kind) VALUES ('rel:_t1_bad','relationship')")
    cur.execute("""
        INSERT INTO core.relationship(id, src_ref, dst_ref, relation_type,
                                       is_affirmative, provenance_ref, review_status)
        SELECT 'rel:_t1_bad', ki.id, ki.id, 'causou', true, NULL, 'approved'
        FROM core.knowledge_item ki LIMIT 1
    """)
    # Se inseriu, o invariante NÃO foi imposto → falha.
    rb("t1")
    reg("T1", "[N1]", "negativo (deve falhar)",
        "aresta afirmativa sem proveniência é rejeitada",
        False, "INSERIU sem proveniência — CHECK não barrou (FALHA estrutural).")
except psycopg2.Error as e:
    detail = str(e)
    rb("t1")
    ok = "n1_affirmative_needs_provenance" in detail
    reg("T1", "[N1]", "negativo (deve falhar)",
        "aresta afirmativa sem proveniência é rejeitada",
        ok, "rejeitada por n1_affirmative_needs_provenance (CHECK).")

# ---------------------------------------------------------------------------
# T2 — [N1] positivo: toda aresta afirmativa carregada tem provenance_ref
# ---------------------------------------------------------------------------
afirm = one("SELECT count(*) FROM core.relationship WHERE is_affirmative")
sem = one("SELECT count(*) FROM core.relationship WHERE is_affirmative AND provenance_ref IS NULL")
reg("T2", "[N1]", "positivo",
    "toda aresta afirmativa carregada tem provenance_ref",
    sem == 0,
    "%d arestas afirmativas, todas com proveniência; %d sem proveniência." % (afirm, sem))

# ---------------------------------------------------------------------------
# T3 — Art.6 positivo: view curatorial não contém pending/legal-review/rejected
# ---------------------------------------------------------------------------
vaz = one("SELECT count(*) FROM core.v_displayable_curatorial WHERE review_status <> 'approved'")
tot = one("SELECT count(*) FROM core.v_displayable_curatorial")
reg("T3", "Art.6", "positivo",
    "view curatorial não contém pending/legal-review/rejected",
    vaz == 0 and tot == 23,
    "%d itens não-aprovados vazaram; %d itens exibíveis no total." % (vaz, tot))

# ---------------------------------------------------------------------------
# T4 — Art.6 dinâmico: item legal-review existe na base, INVISÍVEL na view
# ---------------------------------------------------------------------------
sp("t4")
try:
    cur.execute("INSERT INTO core.entity_node(uri, entity_kind) VALUES ('item:_t4_legal','item')")
    cur.execute("""
        INSERT INTO core.knowledge_item(
            id, item_type, domain, title,
            canonical_start, canonical_end, canonical_scalar,
            source_time_basis, display_time,
            review_status, provenance_status,
            per_asset_source_confirmed, ingestion_decision, is_global)
        VALUES ('item:_t4_legal','Event','historia','(teste) item em legal-review',
            -210.5, -210.5, -210.5, 'gregorianCE', '1789',
            'legal-review', 'corpus', true, 'admitido', false)
    """)
    na_base = one("SELECT count(*) FROM core.knowledge_item WHERE id='item:_t4_legal'")
    na_view = one("SELECT count(*) FROM core.v_displayable_curatorial WHERE id='item:_t4_legal'")
    rb("t4")
    reg("T4", "Art.6", "dinâmico (estrutural)",
        "item legal-review existe na base porém é invisível na view",
        na_base == 1 and na_view == 0,
        "na tabela base: %d; visível na view curatorial: %d (o portão filtra, não os dados)." % (na_base, na_view))
except psycopg2.Error as e:
    detail = str(e)
    rb("t4")
    reg("T4", "Art.6", "dinâmico (estrutural)",
        "item legal-review existe na base porém é invisível na view",
        False, "erro inesperado: %s" % detail)

# ---------------------------------------------------------------------------
# T5 — §9/Art.6 positivo: público = approved ∩ corpus ∩ fonte-confirmada; 0 seeded
# ---------------------------------------------------------------------------
seeded_pub = one("SELECT count(*) FROM core.v_publishable_public WHERE provenance_status='seeded-demo'")
pub = one("SELECT count(*) FROM core.v_publishable_public")
fora = one("""SELECT count(*) FROM core.v_publishable_public
              WHERE NOT (review_status='approved'
                         AND provenance_status='corpus'
                         AND per_asset_source_confirmed)""")
reg("T5", "§9 / Art.6", "positivo",
    "view pública = approved ∩ corpus ∩ fonte-confirmada; zero seeded-demo",
    seeded_pub == 0 and pub == 11 and fora == 0,
    "seeded-demo vazados ao público: %d; total público: %d; itens públicos fora do contrato: %d." % (seeded_pub, pub, fora))

# ---------------------------------------------------------------------------
# T6 — [N3]/Art.11 negativo: kc_service NÃO acessa o schema iso (REVOKE)
#      Conexão própria em autocommit para não tocar a transação principal.
# ---------------------------------------------------------------------------
c6 = psycopg2.connect(DSN)
c6.autocommit = True
cur6 = c6.cursor()
try:
    cur6.execute("SET ROLE kc_service")
    try:
        cur6.execute("SELECT count(*) FROM iso.media_asset_isolated")
        cur6.fetchone()
        t6_ok = False
        t6_det = "kc_service LEU o schema iso (FALHA de isolamento)."
    except psycopg2.Error:
        t6_ok = True
        t6_det = "permissão negada no schema iso para kc_service (REVOKE efetivo)."
finally:
    try:
        cur6.close()
        c6.close()
    except Exception:
        pass
reg("T6", "[N3]/Art.11", "negativo (deve falhar)",
    "kc_service não acessa o schema iso", t6_ok, t6_det)

# ---------------------------------------------------------------------------
# T7 — [N2] misto: derived_cache não é nó autoritativo e não carrega proveniência
# ---------------------------------------------------------------------------
fks = one("""SELECT count(*) FROM pg_constraint con
             JOIN pg_class rel ON rel.oid = con.conrelid
             JOIN pg_namespace n ON n.oid = rel.relnamespace
             WHERE n.nspname='derived' AND rel.relname='derived_cache' AND con.contype='f'""")
sp("t7a")
accept_false = False
try:
    cur.execute("INSERT INTO derived.derived_cache(id,cache_kind,carries_provenance) VALUES ('cache:_t7','index',false)")
    accept_false = True
    rb("t7a")
except psycopg2.Error:
    rb("t7a")
sp("t7b")
reject_true = False
try:
    cur.execute("INSERT INTO derived.derived_cache(id,cache_kind,carries_provenance) VALUES ('cache:_t7b','index',true)")
    rb("t7b")
except psycopg2.Error:
    reject_true = True
    rb("t7b")
reg("T7", "[N2]", "misto (estrutural + negativo)",
    "cache derivado não é nó autoritativo e não pode carregar proveniência",
    fks == 0 and accept_false and reject_true,
    "FKs de derived_cache para entity_node: %d; aceita carries_provenance=false: %s; rejeita carries_provenance=true: %s." % (fks, accept_false, reject_true))

# ---------------------------------------------------------------------------
# T8 — Art.11/D-B2.4 misto: SA rejeitado no media-store, aceito no isolated-store
# ---------------------------------------------------------------------------
sp("t8")
sa_rejected = False
sa_accepted = False
try:
    cur.execute("""INSERT INTO core.license_profile(id,label,share_alike,license_risk_level)
                   VALUES ('lp:_t8_sa','CC BY-SA (teste)',true,0)
                   ON CONFLICT (id) DO NOTHING""")
    cur.execute("""INSERT INTO core.entity_node(uri,entity_kind)
                   VALUES ('asset:_t8','media_asset') ON CONFLICT (uri) DO NOTHING""")
    sp("t8a")
    try:
        cur.execute("""INSERT INTO core.media_asset(id,nature_label,license_profile_ref,storage_partition)
                       VALUES ('asset:_t8','mapa','lp:_t8_sa','media-store')""")
        rb("t8a")  # não deveria chegar
    except psycopg2.Error:
        sa_rejected = True
        rb("t8a")
    sp("t8b")
    try:
        cur.execute("""INSERT INTO core.media_asset(id,nature_label,license_profile_ref,storage_partition)
                       VALUES ('asset:_t8','mapa','lp:_t8_sa','isolated-license-store')""")
        sa_accepted = True
        rb("t8b")
    except psycopg2.Error:
        rb("t8b")
    rb("t8")
except psycopg2.Error as e:
    detail = str(e)
    rb("t8")
reg("T8", "Art.11/D-B2.4", "misto",
    "SA rejeitado no media-store, aceito no isolated-store",
    sa_rejected and sa_accepted,
    "asset ShareAlike no media-store rejeitado: %s; no isolated-store aceito: %s." % (sa_rejected, sa_accepted))

# ---------------------------------------------------------------------------
# T9 — Art.12/§8 negativo: paleogeometria NÃO-reconstrução é rejeitada (CHECK)
# ---------------------------------------------------------------------------
sp("t9")
t9_ok = False
try:
    item_id = one("SELECT id FROM core.knowledge_item ORDER BY id LIMIT 1")
    cur.execute("""INSERT INTO core.geometry_version(id,item_ref,geom,is_paleo,is_reconstruction)
                   VALUES ('geom:_t9', %s, ST_SetSRID(ST_MakePoint(0,0),4326), true, false)""",
                (item_id,))
    rb("t9")  # não deveria chegar
except psycopg2.Error as e:
    detail = str(e)
    t9_ok = "paleo_is_always_reconstruction" in detail
    rb("t9")
reg("T9", "Art.12/§8", "negativo (deve falhar)",
    "paleogeometria não-reconstrução é rejeitada",
    t9_ok, "rejeitada por paleo_is_always_reconstruction (CHECK).")

# ---------------------------------------------------------------------------
# T10 — carga/3Z positivo: contagens batem; claims_total = item + membros
#       (queries idênticas às de migrate.py)
# ---------------------------------------------------------------------------
obtido = {
    "itens": one("SELECT count(*) FROM core.knowledge_item"),
    "approved": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='approved'"),
    "pending": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='pending'"),
    "legal_review": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='legal-review'"),
    "seeded": one("SELECT count(*) FROM core.knowledge_item WHERE provenance_status='seeded-demo'"),
    "corpus": one("SELECT count(*) FROM core.knowledge_item WHERE provenance_status='corpus'"),
    "claims_total": one("SELECT count(*) FROM core.claim"),
    "claims_de_item": one("SELECT count(*) FROM core.claim c JOIN core.knowledge_item i ON c.subject_ref=i.id"),
    "claims_membros": one("SELECT count(*) FROM core.claim_set_member"),
    "claimsets": one("SELECT count(*) FROM core.claim_set"),
}
esper = {
    "itens": 35, "approved": 23, "pending": 12, "legal_review": 0,
    "seeded": 8, "corpus": 27, "claims_total": 39,
    "claims_de_item": 35, "claims_membros": 4, "claimsets": 2,
}
soma_ok = obtido["claims_total"] == obtido["claims_de_item"] + obtido["claims_membros"]
reg("T10", "carga/3Z", "positivo",
    "contagens batem; claims_total = claims_de_item + claims_membros",
    obtido == esper and soma_ok,
    "obtido %s." % json.dumps(obtido, ensure_ascii=False))

# ---------------------------------------------------------------------------
# Encerramento — relatório
# ---------------------------------------------------------------------------
conn.rollback()  # nenhum efeito colateral persiste; verify.py é read-only por desenho
cur.close()
conn.close()

passaram = sum(1 for r in resultados if r["passou"])
report = {
    "total": len(resultados),
    "passaram": passaram,
    "falharam": len(resultados) - passaram,
    "testes": resultados,
}
os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "verification_report.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(json.dumps(report, ensure_ascii=False, indent=2))
if report["falharam"] != 0:
    sys.exit(1)
