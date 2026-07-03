# Etapa 2 — Modelagem do Knowledge Core

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 2 · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1 e o portão de ingestão da Etapa 1.1 · 12/06/2026
**Escopo desta etapa (e seus limites):** esta etapa **modela conceitualmente** o Knowledge Core. Conforme solicitado, ela **não** escreve código de aplicação, **não** propõe MVP, **não** define stack técnica, **não** avança para UX/UI e **não** desenha pipeline de ingestão. O que segue é um **modelo conceitual** — entidades, campos, relações, invariantes e exemplos — que governa a Etapa 3 (timeline/globo), a Etapa 5 (simultaneidade) e a Etapa 13 (pipeline), e que já nasce obrigado pelo portão da Etapa 1.1.
**O que esta modelagem herda e respeita:** D4/A6 (simultaneidade como capacidade nativa do núcleo), D5/A5 (espinha dorsal como hipótese, cobertura estrutural e não exaustiva), D6 (tempo híbrido profundo + histórico, multiescala), D7 (honestidade epistêmica como estrutura, não enfeite), D8 (lente Brasil estrutural), D11 (fato × expressão, prioridade a PD/CC/dados abertos, Wikidata só índice, curadoria humana), e a Etapa 1.1 inteira (`ProvenanceMetadata`, separação índice × autoridade, isolamento ShareAlike, tipagem de claim + nível de confiança como pré-requisito).

---

## Sumário

1. Princípios do Knowledge Core
2. Entidades centrais
3. Modelo claim-first
4. Modelo temporal
5. Modelo geoespacial
6. Relationship Graph
7. Governança, licença e proveniência
8. Camadas especiais (States)
9. Exemplos completos
10. Fronteira com camadas futuras
11. Decisões pendentes para etapas futuras

> **Convenção de leitura.** Nomes de entidades vêm em `CamelCase`; nomes de campos em `camelCase`; tipos enumerados aparecem como listas de valores. Onde escrevo "esquema de referência", trata-se de **especificação conceitual de campos** — um dicionário —, nunca de implementação. Nenhuma sintaxe aqui é código executável: é notação para fixar significado.

---

## 1. Princípios do Knowledge Core

### 1.1 O que o Knowledge Core é

O Knowledge Core (KC) é o **grafo universal de conhecimento factual tipado e com proveniência** do produto: o conjunto de coisas que sabemos sobre o universo, a Terra, a vida, a humanidade, as civilizações, a ciência, a tecnologia, a cultura, a economia e a geografia — do Big Bang ao presente — em que **cada afirmação relevante carrega tempo, espaço, tipo de claim, fonte e nível de confiança**. É a tradução em modelo de dados da tese da Etapa 0: conhecimento universal primeiro; currículo, professor e experiência depois.

O KC é um **núcleo soberano**: ele não conhece, não importa e não depende de nada das camadas externas (BNCC, planejamento docente, aluno, LMS). A dependência é sempre invertida — as camadas de fora apontam para dentro do KC por identificadores estáveis; o KC nunca aponta para fora. Essa inversão é o que torna o núcleo **universal e reutilizável** por escola pública, privada, museu, secretaria ou exploração livre, sem reescrita.

### 1.2 Os dez princípios (P1–P10)

| # | Princípio | O que significa na modelagem |
|---|---|---|
| **P1** | **Universalidade** | O KC modela conhecimento, não currículo. Nenhuma entidade do núcleo referencia BNCC, série, disciplina ou aula. A indexação curricular é **anotação externa** (Etapa 6), nunca campo do núcleo. |
| **P2** | **Independência da BNCC** | A BNCC é consumidora do KC, não componente dele. Remover a BNCC inteira não muda um único campo do núcleo. |
| **P3** | **Rastreabilidade por fonte** | Toda entidade factual carrega `ProvenanceMetadata` (Etapa 1.1). Não existe "entidade sem proveniência". |
| **P4** | **Orientação a claim** | A unidade atômica de verdade é o `Claim` tipado e fonteado, não o parágrafo de texto. Narrativa é camada derivada que **cita** claims (Tarefa 3). |
| **P5** | **Temporalidade nativa** | Todo item posicionável no tempo carrega `TimeRange` num eixo único que vai de Ga a um dia (Tarefa 4). O tempo é índice de primeira classe, não atributo secundário. |
| **P6** | **Geoespacialidade nativa** | Todo item localizável carrega geometria versionada no tempo e correspondência com o território atual (Tarefa 5). O espaço é índice de primeira classe. |
| **P7** | **Simultaneidade como propriedade emergente** | Por P5 + P6, "o que acontecia no mundo neste momento?" é a **interseção** dos índices temporal e espacial — não um módulo à parte (D4/A6). Detalhado em 1.4. |
| **P8** | **Incerteza tipada** | Todo claim carrega `ClaimType`, `ConfidenceLevel`, `EvidenceLevel` e `UncertaintyProfile`. Fato, medição, inferência, estimativa, hipótese, controvérsia, interpretação historiográfica, reconstrução e representação são **valores distintos**, exibíveis (D7). |
| **P9** | **Tempo profundo e tempo histórico no mesmo eixo** | Idade geológica em Ma/Ga e data calendárica BCE/CE coexistem num eixo canônico ordenável, com precisão e incerteza próprias de cada regime (D6). |
| **P10** | **Pronto para estados e mídia** | Além de eventos pontuais, o KC modela **estados** de sistemas (atmosfera, tectônica, clima, civilização, economia…) ao longo do tempo (Tarefa 8) e **mídia** com regime de licença isolado por asset (Tarefa 2/7). |

### 1.3 O que entra e o que não entra

**Entra no Knowledge Core:**

- coisas conhecidas: `Event`, `Process`, `Concept`, `Entity` (pessoas, instituições, objetos, táxons, tecnologias…);
- o eixo espaço-tempo: `Place`, `Region`, `TimeRange`, geometrias versionadas, escala cronoestratigráfica;
- a espinha epistêmica: `Source`, `Citation`, `Claim`, `ClaimSet`, e os perfis de confiança/evidência/incerteza;
- o grafo: `Relationship` entre quaisquer itens;
- mídia e cartografia como **assets** com licença isolada: `MediaAsset`, `MapAsset`;
- estados de sistemas no tempo (Tarefa 8);
- governança: `ProvenanceMetadata`, `LicenseProfile`, `ReviewStatus`, `DatasetSnapshot`.

**Não entra no Knowledge Core (pertence a camadas posteriores):**

- BNCC, competências, habilidades, áreas e componentes curriculares — **Compliance Layer (Etapa 6)**;
- currículo estadual/municipal, grade prática, série, bimestre — **Planning Layer (Etapa 7)**;
- plano de aula, roteiro, quiz, rubrica, atividade, material do aluno — **Output Layer (Etapa 9)**;
- modo professor, modo estudante, qualquer tela — **Experience Layer (Etapa 10)**;
- dados de aluno/turma, personalização, analytics de uso, integração LMS — **Privacidade/telemetria (transversal) e camadas externas**;
- **fatos vindos de IA generativa** ou de índices (Wikidata/Wikipedia) como autoridade — proibido por A3/Q5 e pelo portão (Etapa 1.1).

A fronteira completa, com o mecanismo de não-contaminação, está na Tarefa 10.

### 1.4 Como "o que acontecia no mundo neste momento?" nasce do próprio núcleo

A função não é uma feature acoplada; é uma **leitura natural da estrutura**. Como todo item factual carrega (por P5/P6/P8) um intervalo temporal canônico, uma geometria com correspondência ao território atual, um tema e um nível de confiança, a pergunta se resolve assim, conceitualmente:

1. **Traduzir o instante/intervalo da consulta** (ex.: o ano 1789, ou a idade 2,4 Ga) para o **eixo temporal canônico** (Tarefa 4).
2. **Selecionar** todo `Event`/`Process`/`State` cujo `TimeRange` **intersecta** esse intervalo.
3. **Agrupar** o resultado por `Region`, por **tema/camada** (ciência, política, economia, ambiente…) e por **território atual** (via `ModernCorrespondence`, para a lente Brasil de D8).
4. **Anexar** a cada resultado seu `ClaimType` e `ConfidenceLevel`, para que a interface mostre o que é fato, inferência ou reconstrução (D7).

Nenhum dado novo precisa existir para a função funcionar: ela é a **interseção dos índices temporal e espacial sobre claims tipados**. Por isso D4/A6 diz que a simultaneidade "influencia o modelo de dados desde a origem" — e é por isso que ela é Tarefa central desta modelagem, não um apêndice.

### 1.5 Como o núcleo conversa com BNCC e planejamento sem depender deles

O acoplamento é por **referência externa e anotação**, em três regras:

- **Identificador estável.** Toda entidade do KC tem um `knowledgeItemId` permanente e versionado. As camadas externas guardam *seus próprios* registros que **apontam** para esses IDs (ex.: um índice BNCC dizendo "a habilidade EF08HI06 se relaciona aos itens `evt:revolucao-francesa`, `evt:inconfidencia-mineira`").
- **Direção única de dependência.** O índice BNCC conhece o KC; o KC **não** conhece o índice BNCC. Apagar a camada BNCC não deixa nenhum campo órfão no núcleo.
- **Interface de leitura.** As camadas externas consultam o KC por tempo, espaço, tema, tipo e confiança — exatamente os índices que a simultaneidade usa. O motor de correspondência (Etapa 8) é, do ponto de vista do núcleo, **mais um leitor** desses índices, com filtros pedagógicos aplicados *fora* do núcleo.

