# Etapa 4D — Cena Canônica de 1789 Ponta-a-Ponta

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4D · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A), o lote-piloto P0 (Etapa 4B) e a normalização/entidades de referência (Etapa 4C) · 12/06/2026
**Escopo desta etapa (e seus limites):** transformar a cena-piloto de 1789 em um **recorte temporal completo e demonstrativo** do Knowledge Core — a primeira realização ponta-a-ponta da função *"O que acontecia no mundo neste momento?"*. Foco: **Revolução Francesa**, mas com o **mundo de 1789 em simultaneidade**. Conforme solicitado, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** cria milhares de eventos, **não** usa Wikidata/Wikipedia como autoridade, **não** copia texto de fontes e **não** usa mídia como evidência factual.

**O que herda e respeita.** Os nós de 4B (SCENE-01..08, HIST-15/16, AFR-03, IND-01/03, BR-03/05) e de 4C (Concepts, Entities, Places, Regions, ClaimSets `claimset:`, separação `pilotCode`×`knowledgeItemId`, geometryStatus, invariante de exibição). Itens reusados **não** são reescritos — são **referenciados e aprofundados**; itens novos seguem o template e o gabarito ouro.

> **Diferencial que esta cena prova:** a Revolução Francesa **não** aparece isolada. Ela aparece como parte de um **planeta vivo em 1789** — ciência (Lavoisier), escravidão e tráfico, impérios (Otomano, Qing), África Ocidental, Brasil colonial (Inconfidência/Minas), EUA (Washington), povos indígenas, economia atlântica e ideias circulando **ao mesmo tempo**.

---

## Sumário

1. Objeto conceitual da cena 1789 (Tarefa 1)
2. Itens centrais da cena (Tarefa 2)
3. Itens simultâneos globais (Tarefa 3)
4. ModernCorrespondence e anacronismo (Tarefa 4)
5. ClaimSets da cena (Tarefa 5)
6. Relationship Graph da cena (Tarefa 6)
7. Globo/mapa da cena (Tarefa 7)
8. Timeline da cena (Tarefa 8)
9. Dossiê da cena (Tarefa 9)
10. Relatório de qualidade da cena (Tarefa 10)
11. Próximos passos para a Etapa 4E (Tarefa 11)

---

## 1. Objeto conceitual da cena 1789 (Tarefa 1)

A cena é um **objeto de consulta materializado** — não um novo tipo de conteúdo, e sim a interseção espaço-temporal dos índices (Etapa 2, P7; `concept:simultaneidade-historica`). Ela **referencia** itens; não os duplica.

**`scene:world-1789-french-revolution`**
- **id:** `scene:world-1789-french-revolution` · **pilotCode:** SCENE-1789 · **version:** 1.0
- **título:** O mundo em 1789 — Revolução Francesa em simultaneidade
- **foco principal:** Revolução Francesa (`proc:revolucao-francesa`, HIST-15)
- **TimeRange:** ano de 1789 (núcleo), com janela contextual 1787–1792 · **TimePrecision:** `ano` (eventos pontuais em `dia`)
- **escopo espacial:** global (multi-região), sem fechar no eixo europeu
- **camadas ativadas:** 13 Política · 14 Economia · 15 Ciência · 16 Tecnologia · 17 Cultura · 20 Brasil · 21 África/diáspora · 22 Povos indígenas · 23 Mundo contemporâneo (recorte) · 25 Fontes/meta
- **itens centrais:** `proc:revolucao-francesa`, `evt:estados-gerais-1789`, `evt:queda-bastilha-1789`, `evt:declaracao-direitos-1789`, `proc:crise-fiscal-franca`, `state:franca-1789`, `concept:antigo-regime`, `concept:iluminismo`, `evt:lavoisier-traite-1789`, `entity:lavoisier`
- **itens contextuais (simultâneos):** `evt:inconfidencia-mineira`, `state:eua-governo-1789`, `entity:george-washington`, `evt:posse-washington-1789`, `state:imperio-otomano-1789`, `state:china-qing-1789`, `state:africa-ocidental-1789`, `state:economia-mundo-atlantico-1789`, `state:ciclo-ouro-minas`, `region:*` e `place:*` associados
- **itens sensíveis (gated):** `proc:trafico-atlantico`, `concept:escravidao`, `concept:colonialismo`, `concept:diaspora`, `state:sociedades-precolombianas` (IND-01), `proc:resistencia-indigena` (IND-03), `state:indigenas-pre1500-brasil` (BR-03), `entity:povos-indigenas-brasil`, `entity:africanos-escravizados-afrodescendentes`, e todos os ClaimSets sensíveis
- **Claims principais da cena:** "Em 1789, transformações políticas, científicas e econômicas ocorriam simultaneamente em várias partes do mundo, conectadas pelo sistema atlântico" — `interpretação historiográfica` apoiada em fatos documentados datados.
- **ClaimSets envolvidos:** `claimset:causas-revolucao-francesa`, `claimset:atlantico-revolucionario-1789`, `claimset:inconfidencia-interpretacoes`, `claimset:direitos-universais-limites`, `claimset:escravidao-centralidade-atlantica`, `claimset:presenca-indigena-apagamento`, `claimset:iluminismo-limites`
- **fontes A/B necessárias:** historiografia revisada (A/B); Arquivo Nacional/BN e IBGE (Brasil, A); história da ciência (Lavoisier, A/B); OWID (economia, B); Natural Earth histórico/geoBoundaries (geometria); fontes africanas e indígenas (incl. **tradição/registro oral**)
- **reviewStatus (da cena):** `pending` — a cena **como um todo** só é publicável quando seus itens sensíveis forem revisados; o **núcleo factual** (eventos datados de 1789) é exibível desde já
- **risco editorial:** **alto** (cruza escravidão, colonialismo, povos indígenas — Leis 10.639/11.645)
- **risco de licença:** baixo–médio (fontes verdes; risco 0–2); geometrias históricas em `PENDENTE_REFINAMENTO_ESPACIAL`
- **timeline:** zoom em 1789; processos longos atravessando o ano; eventos pontuais marcados por dia (ver §8)
- **globo/mapa:** foco inicial na França, com marcadores simultâneos em Minas, América do Norte, território otomano, China Qing, África Ocidental e rotas atlânticas (ver §7)
- **dossiê:** 15 blocos navegáveis (ver §9), com legendas epistemológica/temporal/editorial
- **itens não exibíveis enquanto pending:** todos os itens sensíveis listados acima e os ClaimSets sensíveis — aparecem **mediados** (rótulo "em revisão") ou ocultos, **nunca** como fato cru

---

## 2. Itens centrais da cena (Tarefa 2)

Itens do foco francês. Os já existentes (HIST-15, SCENE-01/07/08) são **referenciados e aprofundados**; os novos recebem template completo. **Regra mantida:** as **causas** da Revolução Francesa permanecem em `claimset:causas-revolucao-francesa`, nunca como claim único.

