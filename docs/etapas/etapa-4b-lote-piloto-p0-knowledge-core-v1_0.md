# Etapa 4B — Lote-Piloto P0 da Espinha Dorsal do Knowledge Core

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4B · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1 e a arquitetura de camadas da Etapa 4A · 12/06/2026
**Escopo:** primeiro **lote-piloto controlado e auditável** de povoamento do KC — um conjunto **pequeno, exemplar e rastreável** (não exaustivo) que demonstra o *padrão* de povoamento. Conforme solicitado, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico completo, **não** popula milhares de eventos, **não** copia texto de fontes, **não** usa Wikidata/Wikipedia como autoridade e **não** usa mídia como evidência factual.

**O objetivo não é quantidade — é padrão.** Cada item demonstra como o KC estrutura claims, liga fontes, exibe incerteza, separa fato/interpretação/hipótese/reconstrução, evita falsa equivalência e faz Brasil/África/povos indígenas nascerem **junto** com a espinha.

> **Marcas de pendência** (usadas quando um dado ainda não pode ser confirmado — *não se inventa precisão*): `PENDENTE_CONFIRMACAO_FONTE` · `PENDENTE_REVISAO_HUMANA` · `PENDENTE_REFINAMENTO_TEMPORAL` · `PENDENTE_REFINAMENTO_ESPACIAL` · `PENDENTE_LICENCA` · `PENDENTE_CLAIMSET`.

---

## Sumário

1. Template do item-piloto (Tarefa 1)
2. Lote científico "limpo" — blocos 1–10 (Tarefa 2)
3. Lote humano/histórico — blocos 11–20 (Tarefa 3)
4. Os três paralelos obrigatórios — Brasil, África/diáspora, povos indígenas (Tarefa 4)
5. Cena canônica de 1789 (Tarefa 5)
6. Exemplos de ClaimSet (Tarefa 6)
7. Validação do vocabulário controlado (Tarefa 7)
8. Relationship graph mínimo (Tarefa 8)
9. Relatório de qualidade do lote (Tarefa 9)
10. Próximos passos para a Etapa 4C (Tarefa 10)

---

## 1. Template do item-piloto (Tarefa 1)

O item-piloto é **textual, não código**. Cada campo deriva diretamente das etapas anteriores:

| Campo | Deriva de | O que registra |
|---|---|---|
| `id` | Etapa 2 (`knowledgeItemId` estável/versionado) | identificador permanente com prefixo de tipo (`evt:`/`proc:`/`state:`/`concept:`/`entity:`/`place:`/`region:`). |
| `tipo` | Etapa 2 (`itemType`) | `Event` / `Process` / `Concept` / `Entity` / `Place` / `Region` / `State`. |
| `camadaP` / `camadasS` | Etapa 4A (25 camadas) | camada principal + secundárias. |
| `título` | Etapa 2 (`preferredLabel`) | rótulo legível. |
| `desc` | Etapa 2 (`shortDescription`, **não é claim**) | descrição didática própria (jamais copiada de fonte). |
| `TimeRange` | Etapa 2 §4 (eixo canônico Ga↔dia; `DeepTimeAge`/`CalendarDate`) | intervalo no eixo único, com ±. |
| `TimePrecision` | Etapa 2 (`TimePrecision`) | granularidade (ver §7 para o vocabulário proposto). |
| `Place/Region` | Etapa 2 §5 (`GeometryVersion`/`PaleogeographicPosition`/`ModernCorrespondence`/`SpatialUncertainty`) | espaço, quando aplicável. |
| `ClaimPrinc` | Etapa 2 §3 + 3.1 (`claimType`) | afirmação central tipada. |
| `ClaimTemp` | Etapa 2 §4 | afirmação temporal tipada. |
| `ClaimEsp` | Etapa 2 §5 | afirmação espacial tipada (quando aplicável). |
| `Source A/B (tier, status)` | Etapa 1/1.1 (`sourceTier` A/B/C; `ingestionDecision`) | fonte + nível + decisão de ingestão; índice (C) nunca sustenta claim. |
| `conf` | Etapa 2 (`ConfidenceLevel`) | `alta`/`média`/`baixa`/`contestada` + base. |
| `evid` | Etapa 2 (`EvidenceLevel`) | natureza da evidência (ortogonal à confiança). |
| `uncert` | Etapa 2 (`UncertaintyProfile`) | incerteza temporal/espacial/magnitude/interpretativa + `modelDependence`. |
| `review` | Etapa 1.1 + 3.1 (`reviewStatus`) | `pending`/`approved`/`legal-review`/`rejected`; só `approved` é exibível. |
| `riscoEd` | Etapa 3.1 + 4A §5 | risco editorial (baixo→crítico) e por quê. |
| `riscoLic` | Etapa 1.1 + 4A §4 (`licenseRiskLevel` 0–5) | risco de licença. |
| `rel[]` | Etapa 2 §6 (`Relationship`) | grafo mínimo (≥1 aresta tipada). |
| `timeline` | Etapa 3 / 4A | se e como aparece na timeline. |
| `globe` | Etapa 3 / 4A | se e como aparece no globo/mapa. |
| `simultaneidade` | Etapa 0 (D4/A6) + 4A | se aparece na função "o que acontecia no mundo neste momento?" + observação. |
| `notes` | — | observações de curadoria/pendências. |

**Invariante herdado (Etapa 1.1/3.1):** todo item nasce com `ProvenanceMetadata` + `claimType` + `confidenceLevel` + `reviewStatus`; item com `reviewStatus ∈ {pending, rejected, legal-review}` **não é exibível** nem entra na simultaneidade. Os estados de maturidade (Etapa 4A §8): `incompleto → rascunho → revisado → publicável → bloqueado`.

> Nos itens abaixo, campos óbvios ou repetitivos são abreviados; campos sensíveis (editorial, ClaimSet, simultaneidade) são detalhados. Onde um valor não pode ser fixado, usa-se uma marca `PENDENTE_*`.

---

## 2. Lote científico "limpo" — blocos 1–10 (Tarefa 2)

Editorialmente de baixo risco (exceto onde cruza negacionismo). Regra da Etapa 3.1 aplicada: Big Bang, evolução, idade da Terra e origem da vida entram como **consenso tipado como consenso** ou **hipótese tipada como hipótese**; negacionismo **fora** do ClaimSet; incerteza interna separada do fato consolidado.

---

**SCI-01 · `evt:big-bang`**
- tipo: `Event`/`Process` · camadaP: 1 Universo · camadasS: 25
- título: Big Bang · desc: início da expansão do universo observável a partir de um estado quente e denso.
- TimeRange: ~13,8 Ga (±~0,02 Ga) · TimePrecision: `Ga` · Place/Region: `sem-localização` (o espaço-tempo origina-se aqui).
- ClaimPrinc: "O universo observável iniciou expansão há ~13,8 Ga" — `inferência científica`.
- ClaimTemp: idade ~13,8 Ga ± 0,02 — `inferência científica`. · ClaimEsp: N/A (`sem-localização`).
- Source: NASA (A, PD, AUTO); cosmologia revisada (A/B) · conf: **alta** (base: consenso + CMB) · evid: `dado modelado` + observação (CMB) · uncert: modelDependence=parcial; primeiros instantes em aberto (ver SCI-claim separado).
- review: `approved` (consenso) · riscoEd: **baixo-médio** — Big Bang × criacionismo/terraplanismo é **negacionismo**, fora de ClaimSet · riscoLic: 0.
- rel[]: `predecessor-de` SCI-05; `relacionado-a` `concept:expansao-universo`.
- timeline: **zero absoluto** do eixo · globe: vista de cosmos, sem globo · simultaneidade: âncora inicial ("há 13,8 Ga" retorna isto + ausência de States planetários).
- notes: a inflação cósmica entra como **claim separado** (`hipótese`, conf média), nunca fundida ao fato da expansão.

**SCI-02 · `evt:recombinacao-cmb`**
- tipo: `Event` · camadaP: 1 · camadasS: 25
- título: Recombinação / radiação cósmica de fundo · desc: o universo torna-se transparente; libera-se a radiação que hoje observamos como CMB.
- TimeRange: ~380 mil anos após o Big Bang (~13,8 Ga) · TimePrecision: `ka`(relativo) · Place/Region: global cósmico.
- ClaimPrinc: "A CMB foi emitida na recombinação, ~380 ka após o Big Bang" — `inferência científica`.
- ClaimTemp: ~380 ka pós-BB — `inferência`. · ClaimEsp: N/A.
- Source: NASA (A, PD, AUTO); cosmologia (A/B) · conf: **alta** · evid: `medição instrumental` (mapas de CMB) + `dado modelado` · uncert: baixa.
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `ocorreu-durante` universo inicial; `evidenciado-por` observações de CMB; `sucessor-de` SCI-01.
- timeline: bloco do universo inicial · globe: vista de cosmos · simultaneidade: pano de fundo cósmico.
- notes: a CMB é a **evidência observacional** central do Big Bang — útil para ensinar "como sabemos".

**SCI-03 · `proc:primeiras-estrelas`**
- tipo: `Process` · camadaP: 1 · camadasS: 2, 25
- título: Primeiras estrelas (População III) · desc: formação das primeiras estrelas, encerrando a "idade das trevas" cósmica.
- TimeRange: ~13,5–13,2 Ga `PENDENTE_REFINAMENTO_TEMPORAL` (faixa) · TimePrecision: `Ga`(faixa) · Place/Region: global cósmico.
- ClaimPrinc: "As primeiras estrelas se formaram algumas centenas de Ma após o Big Bang" — `inferência científica`.
- ClaimTemp: faixa ~13,5–13,2 Ga — `inferência` (faixa) · ClaimEsp: N/A.
- Source: NASA (A, PD, AUTO); astrofísica (A/B) · conf: **média-alta** · evid: `dado modelado` + observação indireta · uncert: faixa ampla; modelDependence=alto.
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `possibilitou` SCI-04; `ocorreu-durante` universo inicial.
- timeline: bloco "estrelas, elementos e galáxias" · globe: cosmos · simultaneidade: pano de fundo.
- notes: datação observacional ainda em refinamento — manter faixa, não número seco.

**SCI-04 · `proc:nucleossintese-estelar`**
- tipo: `Process` · camadaP: 1 · camadasS: 2, 25
- título: Formação de elementos pesados · desc: forja de elementos químicos em estrelas e supernovas, enriquecendo o meio interestelar.
- TimeRange: contínuo a partir de ~13,5 Ga · TimePrecision: `Ga`(processo contínuo) · Place/Region: global cósmico.
- ClaimPrinc: "Os elementos mais pesados que H/He formam-se em estrelas e supernovas" — `inferência científica` (consenso).
- ClaimTemp: contínuo desde as 1ªs estrelas — `inferência` · ClaimEsp: N/A.
- Source: NASA (A, PD, AUTO); astrofísica nuclear (A/B) · conf: **alta** · evid: `medição instrumental` (espectroscopia) + `dado modelado` · uncert: baixa no princípio.
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `possibilitou` SCI-05 e SCI-06 (matéria planetária); `decorreu-de` SCI-03.
- timeline: bloco "estrelas, elementos e galáxias" · globe: cosmos · simultaneidade: pano de fundo (origem da matéria dos planetas).
- notes: liga "somos poeira de estrelas" à camada química — alto valor didático.

**SCI-05 · `proc:formacao-sistema-solar`**
- tipo: `Process`/`Event` · camadaP: 2 Sistema Solar · camadasS: 1, 25
- título: Formação do Sistema Solar · desc: colapso de uma nuvem molecular forma o Sol e o disco que origina os planetas.
- TimeRange: ~4,57 Ga (±~0,001) · TimePrecision: `Ga` · Place/Region: Sistema Solar.
- ClaimPrinc: "O Sistema Solar formou-se há ~4,57 Ga a partir de um disco protoplanetário" — `inferência científica`.
- ClaimTemp: ~4,57 Ga — `inferência` (datação radiométrica de meteoritos) · ClaimEsp: Sistema Solar.
- Source: NASA/JPL (A, PD, AUTO) · conf: **alta** · evid: `medição instrumental` (meteoritos) + `dado modelado` · uncert: baixa.
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `predecessor-de` SCI-06; `parte-de` Via Láctea; `sucessor-de` SCI-04.
- timeline: âncora ~4,6 Ga · globe: vista do Sistema Solar · simultaneidade: "há 4,6 Ga" troca a cena para formação planetária.
- notes: datação por meteoritos é a mais firme do tempo profundo — bom caso de `medição`.

**SCI-06 · `evt:formacao-terra`**
- tipo: `Event`/`Process` · camadaP: 3 Terra geológica · camadasS: 2, 25
- título: Formação da Terra · desc: acreção da Terra a partir do disco protoplanetário.
- TimeRange: ~4,54 Ga (±~0,05) · TimePrecision: `Ga` · Place/Region: Terra (proto).
- ClaimPrinc: "A Terra formou-se por acreção há ~4,54 Ga" — `inferência científica`.
- ClaimTemp: ~4,54 Ga — `inferência` (radiometria) · ClaimEsp: corpo terrestre.
- Source: NASA (A, PD, AUTO); Macrostrat (B, CC BY, ATRIB para a régua) · conf: **alta** · evid: `medição instrumental` + `dado modelado` · uncert: baixa.
- review: `approved` · riscoEd: **baixo-médio** — idade da Terra × jovem-terrismo é **negacionismo**, fora de ClaimSet · riscoLic: 0/1.
- rel[]: `predecessor-de` SCI-07, SCI-08; `parte-de` SCI-05.
- timeline: início do palco planetário (~4,54 Ga) · globe: surge o globo (Hadeano) · simultaneidade: pano de fundo planetário.
- notes: a idade da Terra é **fato consolidado**; entra como consenso, não como "uma teoria".

