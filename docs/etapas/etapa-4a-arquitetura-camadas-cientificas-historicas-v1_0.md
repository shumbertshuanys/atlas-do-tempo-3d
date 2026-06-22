# Etapa 4A — Arquitetura das Camadas Científicas e Históricas

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4A · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência espaçotemporal (Etapa 3) e a **política editorial vinculante da Etapa 3.1** · 12/06/2026
**Escopo desta etapa (e seus limites):** esta etapa define a **arquitetura conceitual** das camadas científicas e históricas que serão povoadas no Knowledge Core. Conforme solicitado, ela **não** popula milhares de eventos, **não** escreve código, **não** propõe MVP, **não** define stack técnica, **não** avança para UX final, **não** entra em currículo/professor/plano de aula e **não** desenha o pipeline técnico completo de ingestão. O que segue **prepara o terreno** para o povoamento real (Etapa 4B em diante): mapa de camadas, prioridade, unidade mínima, matriz fonte→camada, risco editorial, incerteza, espinha dorsal, regras de claim, relações e erros a evitar.

**O que esta arquitetura herda e respeita (vinculante):**
- Da **Etapa 2**: as entidades do KC (`KnowledgeItem`→`Event`/`Process`/`Concept`/`Entity`; `Place`/`Region`; `Claim`/`Source`/`Citation`/`ClaimSet`; `Relationship`; `MediaAsset`/`MapAsset`; governança `ProvenanceMetadata`/`LicenseProfile`/`ReviewStatus`/`DatasetSnapshot`; objetos de valor `TimeRange`/`ConfidenceLevel`/`EvidenceLevel`/`UncertaintyProfile`/`ChronologicalScale`), os dez `State` (Atmosphere, Tectonic, Paleogeographic, Climate, Biome, Civilization, Technology, Population, Cultural, Economic), o eixo temporal canônico (Ga↔dia), `GeometryVersion`/`PaleogeographicPosition`/`ModernCorrespondence`/`SpatialUncertainty`.
- Da **Etapa 1 / 1.1**: os três níveis de autoridade (**A** primária / **B** agregador / **C** índice — nunca fonte de claim), os níveis de risco de licença **0–5**, os códigos de decisão de ingestão (**AUTO / ATRIB / ISOLA / FATO / REVH / CONF / COMER / NÃO / INDX**), o padrão **fato ≠ expressão** (fonte NC entra só como fato recodificado) e o **isolamento ShareAlike**.
- Da **Etapa 3.1** (agora **vinculante**): controvérsia legítima → `ClaimSet`; **negacionismo nunca vira claim concorrente**; consenso é tipado como consenso; incerteza legítima separada do fato consolidado; temas sensíveis com **revisão humana obrigatória**; mídia sensível com `natureLabel` + licença + revisão; **Leis 10.639/2003 e 11.645/2008 como cobertura estrutural** (presença e protagonismo, não nota de rodapé).
- O enum `claimType` (Etapa 3.1): `fato documentado` · `medição` · `inferência científica` · `estimativa` · `hipótese` · `controvérsia` · `interpretação historiográfica` · `reconstrução modelada` · `representação artística` · `aproximação didática`.
- O vocabulário `consensusStatus`: `consenso amplo` · `consenso majoritário` · `debate acadêmico` · `hipóteses concorrentes` · `controvérsia historiográfica` · `terminologia sensível` · `desinformação/negacionismo rejeitado` · `insuficiência de evidência`.
- O **invariante de exibição**: nada com `reviewStatus ∈ {pending, rejected, legal-review}` é renderizável nem aparece na simultaneidade.

> **Convenção de leitura.** `CamelCase` = entidade; `camelCase` = campo; valores enumerados em listas. Notação conceitual, **não** código executável. "Povoar" significa criar itens factuais tipados, atribuídos, rotulados e revisados — nunca copiar texto de fontes.

---

## Sumário

1. Mapa geral das camadas (Tarefa 1)
2. Prioridade de povoamento P0/P1/P2/P3 (Tarefa 2)
3. Unidade mínima de povoamento por camada (Tarefa 3)
4. Matriz fonte → camada (Tarefa 4)
5. Riscos editoriais por camada (Tarefa 5)
6. Incertezas científicas por camada (Tarefa 6)
7. Espinha dorsal inicial (Tarefa 7)
8. Regras de povoamento por claim (Tarefa 8)
9. Relação entre camadas (Tarefa 9)
10. Erros a evitar na Etapa 4 (Tarefa 10)
11. Próximos passos para a Etapa 4B (Tarefa 11)

---

## 1. Mapa geral das camadas (Tarefa 1)

São **25 camadas**. As 23 primeiras são camadas **de conteúdo** (povoam itens e States); as duas últimas (**24 Mídia e acervos** e **25 Fontes, claims e incerteza**) são camadas **transversais/meta** — não descrevem o mundo, mas governam *como* todas as outras entram, são ilustradas e são rotuladas.

**Template de cada camada** (onze atributos pedidos): **Finalidade** · **Entidades do KC** · **Tipo de Claim esperado** · **Tipo de State** · **Fontes prioritárias** · **Incerteza típica** · **Riscos editoriais** · **Riscos de licença** · **Relação com simultaneidade** · **Relação com o globo/mapa** · **Relação com a timeline**.

> Onde uma camada não gera `State` próprio, registro o(s) State(s) de outras famílias que ela alimenta ou consome — o modelo da Etapa 2 tem **dez** States fixos; a Etapa 4A **não** cria entidades novas (isso seria remodelagem; ver §11).

---

### Camada 1 — Universo e cosmologia

- **Finalidade.** Ancorar o início absoluto do eixo (Big Bang ~13,8 Ga) e os primeiros processos cósmicos (inflação, nucleossíntese, recombinação/CMB).
- **Entidades.** `Event`/`Process` (Big Bang, inflação), `Concept` (expansão do universo, inflação cósmica), `Entity` (CMB como objeto observacional).
- **Tipo de Claim.** Predominante `inferência científica` (alta confiança para a expansão); `hipótese` para os primeiros instantes (inflação).
- **Tipo de State.** Nenhum State próprio; o "pano de fundo" deste momento é a *ausência* de States planetários — mostrada como ausência (D7), não preenchida.
- **Fontes prioritárias.** NASA (PD, A); literatura cosmológica revisada (A/B).
- **Incerteza típica.** **Muito alta** nos primeiros instantes; alta-a-média a partir da nucleossíntese.
- **Riscos editoriais.** Baixo-médio: Big Bang × criacionismo/terraplanismo é **negacionismo**, não `ClaimSet` (§3.4 da 3.1) — entra o consenso; a posição negacionista só como objeto rotulado, se útil à alfabetização científica.
- **Riscos de licença.** Baixo (NASA PD). Ilustrações sempre `representação artística`/`reconstrução modelada` — nunca "fotografia" do evento.
- **Simultaneidade.** É a **âncora inicial**: "o que acontecia há 13,8 Ga?" retorna este item, com States planetários inexistentes e tudo rotulado como inferência.
- **Globo/mapa.** `sem-localização` (o espaço-tempo origina-se aqui); vista de céu/cosmos, não globo terrestre.
- **Timeline.** Marca o **zero absoluto** do eixo profundo; régua em Ga.

### Camada 2 — Astronomia e Sistema Solar

- **Finalidade.** Formação do Sol, dos planetas, da Terra e da Lua (~4,6 Ga); corpos celestes navegáveis e nomenclatura.
- **Entidades.** `Event` (formação solar, acreção planetária, impacto formador da Lua), `Entity` (Sol, planetas, luas, corpos menores), `Concept` (acreção, diferenciação planetária).
- **Tipo de Claim.** `inferência científica` (formação); `medição` (efemérides, parâmetros orbitais atuais); `hipótese` (detalhes do impacto lunar).
- **Tipo de State.** Nenhum State próprio (precede a Terra com sistemas); alimenta a transição para as camadas 3–4.
- **Fontes prioritárias.** NASA / JPL (PD, A), NASA Exoplanet Archive (P1), IAU (nomenclatura, "fato"), ESA/Gaia (CC BY-SA IGO → **ISOLA**).
- **Incerteza típica.** Baixa-média (parâmetros atuais medidos; formação inferida).
- **Riscos editoriais.** Baixo.
- **Riscos de licença.** Baixo no núcleo (NASA PD); **ShareAlike** da ESA/Gaia exige camada isolada (L2).
- **Simultaneidade.** Âncora ~4,6 Ga; "o que acontecia há 4,6 Ga?" troca a cena para formação do Sistema Solar.
- **Globo/mapa.** Vista do Sistema Solar / céu antes do globo terrestre; nomenclatura IAU como rótulos.
- **Timeline.** Bloco ~4,6 Ga; transição cósmico→planetário.

### Camada 3 — Terra geológica

- **Finalidade.** A **régua do tempo profundo** — éons/eras/períodos/épocas/idades — sobre a qual todas as demais camadas se posicionam.
- **Entidades.** `ChronologicalScale` (objeto de valor), `Process`/`Event` (diferenciação da Terra, formação da crosta), `Region` (crátons, províncias geológicas).
- **Tipo de Claim.** `fato documentado` para a **escala** (nomes+idades de limite, recodificados do ICS); `inferência científica` para os processos profundos.
- **Tipo de State.** Subjaz a `TectonicState`/`PaleogeographicState`; não gera State próprio.
- **Fontes prioritárias.** **Macrostrat** (CC BY, API — **ATRIB**), **ICS** (gráfico NC → **FATO**: nomes+idades recodificados, atribuir Cohen et al./ICS), USGS (PD, P1).
- **Incerteza típica.** Média (idades de limite têm ± conhecidos; Pré-cambriano mais incerto).
- **Riscos editoriais.** Baixo.
- **Riscos de licença.** **Gráfico do ICS é CC BY-NC-SA** → nunca reproduzir a imagem; usar só o **fato** recodificado e renderizar visualização própria.
- **Simultaneidade.** É **a régua** que traduz qualquer instante profundo para o eixo canônico; pré-condição de toda interseção temporal.
- **Globo/mapa.** Base geológica; provê as idades para rotacionar a paleogeografia.
- **Timeline.** É a **espinha métrica** do eixo profundo (Ga/Ma), costurada ao eixo histórico.

### Camada 4 — Atmosfera

