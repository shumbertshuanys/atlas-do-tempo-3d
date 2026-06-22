# Passo B1 — Decisão do motor de banco

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** decisão de fundação de dados (Trilha B do `estado-atual-e-roteiro`). Resolve a `[PENDÊNCIA]` E11 §4 → E12 (escolha RDF* × property graph × relacional), agora **com os padrões reais de consulta do protótipo como evidência** (governança P3). Cadência de handoff dos 4Z/5Z.
**Status:** entrega do Passo B1, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a arquitetura técnica (Etapa 11), o recorte do MVP (Etapa 12), o datum temporal (Etapa 3Z) e a *Decisão de re-centragem da tese*.
**Data:** revisão atual.

**Limites (o que B1 NÃO faz):** não escreve código de aplicação; não cria banco real; não migra dados de fato (entrega o **plano**); não escolhe produto/versão final de biblioteca; não desenha UX; não popula o Knowledge Core; não reabre auditoria de fontes (1/1.1) nem política editorial (3.1); não decide reificação física (isso é o B2). A escolha de **classe de motor** é o objeto; a escolha de **produto específico** e a implementação pertencem ao A3/implementação.

---

## 1. Objetivo

Decidir a **classe de motor de banco** que sustentará o Knowledge Core como fundação durável (deixando de ser protótipo descartável), preservando os invariantes da Etapa 11, e entregar três artefatos:

1. **Comparativo** fundamentado — RDF*/triplestore × property graph × relacional — pesado pelos padrões de consulta que o protótipo de fato exerce.
2. **Esquema mínimo do grafo** — os tipos, arestas, campos e *constraints* vinculantes do núcleo factual.
3. **Plano de migração** dos dados do protótipo (um *graph-seed* claim-first) para o motor escolhido, reconciliando protótipo × corpus.

O invariante que governa a decisão (Etapa 11 §4.2): **"grafo tipado com proveniência por aresta" é a propriedade vinculante, não a tecnologia.** B1 escolhe a tecnologia que melhor sustenta essa propriedade *para os padrões de acesso reais deste produto* — sem ideologia de "knowledge graph ⇒ graph database".

---

## 2. Escopo

**Dentro:**
- O **núcleo factual autoritativo** (KC): `KnowledgeItem` e subtipos, `Claim`/`ClaimSet`, `Relationship`, `Source`/`Citation`/`ProvenanceMetadata`, `MediaAsset`, e os índices de primeira classe (temporal canônico, geoespacial).
- A separação **autoritativo × derivado** (índices/caches/`MomentResult`/`MatchSet`) como propriedade estrutural.
- O lugar físico do **`IsolatedLicenseStore`** (geometrias SA/ODbL e assets NC), mesmo vazio.

**Fora (apontam ao KC por REF, não entram no grafo factual — Etapa 11 §4.3):**
- Camada de conformidade BR (`ComplianceProfile`/`BNCCMapping`…) — vive em relacional externo.
- Planejamento do professor (`PlanningProfile`) — relacional/efêmero, descartável.
- Content Matching Engine (`MatchSet`/`MatchScore`) — derivado de planejamento × KC.
- Saída pedagógica (`PedagogicalOutput`) — relacional/documental versionado.
- Experiência (`ExperienceSession`/`NavigationState`) — efêmero, minimizado.

> **Separação obrigatória (item 12 do prompt-mestre):** o **conhecimento universal** vive no núcleo factual decidido aqui; **conformidade BR**, **planejamento**, **matching**, **saída pedagógica** e **experiência** são leitores/anotadores externos que apontam ao núcleo por REF. B1 decide só o motor do **núcleo** (e qual motor hospeda as camadas externas), nunca funde os dois.

---

## 3. Diagnóstico

### 3.1 A evidência que faltava: o que o protótipo prova sobre os padrões de consulta

A decisão estava diferida (E11→E12) à espera de "padrões reais de consulta como evidência". O protótipo agora os fornece. Os padrões dominantes são:

