# Etapa 4E — Cena Canônica de Tempo Profundo: 2,4 Ga / Grande Evento de Oxidação

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4E · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A), o lote-piloto P0 (Etapa 4B), a normalização/entidades de referência (Etapa 4C) e a cena ponta-a-ponta de 1789 (Etapa 4D) · 12/06/2026
**Escopo desta etapa (e seus limites):** replicar o padrão de cena ponta-a-ponta em um **recorte de tempo profundo** — provar que *"O que acontecia na Terra há ~2,4 bilhões de anos?"* funciona **antes** da história humana, das civilizações, dos países e das fontes documentais. Foco: **Grande Evento de Oxidação (GOE)**. Conforme solicitado, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** cria milhares de eventos, **não** usa Wikidata/Wikipedia como autoridade, **não** copia texto de fontes, **não** usa mídia como evidência factual, **não** inventa composição atmosférica precisa e **não** inventa paleomapa.

**O que herda e respeita.** Os nós de 4B (SCI-09 `state:atmosfera-primitiva`, SCI-12 `proc:fotossintese-oxigenica`, SCI-13 `proc:goe`, SCI-14 `evt:surgimento-eucariontes`) e de 4C (`concept:atmosfera-anoxica`, `concept:fotossintese-oxigenica`, `concept:oxigenacao-atmosferica`, `concept:tectonica-placas`, `concept:supercontinente`, `entity:cianobacterias`, `entity:terra`, `region:pangeia`/`region:rodinia` — **excluídas** desta cena por anacronismo). Itens reusados são referenciados e aprofundados; novos seguem o template.

> **Diferencial que esta cena prova:** o sistema **não** serve só para história humana. Ele representa uma **Terra profunda** — sem documentos, sem países, sem fronteiras, sem humanos — usando evidências científicas, proxies geoquímicos, reconstruções modeladas e **incerteza honesta**. 1789 provou simultaneidade **histórica**; 2,4 Ga prova simultaneidade **planetária profunda**.

> **Nova dimensão de risco nesta cena: `scientificRisk`.** Em tempo profundo o risco dominante **não** é editorial (não há sensibilidade humana direta — salvo o cruzamento com negacionismo de idade da Terra, tratado **fora** de ClaimSet, como o Big Bang), e sim **científico**: magnitude, ritmo, datas e paleogeografia carregam incerteza alta.

---

## Sumário

1. Objeto conceitual da cena 2,4 Ga / GOE (Tarefa 1)
2. Itens centrais da cena (Tarefa 2)
3. States planetários da cena (Tarefa 3)
4. Evidências e claims geoquímicos (Tarefa 4)
5. ClaimSets e incertezas (Tarefa 5)
6. Anacronismo espacial em tempo profundo (Tarefa 6)
7. Relationship Graph da cena (Tarefa 7)
8. Globo/mapa da cena (Tarefa 8)
9. Timeline da cena (Tarefa 9)
10. Dossiê da cena (Tarefa 10)
11. Relatório de qualidade da cena (Tarefa 11)
12. Próximos passos para a Etapa 4F (Tarefa 12)

---

## 1. Objeto conceitual da cena 2,4 Ga / GOE (Tarefa 1)

**`scene:earth-2-4ga-great-oxidation-event`**
- **id:** `scene:earth-2-4ga-great-oxidation-event` · **pilotCode:** SCENE-GOE · **version:** 1.0
- **título:** A Terra há ~2,4 Ga — o Grande Evento de Oxidação
- **foco principal:** Grande Evento de Oxidação (`proc:goe`, SCI-13)
- **TimeRange:** **~2,4 Ga** (núcleo), com janela ampla ~2,5–2,0 Ga · **TimePrecision:** `Ga` (faixa) — **"2,4 Ga" é uma aproximação de tempo profundo, não uma data histórica exata**
- **escopo espacial:** **planetário/global** — não há regiões políticas; a localização fina é incerta e modelada
- **camadas ativadas:** 4 Atmosfera · 5 Clima · 7 Oceanos · 6 Tectônica/paleogeografia · 8 Vida/evolução · 9 Paleobiologia · 25 Fontes/meta
- **itens centrais:** `proc:goe`, `state:atmosfera-primitiva` (pré-GOE), `proc:fotossintese-oxigenica`, `entity:cianobacterias`, `concept:oxigenacao-atmosferica`, `concept:formacoes-ferriferas-bandadas`, `state:oceanos-ferruginosos`, `state:biota-microbiana-2-4ga`, `entity:organismos-anaerobios`, `entity:terra`
- **itens contextuais:** `state:clima-goe` (glaciações huronianas), `state:paleogeografia-2-4ga` (incerta), `state:geoquimica-2-4ga`, `concept:proterozoico`, `concept:proxy-geoquimico`, `place:*` (localidades de evidência atual)
- **itens sensíveis:** **nenhum** em sentido editorial humano (sem Leis 10.639/11.645). **Exceção:** o cruzamento com **negacionismo de idade da Terra/evolução** é tratado **fora** de ClaimSet (como o Big Bang).
- **Claims principais da cena:** "Há ~2,4 Ga o oxigênio livre subiu significativamente na atmosfera da Terra, reorganizando atmosfera, oceanos e biosfera" — `inferência científica`, **consenso amplo** para o fato; detalhes em ClaimSets/UncertaintyProfiles.
- **ClaimSets envolvidos:** `claimset:goe-timing-fases`, `claimset:goe-ritmo-oxigenacao`, `claimset:goe-causas`, `claimset:goe-glaciacoes`, `claimset:goe-impacto-anaerobios`, `claimset:kenorland-existencia` · **UncertaintyProfiles:** `uncertaintyprofile:goe-magnitude-o2`, `uncertaintyprofile:paleogeografia-2-4ga`
- **fontes A/B necessárias:** NOAA/NCEI Paleo (A, PD); PBDB (A); Macrostrat/ICS (escala, A/B); USGS (A); geociências revisadas (A/B); EarthByte/GPlates (paleogeografia, A, CC BY)
- **reviewStatus (da cena):** núcleo factual `approved` (revisão científica do piloto); paleogeografia, magnitude e datas finas `pending` por incerteza científica
- **risco editorial:** **baixo** (sem sensibilidade humana; só a nota antinegacionismo)
- **risco de licença:** **baixo** (fontes verdes; risco 0–1; paleogeografia CC BY = 1; Deep Time Maps **proibido**)
- **risco científico:** **alto** — magnitude do O₂, ritmo, datas exatas e paleogeografia são incertos; **a cena deve exibir essa incerteza, não escondê-la**
- **timeline:** zoom em ~2,4 Ga, janela ampla do GOE; processos longos e States de fundo, **sem eventos pontuais datados** (ver §9)
- **globo/mapa:** globo **esquemático** com halo atmosférico em transição e oceanos ferruginosos didáticos; paleogeografia rotulada como reconstrução/pendente (ver §8)
- **dossiê:** 18 blocos com ênfase em "como sabemos disso" (ver §10)
- **itens não exibíveis enquanto pending:** paleogeografia 2,4 Ga, existência de Kenorland, magnitude precisa de O₂ e datas finas — aparecem **mediados** (rótulo "reconstrução/incerto") ou ocultos, **nunca** como fato cru