Assim, o KC permanece universal e o produto continua compatível com a educação brasileira — sem que a compatibilidade entre no núcleo.

---

## 2. Entidades centrais

As 23 entidades pedidas são organizadas em seis famílias. Para cada uma: **finalidade**, **campos principais**, **relações**, **exemplo**, **o que herda do portão (Etapa 1.1)** e **classificação** (universal / científica / histórica / geográfica / mídia / governança).

> **Hierarquia de tipos.** `KnowledgeItem` é o supertipo abstrato de tudo que é "conhecido". `Event`, `Process`, `Concept` e `Entity` são seus subtipos. `Place` e `Region` são itens espaciais. `Claim`, `Source`, `Citation`, `ClaimSet` formam a espinha epistêmica. `Relationship` é a aresta do grafo. `MediaAsset`/`MapAsset` são assets de licença isolada. `ProvenanceMetadata`, `LicenseProfile`, `ReviewStatus`, `DatasetSnapshot` são governança. `TimeRange`, `ConfidenceLevel`, `EvidenceLevel`, `UncertaintyProfile`, `ChronologicalScale` são **objetos de valor** (não têm vida própria; existem acoplados a um item ou claim).

### Família A — Item de conhecimento e subtipos

#### `KnowledgeItem` (abstrato)
- **Finalidade.** Supertipo de tudo que o núcleo conhece; carrega o que é comum a qualquer item: identidade estável, rotulagem, tempo, espaço, proveniência e governança.
- **Campos principais.** `knowledgeItemId` (estável, versionado), `itemType` (`event`/`process`/`concept`/`entity`/`place`/`region`/`state`), `preferredLabel`, `aliases[]`, `shortDescription` (didática, **não** é claim — ver Tarefa 3), `themeTags[]` (universo, geologia, vida, história, ciência, tecnologia, economia, cultura, ambiente…), `primaryTimeRange` (opcional), `primaryGeoReference` (opcional), `claimSetRef`, `provenanceRef`, `reviewStatus`, `versionInfo`.
- **Relações.** Liga-se a `Claim`/`ClaimSet`, a `Relationship` (como origem/destino), a `MediaAsset`/`MapAsset`, e a `TimeRange`/`GeoReference`.
- **Exemplo.** Qualquer um dos seis casos da Tarefa 9 é um `KnowledgeItem` de subtipo específico.
- **Herda do portão.** `provenanceRef` e `reviewStatus` obrigatórios; item com `reviewStatus = pending|blocked` não é exibível (invariante da Etapa 1.1, Tarefa 7).
- **Classificação.** Estrutural/universal.

#### `Event`
- **Finalidade.** Acontecimento **delimitado** no tempo (pontual ou de curta duração) e, em geral, no espaço.
- **Campos principais.** herda de `KnowledgeItem` + `timeRange` (com `TimePrecision`), `geoReference`, `eventKind` (descoberta, batalha, erupção, lançamento, publicação, transição de estado…), `participants[]` (refs a `Entity`), `outcomeClaims[]`.
- **Relações.** `causou`/`influenciou`/`ocorreu-durante` outros itens; `localizado-em` `Place`/`Region`; `evidenciado-por` `Source`/`MediaAsset`.
- **Exemplo.** Queda da Bastilha (14/07/1789); lançamento da Apollo 11 (16/07/1969).
- **Herda do portão.** Cada `outcomeClaim` precisa de fonte A/B (Tarefa 3/7).
- **Classificação.** Universal; instanciado como histórico ou científico conforme o tema.

#### `Process`
- **Finalidade.** Fenômeno **estendido** no tempo, sem instante único — graduais, com início/fim difusos e frequentemente modelados, não observados.
- **Campos principais.** herda de `KnowledgeItem` + `timeRange` (tipicamente longo, com `TimeUncertainty`), `processKind` (oxidação, orogenia, evolução de táxon, industrialização…), `phases[]` (sub-`TimeRange` opcionais), `drivingClaims[]`.
- **Relações.** `parte-de` processos maiores; `causou` eventos; `ocorreu-durante` unidades cronostratigráficas.
- **Exemplo.** Grande Evento de Oxidação (~2,4–2,0 Ga); industrialização (séc. XVIII–XIX).
- **Herda do portão.** Processos de tempo profundo são tipicamente `claimType = inferência/reconstrução modelada` → rótulo obrigatório (D7/C2).
- **Classificação.** Universal; majoritariamente científica em tempo profundo.

#### `Concept`
- **Finalidade.** Ideia, teoria, conceito ou unidade de conhecimento **atemporal ou transtemporal** (não é um acontecimento).
- **Campos principais.** herda de `KnowledgeItem` + `conceptKind` (lei física, teoria, conceito histórico, categoria), `definitionClaims[]`, `relatedConcepts[]`. Em geral **sem** `timeRange` próprio (ou com `timeRange` de *formulação*, que é um `Event` separado).
- **Relações.** `relacionado-a` outros conceitos; `evidenciado-por` eventos/processos; um `Event` de formulação **instancia** o conceito no tempo.
- **Exemplo.** "Inflação cósmica"; "soberania popular"; "tectônica de placas".
- **Herda do portão.** Definições contestadas viram `ClaimSet` com claims concorrentes (Tarefa 3).
- **Classificação.** Universal/conceitual.

#### `Entity`
- **Finalidade.** Coisa nomeável que **participa** de eventos/processos: pessoa, instituição, objeto, missão, táxon, tecnologia, corpo celeste.
- **Campos principais.** herda de `KnowledgeItem` + `entityKind` (pessoa, organização, artefato, táxon, corpo celeste, tecnologia…), `existenceTimeRange` (nascimento–morte, vigência), `gazetteerLinks[]`/`authorityLinks[]` (VIAF para pessoas, IAU para corpos celestes…).
- **Relações.** `participou-de` eventos; `parte-de` instituições; `sucessor/predecessor` de outras entidades.
- **Exemplo.** Antoine Lavoisier; NASA; Saturn V; *Australopithecus*; Tiradentes.
- **Herda do portão.** `authorityLinks` para índices (VIAF/Wikidata) entram como **reconciliação**, nunca como fonte de claim (Tarefa 7).
- **Classificação.** Universal; histórica ou científica conforme o caso.

### Família B — Espaço e tempo (entidades-âncora; detalhe nas Tarefas 4 e 5)

#### `Place`
- **Finalidade.** Lugar com **identidade estável** ao longo do tempo, cuja **geometria varia** (cidade, sítio, território). A identidade é separada da forma.
- **Campos principais.** `placeId`, `preferredName`, `nameVariants[]` (com `TimeRange` de vigência de cada nome), `geometryVersions[]` (ver `GeometryVersion`, Tarefa 5), `gazetteerLinks[]` (Pleiades/WHG/GeoNames), `modernCorrespondence`.
- **Relações.** `localizado-em` `Region`; alvo de `localizado-em` por eventos.
- **Exemplo.** Paris; Vila Rica / Ouro Preto; o sítio do sambaqui de Sambaqui.
- **Herda do portão.** Geometrias de fontes ShareAlike/ODbL (OSM) ficam em camada isolada (Tarefa 5/7).
- **Classificação.** Geográfica.

#### `Region`
- **Finalidade.** Agregado espacial nomeado, possivelmente difuso ou cultural, não necessariamente administrativo.
- **Campos principais.** `regionId`, `regionKind` (administrativa, cultural, física, histórica, paleo), `geometryVersions[]`, `spatialUncertainty`, `modernCorrespondence`.
- **Relações.** `contém` places; `equivalente-aproximado` de outras regiões em outras épocas.
- **Exemplo.** Capitania de Minas Gerais (1789); "território que hoje é o Brasil"; Pangeia (região paleogeográfica).
- **Herda do portão.** Fronteiras vêm de geoBoundaries/Natural Earth (CC BY/PD); GADM (NC) é proibido (Etapa 1.1).
- **Classificação.** Geográfica.

#### `TimeRange` (objeto de valor)
- **Finalidade.** Intervalo temporal canônico de qualquer item; suporta ponto, intervalo, profundidade geológica e incerteza. Detalhe completo na Tarefa 4.
- **Campos principais.** `canonicalStart`, `canonicalEnd` (escalar ordenável no eixo único), `precision` (`TimePrecision`), `uncertainty` (`TimeUncertainty`), `humanRepresentation` (`CalendarDate` ou `DeepTimeAge` ou `ChronostratigraphicUnit`).
- **Classificação.** Estrutural (objeto de valor).

