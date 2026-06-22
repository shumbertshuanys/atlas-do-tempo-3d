# Etapa 5 — Função “O que acontecia no mundo neste momento?”

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da **Etapa 5** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, a arquitetura de camadas (4A) e o método/`Scene` v1.1 consolidado (4F, 4H, 4Z) · 12/06/2026
**Escopo desta etapa (e seus limites):** **generalizar a função central do produto** — transformar as três cenas-gabarito (1789, 2,4 Ga, 66 Ma) em uma **capacidade reutilizável** do Knowledge Core que consulta tempo, espaço, camadas, claims, States, relações, publicabilidade e incerteza, e **produz** respostas e cenas reutilizáveis sob `Scene` v1.1. Conforme solicitado, esta etapa **não** cria cena manual nova, **não** povoa conteúdos, **não** escreve código (a notação `{ }`/`txt` abaixo é **dicionário conceitual de campos**, jamais implementação), **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico completo, **não** reabre auditoria de fontes (1/1.1) e **não** reabre política editorial (3.1).

**O que herda e respeita.** A leitura emergente da simultaneidade (Etapa 2, §1.4 / P7 — “a função é interseção dos índices temporal e espacial sobre claims tipados”); o eixo `canonicalTimeScalar` (T0 = 2000.0 CE ≈ J2000) e a preservação de `sourceTimeBasis` (3Z); os quatro mecanismos espaciais `modernGeometry`/`historicalGeometryVersions`/`paleoPositions`/`modernCorrespondence` (Etapa 2 §5 + 4H §5); o modelo claim-first com `claimType`/`ConfidenceLevel`/`EvidenceLevel`/`UncertaintyProfile` (Etapa 2 §3); os 11 `State Types` oficiais (4Z §6); o `RelationshipGraph` (Etapa 2 §6); o invariante de exibição (nada `pending`/`legal-review`/`rejected` aparece como fato ou na simultaneidade — 1.1/3.1); a disciplina anti-falsa-equivalência via `weightedClaimSets` (4H §4); e o padrão `Scene` v1.1 com seus 34 campos (4H §2).

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores. Blocos `txt` são **especificação de campos** — um dicionário —, nunca código executável. Onde se escreve “a função”, lê-se a capacidade `WhatWasHappeningAtMoment` definida na Seção 1.

-----

## Sumário

1. Definição da função como capacidade do Knowledge Core
1. Tipos de consulta
1. Entradas da função (`MomentQuery`)
1. Saídas da função (`MomentResult`)
1. Normalização temporal
1. Normalização espacial
1. Seleção e ranqueamento de itens
1. Publicabilidade e gating
1. Anacronismo e equivalência
1. Geração de `Scene` candidate
1. Padrões de resposta por tipo de consulta
1. Modos de resultado
1. Limites da função
1. Próximos passos para a Etapa 6

-----

## 1. Definição da função como capacidade do Knowledge Core (Tarefa 1)

### 1.1 Nome e natureza

A capacidade chama-se **`WhatWasHappeningAtMoment`** (gloss em português: *“O que acontecia no mundo neste momento?”*; nome curto de consulta: **função de momento**).

Ela é uma **capacidade de leitura do Knowledge Core**, não uma feature de UI. Isso tem três consequências estruturais:

1. **É a materialização da propriedade emergente P7.** A Etapa 2 (§1.4) já estabeleceu que a simultaneidade *não é módulo à parte*: é a **interseção dos índices temporal e espacial sobre claims tipados**. A função de momento é o nome dessa interseção quando exposta como serviço de consulta reutilizável. As cenas-gabarito 4D/4E/4G são **instâncias** dessa função; a Etapa 5 a torna **geral**.
1. **É somente leitura.** A função **nunca** escreve no núcleo: não cria `KnowledgeItem`, não cria `Claim`, não cria aresta, não altera `reviewStatus`. Ela **consulta** o KC e **compõe** um resultado (`MomentResult`) e, opcionalmente, uma **cena candidata** (`Scene` v1.1). Toda criação/edição de conteúdo permanece sob curadoria humana (Etapas 4x/13).
1. **As camadas externas a consomem por fora.** Compliance (BNCC, Etapa 6), Planning (7), Matching (8), Output (9) e Experience (10) são **leitoras/anotadoras** do `MomentResult` — aplicam seus filtros (tags, recorte regional, faixa) **sobre a saída**, sem entrar no núcleo (Etapa 2, Tarefa 10). A direção de dependência permanece invertida.

### 1.2 Objetivo, entradas, saídas, dependências

|Aspecto         |Definição                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Objetivo**    |Dado um instante/intervalo (de qualquer regime: cósmico→futuro) e um recorte espacial (de “sem lugar” a “global”, de paleoposição a território atual), retornar **o que coexistia** ali e então — itens de foco, simultâneos, States de fundo, evidências, debates e consequências — cada um com **tempo, espaço, tipo de claim, fonte, confiança, incerteza e publicabilidade**, e (quando couber) uma **cena reutilizável** sob `Scene` v1.1.|
|**Entradas**    |Um objeto `MomentQuery` (Seção 3).                                                                                                                                                                                                                                                                                                                                                                                                             |
|**Saídas**      |Um objeto `MomentResult` (Seção 4), opcionalmente contendo um `generatedSceneCandidate` (`Scene` v1.1; Seção 10).                                                                                                                                                                                                                                                                                                                              |
|**Dependências**|Etapa 2 (KC), 3 (timeline/globo), 3Z (datum), 3.1 (política editorial), 4A (camadas), 4F (padrão genérico), 4H (`Scene` v1.1), 4Z (handoff); cenas 4D/4E/4G **como exemplos, não como modelos novos**.                                                                                                                                                                                                                                         |

### 1.3 Entidades consumidas

A função **lê** (nunca grava) as seguintes entidades e objetos de valor:

`KnowledgeItem` (e subtipos `Event`/`Process`/`Concept`/`Entity`) · `Place` · `Region` · os 11 `State Types` · `Claim` · `ClaimSet` (e `WeightedClaim`) · `Source` · `Citation` · `Relationship` · `MediaAsset`/`MapAsset` · e os objetos de valor `TimeRange`, `ConfidenceLevel`, `EvidenceLevel`, `UncertaintyProfile`, `ModernCorrespondence`, `PaleoPosition`, `ProvenanceMetadata`, `ReviewStatus`.

### 1.4 Como a função usa cada subsistema

- **`TimeRange` / `canonicalTimeScalar`.** A consulta converte `timeInput` para o eixo único (T0 = 2000.0 CE) e seleciona todo item cujo intervalo `[canonicalStart, canonicalEnd]` **intersecta** o intervalo consultado. É o que permite intersectar **regimes diferentes no mesmo eixo** (1789 e 2,4 Ga). A exibição usa `displayTime` por regime, **nunca** o escalar cru (3Z §4).
- **`Place`/`Region`/`paleoPosition`/`modernCorrespondence`.** A consulta resolve `spatialInput` para um `normalizedSpatialScope` e escolhe **qual geometria** usar por regime: `modernGeometry` (atual), `historicalGeometryVersions` (histórico documentado), `paleoPositions` (tempo profundo, sempre rotulada/incerta) e `modernCorrespondence` (a **lente** “o que hoje é…”, para a lente Brasil de D8). O usuário **sempre vê** qual está em uso (4H §5).
- **`States`.** A função recupera as **condições de fundo** do momento (atmosfera, oceano, clima, biosfera, civilização, economia, população…) como contexto que não é “evento”, mas é parte do que “acontecia”. Em tempo profundo, os States **dominam** o resultado (4E).
- **`Claims` / `ClaimSets` / `UncertaintyProfiles`.** Cada item carrega seu `claimType`, `confidenceLevel` e `evidenceLevel` — a função os **anexa** ao resultado para a interface separar fato × inferência × hipótese × reconstrução (D7). Debate legítimo entra como `ClaimSet` (lados **discretos**); incerteza entra como `UncertaintyProfile` (**faixa**, não lados). Essa distinção é mantida rigidamente (4F/4H).
- **`RelationshipGraph`.** O grafo fornece **relevância curada**: `contemporâneo-de` materializa simultaneidade significativa (não a lista bruta de tudo que coincide); `causou`/`possibilitou`/`decorreu-de`/`afetou` alimentam “consequências” e “antes/depois”; `evidenciado-por` alimenta o bloco “como sabemos”; e os vizinhos por tipo de relação alimentam `navigationSuggestions`.
- **`publicabilityStatus` / `reviewStatus`.** A função aplica o **invariante de exibição**: item `pending`/`legal-review`/`rejected` **não** aparece como fato nem entra na simultaneidade pública. A função agrega um `publicabilityStatus` (1–5) e nomeia o `gatingReason` (Seção 8).
- **Anacronismo.** A função produz `anachronismWarnings` e exclui itens **não contemporâneos** ao recorte (ex.: Mali em 1789, Pangeia em 2,4 Ga), usando `modernCorrespondence` no histórico e `paleoPosition` no profundo (Seção 9).
- **Falsa equivalência.** A função respeita `weightedClaimSets`: claims com pesos assimétricos exibem hierarquia; negacionismo é **objeto rotulado-rejeitado fora do `ClaimSet`**, nunca “lado” (Seção 9).
- **`sourceTimeBasis`.** A função **nunca** apaga o datum nativo: o resultado pode mostrar “como a fonte mediu o tempo” (ex.: “12.000 ¹⁴C BP”), com o canônico marcado como derivado (3Z §3).
- **Geração de `Scene` v1.1.** Quando o recorte tem coesão suficiente, a função emite um `generatedSceneCandidate` que **referencia** itens por `knowledgeItemId` (jamais duplica conteúdo) e segue os 34 campos do padrão (Seção 10).

-----

## 2. Tipos de consulta (Tarefa 2)

Treze tipos. Cada um normaliza para o eixo canônico e mapeia para o campo `queryType` da `Scene` (taxonomia 4F §3 / matriz 4H §6).