---

## 2. Itens centrais da cena (Tarefa 2)

Itens do foco geoquímico-planetário. Existentes (SCI-09/12/13, Concepts e Entities de 4C) são referenciados e aprofundados; novos recebem template. **Regra mantida:** separar **fato consolidado** (aumento importante de O₂) · **evidência** (proxies geoquímicos) · **hipótese** (detalhes causais e ritmos) · **incerteza** (magnitude, duração, variação regional).

**`proc:goe`** *(SCI-13 — existente, aprofundado)*
- tipo: `Process` · camadaP: 4 Atmosfera · camadasS: 8, 5, 7, 25 · título: Grande Evento de Oxidação
- TimeRange: ~2,4–2,0 Ga · Place/Region: global · TimePrecision: `Ga` (faixa)
- ClaimPrinc: "Por volta de ~2,4 Ga o O₂ livre subiu de níveis vestigiais para uma fração pequena mas não-desprezível, alterando a química do planeta" — `inferência científica`, **consenso amplo** (fato); magnitude/ritmo em UncertaintyProfile/ClaimSet · ClaimTemp: ~2,4 Ga (faixa) — `inferência` · ClaimEsp: global.
- Source: NOAA/NCEI Paleo (A); PBDB (A) `PENDENTE_CONFIRMACAO_FONTE` · conf: **alta** (fato), **média** (detalhes) · evid: `registro material` (proxies geoquímicos) · uncert: alta em magnitude/ritmo, baixa na existência do aumento.
- review: `approved` (fato) · scientificRisk: **médio-alto** · editorialRisk: baixo (idade/evolução × negacionismo, **fora** de ClaimSet) · licenseRisk: 0–1.
- rels: **`decorreu-de` `proc:fotossintese-oxigenica`**; `afetou` `state:atmosfera-primitiva`, `state:oceanos-ferruginosos`, `state:biota-microbiana-2-4ga`; `qualificado-por` `claimset:goe-causas`, `uncertaintyprofile:goe-magnitude-o2`.
- timeline: **processo longo** (faixa ~2,4–2,0 Ga), não ponto · globe: troca o `AtmosphereState` (halo) · simultaneidade: **âncora** da cena.

**`state:atmosfera-primitiva`** *(SCI-09 — existente)* — AtmosphereState **pré-GOE**
- tipo: `State` (`AtmosphereState`) · camadaP: 4 · camadasS: 5, 8 · título: Atmosfera anóxica pré-GOE
- TimeRange: ~Hadeano–~2,4 Ga · Place/Region: global · ClaimPrinc: "Antes do GOE, a atmosfera tinha O₂ livre vestigial (anóxica)" — `inferência científica`, alta · evid: `registro material` (ausência de O₂ inferida de minerais detríticos sensíveis ao redox) · uncert: alta na composição exata (faixa, **nunca número seco**).
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 0.
- rels: `relacionado-a` `concept:atmosfera-anoxica`; **transição→** via `proc:goe` para `state:atmosfera-oxigenacao-goe`.
- timeline: State de fundo (antes) · globe: halo anóxico · simultaneidade: o "antes" da cena.

**`proc:fotossintese-oxigenica`** *(SCI-12 — existente, aprofundado)*
- tipo: `Process` · camadaP: 8 Vida/evolução · camadasS: 4 · título: Fotossíntese oxigênica
- TimeRange: estabelecida por ~2,4 Ga (possivelmente antes) · Place/Region: oceânico/global · ClaimPrinc: "Cianobactérias passaram a produzir O₂ por fotossíntese, fornecendo a fonte do oxigênio do GOE" — `inferência científica`, alta · evid: `registro material` + `inferência indireta` · uncert: média na data de origem (debate sobre "lag" entre origem e GOE).
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: **`causou` `proc:goe`**; `realizada-por` `entity:cianobacterias`.
- timeline: processo (antes/durante) · globe: overlay biótico · simultaneidade: a **causa biológica** do GOE.

**`entity:cianobacterias`** *(4C — existente)*
- tipo: `Entity` (grupo de microrganismos) · camadaP: 8 · TimeRange: ~Arqueano–presente · ClaimPrinc: "Bactérias fotossintetizantes produtoras de O₂, motor biológico da oxigenação" — `inferência científica`, alta · evid: `registro material`.
- review: `approved` · scientificRisk: baixo · editorialRisk: baixo · licenseRisk: 1.
- rels: `realiza` `proc:fotossintese-oxigenica`; `relacionado-a` `state:biota-microbiana-2-4ga`.
- simultaneidade: o **agente vivo** da cena (sem humanos — a vida é microbiana).

**`concept:oxigenacao-atmosferica`** *(4C — existente)* — aprofundado como ideia estruturante
- ClaimPrinc: "Acúmulo de O₂ livre na atmosfera ao longo do tempo geológico" — `inferência científica`, alta · rels: `explica` `proc:goe`; `decorreu-de` `concept:fotossintese-oxigenica`. · review: `approved`.

**`concept:formacoes-ferriferas-bandadas`** *(novo)* · Formações ferríferas bandadas (BIFs)
- knowledgeItemId: `concept:formacoes-ferriferas-bandadas` · tipo: `Concept` · camadaP: 9 Paleobiologia/geologia · camadasS: 7, 4
- def: rochas sedimentares em bandas de óxido de ferro e sílica, formadas em oceanos com ferro dissolvido. · ClaimPrinc: "As BIFs registram a interação entre oxigênio e ferro dissolvido nos oceanos antigos" — `inferência científica`, alta · Source: USGS/geociências (A/B) · conf: alta · evid: `registro material` · uncert: mecanismos de bandeamento debatidos.
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: `evidência-de` `proc:goe` e `state:oceanos-ferruginosos`; resultam de `proc:deposicao-bif`. · ling. escolar: "as listras de ferro são uma pista química", não decoração.

**`proc:deposicao-bif`** *(novo)* · Deposição de formações ferríferas bandadas
- knowledgeItemId: `proc:deposicao-bif` · tipo: `Process` · camadaP: 7 Oceanos · camadasS: 9, 4 · TimeRange: pico ~2,5–1,8 Ga · Place/Region: bacias oceânicas (hoje: Hamersley, Transvaal etc.)
- ClaimPrinc: "A precipitação de óxidos de ferro formou grandes BIFs quando o O₂ encontrou o ferro dissolvido" — `inferência científica`, alta · evid: `registro material` · uncert: média (papel do O₂ vs micróbios anaeróbios oxidantes de ferro).
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: produz `concept:formacoes-ferriferas-bandadas`; `evidencia` `proc:goe`. · simultaneidade: o **registro** do processo no fundo do mar.