#### `ChronologicalScale` / `ChronostratigraphicUnit`
- **Finalidade.** A **régua** do tempo profundo: éons, eras, períodos, épocas, idades, com nomes e idades de limite. Detalhe na Tarefa 4.
- **Campos principais.** `unitId`, `rank` (éon/era/período/época/idade), `name`, `boundaryStartAge`/`boundaryEndAge` (Ma, com incerteza), `parentUnit`, `sourceRef` (ICS via Macrostrat).
- **Herda do portão.** Ingerida como **fato recodificado** do ICS (o gráfico é NC; os fatos são livres) — caso canônico da Etapa 1.1.
- **Classificação.** Científica/estrutural.

### Família C — Espinha epistêmica

#### `Source`
- **Finalidade.** A origem autoritativa de um claim: instituição, dataset, publicação, documento primário.
- **Campos principais.** `sourceId`, `sourceName`, `sourceTier` (A/B/C), `authorityType` (`primary`/`aggregator`/`index`), `licenseProfileRef`, `originalUrl`, `datasetSnapshotRef`.
- **Relações.** `Citation` aponta para `Source`; `Claim` referencia `Citation`.
- **Exemplo.** NASA; Macrostrat; Paleobiology Database; Arquivo Nacional; IBGE.
- **Herda do portão.** `sourceTier` e `authorityType` obrigatórios; fonte C (Wikidata) nunca sustenta claim (Tarefa 7).
- **Classificação.** Governança/epistêmica.

#### `Citation`
- **Finalidade.** Ligação precisa entre um `Claim` e o ponto exato da `Source` que o sustenta (página, registro, identificador de dataset, DOI).
- **Campos principais.** `citationId`, `sourceRef`, `locator` (página/registro/DOI/linha), `retrievedAt`, `quotedFact` (o **fato** re-codificado, não a expressão), `attributionText`.
- **Relações.** Pertence a um `Claim`; aponta a uma `Source`.
- **Exemplo.** "PBDB, ocorrência #1234567, acessada em 2026-06-12".
- **Herda do portão.** `attributionText` pronto para exibição (campo da Etapa 1.1); para fontes NC, registra **fato** re-derivado, jamais a expressão.
- **Classificação.** Governança/epistêmica.

#### `Claim`
- **Finalidade.** **Unidade atômica de verdade** do KC. Toda afirmação factual relevante é um `Claim`. Modelo detalhado na Tarefa 3.
- **Campos principais.** `claimId`, `statement` (texto curto e preciso), `claimType`, `subjectRef` (o item de que trata), `citation`/`sourceRef` (A/B), `confidenceLevel`, `evidenceLevel`, `uncertaintyProfile`, `temporalScope` (`TimeRange`), `spatialScope` (`GeoReference`), `reviewStatus`, `provenanceRef`, `relatedClaims[]`.
- **Relações.** `evidenciado-por`/`contradito-por`/`hipótese-concorrente` de outros claims; pertence a um `ClaimSet`.
- **Exemplo.** "A Queda da Bastilha ocorreu em 14/07/1789" (`claimType = fato documentado`).
- **Herda do portão.** Hard stops da Etapa 1.1: sem fonte A/B → não entra como claim; sem `confidenceLevel`/`claimType` → bloqueia; inferência/controvérsia sem rótulo → não publica.
- **Classificação.** Epistêmica (a entidade mais importante do núcleo).

#### `ClaimSet`
- **Finalidade.** Agrupa claims que descrevem **o mesmo assunto** e, sobretudo, modela **controvérsia**: várias leituras concorrentes de um mesmo fato.
- **Campos principais.** `claimSetId`, `subjectRef`, `claims[]`, `consensusStatus` (`consenso`/`majoritário`/`em disputa`/`hipóteses concorrentes`), `editorialNote`.
- **Relações.** Cada `KnowledgeItem` referencia um `ClaimSet`; claims internos podem ter `hipótese-concorrente` entre si.
- **Exemplo.** Datas e causas do colapso de uma civilização com leituras historiográficas distintas; cenários de povoamento das Américas.
- **Herda do portão.** `editorialNote` e rótulos vêm da **política editorial de controvérsias** (R3, a ser escrita antes da Etapa 4).
- **Classificação.** Epistêmica.

#### `ConfidenceLevel` (objeto de valor)
- **Finalidade.** Quão **seguros estamos** de que o claim é verdadeiro, exibível na interface (D7).
- **Campos principais.** `level` (ex.: `alta`/`média`/`baixa`/`contestada`), `basis` (texto curto: "consenso científico", "fonte primária única", "estimativa de modelo"), `lastReviewed`.
- **Classificação.** Epistêmica (objeto de valor).

#### `EvidenceLevel` (objeto de valor)
- **Finalidade.** **Qual a natureza da evidência** que sustenta o claim (independente da confiança): observação direta, medição, registro documental primário, dado modelado, inferência indireta.
- **Campos principais.** `level` (`observação direta`/`medição instrumental`/`documento primário`/`dado modelado`/`inferência indireta`/`testemunho secundário`), `note`.
- **Distinção útil.** Confiança e evidência são ortogonais: uma medição instrumental pode ter confiança média (instrumento ruidoso); um documento primário pode dar confiança alta. Modelá-los separados evita colapsar "como sabemos" com "quão certos estamos".
- **Classificação.** Epistêmica (objeto de valor).

#### `UncertaintyProfile` (objeto de valor)
- **Finalidade.** Descrição estruturada da **incerteza** — temporal, espacial, de magnitude, de interpretação — sem reduzir tudo a um número.
- **Campos principais.** `temporalUncertainty` (ref a `TimeUncertainty`), `spatialUncertainty` (ref a `SpatialUncertainty`), `magnitudeUncertainty` (±, faixa), `interpretiveUncertainty` (texto: o que está em disputa), `modelDependence` (booleano: o claim depende de um modelo?).
- **Exemplo.** Idade do limite Jurássico ~201,4 ± 0,2 Ma; posição paleogeográfica de um cráton em 2,4 Ga com larga incerteza de rotação.
- **Classificação.** Epistêmica (objeto de valor).

### Família D — Grafo

#### `Relationship`
- **Finalidade.** Aresta tipada entre dois `KnowledgeItem` quaisquer; sustenta simultaneidade, trilhas, correlações e dossiês. Tipos detalhados na Tarefa 6.
- **Campos principais.** `relationshipId`, `fromRef`, `toRef`, `relationType` (causou, influenciou, ocorreu-durante, parte-de, contemporâneo-de, localizado-em, evidenciado-por, contradito-por, hipótese-concorrente, sucessor/predecessor, equivalente-aproximado, versão-historiográfica…), `directionality`, `claimBacking` (relações afirmativas, como "causou", **são elas próprias claims** com fonte e confiança), `temporalScope`.
- **Relações.** É a própria relação.
- **Exemplo.** `evt:revolucao-francesa --influenciou--> evt:independencias-americas`; `evt:inconfidencia-mineira --contemporâneo-de--> evt:revolucao-francesa`.
- **Herda do portão.** Relações causais/interpretativas exigem fonte A/B e tipo de claim (não se afirma "X causou Y" sem proveniência).
- **Classificação.** Estrutural/universal.

### Família E — Mídia (licença isolada por asset)

#### `MediaAsset`
- **Finalidade.** Imagem, vídeo, áudio ou ilustração de dossiê, com **natureza** e **licença** próprias, modelada **separada do grafo factual** (Etapa 1.1, Tarefa 7).
- **Campos principais.** `mediaAssetId`, `mediaKind` (fotografia, vídeo, áudio, ilustração), `natureLabel` (**fotografia/mapa/gráfico/reconstrução científica/simulação/representação artística/aproximação didática** — D7), `licenseProfileRef`, `provenanceRef`, `allowedUse` (`media-dossier`/`isolated-layer`/`blocked`), `attributionText`, `depictsRefs[]` (itens que ilustra).
- **Relações.** `ilustra`/`evidencia` itens; **nunca** é fonte de claim factual por si só.
- **Exemplo.** Foto da pegada de Aldrin (NASA, PD, natureza = fotografia); ilustração de Pangeia (reconstrução modelada, rotulada).
- **Herda do portão.** Triagem por asset (Commons/Europeana → CONF); SA → `isolated-layer`; NC → não entra; imagem gerada por IA → rótulo "representação artística/aproximação didática gerada por IA" + revisão humana (casos de borda 3, 8 da Etapa 1.1).
- **Classificação.** Mídia.

#### `MapAsset`
- **Finalidade.** Mapa (histórico ou científico) como asset visual, distinto da **geometria** factual (que vive em `GeometryVersion`). Um `MapAsset` é uma *imagem de mapa*; uma `GeometryVersion` é *dado vetorial*.
- **Campos principais.** `mapAssetId`, `mapKind` (mapa histórico, mapa científico, reconstrução paleogeográfica), `natureLabel`, `licenseProfileRef`, `coverageTimeRange`, `coverageRegionRef`, `allowedUse`, `attributionText`.
- **Relações.** `representa` regiões/épocas; pode `evidenciar` um claim geográfico (com fonte).
- **Exemplo.** Reconstrução EarthByte de Pangeia (CC BY, reconstrução modelada); mapa histórico PD obtido de provedor PD-explícito (não do scan NC do David Rumsey).
- **Herda do portão.** Caso de borda do "mapa PD com scan NC": usar provedor PD; David Rumsey (NC-SA) proibido como expressão (Etapa 1.1).
- **Classificação.** Mídia/geográfica.

