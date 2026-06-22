# Passo B2 — Reificação de Source / Claim / MediaAsset

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** decisão de modelagem de dados (Trilha B do `estado-atual-e-roteiro`). Promove `Source`/`Claim`/`MediaAsset` de **tabelas reservadas / objetos de valor** (B1 §4.4) a **tipos de primeira classe, endereçáveis e reificáveis**. Fecha a pendência **F4** (P08 reificar `Source`, P09 reificar `MediaAsset`, P11 isolamento físico SA/ODbL). Cadência de handoff dos 4Z/5Z.
**Status:** entrega do Passo B2, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), o datum temporal (Etapa 3Z), a política editorial (Etapa 3.1), a arquitetura técnica (Etapa 11), o pipeline de ingestão (Etapa 13), o recorte do MVP (Etapa 12) e a **decisão de motor do Passo B1** (relacional + JSONB + PostGIS, esquema portável a grafo).
**Data:** revisão atual.

> **Nota de proveniência deste documento.** Esta é a **reconstituição fiel** do handoff do Passo B2, originalmente produzido no chat de autoria *"Esclarecimentos sobre pendência F4 e políticas P1/P2/P7"* e **já ratificado** na **Constituição v1.1** (Arts. 10/11/12, que citam por número D-B2.2, D-B2.4 e D-B2.6) e referido no **Playbook v1.3** (precedente vivo). As decisões D-B2.1…D-B2.7 **não** são reabertas aqui: são as mesmas já vinculantes no corpus. Em qualquer divergência, a Constituição vence (régua do Art. 17 / regra de emenda do Art. 18).

**Limites (o que B2 NÃO faz):** não escreve código de aplicação; não cria banco real; não migra os dados do protótipo de fato (entrega o **esquema** e o ponto de imposição — a migração roda no A3, pelas Fases 1–6 do B1 §6); não escolhe produto/versão final de PostgreSQL/PostGIS; não desenha UX; não popula o Knowledge Core; não reabre a auditoria de fontes (1/1.1) nem a política editorial (3.1); não reabre a decisão de motor (B1) — herda-a; não refatora as camadas derivadas (elas permanecem **não-reificadas por projeto**, e isso é uma decisão de B2, não um esquecimento). É **notação de esquema (design)**, não implementação.

---

## 1. Objetivo

Promover os três tipos que o B1 deixou como **tabelas próprias reservadas** a **tipos de primeira classe**, no sentido forte de modelagem: entidades com **identidade estável**, **endereçáveis** por outras entidades, **versionáveis** e — o ponto central — **reificáveis**, isto é, capazes de serem **sujeitos** de novos enunciados (claims sobre claims, claims sobre fontes, claims sobre assets).

Entregar quatro artefatos:

1. **Padrão de reificação** — o mecanismo único pelo qual um enunciado se torna endereçável (registro de entidades endereçáveis, `entity_node`).
2. **Delta de esquema sobre o B1 §5.2** — os campos, FKs e *constraints* que promovem os três tipos e religam as referências polimórficas a FK real.
3. **Ponto de imposição do isolamento de licença** (P11) — onde o esquema força SA/ODbL ao `isolated-license-store` e bloqueia NC-como-expressão, sem caminho de leitura do núcleo para o store isolado.
4. **Regra de versionamento por depreciação** dos três tipos (E13 §9.7–§9.10), preservando a portabilidade a grafo do B1.

O invariante que governa B2 (Etapa 11 §4.2; B1 [N1]): **proveniência por aresta/claim é propriedade estrutural, não convenção.** B2 é exatamente o passo em que essa propriedade deixa de ser "coluna por convenção" e vira **FK a uma entidade real** — fechando o risco R-B1.1.

---

## 2. Escopo