|# |Tipo (`queryMode`)                    |Exemplo                                        |Entrada esperada            |Normalização temporal                                     |Decisão de `spatialScope`                        |Entidades consultadas                                        |Riscos                                    |Saída esperada                                |
|--|--------------------------------------|-----------------------------------------------|----------------------------|----------------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------|------------------------------------------|----------------------------------------------|
|1 |**Por ano/data**                      |“…em 1789?”                                    |ano ou data ISO             |`1789`→escalar; data→dia                                  |global por padrão; estreitável                   |Event/Process/State + Region                                 |excesso de itens; falsa precisão sub-anual|corte de simultaneidade                       |
|2 |**Por período**                       |“…durante o séc. XVIII?”                       |faixa (datas/séculos)       |faixa→`[start,end]`                                       |global                                           |mistura                                                      |borda difusa; sobrecarga                  |panorama de período                           |
|3 |**Por idade geológica**               |“…há 2,4 Ga?”                                  |Ma/Ga (+faixa)              |Ma/Ga→escalar; offset 50 anos descartado                  |planetário (sem países)                          |State/Process + Place de evidência                           |falsa precisão; paleomapa como fato       |corte planetário                              |
|4 |**Por evento foco**                   |“…ao mesmo tempo que a Queda da Bastilha?”     |`focusItem` (Event)         |herda `timeRange` do foco                                 |herda foco + global                              |foco + `contemporâneo-de`                                    |confundir foco com contexto               |foco + simultâneos                            |
|5 |**Por processo foco**                 |“…durante a Revolução Industrial?”             |`focusItem` (Process)       |herda faixa do processo                                   |região-núcleo + global                           |foco + States + simultâneos                                  |tratar processo longo como ponto          |processo + contexto                           |
|6 |**Por lugar/região**                  |“…na Mesopotâmia em −2000?”                    |`Place`/`Region` + tempo    |tempo→escalar                                             |recorte do lugar (geometria por regime)          |itens `localizado-em` + States                               |geometria pendente                        |corte local                                   |
|7 |**Por território atual (lente)**      |“…no território que hoje é o Brasil em 1789?”  |território atual + tempo    |tempo→escalar                                             |polígono atual → itens via `modernCorrespondence`|itens históricos com `ModernCorrespondence`                  |anacronismo (Brasil-nação)                |corte com lente moderna rotulada              |
|8 |**Por tempo profundo c/ paleoposição**|“…onde ficava o impacto de Chicxulub em 66 Ma?”|`Place` + idade             |idade→escalar                                             |`paleoPosition` (rotulada) ≠ posição atual       |`Place`+`PaleoPosition`+State                                |usar coordenada moderna como antiga       |marcador paleo rotulado                       |
|9 |**Por camada temática**               |“…na ciência em 1789?”                         |tempo + `layerFilters`      |tempo→escalar                                             |conforme camada                                  |itens da(s) camada(s) 4A                                     |recorte que apaga conexões                |lista por camada                              |
|10|**Por antes/depois**                  |“…antes e depois do K-Pg?”                     |`focusItem` + janela ±      |dois cortes ao redor do escalar                           |herda foco                                       |par de States/itens (`ocorreu-antes`/`-depois`)              |sugerir determinismo                      |comparação temporal                           |
|11|**Por consequências**                 |“…o que o GOE causou?”                         |`focusItem` + sentido causal|da origem para frente                                     |herda foco; pode globalizar                      |arestas `causou`/`possibilitou`/`afetou` + `cascadeStructure`|hipótese como cadeia rígida               |cadeia de consequências com confiança decaindo|
|12|**Por comparação**                    |“Brasil × França em 1789?”                     |dois recortes (A,B)         |tempo comum                                               |dois `spatialScope`                              |dois cortes paralelos                                        |falsa simetria entre A e B                |comparação lado a lado                        |
|13|**Por cenário futuro/projetivo**      |“…em 2100 num cenário climático?”              |ano de cenário + modelo     |ano→escalar **positivo**; `sourceTimeBasis = scenarioYear`|global/regional                                  |`Process`/`State` projetivos + modelo                        |projeção exibida como fato                |corte projetivo rotulado                      |


> **Regra transversal:** o `queryMode` define o **comportamento dominante**, mas a função pode combinar tipos (ex.: 7 + 9 = “ciência no território que hoje é o Brasil em 1789”). A combinação **nunca** relaxa o invariante de exibição nem a política de anacronismo.

-----

## 3. Entradas da função — `MomentQuery` (Tarefa 3)

```txt
MomentQuery = {
  queryId,             # id da consulta (para rastreio/cache; não é dado do KC)
  queryText,           # texto livre original do usuário (ex.: "o que acontecia em 1789?")
  queryMode,           # um dos 13 tipos da Seção 2 (inferido do texto ou explícito)
  focusItem,           # knowledgeItemId do item-âncora, quando há foco (Event/Process/...); senão vazio
  timeInput,           # entrada temporal BRUTA, pré-normalização (ano | faixa | Ma/Ga | BP/¹⁴C | ano-cenário)
  spatialInput,        # entrada espacial BRUTA (Place | Region | território-atual | "global" | "sem-lugar")
  layerFilters,        # camadas 4A a incluir/excluir (ex.: só ciência; tudo menos guerra)
  confidenceFilters,   # piso de confidenceLevel/evidenceLevel (ex.: ocultar baixa confiança)
  claimTypeFilters,    # filtro por claimType (ex.: só "fato documentado"; ou incluir "hipótese")
  publicabilityMode,   # contexto de publicabilidade: público | interno-curadoria | pesquisa
  ageLevelMode,        # faixa: 6-8 | 9-11 | 12-14 | 15-17 | adulto/professor (modula profundidade/linguagem/mídia)
  comparisonMode,      # quando comparativo: antes/depois | A×B | nenhum
  includeHiddenSummary,# incluir CONTAGEM/resumo interno de itens ocultos (sem expô-los)
  includeUncertainty,  # anexar UncertaintyProfiles
  includeSources,      # anexar proveniência (Source/Citation/ProvenanceMetadata)
  includeMedia,        # anexar MediaAsset/MapAsset (sempre com natureLabel)
  outputMode           # um dos 10 modos da Seção 12
}
```

**Definição dos campos sensíveis:**

- **`queryMode`** — determina a normalização e o ranqueamento; quando o texto é ambíguo, a função infere e **registra a inferência** (não inventa precisão).
- **`focusItem`** — quando presente, a consulta herda `timeRange`/`spatialScope` do item e prioriza suas relações (`contemporâneo-de`, `causou`…).
- **`timeInput` / `spatialInput`** — sempre **brutos**; a normalização vive nas Seções 5 e 6 e produz `normalizedTimeRange`/`normalizedSpatialScope` no resultado. O bruto é **preservado** (honestidade).
- **`publicabilityMode`** — seleciona o conjunto de gating aplicável: em `público` valem todos os portões; em `interno-curadoria`, itens `pending` podem ser **contabilizados** (não exibidos como fato) para o curador; em `pesquisa`, mais incerteza é exposta, ainda rotulada.
- **`ageLevelMode`** — modula **profundidade, linguagem e mídia**, **nunca** o fato em si (PE-Ed8, 3.1 §6). Em faixas menores, temas sensíveis exigem mediação/ocultação parcial por padrão.
- **`includeHiddenSummary`** — permite dizer “há N itens não exibíveis aqui (em revisão)” **sem** revelar conteúdo — transparência sobre a ausência, sem vazamento.

**Fontes de entrada (como a `MomentQuery` nasce):**