### Família F — Governança e versionamento

#### `DatasetSnapshot`
- **Finalidade.** **Congela** uma versão da fonte ingerida, para antifragilidade (C4/R7: fontes adormecem; não se depende do acesso ao vivo).
- **Campos principais.** `snapshotId`, `sourceRef`, `snapshotDate`, `sourceVersion`, `checksum`, `coverageNote`.
- **Relações.** `Source` referencia seus snapshots; `Citation` pode apontar ao snapshot exato.
- **Exemplo.** "Macrostrat timescale, snapshot 2026-06-01".
- **Herda do portão.** `retrievedAt`/versionamento são exigência da Etapa 1.1.
- **Classificação.** Governança.

#### `ProvenanceMetadata` (objeto de valor — importado integral da Etapa 1.1)
- **Finalidade.** Viaja **acoplado a todo item factual** (claim, fonte, mídia, geometria). É o portão tornado dado.
- **Campos principais.** todos os da Tarefa 5 da Etapa 1.1: `sourceId`, `sourceName`, `originalUrl`, `retrievedAt`, `license`, `licenseUrl`, `licenseRiskLevel` (0–5), `attributionRequired`, `attributionText`, `shareAlikeRequired`, `nonCommercial`, `itemLevelLicense`, `sourceTier`, `authorityType`, `provenanceChain[]`, `rightsNotes`, `allowedUse`, `ingestionDecision`, `reviewStatus`.
- **Classificação.** Governança. **Não opcional** (Etapa 1.1, Tarefa 7.1).

#### `LicenseProfile` (objeto de valor)
- **Finalidade.** Perfil de licença reutilizável, derivado da política da Etapa 1.1 (Tarefa 3 de lá).
- **Campos principais.** `license` (enum: PD/CC0/CC BY/CC BY-SA/ODbL/CC BY-NC/CC BY-NC-SA/proprietária/por-item/legal-BR/fato/sem-licenca), `nonCommercial`, `shareAlikeRequired`, `attributionRequired`, `licenseRiskLevel` (0–5), `allowedUse`.
- **Relações.** Referenciado por `Source`, `MediaAsset`, `MapAsset`, `GeometryVersion`.
- **Classificação.** Governança.

#### `ReviewStatus` (objeto de valor)
- **Finalidade.** Estado de curadoria que **governa publicação** (invariante de exibição).
- **Campos principais.** `status` (`not-required`/`pending`/`approved`/`rejected`/`legal-review`), `reviewer`, `reviewedAt`, `note`.
- **Invariante.** Item com `status ∈ {pending, rejected, legal-review}` **não é exibível** nem consultável pela experiência (Etapa 1.1, Tarefa 7.5).
- **Classificação.** Governança.

---

## 3. Modelo claim-first

### 3.1 A regra

**Nenhuma afirmação factual relevante existe apenas como texto solto.** Toda afirmação que o produto trata como verdade sobre o mundo é um `Claim` — atômico, tipado, fonteado e datado. O texto que o aluno lê é uma **camada derivada** que *cita* claims; não é onde a verdade mora.

Isso resolve, em estrutura, o diferencial da Etapa 0 (D7) e a salvaguarda R9: contra pipelines "Wikipedia + IA como autoridade", o KC só admite verdade que rastreia a uma fonte A/B e carrega seu tipo e sua confiança.

### 3.2 Anatomia de um `Claim`

Todo `Claim` relevante carrega, obrigatoriamente:

| Componente | Campo | Observação |
|---|---|---|
| Texto | `statement` | curto, preciso, uma asserção por claim |
| Tipo | `claimType` | enum abaixo (3.4) |
| Fonte | `sourceRef` (A/B) + `citation` | hard stop: sem A/B, não entra como claim |
| Confiança | `confidenceLevel` | exibível (D7) |
| Evidência | `evidenceLevel` | natureza da evidência (ortogonal à confiança) |
| Incerteza | `uncertaintyProfile` | temporal/espacial/magnitude/interpretativa |
| Escopo temporal | `temporalScope` (`TimeRange`) | quando o claim vale (Tarefa 4) |
| Escopo espacial | `spatialScope` (`GeoReference`) | onde o claim vale (Tarefa 5) |
| Revisão | `reviewStatus` | governa publicação |
| Proveniência | `provenanceRef` (`ProvenanceMetadata`) | portão da Etapa 1.1 |
| Relações | `relatedClaims[]` | evidência/contradição/concorrência |

### 3.3 O que um `Claim` **não** é (diferenciação)

| Não é claim | É… | Como o modelo trata |
|---|---|---|
| **Narrativa didática** | prosa que organiza vários claims numa história | objeto separado (`Narrative`, fora do núcleo factual; vive na Output Layer ou como `shortDescription` rotulada) que **referencia** claims por ID; nunca afirma fato novo. |
| **Descrição curta** | `shortDescription` do item | rótulo de conveniência; **não** consultável como verdade; sem peso epistêmico. |
| **Resumo** | condensação de claims | derivado; cita os claims que resume; não é fonte. |
| **Texto gerado por IA** | rascunho de linguagem (A3/Q5) | nunca claim; `reviewStatus = pending` + rótulo de IA; entra só após curadoria humana, e ainda assim como narrativa, não como fato. |
| **Representação visual / mídia** | `MediaAsset`/`MapAsset` | ilustra; só **evidencia** um claim se for fonte A/B (ex.: fotografia documental); reconstrução/ilustração nunca é fato. |
| **Hipótese** | `claimType = hipótese` | é um claim, mas tipado como hipótese, com confiança correspondente; não se apresenta como consenso. |
| **Controvérsia** | `ClaimSet` com `consensusStatus = em disputa` | não é um claim único; é um conjunto de claims concorrentes ligados por `hipótese-concorrente`/`contradito-por`. |

A fronteira essencial: **claim = asserção verificável sobre o mundo, com fonte**; tudo o mais (narrativa, resumo, ilustração, texto de IA) é **apresentação que aponta para claims**, sem poder de afirmar.

### 3.4 Tipos de claim (`claimType`)

Enum exibível na interface (D7), herdado da Etapa 0/1.1:

`fato documentado` · `medição direta` · `inferência científica` · `estimativa` · `hipótese` · `controvérsia` · `interpretação historiográfica` · `reconstrução modelada` · `representação artística` · `aproximação didática`.

Regra de publicação (Etapa 1.1, hard stop 6): claim de tipo `inferência`/`hipótese`/`controvérsia`/`reconstrução` **sem rótulo visível** não publica. A cena canônica do Grande Evento de Oxidação (`reconstrução modelada` + nota de incerteza) é o teste desse tipo.

### 3.5 Como a controvérsia é modelada (sem escolher lado)

Uma controvérsia não vira "claim neutro". Vira um `ClaimSet` com `consensusStatus = em disputa`, contendo dois ou mais `Claim` (cada um com sua fonte A/B e sua confiança), ligados por `Relationship` do tipo `hipótese-concorrente` ou `contradito-por`. A interface mostra as leituras lado a lado, com fontes — exatamente a mitigação de R3/C3. A escolha de **quais** controvérsias destacar e como narrá-las é da **política editorial** (R3), externa a este modelo.

---

## 4. Modelo temporal

### 4.1 O problema e a decisão (D6)

O KC precisa colocar, no **mesmo eixo navegável**, "13,8 Ga" e "14 de julho de 1789" e "16:50 UTC de 20/07/1969" — e ainda dizer, de cada um, **quão preciso** e **quão incerto** é. A decisão D6 fixa: tempo profundo pela escala cronoestratigráfica do ICS; tempo histórico por datas calendáricas com intervalo e incerteza; navegação multiescala (zoom logarítmico de Ga a um dia).

A modelagem resolve isso com **dupla representação**: um **escalar canônico** (para ordenar, indexar, intersectar — é o que a timeline e a simultaneidade usam) e uma **representação humana rica** (calendário, idade geológica, unidade cronostratigráfica — é o que se exibe).

### 4.2 O eixo canônico

- Um valor escalar ordenável posiciona qualquer item no eixo único. Conceitualmente, "anos a partir de um datum fixo", com sinal, em **escala logarítmica para tempo profundo** e linear para tempo histórico, costurados num contínuo navegável.
- **O datum é fixo, não "agora".** Idades de tempo profundo são ancoradas a um ponto de referência estável (convenção "antes do presente" com presente fixado, p. ex. 1950, ou época astronômica J2000), **não** ao instante atual. Isso evita que o eixo inteiro escorregue quando o tempo passa — só a ponta "presente móvel" (4.6) avança.
- A representação humana (`CalendarDate`, `DeepTimeAge`, `ChronostratigraphicUnit`) é derivável do escalar e vice-versa, mas **carrega sua própria precisão e incerteza**.

### 4.3 Entidades e objetos de valor temporais

#### `TimeRange`
- `canonicalStart`, `canonicalEnd` (escalar do eixo); para evento pontual, start = end.
- `precision` (`TimePrecision`), `uncertainty` (`TimeUncertainty`).
- `humanRepresentation` (um de `CalendarDate` / `DeepTimeAge` / `ChronostratigraphicUnit`).
- `rangeKind` (`instante` / `intervalo` / `processo longo` / `aproximado`).