**`proc:revolucao-francesa`** *(HIST-15 — existente, aprofundado)*
- tipo: `Process` · camadaP: 13 Política · camadasS: 17, 14, 19 · título: Revolução Francesa
- TimeRange: 1789–1799 · Place/Region: `region:franca-1789` / `place:paris`, `place:versalhes`
- ClaimPrinc: "Processo revolucionário que derrubou o Antigo Regime na França a partir de 1789" — `fato documentado` (eventos) + `interpretação` (alcance) · ClaimTemp: início em 1789 — `fato documentado` · ClaimEsp: França.
- Source: historiografia revisada (A/B); fontes primárias · conf: alta · evid: `documental` · uncert: causas em ClaimSet · review: `pending` (revisão histórica) · editorialRisk: médio-alto · licenseRisk: 0–1.
- rels: `decorreu-de` `proc:crise-fiscal-franca`; `influenciada-por` `concept:iluminismo`; `contém` `evt:estados-gerais-1789`, `evt:queda-bastilha-1789`, `evt:declaracao-direitos-1789`; `qualificada-por` `claimset:causas-revolucao-francesa`; `contemporânea-de` `evt:inconfidencia-mineira`.
- timeline: bloco-processo 1789–99 · globe: França destacada · simultaneidade: **âncora** da cena.