- **Finalidade.** Composição/química atmosférica ao longo do tempo (atmosfera primitiva → Grande Evento de Oxidação → atmosfera moderna).
- **Entidades.** `Process` (GOE), `Event` (transições), `Claim` de composição.
- **Tipo de Claim.** `inferência científica` no tempo profundo (ex.: % O₂); `medição` no moderno (séries instrumentais).
- **Tipo de State.** **`AtmosphereState`** (composição num intervalo; transições por `Process`).
- **Fontes prioritárias.** NOAA/NCEI (incl. Paleo) (PD, A); literatura revisada (A/B).
- **Incerteza típica.** **Alta** na atmosfera primitiva; média no Fanerozoico; baixa no moderno.
- **Riscos editoriais.** Baixo (a química profunda é inferência rotulada).
- **Riscos de licença.** Baixo (NOAA PD).
- **Simultaneidade.** **Pano de fundo** de cenas profundas (ex.: "há 2,4 Ga" → `AtmosphereState` oxidando).
- **Globo/mapa.** *Overlay* atmosférico/composicional sobre o globo da idade.
- **Timeline.** Transições atmosféricas marcam blocos (GOE etc.).

### Camada 5 — Clima

- **Finalidade.** Estados climáticos/temperatura num intervalo (glaciações, ótimos climáticos, clima moderno).
- **Entidades.** `Process` (glaciações, snowball Earth), `Event`, `Claim` de temperatura/forçantes.
- **Tipo de Claim.** `inferência científica`/`reconstrução modelada` no profundo; `medição` no moderno; incerteza de projeção como **faixa**, não como dúvida do fato.
- **Tipo de State.** **`ClimateState`**.
- **Fontes prioritárias.** NOAA/NCEI, NASA GISS, Berkeley Earth (CC BY), Copernicus/ERA5 (atrib.), IPCC (**figuras com termos próprios → recriar visualização**); INPE/MapBiomas (Brasil, **ISOLA**).
- **Incerteza típica.** Alta no profundo; baixa no moderno (medido).
- **Riscos editoriais.** **Alto.** Mudança climática antrópica é **consenso** → **sem equivalência** ao negacionismo (§3.4). `ClaimSet` **apenas** para incerteza *interna* (faixas de sensibilidade/projeção), nunca consenso × negação.
- **Riscos de licença.** Médio: figuras do IPCC e dados Copernicus exigem cuidado; MapBiomas é ShareAlike → isolar.
- **Simultaneidade.** Pano de fundo climático de qualquer cena.
- **Globo/mapa.** *Overlay* de temperatura/clima por idade.
- **Timeline.** Glaciações e clima moderno como blocos; séries na ponta contemporânea.

### Camada 6 — Tectônica e paleogeografia

- **Finalidade.** Configuração de placas e **posição dos continentes por idade** — a morfologia do globo no tempo profundo.
- **Entidades.** `PaleogeographicPosition` (rotacionada por idade), `Region` paleogeográfica, `Process` (orogenia, rifteamento), `Concept` (tectônica de placas, supercontinentes).
- **Tipo de Claim.** **`reconstrução modelada`** (rótulo obrigatório, C2/D7); confiança alta na existência de supercontinentes, incerteza nas posições finas.
- **Tipo de State.** **`TectonicState`** + **`PaleogeographicState`**.
- **Fontes prioritárias.** **GPlates + EarthByte** (dados CC BY 3.0 → **ATRIB**; software GPL). **Deep Time Maps proibido** (proprietário); PALEOMAP/Scotese restrito até confirmação.
- **Incerteza típica.** **Alta** em supercontinentes antigos (Rodinia, Columbia/Nuna); média na Pangeia; menor no Cenozoico.
- **Riscos editoriais.** Baixo.
- **Riscos de licença.** Médio (modelo): EarthByte ok com atribuição; substituir Deep Time Maps por reconstruções próprias renderizadas dos dados EarthByte.
- **Simultaneidade.** **Muda o próprio globo**: "o que acontecia há 250 Ma?" troca a Terra para a reconstrução de Pangeia (rotulada).
- **Globo/mapa.** É **o que o globo mostra** no tempo profundo (geometria rotacionada por `ageMa`).
- **Timeline.** Montagem/fragmentação de supercontinentes como blocos estruturais.

### Camada 7 — Oceanos

- **Finalidade.** Bacias oceânicas, circulação, química e nível do mar ao longo do tempo.
- **Entidades.** `Region` (bacias oceânicas), `Process` (abertura/fechamento de oceanos, eventos anóxicos), `Claim` de circulação/nível.
- **Tipo de Claim.** `reconstrução modelada`/`inferência científica` no profundo; `medição` no moderno (nível do mar, temperatura de superfície).
- **Tipo de State.** **Sem State próprio no modelo da Etapa 2.** É servida por `PaleogeographicState` (bacias), `ClimateState` (temperatura/circulação) e `BiomeState` (vida marinha). → **Sinalizar à modelagem** se um `OceanographicState` dedicado será necessário (decisão de remodelagem, não da 4A; ver §11).
- **Fontes prioritárias.** NOAA/NCEI (PD), EarthByte (bacias, CC BY), PBDB (vida marinha, CC BY).
- **Incerteza típica.** Alta no profundo (circulação/química antigas); baixa no moderno.
- **Riscos editoriais.** Baixo.
- **Riscos de licença.** Baixo.
- **Simultaneidade.** Pano de fundo (extensão oceânica, eventos anóxicos coincidentes com extinções).
- **Globo/mapa.** Massas d'água da idade; *overlay* de circulação/nível.
- **Timeline.** Eventos oceânicos (anóxia, fechamento de Tétis) como marcos.

### Camada 8 — Vida e evolução

- **Finalidade.** Origem da vida e as **grandes transições** biológicas (procarionte→eucarionte, multicelularidade, conquista da terra firme).
- **Entidades.** `Process` (evolução de táxons, transições), `Event` (origem da vida, explosão cambriana), `Concept` (seleção natural, ancestralidade comum), `Entity` (grandes clados).
- **Tipo de Claim.** `inferência científica` (evolução como fato; ancestralidade comum); `hipótese` para a **origem da vida** (mecanismos concorrentes).
- **Tipo de State.** **`BiomeState`** (cobertura/biota num intervalo).
- **Fontes prioritárias.** **PBDB** (CC BY, API — **ATRIB**), Open Tree of Life (CC0), Macrostrat (litologia↔fóssil↔tempo).
- **Incerteza típica.** **Alta** na origem da vida; média nas transições profundas.
- **Riscos editoriais.** Médio: evolução é **consenso** → criacionismo/desenho inteligente é **negacionismo**, não `ClaimSet`. Vigilância anti-racista no cruzamento com a camada 10.
- **Riscos de licença.** Baixo.
- **Simultaneidade.** Pano de fundo biótico de qualquer cena profunda.
- **Globo/mapa.** *Overlay* de biota/biomas por idade.
- **Timeline.** Grandes transições como blocos estruturais.

### Camada 9 — Paleobiologia e extinções

- **Finalidade.** Surgimento/extinção de táxons e as **cinco grandes extinções** (eventos biológicos do tempo profundo).
- **Entidades.** `Event`/`Process` (extinções), `Entity` (táxons), ocorrências fósseis ligadas a `Place`/`Region`/`TimeRange`.
- **Tipo de Claim.** `inferência científica` (datas/ocorrências); `hipótese`/`controvérsia` para **causas** (ex.: K-Pg impacto × vulcanismo → `hipóteses concorrentes`).
- **Tipo de State.** **`BiomeState`** (composição da biota antes/depois).
- **Fontes prioritárias.** **PBDB** (CC BY — **ATRIB**), GBIF (filtrar por dataset CC0/CC BY), Macrostrat.
- **Incerteza típica.** Média nas ocorrências; **alta** nas atribuições causais finas.
- **Riscos editoriais.** Baixo (causas em `ClaimSet`, não veredito).
- **Riscos de licença.** Baixo (filtrar GBIF na entrada).
- **Simultaneidade.** Extinções como eventos globais que reorganizam a cena.
- **Globo/mapa.** Distribuição de ocorrências; *overlay* de turnover biótico.
- **Timeline.** As cinco extinções como marcos de primeira ordem.

### Camada 10 — Homo sapiens e evolução humana

- **Finalidade.** Linhagem dos hominíneos e surgimento do *Homo sapiens* (sem progresso linear).
- **Entidades.** `Process` (evolução humana), `Event` (surgimento de espécies, dispersões iniciais), `Entity` (hominíneos), `Place` (sítios).
- **Tipo de Claim.** `inferência científica`; `hipótese`/`hipóteses concorrentes` para ramos e cronologias finas.
- **Tipo de State.** `BiomeState` (contexto) e início de `CivilizationState` (cultura material inicial).
- **Fontes prioritárias.** Paleoantropologia revisada (A/B), PBDB, Open Tree of Life (CC0).
- **Incerteza típica.** **Alta** na evolução humana fina (ramificações, datas).
- **Riscos editoriais.** **Alto.** Cruzamento **raça e ciência**: jamais insinuar hierarquia entre populações humanas; iconografia não pode sugerir "progresso linear". **Revisão obrigatória** no cruzamento com raça.
- **Riscos de licença.** Baixo nos dados; reconstruções de hominíneos = `representação artística`.
- **Simultaneidade.** Pano de fundo da pré-história humana.
- **Globo/mapa.** Mapas de dispersão **rotulados como modelo**.
- **Timeline.** Surgimento de espécies como marcos.

### Camada 11 — Migrações humanas

- **Finalidade.** Dispersões do *Homo sapiens* e povoamentos (Out of Africa, povoamento das Américas, expansões posteriores).
- **Entidades.** `Process`/`Event` (migrações), `Place`/`Region`, `Relationship` (rotas).
- **Tipo de Claim.** `inferência científica`; **`hipóteses concorrentes`** para rotas/cronologias (ex.: povoamento das Américas).
- **Tipo de State.** `PopulationState` (onde houver estimativa) e `CivilizationState`.
- **Fontes prioritárias.** World Historical Gazetteer (estrutura CC BY; **filtrar** datasets), arqueologia revisada, IBGE (povoamento do território brasileiro).
- **Incerteza típica.** **Alta** (rotas, datas, especialmente povoamento das Américas).
- **Riscos editoriais.** Médio: evitar narrativas de substituição simplista; cruzamento com povos originários (camada 22).
- **Riscos de licença.** Médio (filtrar WHG por dataset).
- **Simultaneidade.** Conecta povoamentos simultâneos em continentes distintos.
- **Globo/mapa.** Rotas como geometrias **rotuladas (modelo/inferência)**.
- **Timeline.** Dispersões como processos longos.

### Camada 12 — Civilizações