**`state:oceanos-ferruginosos`** *(novo)* — OceanState provisório (ver §3)
- knowledgeItemId: `state:oceanos-ferruginosos` · tipo: `State` (OceanographicState **proposto**) · camadaP: 7 Oceanos · camadasS: 4, 9 · título: Oceanos ricos em ferro dissolvido
- TimeRange: ~Arqueano–~Paleoproterozoico · Place/Region: global · ClaimPrinc: "Antes/durante o GOE, os oceanos eram amplamente anóxicos e ricos em ferro dissolvido (ferruginosos)" — `inferência científica`, média-alta · evid: `registro material` (BIFs, especiação de ferro) · uncert: alta na variação regional/temporal.
- review: `pending` (`PENDENTE_REVISAO_HUMANA` não se aplica; aqui = revisão científica) · scientificRisk: médio-alto · editorialRisk: baixo · licenseRisk: 1.
- rels: `afetado-por` `proc:goe`; registrado por `proc:deposicao-bif`. · representationType: **reconstrução modelada** (didática). · timeline: State de fundo · globe: oceanos esverdeados/ferruginosos **didáticos** (rótulo). · simultaneidade: a camada **oceânica** da cena.

**`state:biota-microbiana-2-4ga`** *(novo)* — BiomeState microbiano
- knowledgeItemId: `state:biota-microbiana-2-4ga` · tipo: `State` (`BiomeState`) · camadaP: 8 Vida/evolução · camadasS: 9 · título: Biosfera microbiana ~2,4 Ga
- TimeRange: ~Arqueano–Paleoproterozoico · Place/Region: oceânico/global · ClaimPrinc: "A vida era exclusivamente microbiana (procariontes), com cianobactérias e anaeróbios" — `inferência científica`, alta · evid: `registro material` (microfósseis, estromatólitos) + `inferência indireta` (biomarcadores contestados) · uncert: média.
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: contém `entity:cianobacterias`, `entity:organismos-anaerobios`; `afetada-por` `proc:goe`. · simultaneidade: a **biosfera** da cena (sem plantas, animais ou humanos).

**`entity:organismos-anaerobios`** *(novo)*
- knowledgeItemId: `entity:organismos-anaerobios` · tipo: `Entity` (grupo de microrganismos) · camadaP: 8 · TimeRange: ~Arqueano–presente · ClaimPrinc: "Microrganismos que viviam sem O₂ e para os quais o oxigênio podia ser tóxico" — `inferência científica`, alta · evid: `inferência indireta` (fisiologia atual + filogenia) · uncert: alta sobre o real impacto demográfico do GOE.
- review: `approved` · scientificRisk: médio · editorialRisk: baixo · licenseRisk: 1.
- rels: `afetado-por` `proc:goe` (ver `claimset:goe-impacto-anaerobios`). · simultaneidade: quem **sofreu** a mudança.

**`entity:terra`** *(4C — existente)* — Terra ~2,4 Ga
- ClaimPrinc: "O planeta Terra, no Paleoproterozoico inicial, em transição química" — `inferência científica` · rels: palco de toda a cena; `relacionado-a` `state:paleogeografia-2-4ga`. · review: `approved`.

**`concept:proterozoico`** *(novo, leve)* · Proterozoico (inicial)
- tipo: `Concept` · camadaP: 3/25 · def: éon geológico (~2,5 Ga–541 Ma); o GOE marca seu início. · ClaimPrinc: "O GOE situa-se no início do Proterozoico" — `fato documentado` (escala ICS) · Source: ICS via fato (A) · review: `approved` · scientificRisk: baixo. · rels: `contextualiza` `proc:goe`. · ling.: nome de éon, referência de escala — não "era dos micróbios" simplista.

---

## 3. States planetários da cena (Tarefa 3)

Os States representam **condições do planeta** num intervalo — a espinha dorsal de uma cena de tempo profundo (que, ao contrário de 1789, é dominada por States e processos longos, não por eventos pontuais). `representationType ∈ {medição, reconstrução modelada, aproximação didática}`.

| State (`knowledgeItemId`) | TimeRange | camadas | claims mínimos | fontes | conf | evid | uncertaintyProfile | representationType | globeBehavior | timelineBehavior | review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `state:atmosfera-primitiva` (AtmosphereState pré-GOE) | ~Hadeano–2,4 Ga | 4, 8 | "atmosfera anóxica, O₂ vestigial" | NOAA Paleo (A) | alta | registro material | composição exata incerta (faixa) | reconstrução modelada | halo anóxico | State de fundo (antes) | approved |
| `state:atmosfera-oxigenacao-goe` *(novo)* (AtmosphereState durante) | ~2,4–2,0 Ga | 4, 5 | "O₂ sobe a fração pequena mas não-desprezível" | NOAA Paleo (A) | alta (fato) / média (nível) | registro material | **magnitude** em `uncertaintyprofile:goe-magnitude-o2` | reconstrução modelada | halo em transição (nota incerteza) | State de transição | approved (fato) |
| `state:oceanos-ferruginosos` *(novo)* (**OceanographicState proposto**) | ~Arqueano–Paleoprot. | 7, 4, 9 | "oceanos anóxicos, ricos em ferro dissolvido" | USGS/geociências (A/B) | média-alta | registro material (BIFs) | variação regional alta | reconstrução modelada | oceanos ferruginosos didáticos | State de fundo | pending (científica) |
| `state:clima-goe` *(novo)* (ClimateState) | ~2,4–2,2 Ga | 5, 4 | "glaciações huronianas no período, possivelmente ligadas ao GOE" | NOAA Paleo/geociências (A/B) | média | registro material (diamictitos) | relação causal com GOE em ClaimSet | reconstrução modelada | overlay glacial (didático) | State de fundo | pending |
| `state:paleogeografia-2-4ga` *(novo)* (PaleogeographicState) | ~2,4 Ga | 6 | "crátons arqueanos dispersos; configuração **muito incerta**" | EarthByte/GPlates (A, CC BY) | **baixa** | dado modelado | **alta** (`uncertaintyprofile:paleogeografia-2-4ga`) | reconstrução modelada / **esquemático** | crátons esquemáticos rotulados | State de fundo | pending (incerteza alta) |
| `state:biota-microbiana-2-4ga` *(novo)* (BiomeState) | ~Arqueano–Paleoprot. | 8, 9 | "vida exclusivamente microbiana" | PBDB (A) | alta | registro material | média | reconstrução modelada | overlay biótico microbiano | State de fundo | approved |
| `state:geoquimica-2-4ga` *(novo)* (**GeochemicalState proposto**) | ~2,5–2,0 Ga | 25, 7, 4 | "assinaturas geoquímicas (S, Fe, redox) registram a oxigenação" | NOAA Paleo/literatura (A/B) | alta (proxies) | registro material | proxies com margens | medição (de proxies) | painel de proxies (não geográfico) | painel de fundo | approved |

