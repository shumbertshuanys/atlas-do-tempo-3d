# Etapa 4F — Padrão Genérico de Cena e Revisão Controlada dos State Types

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4F · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A), a normalização/entidades de referência (Etapa 4C) e as duas cenas-gabarito (Etapas 4D e 4E) · 12/06/2026
**Escopo desta etapa (e seus limites):** **consolidar método, tipos e critérios** — transformar as duas cenas-gabarito em um **padrão genérico de cena** e resolver, de forma **controlada**, a pendência estrutural sobre novos `State Types` (`OceanographicState`, `GeochemicalState`, `EarthSystemState`). Conforme solicitado, **não** cria cena nova, **não** povoa lotes, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** reabre auditoria de fontes (1/1.1), **não** reabre a política editorial (3.1), **não** usa Wikidata/Wikipedia como autoridade e **não** copia texto de fontes.

**Natureza desta etapa.** É uma **mini-reabertura controlada da Etapa 2**, restrita aos tipos de State escalados nas Etapas 4A/4B/4E. Nada além disso é remodelado.

---

## Sumário

1. Comparação 1789 × 2,4 Ga (Tarefa 1)
2. Padrão genérico de `Scene` (Tarefa 2)
3. Taxonomia de cenas (Tarefa 3)
4. Matriz tipo de tempo × representação (Tarefa 4)
5. Decisão sobre `OceanographicState` (Tarefa 5)
6. Decisão sobre `GeochemicalState` (Tarefa 6)
7. Decisão sobre `EarthSystemState` (Tarefa 7)
8. Lista oficial revisada de `State Types` (Tarefa 8)
9. Critérios de publicabilidade de cenas (Tarefa 9)
10. Padrão de dossiê de cena (Tarefa 10)
11. Padrão de globo/timeline por cena (Tarefa 11)
12. Próximos passos para a Etapa 4G (Tarefa 12)

---

## 1. Comparação 1789 × 2,4 Ga (Tarefa 1)

Comparação formal das duas cenas-gabarito. As diferenças **não** são defeitos — são o que o padrão genérico precisa **acomodar**.

| Dimensão | `scene:world-1789-french-revolution` (A) | `scene:earth-2-4ga-great-oxidation-event` (B) |
|---|---|---|
| Natureza do tempo | histórico (documental) | geológico profundo |
| Precisão temporal | dia/mês/ano | Ga (faixa); "aproximação de tempo profundo" |
| Tipo de evidência | documental (arquivos, fontes primárias) | proxy geoquímico (BIFs, S-MIF, minerais redox) |
| Tipos de item dominantes | Event + Process + Entity + Place/Region | State + Process (sem Event) |
| Presença de **Event** | **alta** (Bastilha, Estados Gerais, Declaração, posse) | **zero** (nenhum evento pontual datado) |
| Presença de **Place/Region** | **alta** (6 Places, 8 Regions políticas) | Places = localidades de **evidência atual**; **Region política = zero** |
| Papel dos **States** | secundário (condições políticas/econômicas em 1789) | **central** (atmosfera, oceano, clima, biosfera, geoquímica) |
| Papel dos **ClaimSets** | controvérsias historiográficas e terminologia sensível | debates científicos (timing, ritmo, causas, glaciações) |
| Papel dos **UncertaintyProfiles** | baixo (poucos) | **alto** (magnitude de O₂, paleogeografia) |
| Fontes | historiografia, Arquivo Nacional, IBGE, OWID | NOAA Paleo, PBDB, USGS, GPlates |
| Risco editorial | **alto** (escravidão, colonialismo, indígenas — Leis 10.639/11.645) | **baixo** (só nota antinegacionismo de idade/evolução) |
| Risco científico | baixo | **alto** (magnitude, ritmo, datas, paleogeografia) |
| Risco de licença | baixo–médio (0–2) | baixo (0–1; Deep Time Maps proibido) |
| Timeline | rica em eventos de dia; processos longos atravessando o ano | dominada por processos longos e States; bordas difusas |
| Globo/mapa | foco regional (França) + marcadores simultâneos; fronteiras históricas | globo **esquemático**; halo atmosférico; oceanos ferruginosos; sem fronteiras |
| Dossiê | 15 blocos; ênfase em simultaneidade humana | 18 blocos; ênfase em **"como sabemos disso"** |
| Anacronismo mais perigoso | projetar fronteiras/nações atuais (Brasil, D.C.); apagar indígenas | projetar continentes/países modernos; tratar paleomapa como fato; rocha de hoje ≠ lugar antigo |
| Itens ocultos/pending | sensíveis (escravidão, colonialismo, indígenas) — gating **editorial** | incertos (paleogeografia, Kenorland, magnitude) — gating **científico** |
| Relação com simultaneidade | "o mundo ao mesmo tempo" (regiões humanas) | "o planeta ao mesmo tempo" (sistemas terrestres) |