|Origem                                              |Como popula a `MomentQuery`                                                                                                 |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|**Busca livre**                                     |`queryText` → inferência de `queryMode`/`timeInput`/`spatialInput`.                                                         |
|**Busca estruturada**                               |usuário preenche campos diretamente (modo avançado/curadoria).                                                              |
|**Seleção na timeline**                             |a posição/intervalo selecionado vira `timeInput`; `queryMode` = período/ano.                                                |
|**Clique no globo**                                 |o ponto/região vira `spatialInput`; combina com o tempo corrente da timeline.                                               |
|**Clique em evento**                                |o item vira `focusItem`; `queryMode` = evento/processo foco.                                                                |
|**Consulta de professor/aluno/pesquisador (futuro)**|seleciona `ageLevelMode`/`publicabilityMode`; **sem** entrar em currículo — apenas modula profundidade/gating sobre a saída.|

-----

## 4. Saídas da função — `MomentResult` (Tarefa 4)

```txt
MomentResult = {
  query,                  # eco da MomentQuery já normalizada (inclui as inferências feitas)
  normalizedTimeRange,    # TimeRange canônico resolvido (Seção 5), com displayTime por regime
  normalizedSpatialScope, # escopo espacial resolvido (Seção 6), com a geometria escolhida rotulada
  focusSummary,           # síntese do foco, quando há focusItem
  mainItems,              # foco principal (itens-âncora do recorte)
  simultaneousItems,      # simultâneos (centrais + contextuais), já ranqueados (Seção 7)
  states,                 # States de fundo do momento (condições do sistema)
  claimSets,              # debates discretos legítimos (com peso quando preciso)
  uncertaintyProfiles,    # faixas/margens (não "lados")
  hiddenItems,            # itens NÃO exibíveis — referência interna; conteúdo exposto só conforme modo/publicabilidade
  sourceSummary,          # síntese de proveniência A/B por claim relevante
  confidenceSummary,      # síntese de confidenceLevel/evidenceLevel do conjunto
  anachronismWarnings,    # avisos de anacronismo aplicáveis ao recorte (Seção 9)
  equivalenceWarnings,    # avisos anti-falsa-equivalência (Seção 9) — ADIÇÃO ao exemplo do enunciado
  publicabilityStatus,    # nível agregado do resultado (1–5)
  gatingReason,           # razão principal + tipo do gating (editorial/científico/licença/...)
  generatedSceneCandidate,# Scene v1.1 candidata, quando gerada (Seção 10); senão vazio
  navigationSuggestions   # próximos passos: outro lugar/período, consequências, comparar antes/depois
}
```

**Definição dos campos sensíveis:**

- **`mainItems` × `simultaneousItems`** — `mainItems` é o que a consulta tem por foco; `simultaneousItems` é o que **coexistia** e é relevante (categorizado em centrais/contextuais — Seção 7). A separação evita afogar o foco no contexto.
- **`hiddenItems`** — **nunca** expõe conteúdo `pending`/`rejected`/`legal-review` como fato. Em `público`, traz no máximo a **contagem** (se `includeHiddenSummary`); em `interno-curadoria`, lista para revisão.
- **`anachronismWarnings` / `equivalenceWarnings`** — gerados **sempre** que o recorte tocar os gatilhos da Seção 9; ausência de aviso é decisão explícita, não esquecimento.
- **`generatedSceneCandidate`** — presente apenas quando os critérios da Seção 10 são satisfeitos; caso contrário a função retorna **lista**, não cena.
- **`navigationSuggestions`** — derivadas do `RelationshipGraph` (vizinhos por tipo de relação) e do eixo (períodos adjacentes).

**A saída deve poder alimentar:** `timeline` (itens posicionados por `canonicalTimeScalar`, exibidos por `displayTime`) · `globo/mapa` (geometria escolhida e rotulada) · `dossiê` (foco + claims + relações agrupadas + “como sabemos”) · `Scene` v1.1 (`generatedSceneCandidate`) · `comparação antes/depois` (par de cortes) · `navegação para outro lugar` · `navegação para consequências` (cadeia causal).

-----

## 5. Normalização temporal (Tarefa 5)

A função aplica integralmente a Etapa 3Z. Ela:

- **converte** `timeInput` para `canonicalTimeScalar` (anos rel. a T0 = 2000.0 CE; negativo = passado, positivo = futuro), preenchendo `[canonicalStart, canonicalEnd]`;
- **preserva** `sourceTimeBasis` + o valor nativo (jamais apaga o datum da fonte);
- **respeita** `timePrecision` (Ga|Ma|ka|século|década|ano|mês|dia|cenário) e `timeUncertainty` (±/faixa/distribuição);
- **lida com** data exata, século, Ma/Ga, BP/cal BP (com **calibração obrigatória** de ¹⁴C antes do eixo) e futuro projetivo;
- **evita precisão falsa**: a interseção respeita a faixa — um item de borda difusa “aparece” no momento consultado **com a ressalva de incerteza**, não como presença cravada;
- **distingue factual de projetivo** ao responder consultas no lado positivo do eixo (resultado projetivo é **sempre** rotulado como cenário/modelo).

**Exemplos obrigatórios (aplicação de 3Z §6):**

|Entrada           |`sourceTimeBasis`  |`canonical` (anos rel. T0)|`displayTime`     |`timePrecision`|Tratamento na função                                              |
|------------------|-------------------|--------------------------|------------------|---------------|------------------------------------------------------------------|
|**1789**          |gregorianCE        |≈ −211                    |“1789”            |ano            |corte anual; offset de 50 anos **aplicado** (regime histórico)    |
|**1969-07-20**    |ISO 8601           |≈ −30,46                  |“20 jul 1969”     |dia            |corte diário; dados contemporâneos na ponta presente              |
|**~66 Ma**        |Ma (ICS)           |≈ −6,6×10⁷                |“~66 Ma”          |Ma (faixa)     |offset de 50 anos **descartado**; faixa preservada                |
|**~2,4 Ga**       |Ga (NOAA Paleo)    |≈ [−2,4×10⁹, −2,0×10⁹]    |“~2,4 Ga”         |Ga (faixa)     |processo, não ponto; bordas difusas                               |
|**radiocarbon BP**|radiocarbonBP→calBP|derivado do **cal BP**    |“~X anos atrás”   |século/milênio |**¹⁴C bruto preservado mas nunca usado direto**; calibrar primeiro|
|**2050 (cenário)**|scenarioYear       |≈ +50                     |“2050 (cenário X)”|cenário        |lado **positivo**; rótulo de modelo/RCP-SSP obrigatório           |

