-- =====================================================================
-- Atlas do Tempo 3D — Passo A4 · Fatia 2
-- a4-leitura-simultaneidade.sql — CAMADA DE LEITURA GATEADA
-- A função central do produto: "O que acontecia no mundo neste momento?"
--
-- Princípio (Constituição Art.6/§9 + datum 3Z + [N4]):
--   * A simultaneidade é uma INTERSEÇÃO no eixo canônico (3Z): um item é
--     simultâneo a um instante/intervalo se [canonical_start, canonical_end]
--     SOBREPÕE o intervalo consultado (ponto = start=end).
--   * O PORTÃO é estrutural: a consulta PÚBLICA lê SOMENTE de
--     v_publishable_public (approved ∩ corpus ∩ fonte-por-asset-confirmada).
--     pending / legal-review / rejected / seeded-demo NUNCA entram — nem como
--     fato, nem de outra forma — porque não existem na view-fonte.
--   * A consulta CURATORIAL (ferramenta editorial) enxerga o pipeline, mas
--     jamais como fato: corpus-approved → 'fato'; seeded-demo-approved →
--     'demonstração' (is_fact=false); pending → 'em-revisão' (is_fact=false).
--     legal-review / rejected continuam invisíveis até liberação (Art.6).
--   * [N4]: o índice/eixo ORDENA e SELECIONA por tempo; NÃO decide verdade
--     nem publicabilidade — esses vêm reidratados do autoritativo (as views).
--
-- Cada linha devolve o pacote epistêmico do §8: tipo (claim_type), confiança,
-- incerteza-como-faixa, atribuição (proveniência), displayTime por regime,
-- sourceTimeBasis preservado, e o SELO de proveniência + flag is_fact.
-- =====================================================================

-- Tipo de retorno comum às duas funções (linha de simultaneidade gateada).
DROP TYPE IF EXISTS core.t_simultaneidade_row CASCADE;
CREATE TYPE core.t_simultaneidade_row AS (
  id                 TEXT,
  title              TEXT,
  item_type          TEXT,          -- Event|Process|Concept|State|Species|Entity
  domain             TEXT,          -- lente de domínio
  -- tipagem epistêmica (Art.7) — vem do claim do item (subject_ref = item)
  epistemic_type     TEXT,          -- claim_type: fato-documentado|reconstrução-modelada|...
  confidence         TEXT,          -- alta|média-alta|média|...
  -- tempo (3Z): exibição por regime + datum nativo preservado + incerteza como faixa
  display_time       TEXT,
  source_time_basis  TEXT,
  time_precision     TEXT,
  time_uncertainty   TEXT,          -- faixa/±  (nunca número seco quando há incerteza)
  canonical_start    DOUBLE PRECISION,
  canonical_end      DOUBLE PRECISION,
  canonical_scalar   DOUBLE PRECISION,
  is_global          BOOLEAN,
  anachronism_note   TEXT,          -- paleoposição ≠ atual (Art.12/§8)
  -- proveniência / atribuição
  attribution        TEXT,          -- fonte (corpus) OU rótulo de demonstração
  provenance_status  TEXT,          -- corpus | seeded-demo
  review_status      TEXT,          -- approved | pending  (curatorial expõe; público sempre approved)
  -- SELO de exibição (o que a UI pode afirmar)
  selo               TEXT,          -- 'público' | 'fato' | 'demonstração' | 'em-revisão'
  is_fact            BOOLEAN        -- TRUE só quando pode ser exibido COMO FATO
);

-- ---------------------------------------------------------------------
-- Atribuição: a proveniência declarada de um item, derivada do claim do
-- item (subject_ref = item) → provenance_metadata → source. Para seeded-demo,
-- a fonte não é inventada (D-A3.1): devolve rótulo de demonstração.
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION core.f_item_attribution(p_item TEXT)
RETURNS TEXT AS $$
  SELECT COALESCE(
           NULLIF(string_agg(
             CASE
               WHEN s.title IS NOT NULL AND s.authority_tier IS NOT NULL
                 THEN s.title || ' (tier ' || s.authority_tier || ')'
               WHEN s.title IS NOT NULL
                 THEN s.title
               ELSE NULL
             END, '; '), ''),
           'demonstração — fonte não validada contra o corpus'
         )
  FROM core.claim c
  LEFT JOIN core.provenance_metadata pm ON pm.id = c.provenance_ref
  LEFT JOIN core.source s ON s.id = pm.source_id
  WHERE c.subject_ref = p_item;
$$ LANGUAGE sql STABLE;

-- ---------------------------------------------------------------------
-- Tipagem epistêmica + confiança do item, derivadas do claim do item.
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION core.f_item_epistemics(p_item TEXT,
                                                   OUT claim_type TEXT,
                                                   OUT confidence TEXT)
AS $$
  SELECT c.claim_type, c.confidence
  FROM core.claim c
  WHERE c.subject_ref = p_item
  ORDER BY c.id
  LIMIT 1;
$$ LANGUAGE sql STABLE;