- **Finalidade.** Configuração de sociedades/polities num intervalo (do Neolítico aos impérios e Estados pré-modernos), com agência de África, Ásia, Américas e Europa em **simultaneidade**.
- **Entidades.** `CivilizationState`, `Event`, `Place`, `Entity` (instituições, pessoas), `Concept`, `Region` (com `GeometryVersion`).
- **Tipo de Claim.** `fato documentado` (eventos datados) + **`interpretação historiográfica`** (causas, naturezas) em `ClaimSet`.
- **Tipo de State.** **`CivilizationState`** (+ `PopulationState`/`EconomicState` quando houver dado).
- **Fontes prioritárias.** **Pleiades** (CC BY — **ATRIB**), **WHG** (CC BY na estrutura; **filtrar**), fontes A primárias e historiografia; **Seshat só como leitura** (CC BY-NC-SA → **NÃO** como expressão; fato re-derivável de fonte A via curadoria).
- **Incerteza típica.** Média (demografia e cronologias antigas têm `estimativa`).
- **Riscos editoriais.** **Alto.** Colonização, escravidão, povos originários → `ClaimSet` + **revisão obrigatória**; Leis 10.639/11.645 como **cobertura estrutural**; antieurocentrismo via simultaneidade.
- **Riscos de licença.** Médio: Seshat fora como expressão; WHG por dataset.
- **Simultaneidade.** **Núcleo** da função "o que acontecia no mundo neste momento?".
- **Globo/mapa.** Territórios por `GeometryVersion` da época; nomes datados (`nameVariants[]`).
- **Timeline.** Ascensão/auge/queda como processos; eventos pontuais internos.

### Camada 13 — Política e Estados

- **Finalidade.** Formação de Estados, regimes, revoluções, fronteiras e instituições políticas.
- **Entidades.** `Event`/`Process`, `Region` (com `GeometryVersion`), `Entity` (Estados, líderes, instituições), `ClaimSet`.
- **Tipo de Claim.** `fato documentado` (datas, atos) + `interpretação historiográfica` (causas/significado).
- **Tipo de State.** `CivilizationState` (configuração política); `PopulationState` quando aplicável.
- **Fontes prioritárias.** WHG, **geoBoundaries** (CC BY — **ATRIB**, fronteiras modernas), IBGE (Brasil), OWID/World Bank (indicadores políticos modernos), Arquivo Nacional/Biblioteca Nacional (Brasil). **ACLED excluído** (licença comercial).
- **Incerteza típica.** Baixa-média (eventos modernos bem documentados; fronteiras antigas difusas → `SpatialUncertainty`).
- **Riscos editoriais.** **Alto a crítico.** Ditaduras, violência de Estado, conflitos contemporâneos; **pessoas vivas/identificáveis** exigem LGPD/revisão. Fatos documentados de repressão **não** são "um dos lados".
- **Riscos de licença.** Médio: ACLED fora; geoBoundaries no lugar do GADM (CC BY-NC).
- **Simultaneidade.** **Núcleo** (Revolução Francesa × Inconfidência × EUA, 1789).
- **Globo/mapa.** Fronteiras por idade; disputas territoriais como `ClaimSet` cartográfico.
- **Timeline.** Regimes/revoluções como blocos.

### Camada 14 — Economia

- **Finalidade.** Configuração econômica num intervalo (sistemas produtivos, comércio, indicadores).
- **Entidades.** `EconomicState`, `Process` (industrialização, globalização), `Event`, `Concept`.
- **Tipo de Claim.** `medição` (indicadores modernos); `estimativa` (economia histórica/antiga).
- **Tipo de State.** **`EconomicState`** (+ `PopulationState`).
- **Fontes prioritárias.** **Our World in Data** (CC BY — **ATRIB**), **World Bank** (CC BY 4.0 — **ATRIB**), IPEA/IBGE (Brasil).
- **Incerteza típica.** Baixa no moderno; **alta** em séries econômicas pré-estatísticas (rotular `estimativa`).
- **Riscos editoriais.** Médio (interpretações de causas de desenvolvimento/desigualdade → `ClaimSet`; o produto não opina sobre política econômica).
- **Riscos de licença.** Baixo (CC BY com atribuição rastreada).
- **Simultaneidade.** Pano de fundo econômico de qualquer cena.
- **Globo/mapa.** *Overlay* de indicadores por região/idade.
- **Timeline.** Séries econômicas na ponta moderna; transições (industrialização) como blocos.

### Camada 15 — Ciência

- **Finalidade.** Descobertas, teorias e instrumentos científicos no tempo (ciência como atividade histórica e simultânea).
- **Entidades.** `Event` (descobertas, publicações), `Concept` (teorias, leis), `Entity` (cientistas, instituições).
- **Tipo de Claim.** `fato documentado` (datas de descoberta/publicação); `inferência`/`interpretação` em história da ciência.
- **Tipo de State.** Sem State próprio; relaciona-se a `TechnologyState` e `CulturalState`.
- **Fontes prioritárias.** Arquivos/bibliotecas (A), OWID (marcos), museus de ciência (parcerias/curadoria).
- **Incerteza típica.** Baixa (datas) a média (atribuições de prioridade/autoria).
- **Riscos editoriais.** Médio: cruzamento **raça e ciência** (camada 10) exige vigilância; evitar "gênio solitário" e priorização eurocêntrica.
- **Riscos de licença.** Médio (mídia de acervos por asset).
- **Simultaneidade.** Caso canônico: **Lavoisier publica o *Traité* em 1789**, simultâneo à Revolução Francesa.
- **Globo/mapa.** Lugar da descoberta/instituição.
- **Timeline.** Descobertas como pontos; programas científicos como processos.

### Camada 16 — Tecnologia

- **Finalidade.** Tecnologias disponíveis/difundidas num intervalo (do controle do fogo às tecnologias digitais).
- **Entidades.** `TechnologyState`, `Event` (invenções), `Concept`, `Entity` (artefatos, sistemas técnicos).
- **Tipo de Claim.** `fato documentado` (invenções datadas); `estimativa` (difusão, datação de tecnologias antigas).
- **Tipo de State.** **`TechnologyState`**.
- **Fontes prioritárias.** OWID, literatura, museus (curadoria).
- **Incerteza típica.** Média (datação e difusão de tecnologias pré-modernas).
- **Riscos editoriais.** Baixo.
- **Riscos de licença.** Médio (imagens de acervo por asset).
- **Simultaneidade.** Pano de fundo técnico (o que se podia fazer naquele momento).
- **Globo/mapa.** Difusão tecnológica por região/idade.
- **Timeline.** Trilhas tecnológicas como processos.

### Camada 17 — Cultura

- **Finalidade.** Produção e movimentos culturais num intervalo (arte, literatura, música, práticas).
- **Entidades.** `CulturalState`, `Event`, `Concept` (movimentos), `Entity` (obras como objetos históricos, autores), `MediaAsset`.
- **Tipo de Claim.** `fato documentado` (datas/autorias) + `interpretação historiográfica` (significado de movimentos).
- **Tipo de State.** **`CulturalState`**.
- **Fontes prioritárias.** Met Open Access/Smithsonian (CC0), Biblioteca Nacional/Hemeroteca (Brasil, muito PD), IPHAN (patrimônio), Europeana/DPLA (**por asset**), Wikimedia Commons (**por asset**).
- **Incerteza típica.** Baixa-média.
- **Riscos editoriais.** Médio: cruzamento com religião (camada 18) e apropriação/sacralidade; sem proselitismo nem ridicularização.
- **Riscos de licença.** **Alto** (mídia por asset — o ponto mais sensível de licença depois da 24).
- **Simultaneidade.** Pano de fundo cultural.
- **Globo/mapa.** Lugar de produção/movimento.
- **Timeline.** Movimentos como blocos.

### Camada 18 — Religiões e sistemas simbólicos

- **Finalidade.** Religiões, cosmovisões e sistemas simbólicos **como fenômenos histórico-culturais** (não como afirmações doutrinárias de verdade).
- **Entidades.** `Process`/`Event` (surgimento, difusão, reformas), `Concept` (tradições, doutrinas como objeto de estudo), `Entity` (figuras, instituições), `CulturalState`.
- **Tipo de Claim.** `fato documentado` (existência/prática/difusão); `interpretação historiográfica`. **Nunca** claim de verdade doutrinária.
- **Tipo de State.** `CulturalState` (configuração simbólica de uma sociedade).
- **Fontes prioritárias.** Historiografia das religiões (A/B), acervos (por asset), IPHAN (patrimônio religioso brasileiro, incl. afro e indígena).
- **Incerteza típica.** Média (origens e cronologias de tradições antigas).
- **Riscos editoriais.** **Alto.** Sacralidade, proselitismo, ridicularização; imagens religiosas sensíveis com revisão; equidade entre tradições (incl. religiões afro-brasileiras e indígenas — Leis 10.639/11.645).
- **Riscos de licença.** Alto (mídia por asset; símbolos sensíveis).
- **Simultaneidade.** Pano de fundo simbólico (sistemas de crença coexistentes).
- **Globo/mapa.** Difusão de tradições por região/idade.
- **Timeline.** Surgimento/difusão como processos.

### Camada 19 — Guerras e conflitos

- **Finalidade.** Guerras, conflitos, genocídios e violência organizada no tempo.
- **Entidades.** `Event`/`Process`, `Region`, `Entity` (forças, atores), `ClaimSet` (causas/responsabilidades).
- **Tipo de Claim.** `fato documentado` (ocorrência/datas); `interpretação historiográfica` (causas); **negação de genocídio = negacionismo**, fora de qualquer `ClaimSet`.
- **Tipo de State.** Sem State próprio; muda `CivilizationState`/`PopulationState`.
- **Fontes prioritárias.** Historiografia revisada, arquivos, comissões da verdade (Brasil). **ACLED excluído**; GDELT só como sinal (alto risco).
- **Incerteza típica.** Média (números de baixas, causas).
- **Riscos editoriais.** **Alto a crítico.** Dignidade às vítimas; mídia gráfica **oculta por padrão** e rotulada; falsa simetria proibida onde há crime documentado; conflitos contemporâneos com cautela máxima.
- **Riscos de licença.** Médio-alto (ACLED fora; mídia de violência restrita e por asset).
- **Simultaneidade.** Conflitos simultâneos em várias regiões.
- **Globo/mapa.** Frentes/territórios por idade; mídia gráfica não exibida por padrão.
- **Timeline.** Guerras como blocos; eventos pontuais internos.

### Camada 20 — Brasil e territórios que hoje correspondem ao Brasil