**Leitura.** A mesma função ("o que acontecia neste momento?") opera em dois regimes opostos: um **rico em eventos e regiões, com gating editorial**; outro **rico em States e incerteza, com gating científico**. O padrão genérico de `Scene` deve cobrir **ambos os extremos** e tudo entre eles.

---

## 2. Padrão genérico de `Scene` (Tarefa 2)

Uma `Scene` **não duplica conteúdo** — é uma **consulta materializada / interpretação controlada** sobre o Knowledge Core (realiza `concept:simultaneidade-historica`/planetária). Cada campo é definido conceitualmente, com exemplos de A (1789) e B (2,4 Ga).

| Campo | Definição conceitual | Exemplo A (1789) | Exemplo B (2,4 Ga) |
|---|---|---|---|
| `id` | identificador `scene:` estável | `scene:world-1789-french-revolution` | `scene:earth-2-4ga-great-oxidation-event` |
| `title` | rótulo exibível | "O mundo em 1789…" | "A Terra há ~2,4 Ga…" |
| `focusItem` | item-âncora do recorte | `proc:revolucao-francesa` | `proc:goe` |
| `queryType` | tipo de consulta (ver taxonomia §3) | simultaneidade global histórica | tempo profundo / evidência |
| `timeRange` | janela no eixo canônico | 1789 (núcleo); 1787–1792 | ~2,4 Ga; janela ~2,5–2,0 Ga |
| `timePrecision` | granularidade + nota de aproximação | dia/ano | Ga (faixa); "aproximação" |
| `spatialScope` | recorte espacial | regional→global | planetário/global |
| `activatedLayers` | camadas (Etapa 4A) ligadas | 13,14,15,17,20,21,22 | 4,5,6,7,8,9,25 |
| `centralItems` | itens do foco | Bastilha, Estados Gerais, Declaração… | GOE, fotossíntese, BIFs… |
| `contextualItems` | simultâneos/contexto | EUA, Otomano, Qing, África… | clima, paleogeografia, geoquímica |
| `sensitiveItems` | itens com gating editorial | escravidão, colonialismo, indígenas | **nenhum** (exceto nota antinegacionismo) |
| `hiddenItems` | itens não exibíveis enquanto pending | sensíveis em revisão | paleogeografia, Kenorland, magnitude |
| `claimSets` | debates discretos legítimos | causas da Revolução, 1492, escravidão | timing, ritmo, causas, glaciações |
| `uncertaintyProfiles` | faixas/margens sem "lados" | poucos | magnitude de O₂, paleogeografia |
| `states` | condições de fundo (Etapa 2 + §8) | França-1789, economia atlântica | atmosfera, oceano, clima, biosfera |
| `sources` | proveniência A/B por claim | historiografia, IBGE, OWID | NOAA Paleo, PBDB, GPlates |
| `evidenceProfile` | natureza dominante da evidência | documental | proxy geoquímico |
| `editorialRisk` | risco editorial agregado | alto | baixo |
| `scientificRisk` | risco científico agregado | baixo | alto |
| `licenseRisk` | risco de licença agregado (0–5) | 0–2 | 0–1 |
| `reviewStatus` | portão de exibição da cena | pending (núcleo factual exibível) | núcleo approved; incerto pending |
| `timelineBehavior` | como aparece no eixo | eventos de dia + processos | processos + States, bordas difusas |
| `globeBehavior` | como aparece no globo | foco regional + marcadores | esquemático + halo + oceanos |
| `dossierBehavior` | estrutura do dossiê (§10) | 15 blocos humanos | 18 blocos com "como sabemos" |
| `simultaneityBehavior` | como entra em "o que acontecia…" | mundo humano ao mesmo tempo | planeta ao mesmo tempo |
| `anachronismPolicy` | regra antianacronismo (§6 de 4D/4E) | ModernCorrespondence; excluir Mali | sem países; excluir Rodinia/Pangeia |
| `publicabilityStatus` | nível de publicabilidade (§9) | parcialmente publicável | parcialmente publicável |

**Invariantes do padrão** (valem para toda `Scene`): (1) **não duplica** itens — referencia `knowledgeItemId`; (2) respeita o **invariante de exibição** (pending/legal-review/rejected não aparece como fato); (3) carrega **três riscos** (editorial, científico, licença); (4) declara **anachronismPolicy** explícita; (5) separa **fato × evidência × hipótese × incerteza**; (6) exibe **ClaimSet** (lados) distinto de **UncertaintyProfile** (faixa).

---

## 3. Taxonomia de cenas (Tarefa 3)

Doze tipos de cena. Cada um herda o padrão genérico (§2), variando os pesos. "Place/Region" e "State" indicam **presença típica** (alta/média/baixa/nula).

