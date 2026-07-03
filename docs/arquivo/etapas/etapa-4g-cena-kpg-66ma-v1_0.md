# Etapa 4G — Cena Canônica 66 Ma / Extinção K-Pg

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4G · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A), o lote-piloto P0 (Etapa 4B), a normalização (Etapa 4C), a cena histórica de 1789 (Etapa 4D), a cena de tempo profundo / GOE (Etapa 4E) e o padrão genérico de `Scene` + `State Types` revisados (Etapa 4F) · 12/06/2026
**Escopo desta etapa (e seus limites):** aplicar o **padrão genérico de `Scene`** (4F) a uma **terceira cena, híbrida** — tempo profundo **com** evento relativamente pontual (impacto), extinção em massa e perturbação do sistema terrestre (atmosfera, oceanos, clima, vida terrestre e marinha) —, e fazer a **primeira instanciação oficial de `OceanographicState`**. Conforme solicitado, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** cria milhares de eventos, **não** usa Wikidata/Wikipedia como autoridade, **não** copia texto de fontes, **não** usa mídia como evidência factual, **não** inventa paleomapa e **não** inventa precisão onde há incerteza.

**O que herda e respeita.** O padrão de `Scene` e os 11 `State Types` oficiais da 4F (incl. `OceanographicState`, aqui instanciado); os nós de 4B/4C (`evt:extincao-kpg`→reframe para `proc:extincao-kpg`, `entity:dinossauros-nao-avianos`, `place:chicxulub`→`place:cratera-chicxulub`, `claimset:k-pg-causa`/CS4); os invariantes de exibição e a disciplina ClaimSet × UncertaintyProfile.

> **Diferencial que esta cena prova (o terceiro):** 1789 provou a simultaneidade **histórica**; 2,4 Ga provou a simultaneidade **planetária profunda**; **66 Ma / K-Pg** prova a **cena híbrida** — um **evento pontual** (impacto) desencadeando **processos longos** e **States** de todo o sistema terrestre, com extinções **seletivas** e recuperação.

> **Disciplina central (Etapa 3.1 + regra da etapa):** **não** reduzir K-Pg a "meteoro matou dinossauros". O impacto de Chicxulub é a **causa central fortemente sustentada**; o vulcanismo do Deccan entra como **fator contribuinte/debate legítimo**, **sem** falsa equivalência (as fontes sustentam pesos diferentes). Aves **são** dinossauros que sobreviveram. "66 Ma" é **aproximação geológica de alta resolução relativa**, não data histórica exata.

---

## Sumário

1. Objeto conceitual da cena 66 Ma / K-Pg (Tarefa 1)
2. Itens centrais da cena (Tarefa 2)
3. States da cena (Tarefa 3)
4. `OceanographicState` oficial (Tarefa 4)
5. Evidências e claims científicos (Tarefa 5)
6. ClaimSets e incertezas (Tarefa 6)
7. Anacronismo espacial em 66 Ma (Tarefa 7)
8. Relationship Graph da cena (Tarefa 8)
9. Globo/mapa da cena (Tarefa 9)
10. Timeline da cena (Tarefa 10)
11. Dossiê da cena (Tarefa 11)
12. Relatório de qualidade da cena (Tarefa 12)
13. Próximos passos para a Etapa 4H (Tarefa 13)

---

## 1. Objeto conceitual da cena 66 Ma / K-Pg (Tarefa 1)

**`scene:earth-66ma-kpg-extinction`** (instância do padrão genérico de `Scene`, 4F §2)
- **id:** `scene:earth-66ma-kpg-extinction` · **pilotCode:** SCENE-KPG · **version:** 1.0
- **título:** A Terra há ~66 Ma — a extinção K-Pg e o impacto de Chicxulub
- **focusItem:** `proc:extincao-kpg` (com `evt:impacto-chicxulub` como gatilho)
- **queryType:** **cena híbrida** — tempo profundo + evento pontual + sistema terrestre (taxonomia 4F: tipos 7+1+12+10)
- **TimeRange:** **~66 Ma** (limite K-Pg), com janela ~67–63 Ma (antes/recuperação) · **TimePrecision:** `Ma` de **alta resolução relativa** (o limite K-Pg é dos mais bem datados do tempo profundo) — ainda **aproximação**, não data exata
- **escopo espacial:** **global**, com **um ponto localizado** (cratera de Chicxulub) — diferença-chave em relação ao GOE
- **camadas ativadas (4A):** 2 Astronomia (impactor) · 4 Atmosfera · 5 Clima · 7 Oceanos · 6 Tectônica/paleogeografia · 8 Vida/evolução · 9 Paleobiologia/extinções · 25 Fontes/meta
- **centralItems:** `evt:impacto-chicxulub`, `proc:extincao-kpg`, `place:cratera-chicxulub`, `concept:limite-kpg`, `concept:anomalia-iridio`, `concept:extincao-em-massa`, `entity:dinossauros-nao-avianos`, `entity:aves`, `entity:mamiferos`, `entity:plancton-marinho`, `proc:recuperacao-ecologica-pos-kpg`, `proc:vulcanismo-deccan-traps`
- **contextualItems:** os 7 States (atmosfera, clima, oceano, bioma terrestre, bioma marinho, paleogeografia, tectônica Deccan), `concept:inverno-impacto`, `concept:proxy-geoquimico`
- **sensitiveItems:** **nenhum** editorial-humano (sem Leis 10.639/11.645). **Exceção:** cruzamento com **negacionismo de idade da Terra/evolução** → tratado **fora** de ClaimSet (como Big Bang/GOE)
- **Claims principais:** "Há ~66 Ma, o impacto de um asteroide em Chicxulub desencadeou uma extinção em massa que eliminou os dinossauros não-avianos e reorganizou a biosfera" — `inferência científica`, **consenso amplo** para impacto-como-gatilho-central; pesos causais finos em ClaimSet
- **ClaimSets:** `claimset:k-pg-causa`, `claimset:kpg-ritmo-extincao`, `claimset:kpg-mecanismos-mortalidade`, `claimset:kpg-incendios`, `claimset:kpg-acidificacao-oceanica`, `claimset:kpg-seletividade` · **UncertaintyProfiles:** `uncertaintyprofile:kpg-inverno-intensidade-duracao`, `uncertaintyprofile:kpg-recuperacao-tempo`, `uncertaintyprofile:paleogeografia-66ma`
- **States:** `state:atmosfera-pos-impacto-kpg`, `state:clima-pos-impacto-kpg`, `state:oceanos-pos-impacto-kpg` (**OceanographicState oficial**), `state:bioma-terrestre-kpg`, `state:bioma-marinho-kpg`, `state:paleogeografia-66ma`, `state:tectonica-deccan-66ma`
- **fontes A/B necessárias:** PBDB (A); Macrostrat/ICS (escala, A/B); USGS (A); NOAA/NCEI Paleo (A); GPlates/EarthByte (paleogeografia, A, CC BY); geociências revisadas (A/B)
- **evidenceProfile:** **misto** — geoquímico (irídio, esférulas), estratigráfico (camada-limite), estrutural (cratera) e paleontológico (registro fóssil) — distinção que a cena deve manter clara
- **reviewStatus (da cena):** núcleo factual `approved` (revisão científica do piloto); pesos causais, paleogeografia, mecanismos finos `pending`
- **editorialRisk:** **baixo** (só nota antinegacionismo)
- **scientificRisk:** **médio-alto** — pesos causais (impacto×Deccan), ritmo, mecanismos de mortalidade, paleogeografia
- **licenseRisk:** **baixo** (fontes verdes; risco 0–1; Deep Time Maps **proibido**)
- **publicabilityStatus:** **Nível 2 — parcialmente publicável** (4F §9): núcleo exibível; itens incertos mediados
- **timelineBehavior:** **evento pontual** (impacto) sobre **processos longos** (extinção, Deccan, recuperação) e States de fundo (ver §10)
- **globeBehavior:** globo **paleogeográfico rotulado** com **marcador localizado** (Chicxulub) + overlays de atmosfera/oceano/bioma (ver §9)
- **dossierBehavior:** 20 blocos, com ênfase em sistema terrestre e "como sabemos" (ver §11)
- **simultaneityBehavior:** "o planeta em 66 Ma" — um instante de **crise sistêmica** encadeada a partir de um ponto
- **anachronismPolicy:** sem países; "México" não existe em 66 Ma; continentes em configuração diferente; placa indiana em outra latitude; aves ≠ "todos os dinossauros morreram"; marcadores de evidência atual ≠ posição paleogeográfica (ver §7)