- **Finalidade.** A **lente Brasil** (D8): história e territórios que hoje correspondem ao Brasil, em **simultaneidade** com o mundo, sem anacronismo.
- **Entidades.** Todas as famílias + **`ModernCorrespondence`** (ponte território histórico → unidades atuais), `CivilizationState`/`EconomicState`/`PopulationState`/`CulturalState`.
- **Tipo de Claim.** `fato documentado` + `interpretação historiográfica` em `ClaimSet` (colonização, escravidão).
- **Tipo de State.** `CivilizationState` (indígena/colonial/nacional), `EconomicState` (economia mineradora etc.), `PopulationState`.
- **Fontes prioritárias.** **IBGE** (aberto — **ATRIB**), IPHAN, Arquivo Nacional, Biblioteca Nacional, INPE, **MapBiomas** (CC BY-SA → **ISOLA**), CPRM/SGB (geologia).
- **Incerteza típica.** Baixa-média (boa documentação moderna; território colonial com `SpatialUncertainty`).
- **Riscos editoriais.** **Alto.** Colonização, escravidão, povos indígenas, ditadura militar; **revisão obrigatória**; Leis 10.639/11.645 estruturais.
- **Riscos de licença.** Médio (MapBiomas ShareAlike → isolar; microdados IBGE restritos → não ingerir não desidentificados).
- **Simultaneidade.** **Estrutural**: a cena canônica ("Inconfidência Mineira em 1789") é o teste-padrão.
- **Globo/mapa.** `ModernCorrespondence` resolve "o que hoje é o Brasil" sem reescrever a história.
- **Timeline.** Brasil **em paralelo** ao eixo mundial.

### Camada 21 — África e diáspora africana

- **Finalidade.** Civilizações africanas, tráfico atlântico e diáspora — presença e protagonismo (Lei 10.639/2003).
- **Entidades.** `CivilizationState`, `Process` (sistema escravista/tráfico, com rotas como `Relationship`), `Event`, `Place` (portos, reinos), `Region`.
- **Tipo de Claim.** `fato documentado` (sistema/rotas/eventos) + `interpretação historiográfica` (causas/escala).
- **Tipo de State.** `CivilizationState`, `PopulationState`, `CulturalState`.
- **Fontes prioritárias.** WHG (filtrar), historiografia africana e afro-brasileira, bases acadêmicas do tráfico transatlântico, acervos (por asset).
- **Incerteza típica.** Média (demografia do tráfico, cronologias de reinos).
- **Riscos editoriais.** **Alto.** Escravidão (violência sistêmica), raça; "pessoas escravizadas", sem eufemismo; nomear resistência (quilombos); **África como origem de civilizações**, não periferia.
- **Riscos de licença.** Médio-alto (mídia por asset).
- **Simultaneidade.** **Antídoto ao eurocentrismo** — África em paralelo cronológico com Europa/Américas.
- **Globo/mapa.** Territórios africanos + rotas da diáspora.
- **Timeline.** **Em paralelo** ao eixo mundial.

### Camada 22 — Povos indígenas e história profunda das Américas

- **Finalidade.** História profunda das Américas e diversidade/protagonismo indígena — presente **e** passado (Lei 11.645/2008).
- **Entidades.** `CivilizationState`, `Event`/`Process` (povoamento, sambaquis, marajoara, sociedades complexas), `Entity` (povos, com etnônimos/autodenominações), `Place`.
- **Tipo de Claim.** `fato documentado` + **`hipóteses concorrentes`** (datação/rotas de povoamento).
- **Tipo de State.** `CivilizationState`, `PopulationState`, `CulturalState`.
- **Fontes prioritárias.** Etno-historiografia, arqueologia, IPHAN, IBGE, **fontes indígenas**.
- **Incerteza típica.** **Alta** (povoamento das Américas; cronologias concorrentes).
- **Riscos editoriais.** **Alto.** Homogeneização ("índio" genérico), sacralidade, "povos do passado"; centenas de povos, presença contemporânea; cautela/consentimento com imagens de pessoas e rituais.
- **Riscos de licença.** Médio-alto (mídia sensível; consentimento).
- **Simultaneidade.** **Em paralelo** — Américas povoadas e complexas em simultaneidade com o Velho Mundo.
- **Globo/mapa.** Territórios originários; nomes em primeiro plano sobre nomes coloniais (variantes datadas).
- **Timeline.** **Em paralelo**, da história profunda ao presente.

### Camada 23 — Mundo contemporâneo

- **Finalidade.** A ponta contemporânea: indicadores, eventos recentes e o "presente móvel".
- **Entidades.** `Event`, `EconomicState`/`PopulationState`/`ClimateState` (moderno), `Entity` (Estados, organizações; **pessoas vivas com LGPD**).
- **Tipo de Claim.** `medição` (indicadores); `fato documentado` (eventos); projeções como `estimativa`/faixa.
- **Tipo de State.** `EconomicState`, `PopulationState`, `ClimateState`.
- **Fontes prioritárias.** OWID, World Bank, UN/UNESCO/WHO (por dataset), IBGE, INPE.
- **Incerteza típica.** Baixa (medido); projeções rotuladas como faixa.
- **Riscos editoriais.** **Alto a crítico.** Temas polarizados, pandemias, conflitos contemporâneos, **pessoas vivas/identificáveis**; consenso científico não relativizado por polarização; o produto não emite opinião institucional.
- **Riscos de licença.** Médio (datasets ONU por item; ACLED fora).
- **Simultaneidade.** A **borda "agora"** do eixo (presente móvel derivado do relógio).
- **Globo/mapa.** *Overlays* de indicadores atuais.
- **Timeline.** Ponta contemporânea; "em curso" rotulado.

### Camada 24 — Mídia e acervos *(transversal/meta)*

- **Finalidade.** Governar **toda** imagem/mapa/mídia que ilustra as outras camadas. **Mídia não é evidência.**
- **Entidades.** `MediaAsset`, `MapAsset`, `LicenseProfile`, `natureLabel`.
- **Tipo de Claim.** Não afirma fato; carrega `natureLabel` (`fotografia` / `mapa` / `reconstrução modelada` / `representação artística`).
- **Tipo de State.** N/A (ilustra States, não é State).
- **Fontes prioritárias.** Wikimedia Commons (**por asset**, filtrar), Met/Smithsonian (CC0), Library of Congress/Internet Archive (muito PD), Europeana/DPLA (**por asset**), Biblioteca Nacional, IPHAN. **David Rumsey (scans CC BY-NC-SA) → NÃO**; obter o original PD por provedor PD-explícito.
- **Incerteza típica.** N/A (a "incerteza" aqui é a **natureza** do asset, não confiança factual).
- **Riscos editoriais.** **Alto.** Violência/vítimas, propaganda (sempre rotulada), símbolos autoritários, imagem religiosa sensível, **menores**, **toda mídia gerada por IA** (rotulada + revisada).
- **Riscos de licença.** **Crítico** — é a camada de maior risco jurídico: licença **por asset**, isolar ShareAlike/ODbL, NC fora, confirmação obrigatória (CONF/REVH).
- **Simultaneidade.** Ilustra a cena; nunca a sustenta como prova.
- **Globo/mapa.** *Overlays* visuais; `MapAsset` com `GeometryVersion` e rótulo.
- **Timeline.** Ilustra blocos; nunca substitui o claim.

### Camada 25 — Fontes, claims e incerteza *(transversal/meta — a espinha epistêmica)*

- **Finalidade.** Garantir que **todo** item de todas as camadas carregue fonte, tipo de claim e incerteza — é o **portão** por onde tudo passa (D7, Etapa 1.1).
- **Entidades.** `Source`, `Citation`, `Claim`, `ClaimSet`, `ProvenanceMetadata`, `ReviewStatus`, e os objetos de valor `ConfidenceLevel`/`EvidenceLevel`/`UncertaintyProfile`.
- **Tipo de Claim.** Define **todos** os `claimType`; não tem claim próprio — é a tipagem.
- **Tipo de State.** N/A.
- **Fontes prioritárias.** Todas as A/B das demais camadas; **Wikidata/VIAF apenas INDX** (reconciliação de identificadores, nunca origem de claim).
- **Incerteza típica.** É **onde a incerteza vive** — `UncertaintyProfile` é sua razão de existir.
- **Riscos editoriais.** Governa o risco de **todas**: falsa equivalência, inferência-como-fato, claim sem fonte.
- **Riscos de licença.** Governa a licença de todas (campos `license`/`licenseRiskLevel`/`ingestionDecision`).
- **Simultaneidade.** Anexa `claimType`+`confidenceLevel` a cada resultado da interseção temporal/espacial.
- **Globo/mapa.** Faz o globo/timeline distinguir, à vista, fato × inferência × reconstrução.
- **Timeline.** Garante que nada apareça no eixo sem tempo, fonte e tipo.

---

## 2. Prioridade de povoamento P0/P1/P2/P3 (Tarefa 2)

**Definições.** **P0** — espinha dorsal inicial (presença estrutural *fina*, não exaustiva); **P1** — essencial para V1; **P2** — importante para profundidade; **P3** — expansão futura.

**Critérios** (Etapa 0/D5): valor para "o que acontecia no mundo neste momento?"; valor visual no globo/timeline; fonte aberta confiável; baixa complexidade jurídica; baixa complexidade editorial; utilidade escolar; cobertura Brasil; capacidade de gerar simultaneidade.

> **Nota.** P0 é um **corte vertical fino** que atravessa muitas camadas (o eixo Big Bang→presente toca quase todas), não algumas camadas "completas". Camadas estruturalmente obrigatórias por mandato (20/21/22, Leis 10.639/11.645) entram em P0 **mesmo com alta complexidade editorial** — mas com `reviewStatus = pending` por padrão.