-----

## 6. Normalização espacial (Tarefa 6)

A função resolve `spatialInput` para `normalizedSpatialScope`, **escolhendo a geometria certa por regime** e **sempre rotulando** qual está em uso (4H §5). Ela lida com:

- **lugar atual** → `modernGeometry`;
- **lugar histórico** / **região histórica** → `historicalGeometryVersions` (vigência por `TimeRange`);
- **território atual como lente moderna** → polígono atual + `modernCorrespondence` (ponte, **não** projeção da realidade atual ao passado);
- **paleoposição** → `paleoPositions` (sempre `reconstrução modelada`, rotulada, com confiança que **decai** com a idade);
- **localidade de evidência atual** → `Place` marcado como **janela/evidência** (“encontrado hoje em X”), separado da posição antiga;
- **região política inexistente no período** → **nenhum** `Region` político (omitir nomes modernos);
- **evento sem localização precisa** → `SpatialUncertainty` (`sem-localização` / `localização-inferida` / `fronteira-difusa`); globo esquemático, nunca geometria inventada;
- **cena global/planetária** → `spatialScope = planetário`, sem marcadores nacionais;
- **cena cósmica sem globo terrestre** → `spatialScope = sem-lugar-terrestre`; a função **não** força o globo.

**Exemplos obrigatórios:**

|Entrada                                   |`spatialScope` resolvido     |Geometria usada                                  |Anacronismo evitado                                                  |
|------------------------------------------|-----------------------------|-------------------------------------------------|---------------------------------------------------------------------|
|**território que hoje é o Brasil em 1789**|recorte por lente moderna    |polígono atual → itens via `modernCorrespondence`|“Brasil” não era Estado-nação; rótulo “colônia, não o Brasil de hoje”|
|**Capitania de Minas Gerais em 1789**     |região histórica             |`historicalGeometryVersions` (capitania)         |não confundir capitania com o estado de MG atual                     |
|**Chicxulub em 66 Ma**                    |ponto em paleoposição        |`paleoPositions[66 Ma]` (rotulada)               |marcador **não** fica na coordenada moderna do Yucatán               |
|**Deccan Traps em 66 Ma**                 |região em paleoposição       |`paleoPositions` da placa indiana                |posição da placa ≠ Índia atual                                       |
|**Hamersley (evidência do GOE)**          |localidade de evidência atual|`modernPlace` + nota “janela para o passado”     |depósito atual ≠ “onde aconteceu”                                    |
|**Big Bang**                              |sem lugar terrestre          |nenhuma geometria de globo                       |não ancorar o universo num ponto da Terra                            |

-----

## 7. Seleção e ranqueamento de itens (Tarefa 7)

A função pontua candidatos por critérios combinados e os distribui em **categorias de resultado**. O ranqueamento serve à **relevância curada** (não despejar tudo que coincide no tempo — Etapa 2 §6.3).

**Critérios mínimos** (combinados, não lexicográficos):

- interseção temporal e **proximidade temporal** ao núcleo do recorte;
- interseção espacial e **proximidade espacial**;
- relação com `focusItem` (via grafo): `contemporâneo-de`, `causou`/`possibilitou`/`decorreu-de`/`afetou`, `parte-de`;
- camada temática (`layerFilters`) e **relevância didática**;
- `confidenceLevel` e `evidenceLevel` (itens de baixa confiança descem ou recebem rótulo, conforme `confidenceFilters`);
- `publicabilityStatus` e `reviewStatus` (o invariante de exibição **precede** o ranqueamento: o não exibível não compete);
- **diversidade geográfica e temática**; **evitar eurocentrismo**; **incluir Brasil/África/povos indígenas quando relevante** (camadas 20/21 da 4A; as três cenas-gabarito tratam isso como estrutural, não nota de rodapé);
- **evitar sobrecarga** (teto por categoria; o excesso vira `navigationSuggestions`, não lista infinita).

**Categorias de resultado:**

|Categoria                  |O que entra                                                   |Campo do `MomentResult`               |
|---------------------------|--------------------------------------------------------------|--------------------------------------|
|**Foco principal**         |itens-âncora do recorte                                       |`mainItems`                           |
|**Simultâneos centrais**   |coexistentes de alta relevância/relação direta                |`simultaneousItems` (subgrupo)        |
|**Simultâneos contextuais**|coexistentes de contexto (menor peso)                         |`simultaneousItems` (subgrupo)        |
|**States de fundo**        |condições do sistema (atmosfera/economia/…)                   |`states`                              |
|**Evidências**             |claims `evidenciado-por` (“como sabemos”)                     |dentro de `sourceSummary`/dossiê      |
|**Debates/`ClaimSets`**    |controvérsias legítimas (com peso quando preciso)             |`claimSets`                           |
|**Consequências**          |cadeia causal a jusante (`cascadeStructure` quando há gatilho)|dentro de `navigationSuggestions`/cena|
|**Itens ocultos/mediados** |não exibíveis como fato; contabilizáveis                      |`hiddenItems`                         |

-----

## 8. Publicabilidade e gating (Tarefa 8)

A função aplica, nesta ordem: **(1) invariante de exibição** → **(2) gating por contexto** → **(3) modulação por faixa**.