| # | Tipo de cena | Entidades dominantes | Precisão temporal típica | Place/Region | State | Risco editorial | Risco científico | Tipo de fonte | Globo | Timeline | Exemplo possível |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Histórica pontual** | Event, Entity | dia/ano | alta | baixa | médio-alto | baixo | documental/arquivo | marcador no local | ponto datado | Queda da Bastilha |
| 2 | **Histórica de processo** | Process, State | ano/década | alta | média | médio-alto | baixo | historiografia | região + fluxos | bloco longo | Revolução Industrial |
| 3 | **Biográfica** | Entity (pessoa), Event | ano | média | baixa | médio (LGPD se vivo) | baixo | arquivo/biografia | trajetória/locais | barra de existência | Lavoisier |
| 4 | **Civilizacional** | State (CivilizationState), Entity | século | média | alta (CivilizationState) | alto (Leis 10.639/11.645) | baixo-médio | historiografia/arqueologia | território difuso | faixa secular | Império do Mali |
| 5 | **Regional** | Region, State, Process | década/século | **alta** | média | variável | baixo | historiografia/IBGE | foco regional | recorte local | Capitania de Minas Gerais |
| 6 | **Planetária contemporânea** | State, Process, dados | ano | global | alta | médio-alto (clima) | médio | OWID/NASA/INPE | overlays globais | séries recentes | Mudanças climáticas modernas |
| 7 | **Tempo profundo** | State, Process | Ga/Ma (faixa) | nula (política); Place=evidência | **alta** | baixo | **alto** | NOAA Paleo/PBDB/GPlates | esquemático rotulado | processos/States | GOE (2,4 Ga) |
| 8 | **Cósmica** | Event/Process, Entity cósmica | Ga (faixa) | nula | média | baixo (antinegacionismo) | médio-alto | NASA/astrofísica | cosmos (sem globo) | zero absoluto+faixas | Big Bang |
| 9 | **Científica conceitual** | Concept, Process | transtemporal | nula/difusa | baixa | médio | médio | literatura revisada | esquema/diagrama | atemporal/faixa | Tectônica de placas |
| 10 | **Comparativa antes/depois** | State (×2), Process | conforme par | conforme par | **alta** (par de States) | conforme tema | conforme tema | conforme tema | split/transição | dois cortes | Atmosfera antes/depois do GOE |
| 11 | **Simultaneidade global** | mix (Event+State+Region) | conforme âncora | alta | alta | alto | variável | múltiplas A/B | mundo + marcadores | corte temporal único | O mundo em 1789 |
| 12 | **Evidência/proxy** | Claim de evidência, Place (localidade) | conforme alvo | Place=localidade atual | média | baixo | **alto** | dados primários/proxies | marcadores "onde encontramos hoje" | linha de inferência | BIFs como prova do GOE |

**Observações.** As cenas-gabarito atuais combinam tipos: **1789** é principalmente **11 (simultaneidade global)** com elementos de 1, 2 e 5; **2,4 Ga** é **7 (tempo profundo)** com forte componente **12 (evidência/proxy)** e **10 (comparativa)**. Uma cena real costuma ser um **blend** de tipos — a taxonomia define os **pesos**, não caixas exclusivas.

---

## 4. Matriz tipo de tempo × representação (Tarefa 4)

Sete regimes de tempo. Cada um impõe escala, evidência, incerteza e anacronismo próprios — e tende a ser alimentado por fontes P0/P1 específicas (Etapa 1/1.1).