**SCI-07 · `evt:formacao-lua`**
- tipo: `Event` · camadaP: 2 Sistema Solar · camadasS: 3, 25
- título: Formação da Lua (impacto gigante) · desc: colisão de um corpo do tamanho de Marte com a proto-Terra forma a Lua.
- TimeRange: ~4,51 Ga `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `Ga` · Place/Region: sistema Terra-Lua.
- ClaimPrinc: "A Lua formou-se de um impacto gigante na proto-Terra" — `inferência científica` (hipótese dominante).
- ClaimTemp: ~4,51 Ga — `inferência` · ClaimEsp: órbita terrestre.
- Source: NASA (A, PD, AUTO); ciência lunar (A/B) · conf: **média-alta** (hipótese dominante; detalhes em aberto) · evid: `dado modelado` + amostras Apollo · uncert: interpretativa (variantes do modelo de impacto).
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `relacionado-a` SCI-06; `evidenciado-por` amostras lunares (Apollo, cf. HIST-19).
- timeline: bloco "Terra e Lua" · globe: sistema Terra-Lua · simultaneidade: pano de fundo.
- notes: variantes (impactor único × múltiplos) → se virarem peso real, `PENDENTE_CLAIMSET`.

**SCI-08 · `proc:diferenciacao-terra`**
- tipo: `Process` · camadaP: 3 Terra geológica · camadasS: 6, 25
- título: Diferenciação da Terra · desc: separação em núcleo, manto e crosta por densidade.
- TimeRange: ~4,5–4,4 Ga · TimePrecision: `Ga`(faixa) · Place/Region: Terra.
- ClaimPrinc: "A Terra diferenciou-se em núcleo/manto/crosta no Hadeano" — `inferência científica`.
- ClaimTemp: ~4,5–4,4 Ga — `inferência` · ClaimEsp: corpo terrestre.
- Source: Macrostrat (B, CC BY, ATRIB); geofísica (A/B) · conf: **alta** · evid: `dado modelado` + geoquímica · uncert: média (cronologia fina).
- review: `approved` · riscoEd: baixo · riscoLic: 0/1.
- rel[]: `possibilitou` campo magnético e tectônica (SCI-19); `ocorreu-durante` Hadeano.
- timeline: bloco "Terra e Lua" · globe: estrutura interna (overlay) · simultaneidade: pano de fundo.
- notes: base para atmosfera (SCI-09) e tectônica (camada 6).

**SCI-09 · `state:atmosfera-primitiva`** *(AtmosphereState)*
- tipo: `State` · camadaP: 4 Atmosfera · camadasS: 7, 25
- título: Atmosfera primitiva · desc: atmosfera anóxica (sem O₂ livre) do Hadeano/Arqueano.
- TimeRange: ~4,4–2,4 Ga · TimePrecision: `Ga`(intervalo) · Place/Region: global.
- ClaimPrinc: "A atmosfera primitiva era essencialmente anóxica" — `inferência científica` (faixa de composição).
- ClaimTemp: ~4,4–2,4 Ga — `inferência` · ClaimEsp: global — `inferência`.
- Source: NOAA/NCEI Paleo (A, PD, AUTO); geoquímica (A/B) · conf: **média-alta** (anóxia consensual; composição fina incerta) · evid: `inferência indireta` (registro geoquímico) · uncert: magnitude (proporções) em faixa; modelDependence=alto.
- review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `transicionou-para` pós-GOE (SCI-13); `relacionado-a` SCI-10.
- timeline: bloco "atmosfera e oceanos" · globe: overlay atmosférico (Arqueano) · simultaneidade: pano de fundo de cenas profundas.
- notes: composição exata = faixa, **nunca** número seco; é `State`, não evento.

**SCI-10 · `evt:formacao-oceanos`**
- tipo: `Event`/`Process` · camadaP: 7 Oceanos · camadasS: 4, 25
- título: Formação dos oceanos · desc: condensação de água líquida na superfície terrestre.
- TimeRange: ~4,4 Ga `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `Ga` · Place/Region: global.
- ClaimPrinc: "Oceanos de água líquida existiam por volta de ~4,4 Ga" — `inferência científica`.
- ClaimTemp: ~4,4 Ga — `inferência` (zircões de Jack Hills) · ClaimEsp: global.
- Source: Macrostrat/geologia (B/A, ATRIB); literatura (A/B) · conf: **média** (evidência indireta) · evid: `inferência indireta` (zircões) · uncert: alta (cronologia); modelDependence=médio.
- review: `approved` · riscoEd: baixo · riscoLic: 0/1.
- rel[]: `possibilitou` SCI-11 (origem da vida); `relacionado-a` SCI-09.
- timeline: bloco "atmosfera e oceanos" · globe: massas d'água (Hadeano tardio) · simultaneidade: pano de fundo.
- notes: **camada Oceanos sem State próprio** — servida por Paleogeo/Climate/Biome; ver §10/lacuna de modelagem.

**SCI-11 · `evt:origem-vida`**
- tipo: `Event`/`Process` · camadaP: 8 Vida e evolução · camadasS: 7, 25
- título: Origem da vida · desc: surgimento das primeiras formas de vida; mecanismo **em aberto**.
- TimeRange: ~3,7–4,0+ Ga (faixa) · TimePrecision: `Ga`(faixa) · Place/Region: global (ambiente preciso incerto).
- ClaimPrinc: "A vida surgiu na Terra há ao menos ~3,7 Ga" — `inferência científica` (existência); **mecanismo** = `hipótese` (ClaimSet CS-03).
- ClaimTemp: ≥~3,7 Ga — `inferência` · ClaimEsp: `sem-localização-precisa` (fontes hidrotermais × poças × outros).
- Source: PBDB/astrobiologia (A/B) · conf: **alta** (que surgiu cedo) / **baixa-média** (como) · evid: `inferência indireta` (registro isotópico/microfóssil) · uncert: interpretativa alta; **ver CS-03**.
- review: `approved` (existência); mecanismo via `PENDENTE_CLAIMSET` → CS-03 · riscoEd: baixo-médio · riscoLic: 0/1.
- rel[]: `possibilitou` SCI-12; `hipótese-concorrente` interna (CS-03).
- timeline: bloco "vida inicial" — rótulo "em aberto" no mecanismo · globe: overlay de biosfera incipiente · simultaneidade: pano de fundo biótico.
- notes: **separar o fato (vida cedo) da hipótese (como)** — caso-modelo de honestidade epistêmica.

**SCI-12 · `proc:fotossintese-oxigenica`**
- tipo: `Process` · camadaP: 8 Vida e evolução · camadasS: 4, 25
- título: Fotossíntese oxigênica · desc: cianobactérias passam a produzir O₂, precondição do GOE.
- TimeRange: estabelecida por ~2,7–3,0 Ga `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `Ga`(faixa) · Place/Region: global (oceanos rasos).
- ClaimPrinc: "A fotossíntese oxigênica evoluiu antes do GOE" — `inferência científica`.
- ClaimTemp: ~2,7–3,0 Ga (debatido) — `inferência` · ClaimEsp: ambientes marinhos rasos.
- Source: PBDB (A, CC BY, ATRIB); NOAA Paleo (A, PD) · conf: **média-alta** (timing debatido) · evid: `inferência indireta` (biomarcadores/registro) · uncert: timing em faixa.
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: **`causou` SCI-13 (GOE)** — aresta afirmativa com fonte; `parte-de` evolução microbiana.
- timeline: bloco "vida inicial" · globe: overlay biótico · simultaneidade: pano de fundo.
- notes: aresta `causou`→GOE é exemplo obrigatório do grafo (§8).

**SCI-13 · `proc:goe`**
- tipo: `Process` · camadaP: 4 Atmosfera · camadasS: 8, 7, 25
- título: Grande Evento de Oxidação (GOE) · desc: subida significativa do O₂ atmosférico.
- TimeRange: ~2,4–2,0 Ga · TimePrecision: `Ga`(processo) · Place/Region: global.
- ClaimPrinc: "O O₂ atmosférico subiu significativamente a partir de ~2,4 Ga" — `inferência científica` (conf alta).
- ClaimTemp: ~2,4–2,0 Ga — `inferência` · ClaimEsp: global.
- Source: NOAA/NCEI Paleo (A, PD, AUTO); PBDB (A, CC BY) · conf: **alta** (subida); **média-alta** (atribuição causal fina) · evid: `inferência indireta` (registro geoquímico) · uncert: causal fina em aberto.
- review: `approved` · riscoEd: baixo · riscoLic: 0/1.
- rel[]: `decorreu-de` SCI-12; **`afetou` evolução da vida**; `transicionou` AtmosphereState (pré→pós).
- timeline: marco de 1ª ordem (atmosfera) · globe: troca de overlay atmosférico · simultaneidade: "há 2,4 Ga" → GOE + States, tudo rotulado inferência.
- notes: **caso-teste de honestidade epistêmica** da Etapa 0.

**SCI-14 · `evt:surgimento-eucariontes`**
- tipo: `Event`/`Process` · camadaP: 8 Vida e evolução · camadasS: 9, 25
- título: Surgimento dos eucariontes · desc: células com núcleo, via endossimbiose.
- TimeRange: ~2,1–1,6 Ga `PENDENTE_REFINAMENTO_TEMPORAL` (faixa) · TimePrecision: `Ga`(faixa) · Place/Region: global marinho.
- ClaimPrinc: "Os eucariontes surgiram por endossimbiose no Proterozoico" — `inferência científica`.
- ClaimTemp: faixa ~2,1–1,6 Ga (datação debatida) — `inferência` · ClaimEsp: marinho.
- Source: PBDB (A, CC BY, ATRIB); Open Tree of Life (B, CC0) · conf: **média-alta** (endossimbiose consensual; datas em faixa) · evid: `inferência indireta` (microfósseis/filogenia) · uncert: timing em faixa.
- review: `approved` · riscoEd: baixo · riscoLic: 0/1.
- rel[]: `predecessor-de` SCI-15; `ocorreu-durante` Proterozoico.
- timeline: bloco "grandes transições biológicas" · globe: overlay biótico · simultaneidade: pano de fundo.
- notes: datas em revisão ativa — manter faixa.

**SCI-15 · `proc:multicelularidade`**
- tipo: `Process` · camadaP: 8 Vida e evolução · camadasS: 9, 25
- título: Multicelularidade complexa · desc: surgimento independente de organismos multicelulares complexos.
- TimeRange: ~1,0–0,6 Ga (origens múltiplas) · TimePrecision: `Ga`(faixa) · Place/Region: global marinho.
- ClaimPrinc: "A multicelularidade complexa evoluiu várias vezes, intensificando-se no Neoproterozoico" — `inferência científica`.
- ClaimTemp: ~1,0–0,6 Ga — `inferência` · ClaimEsp: marinho.
- Source: PBDB (A, CC BY, ATRIB) · conf: **média-alta** · evid: `inferência indireta` · uncert: origens múltiplas (não um evento único).
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `predecessor-de` SCI-16; `parte-de` evolução animal.
- timeline: bloco "grandes transições biológicas" · globe: overlay biótico · simultaneidade: pano de fundo.
- notes: enfatizar **origens múltiplas** (não "progresso linear").

**SCI-16 · `state:biota-ediacarana`** *(BiomeState)*
- tipo: `State` · camadaP: 9 Paleobiologia · camadasS: 8, 25
- título: Biota de Ediacara · desc: primeiros ecossistemas de macroorganismos de corpo mole.
- TimeRange: ~635–538,8 Ma · TimePrecision: `Ma`(intervalo, base ICS) · Place/Region: global marinho.
- ClaimPrinc: "A biota ediacarana representa os primeiros macroorganismos complexos" — `inferência científica`.
- ClaimTemp: ~635–538,8 Ma — `inferência` (limites ICS via Macrostrat) · ClaimEsp: marinho.
- Source: PBDB (A, CC BY, ATRIB); Macrostrat/ICS-fato (B/A) · conf: **média-alta** (afinidades de alguns táxons debatidas) · evid: `registro material` (fósseis) · uncert: interpretativa (natureza de táxons).
- review: `approved` · riscoEd: baixo · riscoLic: 0/1.
- rel[]: `predecessor-de` SCI-17; `ocorreu-durante` Ediacarano.
- timeline: bloco "grandes transições" · globe: overlay biótico · simultaneidade: pano de fundo.
- notes: limites temporais ancorados na régua ICS (recodificada) — exemplo de `ChronologicalScale`.

**SCI-17 · `proc:explosao-cambriana`**
- tipo: `Process`/`Event` · camadaP: 9 Paleobiologia · camadasS: 8, 25
- título: Explosão Cambriana · desc: rápida diversificação dos filos animais.
- TimeRange: ~538,8–520 Ma · TimePrecision: `Ma` · Place/Region: global marinho.
- ClaimPrinc: "Os principais filos animais diversificaram-se rapidamente no início do Cambriano" — `inferência científica`.
- ClaimTemp: ~538,8–520 Ma (base Cambriano, ICS) — `inferência` · ClaimEsp: marinho.
- Source: PBDB (A, CC BY, ATRIB); Macrostrat/ICS-fato · conf: **alta** (padrão); **média** (ritmo/causas) · evid: `registro material` (fósseis) · uncert: causas em aberto.
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `sucessor-de` SCI-16; `predecessor-de` SCI-18; `ocorreu-durante` Cambriano.
- timeline: marco de 1ª ordem · globe: overlay biótico · simultaneidade: "há ~520 Ma" → biota cambriana.
- notes: base do Cambriano (538,8 Ma) ancorada na ICS.

**SCI-18 · `proc:colonizacao-terrestre`**
- tipo: `Process` · camadaP: 8 Vida e evolução · camadasS: 9, 25
- título: Colonização do ambiente terrestre · desc: plantas e depois animais ocupam o continente.
- TimeRange: plantas ~470 Ma; animais ~430–360 Ma · TimePrecision: `Ma`(faixas, fases) · Place/Region: continentes (Paleozoico).
- ClaimPrinc: "A vida colonizou o ambiente terrestre no Paleozoico, plantas antes de animais" — `inferência científica`.
- ClaimTemp: fases ~470 / ~430–360 Ma — `inferência` · ClaimEsp: continentes da época (paleo).
- Source: PBDB (A, CC BY, ATRIB) · conf: **média-alta** · evid: `registro material` (fósseis) · uncert: cronologia fina das fases.
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `ocorreu-durante` Paleozoico; `relacionado-a` SCI-19 (paleogeografia).
- timeline: bloco "grandes transições" · globe: overlay biótico sobre paleogeografia · simultaneidade: pano de fundo.
- notes: usar `phases[]` (plantas/animais) — exemplo de processo multifásico.

**SCI-19 · `state:pangeia`** *(PaleogeographicState)*
- tipo: `State` · camadaP: 6 Tectônica/paleogeo · camadasS: 5, 25
- título: Pangeia · desc: supercontinente que reuniu as massas continentais.
- TimeRange: reunido ~335 Ma; fragmentando ~175 Ma · TimePrecision: `Ma`(intervalo) · Place/Region: `PaleogeographicPosition` global (GPlates/EarthByte).
- ClaimPrinc: "Os continentes estiveram reunidos em Pangeia entre ~335 e ~175 Ma" — **`reconstrução modelada`** (rótulo obrigatório).
- ClaimTemp: ~335–175 Ma — `reconstrução modelada` · ClaimEsp: posições por idade — `reconstrução modelada` (incerteza nas posições finas).
- Source: EarthByte/GPlates (A, dados CC BY 3.0, ATRIB) · conf: **alta** (existência) / incerteza explícita nas bordas · evid: `dado modelado` · uncert: modelDependence=**true**; posições finas em faixa.
- review: `approved` (rótulo de modelo obrigatório) · riscoEd: baixo · riscoLic: 1 (EarthByte CC BY; **Deep Time Maps proibido**).
- rel[]: **`relacionado-a` deriva continental/tectônica** (exemplo §8); `predecessor-de` configuração atual; `afetou` clima/biota.
- timeline: bloco "tectônica e supercontinentes" · globe: **troca o globo** para a reconstrução de Pangeia (rotulada) · simultaneidade: "há ~250 Ma" → globo de Pangeia.
- notes: **nunca** apresentado como mapa observado — sempre reconstrução rotulada.

**SCI-20 · `evt:extincao-permiano-triassico`**
- tipo: `Event`/`Process` · camadaP: 9 Paleobiologia · camadasS: 4, 5, 25
- título: Extinção Permiano-Triássico · desc: a maior extinção em massa conhecida ("Great Dying").
- TimeRange: ~251,9 Ma · TimePrecision: `Ma` · Place/Region: global.
- ClaimPrinc: "A extinção P-T (~251,9 Ma) eliminou a maioria das espécies marinhas" — `inferência científica`.
- ClaimTemp: ~251,9 Ma (limite ICS) — `inferência` · ClaimEsp: global.
- Source: PBDB (A, CC BY, ATRIB); Macrostrat/ICS-fato · conf: **alta** (magnitude); causas `hipóteses concorrentes` · evid: `registro material` + `dado modelado` · uncert: causal (vulcanismo siberiano dominante; detalhes em aberto).
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `ocorreu-durante` limite Permiano-Triássico; `afetou` biota global.
- timeline: marco de 1ª ordem · globe: overlay de turnover biótico · simultaneidade: evento global.
- notes: causas podem virar `PENDENTE_CLAIMSET` se múltiplas leituras tiverem peso.

**SCI-21 · `evt:extincao-kpg`**
- tipo: `Event`/`Process` · camadaP: 9 Paleobiologia · camadasS: 6, 25
- título: Extinção K-Pg · desc: extinção que eliminou os dinossauros não-avianos.
- TimeRange: ~66,0 Ma · TimePrecision: `Ma` · Place/Region: global (impacto em Chicxulub, hoje México).
- ClaimPrinc: "A extinção K-Pg (~66 Ma) eliminou os dinossauros não-avianos" — `inferência científica` (fato); **causa** = `hipóteses concorrentes` (CS-04).
- ClaimTemp: ~66,0 Ma (limite ICS) — `inferência` · ClaimEsp: global; impacto localizado (`localização-inferida` Chicxulub).
- Source: PBDB (A, CC BY, ATRIB); Macrostrat/ICS-fato · conf: **alta** (extinção); causa via **CS-04** · evid: `registro material` + `dado modelado` (camada de Ir, cratera) · uncert: causal → ClaimSet.
- review: `approved` (fato); causa `PENDENTE_CLAIMSET` → CS-04 · riscoEd: baixo · riscoLic: 1.
- rel[]: **`causou` extinção de dinossauros não-avianos** (exemplo §8); `hipótese-concorrente` (impacto×vulcanismo, CS-04).
- timeline: marco de 1ª ordem · globe: overlay; ponto de impacto rotulado · simultaneidade: evento global.
- notes: separar **fato (extinção)** de **causa (ClaimSet)** — caso-modelo.

**SCI-22 · `proc:surgimento-homo`**
- tipo: `Process`/`Event` · camadaP: 10 Evolução humana · camadasS: 25
- título: Surgimento do gênero *Homo* · desc: aparecimento das primeiras espécies do gênero *Homo* na África.
- TimeRange: ~2,8–2,3 Ma `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `Ma`(faixa) · Place/Region: África (sítios; `localização-inferida`).
- ClaimPrinc: "O gênero *Homo* surgiu na África há ~2,8–2,3 Ma" — `inferência científica`.
- ClaimTemp: faixa ~2,8–2,3 Ma — `inferência` · ClaimEsp: África (sítios fósseis).
- Source: paleoantropologia revisada (A/B) `PENDENTE_CONFIRMACAO_FONTE` (asset específico) · conf: **média-alta** (ramos finos debatidos) · evid: `registro material` (fósseis) · uncert: ramos/datas em faixa; **ver CS-07**.
- review: **`pending`** — `PENDENTE_REVISAO_HUMANA` (cruzamento raça e ciência) · riscoEd: **alto** (raça) · riscoLic: 1.
- rel[]: `predecessor-de` SCI-23; `hipótese-concorrente` (ramos, CS-07).
- timeline: bloco "evolução humana" · globe: África (sítios) · simultaneidade: pano de fundo.
- notes: **vigilância anti-racista** — jamais hierarquia entre populações; iconografia sem "progresso linear".