| # | Padrão de consulta (do protótipo) | Forma técnica | Profundidade |
|---|---|---|---|
| Q1 | **Recorte temporal** ("tudo entre t₁ e t₂") | intervalo 1D sobre `canonicalTimeScalar` | índice B-tree |
| Q2 | **Simultaneidade** ("o que era contemporâneo de X") | sobreposição de `[canonicalStart, canonicalEnd]` | interseção 1D, **não** travessia |
| Q3 | **Lente de domínio** ("dos itens nesta janela, quais do domínio D") | filtro por atributo `domain`/camada, combinado a Q1 | índice composto |
| Q4 | **Recorte espacial** ("o que está nesta região") | índice geoespacial (PostGIS-classe), combinado a Q1/Q3 | GIST |
| Q5 | **Dossiê de evento** (item + claims + relações de saída agrupadas por tipo + assets) | travessia **1–2 hops**, fan-out limitado | rasa |
| Q6 | **ClaimSet** (leituras concorrentes com pesos; não-falsa-equivalência) | leitura de subgrafo pequeno e limitado | rasa |
| Q7 | **Reidratação de gating** (todo read reidrata `claimType`/`confidence`/`reviewStatus` do autoritativo) | *join*/lookup obrigatório por item | constante |

**Leitura crítica:** o "grafo" deste produto é **largo e raso**, não profundo. As consultas que matam (Q1–Q4) são **intervalo temporal + filtro de atributo + geoespacial**; as travessias (Q5–Q6) são de 1–2 saltos com leque limitado. **Pathfinding de comprimento variável** — onde um banco de grafo dedicado brilha — **não é um padrão dominante aqui.** A simultaneidade (Q2), que poderia parecer travessia, é na verdade interseção temporal: a Etapa 2 §6.3 já estabelece que `contemporâneo-de` é *derivado* da interseção, com o grafo apenas **materializando seletivamente** as conexões mais relevantes (contexto curado, não lista bruta).

### 3.2 Os invariantes que constrangem qualquer escolha (Etapa 11)

Qualquer motor escolhido deve sustentar, como **propriedade estrutural** (não promessa):

- **[N1]** Toda aresta afirmativa (`causou`, `influenciou`, `afetou`) e todo claim carregam `provenanceRef` + `reviewStatus`. Aresta afirmativa sem fonte A/B + `claimType` + confiança é **rejeitada** (Etapa 2 §6.4).
- **[N2]** Autoritativo nunca depende de derivado para existir. Reconstruir todo índice/cache a partir do autoritativo é sempre possível; o caminho inverso é **proibido**. ("Cache não é verdade"; "busca/embedding não é verdade".)
- **[N3]** Geometrias SA/ODbL (OSM/MapBiomas) **não** entram no índice geoespacial junto ao núcleo — vão para o `IsolatedLicenseStore` físico. Paleoposições são **sempre** rotuladas como reconstrução modelada.
- **[N4]** O índice temporal **ordena e seleciona**; não decide confiança nem publicabilidade — esses vêm reidratados do autoritativo (Q7).
- **[N5]** Camadas externas (Compliance/Planning/Match/Output/Experience) **apontam** ao KC por REF; nenhuma é gravada dentro do grafo factual.

### 3.3 O precedente da Etapa 12 (que B1 refina, não contradiz)

A Etapa 12 (MVP), forçada a escolher um recorte mínimo, já **inclinou** para: **tabelas de aresta + JSONB no PostgreSQL**, com `provenanceRef` obrigatório por aresta, + **PostGIS** (geoespacial) + B-tree sobre `canonicalTimeScalar` + full-text (`tsvector`) devolvendo ponteiros, com migração a grafo dedicado "quando a travessia pesar (E13/E14)". B1 não tem evidência que contrarie essa inclinação — tem evidência (§3.1) que a **confirma e a fundamenta** como decisão de fundação, não só de MVP.

---

## 4. Decisões principais

### 4.1 Decisão (D-B1.1) — Motor do núcleo

**Adotar a classe RELACIONAL + JSONB + PostGIS (PostgreSQL-classe) como motor do núcleo factual**, com o invariante "grafo tipado com proveniência por aresta" **imposto no esquema e na aplicação**, e com o **esquema desenhado para ser portável a grafo** (RDF*/property graph) caso travessia profunda ou interoperabilidade semântica venham a se justificar por evidência.