**Dentro:**
- Promoção de `Source`, `Claim`, `MediaAsset` a **nós endereçáveis** de primeira classe.
- O **backbone de reificação**: `entity_node` (IRI interna estável) como única espinha pela qual algo pode ser sujeito de enunciado.
- Religação de `claim.subject_ref`, dos extremos de `relationship` e de `claim.provenance_ref` para **FK → `entity_node`** (mata a referência polimórfica por texto).
- Campos de primeira classe do `MediaAsset`: `natureLabel`, `licenseProfileRef`, `storagePartition`, `textualEquivalent`, `attributionText`, e as arestas `representa`/`evidencia` (P09).
- Imposição do isolamento físico de licença no esquema (P11; E11 §9.2/§9.7; E13 §8.11).
- Versionamento por depreciação dos três tipos (E13 §9.7/§9.8/§9.10).

**Fora (mantido como no B1 — apontam ao KC por REF, não viram nós reificáveis — E11 §4.3, [N2]/[N5]):**
- Índices, caches, `MomentResult`, `Scene`, `MatchSet` e demais **derivados** — explicitamente **não** são `entity_node` (preserva [N2]).
- Camada de conformidade BR, planejamento docente, matching, saída pedagógica, experiência — relacional externo, REF ao KC.
- A escolha de produto/versão e a implementação física — A3.

> **Separação obrigatória (item 12 do prompt-mestre):** B2 reifica somente o **núcleo factual autoritativo**. Conhecimento universal vira nó endereçável; conformidade/planejamento/matching/saída/experiência continuam leitores externos que apontam por REF, nunca sujeitos do grafo factual.

---

## 3. Diagnóstico

### 3.1 Por que reificar — o produto é claim-first e precisa de enunciados sobre enunciados

A unidade atômica de verdade é o `Claim` tipado e fonteado (Etapa 2, P4), não o parágrafo. Mas vários requisitos já firmados **exigem tratar o próprio claim/fonte/asset como sujeito**:

| Requisito do corpus | Por que exige reificação |
|---|---|
| `ClaimSet` com pesos e não-falsa-equivalência (Etapa 3.1; B1 Q6) | um `ClaimSet` é um enunciado **sobre** outros claims (as leituras concorrentes) — claim-sobre-claims |
| Depreciação sem apagar (E13 §9.8/§9.10) | "este claim foi substituído por aquele" é um enunciado **sobre** um claim |
| Corroboração/contestação entre fontes | "a fonte A corrobora B", "a fonte C é contestada" é um enunciado **sobre** fontes |
| `natureLabel` do asset (E2; E11 §4.7) | "este asset é uma reconstrução modelada de X" é um enunciado **sobre** o asset, não sobre o fato |
| `reviewStatus` auditável por item e versão (E13 §9.11) | o estado de revisão é predicado **do** item/claim, rastreável no tempo |

Sem reificação, esses enunciados viram texto solto ou colunas frágeis. Com reificação, são arestas e claims de primeira classe, auditáveis.

### 3.2 O que o B1 deixou aberto (e B2 fecha)

O B1 §5.2 já modelou `claim.subject_ref` como **referência polimórfica** ("item OU aresta a que o claim se refere"). Isso é uma reificação **latente, ainda não fechada**: o tipo de sujeito é livre, sem integridade referencial, e a proveniência por aresta é "coluna obrigatória + *constraint*" — exatamente o ponto que o risco **R-B1.1** sinaliza como "convenção frágil". A pendência **F4** (P08/P09/P11) é, em uma frase, *fechar esta reificação latente com integridade real e isolamento físico*.

### 3.3 Os invariantes que constrangem B2 (herdados)

- **[N1]** Toda aresta afirmativa e todo claim carregam `provenanceRef` + `reviewStatus`. B2 torna `provenanceRef` **FK a entidade real**, não convenção.
- **[N2]** Autoritativo nunca depende de derivado. B2 **não** reifica derivados; eles carregam `carriesProvenance = false`.
- **[N3]** Geometrias/assets SA/ODbL/NC não entram no índice/núcleo — vão para o `isolated-license-store`. B2 impõe isso no `MediaAsset`.
- **[N5]** Camadas externas apontam ao KC por REF; nenhuma vira sujeito do grafo factual.
- **Portabilidade (B1 D-B1.2):** o esquema permanece convertível a property graph / RDF* sem reescrita. B2 desenha o backbone justamente para isso.

---

## 4. Decisões principais

### 4.1 Decisão (D-B2.1) — Backbone de reificação: registro de entidades endereçáveis

