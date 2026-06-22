# Etapa 4H — Consolidação Pós-Três Cenas e Atualização do Padrão de Scene v1.1

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4H · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A), a normalização (Etapa 4C), e as três cenas-gabarito + o padrão genérico de `Scene` (Etapas 4D, 4E, 4F, 4G) · 12/06/2026
**Escopo desta etapa (e seus limites):** **consolidar método** — comparar as três cenas-gabarito, atualizar o padrão genérico de `Scene` para **v1.1** (incorporando `cascadeStructure`, `ClaimSet` com peso por claim e `paleoPosition` em `Place`), e produzir matriz de padrões, checklist operacional e critérios de "cena-gabarito". Conforme solicitado, **não** cria quarta cena, **não** povoa lotes, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** reabre auditoria de fontes (1/1.1), **não** reabre política editorial (3.1), **não** usa Wikidata/Wikipedia como autoridade e **não** copia texto de fontes.

**Natureza desta etapa.** Atualização de **padrão** (Scene v1.1) e de **vocabulário** (ClaimSet com peso; paleoPosition), restrita aos refinamentos escalados pela 4G. Nada além é remodelado.

---

## Sumário

1. Comparação das três cenas-gabarito (Tarefa 1)
2. Padrão genérico de `Scene` v1.1 (Tarefa 2)
3. Definição de `cascadeStructure` (Tarefa 3)
4. `ClaimSet` com peso por claim (Tarefa 4)
5. `paleoPosition` em `Place` (Tarefa 5)
6. Matriz de padrões por tipo de cena (Tarefa 6)
7. Checklist operacional de criação de `Scene` (Tarefa 7)
8. Revisão de publicabilidade (Tarefa 8)
9. Definição de "cena-gabarito" (Tarefa 9)
10. Recomendação da próxima cena ideal (Tarefa 10)
11. Próximos passos para a Etapa 4I (Tarefa 11)

---

## 1. Comparação das três cenas-gabarito (Tarefa 1)

| Dimensão | A · `scene:world-1789-french-revolution` | B · `scene:earth-2-4ga-great-oxidation-event` | C · `scene:earth-66ma-kpg-extinction` |
|---|---|---|---|
| Regime temporal | histórico (documental) | geológico profundo | geológico profundo + evento pontual (**híbrido**) |
| Precisão temporal | dia/mês/ano | Ga (faixa) | Ma (alta resolução relativa) |
| Tipo de evidência | documental | proxy geoquímico | misto: geoquímico + estrutural + estratigráfico + paleontológico |
| Item dominante | Event + Entity + Region | State + Process | Event(gatilho) + Process + State |
| Presença de **Event** | **alta** (vários) | **zero** | **1** (impacto) |
| Presença de **Process** | alta | alta | alta |
| Presença de **State** | média | **alta** | **alta** |
| Presença de **Place/Region** | alta (6 Places, 8 Regions) | Place=evidência; Region política=0 | 1 Place (+3) ; Region política=0 |
| Presença de **ClaimSet** | controvérsias historiográficas/terminologia | debates científicos | debates científicos **com peso** |
| Presença de **UncertaintyProfile** | baixa | alta | alta |
| Risco editorial | **alto** | baixo | baixo |
| Risco científico | baixo | **alto** | médio-alto |
| Risco de licença | baixo-médio (0–2) | baixo (0–1) | baixo (0–1) |
| Timeline | eventos de dia + processos | processos/States, bordas difusas | **1 evento** + processos + States |
| Globo/mapa | foco regional + marcadores; fronteiras históricas | esquemático; halo; oceanos | paleogeográfico rotulado + **marcador pontual** |
| Dossiê | 15 blocos (simultaneidade humana) | 18 blocos ("como sabemos") | 20 blocos (sistema + "como sabemos") |
| Tipo de anacronismo | fronteiras/nações atuais; apagar indígenas | continentes/países modernos; paleomapa como fato | "México" em 66 Ma; aves≠todos dinossauros; paleoposição≠atual |
| Tipo de simultaneidade | mundo humano ao mesmo tempo | planeta (sistemas) ao mesmo tempo | planeta em **crise sistêmica encadeada** |
| Tipo de publicabilidade | Nível 2 (gargalo editorial) | Nível 2→3 (gargalo científico) | Nível 2 (gargalo científico) |
| **Principal aprendizado metodológico** | simultaneidade histórica; ModernCorrespondence; gating editorial | tempo profundo; evidência sem documentos; ClaimSet×UncertaintyProfile; States dominantes | **cena híbrida**: gatilho→cascata; **ClaimSet com peso**; **paleoPosition**; OceanographicState oficial |