**`evt:estados-gerais-1789`** *(novo)*
- knowledgeItemId: `evt:estados-gerais-1789` · tipo: `Event` · camadaP: 13 Política · camadasS: 17 · título: Abertura dos Estados Gerais
- TimeRange: maio de 1789 (abertura em 5 de maio) · Place/Region: `place:versalhes` / `region:franca-1789`
- ClaimPrinc: "Os Estados Gerais foram convocados e abertos em maio de 1789, em Versalhes" — `fato documentado` · ClaimTemp: 05/05/1789 — `fato documentado` · ClaimEsp: Versalhes.
- Source: historiografia/arquivos (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: alta · evid: `documental` · uncert: baixa · review: `approved` (núcleo factual) · editorialRisk: baixo · licenseRisk: 0–1.
- rels: `parte-de` `proc:revolucao-francesa`; `predecessor-de` `evt:queda-bastilha-1789`; `localizado-em` `place:versalhes`.
- timeline: ponto, maio/1789 · globe: marcador em Versalhes · simultaneidade: início institucional da Revolução.

**`evt:queda-bastilha-1789`** *(novo)*
- knowledgeItemId: `evt:queda-bastilha-1789` · tipo: `Event` · camadaP: 13 Política · camadasS: 17 · título: Queda da Bastilha
- TimeRange: 14 de julho de 1789 · Place/Region: `place:paris` / `region:franca-1789`
- ClaimPrinc: "Em 14 de julho de 1789 a fortaleza-prisão da Bastilha foi tomada em Paris" — `fato documentado` · ClaimTemp: 14/07/1789 — `fato documentado` · ClaimEsp: Paris.
- Source: historiografia/arquivos (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: alta · evid: `documental` · uncert: baixa · review: `approved` · editorialRisk: baixo · licenseRisk: 0–1.
- rels: `ocorreu-durante` `proc:revolucao-francesa`; `sucessor-de` `evt:estados-gerais-1789`; `localizado-em` `place:paris`.
- timeline: ponto, 14/07/1789 (marco simbólico) · globe: marcador em Paris · simultaneidade: evento-ícone de 1789.

**`evt:declaracao-direitos-1789`** *(novo)*
- knowledgeItemId: `evt:declaracao-direitos-1789` · tipo: `Event` · camadaP: 13 Política · camadasS: 17, 25 · título: Declaração dos Direitos do Homem e do Cidadão
- TimeRange: 26 de agosto de 1789 · Place/Region: `region:franca-1789` / `place:paris`
- ClaimPrinc: "Em agosto de 1789 a Assembleia proclamou a Declaração dos Direitos do Homem e do Cidadão" — `fato documentado`. "O alcance 'universal' desses direitos teve limites históricos (gênero, escravidão, colônias)" — `interpretação` (ver `claimset:direitos-universais-limites`). · ClaimTemp: 26/08/1789 — `fato documentado` · ClaimEsp: França.
- Source: texto histórico (livre); historiografia (A/B) · conf: alta · evid: `documental` · uncert: alcance em ClaimSet · review: `pending` (limites sociais = revisão) · editorialRisk: médio-alto · licenseRisk: 0–1.
- rels: `ocorreu-durante` `proc:revolucao-francesa`; `qualificada-por` `claimset:direitos-universais-limites`; `relacionada-a` `concept:iluminismo`.
- timeline: ponto, 26/08/1789 · globe: França · simultaneidade: dimensão **ideológica** da cena.

**`proc:crise-fiscal-franca`** *(novo)*
- knowledgeItemId: `proc:crise-fiscal-franca` · tipo: `Process` · camadaP: 14 Economia · camadasS: 13 · título: Crise fiscal-financeira francesa (anos 1780)
- TimeRange: ~1770s–1789 · Place/Region: `region:franca-1789`
- ClaimPrinc: "O Estado francês enfrentava grave crise fiscal-financeira às vésperas de 1789" — `fato documentado`/`interpretação` · ClaimTemp: anos 1780 — `fato documentado` · ClaimEsp: França.
- Source: historiografia econômica (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: alta · evid: `documental` · uncert: peso causal em ClaimSet · review: `pending` · editorialRisk: médio · licenseRisk: 0–1.
- rels: `contribuiu-para` `proc:revolucao-francesa` (uma das causas em `claimset:causas-revolucao-francesa`).
- timeline: processo que **antecede e atravessa** 1789 · globe: França · simultaneidade: causa econômica (uma entre várias).

**`state:franca-1789`** *(novo)*
- knowledgeItemId: `state:franca-1789` · tipo: `State` (CivilizationState/Political) · camadaP: 13 Política · camadasS: 14, 17 · título: França em 1789 (Antigo Regime em crise)
- TimeRange: 1789 (recorte) · Place/Region: `region:franca-1789`
- ClaimPrinc: "Em 1789 a França era uma monarquia do Antigo Regime em crise política, fiscal e social" — `fato documentado`/`interpretação` · ClaimTemp: 1789 — `fato documentado` · ClaimEsp: `region:franca-1789` (`PENDENTE_REFINAMENTO_ESPACIAL`).
- Source: historiografia (A/B) · conf: alta · evid: `documental` · uncert: baixa (condição), média (fronteiras) · review: `pending` · editorialRisk: médio · licenseRisk: 0–1.
- rels: condição de `entity:franca`; `relacionado-a` `concept:antigo-regime`; palco de `proc:revolucao-francesa`.
- timeline: estado em 1789 · globe: França (fronteira de 1789, pendente) · simultaneidade: o "ponto de partida" político da cena.

**`concept:antigo-regime`** *(novo)*
- knowledgeItemId: `concept:antigo-regime` · tipo: `Concept` · camadaP: 13 Política · camadasS: 14, 17 · título: Antigo Regime
- def: ordem social e política da Europa pré-revolucionária, marcada por monarquia absoluta, sociedade de ordens e privilégios.
- ClaimPrinc: "É um conceito que descreve a ordem pré-revolucionária por contraste com o que veio depois" — `interpretação historiográfica` · ClaimTemp: ~séc. XVI–XVIII (transtemporal) · ClaimEsp: difuso (Europa).
- Source: historiografia (A/B) · conf: média · evid: `documental` · uncert: conceito construído a posteriori · review: `pending` · editorialRisk: médio · licenseRisk: 0.
- rels: `explica` `state:franca-1789`; `relacionado-a` `proc:revolucao-francesa`. · ling. escolar: "Antigo Regime" é um rótulo retrospectivo, não um nome da época.

**`concept:iluminismo`** *(SCENE-08 — existente, aprofundado)*
- tipo: `Concept` · camadaP: 17 Cultura · título: Iluminismo · TimeRange: difusão séc. XVII–XVIII.
- ClaimPrinc: "Movimento intelectual que influenciou as revoluções atlânticas" — `interpretação historiográfica` (influência = claim com fonte, não nexo automático). · review: `approved` (núcleo) com limites em `claimset:iluminismo-limites`.
- rels: `influenciou` `proc:revolucao-francesa`, `evt:declaracao-direitos-1789`; `qualificado-por` `claimset:iluminismo-limites`.
- simultaneidade: corrente de **ideias** da cena.

**`evt:lavoisier-traite-1789`** *(SCENE-01 — existente)* + **`entity:lavoisier`** *(SCENE-07 — existente, normalizado)*
- `evt:lavoisier-traite-1789`: `Event` · camadaP: 15 Ciência · TimeRange: 1789 · `place:paris`. ClaimPrinc: "Lavoisier publicou em 1789 obra que sistematizou a química moderna" — `fato documentado` · review: `approved` · editorialRisk: baixo.
- `entity:lavoisier`: `Entity` (pessoa) · 1743–1794 · `participou-de` `evt:lavoisier-traite-1789`; `contemporâneo-de` `proc:revolucao-francesa`.
- simultaneidade: **ciência simultânea** à política — prova que 1789 não é só revolução.

---

## 3. Itens simultâneos no mundo em 1789 (Tarefa 3)

O que ocorria **ao mesmo tempo**, fora da França. Itens existentes são referenciados; novos recebem template. **Antianacronismo (pedido explícito):** o **Império do Mali não é contemporâneo de 1789** (declinou por volta de ~1600) — entra apenas como **contexto histórico africano anterior** (ver §4), **não** como simultâneo. Para a África de 1789 usa-se o recorte adequado: `state:africa-ocidental-1789` (polities ativas como Oyo, Daomé, Axânti). *(Nota: o Califado de Sokoto só surge em 1804 — também fora de 1789.)*

**`evt:inconfidencia-mineira`** *(HIST-16 — existente, aprofundado)*
- tipo: `Event` · camadaP: 20 Brasil · camadasS: 13, 14, 21 · título: Inconfidência Mineira
- TimeRange: 1789 (conspiração denunciada; Tiradentes executado em 1792) · Place/Region: `region:capitania-minas-gerais` → `concept:modern-correspondence` → MG atual
- ClaimPrinc: "Movimento de elites coloniais em Minas, em 1789, contra a pressão fiscal da Coroa portuguesa" — `fato documentado` + `interpretação` (alcance e caráter em ClaimSet) · ClaimTemp: 1789 — `fato documentado` · ClaimEsp: Capitania de Minas Gerais.
- Source: Arquivo Nacional/BN, IBGE, historiografia (A/B) · conf: alta · evid: `documental` · uncert: caráter em ClaimSet · review: `pending` (Brasil sensível) · editorialRisk: médio-alto · licenseRisk: 0–1.
- rels: `contemporânea-de` `proc:revolucao-francesa`; `localizada-em` `region:capitania-minas-gerais`; `qualificada-por` `claimset:inconfidencia-interpretacoes`; `relacionada-a` `state:ciclo-ouro-minas`.
- timeline: ponto, 1789 (Brasil) · globe: marcador em Minas (via correspondência moderna) · simultaneidade: **Brasil simultâneo** à França — par canônico.

**`state:ciclo-ouro-minas`** *(BR-05 — existente, aprofundado para 1789)*
- tipo: `State` · camadaP: 20 Brasil · camadasS: 14, 21 · título: Ciclo do ouro / Minas colonial
- TimeRange: ~1690s–1750s (auge); **em 1789 já em declínio** · Place/Region: `region:capitania-minas-gerais`
- ClaimPrinc: "A mineração aurífera estruturou Minas colonial; em 1789 estava em declínio, agravando a pressão fiscal" — `fato documentado`/`interpretação` · ClaimTemp: auge até ~1750; declínio em 1789 — `interpretação` · ClaimEsp: Minas.
- Source: historiografia/Arquivo Nacional (A/B) · conf: alta · evid: `documental` · uncert: média · review: `pending` (escravidão/ouro) · editorialRisk: alto (trabalho escravizado) · licenseRisk: 1.
- rels: `contextualiza` `evt:inconfidencia-mineira` (o declínio e a *derrama* ligam-se à revolta); `relacionado-a` `proc:trafico-atlantico`, `concept:escravidao`.
- timeline: estado em declínio em 1789 · globe: Minas · simultaneidade: liga economia, escravidão e a Inconfidência.

**`state:eua-governo-1789`** *(SCENE-02 — existente)* + **`entity:george-washington`** *(novo)* + **`evt:posse-washington-1789`** *(novo)*
- `state:eua-governo-1789`: `State` · camadaP: 13 · 1789 · `region:america-norte-1789`. ClaimPrinc: "Instalou-se em 1789 o primeiro governo dos EUA sob a Constituição" — `fato documentado` · review: `approved` · editorialRisk: baixo.
- `entity:george-washington` *(novo)*: `Entity` (pessoa) · camadaP: 13 · TimeRange (existência): 1732–1799 · Place/Region: EUA. ClaimPrinc: "Primeiro presidente dos EUA, empossado em 1789" — `fato documentado` · Source: arquivos/historiografia (A/B) · conf: alta · evid: `documental` · review: `approved` · editorialRisk: baixo · licenseRisk: 0. rels: `participou-de` `evt:posse-washington-1789`. nomenclatura: figura histórica (falecida); sem questão de LGPD.
- `evt:posse-washington-1789` *(novo)*: `Event` · camadaP: 13 · **30 de abril de 1789, em Nova York** (a capital **não** era Washington, D.C.). ClaimPrinc: "Washington foi empossado em 30/04/1789, na então capital Nova York" — `fato documentado` · review: `approved` · editorialRisk: baixo · licenseRisk: 0. rels: `parte-de` `state:eua-governo-1789`; `contemporâneo-de` `proc:revolucao-francesa`. **antianacronismo:** ver §4, caso 4.
- simultaneidade: **terceira revolução atlântica** (EUA) no mesmo ano.

**`state:imperio-otomano-1789`** *(SCENE-03 — existente, aprofundado)*
- tipo: `State` · camadaP: 13 · título: Império Otomano em 1789
- TimeRange: 1789 (início do reinado de Selim III, 7/4/1789) · Place/Region: território otomano (`PENDENTE_REFINAMENTO_ESPACIAL`)
- ClaimPrinc: "Em 1789 começava o reinado de Selim III, com tentativas de reforma" — `fato documentado` + `interpretação` · review: `pending` · editorialRisk: médio · licenseRisk: 1.
- rels: condição de `entity:imperio-otomano`; `contemporâneo-de` `proc:revolucao-francesa`. · simultaneidade: **recorte não eurocêntrico** do mesmo ano.

**`state:china-qing-1789`** *(SCENE-04 — existente, aprofundado)*
- tipo: `State` · camadaP: 12 Civilizações · título: China Qing em 1789
- TimeRange: 1789 (reinado de Qianlong) · Place/Region: `region:china-qing` (`PENDENTE_REFINAMENTO_ESPACIAL`)
- ClaimPrinc: "Em 1789 a China Qing era um dos maiores Estados e economias do mundo" — `fato documentado` + `interpretação` (peso econômico) · review: `pending` · editorialRisk: médio · licenseRisk: 1.
- rels: condição de `entity:china-qing`; `relacionado-a` `state:economia-mundo-atlantico-1789` (contraponto). · simultaneidade: contrapeso à centralidade europeia.

**`state:africa-ocidental-1789`** *(SCENE-05 — existente, aprofundado)*
- tipo: `State` · camadaP: 21 África · título: Estados da África Ocidental em 1789 (recorte adequado a 1789)
- TimeRange: 1789 (recorte) · Place/Region: `region:africa-ocidental`, `region:sahel` (`PENDENTE_REFINAMENTO_ESPACIAL`)
- ClaimPrinc: "Em 1789 a África Ocidental abrigava Estados complexos e ativos no comércio atlântico (ex.: Oyo, Daomé, Axânti)" — `fato documentado` (existência) + `interpretação` · Source: historiografia africana (A/B) `PENDENTE_CONFIRMACAO_FONTE` · conf: média · evid: `documental` + `tradição/registro oral` · review: `pending` · editorialRisk: **alto** (Lei 10.639) · licenseRisk: 1–2.
- rels: `contemporâneo-de` `proc:revolucao-francesa`; `relacionado-a` `proc:trafico-atlantico`; **não** confundir com `entity:imperio-mali` (anterior, ver §4). · simultaneidade: **antieurocentrismo estrutural** — África como agente em 1789.

**`state:economia-mundo-atlantico-1789`** *(SCENE-06 — existente, aprofundado)*
- tipo: `State` (EconomicState) · camadaP: 14 Economia · título: Economia do mundo atlântico em 1789
- TimeRange: 1789 (recorte) · Place/Region: `region:mundo-atlantico`
- ClaimPrinc: "Em 1789 a economia atlântica articulava Europa, África e Américas em torno do trabalho escravizado e do comércio" — `interpretação historiográfica` + `estimativa` · Source: OWID/literatura (B) `PENDENTE_CONFIRMACAO_FONTE` · conf: média · evid: `inferência indireta` · review: `pending` · editorialRisk: alto (escravidão) · licenseRisk: 1.
- rels: `relacionado-a` `proc:trafico-atlantico`, `concept:escravidao`, `state:ciclo-ouro-minas`; `qualificado-por` `claimset:escravidao-centralidade-atlantica`. · simultaneidade: **contexto econômico** que conecta a cena.

**`proc:trafico-atlantico`** *(AFR-03 — existente)* + **`entity:africanos-escravizados-afrodescendentes`** *(4C)*
- `proc:trafico-atlantico`: `Process` · camadaP: 21 · TimeRange: séc. XVI–XIX (**ativo e intenso em 1789**) · `region:mundo-atlantico`, `place:caribe`. ClaimPrinc: "O tráfico atlântico deslocava à força milhões de pessoas africanas; estava ativo em 1789" — `fato documentado` · Source: bases do tráfico/historiografia (A/B) · conf: alta · evid: `documental` · review: `pending` (obrigatória) · editorialRisk: **crítico** (Lei 10.639) · licenseRisk: 1.
- `entity:africanos-escravizados-afrodescendentes`: grupo humano sensível — "pessoas escravizadas e seus descendentes, agentes de cultura e resistência" — review: `pending` obrigatória; **agência**, não objeto.
- rels: `causou` `concept:diaspora`; `conecta` África↔Brasil↔Caribe (`region:mundo-atlantico`); `qualificado-por` `claimset:escravidao-centralidade-atlantica`. · simultaneidade: a escravidão **não** é detalhe econômico neutro — é estrutura central de 1789.

**`state:sociedades-precolombianas`** *(IND-01)* · **`proc:resistencia-indigena`** *(IND-03)* · **`state:indigenas-pre1500-brasil`** *(BR-03)* · **`entity:povos-indigenas-brasil`** *(4C)*
- Em 1789, povos indígenas **existiam e agiam** em toda a América, inclusive no território hoje brasileiro — antes, durante e depois da colonização. ClaimPrinc (síntese): "Povos indígenas eram presença viva e agente nas Américas em 1789, resistindo e persistindo" — `fato documentado`/`interpretação` · evid: `documental` + `registro material` + `tradição/registro oral` · review: `pending` (obrigatória, Lei 11.645) · editorialRisk: **crítico** · licenseRisk: 1–2.
- rels: `contemporâneos-de` `proc:revolucao-francesa`; `qualificados-por` `claimset:presenca-indigena-apagamento`; `agência-de` `entity:povos-indigenas-brasil`.
- **antianacronismo:** não apagar territórios indígenas sob fronteiras coloniais (ver §4, caso 5). · simultaneidade: **povos indígenas na cena**, não como nota de rodapé.

**Ciência e tecnologia em 1789** *(síntese ancorada em itens existentes)*
- `evt:lavoisier-traite-1789` (química moderna) + `proc:revolucao-cientifica` (HIST-14, em curso) + industrialização incipiente (`proc:revolucao-industrial`, HIST-17, ~1760–1840, em curso). ClaimPrinc: "Em 1789 a ciência e a técnica europeias passavam por transformações (química moderna, industrialização incipiente)" — `fato` + `interpretação` · review: núcleo `approved`, contexto `pending` · editorialRisk: baixo-médio.
- simultaneidade: **camada científico-tecnológica** da cena.

---

## 4. ModernCorrespondence e anacronismo (Tarefa 4)

A cena evita anacronismo usando `concept:modern-correspondence` (4C): liga o passado a referências atuais **sem** projetar fronteiras/realidades de hoje sobre 1789. Sete casos obrigatórios.

| Caso | Risco de anacronismo | Correção conceitual | Place/Region correto | ModernCorrespondence | Como aparece no dossiê |
|---|---|---|---|---|---|
| 1. "Brasil" em 1789 | tratar 1789 como se já existisse o Brasil nação | em 1789 há **colônia portuguesa**, não Estado-nação brasileiro | `region:capitania-minas-gerais`, demais capitanias; **não** `region:territorio-brasil-atual` como realidade política | capitanias → unidades atuais (lente) | rótulo "Brasil colonial (não o Brasil de hoje)" |
| 2. Inconfidência Mineira | localizá-la em "Minas Gerais" estado atual | ocorre na **Capitania de Minas Gerais** | `region:capitania-minas-gerais` | Capitania → estado de MG | nota "Capitania, não estado" |
| 3. "Território que hoje corresponde ao Brasil" | confundir a **lente moderna** com realidade política de 1789 | é um **recorte de referência**, não um Estado de 1789 | `region:territorio-brasil-atual` (apenas como lente) | é a própria ModernCorrespondence | legenda epistemológica explícita |
| 4. Washington, D.C. | supor que a capital dos EUA em 1789 era Washington | em 1789 a capital era **Nova York**; D.C. fundada em 1790 | `place:washington-dc` marcado como **posterior**; capital de 1789 = Nova York | — | nota "capital em 1789: Nova York" |
| 5. Povos indígenas | apagá-los sob fronteiras coloniais | territórios indígenas **precedem e atravessam** as fronteiras coloniais | territórios indígenas próprios (geometria `PENDENTE_REFINAMENTO_ESPACIAL`) | territórios → referências atuais sem reduzir | camada indígena **sobreposta**, não substituída por colônias |
| 6. África | aparecer só em função da Europa | África com **agência própria** (Oyo, Daomé, Axânti) | `region:africa-ocidental`, `region:sahel` | — | seção africana autônoma no dossiê |
| 7. Mundo atlântico | tratá-lo como um Estado | é **recorte analítico**, não entidade política | `region:mundo-atlantico` (geometryStatus inferido) | — | rótulo "recorte analítico, não Estado" |

**Caso especial — Império do Mali.** O Mali (`entity:imperio-mali`, auge séc. XIII–XIV) **não** é contemporâneo de 1789. Na cena ele aparece **apenas** como **contexto histórico africano anterior** (link "para entender a África Ocidental de 1789, veja a história anterior"), nunca como Estado simultâneo. O recorte simultâneo correto é `state:africa-ocidental-1789`. Isso demonstra a regra: **não forçar item anacrônico**.

---

## 5. ClaimSets da cena 1789 (Tarefa 5)

Sete ClaimSets. Regras reafirmadas: **não** transformar debate historiográfico legítimo em narrativa única; **não** criar falsa equivalência entre fato documentado e negacionismo; **não** apresentar escravidão como detalhe econômico neutro.

**`claimset:causas-revolucao-francesa`** *(CS1 — existente)*
- tema: causas da Revolução Francesa · consensusStatus: **controvérsia historiográfica**
- claims legítimos: crise fiscal-financeira; tensões sociais/de ordem; ideias iluministas; crise de subsistência. Cada um com peso e autores · conf por claim: alta (existência dos fatores), média (peso relativo)
- sem equivalência: nenhuma — todos têm base documental · fontes: historiografia revisada (A/B) · review: `pending`
- nota: separar **fatos datados** das **causas**; exibir pesos, não "alguns dizem" · impacto: exibe pluralidade; não elege "a" causa.

**`claimset:atlantico-revolucionario-1789`** *(novo)*
- tema: 1789 e o Atlântico revolucionário (conexões entre revoluções americana, francesa e tensões coloniais) · consensusStatus: **debate acadêmico**
- claims legítimos: (a) existência de um "ciclo de revoluções atlânticas" conectado; (b) ênfase nas especificidades locais sobre a conexão; (c) o papel das revoltas escravas/coloniais no ciclo · conf: média
- sem equivalência: negar a circulação de ideias/pessoas no Atlântico · fontes: historiografia atlântica (A/B) · review: `pending`
- nota: conexão **e** especificidade, sem determinismo · impacto: oferece a leitura conectada como interpretação, não como fato fechado.

**`claimset:inconfidencia-interpretacoes`** *(novo)*
- tema: Inconfidência Mineira — separatismo, elite colonial, fiscalidade e escravidão · consensusStatus: **controvérsia historiográfica**
- claims legítimos: (a) movimento separatista/independentista; (b) reação de elites à pressão fiscal (*derrama*); (c) projeto limitado que **não** rompia com a escravidão; (d) leituras sobre seu caráter "nacional" posterior · conf: alta (fatos), média (caráter)
- **sem equivalência:** mitos que apagam o caráter elitista/escravista do movimento; usos puramente heroicizantes acríticos · fontes: Arquivo Nacional/historiografia (A/B) · review: `pending` (obrigatória)
- nota: nem mito heroico nem irrelevância; **escravidão não é nota de rodapé** · impacto: dossiê apresenta as interpretações lado a lado.

**`claimset:direitos-universais-limites`** *(novo)*
- tema: "direitos universais" de 1789 e seus limites sociais/históricos · consensusStatus: **interpretação historiográfica consolidada**
- claims legítimos: (a) a Declaração proclamou direitos em linguagem universal; (b) na prática excluiu mulheres, pessoas escravizadas e colônias; (c) debate sobre se isso é "contradição" ou "limite de época" · conf: alta (exclusões documentadas), média (leitura)
- **sem equivalência:** negar as exclusões ou tratá-las como detalhe · fontes: historiografia (A/B); estudos de gênero e da escravidão · review: `pending`
- nota: universalidade proclamada × universalidade praticada · impacto: a Declaração aparece com seus limites, sem anular sua importância.

**`claimset:escravidao-centralidade-atlantica`** *(novo)*
- tema: centralidade econômica da escravidão no mundo atlântico de 1789 · consensusStatus: **debate acadêmico** (sobre **grau/peso**, não sobre existência ou moralidade)
- claims legítimos: (a) a escravidão era estrutural para a economia atlântica (tese da centralidade); (b) ênfases que matizam seu peso relativo frente a outros fatores · conf: alta (escravidão como sistema), média (peso econômico exato)
- **sem equivalência:** naturalizar, minimizar ou moralmente relativizar a violência escravista; tratá-la como "mão de obra" neutra · fontes: historiografia da escravidão (A/B); fontes afro-diaspóricas · review: `pending` (obrigatória)
- nota: o **debate é sobre peso econômico**, jamais sobre a violência ser ou não condenável · impacto: escravidão aparece como **estrutura central**, com agência das pessoas escravizadas.

**`claimset:presenca-indigena-apagamento`** *(novo)*
- tema: presença indígena viva × apagamento cartográfico/historiográfico · consensusStatus: **terminologia sensível / interpretação**
- claims legítimos: (a) povos indígenas eram presença demográfica e política em 1789; (b) crítica ao apagamento em mapas/narrativas coloniais; (c) reconhecimento de territorialidades próprias · conf: alta
- **sem equivalência:** narrativas de "vazio demográfico" ou de povos "já extintos" · fontes: etno-historiografia, IPHAN, **fontes indígenas** (A/B) · review: `pending` (obrigatória, Lei 11.645)
- nota: presença e **agência**; mapas coloniais são fontes a criticar, não verdade neutra · impacto: camada indígena sobreposta, mediada, nunca apagada.

**`claimset:iluminismo-limites`** *(novo)*
- tema: Iluminismo — circulação de ideias e limites históricos · consensusStatus: **interpretação historiográfica**
- claims legítimos: (a) influência intelectual ampla das ideias ilustradas; (b) limites e contradições (autores que conviviam com escravidão/colonialismo); (c) circulação **não** unidirecional (trocas com outros mundos) · conf: média
- **sem equivalência:** apresentar o Iluminismo como causa única/automática da Revolução, ou como projeto sem contradições · fontes: historiografia (A/B) · review: `pending`
- nota: influência é claim com fonte, não nexo automático · impacto: Iluminismo aparece como corrente influente **e** contraditória.

---

## 6. Relationship Graph da cena (Tarefa 6)

Malha específica de 1789. Arestas afirmativas (`influenciou`/`contribuiu-para`/`causou`) **são claims** (têm evidência/confiança); arestas de ordem/índice (`predecessor-de`/`contemporâneo-de`/`localizado-em`) são estruturais.

| relId | sourceItem | relationshipType | targetItem | claim/evidence | conf | reviewStatus | obs. editorial |
|---|---|---|---|---|---|---|---|
| rel:S01 | `concept:iluminismo` | influenciou | `proc:revolucao-francesa` | documental (claim) | média | pending | influência ≠ causa única (CS1, `iluminismo-limites`) |
| rel:S02 | `proc:crise-fiscal-franca` | contribuiu-para | `proc:revolucao-francesa` | documental (claim) | alta/média | pending | uma causa entre várias (CS1) |
| rel:S03 | `evt:estados-gerais-1789` | predecessor-de | `evt:queda-bastilha-1789` | índice temporal | — | approved | maio → julho de 1789 |
| rel:S04 | `evt:queda-bastilha-1789` | ocorreu-durante | `proc:revolucao-francesa` | índice temporal | — | approved | evento dentro do processo |
| rel:S05 | `evt:declaracao-direitos-1789` | ocorreu-durante | `proc:revolucao-francesa` | índice temporal | — | pending | agosto/1789; limites em `direitos-universais-limites` |
| rel:S06 | `proc:revolucao-francesa` | contemporâneo-de | `evt:inconfidencia-mineira` | índice temporal | — | pending | par canônico França↔Brasil |
| rel:S07 | `evt:inconfidencia-mineira` | localizado-em | `region:capitania-minas-gerais` | documental | alta | pending | Capitania, não estado atual |
| rel:S08 | `region:capitania-minas-gerais` | modernCorrespondence | MG atual (`place:ouro-preto`/estado) | definição de modelo | alta | pending | antianacronismo (§4) |
| rel:S09 | `entity:lavoisier` | contemporâneo-de | `proc:revolucao-francesa` | índice temporal | — | approved | ciência simultânea |
| rel:S10 | `state:eua-governo-1789` | contemporâneo-de | `proc:revolucao-francesa` | índice temporal | — | approved | revolução atlântica simultânea |
| rel:S11 | `evt:posse-washington-1789` | parte-de | `state:eua-governo-1789` | documental | alta | approved | 30/04/1789, Nova York |
| rel:S12 | `proc:trafico-atlantico` | contemporâneo-de | `proc:revolucao-francesa` | índice temporal | — | pending | escravidão ativa em 1789 |
| rel:S13 | `entity:povos-indigenas-brasil` | contemporâneo-de | (1789) `scene:world-1789-french-revolution` | índice temporal | — | pending | povos indígenas na cena |
| rel:S14 | `region:mundo-atlantico` | conecta | Europa↔África↔Américas | interpretação (claim) | alta | pending | recorte analítico (§4) |
| rel:S15 | `concept:escravidao` | conecta | África↔Brasil↔Caribe↔economia atlântica | interpretação (claim) | alta | pending | estrutura central, não detalhe |
| rel:S16 | `state:ciclo-ouro-minas` | contextualiza | `evt:inconfidencia-mineira` | documental | alta | pending | declínio + *derrama* → revolta |
| rel:S17 | `state:africa-ocidental-1789` | contemporâneo-de | `proc:revolucao-francesa` | índice temporal | — | pending | África com agência (Lei 10.639) |
| rel:S18 | `entity:imperio-mali` | contexto-anterior-de | `state:africa-ocidental-1789` | documental | alta | pending | **não** simultâneo (§4) |
| rel:S19 | `claimset:causas-revolucao-francesa` | qualifica | `proc:revolucao-francesa` | estrutural | — | pending | ClaimSet → Process |
| rel:S20 | `proc:trafico-atlantico` | causou | `concept:diaspora` | documental (claim) | alta | pending | diáspora como agência/cultura |

> Links inválidos evitados: nenhuma aresta usa `entity:imperio-mali` como **simultâneo** de 1789 (apenas `contexto-anterior-de`). Nenhuma aresta afirmativa sem fonte/confiança.

---

## 7. Globo/mapa da cena 1789 (Tarefa 7)

Descrição **conceitual** (sem UI final; sem geometria inventada). Onde não há geometria validada: `PENDENTE_REFINAMENTO_ESPACIAL`.

- **Foco inicial:** França (`region:franca-1789`), com a Europa Ocidental enquadrada — mas **com indicadores de simultaneidade acesos** em outras regiões (não um mapa só da França).
- **Regiões visíveis:** França; Capitania de Minas Gerais (via correspondência moderna); América do Norte (1789); mundo atlântico (rotas); África Ocidental/Sahel; território otomano; China Qing; territórios indígenas nas Américas.
- **Marcadores (pontuais):** `place:paris` (Bastilha/Declaração), `place:versalhes` (Estados Gerais), **marcador Lavoisier/Paris** (ciência), **marcador Inconfidência/Minas** (`place:ouro-preto`), Nova York (posse de Washington — **não** Washington, D.C.), `place:caribe` (nó do tráfico).
- **Rotas:** rotas atlânticas do tráfico e do comércio (`region:mundo-atlantico`) — exibidas como **fluxos**, com rótulo de que conectam pessoas escravizadas, mercadorias e capitais.
- **Fronteiras históricas:** França 1789, América do Norte 1789, território otomano, China Qing — todas marcadas `PENDENTE_REFINAMENTO_ESPACIAL` até geometria validada (Natural Earth histórico). **Nunca** projetar fronteiras atuais.
- **ModernCorrespondence:** Capitania de MG → MG atual; "território que hoje é o Brasil" como **lente**; territórios indígenas sobrepostos às fronteiras coloniais, não substituídos.
- **Camadas ligadas/desligadas:** ligadas por padrão — Política, Ciência, Brasil colonial, simultaneidade; sob demanda — Economia/escravidão (mediada), África, povos indígenas. Paleogeografia: desligada (irrelevante em 1789).
- **Itens sensíveis ocultos ou mediados:** tráfico, escravidão, violência colonial, povos indígenas → exibidos **mediados** (rótulo "tema sensível — em revisão") ou ocultos enquanto `pending`; jamais como fato cru.
- **Itens pending não exibidos:** todos com `reviewStatus ∈ {pending, legal-review}` (invariante de exibição). O **núcleo factual** (eventos datados) aparece; o restante aguarda revisão.
- **Níveis de zoom:** (1) mundo/simultaneidade; (2) região (ex.: França, Minas, África Ocidental); (3) local/marcador (Paris, Ouro Preto). Sem inventar detalhe geométrico em nível fino.
- **Legenda epistemológica:** distingue fato documentado · interpretação · estimativa · reconstrução · ClaimSet (cores/ícones conceituais, não definidos como UI).
- **Legenda temporal:** distingue evento pontual (1789) · processo longo (atravessa 1789) · estado (condição em 1789) · contexto anterior/posterior.
- **Legenda editorial:** sinaliza tema sensível, item em revisão, fonte pendente, geometria pendente.

**Obrigatórios presentes:** França ✓ · Capitania de Minas Gerais ✓ · América do Norte ✓ · mundo atlântico ✓ · África Ocidental ✓ · Império Otomano ✓ · China Qing ✓ · territórios indígenas nas Américas ✓ · rotas atlânticas ✓ · marcador Lavoisier/Paris ✓ · marcador Inconfidência/Minas ✓.

---

## 8. Timeline da cena 1789 (Tarefa 8)

Descrição conceitual do eixo. Distingue **processo longo · evento pontual · state · contexto anterior · consequência posterior · ClaimSet · nota editorial**.

- **Zoom no ano de 1789:** eixo centrado em 1789, com resolução de **mês/dia** para os eventos pontuais.
- **Eventos pontuais de 1789 (dia):** Estados Gerais (maio) → posse de Washington (30/04) → Queda da Bastilha (14/07) → Declaração dos Direitos (26/08); Inconfidência (1789); início do reinado de Selim III (04/1789); publicação do *Traité* de Lavoisier (1789).
- **Processos longos que atravessam 1789:** Revolução Francesa (1789–99); crise fiscal francesa (1770s–89); tráfico atlântico (séc. XVI–XIX); Revolução Industrial (1760–1840); resistência indígena (1500–presente).
- **States (condição em 1789):** França do Antigo Regime; governo constitucional dos EUA; Império Otomano; China Qing; África Ocidental; economia atlântica; ciclo do ouro em declínio.
- **Contexto anterior relevante:** Estados Gerais como antecedente institucional; Império do Mali (séc. XIII–XIV) como **contexto africano anterior**; Revolução Americana (1776) como antecedente atlântico.
- **Consequência posterior imediata:** Tiradentes executado (1792); radicalização/Terror (1792–94); morte de Lavoisier (1794) — ligados por `ver consequências`.
- **Filtros por camada:** Política, Economia, Ciência, Brasil, África, Povos indígenas, Cultura — cada um liga/desliga itens.
- **Claims e ClaimSets na timeline:** itens com ClaimSet exibem ícone de **debate** (causas da Revolução, Inconfidência, direitos universais, escravidão, presença indígena, Iluminismo) — abrem a pluralidade, não um veredito.
- **Incerteza:** processos com início difuso (crise fiscal) e estados com fronteira/peso incertos aparecem com marcação de incerteza (faixa), nunca data seca inventada.
- **Itens pending ocultos:** itens sensíveis em revisão não aparecem como fato; aparecem **mediados** ou ocultos.
- **Itens publicáveis exibidos:** eventos datados do núcleo factual (Estados Gerais, Bastilha, Declaração, posse de Washington, *Traité*) já são exibíveis.

---

## 9. Dossiê da cena 1789 (Tarefa 9)

Desenho **conceitual** do dossiê (não é plano de aula, não é currículo, não é UI final). Quinze blocos navegáveis, cada um com sua legenda epistemológica.

1. **Visão geral** — "1789: o mundo em simultaneidade". Síntese: a Revolução Francesa como parte de um planeta vivo. Claim da cena + aviso de que temas sensíveis estão em revisão.
2. **O foco: França e Revolução Francesa** — Estados Gerais → Bastilha → Declaração; `state:franca-1789`, `concept:antigo-regime`; causas em `claimset:causas-revolucao-francesa` (debate, não veredito).
3. **O mundo em 1789** — painel de simultaneidade: EUA, Otomano, Qing, África Ocidental, Brasil colonial, mundo atlântico, povos indígenas — cada um com seu cartão.
4. **Brasil colonial / Capitania de Minas Gerais** — Inconfidência Mineira; ciclo do ouro em declínio; *derrama*; `claimset:inconfidencia-interpretacoes`; nota antianacronismo (Capitania, não estado).
5. **África e mundo atlântico** — `state:africa-ocidental-1789` (Oyo, Daomé, Axânti) com **agência própria**; rotas atlânticas; nota de que o Mali é contexto anterior, não simultâneo.
6. **Povos indígenas nas Américas** — presença viva e resistência (`claimset:presenca-indigena-apagamento`); territórios sobrepostos às fronteiras coloniais; **fontes orais** reconhecidas.
7. **Ciência e tecnologia** — Lavoisier e a química moderna; Revolução Científica/industrialização incipiente; "1789 não é só política".
8. **Economia global** — economia atlântica e o lugar **central** (não neutro) da escravidão; `claimset:escravidao-centralidade-atlantica`; China Qing como grande economia (contraponto).
9. **ClaimSets e debates historiográficos** — hub dos 7 ClaimSets da cena; cada debate com seus claims legítimos e a posição sem equivalência claramente marcada.
10. **Fontes e confiança** — proveniência por claim (`source:`); nível de confiança; o que é fato, interpretação, estimativa, reconstrução; fontes pendentes sinalizadas.
11. **Itens ocultos por pendência/revisão** — lista transparente do que **não** está exibido e **por quê** (sensível/em revisão/fonte pendente) — honestidade epistêmica como recurso, não defeito.
12. **Como evitar anacronismos** — os 7 casos da §4, em linguagem de dossiê (Brasil colonial ≠ Brasil; Capitania ≠ estado; D.C. ainda não é capital; África com agência; atlântico é recorte).
13. **Botão "navegar para outro lugar em 1789"** — troca o **foco espacial** mantendo o ano: da França para Minas, África Ocidental, China, território otomano — a simultaneidade em ação.
14. **Botão "comparar com 1788 / 1790 / 1792"** — desloca o **eixo temporal** mantendo o escopo: antecedentes (1788), desdobramentos (1790), radicalização (1792, execução de Tiradentes).
15. **Botão "ver consequências"** — segue as arestas `sucessor-de`/`causou` para frente: Terror, abolições futuras, independências — sem fechar em narrativa única.

---

## 10. Relatório de qualidade da cena (Tarefa 10)

Roster curado da cena `scene:world-1789-french-revolution` (reúso de 4B/4C + 8 itens novos + 6 ClaimSets novos + 1 objeto de cena).

1. **Itens na cena:** **~60** (59 itens + o objeto de cena), dos quais **15 novos** nesta etapa (8 nós + 6 ClaimSets + 1 objeto).
2. **Event:** **6** — `estados-gerais-1789`, `queda-bastilha-1789`, `declaracao-direitos-1789`, `posse-washington-1789`, `lavoisier-traite-1789`, `inconfidencia-mineira`.
3. **Process:** **4** centrais — `revolucao-francesa`, `crise-fiscal-franca`, `trafico-atlantico`, `resistencia-indigena` (+ 2 contextuais: `revolucao-cientifica`, `revolucao-industrial`).
4. **State:** **9** — `franca-1789`, `eua-governo-1789`, `imperio-otomano-1789`, `china-qing-1789`, `africa-ocidental-1789`, `economia-mundo-atlantico-1789`, `ciclo-ouro-minas`, `sociedades-precolombianas`, `indigenas-pre1500-brasil`.
5. **Concept:** **10** — `iluminismo`, `antigo-regime`, `escravidao`, `colonialismo`, `diaspora`, `revolucao-politica`, `imperio`, `estado`, `modern-correspondence`, `simultaneidade-historica`.
6. **Entity:** **9** — `franca`, `estados-unidos`, `george-washington`, `imperio-otomano`, `china-qing`, `lavoisier`, `povos-indigenas-brasil`, `africanos-escravizados-afrodescendentes`, `imperio-mali` (contexto).
7. **Place:** **6** — `paris`, `versalhes`, `ouro-preto`, `washington-dc`, `caribe`, `lisboa`.
8. **Region:** **8** — `franca-1789`, `capitania-minas-gerais`, `territorio-brasil-atual`, `america-norte-1789`, `africa-ocidental`, `sahel`, `china-qing`, `mundo-atlantico`.
9. **ClaimSet:** **7** — `causas-revolucao-francesa`, `atlantico-revolucionario-1789`, `inconfidencia-interpretacoes`, `direitos-universais-limites`, `escravidao-centralidade-atlantica`, `presenca-indigena-apagamento`, `iluminismo-limites`.
10. **Publicáveis (núcleo factual, baixo risco):** **~20** — eventos datados (Estados Gerais, Bastilha, posse de Washington, *Traité*), entidades/personagens factuais (Washington, Lavoisier, França, EUA), conceitos não sensíveis (Iluminismo núcleo, Antigo Regime, Estado, Império, ModernCorrespondence, Simultaneidade) e places (Paris, Versalhes, Lisboa).
11. **Pending:** **~37** — todos os itens sensíveis (escravidão, tráfico, colonialismo, diáspora, povos indígenas, Inconfidência, África Ocidental, economia atlântica, ciclo do ouro, Otomano, Qing), os 7 ClaimSets e os itens com refinamento espacial/fonte pendentes.
12. **Risco editorial alto/crítico:** **~13** — `trafico-atlantico` (crítico), `escravidao` (crítico), `africanos-escravizados` (crítico), `povos-indigenas-brasil`/IND-01/IND-03/BR-03 (crítico), `africa-ocidental-1789` (alto), `ciclo-ouro-minas` (alto), `economia-mundo-atlantico-1789` (alto), `colonialismo` (alto), `inconfidencia-mineira` (médio-alto).
13. **Risco de licença:** **baixo/médio** — todos em risco **0–2** (fontes verdes); **nenhum** alto. Geometrias históricas em `PENDENTE_REFINAMENTO_ESPACIAL` (não é risco de licença).
14. **Não exibíveis ainda:** os ~37 itens `pending` + qualquer overlay sensível; **só** o núcleo factual datado aparece no globo/timeline/dossiê.
15. **Gabarito para cenas futuras:** o próprio objeto `scene:world-1789-french-revolution` (padrão de cena); `evt:queda-bastilha-1789` (evento datado limpo); `evt:inconfidencia-mineira` (ModernCorrespondence sem anacronismo); `state:africa-ocidental-1789` (antieurocentrismo com fonte oral); `claimset:escravidao-centralidade-atlantica` (debate sobre **peso**, nunca sobre moralidade); `claimset:presenca-indigena-apagamento` (presença/agência); o **caso Mali** (como tratar contexto anterior sem anacronismo).
16. **Fontes a confirmar:** `state:africa-ocidental-1789` (`PENDENTE_CONFIRMACAO_FONTE` — polities específicas); `state:economia-mundo-atlantico-1789` (OWID/quantitativos); eventos franceses (Arquivo/historiografia, confirmação por asset); geometrias históricas de 1789 (Natural Earth histórico); fontes africanas e indígenas (incl. **tradição/registro oral**).

---

## 11. Próximos passos para a Etapa 4E (Tarefa 11)

A Etapa 4D entregou a **primeira cena ponta-a-ponta** — a função "O que acontecia no mundo neste momento?" demonstrada com rigor, simultaneidade global e antianacronismo. A **Etapa 4E**, quando solicitada, pode:

1. **Replicar o padrão de cena em um segundo recorte temporal** (ex.: outra data canônica), reusando o objeto `scene:` e o gabarito desta etapa — provando que a cena de 1789 **virou método**, não caso único.
2. **Concluir a revisão humana** dos ~37 itens `pending` desta cena (papéis da Etapa 3.1: histórica, vieses, oral indígena/afro), liberando-os para exibição.
3. **Fechar `PENDENTE_REFINAMENTO_ESPACIAL`** das fronteiras de 1789 (França, América do Norte, território otomano, China Qing) com geometria histórica validada — sem inventar fronteiras.
4. **Reificar `Source` e `MediaAsset`** da cena (proveniência por claim; mídia com `natureLabel`/licença-por-asset), confirmando as fontes pendentes.
5. **Testar os botões de navegação** (outro lugar em 1789; comparar 1788/1790/1792; ver consequências) como **consultas** sobre o grafo, ainda conceitualmente — não como UI.
6. **Escalar à modelagem** (não resolver) as pendências estruturais herdadas: datum do eixo (1950 BP × J2000) e `OceanographicState` — embora não afetem 1789, seguem em aberto.

**O que a 4E explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (1/1.1), modelagem (Etapa 2) ou política editorial (Etapa 3.1).

---

*Documento de entrega da Etapa 4D, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B, 4C). Entrega a cena canônica de 1789 ponta-a-ponta: objeto de cena `scene:world-1789-french-revolution`, itens centrais e simultâneos (com a Revolução Francesa em simultaneidade global — Brasil colonial, EUA, Otomano, Qing, África Ocidental, mundo atlântico, escravidão, povos indígenas, ciência e economia), tratamento explícito de ModernCorrespondence/anacronismo (incluindo o caso Mali), 7 ClaimSets da cena, relationship graph, descrição conceitual de globo e timeline, dossiê de 15 blocos e relatório de qualidade. Não escreve código, não propõe MVP, não define stack, não avança para UX final e não entra em currículo/professor/plano de aula. Próxima etapa, quando solicitada: Etapa 4E — replicação do padrão de cena em novo recorte e conclusão das revisões.*