**SCI-23 · `evt:surgimento-homo-sapiens`**
- tipo: `Event`/`Process` · camadaP: 10 Evolução humana · camadasS: 11, 25
- título: *Homo sapiens* · desc: surgimento da nossa espécie na África.
- TimeRange: ~300 ka `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `ka`(faixa) · Place/Region: África (origem em mosaico).
- ClaimPrinc: "*Homo sapiens* surgiu na África há ~300 ka" — `inferência científica`.
- ClaimTemp: ~300 ka (Jebel Irhoud e outros) — `inferência` · ClaimEsp: África (origem pan-africana/mosaico).
- Source: paleoantropologia revisada (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média-alta** · evid: `registro material` (fósseis) · uncert: origem em mosaico (não um ponto único).
- review: **`pending`** — `PENDENTE_REVISAO_HUMANA` (raça) · riscoEd: **alto** (raça) · riscoLic: 1.
- rel[]: `sucessor-de` SCI-22; **`predecessor-de` HIST-01 (saída da África)**.
- timeline: bloco "evolução humana" · globe: África · simultaneidade: âncora da pré-história humana.
- notes: **unidade da humanidade** — sem hierarquia; origem africana é consenso.

---

## 3. Lote humano/histórico — blocos 11–20 (Tarefa 3)

Aqui a política da Etapa 3.1 fica ativa: controvérsia legítima → `ClaimSet`; negacionismo → rejeitado, fora do ClaimSet; revisão humana obrigatória nos sensíveis; linguagem não eurocêntrica; Leis 10.639/11.645 como cobertura estrutural.

---

**HIST-01 · `proc:saida-africa`**
- tipo: `Process` · camadaP: 11 Migrações · camadasS: 10, 25
- título: Saída da África / dispersão do *Homo sapiens* · desc: dispersão do *H. sapiens* pelo planeta a partir da África.
- TimeRange: dispersão principal ~70–60 ka (dispersões anteriores debatidas) · TimePrecision: `ka`(faixa) · Place/Region: África → Eurásia → mundo (`reconstrução-modelada`).
- ClaimPrinc: "O *H. sapiens* dispersou-se da África pelo mundo, com pulso principal ~70–60 ka" — `inferência científica`.
- ClaimTemp: faixa ~70–60 ka — `inferência` · ClaimEsp: rotas — `reconstrução modelada`.
- Source: paleoantropologia/genética populacional (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média-alta** (pulso principal); dispersões precoces em debate · evid: `inferência indireta` (genética + fósseis) · uncert: rotas/cronologias em faixa.
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (cruza raça) · riscoEd: médio-alto · riscoLic: 1.
- rel[]: `sucessor-de` SCI-23; `predecessor-de` HIST-02; rotas como `Relationship`.
- timeline: bloco "migrações" · globe: rotas rotuladas (modelo) · simultaneidade: pano de fundo da pré-história humana.
- notes: sem narrativa de "superioridade"; diversidade humana é variação, não hierarquia.

**HIST-02 · `proc:povoamento-americas`** *(também paralelo indígena — IND)*
- tipo: `Process` · camadaP: 22 Povos indígenas/Américas · camadasS: 11, 25
- título: Povoamento das Américas · desc: chegada e dispersão dos primeiros povos nas Américas.
- TimeRange: ~25–15 ka+ (pré-Clóvis debatido) `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `ka`(faixa) · Place/Region: Beríngia → Américas.
- ClaimPrinc: "As Américas foram povoadas por populações vindas da Ásia via Beríngia" — `inferência científica`; **datas/rotas** = `hipóteses concorrentes` (CS-06).
- ClaimTemp: faixa ~25–15 ka+ — `hipóteses concorrentes` · ClaimEsp: Beríngia/costa/interior — `reconstrução modelada`.
- Source: arqueologia/genética (A/B); WHG (B, CC BY, ATRIB/filtrar) `PENDENTE_CONFIRMACAO_FONTE` · conf: **contestada** (cronologia) → **CS-06** · evid: `registro material` + genética · uncert: alta; ClaimSet.
- review: `pending` — `PENDENTE_REVISAO_HUMANA`, `PENDENTE_CLAIMSET` (CS-06) · riscoEd: **alto** (homogeneização; Lei 11.645) · riscoLic: 1–2.
- rel[]: `sucessor-de` HIST-01; `predecessor-de` IND/BR pré-1500; `hipótese-concorrente` (CS-06).
- timeline: **em paralelo** (Américas povoadas cedo) · globe: rotas rotuladas · simultaneidade: antídoto ao eurocentrismo (Américas habitadas há milênios).
- notes: cronologias **lado a lado**, sem veredito; povos como agentes, não "fundo".

**HIST-03 · `proc:revolucao-neolitica`**
- tipo: `Process` · camadaP: 12 Civilizações · camadasS: 11, 16, 25
- título: Revolução Neolítica · desc: domesticação de plantas/animais em **múltiplos centros independentes**.
- TimeRange: ~12–10 ka em diante · TimePrecision: `ka`(faixa, multifásico) · Place/Region: Crescente Fértil, China, Mesoamérica, Andes, Nova Guiné… (múltiplos focos).
- ClaimPrinc: "A agricultura surgiu de forma independente em vários centros mundiais" — `inferência científica`.
- ClaimTemp: ~12–10 ka+ (por centro) — `inferência` · ClaimEsp: múltiplos focos globais.
- Source: WHG (B, CC BY, ATRIB/filtrar); arqueologia (A/B) · conf: **alta** (múltiplos centros) · evid: `registro material` · uncert: cronologia fina por região.
- review: `approved` · riscoEd: médio (**evitar "um só berço"**) · riscoLic: 1.
- rel[]: `possibilitou` HIST-04; `parte-de` transição para civilizações.
- timeline: bloco "revoluções agrícolas" · globe: focos de domesticação (vários continentes) · simultaneidade: pano de fundo global.
- notes: explicitar **policentrismo** — não difusão a partir de um centro europeu/oriental único.

**HIST-04 · `proc:primeiras-cidades`**
- tipo: `Process`/`Event` · camadaP: 12 Civilizações · camadasS: 13, 14, 25
- título: Primeiras cidades · desc: surgimento de assentamentos urbanos (ex.: Uruk).
- TimeRange: ~4º milênio BCE em diante · TimePrecision: `século`/`milênio` · Place/Region: Mesopotâmia (Uruk) e outros.
- ClaimPrinc: "Os primeiros grandes centros urbanos surgiram no 4º milênio BCE" — `fato documentado`/`inferência`.
- ClaimTemp: ~4º mil. BCE — `inferência` · ClaimEsp: Mesopotâmia (`Place`).
- Source: Pleiades (A, CC BY, ATRIB); WHG (B) · conf: **alta** · evid: `registro material` · uncert: baixa-média.
- review: `approved` · riscoEd: baixo-médio (vários centros) · riscoLic: 1.
- rel[]: `sucessor-de` HIST-03; `predecessor-de` HIST-07.
- timeline: bloco "primeiras civilizações" · globe: sítios urbanos · simultaneidade: pano de fundo.
- notes: conectar a Mesopotâmia (HIST-07) e outros focos.

**HIST-05 · `evt:invencao-escrita`**
- tipo: `Event`/`Process` · camadaP: 15 Ciência · camadasS: 12, 17, 25
- título: Invenção da escrita · desc: surgimento de sistemas de escrita (cuneiforme, hieróglifos) de forma independente.
- TimeRange: ~3400–3200 BCE (Mesopotâmia/Egito); independente na China e Mesoamérica · TimePrecision: `século` · Place/Region: Mesopotâmia, Egito (+ outros).
- ClaimPrinc: "A escrita foi inventada de forma independente em diferentes regiões" — `fato documentado`/`inferência`.
- ClaimTemp: ~3400–3200 BCE (e depois alhures) — `inferência` · ClaimEsp: múltiplos focos.
- Source: Pleiades/WHG (A/B, CC BY) · conf: **alta** · evid: `registro material` (tabuletas/inscrições) · uncert: prioridade entre focos.
- review: `approved` · riscoEd: baixo (evitar "só a Mesopotâmia") · riscoLic: 1.
- rel[]: `possibilitou` registro histórico; `parte-de` HIST-07/HIST-06.
- timeline: bloco "primeiras civilizações" · globe: focos · simultaneidade: pano de fundo.
- notes: marca o início da "história registrada" — sem apagar a oralidade.

**HIST-06 · `state:egito-antigo`** *(CivilizationState)*
- tipo: `State` · camadaP: 12 Civilizações · camadasS: 21, 18, 25
- título: Egito Antigo · desc: civilização do vale do Nilo, **africana**.
- TimeRange: ~3100–30 BCE · TimePrecision: `século`(intervalo) · Place/Region: vale do Nilo (`GeometryVersion`).
- ClaimPrinc: "O Egito Antigo foi uma civilização africana do vale do Nilo (~3100–30 BCE)" — `fato documentado`/`interpretação`.
- ClaimTemp: ~3100–30 BCE — `fato documentado` · ClaimEsp: vale do Nilo.
- Source: Pleiades (A, CC BY, ATRIB); WHG; historiografia (A/B) · conf: **alta** · evid: `registro material`+`documental` · uncert: cronologias dinásticas finas.
- review: `approved` (PENDENTE_REVISAO_HUMANA se entrar "raça"/iconografia) · riscoEd: médio (**africanidade do Egito**; Lei 10.639) · riscoLic: 1–2 (mídia por asset).
- rel[]: `contemporâneo-de` HIST-07; `parte-de` mundo antigo.
- timeline: bloco "mundo antigo" · globe: vale do Nilo · simultaneidade: pano de fundo do mundo antigo.
- notes: enquadrar o Egito como **África**, não apêndice do "Oriente Próximo" europeizado.

**HIST-07 · `state:mesopotamia`** *(CivilizationState)*
- tipo: `State` · camadaP: 12 Civilizações · camadasS: 13, 25
- título: Mesopotâmia · desc: civilizações entre os rios Tigre e Eufrates (Suméria, Babilônia, Assíria).
- TimeRange: ~3500 BCE em diante · TimePrecision: `século`(intervalo) · Place/Region: Mesopotâmia.
- ClaimPrinc: "A Mesopotâmia abrigou algumas das primeiras civilizações urbanas e estatais" — `fato documentado`.
- ClaimTemp: ~3500 BCE+ — `fato documentado` · ClaimEsp: bacia Tigre-Eufrates.
- Source: Pleiades (A, CC BY, ATRIB); WHG · conf: **alta** · evid: `registro material`+`documental` · uncert: baixa-média.
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `contemporâneo-de` HIST-06; `predecessor-de` HIST-08.
- timeline: bloco "mundo antigo" · globe: Mesopotâmia · simultaneidade: pano de fundo.
- notes: berço de escrita/direito/cidade — conectar a HIST-04/05.