**Síntese.** As três cenas cobrem três regimes (histórico, profundo-sem-evento, profundo-com-evento) e três perfis de risco (editorial, científico, científico-com-cascata). Os refinamentos que a 4G revelou — **cascata**, **peso em ClaimSet**, **paleoposição** — são exatamente o que falta ao padrão da 4F para cobrir o **terceiro regime**. É o que a v1.1 incorpora.

---

## 2. Padrão genérico de `Scene` v1.1 (Tarefa 2)

O padrão v1.1 mantém os 27 campos da 4F e adiciona **7 campos novos** (motivados pela cena híbrida). Definição conceitual, sem código.

```txt
Scene = {
  // --- campos herdados da v1.0 (4F) ---
  id, title, focusItem, queryType, timeRange, timePrecision, spatialScope,
  activatedLayers, centralItems, contextualItems, sensitiveItems, hiddenItems,
  claimSets, uncertaintyProfiles, states, sources, evidenceProfile,
  editorialRisk, scientificRisk, licenseRisk, reviewStatus,
  timelineBehavior, globeBehavior, dossierBehavior, simultaneityBehavior,
  anachronismPolicy, publicabilityStatus,

  // --- novos campos v1.1 ---
  triggerItem,            # Event-gatilho, quando a cena nasce de um disparo
  cascadeStructure,       # encadeamento causal gatilho→efeitos (ver §3)
  weightedClaimSets,      # ClaimSets com peso por claim (ver §4)
  paleoPositionPolicy,    # como a cena trata posição atual × paleoposição (ver §5)
  scenePatternType,       # tipo da cena na taxonomia (4F §3 / §6 abaixo)
  gatingReason,           # por que a cena está parcial/mediada/bloqueada (ver §8)
  sceneCompletenessLevel  # rascunho | gabarito-interno | publicável
}
```

**Definição e regras de cada campo novo:**

- **`triggerItem`** — o `Event` que **dispara** a cena. **Existe quando** a cena nasce de um evento pontual com consequências (K-Pg: `evt:impacto-chicxulub`). **Não existe quando** a cena é puramente um corte de simultaneidade (1789) ou um regime de States/processos sem gatilho único (2,4 Ga — a oxigenação é gradual, sem disparo pontual).
- **`cascadeStructure`** — o encadeamento causal a partir do `triggerItem` (ver §3). **Obrigatório quando** há `triggerItem` com propagação multi-camada (K-Pg). **Dispensável quando** não há gatilho (1789, 2,4 Ga) — embora possa haver **mini-cascatas** locais (crise fiscal→Revolução).
- **`weightedClaimSets`** — os `ClaimSets` da cena que carregam **peso por claim** (ver §4). Evita falsa equivalência ao marcar explicitamente que claims concorrentes **não** têm o mesmo estatuto (K-Pg: impacto ≫ Deccan; clima: consenso vs negacionismo rejeitado).
- **`paleoPositionPolicy`** — declara como a cena distingue **localidade atual** de **paleoposição** (ver §5). **Crítico em tempo profundo** (Chicxulub hoje no Yucatán ≠ paleoposição em 66 Ma); **trivial/ausente** em cena histórica recente.
- **`scenePatternType`** — classifica a cena na taxonomia (histórica pontual, simultaneidade global, tempo profundo com/sem evento, extinção em massa, cósmica, contemporânea, comparativa, evidência/proxy). Guia o comportamento esperado (§6).
- **`gatingReason`** — explica **por que** a cena não é totalmente publicável: razão principal + tipo de gating (editorial/científico/licença/revisão-humana/geometria/mídia/fonte/legal) (ver §8). 1789 → editorial; 2,4 Ga e 66 Ma → científico.
- **`sceneCompletenessLevel`** — distingue **`rascunho`** (incompleto, em construção), **`gabarito-interno`** (completo e exemplar, mas com pendências que impedem exibição pública) e **`publicável`** (pronto para o público). Diferente de `publicabilityStatus` (que é sobre **exibição**); este é sobre **maturidade da cena como artefato de método**.

> **Relação `sceneCompletenessLevel` × `publicabilityStatus`.** Uma cena pode ser `gabarito-interno` (maturidade alta como exemplo) e ainda `parcialmente publicável` (exibição limitada por pendências). As três cenas atuais são **`gabarito-interno`**, **parcialmente publicáveis**.

---

## 3. Definição de `cascadeStructure` (Tarefa 3)

Estrutura que descreve um **encadeamento causal** disparado por um `triggerItem`, propagando-se por camadas, tempo e espaço, com consequências sistêmicas. É o que diferencia uma **cena híbrida** (K-Pg) de uma cena de simultaneidade pura.