| Tipo de tempo | Escala | Precisão possível | Tipo de evidência | Tipo de incerteza | Item dominante | Timeline | Globo | Anacronismo a evitar | Fonte P0/P1 típica |
|---|---|---|---|---|---|---|---|---|---|
| **Cósmico** | ~13,8 Ga → presente | Ga (faixa) | observação indireta (CMB, redshift) | modelagem dos primeiros instantes | Event/Process cósmico | zero absoluto + faixas | cosmos (sem globo terrestre) | aplicar geografia/tempo terrestre ao cosmos | NASA, astrofísica revisada |
| **Geológico profundo** | ~4,5 Ga → ~541 Ma | Ga/Ma (faixa) | proxy geoquímico, paleomagnetismo | magnitude, ritmo, paleogeografia | State (planetário) | processos/States, bordas difusas | esquemático/reconstrução rotulada | continentes/países modernos; paleomapa como fato | NOAA Paleo, GPlates, Macrostrat, USGS |
| **Biológico/evolutivo** | ~541 Ma → ~300 ka | Ma/ka (faixa) | registro fóssil, filogenia | datas de origem, topologia | Process, BiomeState | faixas evolutivas | reconstrução de biomas | "progresso"/escada evolutiva; hierarquia | PBDB, Open Tree of Life |
| **Arqueológico** | ~300 ka → ~3000 a.C. | ka/século (faixa) | registro material, datação | datação, atribuição cultural | Process, State, Entity (grupo) | faixas com incerteza | sítios + territorialidades | apagar povos; fronteiras modernas | arqueologia revisada, fontes orais |
| **Histórico** | ~3000 a.C. → ~1950 | século→dia | documental, fontes primárias | interpretação, lacunas documentais | Event, Process, Entity, Region | eventos + processos | fronteiras históricas + ModernCorrespondence | projetar nações/fronteiras atuais | historiografia, arquivos, IBGE, WHG/Pleiades |
| **Contemporâneo** | ~1950 → presente | ano/dia | documental + dados quantitativos | projeção, dados em disputa | State, Process, dados | séries temporais recentes | overlays de dados globais | presentismo; dados sem fonte | OWID, World Bank, NASA, INPE, IBGE |
| **Projetivo/futuro** | presente → futuro | cenário (faixa) | modelo/projeção | cenários, sensibilidade | UncertaintyProfile, ClaimSet | faixas de cenário | projeções rotuladas | tratar projeção como fato | IPCC/modelos (figuras recriadas) |

**Princípio integrador.** O **eixo é único** (Ga↔dia, Etapa 2), mas **precisão, evidência e incerteza variam por regime**. A pendência do **datum** (1950 BP × J2000) é justamente o ponto onde os regimes geológico/arqueológico e histórico/contemporâneo precisam se encontrar — decisão da **Etapa 3**, aqui reforçada (ver §12).

---

## 5. Decisão sobre `OceanographicState` (Tarefa 5)

**Decisão: APROVADO — criar `OceanographicState` como `State Type` oficial.**

**Por que `PaleogeographicState`, `ClimateState` e `BiomeState` não bastam.** `PaleogeographicState` descreve **posição/configuração** continental-oceânica, não a **química/física interna** do oceano (redox, ferro dissolvido, salinidade). `ClimateState` cobre **clima atmosférico/temperatura**, não a **circulação e o estado redox** oceânicos. `BiomeState` cobre **vida**, não o **meio físico-químico** do mar. Na cena 2,4 Ga, "oceanos anóxicos e ferruginosos" é uma condição **própria**, central, que hoje seria **espremida** nesses três tipos com perda de fidelidade.

**Cenas/camadas que dependem dele:** toda cena de **tempo profundo** e **geológico** (GOE, Cambriano, formação dos oceanos), a camada **7 Oceanos** (Etapa 4A, que não tinha State dedicado), e cenas **paleoclimáticas/contemporâneas** (circulação, nível do mar, acidificação).

**Campos mínimos (especificação conceitual ajustada):**

```txt
OceanographicState = {
  id,                  # state:<...>
  timeRange,           # eixo canônico (Ga↔dia)
  spatialScope,        # global ou bacia; SpatialUncertainty quando difuso
  oceanConfiguration,  # extensão/disposição (liga a PaleogeographicState; reconstrução)
  seaLevel,            # nível relativo (faixa/incerteza; PENDENTE quando sem proxy)
  redoxState,          # anóxico/subóxico/óxico/ferruginoso/euxínico (qualitativo)
  dissolvedIron,       # presença/abundância de Fe dissolvido (qualitativo/faixa)
  oxygenation,         # O2 dissolvido (faixa; liga a AtmosphereState)
  circulationPattern,  # padrão de circulação (reconstrução; alta incerteza em deep time)
  temperatureProfile,  # faixa térmica (proxy; incerteza)
  iceCover,            # cobertura de gelo (liga a ClimateState)
  salinityProfile,     # salinidade (faixa; frequentemente PENDENTE em deep time)
  biologicalContext,   # referência a BiomeState (não duplica vida)
  evidenceClaims[],    # claims de evidência (BIFs, especiação de Fe, isótopos)
  uncertaintyProfile,  # faixa/margem dominante
  sources[],           # A/B (NOAA Paleo, USGS, NOAA OISST p/ contemporâneo)
  representationType,  # medição | reconstrução modelada | aproximação didática
  reviewStatus         # portão de exibição
}
```

*(Ajuste em relação à proposta da 4E: `salinityProfile` rebaixado para opcional/PENDENTE em tempo profundo; `biologicalContext` é **referência** a `BiomeState`, não cópia.)*