**Por quê (evidência, não ideologia):**
- Os padrões reais (§3.1) são intervalo temporal + filtro + geoespacial + travessia rasa — exatamente o ponto forte de relacional+PostGIS, e exatamente onde um grafo dedicado seria sobre-engenharia.
- O produto precisa de geoespacial **e** temporal de primeira classe sobre 13,8 bilhões de anos **e** geometrias modernas. PostGIS é classe-líder em geoespacial; B-tree sobre o escalar canônico é trivial e rápido. Property graph e RDF* são mais fracos nisso e **forçariam um arranjo poliglota** (grafo + PostGIS), dobrando o custo operacional — algo que um MVP enxuto com time pequeno não pode pagar.
- O invariante [N1] é uma **propriedade exigível em relacional** (proveniência como coluna/aresta obrigatória + *constraint*), não um mandato por motor de grafo.
- Mantém **coerência com a Etapa 12** em vez de criar uma bifurcação MVP × fundação.

**O que NÃO se está afirmando:** *não* é "relacional venceu grafo no mérito para sempre". É: *a evidência de consulta + economia de motor único + maturidade operacional favorecem relacional agora, e o esquema é projetado para portar a RDF*/property graph se a travessia/interop ganhar o seu sustento.*

### 4.2 Decisão (D-B1.2) — Gatilho de migração (anti-lock-in)

Migrar (total ou parcialmente) o **núcleo** para grafo dedicado **somente quando medido**, não por antecipação. Gatilhos:
- **G1 — Travessia:** consultas de dossiê/relação passarem a exigir profundidade > 2 hops com leque alto, e o desempenho relacional (R-33) degradar de forma medida.
- **G2 — Interop semântica:** surgir requisito real de publicar/consumir SPARQL, vocabulários RDF padronizados, ou *linked data* externo.
- **G3 — Volume de arestas afirmativas** com travessia recorrente tornar o *join* o gargalo dominante em produção.
Até lá, o esquema portável (§5.3) garante que a migração é **conversão**, não reescrita.

### 4.3 Decisão (D-B1.3) — Motores das camadas externas

- **Relacional (mesmo PostgreSQL-classe, esquemas separados)** para Compliance/Planning/Matching/Output/Experience/identidade — apontando ao KC por REF ([N5]).
- **`IsolatedLicenseStore`** como *schema*/*bucket* **fisicamente separado** desde já (mesmo vazio): geometrias SA/ODbL e assets NC nunca tocam o núcleo ([N3]).
- **Object storage + CDN** para binários (mídia/tiles/3D livres); assets de risco isolados ou bloqueados.
- **Busca textual** = full-text do PostgreSQL devolvendo **ponteiros** (reidrata rótulos); **busca vetorial fica fora** por ora (risco de virar "fonte" — `carriesProvenance=false` se um dia adotada).
- **Cache** (`MomentResult`/`Scene`) em processo/Redis-classe com `inputVersionSet`; cache nunca serve item revogado ([N2]).

### 4.4 Decisão (D-B1.4) — Entrega para o B2

O esquema de §5 já reserva `Source`/`Claim`/`MediaAsset` como **tabelas próprias** (não embutidas), deixando a mesa posta para o **B2 (reificação)** promovê-las a tipos de primeira classe sem reestruturar o núcleo.

---

## 5. Modelo conceitual

> **Notação de projeto, não implementação.** O DDL abaixo é *esboço de esquema* (design), não código de aplicação nem criação de banco real — coerente com os limites de B1/E11/E12. A implementação real pertence ao A3.

### 5.1 Comparativo das três classes (entregável 1)

Peso: ● forte · ◐ médio · ○ fraco — **para os padrões deste produto** (§3.1), não em abstrato.

| Critério | Relacional + JSONB + PostGIS | Property graph | RDF* / triplestore |
|---|---|---|---|
| Proveniência por aresta/claim ([N1]) | ◐ coluna/aresta obrigatória + *constraint* | ● propriedade de aresta nativa | ● *statement-level* nativo (RDF* é feito p/ isso) |
| Consulta temporal Q1 (range em escalar) | ● B-tree | ◐ requer modelagem | ◐ requer modelagem |
| Geoespacial Q4 (PostGIS-classe) | ● classe-líder | ○ fraco/externo | ○ fraco/externo |
| Simultaneidade Q2 (interseção temporal) | ● índice resolve | ◐ não é o forte | ◐ não é o forte |
| Dossiê Q5 (1–2 hops) | ● *join* barato em profundidade rasa | ● ergonômico | ● ergonômico |
| Travessia profunda / pathfinding variável | ○ custoso (mas **não exigido**, §3.1) | ● o ponto forte | ◐ bom |
| Camadas externas no mesmo motor ([N5]) | ● relacional já as hospeda | ○ forçaria poliglota | ○ forçaria poliglota |
| Isolamento de licença ([N3]) | ● *schema*/bucket separado trivial | ◐ possível | ◐ possível |
| Maturidade operacional / time pequeno | ● altíssima | ◐ média | ◐ média (talento SPARQL escasso) |
| Custo de poliglota (geoespacial obrigatório) | ● um motor cobre tudo | ○ grafo + PostGIS | ○ triplestore + PostGIS |
| Interop semântica / padrões (SPARQL) | ○ não nativo | ◐ parcial | ● nativo |
| Curva de aprendizado | ● baixa | ◐ média | ○ alta |
| **Veredito p/ este produto agora** | **● Recomendado** | ◐ reserva (gatilho G1) | ◐ reserva (gatilho G2) |