```txt
CascadeStructure = {
  id,                   # cascade:<...>
  triggerItem,          # o Event-gatilho (ex.: evt:impacto-chicxulub)
  stages[],             # estágios ordenados (cada um: item/processo/state + descrição)
  affectedStates[],     # States perturbados ao longo da cascata
  affectedLayers[],     # camadas (4A) atravessadas
  temporalPropagation,  # ritmo/escala da propagação (instantâneo→Ma)
  spatialPropagation,   # do ponto ao global; ou difuso
  evidenceClaims[],     # evidências que sustentam cada elo
  uncertaintyProfile,   # incerteza por elo (não cadeia rígida)
  claimSets[],          # debates sobre mecanismos/pesos
  confidenceByStage[],  # confiança POR estágio (decai ao longo da cascata)
  visualizationNotes,   # como animar/exibir sem sugerir determinismo
  reviewStatus
}
```

**Conexões:**
- **Relationship Graph:** a cascata **é uma vista ordenada** sobre arestas já existentes (`causou`/`perturbou`/`afetou`) — não duplica o grafo, **seleciona e ordena** um caminho causal. Cada `stage` aponta para arestas reais (ex.: K-Pg rel:K02→K03→K04…).
- **Timeline:** exibida como **sequência logo após o `triggerItem`**, com os estágios em ordem e barras de incerteza crescentes.
- **Globo:** propagação **espacial** animável (do ponto de Chicxulub ao global), com rótulo de que a animação é **didática**, não medição.
- **Dossiê:** vira a espinha dos blocos de consequências ("atmosfera→clima→oceano→vida→recuperação").

**Como evitar transformar hipótese em cadeia causal rígida:**
- `confidenceByStage` **decai** ao longo da cascata — o gatilho (impacto) é alta confiança; "extensão dos incêndios" é baixa. A exibição mostra esse **gradiente**, não uma seta uniforme.
- Cada elo é um **claim com evidência** (não fato encadeado automaticamente); elos debatidos remetem a `claimSets`/`uncertaintyProfile`.
- A `visualizationNotes` proíbe animações que sugiram **determinismo** ("e então inevitavelmente…").

**Quando uma cena histórica pode ou não ter cascata:**
- **Pode:** quando há um gatilho com efeitos encadeados (ex.: uma erupção→fome→migração; uma quebra→crise→revolta). Aí a cascata histórica é legítima, **mas** os elos são `interpretação` historiográfica, não lei física — confiança ainda menor.
- **Não:** quando a cena é **simultaneidade pura** (1789) — múltiplos processos coexistem **sem** um único gatilho. Forçar cascata aqui seria criar causalidade falsa.

**Aplicação aos três casos:**
- **1789 (A):** **sem `cascadeStructure` principal.** É simultaneidade. Há **mini-cascatas** locais (`proc:crise-fiscal-franca` → `proc:revolucao-francesa`), mas como arestas, não como cascata sistêmica. `triggerItem` = ausente.
- **2,4 Ga (B):** **cascata lenta e difusa**, sem gatilho pontual: fotossíntese oxigênica → acúmulo de O₂ (GOE) → mudança atmosférica/oceânica → (muito depois) eucariontes. `triggerItem` = ausente (processo gradual); modelável como cascata **de baixa taxa**, com elos distantes marcados como tais.
- **66 Ma (C):** **cascata canônica**, com gatilho pontual: `evt:impacto-chicxulub` → ejecta/poeira → perturbação atmosférica → resfriamento → queda de produtividade → colapso de cadeias → extinção seletiva → recuperação. `confidenceByStage` decai do impacto (alta) aos incêndios (baixa). É o **exemplo de referência** de `cascadeStructure`.

---

## 4. `ClaimSet` com peso por claim (Tarefa 4)

Atualização de política: nem todo `ClaimSet` representa "lados iguais". Um `ClaimSet` passa a poder conter **claims com peso assimétrico**, sem que isso vire relativização do consenso nem promoção de negacionismo.

```txt
WeightedClaim = {
  claimId,
  claimText,            # texto próprio (jamais transcrição)
  positionType,         # consenso | interpretação concorrente | hipótese | minoria legítima | rejeitado
  evidenceWeight,       # força da evidência empírica
  scholarlyWeight,      # grau de aceitação acadêmica
  confidenceLevel,      # confiança no claim
  evidenceLevel,        # tipo de evidência
  consensusAlignment,   # relação com o consenso
  displayWeight,        # como aparece na exibição
  nonEquivalentTo[],    # claims dos quais NÃO é equivalente
  editorialNote
}
```

**Valores possíveis:**
- **`evidenceWeight`** := `dominante` · `forte` · `moderado` · `fraco` · `marginal` · `nulo (rejeitado)`
- **`scholarlyWeight`** := `majoritário` · `substancial` · `minoritário-legítimo` · `marginal` · `fora-da-academia`
- **`displayWeight`** := `primário` (destaque) · `secundário` (lado a lado, menor) · `nota` (rodapé/contexto) · `rotulado-rejeitado` (mostrado **apenas** como objeto rejeitado, fora do ClaimSet) · `oculto`
- **`consensusAlignment`** := `é-consenso` · `debate-interno-ao-consenso` · `interpretação-concorrente-legítima` · `minoria-legítima` · `fora-do-consenso-rejeitado`

