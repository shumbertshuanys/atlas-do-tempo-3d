-- =====================================================================
-- Atlas do Tempo 3D — Passo A3 · D-A3.3
-- 011-momento-envelope.sql — ENVELOPE MomentResult (forma β)
-- ADIÇÃO ao lado das funções A4 provadas. NÃO reescreve 010.
--
-- Princípio (Etapa 11 §6.3 [NORMATIVO] + Playbook §8):
--   A leitura factual NUNCA devolve "texto pelado". Cada item carrega o pacote
--   §8 (tipo epistêmico, confiança, atribuição+proveniência, regime de geometria,
--   flag de reconstrução, política de incerteza, selo, is_fact). O envelope nasce
--   NO BANCO, derivado do autoritativo — não é montado na borda HTTP.
--
-- Gating por construção (herdado do A4): a porta PÚBLICA reusa
-- f_simultaneidade_publica (lê só v_publishable_public); a CURATORIAL reusa
-- f_simultaneidade_curatorial. É IMPOSSÍVEL a pública devolver não-fato porque a
-- fonte não o contém. ClaimSet só aparece se seu HOST estiver entre os itens
-- exibidos da porta (gating por host — §5.5 do plano).
--
-- Forma β: UMA linha (RETURNS core.t_momento), com escalares tipados +
-- arrays/objetos JSONB. Cada função-porta devolve o MomentResult completo.
--
-- Descoberta que ajustou o contrato (nota-descoberta-a3-api-envelope.md):
--   * Só cset:kpg-causa tem host público (chicxulub); goe-ritmo/rev-francesa têm
--     host com fonte-por-asset pendente → NÃO públicos (por construção, não lista).
--   * claim_set_member tem UM weight (não a tripla evidence/scholarly/display):
--     expõe-se o real (pesos assimétricos) + a fronteira resolution; sem fabricar.
-- =====================================================================

-- ---------------------------------------------------------------------
-- TYPE composto do envelope (forma β). RETURNS core.t_momento (1 linha).
-- ---------------------------------------------------------------------
DROP TYPE IF EXISTS core.t_momento CASCADE;
CREATE TYPE core.t_momento AS (
  porta                     TEXT,    -- 'publica' | 'curatorial'
  query                     JSONB,   -- eco normalizado da MomentQuery
  normalized_time_range     JSONB,   -- [canonicalStart, canonicalEnd]
  normalized_spatial_scope  JSONB,   -- escopo + rótulo de geometria visível
  items                     JSONB,   -- array do contrato §8 por item
  states                    JSONB,   -- subconjunto itemType='State' (fundo)
  claim_sets                JSONB,   -- controvérsias c/ pesos assimétricos + fronteira
  uncertainty_profiles      JSONB,   -- faixas/margens por item (não "lados")
  anachronism_warnings      JSONB,   -- avisos de anacronismo do recorte
  equivalence_warnings      JSONB,   -- avisos anti-falsa-equivalência
  publicability_status      INT,     -- 1..5 (pública exibida = 1)
  gating_reason             TEXT,    -- explica o nível (NULL na pública exibida)
  gating_type               TEXT,    -- editorial|científico|licença|revisão-humana|...
  hidden_summary            JSONB,   -- pública: contagem; curatorial: lista
  navigation_suggestions    JSONB,   -- vizinhos (raso no A3)
  generated_scene_candidate JSONB    -- vazio no A3 (função não cria cena)
);

-- ---------------------------------------------------------------------
-- Núcleo §8 por item, PORTA-INDEPENDENTE (single-source; reduz divergência).
-- Os campos dependentes de porta (selo, isFact, reviewStatus,
-- uncertaintyDisplayPolicy) são mesclados por cada função com '||'.
-- Cada campo deriva do autoritativo: claim (epistemics, evidence_level,
-- provenance_ref), source (tier), geometry_version (regime/reconstrução).
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION core.f_item_envelope_core(p_item TEXT)
RETURNS JSONB AS $$
  SELECT jsonb_build_object(
    'itemId',         ki.id,
    'title',          ki.title,
    'itemType',       ki.item_type,
    'domain',         ki.domain,
    'epistemicType',  ep.claim_type,
    'confidenceLevel',ep.confidence,
    'evidenceLevel',  cl.evidence_level,
    'attributionRef', jsonb_build_object(
                        'label',        core.f_item_attribution(ki.id),
                        'provenanceRef',cl.provenance_ref,   -- [N1] NOT NULL
                        'sourceTier',   cl.authority_tier),
    'geometryRegime',
      CASE
        WHEN EXISTS (SELECT 1 FROM core.geometry_version g
                      WHERE g.item_ref = ki.id AND g.is_paleo)        THEN 'paleoPositions'
        WHEN EXISTS (SELECT 1 FROM core.geometry_version g
                      WHERE g.item_ref = ki.id)                       THEN 'modernGeometry'
        ELSE 'semLugarTerrestre'   -- escopo planetário/global, sem ponto terrestre
      END,
    'reconstructionFlag',
      (ep.claim_type = 'reconstrução-modelada')
      OR EXISTS (SELECT 1 FROM core.geometry_version g
                  WHERE g.item_ref = ki.id AND g.is_reconstruction),
    'displayTime',    ki.display_time,
    'sourceTimeBasis',ki.source_time_basis,
    'timePrecision',  ki.time_precision,
    'canonicalStart', ki.canonical_start,
    'canonicalEnd',   ki.canonical_end,
    'isGlobal',       ki.is_global,
    'anachronismNote',ki.anachronism_note
  )
  FROM core.knowledge_item ki
  CROSS JOIN LATERAL core.f_item_epistemics(ki.id) ep
  LEFT JOIN LATERAL (
    SELECT c.evidence_level, c.provenance_ref, s.authority_tier
    FROM core.claim c
    LEFT JOIN core.provenance_metadata pm ON pm.id = c.provenance_ref
    LEFT JOIN core.source s ON s.id = pm.source_id
    WHERE c.subject_ref = ki.id
    ORDER BY c.id LIMIT 1
  ) cl ON true
  WHERE ki.id = p_item;