**Adotar um registro único, `entity_node`, com IRI interna estável, como a espinha de toda reificação.** Tudo que pode ser **sujeito** de um enunciado registra-se nele: `item`, `relationship` (aresta), `claim`, `source`, `media_asset`, `claim_set`. Esse é o mecanismo que torna "enunciado sobre enunciado" trivial: um `claim` é um nó; outro `claim` pode referenciá-lo como sujeito; uma aresta pode ligar dois claims ou duas fontes.

**Por quê:** é o padrão de reificação mais limpo e o **mais portável** — `entity_node.uri` é a IRI no RDF* e o *node id* no property graph; um enunciado reificado migra como *named statement* (RDF*) ou aresta-com-propriedade (property graph), sem reestruturar nada (honra B1 D-B1.2).

### 4.2 Decisão (D-B2.2) — Promoção a primeira classe + FK real (fecha R-B1.1)

**Promover `Source`, `Claim`, `MediaAsset` a tipos de primeira classe**, cada um com identidade própria e linha de versão própria, e **religar** `claim.subject_ref`, os extremos de `relationship` e `claim.provenance_ref` para **FK → `entity_node(uri)`**. Com isso, a proveniência por aresta deixa de ser convenção e passa a ser **integridade referencial estrutural** — uma aresta afirmativa órfã de proveniência torna-se **impossível de inserir**, não apenas "rejeitada por trigger".

*(Ratificado na Constituição v1.1, Art. 10.)*

### 4.3 Decisão (D-B2.3) — `MediaAsset` de primeira classe com natureza e licença (P09)

**`MediaAsset` carrega como campos de primeira classe:** `natureLabel` (enum: `fotografia` | `mapa` | `gráfico` | `reconstrução-científica` | `simulação` | `representação-artística` | `aproximação-didática`), `licenseProfileRef`, `storagePartition`, `textualEquivalent` (equivalente textual / acessibilidade), `attributionText`. A relação asset↔fato é **aresta** (`representa` / `evidencia`), nunca embutida — separando *o asset* (governado pela licença) do *fato* (re-codificável). O `attributionText` **viaja com o asset** por exibição, cache, exportação e offline (E11 §9.9, invariante 17).

### 4.4 Decisão (D-B2.4) — Isolamento de licença imposto no esquema (P11)

**O esquema força a partição de armazenamento por licença** (E11 §9.2/§9.7; E13 §8.11):
- `shareAlikeRequired = true` (SA/ODbL — OSM, MapBiomas, ESA/Gaia, texto de Wikipedia) → `storagePartition = isolated-license-store`, **obrigatório**.
- NC-como-expressão (`licenseRiskLevel = 4`) → `storagePartition = blocked` (o asset não é servido; só o **fato re-derivado de fonte livre** entra, com fonte própria).
- O `KnowledgeCoreService` **não tem caminho de leitura** para o `isolated-license-store` ao compor `Claim`; quando exibido, o conteúdo isolado aparece como **camada ao lado** do núcleo, com atribuição, sem fusão.

**A reificação não cruza a fronteira de isolamento:** uma aresta reificada nunca funde um nó do núcleo com um nó do store isolado para compor fato.

*(Ratificado na Constituição v1.1, Art. 11 — "a licença governa a expressão/asset, nunca o fato recodificado".)*

### 4.5 Decisão (D-B2.5) — Reificação é limitada (preserva [N2])

**Apenas fatos autoritativos são sujeitos reificáveis.** Derivados — índice temporal/geoespacial, cache, `MomentResult`, `Scene`, `MatchSet` — **não** são `entity_node` e carregam `carriesProvenance = false`. O `entity_kind` é uma **lista fechada** de seis valores; nada fora dela vira nó. Isso impede que "cache vire verdade" ou que "busca/embedding vire fonte" por porta dos fundos.

### 4.6 Decisão (D-B2.6) — Versionamento por depreciação dos três tipos