**EarthSystemState — decisão.** A cena pediu, opcionalmente, um `EarthSystemState` para "representar a cena inteira". **Recomendação: não criar um novo tipo** — o próprio objeto `scene:earth-2-4ga-great-oxidation-event` **já cumpre** esse papel (é a visão integrada atmosfera+oceano+clima+tectônica+biosfera). Um `EarthSystemState` seria redundante com a cena.

**OceanographicState — decisão (responde à pendência herdada da 4A/4B).** A cena **consegue funcionar** sem um `OceanographicState` oficial — `state:oceanos-ferruginosos` pode, no limite, ser servido por `PaleogeographicState`+`ClimateState`+`BiomeState`. **Porém**, a química redox/ferro do oceano é **central** a esta cena e fica mal acomodada nesses tipos. **Esta etapa recomenda formalmente a criação de `OceanographicState`** (e, secundariamente, de `GeochemicalState`) — mas **não** o cria aqui: é decisão de **modelagem (reabertura controlada da Etapa 2)**, que escalo, não executo. Enquanto não houver decisão, `state:oceanos-ferruginosos` e `state:geoquimica-2-4ga` ficam como **propostas conceituais rotuladas**.

---

## 4. Evidências e claims geoquímicos (Tarefa 4)

O coração epistêmico da cena: **"como sabemos disso?"** sem nenhuma fonte documental humana. Cada linha é um claim de **evidência** (texto próprio, jamais transcrição), classificado por tipo, com sua relação ao GOE e seu caráter (direta/proxy/inferência/modelo).

| # | Claim (texto próprio) | claimType | EvidenceLevel | Conf | Fonte A/B | Incerteza | Relação com o GOE | Caráter | No dossiê |
|---|---|---|---|---|---|---|---|---|---|
| E1 | "Grandes formações ferríferas bandadas registram oceanos com ferro dissolvido interagindo com oxigênio" | `inferência científica` | registro material | alta | USGS/geociências (A/B) | mecanismo de bandeamento debatido | evidência da oxigenação oceânica | **proxy** | bloco "Oceanos e ferro" |
| E2 | "O desaparecimento do fracionamento isotópico de enxofre independente de massa marca a subida do O₂ atmosférico" | `inferência científica` | registro material | **alta** | NOAA Paleo/literatura (A/B) | datação fina varia por bacia | **proxy-chave** do timing do GOE | **proxy** | bloco "Como sabemos disso" |
| E3 | "A perda de minerais detríticos sensíveis ao redox (que só sobrevivem sem O₂) indica atmosfera antes anóxica" | `inferência científica` | registro material | alta | geociências (A/B) | preservação seletiva | evidência do estado **pré**-GOE | **proxy** | bloco "Atmosfera antes e durante" |
| E4 | "Elementos sensíveis ao redox (ex.: molibdênio, cromo) variam conforme a disponibilidade de oxigênio" | `inferência científica` | registro material | média-alta | literatura geoquímica (A/B) | calibração de proxies | proxy de níveis de O₂ | **proxy** | bloco "Evidências geoquímicas" |
| E5 | "Microfósseis e estromatólitos indicam atividade microbiana (incl. possivelmente fotossintética)" | `inferência científica` | registro material | média | PBDB (A) | biomarcadores moleculares **contestados** | evidência da fonte biológica de O₂ | **proxy + inferência** | bloco "Vida microbiana" |
| E6 | "A especiação de ferro e outros indicadores apontam mudança no estado redox dos oceanos" | `inferência científica` | registro material | média-alta | geociências (A/B) | variação regional | evidência de mudança oceânica | **proxy** | bloco "Oceanos e ferro" |
| E7 | "Depósitos glaciais (diamictitos) do período sugerem glaciações huronianas, possivelmente associadas ao GOE" | `hipótese`/`inferência` | registro material | média | NOAA Paleo/geociências (A/B) | associação causal incerta | possível **consequência climática** | **proxy + hipótese** | bloco "Consequências climáticas" |

**Princípio (Etapa 3.1 aplicado ao tempo profundo):** o produto exibe a **cadeia de inferência** — "a rocha X, no lugar Y, com a assinatura Z, leva a concluir W, com confiança C". Nenhum proxy é apresentado como observação direta; nenhum é escondido sob "os cientistas dizem". A mídia (foto de afloramento, gráfico isotópico) **ilustra**, nunca **prova** (mídia ≠ evidência factual).

---

## 5. ClaimSets e incertezas da cena (Tarefa 5)

Distinção central: **ClaimSet** (claims discretos concorrentes legítimos) × **UncertaintyProfile** (faixa/margem em torno de um valor, sem "lados" discretos). Regra: **não** transformar incerteza legítima em "não sabemos nada"; distinguir **consenso geral** de **incerteza interna**.

**`claimset:goe-timing-fases`** *(novo)* — ClaimSet
- tema: timing exato do início e das fases do GOE · consensusStatus: **debate acadêmico** · claims: (a) subida principal ~2,4–2,3 Ga; (b) "sopros" de O₂ anteriores (whiffs) no Arqueano tardio; (c) fases múltiplas com recuos · conf por claim: alta (existência), média (limites finos) · fontes: NOAA Paleo/literatura (A/B) · review: pending · nota científica: o **fato** (subida) é consenso; as **datas/fases** debatem-se · impacto: exibir faixa e fases, não data única.

**`claimset:goe-ritmo-oxigenacao`** *(novo)* — ClaimSet
- tema: ritmo da oxigenação (gradual × em degraus × "yo-yo") · consensusStatus: **hipóteses concorrentes** · claims: (a) subida relativamente rápida; (b) gradual; (c) oscilante com avanços e recuos · conf: média · fontes: literatura geoquímica (A/B) · review: pending · nota: ritmo ≠ existência · impacto: animação/curva exibe **cenários**, não uma curva única.

**`uncertaintyprofile:goe-magnitude-o2`** *(novo)* — **UncertaintyProfile** (não ClaimSet)
- tema: magnitude do O₂ atmosférico após o GOE · natureza: **faixa**, não claims discretos · consensusStatus: **consenso amplo** de que subiu; **incerteza** sobre **quanto** · claims: O₂ passou de vestigial para uma fração ainda pequena do nível atual — **faixa ampla**, sem número seco · conf: alta (subiu), baixa (valor exato) · fontes: NOAA Paleo/literatura (A/B) · review: pending · nota: **não inventar composição precisa** · impacto: exibir como **faixa com barras de incerteza**.