**HIST-08 · `state:grecia-antiga`** *(CivilizationState)*
- tipo: `State` · camadaP: 12 Civilizações · camadasS: 13, 15, 18, 25
- título: Grécia Antiga · desc: cidades-Estado gregas e sua produção política/filosófica/científica.
- TimeRange: ~800–146 BCE · TimePrecision: `século`(intervalo) · Place/Region: Egeu/Mediterrâneo.
- ClaimPrinc: "As pólis gregas desenvolveram instituições políticas e tradições intelectuais influentes" — `fato documentado`/`interpretação`.
- ClaimTemp: ~800–146 BCE — `fato documentado` · ClaimEsp: mundo egeu.
- Source: Pleiades (A, CC BY, ATRIB); WHG; historiografia · conf: **alta** · evid: `documental`+`material` · uncert: interpretativa (idealizações).
- review: `approved` · riscoEd: médio (**evitar "milagre grego" eurocêntrico**) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` impérios contemporâneos; `influenciou` HIST-09.
- timeline: bloco "mundo antigo" · globe: Egeu · simultaneidade: pano de fundo.
- notes: mostrar trocas com Egito/Pérsia — não isolamento heroico.

**HIST-09 · `state:roma-antiga`** *(CivilizationState)*
- tipo: `State` · camadaP: 13 Política/Estados · camadasS: 12, 19, 25
- título: Roma Antiga · desc: República e Império Romano no Mediterrâneo.
- TimeRange: 753 BCE–476 CE (Ocidente) · TimePrecision: `século`(intervalo) · Place/Region: Mediterrâneo (`GeometryVersion` por época).
- ClaimPrinc: "Roma estruturou um vasto império mediterrânico com instituições duradouras" — `fato documentado`/`interpretação`.
- ClaimTemp: 753 BCE–476 CE — `fato documentado` · ClaimEsp: bacia mediterrânica (fronteira variável).
- Source: Pleiades (A, CC BY, ATRIB); WHG; historiografia · conf: **alta** · evid: `documental`+`material` · uncert: datas de fundação lendárias (rotular).
- review: `approved` · riscoEd: médio (escravidão romana; conquista) · riscoLic: 1–2.
- rel[]: `sucessor-de` HIST-08; `predecessor-de` mundo medieval.
- timeline: bloco "mundo antigo" · globe: império (fronteira por idade) · simultaneidade: pano de fundo.
- notes: fronteira muda no tempo → `GeometryVersion` múltipla.

**HIST-10 · `state:imperio-mali`** *(CivilizationState — também paralelo AFR)*
- tipo: `State` · camadaP: 21 África/diáspora · camadasS: 12, 14, 18, 25
- título: Império do Mali · desc: poderoso império da África Ocidental, centro de comércio e saber (Tombuctu).
- TimeRange: ~1235–1600 CE · TimePrecision: `século`(intervalo) · Place/Region: África Ocidental (Sahel).
- ClaimPrinc: "O Império do Mali foi um centro político, comercial e intelectual da África Ocidental" — `fato documentado`/`interpretação`.
- ClaimTemp: ~1235–1600 CE — `fato documentado` · ClaimEsp: Sahel ocidental.
- Source: WHG (B, CC BY, ATRIB/filtrar); historiografia africana (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (existência/relevância) · evid: `documental`+`material` · uncert: cronologias/extensão.
- review: `approved` (PENDENTE_REVISAO_HUMANA se mídia) · riscoEd: médio (**Lei 10.639: África central**) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` HIST-11; `relacionado-a` rotas transaarianas (AFR).
- timeline: bloco "mundo medieval" — **em paralelo** · globe: Sahel · simultaneidade: África protagonista, não periferia.
- notes: Mansa Musa/Tombuctu como saber e riqueza — antídoto ao eurocentrismo medieval.

**HIST-11 · `state:mundo-islamico-medieval`** *(CivilizationState)*
- tipo: `State`/`Process` · camadaP: 12 Civilizações · camadasS: 15, 18, 25
- título: Mundo islâmico medieval · desc: florescimento científico, filosófico e comercial do mundo islâmico.
- TimeRange: ~7º–13º séc. CE · TimePrecision: `século`(intervalo) · Place/Region: do Magreb à Ásia Central.
- ClaimPrinc: "O mundo islâmico medieval foi centro de ciência, filosofia e comércio" — `fato documentado`/`interpretação`.
- ClaimTemp: ~7º–13º séc. CE — `fato documentado` · ClaimEsp: amplo (multirregional).
- Source: WHG (B, CC BY, ATRIB); historiografia (A/B) · conf: **alta** · evid: `documental` · uncert: interpretativa (periodização).
- review: `approved` · riscoEd: médio (religião; evitar caricatura) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` HIST-10; `influenciou` Revolução Científica (HIST-14) via transmissão.
- timeline: bloco "mundo medieval" · globe: do Magreb à Ásia Central · simultaneidade: pano de fundo global.
- notes: preservação/avanço do saber — ponte à ciência moderna (não "idade das trevas").

**HIST-12 · `proc:expansao-maritima-portuguesa`**
- tipo: `Process` · camadaP: 13 Política/Estados · camadasS: 12, 14, 19, 20, 21, 25
- título: Expansão marítima portuguesa · desc: navegações atlânticas que ligaram continentes e iniciaram o sistema colonial.
- TimeRange: séc. XV–XVI · TimePrecision: `século` · Place/Region: Atlântico, África, Ásia, Américas.
- ClaimPrinc: "A expansão marítima portuguesa conectou continentes e inaugurou redes coloniais" — `fato documentado`/`interpretação`.
- ClaimTemp: séc. XV–XVI — `fato documentado` · ClaimEsp: rotas atlânticas/índicas.
- Source: WHG (B, CC BY, ATRIB); IBGE (Brasil); Arquivo Nacional/BN (A, CONF) · conf: **alta** · evid: `documental` · uncert: interpretativa (natureza do processo).
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (colonização/tráfico) · riscoEd: **alto** (colonial; cruza tráfico AFR e contato IND) · riscoLic: 1–2 (mídia por asset).
- rel[]: `causou` HIST-13, chegada ao Brasil (BR); `relacionado-a` tráfico atlântico (AFR).
- timeline: bloco "expansões marítimas" · globe: rotas · simultaneidade: liga Europa↔África↔Américas↔Ásia.
- notes: nomear o lado colonial/escravista do processo, não só "descobertas".

**HIST-13 · `evt:1492-travessia-colombo`**
- tipo: `Event` · camadaP: 13 Política/Estados · camadasS: 22, 21, 19, 25
- título: 1492 — travessia atlântica de Colombo · desc: a travessia de 1492 e o início do contato sustentado Europa–Américas.
- TimeRange: 1492 (12/10/1492) · TimePrecision: `dia` · Place/Region: Caribe (Américas).
- ClaimPrinc: "Em 1492, a expedição de Colombo iniciou contato sustentado entre Europa e Américas" — `fato documentado`; **terminologia** = `ClaimSet` (CS-02).
- ClaimTemp: 12/10/1492 — `fato documentado` · ClaimEsp: Caribe.
- Source: WHG/historiografia (A/B); fontes ameríndias `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (o fato) · evid: `documental` · uncert: **terminológica** → CS-02.
- review: `pending` — `PENDENTE_REVISAO_HUMANA`, `PENDENTE_CLAIMSET` (CS-02) · riscoEd: **alto** ("descobrimento"×"invasão"×"encontro") · riscoLic: 1–2.
- rel[]: `terminologia-sensível` (CS-02); `causou` contato/violência colonial (IND); `contemporâneo-de` sociedades indígenas já complexas.
- timeline: bloco "expansões marítimas" · globe: Caribe + simultâneos (Américas povoadas, África, Ásia) · simultaneidade: mostra **Américas já habitadas e complexas** em 1492.
- notes: nunca "descoberta de terra vazia"; povos originários presentes e diversos (Lei 11.645).

**HIST-14 · `proc:revolucao-cientifica`**
- tipo: `Process` · camadaP: 15 Ciência · camadasS: 16, 17, 25
- título: Revolução Científica · desc: transformação do conhecimento natural (Copérnico a Newton).
- TimeRange: ~1543–1687 · TimePrecision: `ano`(faixa) · Place/Region: Europa (com raízes islâmicas/asiáticas).
- ClaimPrinc: "Entre os séc. XVI–XVII consolidou-se o método científico moderno" — `fato documentado`/`interpretação`.
- ClaimTemp: ~1543–1687 — `fato documentado` · ClaimEsp: Europa (multi-cidade).
- Source: arquivos/historiografia da ciência (A/B); OWID (marcos) · conf: **alta** · evid: `documental` (obras datadas) · uncert: interpretativa (recorte).
- review: `approved` · riscoEd: médio (evitar eurocentrismo; creditar transmissão islâmica) · riscoLic: 1–2.
- rel[]: **`influenciou` Iluminismo → HIST-15** (exemplo §8); `sucessor-de` HIST-11 (transmissão).
- timeline: bloco "modernidade" · globe: cidades europeias · simultaneidade: pano de fundo científico.
- notes: liga-se à cena de 1789 (Lavoisier) — ciência simultânea à política.

**HIST-15 · `proc:revolucao-francesa`**
- tipo: `Process`/`Event` · camadaP: 13 Política/Estados · camadasS: 19, 15, 25
- título: Revolução Francesa · desc: processo revolucionário que derrubou o Antigo Regime na França.
- TimeRange: 1789–1799 (Queda da Bastilha 14/07/1789) · TimePrecision: `dia`(eventos)/`ano`(processo) · Place/Region: França (Paris).
- ClaimPrinc: "A Revolução Francesa (1789–1799) derrubou o Antigo Regime" — `fato documentado`; **causas** = `ClaimSet` (CS-01).
- ClaimTemp: 1789–1799 — `fato documentado` · ClaimEsp: França (`GeometryVersion` da época).
- Source: Arquivo/BN (A, CONF); historiografia (A/B) · conf: **alta** (fatos datados); causas via **CS-01** · evid: `documental` · uncert: causal → ClaimSet.
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (violência política; ClaimSet) · riscoEd: **alto** (Terror; interpretações) · riscoLic: 1–2.
- rel[]: `sucessor-de` HIST-14 (via Iluminismo); **`contemporâneo-de` HIST-16 (Inconfidência)**; causas `ClaimSet` (CS-01).
- timeline: bloco "revoluções políticas e industriais" · globe: França + simultâneos · simultaneidade: **âncora da cena canônica de 1789** (§5).
- notes: separar **fatos datados (alta confiança)** de **causas (ClaimSet)**.

**HIST-16 · `evt:inconfidencia-mineira`** *(também paralelo BR)*
- tipo: `Event`/`Process` · camadaP: 20 Brasil · camadasS: 13, 19, 25
- título: Inconfidência Mineira · desc: conspiração separatista na Capitania de Minas Gerais (1789).
- TimeRange: 1789 (devassa); Tiradentes executado 1792 · TimePrecision: `ano`/`dia` · Place/Region: Capitania de Minas Gerais → **MG hoje** (`ModernCorrespondence`).
- ClaimPrinc: "A Inconfidência Mineira (1789) foi um movimento separatista na Capitania de Minas" — `fato documentado`.
- ClaimTemp: 1789 (e 1792) — `fato documentado` · ClaimEsp: Capitania de Minas; `ModernCorrespondence` → estado de MG.
- Source: Arquivo Nacional/BN (A, CONF); IBGE (território); historiografia (A/B) · conf: **alta** · evid: `documental` (autos da devassa) · uncert: interpretativa (alcance/significado).
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (Brasil sensível) · riscoEd: médio-alto · riscoLic: 1–2.
- rel[]: **`contemporâneo-de` HIST-15** (1789); `modernCorrespondence` Capitania→MG; `parte-de` Brasil colonial.
- timeline: **em paralelo** a 1789 · globe: Minas (via `ModernCorrespondence`) · simultaneidade: **peça central da cena de 1789** (§5).
- notes: anacronismo evitado — "Brasil" não existia como hoje; a ponte é `ModernCorrespondence`.

**HIST-17 · `proc:revolucao-industrial`**
- tipo: `Process` · camadaP: 16 Tecnologia · camadasS: 14, 5, 23, 25
- título: Revolução Industrial · desc: industrialização baseada em máquinas e combustíveis fósseis.
- TimeRange: ~1760–1840 (e ondas seguintes) · TimePrecision: `ano`(faixa) · Place/Region: Grã-Bretanha → mundo.
- ClaimPrinc: "A Revolução Industrial mecanizou a produção e iniciou o uso massivo de combustíveis fósseis" — `fato documentado`.
- ClaimTemp: ~1760–1840 — `fato documentado` · ClaimEsp: Grã-Bretanha (difusão).
- Source: OWID (B, CC BY, ATRIB); World Bank; historiografia · conf: **alta** · evid: `documental`+`medição` (séries) · uncert: baixa.
- review: `approved` · riscoEd: médio (custos sociais; trabalho) · riscoLic: 1.
- rel[]: **`causou` mudanças climáticas modernas (HIST-21)** (exemplo §8); `decorreu-de` HIST-14.
- timeline: bloco "revoluções políticas e industriais" · globe: difusão industrial · simultaneidade: pano de fundo econômico-técnico.
- notes: ponte direta ao clima antrópico (HIST-21) — relação `causou` com fonte.

**HIST-18 · `evt:abolicao-brasil`** *(também paralelo BR/AFR)*
- tipo: `Event` · camadaP: 20 Brasil · camadasS: 21, 13, 25
- título: Abolição da escravidão no Brasil (Lei Áurea) · desc: fim legal da escravidão no Brasil em 1888.
- TimeRange: 13/05/1888 · TimePrecision: `dia` · Place/Region: Brasil (Império).
- ClaimPrinc: "A Lei Áurea aboliu legalmente a escravidão no Brasil em 13/05/1888" — `fato documentado`.
- ClaimTemp: 13/05/1888 — `fato documentado` · ClaimEsp: Império do Brasil.
- Source: Arquivo Nacional/BN (A, CONF); IBGE; historiografia afro-brasileira (A/B) · conf: **alta** (a data) · evid: `documental` (lei) · uncert: interpretativa (limites/continuidades pós-1888).
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (escravidão/raça) · riscoEd: **alto** (Lei 10.639; agência negra) · riscoLic: 1–2.
- rel[]: `sucessor-de` tráfico atlântico (AFR); `relacionado-a` luta abolicionista e quilombos (AFR).
- timeline: bloco "século XX" (limiar) · globe: Brasil · simultaneidade: pano de fundo atlântico.
- notes: **protagonismo negro** na abolição (não só "ato imperial"); continuidades do racismo pós-1888.

**HIST-19 · `evt:apollo-11`**
- tipo: `Event` · camadaP: 16 Tecnologia · camadasS: 2, 13, 25
- título: Apollo 11 · desc: primeira missão tripulada a pousar na Lua (1969).
- TimeRange: 16–24/07/1969 (pouso 20/07) · TimePrecision: `dia` · Place/Region: Terra→Lua (EUA).
- ClaimPrinc: "Em julho de 1969, a Apollo 11 levou os primeiros humanos à superfície lunar" — `fato documentado`.
- ClaimTemp: 20/07/1969 — `fato documentado` · ClaimEsp: Mar da Tranquilidade (Lua); lançamento EUA.
- Source: NASA (A, PD, AUTO) · conf: **alta** · evid: `documental`+`observação direta` (registros da missão) · uncert: baixa.
- review: `approved` · riscoEd: baixo (negacionismo "pouso falso" = rejeitado, fora de ClaimSet) · riscoLic: 0.
- rel[]: **`decorreu-de` Guerra Fria; `parte-de` tecnologia espacial** (exemplo §8); `relacionado-a` SCI-07 (amostras lunares).
- timeline: bloco "século XX" · globe: Lua + EUA · simultaneidade: pano de fundo tecnológico/geopolítico.
- notes: imagens NASA são PD; "pouso encenado" é negacionismo rotulado, nunca claim concorrente.

**HIST-20 · `evt:criacao-www`**
- tipo: `Event`/`Process` · camadaP: 16 Tecnologia · camadasS: 23, 14, 25
- título: Criação da World Wide Web · desc: proposta (1989) e primeiros sistemas da Web por Tim Berners-Lee no CERN.
- TimeRange: 1989–1991 · TimePrecision: `ano` · Place/Region: CERN (Suíça/França).
- ClaimPrinc: "A World Wide Web foi proposta em 1989 e disponibilizada no início dos anos 1990" — `fato documentado`.
- ClaimTemp: 1989–1991 — `fato documentado` · ClaimEsp: CERN.
- Source: OWID/registros do CERN (A/B) `PENDENTE_CONFIRMACAO_FONTE` (asset) · conf: **alta** · evid: `documental` · uncert: baixa.
- review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `sucessor-de` computação; `relacionado-a` mundo contemporâneo (camada 23).
- timeline: bloco "mundo contemporâneo" · globe: CERN · simultaneidade: ponta contemporânea.
- notes: distinguir **Web** (Berners-Lee) de **Internet** (anterior) — precisão conceitual.