$$ LANGUAGE sql STABLE;

-- =====================================================================
-- PORTA PÚBLICA — envelope completo, gated por construção.
-- Fonte: f_simultaneidade_publica (só v_publishable_public).
-- selo='público', isFact=TRUE por construção; uncertaintyDisplayPolicy nunca
-- 'omitir' (sempreRotular p/ tipos incertos; rótuloCompacto senão).
-- claim_sets: só os com host entre os itens públicos exibidos.
-- =====================================================================
CREATE OR REPLACE FUNCTION core.f_momento_publico(
  p_start  DOUBLE PRECISION,
  p_end    DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL
) RETURNS core.t_momento AS $$
  WITH g AS (
    SELECT * FROM core.f_simultaneidade_publica(p_start, p_end, p_lenses)
  ),
  it AS (
    SELECT r.id, r.item_type, r.anachronism_note, r.time_uncertainty,
      core.f_item_envelope_core(r.id)
      || jsonb_build_object(
           'selo',        r.selo,
           'isFact',      r.is_fact,
           'reviewStatus',r.review_status,
           'uncertaintyDisplayPolicy',
             CASE WHEN r.epistemic_type IN
                       ('reconstrução-modelada','hipótese','estimativa','proxy','inferência-científica')
                  THEN 'sempreRotular' ELSE 'rótuloCompacto' END
         ) AS obj
    FROM g r
  )
  SELECT ROW(
    'publica',
    jsonb_build_object('start', p_start, 'end', p_end,
                       'lenses', COALESCE(to_jsonb(p_lenses), '[]'::jsonb)),
    jsonb_build_object('canonicalStart', p_start, 'canonicalEnd', p_end),
    jsonb_build_object('scope', 'global', 'geometryLabelVisible', true),
    COALESCE((SELECT jsonb_agg(obj ORDER BY id) FROM it), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(obj ORDER BY id) FROM it WHERE item_type = 'State'), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object(
        'claimSetId',         cs.id,
        'host',               cs.subject_ref,
        'tema',               cs.tema,
        'resolutionBoundary', cs.resolution,
        'members', COALESCE((SELECT jsonb_agg(jsonb_build_object(
              'statement', mc.statement, 'weight', m.weight, 'stance', m.stance)
              ORDER BY m.weight DESC)
            FROM core.claim_set_member m JOIN core.claim mc ON mc.id = m.claim_id
            WHERE m.claim_set_id = cs.id), '[]'::jsonb)
      ) ORDER BY cs.id)
      FROM core.claim_set cs WHERE cs.subject_ref IN (SELECT id FROM it)), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object('itemId', id, 'uncertainty', time_uncertainty)
              ORDER BY id) FROM it WHERE time_uncertainty IS NOT NULL), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object('itemId', id, 'note', anachronism_note)
              ORDER BY id) FROM it WHERE anachronism_note IS NOT NULL), '[]'::jsonb),
    '[]'::jsonb,                                   -- equivalence_warnings (nenhum negacionismo carregado)
    1,                                             -- publicability_status: conjunto público exibido = nível 1
    NULL,                                          -- gating_reason (nada gated no exibido)
    NULL,                                          -- gating_type
    jsonb_build_object('hiddenCount',              -- só contagem; nunca identidades pela pública
      (SELECT count(*) FROM core.f_simultaneidade_curatorial(p_start, p_end, p_lenses))
      - (SELECT count(*) FROM g)),
    '[]'::jsonb,                                   -- navigation_suggestions (raso no A3)
    NULL                                           -- generated_scene_candidate (vazio no A3)
  )::core.t_momento;
$$ LANGUAGE sql STABLE SECURITY DEFINER SET search_path = core, public;

