# Etapa 1.1 — Checklist de Licenças e Portão de Ingestão

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Microetapa operacional · sob a baseline v1.0 (Etapa 0) e a auditoria aprovada (Etapa 1) · 12/06/2026
**Natureza:** documento **operacional de curadoria e licenciamento**. Não modela o Knowledge Core, não contém código de aplicação, não propõe MVP, não avança para arquitetura técnica. É a ferramenta que impede que dados, imagens, mapas, textos ou *assets* entrem no sistema com licença incompatível, fonte fraca ou *claim* sem proveniência.
**Público:** curadores (decidem por item), desenvolvedores (implementam o portão na Etapa 2+), revisores jurídicos (resolvem os casos de risco alto).

> **Nota sobre os campos de metadados (Tarefa 5):** o que segue ali é uma **especificação de metadados de curadoria/licença** — um dicionário de campos —, não implementação de software. Mirrors a estrutura que você forneceu apenas para legibilidade.

---

## Como usar este documento (fluxo de um item)

```
Item chega
   │
   ▼
[T1] Checklist de entrada (15 perguntas) ──► determina natureza, fonte, licença, epistemia
   │
   ▼
[T4] Classificação de risco (0–5) ──────────► dá o nível de risco do item
   │
   ▼
[T2] Matriz de decisão ─────────────────────► converte risco+natureza em UMA decisão de entrada
   │
   ▼
[T3] Política de licenças ──────────────────► justifica a decisão por tipo de licença
   │
   ▼
[T5] Metadados obrigatórios ────────────────► registra proveniência/licença junto ao item
   │
   ▼
[T6] Casos de borda ────────────────────────► resolve os itens ambíguos
```

Regra de ouro herdada da Etapa 1: **fato × expressão × objeto digitalizado.** Fato não é protegível (re-codificável com atribuição); expressão é governada pela licença; obra em domínio público digitalizada por terceiro depende de **qual provedor** entregou o *scan*.

---

## TAREFA 1 — Checklist de entrada (Portão)

Toda a 15 perguntas devem ser respondidas e registradas **antes** de o item entrar. A coluna "Gatilho" indica a resposta que **bloqueia** ou **escalona** (envia a curador/jurídico).

| # | Pergunta | O que registrar | Gatilho de bloqueio/escalonamento |
|---|---|---|---|
| 1 | É **fato, expressão ou objeto digitalizado**? | `fato` / `expressão` / `obj-digitalizado` | Se `expressão` + licença NC → bloqueia como expressão (ver Q7) |
| 2 | Qual é a **fonte original**? | `sourceName`, `originalUrl` | Sem fonte identificável → bloqueia |
| 3 | A fonte é **autoridade primária (A), agregador confiável (B) ou índice (C)**? | `sourceTier` = A/B/C | Se C e o item for *claim* → só índice (ver Q11/Q12) |
| 4 | A licença permite **uso comercial**? | `nonCommercial` = sim/não | Se não-comercial → Risco 4 (ver Q7) |
| 5 | A licença exige **atribuição**? | `attributionRequired` = sim/não | Sem texto de atribuição definido quando exigido → bloqueia |
| 6 | A licença exige **ShareAlike**? | `shareAlikeRequired` = sim/não | Se sim → camada isolada obrigatória (Risco 3) |
| 7 | A licença é **não-comercial (NC)**? | parte de `license` | Se sim e for expressão → **não entra como expressão**; só fato re-derivado de fonte livre |
| 8 | A licença é **por item/dataset**? | `itemLevelLicense` = sim/não | Se sim e a licença do item específico for desconhecida → bloqueia até confirmar |
| 9 | Há risco de **contaminar o Knowledge Core**? | `rightsNotes` | NC/SA/ODbL/proprietária sem tratamento → bloqueia/escalona |
| 10 | O item é **claim, fonte, mídia, mapa, dado tabular, geometria, texto ou imagem**? | tipo do item | Mídia/mapa/imagem → regime de licença por asset (camada de mídia) |
| 11 | O item tem **fonte A/B**? | referência à fonte A/B | *Claim* sem fonte A/B → **não entra como claim** (no máximo índice) |
| 12 | O item depende de **Wikidata/Wikipedia/IA como autoridade**? | sim/não | Se sim → **rejeita como autoridade**; rebaixa a índice ou busca fonte A/B |
| 13 | O item tem **nível de confiança**? | `confidenceLevel` (campo da Etapa 2) | *Claim* sem nível de confiança → bloqueia até tipar |
| 14 | O item envolve **hipótese, controvérsia ou inferência**? | `claimType` (campo da Etapa 2) | Se sim e não rotulado → **não publica** antes de rotular |
| 15 | O item exige **revisão humana** antes da publicação? | `reviewStatus` | Tópico sensível/controverso/NC/sem licência → revisão obrigatória |