- **Fontes:** NOAA/NCEI Paleo (deep time, PD); USGS; NOAA OISST/World Ocean Atlas (contemporâneo); GPlates (configuração).
- **Claims que recebe:** redox, ferro, oxigenação, circulação, temperatura, nível do mar — quase sempre `inferência científica`/`reconstrução modelada` em deep time; `medição` no contemporâneo.
- **Globo:** oceanos com tom/overlay **didático rotulado** (ferruginoso, anóxico); contemporâneo com dados reais.
- **Timeline:** State de fundo (faixa).
- **Relação com outros States:** liga-se a `AtmosphereState` (oxigenação), `ClimateState` (gelo/temperatura), `BiomeState` (vida), `PaleogeographicState` (configuração); **não** duplica nenhum.
- **Riscos:** incerteza alta em deep time (`scientificRisk`); licença baixa (fontes verdes).

`state:oceanos-ferruginosos` (4E) passa de **proposta** a **instância** de `OceanographicState`.

---

## 6. Decisão sobre `GeochemicalState` (Tarefa 6)

**Decisão: NÃO criar agora — manter geoquímica como (a) `evidenceClaims` e (b) campos redox/oxigenação nos States existentes.** Reavaliar no futuro se surgir necessidade recorrente.

**Quando uma condição geoquímica é pano de fundo × quando é evidência.** Na prática, a geoquímica aparece em dois papéis: como **evidência** ("a assinatura X indica Y" → é um `evidenceClaim`, padrão E1–E7 da 4E) ou como **condição de fundo** (redox do oceano/atmosfera → já é campo de `OceanographicState.redoxState` e `AtmosphereState.oxygenation`). **Em ambos os casos, um tipo `GeochemicalState` dedicado seria redundante.**

**Diferença entre `GeochemicalState` e `EvidenceClaim`.** Um `EvidenceClaim` é uma **afirmação de evidência com proveniência** (proxy → conclusão → confiança). Um `GeochemicalState` seria uma **condição agregada** — mas essa agregação já é alcançada pelos campos redox dos States físicos + o cluster de evidências. Criar o tipo aumentaria a **superfície de modelo** sem ganho claro.

**Riscos de criar tipo demais.** Proliferação de States dificulta curadoria, gera sobreposição (quem detém o redox: o GeochemicalState ou o OceanographicState?) e confunde o invariante "um fato, um lar". **Risco de não criar:** baixo — nenhuma cena atual fica inviável; `state:geoquimica-2-4ga` (4E) é reexpresso como **cluster de `evidenceClaims`** (E1–E7) ancorado no `proc:goe` e nos campos redox dos States.

**Critério de reabertura futura:** só criar `GeochemicalState` se surgirem **≥3 cenas** em que a geoquímica seja condição de fundo **não** redutível a redox de oceano/atmosfera nem a evidência (ex.: ciclos biogeoquímicos complexos como cena própria). Até lá, **não criar**.

> Especificação proposta na 4E fica **registrada como rascunho não aprovado**, disponível caso o critério de reabertura seja atingido.

---

## 7. Decisão sobre `EarthSystemState` (Tarefa 7)

**Decisão: NÃO criar como `State Type` — tratar como AGREGAÇÃO VIRTUAL da `Scene`** (confirma a recomendação da 4E, agora com justificativa formal).

- **Vantagens de criar:** um "estado do sistema Terra" num instante seria conceitualmente elegante para cenas planetárias.
- **Riscos de redundância:** a `Scene` **já é** a visão integrada de atmosfera + oceano + clima + tectônica + biosfera num recorte. Um `EarthSystemState` **duplicaria** a Scene e competiria com ela pela função de "integrador", violando "não duplicar".
- **Impacto no modelo:** criar adicionaria um tipo que **agrega outros States** — uma relação de composição que o modelo não tem hoje e que melhor pertence à camada de **consulta** (Scene), não à de **dados** (State).
- **Impacto em cenas futuras:** nenhuma perda — toda cena planetária usa a própria `Scene` como integradora, referenciando os States componentes.
- **Relação com Scene:** `EarthSystemState` ≡ **projeção/agregação derivada** da `Scene` (um *view*, não um registro armazenado). Fica como **conceito virtual**, não como tipo.

**Resumo das três decisões:** `OceanographicState` **criado**; `GeochemicalState` **não criado** (evidência + campos redox); `EarthSystemState` **não criado** (agregação virtual via Scene).

---

## 8. Lista oficial revisada de `State Types` (Tarefa 8)

Após as decisões da §5–§7, o Knowledge Core passa de **10** para **11** `State Types` oficiais (+ `OceanographicState`; `GeochemicalState`/`EarthSystemState` **não** entram).