**`claimset:goe-causas`** *(novo)* — ClaimSet
- tema: causas principais da oxigenação · consensusStatus: **hipóteses concorrentes** · claims: (a) evolução/expansão da fotossíntese oxigênica; (b) mudanças nos **sumidouros** de O₂ (menos gases vulcânicos redutores); (c) fatores tectônicos/soterramento de carbono orgânico · conf: média · **sem equivalência:** criacionismo/jovem-Terra (negacionismo, **fora** do ClaimSet) · fontes: geociências (A/B) · review: pending · nota: provavelmente **combinação** de fatores · impacto: causas lado a lado, com pesos.

**`claimset:goe-glaciacoes`** *(novo)* — ClaimSet
- tema: relação entre GOE e glaciações huronianas · consensusStatus: **hipóteses concorrentes** · claims: (a) a subida de O₂ teria reduzido metano (forte gás-estufa), resfriando o planeta ("colapso do metano"); (b) glaciações com outras causas, coincidência temporal · conf: média · fontes: NOAA Paleo/geociências (A/B) · review: pending · nota: associação **plausível**, não provada · impacto: exibir como hipótese ligada, com nota.

**`claimset:goe-impacto-anaerobios`** *(novo)* — ClaimSet/UncertaintyProfile híbrido
- tema: impacto do O₂ sobre organismos anaeróbios ("catástrofe do oxigênio") · consensusStatus: **debate acadêmico** · claims: (a) extinção/retração significativa de anaeróbios ("holocausto do oxigênio"); (b) impacto mais modesto, com refúgios anóxicos persistentes · conf: média · fontes: literatura (A/B) · review: pending · nota: o termo "catástrofe" é **didático/hipotético**, não fato estabelecido · impacto: evitar dramatização; exibir as duas leituras.

**`claimset:kenorland-existencia`** *(novo)* — ClaimSet (cautela **extrema**)
- tema: existência/configuração de um supercontinente arqueano-paleoproterozoico (ex.: "Kenorland") em ~2,4 Ga · consensusStatus: **hipóteses concorrentes / insuficiência de evidência** · claims: (a) existência de um supercontinente/superCráton; (b) crátons dispersos sem um único supercontinente; (c) reconstruções alternativas incompatíveis · conf: **baixa** · fontes: EarthByte/GPlates/literatura (A/B) · review: pending · nota: tratar com **cautela extrema**; **não** afirmar Kenorland como fato · impacto: paleogeografia exibida como **esquema rotulado**, com aviso de baixa confiança.

**`uncertaintyprofile:paleogeografia-2-4ga`** *(novo)* — **UncertaintyProfile**
- tema: posições continentais a ~2,4 Ga · natureza: incerteza **muito alta** em todas as posições · consensusStatus: **insuficiência de evidência** para detalhe fino · conf: baixa · fontes: EarthByte/GPlates (A, CC BY) · review: pending · nota: **não inventar paleomapa**; quando não houver dado, globo **esquemático** · impacto: globo paleogeográfico sempre rotulado "reconstrução modelada / incerta".

---

## 6. Anacronismo espacial em tempo profundo (Tarefa 6)

Aqui o `concept:modern-correspondence` de 1789 **não se aplica** do mesmo modo: não há países, fronteiras ou continentes modernos para "corresponder". O risco é projetar a geografia atual sobre um planeta irreconhecível. Sete casos obrigatórios.

| Caso | Risco de anacronismo | Correção conceitual | Place/Region correto | No dossiê | No globo/mapa |
|---|---|---|---|---|---|
| 1. Não existem países | falar de "Brasil/EUA/China" há 2,4 Ga | só há um **planeta**; nenhuma entidade política | nenhum `region:` político | aviso "sem países, sem fronteiras" | sem rótulos nacionais |
| 2. Continentes modernos | mostrar América/África atuais | massas continentais eram **outras** (crátons dispersos) | `state:paleogeografia-2-4ga` (esquemático) | "os continentes de hoje não existiam" | crátons esquemáticos, não continentes atuais |
| 3. Brasil/África/França como regiões | usar recortes modernos | **anacrônicos** — não existiam | nenhum | omitir nomes modernos | omitir |
| 4. Paleogeografia | exibir paleomapa como fato | é **reconstrução modelada** de **baixa** confiança | `state:paleogeografia-2-4ga` + `uncertaintyprofile:paleogeografia-2-4ga` | rótulo "reconstrução / incerta" | sempre rotulado, ou globo esquemático |
| 5. Lugar atual da rocha ≠ lugar original | supor que onde a rocha está hoje é onde "aconteceu" | placas moveram-se; a posição original difere | localidade atual (`place:*`) **separada** da posição paleo | "encontrada **hoje** em X; posição antiga incerta" | marcador atual ≠ posição paleogeográfica |
| 6. Depósitos atuais = janelas | tratar afloramento como "o evento" | depósitos são **registros** de processos antigos | `place:bacia-hamersley` etc. como **evidência** | "janela para o passado" | marcadores "onde encontramos evidências hoje" |
| 7. Sem geometria validada | inventar geometria | se não há dado, **globo esquemático** | `PENDENTE_REFINAMENTO_ESPACIAL` | aviso explícito | esquema, nunca paleomapa inventado |

**Exclusões obrigatórias por anacronismo temporal (análogo ao caso Mali em 1789):**
- **Rodinia** (`region:rodinia`, ~1,3–0,75 Ga) — **NÃO** é simultânea: é ~1,3 **bilhão** de anos **posterior** ao GOE. Excluída da cena; só aparece como "muito depois" se o usuário navegar para frente.
- **Pangeia** (`region:pangeia`/`state:pangeia`, ~335–175 Ma) — idem, ~2 bilhões de anos depois. Excluída.
- **Nuna/Columbia** (~1,8–1,6 Ga) — também **posterior** ao GOE; não simultânea.
- O único supercontinente que **poderia** tocar ~2,4 Ga é o hipotético **Kenorland** — e mesmo esse entra apenas via `claimset:kenorland-existencia`, com **cautela extrema** e baixa confiança, **nunca** como fato.

> **Localidades de evidência (Places) — "onde encontramos hoje", não "onde aconteceu":** `place:bacia-hamersley` (Austrália; BIFs), `place:supergrupo-huroniano` (Canadá; glaciações/registro), `place:bacia-transvaal` (África do Sul; registro do GOE). Cada um marcado como **janela atual** para o processo antigo, com a ressalva de que sua posição há 2,4 Ga era outra (`PENDENTE_REFINAMENTO_ESPACIAL`).

---

## 7. Relationship Graph da cena (Tarefa 7)

Malha específica de 2,4 Ga / GOE. Arestas afirmativas **são claims** (evidência/confiança); cada uma carrega `uncertaintyNote`. Relações projetadas ao futuro (ozônio, eucariontes) recebem cautela explícita.