| # | Camada | Prioridade | Por quê |
|---|---|---|---|
| 1 | Universo e cosmologia | **P0** | Âncora inicial do eixo; fonte aberta (NASA PD); baixo risco; alto valor visual. |
| 2 | Astronomia e Sistema Solar | **P0** | Âncora ~4,6 Ga; NASA/JPL PD; baixo risco; transição cósmico→planetário. |
| 3 | Terra geológica | **P0** | **A régua do tempo** (Macrostrat/ICS-fato); pré-condição de tudo. |
| 4 | Atmosfera | **P0** | Pano de fundo das cenas profundas (GOE); NOAA PD; baixo risco. |
| 5 | Clima | **P1** | Backdrop importante, mas risco editorial alto (clima) e maior peso na ponta moderna → após espinha. |
| 6 | Tectônica e paleogeografia | **P0** | **É o que o globo mostra** no tempo profundo; EarthByte CC BY; alto valor visual. |
| 7 | Oceanos | **P2** | Servida por outros States; profundidade depois (e questão de modelagem aberta). |
| 8 | Vida e evolução | **P0** | Grandes transições estruturam o eixo; PBDB CC BY; risco médio gerenciável. |
| 9 | Paleobiologia e extinções | **P0** | As cinco extinções são marcos de 1ª ordem; PBDB API; baixo risco. |
| 10 | Homo sapiens e evolução humana | **P0** | Origem da linhagem humana; estrutural — porém **revisão obrigatória** (raça). |
| 11 | Migrações humanas | **P1** | Profundidade da simultaneidade humana; alta incerteza → depois da espinha. |
| 12 | Civilizações | **P0** | **Núcleo** da simultaneidade; Pleiades/WHG; editorial-gated. |
| 13 | Política e Estados | **P0** | **Núcleo** (cena canônica 1789); editorial-gated (contemporâneo→P1/P2). |
| 14 | Economia | **P1** | OWID/World Bank limpos; mais valor na ponta moderna. |
| 15 | Ciência | **P1** | Precisa de **âncoras P0 finas** (Lavoisier 1789); profundidade em P1. |
| 16 | Tecnologia | **P1** | Backdrop útil; datação difusa → profundidade depois. |
| 17 | Cultura | **P2** | Mídia-pesada (licença alta); profundidade depois. |
| 18 | Religiões e sistemas simbólicos | **P2** | Editorial sensível + licença de mídia; cuidado e curadoria → depois. |
| 19 | Guerras e conflitos | **P1** | Essencial à simultaneidade; editorial alto; contemporâneo restrito → P2. |
| 20 | Brasil e territórios | **P0** | **Lente Brasil estrutural** (D8); IBGE aberto; cena canônica; editorial-gated. |
| 21 | África e diáspora | **P0** | **Lei 10.639 — cobertura estrutural**; antieurocentrismo; editorial-gated. |
| 22 | Povos indígenas e Américas | **P0** | **Lei 11.645 — cobertura estrutural**; cena canônica; editorial-gated. |
| 23 | Mundo contemporâneo | **P1** | Ponta "agora" (OWID/World Bank limpos); polarizados/pessoas vivas → P2. |
| 24 | Mídia e acervos | **P0 (esqueleto)** | O **regime `natureLabel`/licença** precisa existir desde o 1º asset; povoamento amplo é P1/P2. |
| 25 | Fontes, claims e incerteza | **P0 (meta)** | É o **portão**; nenhuma camada entra sem ele. |

**P3 — expansão futura (modo, não lista de camadas):** granularidade fina de todas as camadas; regiões além da espinha; tópicos de nicho; fontes P2 de aprofundamento da Etapa 1 (CDS/SIMBAD, GBIF em profundidade, PeriodO, Pelagios etc.); profundidade de mídia; **ondas de conteúdo para faixas 6–11 anos** (D9: V1 foca Fundamental II + EM). Nada disso bloqueia a espinha.

---

## 3. Unidade mínima de povoamento por camada (Tarefa 3)

Para cada camada: **entidades obrigatórias** · **claims mínimos** · **fontes mínimas** · **campos de tempo/espaço indispensáveis** · **relações necessárias** · **itens que exigem revisão humana**. A unidade mínima é o **menor item publicável** (ver §8: estado `publicável`).

> Regra transversal (Etapa 1.1 + 3.1): **todo** item, em qualquer camada, exige `ProvenanceMetadata` + `claimType` + `confidenceLevel` + `reviewStatus`. Abaixo, só o que é *específico* de cada camada.

| Camada | Unidade mínima | Entidades obrigatórias | Claims mínimos | Fontes mínimas | Tempo/Espaço | Relações | Revisão humana |
|---|---|---|---|---|---|---|---|
| 1 Universo | `Event`/`Process` + Claims | Event/Process | claim principal + temporal | NASA + literatura A/B | `DeepTimeAge`±; sem localização | predecessor-de (Sistema Solar) | Não (salvo cruzar negacionismo) |
| 2 Astronomia/SS | `Event`/`Entity` + Claims | Event ou Entity | principal + temporal | NASA/JPL; IAU (nomes) | `DeepTimeAge`; órbita/sem-superfície | parte-de (Sistema Solar) | Não |
| 3 Terra geológica | unidade da `ChronologicalScale` | ChronologicalScale | escala (nomes+idades) | Macrostrat + ICS(fato) | limites em Ma/Ga ± | contém/ordena períodos | Não |
| 4 Atmosfera | `AtmosphereState` + Claims | AtmosphereState | composição + temporal | NOAA/NCEI Paleo | `TimeRange` longo; global | transitionsFrom/To (GOE) | Não |
| 5 Clima | `ClimateState` + Claims | ClimateState | temperatura/forçante + temporal | NOAA/GISS/Berkeley | `TimeRange`; região/global | contextualiza vida/civilização | **Sim** (tema clima) |
| 6 Tectônica/paleogeo | `PaleogeographicState` + `PaleogeographicPosition` | TectonicState/PaleogeoState | reconstrução + idade | EarthByte/GPlates | `ageMa`; geometria rotacionada | base do globo da idade | Não (rótulo modelo obrigatório) |
| 7 Oceanos | `Region` oceânica + Claims (via States existentes) | Region + Paleogeo/Climate/Biome State | extensão/circulação + temporal | NOAA/EarthByte/PBDB | `TimeRange`; bacia | parte-de paleogeografia | Não |
| 8 Vida/evolução | `Process`/`Event` + `BiomeState` | Process/Event | principal + temporal | PBDB/OToL | `TimeRange`; região/global | causou/afetou biota | **Sim** se cruza raça (cam.10) |
| 9 Paleobiologia/extinções | `Event` extinção + ocorrências | Event/Process | ocorrência + temporal + causa(ClaimSet) | PBDB | `TimeRange`; ocorrência geo | ocorreu-durante (período) | Não |
| 10 Homo sapiens | `Process`/`Event` + `Entity` | Process/Event/Entity | principal + temporal | paleoantropologia A/B | `TimeRange`; sítio (`SpatialUncertainty`) | descende-de/relacionado | **Sim, obrigatória** (raça) |
| 11 Migrações | `Process`/`Event` + rotas | Process/Event/Relationship | rota(hipótese) + temporal | WHG/arqueologia | `TimeRange`; rota (modelo) | origem→destino | **Sim** (cruza povos originários) |
| 12 Civilizações | `CivilizationState` + Events + Places | CivilizationState/Place | configuração + temporal + (ClaimSet) | Pleiades/WHG/A primárias | `TimeRange`; `GeometryVersion` | conecta povos/lugares/eventos | **Sim, obrigatória** (sensíveis) |
| 13 Política/Estados | Events + Regions + ClaimSets | Event/Region | fato datado + interpretação(ClaimSet) | WHG/geoBoundaries/IBGE | `TimeRange`; fronteira datada | causou/sucedeu | **Sim** (contemp./pessoas vivas) |
| 14 Economia | `EconomicState` + indicadores | EconomicState | indicador(medição/estimativa) + temporal | OWID/World Bank/IBGE | `TimeRange`; região | liga a período/região | Conforme |
| 15 Ciência | `Event`/`Concept` + `Entity` | Event/Concept | descoberta datada | arquivos/OWID | `TimeRange`; lugar | instancia conceito | Conforme (raça) |
| 16 Tecnologia | `TechnologyState` + Events | TechnologyState/Event | invenção/difusão + temporal | OWID/museus | `TimeRange`; região | liga a período/região | Não |
| 17 Cultura | `CulturalState` + Events + MediaAsset | CulturalState | fato + interpretação | acervos/IPHAN | `TimeRange`; lugar | liga arte a tempo/lugar | **Sim** (mídia/sacralidade) |
| 18 Religiões | `Process`/`Concept` + `CulturalState` | Process/Concept | fato histórico de crença/prática | historiografia/IPHAN | `TimeRange`; difusão | difundiu-se/influenciou | **Sim, obrigatória** |
| 19 Guerras | `Event`/`Process` + `Region` + ClaimSet | Event/Region | fato + causas(ClaimSet) | historiografia/comissões | `TimeRange`; frente | causou/contemporâneo | **Sim, obrigatória** |
| 20 Brasil | Events + `ModernCorrespondence` + States regionais | Event/ModernCorrespondence | fato + interpretação(ClaimSet) | IBGE/IPHAN/Arquivo Nac. | `TimeRange`; `GeometryVersion`+`ModernCorrespondence` | Brasil↔mundo simultâneo | **Sim, obrigatória** |
| 21 África/diáspora | `CivilizationState` + `Process`(tráfico) + rotas | CivilizationState/Process | fato + interpretação | WHG/historiografia afro | `TimeRange`; território+rotas | Brasil↔África↔Europa | **Sim, obrigatória** |
| 22 Povos indígenas | `CivilizationState` + Events + `Entity`(povos) | CivilizationState/Entity | fato + (hipóteses concorrentes) | etno-historiografia/IPHAN/IBGE | `TimeRange`; território (autodenom.) | presente↔passado | **Sim, obrigatória** |
| 23 Contemporâneo | `Event` + States modernos | Event/EconomicState | medição + datado | OWID/World Bank/ONU | `TimeRange`(agora); região | borda do eixo | **Sim** (pessoas vivas/polarizado) |
| 24 Mídia | `MediaAsset`/`MapAsset` + `natureLabel` | MediaAsset/LicenseProfile | (não-claim) natureLabel + licença | acervos PD/CC0/CC BY (por asset) | (acoplado ao item ilustrado) | ilustra item | **Sim** (violência/IA/menores/propaganda) |
| 25 Fontes/claims | `Source`+`Citation`+`Claim` (a tipagem) | Source/Citation/Claim | — (é a tipagem de todos) | A/B; Wikidata só INDX | — | sustenta todo item | Governa toda revisão |

---

## 4. Matriz fonte → camada (Tarefa 4)

Relaciona as fontes da Etapa 1 às camadas, **sem reabrir a auditoria** (usa Etapa 1 + 1.1 como base). Colunas: **camada(s) atendida(s)** · **tipo de dado** · **autoridade A/B/C** · **risco de licença (0–5)** · **decisão de ingestão (1.1)** · **uso permitido** · **observação de curadoria**.