- **`reviewStatus`** — `not-required`/`pending`/`approved`/`rejected`/`legal-review`. Item `pending`/`rejected`/`legal-review` **não** é exibível nem entra na simultaneidade pública.
- **`publicabilityStatus`** — nível agregado do resultado: **1. publicável · 2. parcialmente publicável · 3. mediada · 4. apenas interna · 5. bloqueada** (5 níveis da 4F/4H bastam).
- **`gatingReason`** — razão principal **+ tipo**: `editorial` · `científico` · `licença` · `revisão-humana` · `geometria` · `mídia` · `fonte` · `legal`.
- **`licenseRisk` / `editorialRisk` / `scientificRisk`** — riscos agregados que **explicam** o nível e o tipo de gating.
- **`ageLevelMode`** — modula profundidade/linguagem/mídia; em faixas menores, mídia gráfica oculta por padrão e temas sensíveis exigem mediação (3.1 §6).
- **`hiddenItems` / `includeHiddenSummary`** — o oculto pode ser **contabilizado** (transparência) sem ser **exposto**.

**Regras (vinculantes):**

1. **Itens `pending` não podem aparecer como fato.** (Podem ser contados em `includeHiddenSummary`.)
1. **Itens sensíveis não revisados não podem aparecer para estudante.** A mediação por faixa é obrigatória onde a 3.1 exige.
1. **Itens de alto risco científico podem aparecer com rótulo e mediação** (não são ocultados por incerteza; são **rotulados** — hipótese como hipótese, faixa como faixa).
1. **Itens bloqueados não aparecem**, mas podem ser **contabilizados em resumo interno** de curadoria.

-----

## 9. Anacronismo e equivalência (Tarefa 9)

A função gera `anachronismWarnings` e `equivalenceWarnings` e **exclui** itens não contemporâneos.

**Anacronismos a evitar (e correção aplicada):**

|Risco                                    |Correção da função                                                             |
|-----------------------------------------|-------------------------------------------------------------------------------|
|**Brasil em 1789 como Estado nacional**  |colônia portuguesa + capitanias; `modernCorrespondence` como lente rotulada    |
|**“México” em 66 Ma**                    |nenhum país; só placas/paleogeografia                                          |
|**fronteiras modernas em tempo profundo**|omitir recortes políticos; crátons/placas esquemáticos                         |
|**paleomapa como fato**                  |`paleoPosition` sempre `reconstrução modelada`, rotulada, incerta              |
|**evidência atual como posição antiga**  |separar localidade de evidência (hoje) da paleoposição                         |
|**negacionismo como lado equivalente**   |objeto `rotulado-rejeitado` **fora** do `ClaimSet`, nunca “lado”               |
|**hipótese como consenso**               |`claimType`/`positionType` explícitos; consenso é consenso, hipótese é hipótese|
|**incerteza como ignorância total**      |`UncertaintyProfile` mostra **faixa**, não “não se sabe nada”                  |
|**projeção futura como previsão certa**  |rótulo de cenário/modelo obrigatório no lado positivo do eixo                  |

**Equivalência (anti-falsa-equivalência, via `weightedClaimSets`):** claims concorrentes carregam `evidenceWeight`/`scholarlyWeight`/`displayWeight` assimétricos; o dominante recebe destaque (`primário`), o contribuinte recebe `secundário`/`nota`; **minoria legítima nunca vira oculta**; negacionismo recebe `rotulado-rejeitado` e fica fora do conjunto. A função **não decide** debates científicos abertos — apresenta os pesos definidos na curadoria.

-----

## 10. Geração de `Scene` candidate (Tarefa 10)

A função **pode** emitir um `generatedSceneCandidate` (`Scene` v1.1; 34 campos), mas **não cria cena agora** — esta seção define apenas a **mecânica**. A cena candidata **referencia** itens por `knowledgeItemId` (jamais duplica).

**Quando gerar cena × quando apenas retornar lista:**

|Situação                                                                   |Decisão                                             |
|---------------------------------------------------------------------------|----------------------------------------------------|
|recorte coeso, com foco e simultaneidade real, e `outputMode = cena/dossiê`|**gerar** `Scene` candidata                         |
|consulta exploratória ampla, sem foco, `outputMode = resumo/lista`         |**retornar lista** (`MomentResult` sem cena)        |
|recorte cruza muitos itens `pending`/sem geometria                         |retornar lista + cena marcada **bloqueada/rascunho**|

**Acionamento dos campos v1.1:**

- **`triggerItem`** — preencher quando o recorte nasce de um `Event` pontual com consequências (K-Pg); **deixar vazio** em simultaneidade pura (1789) ou processo gradual (2,4 Ga).
- **`cascadeStructure`** — preencher quando há `triggerItem` com propagação multi-camada; `confidenceByStage` **decai** ao longo da cascata; **dispensar** sem gatilho (admite mini-cascatas locais).
- **`weightedClaimSets`** — usar sempre que houver claims de peso assimétrico (causa do K-Pg; consenso × negacionismo climático).
- **`paleoPositionPolicy`** — declarar em tempo profundo com lugar (Chicxulub, GOE); trivial/ausente em cena histórica recente.

**Marcação de maturidade (`sceneCompletenessLevel`) × exibição (`publicabilityStatus`):**

|Marcar como                                            |Quando                                                                                               |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|**`rascunho`**                                         |recorte incompleto, pendências de povoamento/geometria abertas                                       |
|**`gabarito-interno`**                                 |completo e exemplar, mas com pendências que impedem exibição pública (as três cenas atuais)          |
|**parcialmente publicável** (`publicabilityStatus = 2`)|núcleo factual exibível, sensíveis/incertos retidos                                                  |
|**bloquear** (`publicabilityStatus = 5`)               |gating dominante impede exibição (sensível não revisado, licença proibida, geometria ausente crítica)|


> A função **não** promove uma cena a `gabarito-interno` automaticamente — gabarito é decisão de curadoria (4H §9, 12 critérios). A função apenas **propõe** a candidata e registra suas pendências (não esconde o que falta).

-----

## 11. Padrões de resposta por tipo de consulta (Tarefa 11)

Oito padrões. Cada um indica `queryType`, entidades consultadas, resposta esperada, riscos e alimentação de timeline/globo/dossiê.