| relId | sourceItem | relationshipType | targetItem | claim/evidence | conf | review | uncertaintyNote | obs. científica |
|---|---|---|---|---|---|---|---|---|
| rel:G01 | `entity:cianobacterias` | realiza | `proc:fotossintese-oxigenica` | registro material | alta | approved | origem exata debatida | motor biológico |
| rel:G02 | `proc:fotossintese-oxigenica` | causou | `proc:goe` | registro material (proxy) | alta | approved | "lag" origem→GOE incerto | fonte do O₂ |
| rel:G03 | `proc:goe` | afetou | `state:atmosfera-oxigenacao-goe` | proxy (S-MIF) | alta | approved | magnitude incerta | mudança atmosférica |
| rel:G04 | `proc:goe` | afetou | `state:oceanos-ferruginosos` | registro material (BIFs) | média-alta | pending | variação regional | mudança oceânica |
| rel:G05 | O₂ + ferro dissolvido | produziu | `concept:formacoes-ferriferas-bandadas` | registro material | alta | approved | papel de micróbios oxidantes de Fe | BIFs |
| rel:G06 | `proc:goe` | afetou | `entity:organismos-anaerobios` | inferência indireta | média | pending | magnitude do impacto (ver CS) | "catástrofe do O₂" (hipótese) |
| rel:G07 | `proc:goe` | possibilitou (futuro) | respiração aeróbia complexa | inferência | média | pending | **muito posterior**; não imediato | cautela: consequência distante |
| rel:G08 | `proc:goe` | possibilitou (futuro) | `evt:surgimento-eucariontes` (SCI-14, ~1,6–2,1 Ga) | inferência | média | pending | **posterior**; nexo não automático | cautela explícita |
| rel:G09 | `proc:goe` | possibilitou (futuro) | camada de ozônio | inferência | baixa-média | pending | ozônio significativo é **bem posterior** | cautela: não no GOE |
| rel:G10 | `state:paleogeografia-2-4ga` | contextualiza | `state:oceanos-ferruginosos`, `state:atmosfera-oxigenacao-goe` | dado modelado | baixa | pending | **paleogeografia muito incerta** | pano de fundo incerto |
| rel:G11 | `concept:proxy-geoquimico` | evidencia | `proc:goe` | registro material | alta | approved | calibração de proxies | "como sabemos" |
| rel:G12 | `proc:goe` | relacionado-a (hipótese) | `state:clima-goe` (glaciações huronianas) | proxy + hipótese | média | pending | associação causal incerta (CS) | colapso do metano? |
| rel:G13 | `entity:imperio-mali`/`region:rodinia` | **NÃO-simultâneo-de** | cena 2,4 Ga | — | — | — | exclusão por anacronismo | registro de que **não** entram |

> **Cautela com o futuro (G07–G09):** ozônio, eucariontes e respiração complexa são **consequências distantes** (centenas de milhões a bilhões de anos depois), não efeitos imediatos do GOE. As arestas existem, mas com `confidenceLevel` reduzido e nota de que **não** são contemporâneas da cena — exibidas só no botão "ver consequências futuras". **Nenhuma** aresta trata Rodinia/Pangeia como simultâneas (G13 registra a exclusão).

---

## 8. Globo/mapa da cena 2,4 Ga (Tarefa 8)

Descrição **conceitual** (sem UI final; sem geometria inventada; **sem paleomapa inventado**). O globo de tempo profundo é, por padrão, **mais esquemático e mais rotulado** que o de 1789.

- **Foco inicial:** o **planeta inteiro** (não uma região) — a cena é global por natureza.
- **Tipo de globo:** **esquemático/estilizado** quando a paleogeografia é incerta; **reconstrução modelada rotulada** quando houver dado GPlates. Nunca um mapa "realista" não-rotulado.
- **Atmosfera visual:** **halo atmosférico** que transiciona de **anóxico** (pré-GOE) para **levemente oxigenado** (durante), **com barra/nota de incerteza** na transição — a cor é didática, não medição.
- **Oceanos:** representação **didática** de oceanos **ferruginosos** (ricos em ferro), rotulada como reconstrução; não afirmar tom/extensão exatos.
- **Continentes/crátons:** **crátons esquemáticos** dispersos, rotulados "reconstrução incerta" — **sem** continentes modernos, **sem** Kenorland afirmado.
- **Zonas de deposição de ferro:** indicadas de forma **didática** (onde BIFs se formavam), com ressalva de posição paleogeográfica incerta.
- **Camadas ligadas/desligadas:** ligadas — Atmosfera, Oceanos, Biosfera microbiana, Geoquímica (painel de proxies); sob demanda — Paleogeografia (sempre rotulada), Clima (glaciações). Política/Brasil/África/Indígenas: **inexistentes nesta era** (desligadas e indisponíveis).
- **Itens incertos mediados:** paleogeografia, magnitude de O₂, Kenorland → exibidos **mediados** (rótulo "reconstrução / incerto / baixa confiança").
- **Itens pending não exibidos:** `state:paleogeografia-2-4ga`, `claimset:kenorland-existencia` e magnitude precisa não aparecem como fato; aparecem mediados ou ocultos.
- **Níveis de zoom:** (1) planeta/sistema (atmosfera+oceano); (2) processo (deposição de BIF, oxigenação); (3) **localidade de evidência atual** (Hamersley, Huroniano, Transvaal) — neste nível, marcador é "onde encontramos hoje", não "onde aconteceu".
- **Legenda epistemológica:** fato consolidado · proxy · inferência · reconstrução modelada · aproximação didática.
- **Legenda temporal:** "~2,4 Ga (aproximação de tempo profundo)"; faixa do GOE; "antes/durante/depois".
- **Legenda científica:** explica cada proxy (BIF, S-MIF, minerais detríticos, elementos redox) em linguagem acessível.
- **Reconstrução × aproximação didática:** **distinção visual obrigatória** — o que é reconstrução modelada (com dado) difere do que é apenas aproximação didática (sem dado fino); ambos rotulados.

**Obrigatórios presentes:** halo atmosférico anóxico/pré-oxigenação ✓ · transição visual de O₂ com nota de incerteza ✓ · oceanos ricos em ferro (didático) ✓ · ausência de fronteiras modernas ✓ · paleogeografia rotulada como reconstrução/pendente ✓ · marcadores de evidência atual como "onde encontramos hoje", não "onde aconteceu" ✓.

---

## 9. Timeline da cena 2,4 Ga (Tarefa 9)

A timeline de tempo profundo é **dominada por processos longos e States**, **sem eventos pontuais datados** — contraste direto com 1789 (rica em eventos de dia). Distingue **processo longo · State · evidência proxy · hipótese · consequência posterior · ClaimSet · UncertaintyProfile**.