**Síntese honesta dos trade-offs:** RDF* tem a proveniência *statement-level* mais elegante para claim-first (sua força real); property graph tem a travessia de aresta-com-propriedade mais ergonômica (sua força real). A decisão vira em três pontos: (a) o produto exige temporal+geoespacial de primeira classe, que relacional+PostGIS faz melhor e os outros forçam a poliglota; (b) as travessias do protótipo são rasas; (c) MVP enxuto + time pequeno não pagam ops poliglota nem talento escasso. O invariante é "grafo com proveniência por aresta" — *propriedade*, não *engine*.

### 5.2 Esquema mínimo do grafo (entregável 2)

Núcleo factual autoritativo. Campos temporais herdam **integralmente** o `TimeRange` da Etapa 3Z (`T0 = 2000.0 CE ≈ J2000`).

```sql
-- ===== TEMPO CANÔNICO (Etapa 3Z) — embutido como colunas reutilizáveis =====
-- canonical_time_scalar : anos rel. a T0=2000.0 CE; negativo=passado  (índice B-tree)  [Q1/Q2]
-- canonical_start, canonical_end : limites do intervalo no eixo canônico
-- source_time_basis     : datum nativo  (BP1950|calBP|radiocarbonBP|J2000|gregorianCE|ISO8601|Ma|Ga|scenarioYear)  [NUNCA apagado]
-- display_time          : string de exibição por regime  ("~13,8 Ga"; "1789"; "20 jul 1969")
-- time_precision        : Ga|Ma|ka|século|década|ano|mês|dia|cenário
-- time_uncertainty      : ± / faixa / distribuição
-- temporal_confidence   : alta|média-alta|média|média-baixa|baixa
-- conversion_method, conversion_notes : como a fonte virou canônico + ressalvas

-- ===== ITEM (KnowledgeItem + subtipos via type + JSONB) =====
knowledge_item (
  id              TEXT PK,
  item_type       TEXT NOT NULL,   -- Event|Process|Concept|Place|Region|Entity|Species|Civilization|Technology|Biome|<State>
  label           TEXT NOT NULL,
  description      TEXT,
  domain          TEXT[],          -- lentes (história|química|física|geologia|vida|clima…)  [Q3]
  canonical_time_scalar  DOUBLE PRECISION,   -- [Q1/Q2]
  canonical_start DOUBLE PRECISION,
  canonical_end   DOUBLE PRECISION,
  source_time_basis  TEXT,  display_time TEXT,  time_precision TEXT,
  time_uncertainty   TEXT,  temporal_confidence TEXT,
  conversion_method  TEXT,  conversion_notes TEXT,
  geometry_ref    TEXT,             -- FK -> geometry_version (geoespacial)  [Q4]
  review_status   TEXT NOT NULL,    -- pending|legal-review|approved   [N1/N4/Q7]
  provenance_status TEXT NOT NULL,  -- corpus|seeded-demo   [reconciliação protótipo×corpus, §6]
  subtype_attrs   JSONB             -- campos específicos do subtipo (State, Species, etc.)
)
-- Índices: B-tree(canonical_time_scalar); B-tree(canonical_start, canonical_end);
--          GIN(domain); GIN(subtype_attrs); FK(geometry_ref).

-- ===== FONTE / CITAÇÃO / PROVENIÊNCIA  (tabelas próprias -> prontas p/ B2) =====
source ( id TEXT PK, title TEXT, source_type TEXT, authority_tier TEXT, license TEXT, uri TEXT, retrieved_at TIMESTAMPTZ )
citation ( id TEXT PK, source_id TEXT FK->source, locator TEXT, quote_excerpt TEXT )
provenance_metadata ( id TEXT PK, source_id TEXT FK->source, dataset_snapshot TEXT, method TEXT, scale_version TEXT, created_by TEXT, created_at TIMESTAMPTZ )

-- ===== CLAIM / CLAIMSET  (tabelas próprias -> prontas p/ B2) =====
claim (
  id            TEXT PK,
  subject_ref   TEXT NOT NULL,   -- item OU aresta a que o claim se refere
  statement     TEXT NOT NULL,
  claim_type    TEXT NOT NULL,   -- fato-documentado|interpretação|inferência-científica|proxy|reconstrução-modelada|estimativa|hipótese
  evidence_level TEXT,           -- inclui tradição/registro-oral (vocab 4B)
  confidence    TEXT NOT NULL,
  review_status TEXT NOT NULL,   -- [N1]
  provenance_ref TEXT NOT NULL FK->provenance_metadata   -- [N1] OBRIGATÓRIO
)
claim_set (
  id            TEXT PK,
  subject_ref   TEXT NOT NULL,
  resolution    TEXT NOT NULL    -- regra de não-falsa-equivalência (pesos das leituras concorrentes)  [Q6]
)
claim_set_member ( claim_set_id TEXT FK, claim_id TEXT FK, weight NUMERIC, stance TEXT )  -- ex.: k-pg-causa: impacto=central, Deccan=contribuinte

-- ===== RELAÇÃO (aresta tipada) — o "grafo" =====
relationship (
  id            TEXT PK,
  from_id       TEXT NOT NULL FK->knowledge_item,
  to_id         TEXT NOT NULL FK->knowledge_item,
  relation_type TEXT NOT NULL,   -- causou|influenciou|afetou | ocorreu-durante|contemporâneo-de|… | parte-de|… | localizado-em | evidenciado-por|contradito-por|hipótese-concorrente|versão-historiográfica
  is_affirmative BOOLEAN NOT NULL,
  claim_type    TEXT,            -- exigido se is_affirmative
  confidence    TEXT,            -- exigido se is_affirmative
  review_status TEXT NOT NULL,
  provenance_ref TEXT FK->provenance_metadata,
  -- [N1] INVARIANTE (constraint/trigger):
  CHECK ( is_affirmative = FALSE
          OR (provenance_ref IS NOT NULL AND claim_type IS NOT NULL AND confidence IS NOT NULL) )
)
-- Índices: B-tree(from_id, relation_type); B-tree(to_id, relation_type)  [Q5]

-- ===== GEOMETRIA (índice geoespacial PostGIS) =====
geometry_version (
  id            TEXT PK,
  item_ref      TEXT FK->knowledge_item,
  kind          TEXT NOT NULL,   -- modern|historical|paleo
  geom          GEOMETRY,        -- GIST  [Q4]
  is_reconstruction BOOLEAN,     -- paleo => SEMPRE TRUE (rotulado reconstrução modelada) [N3]
  valid_from    DOUBLE PRECISION, valid_to DOUBLE PRECISION  -- no eixo canônico
)
-- modern_correspondence: ponte paleo/histórico -> território atual (lente Brasil, simultaneidade)

-- ===== MÍDIA (object storage por REF; natureLabel + licença) =====
media_asset (
  id            TEXT PK,
  item_ref      TEXT FK->knowledge_item,
  nature_label  TEXT NOT NULL,   -- fotografia|mapa|gráfico|reconstrução-científica|simulação|representação-artística|aproximação-didática
  license       TEXT NOT NULL,   -- por asset
  storage_uri   TEXT,            -- object storage/CDN; NC/proprietário -> isolated store
  isolated      BOOLEAN NOT NULL DEFAULT FALSE
)
```

