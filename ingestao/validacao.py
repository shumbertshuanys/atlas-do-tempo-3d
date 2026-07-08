# -*- coding: utf-8 -*-
"""
Validação automática do pacote de ingestão — lista FECHADA v0 (spec §4).
QA bloqueia: falha em qualquer check ⇒ `bloqueado-validacao`, sem override,
sem waived (Art.13). Retorna (ok, falhas): falhas é lista de strings tipadas;
ok == (falhas == []).

Formato do pacote (JSON por rascunho em ingestao/rascunhos/<pacote_id>.json):

{
  "pacote_id": "pkg-...",
  "item": {
    "id","item_type","domain","title","layer"?,
    "canonical_start","canonical_end","canonical_scalar",
    "source_time_basis","display_time","time_precision","time_uncertainty",
    "is_global"?, "anachronism_note"?,
    "geo": null | {"lat","lng","place","is_paleo","is_reconstruction","modern_correspondence"?}
  },
  "claims":  [ {"local_id","statement","claim_type","confidence","evidence_level"?,
                "uncertainty_profile"?, "bindings":[{"source_local_id","locator"}, ...]} ],
  "sources": [ {"local_id","title","authority_tier","license","uri"?, "is_aggregator"?} ],
  "relations": [ {"local_id","src_ref","dst_ref","relation_type",
                  "bindings":[{"source_local_id","locator"}, ...]} ],   # afirmativas; opcional
  "claim_set": null | {"tema","resolution","members":[{"statement","weight","stance"}]},
  "pg5": "público|mediado|legal-review",
  "tier_proposto": "T0|T1",
  "pessoa_viva_citada": bool?,   # default false
  "contem_dado_menor": bool?,    # default false
  "notas": str?
}
"""
import vocab