- **Zoom em ~2,4 Ga:** escala em **Ga**, com a etiqueta permanente "aproximação de tempo profundo" — sem resolução de dia/ano (que não existe aqui).
- **Janela temporal ampla do GOE:** faixa ~2,5–2,0 Ga exibida como **bloco com bordas difusas** (início/fim incertos), não linha nítida.
- **Atmosfera anóxica anterior:** `state:atmosfera-primitiva` como State de fundo **antes** da faixa.
- **Fotossíntese oxigênica anterior:** `proc:fotossintese-oxigenica` começando **antes** do GOE (com o "lag" marcado como incerto).
- **Fases da oxigenação:** exibidas via `claimset:goe-timing-fases` e `claimset:goe-ritmo-oxigenacao` — **cenários** (gradual/degraus/oscilante), não uma curva única.
- **Eventos posteriores relacionados:** `evt:surgimento-eucariontes` (~1,6–2,1 Ga) e consequências distantes (ozônio, respiração complexa) — claramente **muito depois**, acessíveis por "ver consequências futuras".
- **Incerteza temporal:** bordas difusas e barras de incerteza em **todos** os limites; magnitude via `uncertaintyprofile:goe-magnitude-o2`.
- **Claims e ClaimSets:** ícone de **debate** nos itens com ClaimSet (timing, ritmo, causas, glaciações, anaeróbios, Kenorland); ícone de **faixa** nos UncertaintyProfiles (magnitude, paleogeografia).
- **States de fundo:** atmosfera (pré/durante), oceanos ferruginosos, clima, biosfera microbiana, geoquímica — faixas paralelas sob o processo central.
- **Itens pending ocultos:** paleogeografia e Kenorland não aparecem como fato; mediados ou ocultos.
- **Itens publicáveis exibidos:** o **fato consolidado** (subida de O₂ ~2,4 Ga), a fotossíntese oxigênica, as BIFs e a biosfera microbiana já são exibíveis (revisão científica do piloto aplicada).

**Distinções na timeline:** processo longo (GOE, fotossíntese, deposição de BIF) · State (atmosfera, oceano, clima, biosfera) · evidência proxy (S-MIF, BIF, minerais redox) · hipótese (colapso do metano, catástrofe do O₂) · consequência posterior (eucariontes, ozônio) · ClaimSet (debates discretos) · UncertaintyProfile (faixas).

---

## 10. Dossiê da cena 2,4 Ga (Tarefa 10)

Desenho **conceitual** do dossiê (não é plano de aula, não é currículo, não é UI final). Dezoito blocos, com ênfase em **"como sabemos disso"** — porque aqui não há nenhuma fonte documental humana.

1. **Visão geral** — "A Terra há ~2,4 bilhões de anos" (com a etiqueta "aproximação de tempo profundo"). O O₂ subiu e mudou o planeta; os detalhes têm incerteza.
2. **O foco: Grande Evento de Oxidação** — `proc:goe`: o fato consolidado (subida de O₂) separado de magnitude/ritmo/causas (em ClaimSet/UncertaintyProfile).
3. **Como era a Terra nesse período** — planeta microbiano, sem continentes modernos, sem vida complexa, sem fronteiras; `entity:terra` no Paleoproterozoico inicial.
4. **Atmosfera antes e durante** — `state:atmosfera-primitiva` (anóxica) → `state:atmosfera-oxigenacao-goe`; composição em **faixa**, nunca número seco.
5. **Oceanos e ferro** — `state:oceanos-ferruginosos`; BIFs (`concept:formacoes-ferriferas-bandadas`); a química Fe+O₂.
6. **Vida microbiana** — `state:biota-microbiana-2-4ga`; `entity:cianobacterias` (produtoras de O₂) e `entity:organismos-anaerobios` (afetados).
7. **Como sabemos disso** — a **cadeia de inferência**: rocha → assinatura → conclusão → confiança; proxies explicados (sem fonte documental humana).
8. **Evidências geoquímicas** — E1–E7: BIFs, S-MIF, minerais detríticos, elementos redox, microfósseis, especiação de ferro, diamictitos.
9. **Incertezas e ClaimSets** — hub dos 6 ClaimSets + 2 UncertaintyProfiles; o que é debate legítimo × o que é consenso.
10. **Tectônica e paleogeografia** — `state:paleogeografia-2-4ga` (baixa confiança); o caso **Kenorland** com cautela extrema; "não há paleomapa confiável".
11. **Consequências biológicas** — impacto sobre anaeróbios (`claimset:goe-impacto-anaerobios`); caminho **distante** para respiração aeróbia e eucariontes (cautela).
12. **Consequências climáticas** — glaciações huronianas (`state:clima-goe`); hipótese do colapso do metano (`claimset:goe-glaciacoes`).
13. **Fontes e confiança** — proveniência por claim (NOAA Paleo, PBDB, USGS, GPlates); nível de confiança; fato × proxy × inferência × reconstrução.
14. **Itens ocultos por pendência/revisão** — lista transparente do que **não** está exibido (paleogeografia, Kenorland, magnitude precisa) e **por quê** (incerteza científica) — honestidade epistêmica como recurso.
15. **Como evitar anacronismos** — os 7 casos da §6: sem países, sem continentes modernos, paleogeografia é reconstrução, rocha de hoje ≠ lugar antigo, depósitos são janelas.
16. **Botão "navegar para outro período"** — troca o **recorte temporal** mantendo o modo planetário: da Terra de 2,4 Ga para o Cambriano, ou para a formação da Terra.
17. **Botão "comparar antes/depois do GOE"** — desloca dentro da janela: atmosfera anóxica (antes) × oxigenada (depois); oceanos ferruginosos × pós-BIF.
18. **Botão "ver consequências futuras"** — segue as arestas `possibilitou (futuro)` com **cautela**: camada de ozônio, eucariontes, respiração complexa — sempre marcadas como **muito posteriores**, não imediatas.

---

## 11. Relatório de qualidade da cena (Tarefa 11)

Roster curado da cena `scene:earth-2-4ga-great-oxidation-event` (reúso de 4B/4C + ~10 itens novos + 6 ClaimSets + 2 UncertaintyProfiles + 1 objeto de cena).