**Como o esquema resolve cada padrão:** Q1/Q2 pelo índice B-tree no escalar; Q3 pelo GIN em `domain`; Q4 pelo GIST do PostGIS; Q5 pelos índices `(from_id, relation_type)`/`(to_id, relation_type)`; Q6 por `claim_set`/`claim_set_member` com pesos; Q7 porque `claim_type`/`confidence`/`review_status` vivem no autoritativo e são reidratados a cada leitura — o índice nunca os decide ([N4]).

**Simultaneidade (Q2) — implementação fiel à Etapa 2 §6.3:** o índice temporal calcula a interseção *bruta*; arestas `contemporâneo-de` armazenadas são apenas os **destaques curados** (contexto relevante), não a lista completa. Materialização seletiva, não exaustiva.

### 5.3 Portabilidade para grafo (garante a D-B1.2, anti-lock-in)

O mesmo modelo mapeia 1:1 para RDF*/property graph quando um gatilho disparar:

| Construto relacional | Property graph | RDF* / triplestore |
|---|---|---|
| `knowledge_item` (linha) | nó rotulado por `item_type` | recurso com `rdf:type` |
| `relationship` (linha) | aresta rotulada `relation_type` | *triple* (s, p, o) |
| `provenance_ref` na aresta afirmativa | propriedade de aresta | **anotação RDF* no *statement*** |
| `claim` / `claim_set` | nós `Claim`/`ClaimSet` + arestas | grafos nomeados / *statements* anotados |
| `canonical_time_scalar` | propriedade de nó | literal tipado |
| `geometry_version` (PostGIS) | propriedade + GeoSPARQL externo | GeoSPARQL |