**Regras de parada (resumo dos *hard stops*):**

1. *Claim* sem fonte A/B → não entra (Q11).
2. Dependência de Wikidata/Wikipedia/IA como autoridade → não entra como fato (Q12).
3. Expressão sob NC → não entra como expressão (Q7); só o fato re-derivado de fonte livre.
4. Licença por item desconhecida → bloqueio até confirmação (Q8).
5. Fonte sem licença declarada → bloqueio (Q2 + política §10).
6. Inferência/hipótese/controvérsia sem rótulo → não publica (Q13/Q14).

---

## TAREFA 2 — Matriz de decisão

**Saídas de decisão (códigos):**

| Código | Decisão |
|---|---|
| **AUTO** | entra automaticamente |
| **ATRIB** | entra com atribuição |
| **ISOLA** | entra em camada isolada (ShareAlike/ODbL) |
| **FATO** | entra apenas como fato recodificado |
| **REVH** | entra apenas após revisão humana |
| **CONF** | entra apenas após confirmação por asset |
| **COMER** | entra somente com licença comercial (contrato) |
| **NAO** | não entra |
| **INDX** | pode ser usado apenas como índice |

**Aplicação aos exemplos obrigatórios** (decisão primária = o caso típico; condicionais = quando o item difere):

| Fonte | Decisão primária | Decisões condicionais | Regra / razão |
|---|---|---|---|
| **NASA** | **AUTO** | imagem com pessoa identificável/logo → REVH | Domínio público (US gov). Atribuição é boa prática, não exigência. |
| **Macrostrat** | **ATRIB** | — | CC BY, API. Atribuição rastreada. |
| **ICS** | **FATO** | gráfico/imagem do chart → NAO | Limites e nomes são fato; o gráfico é CC BY-NC-SA. Atribuir Cohen et al./ICS. |
| **GPlates/EarthByte** | **ATRIB** | sempre rotular como **reconstrução modelada** | Dados CC BY 3.0 / software GPL. Claim do tipo "inferência/modelo". |
| **PBDB** | **ATRIB** | registros com restrição histórica de contribuidor → CONF | CC BY 4.0; usar a versão pública liberada. |
| **Natural Earth** | **AUTO** | — | Domínio público. |
| **geoBoundaries** | **ATRIB** | — | CC BY 4.0. Substituto aberto do GADM. |
| **IBGE** | **ATRIB** | microdados **não** desidentificados → NAO/REVH (SAR) | Aberto (Dec. 8.777 + LAI) com atribuição; microdados restritos. |
| **BNCC/LDB/LGPD** | **AUTO** | — | Texto legal/normativo não protegido (Lei 9.610/98, art. 8). Camada de conformidade. |
| **Wikidata** | **INDX** | — | CC0, porém **índice/ponte apenas**. Nunca origem de claim. |
| **Wikipedia** | **INDX** | — | CC BY-SA; localização/orientação apenas. Nunca autoridade. |
| **Seshat** | **NAO** | fato re-derivável de fonte A livre → FATO (via curadoria) | CC BY-NC-SA. Não ingerir a expressão. |
| **GADM** | **NAO** | — | CC BY-NC. Usar geoBoundaries. |
| **ACLED** | **NAO** | com contrato → COMER | Licença comercial obrigatória + cláusula anti-substituto. |
| **David Rumsey** | **NAO** | mesmo original PD via provedor PD-explícito → CONF/ATRIB | *Scans* CC BY-NC-SA; a obra original pode ser PD em outra fonte. |
| **OSM** | **ISOLA** | — | ODbL (ShareAlike de banco derivado). Atribuição "© OpenStreetMap contributors". |
| **MapBiomas** | **ISOLA** | — | CC BY-SA. Camada isolada. |
| **Wikimedia Commons** | **CONF** | PD/CC0 → AUTO · CC BY → ATRIB · CC BY-SA → ISOLA · NC → NAO | Licença **por arquivo**; triagem por asset. |
| **Europeana/DPLA** | **CONF** | conforme *rights statement* do item | Agregadores; licença por item. |
| **Our World in Data** | **ATRIB** | dados de terceiros → CONF por indicador | CC BY (próprio); terceiros pela licença original. |