**Como evitar os cinco erros:**
- **Falsa equivalência:** `displayWeight`/`evidenceWeight` assimétricos — o claim dominante recebe `primário`; o contribuinte, `secundário`. A exibição **mostra a hierarquia**.
- **Apagamento de minorias legítimas:** `minoria-legítima` **nunca** vira `oculto` — recebe `secundário`/`nota`, preservando vozes legítimas (ex.: interpretações historiográficas minoritárias com base).
- **Confundir consenso com unanimidade:** `é-consenso` **+** `debate-interno-ao-consenso` coexistem — o consenso pode ter debate interno legítimo (ex.: clima: aquecimento antrópico é consenso; faixas de projeção, debate interno).
- **Negacionismo como claim concorrente:** `fora-do-consenso-rejeitado` recebe `displayWeight = rotulado-rejeitado` e fica **fora** do `ClaimSet` — é objeto rotulado, nunca "lado".
- **Simplificar debates legítimos:** múltiplos claims `interpretação-concorrente-legítima` coexistem com pesos próprios — não se colapsa em narrativa única.

**Aplicação aos cinco exemplos:**

| Exemplo | Claim | positionType | evidenceWeight | scholarlyWeight | displayWeight | consensusAlignment |
|---|---|---|---|---|---|---|
| **1. K-Pg** | Impacto de Chicxulub (causa central) | interpretação | **dominante** | majoritário | **primário** | é-consenso (gatilho) |
| | Deccan Traps (contribuinte) | hipótese | moderado | substancial | secundário | debate-interno |
| | Combinação/sinergia | interpretação | forte | substancial | secundário | debate-interno |
| | "Não houve impacto/extinção" | rejeitado | nulo | fora-da-academia | rotulado-rejeitado | fora-do-consenso-rejeitado |
| **2. Rev. Francesa (causas)** | Crise fiscal · Tensões sociais · Iluminismo · Subsistência | interpretação concorrente | forte (cada) | substancial | secundário (todos, **coexistem**) | interpretação-legítima |
| **3. Clima moderno** | Aquecimento real e antrópico | consenso | **dominante** | majoritário | **primário** | é-consenso |
| | Faixas de sensibilidade/projeção | debate interno | forte | substancial | secundário | debate-interno-ao-consenso |
| | "Não há aquecimento/não é antrópico" | rejeitado | nulo | fora-da-academia | rotulado-rejeitado | fora-do-consenso-rejeitado |
| **4. 1492** | "Encontro" / "Invasão" / "Descobrimento" | interpretação (terminologia sensível) | — (não é peso empírico) | — | "invasão"/"encontro" **primário** com contexto; "descobrimento" **nota** (eurocêntrico) | interpretação-legítima (com estatuto editorial distinto) |
| | "Terra vazia / sem povos" | rejeitado | nulo | fora-da-academia | rotulado-rejeitado | fora-do-consenso-rejeitado |
| **5. Origem da vida** | Mundo de RNA · Fontes hidrotermais · Química de superfície | hipótese concorrente | moderado (cada) | substancial | secundário (coexistem) | hipóteses-legítimas |
| | Criacionismo/desenho inteligente | rejeitado | nulo | fora-da-academia | rotulado-rejeitado | fora-do-consenso-rejeitado |

> **Nota (1492):** o peso aqui **não** é empírico (os fatos da travessia são documentados), e sim **editorial/terminológico** — `evidenceWeight` não se aplica; o que difere é o **estatuto editorial** dos termos. O modelo acomoda isso via `displayWeight` + `editorialNote`, sem inventar peso empírico.

---

## 5. `paleoPosition` em `Place` (Tarefa 5)

Atualização da entidade `Place` para tempo profundo: um lugar atual pode ser **evidência** geológica, mas sua **posição no passado** era outra (placas se movem). Sem essa distinção, o globo de tempo profundo cai em anacronismo.

```txt
PaleoPosition = {
  timeRange,            # quando esta paleoposição vale
  modernPlace,          # ref ao Place atual (ex.: place:cratera-chicxulub)
  paleogeographicModel, # modelo usado (ex.: GPlates/EarthByte)
  paleoCoordinates,     # coordenadas reconstruídas (ou PENDENTE)
  confidenceLevel,      # confiança na reconstrução (decai com a idade)
  spatialUncertainty,   # margem espacial
  source,               # A/B (GPlates, CC BY)
  reconstructionModel,  # versão/identificação da reconstrução
  representationType,   # reconstrução modelada (default em deep time)
  reviewStatus,
  notes                 # ressalvas
}

Place = {
  id,
  preferredName,
  nameVariants,
  modernGeometry,             # geometria atual (real/moderno)
  historicalGeometryVersions, # geometrias em períodos históricos (ex.: fronteira de 1789)
  paleoPositions[],           # paleoposições em tempo profundo (NOVO)
  modernCorrespondence,       # lente "o que hoje é..."
  geometryStatus,             # real|histórico|inferido|moderno|paleogeográfico|pendente
  spatialUncertainty,
  sources,
  licenseProfile,
  reviewStatus
}
```