Como proveniência e estado de revisão já são **atributos explícitos por aresta/claim** (não convenção implícita), a conversão preserva [N1]/[N2] sem remodelagem.

---

## 6. Plano de migração do protótipo (entregável 3)

O protótipo é um *graph-seed claim-first* embutido no HTML/JS. A migração **não é só ETL — é a oportunidade de reconciliar protótipo × corpus**, registrando honestamente a proveniência (a regra anti-divergência do `estado-atual-e-roteiro`).

**Insumo:** `atlas-prototipo-3d.html` (principal), `atlas-mvp-incremento-1.html`, `atlas-1789-fatia-vertical.html` — reenviados quando a migração for executada (arquivos não atravessam chats sozinhos).

**Fases:**

1. **Extração.** Ler os itens/claims/relações semeados no protótipo para uma forma intermediária (JSON normalizado), preservando `claimType`, fonte, "como sabemos" e gating de cada item.
2. **Classificação de proveniência (reconciliação — crítico).** Marcar `provenance_status` por item:
   - `corpus` — GOE (2,4 Ga, 4E) e K-Pg (66 Ma, 4G): **fiéis ao corpus**, migram como conteúdo real.
   - `seeded-demo` — os itens de química/física/geologia/vida de **1789**: **semeados para demonstração, NÃO estão no corpus** (a 4D é só história). Migram **marcados**, nunca como se fossem corpus. Geometrias de cena profunda = **esquemáticas**, não paleogeografia real → `is_reconstruction=TRUE` + nota.
3. **Normalização ao esquema (§5.2).** Converter cada item ao `knowledge_item`; cada relação afirmativa ao `relationship` com a *constraint* [N1] — **arestas afirmativas sem fonte A/B + `claimType` + confiança são rejeitadas ou rebaixadas a `pending`**, não inseridas à força.
4. **Datum temporal.** Garantir `canonical_time_scalar` (T0=2000.0 CE) + `source_time_basis` preservado para todos; aplicar calibração ¹⁴C / offset de 50 anos só onde 3Z manda (regimes 4–5).
5. **Carga + verificação.** Inserir no motor escolhido; validar invariantes ([N1]–[N5]) por *check* automatizado; conferir que nenhum item `pending`/`legal-review` apareceria no globo/timeline/simultaneidade (invariante de exibição).
6. **Registro de divergências.** Toda lacuna protótipo×corpus vira **tarefa de modelagem registrada** (pendências F1/F2), fechando a regra "protótipo e corpus não divergem em silêncio".