| State Type | Finalidade | Quando usar | Quando **não** usar | Campos mínimos | Fontes típicas | Risco típico | Exemplo de cena | Relação com outros |
|---|---|---|---|---|---|---|---|---|
| **AtmosphereState** | composição/estado da atmosfera | mudança atmosférica (O₂, CO₂, gases) | química oceânica (→ Oceanographic) | timeRange, composição (faixa), oxygenation, uncert | NOAA Paleo, NASA | científico (deep time) | GOE; atmosfera anóxica | ↔ Oceanographic (O₂), Climate |
| **TectonicState** | regime tectônico (placas, atividade) | tectônica/vulcanismo de um período | posição de massas (→ Paleogeographic) | timeRange, regime, atividade, uncert | USGS, GPlates | científico | Pangeia (tectônica) | ↔ Paleogeographic |
| **PaleogeographicState** | posição/configuração de massas | reconstrução de continentes/oceanos | química oceânica (→ Oceanographic) | timeRange, configuração (reconstrução), SpatialUncertainty | GPlates/EarthByte | científico (alto em deep time) | Pangeia; crátons 2,4 Ga | ↔ Tectonic, Oceanographic |
| **ClimateState** | clima/temperatura/glaciações | regime climático de um período | química oceânica (→ Oceanographic) | timeRange, regime térmico, gelo, uncert | NOAA Paleo, INPE, IPCC | científico/editorial (clima) | glaciações huronianas; clima moderno | ↔ Atmosphere, Oceanographic |
| **OceanographicState** *(novo)* | estado físico-químico do oceano | redox/ferro/circulação/nível do mar | clima atmosférico (→ Climate) | ver §5 | NOAA Paleo, USGS, OISST | científico (deep time) | oceanos ferruginosos 2,4 Ga | ↔ Atmosphere, Climate, Biome, Paleogeographic |
| **BiomeState** | estado da biosfera/biomas | vida dominante de um período | meio físico (→ Climate/Oceanographic) | timeRange, biota dominante, uncert | PBDB, MapBiomas (isolar) | científico | biosfera microbiana 2,4 Ga | ↔ Oceanographic, Climate |
| **CivilizationState** | condição de uma sociedade/Estado | civilizações/impérios num recorte | pessoa (→ Entity) | timeRange, organização, território difuso | historiografia, arqueologia | **editorial** (Leis 10.639/11.645) | Mali; China Qing 1789 | ↔ Population, Economic, Cultural |
| **TechnologyState** | nível/estado tecnológico | técnica dominante de um período | invenção pontual (→ Event) | timeRange, técnicas, difusão | historiografia, OWID | editorial (médio) | industrialização incipiente 1789 | ↔ Economic, Cultural |
| **PopulationState** | demografia de um grupo/região | população/demografia num recorte | indivíduo (→ Entity) | timeRange, demografia (faixa) | IBGE, OWID, World Bank | editorial (sensível) | permanência indígena contemporânea | ↔ Civilization, Economic |
| **CulturalState** | condição cultural/intelectual | cultura/ideias de um período | conceito atemporal (→ Concept) | timeRange, correntes, difusão | historiografia | editorial (médio) | cultura afro-brasileira | ↔ Civilization, Technology |
| **EconomicState** | condição econômica | economia de um recorte | transação pontual (→ Event) | timeRange, regime econômico, fluxos | OWID, World Bank, IBGE | editorial (escravidão etc.) | economia atlântica 1789 | ↔ Population, Technology |

**Não oficializados:** `GeochemicalState` (geoquímica = `evidenceClaims` + campos redox dos States acima); `EarthSystemState` (agregação virtual da `Scene`).

---

## 9. Critérios de publicabilidade de cenas (Tarefa 9)

Cinco níveis de publicabilidade de uma `Scene`, com os gatilhos que rebaixam o nível. Uma cena assume o **nível do seu pior gargalo** (princípio do elo mais fraco).

| Nível | Definição | Gatilhos que levam a este nível |
|---|---|---|
| **1. Publicável** | exibível integralmente | todos os itens `approved`; sem ClaimSet pending crítico; fontes confirmadas; geometrias ok; sem mídia pendente; sem IA não rotulada |
| **2. Parcialmente publicável** | núcleo factual exibível; partes mediadas/ocultas | alguns itens/ClaimSets `pending`; algumas fontes/geometrias pendentes |
| **3. Mediada** | exibível só com rótulos/avisos em toda a cena | tema sensível transversal; incerteza científica alta dominante |
| **4. Apenas interna** | serve de gabarito/referência, não vai ao público | revisões essenciais não concluídas; muitos itens pending |
| **5. Bloqueada** | não exibível de forma alguma | risco jurídico (LGPD/legal-review) não resolvido; licença de asset proibida; conteúdo rejeitado |

**Critérios considerados (checklist por cena):** itens pending · ClaimSets pending · temas sensíveis · fontes pendentes · geometrias pendentes · incerteza científica alta · risco editorial alto · risco jurídico · mídia pendente · presença de IA (rotular) · licença de assets.

**Aplicação às duas cenas:**