**Diferença entre os quatro mecanismos espaciais (e quando cada um se aplica):**
- **`modernGeometry`** — a forma **atual** do lugar (cidade, sítio). Aplica-se sempre que o lugar existe hoje (Paris, Yucatán). É o que se vê num mapa atual.
- **`historicalGeometryVersions`** — formas em **períodos históricos** documentados (ex.: fronteira da França em 1789, Capitania de Minas). Aplica-se ao **tempo histórico**, onde há reconstrução cartográfica de fronteiras.
- **`paleoPositions`** — **posições paleogeográficas** em tempo profundo (Chicxulub em 66 Ma; Deccan/placa indiana; localidades do GOE). Aplica-se ao **tempo geológico**, sempre como **reconstrução modelada** rotulada.
- **`modernCorrespondence`** — a **lente** "o que hoje chamamos de…" (Capitania→MG). Liga passado a referência atual **sem** projetar a realidade atual ao passado.

**Como aparece:**
- **Globo:** o marcador do lugar usa `modernGeometry` em cenas atuais, `historicalGeometryVersions` em cenas históricas e `paleoPositions` (rotulada/incerta) em cenas profundas. **O usuário sempre vê qual está sendo usada.**
- **Dossiê:** bloco do lugar mostra "hoje: X; em [período]: Y (reconstrução)", separando explicitamente localidade atual de paleoposição.

**Impacto em cenas de tempo profundo:** resolve o ponto mais sutil da 4G — o marcador de Chicxulub deve ficar na **paleoposição** de 66 Ma (rotulada), não na coordenada moderna de Yucatán; as localidades do GOE (Hamersley, Huroniano, Transvaal) são **`modernPlace`** de evidência, com `paleoPositions` próprias e incertas. Sem geometria validada: `geometryStatus = pendente` + `PENDENTE_REFINAMENTO_ESPACIAL`.

> **Retro-aplicação aos Places existentes (4C/4G):** `place:cratera-chicxulub` ganha `paleoPositions[66 Ma]`; `place:chicxulub`/Hamersley/Huroniano/Transvaal idem; `place:paris`/`place:ouro-preto` usam `modernGeometry`+`historicalGeometryVersions`, **sem** `paleoPositions` (irrelevante no tempo histórico).

---

## 6. Matriz de padrões por tipo de cena (Tarefa 6)

Combina a taxonomia da 4F com os campos da v1.1. "trigger?", "cascade?", "weighted?", "paleoPos?" = se o tipo **tipicamente** requer o campo.

| # | Tipo de cena | trigger? | cascade? | weighted? | paleoPos? | Item dominante | State dominante | Evidência dominante | Risco dominante | Globo | Timeline | Exemplo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Histórica pontual | às vezes | raro | às vezes | não | Event | — | documental | editorial | marcador no local | ponto datado | Queda da Bastilha |
| 2 | Histórica de processo | não | mini-cascata | sim | não | Process | Civilization/Economic | documental | editorial | região + fluxos | bloco longo | Rev. Industrial |
| 3 | Simultaneidade global | **não** | não | sim | parcial | mix | vários | múltipla | editorial | mundo + marcadores | corte único | 1789 |
| 4 | Tempo profundo sem evento | **não** | cascata lenta | sim | **sim** | State/Process | Atmosphere/Ocean/Biome | proxy | científico | esquemático rotulado | processos/States | GOE 2,4 Ga |
| 5 | Tempo profundo com evento | **sim** | **sim** | sim | **sim** | Event+Process+State | vários | proxy+estrutural | científico | paleogeo + marcador | evento+processos | (genérico) |
| 6 | Extinção em massa | **sim** | **sim** | **sim** (causa) | **sim** | Event+Process | Bio/Atm/Ocean | misto | científico | paleogeo + marcador | evento+cascata | K-Pg 66 Ma |
| 7 | Cósmica | às vezes | às vezes | às vezes | **não** (sem globo) | Event/Process cósmico | — | observação indireta | científico (antinegacionismo) | cosmos (sem globo) | zero+faixas | Big Bang |
| 8 | Contemporânea | às vezes | às vezes | **sim** (consenso×neg.) | não | State/Process+dados | Climate/Economic/Population | dados+medição | editorial+científico | overlays de dados | séries recentes | Clima moderno |
| 9 | Comparativa antes/depois | conforme par | conforme | conforme | conforme | State(×2) | par de States | conforme | conforme | split/transição | dois cortes | Antes/depois do GOE |
| 10 | Evidência/proxy | não | não | às vezes | **sim** | Claim de evidência + Place | — | proxy | científico | marcadores "hoje" | linha de inferência | BIFs / irídio |

