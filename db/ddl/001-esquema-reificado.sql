-- =====================================================================
-- Atlas do Tempo 3D — DDL do esquema REIFICADO (bundle 00→05)
-- Reconstrução fiel (Passo A4) do esquema aplicado no Passo A3.
-- Fontes de design: Passo B1 §5.2 (tabelas reservadas), Passo B2 §5.1
-- (delta de reificação), Constituição v1.1 (Arts. 6/7/10/11/12, [N1]–[N5]),
-- datum temporal 3Z (canonicalTimeScalar, T0=2000.0 CE). Nomes de constraint
-- e contagens-alvo conferem com verification_report.json (A3).
--
-- O esquema carrega os invariantes NA ESTRUTURA (não na boa vontade do
-- código de aplicação). O portão (Art.6/§9) é propriedade das VIEWS; os
-- dados continuam íntegros por trás do portão.
-- =====================================================================

-- ===== 00 — esquemas, extensão, papéis =====
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE SCHEMA IF NOT EXISTS core;       -- núcleo factual autoritativo (Knowledge Core)
CREATE SCHEMA IF NOT EXISTS derived;    -- derivados ([N2]: nunca verdade)
CREATE SCHEMA IF NOT EXISTS iso;        -- IsolatedLicenseStore ([N3]/Art.11): SA/ODbL/NC

-- Papel de serviço do núcleo. Compõe Claim a partir do núcleo; por [N3]/Art.11
-- NUNCA pode ler o store isolado. (T6: REVOKE efetivo sobre o schema iso.)
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='kc_service') THEN
    CREATE ROLE kc_service NOLOGIN;
  END IF;
END $$;

-- ===== 01 — backbone de reificação + proveniência/fonte/licença =====
-- [D-B2.1] entity_node: única espinha pela qual algo é SUJEITO de enunciado.
-- [D-B2.5] entity_kind é LISTA FECHADA de 6 valores; derivado NUNCA entra aqui.
CREATE TABLE core.entity_node (
  uri                 TEXT PRIMARY KEY,
  entity_kind         TEXT NOT NULL,
  current_version_ref TEXT,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT entity_kind_closed_list CHECK
    (entity_kind IN ('item','relationship','claim','source','media_asset','claim_set'))
);

-- Fonte (promovida a 1ª classe — P08). Classificada por confiabilidade/licença.
CREATE TABLE core.source (
  id             TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  title          TEXT,
  source_type    TEXT,
  authority_tier TEXT,             -- A | B | C | NULL (NULL = sem tier, ex.: demonstração)
  license        TEXT,
  uri            TEXT,
  retrieved_at   TIMESTAMPTZ,
  CONSTRAINT authority_tier_domain CHECK (authority_tier IS NULL OR authority_tier IN ('A','B','C'))
);

-- Perfil de licença (governa a EXPRESSÃO/asset, nunca o fato — Art.11).
CREATE TABLE core.license_profile (
  id                 TEXT PRIMARY KEY,
  label              TEXT NOT NULL,
  share_alike        BOOLEAN NOT NULL DEFAULT false,   -- SA/ODbL
  license_risk_level INT NOT NULL DEFAULT 0            -- 4 = NC-como-expressão (bloqueado)
);