#### `TimePoint`
- Um instante (start = end). Usado por eventos pontuais (lançamento, publicação, batalha).

#### `TimePrecision`
- `granularity` (`dia`/`mês`/`ano`/`década`/`século`/`milênio`/`ka`/`Ma`/`Ga`). Define **até onde** a data é conhecida — distinta de incerteza (uma data pode ser precisa ao dia e ainda assim ter zero incerteza, ou precisa ao Ma com ±0,2 Ma de incerteza).

#### `TimeUncertainty`
- `plusMinus` (±, na unidade da granularidade), `distributionNote` (ex.: "limite estratigráfico com intervalo de confiança"), `basis` (medição radiométrica, datação relativa, fonte documental ambígua…).

#### `ChronostratigraphicUnit`
- A régua de tempo profundo (ver Família B). `rank`, `name`, `boundaryStartAge`/`boundaryEndAge` (Ma + incerteza), `parentUnit`. Ingerida como **fato recodificado** do ICS via **Macrostrat** (CC BY, API) — caso de ouro da Etapa 1.1.

#### `CalendarDate`
- `calendarSystem` (gregoriano/juliano/outros quando necessário), `year` (com sinal; BCE/CE), `month`, `day`, `timeOfDay` (opcional, UTC). Suporta **anos antes do presente** e **anos astronômicos**.

#### `DeepTimeAge`
- `ageValue` (Ma ou Ga), `uncertainty` (±), `referenceDatum`. Para Big Bang, formação do Sistema Solar, GOE etc.

#### `TemporalRelation`
- Um `Relationship` temporal especializado: `antes-de`/`depois-de`/`durante`/`sobrepõe`/`contemporâneo-de`. Sustenta navegação e simultaneidade.

### 4.4 Como o modelo responde "o que acontecia no mundo em 1789?"

1. **Traduzir** 1789 (ou o intervalo 01/01/1789–31/12/1789) para o escalar canônico.
2. **Selecionar** todo `Event`/`Process`/`State` cujo `TimeRange.[canonicalStart, canonicalEnd]` **intersecta** esse intervalo (`TemporalRelation = durante/sobrepõe`).
3. **Agrupar** por `Region`/tema/`ModernCorrespondence` e **anexar** `claimType` + `confidenceLevel`.
4. **Resultado** (conceitual): Revolução Francesa (França, fato documentado), Inconfidência Mineira (capitania de Minas → território que hoje é o Brasil, fato documentado), primeiro governo sob a Constituição dos EUA (fato documentado), Lavoisier publica o *Traité élémentaire de chimie* (ciência, fato documentado) — a cena canônica da Etapa 0.

### 4.5 Como o modelo responde "o que acontecia há 2,4 bilhões de anos?"

Mesma operação, na porção de **tempo profundo** do eixo:

1. **Traduzir** 2,4 Ga para o escalar canônico (com a incerteza própria da idade).
2. **Selecionar** itens que intersectam — aqui predominam **States** (Tarefa 8), não eventos pontuais: `AtmosphereState` (subida de O₂), `TectonicState`/`PaleogeographicState` (configuração de crátons), `ClimateState` (contexto), e o `Process` "Grande Evento de Oxidação".
3. **Rotular tudo** como `inferência científica`/`reconstrução modelada` com `UncertaintyProfile` — pré-condição de não apresentar modelo como fato (C2/D7).
4. **Resultado:** o globo troca para reconstrução paleogeográfica rotulada; o dossiê do GOE aparece como inferência com nota de incerteza.

### 4.6 Presente móvel e simultaneidade

- **Presente móvel.** Há um único ponto "agora" derivado do relógio, usado só na ponta contemporânea (indicadores de OWID/World Bank) e na rotulagem "em curso". Ele **não** redefine o datum do eixo profundo.
- **Simultaneidade** é a interseção temporal (4.4/4.5) cruzada com o índice espacial (Tarefa 5). É a base estrutural de D4/A6 e da função central — modelada aqui como propriedade do eixo, não como feature à parte.

---

## 5. Modelo geoespacial

### 5.1 A decisão estruturante: identidade separada da geometria

Lugares **persistem**; suas **formas mudam**. Vila Rica e Ouro Preto são o mesmo `Place` com nomes e fronteiras distintos no tempo. A fronteira do "Brasil" de 1789 não é a de hoje. Continentes ocupavam outras posições em 2,4 Ga. Logo: **`Place`/`Region` têm identidade estável; a geometria é versionada por `TimeRange`** (`GeometryVersion`). Essa separação é o que torna possível a navegação espacial em qualquer época e a lente Brasil de D8.

### 5.2 Entidades e objetos de valor espaciais

#### `Place` (ver Família B)
Identidade estável + `nameVariants[]` (com vigência) + `geometryVersions[]` + `gazetteerLinks[]` + `modernCorrespondence`.

#### `Region` (ver Família B)
Agregado nomeado (administrativo/cultural/físico/histórico/paleo) + geometrias versionadas + `spatialUncertainty`.

#### `GeoReference`
- **Finalidade.** Como um claim/evento se ancora no espaço, quando não é um `Place` nomeado.
- **Campos.** `geometryType` (`ponto`/`polígono`/`multipolígono`/`linha`/`sem-localização`), `coordinatesRef` (ou `placeRef`/`regionRef`), `spatialUncertainty`, `validTimeRange` (a qual época esta geometria pertence).

#### `GeometryVersion`
- **Finalidade.** Uma forma específica de um `Place`/`Region` **válida num intervalo de tempo**.
- **Campos.** `geometry` (vetorial), `validTimeRange`, `sourceRef`, `licenseProfileRef`, `geometryKind` (`fronteira moderna`/`fronteira histórica`/`território aproximado`/`paleogeografia`).
- **Herda do portão.** Geometria de OSM (ODbL) ou MapBiomas (SA) → `allowedUse = isolated-layer` (camada isolada); geoBoundaries/Natural Earth (CC BY/PD) → núcleo.

#### `GazetteerLink`
- **Finalidade.** Reconciliação com gazetteers autoritativos.
- **Campos.** `gazetteer` (Pleiades/WHG/GeoNames/PeriodO), `externalId`, `linkType` (`exato`/`aproximado`).
- **Herda do portão.** Pleiades/WHG são A/B (entram como fonte); Wikidata, se usado, é **só índice** (Tarefa 7).

#### `PaleogeographicPosition`
- **Finalidade.** Posição **rotacionada por idade** no tempo profundo (placas tectônicas).
- **Campos.** `ageMa`, `rotatedGeometry`, `plateModelRef` (GPlates/EarthByte), `uncertaintyNote`.
- **Herda do portão.** Sempre `claimType = reconstrução modelada`, rótulo obrigatório (C2); dados EarthByte são CC BY 3.0 (entram com atribuição); Deep Time Maps (proprietário) é proibido.

#### `ModernCorrespondence`
- **Finalidade.** O coração da **lente Brasil** (D8): liga um lugar/território histórico ou paleo às unidades administrativas **de hoje**.
- **Campos.** `historicalRef` (place/region/geometria histórica), `modernUnits[]` (país/estado/município atuais que cobrem aquele espaço), `correspondenceType` (`contido-em`/`sobrepõe`/`aproximado`), `note`.
- **Exemplo.** Capitania de Minas Gerais (1789) → estado de Minas Gerais (hoje); sítio de sambaqui → município atual.

#### `SpatialUncertainty`
- **Finalidade.** Incerteza de localização (lugar inferido, território difuso, evento sem ponto exato).
- **Campos.** `uncertaintyKind` (`localização inferida`/`fronteira difusa`/`sem localização precisa`/`reconstrução`), `radiusOrBuffer`, `note`.

### 5.3 Como o modelo responde "e no território que hoje é o Brasil em 1789?"

1. **Resolver** o polígono do Brasil **atual** (geoBoundaries/Natural Earth).
2. **Selecionar** todo item com `TimeRange` intersectando 1789 **e** cuja geometria, **válida em 1789** (`GeometryVersion.validTimeRange`), se relacione ao polígono atual via `ModernCorrespondence` (`contido-em`/`sobrepõe`).
3. **Retornar** Inconfidência Mineira (capitania de Minas → MG hoje), além de processos simultâneos no território (economia mineradora, ocupação, povos indígenas), cada um com fonte e confiança.
4. **Nota epistêmica.** A pergunta é honesta sobre anacronismo: "Brasil" não existia como hoje em 1789; a `ModernCorrespondence` faz a ponte **sem** reescrever a história — o item histórico mantém sua própria geometria e nome de época.

---

## 6. Relationship Graph

### 6.1 Papel

O grafo é o que transforma um catálogo de itens num **conhecimento navegável**: sustenta simultaneidade, trilhas, correlações interdisciplinares, navegação por contexto e os dossiês de evento. Toda aresta é um `Relationship` tipado (Família D); arestas **afirmativas** (causou, influenciou) são elas próprias claims, com fonte e confiança.

### 6.2 Tipos de relação (`relationType`)