**Leitura.** `triggerItem`/`cascadeStructure` concentram-se nos tipos **5 e 6** (tempo profundo com evento; extinção); `weightedClaimSets` é quase universal mas **crítico** em 6 e 8 (causa K-Pg; consenso×negacionismo climático); `paleoPosition` é obrigatório nos tipos **4, 5, 6, 10** (qualquer coisa em tempo profundo com lugar).

---

## 7. Checklist operacional de criação de `Scene` (Tarefa 7)

Aplicar **antes** de criar qualquer cena (Big Bang, Cambriano, Pangeia, 1492, Rev. Industrial, Apollo 11, clima moderno…). 25 perguntas, agrupadas.

**Foco e tempo**
1. Qual é o **foco** da cena (`focusItem`)?
2. Qual é o **regime temporal** (cósmico/geológico/biológico/arqueológico/histórico/contemporâneo/projetivo)?
3. Qual a **precisão temporal** possível? (não inventar)

**Estrutura (v1.1)**
4. Há **`triggerItem`** (evento-gatilho)?
5. Há **`cascadeStructure`** (encadeamento causal)? Se sim, `confidenceByStage` decai?
6. Há **Place/Region**?
7. Há **`paleoPosition`** (tempo profundo)?
8. Há **States obrigatórios** para o regime?
9. Quais **camadas** (4A) estão ativadas?

**Claims e evidência**
10. Quais **claims principais** existem? (fato × interpretação × hipótese)
11. Quais **evidências** sustentam a cena? ("como sabemos disso")
12. Há **`ClaimSet`**?
13. O `ClaimSet` precisa de **peso** (`weightedClaimSets`)? Há posição **sem equivalência**?
14. Há **`UncertaintyProfile`** (faixas, não lados)?

**Riscos**
15. Há **risco editorial**? (Leis 10.639/11.645; sensibilidade)
16. Há **risco científico**? (incerteza alta)
17. Há **risco de licença**? (assets; Deep Time Maps proibido)

**Exibição**
18. Há **itens pending**?
19. O que fica **oculto/mediado** e por quê (`gatingReason`)?
20. Qual o **`publicabilityStatus`** (1–5)?
21. Quais **anacronismos** evitar (`anachronismPolicy`)?
22. Quais **fontes A/B** precisam ser confirmadas?

**Validação final**
23. A cena tem **simultaneidade real** (algo significativo coexistindo)?
24. A cena **cabe** no globo/timeline (sem inventar geometria/precisão)?
25. O **dossiê** consegue explicar **"como sabemos disso"**?

> **Regra de bloqueio:** se 13 (equivalência indevida), 19 (gating não declarado), 21 (anacronismo não tratado) ou 25 (não explica "como sabemos") falharem, a cena **não** avança — são os quatro pontos onde as três cenas-gabarito mais ensinaram.

---

## 8. Revisão de publicabilidade (Tarefa 8)

Os **cinco níveis da 4F continuam suficientes** após a K-Pg. A cena híbrida **não** exigiu um sexto nível — exigiu apenas **explicitar a razão e o tipo do gating** (que a v1.1 captura em `gatingReason`).

**Níveis (mantidos):** 1. publicável · 2. parcialmente publicável · 3. mediada · 4. apenas interna · 5. bloqueada.

**Acréscimo (v1.1) — `gatingReason` = razão principal + tipo:**

| Tipo de gating | O que trava | Exemplo |
|---|---|---|
| **editorial** | sensibilidade (Leis 10.639/11.645; raça, colonização, escravidão) | itens sensíveis de 1789 |
| **científico** | incerteza alta (magnitude, paleogeografia, peso causal) | paleogeografia 2,4 Ga; peso do Deccan |
| **licença** | asset com licença restritiva/proibida | Deep Time Maps |
| **revisão-humana** | revisão obrigatória não concluída | temas sensíveis pending |
| **geometria** | sem geometria validada | fronteiras 1789; crátons 2,4 Ga |
| **mídia** | asset de mídia pendente/não rotulado | reconstruções sem `natureLabel` |
| **fonte** | fonte A/B não confirmada por asset | `PENDENTE_CONFIRMACAO_FONTE` |
| **legal** | risco jurídico (LGPD/pessoas vivas) | BR-07 ditadura (não nesta cena) |

**Aplicação às três cenas (com `gatingReason`):**