**HIST-21 · `proc:mudancas-climaticas-modernas`** *(+ ClimateState moderno)*
- tipo: `Process`/`State` · camadaP: 5 Clima · camadasS: 23, 16, 25
- título: Mudanças climáticas modernas · desc: aquecimento global de origem **antrópica** desde a era industrial.
- TimeRange: ~1850–presente · TimePrecision: `ano` (séries) · Place/Region: global.
- ClaimPrinc: "O aquecimento global observado desde ~1850 é majoritariamente antrópico" — **`medição`/consenso `amplo`**; projeções = `estimativa` (faixa) — `ClaimSet` interno (CS-05).
- ClaimTemp: ~1850–presente — `medição` · ClaimEsp: global — `medição`.
- Source: NOAA/NCEI, NASA GISS, Berkeley Earth, Copernicus, IPCC (**figuras recriadas**); INPE/MapBiomas (Brasil, **ISOLA**) · conf: **alta** (consenso antrópico) · evid: `medição instrumental` · uncert: **interna** (faixas de projeção) ≠ dúvida do fato.
- review: `pending` — `PENDENTE_REVISAO_HUMANA` (tema-alvo de negacionismo) · riscoEd: **alto** — **consenso × negação SEM equivalência** (§3.4); CS-05 só para incerteza interna · riscoLic: 2–3 (IPCC/Copernicus; MapBiomas SA→isolar).
- rel[]: **`decorreu-de` HIST-17 (Revolução Industrial)** (exemplo §8); `afetou` sistemas naturais/sociais.
- timeline: bloco "mundo contemporâneo" · globe: overlay de temperatura · simultaneidade: ponta contemporânea.
- notes: **caso-modelo de "incerteza sem falsa equivalência"** (PE-Ed5): afirmar o consenso; mostrar projeção como faixa; negação fora do ClaimSet.

---

## 4. Os três paralelos obrigatórios (Tarefa 4)

Brasil, África/diáspora e povos indígenas **nascem junto** com a espinha (Etapa 4A; Leis 10.639/11.645). Itens já criados que pertencem a estes eixos são **reaproveitados por referência** (não duplicados): HIST-02 (povoamento das Américas), HIST-10 (Mali), HIST-13 (1492), HIST-16 (Inconfidência), HIST-18 (abolição). Abaixo, apenas os **itens novos**. Quase todos os sensíveis entram `pending`.

### A. Brasil e territórios que hoje correspondem ao Brasil