1. **Itens na cena:** **~29** (+ o objeto de cena, + 7 claims de evidência E1–E7), dos quais **~19 novos** nesta etapa (10 nós + 6 ClaimSets + 2 UncertaintyProfiles + 1 objeto).
2. **Event:** **0** — *ponto-chave epistêmico:* em tempo profundo **não há eventos pontuais datados**; a cena é feita de **processos longos e States** (contraste direto com 1789, rica em eventos de dia).
3. **Process:** **3** — `proc:goe`, `proc:fotossintese-oxigenica`, `proc:deposicao-bif`.
4. **State:** **7** — `atmosfera-primitiva`, `atmosfera-oxigenacao-goe`, `oceanos-ferruginosos`, `clima-goe`, `paleogeografia-2-4ga`, `biota-microbiana-2-4ga`, `geoquimica-2-4ga`.
5. **Concept:** **8** — `atmosfera-anoxica`, `fotossintese-oxigenica`, `oxigenacao-atmosferica`, `formacoes-ferriferas-bandadas`, `tectonica-placas`, `supercontinente`, `proterozoico`, `proxy-geoquimico` (este último, nó referenciado).
6. **Entity:** **3** — `cianobacterias`, `organismos-anaerobios`, `terra`.
7. **Place:** **3** — `bacia-hamersley`, `supergrupo-huroniano`, `bacia-transvaal` (localidades de **evidência atual**, não de "onde aconteceu").
8. **Region:** **0** — *ponto-chave:* **não há regiões políticas** em tempo profundo; a "geografia" é um `PaleogeographicState` incerto, não um conjunto de Regions (contraste com as 8 Regions de 1789).
9. **ClaimSet:** **6** — `goe-timing-fases`, `goe-ritmo-oxigenacao`, `goe-causas`, `goe-glaciacoes`, `goe-impacto-anaerobios`, `kenorland-existencia`.
10. **UncertaintyProfile:** **2** — `goe-magnitude-o2`, `paleogeografia-2-4ga` (incerteza em **faixa**, não claims discretos).
11. **Publicáveis (núcleo factual, pós-revisão científica do piloto):** **~16** — o fato do GOE, fotossíntese oxigênica, deposição de BIF, cianobactérias, biosfera microbiana, geoquímica/proxies (E1–E6), atmosfera (pré e durante, qualitativa), e os Concepts não controversos.
12. **Pending (incerteza científica):** **~13** — oceanos ferruginosos, clima/glaciações, paleogeografia, organismos anaeróbios (impacto), os 6 ClaimSets, os 2 UncertaintyProfiles e a evidência E7 (glaciação como hipótese).
13. **Risco científico alto:** **~6** — `state:paleogeografia-2-4ga`, `claimset:kenorland-existencia`, `uncertaintyprofile:paleogeografia-2-4ga`, `uncertaintyprofile:goe-magnitude-o2`, `claimset:goe-impacto-anaerobios`, `claimset:goe-glaciacoes`.
14. **Risco de licença:** **baixo** — todos em risco **0–1** (NOAA Paleo PD=0; PBDB/USGS/GPlates=0–1; **Deep Time Maps proibido**); **nenhum** médio/alto.
15. **Não exibíveis ainda:** os ~13 itens `pending` (paleogeografia, Kenorland, magnitude, glaciações, oceanos ferruginosos como proposta) — exibidos **mediados** ou ocultos; só o núcleo factual aparece.
16. **Gabarito para cenas futuras de tempo profundo:** o objeto `scene:earth-2-4ga-great-oxidation-event`; o **padrão de evidência E1–E7** ("como sabemos" sem documentos); a disciplina **ClaimSet × UncertaintyProfile**; o **globo esquemático rotulado**; a **exclusão por anacronismo temporal** (Rodinia/Pangeia/Nuna fora; Kenorland só como hipótese); a distinção **localidade de evidência atual ≠ posição paleogeográfica**.
17. **Fontes a confirmar:** NOAA/NCEI Paleo (assets de proxies); GPlates/EarthByte (paleogeografia ~2,4 Ga); literatura geoquímica (calibração de S-MIF, elementos redox); PBDB (microfósseis/estromatólitos). Todas `PENDENTE_CONFIRMACAO_FONTE` por asset.
18. **Recomendação de modelagem (`OceanographicState`/`GeochemicalState`):**
    - **`OceanographicState`: recomendado criar.** A química redox/ferro do oceano é central a esta cena e fica mal acomodada em `Paleogeographic`/`Climate`/`Biome`. A cena **funciona** sem ele (via `state:oceanos-ferruginosos` provisório), mas com **menor fidelidade**.
    - **`GeochemicalState`: recomendado, secundário.** Útil para consolidar proxies (S, Fe, redox); alternativamente, pode permanecer como **conjunto de claims de evidência** (E1–E7) sem virar tipo próprio.
    - **`EarthSystemState`: não recomendado** — o objeto `scene:` já cumpre o papel de visão integrada; criar o tipo seria redundante.
    - Estas são decisões de **modelagem (reabertura controlada da Etapa 2)**, **escaladas** aqui, não executadas.

---

## 12. Próximos passos para a Etapa 4F (Tarefa 12)

A Etapa 4E entregou a **segunda cena ponta-a-ponta** — agora em **tempo profundo** —, provando que a função "O que acontecia neste momento?" vale para uma Terra sem documentos, países, fronteiras ou humanos, com proxies, reconstruções e incerteza honesta. A **Etapa 4F**, quando solicitada, pode:

1. **Decidir os tipos de State escalados** (`OceanographicState`, `GeochemicalState`) em uma **mini-reabertura controlada da Etapa 2**, convertendo `state:oceanos-ferruginosos`/`state:geoquimica-2-4ga` de propostas em tipos oficiais — ou confirmando que permanecem provisórios.
2. **Concluir a revisão científica** dos ~13 itens `pending` desta cena (paleogeografia, magnitude, glaciações, impacto em anaeróbios), liberando o que for liberável e mantendo a incerteza onde ela é real.
3. **Confirmar as fontes por asset** (NOAA Paleo, GPlates, geoquímica, PBDB) e fechar `PENDENTE_CONFIRMACAO_FONTE` sem inventar precisão.
4. **Resolver o datum do eixo temporal** (1950 BP × J2000) — pendência herdada desde a 4B, que afeta a interoperabilidade entre cenas históricas (1789) e profundas (2,4 Ga); é decisão da **Etapa 3**, aqui apenas reforçada como bloqueio à integração das duas escalas.
5. **Comparar formalmente as duas cenas-gabarito** (1789 × 2,4 Ga) para extrair o **padrão de cena genérico** (histórica e profunda) que guiará povoamentos futuros — sem ainda povoar em massa.
6. **Reificar `Source`/`MediaAsset`** das evidências (proxies com `natureLabel` `gráfico`/`reconstrução científica`; afloramentos como `fotografia` que **ilustra**, não prova).

**O que a 4F explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (1/1.1) ou política editorial (Etapa 3.1). A reabertura da Etapa 2 (tipos de State) é **mínima e controlada**, restrita aos tipos escalados.

---

*Documento de entrega da Etapa 4E, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B, 4C, 4D). Entrega a cena canônica de tempo profundo a ~2,4 Ga (Grande Evento de Oxidação): objeto `scene:earth-2-4ga-great-oxidation-event`, itens centrais geoquímico-planetários, States planetários (com recomendação de `OceanographicState`/`GeochemicalState`), 7 claims de evidência ("como sabemos sem documentos"), 6 ClaimSets e 2 UncertaintyProfiles, tratamento do anacronismo espacial profundo (exclusão de Rodinia/Pangeia; cautela extrema com Kenorland), relationship graph, globo esquemático e timeline dominada por processos/States, dossiê de 18 blocos e relatório de qualidade. Não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não inventa composição atmosférica precisa e não inventa paleomapa. Próxima etapa, quando solicitada: Etapa 4F — decisão dos tipos de State escalados, conclusão de revisões científicas e extração do padrão de cena genérico (histórica × profunda).*