| Cena | publicabilityStatus | gatingReason (principal) | Tipo |
|---|---|---|---|
| **1789 (A)** | Nível 2 (parcialmente publicável) | itens sensíveis (escravidão/colonização/indígenas) aguardam revisão | **editorial** + revisão-humana |
| **2,4 Ga (B)** | Nível 2→3 (parcial→mediada na paleogeografia) | incerteza científica alta (paleogeografia, magnitude, Kenorland) | **científico** + geometria |
| **66 Ma (C)** | Nível 2 (parcialmente publicável) | peso causal (Deccan), paleogeografia fina, inverno/incêndios incertos | **científico** + geometria |

> **Conclusão:** 5 níveis bastam; o que faltava era **nomear o porquê** (editorial × científico × …). A v1.1 resolve com `gatingReason`. Nenhum sexto nível.

---

## 9. Definição de "cena-gabarito" (Tarefa 9)

Uma `Scene` é **cena-gabarito** quando serve de **padrão de referência** para cenas futuras. Critérios mínimos (todos obrigatórios):

1. **demonstra um tipo de cena** da taxonomia (§6);
2. tem **padrão completo de `Scene` v1.1** (todos os campos aplicáveis preenchidos);
3. **separa `Event`/`Process`/`State`** corretamente;
4. usa **`ClaimSet`** corretamente (com peso quando preciso);
5. usa **`UncertaintyProfile`** corretamente (faixa ≠ lados);
6. tem **`anachronismPolicy`** explícita;
7. tem **`publicabilityStatus`** + `gatingReason`;
8. tem **evidências e fontes** A/B ("como sabemos disso");
9. tem **dossiê conceitual**;
10. tem **comportamento de globo/timeline** definido;
11. **registra pendências** (não esconde o que falta);
12. **ensina algo** novo para cenas futuras.

**Avaliação das três cenas atuais:**

| Cena | É gabarito? | Tipo que exemplifica | Pendências que ainda possui | Padrão que ensina |
|---|---|---|---|---|
| **1789 (A)** | **Sim** | simultaneidade global histórica (tipo 3) | revisão editorial dos sensíveis; geometrias históricas de 1789 | simultaneidade humana; ModernCorrespondence; gating **editorial**; três paralelos (Brasil/África/indígenas) |
| **2,4 Ga (B)** | **Sim** | tempo profundo sem evento (tipo 4) | revisão científica; paleogeografia/Kenorland/magnitude; datum do eixo | evidência **sem documentos** (proxies); `ClaimSet`×`UncertaintyProfile`; States dominantes; globo esquemático; **zero Event** |
| **66 Ma (C)** | **Sim** | tempo profundo com evento / extinção em massa (tipos 5–6) | revisão científica; peso do Deccan; paleoposições; Places de evidência a criar | cena **híbrida**; `cascadeStructure`; **`ClaimSet` com peso**; `paleoPosition`; `OceanographicState` oficial |

**As três são gabarito** — cada uma exemplar de um tipo distinto e cada uma ensinando algo que as outras não ensinam. Juntas, cobrem os eixos **histórico × profundo** e **simultaneidade × cascata**. Pendências existem, mas são de **revisão/refinamento**, não de método — e estão **registradas** (critério 11), o que é parte do padrão.

> **Lacuna de cobertura (para a Tarefa 10):** ainda **não** há gabarito para os tipos **7 (cósmica)**, **8 (contemporânea)** e **9 (comparativa)**. A próxima cena deve cobrir uma dessas lacunas.

---

## 10. Recomendação da próxima cena ideal (Tarefa 10)

Cinco opções avaliadas pelo que **testam** e pela **lacuna** que cobrem.

| Opção | Tipo que testa | Lacuna que cobre | Riscos | Fontes | Valor visual | Valor p/ produto | Complex. editorial | Complex. científica |
|---|---|---|---|---|---|---|---|---|
| **1. Big Bang** | cósmica (tipo 7) | **cósmica** (sem globo; modelo×observação) | antinegacionismo | NASA, astrofísica | alto (origem do universo) | alto (marco-âncora) | baixa | média |
| **2. Cambriano** | biológico/evolutiva (tipo 4/6) | parcial (já há tempo profundo) | "progresso evolutivo" | PBDB, Macrostrat | médio-alto | médio | baixa-média | média |
| **3. 1492** | histórica sensível/global (tipo 3) | parcial (1789 já fez histórica) | **alto** (Leis 10.639/11.645; terminologia) | historiografia, fontes indígenas | alto | alto | **alta** | baixa |
| **4. Rev. Industrial** | histórica de processo + clima/tecnologia (tipo 2) | processo+`cascadeStructure` histórica | médio (trabalho, ambiente) | OWID, historiografia | médio | alto | média | média |
| **5. Mudanças climáticas modernas** | **contemporânea/projetiva** (tipo 8) | **contemporânea** (dados/séries/projeção) | médio-alto (negacionismo) | OWID, NASA, NOAA, INPE, IPCC | alto (séries, presente) | **muito alto** (missão educativa) | média (negacionismo) | média-alta (projeção) |