**1. “O que acontecia no mundo em 1789?”** — *Tipo 1/3 (simultaneidade global histórica).* Entidades: Events (Bastilha, Estados Gerais, Declaração), Process (Revolução Francesa, industrialização incipiente, escravidão atlântica), Region (França, EUA, Qing, Otomano, África Ocidental), States (econômico/populacional), `ClaimSet` (causas), Brasil/África/indígenas (camadas 20/21). Resposta: corte do mundo humano simultâneo, com a lente Brasil e os três paralelos. Riscos: **eurocentrismo**; apagamento indígena; tratar “Brasil” como nação. Alimenta: timeline (eventos de dia + processos); globo (foco regional + marcadores, fronteiras históricas); dossiê (~15 blocos). Gating: **editorial**.

**2. “…no território que hoje é o Brasil em 1789?”** — *Tipo 7 (lente moderna).* Entidades: itens históricos com `ModernCorrespondence` (Inconfidência Mineira → Capitania de Minas → MG hoje), `EconomicState` (mineração), populações indígenas/escravizadas. Resposta: corte local com **lente moderna rotulada**. Riscos: anacronismo (Brasil-nação; capitania×estado); apagamento indígena sob fronteira colonial. Alimenta: globo (capitanias com `historicalGeometryVersions`); dossiê (rótulo “colônia, não o Brasil de hoje”).

**3. “…na Terra há 2,4 Ga?”** — *Tipo 4 (tempo profundo sem evento).* Entidades: `Process` (fotossíntese oxigênica, GOE), States (`AtmosphereState`/`OceanographicState`/`PaleogeographicState`), `Place` de evidência (Hamersley/Huroniano/Transvaal), `ClaimSet` (timing/ritmo/Kenorland) × `UncertaintyProfile` (magnitude/paleogeografia). Resposta: corte **planetário de sistemas**, **zero Event**, evidência sem documentos. Riscos: paleomapa como fato; falsa precisão; Kenorland como consenso. Alimenta: timeline (processos/States, bordas difusas); globo (esquemático + halo); dossiê (~18 blocos “como sabemos”). Gating: **científico** + geometria.

**4. “…na Terra há 66 Ma?”** — *Tipo 5/6 (tempo profundo com evento / extinção).* Entidades: `Event` gatilho (impacto Chicxulub), `cascadeStructure`, States (Bio/Atm/Ocean), `Place`+`PaleoPosition` (Chicxulub, Deccan), `weightedClaimSets` (impacto ≫ Deccan). Resposta: cena **híbrida** com cascata e pesos. Riscos: “México” em 66 Ma; paleoposição = atual; impacto e Deccan como equivalentes; cadeia determinista. Alimenta: timeline (1 evento + processos + States); globo (paleogeográfico + marcador pontual rotulado); dossiê (~20 blocos). Gating: **científico**.

**5. “…antes e depois do K-Pg?”** — *Tipo 10 (antes/depois) + 11 (consequências).* Entidades: par de States/Process via `ocorreu-antes`/`ocorreu-depois`; `cascadeStructure` para o “depois”. Resposta: comparação temporal (Cretáceo tardio × recuperação paleógena). Riscos: sugerir determinismo; achatar a recuperação. Alimenta: timeline (dois cortes + transição); dossiê (espinha “atmosfera→clima→oceano→vida→recuperação”, confiança decaindo).

**6. “…durante a Revolução Industrial?”** — *Tipo 5 (processo foco).* Entidades: `Process` (industrialização ~1760–1840), States (`Economic`/`Technology`/`Population`/`Cultural`), Region (Grã-Bretanha núcleo + difusão), simultâneos globais. Resposta: processo longo + contexto, **não** ponto. Riscos: tratar faixa longa como data; eurocentrismo (omitir efeitos coloniais). Alimenta: timeline (bloco longo); globo (região + fluxos); dossiê (trilha máquina→industrialização→urbanização).

**7. “…hoje em relação às mudanças climáticas modernas?”** — *Tipo 8 (contemporânea).* Entidades: `Process` (mudança climática antrópica), States (`Climate`/`Economic`/`Population`) com **dados medidos** (séries recentes), **claim de consenso com `UncertaintyProfile`** (faixas de projeção) + `ClaimSet` **só** para o debate interno de projeção. Resposta: estado presente com consenso tipado como consenso. Riscos: **negacionismo como lado** (proibido — `rotulado-rejeitado` fora do conjunto); confundir dado medido com estimativa. Alimenta: timeline (séries recentes); globo (overlays de dados); dossiê (fato físico separado de opinião sobre política — o produto não opina).

**8. “…em 2100 num cenário climático?”** — *Tipo 13 (projetivo).* Entidades: `Process`/`State` projetivos + modelo (RCP/SSP); `sourceTimeBasis = scenarioYear`. Resposta: corte **projetivo rotulado** (lado positivo do eixo). Riscos: **projeção como fato/previsão certa**; omitir o modelo. Alimenta: timeline (faixa futura rotulada); dossiê (faixa de cenários, não número cravado; modelo explícito).

-----

## 12. Modos de resultado (Tarefa 12)

Dez modos (`outputMode`). Cada um declara quando usar, campos exigidos, o que oculta e como preserva fontes/incerteza/publicabilidade.