**O que a migração NÃO faz:** não inventa fontes para os itens semeados de 1789; não promove `seeded-demo` a `corpus`; não povoa itens novos além do que o protótipo já tem.

---

## 7. Fontes / insumos necessários

B1 é infraestrutura, não conteúdo — consome **artefatos do corpus**, não fontes externas de dados:
- **Etapa 2** (Knowledge Core): tipos, `relationType`, invariante do grafo (§6.4), vocabulário (4B).
- **Etapa 3Z**: o `TimeRange` canônico completo (já embutido em §5.2).
- **Etapa 11**: invariantes normativos [N1]–[N5], tabela tipo-de-dado → armazenamento.
- **Etapa 12**: o recorte de motor do MVP (precedente confirmado).
- **Protótipos `.html`**: o *graph-seed* a migrar (reenviar na execução).
- **Para o A3/implementação (fora de B1):** escolha do produto/versão específico de PostgreSQL/PostGIS, parâmetros de índice, *tuning* de travessia (R-33).

---

## 8. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| R-B1.1 | Proveniência por aresta vira **convenção frágil** (relacional não a impõe nativamente) | *Constraint*/trigger [N1] no esquema; rejeição de aresta afirmativa órfã; verificação na carga |
| R-B1.2 | Travessia exceder 2 hops no futuro e relacional degradar (E11 R-33) | Gatilho G1 medido + esquema portável (§5.3) → migração é conversão, não reescrita |
| R-B1.3 | Erro de datum na conversão temporal | Herdar 3Z literalmente; preservar `source_time_basis`; calibração ¹⁴C antes do canônico |
| R-B1.4 | Vazamento de licença (SA/ODbL/NC) para o núcleo | `IsolatedLicenseStore` físico separado **desde já** ([N3]), mesmo vazio |
| R-B1.5 | Item `seeded-demo` de 1789 ser confundido com corpus | `provenance_status` obrigatório; gating; registro de divergência (F1/F2) |
| R-B1.6 | Índice/cache tratado como verdade | Assimetria [N2] estrutural; `carriesProvenance=false` em derivados; cache com `inputVersionSet` |
| R-B1.7 | Decisão parecer "ideológica" (anti-graph) e travar interop futura | D-B1.2 com gatilhos explícitos (G1/G2/G3) + portabilidade documentada |

---

## 9. Entregáveis

1. **Comparativo** RDF* × property graph × relacional, pesado pelos padrões reais do protótipo — §5.1.
2. **Esquema mínimo do grafo** (esboço de design, com *constraints* vinculantes) + mapa de portabilidade a grafo — §5.2 e §5.3.
3. **Plano de migração** do protótipo, com reconciliação corpus × seeded-demo — §6.
4. **Decisão registrada:** relacional+JSONB+PostGIS como motor do núcleo, com gatilhos de migração — §4.

---

## 10. Próximos passos

- **B2 — Reificação** (próximo na Trilha B): promover `Source`/`Claim`/`MediaAsset` a tipos de primeira classe — o esquema de §5.2 já reserva as tabelas; B2 fecha a pendência F4.
- **A3 — Produção 3D (Claude Code):** recebe o motor decidido como destino real dos dados; implementa o esquema de fato (DDL real, banco real) — fora de B1.
- **Em paralelo — C1:** ratificar P1/P2/P7 (governança), fixando "pronto = evidência" e a separação Constituição/Playbook.
- **Quando da execução da migração:** reenviar os `.html` do protótipo; rodar as Fases 1–6 de §6.

---

*Documento de entrega do Passo B1, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o recorte do MVP (Etapa 12) e a Decisão de re-centragem da tese. Resolve a `[PENDÊNCIA]` E11→E12 do motor do grafo com os padrões reais de consulta do protótipo como evidência (P3). Decide a **classe de motor** (relacional+JSONB+PostGIS, esquema portável a grafo, gatilhos de migração explícitos), entrega o esquema mínimo e o plano de migração. Não escreve código de aplicação, não cria banco real, não migra dados de fato, não escolhe produto/versão final, não desenha UX, não popula o Knowledge Core, não reifica fisicamente (B2) e não reabre auditoria de fontes nem política editorial. Próximo passo na Trilha B, quando solicitado: B2 — Reificação de `Source`/`Claim`/`MediaAsset`.*