| Grupo | Tipos | Natureza |
|---|---|---|
| **Causais/influência** | `causou`, `influenciou`, `afetou` | **afirmativas** → exigem fonte A/B + `claimType` + confiança |
| **Temporais** | `ocorreu-durante`, `ocorreu-antes`, `ocorreu-depois`, `contemporâneo-de` | derivam do eixo temporal (Tarefa 4); base da simultaneidade |
| **Composicionais** | `parte-de`, `sucessor-de`, `predecessor-de` | estrutura de trilhas e cadeias |
| **Associativas** | `relacionado-a`, `equivalente-aproximado` | correlações e pontes interépoca/intertema |
| **Espaciais** | `localizado-em` | liga itens a `Place`/`Region` (Tarefa 5) |
| **Epistêmicas** | `evidenciado-por`, `contradito-por`, `hipótese-concorrente`, `versão-historiográfica` | sustentam claim-first e controvérsia (Tarefa 3) |

### 6.3 Como o grafo sustenta cada capacidade

- **Simultaneidade.** `contemporâneo-de` é, na prática, **derivado** da interseção temporal — o grafo materializa as conexões mais relevantes para que a função central (D4/A6) retorne contexto curado, não só uma lista bruta de tudo que coincide no tempo.
- **Trilhas de conhecimento.** Cadeias de `parte-de`/`sucessor-de`/`influenciou` constroem percursos ("da máquina a vapor à industrialização à urbanização") que a Output Layer (Etapa 9) depois recorta pedagogicamente.
- **Correlações interdisciplinares.** `relacionado-a` entre itens de temas distintos (Lavoisier ↔ Revolução Francesa; oxigênio atmosférico ↔ evolução da vida) habilita a leitura interdisciplinar que diferencia o produto.
- **Navegação por contexto.** A partir de qualquer item, o grafo dá os vizinhos por tipo de relação — é a estrutura que a Experience Layer (Etapa 10) percorre.
- **Dossiês de evento.** O dossiê de um `Event` é, conceitualmente, o item **mais** seus claims **mais** suas relações de saída agrupadas por tipo **mais** seus assets — tudo já no modelo.
- **Filtros do professor (etapas futuras).** O Content Matching Engine (Etapa 8) percorre o mesmo grafo, mas com **escopo dado por anotações externas** (tags BNCC, recorte regional). O grafo é universal; o filtro é aplicado por fora, sem entrar no núcleo (Tarefa 10).

### 6.4 Invariante do grafo

Uma aresta afirmativa (`causou`, `influenciou`) **sem** fonte A/B e sem `claimType` é rejeitada — não se afirma causalidade sem proveniência. Arestas puramente estruturais/temporais (`parte-de`, `ocorreu-durante`) derivam de campos já fonteados dos itens e não exigem fonte adicional.

---

## 7. Governança, licença e proveniência

Esta seção **incorpora obrigatoriamente** a Etapa 1.1: o portão deixa de ser documento operacional e vira **invariante de modelagem**. Todo item factual do KC carrega `ProvenanceMetadata` + `LicenseProfile` + `sourceTier` + `authorityType` + `licenseRiskLevel` + `attributionText` + `provenanceChain` + `allowedUse` + `ingestionDecision` + `reviewStatus`, e — pela espinha epistêmica — `claimType` + `confidenceLevel`. Sem esses campos, o item não existe no núcleo.

### 7.1 Como impedir claim sem fonte A/B

Invariante: `Claim.sourceRef.authorityType ∈ {primary, aggregator}` (A/B). Se a única origem é índice (C — Wikidata/Wikipedia/IA), o item **não entra como claim**; no máximo, vira ligação de reconciliação (7.4). Operacionalmente é o hard stop 1 da Etapa 1.1 elevado a invariante do modelo: a entidade `Claim` é **inconstruível** sem `citation` para fonte A/B.

### 7.2 Como impedir item NC como expressão

`LicenseProfile.nonCommercial = true` + item é **expressão** → `allowedUse` não pode ser `knowledge-core`; o caminho é `FATO` (fato re-derivado de fonte livre) ou `rejected`. A expressão NC (texto, gráfico, scan) nunca entra; o **fato** subjacente entra recodificado, de outra fonte A/B livre, com `provenanceChain` registrando a derivação. Casos canônicos: Seshat, gráfico do ICS, scans do David Rumsey, GADM.

### 7.3 Como isolar ShareAlike/ODbL

`LicenseProfile.shareAlikeRequired = true` (CC BY-SA, ODbL) → `allowedUse = isolated-layer`. A modelagem mantém esses dados **fisicamente/logicamente separados** do núcleo proprietário, para a obrigação copyleft **não atravessar a fronteira**. `GeometryVersion` de OSM, raster de MapBiomas, imagem CC BY-SA do Commons vivem em camadas isoladas que o núcleo **referencia**, mas não **incorpora**. A fronteira "núcleo × camada isolada" é decisão de modelagem (Etapa 1.1, Tarefa 7.3), não verificação ad hoc.

### 7.4 Como tratar Wikidata (e índices) como índice

`authorityType = index` (C) define um **subsistema de reconciliação separado**, sem poder de afirmar. Wikidata/Wikipedia/DBpedia/VIAF entram só como `GazetteerLink`/`authorityLinks` — resolvem "este 'Paris' é o mesmo 'Paris'", "esta pessoa é o mesmo Lavoisier" — e **jamais** aparecem como `sourceRef` de um `Claim`. Modelar índice e autoridade como subsistemas distintos resolve a regra "Wikidata é ponte, não autoridade" como **estrutura**, não como recomendação (Etapa 1.1, Tarefa 7.2).

### 7.5 Como tratar IA generativa

IA é `authorityType = index`, **nunca** fonte factual (A3/Q5). No modelo, conteúdo de IA só pode existir como **narrativa rotulada** (fora do núcleo factual), com `reviewStatus = pending` até curadoria humana e rótulo de IA permanente. Imagem de IA, se usada, é `MediaAsset` com `natureLabel = "representação artística / aproximação didática gerada por IA"` + revisão humana obrigatória. A IA **não cria, altera nem "completa"** claims, fontes, níveis de confiança ou geometria.

### 7.6 Como bloquear itens pendentes de revisão

`ReviewStatus.status ∈ {pending, rejected, legal-review}` ou `ingestionDecision = blocked` → **invariante de exibição**: o item não é consultável nem exibível pela Experience Layer e não aparece em nenhuma consulta de simultaneidade. Publicação é função de estado, não de boa vontade. Tópico sensível/controverso/NC/sem licença → `reviewStatus = pending` por padrão (Etapa 1.1, Tarefas 1 e 4).

### 7.7 Protótipo só toca fontes "verdes"

Coerente com a Etapa 1.1 (Tarefa 7.8): qualquer modelagem-piloto futura (Etapa 12+) só instancia itens de fontes Risco 0/1 (e, no máximo, 2 com confirmação): NASA, Macrostrat, Natural Earth, geoBoundaries, PBDB, IBGE, Pleiades, OWID, World Bank, BNCC. **Nada de Risco 4/5** (Seshat, GADM, ACLED, David Rumsey, Deep Time Maps) entra como expressão.

---

## 8. Camadas especiais (States)

### 8.1 O conceito de `State`

Além de `Event` (pontual) e `Process` (estendido), o KC precisa representar **a condição de um sistema durante um intervalo** — "como era a atmosfera", "onde estavam os continentes", "qual o clima", "qual a configuração de uma civilização". Isso é um **`State`**: um subtipo de `KnowledgeItem` que descreve o **estado de um sistema** sobre um `TimeRange` e um `Place`/`Region`, sustentado por claims e fontes.

`State` é o que o **globo renderiza** quando o usuário para num instante: não um ponto, mas o *pano de fundo* daquele momento. Distingue-se do evento (que *acontece*) e do processo (que *transcorre*): o estado *é* num intervalo.

**Esquema comum a todo `State`:**
`stateId`, `stateType` (uma das dez abaixo), `timeRange`, `regionRef`/`geoReference`, `valueClaims[]` (os claims que descrevem o estado), `sourceRefs[]`, `claimType` (quase sempre `inferência`/`reconstrução` em tempo profundo), `confidenceLevel`, `uncertaintyProfile`, `transitionsFrom`/`transitionsTo` (eventos/processos que mudam o estado).

### 8.2 As dez camadas e suas conexões