---

## TAREFA 3 — Política de licenças

Para cada categoria: **(KC)** pode entrar no Knowledge Core (núcleo factual)? **(ISO)** pode entrar em camada isolada? **(COM)** uso comercial? **(ATR)** exige atribuição? **(ISOL)** exige isolamento? **(JUR)** exige revisão jurídica? + recomendação.

| # | Categoria | KC | ISO | COM | ATR | ISOL | JUR | Recomendação |
|---|---|---|---|---|---|---|---|---|
| 1 | **Domínio público (PD)** | Sim | n/a | Sim | Não¹ | Não | Não | Entrada livre; registrar proveniência. |
| 2 | **CC0** | Sim | n/a | Sim | Não¹ | Não | Não | Como PD: livre, registrar origem. |
| 3 | **CC BY** | Sim | n/a | Sim | **Sim** | Não | Não | Entrada com atribuição rastreada (texto de crédito no item). |
| 4 | **CC BY-SA** | **Não (núcleo)** | **Sim** | Sim | Sim | **Sim** | Recom. | Camada isolada; não fundir no núcleo factual. |
| 5 | **ODbL** | **Não (núcleo)** | **Sim** | Sim | Sim | **Sim** | Recom. | Camada isolada de dados; isolar o banco derivado. |
| 6 | **CC BY-NC** | **Não (expressão)** | Não resolve² | **Não** | Sim | n/a | Se houver dúvida | Não entra como expressão; só o fato re-derivado de fonte livre. |
| 7 | **CC BY-NC-SA** | **Não** | Não resolve² | **Não** | Sim | n/a | Se houver dúvida | Idem NC; usar fato re-derivado. |
| 8 | **Proprietária** | **Não sem contrato** | Não sem contrato | Só c/ licença | Conforme contrato | — | **Sim** | Bloquear até contrato; revisão jurídica. |
| 9 | **Por item/dataset** | Condicional | Condicional | Condicional | Condicional | Condicional | Conforme item | Triagem por asset: resolver à categoria real antes de decidir. |
| 10 | **Sem licença clara** | **Não** | Não | Não | — | — | **Sim** | Bloquear. "Ausência de licença ≠ domínio público." |
| 11 | **Texto legal/normativo BR** | **Sim** | n/a | Sim | Não¹ | Não | Não | Livre (art. 8, Lei 9.610/98). É conformidade, não conhecimento. |
| 12 | **Fatos recodificados** | **Sim** | n/a | Sim | Sim¹ | Não | Não³ | **Padrão de ouro** de ingestão; registrar a fonte do fato. |
| 13 | **Imagens/mapas históricos** | Condicional | Condicional | Condicional | Conforme | Conforme | Conforme | Confirmar (a) PD da obra original e (b) licença do *scan*; preferir provedor PD-explícito. |
| 14 | **Dados científicos derivados** | Condicional | Condicional | Conforme | Sim | Se houver SA na cadeia | Se houver dúvida | Herdam a licença **mais restritiva** da cadeia; rastrear proveniência completa. |
| 15 | **Dados gerados por IA** | **Não (fato/fonte)** | Auxiliar rotulado | n/a | n/a | n/a | Rotulagem | Nunca fonte factual; nada entra sem curadoria humana; sempre rotulado (A3/Q5). |