**Recomendação: opção 5 — Mudanças climáticas modernas (cena contemporânea/projetiva).**

**Justificativa:**
- **Cobre a maior lacuna de regime:** é a única que testa o **tempo contemporâneo/projetivo** (dados reais, séries, cenários futuros) — completamente inédito nas três cenas profundas/históricas já feitas.
- **É o teste definitivo de `weightedClaimSets`:** o caso **consenso antrópico × negacionismo** é exatamente o que o `WeightedClaim` (§4) foi desenhado para resolver — `é-consenso` (primário) + `debate-interno` (projeções, secundário) + `fora-do-consenso-rejeitado` (negacionismo, rotulado-rejeitado, fora do ClaimSet). Validar isso numa cena real é o próximo passo natural após defini-lo.
- **Exercita `UncertaintyProfile` no caso mais importante:** incerteza de **projeção** (cenários/sensibilidade) sem virar "não sabemos nada" nem falsa equivalência.
- **Máximo valor para o produto:** conecta o tempo profundo (a Terra que mudou sozinha) ao presente (a Terra que mudamos), fechando a narrativa do projeto; alta relevância educativa.
- **Liga-se a itens já existentes:** `proc:mudancas-climaticas-modernas` (HIST-21), `concept:mudanca-climatica-antropica` (4C), `claimset:clima-projecoes` (4C) — reúso, não povoamento novo massivo.

**Alternativa de menor risco (runner-up): opção 1 — Big Bang.** Se a equipe preferir validar o **regime cósmico** (sem globo) antes de enfrentar a sensibilidade do negacionismo climático, o Big Bang é a escolha mais limpa (baixo risco editorial, alto valor de âncora). Recomendo clima como **primária** pelo maior ganho de cobertura + teste do `weightedClaimSets`; Big Bang como **próxima logo em seguida**.

---

## 11. Próximos passos para a Etapa 4I (Tarefa 11)

A Etapa 4H consolidou o método: há **três cenas-gabarito**, o **padrão `Scene` v1.1** (com `cascadeStructure`, `weightedClaimSets`, `paleoPosition`), **State Types revisados**, **checklist operacional** e **critérios de cena-gabarito**. A **Etapa 4I**, quando solicitada, deve:

1. **Criar a próxima cena** seguindo o padrão v1.1 e a checklist (§7) — recomendada: **mudanças climáticas modernas** (contemporânea/projetiva), testando `weightedClaimSets` no caso consenso×negacionismo e o tempo projetivo; alternativamente, **Big Bang** (cósmica).
2. **Aplicar `weightedClaimSets`** na prática (clima: consenso primário; projeções secundárias; negacionismo rotulado-rejeitado fora do ClaimSet) — primeira validação real do vocabulário da §4.
3. **Exercitar `paleoPositionPolicy`** como "não aplicável" numa cena contemporânea (ou central, numa cósmica) — confirmando que o campo é condicional ao regime.
4. **Resolver o datum do eixo temporal** (1950 BP × J2000) — pendência herdada desde a 4B, agora urgente porque uma cena **contemporânea** precisa se conectar às cenas **profundas** no mesmo eixo; decisão da **Etapa 3**, aqui reforçada.
5. **Reificar `Source`/`MediaAsset`** conforme o padrão (séries climáticas com `natureLabel` `gráfico`; figuras recriadas dos dados, nunca copiadas; rotular IA quando houver).

**O que a 4I explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (1/1.1) ou política editorial (3.1). A única reabertura permitida é instanciar/validar os refinamentos v1.1 já aprovados.

---

*Documento de entrega da Etapa 4H, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B, 4C, 4D, 4E, 4F, 4G). Consolida o método após três cenas-gabarito: comparação formal das cenas 1789 × 2,4 Ga × 66 Ma, atualização do padrão genérico de `Scene` para **v1.1** (novos campos `triggerItem`, `cascadeStructure`, `weightedClaimSets`, `paleoPositionPolicy`, `scenePatternType`, `gatingReason`, `sceneCompletenessLevel`), definição de `cascadeStructure` (com `confidenceByStage` que decai), `ClaimSet` com peso por claim (`WeightedClaim`, anti-falsa-equivalência), `paleoPosition` em `Place` (localidade atual × paleoposição), matriz de padrões por tipo de cena, checklist operacional de 25 itens, revisão de publicabilidade (5 níveis + `gatingReason`), definição de cena-gabarito (as três confirmadas) e recomendação da próxima cena (clima moderno, com Big Bang como alternativa). Não cria cena nova, não povoa lotes, não escreve código, não propõe MVP, não define stack, não avança para UX final e não entra em currículo/professor/plano de aula. Próxima etapa, quando solicitada: Etapa 4I — criação da próxima cena (clima moderno ou Big Bang) sob o padrão v1.1.*