- **`scene:world-1789-french-revolution` → Nível 2 (parcialmente publicável).** Núcleo factual datado (Bastilha, Estados Gerais, Declaração, posse de Washington, *Traité*) é exibível; itens sensíveis (escravidão, colonialismo, indígenas, Inconfidência) ficam **mediados/ocultos** até revisão humana; nenhum bloqueio jurídico ativo (BR-07 ditadura **não** integra esta cena). Gargalo: revisão editorial dos sensíveis.
- **`scene:earth-2-4ga-great-oxidation-event` → Nível 2 (parcialmente publicável), tendendo a Mediada (3) na camada paleogeográfica.** Núcleo factual (subida de O₂, fotossíntese, BIFs, biosfera microbiana) exibível após revisão científica; paleogeografia/Kenorland/magnitude ficam **mediados** (rótulo "reconstrução/incerto"). Gargalo: incerteza científica alta (não editorial).

> Nota: o nível da cena **não** é a média dos itens — é o **pior gargalo**. Uma única dependência sensível ou bloqueada rebaixa a cena inteira, ainda que o resto esteja `approved`.

---

## 10. Padrão de dossiê de cena (Tarefa 10)

Padrão genérico extraído dos dossiês de 1789 (15 blocos) e 2,4 Ga (18 blocos). **Blocos obrigatórios** (toda cena) e **opcionais** (conforme tipo).

**Blocos obrigatórios (núcleo do dossiê):**
1. **Visão geral** — síntese + etiqueta de precisão temporal + aviso de itens em revisão.
2. **Foco principal** — o `focusItem`, com fato separado de debate.
3. **Contexto temporal** — quando, com precisão e incerteza.
4. **Mundo/sistema nesse momento** — a simultaneidade (humana ou planetária).
5. **ClaimSets e debates** — hub dos debates legítimos, com posições sem equivalência marcadas.
6. **Evidências / como sabemos** — a cadeia de inferência (documental ou proxy).
7. **Incertezas** — ClaimSets × UncertaintyProfiles, sem virar "não sabemos nada".
8. **Fontes e confiança** — proveniência por claim; fato × evidência × hipótese × reconstrução.
9. **Itens ocultos por pendência/revisão** — lista transparente do que não aparece e por quê.
10. **Como evitar anacronismos** — a `anachronismPolicy` da cena.

**Blocos opcionais (conforme tipo):**
- **Contexto espacial** (cenas com Place/Region; menos relevante em cósmica).
- **Itens simultâneos detalhados** (simultaneidade global).
- **States de fundo** (planetária/tempo profundo).
- **Consequências** (biológicas/climáticas/políticas).
- **Navegar para outro lugar/período** · **Comparar antes/depois** · **Ver consequências** (botões de navegação).

**Diferenciação por tipo de cena:**

| Tipo de dossiê | Ênfase | Blocos que ganham peso | Blocos que somem/encolhem |
|---|---|---|---|
| **Histórica** | simultaneidade humana, agência, sensibilidade | contexto espacial, itens simultâneos, anacronismo (ModernCorrespondence) | States de fundo (menores) |
| **Tempo profundo** | "como sabemos", incerteza, evidência | evidências/proxy, incertezas, States de fundo | contexto espacial político (ausente) |
| **Cósmica** | escala, modelo × observação, antinegacionismo | foco, evidências indiretas, incerteza | contexto espacial (sem globo), itens simultâneos políticos |
| **Contemporânea** | dados, séries, projeção | fontes/confiança, incertezas (projeção), consequências | anacronismo (menor) |

---

## 11. Padrão de globo/timeline por cena (Tarefa 11)

### 11.1 Globo/mapa — padrão genérico

| Aspecto | Regra genérica | Cena histórica (1789) | Cena de tempo profundo (2,4 Ga) |
|---|---|---|---|
| Foco inicial | no `focusItem`/`spatialScope` | região do foco (França) | planeta inteiro |
| Layers | só as `activatedLayers` | política, economia, cultura, Brasil… | atmosfera, oceano, biosfera, geoquímica |
| States | overlays de fundo | políticos/econômicos | atmosfera/oceano/clima/biosfera |
| Markers | pontuais, datados ou de evidência | Paris, Versalhes, Minas, Nova York | localidades de **evidência atual** (Hamersley…) |
| Routes | fluxos quando aplicável | rotas atlânticas | (em geral ausentes) |
| Regions | históricas/políticas ou nulas | 8 Regions (1789) | **nenhuma** Region política |
| Geometrias | nunca inventadas; senão `PENDENTE_REFINAMENTO_ESPACIAL` | fronteiras de 1789 (pendentes) | crátons esquemáticos (pendentes) |
| Legenda epistemológica | fato/evidência/inferência/reconstrução | aplicável | aplicável |
| Legenda temporal | precisão + aproximação | dia/ano | "~2,4 Ga (aproximação)" |
| Legenda editorial/científica | sensível/revisão (hist.) ou incerto (deep) | editorial | científica |
| Itens ocultos | pending mediado/oculto | sensíveis | incertos (paleogeografia) |
| Reconstruction labels | obrigatórios em reconstrução | fronteiras históricas | paleogeografia, oceanos, atmosfera |