| Fonte | Camada(s) | Tipo de dado | A/B/C | Risco | Decisão | Uso permitido | Observação de curadoria |
|---|---|---|---|---|---|---|---|
| **NASA** (Open Data/JPL/Image Lib.) | 1, 2 | tabular/imagem/efemérides | A | 0 | **AUTO** | tudo (PD) | Imagem com pessoa/logo → REVH. |
| **ESA** (Hubble/Gaia/ESASky) | 2, (1) | tabular/imagem | A | 3 | **ISOLA** | camada isolada (CC BY-SA IGO) | Não deixar SA contaminar o núcleo. |
| **JPL** (efemérides/missões) | 2 | efemérides/tabular | A | 0 | **AUTO** | tudo (PD) | Parte da NASA; órbitas como `medição`. |
| **NASA Exoplanet Archive** | 2 | tabular | A | 0–1 | **AUTO/ATRIB** | catálogo (público) | P1; fora da espinha mínima. |
| **Macrostrat** | 3, 8, 9 | escala/coluna geológica | B | 1 | **ATRIB** | tudo c/ atribuição | **Veículo aberto da régua do tempo** (API). |
| **ICS** (via fatos recodificados) | 3 | nomes+idades de limite | A | 4 (gráfico)/0 (fato) | **FATO** | só o **fato** recodificado | Gráfico NC → nunca a imagem; atribuir Cohen et al./ICS. |
| **NOAA/NCEI** (+Paleo) | 4, 5, 7, 23 | séries/raster | A | 0 | **AUTO** | tudo (PD) | Paleoclima = `inferência` rotulada. |
| **GPlates/EarthByte** | 6, 7 | modelo/vetorial | A | 1 | **ATRIB** | dados CC BY 3.0 | **Sempre `reconstrução modelada`**; substitui Deep Time Maps. |
| **Paleobiology Database** | 8, 9, (7) | ocorrências/tabular | A | 1 | **ATRIB** | tudo c/ atribuição | Usar versão pública; restrição de contribuidor → CONF. |
| **Natural Earth** | 6, 13, 20 | vetorial base | A/B | 0 | **AUTO** | tudo (PD) | Base do mundo atual. |
| **geoBoundaries** | 13, 20, 23 | fronteiras admin. | A/B | 1 | **ATRIB** | tudo c/ atribuição | **Substitui GADM** (CC BY-NC). |
| **Pleiades** | 12 | gazetteer antigo | A | 1 | **ATRIB** | lugares antigos | Conector lugar↔evento na Antiguidade. |
| **World Historical Gazetteer** | 11, 12, 13, 21 | gazetteer/linked | B | 1–2 | **ATRIB/CONF** | estrutura CC BY; **datasets filtrados** | Datasets contribuídos têm licença variável → filtrar. |
| **Our World in Data** | 14, 23, (5) | tabular | B | 1 | **ATRIB** | próprio CC BY; terceiros por item | Terceiros embutidos → verificar item. |
| **World Bank** | 14, 23, 13 | tabular | A/B | 1 | **ATRIB** | tudo c/ atribuição | Indicadores modernos. |
| **IBGE** | 20, 13, 14, 22, 23 | tabular/vetorial | A | 1 | **ATRIB** | aberto (Dec. 8.777) | **Microdados não desidentificados → NÃO/REVH (SAR)**. |
| **INPE** | 5, 20, 23 | raster/séries | A | 1 | **ATRIB** | monitoramento aberto | Brasil: clima/desmatamento como `medição`. |
| **MapBiomas** | 5, 20 | raster/vetorial | A/B | 3 | **ISOLA** | camada isolada (CC BY-SA) | ShareAlike → isolar do núcleo. |
| **CPRM/SGB** | 3, 20 | geologia BR | A | 1 | **ATRIB** | geologia nacional | Cobertura geológica do território brasileiro. |
| **Arquivo Nacional** | 13, 17, 19, 20, 21 | documento/imagem | A | 2 | **CONF** | por asset (muito PD) | Confirmar licença por documento. |
| **Biblioteca Nacional** | 17, 20, 21, 24 | texto/imagem | A | 2 | **CONF** | por asset (muito PD) | Hemeroteca: confirmar por item. |
| **IPHAN** | 17, 18, 20, 22 | patrimônio | A | 2 | **CONF** | por asset | Patrimônio afro/indígena: sacralidade + consentimento. |
| **Wikidata** | (todas, como índice) | linked data | C | 0 (CC0) | **INDX** | **só reconciliação** | **Nunca** origem de claim. |
| **Wikimedia Commons** | 24 (todas via asset) | imagem/mídia | B | 2 | **CONF** | por asset | Filtrar PD/CC0/CC BY; rejeitar NC/desconhecido. |
| **Europeana / DPLA** | 24, 17 | metadado/imagem | B | 2 | **CONF** | por asset (rights statements) | Agregadores → licença por item. |

**Lembrete de *hard stops* (1.1):** Seshat (CC BY-NC-SA) → **NÃO** como expressão (fato re-derivável via curadoria); GADM (CC BY-NC) → **NÃO** (usar geoBoundaries); ACLED (comercial) → **NÃO** sem contrato; David Rumsey (scans NC) → **NÃO** (original PD por outro provedor); Deep Time Maps (proprietário) → **NÃO** (usar EarthByte).

---

## 5. Riscos editoriais por camada (Tarefa 5)

Sob a Etapa 3.1. Escala: **baixo / médio / alto / crítico**. Para cada tema: por que é sensível · exige `ClaimSet`? · revisão humana obrigatória? · restrição de mídia? · faixa etária de cuidado · como evitar falsa equivalência.

> "Crítico" = combina **fato sensível documentado + pessoas vivas/identificáveis (LGPD) + alvo ativo de negacionismo/polarização**, exigindo revisão jurídica além da editorial.

| Tema | Risco | Por que é sensível | `ClaimSet`? | Revisão obrigatória? | Restrição de mídia? | Faixa de cuidado | Como evitar falsa equivalência |
|---|---|---|---|---|---|---|---|
| **Colonização** | **Alto** | Conflito de memória; sensibilidade colonial | Sim (interpretações/termos) | **Sim** | Imagens de violência ocultas | 9+ mediação; 12+ termos | Fato do processo ≠ leitura; nomear violência e agência indígena. |
| **Escravidão** | **Alto** | Violência sistêmica; raça | Em causas/escala (fato é fato) | **Sim** | Gráfico oculto; só 15+ c/ aviso | 9+ mediação forte | "Pessoas escravizadas"; sem eufemismo; resistência (quilombos). |
| **Povos indígenas** | **Alto** | Homogeneização; sacralidade; "povos do passado" | Em datação/povoamento (hipóteses) | **Sim** | Consentimento p/ pessoas/rituais | Todas, profundidade crescente | Diversidade (centenas de povos); presente **e** passado (Lei 11.645). |
| **Religiões** | **Alto** | Proselitismo; ridicularização; sacralidade | Conforme | **Sim** | Imagem religiosa sensível revisada | Conforme | Crença como objeto de estudo; sem verdade doutrinária; equidade entre tradições. |
| **Guerras** | **Alto** | Violência; vítimas | Em causas/responsabilidades | **Sim** | Gráfico oculto por padrão | 12+ p/ cenas fortes | Fato ≠ interpretação; sem "excessos dos dois lados" onde há crime. |
| **Genocídios** | **Crítico** | Trauma; **negação de genocídio = negacionismo** | Só interpretações legítimas | **Sim** | Mídia gráfica restrita | 12+ mediação; 15+ pluralidade | Negação **fora** do `ClaimSet`, rotulada `rejeitado`. |
| **Ditaduras** | **Crítico** | Violência de Estado; **pessoas vivas (LGPD)** | Só em interpretações (não sobre repressão documentada) | **Sim** (jurídica + historiográfica) | Propaganda **sempre rotulada** | 12+ mediação; 15+ pluralidade | Repressão/tortura documentadas não são "um lado". |
| **Raça e ciência** | **Crítico** | Risco de racialismo/determinismo | Não (não há "outro lado" para hierarquia) | **Sim, obrigatória** | Iconografia sem "progresso linear" | Todas, com vigilância | Jamais hierarquia entre populações; racismo como objeto, não voz. |
| **Evolução humana** | **Alto** | Cruza raça; mal-entendido de "progresso" | Em ramos/cronologias (hipóteses) | **Sim** (cruzamento raça) | Reconstruções rotuladas | Todas | Evolução é fato; criacionismo é negacionismo, fora do `ClaimSet`. |
| **Mudanças climáticas** | **Alto** | Consenso + alvo de negacionismo + polarização | **Só incerteza interna** (faixas) | **Sim** | Gráficos recriados dos dados | Todas | **Caso-modelo**: consenso × negação **sem equivalência** (§3.4). |
| **Pandemias** | **Alto** | Saúde; trauma recente; conspiração | Modelos/origens (quando em aberto) | **Sim** | Cautela; sem pânico | Conforme; proximidade com saúde | Conspiração ≠ investigação; incerteza sem alimentar boato. |
| **Conflitos contemporâneos** | **Crítico** | Polarização; pessoas vivas; fonte restrita (ACLED) | Conforme (descrição factual) | **Sim** | Cautela máxima | 15–17 sem opinião institucional | Posições com fonte; produto não endossa lado; consenso não relativizado. |

Regra transversal: toda linha marcada como **revisão obrigatória** herda `reviewStatus = pending` e **não é exibível** até aprovação humana (fluxo de §9 da Etapa 3.1).

---

## 6. Incertezas científicas por camada (Tarefa 6)

Para cada: qual é a incerteza · como rotular · entra como `hipótese`, `inferência` ou `reconstrução modelada`? · exige `ClaimSet`? · fontes preferenciais · como aparece no globo/timeline.