---

## 2. Itens centrais da cena (Tarefa 2)

A distinção **Event × Process × State** é o teste central desta cena: o **impacto** é um `Event` (relativamente pontual); a **extinção** é um `Process` (intervalo); as **condições do sistema** são `States`. Itens existentes são referenciados/normalizados; novos recebem template. **Regra:** representar o **sistema terrestre** (impacto → atmosfera → clima → oceanos → ecossistemas → extinções seletivas → recuperação), nunca "meteoro matou dinossauros".

**`evt:impacto-chicxulub`** *(novo)* — o gatilho pontual
- knowledgeItemId: `evt:impacto-chicxulub` · tipo: `Event` · camadaP: 2 Astronomia/SS · camadasS: 9, 4, 6 · título: Impacto de Chicxulub
- TimeRange: ~66 Ma · TimePrecision: `Ma` (alta resolução relativa) · Place/Region: `place:cratera-chicxulub` (Yucatán atual)
- ClaimPrinc: "Um asteroide de ~10 km atingiu a região de Chicxulub há ~66 Ma, formando uma cratera de ~180–200 km" — `inferência científica`, **alta** · ClaimTemp: ~66 Ma — `inferência` (datação radiométrica + estratigrafia) · ClaimEsp: Yucatán (cratera soterrada; `SpatialUncertainty` baixa para a cratera, mas **posição paleogeográfica** distinta da atual).
- Source: USGS/geociências (A/B); PBDB `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `registro material` (cratera, ejecta, irídio) · uncert: baixa na existência; média em parâmetros finos (ângulo, tamanho exato).
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 0–1.
- rels: **`causou` `proc:extincao-kpg`** (gatilho); `produziu` `concept:anomalia-iridio`, ejecta/quartzo chocado; `localizado-em` `place:cratera-chicxulub`; `perturbou` `state:atmosfera-pos-impacto-kpg`.
- timeline: **evento pontual** (~66 Ma) — o único ponto da cena · globe: **marcador localizado** em Chicxulub (paleoposição rotulada) · simultaneidade: o instante-gatilho do colapso.

**`proc:extincao-kpg`** *(reframe de SCI-21 `evt:extincao-kpg`)* — a extinção como intervalo
- knowledgeItemId: `proc:extincao-kpg` · tipo: **`Process`** (reframe: a extinção é um **intervalo**, não um ponto) · camadaP: 9 Paleobiologia/extinções · camadasS: 8, 4, 5, 7 · título: Extinção em massa K-Pg
- TimeRange: ~66 Ma (intervalo curto em escala geológica) · Place/Region: global · ClaimPrinc: "A extinção K-Pg eliminou os dinossauros não-avianos e ~grande parte das espécies, marinhas e terrestres" — `inferência científica`, **alta** (fato); ritmo/mecanismos em ClaimSet · ClaimTemp: ~66 Ma — `inferência` · ClaimEsp: global.
- Source: PBDB (A); Macrostrat (escala) · conf: **alta** (extinção), **média** (ritmo/seletividade fina) · evid: `registro material` (registro fóssil) · uncert: ritmo e mecanismos em ClaimSet.
- review: `approved` (fato) · scientificRisk: médio-alto · editorialRisk: baixo (idade/evolução × negacionismo, **fora** de ClaimSet) · licenseRisk: 1.
- rels: `decorreu-de` `evt:impacto-chicxulub`; `qualificado-por` `claimset:k-pg-causa`, `claimset:kpg-ritmo-extincao`, `claimset:kpg-seletividade`; `causou` desaparecimento de `entity:dinossauros-nao-avianos`; `seguido-por` `proc:recuperacao-ecologica-pos-kpg`.
- timeline: **processo/intervalo** (não ponto) · globe: turnover global (overlay de bioma) · simultaneidade: a crise biótica. · **nota de normalização:** substitui o enquadramento `evt:extincao-kpg` do 4B (SCI-21) — a extinção é Process; o Event é o impacto.

**`place:cratera-chicxulub`** *(refina `place:chicxulub` de 4C)*
- tipo: `Place` · camadaP: 6 · título: Cratera de Chicxulub · variantes: ["Chicxulub crater"] · TimeRange: impacto ~66 Ma · geometryStatus: **inferido** (estrutura soterrada, geofísica) · ModernCorr: península de Yucatán, México (**localidade atual**; em 66 Ma, posição paleogeográfica distinta) · SpatialUncertainty: média (extensão) · Source: USGS/geociências (A/B) · riscoEd: baixo · riscoLic: 1.
- rels: `local-de` `evt:impacto-chicxulub`; `evidência-de` o impacto. · simultaneidade: **o ponto** da cena (raro em tempo profundo).

**`concept:limite-kpg`** *(novo)* · Limite K-Pg (camada-limite)
- knowledgeItemId: `concept:limite-kpg` · tipo: `Concept` · camadaP: 9 · camadasS: 25 · def: o nível estratigráfico global que marca a fronteira Cretáceo-Paleogeno, frequentemente uma fina camada de argila enriquecida em irídio.
- ClaimPrinc: "O limite K-Pg é um marcador estratigráfico global do evento de extinção" — `fato documentado` (estratigrafia)/`inferência`, alta · Source: Macrostrat/ICS (A/B); geociências · conf: alta · evid: `registro material`.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `evidência-de` `proc:extincao-kpg`; contém `concept:anomalia-iridio`. · ling. escolar: "uma linha no registro das rochas que separa dois mundos".

**`concept:anomalia-iridio`** *(novo)* · Anomalia de irídio
- knowledgeItemId: `concept:anomalia-iridio` · tipo: `Concept` · camadaP: 25/9 · def: enriquecimento global de irídio na camada-limite K-Pg, elemento raro na crosta e mais comum em asteroides.
- ClaimPrinc: "A anomalia global de irídio é uma evidência-chave de origem extraterrestre do evento" — `inferência científica`, alta · Source: geociências (A/B) · conf: alta · evid: `registro material` (geoquímica).
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `evidencia` `evt:impacto-chicxulub`; `parte-de` `concept:limite-kpg`. · ling.: "uma pista química que aponta para o céu".

**`concept:extincao-em-massa`** *(novo)* · Extinção em massa
- knowledgeItemId: `concept:extincao-em-massa` · tipo: `Concept` · camadaP: 9 · def: perda rápida e global de grande proporção das espécies. · ClaimPrinc: "É uma das poucas grandes extinções em massa do Fanerozoico" — `interpretação`/`inferência`, alta · Source: PBDB (A) · conf: alta · evid: `registro material`.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `explica` `proc:extincao-kpg`; `relacionado-a` `evt:extincao-permiano-triassico` (SCI-20, outra extinção). · ling.: contextualiza K-Pg entre as "cinco grandes".

**`concept:inverno-impacto`** *(novo)* · Inverno de impacto
- knowledgeItemId: `concept:inverno-impacto` · tipo: `Concept` · camadaP: 5 Clima · camadasS: 4 · def: resfriamento global causado por poeira/aerossóis/fuligem que bloqueiam a luz solar após um grande impacto.
- ClaimPrinc: "O bloqueio da luz solar teria causado resfriamento e colapso da fotossíntese" — `hipótese`/`inferência`, média-alta · Source: geociências/modelos (A/B) · conf: média-alta · evid: `dado modelado` + `inferência indireta`.
- review: `pending` (intensidade/duração em UncertaintyProfile) · scientificRisk: médio-alto · editorialRisk: baixo · licenseRisk: 1.
- rels: `explica` parte de `proc:extincao-kpg`; intensidade em `uncertaintyprofile:kpg-inverno-intensidade-duracao`. · ling.: mecanismo plausível, com magnitude incerta.

**`entity:dinossauros-nao-avianos`** *(4C — existente, aprofundado)*
- tipo: `Entity` (grupo) · camadaP: 9 · TimeRange: ~Triássico–66 Ma · ClaimPrinc: "Extinguiram-se no K-Pg (~66 Ma)" — `inferência científica`, alta · evid: `registro material`.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `afetado-por` `proc:extincao-kpg` (extinção). · nomenclatura: **"não-avianos" é essencial — aves SÃO dinossauros** (ver `entity:aves`).

**`entity:aves`** *(novo)* · Aves (dinossauros avianos sobreviventes)
- knowledgeItemId: `entity:aves` · tipo: `Entity` (grupo biológico) · camadaP: 8 · camadasS: 9 · TimeRange: ~Jurássico–presente · ClaimPrinc: "As aves são dinossauros avianos que **sobreviveram** ao K-Pg" — `inferência científica`, alta · Source: PBDB/biologia (A) · conf: alta · evid: `registro material` + filogenia.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `sobreviveu-a` `proc:extincao-kpg`; `relacionado-a` `entity:dinossauros-nao-avianos` (clado-irmão sobrevivente). · nomenclatura: **corrige a simplificação** "todos os dinossauros morreram".

**`entity:mamiferos`** *(novo)* · Mamíferos
- knowledgeItemId: `entity:mamiferos` · tipo: `Entity` (grupo biológico) · camadaP: 8 · camadasS: 9 · TimeRange: ~Triássico–presente · ClaimPrinc: "Mamíferos sobreviveram ao K-Pg e diversificaram-se depois" — `inferência científica`, alta · Source: PBDB (A) · conf: alta · evid: `registro material`.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `sobreviveu-a` `proc:extincao-kpg`; `beneficiado-por` `proc:recuperacao-ecologica-pos-kpg` (oportunidade ecológica). · nomenclatura: **"mamíferos dominaram logo depois" é simplificação** — a radiação levou tempo (ver §7).

**`entity:plancton-marinho`** *(novo)* · Plâncton marinho (foraminíferos, nanoplâncton)
- knowledgeItemId: `entity:plancton-marinho` · tipo: `Entity` (grupo) · camadaP: 8 · camadasS: 7, 9 · TimeRange: ~contínuo · ClaimPrinc: "Grupos de plâncton calcário sofreram forte extinção/turnover no K-Pg" — `inferência científica`, alta · Source: PBDB/geociências (A) · conf: alta · evid: `registro material` (microfósseis).
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: `afetado-por` `proc:extincao-kpg`, `state:oceanos-pos-impacto-kpg`; evidencia o colapso da produtividade. · simultaneidade: a **base marinha** atingida.

**`proc:recuperacao-ecologica-pos-kpg`** *(novo)* · Recuperação ecológica pós-K-Pg
- knowledgeItemId: `proc:recuperacao-ecologica-pos-kpg` · tipo: `Process` · camadaP: 8 · camadasS: 9 · TimeRange: ~66 Ma em diante (centenas de ka a Ma) · Place/Region: global
- ClaimPrinc: "A biosfera recuperou-se por sucessão ao longo do Paleoceno, com radiação de mamíferos e aves" — `inferência científica`, média-alta · ClaimTemp: ~66–60 Ma (faixa) · ClaimEsp: global.
- Source: PBDB (A) · conf: média-alta · evid: `registro material` · uncert: tempo de recuperação em UncertaintyProfile.
- review: `pending` (`uncertaintyprofile:kpg-recuperacao-tempo`) · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: `sucessor-de` `proc:extincao-kpg`; `beneficiou` `entity:mamiferos`, `entity:aves`. · timeline: processo posterior · simultaneidade: o "depois" da cena.

**`proc:vulcanismo-deccan-traps`** *(novo)* · Vulcanismo do Deccan (fator em debate)
- knowledgeItemId: `proc:vulcanismo-deccan-traps` · tipo: `Process` · camadaP: 6 Tectônica · camadasS: 4, 5, 9 · TimeRange: ~ antes e depois de 66 Ma (atravessa o limite) · Place/Region: Índia atual (placa indiana em **outra** latitude em 66 Ma)
- ClaimPrinc: "O vulcanismo dos Deccan Traps ocorreu em torno do limite K-Pg e é debatido como **fator contribuinte**" — `hipótese`/`inferência`, média · ClaimTemp: ~ em torno de 66 Ma · ClaimEsp: Índia (paleoposição distinta).
- Source: geociências (A/B); GPlates (paleoposição) `PENDENTE_CONFIRMACAO_FONTE` · conf: média · evid: `registro material` (basaltos) · uncert: peso causal relativo ao impacto (ver `claimset:k-pg-causa`).
- review: `pending` · scientificRisk: **médio-alto** · editorialRisk: baixo · licenseRisk: 1.
- rels: `contribuiu-para` (debate) `proc:extincao-kpg` via `claimset:k-pg-causa`; **não** apresentado em equivalência com o impacto. · timeline: **processo paralelo** atravessando o limite · simultaneidade: o fator vulcânico de fundo.

---

## 3. States da cena (Tarefa 3)

Sete States instanciados — incluindo a **primeira instanciação oficial de `OceanographicState`** (detalhada na §4). `representationType ∈ {medição, reconstrução modelada, aproximação didática}`.

| State (`knowledgeItemId`) | State Type | TimeRange | spatialScope | claims mínimos | fontes | conf | evid | uncertaintyProfile | representationType | globeBehavior | timelineBehavior | review | sciRisk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `state:atmosfera-pos-impacto-kpg` | AtmosphereState | ~66 Ma (crise breve) | global | "atmosfera carregada de poeira/aerossóis/fuligem, bloqueando luz" | NOAA Paleo/modelos (A/B) | média-alta | dado modelado + registro material (fuligem) | densidade/duração incertas | reconstrução modelada | halo opaco/escurecido (didático) | State de transição (curto) | pending | médio-alto |
| `state:clima-pos-impacto-kpg` | ClimateState | ~66 Ma → recuperação | global | "resfriamento abrupto (inverno de impacto), depois recuperação" | NOAA Paleo/modelos (A/B) | média | dado modelado | intensidade/duração em UP | reconstrução modelada | overlay de resfriamento (didático) | State de transição | pending | médio-alto |
| `state:oceanos-pos-impacto-kpg` | **OceanographicState** | ~66 Ma → recuperação | global | "colapso de produtividade ('oceano Strangelove'); perturbação/acidificação" | NOAA Paleo/PBDB (A) | média | registro material (foraminíferos, isótopos de C) | acidificação/circulação incertas | reconstrução modelada | overlay oceânico oficial (ver §4) | State de transição | pending | médio-alto |
| `state:bioma-terrestre-kpg` | BiomeState | ~66 Ma | global (continentes) | "colapso de ecossistemas terrestres; extinção de dinossauros não-avianos; flora perturbada (pico de fungos/samambaias)" | PBDB (A) | média-alta | registro material (pólen, fósseis) | variação regional | reconstrução modelada | overlay biótico terrestre | State de fundo | pending | médio |
| `state:bioma-marinho-kpg` | BiomeState | ~66 Ma | oceanos | "extinção/turnover de plâncton calcário, amonites; reorganização marinha" | PBDB (A) | alta | registro material (microfósseis) | seletividade fina | reconstrução modelada | overlay biótico marinho | State de fundo | pending | médio |
| `state:paleogeografia-66ma` | PaleogeographicState | ~66 Ma | global | "continentes próximos da configuração atual, mas distintos; Atlântico mais estreito; Índia separada migrando ao norte" | GPlates/EarthByte (A, CC BY) | **média** (melhor que 2,4 Ga, ainda incerta) | dado modelado | `uncertaintyprofile:paleogeografia-66ma` | reconstrução modelada (rotulada) | globo paleogeográfico rotulado | State de fundo | pending | médio |
| `state:tectonica-deccan-66ma` | TectonicState | ~ em torno de 66 Ma | Índia (paleoposição) | "grande província ígnea (Deccan) ativa em torno do limite" | USGS/geociências (A/B) | média-alta | registro material (basaltos) | duração/volume e relação com o limite | reconstrução modelada | marcador Deccan (paleoposição) | processo/State paralelo | pending | médio-alto |

**Nota.** Em 66 Ma a paleogeografia tem **confiança média** (melhor que os ~2,4 Ga do GOE, pior que 1789) — exemplo de como o mesmo `PaleogeographicState` varia de confiança conforme o regime de tempo (4F §4). Nenhum paleomapa é inventado: sem geometria validada, `PENDENTE_REFINAMENTO_ESPACIAL`.

---

## 4. `OceanographicState` oficial (Tarefa 4)

**Primeira instanciação oficial de `OceanographicState`** após a aprovação na Etapa 4F (§5). Valida os campos da especificação contra uma cena real.

**`state:oceanos-pos-impacto-kpg`**
- **id:** `state:oceanos-pos-impacto-kpg` · **State Type:** `OceanographicState`
- **timeRange:** ~66 Ma (crise breve) → recuperação ao longo do Paleoceno
- **spatialScope:** global (com variação regional `PENDENTE_REFINAMENTO_ESPACIAL`)
- **oceanConfiguration:** oceanos do Cretáceo Superior (Atlântico mais estreito, mares epicontinentais amplos) — **reconstrução modelada** (liga a `state:paleogeografia-66ma`)
- **seaLevel:** alto no Cretáceo Superior, em regressão geral — **faixa**, `PENDENTE_REFINAMENTO_ESPACIAL` no detalhe
- **redoxState:** majoritariamente **oxigenado** na superfície (oceano fanerozoico), com possíveis perturbações transientes — **contraste explícito com o oceano ferruginoso/anóxico de 2,4 Ga**
- **dissolvedIron:** **não aplicável** como condição dominante (≠ GOE) — campo presente, mas marcado N/A; demonstra que o tipo serve a oceanos muito diferentes
- **oxygenation:** oxigenado (liga a `state:atmosfera-pos-impacto-kpg`); possível estresse transiente
- **circulationPattern:** circulação do Cretáceo Superior — **reconstrução**, incerteza média-alta
- **temperatureProfile:** pulso de **resfriamento** pós-impacto (liga a `state:clima-pos-impacto-kpg`), depois recuperação — faixa
- **iceCover:** mínima (mundo de efeito estufa) — qualitativo
- **salinityProfile:** **PENDENTE** (sem proxy fino confiável — não inventar)
- **biologicalContext:** referência a `state:bioma-marinho-kpg` (colapso de plâncton) — **não duplica** a vida
- **evidenceClaims:** turnover de foraminíferos; **excursão isotópica de carbono** (queda de produtividade, "oceano Strangelove"); argila da camada-limite (ver §5, E7–E9)
- **uncertaintyProfile:** acidificação, circulação e duração da crise = **incerteza média-alta**
- **sources:** NOAA/NCEI Paleo (A, PD); PBDB (A); geociências (A/B) `PENDENTE_CONFIRMACAO_FONTE`
- **representationType:** **reconstrução modelada**
- **reviewStatus:** `pending` (revisão científica; núcleo do colapso de produtividade é robusto)

**Por que este State não é apenas...**
- **...ClimateState:** o `ClimateState` cobre temperatura/clima atmosférico; **não** cobre redox, acidificação, circulação ou produtividade **oceânica**. O colapso de produtividade ("Strangelove ocean") e a acidificação são condições **do oceano**, não do clima.
- **...BiomeState:** o `BiomeState` marinho cobre a **vida** (plâncton, amonites); **não** cobre o **meio físico-químico** (redox, acidez, circulação) em que essa vida colapsou. São complementares, não o mesmo.
- **...PaleogeographicState:** o paleogeográfico cobre **onde** estavam os oceanos (configuração/posição); **não** cobre **como estavam** (química/física internas).
- **Globo:** overlay oceânico oficial — perturbação/acidificação **didática** rotulada; cor/tom não afirmados como medição.
- **Dossiê:** bloco "Oceanos pós-impacto" (ver §11), com a excursão de carbono explicada como evidência.
- **Incertezas que carrega:** grau/extensão da acidificação; mudanças de circulação; duração da crise; variação regional — todas em `uncertaintyProfile`, nunca number-seco.

**Veredito da instanciação:** o `OceanographicState` **funcionou** como tipo oficial — acomodou um oceano (66 Ma: oxigenado, em crise de produtividade) radicalmente diferente do que motivou sua criação (2,4 Ga: anóxico, ferruginoso), **sem** forçar `Climate`/`Biome`/`Paleogeographic`. Confirma a decisão da 4F (ver §12, item 19).

---

## 5. Evidências e claims científicos (Tarefa 5)

O aluno deve entender **"como sabemos disso"** sem confundir **evidência geoquímica** (irídio), **estrutural** (cratera), **estratigráfica** (camada-limite), **paleontológica** (registro fóssil) e **interpretação causal**. Cada linha é um claim de evidência (texto próprio).

| # | Claim (texto próprio) | claimType | EvidenceLevel | Conf | Fonte A/B | Incerteza | Relação com K-Pg | Caráter | No dossiê |
|---|---|---|---|---|---|---|---|---|---|
| E1 | "Uma anomalia global de irídio marca a camada-limite K-Pg" | `inferência científica` | registro material | **alta** | geociências (A/B) | calibração entre seções | evidência de origem extraterrestre | **proxy geoquímico** | "Evidências geoquímicas" |
| E2 | "A cratera de Chicxulub, da idade e tamanho compatíveis, registra o impacto" | `inferência científica` | registro material | **alta** | USGS (A/B) | parâmetros finos do impacto | evidência **estrutural** do impacto | **estrutura/medição** | "O impacto Chicxulub" |
| E3 | "Grãos de quartzo chocado indicam pressões típicas de impacto" | `inferência científica` | registro material | alta | geociências (A/B) | distribuição global | evidência de impacto | **proxy mineralógico** | "Evidências geoquímicas e estratigráficas" |
| E4 | "Esférulas/ejetos distribuídos globalmente são compatíveis com ejeção de impacto" | `inferência científica` | registro material | alta | geociências (A/B) | correlação entre sítios | evidência de impacto | **proxy** | "Como sabemos disso" |
| E5 | "A camada-limite K-Pg é um marcador estratigráfico global" | `fato documentado` | registro material | alta | Macrostrat/ICS (A/B) | correlação regional | marco do evento | **estratigráfico** | "Evidências... estratigráficas" |
| E6 | "O registro fóssil mostra desaparecimento abrupto de muitos grupos no limite" | `inferência científica` | registro material | alta | PBDB (A) | completude do registro (efeito Signor-Lipps) | evidência da extinção | **paleontológico** | "Vida terrestre/marinha" |
| E7 | "Grupos de plâncton calcário sofrem extinção/turnover acentuado no limite" | `inferência científica` | registro material | alta | PBDB (A) | seletividade fina | evidência marinha | **paleontológico** | "Vida marinha" |
| E8 | "Uma excursão isotópica de carbono indica colapso de produtividade oceânica" | `inferência científica` | registro material | média-alta | geociências (A/B) | duração/magnitude | evidência **oceânica** (Strangelove) | **proxy isotópico** | "Oceanos pós-impacto" |
| E9 | "Indicadores climáticos sugerem perturbação/resfriamento pós-impacto" | `hipótese`/`inferência` | dado modelado + registro material | média | NOAA Paleo/modelos (A/B) | intensidade/duração | evidência de perturbação climática | **proxy + modelo** | "Atmosfera pós-impacto" |
| E10 | "Os basaltos do Deccan registram vulcanismo intenso em torno do limite" | `inferência científica` | registro material | alta (existência) | USGS/geociências (A/B) | timing fino e **peso causal** | fator em **debate** (não causa central) | **registro vulcânico** | "Tectônica, Deccan e paleogeografia" |

**Princípio (Etapa 3.1 em tempo profundo):** distinguir **o que cada evidência sustenta**. O irídio (E1) e a cratera (E2) sustentam **o impacto**; o registro fóssil (E6–E7) sustenta **a extinção**; a excursão de carbono (E8) sustenta **o colapso oceânico**; os basaltos (E10) sustentam **a existência do Deccan** — **não** automaticamente seu peso causal. Confundir esses níveis é o erro a evitar. Mídia (foto de afloramento, gráfico isotópico) **ilustra**, nunca **prova**.

---

## 6. ClaimSets e incertezas da cena (Tarefa 6)

**ClaimSet** (lados discretos legítimos) × **UncertaintyProfile** (faixa). **Regra crítica desta cena:** o impacto de Chicxulub é a **explicação central fortemente sustentada**; o Deccan entra como **fator contribuinte/debate**, **sem falsa equivalência** — as fontes sustentam **pesos diferentes**, e a exibição deve refletir isso.

**`claimset:k-pg-causa`** *(CS4 de 4C — aprofundado)* — ClaimSet **com pesos assimétricos**
- tema: causa principal da extinção · consensusStatus: **debate acadêmico com posição majoritária** · claims: (a) **impacto de Chicxulub como gatilho/causa principal** — *fortemente sustentado, peso alto*; (b) **Deccan Traps como fator contribuinte/estressor** — *peso menor, legítimo*; (c) **combinação/sinergia** — *crescentemente aceita* · conf por claim: (a) **alta**; (b) média; (c) média-alta · **sem equivalência:** negar o impacto ou a extinção (negacionismo, **fora** do ClaimSet); **e também:** apresentar (a) e (b) como **equivalentes** — a exibição deve mostrar o impacto como dominante · fontes: PBDB/geociências (A/B) · review: pending · nota científica: **assimetria de peso é parte do claim** · impacto: exibir hierarquia de evidência, não "dois lados iguais".

**`claimset:kpg-ritmo-extincao`** *(novo)* — ClaimSet
- tema: ritmo da extinção (abrupta × em declínio prévio) · consensusStatus: **debate acadêmico** · claims: (a) extinção abrupta no limite; (b) alguns grupos já em declínio antes · conf: média · fontes: PBDB (A) · review: pending · nota: **efeito Signor-Lipps** (lacunas do registro) complica leituras de "declínio gradual" · impacto: exibir as leituras com a ressalva do registro.

**`claimset:kpg-mecanismos-mortalidade`** *(novo)* — ClaimSet
- tema: mecanismos de mortalidade (escuridão/colapso da fotossíntese × resfriamento × incêndios × acidificação × chuva ácida) · consensusStatus: **hipóteses concorrentes/combinadas** · claims: os vários mecanismos, provavelmente **combinados** · conf: média · fontes: geociências/modelos (A/B) · review: pending · nota: provavelmente **múltiplos mecanismos**, não um só · impacto: exibir como cascata, com pesos incertos.

**`claimset:kpg-incendios`** *(novo)* — ClaimSet
- tema: extensão dos incêndios globais pós-impacto · consensusStatus: **hipóteses concorrentes** · claims: (a) incêndios globais amplos; (b) incêndios mais localizados/limitados · conf: média-baixa · fontes: geociências (A/B) · review: pending · nota: evidência de fuligem debatida em extensão · impacto: tratar com **cautela** (a etapa pediu cautela com incêndios/ejeção).

**`claimset:kpg-acidificacao-oceanica`** *(novo)* — ClaimSet
- tema: ocorrência/intensidade da acidificação oceânica · consensusStatus: **debate acadêmico** · claims: (a) acidificação significativa contribuindo para extinção de calcificadores; (b) papel mais modesto · conf: média · fontes: geociências (A/B) · review: pending · nota: liga-se a `state:oceanos-pos-impacto-kpg` · impacto: exibir como fator oceânico debatido.

**`claimset:kpg-seletividade`** *(novo)* — ClaimSet
- tema: seletividade das extinções (quem morre × quem sobrevive e por quê) · consensusStatus: **debate acadêmico** · claims: hipóteses sobre traços de sobrevivência (tamanho, dieta, hábitat, capacidade de dormência/aquático) explicando por que aves/mamíferos/alguns grupos passaram · conf: média · fontes: PBDB (A) · review: pending · nota: **inclui a sobrevivência de aves e mamíferos** (pedido da Tarefa 6, item 9) · impacto: exibir padrões de seletividade como debate, não regra simples.

**`uncertaintyprofile:kpg-inverno-intensidade-duracao`** *(novo)* — **UncertaintyProfile**
- tema: intensidade e duração do inverno de impacto · natureza: **faixa** (anos a décadas; queda de temperatura em faixa) · consensusStatus: consenso de que **houve** perturbação; **incerteza** sobre **quanto/quanto tempo** · conf: média · fontes: modelos/geociências (A/B) · review: pending · nota: **não inventar precisão** de °C ou de anos · impacto: exibir como faixa com barras de incerteza.

**`uncertaintyprofile:kpg-recuperacao-tempo`** *(novo)* — **UncertaintyProfile**
- tema: tempo de recuperação ecológica · natureza: **faixa** (centenas de ka a alguns Ma) · consensusStatus: consenso de recuperação por sucessão; **incerteza** no tempo e no padrão · conf: média · fontes: PBDB (A) · review: pending · nota: varia por grupo/ambiente · impacto: faixa, não número único.

**`uncertaintyprofile:paleogeografia-66ma`** *(novo)* — **UncertaintyProfile**
- tema: posições continentais a 66 Ma · natureza: incerteza **média** (menor que 2,4 Ga) · consensusStatus: configuração geral conhecida; detalhes incertos · conf: média · fontes: GPlates/EarthByte (A, CC BY) · review: pending · nota: **não inventar paleomapa**; rotular reconstrução · impacto: globo paleogeográfico rotulado.

---

## 7. Anacronismo espacial em 66 Ma (Tarefa 7)

Como em 2,4 Ga, não há países; mas, ao contrário do GOE, há uma **localidade pontual** (Chicxulub) e uma paleogeografia de **confiança média** — o que cria riscos próprios. Oito casos obrigatórios.

| Caso | Risco de anacronismo | Correção conceitual | Place/Region correto | No dossiê | No globo/mapa |
|---|---|---|---|---|---|
| 1. Não existem países atuais | falar de nações em 66 Ma | só há um **planeta** com configuração distinta | nenhum `region:` político | aviso "sem países" | sem rótulos nacionais |
| 2. "México" em 66 Ma | dizer que o impacto foi "no México" | o México não existia; a **localidade atual** é Yucatán | `place:cratera-chicxulub` (localidade atual) | "onde **hoje** é Yucatán" | marcador rotulado "localidade atual" |
| 3. Chicxulub ≠ Estado moderno | tratar a cratera como entidade política | é uma **estrutura geológica** | `place:cratera-chicxulub` (geometryStatus inferido) | "cratera soterrada" | marcador estrutural |
| 4. Continentes diferentes | exibir o mapa atual | configuração de 66 Ma era distinta (Atlântico estreito, mares epicontinentais) | `state:paleogeografia-66ma` (reconstrução) | "os continentes eram diferentes" | globo paleogeográfico rotulado |
| 5. "Dinossauros morreram" | dizer que **todos** os dinossauros se extinguiram | **não-avianos** se extinguiram; **aves sobreviveram** (são dinossauros) | `entity:dinossauros-nao-avianos` × `entity:aves` | destaque "aves = dinossauros sobreviventes" | camada de bioma diferencia clados |
| 6. "Mamíferos dominaram logo" | simplificar a radiação como imediata | a radiação levou **tempo** (Paleoceno) | `proc:recuperacao-ecologica-pos-kpg` | "a ascensão foi gradual, não imediata" | timeline mostra o intervalo |
| 7. Deccan "na Índia" | usar a posição atual da Índia | a **placa indiana** estava em **outra latitude**, migrando ao norte | `state:tectonica-deccan-66ma` (paleoposição) | "a Índia estava em outro lugar" | marcador Deccan em paleoposição rotulada |
| 8. Evidência atual ≠ posição original | supor que onde achamos a evidência é onde "aconteceu" | placas moveram-se; localidade atual ≠ posição paleogeográfica | localidades (`place:*`) **separadas** da paleoposição | "encontrada hoje em X; posição antiga incerta" | marcador atual ≠ paleoposição |

> **Diferença em relação ao GOE:** aqui há **um evento localizável** (impacto), então o globo combina **paleogeografia rotulada** + **marcador pontual** — mas o marcador deve indicar a **paleoposição** (rotulada/incerta), não a coordenada atual de Yucatán. É o ponto mais sutil da cena.

---

## 8. Relationship Graph da cena (Tarefa 8)

Malha específica de 66 Ma / K-Pg. Arestas afirmativas **são claims** (evidência/confiança) e carregam `uncertaintyNote`. A cascata causal (impacto → atmosfera → clima → produtividade → cadeias → extinção) é o coração da cena.

| relId | sourceItem | relationshipType | targetItem | claim/evidence | conf | review | uncertaintyNote | obs. científica |
|---|---|---|---|---|---|---|---|---|
| rel:K01 | `evt:impacto-chicxulub` | produziu | ejecta/`concept:anomalia-iridio`/quartzo chocado | registro material | alta | approved | distribuição global | evidência de impacto |
| rel:K02 | `evt:impacto-chicxulub` | perturbou | `state:atmosfera-pos-impacto-kpg` | dado modelado + fuligem | média-alta | pending | densidade/duração | injeção de poeira/aerossóis |
| rel:K03 | `state:atmosfera-pos-impacto-kpg` | causou | `state:clima-pos-impacto-kpg` (resfriamento/inverno) | dado modelado | média | pending | intensidade/duração (UP) | inverno de impacto |
| rel:K04 | `state:clima-pos-impacto-kpg` | causou | queda de produtividade primária | inferência | média-alta | pending | magnitude | colapso da fotossíntese |
| rel:K05 | queda de produtividade | causou | colapso de cadeias alimentares | inferência | média-alta | pending | seletividade | base das cadeias |
| rel:K06 | `state:oceanos-pos-impacto-kpg` | afetou | `entity:plancton-marinho` | registro material (microfósseis) | alta | pending | acidificação (CS) | Strangelove ocean |
| rel:K07 | `proc:extincao-kpg` | causou | desaparecimento de `entity:dinossauros-nao-avianos` | registro material | alta | approved | ritmo (CS) | extinção seletiva |
| rel:K08 | `proc:extincao-kpg` | poupou | `entity:aves` (sobrevivência) | registro material + filogenia | alta | approved | traços de sobrevivência (CS) | **aves = dinossauros** |
| rel:K09 | `proc:extincao-kpg` | abriu-oportunidade-para | `entity:mamiferos` | inferência | média-alta | pending | radiação **gradual** | oportunidade ecológica |
| rel:K10 | `proc:vulcanismo-deccan-traps` | contribuiu-para (debate) | `proc:extincao-kpg` | registro material (basaltos) | **média (peso menor)** | pending | peso causal (CS, assimétrico) | **sem equivalência com o impacto** |
| rel:K11 | `place:cratera-chicxulub` | evidência-de | `evt:impacto-chicxulub` | estrutura/geofísica | alta | approved | parâmetros finos | cratera |
| rel:K12 | `concept:anomalia-iridio` | evidência-global-de | `evt:impacto-chicxulub` | registro material | alta | approved | calibração | irídio |
| rel:K13 | `concept:limite-kpg` | marcador-de | `proc:extincao-kpg` | estratigrafia | alta | approved | correlação | camada-limite |
| rel:K14 | `proc:recuperacao-ecologica-pos-kpg` | sucessor-de | `proc:extincao-kpg` | registro material | média-alta | pending | tempo (UP) | sucessão pós-extinção |
| rel:K15 | `evt:impacto-chicxulub` | gatilho-de | `proc:extincao-kpg` | múltiplas evidências | alta | approved | ritmo/mecanismos (CS) | **causa central** |

> **Disciplina anti-falsa-equivalência:** K15 (impacto→extinção, causa central, alta) e K10 (Deccan→extinção, contribuinte, peso menor) **não** são simétricas — o grafo carrega o **peso** na própria aresta. Cautela explícita com a cascata atmosférica/oceânica (K02–K06): cada elo é hipótese/inferência com incerteza, não fato encadeado automaticamente.

---

## 9. Globo/mapa da cena 66 Ma (Tarefa 9)

Descrição **conceitual** (sem UI final; sem geometria inventada; **sem paleomapa inventado**). A cena combina o **globo esquemático/reconstruído de tempo profundo** (4E) com um **marcador pontual localizado** (4D) — o híbrido.

- **Foco inicial:** **planeta inteiro** (paleogeografia de 66 Ma), com **zoom disponível** ao ponto de Chicxulub.
- **Tipo de globo:** **reconstrução modelada rotulada** (GPlates) — confiança **média** (melhor que 2,4 Ga); onde faltar dado, esquemático.
- **Paleogeografia:** continentes de 66 Ma (Atlântico estreito, mares epicontinentais, Índia separada ao norte) — **sempre rotulada "reconstrução modelada"**, nunca mapa atual.
- **Marcador Chicxulub:** ponto na **paleoposição** de Yucatán (rotulada/incerta), com nota "localidade atual: Yucatán, México" — **não** a coordenada moderna.
- **Marcador Deccan Traps:** na **paleoposição** da placa indiana (outra latitude), rotulado como **fator em debate**, visualmente **subordinado** ao impacto (sem equivalência).
- **Camadas atmosféricas:** halo **opaco/escurecido** (poeira/aerossóis/fuligem) — didático, rotulado; transição de opacidade com nota de incerteza.
- **Camadas oceânicas:** overlay do `state:oceanos-pos-impacto-kpg` (**OceanographicState oficial**) — perturbação/colapso de produtividade didático; **contraste** com o oceano ferruginoso de 2,4 Ga.
- **BiomeState terrestre:** overlay de colapso ecossistêmico (ex.: pico de fungos/samambaias) — rotulado.
- **BiomeState marinho:** overlay de turnover de plâncton/amonites — rotulado.
- **Zonas de evidência atual:** marcadores "onde encontramos evidências **hoje**" (Gubbio/seções de irídio, Hell Creek/registro terrestre, seções da camada-limite) — **separados** da paleoposição.
- **Itens pending não exibidos:** paleogeografia fina, peso causal do Deccan, intensidade do inverno, acidificação — mediados ou ocultos.
- **Níveis de zoom:** (1) planeta/paleogeografia; (2) cascata sistêmica (atmosfera/oceano/bioma); (3) ponto de Chicxulub / localidades de evidência atual.
- **Legenda epistemológica:** fato · proxy · inferência · reconstrução modelada · aproximação didática.
- **Legenda temporal:** "~66 Ma (aproximação geológica de alta resolução relativa)".
- **Legenda científica:** explica irídio, quartzo chocado, camada-limite, excursão de carbono.
- **Reconstrução × aproximação didática:** distinção visual obrigatória — paleogeografia/oceano (reconstrução com dado) ≠ halo de poeira (aproximação didática); ambos rotulados.

**Obrigatórios presentes:** globo paleogeográfico rotulado ✓ · marcador Chicxulub (paleoposição) ✓ · camada de perturbação atmosférica ✓ · camada oceânica oficial via `OceanographicState` ✓ · camada de extinção/bioma ✓ · ausência de fronteiras modernas ✓ · marcadores de evidência atual como "onde encontramos hoje" ✓.

---

## 10. Timeline da cena 66 Ma (Tarefa 10)

A timeline da cena híbrida combina **um evento pontual** (impacto) com **processos longos** e **States** — o contraste com 2,4 Ga (que não tinha nenhum evento pontual). Distingue **evento pontual · processo longo · State · evidência proxy · hipótese · consequência posterior · ClaimSet · UncertaintyProfile**.

- **Zoom em ~66 Ma:** escala em **Ma** com a etiqueta "aproximação de alta resolução relativa"; o limite K-Pg é dos mais bem datados do tempo profundo.
- **Impacto como evento pontual:** `evt:impacto-chicxulub` marcado como **ponto** (o único da cena) — geologicamente quase instantâneo.
- **Extinção como processo/intervalo:** `proc:extincao-kpg` como **bloco curto** (não ponto), com ritmo em `claimset:kpg-ritmo-extincao`.
- **Deccan Traps como processo paralelo:** `proc:vulcanismo-deccan-traps` como **faixa** atravessando o limite (antes e depois) — visualmente paralelo, peso menor.
- **Perturbação atmosférica/oceânica:** `state:atmosfera-pos-impacto-kpg` e `state:oceanos-pos-impacto-kpg` como States de **transição** curtos logo após o ponto.
- **Colapso ecológico:** queda de produtividade → cadeias (cascata) exibida como sequência **logo após** o impacto.
- **Recuperação posterior:** `proc:recuperacao-ecologica-pos-kpg` como processo **estendido** (Paleoceno), com tempo em `uncertaintyprofile:kpg-recuperacao-tempo`.
- **Incerteza temporal:** ritmo da extinção, duração do inverno e tempo de recuperação com **barras de incerteza**; nada de número seco.
- **Claims e ClaimSets:** ícone de **debate** nos itens com ClaimSet (causa, ritmo, mecanismos, incêndios, acidificação, seletividade); ícone de **faixa** nos UncertaintyProfiles (inverno, recuperação, paleogeografia).
- **States de fundo:** paleogeografia, bioma terrestre/marinho como faixas paralelas.
- **Itens pending ocultos:** peso causal do Deccan, paleogeografia fina, intensidade do inverno — mediados/ocultos.
- **Itens publicáveis exibidos:** impacto, extinção (fato), anomalia de irídio, cratera, limite K-Pg, sobrevivência de aves/mamíferos.

**Distinções na timeline:** evento pontual (impacto) · processo longo (extinção, Deccan, recuperação) · State (atmosfera, clima, oceano, biomas, paleogeografia) · evidência proxy (irídio, esférulas, isótopos) · hipótese (inverno, incêndios) · consequência posterior (radiação de mamíferos) · ClaimSet (debates) · UncertaintyProfile (faixas).

---

## 11. Dossiê da cena 66 Ma (Tarefa 11)

Desenho **conceitual** do dossiê (não é plano de aula, não é currículo, não é UI final). Vinte blocos, combinando o "como sabemos" do tempo profundo (4E) com a cascata sistêmica de um evento (4D).

1. **Visão geral** — "A Terra há ~66 Ma: a extinção K-Pg" (etiqueta de aproximação geológica). O sistema terrestre em crise — não "meteoro matou dinossauros".
2. **O foco: extinção K-Pg** — `proc:extincao-kpg`: o fato (extinção) separado de ritmo/mecanismos/causa (ClaimSets).
3. **O impacto Chicxulub** — `evt:impacto-chicxulub`: o gatilho pontual; cratera, ejecta, irídio.
4. **Como era a Terra em 66 Ma** — `state:paleogeografia-66ma` (reconstrução rotulada); continentes diferentes; mundo de efeito estufa.
5. **Atmosfera pós-impacto** — `state:atmosfera-pos-impacto-kpg`; poeira/aerossóis/fuligem; `concept:inverno-impacto`.
6. **Oceanos pós-impacto** — `state:oceanos-pos-impacto-kpg` (**OceanographicState oficial**); colapso de produtividade (Strangelove), acidificação debatida.
7. **Vida terrestre** — `state:bioma-terrestre-kpg`; extinção de dinossauros não-avianos; flora perturbada; **aves sobrevivem**.
8. **Vida marinha** — `state:bioma-marinho-kpg`; turnover de plâncton e amonites.
9. **Como sabemos disso** — a cadeia de inferência, distinguindo evidência geoquímica × estrutural × estratigráfica × paleontológica × interpretação causal.
10. **Evidências geoquímicas e estratigráficas** — E1–E10: irídio, cratera, quartzo chocado, esférulas, camada-limite, registro fóssil, isótopos de C, basaltos do Deccan.
11. **ClaimSets e debates científicos** — hub dos 6 ClaimSets + 3 UncertaintyProfiles; **com pesos** (impacto dominante × Deccan contribuinte), sem falsa equivalência.
12. **Tectônica, Deccan Traps e paleogeografia** — `proc:vulcanismo-deccan-traps` (paleoposição), `state:tectonica-deccan-66ma`; nota sobre a placa indiana.
13. **Consequências biológicas** — extinções seletivas; sobrevivência de aves/mamíferos; `claimset:kpg-seletividade`.
14. **Recuperação ecológica** — `proc:recuperacao-ecologica-pos-kpg`; radiação **gradual** de mamíferos; tempo em UncertaintyProfile.
15. **Fontes e confiança** — proveniência por claim (PBDB, USGS, NOAA Paleo, GPlates); fato × proxy × inferência × reconstrução.
16. **Itens ocultos por pendência/revisão** — lista transparente do que não aparece e por quê (peso causal do Deccan, paleogeografia fina, intensidade do inverno).
17. **Como evitar anacronismos** — os 8 casos da §7: sem países; "Yucatán" hoje; aves = dinossauros; Índia em outra latitude; evidência atual ≠ paleoposição.
18. **Botão "navegar para outro período"** — para o GOE (2,4 Ga), o Cambriano, ou o presente.
19. **Botão "comparar antes/depois do K-Pg"** — Cretáceo (dinossauros não-avianos dominantes) × Paleoceno (radiação de mamíferos).
20. **Botão "ver consequências futuras"** — segue a radiação de mamíferos → eventual surgimento de primatas → (muito depois) `entity:genero-homo` — com cautela de que são consequências **distantes**.

---

## 12. Relatório de qualidade da cena (Tarefa 12)

Roster curado da cena `scene:earth-66ma-kpg-extinction`.

1. **Itens na cena:** **~32** (+ objeto de cena, + 10 claims de evidência E1–E10), dos quais **~30 novos/reframe** nesta etapa.
2. **Event:** **1** — `evt:impacto-chicxulub` (o **único** evento pontual; contraste com 2,4 Ga, que tinha zero, e com 1789, que tinha vários).
3. **Process:** **3** — `proc:extincao-kpg` (reframe de SCI-21), `proc:recuperacao-ecologica-pos-kpg`, `proc:vulcanismo-deccan-traps`.
4. **State:** **7** — atmosfera, clima, **oceano (OceanographicState)**, bioma terrestre, bioma marinho, paleogeografia, tectônica Deccan.
5. **Concept:** **6** — `limite-kpg`, `anomalia-iridio`, `extincao-em-massa`, `inverno-impacto` (+ `proxy-geoquimico`, `tectonica-placas` referenciados).
6. **Entity:** **5** — `dinossauros-nao-avianos`, `aves`, `mamiferos`, `plancton-marinho` (+ `terra` contexto).
7. **Place:** **1** completo — `cratera-chicxulub`; **+3 referenciados** (localidades de evidência: Gubbio, Hell Creek, seções da camada-limite) a criar como nós.
8. **Region:** **0** política — consistente com tempo profundo; a "geografia" é `PaleogeographicState`.
9. **ClaimSet:** **6** — `k-pg-causa` (com pesos), `kpg-ritmo-extincao`, `kpg-mecanismos-mortalidade`, `kpg-incendios`, `kpg-acidificacao-oceanica`, `kpg-seletividade`.
10. **UncertaintyProfile:** **3** — `kpg-inverno-intensidade-duracao`, `kpg-recuperacao-tempo`, `paleogeografia-66ma`.
11. **Publicáveis (núcleo factual, pós-revisão científica do piloto):** **~14** — impacto, extinção (fato), irídio, cratera, limite K-Pg, extinção-em-massa, sobrevivência de aves e mamíferos, plâncton (fato do turnover).
12. **Pending (incerteza científica):** **~18** — peso causal do Deccan, paleogeografia fina, inverno, acidificação, recuperação, os States de transição, os 6 ClaimSets e os 3 UncertaintyProfiles.
13. **Risco científico alto:** **~7** — `claimset:k-pg-causa` (pesos), `kpg-mecanismos`, `kpg-incendios`, `uncertaintyprofile:kpg-inverno`, `proc:vulcanismo-deccan-traps`/`state:tectonica-deccan-66ma`, `state:atmosfera/clima/oceano-pos-impacto`.
14. **Risco editorial alto:** **0** — sem sensibilidade humana (só a nota antinegacionismo de idade/evolução, fora de ClaimSet). Contraste forte com 1789.
15. **Risco de licença:** **baixo** — todos em risco **0–1** (PBDB/USGS/NOAA Paleo/GPlates); **nenhum** médio/alto; **Deep Time Maps proibido**.
16. **Não exibíveis ainda:** os ~18 itens `pending` — mediados (rótulo "reconstrução/incerto/debate") ou ocultos; só o núcleo factual aparece.
17. **Gabarito para cenas futuras:** o objeto `scene:earth-66ma-kpg-extinction` (padrão **híbrido evento+sistema**); a distinção **Event (impacto) × Process (extinção) × State (condições)**; o **ClaimSet com pesos assimétricos** (impacto × Deccan, sem falsa equivalência); o **marcador pontual em paleoposição rotulada**; a separação **evidência atual ≠ paleoposição**.
18. **Fontes a confirmar:** PBDB (registro fóssil/seletividade), USGS (cratera/Deccan), NOAA Paleo (clima/oceano), GPlates (paleogeografia 66 Ma), geociências (irídio/isótopos) — todas `PENDENTE_CONFIRMACAO_FONTE` por asset; criar os Places de evidência (Gubbio/Hell Creek).
19. **O `OceanographicState` funcionou como State oficial?** **Sim.** `state:oceanos-pos-impacto-kpg` acomodou um oceano **oxigenado, em crise de produtividade e possivelmente acidificado** — radicalmente diferente do oceano **anóxico/ferruginoso** de 2,4 Ga que motivou o tipo — **sem** forçar `Climate`/`Biome`/`Paleogeographic`. O campo `dissolvedIron = N/A` aqui (vs central no GOE) prova que o tipo é **genérico**, não casado a um único cenário. **A decisão da 4F está confirmada na prática.**
20. **Ajustes que o padrão genérico de `Scene` precisa após esta cena:**
    - **(a) Estrutura de gatilho→cascata.** A cena híbrida expôs a necessidade de marcar explicitamente um **`triggerItem`** (Event) que desencadeia uma **cascata** de Processes/States. Proposta: adicionar ao padrão de `Scene` um campo opcional **`cascadeStructure`** (gatilho → encadeamento), distinto de simultaneidade pura.
    - **(b) ClaimSet com peso.** Confirmar no padrão que **`ClaimSet` pode carregar peso por claim** (assimetria legítima, como impacto × Deccan) — não apenas listas de "lados iguais". Reforço de vocabulário, não novo tipo.
    - **(c) Paleoposição em `Place`.** Em tempo profundo, `Place` precisa distinguir **localidade atual** de **paleoposição** (campo `paleoPosition`, frequentemente `PENDENTE_REFINAMENTO_ESPACIAL`). Pequeno ajuste no nó `Place`, não remodelagem.
    - Estes são **refinamentos**, escalados à modelagem; nenhum exige remodelar o padrão da 4F.

---

## 13. Próximos passos para a Etapa 4H (Tarefa 13)

A Etapa 4G entregou a **terceira cena-gabarito** — a **híbrida** (evento pontual + sistema terrestre) — e fez a **primeira instanciação oficial do `OceanographicState`**, confirmando a decisão da 4F. A **Etapa 4H**, quando solicitada, pode:

1. **Aplicar os três refinamentos do padrão** (cascadeStructure; ClaimSet com peso; paleoPosition em Place) propostos na §12.20, atualizando o padrão genérico da 4F sem remodelá-lo.
2. **Aplicar o padrão a um quarto tipo de cena ainda não exercitado** — **cósmica** (Big Bang) ou **contemporânea** (clima moderno) — para cobrir os extremos restantes da taxonomia (4F §3).
3. **Concluir a revisão científica** dos ~18 itens `pending` desta cena e criar os **Places de evidência** (Gubbio, Hell Creek, seções da camada-limite) como nós.
4. **Resolver o datum do eixo temporal** (1950 BP × J2000) — pendência herdada desde a 4B, necessária para integrar cenas históricas (1789) e profundas (2,4 Ga, 66 Ma) no mesmo eixo; decisão da **Etapa 3**, aqui reforçada.
5. **Reificar `Source`/`MediaAsset`** das evidências (proxies/cratera/registro fóssil com `natureLabel` e licença-por-asset; afloramentos como `fotografia` que **ilustra**, não prova).

**O que a 4H explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (1/1.1) ou política editorial (3.1). Reaberturas da Etapa 2 ficam restritas aos refinamentos mínimos já escalados.

---

*Documento de entrega da Etapa 4G, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B, 4C, 4D, 4E, 4F). Entrega a cena canônica híbrida de 66 Ma / extinção K-Pg: objeto `scene:earth-66ma-kpg-extinction`, itens centrais (com a distinção Event-impacto × Process-extinção × State-condições), 7 States, a **primeira instanciação oficial de `OceanographicState`** (`state:oceanos-pos-impacto-kpg`, que confirmou o tipo na prática), 10 claims de evidência, 6 ClaimSets (com pesos assimétricos, sem falsa equivalência impacto × Deccan) e 3 UncertaintyProfiles, tratamento do anacronismo espacial profundo (aves ≠ "todos os dinossauros"; paleoposição ≠ localidade atual), relationship graph, globo paleogeográfico com marcador pontual, timeline com evento sobre processos, dossiê de 20 blocos e relatório de qualidade. Não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não inventa paleomapa e não inventa precisão. Próxima etapa, quando solicitada: Etapa 4H — refinamentos do padrão de Scene, quarta cena (cósmica ou contemporânea) e conclusão de revisões.*