### 11.2 Timeline — padrão genérico

| Aspecto | Regra genérica | Cena histórica (1789) | Cena de tempo profundo (2,4 Ga) |
|---|---|---|---|
| Escala | conforme regime de tempo | dia/mês/ano | Ga (faixa) |
| Zoom | centrado no `timeRange` | 1789 (janela 1787–92) | ~2,4 Ga (janela 2,5–2,0 Ga) |
| Eventos | pontuais quando existirem | Bastilha, Estados Gerais… | **nenhum** |
| Processos | blocos longos | Revolução, crise fiscal, tráfico | GOE, fotossíntese, deposição de BIF |
| States | faixas de fundo | França-1789, economia atlântica | atmosfera, oceano, clima, biosfera |
| Evidências | linha de inferência | documental | proxy (S-MIF, BIF…) |
| Claims/ClaimSets | ícone de debate | causas, 1492, escravidão | timing, ritmo, causas, glaciações |
| UncertaintyProfiles | ícone de faixa | poucos | magnitude, paleogeografia |
| Consequência futura | arestas "para frente", com cautela | Terror, abolições | eucariontes, ozônio (muito depois) |
| Antes/depois | cortes comparativos | 1788/1790/1792 | antes/depois do GOE |
| Itens pending | ocultos/mediados | sensíveis | incertos |

**Princípio comum.** Globo e timeline **leem a mesma cena** por ângulos diferentes (espaço × tempo), respeitando os mesmos invariantes: nada pending exibido como fato; reconstrução sempre rotulada; precisão nunca inventada; ClaimSet (lados) distinto de UncertaintyProfile (faixa).

---

## 12. Próximos passos para a Etapa 4G (Tarefa 12)

A Etapa 4F transformou **duas cenas-gabarito em método**: há um padrão genérico de `Scene`, uma taxonomia de 12 tipos, uma matriz de 7 regimes de tempo, decisões fechadas sobre os `State Types` e critérios de publicabilidade. A partir daqui, **qualquer** nova cena (K-Pg, 1492, Revolução Industrial, Apollo 11, Cambriano, formação da Terra, Big Bang) segue o mesmo padrão. A **Etapa 4G**, quando solicitada, pode:

1. **Aplicar o padrão a uma terceira cena** de um tipo ainda não exercitado (ex.: **cósmica** — Big Bang; ou **biológico/evolutiva** — Cambriano; ou **contemporânea** — clima moderno), testando o padrão genérico e o novo `OceanographicState` fora dos dois extremos já feitos.
2. **Instanciar `OceanographicState`** oficialmente (converter `state:oceanos-ferruginosos` e validar os campos da §5 numa cena real), confirmando a decisão da §5.
3. **Resolver o datum do eixo temporal** (1950 BP × J2000) — pendência herdada desde a 4B, necessária para integrar cenas históricas e profundas no mesmo eixo; decisão da **Etapa 3**, aqui reforçada como bloqueio à interoperabilidade.
4. **Reificar `Source`/`MediaAsset`** segundo o padrão (proveniência por claim; mídia com `natureLabel`/licença-por-asset; rotular IA quando houver).
5. **Validar os critérios de publicabilidade** (§9) como checklist operacional aplicado a cada nova cena, antes de qualquer exibição.

**O que a 4G explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (1/1.1) ou política editorial (3.1). Reaberturas da Etapa 2 ficam restritas a instanciar o `OceanographicState` já aprovado.

---

*Documento de entrega da Etapa 4F, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B, 4C, 4D, 4E). Consolida método e tipos: comparação formal das cenas 1789 × 2,4 Ga, padrão genérico de `Scene` (consulta materializada, não duplicação), taxonomia de 12 tipos de cena, matriz de 7 regimes de tempo, e as decisões controladas sobre `State Types` — `OceanographicState` **aprovado** (11º tipo oficial), `GeochemicalState` **não criado** (evidência + campos redox), `EarthSystemState` **não criado** (agregação virtual da Scene). Entrega ainda a lista oficial revisada de State Types, critérios de publicabilidade de cenas em 5 níveis e os padrões genéricos de dossiê e de globo/timeline. Não cria cena nova, não povoa lotes, não escreve código, não propõe MVP, não define stack, não avança para UX final e não entra em currículo/professor/plano de aula. Próxima etapa, quando solicitada: Etapa 4G — aplicação do padrão a uma terceira cena e instanciação oficial do OceanographicState.*