| State | O que descreve | Fonte típica (Etapa 1) | Conexão a eventos/períodos/lugares/claims |
|---|---|---|---|
| **AtmosphereState** | composição/química atmosférica num intervalo | NOAA/NCEI Paleo; literatura revisada | transição causada por `Process` (GOE); `valueClaims` = % O₂ como inferência rotulada |
| **TectonicState** | configuração de placas/limites | GPlates+EarthByte | base do `PaleogeographicState`; muda por processos (orogenia, rifteamento) |
| **PaleogeographicState** | posição de continentes/oceanos por idade | GPlates+EarthByte (`PaleogeographicPosition`) | o que o globo mostra em tempo profundo; sempre `reconstrução modelada` |
| **ClimateState** | clima/temperatura num intervalo | NOAA/NCEI, Berkeley Earth, Copernicus | contextualiza vida/civilização; profundo = inferência, moderno = medição |
| **BiomeState** | biomas/cobertura vegetal | MapBiomas (Brasil, SA → isolado), PBDB para contexto | liga `Species`/evolução a `Region`; muda por clima/eventos |
| **CivilizationState** | configuração de uma sociedade/política num intervalo | WHG, Pleiades, fontes A primárias (Seshat só como leitura) | conecta povos, lugares, eventos; controvérsias via `ClaimSet` |
| **TechnologyState** | tecnologias disponíveis/difundidas | OWID, literatura, museus | liga `Technology` a período/região; sustenta trilhas tecnológicas |
| **PopulationState** | população/demografia num intervalo | OWID, World Bank, IBGE (Brasil) | indicador contemporâneo e histórico; medição vs. estimativa |
| **CulturalState** | produção/movimentos culturais num intervalo | acervos, bibliotecas digitais, IPHAN | conecta arte/cultura a tempo/lugar; mídia em camada isolada |
| **EconomicState** | configuração econômica num intervalo | OWID, World Bank, IPEA/IBGE | liga economia a período/região; indicadores com fonte e confiança |

### 8.3 Por que States, e não só eventos

Sem `State`, "o que acontecia há 2,4 Ga?" só devolveria eventos pontuais — mas o interessante ali é o **pano de fundo** (atmosfera oxidando, continentes em outra posição, clima distinto). States são o que dá **profundidade de cena** à simultaneidade e ao globo, e o que mais exige rotulagem de incerteza (C2/D7): quase todo State de tempo profundo é inferência/reconstrução, nunca observação.

---

## 9. Exemplos completos

Seis registros conceituais (não código), cada um mostrando como o modelo se instancia. Campos abreviados por legibilidade; toda fonte respeita o portão da Etapa 1.1.

### 9.1 Big Bang
- **Item.** `Event`/`Process` `evt:big-bang` · `itemType = event` (com fase de processo) · tema: universo, cosmologia.
- **TimeRange.** `DeepTimeAge ≈ 13,8 Ga` (± ~0,02 Ga) · `precision = Ga` · `claimType = inferência científica`.
- **Place/Region.** `sem-localização` (o espaço-tempo origina-se aqui) · `SpatialUncertainty = sem localização precisa`.
- **Claims.** "O universo observável iniciou expansão há ~13,8 Ga" (`inferência científica`, confiança alta, evidência = `dado modelado` + observação CMB). "A inflação cósmica é o mecanismo proposto para os primeiros instantes" (`hipótese`, confiança média).
- **Sources.** NASA (PD, A); literatura cosmológica revisada (A/B). `provenanceChain` registra a cadeia.
- **Confidence.** alta para a expansão; média para inflação (separadas em claims distintos).
- **Relationships.** `predecessor-de` formação do Sistema Solar; `relacionado-a` `Concept` "expansão do universo".
- **Media/Map.** ilustrações rotuladas `representação artística` / `reconstrução modelada`; nenhuma "fotografia" do evento.
- **Na simultaneidade.** é a **âncora inicial** do eixo; "o que acontecia há 13,8 Ga?" retorna este item + `ClimateState`/`AtmosphereState` inexistentes (universo primordial), tudo rotulado como inferência.

### 9.2 Grande Evento de Oxidação (GOE)
- **Item.** `Process` `proc:goe` · tema: Terra, atmosfera, vida.
- **TimeRange.** ~2,4–2,0 Ga · `rangeKind = processo longo` · `TimeUncertainty` ampla · `claimType = inferência científica`.
- **Place/Region.** global; `PaleogeographicState` associado (crátons arqueanos em posições reconstruídas).
- **Claims.** "O O₂ atmosférico subiu significativamente a partir de ~2,4 Ga" (`inferência científica`, confiança alta, evidência = registro geoquímico). "Cianobactérias fotossintetizantes são a causa principal proposta" (`interpretação/inferência`, confiança média-alta).
- **Sources.** NOAA/NCEI Paleo (PD, A); PBDB para contexto biótico (CC BY, A); literatura (A/B).
- **Confidence.** alta para a subida de O₂; média para atribuição causal fina.
- **Relationships.** `AtmosphereState` (pré-GOE → pós-GOE) `transitionsFrom`/`transitionsTo`; `afetou` evolução da vida; `ocorreu-durante` Paleoproterozoico.
- **Media/Map.** reconstrução paleogeográfica (EarthByte, CC BY, `reconstrução modelada`); gráficos próprios de O₂ (recriados dos dados, não do gráfico alheio).
- **Na simultaneidade.** é o **caso-teste de honestidade epistêmica** da Etapa 0: "há 2,4 Ga?" devolve o GOE + States, todos rotulados como inferência com nota de incerteza.

### 9.3 Pangeia
- **Item.** `PaleogeographicState`/`Concept` `state:pangeia` · tema: tectônica, paleogeografia.
- **TimeRange.** supercontinente reunido ~335–175 Ma (montagem/fragmentação) · `claimType = reconstrução modelada`.
- **Place/Region.** `Region` paleogeográfica global; `PaleogeographicPosition` por idade (GPlates/EarthByte).
- **Claims.** "Os continentes estiveram reunidos no supercontinente Pangeia entre ~335 e ~175 Ma" (`reconstrução modelada`, confiança alta no fato da reunião, **incerteza nas posições finas**).
- **Sources.** EarthByte/GPlates (CC BY 3.0, A); literatura (A/B). `plateModelRef` registrado.
- **Confidence.** alta para a existência; incerteza explícita nas bordas e posições (`UncertaintyProfile.modelDependence = true`).
- **Relationships.** `TectonicState` subjacente; `predecessor-de` configuração continental atual; `afetou` `ClimateState`/`BiomeState` do período.
- **Media/Map.** `MapAsset` de reconstrução (EarthByte, `reconstrução modelada`) — **nunca** apresentado como fotografia/mapa observado.
- **Na simultaneidade.** "o que acontecia há 250 Ma?" troca o globo para a reconstrução de Pangeia (rotulada) + `ClimateState`/extinções do entorno.

### 9.4 Revolução Francesa
- **Item.** `Event`/`Process` `evt:revolucao-francesa` · tema: história, política.
- **TimeRange.** 1789–1799 (processo), com eventos pontuais internos (Queda da Bastilha, 14/07/1789) · `precision = dia` para os pontuais · `claimType = fato documentado`.
- **Place/Region.** `Place` Paris; `Region` França (com `GeometryVersion` de fronteira da época).
- **Claims.** "A Queda da Bastilha ocorreu em 14/07/1789" (`fato documentado`, confiança alta, evidência = documento primário). Interpretações sobre causas → `ClaimSet` com `interpretação historiográfica` (várias leituras, fontes visíveis).
- **Sources.** Arquivos/bibliotecas (A); literatura historiográfica (A/B). Wikidata só para reconciliar identidades (índice).
- **Confidence.** alta para fatos datados; leituras causais em `ClaimSet` (`em disputa` quando for o caso).
- **Relationships.** `contemporâneo-de` Inconfidência Mineira e primeiro governo dos EUA; `influenciou` independências; `relacionado-a` Lavoisier (ciência simultânea).
- **Media/Map.** imagens de época PD (provedor PD-explícito); mapas históricos PD; tudo com `natureLabel`.
- **Na simultaneidade.** é a **cena canônica**: foco em Paris/1789, e "o que acontecia no mundo?" acende Minas Gerais, EUA e a ciência (Lavoisier) — todos com seus rótulos.

### 9.5 Inconfidência Mineira
- **Item.** `Event`/`Process` `evt:inconfidencia-mineira` · tema: história do Brasil.
- **TimeRange.** articulação ~1788–1789; desmantelamento em 1789 · `precision = ano/dia` · `claimType = fato documentado`.
- **Place/Region.** `Place` Vila Rica (hoje Ouro Preto); `Region` Capitania de Minas Gerais (1789) com `GeometryVersion` histórica; `ModernCorrespondence → Minas Gerais (hoje)`.
- **Claims.** "A Inconfidência Mineira foi desmantelada em 1789" (`fato documentado`, confiança alta, evidência = documento primário/Arquivo Nacional). Leituras sobre alcance e motivações → `ClaimSet` (`interpretação historiográfica`).
- **Sources.** Arquivo Nacional, Biblioteca Nacional (A, itens muito PD); IBGE para a base territorial (aberto, A). Respeita Leis 10.639/2003 e 11.645/2008 no entorno (povos e território).
- **Confidence.** alta para fatos; interpretações em `ClaimSet`.
- **Relationships.** `contemporâneo-de` Revolução Francesa; `localizado-em` Minas Gerais; `relacionado-a` ciclo do ouro e ocupação do território.
- **Media/Map.** documentos PD; mapas históricos da capitania (provedor PD); rótulos de natureza.
- **Na simultaneidade.** é o que a lente Brasil (D8) acende quando o foco está em 1789 — a resposta direta a "e no território que hoje é o Brasil?".