**Correção cria nova versão, deprecia a anterior, nunca apaga** (E13 §9.7/§9.8/§9.10):
- `Source` versiona ao mudar classificação A/B/C, licença ou identidade institucional (dispara revalidação de `LicenseStorageBinding` e invalidação de derivados).
- `Claim` versiona ao mudar `statement`, `claimType`, `confidence`, `evidenceLevel`, `UncertaintyProfile`, escopo temporal/espacial ou fonte; a versão anterior fica `deprecated`, preservada para auditoria do que foi exibido antes da correção.
- `MediaAsset` versiona ao mudar `natureLabel`, licença, `textualEquivalent` ou o binário.
- `entity_node.current_version_ref` aponta sempre à versão ativa; versões `deprecated` permanecem consultáveis pela auditoria, jamais exibíveis como fato atual.

*(Ratificado na Constituição v1.1, Art. 12 — `supersedes`; `DatasetSnapshot` imutável.)*

### 4.7 Decisão (D-B2.7) — Portabilidade preservada (não reabre B1)

O backbone `entity_node` é desenhado para que a migração a grafo (gatilhos G1/G2/G3 do B1) seja **conversão, não reescrita**: `uri`→IRI/node id; `claim`/`source`/`media_asset`→nós rotulados; `relationship`→arestas entre node ids; enunciado reificado→*named statement* (RDF*) / aresta anotada (property graph). B2 **não** reabre a decisão de classe de motor.

---

## 5. Modelo conceitual

> **Notação de projeto, não implementação.** O DDL abaixo é *esboço de esquema* (design), coerente com os limites de B1/B2/E11/E12. A implementação real (DDL real, banco real, *constraints* executáveis, índices) pertence ao A3.

### 5.1 Delta de esquema sobre o B1 §5.2 (entregável 2)