¹ Atribuição não é exigência legal, mas é **boa prática científica** e fica no registro de proveniência.
² Isolamento **não** remove a obrigação NC: a expressão continua não-comercial onde quer que esteja.
³ Fato não é protegível, logo não exige revisão jurídica; ainda assim registra-se de onde o fato veio.

---

## TAREFA 4 — Classificação de risco

| Nível | Definição | Exemplos | Decisão padrão | Revisão necessária | Como registrar |
|---|---|---|---|---|---|
| **Risco 0** | Livre | PD, CC0, fato recodificado, texto legal BR (NASA, Natural Earth, BNCC) | **AUTO** | Validação automática de licença | `licenseRiskLevel=0`, `ingestionDecision=auto` |
| **Risco 1** | Atribuição simples | CC BY (Macrostrat, PBDB, geoBoundaries, Pleiades, World Bank, OWID próprio) | **ATRIB** | Conferência do texto de atribuição | `riskLevel=1`, `attributionRequired=true`, `attributionText` preenchido |
| **Risco 2** | Licença heterogênea por item | Wikimedia Commons, Europeana/DPLA, GBIF, datasets do WHG | **CONF** | Curador confirma licença do item específico | `riskLevel=2`, `itemLevelLicense=true`, `reviewStatus=pending` até confirmar |
| **Risco 3** | ShareAlike/ODbL — exige isolamento | OSM, MapBiomas, ESA/Gaia, texto de Wikipedia | **ISOLA** | Confirmar fronteira de isolamento; jurídica recomendada | `riskLevel=3`, `shareAlikeRequired=true`, `allowedUse=isolated-layer` |
| **Risco 4** | Não-comercial — não entra como expressão | Seshat, GADM, gráfico do ICS, *scans* do David Rumsey | **NAO** (expressão) / **FATO** se re-derivável de fonte livre | Curador + confirmação da re-derivação | `riskLevel=4`, `nonCommercial=true`, `ingestionDecision=fact-only` ou `rejected` |
| **Risco 5** | Proprietária/comercial/restritiva | ACLED, Deep Time Maps | **NAO** sem contrato (**COMER** com contrato) | **Jurídica obrigatória** | `riskLevel=5`, `license=proprietary`, `ingestionDecision=blocked-pending-contract` |

---

## TAREFA 5 — Metadados obrigatórios