**BR-01 · `state:povos-sambaquieiros`** *(CivilizationState)*
- tipo: `State` · camadaP: 20 Brasil · camadasS: 22, 25 · título: Povos sambaquieiros
- desc: populações litorâneas que ergueram sambaquis no litoral do atual Brasil.
- TimeRange: ~8.000–1.000 BP `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `ka`(faixa) · Place/Region: litoral do território hoje brasileiro (`ModernCorrespondence`).
- ClaimPrinc: "Povos sambaquieiros ocuparam o litoral do atual Brasil por milênios" — `inferência científica` (arqueológica).
- ClaimTemp: ~8.000–1.000 BP — `inferência` · ClaimEsp: litoral BR (`localização-inferida`).
- Source: IPHAN (A, CONF); arqueologia (A/B); IBGE (território) · conf: **média-alta** · evid: `registro material` · review: `pending` (`PENDENTE_REVISAO_HUMANA`) · riscoEd: **alto** (Lei 11.645) · riscoLic: 1–2.
- rel[]: `predecessor-de` BR-03; `parte-de` história profunda das Américas (camada 22).
- timeline: **em paralelo** (Brasil profundo) · globe: litoral BR · simultaneidade: Brasil habitado há milênios antes de 1500.
- notes: presença indígena profunda — **não** "terra vazia" antes dos europeus.

**BR-02 · `state:cultura-marajoara`** *(CivilizationState)*
- tipo: `State` · camadaP: 20 Brasil · camadasS: 22, 17, 25 · título: Cultura marajoara
- desc: sociedade complexa da Ilha de Marajó, com cerâmica elaborada e manejo do ambiente.
- TimeRange: ~400–1300 CE `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `século`(faixa) · Place/Region: Ilha de Marajó (PA hoje).
- ClaimPrinc: "A cultura marajoara desenvolveu sociedade complexa e cerâmica sofisticada em Marajó" — `inferência científica`.
- ClaimTemp: ~400–1300 CE — `inferência` · ClaimEsp: Marajó (`ModernCorrespondence` → PA).
- Source: IPHAN (A, CONF); arqueologia amazônica (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média-alta** · evid: `registro material` · review: `pending` · riscoEd: **alto** (Lei 11.645) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` sociedades pré-colombianas (IND-01); `parte-de` Brasil profundo.
- timeline: **em paralelo** · globe: Amazônia (Marajó) · simultaneidade: complexidade amazônica pré-colonial.
- notes: contraria estereótipo de Amazônia "vazia/primitiva".

**BR-03 · `state:indigenas-pre1500-brasil`** *(CivilizationState — compartilhado com IND)*
- tipo: `State` · camadaP: 22 Povos indígenas · camadasS: 20, 25 · título: Povos indígenas no território hoje brasileiro antes de 1500
- desc: ampla diversidade de povos e línguas no território que hoje é o Brasil antes da chegada europeia.
- TimeRange: história profunda – 1500 · TimePrecision: `intervalo-difuso` · Place/Region: território hoje brasileiro.
- ClaimPrinc: "Antes de 1500, o território hoje brasileiro abrigava centenas de povos indígenas diversos" — `inferência científica`/`fato documentado`.
- ClaimTemp: até 1500 — `inferência` · ClaimEsp: território BR (difuso).
- Source: IPHAN, IBGE, etno-historiografia (A/B), **fontes indígenas** `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (diversidade) · evid: `registro material`+`documental`+`oral` · review: `pending` · riscoEd: **alto** (homogeneização; Lei 11.645) · riscoLic: 1–2.
- rel[]: `predecessor-de` BR-04/contato; `sucessor-de` HIST-02.
- timeline: **em paralelo** · globe: território BR · simultaneidade: Brasil plural antes da colonização.
- notes: etnônimos/autodenominações; **não** "índio" genérico; presença, não ausência.

**BR-04 · `evt:chegada-portuguesa-brasil`**
- tipo: `Event`/`Process` · camadaP: 20 Brasil · camadasS: 13, 22, 21, 25 · título: Chegada portuguesa ao território hoje brasileiro
- desc: chegada das embarcações portuguesas (1500) e início da colonização.
- TimeRange: 1500 em diante · TimePrecision: `ano`(início)/`processo` · Place/Region: litoral do atual Brasil.
- ClaimPrinc: "A chegada portuguesa (1500) iniciou a colonização do território hoje brasileiro" — `fato documentado`; natureza = `interpretação`/`ClaimSet`.
- ClaimTemp: 1500+ — `fato documentado` · ClaimEsp: litoral BR.
- Source: Arquivo Nacional/BN (A, CONF); IBGE; etno-historiografia (A/B) · conf: **alta** (o fato) · evid: `documental` · review: `pending` (`PENDENTE_REVISAO_HUMANA`, possível `PENDENTE_CLAIMSET` terminológico) · riscoEd: **alto** (colonial; cruza IND) · riscoLic: 1–2.
- rel[]: `causou` IND-02 (contato/violência); `sucessor-de` HIST-12; `decorreu-de` 1492 (HIST-13).
- timeline: **em paralelo** · globe: litoral BR · simultaneidade: liga Brasil ao sistema atlântico.
- notes: nomear colonização e agência indígena; evitar "chegada heroica a terra vazia".

**BR-05 · `state:ciclo-ouro-minas`** *(EconomicState)*
- tipo: `State` · camadaP: 14 Economia · camadasS: 20, 21, 25 · título: Ciclo do ouro / Minas colonial
- desc: economia mineradora em Minas Gerais (séc. XVIII), com trabalho escravizado.
- TimeRange: ~1690s–1800s · TimePrecision: `século`(faixa) · Place/Region: Minas Gerais colonial.
- ClaimPrinc: "A mineração de ouro estruturou a economia de Minas colonial, baseada em trabalho escravizado" — `fato documentado`/`interpretação`.
- ClaimTemp: ~1690s–1800s — `fato documentado` · ClaimEsp: Minas (`ModernCorrespondence` → MG).
- Source: Arquivo Nacional/BN (A, CONF); IBGE; historiografia (A/B) · conf: **alta** · evid: `documental` · review: `pending` (`PENDENTE_REVISAO_HUMANA` — escravidão) · riscoEd: **alto** · riscoLic: 1–2.
- rel[]: `contemporâneo-de` HIST-16 (Inconfidência); `relacionado-a` tráfico atlântico (AFR-04).
- timeline: **em paralelo** (séc. XVIII) · globe: Minas · simultaneidade: contexto econômico da cena de 1789.
- notes: nomear escravidão como base do ciclo, sem eufemismo.

**BR-06 · `evt:proclamacao-republica-brasil`**
- tipo: `Event` · camadaP: 13 Política/Estados · camadasS: 20, 25 · título: Proclamação da República (Brasil)
- desc: fim da monarquia e início da República no Brasil (1889).
- TimeRange: 15/11/1889 · TimePrecision: `dia` · Place/Region: Brasil.
- ClaimPrinc: "A República foi proclamada no Brasil em 15/11/1889" — `fato documentado`.
- ClaimTemp: 15/11/1889 — `fato documentado` · ClaimEsp: Brasil.
- Source: Arquivo Nacional/BN (A, CONF); IBGE · conf: **alta** · evid: `documental` · review: `approved` (interpretações → ClaimSet se necessário) · riscoEd: médio · riscoLic: 1.
- rel[]: `sucessor-de` Império; `predecessor-de` BR-07.
- timeline: **em paralelo** (fim séc. XIX) · globe: Brasil · simultaneidade: pano de fundo.
- notes: caráter do processo (golpe militar × movimento) pode virar `PENDENTE_CLAIMSET`.

**BR-07 · `proc:ditadura-militar-brasil`**
- tipo: `Process` · camadaP: 13 Política/Estados · camadasS: 20, 19, 25 · título: Ditadura militar brasileira
- desc: regime autoritário no Brasil (1964–1985), com repressão e violência de Estado documentadas.
- TimeRange: 1964–1985 · TimePrecision: `ano` · Place/Region: Brasil.
- ClaimPrinc: "O Brasil viveu uma ditadura militar (1964–1985) com repressão documentada" — `fato documentado`; avaliações = `interpretação`/`ClaimSet`.
- ClaimTemp: 1964–1985 — `fato documentado` · ClaimEsp: Brasil.
- Source: **Comissão Nacional da Verdade**, Arquivo Nacional (A, CONF); historiografia (A/B) · conf: **alta** (repressão/tortura documentadas) · evid: `documental` (relatórios/arquivos) · review: **`legal-review`/`pending`** (`PENDENTE_REVISAO_HUMANA`, pessoas vivas/LGPD) · riscoEd: **crítico** · riscoLic: 2 (pessoas vivas; mídia).
- rel[]: `predecessor-de` BR-08; `relacionado-a` Guerra Fria.
- timeline: **em paralelo** (séc. XX) · globe: Brasil · simultaneidade: pano de fundo.
- notes: repressão/tortura são **fato documentado**, não "um dos lados"; propaganda do regime sempre rotulada; cautela LGPD.

**BR-08 · `evt:constituicao-1988-brasil`**
- tipo: `Event` · camadaP: 13 Política/Estados · camadasS: 20, 22, 25 · título: Constituição de 1988
- desc: promulgação da Constituição democrática do Brasil (1988), com direitos a indígenas e quilombolas.
- TimeRange: 05/10/1988 · TimePrecision: `dia` · Place/Region: Brasil.
- ClaimPrinc: "A Constituição de 1988 reinstaurou a ordem democrática e reconheceu direitos de povos indígenas e quilombolas" — `fato documentado`.
- ClaimTemp: 05/10/1988 — `fato documentado` · ClaimEsp: Brasil.
- Source: Planalto (texto legal, livre); Arquivo Nacional (A) · conf: **alta** · evid: `documental` (texto legal) · review: `approved` (PENDENTE_REVISAO_HUMANA se entrar disputa contemporânea) · riscoEd: médio-alto · riscoLic: 0–1.
- rel[]: `sucessor-de` BR-07; `relacionado-a` IND-05 (permanência indígena).
- timeline: **em paralelo** · globe: Brasil · simultaneidade: pano de fundo contemporâneo.
- notes: direitos indígenas/quilombolas (arts. 231/232; ADCT 68) — ponte às Leis 10.639/11.645.

### B. África e diáspora africana

**AFR-01 · `state:reino-axum`** *(CivilizationState)*
- tipo: `State` · camadaP: 21 África/diáspora · camadasS: 12, 14, 25 · título: Reino de Axum
- desc: potência comercial do nordeste africano (Chifre da África), com escrita e moeda próprias.
- TimeRange: ~100–940 CE `PENDENTE_REFINAMENTO_TEMPORAL` · TimePrecision: `século`(faixa) · Place/Region: nordeste africano (Etiópia/Eritreia hoje).
- ClaimPrinc: "Axum foi uma potência comercial africana com Estado, escrita e moeda próprios" — `fato documentado`/`interpretação`.
- ClaimTemp: ~100–940 CE — `fato documentado` · ClaimEsp: Chifre da África.
- Source: WHG (B, CC BY, ATRIB/filtrar); historiografia africana (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `documental`+`material` · review: `approved` (PENDENTE_REVISAO_HUMANA se mídia) · riscoEd: médio (Lei 10.639) · riscoLic: 1–2.
- rel[]: `predecessor-de`/`contemporâneo-de` outros Estados africanos; `parte-de` mundo antigo/medieval africano.
- timeline: **em paralelo** · globe: Chifre da África · simultaneidade: África estatal e letrada cedo.
- notes: alternativa estrutural a "Mali" (a Tarefa 4 pediu Kush **ou** Axum); África como origem de Estados complexos.

**AFR-02 · `proc:rotas-transaarianas`**
- tipo: `Process` · camadaP: 21 África/diáspora · camadasS: 14, 12, 25 · título: Rotas transaarianas
- desc: redes de comércio através do Saara ligando a África subsaariana ao Mediterrâneo.
- TimeRange: da Antiguidade ao séc. XVI (auge ~8º–16º) · TimePrecision: `século`(faixa) · Place/Region: Saara e Sahel.
- ClaimPrinc: "Rotas transaarianas integraram a África subsaariana a redes comerciais amplas" — `fato documentado`/`interpretação`.
- ClaimTemp: auge ~8º–16º séc. CE — `fato documentado` · ClaimEsp: Saara/Sahel (rotas).
- Source: WHG (B, CC BY, ATRIB); historiografia (A/B) · conf: **alta** · evid: `documental`+`material` · review: `approved` · riscoEd: médio (Lei 10.639) · riscoLic: 1–2.
- rel[]: `relacionado-a` HIST-10 (Mali) e AFR-01; `possibilitou` integração comercial.
- timeline: **em paralelo** · globe: Saara/Sahel · simultaneidade: África conectada, não isolada.
- notes: comércio (ouro, sal, saber) — antídoto à imagem de "África sem história".

**AFR-03 · `proc:trafico-atlantico`**
- tipo: `Process` · camadaP: 21 África/diáspora · camadasS: 20, 19, 25 · título: Tráfico atlântico de pessoas escravizadas
- desc: sistema de escravização e deslocamento forçado de milhões de africanos para as Américas.
- TimeRange: séc. XVI–XIX · TimePrecision: `século` · Place/Region: África ↔ Américas (rotas atlânticas).
- ClaimPrinc: "O tráfico atlântico escravizou e deslocou milhões de africanos para as Américas (séc. XVI–XIX)" — `fato documentado`; **escala/causas** podem ter `interpretação`.
- ClaimTemp: séc. XVI–XIX — `fato documentado` · ClaimEsp: rotas atlânticas (`Relationship`).
- Source: bases acadêmicas do tráfico transatlântico (A/B) `PENDENTE_CONFIRMACAO_FONTE`; historiografia afro-brasileira · conf: **alta** (o sistema) · evid: `documental`+`quantitativo` · review: **`pending`** (`PENDENTE_REVISAO_HUMANA`) · riscoEd: **crítico** (violência sistêmica; raça) · riscoLic: 2 (mídia gráfica restrita).
- rel[]: `causou` AFR-05 (diáspora); `relacionado-a` BR-05/escravidão; `predecessor-de` HIST-18 (abolição).
- timeline: **em paralelo** · globe: rotas atlânticas · simultaneidade: pano de fundo do mundo atlântico (inclusive 1789, §5).
- notes: "pessoas escravizadas"; sem eufemismo ("comércio"); mídia gráfica oculta por padrão (3.1 §7); nomear resistência.

**AFR-04 · `proc:quilombos-brasil`** *(também BR)*
- tipo: `Process` · camadaP: 21 África/diáspora · camadasS: 20, 25 · título: Quilombos no Brasil
- desc: comunidades de pessoas escravizadas fugidas e seus descendentes (ex.: Palmares).
- TimeRange: séc. XVI–XIX (Palmares ~séc. XVII) · TimePrecision: `século` · Place/Region: território colonial brasileiro.
- ClaimPrinc: "Os quilombos foram comunidades de resistência à escravidão no Brasil" — `fato documentado`/`interpretação`.
- ClaimTemp: séc. XVI–XIX — `fato documentado` · ClaimEsp: Brasil colonial (`ModernCorrespondence`).
- Source: historiografia afro-brasileira (A/B); IPHAN; Arquivo Nacional (CONF) · conf: **alta** · evid: `documental` · review: `pending` (`PENDENTE_REVISAO_HUMANA`) · riscoEd: **alto** (Lei 10.639; agência negra) · riscoLic: 1–2.
- rel[]: `decorreu-de` AFR-03; `relacionado-a` HIST-18; comunidades quilombolas atuais (Constituição 1988, BR-08).
- timeline: **em paralelo** · globe: Brasil · simultaneidade: resistência simultânea à escravidão.
- notes: **agência e resistência**, não vitimização passiva; ponte aos direitos quilombolas atuais.

**AFR-05 · `proc:diaspora-africana-americas`**
- tipo: `Process` · camadaP: 21 África/diáspora · camadasS: 17, 20, 25 · título: Diáspora africana nas Américas
- desc: presença e formação de populações afrodescendentes nas Américas.
- TimeRange: séc. XVI–presente · TimePrecision: `século`(processo longo) · Place/Region: Américas (com foco Brasil).
- ClaimPrinc: "A diáspora africana moldou demografia e cultura das Américas" — `fato documentado`/`interpretação`.
- ClaimTemp: séc. XVI–presente — `fato documentado` · ClaimEsp: Américas.
- Source: historiografia (A/B); IBGE (Brasil) · conf: **alta** · evid: `documental`+`quantitativo` · review: `pending` · riscoEd: **alto** · riscoLic: 1–2.
- rel[]: `decorreu-de` AFR-03; `predecessor-de` AFR-06; `relacionado-a` BR.
- timeline: **em paralelo** · globe: Américas · simultaneidade: pano de fundo contínuo.
- notes: diáspora como **processo cultural ativo**, não só consequência demográfica.

**AFR-06 · `state:cultura-afrobrasileira`** *(CulturalState)*
- tipo: `State`/`Process` · camadaP: 17 Cultura · camadasS: 21, 18, 20, 25 · título: Cultura afro-brasileira (processo histórico-cultural)
- desc: formação de práticas, religiões e expressões afro-brasileiras ao longo da história.
- TimeRange: período colonial – presente · TimePrecision: `século`(processo) · Place/Region: Brasil.
- ClaimPrinc: "A cultura afro-brasileira é processo histórico-cultural central na formação do Brasil" — `fato documentado`/`interpretação`.
- ClaimTemp: colonial–presente — `fato documentado` · ClaimEsp: Brasil.
- Source: IPHAN (A, CONF); historiografia/etnografia (A/B); acervos (por asset) · conf: **alta** · evid: `documental`+`etnográfico` · review: `pending` (`PENDENTE_REVISAO_HUMANA` — sacralidade religiosa) · riscoEd: **alto** (religiões afro; sacralidade) · riscoLic: 2 (mídia/sacralidade).
- rel[]: `decorreu-de` AFR-05; `parte-de` cultura brasileira; `relacionado-a` religiões (camada 18).
- timeline: **em paralelo** · globe: Brasil · simultaneidade: pano de fundo cultural.
- notes: religiões afro-brasileiras como objeto de estudo respeitoso (sem proselitismo/ridicularização); Lei 10.639.

### C. Povos indígenas e história profunda das Américas

**IND-01 · `state:sociedades-precolombianas`** *(CivilizationState)*
- tipo: `State` · camadaP: 22 Povos indígenas/Américas · camadasS: 12, 25 · título: Sociedades indígenas pré-colombianas
- desc: sociedades complexas das Américas antes de 1492 (ex.: andinas, mesoamericanas, amazônicas).
- TimeRange: história profunda – 1492 · TimePrecision: `intervalo-difuso` · Place/Region: Américas.
- ClaimPrinc: "As Américas abrigavam sociedades complexas e diversas antes de 1492" — `fato documentado`/`inferência`.
- ClaimTemp: até 1492 — `inferência`/`fato documentado` · ClaimEsp: Américas (vários focos).
- Source: arqueologia/etno-historiografia (A/B); WHG (filtrar) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `registro material`+`documental` · review: `pending` · riscoEd: **alto** (Lei 11.645) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` BR-02 (marajoara); `predecessor-de` IND-02.
- timeline: **em paralelo** · globe: Américas · simultaneidade: Américas complexas em 1492 (cruza HIST-13).
- notes: diversidade e complexidade; sem "povos sem história".

**IND-02 · `proc:contato-violencia-colonial`**
- tipo: `Process` · camadaP: 22 Povos indígenas · camadasS: 13, 19, 20, 25 · título: Contato e violência colonial
- desc: violência, epidemias e despossessão decorrentes da colonização europeia das Américas.
- TimeRange: 1492/1500 em diante · TimePrecision: `século`(processo) · Place/Region: Américas (foco território BR).
- ClaimPrinc: "A colonização provocou violência, epidemias e despossessão de povos indígenas" — `fato documentado`; ênfases = `interpretação`.
- ClaimTemp: 1492/1500+ — `fato documentado` · ClaimEsp: Américas.
- Source: etno-historiografia (A/B); IPHAN; fontes indígenas `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (o fenômeno) · evid: `documental`+`material` · review: **`pending`** (`PENDENTE_REVISAO_HUMANA`) · riscoEd: **crítico** (genocídio/violência; Lei 11.645) · riscoLic: 2 (mídia restrita).
- rel[]: `decorreu-de` HIST-13/BR-04; `predecessor-de` IND-03 (resistência).
- timeline: **em paralelo** · globe: Américas · simultaneidade: contraponto à narrativa de "encontro" idílico.
- notes: dignidade às vítimas; onde houver disputa legítima "genocídio"×outro termo → `ClaimSet` terminologia sensível; negação = rejeitada.

**IND-03 · `proc:resistencia-indigena`**
- tipo: `Process` · camadaP: 22 Povos indígenas · camadasS: 20, 13, 25 · título: Resistência indígena
- desc: resistências, revoltas e estratégias de sobrevivência indígena ao longo da colonização e depois.
- TimeRange: 1500 – presente · TimePrecision: `século`(processo) · Place/Region: Américas (foco BR).
- ClaimPrinc: "Povos indígenas resistiram ativamente à colonização e persistem como agentes históricos" — `fato documentado`/`interpretação`.
- ClaimTemp: 1500–presente — `fato documentado` · ClaimEsp: Américas/Brasil.
- Source: etno-historiografia (A/B); IPHAN; fontes indígenas · conf: **alta** · evid: `documental`+`oral` · review: `pending` · riscoEd: **alto** (Lei 11.645) · riscoLic: 1–2.
- rel[]: `decorreu-de` IND-02; `predecessor-de` IND-05.
- timeline: **em paralelo** · globe: Américas/Brasil · simultaneidade: agência, não só sujeição.
- notes: **resistência e agência** centrais; evitar narrativa de extinção.

**IND-04 · `state:permanencia-indigena-contemporanea`** *(CivilizationState/PopulationState)*
- tipo: `State` · camadaP: 22 Povos indígenas · camadasS: 23, 20, 25 · título: Permanência contemporânea dos povos indígenas
- desc: presença atual de centenas de povos indígenas, com línguas e territórios reconhecidos.
- TimeRange: presente · TimePrecision: `ano`(atual) · Place/Region: Brasil/Américas.
- ClaimPrinc: "Centenas de povos indígenas vivem hoje no Brasil, com línguas e territórios" — `fato documentado`/`medição`.
- ClaimTemp: presente — `medição` (censo) · ClaimEsp: Brasil (terras indígenas).
- Source: **IBGE** (A, aberto, ATRIB) `PENDENTE_REFINAMENTO_ESPACIAL` (números/territórios exatos); IPHAN/FUNAI `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (presença) · evid: `medição` (censo) · review: `pending` (`PENDENTE_REVISAO_HUMANA`; pessoas/comunidades vivas) · riscoEd: **alto** ("povos do passado"; Lei 11.645) · riscoLic: 1 (IBGE aberto).
- rel[]: `sucessor-de` IND-03; `relacionado-a` BR-08 (Constituição 1988).
- timeline: ponta contemporânea · globe: terras indígenas (Brasil) · simultaneidade: **presente**, não passado.
- notes: presente **e** passado; números exatos com fonte (IBGE 2022) a confirmar — não estimar.

---

## 5. Cena canônica de 1789 (Tarefa 5)

A cena prova a função **"O que acontecia no mundo neste momento?"** — ensinar a Revolução Francesa **sem fechar o mundo ao redor dela**. A consulta é a interseção temporal/espacial sobre claims tipados (Etapa 2, P7); nada de novo precisa existir além de itens já tipados.

**Consulta:** `ano = 1789` · `foco = Revolução Francesa (HIST-15)` · `modo = simultaneidade global`.

A cena reutiliza itens da espinha (HIST-15, HIST-16, AFR-03, IND-01/IND-03) e adiciona **8 itens-piloto de contexto** (SCENE-xx), no mesmo padrão, para os recortes que faltavam. Isso eleva o lote total a **70 itens** (62 espinha + 8 cena) — dentro do teto pedido.

### Itens de contexto adicionados para a cena

**SCENE-01 · `evt:lavoisier-traite-1789`**
- tipo: `Event` · camadaP: 15 Ciência · camadasS: 17, 25 · título: Publicação do *Traité élémentaire de chimie* · desc: marco da química moderna, publicado em 1789.
- TimeRange: 1789 · TimePrecision: `ano` · Place/Region: Paris (`Place`).
- ClaimPrinc: "Lavoisier publicou em 1789 uma obra que sistematizou a química moderna" — `fato documentado`.
- ClaimTemp: 1789 — `fato documentado` · ClaimEsp: Paris, França.
- Source: história da ciência (A/B); arquivos `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `documental` · review: `approved` · riscoEd: baixo · riscoLic: 1 (mídia por asset).
- rel[]: `contemporâneo-de` HIST-15, HIST-16; `parte-de` HIST-14; `participante` SCENE-07.
- timeline: ponto em 1789 · globe: Paris · simultaneidade: **ciência simultânea** à política — coração da cena.
- notes: mostra que 1789 não é só política; a química moderna nasce no mesmo ano.

**SCENE-07 · `ent:lavoisier`**
- tipo: `Entity` (pessoa) · camadaP: 15 Ciência · camadasS: 25 · título: Antoine-Laurent de Lavoisier · desc: químico francês, figura central da química moderna.
- TimeRange (existência): 1743–1794 · TimePrecision: `ano` · Place/Region: França.
- ClaimPrinc: "Lavoisier (1743–1794) foi figura central da química moderna" — `fato documentado`.
- ClaimTemp: existência 1743–1794 — `fato documentado` · ClaimEsp: França.
- Source: história da ciência (A/B); VIAF só reconciliação (C/INDX) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `documental` · review: `approved` · riscoEd: baixo · riscoLic: 0.
- rel[]: `participou-de` SCENE-01; `relacionado-a` HIST-14.
- timeline: barra de existência · globe: França · simultaneidade: ator da ciência de 1789.
- notes: **único `Entity`-pessoa do lote** — demonstra o tipo (VIAF apenas reconcilia, nunca afirma).

**SCENE-02 · `state:eua-governo-1789`**
- tipo: `State` (`CivilizationState`) · camadaP: 13 Política · camadasS: 25 · título: Início do governo constitucional dos EUA · desc: posse de Washington e primeiro governo sob a Constituição (1789).
- TimeRange: 1789 · TimePrecision: `ano` · Place/Region: Estados Unidos.
- ClaimPrinc: "Em 1789 instalou-se o primeiro governo dos EUA sob a Constituição, com a posse de Washington" — `fato documentado`.
- ClaimTemp: 1789 — `fato documentado` · ClaimEsp: EUA (`GeometryVersion` de 1789).
- Source: arquivos/historiografia (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `documental` · review: `approved` · riscoEd: baixo · riscoLic: 1.
- rel[]: `contemporâneo-de` HIST-15, HIST-16.
- timeline: 1789 · globe: América do Norte (fronteira de 1789) · simultaneidade: terceira revolução atlântica simultânea.
- notes: tríade atlântica (França/Brasil/EUA) num só ano.

**SCENE-03 · `state:imperio-otomano-1789`**
- tipo: `State` (`CivilizationState`) · camadaP: 13 Política · camadasS: 12, 18, 25 · título: Império Otomano em 1789 · desc: início do reinado de Selim III e tentativas de reforma.
- TimeRange: 1789 (recorte) · TimePrecision: `ano` · Place/Region: Anatólia, Bálcãs, Levante, N. da África.
- ClaimPrinc: "Em 1789 o Império Otomano iniciava o reinado de Selim III e um programa de reformas" — `fato documentado` + `interpretação historiográfica` (alcance das reformas).
- ClaimTemp: 1789 — `fato documentado` · ClaimEsp: território otomano (`GeometryVersion`).
- Source: historiografia (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média-alta** · evid: `documental` · review: `pending` (`PENDENTE_REVISAO_HUMANA`) · riscoEd: médio · riscoLic: 1.
- rel[]: `contemporâneo-de` HIST-15.
- timeline: estado em 1789 · globe: território otomano · simultaneidade: **recorte não eurocêntrico** do mesmo ano.
- notes: descentra a narrativa europeia sem apagá-la.

**SCENE-04 · `state:china-qing-1789`**
- tipo: `State` (`CivilizationState`) · camadaP: 12 Civilizações · camadasS: 13, 14, 25 · título: China Qing em 1789 · desc: império Qing sob Qianlong, entre as maiores economias do mundo à época.
- TimeRange: 1789 (recorte) · TimePrecision: `ano` · Place/Region: Ásia Oriental.
- ClaimPrinc: "Em 1789 a China Qing era um dos maiores Estados e economias do mundo" — `fato documentado` + `interpretação` (peso econômico relativo).
- ClaimTemp: 1789 — `fato documentado` · ClaimEsp: território Qing.
- Source: historiografia (A/B); OWID p/ ordem de grandeza econômica `PENDENTE_CONFIRMACAO_FONTE` · conf: **média-alta** · evid: `documental` · review: `pending` · riscoEd: médio · riscoLic: 1.
- rel[]: `contemporâneo-de` HIST-15, SCENE-04.
- timeline: estado em 1789 · globe: Ásia Oriental · simultaneidade: contrapeso à centralidade europeia.
- notes: peso econômico como `interpretação`, com fonte; não afirmar ranking como fato seco.

**SCENE-05 · `state:africa-ocidental-1789`**
- tipo: `State` (`CivilizationState`) · camadaP: 21 África · camadasS: 12, 19, 25 · título: Estados da África Ocidental em 1789 · desc: recorte de polities africanas ativas (ex.: Oyo, Daomé, Axânti) à época.
- TimeRange: 1789 (recorte) · TimePrecision: `ano` `PENDENTE_REFINAMENTO_ESPACIAL` · Place/Region: África Ocidental.
- ClaimPrinc: "Em 1789 a África Ocidental abrigava Estados complexos e ativos no comércio atlântico" — `fato documentado` (existência) + `interpretação`.
- ClaimTemp: 1789 — `fato documentado` · ClaimEsp: África Ocidental (`SpatialUncertainty = fronteira difusa`).
- Source: historiografia africana (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média** · evid: `documental` + `registro material` · review: `pending` (`PENDENTE_REVISAO_HUMANA`) · riscoEd: **alto** (Lei 10.639; cruza tráfico) · riscoLic: 1–2.
- rel[]: `contemporâneo-de` HIST-15; `relacionado-a` AFR-03.
- timeline: estado em 1789 · globe: África Ocidental · simultaneidade: **antieurocentrismo estrutural** — África como agente em 1789.
- notes: nomear polities específicas exige confirmação por fonte; aqui entra como recorte, não lista fechada.

**SCENE-06 · `state:economia-mundo-atlantico-1789`**
- tipo: `State` (`EconomicState`) · camadaP: 14 Economia · camadasS: 21, 25 · título: Economia do mundo atlântico em 1789 · desc: economia mercantil-escravista que conectava Europa, África e Américas.
- TimeRange: 1789 (recorte) · TimePrecision: `ano` · Place/Region: bacia atlântica.
- ClaimPrinc: "Em 1789, a economia atlântica articulava Europa, África e Américas em torno do trabalho escravizado e do comércio" — `interpretação historiográfica` apoiada em `estimativa`.
- ClaimTemp: 1789 — `estimativa` · ClaimEsp: bacia atlântica.
- Source: OWID/literatura econômica (B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **média** · evid: `inferência indireta` · review: `pending` · riscoEd: alto (cruza escravidão) · riscoLic: 1.
- rel[]: `relacionado-a` AFR-03, SCENE-05; `contexto-de` HIST-15.
- timeline: estado em 1789 · globe: overlay econômico atlântico · simultaneidade: contexto econômico da cena.
- notes: números antigos = faixa/`estimativa`, jamais `medição`.

**SCENE-08 · `concept:iluminismo`**
- tipo: `Concept` · camadaP: 17 Cultura · camadasS: 13, 15, 25 · título: Iluminismo · desc: movimento intelectual que influenciou as revoluções atlânticas.
- TimeRange: formulação ~séc. XVII–XVIII (transtemporal) · TimePrecision: `século` · Place/Region: Europa/Atlântico (difusão).
- ClaimPrinc: "O Iluminismo foi um movimento intelectual que influenciou as revoluções do fim do século XVIII" — `interpretação historiográfica`.
- ClaimTemp: difusão séc. XVII–XVIII — `interpretação` · ClaimEsp: difuso (`SpatialUncertainty = fronteira difusa`).
- Source: historiografia (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** · evid: `documental` · review: `approved` · riscoEd: médio (evitar leitura unicausal) · riscoLic: 0.
- rel[]: `influenciou` HIST-15; `sucessor-de` HIST-14.
- timeline: faixa de difusão · globe: Europa/Atlântico · simultaneidade: corrente de ideias da cena.
- notes: **único `Concept` do lote** — demonstra o tipo; influência é claim com fonte, não nexo automático.

### Resultado da cena (12 retornos)

| # | Item | Tipo | Camada | Lugar/Região | TimeRange | conf | Fonte A/B | Natureza | Globo | Timeline | Obs. editorial |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HIST-15 `proc:revolucao-francesa` | Process | 13 Política | França/Paris | 1789–1799 | alta | arquivos/historiografia (A/B) | **fato** (eventos) + **ClaimSet** (causas, CS1) | França destacada | bloco 1789–99 | é o **foco**, não o centro do mundo. |
| 2 | HIST-16 `evt:inconfidencia-mineira` | Event | 20 Brasil | território→MG (`ModernCorrespondence`) | 1789 | alta | IBGE/Arquivo Nac. (A) | **fato documentado** | Minas via correspondência moderna | ponto 1789 | Brasil simultâneo; sem anacronismo. |
| 3 | SCENE-02 `state:eua-governo-1789` | State | 13 Política | EUA | 1789 | alta | arquivos (A/B) | **fato documentado** | América do Norte | 1789 | tríade atlântica. |
| 4 | SCENE-01 `evt:lavoisier-traite-1789` (+SCENE-07) | Event/Entity | 15 Ciência | Paris | 1789 | alta | história da ciência (A/B) | **fato documentado** | Paris (ponto) | ponto 1789 | ciência simultânea à política. |
| 5 | SCENE-03 `state:imperio-otomano-1789` | State | 13 Política | território otomano | 1789 | média-alta | historiografia (A/B) | fato + **interpretação** | território otomano | estado 1789 | recorte não europeu. |
| 6 | SCENE-04 `state:china-qing-1789` | State | 12 Civilizações | Ásia Oriental | 1789 | média-alta | historiografia/OWID | fato + **interpretação** (peso econ.) | Ásia Oriental | estado 1789 | contrapeso à centralidade europeia. |
| 7 | SCENE-05 `state:africa-ocidental-1789` | State | 21 África | África Ocidental | 1789 | média | historiografia africana (A/B) | **fato** (existência) + interpretação | África Ocidental | estado 1789 | **Lei 10.639**; antieurocentrismo. |
| 8 | AFR-03 `proc:trafico-atlantico` | Process | 21 África | bacia atlântica | séc. XVI–XIX (ativo em 1789) | alta | bases do tráfico (A/B) | **fato documentado** (revisão obrigatória) | rotas atlânticas | processo | escravidão ativa em 1789. |
| 9 | IND-03 `proc:resistencia-indigena` / IND-01 | Process/State | 22 Indígenas | Américas | contemporâneo a 1789 | alta | etno-historiografia (A/B) | fato + **interpretação** | Américas | paralelo | **Lei 11.645**; agência indígena. |
| 10 | SCENE-06 `state:economia-mundo-atlantico-1789` | State | 14 Economia | bacia atlântica | 1789 | média | OWID/literatura (B) | **estimativa** | overlay econômico | estado 1789 | contexto econômico; faixa, não número seco. |
| 11 | HIST-14 `proc:revolucao-cientifica` + HIST-17 `proc:revolucao-industrial` (em curso) + SCENE-01 | Process | 15/16 Ciência/Tecnologia | Europa/global | c.1789 | média-alta | historiografia/OWID | fato + **interpretação** | overlay tecnológico | processos | industrialização incipiente; contexto técnico-científico. |
| 12 | *(síntese política mundial)* | — | 13 Política | global | 1789 | — | múltiplas (A/B) | **síntese** (não-opinativa) | mapa-mundi de regimes | 1789 | o produto **descreve** o tabuleiro político; não opina. |

**O que a cena prova.** O sistema ensina a Revolução Francesa **e** mantém o globo aberto: Brasil (Inconfidência), EUA, Otomanos, China, África Ocidental, escravidão atlântica, povos indígenas, ciência (Lavoisier), economia e tecnologia aparecem no **mesmo instante**, cada um com tipo, fonte e confiança. A simultaneidade é a interseção dos índices, não um módulo — e os três paralelos (Brasil/África/indígenas) entram **na cena**, não como nota de rodapé.

---

## 6. Exemplos de ClaimSet (Tarefa 6)

Sete `ClaimSet`-piloto. Cada um: **tema · `consensusStatus` · claims concorrentes legítimos · posição SEM equivalência (se houver) · fontes preferenciais · `reviewStatus` · nota editorial**. Regra-mãe (Etapa 3.1, §3.4): controvérsia legítima recebe pluralidade; **negacionismo recebe rótulo de rejeição, fora do `ClaimSet`**.

**CS1 — Causas da Revolução Francesa** *(→ HIST-15)*
- `consensusStatus`: **controvérsia historiográfica**.
- Claims legítimos: (a) crise fiscal-financeira do Estado; (b) tensões sociais e de ordem; (c) circulação de ideias iluministas; (d) crise de subsistência/agrária. Cada um atribuído a correntes/autores, com peso.
- Sem equivalência: nenhuma — todas têm base documental; o produto **não** elege vencedor.
- Fontes: historiografia revisada (A/B); fontes primárias.
- `reviewStatus`: `pending` (revisão historiográfica).
- Nota: separar **fatos datados** (fato documentado) das **causas** (interpretação); exibir pesos, não "alguns dizem".

**CS2 — 1492: "descobrimento", "invasão" ou "encontro"** *(→ HIST-13)*
- `consensusStatus`: **terminologia sensível**.
- Claims legítimos: os três termos, cada um com seu enquadramento e contexto; o **fato** da travessia de 1492 é fato documentado (fora de disputa).
- Sem equivalência: narrativas que apagam a presença/agência dos povos originários.
- Fontes: historiografia plural; fontes ameríndias; WHG.
- `reviewStatus`: `pending` (revisão obrigatória; Lei 11.645).
- Nota: o **nome é a controvérsia**; apresentar termos com contexto, sem impor um como "neutro".

**CS3 — Origem da vida** *(→ SCI-11)*
- `consensusStatus`: **hipóteses concorrentes**.
- Claims legítimos: mundo de RNA; fontes hidrotermais; panspermia (como hipótese de transporte, não de origem última); química prebiótica de superfície. Todos `claimType = hipótese`.
- Sem equivalência: criacionismo/desenho inteligente (**negacionismo**, fora do `ClaimSet`).
- Fontes: astrobiologia/bioquímica revisada (A/B); PBDB para contexto.
- `reviewStatus`: `pending` (científica).
- Nota: o **fato** (vida cedo, ~3,5 Ga) é separado do **mecanismo** (em aberto).

**CS4 — K-Pg: impacto, vulcanismo ou combinação** *(→ SCI-21)*
- `consensusStatus`: **hipóteses concorrentes** (com convergência crescente para combinação).
- Claims legítimos: (a) impacto de Chicxulub como gatilho principal; (b) vulcanismo do Deccan; (c) combinação/efeito sinérgico. Cada um com evidência.
- Sem equivalência: negar a extinção ou a idade (~66 Ma) = negacionismo, fora do `ClaimSet`.
- Fontes: PBDB; geociências revisadas (A/B).
- `reviewStatus`: `pending` (científica).
- Nota: **fato** (extinção ~66 Ma, alta confiança) separado da **atribuição causal** (debate).

**CS5 — Mudanças climáticas: consenso antrópico × incertezas de projeção** *(→ HIST-21)*
- `consensusStatus`: **consenso amplo** (aquecimento real e antrópico) **+** debate **interno** sobre faixas de projeção.
- Claims legítimos (apenas internos ao consenso): faixas de sensibilidade climática; cenários de emissão; magnitude/ritmo regionais — `debate acadêmico` dentro do consenso.
- **Sem equivalência:** negação do aquecimento ou de sua causa antrópica (**negacionismo rejeitado**, fora do `ClaimSet`).
- Fontes: NOAA/NCEI, NASA GISS, Berkeley Earth, IPCC (figuras recriadas dos dados); INPE/MapBiomas (Brasil).
- `reviewStatus`: `pending` (científica).
- Nota: **caso-modelo de "incerteza sem falsa equivalência"** — a incerteza é de **projeção**, não do fato.

**CS6 — Povoamento das Américas** *(→ HIST-02 / IND-01)*
- `consensusStatus`: **hipóteses concorrentes**.
- Claims legítimos: cronologias (≥~15–16 ka, com sítios pré-Clóvis sob avaliação, ex.: pegadas datadas mais antigas em revisão) e rotas (costeira do Pacífico × interior). `claimType = hipótese`.
- Sem equivalência: narrativas pseudoarqueológicas sem lastro (fora do `ClaimSet`).
- Fontes: arqueologia/etno-historiografia revisada (A/B).
- `reviewStatus`: `pending` (obrigatória; Lei 11.645).
- Nota: cronologias **em aberto**, lado a lado; não cravar data única; respeitar perspectivas indígenas.

**CS7 — Evolução humana fina** *(→ SCI-22 / SCI-23)*
- `consensusStatus`: **debate acadêmico / hipóteses concorrentes**.
- Claims legítimos: topologia de ramos do gênero *Homo*; grau e momento de hibridização (ex.: com neandertais/denisovanos); modelo de origem do *sapiens* (multirregional fraco × africano com estrutura). `claimType = hipótese`/`inferência`.
- **Sem equivalência:** qualquer hierarquização entre populações humanas (racialismo) — **rejeitado**, não é "lado".
- Fontes: paleoantropologia/paleogenética revisada (A/B).
- `reviewStatus`: `pending` (obrigatória; raça e ciência).
- Nota: evolução é **fato**; os **detalhes** são debate; jamais converter debate em hierarquia.

---

## 7. Validação do vocabulário controlado (Tarefa 7)

Teste dos vocabulários contra os 70 itens. Veredito + ajuste **justificado** (sem remodelar).

| Vocabulário | Valores exercitados no lote | Veredito | Ajuste proposto (justificado) |
|---|---|---|---|
| **claimType** | `fato documentado`, `medição`, `inferência científica`, `estimativa`, `hipótese`, `interpretação historiográfica`, `reconstrução modelada` | **Suficiente.** Os 7 usados cobriram a espinha. | **Depreciar `controvérsia` como `claimType`**: controvérsia é estrutural (vira `ClaimSet`/`consensusStatus`), não tipo de um claim isolado. `representação artística`/`aproximação didática` ficam para mídia/saída (não exercitados aqui). |
| **consensusStatus** | `controvérsia historiográfica`, `terminologia sensível`, `hipóteses concorrentes`, `consenso amplo`, `desinformação/negacionismo rejeitado` | **Suficiente.** Distinguiu pluralidade de rejeição em todos os 7 ClaimSets. | Nenhum. `debate acadêmico` usado dentro de CS7/CS5 confirma a granularidade. |
| **confidenceLevel** | `alta`, `média-alta`, `média`, `média-baixa`(implícito), `baixa`(implícito) | **Suficiente** como escala de 5 pontos. | Fixar oficialmente os **5 níveis**; evitar valores livres. |
| **evidenceLevel** | `dado modelado`, `medição instrumental`, `medição`, `documental`, `registro material`, `inferência indireta`, `oral` | **Quase suficiente**, mas estava **livre demais**. | **Controlar em 6 valores**: `medição/observação direta` · `dado modelado` · `registro material/arqueológico` · `registro documental` · `inferência indireta/multi-proxy` · **`tradição/registro oral`**. O último é **necessário** para fontes indígenas e afro-brasileiras (Leis 11.645/10.639) — não é remodelagem, é reconhecimento de tipo de evidência legítimo. |
| **reviewStatus** | `approved`, `pending` | **Suficiente**, mas faltou aplicar `legal-review`. | **Aplicar `legal-review`** a itens com pessoas vivas/identificáveis — explicitamente **BR-07 (ditadura militar)** deve migrar de `pending` para `legal-review` (LGPD). Mantém o enum `{pending, approved, legal-review, rejected}`. |
| **ingestionDecision** | `AUTO`, `ATRIB`, `REVH`, `CONF` | **Suficiente** para fontes "verdes". | `ISOLA`/`FATO`/`COMER`/`NÃO` não exercitados porque o piloto evitou fontes SA/NC/comerciais (disciplina da Etapa 1.1) — **manter o enum completo** para 4C (ex.: MapBiomas→ISOLA; ICS-gráfico→FATO). |
| **licenseRiskLevel** | `0`, `1`, `2` | **Suficiente.** Lote inteiro em risco 0–2 (sem alto). | Nenhum. Confirma a escolha de fontes limpas; níveis 3–5 só entram com isolamento/contrato em 4C. |
| **natureLabel** | `reconstrução científica` (Pangeia); `representação artística`/`aproximação didática` (previstos) | **Suficiente**, pouco exercitado (mídia adiada). | Nenhum agora; validar de fato quando a camada 24 (Mídia) for povoada (4C+). |
| **TimePrecision** | `Ga`, `Ma`, `ka`, `século`, `década`, `ano`, faixa/relativo | **Suficiente** do tempo profundo ao dia. | **Formalizar modificadores `faixa` e `relativo`**; pendente a decisão de **datum** (1950 BP × J2000) — já encaminhada à Etapa 3 (não se resolve aqui). |
| **SpatialUncertainty** | `sem localização precisa`, `localização inferida`, `fronteira difusa`, `reconstrução` | **Suficiente.** Cobriu desde "sem-localização" (Big Bang) até fronteira difusa (África Ocidental 1789). | Nenhum. |
| **relationshipType** | `predecessor-de`/`sucessor-de`, `ocorreu-durante`, `causou`, `afetou`, `influenciou`, `relacionado-a`, `contemporâneo-de`, `evidenciado-por`, `parte-de`, `localizado-em`/`modernCorrespondence`, `hipótese-concorrente`, `terminologia-sensível`, **`possibilitou`**, **`decorreu-de`**, `participou-de` | **Quase suficiente.** | **Adicionar oficialmente `possibilitou` e `decorreu-de`** à família causal (usados em tecnologia→economia e contato→resistência) — são distinções causais legítimas, não redundância. |

**Conclusão.** Os vocabulários da Etapa 2/3.1 **funcionaram** no povoamento real. Os únicos ajustes necessários são pequenos e justificados: controlar `evidenceLevel` (com `tradição/registro oral`), depreciar `controvérsia` como `claimType`, aplicar `legal-review`, formalizar dois `relationshipType` causais e dois modificadores de `TimePrecision`. Nenhuma remodelagem estrutural.

---

## 8. Relationship Graph mínimo (Tarefa 8)

Primeira malha entre os itens do lote. **Arestas afirmativas** (`causou`/`influenciou`/`afetou`/`possibilitou`/`decorreu-de`) são **elas próprias claims** — carregam fonte e confiança (Etapa 2, §6); não são nexos automáticos.

| # | Origem | `relationshipType` | Destino | claim? (fonte/conf) | Camadas conectadas |
|---|---|---|---|---|---|
| R1 | SCI-12 `fotossintese-oxigenica` | **causou** | SCI-13 `goe` | sim (A, alta) | 8↔4 (vida↔atmosfera) |
| R2 | SCI-19 `pangeia` | **relacionado-a** | `concept:tectonica-placas` (deriva) | — (estrutural) | 6 (tectônica) |
| R3 | SCI-21 `extincao-kpg` | **causou** | extinção de dinossauros não-avianos | sim (A, alta p/ fato; causa em CS4) | 9 (paleobiologia) |
| R4 | HIST-14 `revolucao-cientifica` | **influenciou** | SCENE-08 `concept:iluminismo` | sim (A/B, média-alta) | 15↔17 |
| R5 | SCENE-08 `concept:iluminismo` | **influenciou** | HIST-15 `revolucao-francesa` | sim (A/B, controvérsia → CS1) | 17↔13 |
| R6 | HIST-17 `revolucao-industrial` | **causou** | HIST-21 `mudancas-climaticas-modernas` | sim (A, alta; antrópico) | 16↔5 |
| R7 | AFR-03 `trafico-atlantico` | **causou** | AFR-05 `diaspora-africana-americas` | sim (A/B, alta) | 21 |
| R8 | AFR-05 `diaspora-africana-americas` | **localizado-em / modernCorrespondence** | Brasil (BR-*) | sim (A, alta) | 21↔20 |
| R9 | BR-03 `indigenas-pre1500-brasil` | **localizado-em** | território hoje brasileiro | sim (A) | 22↔20 |
| R10 | BR-04 `chegada-portuguesa-brasil` | **causou** | IND-02 `contato-violencia-colonial` | sim (A/B, alta; terminologia sensível) | 20↔22 |
| R11 | IND-02 `contato-violencia-colonial` | **causou** | IND-03 `resistencia-indigena` | sim (A/B, alta) | 22 |
| R12 | HIST-16 `inconfidencia-mineira` | **contemporâneo-de** | HIST-15 `revolucao-francesa` | — (índice temporal) | 20↔13 |
| R13 | HIST-19 `apollo-11` | **decorreu-de** | `concept:guerra-fria` (a criar em 4C) | sim (A/B, alta) | 2/16↔13/19 |
| R14 | SCI-13 `goe` | **afetou** | SCI-14 `surgimento-eucariontes` | sim (A, média-alta) | 4↔8 |
| R15 | SCI-09 `atmosfera-primitiva` | **transition→** (via SCI-13) | atmosfera pós-GOE | — (estado) | 4 |
| R16 | AFR-03 `trafico-atlantico` | **relacionado-a** | AFR-04 `quilombos-brasil` | sim (A/B, alta) | 21↔20 |
| R17 | HIST-13 `1492-travessia-colombo` | **terminologia-sensível** | (ClaimSet CS2) | — (estrutural) | 12↔22 |
| R18 | SCI-22 `surgimento-homo` | **hipótese-concorrente** | (ClaimSet CS7) | — (estrutural) | 10 |
| R19 | HIST-18 `abolicao-brasil` | **decorreu-de** | AFR-03 `trafico-atlantico` (+ luta abolicionista) | sim (A/B, alta) | 20↔21 |
| R20 | BR-07 `ditadura-militar-brasil` | **predecessor-de** | BR-08 `constituicao-1988-brasil` | sim (A, alta) | 20↔13 |

**Cadeias-exemplo (obrigatórias) montadas:**
- **fotossíntese → GOE → eucariontes** (R1, R14).
- **Pangeia ↔ tectônica/deriva** (R2).
- **K-Pg → extinção dos dinossauros não-avianos** (R3).
- **Revolução Científica → Iluminismo → Revolução Francesa** (R4, R5).
- **Revolução Industrial → mudanças climáticas modernas** (R6).
- **tráfico atlântico → diáspora africana → Brasil** (R7, R8) + quilombos (R16).
- **povos indígenas → território hoje brasileiro → colonização → resistência** (R9, R10, R11).
- **Inconfidência Mineira contemporânea da Revolução Francesa** (R12).
- **Apollo 11 → Guerra Fria → tecnologia espacial** (R13).

> **Nós referenciados ainda não-itens** (a promover na 4C): `concept:tectonica-placas`, `concept:guerra-fria`, `concept:expansao-universo`. Hoje são alvos de aresta, não itens completos — registrado no relatório de qualidade.

---

## 9. Relatório de qualidade do lote (Tarefa 9)

1. **Itens criados:** **70** — 62 da espinha (SCI-01..23, HIST-01..21, BR-01..08, AFR-01..06, IND-01..04) + 8 de cena (SCENE-01..08).
2. **Event:** **20** (19 na espinha + SCENE-01).
3. **Process:** **26**.
4. **Concept:** **1** (SCENE-08 `concept:iluminismo`). *Lacuna: ver item 13.*
5. **State:** **22** (17 na espinha + 5 SCENE). Subtipos exercitados: Atmosphere, Paleogeographic, Biome, Civilization, Cultural, Economic, Population (implícito em IND-04/SCENE-06).
6. **Entity:** **1** (SCENE-07 `ent:lavoisier`). *Lacuna: ver item 13.*
7. **Exigem revisão humana (não-`approved`):** **24 na espinha** (`pending`) + 5 itens de cena `pending` = **~29**; **0 itens** `approved` em temas sensíveis (todos os sensíveis estão retidos).
8. **Têm `ClaimSet` (atual ou pendente):** **9 itens** marcados `PENDENTE_CLAIMSET`/com ClaimSet associado, cobertos pelos **7 ClaimSets** autorais (CS1–CS7) ligados a HIST-15, HIST-13, SCI-11, SCI-21, HIST-21, HIST-02/IND-01, SCI-22/23.
9. **Fonte A/B clara:** **60 de 62** itens da espinha citam fonte **A** explícita (e os 8 de cena citam A/B); **2** dependem de confirmação por asset (`PENDENTE_CONFIRMACAO_FONTE`). Wikidata/VIAF aparecem **só** como índice (INDX), nunca como autoridade.
10. **Risco de licença:** **baixo** (risco 0) em **16**; **baixo** (risco 1) em **41**; **médio** (risco 2) em **5**; **alto (3–5): 0**. O lote ficou inteiramente em fontes "verdes" (Etapa 1.1), sem ShareAlike/NC/comercial.
11. **Pendências abertas** (flags): `PENDENTE_REVISAO_HUMANA` ×24 · `PENDENTE_CONFIRMACAO_FONTE` ×15 · `PENDENTE_REFINAMENTO_TEMPORAL` ×12 · `PENDENTE_CLAIMSET` ×9 · `PENDENTE_REFINAMENTO_ESPACIAL` ×2 · `PENDENTE_LICENCA` ×1. **Inconsistência detectada:** IND-03 referencia `IND-05` (inexistente) — corrigir para `IND-04` na revisão.
12. **Não exibíveis enquanto pendentes (invariante):** todos os ~29 itens com `reviewStatus ∈ {pending, legal-review}` — inclui colonização, escravidão, povos indígenas, ditadura (BR-07 → `legal-review`), raça/evolução humana (SCI-22/23), e os recortes de cena ainda em revisão. **Nenhum** aparece no globo/timeline/simultaneidade até aprovação.
13. **Prontos para gabarito (`approved`, baixo risco):** os 38 itens científicos limpos (maioria de SCI-01..21) + marcos não sensíveis (HIST-19 Apollo, HIST-20 WWW, SCENE-01/07/08). **Gabarito-ouro recomendado:** SCI-01 (Big Bang), SCI-13 (GOE), SCI-19 (Pangeia), SCI-21 (K-Pg) e a cena de 1789 — exemplificam fato × hipótese × reconstrução × ClaimSet × simultaneidade. **Lacunas a sanar na 4C:** poucos `Concept`/`Entity`/`Place`/`Region` como **itens completos** (hoje majoritariamente nós referenciados); promover `concept:tectonica-placas`, `concept:guerra-fria`, `concept:expansao-universo`, e Places-chave (Paris, Minas Gerais, Chicxulub) a itens próprios.

---

## 10. Próximos passos para a Etapa 4C (Tarefa 10)

A Etapa 4B entregou o **padrão** (não o volume): template validado, 70 itens-piloto, 7 ClaimSets, cena de 1789, malha de relações e vocabulário testado. A **Etapa 4C** deve, sem ainda buscar exaustividade:

1. **Sanar as lacunas de tipo:** criar `Concept`/`Entity`/`Place`/`Region` como **itens completos** (não só nós de aresta) — começar pelos referenciados (`concept:tectonica-placas`, `concept:guerra-fria`, `concept:expansao-universo`; Places Paris/Minas Gerais/Chicxulub) e corrigir a referência dangling `IND-05`→`IND-04`.
2. **Concluir o fluxo de revisão (§9 da Etapa 3.1)** dos ~29 itens `pending`/`legal-review`, com os papéis aplicáveis (científica, historiográfica, pedagógica, faixa, jurídica/LGPD, acessibilidade, mídia, vieses), e migrar BR-07 para `legal-review`.
3. **Aplicar os ajustes de vocabulário** validados na Tarefa 7 (controlar `evidenceLevel` com `tradição/registro oral`; depreciar `controvérsia` como `claimType`; formalizar `possibilitou`/`decorreu-de` e os modificadores de `TimePrecision`).
4. **Adensar cada bloco da espinha** de poucos itens exemplares para uma cobertura mínima consistente (ainda **estrutural**, não enciclopédica), sempre com os três paralelos crescendo junto.
5. **Confirmar fontes por asset** (`PENDENTE_CONFIRMACAO_FONTE`) e fechar os refinamentos temporais/espaciais abertos, sem inventar precisão.
6. **Povoar uma primeira leva da camada 24 (Mídia)** sob o regime `natureLabel`/licença-por-asset, para validar de fato esse vocabulário (não exercitado a fundo aqui).
7. **Encaminhar à modelagem** (não resolver na 4C) as questões estruturais que o piloto reexpôs: `OceanographicState` dedicado? datum do eixo (1950 BP × J2000)?

**O que a 4C explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (Etapas 1/1.1) ou política editorial (Etapa 3.1).

---

*Documento de entrega da Etapa 4B, sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1 e a arquitetura das camadas (Etapa 4A). Entrega o primeiro lote-piloto controlado e auditável (70 itens conceituais), com template, lotes científico e humano/histórico, três paralelos obrigatórios, cena canônica de 1789, sete ClaimSets, validação de vocabulário, relationship graph mínimo e relatório de qualidade. Não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula e não desenha pipeline técnico. Próxima etapa, quando solicitada: Etapa 4C — adensamento estrutural, conclusão de revisões, itens Concept/Entity/Place/Region e primeira leva de mídia.*