-- =====================================================================
-- CONSULTA PÚBLICA GATEADA — lê SOMENTE de v_publishable_public.
-- selo := 'público'; is_fact := TRUE para toda linha (por construção da view).
-- Por desenho, é IMPOSSÍVEL devolver pending/legal-review/rejected/seeded:
-- eles não existem na relação-fonte.
-- =====================================================================
CREATE OR REPLACE FUNCTION core.f_simultaneidade_publica(
  p_start  DOUBLE PRECISION,
  p_end    DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL            -- NULL/{} = todas as lentes
) RETURNS SETOF core.t_simultaneidade_row AS $$
  SELECT
    v.id, v.title, v.item_type, v.domain,
    ep.claim_type, ep.confidence,
    v.display_time, v.source_time_basis, v.time_precision, v.time_uncertainty,
    v.canonical_start, v.canonical_end, v.canonical_scalar,
    v.is_global, v.anachronism_note,
    core.f_item_attribution(v.id),
    v.provenance_status, v.review_status,
    'público'::TEXT AS selo,
    TRUE            AS is_fact
  FROM core.v_publishable_public v
  CROSS JOIN LATERAL core.f_item_epistemics(v.id) ep
  WHERE v.canonical_start <= p_end           -- OVERLAP de intervalos no eixo 3Z
    AND v.canonical_end   >= p_start
    AND (p_lenses IS NULL OR array_length(p_lenses,1) IS NULL OR v.domain = ANY(p_lenses))
  ORDER BY v.canonical_scalar, v.id;
$$ LANGUAGE sql STABLE;

-- Atalho "instante" (ponto no eixo): start = end = p_scalar.
CREATE OR REPLACE FUNCTION core.f_simultaneidade_publica_em(
  p_scalar DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL
) RETURNS SETOF core.t_simultaneidade_row AS $$
  SELECT * FROM core.f_simultaneidade_publica(p_scalar, p_scalar, p_lenses);
$$ LANGUAGE sql STABLE;

-- =====================================================================
-- CONSULTA CURATORIAL GATEADA — ferramenta editorial. Enxerga o pipeline,
-- nunca como fato. Fonte: itens approved (= v_displayable_curatorial) com
-- selo por proveniência, MAIS itens pending com selo 'em-revisão'.
-- legal-review / rejected permanecem invisíveis (Art.6 soberano, inclusive
-- na simultaneidade). seeded-demo aparece como 'demonstração' (is_fact=false).
-- =====================================================================
CREATE OR REPLACE FUNCTION core.f_simultaneidade_curatorial(
  p_start  DOUBLE PRECISION,
  p_end    DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL
) RETURNS SETOF core.t_simultaneidade_row AS $$
  SELECT
    ki.id, ki.title, ki.item_type, ki.domain,
    ep.claim_type, ep.confidence,
    ki.display_time, ki.source_time_basis, ki.time_precision, ki.time_uncertainty,
    ki.canonical_start, ki.canonical_end, ki.canonical_scalar,
    ki.is_global, ki.anachronism_note,
    core.f_item_attribution(ki.id),
    ki.provenance_status, ki.review_status,
    CASE
      WHEN ki.review_status = 'approved' AND ki.provenance_status = 'corpus'
        THEN 'fato'
      WHEN ki.review_status = 'approved' AND ki.provenance_status = 'seeded-demo'
        THEN 'demonstração'
      WHEN ki.review_status = 'pending'
        THEN 'em-revisão'
    END::TEXT AS selo,
    (ki.review_status = 'approved' AND ki.provenance_status = 'corpus') AS is_fact
  FROM core.knowledge_item ki
  CROSS JOIN LATERAL core.f_item_epistemics(ki.id) ep
  WHERE ki.ingestion_decision <> 'blocked'
    AND ki.review_status IN ('approved','pending')   -- exclui legal-review/rejected (Art.6)
    AND ki.canonical_start <= p_end
    AND ki.canonical_end   >= p_start
    AND (p_lenses IS NULL OR array_length(p_lenses,1) IS NULL OR ki.domain = ANY(p_lenses))
  ORDER BY ki.canonical_scalar, ki.id;
$$ LANGUAGE sql STABLE;

CREATE OR REPLACE FUNCTION core.f_simultaneidade_curatorial_em(
  p_scalar DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL
) RETURNS SETOF core.t_simultaneidade_row AS $$
  SELECT * FROM core.f_simultaneidade_curatorial(p_scalar, p_scalar, p_lenses);
$$ LANGUAGE sql STABLE;

-- Permissão: kc_service pode executar as leituras (lê só núcleo/views; o
-- isolamento de iso permanece — T6). EXECUTE explícito por robustez.
GRANT EXECUTE ON FUNCTION core.f_simultaneidade_publica(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[]) TO kc_service;
GRANT EXECUTE ON FUNCTION core.f_simultaneidade_publica_em(DOUBLE PRECISION,TEXT[]) TO kc_service;
GRANT EXECUTE ON FUNCTION core.f_simultaneidade_curatorial(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[]) TO kc_service;
GRANT EXECUTE ON FUNCTION core.f_simultaneidade_curatorial_em(DOUBLE PRECISION,TEXT[]) TO kc_service;
GRANT EXECUTE ON FUNCTION core.f_item_attribution(TEXT) TO kc_service;
GRANT EXECUTE ON FUNCTION core.f_item_epistemics(TEXT) TO kc_service;