```sql
-- ===== BACKBONE DE REIFICAÇÃO (novo em B2) =====
entity_node (
  uri                 TEXT PK,             -- IRI interna estável; única identidade endereçável
  entity_kind         TEXT NOT NULL,       -- LISTA FECHADA: item|relationship|claim|source|media_asset|claim_set  [D-B2.5]
  current_version_ref TEXT,                -- aponta à versão ATIVA (depreciação-não-apaga)  [D-B2.6]
  created_at          TIMESTAMPTZ NOT NULL
)
-- INVARIANTE [D-B2.5]: nenhum derivado (índice/cache/MomentResult/Scene/MatchSet) registra-se aqui.
-- INVARIANTE [D-B2.1]: toda linha de item/relationship/claim/source/media_asset/claim_set TEM um entity_node.

-- ===== KNOWLEDGE_ITEM / RELATIONSHIP (B1, agora com FK ao backbone) =====
-- knowledge_item.id  ->  também registrado em entity_node (entity_kind='item')
relationship (
  id            TEXT PK,                   -- também em entity_node (entity_kind='relationship') -> aresta é reificável
  src_ref       TEXT NOT NULL FK->entity_node(uri),   -- [B2] FK real, não texto: liga QUALQUER nó endereçável
  dst_ref       TEXT NOT NULL FK->entity_node(uri),
  relation_type TEXT NOT NULL,             -- vocab Etapa 2 (4B)
  is_affirmative BOOLEAN NOT NULL,         -- causou|influenciou|afetou = TRUE
  provenance_ref TEXT FK->provenance_metadata,  -- [N1] OBRIGATÓRIO se is_affirmative=TRUE (constraint)
  review_status  TEXT NOT NULL             -- [N1]
)
-- CONSTRAINT [N1]/R-B1.1 fechado: is_affirmative=TRUE EXIGE provenance_ref NOT NULL (FK válida). Sem isso, INSERT falha.

-- ===== SOURCE  (promovida a primeira classe — P08) =====
source (
  id            TEXT PK,                   -- também em entity_node (entity_kind='source') -> fonte é sujeito reificável
  title         TEXT, source_type TEXT, authority_tier TEXT,   -- A/B/C
  license       TEXT, uri TEXT, retrieved_at TIMESTAMPTZ
)
source_version ( id TEXT PK, source_id TEXT FK->source, version TEXT, authority_tier TEXT, license TEXT,
                 dataset_snapshot TEXT, status TEXT,   -- active|deprecated  [D-B2.6]
                 changed_reason TEXT, created_at TIMESTAMPTZ )

citation ( id TEXT PK, source_id TEXT FK->source, snapshot_ref TEXT, locator TEXT, quote_excerpt TEXT )
provenance_metadata ( id TEXT PK, source_id TEXT FK->source, dataset_snapshot TEXT, method TEXT,
                      scale_version TEXT, created_by TEXT, created_at TIMESTAMPTZ )

-- ===== CLAIM / CLAIMSET  (promovidos a primeira classe; subject_ref agora FK real) =====
claim (
  id            TEXT PK,                   -- também em entity_node (entity_kind='claim') -> claim é sujeito reificável
  subject_ref   TEXT NOT NULL FK->entity_node(uri),  -- [B2] FK real: item, aresta, source, media_asset OU outro claim
  statement     TEXT NOT NULL,
  claim_type    TEXT NOT NULL,   -- fato-documentado|interpretação|inferência-científica|proxy|reconstrução-modelada|estimativa|hipótese
  evidence_level TEXT,           -- inclui tradição/registro-oral (vocab 4B)
  confidence    TEXT NOT NULL,
  review_status TEXT NOT NULL,                          -- [N1]
  provenance_ref TEXT NOT NULL FK->provenance_metadata  -- [N1] OBRIGATÓRIO
)
claim_version ( id TEXT PK, claim_id TEXT FK->claim, version TEXT, statement TEXT, claim_type TEXT,
                confidence TEXT, evidence_level TEXT, uncertainty_profile TEXT,
                status TEXT,   -- active|deprecated  [D-B2.6]
                changed_reason TEXT, created_at TIMESTAMPTZ )

claim_set (
  id            TEXT PK,                   -- também em entity_node (entity_kind='claim_set') -> claim_set é sujeito reificável
  subject_ref   TEXT NOT NULL FK->entity_node(uri),
  resolution    TEXT NOT NULL    -- regra de não-falsa-equivalência (pesos das leituras concorrentes)  [Q6]
)
claim_set_member ( claim_set_id TEXT FK->claim_set, claim_id TEXT FK->claim, weight NUMERIC, stance TEXT )
-- ex.: k-pg-causa: impacto=central, Deccan=contribuinte ; negacionismo NUNCA é membro (fica em objeto rotulado-rejeitado, E3.1)

-- ===== MEDIA_ASSET  (promovido a primeira classe — P09; natureza + licença + partição) =====
media_asset (
  id              TEXT PK,                 -- também em entity_node (entity_kind='media_asset') -> asset é sujeito reificável
  nature_label    TEXT NOT NULL,   -- fotografia|mapa|gráfico|reconstrução-científica|simulação|representação-artística|aproximação-didática  [D-B2.3]
  license_profile_ref TEXT NOT NULL FK->license_profile,  -- licença POR ASSET  [D-B2.3]
  storage_partition   TEXT NOT NULL,  -- media-store|isolated-license-store|blocked  [D-B2.4/P11]
  textual_equivalent  TEXT,            -- acessibilidade (mesma info + rótulos epistêmicos)
  attribution_text    TEXT,            -- viaja com o asset por exibição/cache/export/offline (E11 §9.9, inv.17)
  storage_uri     TEXT
)
-- A relação asset<->fato é ARESTA (relationship: representa | evidencia), NUNCA embutida —
--   separa o ASSET (governado pela licença) do FATO (recodificável).  [D-B2.3]
-- CHECK [D-B2.4/P11]: shareAlikeRequired => storage_partition='isolated-license-store';
--                     NC-como-expressão  => storage_partition='blocked'.
-- INVARIANTE: nenhum caminho de leitura do núcleo ao isolated-license-store para compor Claim (E11 §9.2; E13 §8.11).

-- ===== DERIVADOS (NÃO reificáveis — D-B2.5 / [N2]) =====
-- índice temporal/geoespacial, cache, MomentResult, Scene, MatchSet: carries_provenance = FALSE; nunca em entity_node.
```

### 5.2 Reificação em ação (três exemplos *worked*)