Especificação dos metadados de **proveniência e licença** que acompanham **todo** item futuro. Dicionário de campos:

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sourceId` | id | Sim | Identificador interno da fonte. |
| `sourceName` | texto | Sim | Nome legível da fonte (ex.: "Paleobiology Database"). |
| `originalUrl` | url | Sim | URL exata do item/registro original. |
| `retrievedAt` | data-hora | Sim | Quando foi obtido (para *snapshot*/versionamento). |
| `license` | enum | Sim | PD / CC0 / CC BY / CC BY-SA / ODbL / CC BY-NC / CC BY-NC-SA / proprietária / por-item / legal-BR / fato / sem-licenca. |
| `licenseUrl` | url | Cond. | Link ao texto da licença (quando aplicável). |
| `licenseRiskLevel` | 0–5 | Sim | Nível da Tarefa 4. |
| `attributionRequired` | booleano | Sim | Se exige atribuição. |
| `attributionText` | texto | Cond. | Texto exato de crédito a exibir (se exigido). |
| `shareAlikeRequired` | booleano | Sim | Se exige ShareAlike (CC BY-SA/ODbL). |
| `nonCommercial` | booleano | Sim | Se é não-comercial. |
| `itemLevelLicense` | booleano | Sim | Se a licença é por item/dataset. |
| `sourceTier` | A/B/C | Sim | Autoridade primária / agregador / índice. |
| `authorityType` | enum | Sim | `primary` / `aggregator` / `index`. |
| `provenanceChain` | lista | Cond. | Cadeia de fontes quando o dado é derivado/sintetizado (L4 da Etapa 1). |
| `rightsNotes` | texto | Cond. | Observações de direitos (ex.: "obra PD, *scan* NC"). |
| `allowedUse` | enum | Sim | `knowledge-core` / `isolated-layer` / `media-dossier` / `index-only` / `blocked`. |
| `ingestionDecision` | enum | Sim | `auto` / `with-attribution` / `isolated-layer` / `fact-only` / `human-review` / `confirm-per-asset` / `commercial-license-only` / `rejected` / `index-only`. |
| `reviewStatus` | enum | Sim | `not-required` / `pending` / `approved` / `rejected` / `legal-review`. |

**Campos epistêmicos companheiros** — exigidos pela checklist (Q13/Q14), mas **pertencem ao modelo do Knowledge Core (Etapa 2)**, não a este portão: `claimType` (fato documentado / medição / inferência científica / estimativa / hipótese / controvérsia / interpretação historiográfica / reconstrução modelada / representação artística / aproximação didática) e `confidenceLevel`. Registrados aqui apenas como referência de acoplamento.

**Esquema de referência** (especificação de metadados — não é implementação):

```
ProvenanceMetadata = {
  sourceId,
  sourceName,
  originalUrl,
  retrievedAt,
  license,                 // enum acima
  licenseUrl,
  licenseRiskLevel,        // 0–5
  attributionRequired,
  attributionText,         // novo: texto de crédito pronto
  shareAlikeRequired,
  nonCommercial,
  itemLevelLicense,
  sourceTier,              // A | B | C
  authorityType,           // primary | aggregator | index
  provenanceChain,         // novo: cadeia multi-elo (L4)
  rightsNotes,
  allowedUse,              // enum acima
  ingestionDecision,       // enum acima
  reviewStatus             // enum acima
  // companheiros (Etapa 2): claimType, confidenceLevel
}
```

Acréscimos justificados em relação à sua lista: `attributionText` (para o crédito ser exibível sem retrabalho) e `provenanceChain` (porque EarthByte/OWID sintetizam várias fontes — a atribuição de um elo só não basta).

---

## TAREFA 6 — Casos de borda

1. **Mapa antigo em PD, mas *scan* com licença NC.** A *obra* é livre; o *scan* específico é NC. Não usar o *scan* NC. Obter o mesmo original de provedor PD-explícito (Library of Congress, Wikimedia Commons PD, Internet Archive, Old Maps Online → instituição hospedeira). Se só existir o *scan* NC, é Risco 4 (não entra como expressão). Registrar `rightsNotes="obra PD; scan NC; usar provedor alternativo"`.

2. **Dado factual em fonte NC.** O fato é livre; a expressão é NC. Re-derivar o fato de uma fonte A/B livre (`FATO`). Se a fonte NC for a única, registrar como pendência e buscar corroboração livre — **nunca** copiar a expressão. Caso canônico: **Seshat**.

3. **Imagem do Wikimedia Commons com CC BY-SA.** Risco 3. Entra na **camada de mídia isolada**, com atribuição. A obrigação ShareAlike fica na imagem; ela **não** deve impor ShareAlike ao núcleo factual. Registrar `shareAlikeRequired=true`, `allowedUse=media-dossier` (isolada).

4. **Dado OSM em ODbL.** Risco 3. Geometria em **camada isolada**; um banco derivado de OSM herda ODbL → manter separado do núcleo. Atribuição obrigatória "© OpenStreetMap contributors". Registrar `allowedUse=isolated-layer`.

5. **Mapa do ICS em CC BY-NC-SA, mas limites estratigráficos como fatos.** Ingerir os **limites e idades como fato recodificado** (`FATO`, Risco 0). Não redistribuir o gráfico. Atribuir Cohen et al./ICS como boa prática. Veículo preferencial: **Macrostrat** (CC BY, API), que entrega os mesmos fatos com licença limpa.

6. **Evento histórico obtido via Wikidata.** Wikidata é **índice** (`INDX`): usar para localizar/desambiguar e capturar o identificador; depois buscar a **autoridade A/B** que sustenta o evento. O *claim* só entra com fonte A/B. Nunca citar Wikidata como autoridade. Registrar a fonte A/B real, não o Wikidata.

7. **Texto gerado por IA.** Nunca fonte nem fato. Pode ser **rascunho de linguagem** (adaptação por faixa etária, resumo didático, roteiro), **rotulado** e **revisado por humano**. Não entra no Knowledge Core como conteúdo factual (A3/Q5). Registrar `reviewStatus=pending` e rótulo de IA.

8. **Imagem gerada por IA.** Não é fotografia nem reconstrução científica. Se usada, rotular explicitamente como **"representação artística / aproximação didática gerada por IA"**; nunca apresentada como fonte/registro. Revisão humana obrigatória; cautela redobrada por o produto ser dirigido a estudantes (inclusive menores) e por temas sensíveis.

9. **Artigo científico com figura protegida.** O **texto e os dados factuais** podem ser parafraseados/recodificados com citação. A **figura específica** é expressão protegida → **não reproduzir** sem permissão/licença. Recriar a visualização a partir dos dados, ou usar figura sob licença aberta. Revisão jurídica se a reprodução for desejada.

10. **Fonte sem licença explícita.** "Sem licença declarada **≠** domínio público." Bloquear até esclarecer; tentar contato/termos de uso. *Default* conservador = **não entra**. Risco indeterminado → revisão jurídica. Registrar `license=sem-licenca`, `reviewStatus=legal-review`.

---

## TAREFA 7 — O que muda na Etapa 2 por causa desta checklist

Concretamente, a modelagem do Knowledge Core (Etapa 2) passa a nascer condicionada por este portão:

1. **`ProvenanceMetadata` é acoplado a todo item, não opcional.** O modelo da Etapa 2 não terá "entidade sem proveniência": os campos da Tarefa 5 viajam com cada *claim*, fonte, mídia e geometria.

2. **`sourceTier` A/B é obrigatório para qualquer entidade factual.** Índices (C — Wikidata/Wikipedia/IA) ficam num **subsistema de reconciliação separado**, sem poder de afirmar. A Etapa 2 modela essa separação explicitamente (resolve a regra "índice ≠ autoridade" como estrutura, não como recomendação).

3. **A fronteira "núcleo proprietário" × "camada isolada (SA/ODbL)" vira decisão de modelagem.** OSM, MapBiomas e demais ShareAlike entram em camadas que a modelagem mantém **fisicamente separadas** do núcleo factual, para a obrigação copyleft não atravessar a fronteira.

4. **O padrão "fato recodificado" é um tipo de ingestão de primeira classe.** Com `provenanceChain` multi-elo para fontes derivadas (EarthByte, OWID) e para fatos extraídos de fontes NC (ICS). A Etapa 2 precisa do campo de cadeia desde o início.

5. **`ingestionDecision`, `licenseRiskLevel` e `reviewStatus` são campos de estado que governam publicação.** Um item com `reviewStatus=pending` ou `ingestionDecision=blocked` **não pode ser exibido** — a Etapa 2 modela esse gating como invariante, não como verificação ad hoc.

6. **`claimType` + `confidenceLevel` são exigidos pela checklist (Q13/Q14)** → a Etapa 2 modela tipagem de claim e nível de confiança **desde o primeiro dia** (já era a decisão D7; agora é pré-requisito operacional).

7. **A camada de mídia (imagens/mapas) é modelada separada do grafo factual**, com seu próprio regime de licença por asset (Risco 2/3) e seus próprios rótulos de natureza (fotografia / mapa / reconstrução / representação artística).

8. **O protótipo de ingestão da Etapa 2 só toca fontes "verdes" desta checklist** — Risco 0/1 e, no máximo, 2 com confirmação: NASA, Macrostrat, Natural Earth, geoBoundaries, PBDB, IBGE, Pleiades, Our World in Data, World Bank, BNCC. **Nada de Risco 4/5** (Seshat, GADM, ACLED, David Rumsey, Deep Time Maps) entra no protótipo.

---

*Documento operacional da Etapa 1.1, sob a baseline v1.0 e a auditoria da Etapa 1. Não modela o Knowledge Core, não contém código de aplicação, não propõe MVP, não define arquitetura técnica. Próxima etapa, quando solicitada: Etapa 2 — modelagem do Knowledge Core, já obrigada a acoplar `ProvenanceMetadata`, separar índices de autoridades, isolar camadas ShareAlike e exigir tipagem de claim + nível de confiança.*