### 9.6 Apollo 11
- **Item.** `Event` `evt:apollo-11` · tema: ciência, tecnologia, exploração espacial.
- **TimeRange.** lançamento 16/07/1969; pouso 20/07/1969 (~20:17 UTC) · `precision = minuto` · `claimType = fato documentado` / `medição direta`.
- **Place/Region.** `Place` Centro Espacial Kennedy (lançamento); `Place` Mar da Tranquilidade, Lua (pouso) — geometria extraterrestre, `GeoReference` com referência lunar.
- **Claims.** "A Apollo 11 pousou na Lua em 20/07/1969" (`fato documentado`, confiança alta, evidência = registro/medição). Dados de trajetória/telemetria (`medição direta`).
- **Sources.** NASA (PD, A — imagens, telemetria, efemérides). `attributionText` registrado (boa prática).
- **Confidence.** alta (registro instrumental e documental abundante).
- **Relationships.** `parte-de` programa Apollo; `sucessor-de` missões anteriores; `relacionado-a` corrida espacial (contexto geopolítico via `Relationship` fonteada).
- **Media/Map.** fotografias NASA (PD, `natureLabel = fotografia`); vídeo PD; nenhuma reconstrução apresentada como registro.
- **Na simultaneidade.** "o que acontecia em julho de 1969?" retorna Apollo 11 + `EconomicState`/`PopulationState`/eventos contemporâneos (OWID/World Bank na ponta presente do eixo).

---

## 10. Fronteira com camadas futuras

### 10.1 O que fica **fora** do Knowledge Core

Nenhum destes é entidade, campo ou tabela do núcleo:

- **BNCC** — competências, habilidades, áreas, componentes curriculares (Compliance Layer, Etapa 6);
- **currículo estadual/municipal** e referenciais locais (Compliance/Planning, Etapas 6–7);
- **planejamento do professor** — série, disciplina, bimestre, temas, objetivos, nível da turma (Planning Layer, Etapa 7);
- **planos de aula, roteiros, trilhas pedagógicas** (Output Layer, Etapa 9);
- **quizzes, avaliações, rubricas, atividades, material do aluno** (Output Layer, Etapa 9);
- **modo professor / modo estudante / qualquer tela** (Experience Layer, Etapa 10);
- **dados de aluno/turma, matrícula, desempenho** (transversal de privacidade; LGPD/menores);
- **personalização educacional** (perfis, recomendação pedagógica);
- **analytics de uso** (telemetria ética, transversal);
- **integração LMS** (conector externo).

### 10.2 Por que ficam de fora (o princípio)

Tudo acima é **contingente** (varia por país, rede, escola, ano, turma, lei educacional vigente); o KC é **universal e estável**. Misturar o contingente no núcleo o tornaria não-reutilizável e o amarraria à BNCC — exatamente o que P1/P2 e a tese da Etapa 0 proíbem. A BNCC pode mudar; o fato de o Jurássico começar em ~201,4 Ma, não.

### 10.3 Como essas camadas se conectam sem contaminar

Três mecanismos, já antecipados em 1.5:

1. **Referência por ID estável, sempre de fora para dentro.** Cada camada externa mantém **seus próprios registros** que apontam para `knowledgeItemId`/`claimId` do núcleo. Exemplo: um `BNCCMapping` (entidade da Etapa 6, **não** do KC) liga a habilidade `EF08HI06` aos itens `evt:revolucao-francesa` e `evt:inconfidencia-mineira`. O KC não sabe que esse mapeamento existe.

2. **Direção única de dependência.** O grafo de dependências aponta **para o núcleo**: Experience → Output → Matching → Planning → Compliance → **Knowledge Core**. O núcleo não tem nenhuma referência de saída para essas camadas. Apagar qualquer camada externa não deixa campo órfão no KC (teste de P2).

3. **Interface de leitura por índices universais.** As camadas externas consultam o KC pelos mesmos índices da simultaneidade — tempo, espaço, tema, tipo de claim, confiança — e aplicam **seus** filtros (tags BNCC, recorte regional, faixa etária) **por fora**. O Content Matching Engine (Etapa 8) é, para o núcleo, apenas mais um leitor desses índices. A adaptação de linguagem por faixa etária (IA, A3/Q5) opera sobre a **saída**, nunca alterando claims do núcleo.

**Resultado:** o KC permanece soberano e universal; a conformidade brasileira, o planejamento docente e a experiência se acoplam como **leitores e anotadores externos** — o produto é compatível com a educação brasileira sem que essa compatibilidade entre no núcleo.

### 10.4 Diagrama de fronteira (conceitual)

```
            CAMADAS EXTERNAS (contingentes)
   Experience · Output · Matching · Planning · Compliance
        │ apontam para dentro por knowledgeItemId
        │ (anotam, filtram, narram — nunca afirmam fato novo)
        ▼
 ┌───────────────────────────────────────────────┐
 │              KNOWLEDGE CORE (universal)         │
 │  KnowledgeItem · Claim · Source · Relationship  │
 │  TimeRange · GeoReference · States · Media      │
 │  + ProvenanceMetadata em TODO item factual      │
 │  → não tem nenhuma referência de saída ←        │
 └───────────────────────────────────────────────┘
        ▲
        │ índices de leitura (tempo · espaço · tema · tipo · confiança)
        │ subsistema de reconciliação (índices C: Wikidata/VIAF) — só identidade
```

---

## 11. Decisões pendentes para etapas futuras

Itens que esta modelagem **deliberadamente não fecha** — por pertencerem a etapas próprias ou dependerem de validação:

1. **Validação numérica da espinha dorsal (A5/D5).** A modelagem é compatível com 150–300 nós / 1.500–3.000 eventos, mas o número fino só se fecha confrontando esta estrutura com a granularidade real desejada — tarefa de seleção de conteúdo, não de modelagem. Não congelado.
2. **Política editorial de controvérsias (R3/C3).** O modelo já provê `ClaimSet`/`consensusStatus`/`hipótese-concorrente`/`interpretação historiográfica`; **qual** controvérsia destacar e **como** narrá-la (colonização, escravidão, povos indígenas, evolução, Big Bang) é decisão editorial a escrever **antes da Etapa 4**.
3. **Datum e unidade exata do eixo canônico (Tarefa 4).** Decidiu-se *dupla representação* e *datum fixo*; a escolha precisa do ponto de referência (1950 BP vs. J2000) e da costura log/linear é detalhe a fixar na Etapa 3 (timeline) junto ao design da navegação multiescala.
4. **Fronteira física núcleo × camada isolada SA/ODbL (L2/7.3).** O **princípio** está fixado (isolamento obrigatório); a fronteira concreta de armazenamento é decisão da Etapa 11 (arquitetura técnica), não desta.
5. **Cadência de atualização por fonte (C5).** Quais fontes (OWID/World Bank/IBGE) atualizam com que frequência e como se versiona o `DatasetSnapshot` é decisão operacional da Etapa 13 (pipeline).
6. **Vocabulários controlados finais.** As enums (`claimType`, `eventKind`, `regionKind`, `natureLabel`, `relationType`) estão definidas em conteúdo; sua normalização final (e mapeamento a padrões externos como PeriodO/CIDOC-CRM, se adotados) é refinamento das Etapas 3–4.
7. **Modelo de identidade de `Entity` pessoa vs. privacidade.** Pessoas históricas são conhecimento; quaisquer pessoas vivas exigem revisão (LGPD/R4) — regra a detalhar com a transversal de privacidade antes de ingerir entidades contemporâneas sensíveis.
8. **Confirmação de licença por asset (Etapa 1.1, §5.3).** A checklist de confirmação por asset é pré-requisito da ingestão (Etapa 13); a modelagem só garante que **há campo** para registrar a decisão (`ProvenanceMetadata`), não a decisão em si.

---

## Encerramento e handoff

Esta modelagem entrega um Knowledge Core **universal, claim-first, espaço-temporal, com proveniência obrigatória e incerteza tipada**, em que a simultaneidade ("o que acontecia no mundo neste momento?") é propriedade emergente dos índices, não módulo à parte (D4/A6), e em que a educação brasileira se acopla por fora, sem entrar no núcleo (P1/P2, Tarefa 10). Todo item factual nasce obrigado pelo portão da Etapa 1.1.

**Handoff para as próximas etapas (quando solicitadas):**
- **Etapa 3 (timeline + globo 3D)** consome o eixo canônico (Tarefa 4), as `GeometryVersion`/`PaleogeographicPosition` (Tarefa 5) e os `States` (Tarefa 8) como o que se renderiza.
- **Etapa 4 (camadas científicas/históricas)** popula os `States` e os `Event`/`Process` por camada, sob a política editorial pendente (item 11.2).
- **Etapa 5 (simultaneidade)** detalha a consulta de interseção já estruturada nas Tarefas 4–6.
- **Etapas 6–9** acoplam BNCC, planejamento, matching e saída pedagógica como **leitores/anotadores externos** (Tarefa 10).

*Documento de entrega da Etapa 2, sob a baseline v1.0, a auditoria da Etapa 1 e o portão da Etapa 1.1. Não escreve código de aplicação, não propõe MVP, não define stack, não avança para UX/UI nem para pipeline. Próxima etapa, quando solicitada: Etapa 3 — Linha do tempo e mapa/globo 3D.*