1. **`ClaimSet` da leitura causal de 1789.** Um nó `claim_set` cujo `subject_ref` é o `item` "Revolução Francesa"; seus `claim_set_member` apontam a dois `claim` concorrentes (leitura social × leitura política), cada um com peso e *stance*, cada um com `provenance_ref` próprio. O `resolution` codifica a não-falsa-equivalência. → *claim-sobre-claims*, endereçável e auditável.
2. **Contestação de fonte.** Um `claim` cujo `subject_ref` é um nó `source` X, com `statement` = "fonte contestada por revisão historiográfica Y", `claim_type` = `interpretação`, `provenance_ref` → fonte Y. → *claim-sobre-fonte*.
3. **Natureza de asset.** Um `media_asset` com `nature_label = reconstrução-científica` (paleogeografia EarthByte de Pangeia), `license_profile_ref` = CC BY, ligado por aresta `representa` ao `item` "Pangeia"; e um `claim` cujo `subject_ref` é esse asset registra "esta imagem é reconstrução modelada, não fotografia". → *enunciado sobre o asset*, separado do fato.

### 5.3 Mapa de portabilidade (herda B1 §5.3)

| Construto B2 (relacional) | Property graph | RDF* / triplestore |
|---|---|---|
| `entity_node.uri` | *node id* | IRI do recurso |
| `claim`/`source`/`media_asset` (nó) | nó rotulado | recurso tipado |
| `relationship` (aresta reificável) | aresta com propriedades | *statement* |
| enunciado reificado (claim cujo `subject_ref` é outro claim/aresta) | aresta→nó-aresta / nó de enunciado | **RDF\* annotation** (*statement-level*, nativo) |
| `provenance_ref` (FK) | propriedade de aresta | propriedade *statement-level* |

A migração é **conversão**, não reescrita (gatilhos G1/G2/G3 do B1). Nota honesta: RDF* faz reificação *statement-level* nativamente — se o gatilho G2 (interop SPARQL) disparar, este backbone é o que torna a conversão direta.

---

## 6. Fontes / insumos necessários

B2 é infraestrutura, não conteúdo — consome **artefatos do corpus**, não fontes externas de dados:
- **Etapa 2** (Knowledge Core): família F (`ProvenanceMetadata`, `LicenseProfile`, `ReviewStatus`, `DatasetSnapshot`, `MediaAsset`/`MapAsset`), princípios P3/P4/P8/P10, vocabulário (4B).
- **Etapa 3.1** (editorial): regra de `ClaimSet`/não-falsa-equivalência; rótulo de rejeição **fora** do `ClaimSet` (negacionismo nunca é "lado"); §7 (mídia: `natureLabel` e licença por asset).
- **Etapa 11**: [N1]–[N5]; invariantes 17–19/27 (licença/atribuição/exportação); isolamento §9.2/§9.7; natureza de mídia §4.7.
- **Etapa 13**: §8 (roteamento de armazenamento: media-store / isolated-license-store / blocked / FATO); §9 (snapshots e versionamento §9.7–§9.11).
- **Passo B1 §5.2**: as tabelas reservadas que B2 promove; §5.3 (portabilidade); R-B1.1 (o risco que B2 fecha); D-B1.4 (a "mesa posta").
- **Para o A3/implementação (fora de B2):** produto/versão de PostgreSQL/PostGIS, *constraints*/triggers executáveis, índices, o `isolated-license-store` físico real, e a execução das Fases 1–6 do B1 §6 sobre o esquema reificado.

---