-- =====================================================================
-- PORTA CURATORIAL — mesmo contrato/forma; difere fonte e valores admissíveis.
-- Fonte: f_simultaneidade_curatorial (approved+pending; exclui legal-review/
-- rejected/blocked). selo ∈ {fato,demonstração,em-revisão}; seeded nunca isFact.
-- uncertaintyDisplayPolicy='aparatoCompleto'. hidden_summary PODE listar.
-- =====================================================================
CREATE OR REPLACE FUNCTION core.f_momento_curatorial(
  p_start  DOUBLE PRECISION,
  p_end    DOUBLE PRECISION,
  p_lenses TEXT[] DEFAULT NULL
) RETURNS core.t_momento AS $$
  WITH g AS (
    SELECT * FROM core.f_simultaneidade_curatorial(p_start, p_end, p_lenses)
  ),
  it AS (
    SELECT r.id, r.item_type, r.anachronism_note, r.time_uncertainty, r.is_fact,
      core.f_item_envelope_core(r.id)
      || jsonb_build_object(
           'selo',        r.selo,
           'isFact',      r.is_fact,
           'reviewStatus',r.review_status,
           'uncertaintyDisplayPolicy', 'aparatoCompleto'
         ) AS obj
    FROM g r
  )
  SELECT ROW(
    'curatorial',
    jsonb_build_object('start', p_start, 'end', p_end,
                       'lenses', COALESCE(to_jsonb(p_lenses), '[]'::jsonb)),
    jsonb_build_object('canonicalStart', p_start, 'canonicalEnd', p_end),
    jsonb_build_object('scope', 'global', 'geometryLabelVisible', true),
    COALESCE((SELECT jsonb_agg(obj ORDER BY id) FROM it), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(obj ORDER BY id) FROM it WHERE item_type = 'State'), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object(
        'claimSetId',         cs.id,
        'host',               cs.subject_ref,
        'tema',               cs.tema,
        'resolutionBoundary', cs.resolution,
        'members', COALESCE((SELECT jsonb_agg(jsonb_build_object(
              'statement', mc.statement, 'weight', m.weight, 'stance', m.stance)
              ORDER BY m.weight DESC)
            FROM core.claim_set_member m JOIN core.claim mc ON mc.id = m.claim_id
            WHERE m.claim_set_id = cs.id), '[]'::jsonb)
      ) ORDER BY cs.id)
      FROM core.claim_set cs WHERE cs.subject_ref IN (SELECT id FROM it)), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object('itemId', id, 'uncertainty', time_uncertainty)
              ORDER BY id) FROM it WHERE time_uncertainty IS NOT NULL), '[]'::jsonb),
    COALESCE((SELECT jsonb_agg(jsonb_build_object('itemId', id, 'note', anachronism_note)
              ORDER BY id) FROM it WHERE anachronism_note IS NOT NULL), '[]'::jsonb),
    '[]'::jsonb,                                   -- equivalence_warnings
    CASE WHEN EXISTS (SELECT 1 FROM it WHERE NOT is_fact) THEN 2 ELSE 1 END,
    CASE WHEN EXISTS (SELECT 1 FROM it WHERE NOT is_fact)
         THEN 'contém itens não-fato (demonstração/em-revisão) marcados; exibição curatorial' END,
    CASE WHEN EXISTS (SELECT 1 FROM it WHERE NOT is_fact) THEN 'revisão-humana' END,
    jsonb_build_object('hiddenItems',              -- curatorial PODE listar o que nem ela exibe
      COALESCE((SELECT jsonb_agg(jsonb_build_object(
            'itemId', ki.id, 'reviewStatus', ki.review_status,
            'ingestionDecision', ki.ingestion_decision) ORDER BY ki.id)
        FROM core.knowledge_item ki
        WHERE ki.canonical_start <= p_end AND ki.canonical_end >= p_start
          AND (p_lenses IS NULL OR array_length(p_lenses,1) IS NULL OR ki.domain = ANY(p_lenses))
          AND (ki.review_status IN ('legal-review','rejected') OR ki.ingestion_decision = 'blocked')),
        '[]'::jsonb)),
    '[]'::jsonb,                                   -- navigation_suggestions
    NULL                                           -- generated_scene_candidate
  )::core.t_momento;
$$ LANGUAGE sql STABLE SECURITY DEFINER SET search_path = core, public;

-- ---------------------------------------------------------------------
-- Portão por GRANT (D-A3.5): fecha a janela do EXECUTE-default-a-PUBLIC.
-- Os papéis atlas_public/atlas_curatorial e seus grants vivem em
-- db/roles/020-papeis-leitura.sql. Aqui só revogamos o default e mantemos
-- kc_service (consistência com 010). REVOKE precede qualquer GRANT externo.
-- ---------------------------------------------------------------------
REVOKE EXECUTE ON FUNCTION core.f_momento_publico(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[])    FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION core.f_momento_curatorial(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[]) FROM PUBLIC;
GRANT  EXECUTE ON FUNCTION core.f_momento_publico(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[])    TO kc_service;
GRANT  EXECUTE ON FUNCTION core.f_momento_curatorial(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[]) TO kc_service;
GRANT  EXECUTE ON FUNCTION core.f_item_envelope_core(TEXT) TO kc_service;