-- Proveniência (FK real — Art.10). É o alvo de provenance_ref.
CREATE TABLE core.provenance_metadata (
  id               TEXT PRIMARY KEY,
  source_id        TEXT REFERENCES core.source(id),
  dataset_snapshot TEXT,
  method           TEXT,
  scale_version    TEXT,
  created_by       TEXT,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ===== 02 — knowledge_item / relationship / claim / claim_set / geometria / mídia =====
-- knowledge_item: também registrado em entity_node (entity_kind='item').
-- Carrega os DOIS eixos de gating (Art.6/§9): review_status e provenance_status,
-- além de per_asset_source_confirmed (§9.2 F2) e ingestion_decision.
-- Datum 3Z embutido: canonical_start/end/scalar + source_time_basis + display.
CREATE TABLE core.knowledge_item (
  id                         TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  item_type                  TEXT NOT NULL,        -- Event|Process|Concept|State|Species|Entity
  domain                     TEXT NOT NULL,        -- lente de domínio (historia|geologia|...)
  layer                      TEXT,
  title                      TEXT NOT NULL,
  -- eixo canônico (3Z): anos rel. a T0=2000.0 CE; negativo=passado
  canonical_start            DOUBLE PRECISION NOT NULL,
  canonical_end              DOUBLE PRECISION NOT NULL,
  canonical_scalar           DOUBLE PRECISION NOT NULL,  -- ponto ordenável (ponto médio)
  source_time_basis          TEXT NOT NULL,        -- gregorianCE|Ma|Ga|scenarioYear|...
  display_time               TEXT NOT NULL,        -- string por regime ("1789"; "~2,4 Ga")
  time_precision             TEXT,                 -- ano|século|Ma|Ga|...
  time_uncertainty           TEXT,                 -- faixa/±  (nunca número seco quando há incerteza)
  -- gating (Art.6 / §9)
  review_status              TEXT NOT NULL,        -- approved|pending|legal-review|rejected
  provenance_status          TEXT NOT NULL,        -- corpus|seeded-demo
  per_asset_source_confirmed BOOLEAN NOT NULL DEFAULT false,  -- §9.2 (F2)
  ingestion_decision         TEXT NOT NULL DEFAULT 'admitido', -- admitido|blocked
  is_global                  BOOLEAN NOT NULL DEFAULT false,
  anachronism_note           TEXT,
  CONSTRAINT review_status_domain CHECK
    (review_status IN ('approved','pending','legal-review','rejected')),
  CONSTRAINT provenance_status_domain CHECK
    (provenance_status IN ('corpus','seeded-demo')),
  CONSTRAINT ingestion_decision_domain CHECK
    (ingestion_decision IN ('admitido','blocked')),
  CONSTRAINT canonical_interval_ok CHECK (canonical_start <= canonical_end)
);

-- claim (promovido a 1ª classe; subject_ref agora FK real ao backbone — Art.10).
-- provenance_ref OBRIGATÓRIO ([N1]).
CREATE TABLE core.claim (
  id             TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  subject_ref    TEXT NOT NULL REFERENCES core.entity_node(uri),  -- item|aresta|source|asset|claim
  statement      TEXT NOT NULL,
  claim_type     TEXT NOT NULL,   -- fato-documentado|inferência-científica|proxy|reconstrução-modelada|estimativa|hipótese|interpretação|medição-direta|representação-artística|aproximação-didática
  evidence_level TEXT,
  confidence     TEXT NOT NULL,   -- alta|média-alta|média|média-baixa|baixa
  review_status  TEXT NOT NULL,   -- [N1]
  provenance_ref TEXT NOT NULL REFERENCES core.provenance_metadata(id)  -- [N1] OBRIGATÓRIO
);

-- relationship (aresta reificável; extremos = FK real ao backbone — Art.10).
-- [N1] como CHECK estrutural: aresta afirmativa órfã de proveniência é
-- IMPOSSÍVEL de inserir (não "rejeitada por trigger").
CREATE TABLE core.relationship (
  id             TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  src_ref        TEXT NOT NULL REFERENCES core.entity_node(uri),
  dst_ref        TEXT NOT NULL REFERENCES core.entity_node(uri),
  relation_type  TEXT NOT NULL,            -- causou|influenciou|afetou|representa|evidencia|...
  is_affirmative BOOLEAN NOT NULL,
  provenance_ref TEXT REFERENCES core.provenance_metadata(id),
  review_status  TEXT NOT NULL,
  CONSTRAINT n1_affirmative_needs_provenance CHECK
    (NOT is_affirmative OR provenance_ref IS NOT NULL)
);

-- claim_set (claim-sobre-claims; pesos assimétricos; não-falsa-equivalência — Art.7).
CREATE TABLE core.claim_set (
  id          TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  subject_ref TEXT NOT NULL REFERENCES core.entity_node(uri),
  tema        TEXT NOT NULL,
  resolution  TEXT NOT NULL   -- regra escrita à mão de não-equivalência (§5.4/§8.1)
);
CREATE TABLE core.claim_set_member (
  claim_set_id TEXT NOT NULL REFERENCES core.claim_set(id),
  claim_id     TEXT NOT NULL REFERENCES core.claim(id),
  weight       NUMERIC,
  stance       TEXT,
  PRIMARY KEY (claim_set_id, claim_id)
);

-- geometry_version: paleoposição é SEMPRE reconstrução (Art.12/§8; [N3]).
-- T9: paleo não-reconstrução é rejeitada por paleo_is_always_reconstruction.
CREATE TABLE core.geometry_version (
  id                TEXT PRIMARY KEY,
  item_ref          TEXT NOT NULL REFERENCES core.knowledge_item(id),
  geom              geometry(Geometry,4326),
  is_paleo          BOOLEAN NOT NULL DEFAULT false,  -- paleoposição (não é a localidade atual)
  is_reconstruction BOOLEAN NOT NULL DEFAULT false,
  scale_version     TEXT,
  CONSTRAINT paleo_is_always_reconstruction CHECK (NOT is_paleo OR is_reconstruction)
);

-- media_asset (1ª classe — P09): natureza + licença + partição (Art.11).
-- A relação asset↔fato é ARESTA (representa|evidencia), nunca embutida.
CREATE TABLE core.media_asset (
  id                  TEXT PRIMARY KEY REFERENCES core.entity_node(uri),
  nature_label        TEXT NOT NULL,   -- fotografia|mapa|gráfico|reconstrução-científica|simulação|representação-artística|aproximação-didática
  license_profile_ref TEXT NOT NULL REFERENCES core.license_profile(id),
  storage_partition   TEXT NOT NULL,   -- media-store|isolated-license-store|blocked
  textual_equivalent  TEXT,
  attribution_text    TEXT,            -- viaja com o asset (inv.17)
  storage_uri         TEXT,
  CONSTRAINT storage_partition_domain CHECK
    (storage_partition IN ('media-store','isolated-license-store','blocked'))
);

-- [D-B2.4/P11] isolamento de licença imposto no esquema, via trigger que
-- consulta o license_profile: SA => isolated-license-store; NC-expr => blocked.
-- (T8: SA no media-store é rejeitado; no isolated-store é aceito.)
CREATE OR REPLACE FUNCTION core.f_enforce_media_isolation() RETURNS trigger AS $$
DECLARE lp core.license_profile%ROWTYPE;
BEGIN
  SELECT * INTO lp FROM core.license_profile WHERE id = NEW.license_profile_ref;
  IF lp.share_alike AND NEW.storage_partition = 'media-store' THEN
    RAISE EXCEPTION 'isolamento de licenca (Art.11/P11): asset ShareAlike nao pode viver no media-store; use isolated-license-store';
  END IF;
  IF lp.license_risk_level = 4 AND NEW.storage_partition <> 'blocked' THEN
    RAISE EXCEPTION 'isolamento de licenca (Art.11/P11): NC-como-expressao deve ser blocked';
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_media_isolation
  BEFORE INSERT OR UPDATE ON core.media_asset
  FOR EACH ROW EXECUTE FUNCTION core.f_enforce_media_isolation();

-- ===== 03 — derivados ([N2]: nunca verdade; nunca em entity_node) =====
-- derived_cache NÃO referencia entity_node e NÃO pode carregar proveniência.
-- (T7: aceita carries_provenance=false; rejeita carries_provenance=true; 0 FKs p/ entity_node.)
CREATE TABLE derived.derived_cache (
  id                 TEXT PRIMARY KEY,
  cache_kind         TEXT NOT NULL,     -- MomentResult|Scene|MatchSet|index|...
  input_version_set  TEXT,              -- de quais versões autoritativas derivou
  payload            JSONB,
  carries_provenance BOOLEAN NOT NULL DEFAULT false,
  CONSTRAINT n2_derived_carries_no_provenance CHECK (carries_provenance = false)
);

-- ===== 04 — IsolatedLicenseStore (schema iso) + REVOKE (T6) =====
-- Espelho mínimo para conteúdo SA/ODbL/NC, fisicamente separado. O núcleo
-- NÃO tem caminho de leitura daqui para compor Claim. kc_service é barrado.
CREATE TABLE iso.media_asset_isolated (
  id                 TEXT PRIMARY KEY,
  nature_label       TEXT NOT NULL,
  license_label      TEXT NOT NULL,
  share_alike        BOOLEAN NOT NULL DEFAULT true,
  attribution_text   TEXT NOT NULL,
  storage_uri        TEXT
);

-- Permissões: kc_service lê o núcleo, NUNCA o store isolado.
GRANT USAGE ON SCHEMA core TO kc_service;
GRANT SELECT ON ALL TABLES IN SCHEMA core TO kc_service;
ALTER DEFAULT PRIVILEGES IN SCHEMA core GRANT SELECT ON TABLES TO kc_service;
REVOKE ALL ON SCHEMA iso FROM kc_service;
REVOKE ALL ON ALL TABLES IN SCHEMA iso FROM kc_service;
ALTER DEFAULT PRIVILEGES IN SCHEMA iso REVOKE ALL ON TABLES FROM kc_service;

-- ===== 05 — VIEWS de exibição (portão Art.6 / §9) e f_simultaneidade base =====
-- v_displayable_curatorial: o que é FATO EXIBÍVEL (Art.6). approved + admitido.
-- Inclui seeded-demo APPROVED (com selo 'demonstração' na apresentação), mas
-- nunca pending/legal-review/rejected/blocked. (T3=23; T4: legal-review some.)
CREATE OR REPLACE VIEW core.v_displayable_curatorial AS
  SELECT *
  FROM core.knowledge_item
  WHERE review_status = 'approved'
    AND ingestion_decision <> 'blocked';

-- v_publishable_public: o que é PUBLICAMENTE PUBLICÁVEL (§9.2 F2 + Art.6).
-- approved ∩ corpus ∩ fonte-por-asset-confirmada. ZERO seeded-demo. (T5=11.)
CREATE OR REPLACE VIEW core.v_publishable_public AS
  SELECT *
  FROM core.knowledge_item
  WHERE review_status = 'approved'
    AND ingestion_decision <> 'blocked'
    AND provenance_status = 'corpus'
    AND per_asset_source_confirmed = true;

-- f_simultaneidade (BASE — herdada do A3): interseção temporal pura no eixo
-- canônico (3Z). [N4]: o índice ORDENA e SELECIONA; não decide verdade nem
-- publicabilidade — esses vêm reidratados do autoritativo (via as views, na
-- camada A4). Esta função base é deliberadamente "crua": opera sobre uma
-- relação-fonte qualquer informada pela camada A4, não sobre a tabela base.
-- (A camada gateada de leitura está em a4-leitura-simultaneidade.sql.)
CREATE OR REPLACE FUNCTION core.f_simultaneidade_base(
  p_scalar  DOUBLE PRECISION,
  p_lenses  TEXT[] DEFAULT NULL          -- NULL = todas as lentes
) RETURNS SETOF core.knowledge_item AS $$
  SELECT *
  FROM core.knowledge_item ki
  WHERE p_scalar BETWEEN ki.canonical_start AND ki.canonical_end
    AND (p_lenses IS NULL OR ki.domain = ANY(p_lenses))
  ORDER BY ki.canonical_scalar, ki.id;
$$ LANGUAGE sql STABLE;

-- Nota: f_simultaneidade_base atravessa a TABELA (curadoria/depuração). A
-- consulta PÚBLICA/CURATORIAL gateada (Art.6/§9) é construída na camada A4,
-- que intersecta as VIEWS — garantindo que não-fato nunca vaze como fato.