## 7. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| R-B2.1 | Reificação **vazar** para derivados (cache/índice viram "sujeito" e logo "verdade") | `entity_kind` é **lista fechada** de 6 valores; derivados com `carriesProvenance=false`; nunca em `entity_node` (D-B2.5/[N2]) |
| R-B2.2 | Integridade da referência polimórfica frágil (subject por texto) | `subject_ref`/`provenance_ref`/extremos de aresta = **FK a `entity_node`/`provenance_metadata`**, não texto livre (D-B2.2) |
| R-B2.3 | Aresta reificada **furar o isolamento** (fundir núcleo com store SA/ODbL/NC) | CHECK de `storage_partition` + ausência de caminho de leitura do núcleo ao `isolated-license-store` (D-B2.4/P11; E13 §8.11) |
| R-B2.4 | **Proliferação de versões** sem versão ativa clara | `entity_node.current_version_ref` é a única fonte da versão ativa; `deprecated` consultável, nunca exibível (D-B2.6) |
| R-B2.5 | **Sobre-engenharia** (reificação universal vira complexidade gratuita) | Reificação **limitada** a 6 tipos de nó; derivados explicitamente fora; backbone único, não um por tipo |
| R-B2.6 | Re-litigar a decisão de motor (parecer que reificação "pede" triplestore) | Portabilidade preservada (D-B2.7/B1 D-B1.2); gatilhos G1/G2/G3 inalterados; B2 não reabre a classe de motor |
| R-B2.7 | `natureLabel`/atribuição **perdidos** em exportação/offline/"limpeza de tela" | `attributionText`+`natureLabel` viajam com o asset por todo caminho (E11 §9.9, inv.17); exportação revalida licença (E13 §8.12) |

---

## 8. Entregáveis

1. **Decisão de padrão de reificação:** `entity_node` (registro de entidades endereçáveis, IRI estável) como backbone único — §4.1.
2. **Delta de esquema** sobre o B1 §5.2, com FK real religando proveniência/sujeito e promovendo os três tipos — §5.1.
3. **Ponto de imposição do isolamento de licença** (P11): partição forçada por licença + ausência de caminho de leitura ao store isolado — §4.4 e §5.1.
4. **Regra de versionamento por depreciação** dos três tipos, com `current_version_ref` — §4.6.
5. **Fechamento da F4:** P08 (`Source` reificada) ✅, P09 (`MediaAsset` com `natureLabel`/licença reificado) ✅, P11 (isolamento SA/ODbL imposto no esquema) ✅ — restando **somente a execução física** (A3).
6. **Mapa de portabilidade** atualizado (relacional → property graph → RDF\*), preservando a migração-conversão do B1 — §5.3.

---

## 9. Próximos passos

- **A3 — Produção 3D / implementação (Claude Code):** implementa o esquema reificado de fato (DDL real, `entity_node` + tabelas, *constraints*/triggers, índices), cria o `isolated-license-store` físico, e roda as **Fases 1–6 do B1 §6** de migração do protótipo **sobre as tabelas reificadas** (a "mesa posta" do B1 §4.4, agora montada).
- **C2 — Fila de revisão como processo** (F1): quando for ao público; a reificação já dá o `reviewStatus` por item/versão auditável de que a fila precisa. *(Nota: na linha do tempo do projeto, C2 e C3 já foram executados após B2 — ver Playbook v1.2/v1.3; este item registra o acoplamento, não uma pendência aberta.)*
- **B1 §6 (migração):** reenviar os `.html` do protótipo na execução; reconciliar corpus × `seeded-demo` (itens de 1789 multidomínio são `seeded-demo`, não corpus — pendências F1/F2).
- **Coerência:** toda lacuna protótipo×corpus surgida na migração vira tarefa de modelagem registrada (regra anti-divergência do `estado-atual-e-roteiro`).

---

*Documento de entrega do Passo B2 (reconstituição fiel), sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o pipeline de ingestão (Etapa 13), o recorte do MVP (Etapa 12) e a decisão de motor do Passo B1. Promove `Source`/`Claim`/`MediaAsset` a tipos de primeira classe via um backbone único de entidades endereçáveis (`entity_node`), religa a proveniência por aresta de convenção a FK real (fechando R-B1.1), impõe o isolamento físico de licença no esquema (P11) e fixa o versionamento por depreciação — fechando a pendência F4 (P08/P09/P11) no nível de design. As decisões D-B2.1…D-B2.7 já estão ratificadas na Constituição v1.1 (Arts. 10/11/12) e referidas no Playbook v1.3; este documento as reconstitui sem reabri-las. Não escreve código de aplicação, não cria banco real, não migra dados de fato, não escolhe produto/versão final, não desenha UX, não popula o Knowledge Core, não reabre auditoria de fontes nem política editorial e não reabre a decisão de motor (herda-a). Próximo passo na Trilha B: a execução física pertence ao A3.*