| Tema | Qual incerteza | Rótulo | Como entra | `ClaimSet`? | Fontes preferenciais | Globo/timeline |
|---|---|---|---|---|---|---|
| **Primeiros instantes do Universo** | Física pré-inflacionária desconhecida | confiança média/baixa | `hipótese` (inflação) separada do fato (expansão = `inferência`, alta) | Sim (mecanismos) | NASA + cosmologia A/B | âncora 13,8 Ga; nota "em aberto". |
| **Origem da vida** | Mecanismo não decidido | média/baixa | `hipótese` (`hipóteses concorrentes`) | Sim | astrobiologia/PBDB A/B | bloco ~3,5–4 Ga rotulado "em aberto". |
| **Atmosfera primitiva** | Composição mal restringida | média | `inferência científica` (faixa) | Não (faixa interna) | NOAA/NCEI Paleo | `AtmosphereState` com `UncertaintyProfile`. |
| **Paleogeografia antiga** | Posições finas dependem do modelo | alta nas bordas | `reconstrução modelada` (obrigatório) | Não (incerteza no `UncertaintyProfile`) | EarthByte/GPlates | globo rotacionado **rotulado como modelo**. |
| **Rodinia / supercontinentes antigos** | Configuração muito incerta | alta | `reconstrução modelada` + nota forte | Sim onde há reconstruções rivais | EarthByte + literatura | globo com "reconstrução incerta" explícita. |
| **Evolução humana fina** | Ramos/datas em revisão | média/alta | `inferência`/`hipóteses concorrentes` | Sim (ramos) | paleoantropologia A/B | árvore sem progresso linear; nós datados ±. |
| **Povoamento das Américas** | Datas/rotas disputadas | alta | `hipóteses concorrentes` | **Sim** | etno-historiografia/arqueologia | rotas **rotuladas**; cronologias lado a lado. |
| **Causas de extinções** | Atribuição causal (ex.: K-Pg) | média/alta | `hipóteses concorrentes` | **Sim** | PBDB + literatura | evento datado; causas em dossiê comparativo. |
| **Clima profundo** | Reconstrução modelada | alta | `inferência`/`reconstrução` (faixa) | Não (faixa); ≠ negacionismo | NOAA/NCEI/Berkeley | `ClimateState` com faixa de incerteza. |
| **Dados populacionais antigos** | Estimativas sem censo | alta | `estimativa` (nunca `medição`) | Conforme (estimativas rivais) | OWID/literatura demográfica | `PopulationState` com faixa, não número seco. |

Princípio (D7): **a incerteza é mostrada como incerteza** — faixa, ±, `UncertaintyProfile`, rótulo de modelo — e **nunca** convertida em falsa equivalência com negacionismo nem em número de aparência precisa.

---

## 7. Espinha dorsal inicial (Tarefa 7)

Uma **estrutura**, não uma lista exaustiva: os blocos-vértebra que sustentam o eixo Big Bang→presente, com Brasil, África e povos indígenas **em paralelo**. Para cada bloco: por que é estrutural · camadas envolvidas · fontes P0/P1 · tipo de item · riscos editoriais · claims mínimos.

> A espinha é **hipótese de cobertura** (D5: ~150–300 nós / ~1.500–3.000 eventos), não meta de volume. Cada bloco é um **vértebra fina**, povoado primeiro com poucos itens exemplares e seus States, deixando profundidade para P1+.

**1. Big Bang e universo inicial** — *estrutural:* zero absoluto do eixo. *Camadas:* 1. *Fontes:* NASA. *Item:* `Event`/`Process` + Concept. *Risco:* negacionismo (não `ClaimSet`). *Claims:* expansão (inferência, alta) + inflação (hipótese, média).

**2. Estrelas, elementos e galáxias** — *estrutural:* origem da matéria. *Camadas:* 1, 2. *Fontes:* NASA. *Item:* `Process`/`Concept`. *Risco:* baixo. *Claims:* nucleossíntese (inferência).

**3. Sistema Solar** — *estrutural:* âncora ~4,6 Ga. *Camadas:* 2. *Fontes:* NASA/JPL, IAU. *Item:* `Event`/`Entity`. *Risco:* baixo. *Claims:* formação (inferência) + parâmetros (medição).

**4. Terra e Lua** — *estrutural:* início do palco planetário. *Camadas:* 2, 3. *Fontes:* NASA, Macrostrat. *Item:* `Event`/`Process`. *Risco:* baixo. *Claims:* acreção/impacto lunar (inferência/hipótese).

**5. Atmosfera e oceanos** — *estrutural:* condições para a vida. *Camadas:* 4, 7. *Fontes:* NOAA/NCEI. *Item:* `AtmosphereState` inicial + `Region` oceânica. *Risco:* baixo. *Claims:* composição primitiva (inferência, faixa).

**6. Tectônica e supercontinentes** — *estrutural:* o globo muda de forma. *Camadas:* 6, 3. *Fontes:* EarthByte/GPlates. *Item:* `PaleogeographicState`/`PaleogeographicPosition`. *Risco:* baixo (rótulo modelo). *Claims:* reconstrução modelada (incerteza nas bordas).

**7. Vida inicial** — *estrutural:* surge a biosfera. *Camadas:* 8, 4. *Fontes:* PBDB, NOAA Paleo. *Item:* `Process`/`Event` + `BiomeState`. *Risco:* origem da vida = hipótese. *Claims:* primeiros procariontes (inferência) + GOE como transição.

**8. Grandes transições biológicas** — *estrutural:* eucariontes, multicelularidade, terra firme. *Camadas:* 8, 9. *Fontes:* PBDB, OToL. *Item:* `Process`. *Risco:* evolução×criacionismo (negacionismo). *Claims:* transições (inferência).

**9. Extinções em massa** — *estrutural:* marcos de 1ª ordem. *Camadas:* 9. *Fontes:* PBDB. *Item:* `Event`/`Process` + `BiomeState`. *Risco:* causas em `ClaimSet`. *Claims:* extinção (inferência) + causas (hipóteses concorrentes).

**10. Evolução humana** — *estrutural:* origem da linhagem. *Camadas:* 10. *Fontes:* paleoantropologia A/B, PBDB. *Item:* `Process`/`Event`/`Entity`. *Risco:* **alto (raça)** — revisão obrigatória. *Claims:* surgimento (inferência) + ramos (hipóteses).

**11. Migrações humanas** — *estrutural:* ocupação do planeta. *Camadas:* 11, 22. *Fontes:* WHG, arqueologia, IBGE. *Item:* `Process`/`Event` + rotas. *Risco:* povoamento das Américas (hipóteses). *Claims:* dispersões (inferência/hipótese).

**12. Revoluções agrícolas** — *estrutural:* base das civilizações. *Camadas:* 11, 12, 16. *Fontes:* WHG, literatura. *Item:* `Process` + `TechnologyState`. *Risco:* médio (múltiplos centros, não um só). *Claims:* domesticação (inferência) em vários focos.

**13. Primeiras civilizações** — *estrutural:* surgem Estados/cidades. *Camadas:* 12, 13. *Fontes:* Pleiades, WHG. *Item:* `CivilizationState` + `Place`/`Event`. *Risco:* antieurocentrismo (vários berços). *Claims:* fato documentado + interpretação.

**14. Mundo antigo** — *estrutural:* impérios e redes. *Camadas:* 12, 13, 15, 18. *Fontes:* Pleiades, WHG. *Item:* `CivilizationState` + Events. *Risco:* alto (religião, conquista). *Claims:* fato + interpretação (ClaimSet).

**15. Mundo medieval** — *estrutural:* policentrismo global. *Camadas:* 12, 13, 18, 21. *Fontes:* WHG, historiografia. *Item:* `CivilizationState` (incl. reinos africanos). *Risco:* alto (eurocentrismo, religião). *Claims:* fato + interpretação; **África central, não periferia** (Lei 10.639).

**16. Expansões marítimas** — *estrutural:* conexão dos continentes; início colonial. *Camadas:* 12, 13, 19, 20, 21, 22. *Fontes:* WHG, IBGE, IPHAN. *Item:* `Process`/`Event` + `ModernCorrespondence`. *Risco:* **alto** (1492: terminologia sensível). *Claims:* fato + `ClaimSet` ("descobrimento"×"invasão"×"encontro").

**17. Modernidade** — *estrutural:* Estados modernos, ciência, capitalismo. *Camadas:* 13, 14, 15, 16. *Fontes:* OWID, arquivos. *Item:* Events + `EconomicState`. *Risco:* médio. *Claims:* fato + interpretação.

**18. Revoluções políticas e industriais** — *estrutural:* a cena canônica (1789) e a industrialização. *Camadas:* 13, 14, 15, 16, 20. *Fontes:* arquivos, OWID, IBGE. *Item:* `Process`/`Event` + States. *Risco:* alto (violência política; cruza Brasil). *Claims:* fato datado + causas (ClaimSet). *Cena-teste:* Revolução Francesa × Inconfidência × EUA × Lavoisier.

**19. Século XX** — *estrutural:* guerras mundiais, descolonização, ditaduras. *Camadas:* 13, 19, 20, 21, 22, 23. *Fontes:* historiografia, comissões, OWID. *Item:* `Process`/`Event` + ClaimSets. *Risco:* **crítico** (genocídios, ditaduras, pessoas vivas). *Claims:* fato documentado + interpretação; negação = rejeitada.

**20. Mundo contemporâneo** — *estrutural:* borda "agora". *Camadas:* 23, 14, 5. *Fontes:* OWID, World Bank, ONU, IBGE, INPE. *Item:* Events + States modernos. *Risco:* alto/crítico (polarização, pessoas vivas). *Claims:* medição + datado; projeções como faixa.

**21. Brasil e territórios brasileiros — em paralelo** — *estrutural:* lente D8 ao longo de todo o eixo. *Camadas:* 20 (+12,13,14,17,19,22). *Fontes:* IBGE, IPHAN, Arquivo Nacional, BN, CPRM/SGB. *Item:* Events + `ModernCorrespondence` + States regionais. *Risco:* **alto** (colonização, escravidão, indígenas, ditadura). *Claims:* fato + interpretação; revisão obrigatória.

**22. África e diáspora — em paralelo** — *estrutural:* antieurocentrismo (Lei 10.639). *Camadas:* 21 (+12,17,18). *Fontes:* WHG, historiografia afro, acervos. *Item:* `CivilizationState` + `Process`(tráfico) + rotas. *Risco:* **alto** (escravidão, raça). *Claims:* fato + interpretação; agência e resistência.

**23. Povos indígenas das Américas — em paralelo** — *estrutural:* história profunda + presente (Lei 11.645). *Camadas:* 22 (+11,12,17,18). *Fontes:* etno-historiografia, arqueologia, IPHAN, IBGE, fontes indígenas. *Item:* `CivilizationState` + Events + `Entity`(povos). *Risco:* **alto** (homogeneização, sacralidade). *Claims:* fato + hipóteses concorrentes (povoamento); presente e passado.

**Leitura da espinha:** os blocos **1–10** são predominantemente científicos (States e processos de tempo profundo, baixa complexidade jurídica/editorial → arrancada P0 "limpa"); **11–20** são a era humana (núcleo da simultaneidade, editorial-gated); **21–23** são os **três paralelos obrigatórios** que correm ao lado de 11–20 do começo ao fim, não como apêndice.

---

## 8. Regras de povoamento por claim (Tarefa 8)

Todo item, em qualquer camada, nasce com:

- **claim principal** (a afirmação central, com `claimType`);
- **claim temporal** (`TimeRange` no eixo canônico — `DeepTimeAge` ou `CalendarDate` — com precisão e incerteza);
- **claim espacial** quando aplicável (`GeoReference`/`GeometryVersion`/`PaleogeographicPosition`/`ModernCorrespondence`; `SpatialUncertainty` se difuso);
- **fonte A/B** (`Source` + `Citation`) — *claim* sem fonte A/B **não entra** (Etapa 1.1);
- **`confidenceLevel`**, **`evidenceLevel`**, **`uncertaintyProfile`**;
- **`provenanceMetadata`** (cadeia multi-elo quando fato recodificado/derivado);
- **`reviewStatus`**;
- **`relationshipGraph` mínimo** (ao menos uma aresta: `ocorreu-durante`, `localizado-em`, `parte-de`, `predecessor-de` etc.).

**Regras de tipagem (Etapa 3.1):**
- Controvérsia legítima (especialistas divergem com evidência) → **`ClaimSet`** com `consensusStatus`, claims atribuídos e **pesos** (maioria/minoria explicitadas).
- Negacionismo/pseudociência → **nunca** claim concorrente; só objeto rotulado `desinformação/negacionismo rejeitado`, **fora** do `ClaimSet`.
- Consenso → tipado como consenso (`consenso amplo`/`majoritário`), sem "outro lado" forjado.
- Inferência/reconstrução/estimativa → **rótulo obrigatório**; nunca exibidas como `fato documentado` ou `medição`.
- Ausência de evidência → `insuficiência de evidência`; a lacuna é mostrada, não preenchida.

**Estados de maturidade do item** (governam exibição — `reviewStatus` é o portão):

| Estado | Definição | Exibível? |
|---|---|---|
| **incompleto** | falta claim principal, temporal, fonte A/B, ou relação mínima | **Não** |
| **rascunho** | tem o mínimo, mas sem revisão aplicável | **Não** |
| **revisado** | passou pelas revisões de §9 da Etapa 3.1 aplicáveis | ainda não publicado |
| **publicável** | revisado + licença confirmada + `reviewStatus = approved` | **Sim** |
| **bloqueado** | `reviewStatus ∈ {pending, rejected, legal-review}`, ou `ingestionDecision = blocked`, ou licença não confirmada, ou fonte risco 4/5 sem caminho | **Não** (nem na simultaneidade) |

Invariante: **só `publicável` aparece** no globo, na timeline e na simultaneidade. Tudo o mais é invisível ao usuário.

---

## 9. Relação entre camadas (Tarefa 9)

As camadas se conectam pelo **Relationship Graph** (Etapa 2, §6): arestas tipadas; arestas **afirmativas** (causou/influenciou) são elas próprias claims, com fonte e confiança. As conexões estruturais:

| Relação | Tipo de aresta | Como aparece no Relationship Graph |
|---|---|---|
| **atmosfera ↔ vida** | causou/afetou | `AtmosphereState` (GOE) `afetou` evolução; transição com fonte. |
| **tectônica ↔ clima** | influenciou | `PaleogeographicState` `influenciou` `ClimateState` (posição dos continentes → circulação). |
| **clima ↔ migrações** | influenciou/possibilitou | `ClimateState` `influenciou` `Process` migratório (corredores/barreiras). |
| **agricultura ↔ civilizações** | possibilitou | `Process` agrícola `precede`/`possibilitou` `CivilizationState`. |
| **tecnologia ↔ economia** | possibilitou | `TechnologyState` `influenciou` `EconomicState` (industrialização). |
| **religião ↔ cultura** | parte-de/influenciou | `CulturalState` ⊃ sistemas simbólicos; `influenciou` produção cultural. |
| **guerras ↔ política** | causou/decorreu-de | `Event` bélico `causou`/`decorreu-de` mudança em `CivilizationState`. |
| **Brasil ↔ África ↔ Europa ↔ povos indígenas** | conectou/contemporâneo-de | rotas (`Relationship`) + `contemporâneo-de` (simultaneidade) + `ModernCorrespondence`. |
| **ciência ↔ tecnologia** | possibilitou/aplicou | `Concept` científico `instanciado` por `Event`; aplicado em `TechnologyState`. |
| **industrialização ↔ clima moderno** | causou | `Process`(industrialização) `causou` mudança em `ClimateState` (antrópico, consenso). |

**Princípios de uso do grafo na Etapa 4:**
- Arestas de **causa** exigem fonte e confiança próprias (são claims) — nunca implícitas.
- **Simultaneidade** usa `contemporâneo-de` + interseção de `TimeRange`/`GeoReference`; é o que liga os três paralelos (Brasil/África/indígenas) à cena europeia.
- Relações **transversais** (atmosfera↔vida, tectônica↔clima) ancoram a "profundidade de cena" dos States no tempo profundo.
- O grafo mínimo de cada item (ao menos uma aresta) cresce por curadoria, **não** por inferência automática de IA (A3/Q5: IA não cria claims nem relações).

---

## 10. Erros a evitar na Etapa 4 (Tarefa 10)

1. **Tentar ser exaustivo cedo demais.** A espinha é cobertura estrutural fina (D5), não enciclopédia. Povoar largura antes de profundidade.
2. **Copiar texto de fontes.** Ingerir **fato recodificado**, nunca a expressão (Etapa 1.1). Descrições são próprias e didáticas, não transcrição.
3. **Ingerir expressões NC.** Seshat, GADM, gráfico do ICS, scans do David Rumsey, ACLED, Deep Time Maps → **fora** como expressão (só fato re-derivável de fonte livre).
4. **Usar Wikidata como autoridade.** Wikidata/VIAF/Wikipedia/IA são **índice** (INDX); jamais origem de claim.
5. **Tratar mídia como evidência.** `MediaAsset` carrega `natureLabel`; ilustra, não prova. Reconstrução nunca é "fotografia".
6. **Confundir consenso e hipótese.** Tipar cada um (`consenso amplo` × `hipótese`); separar fato consolidado de mecanismo/projeção em aberto.
7. **Criar falsa equivalência.** Negacionismo **fora** do `ClaimSet`; consenso não relativizado por polarização; sem "dois lados" onde há crime documentado.
8. **Popular eventos sem claim principal.** Item sem afirmação central tipada é `incompleto` → não entra.
9. **Popular eventos sem tempo/espaço.** Sem `TimeRange` (e `GeoReference` quando aplicável) o item não existe para a simultaneidade nem para o globo.
10. **Ignorar Brasil/África/povos indígenas.** Os três paralelos são **cobertura estrutural** (Leis 10.639/11.645), não apêndice; correm ao lado da cena europeia do início ao fim.
11. **Reduzir história a política europeia.** Eurocentrismo é falha de projeto; a simultaneidade global é o antídoto (D8).
12. **Criar visualizações sem fonte.** Nada renderiza no globo/timeline sem `Source` A/B e `reviewStatus = approved` (invariante de exibição).
13. **(adicional) Inventar precisão.** Estimativa não vira `medição`; população antiga entra como faixa, não número seco.
14. **(adicional) Resolver controvérsia editorialmente.** O produto **estrutura** o debate (`ClaimSet`), não escolhe vencedor em controvérsia legítima.
15. **(adicional) Pular revisão obrigatória.** Temas sensíveis nascem `pending`; "pronto" exige as revisões de §9 da Etapa 3.1 aprovadas.

---

## 11. Próximos passos para a Etapa 4B (Tarefa 11)

A Etapa 4A entregou a **arquitetura conceitual** das camadas. A **Etapa 4B** deve dar o primeiro passo de **povoamento real controlado**, sem ainda buscar volume. Exatamente:

1. **Povoar a espinha dorsal "limpa" (blocos 1–10), em profundidade mínima.** Criar os itens-vértebra de tempo profundo (Universo → evolução humana) com claim principal + temporal + espacial (quando aplicável) + fonte A/B + States associados (`AtmosphereState`, `PaleogeographicState`, `BiomeState`...), todos rotulados (`inferência`/`reconstrução`/`hipótese`). Meta: a cena de tempo profundo navegável, não exaustiva — **poucos itens exemplares por bloco**.

2. **Instanciar a cena canônica (bloco 18) como teste-padrão.** Povoar 1789 com Revolução Francesa, Inconfidência Mineira (via `ModernCorrespondence` → Minas Gerais), primeiro governo dos EUA e Lavoisier — provando a função "o que acontecia no mundo neste momento?" ponta-a-ponta, com `contemporâneo-de` e fontes A/B.

3. **Subir os três paralelos (blocos 21–23) já na primeira leva**, não depois — ao menos um item estrutural de Brasil, África e povos indígenas em simultaneidade com 18, para que a cobertura das Leis 10.639/11.645 nasça junto, não como remendo.

4. **Aplicar o fluxo de revisão (§9 da Etapa 3.1) a todo item sensível** desde o primeiro: itens de colonização/escravidão/indígenas/ditadura entram `pending` e só viram `publicável` após revisão. A 4B **exercita** o portão, não o adia.

5. **Definir e validar os vocabulários controlados finais** (`claimType`, `eventKind`, `regionKind`, `natureLabel`, `relationType`, `consensusStatus`) confrontando-os com os itens reais povoados — refinamento que a Etapa 2 (item 11.6) deixou para as Etapas 3–4.

6. **Sinalizar à modelagem as lacunas estruturais encontradas** (sem resolvê-las na 4B): por exemplo, se a camada **Oceanos** exige um `OceanographicState` dedicado, ou se a precisão do datum do eixo (1950 BP × J2000) precisa ser fechada — encaminhar como decisão de remodelagem/Etapa 3, não improvisar.

7. **Produzir um lote-piloto auditável**: um conjunto pequeno (ordem de dezenas, não milhares) de itens completos cobrindo um bloco científico (ex.: extinções) e um bloco humano (ex.: 1789 + paralelos), com proveniência, tipagem e revisão completas — o **gabarito de qualidade** que rege o povoamento em massa posterior (Etapa 4C+ / pipeline na Etapa 13).

**O que a 4B explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP ou stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar o pipeline técnico de ingestão; reabrir a auditoria de fontes (Etapas 1/1.1) ou a política editorial (Etapa 3.1). A 4B é o **primeiro povoamento controlado e auditável**, sob esta arquitetura e aquela política.

---

*Documento de entrega da Etapa 4A, sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3 e a política editorial vinculante da Etapa 3.1. Define a arquitetura conceitual das camadas; não popula milhares de eventos, não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula e não desenha o pipeline técnico completo de ingestão. Próxima etapa, quando solicitada: Etapa 4B — primeiro povoamento controlado e auditável da espinha dorsal e da cena canônica, com os três paralelos (Brasil/África/povos indígenas) e o fluxo de revisão obrigatória já em operação.*