def _walk(obj, path=""):
    """Gera (caminho, chave) para toda chave de dict aninhado (dicts e listas)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield path, k
            yield from _walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk(v, f"{path}[{i}]")


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _nonvazio(x):
    return isinstance(x, str) and x.strip() != ""


def validate_pacote(pkg, corpus_ids=None, open_ids=None):
    """Valida um pacote. corpus_ids/open_ids: conjuntos de ids de item para o
    check de colisão (§4.6). Retorna (ok: bool, falhas: list[str])."""
    corpus_ids = corpus_ids or set()
    open_ids = open_ids or set()
    f = []  # falhas

    # ---- §4.2 campos proibidos ausentes em QUALQUER nível (a IA não os escreve)
    for _path, chave in _walk(pkg):
        if chave in vocab.CAMPOS_PROIBIDOS:
            f.append(f"campo-proibido: '{chave}' presente no rascunho (§3.1/§4.2) — nasce só na promoção humana")

    # ---- shape mínimo do pacote
    item = pkg.get("item")
    claims = pkg.get("claims")
    sources = pkg.get("sources")
    if not isinstance(item, dict):
        f.append("schema: 'item' ausente ou não-objeto")
        item = {}
    if not isinstance(claims, list) or len(claims) < 1:
        f.append("schema: 'claims' deve ser lista com ≥ 1 claim (§1.1)")
        claims = claims if isinstance(claims, list) else []
    if not isinstance(sources, list) or len(sources) < 1:
        f.append("schema: 'sources' deve ser lista com ≥ 1 fonte (§1.1)")
        sources = sources if isinstance(sources, list) else []
    relations = pkg.get("relations") or []
    claim_set = pkg.get("claim_set")

    # ---- §4.1 vocabulários fechados
    if item.get("item_type") not in vocab.ITEM_TYPES:
        f.append(f"vocab: item_type inválido: {item.get('item_type')!r}")
    if pkg.get("pg5") not in vocab.PG5_VALUES:
        f.append(f"vocab: pg5 inválida: {pkg.get('pg5')!r}")
    if pkg.get("tier_proposto") not in vocab.TIERS:
        f.append(f"vocab: tier_proposto inválido: {pkg.get('tier_proposto')!r}")
    if item.get("source_time_basis") not in vocab.TIME_BASES:
        f.append(f"vocab: source_time_basis inválido: {item.get('source_time_basis')!r}")

    src_locais = set()
    for i, s in enumerate(sources):
        if not isinstance(s, dict):
            f.append(f"schema: sources[{i}] não-objeto"); continue
        lid = s.get("local_id")
        if not _nonvazio(lid):
            f.append(f"schema: sources[{i}].local_id ausente")
        else:
            src_locais.add(lid)
        if s.get("authority_tier") not in vocab.AUTHORITY_TIERS:
            f.append(f"vocab: sources[{i}].authority_tier inválido: {s.get('authority_tier')!r} (A/B/C)")
        if not _nonvazio(s.get("title")):
            f.append(f"schema: sources[{i}].title vazio")
        if not _nonvazio(s.get("license")):
            f.append(f"schema: sources[{i}].license vazia (necessária para o check de licença §6.1.8)")
        # Art.5: binding cita a AUTORIDADE real, nunca o agregador (§3.3)
        if s.get("is_aggregator") is True:
            f.append(f"art5: sources[{i}] marcada como agregador/índice — o binding deve citar a autoridade real (§3.3)")

    for i, c in enumerate(claims):
        if not isinstance(c, dict):
            f.append(f"schema: claims[{i}] não-objeto"); continue
        if c.get("claim_type") not in vocab.CLAIM_TYPES:
            f.append(f"vocab: claims[{i}].claim_type inválido: {c.get('claim_type')!r}")
        if c.get("confidence") not in vocab.CONFIDENCES:
            f.append(f"vocab: claims[{i}].confidence inválida: {c.get('confidence')!r}")
        if not _nonvazio(c.get("statement")):
            f.append(f"schema: claims[{i}].statement vazio")
        # ---- §4.3 binding: todo claim referencia ≥1 fonte do pacote c/ localizador
        bindings = c.get("bindings") or []
        if not bindings:
            f.append(f"[N1] claims[{i}] sem binding a fonte (localizador obrigatório §4.3)")
        for b in bindings:
            if not isinstance(b, dict):
                f.append(f"[N1] claims[{i}] binding não-objeto"); continue
            if b.get("source_local_id") not in src_locais:
                f.append(f"[N1] claims[{i}] binding aponta fonte inexistente no pacote: {b.get('source_local_id')!r}")
            if not _nonvazio(b.get("locator")):
                f.append(f"[N1] claims[{i}] binding com localizador VAZIO (página/URL/trecho §4.3)")

    # ---- §4.3 relações afirmativas: mesmo binding obrigatório
    for i, r in enumerate(relations):
        if not isinstance(r, dict):
            f.append(f"schema: relations[{i}] não-objeto"); continue
        if not _nonvazio(r.get("relation_type")):
            f.append(f"schema: relations[{i}].relation_type vazio")
        for lado in ("src_ref", "dst_ref"):
            ref = r.get(lado)
            if not _nonvazio(ref):
                f.append(f"schema: relations[{i}].{lado} vazio")
        bindings = r.get("bindings") or []
        if not bindings:
            f.append(f"[N1] relations[{i}] (afirmativa) sem binding a fonte (§4.3)")
        for b in bindings:
            if not isinstance(b, dict) or b.get("source_local_id") not in src_locais:
                f.append(f"[N1] relations[{i}] binding aponta fonte inexistente no pacote")
            elif not _nonvazio(b.get("locator")):
                f.append(f"[N1] relations[{i}] binding com localizador VAZIO")

    # ---- §4.4 eixo 3Z
    cs, ce, sc = item.get("canonical_start"), item.get("canonical_end"), item.get("canonical_scalar")
    if not (_num(cs) and _num(ce) and _num(sc)):
        f.append("3Z: canonical_start/end/scalar devem ser numéricos")
    else:
        if cs > ce:
            f.append(f"3Z: canonical_start ({cs}) > canonical_end ({ce})")
        if not (cs <= sc <= ce):
            f.append(f"3Z: canonical_scalar ({sc}) fora de [{cs},{ce}]")
    prec = item.get("time_precision")
    if not _nonvazio(prec):
        f.append("3Z: time_precision não declarada (§4.4)")
    else:
        # incerteza SEMPRE que a precisão não é exata — nunca número seco (§4.4)
        if prec.strip().lower() not in vocab.PRECISOES_EXATAS and not _nonvazio(item.get("time_uncertainty")):
            f.append(f"3Z: precisão '{prec}' não-exata exige time_uncertainty declarada (nunca número seco §4.4)")

    # ---- §4.5 geo: se localizável, geometria válida OU correspondência moderna;
    #      paleo ⇒ reconstrução (espelha o CHECK do banco).
    geo = item.get("geo")
    if isinstance(geo, dict):
        tem_coord = _num(geo.get("lat")) and _num(geo.get("lng"))
        tem_corresp = _nonvazio(geo.get("modern_correspondence"))
        if not (tem_coord or tem_corresp):
            f.append("geo: item localizável sem geometria válida NEM correspondência moderna (§4.5)")
        if tem_coord:
            if not (-90 <= geo["lat"] <= 90 and -180 <= geo["lng"] <= 180):
                f.append(f"geo: coordenadas fora de faixa (lat {geo.get('lat')}, lng {geo.get('lng')})")
        if geo.get("is_paleo") and not geo.get("is_reconstruction"):
            f.append("geo: paleoposição sem is_reconstruction (paleo ⇒ reconstrução §4.5 / CHECK do banco)")

    # ---- §4.6 colisão de id + padrão
    iid = item.get("id")
    if not _nonvazio(iid):
        f.append("id: item.id ausente")
    else:
        if not vocab.ID_PADRAO.match(iid):
            f.append(f"id: '{iid}' fora do padrão ^[a-z]+:[a-z0-9\\-]+$ (§4.6)")
        if iid in corpus_ids:
            f.append(f"id: '{iid}' colide com id já existente no corpus (§4.6)")
        if iid in open_ids:
            f.append(f"id: '{iid}' colide com id de outro pacote aberto (§4.6)")

    # ---- §3.2 claim_set: resolution VAZIA no rascunho; ClaimSet ⇒ tier 0
    if claim_set is not None:
        if not isinstance(claim_set, dict):
            f.append("schema: claim_set deve ser objeto ou null")
        else:
            resol = claim_set.get("resolution")
            if _nonvazio(resol):
                f.append("fronteira: claim_set.resolution deve ser VAZIA no rascunho — escrita só à mão pelo revisor (§3.2/§6.1.10)")
            membros = claim_set.get("members") or []
            if len(membros) < 2:
                f.append("claim_set: exige ≥ 2 membros (leituras concorrentes com pesos)")
            for m in membros:
                if not (isinstance(m, dict) and _num(m.get("weight"))):
                    f.append("claim_set: cada membro precisa de weight numérico (peso assimétrico)")
            if pkg.get("tier_proposto") != "T0":
                f.append("triagem: ClaimSet proposto exige tier T0 obrigatório (§3.2/§5)")

    # ---- §4.7 PII: sem dado de menor; (pessoa viva citada NÃO reprova aqui —
    #      força T0 na triagem §5). Dado de menor bloqueia (Art.14).
    if pkg.get("contem_dado_menor") is True:
        f.append("art14: pacote declara dado de menor — bloqueado (§4.7)")

    return (len(f) == 0, f)