|Modo                              |Quando usar                          |Campos exigidos                                        |O que oculta                          |Preservação                                                          |
|----------------------------------|-------------------------------------|-------------------------------------------------------|--------------------------------------|---------------------------------------------------------------------|
|**Resumo rápido**                 |resposta curta a consulta direta     |`mainItems`, `confidenceSummary`, `publicabilityStatus`|contextuais e ocultos                 |rótulo de confiança presente; gating aplicado                        |
|**Cena completa**                 |recorte coeso para exploração        |`generatedSceneCandidate` (34 campos)                  |itens não exibíveis                   |invariante + anacronismo + pesos                                     |
|**Dossiê**                        |aprofundamento de um foco            |`focusSummary`, `sourceSummary`, evidências, relações  |itens sensíveis por faixa             |“como sabemos” obrigatório                                           |
|**Lista por região**              |comparar geografias no mesmo tempo   |`simultaneousItems` agrupados por `Region`             |regiões anacrônicas                   |geometria por regime rotulada                                        |
|**Lista por camada**              |recorte temático (ciência, política…)|`simultaneousItems` por camada 4A                      |camadas filtradas                     |conexões intercamada sinalizadas                                     |
|**Comparação antes/depois**       |mostrar transição em torno de um foco|par de cortes (`comparisonMode`)                       |ruído fora da janela                  |confiança decaindo, sem determinismo                                 |
|**Linha do tempo**                |navegação temporal                   |itens por `canonicalTimeScalar`                        |—                                     |`displayTime` por regime; `sourceTimeBasis` disponível               |
|**Globo/mapa**                    |navegação espacial                   |`normalizedSpatialScope` + geometria                   |geometria pendente (vira esquema)     |rótulo de qual geometria está em uso                                 |
|**Relatório interno de curadoria**|revisão humana                       |tudo + `hiddenItems` detalhados                        |nada do curador (mas marca pendências)|`pending`/riscos visíveis **para curadoria**, nunca como fato público|


> **Invariante de todos os modos:** nenhum modo expõe item `pending`/`rejected`/`legal-review` como fato; todos carregam `publicabilityStatus`; incerteza é faixa, debate é lado; fontes A/B disponíveis quando `includeSources`.

-----

## 13. Limites da função (Tarefa 13)

A função **NÃO** deve:

- **inventar dados** (nem precisão temporal, nem geometria, nem paleomapa) — usar flags `PENDENTE_*` e `UncertaintyProfile`;
- **criar fato sem claim** — nada é tratado como verdade fora de um `Claim` tipado e fonteado;
- **tratar IA como fonte** — texto de IA é rascunho rotulado (`pending`), nunca claim (A3/Q5, 1.1);
- **exibir `pending` como fato** — invariante de exibição absoluto;
- **transformar currículo em filtro obrigatório** — BNCC/série/faixa são **anotação externa** sobre a saída, nunca campo do núcleo;
- **substituir revisão humana** — o gating sinaliza; quem aprova é a curadoria;
- **criar cena-gabarito automaticamente** — gabarito é decisão de curadoria (12 critérios, 4H §9);
- **resolver licença** — `licenseRisk` é sinalizado, não decidido pela função (asset-level, Etapa 13);
- **resolver geometria pendente** — geometria ausente vira esquema rotulado + `PENDENTE_REFINAMENTO_ESPACIAL`;
- **decidir debates científicos sozinha** — apresenta pesos da curadoria; não arbitra consenso;
- **criar falsa equivalência** — negacionismo é `rotulado-rejeitado` fora do `ClaimSet`; pesos assimétricos são respeitados.

-----

## 14. Próximos passos para a Etapa 6 (Tarefa 14)

Com a Etapa 5, a função central deixa de ser três cenas-instância e passa a ser uma **capacidade de consulta reutilizável** do Knowledge Core, que **produz** `MomentResult` e cenas `Scene` v1.1 — respeitando `canonicalTimeScalar`, `sourceTimeBasis`, publicabilidade, revisão, gating, `weightedClaimSets`, `cascadeStructure`, `paleoPosition`, `ModernCorrespondence`, States, Claims, `RelationshipGraph`, fontes, incerteza, anacronismo e não-falsa-equivalência.

**O que a Etapa 6 (Compliance Layer / BNCC) deve consumir desta etapa:**

1. **O `MomentResult` como interface de leitura.** A camada de conformidade é **leitora/anotadora externa**: aplica tags BNCC, recorte regional e faixa **sobre a saída** da função, pelos mesmos índices (tempo/espaço/tema/tipo/confiança), **sem** entrar no núcleo (Etapa 2, Tarefa 10). A direção de dependência permanece invertida.
1. **Os `queryMode` e `outputMode`** como pontos de acoplamento — um `BNCCMapping` aponta para `knowledgeItemId`/`focusItem` do resultado, nunca o contrário.
1. **O `ageLevelMode`/`publicabilityMode`** como já existentes — a Etapa 6 os **usa**, não os redefine; o recorte pedagógico opera sobre a saída, jamais altera claims.

**Pendências carregadas (registradas, não resolvidas aqui — para outras etapas):** revisão científica dos itens `pending` (magnitude, paleogeografia, pesos causais); revisão editorial dos sensíveis (Leis 10.639/11.645; migração de BR-07 para `legal-review`); geometria histórica/paleogeográfica (`PENDENTE_REFINAMENTO_ESPACIAL`); confirmação de licença asset-level (que passará a preencher `sourceTimeBasis`/`conversionMethod`); curva de calibração ¹⁴C padrão; calendários não-ocidentais. **Nenhuma** destas é tarefa da função de momento — todas pertencem à curadoria/ingestão ou a etapas próprias.

-----

*Documento de entrega da Etapa 5, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z). Generaliza a função central do produto — “O que acontecia no mundo neste momento?” — de cenas-instância (4D/4E/4G) para a capacidade reutilizável de leitura `WhatWasHappeningAtMoment` do Knowledge Core: definição da função, 13 tipos de consulta, objeto de entrada `MomentQuery`, objeto de saída `MomentResult`, normalização temporal (eixo canônico T0 = 2000.0 CE; preservação de `sourceTimeBasis`), normalização espacial (quatro mecanismos `modernGeometry`/`historicalGeometryVersions`/`paleoPositions`/`modernCorrespondence`), seleção e ranqueamento com categorias de resultado, publicabilidade e gating (5 níveis + `gatingReason`), regras de anacronismo e anti-falsa-equivalência (`anachronismWarnings`/`equivalenceWarnings`), mecânica de geração de `Scene` candidate sob `Scene` v1.1, oito padrões de resposta, dez modos de resultado, limites da função e handoff para a Etapa 6. Não cria cena manual nova, não povoa conteúdos, não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não desenha pipeline técnico completo, não reabre auditoria de fontes nem política editorial. Etapa 5 concluída; Etapa 6 — Compliance Layer (BNCC) como leitora externa — habilitada.*