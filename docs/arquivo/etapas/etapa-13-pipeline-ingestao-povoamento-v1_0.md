# Etapa 13 — Pipeline Real de Ingestão, Curadoria e Povoamento do Knowledge Core

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 13** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8, v1.0), a `PedagogicalOutputLayer` (Etapa 9, v1.0), a `DesignUX3DLayer` (Etapa 10, v1.0), a `TechnicalArchitectureLayer` (Etapa 11, v1.0) e o `MVPRelease` (Etapa 12, v1.0) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura operacional de ingestão e povoamento**. Define **como fontes, fatos, claims, citações, licenças, assets, geometrias, snapshots, cenas e relações entram no Knowledge Core** — os papéis humanos de curadoria, os portões, os estados, os metadados obrigatórios, o fluxo de revisão, o tratamento de licenças, a migração do seed do MVP, a priorização de lotes e os critérios de aceite — **sem quebrar proveniência, licença, revisão humana, publicabilidade, versionamento, privacidade, acessibilidade e soberania do núcleo**. Conforme solicitado, esta etapa **não** escreve código; **não** implementa API real; **não** executa scraping real; **não** baixa fontes reais; **não** popula banco real; **não** cria milhares de eventos; **não** altera as cenas-gabarito; **não** cria claims factuais sem fonte A/B; **não** usa IA como fonte factual; **não** usa Wikipedia/Wikidata como autoridade; **não** copia texto protegido; **não** reproduz expressão NC; **não** mistura SA/ODbL no núcleo; **não** coleta dados pessoais reais de alunos; **não** cria *analytics* ou LMS; **não** mapeia BNCC em massa; **não** trata BNCC como fonte factual; **não** trata o seed do MVP como ingestão real; **não** promete homologação MEC/PNLD; e **não** relaxa nenhum invariante das Etapas 11 e 12. Ela **pode**, porém: definir o pipeline completo, propor a primeira ordem de povoamento, definir o lote inicial pós-MVP, definir templates de ingestão, definir filas/estados/validações/critérios de aceite, definir como a IA pode auxiliar a curadoria sem ser fonte, definir como humanos aprovam ou rejeitam, definir como snapshots e licenças são registrados, definir como o seed do MVP se transforma em conteúdo canônico auditável e definir como a Etapa 14 deve operar QA, governança e escala.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Papéis humanos em `camelCase` (ex.: `ingestionCurator`). Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "O KC" = o Knowledge Core (Etapa 2). "O portão" = o checklist/portão de licenças da Etapa 1.1. "A arquitetura técnica" = a `TechnicalArchitectureLayer` (Etapa 11). "O MVP" = o `MVPRelease` (Etapa 12). "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O pipeline" = o `IngestionPopulationPipeline` definido na Seção 1.

> **Convenção de estatuto das decisões (herdada das Etapas 11/12).** **[NORMATIVO]** = vinculante, não pode ser violado sem reabrir a etapa; **[RECOMENDADO]** = opção preferida, substituível por equivalente que preserve os invariantes; **[ALTERNATIVA]** = opção aceitável citada para comparação; **[PENDÊNCIA]** = decisão deliberadamente adiada (para a Etapa 14 ou para a execução), registrada para ser carregada. Nomes de tecnologias concretas, quando aparecem, são sempre **[RECOMENDADO]**/**[ALTERNATIVA]**, nunca **[NORMATIVO]**.

> **Regra central desta etapa.** A ingestão é **o único caminho legítimo de escrita factual no Knowledge Core**. Tudo que vira `Claim`, `Source`, `Citation`, `Relationship`, `Scene`, `MediaAsset`, `MapAsset`, `GeometryVersion`, `DatasetSnapshot` ou `LicenseProfile` passa, sem atalho, por: (1) fonte identificada; (2) classificação A/B/C; (3) decisão de licença; (4) separação fato × expressão × objeto digitalizado; (5) snapshot/versionamento; (6) extração de claims; (7) tipagem epistêmica; (8) validação temporal; (9) validação geoespacial; (10) revisão humana adequada; (11) publicabilidade; (12) auditabilidade; (13) isolamento físico quando houver licença restritiva. A pergunta que esta etapa responde: *"Como o Atlas do Tempo 3D deixa de depender de três cenas seedadas e passa a povoar o Knowledge Core com dados reais, auditáveis, versionados e licenciados, sem permitir que fonte fraca, licença incompatível, IA, cache, busca ou automação virem verdade factual?"* Permanecem canônicas e invioláveis: **forma muda; fato não**; **score não é verdade**; **cache não é verdade**; **busca/embedding não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**.

---

## Sumário

1. Definição do `IngestionPopulationPipeline`
2. Princípios de ingestão
3. Papéis humanos e responsabilidades
4. Estados do pipeline e ciclo de vida
5. Fluxo ponta a ponta da ingestão
6. Templates de ingestão
7. Política de fontes por camada
8. Licenças e isolamento físico no pipeline
9. Proveniência, snapshots e versionamento
10. Extração, normalização e tipagem de claims
11. Normalização temporal e geoespacial
12. Migração do seed do MVP para conteúdo canônico
13. Lotes de povoamento pós-MVP
14. QA, testes e riscos da ingestão
15. Encerramento e handoff para a Etapa 14

---

## 1. Definição do `IngestionPopulationPipeline`

### 1.1 O que o pipeline é

O **`IngestionPopulationPipeline`** é a **camada operacional de escrita factual** do produto: o conjunto disciplinado de papéis humanos, estados, portões, filas, validações, templates e critérios de aceite por meio do qual conteúdo do mundo externo (fontes, datasets, documentos, acervos, geometrias) **entra no Knowledge Core** já tipado, fonteado, licenciado, datado, localizado, revisado e versionado. Ele é o **processo** que transforma o corpus seedado e o modelo conceitual/técnico acumulado (Etapas 0–12) em um **núcleo povoado com dados reais e auditáveis** — sem que o ato de povoar afrouxe qualquer garantia epistêmica, jurídica, de privacidade ou de acessibilidade.

O pipeline é a contraparte operacional de três peças já fixadas: o **portão da Etapa 1.1** (checklist de 15 perguntas, decisão de licença, classificação de risco), a **modelagem da Etapa 2** (claim-first, proveniência obrigatória, incerteza tipada) e a **arquitetura da Etapa 11** (lojas físicas separadas, fronteiras de escrita, isolamento de licença, versionamento, auditoria). Onde a Etapa 1.1 define **o que pode entrar**, a Etapa 2 define **com que forma**, e a Etapa 11 define **onde e sob quais invariantes técnicos**, a Etapa 13 define **por qual processo, por quais mãos, em qual ordem e com quais provas de aceite**.

### 1.2 O que o pipeline **não** é

O pipeline **não é** uma fonte de verdade: ele não "produz" fatos, apenas os faz atravessar do mundo para o núcleo sob curadoria. Ele **não é** um robô de coleta em massa, **não é** um agregador automático de Wikipedia/Wikidata, **não é** um gerador de conteúdo por IA e **não é** um cache/índice que possa substituir o grafo de claims. Ele **não** cria currículo (BNCC/Planning são camadas externas que apenas anotam o núcleo — Etapas 6/7), **não** cria saídas pedagógicas (Etapa 9), **não** cria experiência/UX (Etapa 10), **não** coleta dados pessoais de aluno (Etapa 8 da Etapa 11; LGPD/ECA) e **não** produz *analytics* operacional, LMS ou validação escolar/jurídica/comercial (Etapa 14). E ele **não** é o seed do MVP: o *dataset* das três cenas-gabarito é insumo de demonstração marcado como tal (Etapa 12, §9.7), **não** o resultado do pipeline (ver Seção 12).

### 1.3 Por que é o único caminho de escrita factual no KC

Três mecanismos herdados o tornam **estruturalmente** o único caminho de escrita, não por recomendação, mas por construção: **(1) modelo claim-first** (Etapa 2, §3) — verdade só existe como `Claim` tipado, com `provenanceRef` rastreável a uma `Source` A/B; nada que não tenha passado pela extração/tipagem do pipeline tem esses campos; **(2) invariante de exibição** (Etapas 1.1/3.1/11, invariante 9) — item com `reviewStatus ∈ {pending, legal-review, rejected}` não é exibível como fato em nenhuma vista, cache, índice, exportação ou pacote offline; **(3) fronteiras de escrita** (Etapa 11, §2.3/§3.1, invariante 20) — nenhuma API permite que UX, Output, Matching, Planning ou Compliance gravem `Claim`/`Source`/`Citation`/`Relationship`/`reviewStatus`; toda escrita autoritativa passa pelo pipeline. O `KnowledgeCoreService` (Etapa 11, §3.2) tem **um único caminho de escrita fechado** — preparado pelo MVP (Etapa 12, §1.6) — e a Etapa 13 é o que o liga ao mundo **através** do portão da Etapa 1.1, sem reabrir fronteiras.

### 1.4 Por que não pode ser substituído por IA, busca, cache ou scraping bruto

Cada substituto tentador viola um invariante já fixado: **IA** não tem `provenanceRef` nem `sourceTier` A/B e por contrato nunca é gravada como `Claim`/evidência (invariante 13; A3/Q5) — pode auxiliar a **forma** e a **triagem**, nunca afirmar o fato (Seção 2 e §10.6); **busca textual/vetorial** devolve **ponteiros** para itens, tem `carriesProvenance = false` e nunca "responde um fato" sem reidratar o claim e seus rótulos (invariante 3; `busca/embedding não é verdade`); **cache** é derivado com `originClass = derivado`, carrega o conjunto de versões que o originou e é descartável (invariante 2; `cache não é verdade`); **scraping bruto** copia expressão (potencialmente NC/SA/proprietária) sem separar fato × expressão × objeto digitalizado, sem snapshot, sem decisão de licença e sem revisão humana — exatamente o que o portão (Etapa 1.1) e o isolamento físico (Etapa 11, §9) existem para impedir. O pipeline é o único processo que aplica simultaneamente proveniência, licença, tipagem e revisão; remover qualquer uma dessas etapas reabre a Etapa 1.1, a Etapa 2 ou a Etapa 11.

### 1.5 Relação com as etapas anteriores (síntese)

| Etapa | O que o pipeline herda e respeita |
|---|---|
| **1 / 1.1** | níveis de autoridade A/B/C (C nunca sustenta claim); risco de licença 0–5; códigos de decisão `AUTO`/`ATRIB`/`ISOLA`/`FATO`/`REVH`/`CONF`/`COMER`/`NAO`/`INDX`; `ProvenanceMetadata` obrigatório; separação fato × expressão × objeto digitalizado; hard stops; casos de borda |
| **2** | entidades do KC (claim-first); `claimType`/`confidenceLevel`/`evidenceLevel`/`UncertaintyProfile`; `ClaimSet`/`consensusStatus`; os dez `State`; `DatasetSnapshot`/`LicenseProfile`/`ReviewStatus`; direção única de dependência (KC soberano) |
| **3Z** | `canonicalTimeScalar` (T0 = 2000.0 CE); preservação obrigatória de `sourceTimeBasis`; sete regimes temporais; calibração de radiocarbono; `conversionMethod`/`conversionNotes` |
| **3.1** | controvérsia legítima → `ClaimSet`; negacionismo nunca é claim concorrente; consenso tipado como consenso; temas sensíveis com revisão humana obrigatória; Leis 10.639/2003 e 11.645/2008 como cobertura estrutural |
| **4A–4H / 4Z** | 25 camadas e prioridade P0–P3; matriz fonte→camada; unidade mínima de povoamento; `Scene` v1.1 (34 campos); `cascadeStructure`/`weightedClaimSets`/`paleoPositionPolicy`; `sceneCompletenessLevel`; as três cenas-gabarito (inalteráveis) |
| **5 / 5Z** | `WhatWasHappeningAtMoment`/`MomentQuery`/`MomentResult`; `hiddenItems` nunca como fato; anti-falsa-equivalência; `gatingReason` |
| **6 / 7 / 8 / 9 / 10** | direção única de dependência; o pipeline **não** escreve nessas camadas nem nelas se baseia para afirmar fato; BNCC nunca é fonte factual |
| **11** | lojas físicas `core-store`/`media-store`/`isolated-license-store`/`blocked`; `LicenseStorageBinding`; fronteiras de escrita; 30 invariantes técnicos; cadeia de rastreabilidade; versionamento/snapshots; minimização de PII |
| **12** | marcação `seed-MVP` × ingestão; caminho de escrita único e fechado; lista de placeholders a substituir; `isolated-license-store` já separado; índices derivados reconstruíveis a reindexar sobre o conteúdo real |

### 1.6 A entidade conceitual do pipeline

```txt
IngestionPopulationPipeline = {
  pipelineId,
  scope,                  # cobertura: camadas (4A), regimes temporais (3Z), recorte espacial; nunca currículo/PII
  sourceIntakePolicy,     # como fontes são descobertas, registradas e classificadas A/B/C (Seções 2, 5, 7)
  licenseGatePolicy,      # como o portão da Etapa 1.1 e a matriz de risco 0–5 são aplicados (Seções 5, 8)
  provenancePolicy,       # ProvenanceMetadata + provenanceChain obrigatórios em todo item (Seções 2, 9)
  claimExtractionPolicy,  # como fato bruto vira Claim tipado, sem copiar expressão (Seção 10)
  reviewWorkflowPolicy,   # papéis, transições que exigem revisão humana, escalonamento (Seções 3, 4, 5)
  publicationGatePolicy,  # invariante de exibição; gatingReason; o que pode virar publicável (Seções 4, 5)
  assetIsolationPolicy,   # core-store/media-store/isolated-license-store/blocked; NC/SA/ODbL (Seção 8)
  snapshotPolicy,         # quando DatasetSnapshot é obrigatório; checksum; fonte viva; fonte que sai do ar (Seção 9)
  versioningPolicy,       # versionar Source/Claim/KnowledgeItem/Scene; deprecar sem apagar (Seção 9)
  auditPolicy,            # cadeia artefato→bloco→cena/momento→claim→fonte→licença; gatingReason registrado (Seções 9, 14)
  outputToKnowledgeCore,  # a escrita autoritativa: KnowledgeItem/Claim/Citation/Relationship/Scene/asset versionados
  handoffToOperation      # o que a Etapa 14 recebe para QA, governança, escala (Seção 15)
}
```

**[NORMATIVO]:** `outputToKnowledgeCore` é a **única** porta de escrita factual; `handoffToOperation` entrega processo, não autoriza relaxar invariante. O `scope` jamais inclui currículo (BNCC), planejamento (Planning) ou PII de aluno — esses são externos ao núcleo e ao pipeline.

---

## 2. Princípios de ingestão

Os princípios abaixo são **[NORMATIVO]** e vinculantes. Eles consolidam, no plano operacional, as garantias das Etapas 1.1, 2, 3.1, 11 e 12. Nenhum lote, papel, automação ou pressão comercial pode violá-los; um item que colida com qualquer um deles é barrado **antes** de qualquer escrita no núcleo.

1. **Fonte A/B sustenta claim; fonte C só indexa.** Toda afirmação factual rastreia a uma fonte primária (A) ou agregador confiável (B). Índices (C — Wikidata/Wikipedia/VIAF) servem para **localizar, desambiguar e capturar identificadores**, nunca para afirmar (Etapa 1.1, Q11/Q12; Etapa 2, §3.2).
2. **Wikipedia/Wikidata nunca são autoridade factual.** Mesmo com cobertura abrangente, entram como `INDX` (reconciliação de identidade nos bastidores). O claim só entra com a fonte A/B real registrada — nunca o Wikidata como autoridade (Etapa 1.1, caso de borda 6).
3. **IA nunca é fonte factual.** Modelos podem auxiliar triagem, sugestão de candidatos, extração de rascunho de texto e adaptação de **forma**; nenhuma saída de IA é gravada como `Claim`/evidência, e qualquer texto de IA entra como narrativa rotulada com `reviewStatus = pending` até curadoria humana (invariante 13; A3/Q5; Etapa 1.1, casos 7/8).
4. **Fato ≠ expressão ≠ objeto digitalizado.** O fato é re-codificável com atribuição de origem; a expressão (texto, imagem, gráfico, geometria) é governada pela licença; a obra em domínio público digitalizada por terceiro depende de **qual provedor** entregou o *scan* (Etapa 1.1, regra de ouro; casos 1/5).
5. **Licença governa expressão/asset, não o fato recodificado.** Um limite cronoestratigráfico do ICS (fato) entra livre; o **gráfico** do ICS (expressão NC) não entra. O núcleo guarda o fato; a expressão restritiva fica isolada ou bloqueada (Etapa 11, §9.1/§9.3, invariante 18).
6. **NC não entra como expressão.** Conteúdo *non-commercial* (`licenseRiskLevel = 4`) nunca é reproduzido como expressão no produto; quando muito, o **fato re-derivado de fonte livre** entra com fonte própria, sem o asset (Etapa 11, invariante 19; Etapa 1.1, Q7).
7. **SA/ODbL fica fisicamente isolado.** ShareAlike/ODbL (`licenseRiskLevel = 3`) reside no `isolated-license-store`, nunca misturado ao `core-store`; o isolamento não remove a obrigação SA, que é honrada também em cache, índice, exportação e offline (Etapa 11, §9.2/§9.7, invariantes 18/27).
8. **Todo claim tem `provenanceRef`.** Não existe claim órfão de proveniência. `ProvenanceMetadata` (Etapa 1.1, Tarefa 5) viaja acoplado a todo item factual (Etapa 2, §263–266; invariante de proveniência por aresta da Etapa 11, §4.2).
9. **Todo claim tem `claimType`, `confidenceLevel`, `evidenceLevel` e `UncertaintyProfile`.** A tipagem epistêmica é pré-requisito de entrada, não enfeite: distingue fato, medição, inferência, estimativa, hipótese, controvérsia, interpretação historiográfica, reconstrução modelada, representação artística e aproximação didática (Etapa 2, §3.4/P8; Etapa 1.1, Q13/Q14).
10. **Todo item nasce com `reviewStatus`.** O estado de revisão é atribuído na entrada (em geral `pending`), governa publicação e nunca é presumido como `approved` (Etapa 2, §274–278).
11. **`pending`/`legal-review`/`rejected` não é exibível como fato.** O invariante de exibição vale em toda vista, cache, índice, exportação e pacote offline; ao público, o item simplesmente não existe como fato (Etapa 11, §7.5, invariante 9).
12. **Toda fonte tem `DatasetSnapshot`.** A versão ingerida é congelada (checksum + data de acesso) para antifragilidade — fontes vivas mudam, fontes adormecem (Etapa 2, §255–261; Etapa 11, §5).
13. **Todo asset tem `LicenseProfile`.** Nenhum `MediaAsset`/`MapAsset`/`GeometryVersion`/dado tabular entra órfão de licença; cada um carrega `LicenseProfile` + `ProvenanceMetadata` + `LicenseStorageBinding` (Etapa 11, §9.4, invariante 17).
14. **Toda geometria tem status e licença.** `GeometryVersion`/`PaleoPosition` carregam `geometryStatus` (real/histórico/inferido/moderno/paleogeográfico/pendente) e licença; geometrias SA/ODbL isoladas; paleoposições sempre rotuladas como reconstrução modelada (Etapa 4H, §5; Etapa 11, §4.4).
15. **Todo tempo tem `sourceTimeBasis` preservado.** A base temporal nativa de cada fonte nunca é apagada; `canonicalTimeScalar` é derivado com datum fixo (T0 = 2000.0 CE) e auditável (Etapa 3Z, §3/§9; Etapa 11, invariante 29).
16. **Todo item localizável tem tratamento espacial explícito.** `Place`/`Region`/`GeometryVersion`/`ModernCorrespondence`/`PaleoPosition` distinguem localidade atual de posição histórica e de paleoposição; anacronismo espacial é barrado (Etapa 4H, §5; Etapa 2, §5).
17. **Toda controvérsia legítima vira `ClaimSet`.** Divergência real entre especialistas qualificados, sustentada por evidência, entra como conjunto de claims concorrentes com peso (`weightedClaimSets`), nunca como claim único nem como escolha editorial (Etapa 3.1, §2/§3; Etapa 4H, §4).
18. **Negacionismo não vira claim concorrente.** Rejeição de fato/consenso bem estabelecido sem evidência válida fica **fora** do `ClaimSet`, no máximo como objeto rotulado (`consensusStatus = desinformação/negacionismo rejeitado`; `displayWeight = rotulado-rejeitado`) — nunca equivalido ao consenso (Etapa 3.1, §1.2/§5; Etapa 4H, §4).
19. **Conteúdo sensível exige revisão humana compatível.** Colonização, escravidão, povos indígenas, raça, religião, violência/genocídio, pessoas vivas e mídia gráfica herdam `reviewStatus = pending` na entrada e não são exibíveis até aprovação do revisor adequado (Etapa 3.1, §2/§4/§6/§7).
20. **Ingestão não cria currículo.** O pipeline não escreve BNCC, série, disciplina, competência ou habilidade; a indexação curricular é anotação externa (Etapa 6) que aponta para o núcleo por ID estável (Etapa 2, P1/P2/§10).
21. **Ingestão não cria saída pedagógica nem UX.** Plano de aula, quiz, rubrica, trilha, tela, modo professor/estudante são camadas posteriores (Etapas 9/10); o pipeline para na escrita factual do núcleo (direção única de dependência da Etapa 11).
22. **BNCC nunca é fonte factual.** O texto da BNCC/LDB é conformidade e indexação (entra como texto legal/normativo, `AUTO`), nunca origem de claim sobre o mundo (Etapa 1.1, Tarefa 3, categoria 11; Etapa 6).
23. **O seed do MVP não é pipeline.** O *dataset* das três cenas-gabarito é insumo de demonstração marcado com `DatasetSnapshot` de origem `seed-MVP-cenas-gabarito`; ele só vira conteúdo canônico após reconfirmação de fonte/licença/revisão via pipeline (Etapa 12, §9.7; Seção 12).
24. **Não se copia texto protegido; reescreve-se em linguagem própria mantendo a citação.** O fato é re-codificado; a expressão original não é reproduzida; a citação aponta ao ponto exato da fonte sem republicar o material (Etapa 1.1, casos 2/9; Etapa 12, §12.4).
25. **Toda decisão que impacte publicabilidade registra `gatingReason`.** Por que um item está `pending`/`legal-review`/`rejected`/parcial é sempre registrado e auditável à curadoria — nunca silencioso (Etapa 4H, §8; Etapa 5; Etapa 11, §7.5).
26. **Score não é verdade; cache não é verdade; busca/embedding não é verdade.** Nenhum derivado (relevância de Matching, cache, índice textual/vetorial) é gravado como fato nem promove item `pending` a fato (invariantes 2/3/6 da Etapa 11).
27. **Correção futura não apaga o passado auditável.** Uma correção cria **nova versão**; a versão anterior é deprecada, nunca apagada, para que se possa auditar o que foi mostrado antes da correção (Etapa 11, §5; Seção 9.10).
28. **Offline não relaxa garantias; degradação nunca remove o piso epistêmico.** O conteúdo povoado leva licença, publicabilidade, papel e rótulos epistêmicos embutidos a qualquer modo (3D→2D→estático→offline→projetor) — a ausência de rede não abre o que a política fecharia online (invariantes 11/22 da Etapa 11).

> **Regra-síntese dos princípios.** O pipeline admite **apenas** verdade que rastreia a uma fonte A/B, carrega tipo e incerteza, nasce sob revisão, tem proveniência e snapshot, respeita licença por asset, preserva o datum nativo e o tratamento espacial, estrutura controvérsia sem achatar e sem dar palco a negacionismo, e nunca confunde derivado (IA, cache, busca, score) com fato. Quando houver dúvida de fonte, licença, data, geometria ou `claimType`, o item é marcado `PENDENTE_*` (Seção 14, §22) — **nunca** se inventa precisão.

---

## 3. Papéis humanos e responsabilidades

Os papéis abaixo operam o pipeline. Eles **estendem** e se acoplam aos papéis técnicos/curatoriais da Etapa 11, §7.2 (`systemAdmin`, `curator`, `scientificReviewer`, `editorialReviewer`, `legalReviewer`), refinando-os para o trabalho de ingestão. **[NORMATIVO]:** os papéis de curadoria/ingestão vivem em plano separado dos papéis escolares (teacher/coordinator/student/guardian — Etapa 11, §7.7); nenhum papel de ingestão opera com PII de aluno, e nenhum papel escolar recebe credencial de escrita no KC. **Negar vence em conflito.** Ninguém aprova fora de sua competência (risco R-13.22).

### 3.1 Catálogo de papéis

```txt
ingestionRole = [
  sourceScout, ingestionCurator, licenseReviewer, scientificReviewer,
  historicalReviewer, editorialReviewer, legalReviewer, geoTemporalReviewer,
  accessibilityReviewer, pipelineAdmin
]
```

#### `sourceScout`
- **Responsabilidade.** Descobrir e propor fontes candidatas; registrar `sourceName`/`originalUrl`/natureza preliminar; iniciar o `SourceIntakeRecord`.
- **Pode aprovar.** Nada autoritativo. Move um item de `proposed` para `source-identified` (proposta de fonte), sem decidir licença, tipo de claim ou publicabilidade.
- **Não pode aprovar.** Classificação final A/B/C; decisão de licença; criação de claim; aprovação para o KC; publicação.
- **Quando escala.** Sempre: toda fonte proposta segue para `ingestionCurator` (registro) e `licenseReviewer` (licença). Fonte de risco editorial/sensível é sinalizada desde a proposta.
- **Relação com a Etapa 11.** Antecede o `curator`; alimenta o `SourceProvenanceService` (Etapa 11, §3.3) com candidatos, sem poder de escrita autoritativa.

#### `ingestionCurator`
- **Responsabilidade.** Conduzir o item ao longo do pipeline: registrar a fonte, propor classificação A/B/C, rascunhar claims (`ClaimDraft`), preencher metadados, montar `KnowledgeItemDraft`/`CitationRecord`/`RelationshipDraft`, encaminhar para os revisores e consolidar decisões. É o **dono operacional** do item até a publicação.
- **Pode aprovar.** Completude de metadados e transições internas até `review-pending`; rascunhos de claim/relação/cena (não a verdade final, que depende de revisão). Pode mover para `approved-for-kc` **somente** quando todas as revisões obrigatórias do item retornaram aprovação (Seção 4).
- **Não pode aprovar.** Mérito científico (é do `scientificReviewer`); mérito histórico/editorial (é do `historicalReviewer`/`editorialReviewer`); licença/risco jurídico (é do `licenseReviewer`/`legalReviewer`); tempo/espaço duvidoso (é do `geoTemporalReviewer`); equivalente textual/acessibilidade (é do `accessibilityReviewer`). Não aprova item de tema sensível sem o revisor competente.
- **Quando escala.** A qualquer dúvida de fonte, licença, data, geometria, `claimType` ou sensibilidade. Marca `PENDENTE_*` e roteia ao revisor correspondente.
- **Relação com a Etapa 11.** Corresponde ao `curator` (Etapa 11, §7.2), com escrita no KC **apenas via pipeline** e somente após as aprovações.

#### `licenseReviewer`
- **Responsabilidade.** Aplicar o portão da Etapa 1.1 no plano de licença: classificar `licenseRiskLevel` (0–5), decidir `ingestionDecision`/`allowedUse`, exigir e validar `attributionText`, determinar `storagePartition` (`core-store`/`media-store`/`isolated-license-store`/`blocked`), confirmar licença por asset (`perAssetConfirmed`) e barrar o que não pode entrar.
- **Pode aprovar.** A decisão de licença (`license-screened`); a confirmação por asset; o `LicenseStorageBinding`; o `exportPolicy`.
- **Não pode aprovar.** Mérito factual, científico, histórico ou editorial; publicabilidade de conteúdo cuja pendência seja epistêmica e não de licença.
- **Quando escala.** Risco 5 (proprietário/comercial) e qualquer "sem licença declarada" → `legalReviewer` (jurídica obrigatória). Caso de borda ambíguo (obra PD com *scan* NC; figura protegida) → `legalReviewer`.
- **Relação com a Etapa 11.** Opera o `LicenseComplianceService` (Etapa 11, §3.4/§9); é guardião jurídico-técnico da ingestão e revalida na exportação.

#### `scientificReviewer`
- **Responsabilidade.** Revisar o mérito **científico** dos claims de camadas científicas (cosmologia, geologia, atmosfera, clima, paleogeografia, oceanos, vida/evolução, paleobiologia/extinções, evolução humana): correção de `claimType`/`confidenceLevel`/`evidenceLevel`/`UncertaintyProfile`, rótulo de reconstrução/inferência, estrutura de `ClaimSet`/`weightedClaimSets` em debates científicos e recusa de negacionismo como lado.
- **Pode aprovar.** A aprovação científica (transição de `reviewStatus` para `approved` em itens científicos).
- **Não pode aprovar.** Licença; mérito histórico-editorial de temas humanos sensíveis; tempo/espaço (coordena com `geoTemporalReviewer`); acessibilidade.
- **Quando escala.** Controvérsia científica com componente social sensível (ex.: raça e ciência) → também `editorialReviewer`. Incerteza não resolvível → mantém `PENDENTE_*` e registra `gatingReason`.
- **Relação com a Etapa 11.** Corresponde ao `scientificReviewer` (Etapa 11, §7.2).

#### `historicalReviewer`
- **Responsabilidade.** Revisar o mérito **histórico/historiográfico** dos claims de camadas humanas (civilizações, política/Estados, ciência como história, cultura, religiões, guerras, Brasil, África/diáspora, povos indígenas, contemporâneo): distinção fato documentado × interpretação historiográfica, estrutura de `ClaimSet` para disputas legítimas, terminologia sensível, cobertura estrutural das Leis 10.639/2003 e 11.645/2008, e ausência de eurocentrismo/anacronismo.
- **Pode aprovar.** A aprovação historiográfica de itens históricos.
- **Não pode aprovar.** Licença; mérito científico de camadas científicas; tempo/espaço técnico; acessibilidade. Não decide sozinho temas de máxima sensibilidade — coordena com `editorialReviewer`.
- **Quando escala.** Colonização, escravidão, povos indígenas, racismo, genocídio, conflito contemporâneo, pessoas vivas → revisão conjunta com `editorialReviewer` e, se houver risco jurídico/LGPD, `legalReviewer`.
- **Relação com a Etapa 11.** É uma especialização editorial-historiográfica que opera ao lado do `editorialReviewer` (Etapa 11, §7.2), com o mesmo plano de aprovação de `reviewStatus`.

#### `editorialReviewer`
- **Responsabilidade.** Aplicar a política editorial da Etapa 3.1: tratamento de controvérsias e temas sensíveis, `consensusStatus`, `editorialNote`, mediação por faixa etária, linguagem não sensacionalista, anti-falsa-equivalência (`displayWeight`/`weightedClaimSets`), recusa de negacionismo como lado e proteção de menores.
- **Pode aprovar.** A aprovação editorial (`reviewStatus`, `editorialNote`) de itens sensíveis/controversos; a marcação de `sensitiveItems`/mediação na `Scene`.
- **Não pode aprovar.** Verdade factual sem o revisor científico/histórico competente; licença; tempo/espaço; acessibilidade.
- **Quando escala.** Risco jurídico/LGPD (pessoas vivas, dados sensíveis) → `legalReviewer`; mérito científico → `scientificReviewer`; mérito historiográfico → `historicalReviewer`.
- **Relação com a Etapa 11.** Corresponde ao `editorialReviewer` (Etapa 11, §7.2).

#### `legalReviewer`
- **Responsabilidade.** Resolver casos de risco jurídico: licença ausente/ambígua (`sem-licenca`), risco 5 (proprietário/comercial, contrato), figuras/obras protegidas, LGPD (pessoas vivas/identificáveis, dados sensíveis), ECA/proteção de menores no conteúdo e termos de uso de fontes.
- **Pode aprovar.** A decisão de `legal-review` (liberar, bloquear ou condicionar a contrato); a entrada de conteúdo proprietário **somente** com contrato e sob `isolated-license-store`.
- **Não pode aprovar.** Mérito pedagógico/factual como editor; publicação de item cuja pendência seja científica/historiográfica e não jurídica.
- **Quando escala.** Decisões de política institucional (compra pública, contratos comerciais) → `pipelineAdmin` e operação (Etapa 14).
- **Relação com a Etapa 11.** Corresponde ao `legalReviewer` (Etapa 11, §7.2); decide `legal-review`/licença.

#### `geoTemporalReviewer`
- **Responsabilidade.** Revisar tempo e espaço: correção de `sourceTimeBasis`/`conversionMethod`/`conversionNotes`, regime temporal (3Z), calibração de radiocarbono, `timePrecision`/`timeUncertainty`, e o tratamento espacial (`geometryStatus`, `modernGeometry`/`historicalGeometryVersions`/`paleoPositions`/`modernCorrespondence`, `SpatialUncertainty`), garantindo que paleoposição não seja tratada como localização atual e que não haja anacronismo espacial.
- **Pode aprovar.** A validação temporal e geoespacial do item (pré-condição para `metadata-complete`).
- **Não pode aprovar.** Mérito científico do fenômeno; licença; mérito editorial; acessibilidade.
- **Quando escala.** Geometria sem licença/status, paleoposição sem modelo, datum ambíguo → `PENDENTE_GEOMETRIA`/`PENDENTE_DATA`; se a geometria for proprietária, coordena com `licenseReviewer`/`legalReviewer`.
- **Relação com a Etapa 11.** Sustenta os índices temporal e geoespacial (Etapa 11, §4.4/§4.5) com dados validados; opera dentro do círculo de curadoria.

#### `accessibilityReviewer`
- **Responsabilidade.** Garantir, na ingestão, que todo item com componente visual tenha **equivalente textual** com a mesma informação factual e os mesmos rótulos epistêmicos; que `natureLabel` esteja correto; que a redundância não-cromática e a legibilidade sejam respeitadas no material que será exibido (e-MAG/WCAG/LBI — Etapa 11, §11.8/§11.9, invariante 23).
- **Pode aprovar.** A conformidade de acessibilidade do item/asset (equivalente textual presente e adequado).
- **Não pode aprovar.** Mérito factual; licença; tempo/espaço; mérito editorial.
- **Quando escala.** Asset sem equivalente textual viável → devolve para `needs-rework`; mídia sensível → coordena com `editorialReviewer`.
- **Relação com a Etapa 11.** Operacionaliza a fundação de acessibilidade (Etapa 11, §11.8–11.10), agora na entrada do conteúdo.

#### `pipelineAdmin`
- **Responsabilidade.** Administrar o pipeline (não o conteúdo): configurar filas, papéis e políticas declarativas; manter a auditoria (`IngestionAuditTrail`) e a integridade dos estados; garantir que nenhuma transição contorne as revisões obrigatórias; e zelar pela separação de planos (curadoria × escolar).
- **Pode aprovar.** Configuração técnica do pipeline, papéis e políticas; não conteúdo factual.
- **Não pode aprovar.** Qualquer `Claim`/`Source`/`reviewStatus` como editor; PII de aluno como conteúdo; relaxamento de invariante.
- **Quando escala.** Decisões de governança/escala/retenção → Etapa 14.
- **Relação com a Etapa 11.** Corresponde ao `systemAdmin` (Etapa 11, §7.2), restrito ao domínio de ingestão.

### 3.2 Matriz de competência (quem aprova o quê)

| Decisão | Aprova | Nunca aprova sozinho | Escalonamento típico |
|---|---|---|---|
| Proposta de fonte | `sourceScout` | classificação final; licença; claim | `ingestionCurator` |
| Registro/classificação A/B/C | `ingestionCurator` | mérito factual final | revisores de mérito |
| Licença/risco/isolamento/atribuição | `licenseReviewer` | mérito factual | `legalReviewer` (risco 5, sem-licença) |
| Mérito científico | `scientificReviewer` | licença; tema humano sensível | `editorialReviewer` (raça/ciência) |
| Mérito historiográfico | `historicalReviewer` | licença; tema científico | `editorialReviewer`+`legalReviewer` |
| Tema sensível/controvérsia/mediação | `editorialReviewer` | verdade factual sem revisor de mérito | `legalReviewer` (LGPD) |
| Risco jurídico/LGPD/contrato | `legalReviewer` | mérito pedagógico | `pipelineAdmin`/operação |
| Tempo/espaço/datum/geometria | `geoTemporalReviewer` | mérito do fenômeno; licença | `licenseReviewer` (geometria proprietária) |
| Equivalente textual/acessibilidade | `accessibilityReviewer` | mérito factual | `editorialReviewer` (mídia sensível) |
| Consolidação e `approved-for-kc` | `ingestionCurator` (após todas as revisões) | qualquer revisão de mérito isolada | — |
| Configuração/auditoria do pipeline | `pipelineAdmin` | conteúdo factual | operação (Etapa 14) |

**[NORMATIVO]:** um item de tema sensível (princípio 19) só atinge `approved-for-kc` com a aprovação do(s) revisor(es) competente(s) registrada; `ingestionCurator` consolida, não substitui, as revisões. Toda aprovação/rejeição grava ator, data e `gatingReason` na `IngestionAuditTrail` (Seção 9; Etapa 11, §12).

---

## 4. Estados do pipeline e ciclo de vida

O pipeline controla dois ciclos de vida ortogonais: o **estado de ingestão de um item** (`ingestionStatus`) e o **estado de povoamento de um escopo/lote** (`populationStatus`). Ambos são enums controlados; transições proibidas são barradas pela máquina de estados (operada conceitualmente pelo `pipelineAdmin`, Etapa 11, §3).

### 4.1 Enums de estado

```txt
ingestionStatus = [
  proposed,            # fonte/item proposto, sem registro completo
  source-identified,   # fonte identificada (sourceName/originalUrl), sem classificação final
  license-screened,    # licença classificada (risco 0–5) e ingestionDecision/allowedUse definidos
  snapshot-created,    # DatasetSnapshot congelado (checksum + retrievedAt)
  claim-drafted,       # claims rascunhados (ClaimDraft), ainda sem tipagem/validação completas
  metadata-complete,   # claimType/confidence/evidence/uncertainty + tempo + espaço preenchidos e válidos
  review-pending,      # encaminhado às revisões humanas obrigatórias do item
  approved-for-kc,     # todas as revisões obrigatórias aprovadas; pronto para escrita no núcleo
  rejected,            # recusado (fonte fraca, fora de escopo, mérito insuficiente) — não exibível
  blocked-license,     # barrado por licença incompatível (NC como expressão, sem-licença, etc.)
  legal-review,        # em análise jurídica (risco 5, sem-licença, figura protegida, LGPD)
  needs-rework,        # devolvido para correção (metadados, equivalente textual, tipagem)
  published,           # escrito no núcleo e publicável (reviewStatus=approved, publicabilidade satisfeita)
  deprecated           # versão substituída por correção/atualização; preservada para auditoria
]

populationStatus = [
  not-started,            # escopo/lote ainda não iniciado
  seed-only,              # apenas o seed de demonstração (Etapa 12), sem ingestão real
  pilot-populated,        # lote-piloto ingerido sob curadoria (amostra controlada)
  partially-populated,    # parte do escopo ingerida; cobertura estrutural incompleta
  production-populated,   # escopo ingerido em produção, sob critérios de aceite atendidos
  deprecated              # escopo/lote substituído por versão posterior; preservado para auditoria
]
```

### 4.2 Transições permitidas de `ingestionStatus`

```txt
proposed            → source-identified | rejected
source-identified   → license-screened | rejected
license-screened    → snapshot-created | blocked-license | legal-review | rejected
snapshot-created    → claim-drafted | legal-review | rejected
claim-drafted       → metadata-complete | needs-rework | rejected
metadata-complete   → review-pending | needs-rework
review-pending      → approved-for-kc | needs-rework | legal-review | rejected
needs-rework        → claim-drafted | metadata-complete | review-pending   (retoma de onde a pendência exige)
legal-review        → license-screened | blocked-license | review-pending | rejected
approved-for-kc     → published | needs-rework   (rework só antes da escrita, se surgir falha)
published           → deprecated   (nunca volta a estado anterior; correção cria nova versão — §9.10)
blocked-license     → license-screened   (somente se a base de licença mudar: nova fonte/asset/contrato)
rejected            → (terminal; reabertura cria NOVO item proposto, com novo id de tentativa)
deprecated          → (terminal para aquela versão)
```

**[NORMATIVO] — transições proibidas (exemplos):** `proposed → published` (pula portão, snapshot, tipagem, revisão); `source-identified → approved-for-kc` (pula licença e mérito); qualquer `→ published` sem passar por `approved-for-kc`; `rejected/blocked-license → published` sem reabrir a base que motivou o bloqueio; `published → metadata-complete` (correção é nova versão, não regressão silenciosa). A máquina de estados recusa toda transição não listada em §4.2.

### 4.3 Campos obrigatórios antes de cada transição

| Transição | Campos obrigatórios antes de avançar |
|---|---|
| → `source-identified` | `sourceName`, `originalUrl`, natureza preliminar (fato/expressão/obj-digitalizado) |
| → `license-screened` | `sourceTier` (A/B/C), `authorityType`, `license`, `licenseRiskLevel`, `ingestionDecision`, `allowedUse`, `attributionRequired`/`attributionText`, `shareAlikeRequired`, `nonCommercial`, `storagePartition` |
| → `snapshot-created` | `DatasetSnapshot` com `snapshotDate`, `sourceVersion`, `checksum`, `coverageNote`, `retrievedAt` |
| → `claim-drafted` | `statement` rascunhado, `subjectRef` (item de que trata), `citation` apontando ao locator |
| → `metadata-complete` | `claimType`, `confidenceLevel`, `evidenceLevel`, `UncertaintyProfile`; `TimeRange` com `sourceTimeBasis`/`canonical*`/`timePrecision`/`timeUncertainty`; tratamento espacial (`geometryStatus` + geometria/correspondência aplicável); `provenanceRef` |
| → `review-pending` | item completo + roteamento aos revisores obrigatórios conforme camada/sensibilidade |
| → `approved-for-kc` | todas as revisões obrigatórias do item com `outcome = aprovado` registradas; `gatingReason` resolvido ou nulo |
| → `published` | `reviewStatus = approved`; publicabilidade satisfeita (sem pendência de exibição); `LicenseStorageBinding` definido; equivalente textual presente para itens visuais |
| → `deprecated` | nova versão criada e referenciada; motivo da depreciação registrado (§9.10) |

### 4.4 Transições que exigem revisão humana

**[NORMATIVO]** exigem revisão humana antes de avançar: **(a)** `review-pending → approved-for-kc` (sempre — é o ponto onde o mérito é confirmado); **(b)** qualquer transição de item de tema sensível (princípio 19) — colonização, escravidão, povos indígenas, raça, religião, violência/genocídio, pessoas vivas, mídia gráfica — que herda `reviewStatus = pending` na entrada; **(c)** entrada de qualquer `Claim`/`Source`/`Citation`/`Relationship` afirmativa (causal/interpretativa), `MediaAsset`/`MapAsset`, `GeometryVersion` (Etapa 11, §2.4); **(d)** publicação de cena (`sceneCompletenessLevel → publicável`); **(e)** controvérsia legítima virando `ClaimSet`/`weightedClaimSets`. A automação **não** executa essas transições; ela apenas prepara o item e registra quem revisou, quando e com que nota (Etapa 11, §2.4/§2.6).

### 4.5 Transições bloqueadas por licença

**[NORMATIVO]** o `licenseReviewer`/`LicenseComplianceService` bloqueia: expressão NC (risco 4) tentando `→ published` como expressão (vai a `blocked-license`; só o fato re-derivado entra); SA/ODbL (risco 3) tentando entrar no `core-store` (forçado ao `isolated-license-store`); asset risco 2 sem `perAssetConfirmed` (fica `pending`, não é servido); fonte `sem-licenca` (`→ legal-review`, default não entra); risco 5 sem contrato (`blocked-license`/`legal-review`). Nenhuma dessas é destravada por urgência, intenção declarada ou pressão comercial (princípio 5/6/7; risco R-13.35).

### 4.6 Transições bloqueadas por fonte fraca

**[NORMATIVO]** claim que dependa de fonte C (Wikidata/Wikipedia) como autoridade, ou de IA como fonte, é barrado em `claim-drafted → metadata-complete` (sem fonte A/B real registrada → `needs-rework` ou `rejected`). Item sem `claimType`/`confidenceLevel`/`reviewStatus` não atinge `metadata-complete`. Controvérsia legítima sem `ClaimSet` não é aprovada; negacionismo proposto como claim concorrente é `rejected` como claim (no máximo objeto rotulado — princípio 18).

### 4.7 Ciclo de vida de povoamento (`populationStatus`)

O `populationStatus` mede a maturidade de um **escopo** (uma camada, um lote da Seção 13, um recorte regional/temporal). Transições típicas: `not-started → seed-only` (estado herdado do MVP); `seed-only → pilot-populated` (primeiro lote real curado); `pilot-populated → partially-populated → production-populated` (à medida que os critérios de aceite de cada lote são atendidos — Seção 13); `production-populated → deprecated` quando um escopo é substituído por uma reorganização posterior (sempre preservando versões — §9.10). **[NORMATIVO]:** um escopo só avança de `pilot-populated` em diante quando os testes de invariante (Seção 14) e os critérios de aceite do lote (Seção 13) passam; nenhum escopo é declarado `production-populated` por pressão de prazo (risco R-13.22/R-13.35).

---

## 5. Fluxo ponta a ponta da ingestão

O fluxo abaixo é a sequência canônica de um item, da descoberta da fonte à invalidação de derivados. Cada etapa indica **entrada**, **saída**, **responsável**, **bloqueios**, **artefatos gerados** e **riscos**. As etapas mapeiam diretamente os `ingestionStatus` da Seção 4. **[NORMATIVO]:** nenhuma etapa pode ser pulada; a etapa 5 (decisão de entrada) usa os códigos da Etapa 1.1.

### 5.1 As vinte etapas

**1. Descoberta de fonte.**
- Entrada: necessidade de cobertura (camada/lote/recorte). Saída: fonte candidata (`proposed`).
- Responsável: `sourceScout`. Bloqueios: nenhum (proposta). Artefatos: rascunho de `SourceIntakeRecord`.
- Riscos: descobrir por Wikipedia/IA e confundir índice com autoridade (mitigado: índice só localiza; a autoridade A/B é buscada depois).

**2. Registro da fonte.**
- Entrada: fonte candidata. Saída: `SourceIntakeRecord` com `sourceName`/`originalUrl`/natureza (`source-identified`).
- Responsável: `ingestionCurator`. Bloqueios: sem fonte identificável → barra (Etapa 1.1, Q2). Artefatos: `SourceIntakeRecord`.
- Riscos: fonte sem origem rastreável; URL volátil (mitigado: snapshot na etapa 6).

**3. Classificação A/B/C.**
- Entrada: fonte registrada. Saída: `sourceTier` + `authorityType`.
- Responsável: `ingestionCurator` (proposta) + `licenseReviewer`/revisor de mérito (confirmação). Bloqueios: fonte C destinada a sustentar claim → rebaixada a `INDX` (Etapa 1.1, Q3/Q11).
- Artefatos: classificação no `SourceIntakeRecord`. Riscos: fonte C virando autoridade (mitigado: princípios 1/2).

**4. Análise de licença.**
- Entrada: fonte classificada. Saída: `license`, `licenseRiskLevel` (0–5), `nonCommercial`, `shareAlikeRequired`, `attributionRequired`/`attributionText`, `itemLevelLicense`.
- Responsável: `licenseReviewer`. Bloqueios: `sem-licenca`/risco 5 → `legal-review`. Artefatos: `LicenseScreeningRecord`.
- Riscos: tratar ausência de licença como PD; licença por item desconhecida (mitigado: Etapa 1.1, Q8/Q10; default conservador).

**5. Decisão de entrada.**
- Entrada: licença + risco. Saída: `ingestionDecision` ∈ {`AUTO`, `ATRIB`, `ISOLA`, `FATO`, `REVH`, `CONF`, `COMER`, `NAO`, `INDX`} + `allowedUse` + `storagePartition` (`license-screened`).
- Responsável: `licenseReviewer` (com `legalReviewer` nos casos de risco). Bloqueios: `NAO`/`blocked-license`; `COMER` sem contrato; `CONF` sem confirmação por asset.
- Artefatos: decisão no `LicenseScreeningRecord` + `LicenseStorageBinding` preliminar. Riscos: NC entrando como expressão; SA contaminando o núcleo (mitigado: matriz da Etapa 11, §9.11).

**6. Snapshot.**
- Entrada: decisão de entrada favorável. Saída: `DatasetSnapshot` (`snapshot-created`).
- Responsável: `ingestionCurator` (custódia pelo `SourceProvenanceService`, Etapa 11, §3.3). Bloqueios: sem `checksum`/`retrievedAt` → não avança.
- Artefatos: `DatasetSnapshotRecord`. Riscos: fonte viva muda; fonte sai do ar (mitigado: §9.5/§9.6).

**7. Extração de fatos/claims.**
- Entrada: snapshot. Saída: `ClaimDraft` (afirmações atômicas re-codificadas, sem copiar expressão) (`claim-drafted`).
- Responsável: `ingestionCurator` (IA pode auxiliar rascunho, rotulado, sem virar claim — §10.6). Bloqueios: cópia de texto protegido → barra (princípio 24).
- Artefatos: `ClaimDraft`. Riscos: copiar expressão; granularidade ruim; tradução alterar o fato (mitigado: §10).

**8. Tipagem de claims.**
- Entrada: rascunho de claim. Saída: `claimType`, `confidenceLevel`, `evidenceLevel`, `UncertaintyProfile`, `consensusStatus`.
- Responsável: `ingestionCurator` (proposta) + `scientificReviewer`/`historicalReviewer` (mérito). Bloqueios: sem tipagem → não atinge `metadata-complete` (Etapa 1.1, Q13/Q14).
- Artefatos: campos epistêmicos no `ClaimDraft`. Riscos: inferência apresentada como fato; controvérsia achatada (mitigado: §10).

**9. Normalização temporal.**
- Entrada: claim tipado. Saída: `TimeRange` com `sourceTimeBasis`/`canonicalStart`/`canonicalEnd`/`timePrecision`/`timeUncertainty`/`conversionMethod`/`conversionNotes`.
- Responsável: `geoTemporalReviewer`. Bloqueios: tempo sem `sourceTimeBasis` → barra (Etapa 11, invariante 29). Artefatos: `TimeRange` validado.
- Riscos: falsa precisão; radiocarbono cru; offset de 50 anos no regime errado (mitigado: §11; Etapa 3Z).

**10. Normalização geoespacial.**
- Entrada: claim tipado. Saída: tratamento espacial (`geometryStatus` + `modernGeometry`/`historicalGeometryVersions`/`paleoPositions`/`modernCorrespondence` + `SpatialUncertainty`).
- Responsável: `geoTemporalReviewer`. Bloqueios: geometria sem licença/status; paleoposição sem modelo → `PENDENTE_GEOMETRIA`. Artefatos: `GeometryDraft`/`PaleoPosition`.
- Riscos: paleoposição como localização atual; `ModernCorrespondence` anacrônico; geometria proprietária (mitigado: §11; Etapa 4H, §5).

**11. Criação de `KnowledgeItem`.**
- Entrada: claim tipado + tempo/espaço. Saída: `KnowledgeItemDraft` (subtipo `Event`/`Process`/`Concept`/`Entity`/`Place`/`Region`/`State`) com `knowledgeItemId` estável.
- Responsável: `ingestionCurator`. Bloqueios: id duplicado → reconciliar (não duplicar — §12.9). Artefatos: `KnowledgeItemDraft`.
- Riscos: ids duplicados; `shortDescription` confundida com claim (mitigado: §10.2; Etapa 2, §3.3).

**12. Criação de `Claim`.**
- Entrada: rascunho consolidado. Saída: `Claim` com `provenanceRef` (`metadata-complete`).
- Responsável: `ingestionCurator` (mérito pelos revisores). Bloqueios: sem fonte A/B → barra; sem `provenanceRef` → barra.
- Artefatos: `Claim`. Riscos: claim sem incerteza; claim sem granularidade (mitigado: princípios 8/9; §10).

**13. Criação de `Citation`.**
- Entrada: claim + snapshot. Saída: `CitationRecord` (`locator`, `retrievedAt`, `quotedFact` re-codificado, `attributionText`).
- Responsável: `ingestionCurator`. Bloqueios: `attributionText` ausente quando exigido → barra (Etapa 1.1, Q5). Artefatos: `CitationRecord`.
- Riscos: reproduzir expressão em vez de re-codificar o fato (mitigado: princípio 24).

**14. Criação de `Relationship`.**
- Entrada: itens relacionados. Saída: `RelationshipDraft` tipado (`causou`/`influenciou`/`ocorreu-durante`/`parte-de`/`contemporâneo-de`/`localizado-em`/`evidenciado-por`/`hipótese-concorrente`…).
- Responsável: `ingestionCurator` + revisor de mérito (relações afirmativas são claims — Etapa 2, §229). Bloqueios: relação causal/interpretativa sem fonte A/B → barra.
- Artefatos: `RelationshipDraft`. Riscos: relação sem proveniência (mitigado: princípio 8).

**15. Criação/atualização de `ClaimSet`.**
- Entrada: claims concorrentes sobre o mesmo assunto. Saída: `ClaimSetDraft` com `consensusStatus` e, quando aplicável, `weightedClaimSets`.
- Responsável: `editorialReviewer`/`scientificReviewer`/`historicalReviewer`. Bloqueios: controvérsia sem `ClaimSet`; negacionismo como lado → barra (princípios 17/18).
- Artefatos: `ClaimSetDraft`. Riscos: controvérsia achatada; falsa equivalência (mitigado: §10; Etapa 4H, §4).

**16. Tratamento de assets.**
- Entrada: mídia/mapa/geometria associada. Saída: `AssetIntakeRecord` com `LicenseProfile`/`natureLabel`/`LicenseStorageBinding`/`storagePartition`.
- Responsável: `licenseReviewer` + `accessibilityReviewer` (equivalente textual). Bloqueios: asset órfão de licença; NC como expressão; SA no `core-store`; risco 2 sem `perAssetConfirmed`.
- Artefatos: `AssetIntakeRecord`. Riscos: asset NC reproduzido; geometria proprietária; asset sem equivalente textual (mitigado: §8; Etapa 11, §9).

**17. Revisão humana.**
- Entrada: item completo (`review-pending`). Saída: decisões dos revisores obrigatórios (`ReviewDecision`).
- Responsável: revisores competentes (científico/historiográfico/editorial/jurídico/geo-temporal/acessibilidade). Bloqueios: revisão superficial; aprovação fora de competência → barra (Seção 3.2).
- Artefatos: `ReviewDecision` por revisor. Riscos: revisão superficial; pressão para aprovar rápido (mitigado: critérios de aceite, Seção 14).

**18. Aprovação.**
- Entrada: todas as revisões aprovadas. Saída: `approved-for-kc` + `PublicationDecision` preliminar.
- Responsável: `ingestionCurator` (consolida). Bloqueios: alguma revisão pendente/reprovada → `needs-rework`/`rejected`.
- Artefatos: registro de aprovação. Riscos: consolidar sem todas as revisões (mitigado: princípio 19; §3.2).

**19. Publicação.**
- Entrada: aprovação consolidada. Saída: escrita no núcleo (`published`); `reviewStatus = approved`; publicabilidade satisfeita.
- Responsável: `ingestionCurator` via `outputToKnowledgeCore` (único caminho de escrita). Bloqueios: publicabilidade não satisfeita; equivalente textual ausente.
- Artefatos: `Claim`/`KnowledgeItem`/`Citation`/`Relationship`/asset versionados no KC; `PublicationDecision` registrada. Riscos: output usando item ainda `pending` (mitigado: invariante 9; §5.2).

**20. Invalidação de derivados.**
- Entrada: publicação (ou rejeição/depreciação). Saída: invalidação de cache e reindexação de índices derivados que referenciam o item.
- Responsável: `pipelineAdmin`/`CacheInvalidationService` (Etapa 11, §10). Bloqueios: nenhum (é obrigatória). Artefatos: registro de invalidação (`InvalidationRule` disparada por `reviewStatusChanged`/`publicabilityChanged`/`claimChanged`/`licenseChanged`).
- Riscos: cache servindo versão vencida/revogada; índice mostrando item despublicado (mitigado: invariantes 2/9/26; §9.10).

### 5.2 Diagrama do fluxo (conceitual)

```
[1 descoberta] → [2 registro] → [3 A/B/C] → [4 licença] → [5 decisão AUTO/ATRIB/ISOLA/FATO/REVH/CONF/COMER/NAO/INDX]
      → [6 snapshot] → [7 extração] → [8 tipagem] → [9 tempo] → [10 espaço]
      → [11 KnowledgeItem] → [12 Claim] → [13 Citation] → [14 Relationship] → [15 ClaimSet]
      → [16 assets] → [17 revisão humana] → [18 aprovação] → [19 publicação] → [20 invalidação de derivados]

      bloqueios laterais a qualquer momento: NAO/blocked-license · legal-review · needs-rework · rejected
      regra: nenhuma escrita no núcleo antes de [19]; nenhum item pending exibível como fato
```

### 5.3 Onde a IA pode (e não pode) entrar no fluxo

**[NORMATIVO]** a IA pode auxiliar **apenas** como ferramenta de curadoria, sempre com revisão humana a jusante e nunca como fonte: na etapa 1 (sugerir fontes candidatas a verificar), 7 (rascunhar extração de fatos a re-codificar e revisar), 8 (sugerir tipagem a confirmar), 10 (sugerir `modernCorrespondence`/anacronismos a checar) e na adaptação de **forma/linguagem** que ocorre **fora** do núcleo (Output/UX, Etapa 9/10). Em nenhum ponto a IA grava `Claim`/`Source`/`Citation`/`reviewStatus`, decide licença, aprova revisão ou publica (invariante 13; A3/Q5). Toda sugestão de IA herda `reviewStatus = pending` e é rotulada (Etapa 1.1, casos 7/8).

---

## 6. Templates de ingestão

Os templates abaixo são **dicionário conceitual** (não código). Cada um lista campos obrigatórios (●), opcionais (○) e observações de validação. Eles instrumentam o fluxo da Seção 5 e alimentam as entidades do KC (Etapa 2) e os campos do portão (Etapa 1.1).

### 6.1 `SourceIntakeRecord`

```txt
SourceIntakeRecord = {
  intakeId,            # ● id da tentativa de ingestão (estável; reaberturas geram novo intakeId)
  sourceName,          # ● nome legível da fonte
  originalUrl,         # ● URL exata do item/registro/dataset
  proposedBy,          # ● sourceScout responsável
  proposedAt,          # ● data-hora da proposta
  natureLabelPrelim,   # ● fato | expressão | obj-digitalizado (Etapa 1.1, Q1)
  layerRefs,           # ● camadas-alvo (4A) — nunca currículo/BNCC
  sourceTier,          # ○→● A | B | C (preenchido na etapa 3)
  authorityType,       # ○→● primary | aggregator | index
  sensitivityFlag,     # ○ marca preliminar de tema sensível (princípio 19)
  ingestionStatus,     # ● estado atual (Seção 4)
  notes                # ○ observações
}
```
**Validação:** sem `sourceName`/`originalUrl` não avança de `proposed`; `sourceTier = C` força `authorityType = index` e veda sustentar claim.

### 6.2 `DatasetSnapshotRecord`

```txt
DatasetSnapshotRecord = {
  snapshotId,          # ● id do snapshot
  sourceRef,           # ● referência à fonte (SourceIntakeRecord/Source)
  snapshotDate,        # ● data do congelamento
  retrievedAt,         # ● data-hora de acesso
  sourceVersion,       # ●/○ versão declarada da fonte (ex.: "ICS 2023/09"); ○ se a fonte não versiona
  checksum,            # ● hash do conteúdo congelado (imutável)
  coverageNote,        # ● o que este snapshot cobre (escopo/recorte)
  livenessClass,       # ● estática | viva-atualizada | volátil-em-risco
  storageRef,          # ● onde o snapshot reside (imutável, append-only)
  notes                # ○ ressalvas (ex.: "fonte pode sair do ar")
}
```
**Validação:** snapshot é **imutável**; `checksum` obrigatório; sem snapshot não se cria `Citation` definitiva. Fonte `viva-atualizada` exige política de recadência (§9.5).

### 6.3 `LicenseScreeningRecord`

```txt
LicenseScreeningRecord = {
  screeningId,          # ● id
  sourceRef,            # ● fonte/asset avaliado
  license,              # ● PD|CC0|CC BY|CC BY-SA|ODbL|CC BY-NC|CC BY-NC-SA|proprietária|por-item|legal-BR|fato|sem-licenca
  licenseUrl,           # ○ link ao texto da licença
  licenseRiskLevel,     # ● 0–5 (Etapa 1.1, Tarefa 4)
  nonCommercial,        # ● booleano
  shareAlikeRequired,   # ● booleano
  attributionRequired,  # ● booleano
  attributionText,      # ●/○ texto de crédito pronto (● quando exigido)
  itemLevelLicense,     # ● booleano (licença por item/dataset)
  perAssetConfirmed,    # ●/○ confirmação por asset (● para risco 2)
  ingestionDecision,    # ● AUTO|ATRIB|ISOLA|FATO|REVH|CONF|COMER|NAO|INDX
  allowedUse,           # ● knowledge-core|isolated-layer|media-dossier|index-only|blocked
  storagePartition,     # ● core-store|media-store|isolated-license-store|blocked
  exportPolicy,         # ● exportável|exportável-com-atribuição|nao-exportável|bloqueado
  reviewedBy,           # ● licenseReviewer (e legalReviewer quando aplicável)
  gatingReason,         # ●/○ razão de bloqueio/condição (quando não AUTO/ATRIB)
  rightsNotes           # ○ ex.: "obra PD; scan NC; usar provedor alternativo"
}
```
**Validação:** risco ≥ 3 nunca recebe `storagePartition = core-store`; risco 4 como expressão → `blocked`; `sem-licenca`/risco 5 → `legalReviewer`; risco 2 sem `perAssetConfirmed` → `reviewStatus = pending`.

### 6.4 `ClaimDraft`

```txt
ClaimDraft = {
  claimDraftId,         # ● id do rascunho
  statement,            # ● asserção atômica, em linguagem PRÓPRIA (nunca cópia da fonte)
  subjectRef,           # ● item de que trata (KnowledgeItemDraft)
  claimType,            # ● fato documentado|medição|inferência científica|estimativa|hipótese|
                        #    controvérsia|interpretação historiográfica|reconstrução modelada|
                        #    representação artística|aproximação didática
  confidenceLevel,      # ● alta|média|baixa|contestada + basis
  evidenceLevel,        # ● observação direta|medição instrumental|documento primário|dado modelado|
                        #    inferência indireta|testemunho secundário
  uncertaintyProfile,   # ● temporal/espacial/magnitude/interpretativa + modelDependence
  consensusStatus,      # ●/○ consenso amplo|majoritário|debate acadêmico|hipóteses concorrentes|
                        #    controvérsia historiográfica|terminologia sensível|
                        #    desinformação/negacionismo rejeitado|insuficiência de evidência
  citationRef,          # ● aponta ao CitationRecord (fonte A/B)
  temporalScopeRef,     # ● TimeRange (Seção 11)
  spatialScopeRef,      # ●/○ tratamento espacial (Seção 11), quando localizável
  provenanceRef,        # ● ProvenanceMetadata
  reviewStatus,         # ● not-required|pending|approved|rejected|legal-review (nasce pending salvo trivial)
  draftedBy,            # ● ingestionCurator (IA pode rascunhar, rotulado, sem virar claim)
  aiAssistedFlag,       # ○ marca de auxílio de IA (rascunho), exige revisão humana
  gatingReason          # ●/○ por que ainda não publicável
}
```
**Validação:** sem `claimType`/`confidenceLevel`/`citationRef` (A/B)/`provenanceRef` não atinge `metadata-complete`; `statement` que reproduza expressão protegida é barrado; negacionismo não recebe `claimType` concorrente.

### 6.5 `KnowledgeItemDraft`

```txt
KnowledgeItemDraft = {
  knowledgeItemId,      # ● id estável e versionado (reconciliar para não duplicar — §12.9)
  itemType,             # ● event|process|concept|entity|place|region|state
  preferredLabel,       # ● rótulo preferido
  aliases,              # ○ variantes (com vigência quando aplicável)
  shortDescription,     # ○ didática — NÃO é claim (Etapa 2, §3.3)
  themeTags,            # ● camadas/temas (4A) — nunca série/disciplina/BNCC
  primaryTimeRangeRef,  # ●/○ TimeRange principal (quando posicionável)
  primaryGeoRef,        # ●/○ tratamento espacial principal (quando localizável)
  claimSetRef,          # ●/○ ClaimSet do item
  provenanceRef,        # ● ProvenanceMetadata
  reviewStatus,         # ● governa exibição
  versionInfo           # ● versão do item (nunca apaga versão anterior — §9.10)
}
```
**Validação:** id duplicado → reconciliar com item existente; `itemType = state` exige um dos dez States da Etapa 2; `shortDescription` nunca é consultável como verdade.

### 6.6 `CitationRecord`

```txt
CitationRecord = {
  citationId,           # ● id
  claimRef,             # ● claim que sustenta
  sourceRef,            # ● fonte A/B
  snapshotRef,          # ● DatasetSnapshot apontado (versão exata)
  locator,              # ● página|registro|DOI|linha|id de dataset
  retrievedAt,          # ● data-hora
  quotedFact,           # ● o FATO re-codificado (nunca a expressão original)
  attributionText,      # ●/○ crédito pronto (● quando exigido)
  notes                 # ○ ressalvas
}
```
**Validação:** `quotedFact` é re-codificação, não citação literal de expressão protegida; fonte NC → registra o fato re-derivado, jamais a expressão.

### 6.7 `RelationshipDraft`

```txt
RelationshipDraft = {
  relationshipId,       # ● id
  fromRef,              # ● item origem
  toRef,                # ● item destino
  relationType,         # ● causou|influenciou|ocorreu-durante|parte-de|contemporâneo-de|
                        #    localizado-em|evidenciado-por|contradito-por|hipótese-concorrente|
                        #    sucessor/predecessor|equivalente-aproximado|versão-historiográfica
  directionality,       # ● direcionada|não-direcionada
  claimBacking,         # ●/○ relações afirmativas (causou/influenciou) SÃO claims: fonte A/B + confiança
  temporalScopeRef,     # ○ TimeRange da relação
  provenanceRef,        # ● ProvenanceMetadata (relações afirmativas)
  reviewStatus          # ● governa exibição
}
```
**Validação:** relação causal/interpretativa sem `claimBacking` (fonte A/B) é barrada; relação sem proveniência não publica.

### 6.8 `ClaimSetDraft`

```txt
ClaimSetDraft = {
  claimSetId,           # ● id
  subjectRef,           # ● assunto comum
  claims,               # ● lista de claims concorrentes (cada um com fonte A/B e confiança)
  consensusStatus,      # ● (enum do ClaimDraft)
  weighted,             # ●/○ quando há assimetria de peso (weightedClaimSets — Etapa 4H, §4)
  weights,              # ○ por claim: evidenceWeight|scholarlyWeight|displayWeight|consensusAlignment|nonEquivalentTo
  editorialNote,        # ●/○ nota editorial (Etapa 3.1)
  rejectedObjects,      # ○ negacionismo/desinformação como OBJETO rotulado-rejeitado (fora dos claims)
  reviewStatus          # ● governa exibição (sensível nasce pending)
}
```
**Validação:** controvérsia legítima exige ≥ 2 claims; negacionismo entra apenas em `rejectedObjects` com `displayWeight = rotulado-rejeitado`, nunca em `claims`; minoria legítima nunca é ocultada.

### 6.9 `GeometryDraft`

```txt
GeometryDraft = {
  geometryId,           # ● id
  ownerRef,             # ● Place/Region a que pertence
  geometryStatus,       # ● real|histórico|inferido|moderno|paleogeográfico|pendente
  geometryKind,         # ● modernGeometry|historicalGeometryVersion|paleoPosition
  timeRangeRef,         # ●/○ quando a geometria vale (paleoposição/histórica)
  paleogeographicModel, # ●/○ modelo (ex.: GPlates/EarthByte) quando paleoposição
  spatialUncertainty,   # ● margem espacial (faixa, não ponto cravado em tempo profundo)
  licenseProfileRef,    # ● LicenseProfile (geometria também tem licença)
  storagePartition,     # ● core-store (livre) | isolated-license-store (SA/ODbL) | blocked
  representationType,   # ●/○ reconstrução modelada (default em deep time)
  provenanceRef,        # ● ProvenanceMetadata
  reviewStatus          # ● governa exibição
}
```
**Validação:** SA/ODbL (OSM/MapBiomas) → `isolated-license-store`; paleoposição sempre `representationType = reconstrução modelada`; sem licença/status → `PENDENTE_GEOMETRIA`.

### 6.10 `AssetIntakeRecord`

```txt
AssetIntakeRecord = {
  assetId,              # ● id
  assetKind,            # ● MediaAsset|MapAsset|GeometryVersion|dado-tabular
  natureLabel,          # ● fotografia|mapa|gráfico|reconstrução científica|simulação|
                        #    representação artística|aproximação didática
  depictsRefs,          # ○ itens que ilustra (nunca evidencia por si só, salvo fonte A/B)
  licenseProfileRef,    # ● LicenseProfile
  licenseStorageBinding,# ● storagePartition + exportPolicy + attributionText + perAssetConfirmed
  textualEquivalent,    # ● equivalente textual (acessibilidade) com mesma info + rótulos epistêmicos
  aiGeneratedFlag,      # ○ se gerado por IA → rótulo "representação artística/aproximação didática (IA)" + revisão
  provenanceRef,        # ● ProvenanceMetadata
  reviewStatus          # ● governa exibição
}
```
**Validação:** asset órfão de licença é barrado; NC como expressão → `blocked`; SA/ODbL → isolado; risco 2 sem `perAssetConfirmed` → `pending`; sem `textualEquivalent` → `needs-rework`; imagem de IA exige rótulo + revisão (Etapa 1.1, caso 8).

### 6.11 `ReviewDecision`

```txt
ReviewDecision = {
  decisionId,           # ● id
  itemRef,              # ● item revisado (claim/asset/relação/cena)
  reviewerRole,         # ● scientificReviewer|historicalReviewer|editorialReviewer|legalReviewer|
                        #    geoTemporalReviewer|accessibilityReviewer|licenseReviewer
  reviewerRef,          # ● revisor (pseudonimizado nos logs — Etapa 11, §8)
  reviewedAt,           # ● data-hora
  outcome,              # ● aprovado|reprovado|needs-rework|escalar
  competenceCheck,      # ● confirma que o revisor está dentro de sua competência (§3.2)
  gatingReason,         # ●/○ razão de pendência/reprovação
  note                  # ○ observação técnica (sem PII/sem conteúdo sensível em claro)
}
```
**Validação:** aprovação fora de competência é inválida; item sensível exige `ReviewDecision` do revisor competente; toda decisão é registrada na `IngestionAuditTrail`.

### 6.12 `PublicationDecision`

```txt
PublicationDecision = {
  publicationId,        # ● id
  itemRef,              # ● item a publicar
  approvedReviewRefs,   # ● todas as ReviewDecision aprovadas exigidas
  reviewStatusFinal,    # ● approved
  publicabilityStatus,  # ● publicável|parcialmente-publicável (com restrições de exibição)
  visibilityClass,      # ● studentFacing|teacherOnly|internalReviewOnly|excludedButRelevant (Etapa 11, §7.3)
  storagePartition,     # ● confirma o destino físico (core/media/isolated)
  exportPolicy,         # ● herdada do LicenseStorageBinding
  publishedBy,          # ● ingestionCurator (via outputToKnowledgeCore)
  publishedAt,          # ● data-hora
  invalidationTriggered,# ● registro de invalidação de derivados (etapa 20)
  gatingReason          # ●/○ por que parcial, se aplicável
}
```
**Validação:** publica só com todas as revisões aprovadas; `pending`/`legal-review`/`rejected` nunca recebe `PublicationDecision` como fato; publicação dispara invalidação de cache/índices (invariante 9/26).

---

## 7. Política de fontes por camada

Esta seção **organiza o pipeline**: indica, por área de conteúdo (derivada das 25 camadas da Etapa 4A), quais fontes são A recomendadas, B aceitáveis e C apenas índice, com riscos de licença, riscos editoriais, tratamento de incerteza e prioridade de povoamento. **[NORMATIVO]:** esta seção **não afirma fatos novos** nem povoa conteúdo — apenas roteia o trabalho. Toda fonte herda a decisão de licença da Etapa 1.1 (códigos `AUTO`/`ATRIB`/`ISOLA`/`FATO`/`REVH`/`CONF`/`COMER`/`NAO`/`INDX`).

### 7.1 Cosmologia e astronomia (camadas 1–2)
- **A recomendadas:** NASA, JPL (PD → `AUTO`); NASA Exoplanet Archive; IAU (nomenclatura como **fato**); literatura cosmológica/astronômica revisada por pares (A/B).
- **B aceitáveis:** agregadores científicos confiáveis com proveniência clara; ESA (dados próprios).
- **C apenas índice:** Wikidata/Wikipedia (`INDX`) para desambiguar corpos celestes e capturar identificadores.
- **Riscos de licença:** baixos no núcleo (NASA PD); **ESA/Gaia é CC BY-SA IGO → `ISOLA`** (camada isolada).
- **Riscos editoriais:** Big Bang × criacionismo/terraplanismo é **negacionismo**, não `ClaimSet` (princípio 18); ilustrações sempre `representação artística`/`reconstrução modelada`, nunca "fotografia do evento".
- **Incerteza:** muito alta nos primeiros instantes (inflação = `hipótese`); alta-média a partir da nucleossíntese (`inferência científica`).
- **Prioridade:** **P0** (âncoras iniciais do eixo).

### 7.2 Geologia e escala cronoestratigráfica (camada 3)
- **A recomendadas:** **Macrostrat** (CC BY, API → `ATRIB`); **ICS** (limites e nomes como **fato recodificado** → `FATO`; gráfico CC BY-NC-SA → `NAO` como expressão); USGS (PD → `AUTO`).
- **B aceitáveis:** literatura estratigráfica revisada.
- **C apenas índice:** Wikidata para identificadores de unidades.
- **Riscos de licença:** o **gráfico do ICS é NC** — nunca reproduzir a imagem; usar só o fato e renderizar visualização própria (Etapa 1.1, caso 5).
- **Riscos editoriais:** baixos.
- **Incerteza:** idades de limite têm ± conhecidos; Pré-cambriano mais incerto (preservar `timeUncertainty`).
- **Prioridade:** **P0** (a régua do tempo profundo — pré-condição de toda interseção).

### 7.3 Paleogeografia e tectônica (camada 6)
- **A recomendadas:** **GPlates + EarthByte** (dados CC BY → `ATRIB`; software GPL); sempre rotular como **reconstrução modelada**.
- **B aceitáveis:** literatura tectônica revisada.
- **C apenas índice:** Wikidata para supercontinentes/províncias.
- **Riscos de licença:** **Deep Time Maps (proprietário) → `NAO`**; PALEOMAP/Scotese restrito até confirmação; substituir por reconstruções próprias renderizadas dos dados EarthByte.
- **Riscos editoriais:** baixos.
- **Incerteza:** **alta** em supercontinentes antigos (Rodinia, Columbia/Nuna); média na Pangeia; menor no Cenozoico — `confidenceLevel` decai com a idade.
- **Prioridade:** **P0** (é o que o globo mostra no tempo profundo).

### 7.4 Atmosfera e clima (camadas 4–5)
- **A recomendadas:** NOAA/NCEI (incl. Paleo) (PD → `AUTO`); NASA GISS; Berkeley Earth (CC BY → `ATRIB`); Copernicus/ERA5 (atribuição); literatura revisada.
- **B aceitáveis:** agregadores climáticos com proveniência clara.
- **C apenas índice:** Wikidata.
- **Riscos de licença:** **figuras do IPCC têm termos próprios → recriar a visualização** a partir dos dados (Etapa 1.1, caso 9); **INPE/MapBiomas é CC BY-SA → `ISOLA`**.
- **Riscos editoriais:** **altos** — mudança climática antrópica é **consenso**, sem equivalência ao negacionismo; `ClaimSet` apenas para incerteza interna (faixas de sensibilidade/projeção), nunca consenso × negação (princípio 17/18; Etapa 4H, §4).
- **Incerteza:** alta no profundo (`reconstrução modelada`); baixa no moderno (`medição`); projeções como **faixa**, não como dúvida do fato.
- **Prioridade:** atmosfera **P0** (pano de fundo das cenas profundas); clima **P1** (mais peso na ponta moderna; risco editorial alto).

### 7.5 Oceanos (camada 7)
- **A recomendadas:** NOAA/NCEI (PD → `AUTO`); EarthByte (bacias, CC BY → `ATRIB`); PBDB (vida marinha, CC BY → `ATRIB`).
- **B aceitáveis:** literatura oceanográfica revisada.
- **C apenas índice:** Wikidata.
- **Riscos de licença:** baixos.
- **Riscos editoriais:** baixos.
- **Incerteza:** alta no profundo (circulação/química antigas → `reconstrução modelada`/`inferência`); baixa no moderno (`medição`).
- **Prioridade:** **P2** (servida por States existentes; questão de modelagem de `OceanographicState` registrada na Etapa 4A/4H — não reaberta aqui).

### 7.6 Paleobiologia, vida e extinções (camadas 8–9)
- **A recomendadas:** **PBDB** (CC BY, API → `ATRIB`); Open Tree of Life (CC0 → `AUTO`); Macrostrat (litologia↔fóssil↔tempo).
- **B aceitáveis:** literatura paleobiológica revisada.
- **C apenas índice:** GBIF deve ser **filtrado por dataset** CC0/CC BY na entrada (`CONF`); Wikidata para táxons.
- **Riscos de licença:** baixos com filtragem de GBIF.
- **Riscos editoriais:** evolução é **consenso** → criacionismo/desenho inteligente é **negacionismo**, não `ClaimSet`; vigilância anti-racista no cruzamento com a camada 10.
- **Incerteza:** alta na origem da vida (`hipóteses concorrentes`); média nas transições; **causas de extinção** (K-Pg) como `hipóteses concorrentes`/`weightedClaimSets`.
- **Prioridade:** **P0** (as cinco extinções são marcos de 1ª ordem).

### 7.7 História humana (camadas 10–19)
- **A recomendadas:** **Pleiades** (CC BY → `ATRIB`); historiografia, paleoantropologia e arqueologia revisadas por pares (A/B); arquivos e bibliotecas (A); comissões da verdade (Brasil); museus de ciência sob curadoria.
- **B aceitáveis:** **World Historical Gazetteer** (estrutura CC BY → `ATRIB`; **filtrar datasets**); OWID/World Bank para indicadores modernos.
- **C apenas índice:** Wikidata/VIAF (`INDX`) para reconciliar pessoas/lugares/instituições.
- **Riscos de licença:** **Seshat (CC BY-NC-SA) → `NAO` como expressão**; fato re-derivável de fonte A livre via curadoria (`FATO`); **ACLED (comercial) → `NAO`** (com contrato, `COMER`); **GDELT** só como sinal (alto risco).
- **Riscos editoriais:** **altos a críticos** — colonização, escravidão, povos indígenas, raça, religião, guerras/genocídio, ditaduras, **pessoas vivas** (LGPD). Fatos documentados de repressão **não** são "um dos lados"; negação de genocídio é **negacionismo** (princípio 18; Etapa 3.1, §4).
- **Incerteza:** baixa em eventos modernos bem documentados; média/alta em cronologias e demografias antigas (`estimativa`); rotas/datas de migração e povoamento como `hipóteses concorrentes`.
- **Prioridade:** civilizações, política/Estados → **P0** (núcleo da simultaneidade; cena canônica 1789); ciência → **P1** com âncoras P0 finas (Lavoisier 1789); economia/tecnologia/migrações/guerras → **P1**; cultura/religiões/contemporâneo polarizado → **P1/P2**.

### 7.8 Brasil (camada 20)
- **A recomendadas:** **IBGE** (aberto → `ATRIB`); IPHAN; Arquivo Nacional; Biblioteca Nacional (muito PD); INPE; CPRM/SGB (geologia).
- **B aceitáveis:** historiografia brasileira revisada; IPEA (economia).
- **C apenas índice:** Wikidata para entidades brasileiras.
- **Riscos de licença:** **MapBiomas é CC BY-SA → `ISOLA`**; **microdados do IBGE não desidentificados → `NAO`/`REVH`** (não ingerir microdado restrito); Biblioteca Nacional/Hemeroteca tem muito PD utilizável.
- **Riscos editoriais:** **altos** — colonização, escravidão, povos indígenas, ditadura militar; **revisão obrigatória**; Leis 10.639/2003 e 11.645/2008 como **cobertura estrutural** (presença e protagonismo, não nota de rodapé).
- **Incerteza:** baixa-média (boa documentação moderna; território colonial com `SpatialUncertainty`).
- **Prioridade:** **P0** (lente Brasil estrutural — D8; cena canônica "Inconfidência Mineira em 1789").

### 7.9 África e diáspora (camada 21)
- **A recomendadas:** historiografia africana e afro-brasileira revisada; bases acadêmicas do tráfico transatlântico; IPHAN (patrimônio).
- **B aceitáveis:** WHG (filtrar por dataset → `ATRIB`); acervos por asset.
- **C apenas índice:** Wikidata.
- **Riscos de licença:** médio-alto (mídia por asset → `CONF`/`REVH`).
- **Riscos editoriais:** **altos** — escravidão (violência sistêmica), raça; "pessoas escravizadas" sem eufemismo; nomear resistência (quilombos); **África como origem de civilizações**, não periferia (Lei 10.639/2003).
- **Incerteza:** média (demografia do tráfico; cronologias de reinos → `estimativa`).
- **Prioridade:** **P0** (cobertura estrutural; antieurocentrismo via simultaneidade).

### 7.10 Povos indígenas e história profunda das Américas (camada 22)
- **A recomendadas:** etno-historiografia e arqueologia revisadas; IPHAN; **fontes indígenas**; IBGE (presença contemporânea).
- **B aceitáveis:** WHG (filtrar); acervos por asset.
- **C apenas índice:** Wikidata para povos/sítios.
- **Riscos de licença:** médio-alto (mídia sensível; **consentimento** para imagens de pessoas e rituais → `REVH`).
- **Riscos editoriais:** **altos** — homogeneização ("índio" genérico), sacralidade, "povos do passado"; centenas de povos com autodenominações; presença contemporânea (Lei 11.645/2008).
- **Incerteza:** **alta** (povoamento das Américas; cronologias concorrentes → `hipóteses concorrentes`).
- **Prioridade:** **P0** (cobertura estrutural; cena canônica; "em paralelo" ao Velho Mundo).

### 7.11 Economia e população (camadas 14, 23)
- **A recomendadas:** **Our World in Data** (CC BY → `ATRIB`); **World Bank** (CC BY 4.0 → `ATRIB`); IBGE/IPEA (Brasil).
- **B aceitáveis:** UN/UNESCO/WHO (**por dataset** → `CONF`).
- **C apenas índice:** Wikidata para indicadores/entidades.
- **Riscos de licença:** baixos (CC BY com atribuição rastreada); **datasets da ONU por item**; ACLED fora.
- **Riscos editoriais:** médios — interpretações de causas de desenvolvimento/desigualdade → `ClaimSet`; o produto não opina sobre política econômica; **pessoas vivas/polarização** com cautela (LGPD).
- **Incerteza:** baixa no moderno (`medição`); **alta** em séries pré-estatísticas (`estimativa`); projeções como faixa.
- **Prioridade:** **P1** (maior valor na ponta moderna; ponta "agora" do eixo).

### 7.12 Mídia e acervos (camada 24 — transversal)
- **A recomendadas:** Met Open Access/Smithsonian (CC0 → `AUTO`); Library of Congress/Internet Archive (muito PD → `AUTO`/`CONF`); Biblioteca Nacional; IPHAN.
- **B aceitáveis:** **Wikimedia Commons** (licença por arquivo → `CONF`, triagem por asset); **Europeana/DPLA** (por item → `CONF`).
- **C apenas índice:** —.
- **Riscos de licença:** **críticos** — é a camada de maior risco jurídico: licença **por asset**, isolar SA/ODbL, NC fora, confirmação obrigatória; **David Rumsey (scans CC BY-NC-SA) → `NAO`**; obter o original PD por provedor PD-explícito (Etapa 1.1, caso 1).
- **Riscos editoriais:** **altos** — violência/vítimas (mídia gráfica oculta por padrão e rotulada), propaganda (rotulada), símbolos autoritários, imagem religiosa sensível, **menores**, **toda mídia gerada por IA** (rotulada + revisada).
- **Incerteza:** a "incerteza" aqui é a **natureza** do asset (`natureLabel`), não confiança factual; mídia **não é evidência**.
- **Prioridade:** **P0 (esqueleto)** — o regime `natureLabel`/licença precisa existir desde o primeiro asset; povoamento amplo é P1/P2.

### 7.13 Mapas e geometrias (camadas 6, 13, 20 — base cartográfica)
- **A recomendadas:** **Natural Earth** (PD → `AUTO`, base cartográfica do MVP e além); **geoBoundaries** (CC BY 4.0 → `ATRIB`, substituto aberto do GADM, fronteiras modernas); EarthByte (reconstruções paleogeográficas, CC BY → `ATRIB`, rotuladas como reconstrução).
- **B aceitáveis:** datasets do WHG com geometria (filtrar).
- **C apenas índice:** Wikidata/GeoNames para reconciliação de lugares.
- **Riscos de licença:** **GADM (CC BY-NC) → `NAO`** (usar geoBoundaries); **OSM (ODbL) → `ISOLA`** (atribuição "© OpenStreetMap contributors"); **MapBiomas (CC BY-SA) → `ISOLA`**.
- **Riscos editoriais:** anacronismo espacial (fronteiras atuais projetadas ao passado); paleoposição tratada como localização atual.
- **Incerteza:** fronteiras antigas difusas (`SpatialUncertainty`); paleoposições sempre `reconstrução modelada`.
- **Prioridade:** **P0** (base de domínio público é pré-condição do globo/mapa).

### 7.14 Espinha epistêmica (camada 25 — transversal)
- **A/B:** todas as fontes A/B das demais áreas; é a tipagem que governa **todo** item.
- **C apenas índice:** **Wikidata/VIAF apenas `INDX`** (reconciliação de identificadores, nunca origem de claim).
- **Riscos de licença:** governa a licença de todas (campos `license`/`licenseRiskLevel`/`ingestionDecision`).
- **Riscos editoriais:** governa o risco de todas (falsa equivalência, inferência-como-fato, claim sem fonte).
- **Incerteza:** é **onde a incerteza vive** — `UncertaintyProfile` é sua razão de existir.
- **Prioridade:** **P0 (meta)** — é o portão; nenhuma camada entra sem ele.

---

## 8. Licenças e isolamento físico no pipeline

Esta seção detalha como o pipeline aplica, operacionalmente, o portão da Etapa 1.1 e o isolamento físico da Etapa 11 (§9). O eixo é a regra **licença governa expressão/asset, não o fato recodificado**: o fato entra livre no núcleo; a expressão restritiva é isolada ou bloqueada.

### 8.1 Matriz operacional `licenseRiskLevel` 0–5

| Risco | Exemplos (Etapa 1.1) | `storagePartition` | Entra no núcleo? | Exportação | Decisão típica |
|---|---|---|---|---|---|
| **0 — Livre** | PD, CC0, fato recodificado, texto legal BR (NASA, Natural Earth, ICS-fato, BNCC) | `core-store`/`media-store` | sim (fato/expressão livre) | exportável; atribuição opcional | `AUTO`/`FATO` |
| **1 — Atribuição** | CC BY (Macrostrat, PBDB, geoBoundaries, Pleiades, OWID, World Bank, EarthByte) | `core-store`/`media-store` com `attributionText` | sim, com atribuição | exportável-com-atribuição | `ATRIB` |
| **2 — Por item** | Wikimedia Commons, Europeana/DPLA, GBIF | `media-store` **após** `perAssetConfirmed`; até lá `pending` | só após confirmação por asset | conforme licença confirmada | `CONF` |
| **3 — ShareAlike/ODbL** | OSM, MapBiomas, ESA/Gaia, texto de Wikipedia | **`isolated-license-store`** (físico, separado) | **não** no núcleo; só camada isolada ao lado | só se SA + atribuição honrados; senão impedida | `ISOLA` |
| **4 — Não-comercial** | Seshat, GADM, gráfico ICS, scans David Rumsey | **`blocked`** como expressão; só o **fato** no núcleo | só o fato re-derivado de fonte livre | não-exportável como expressão | `NAO`/`FATO` |
| **5 — Proprietária/comercial** | ACLED, Deep Time Maps | `blocked` sem contrato; com contrato, `isolated-license-store` sob termos | não sem contrato | bloqueada sem contrato | `NAO`/`COMER` |

**[NORMATIVO]:** a matriz é imposta na **ingestão** (etapa 5 do fluxo) e **revalidada na exportação/offline** (Etapa 11, §9.11). Risco 3+ nunca toca o `core-store`; risco 4+ nunca sai como expressão.

### 8.2 Quando entra no `core-store`
Risco 0–1 cujo conteúdo é **fato** ou **expressão livre** (PD/CC0/CC BY), com `provenanceRef` e (se exigido) `attributionText`. O `core-store` guarda o grafo factual (`KnowledgeItem`/`Claim`/`ClaimSet`/`Relationship`/`Scene`) e geometrias livres (Natural Earth/geoBoundaries). **Nunca** recebe SA/ODbL/NC/proprietário.

### 8.3 Quando entra no `media-store`
Assets visuais livres (risco 0–1) e assets risco 2 **após** `perAssetConfirmed`: imagens/mapas/tiles/modelos 3D com `LicenseProfile`, `natureLabel` e `textualEquivalent`. O `media-store` serve o binário; a UX exibe a natureza (Etapa 11, §4.7).

### 8.4 Quando entra no `isolated-license-store`
Conteúdo SA/ODbL (risco 3 — OSM, MapBiomas, ESA/Gaia, texto de Wikipedia) e conteúdo proprietário **com contrato** (risco 5). Reside em *bucket*/namespace/esquema fisicamente separado, com fronteira de processo e de acesso (Etapa 11, §9.2). O `KnowledgeCoreService` **não** tem caminho de leitura para compor `Claim` a partir deste *store*; quando exibido, aparece como **camada isolada ao lado** do núcleo, com atribuição, sem fusão.

### 8.5 Quando é bloqueado (`blocked`)
Expressão NC (risco 4) como expressão; fonte `sem-licenca` (default conservador); risco 5 sem contrato; figura protegida cuja reprodução não foi licenciada. Bloqueado significa que o asset **não é servido** nem exportado; apenas o **fato re-derivado de fonte livre** pode existir no núcleo, com fonte própria.

### 8.6 Quando só o fato recodificado entra (`FATO`)
Quando a fonte é NC/proprietária mas o **fato** é livre: limites do ICS (gráfico NC → fato livre), dados em fonte NC re-deriváveis de fonte A/B livre (caso Seshat). O fato entra no `core-store` com `provenanceChain` registrando a origem; a expressão NC não entra (Etapa 1.1, casos 2/5).

### 8.7 Quando exige contrato comercial (`COMER`)
Risco 5 (ACLED, Deep Time Maps): só entra com contrato comercial validado pelo `legalReviewer`, e mesmo então no `isolated-license-store` sob os termos do contrato, com cláusula anti-substituto respeitada. Sem contrato, `blocked`.

### 8.8 Como registrar atribuição
Quando `attributionRequired = true`, o `attributionText` é preenchido na etapa 4/5 e **viaja com o item/asset por todo o caminho** — exibição, cache, exportação, offline — nunca descartado por "limpeza de tela" ou compactação de pacote (Etapa 11, §9.9, invariante 17).

### 8.9 Como confirmar licença por asset (`perAssetConfirmed`)
Para fontes de licença heterogênea por item (risco 2 — Commons, Europeana/DPLA, GBIF), o `licenseReviewer` confirma a licença **daquele** arquivo/registro antes do uso; até a confirmação, `reviewStatus = pending` e o asset não é servido (Etapa 11, §9.5).

### 8.10 Como impedir NC como expressão
O `LicenseScreeningRecord` marca `nonCommercial = true` e `ingestionDecision = NAO`/`FATO`; o `licenseReviewer` barra a entrada do asset como expressão; a exportação/offline consulta o `exportPolicy` e bloqueia qualquer asset `nao-exportável`/`bloqueado` (Etapa 11, §9.6, invariante 19).

### 8.11 Como impedir SA/ODbL no núcleo
O `LicenseStorageBinding` força `storagePartition = isolated-license-store` para `shareAlikeRequired = true`; o `KnowledgeCoreService` não lê desse *store* para compor `Claim`; a fronteira física e de processo impede a fusão (Etapa 11, §9.2/§9.7, invariante 18).

### 8.12 Como exportação/offline herdam a licença
**[NORMATIVO]** todo `ExportPackage`/`OfflinePackage` revalida a licença no momento da saída: embute `attributionText`, respeita `exportPolicy`, honra SA/ODbL (ou impede o material quando o formato não puder honrar), bloqueia NC/proprietário como expressão e nunca relaxa por ausência de rede (`offline não relaxa garantias` — Etapa 11, §9.7/§9.8, invariantes 10/11/27).

---

## 9. Proveniência, snapshots e versionamento

### 9.1 Como criar `DatasetSnapshot`
Na etapa 6 do fluxo, ao decidir a entrada de uma fonte, o `ingestionCurator` congela a versão ingerida: registra `snapshotDate`, `retrievedAt`, `sourceVersion` (quando a fonte versiona), `checksum` (hash imutável do conteúdo) e `coverageNote`. O snapshot é custodiado pelo `SourceProvenanceService` (Etapa 11, §3.3) em armazenamento **append-only** e referenciado por cada `Citation` (Etapa 2, §255–261).

### 9.2 Quando o snapshot é obrigatório
**[NORMATIVO]** sempre que uma fonte sustenta qualquer `Claim`/`Citation`/`Relationship` afirmativa ou origina um asset/geometria. Não existe `Citation` definitiva sem snapshot. Fonte sem snapshot não avança de `snapshot-created`.

### 9.3 Como registrar `checksum`
O `checksum` é o hash do conteúdo congelado; ele torna o snapshot **imutável** e auditável (qualquer alteração do conteúdo original gera novo snapshot, nunca sobrescreve o anterior). É a prova de que a `Citation` aponta exatamente ao que foi lido.

### 9.4 Como registrar data de acesso
`retrievedAt` (na `DatasetSnapshot` e na `Citation`) registra quando o conteúdo foi obtido — distinto do tempo histórico do conteúdo (Etapa 3Z) e do `occurredAt` técnico da auditoria (Etapa 11, §12.1). É a âncora de reprodutibilidade.

### 9.5 Como lidar com fonte viva/atualizada
Fonte `livenessClass = viva-atualizada` (OWID, World Bank, IBGE, INPE) recebe **política de recadência**: cada atualização relevante gera **novo `DatasetSnapshot`** (nova versão), preservando os anteriores; os `Claim` derivados são versionados (§9.9) e os derivados (cache/índice) invalidados (etapa 20). **[PENDÊNCIA]** a cadência concreta por fonte (mensal/anual/sob demanda) é decisão operacional da Etapa 14 (Etapa 2, §11, item 5).

### 9.6 Como lidar com fonte que sai do ar
Fonte `volátil-em-risco` ou que saiu do ar continua sustentando os claims já ingeridos **pelo snapshot congelado** — o sistema não depende do acesso ao vivo (antifragilidade, C4/R7). Se a fonte desaparece, registra-se em `notes`; o claim permanece válido pela `Citation` ao snapshot, e a curadoria busca corroboração adicional quando o tema exigir.

### 9.7 Como versionar `Source`
`Source` é versionada quando muda sua classificação (A/B/C), sua licença ou sua identidade institucional; cada versão referencia seus `DatasetSnapshot`. Mudança de licença dispara revalidação de `LicenseStorageBinding` e invalidação de derivados.

### 9.8 Como versionar `Claim`
`Claim` é versionado quando muda `statement`, `claimType`, `confidenceLevel`, `evidenceLevel`, `UncertaintyProfile`, `temporalScope`/`spatialScope` ou a fonte. **A nova versão não apaga a anterior**: a anterior é `deprecated`, preservada para auditoria do que foi mostrado antes da correção.

### 9.9 Como versionar `KnowledgeItem` e `Scene`
`KnowledgeItem` mantém `versionInfo`; `Scene` v1.1 é versionada por mudança de qualquer campo dos 34 (Etapa 4H, §2) ou de `sceneCompletenessLevel`/`publicabilityStatus`. **[NORMATIVO]:** timeline e globo referenciam a **mesma versão** de conteúdo (Etapa 11, invariante 28); uma cena nunca é exibida com claims de versões divergentes.

### 9.10 Como deprecar sem apagar
**[NORMATIVO] — regra explícita: correção futura não apaga o passado auditável; ela cria nova versão.** Ao corrigir/atualizar um item, cria-se a nova versão (`published`) e a anterior passa a `deprecated`, com motivo registrado. A versão deprecada não é exibível como fato atual, mas permanece consultável pela auditoria — para reconstruir exatamente o que um `ExportPackage`/`OfflinePackage`/cena mostrou em determinada data (Etapa 11, §5, invariante 16/27).

### 9.11 Como auditar conteúdo usado antes de uma correção
A `IngestionAuditTrail` (abaixo) registra, por **referência e versão**, qual versão de cada item foi servida e quando; cruzando com os snapshots e as `PublicationDecision`, reconstrói-se a cadeia **artefato → bloco → cena/momento → claim → fonte → licença** em qualquer data passada (Etapa 11, §12.4). Material sem caminho de volta à evidência é, por definição, defeito de ingestão.

```txt
IngestionAuditTrail = {
  auditId,
  occurredAt,            # timestamp técnico (UTC) do evento de ingestão
  actorRole,             # papel de ingestão (Seção 3), pseudonimizado nos logs (Etapa 11, §8)
  eventClass,            # proposta | classificação | licença | snapshot | extração | tipagem |
                         # tempo | espaço | revisão | aprovação | publicação | depreciação | invalidação
  itemRef,               # item afetado (por referência e versão; nunca conteúdo sensível em claro)
  contentVersionRef,     # versão de conteúdo envolvida (reprodutibilidade)
  ingestionStatusFrom,   # estado anterior
  ingestionStatusTo,     # estado novo
  decisionRef,           # ReviewDecision/PublicationDecision/LicenseScreeningRecord pertinente
  gatingReason,          # razão de pendência/bloqueio quando aplicável
  dataMinimizationClass  # SEM-PII | PSEUDONIMIZADO | AGREGADO (nunca PII de aluno; nunca PII de menor em claro)
}
```

**[NORMATIVO]:** a `IngestionAuditTrail` registra **referências e versões**, nunca conteúdo sensível em claro nem PII; ela costura-se à `TechnicalAuditTrail` da Etapa 11 (§12) sem duplicá-la, compondo a cadeia de rastreabilidade fim a fim.

---

## 10. Extração, normalização e tipagem de claims

### 10.1 Granularidade de claim
**[NORMATIVO]** um `Claim` é **atômico**: uma asserção verificável por claim. "A Queda da Bastilha ocorreu em 14/07/1789" é um claim; "A Revolução Francesa começou em 1789 por causas fiscais, sociais e iluministas" é um **assunto** que se decompõe em vários claims (cada causa) reunidos em `ClaimSet`/`weightedClaimSets`. Granularidade ruim (claims compostos, vagos ou múltiplos numa frase) é devolvida em `needs-rework` (risco R-13.08).

### 10.2 Diferença entre `shortDescription` e `Claim`
`shortDescription` (campo do `KnowledgeItem`) é prosa didática de conveniência — **não** é claim, **não** é consultável como verdade e **não** tem peso epistêmico (Etapa 2, §3.3). Toda afirmação factual que o produto trata como verdade é um `Claim` tipado e fonteado; a `shortDescription` apenas orienta a leitura e nunca substitui o claim.

### 10.3 `claimType`
Enum exibível (Etapa 2, §3.4): `fato documentado` · `medição direta` · `inferência científica` · `estimativa` · `hipótese` · `controvérsia` · `interpretação historiográfica` · `reconstrução modelada` · `representação artística` · `aproximação didática`. **[NORMATIVO]:** claim de tipo `inferência`/`hipótese`/`controvérsia`/`reconstrução` **sem rótulo visível** não publica (Etapa 1.1, hard stop 6).

### 10.4 `confidenceLevel`, `evidenceLevel` e `UncertaintyProfile`
- **`confidenceLevel`** (`alta`/`média`/`baixa`/`contestada` + `basis`): quão seguros estamos de que o claim é verdadeiro (Etapa 2, §208–211).
- **`evidenceLevel`** (`observação direta`/`medição instrumental`/`documento primário`/`dado modelado`/`inferência indireta`/`testemunho secundário`): a **natureza** da evidência — ortogonal à confiança (Etapa 2, §213–217).
- **`UncertaintyProfile`** (`temporalUncertainty`/`spatialUncertainty`/`magnitudeUncertainty`/`interpretiveUncertainty`/`modelDependence`): a incerteza estruturada, sem reduzir tudo a um número (Etapa 2, §219–223).

### 10.5 `consensusStatus`, controvérsias, hipóteses, inferências, interpretações, estimativas, aproximações e representações
- **`consensusStatus`** (Etapa 4A/3.1): `consenso amplo` · `consenso majoritário` · `debate acadêmico` · `hipóteses concorrentes` · `controvérsia historiográfica` · `terminologia sensível` · `desinformação/negacionismo rejeitado` · `insuficiência de evidência`.
- **Controvérsia legítima** → `ClaimSet` com claims concorrentes e peso (`weightedClaimSets`); o produto **estrutura**, não decide (Etapa 3.1, §3; Etapa 4H, §4).
- **Hipótese** → `claimType = hipótese`, confiança média/baixa, rótulo "em aberto".
- **Inferência científica** → `claimType = inferência científica`, com confiança e `evidenceLevel = dado modelado`/`inferência indireta`.
- **Interpretação historiográfica** → `claimType = interpretação historiográfica` em `ClaimSet` com `consensusStatus = controvérsia historiográfica`.
- **Estimativa** → `claimType = estimativa` (demografias/séries pré-estatísticas), com faixa.
- **Aproximação didática** → `claimType = aproximação didática`, rotulada como simplificação, sem alterar o fato subjacente.
- **Representação artística** → `claimType = representação artística`/`natureLabel = representação artística`, nunca apresentada como registro.

### 10.6 Negacionismo/desinformação e linguagem sensível
**[NORMATIVO]** negacionismo (rejeição de fato/consenso bem estabelecido sem evidência válida) **não** é claim concorrente: entra apenas como **objeto rotulado** (`consensusStatus = desinformação/negacionismo rejeitado`; `displayWeight = rotulado-rejeitado`), **fora** do `ClaimSet`, contraposto ao consenso (Etapa 3.1, §5; Etapa 4H, §4). Linguagem sensível (raça, escravidão, violência, religião) segue a política editorial: sem eufemismo que apague violência, sem reproduzir discurso discriminatório como voz própria, com mediação por faixa etária (Etapa 3.1, §8).

### 10.7 Revisão humana obrigatória na tipagem
**[NORMATIVO]** a tipagem epistêmica final de qualquer claim é confirmada por revisor humano competente (científico/historiográfico/editorial) antes de `approved-for-kc`; a IA pode **sugerir** tipagem, nunca fixá-la (princípio 3; §5.3).

### 10.8 Regras de re-codificação (não copiar; reescrever; manter citação; não alterar o fato)
**[NORMATIVO]** quatro regras inseparáveis na extração (etapa 7) e citação (etapa 13):
1. **Não copiar texto da fonte.** A expressão original não é reproduzida (Etapa 1.1, casos 2/9; princípio 24).
2. **Reescrever em linguagem própria.** O `statement` e o `quotedFact` são re-codificações do fato, em palavras próprias.
3. **Manter a citação.** A `Citation` aponta ao `locator` exato no snapshot, com `attributionText` quando exigido — citar não é reproduzir.
4. **Não alterar o fato ao adaptar a linguagem.** Adaptação de forma/faixa etária (IA inclusive) muda a **forma**, nunca o conteúdo factual (`forma muda; fato não` — Etapa 3.1, §1.8; invariante 14).
5. **Não deixar a IA redigir o claim factual final sem revisão.** Rascunho de IA herda `reviewStatus = pending` e exige confirmação humana (princípio 3).

---

## 11. Normalização temporal e geoespacial

### 11.1 Tempo — base canônica e preservação
**[NORMATIVO]** na etapa 9 do fluxo, todo claim posicionável recebe um `TimeRange` com: `sourceTimeBasis` (datum nativo preservado), `canonicalStart`/`canonicalEnd`/`canonicalTimeScalar` (derivados, em anos relativos a **T0 = 2000.0 CE ≈ J2000**), `timePrecision`, `timeUncertainty`, `conversionMethod` e `conversionNotes` (Etapa 3Z, §2/§9). O `sourceTimeBasis` **nunca** é apagado (Etapa 11, invariante 29).

### 11.2 `sourceTimeBasis` e regimes temporais
`sourceTimeBasis` ∈ {`BP1950`, `calBP`, `radiocarbonBP`, `J2000`, `gregorianCE`, `ISO8601`, `Ma`, `Ga`, `scenarioYear`}. Os **sete regimes** (Etapa 3Z, §4) determinam entrada, conversão e exibição:

| Regime | Datum comum | Conversão | Exibição (`displayTime`) | Risco de erro |
|---|---|---|---|---|
| **1. Cósmico** | inferência astronômica | `Ga → anos rel. T0` | "~13,8 Ga" | tratar como data exata |
| **2. Geológico profundo** | ICS + radiométrica | `Ma/Ga → anos rel. T0` (50 anos = ruído) | "~2,4 Ga"/"~66 Ma" | falsa precisão; ignorar versão ICS |
| **3. Biológico/evolutivo** | PBDB + escala | `Ma/ka → anos rel. T0` | "~300 ka"/"~66 Ma" | datas de origem cravadas |
| **4. Arqueológico** | **cal BP** (¹⁴C calibrado) | calibrar ¹⁴C→cal BP, depois `cal BP → T0` (**+50 anos**) | "~14.000 anos atrás" | usar ¹⁴C bruto; ignorar offset |
| **5. Histórico** | gregoriano proléptico | `CE/BCE → anos rel. T0` (ano-zero astronômico) | "1789", "44 a.C." | erro do ano zero; juliano×gregoriano |
| **6. Contemporâneo** | ISO 8601 | `ISO → anos rel. T0` (direto) | "20 jul 1969" | confundir medido com estimativa |
| **7. Projetivo/futuro** | ano + modelo (RCP/SSP) | `ano → anos rel. T0` (positivo) | "2050 (cenário X)" | exibir projeção como fato |

**[NORMATIVO]:** radiocarbono **nunca** entra cru (calibrar para cal BP antes do eixo, preservar ambos); o **offset de 50 anos** (BP1950→T0) só se aplica aos regimes 4–5; futuro é **sempre** rotulado como projeção, jamais "fato datado" (Etapa 3Z, §4/§9).

### 11.3 Incerteza, intervalos, eventos pontuais, processos longos e States
- **Incerteza temporal** preservada em `timeUncertainty` (± / faixa / distribuição); um item difuso "aparece" no momento consultado **com ressalva**, não como presença cravada (Etapa 3Z, §10).
- **Eventos pontuais**: `canonicalStart = canonicalEnd` (Bastilha 1789-07-14; impacto de Chicxulub ≈ −6,6e7).
- **Intervalos/processos longos**: `[canonicalStart, canonicalEnd]` com bordas difusas quando incertas (GOE ≈ −2,4e9 a −2,0e9).
- **States** (os dez da Etapa 2): faixas de fundo no intervalo canônico.

### 11.4 Calendário histórico e data técnica
**[NORMATIVO]** a **data técnica UTC** do evento de ingestão/exibição (`occurredAt`/`retrievedAt`) é distinta do **tempo histórico** do conteúdo (`displayTime`). Datas pré-gregorianas usam gregoriano proléptico + nota (ano-zero astronômico; juliano×gregoriano). Calendários não-ocidentais são `sourceTimeBasis` adicionais **[PENDÊNCIA]** (Etapa 3Z, §9), preenchidos por curadoria quando surgirem fontes que os exijam.

### 11.5 Espaço — mecanismos e quando cada um se aplica
**[NORMATIVO]** na etapa 10 do fluxo, todo item localizável recebe tratamento espacial via os quatro mecanismos da Etapa 4H (§5):
- **`modernGeometry`** — forma **atual** do lugar (Paris, Yucatán); usada em cenas atuais.
- **`historicalGeometryVersions`** — formas em **períodos históricos** documentados (fronteira da França em 1789; Capitania de Minas); usadas no tempo histórico.
- **`paleoPositions`** — **posições paleogeográficas** em tempo profundo (Chicxulub em 66 Ma); **sempre** `reconstrução modelada` rotulada.
- **`modernCorrespondence`** — a **lente** "o que hoje é…" (Capitania → MG); liga passado a referência atual **sem** projetar a realidade atual ao passado.

### 11.6 `GeometryVersion`, `geometryStatus`, `SpatialUncertainty`, paleoposição e licença
`GeometryVersion` carrega `geometryStatus` (`real`/`histórico`/`inferido`/`moderno`/`paleogeográfico`/`pendente`), `SpatialUncertainty` (faixa, não ponto cravado em tempo profundo), `paleogeographicModel` (GPlates/EarthByte) quando paleoposição, e `licenseProfileRef`/`storagePartition` (geometrias SA/ODbL → `isolated-license-store`). Sem licença/status: `PENDENTE_GEOMETRIA`/`PENDENTE_REFINAMENTO_ESPACIAL` (Etapa 4H, §5).

### 11.7 Evidência atual vs paleoposição; anacronismo espacial
**[NORMATIVO]** um lugar atual pode ser **evidência** geológica (Hamersley, Huroniano, Transvaal são `modernPlace` de evidência do GOE) e ter **paleoposição** própria e incerta no passado. O marcador de tempo profundo usa a **paleoposição rotulada**, nunca a coordenada moderna; o usuário **sempre vê qual geometria está em uso**. Anacronismo espacial (fronteiras/nações atuais projetadas ao passado; "México" em 66 Ma) é barrado e, quando ilustrado, recebe `AnachronismNotice` (Etapa 4H, §5; Etapa 12, §10.1).

### 11.8 Exemplos conceituais (sem alterar as cenas-gabarito)
Os exemplos abaixo **ilustram** como o pipeline normaliza tempo e espaço; eles **não** reescrevem as três cenas-gabarito (Etapa 4H/4Z), apenas demonstram a aplicação das regras a itens análogos.

- **1789 (regime histórico).** Um `Event` análogo à Queda da Bastilha: `sourceTimeBasis = gregorianCE`; `displayTime = "1789"` (evento de dia: `1789-07-14`); `canonical` preciso (sem offset de 50 anos relevante, mas a regra dos regimes 4–5 se aplicaria a datas BP). Espaço: `modernGeometry` (Paris hoje) + `historicalGeometryVersions` (fronteira de 1789) + `modernCorrespondence` (Capitania de Minas → MG). Sem `paleoPositions` (irrelevante no tempo histórico).
- **GOE 2,4 Ga (regime geológico profundo, sem evento).** Um `Process`/`State` análogo à oxigenação: `sourceTimeBasis = Ga`; faixa `[−2,4e9, −2,0e9]`; offset de 50 anos descartado (ruído); `claimType = inferência científica`/`reconstrução modelada` com `UncertaintyProfile` alto. Espaço: localidades de evidência como `modernPlace` com `paleoPositions` esquemáticas e incertas; globo esquemático rotulado.
- **K-Pg 66 Ma (regime geológico profundo, com evento — híbrido).** Um `Event` análogo ao impacto: `sourceTimeBasis = Ma`; ponto `≈ −6,6e7`; extinção como faixa; `cascadeStructure` com `confidenceByStage` decaindo; `weightedClaimSets` (impacto **dominante/primário** ≫ Deccan **contribuinte/secundário**; negacionismo `rotulado-rejeitado` fora do `ClaimSet`). Espaço: `paleoPositions[66 Ma]` para a cratera (paleoposição ≠ Yucatán atual); `AnachronismNotice` para "México em 66 Ma".

**[NORMATIVO]:** estes exemplos são **conceituais**; nenhuma escrita real é feita sobre as cenas-gabarito nesta etapa (Seção 12 trata da migração formal do seed).

---

## 12. Migração do seed do MVP para conteúdo canônico

Esta seção define como as **três cenas-gabarito** da Etapa 12 — `scene:world-1789-french-revolution`, `scene:earth-2-4ga-great-oxidation-event` e `scene:earth-66ma-kpg-extinction` — deixam de ser *seed* de demonstração e passam (quando, e somente quando, autorizadas) a **conteúdo canônico auditável**, sem que isso reabra as cenas-gabarito, duplique claims, apague proveniência ou contorne o portão.

### 12.1 O que é `seed-MVP`

**[NORMATIVO]** o conjunto seedado da Etapa 12 é, por definição, **insumo de demonstração**, não produto do pipeline. Materialmente, ele é identificado por: `DatasetSnapshot` com `snapshotOrigin = "seed-MVP-cenas-gabarito"` (Etapa 12, §9.7); itens com `sceneCompletenessLevel ∈ {gabarito-interno, parcialmente-publicável}` (Etapa 4H/4Z); e *placeholders* explicitamente rotulados de mídia/geometria (Etapa 12, §12.5). O seed entrou por um **caminho de escrita único e fechado**, próprio do MVP (Etapa 12, §1.6), preparado para ser substituído pelo caminho de ingestão da Seção 5 — **não** é o resultado do fluxo de 20 etapas. Por isso o princípio 28 (`seed do MVP não é pipeline`) e o teste de invariante correspondente (§14, T-13.19): nada que ostente apenas a marca `seed-MVP` pode ser contado como conteúdo ingerido, nem exibido como se tivesse atravessado o portão.

### 12.2 O que pode ser aceito como canônico

**[NORMATIVO]** a migração é uma **reingestão sob o pipeline real**, não uma promoção automática. Um item seedado só vira canônico depois de **reentrar pela Seção 5** a partir da etapa apropriada e satisfazer os portões. Em concreto:

- **Aceitável com reconfirmação leve (revalidação):** itens cujo claim já nasceu fonteado em fonte A/B no seed (com `provenanceRef`, `claimType`, `confidenceLevel`, `evidenceLevel`, `UncertaintyProfile` e `reviewStatus` coerentes) — p.ex. a datação da Queda da Bastilha (1789-07-14), a faixa do GOE (≈ −2,4 a −2,0 Ga) e o horizonte do impacto K-Pg (≈ −66 Ma). Esses **revalidam** a fonte e o snapshot (§9.5) e seguem para revisão de confirmação.
- **Aceitável só após reconstrução:** qualquer claim do seed sem fonte A/B explícita, qualquer `shortDescription` que tenha sido usada como se fosse claim, qualquer geometria/mídia *placeholder*. Esses **não** migram como estão: são re-derivados pelo fluxo (etapas 7–16 da Seção 5).
- **Nunca aceitável sem reabertura formal:** alterar a estrutura das cenas-gabarito (os 34 campos, `cascadeStructure`, `weightedClaimSets`, `paleoPositionPolicy`) — isso é proibido nesta etapa (limite de natureza; invariante das Etapas 11/12). A migração **anexa** versões canônicas ao redor do gabarito; não o reescreve.

### 12.3 Reconfirmações obrigatórias por eixo

**[NORMATIVO]** antes de qualquer item seedado receber `populationStatus` acima de `seed-only`, cinco reconfirmações independentes são registradas como `ReviewDecision` (template §6.11), cada uma pelo papel competente (Seção 3) e com `gatingReason` (requisito 24):

| Eixo | Quem | O que reconfirma | Bloqueia se… |
|---|---|---|---|
| **Fonte** | `sourceScout` + `ingestionCurator` | que o claim tem fonte **A/B** real, citável no `locator` do snapshot; que `sourceTier` está correto | fonte ausente, C, ou só índice (`INDX`) → `needs-rework` |
| **Licença** | `licenseReviewer` | `LicenseProfile` de cada fonte/asset; `licenseRiskLevel`; partição física; `perAssetConfirmed` para mídia | NC como expressão, SA/ODbL no `core-store`, asset sem confirmação → `blocked-license`/`legal-review` |
| **Científica** | `scientificReviewer` | `claimType`/`confidenceLevel`/`evidenceLevel`/`UncertaintyProfile`; `consensusStatus`; pesos de `weightedClaimSets` (GOE, K-Pg) | tipagem incoerente, falsa precisão, consenso achatado → `needs-rework` |
| **Editorial** | `editorialReviewer` (+ `historicalReviewer` p/ 1789) | linguagem própria (não copiada), neutralidade, faixa etária, tratamento de tema sensível (1789: violência revolucionária; colonização correlata) | texto copiado, viés, sensível sem cuidado → `needs-rework`/`pending` |
| **Jurídica** | `legalReviewer` | conformidade final de licença/atribuição/exportação; ausência de PII; *hard stops* | qualquer pendência jurídica → `legal-review` (default **não** publica) |

Para temas sensíveis presentes no seed (a violência de 1789; correlatos de colonização/escravidão que toquem a Lei 11.645/2008), a revisão humana é **obrigatória** e o item nasce `pending` até liberação (Etapa 3.1; princípio 19; requisito 25).

### 12.4 Como manter os ids estáveis

**[NORMATIVO]** os identificadores das três cenas e dos itens estáveis do seed são **preservados** na migração. A reingestão **acresce versões** (`KnowledgeItem`/`Claim`/`Scene` ganham nova `versionId` — §9.7–§9.9) ao **mesmo** `sceneId`/`itemId`, em vez de criar ids novos. Isso garante que: ponteiros já existentes (de `MomentResult`, de índices derivados, de cenas) continuem resolvendo; a auditoria ligue a versão seed à versão canônica numa linha contínua; e nenhuma vista aponte para um "órfão". Criar id novo para o mesmo referente é o anti-padrão de ids duplicados (R-13.19) e é barrado por checagem de identidade na curadoria.

### 12.5 Como não duplicar claims

**[NORMATIVO]** a migração é **idempotente por referente**. Antes de gravar um claim canônico, o `ingestionCurator` verifica se já existe claim para a mesma asserção atômica (mesmo referente factual, mesmo `TimeRange` canônico, mesmo lugar) vindo do seed; se existir, **versiona o existente** (nova `claimVersion`, `supersedes` aponta à versão seed) em vez de inserir um segundo claim. O resultado é **um** claim canônico por fato, com histórico, e **nunca** dois claims concorrentes "iguais" inflando o grafo. A de-duplicação é critério de aceite da migração (§12.10) e teste de QA (T-13.20).

### 12.6 Como versionar a migração

**[NORMATIVO]** toda a migração ocorre sob versionamento explícito (§9): cada `Source` revalidada ganha `sourceVersion` nova quando a fonte viva mudou (§9.5); cada `Claim` migrado ganha `claimVersion` com `supersedes`; cada `Scene` migrada sobe de `sceneCompletenessLevel` por uma **nova** `sceneVersion`, sem destruir a versão `gabarito-interno`. Um `DatasetSnapshot` novo, com `snapshotOrigin = "canonical-migration-P0"`, registra o estado canônico, distinto do snapshot `seed-MVP` original — que **permanece** arquivado e auditável.

### 12.7 Como preservar a auditabilidade

**[NORMATIVO]** a cadeia de rastreabilidade da Etapa 11 (artefato → bloco → cena/momento → claim → fonte → licença) é mantida **através** da migração: o `IngestionAuditTrail`/`TechnicalAuditTrail` registra a transição seed→canônico como uma sequência de `ReviewDecision`/`PublicationDecision`, ligando cada versão canônica à sua origem seed e à decisão humana que a liberou. **Correção/depreciação não apaga o passado** (§9.10–§9.11; regra explícita da Seção 9): a versão seed e seu snapshot ficam recuperáveis para reconstruir "o que a demonstração mostrava antes da migração".

### 12.8 Como substituir os placeholders

**[NORMATIVO]** cada *placeholder* rotulado do MVP (Etapa 12, §12.5) é substituído por **asset real** que entrou pelo seu próprio fluxo de ingestão (etapa 16 da Seção 5) com `AssetIntakeRecord` (§6.10) completo: `LicenseProfile`, `licenseRiskLevel`, `storagePartition` correta e — para risco 2 — `perAssetConfirmed = true` (Etapa 11, §9; §8.9). Enquanto o asset real não existir, o item permanece com o marcador `PENDENTE_LICENCA`/`PENDENTE_GEOMETRIA` e **não** é publicado como definitivo (R-13.18). O mapa-base Natural Earth (PD) já validado no MVP pode permanecer como base, revalidado sob `AUTO` (Etapa 1.1). Substituir *placeholder* por "final" sem confirmação por asset é barrado (T-13.06/T-13.21).

### 12.9 Como transformar `gabarito-interno` em publicável

**[NORMATIVO]** a subida de `sceneCompletenessLevel` (`gabarito-interno`/`parcialmente-publicável` → `publicável`) é uma `PublicationDecision` (§6.12), nunca automática. Ela exige: todos os claims da cena `approved-for-kc`; todas as licenças resolvidas (núcleo limpo, isolados separados, NC fora como expressão); todos os *placeholders* substituídos ou explicitamente marcados como pendentes não exibíveis; tempo e espaço normalizados e rotulados; revisão sensível concluída quando aplicável; e `gatingReason` registrando a base da liberação. Sem **todos** os portões, a cena permanece publicável apenas **em parte** (os blocos liberados) — coerente com `sceneCompletenessLevel = parcialmente-publicável` (Etapa 4H/4Z) — e o restante segue `pending`, jamais exibido como fato (invariante 9).

### 12.10 Tabela de migração das três cenas-gabarito

A tabela abaixo é **plano de migração**, não escrita de conteúdo: ela define, por cena, o que revalida, o que reconstrói, o que substitui e o critério de aceite. Nenhuma célula afirma fato novo nem altera a cena-gabarito.

| Cena (`sceneId`) | Regime / camadas | Revalida (fonte A/B + snapshot) | Reconstrói pelo fluxo | Placeholders a substituir | Reconfirmações críticas | Critério de aceite da migração |
|---|---|---|---|---|---|---|
| **`scene:world-1789-french-revolution`** | Histórico (5); camadas 10–19, 20 (lente Brasil) | datação 1789-07-14 e `displayTime`; `historicalGeometryVersions` (fronteira de 1789) e `modernCorrespondence` (Capitania de Minas → MG) a partir de fontes A/B históricas | claims de causa/consequência em `weightedClaimSets`; `Relationship` causais com proveniência; linguagem editorial própria | retratos/ilustrações de época (verificar PD vs acervo); mapa histórico (se não-Natural Earth) | **editorial/histórica** (violência revolucionária; correlatos Lei 11.645/2008) → `pending` até liberar; **licença** de imagens | 1 claim por fato; tema sensível revisado; imagens com `perAssetConfirmed`; ids preservados; cena sobe a `publicável` só com todos os blocos `approved` |
| **`scene:earth-2-4ga-great-oxidation-event`** | Geológico profundo (2); camadas 3, 4–5, 6, 8 | faixa `[−2,4e9, −2,0e9]`; `claimType = inferência científica`/`reconstrução modelada`; `UncertaintyProfile` alto; localidades de evidência (Hamersley/Huroniano/Transvaal) como `modernPlace` | `paleoPositions` esquemáticas rotuladas; pesos de hipóteses concorrentes (causa/ritmo) em `ClaimSet` | globo esquemático rotulado; texturas atmosféricas ilustrativas | **científica** (não cravar data; faixa, não ponto; consenso tipado); **licença** de geometrias (GPlates/EarthByte → atribuição/isolamento) | falsa precisão barrada; paleoposição ≠ atual rotulada; geometrias com licença/status; faixa e incerteza preservadas |
| **`scene:earth-66ma-kpg-extinction`** | Geológico profundo / híbrido (2→3); camadas 3, 6, 8–9 | horizonte `≈ −6,6e7`; impacto **dominante/primário** vs Deccan **contribuinte/secundário** (`weightedClaimSets`); `cascadeStructure` com `confidenceByStage` decaindo | `paleoPositions[66 Ma]` da cratera; `AnachronismNotice` ("México em 66 Ma"); negacionismo como `rotulado-rejeitado` **fora** do `ClaimSet` | reconstrução paleogeográfica; arte do impacto (rotulada `representação artística`) | **científica** (pesos impacto≫Deccan; cascata); **editorial** (arte rotulada, não evidência) | pesos preservados; negacionismo nunca como lado (T-13.11/§14); paleoposição rotulada; arte separada de evidência |

**[NORMATIVO]:** em todas as três, a migração é **aditiva e versionada**; o `gabarito-interno` original e seu snapshot `seed-MVP` permanecem arquivados; nenhuma cena é declarada `publicável` sem `PublicationDecision` com `gatingReason` e sem todos os portões satisfeitos.

---

## 13. Lotes de povoamento pós-MVP

Esta seção define uma **estratégia de povoamento progressivo** — a ordem em que o pipeline (Seção 5) é aplicado a escopos cada vez maiores — **não** uma lista de itens a criar. Cada lote é um **escopo** cujo `populationStatus` (Seção 4.7) evolui sob critérios de aceite verificáveis. **[NORMATIVO]:** a ordem dos lotes herda a prioridade P0–P3 das camadas (Etapa 4A) e **nenhum** lote avança sem que os testes de invariante (Seção 14) e seus próprios critérios de aceite passem; expansão sem prioridade é barrada (R-13.31). Os números abaixo dimensionam **esforço e ordem**, jamais "quantos fatos criar de uma vez" (R-13.01).

### 13.1 `P0-canonical-scenes` — consolidar o gabarito como canônico

- **Objetivo:** transformar as três cenas-gabarito do MVP em conteúdo canônico auditável (Seção 12), estabelecendo o padrão de qualidade que todos os lotes seguintes copiam.
- **Conteúdo incluído:** as três cenas (1789, GOE, K-Pg); seus claims fonteados; geometrias e mídia reais que substituem *placeholders*; reconfirmações dos cinco eixos (§12.3).
- **Fontes prioritárias:** as já auditadas (Etapa 1) por área — históricas A/B para 1789; ICS/PBDB/literatura revisada para GOE e K-Pg; Natural Earth (PD) como base; GPlates/EarthByte (atribuição/isolamento) para paleoposições.
- **Dependências:** Seções 1–12 inteiras (é a primeira aplicação real do pipeline).
- **Riscos:** placeholders virando final (R-13.18); ids duplicados na migração (R-13.19); tema sensível de 1789 sem revisão (R-13.16); falsa precisão em tempo profundo (R-13.11).
- **Critérios de aceite:** três cenas com `PublicationDecision` e `gatingReason`; 1 claim por fato; licenças resolvidas; auditoria seed→canônico contínua; nenhum invariante violado.
- **Quando avança:** quando as três cenas estão `production-populated` no seu escopo e servem de gabarito replicável.
- **Quando bloqueia:** qualquer reconfirmação reprovada, qualquer placeholder não substituível, qualquer claim sem fonte A/B.

### 13.2 `P1-time-spine` — espinha temporal canônica

- **Objetivo:** povoar a **estrutura do tempo** (Etapa 3Z) — os marcos e faixas que ancoram o eixo `canonicalTimeScalar` —, garantindo que todo lote futuro tenha onde se pendurar no tempo.
- **Conteúdo incluído:** marcos cronoestratigráficos (éons/eras/períodos), datums e conversões dos sete regimes, faixas de referência (Big Bang ~13,8 Ga; formação da Terra ~4,54 Ga; etc.), como **referências de eixo**, não como narrativa.
- **Fontes prioritárias:** ICS (escala cronoestratigráfica como **fato**; o gráfico oficial **não** entra como expressão — Etapa 1.1, caso ICS); literatura de cosmologia/geocronologia A.
- **Dependências:** P0 (padrão de qualidade); Etapa 3Z.
- **Riscos:** tempo mal normalizado (R-13.11); radiocarbono cru (Etapa 3Z); ano-zero astronômico (regime 5); falsa precisão (R-13.10).
- **Critérios de aceite:** cada marco com `sourceTimeBasis` preservado, conversão documentada (`conversionMethod`/`conversionNotes`) e incerteza tipada; nenhuma data cravada onde a fonte dá faixa.
- **Quando avança:** quando o eixo cobre do regime 1 ao 7 com marcos canônicos suficientes para datar os demais lotes.
- **Quando bloqueia:** conversão não auditável; reuso do gráfico ICS como imagem; precisão inventada.

### 13.3 `P1-source-spine` — espinha de fontes e licenças

- **Objetivo:** povoar o **catálogo curado de fontes** (a camada 25 e o registro da Etapa 1) com `Source`/`DatasetSnapshot`/`LicenseProfile` revalidados, para que os lotes de conteúdo apenas **liguem** claims a fontes já aprovadas.
- **Conteúdo incluído:** registros de fonte (`SourceIntakeRecord`), snapshots (`DatasetSnapshotRecord`), telas de licença (`LicenseScreeningRecord`) das fontes A/B prioritárias de cada área (Seção 7).
- **Fontes prioritárias:** todas as auditadas na Etapa 1 com decisão `AUTO`/`ATRIB`/`FATO`/`ISOLA`; NASA, Macrostrat, PBDB, Natural Earth, geoBoundaries, IBGE, OWID, etc., cada uma na partição correta.
- **Dependências:** P0; Etapas 1/1.1; §8/§9.
- **Riscos:** licença ausente (R-13.04); SA/ODbL no núcleo (R-13.06); fonte viva muda (R-13.32); fonte sai do ar (R-13.33); snapshot ausente (R-13.07).
- **Critérios de aceite:** cada fonte com `licenseRiskLevel`, partição física, atribuição (quando exigida) e snapshot com `checksum` e `retrievedAt`; isolados fisicamente separados.
- **Quando avança:** quando as fontes A/B das áreas P0/P1 estão catalogadas e licenciadas.
- **Quando bloqueia:** qualquer fonte sem `LicenseProfile` ou snapshot; qualquer tentativa de catalogar fonte C como autoridade (R-13.02).

### 13.4 `P1-geospatial-spine` — espinha geoespacial

- **Objetivo:** povoar a **base de lugares e geometrias** (Etapa 4H) — `Place`/`Region`/`GeometryVersion` modernas, históricas e paleogeográficas — para que itens localizáveis tenham onde se ancorar no espaço.
- **Conteúdo incluído:** geometrias modernas (base), versões históricas documentadas e paleoposições rotuladas, cada uma com `geometryStatus`, `SpatialUncertainty`, `paleogeographicModel` e licença/partição.
- **Fontes prioritárias:** Natural Earth (PD, base moderna `AUTO`); geoBoundaries (atribuição); GPlates/EarthByte (paleoposições, atribuição/isolamento); IBGE (Brasil, atribuição). GADM/OSM/MapBiomas tratados conforme sua decisão (`NAO`/`ISOLA`).
- **Dependências:** P0; P1-source-spine; §8/§11.5–§11.7.
- **Riscos:** geometrias proprietárias no núcleo (R-13.17); paleoposição como localização atual (R-13.12); `ModernCorrespondence` anacrônico (R-13.13); anacronismo espacial (R-13.13).
- **Critérios de aceite:** toda geometria com `geometryStatus` e licença; paleoposições sempre rotuladas e incertas; `modernCorrespondence` sem projetar realidade atual ao passado; isolados separados.
- **Quando avança:** quando as geometrias-base dos escopos P0/P1 estão disponíveis e rotuladas.
- **Quando bloqueia:** geometria sem licença/status (T-13.13); paleoposição tratada como coordenada moderna.

### 13.5 `P1-Brazil-lens` — lente Brasil

- **Objetivo:** povoar o recorte **Brasil** (camada 20) e os correlatos das Leis 10.639/2003 e 11.645/2008 com profundidade e cuidado de tema sensível, por ser eixo de valor do produto e da conformidade (Etapa 6).
- **Conteúdo incluído:** geografia histórica do Brasil, marcos e processos com fonte A/B, lente `modernCorrespondence` (territórios coloniais → unidades atuais), história indígena e afro-brasileira como **cobertura estrutural** (não apêndice).
- **Fontes prioritárias:** IBGE (atribuição); historiografia A/B; fontes A sobre história indígena e africana/diáspora (Seção 7.9–7.10). **BNCC nunca é fonte factual** (princípio/limite; R-13.28) — ela anota currículo na Etapa 6, não afirma fato.
- **Dependências:** P0; P1-source/geospatial-spine; Etapas 3.1/6.
- **Riscos:** conteúdo sensível sem revisão (R-13.16); colonização/escravidão achatadas (R-13.14); negacionismo histórico como "lado" (R-13.15); BNCC como fonte (R-13.28).
- **Critérios de aceite:** temas sensíveis com revisão humana obrigatória concluída (`pending`→liberado); controvérsias legítimas em `ClaimSet`; Leis 10.639/11.645 cobertas estruturalmente; nenhuma fonte BNCC sustentando claim.
- **Quando avança:** quando o recorte Brasil cobre os marcos curriculares estruturais com revisão sensível concluída.
- **Quando bloqueia:** qualquer tema sensível publicado sem revisão; qualquer achatamento de controvérsia legítima.

### 13.6 `P1-deep-time-spine` — espinha de tempo profundo

- **Objetivo:** povoar **cosmologia, geologia, paleogeografia, paleobiologia e extinções** (camadas 1–9) — o arco do Big Bang à vida — como inferência científica tipada, ancorado em P1-time-spine.
- **Conteúdo incluído:** processos e estados de tempo profundo (formação estelar/planetária, tectônica, atmosfera/clima, origem e diversificação da vida, grandes extinções), sempre com `claimType` de inferência/reconstrução e incerteza alta.
- **Fontes prioritárias:** NASA (`AUTO`); Macrostrat (atribuição); PBDB (atribuição); ICS (fato); GPlates/EarthByte (paleoposições); literatura A revisada.
- **Dependências:** P0; P1-time/source/geospatial-spine; §10/§11.
- **Riscos:** falsa precisão em datas profundas (R-13.10/R-13.11); paleoposição como atual (R-13.12); hipóteses concorrentes achatadas (R-13.14); IA "preenchendo" lacunas (R-13.03).
- **Critérios de aceite:** datas como faixas quando a fonte assim dá; `UncertaintyProfile` coerente; hipóteses concorrentes em `ClaimSet` com pesos; paleoposições rotuladas.
- **Quando avança:** quando o arco profundo cobre os marcos P0/P1 com tipagem e incerteza corretas.
- **Quando bloqueia:** data cravada sem base; inferência exibida como medição direta; paleoposição não rotulada.

### 13.7 `P2-curricular-expansion` — expansão curricular

- **Objetivo:** ampliar a cobertura de história humana, ciência, cultura e economia (camadas 10–23) para além dos marcos P1, alinhando-se à utilidade escolar **sem** tratar BNCC como fonte e **sem** mapear BNCC em massa (limites; R-13.27/R-13.28).
- **Conteúdo incluído:** mais eventos/processos/conceitos com fonte A/B, em profundidade crescente por tema, priorizando o que conecta às cenas e momentos já cobertos.
- **Fontes prioritárias:** historiografia e ciência A/B por área (Seção 7); OWID (atribuição) para séries socioeconômicas.
- **Dependências:** todos os P1.
- **Riscos:** ingestão criar currículo (R-13.27); BNCC como fonte (R-13.28); expansão sem prioridade (R-13.31); revisão superficial sob volume (R-13.21); pipeline virando gargalo (R-13.23).
- **Critérios de aceite:** cada item fonteado, tipado, datado, localizado e revisado no mesmo padrão de P0; nenhuma escrita em camadas de currículo/Output/UX; prioridade explícita por tema.
- **Quando avança:** por tema, quando o subescopo atinge `production-populated` sob critérios próprios.
- **Quando bloqueia:** volume comprometendo profundidade de revisão; tentativa de derivar currículo a partir da ingestão.

### 13.8 `P2-media-assets` — acervo de mídia

- **Objetivo:** povoar a camada de **mídia e acervos** (camada 24) com `MediaAsset`/`MapAsset` reais, licenciados e isolados conforme risco, substituindo todo *placeholder* remanescente.
- **Conteúdo incluído:** imagens, ilustrações, reconstruções, mapas — cada um com `AssetIntakeRecord` completo e `perAssetConfirmed` quando risco 2.
- **Fontes prioritárias:** acervos PD/CC0 (`AUTO`); Wikimedia Commons (por item; risco 2, `perAssetConfirmed`); NASA (`AUTO`); coleções com atribuição. NC **nunca** entra como expressão (R-13.05); SA/ODbL **isolado** (R-13.06).
- **Dependências:** P0; P1-source-spine; §8.
- **Riscos:** NC reproduzido (R-13.05); SA/ODbL contaminando núcleo (R-13.06); asset sem licença (R-13.04); placeholder virando final (R-13.18); arte tratada como evidência (R-13.15 correlato).
- **Critérios de aceite:** todo asset com `LicenseProfile`, partição correta e atribuição; risco 2 com confirmação por item; arte rotulada `representação artística`; exportação herda licença.
- **Quando avança:** quando os escopos publicáveis têm mídia real licenciada e nenhum placeholder ativo.
- **Quando bloqueia:** qualquer asset sem confirmação de licença; qualquer NC como expressão; qualquer SA/ODbL no núcleo.

### 13.9 `P3-scale` — escala

- **Objetivo:** escalar a cobertura (mais áreas, mais profundidade, mais recortes regionais/temporais) **somente depois** de a espinha (P1) e os padrões (P0/P2) estarem sólidos, preservando todos os invariantes sob volume.
- **Conteúdo incluído:** expansão ampla e contínua, governada pelos mesmos portões, com lotes temáticos menores herdando os critérios de P0–P2.
- **Fontes prioritárias:** as mesmas, ampliadas por novas fontes que **passem** pela Etapa 1/1.1 antes de uso.
- **Dependências:** P0, todos os P1, P2.
- **Riscos:** ingestão em massa sem curadoria (R-13.01); pipeline virando gargalo (R-13.23); auditoria incompleta sob volume (R-13.24); performance do MVP/núcleo degradada (R-13.29/R-13.30); pressão comercial por velocidade (R-13.35).
- **Critérios de aceite:** throughput sem queda de qualidade de revisão; auditoria completa mantida; performance dentro dos limites da Etapa 11; nenhum invariante relaxado por escala.
- **Quando avança:** continuamente, escopo a escopo, enquanto os critérios se sustentam.
- **Quando bloqueia:** qualquer sinal de revisão superficial, auditoria incompleta ou invariante cedido para ganhar velocidade — escala **pausa** antes de baixar o piso (degradação nunca remove o piso epistêmico).

### 13.10 Regra de sequenciamento

**[NORMATIVO]** os lotes formam um **grafo de dependências**, não uma esteira rígida: P0 precede tudo; as quatro espinhas P1 (time, source, geospatial, deep-time) e a lente Brasil podem progredir em paralelo **desde que** P1-source-spine sustente cada claim e P1-time/geospatial-spine ancorem tempo/espaço; P2 (curricular, media) depende das espinhas; P3 depende de P0–P2 consolidados. Em qualquer ponto, a falha de um teste de invariante (Seção 14) **rebaixa** o `populationStatus` do escopo afetado e bloqueia sua promoção até a correção (versionada — §9), nunca por apagamento.

---

## 14. QA, testes e riscos da ingestão

Esta seção define a **matriz de QA** do pipeline (testes de invariante que **bloqueiam** escrita/publicação quando falham) e o **registro de riscos** da Etapa 13 com mitigação. **[NORMATIVO]:** os testes desta seção são condição de promoção de `ingestionStatus`/`populationStatus` (Seções 4 e 13); falha em qualquer teste de invariante **barra** a transição e devolve o item ao estado seguro (`needs-rework`/`blocked-license`/`legal-review`), nunca por apagamento (§9). Os testes estendem os testes `T-*` do MVP (Etapa 12, §14) e os invariantes técnicos da Etapa 11; não os substituem.

### 14.1 Matriz de testes de invariante (`T-13.NN`)

| ID | O que valida | Cenário/gatilho | Resultado esperado | Base |
|---|---|---|---|---|
| **T-13.01** | Claim sem fonte A/B é barrado | tentativa de `claim-drafted → approved-for-kc` com `provenanceRef` ausente ou `sourceTier = C`/índice | bloqueio; `needs-rework`; `gatingReason = "fonte A/B ausente"` | Etapa 1 (A/B); princípio 1 |
| **T-13.02** | Wikipedia/Wikidata como autoridade é barrado | claim cuja única proveniência é Wikipedia/Wikidata (`INDX`) | bloqueio; aceito só como pista para buscar fonte A/B | princípio 2; Etapa 1.1 (`INDX`) |
| **T-13.03** | IA como fonte é barrada | claim cujo `provenanceRef` é saída de IA/modelo | bloqueio; IA não recebe `sourceTier`; rascunho herda `pending` | invariante 13; princípio 3 |
| **T-13.04** | NC como expressão é barrado | asset/expressão com `licenseRiskLevel = 4` (NC) tentando `→ published` como expressão | `blocked-license`; só o fato re-derivado entra | Etapa 1.1 (risco 4); §8.10; princípio 6 |
| **T-13.05** | SA/ODbL é isolado | fonte/asset SA/ODbL (`licenseRiskLevel = 3`) tentando entrar no `core-store` | redirecionado a `isolated-license-store`; núcleo permanece limpo | invariante 18; §8.11; princípio 7 |
| **T-13.06** | Asset sem licença é barrado | `AssetIntakeRecord` sem `LicenseProfile`, ou risco 2 sem `perAssetConfirmed` | não servido; `pending`/`blocked-license` | invariante 9; §8.9; princípio 13 |
| **T-13.07** | Claim sem `claimType` é barrado | `metadata-complete` sem `claimType` | bloqueio; `needs-rework` | Etapa 2; princípio 9 |
| **T-13.08** | Claim sem `confidenceLevel` é barrado | `metadata-complete` sem `confidenceLevel`/`evidenceLevel`/`UncertaintyProfile` | bloqueio; `needs-rework` | Etapa 2; princípio 9 |
| **T-13.09** | Claim sem `reviewStatus` é barrado | item nascendo sem `reviewStatus` | bloqueio; todo item nasce com `reviewStatus` (default `pending`) | invariante 9; princípio 10 |
| **T-13.10** | Controvérsia sem `ClaimSet` é barrada | controvérsia legítima representada como claim único "verdadeiro" | bloqueio; exige `ClaimSet`/`weightedClaimSets` | Etapa 3.1; princípio 17 |
| **T-13.11** | Negacionismo como claim concorrente é barrado | negacionismo/desinformação inserido como "lado" de um `ClaimSet` | bloqueio; só como objeto `rotulado-rejeitado` **fora** do `ClaimSet` | Etapa 3.1; princípio 18 |
| **T-13.12** | Tempo sem `sourceTimeBasis` é barrado | `TimeRange` derivado sem `sourceTimeBasis` preservado | bloqueio; `PENDENTE_DATA` | invariante 29; Etapa 3Z; princípio 15 |
| **T-13.13** | Geometria sem licença/status é barrada | `GeometryVersion` sem `geometryStatus` ou sem `licenseProfileRef` | bloqueio; `PENDENTE_GEOMETRIA` | Etapa 4H; §11.6; princípio 14 |
| **T-13.14** | `pending` não é exibível | item `pending`/`legal-review`/`rejected` aparecendo em vista/cache/índice/export/offline | não exibido como fato em nenhum caminho | invariante 9/27; princípio 11 |
| **T-13.15** | Snapshot é imutável | tentativa de editar um `DatasetSnapshot` existente | rejeitada; correção cria **novo** snapshot/versão | §9.1; invariante 28; princípio 12 |
| **T-13.16** | Depreciação não apaga versão anterior | `deprecated` removendo a versão anterior | versão anterior permanece auditável; só sai de exibição | §9.10; invariante 29 |
| **T-13.17** | Exportação herda licença | export/offline de item isolado/NC/atribuído sem herdar política | herda `LicenseProfile`/atribuição; isolados não vão para pacote aberto | invariante 27; §8.12 |
| **T-13.18** | Cache/índice invalidado após aprovação/rejeição | `approved-for-kc`/`rejected`/`deprecated` sem disparar invalidação de derivados | `InvalidationRule` dispara; cache/índice reconstruído | invariantes 2/3; etapa 20 do fluxo |
| **T-13.19** | Seed não é confundido com ingestão | item só com marca `seed-MVP` contado/exibido como ingerido | bloqueio; exige reingestão pela Seção 5 (Seção 12) | princípio 28; §12.1 |
| **T-13.20** | De-duplicação na migração | dois claims "iguais" para o mesmo referente (seed + canônico) | versiona o existente (`supersedes`); 1 claim por fato | §12.5; R-13.19 |
| **T-13.21** | Placeholder não vira final sem asset | *placeholder* publicado como definitivo sem `AssetIntakeRecord`/`perAssetConfirmed` | bloqueio; `PENDENTE_LICENCA`/`PENDENTE_GEOMETRIA` | §12.8; R-13.18 |
| **T-13.22** | Revisão dentro de competência | aprovação por papel fora de sua competência (Seção 3.2) | rejeitada; exige o papel correto; "negar vence" | §3.2; R-13.22 |
| **T-13.23** | Paleoposição ≠ coordenada moderna | marcador de tempo profundo usando coordenada moderna como posição | bloqueio; exige `paleoPositions` rotuladas + `AnachronismNotice` | §11.7; R-13.12 |
| **T-13.24** | Relação com proveniência | `Relationship` (causal/temporal/espacial) sem `provenanceRef` | bloqueio; relação herda exigência de proveniência | §6.7; R-13.20 |

**[NORMATIVO]:** nenhum desses testes é destravado por urgência, intenção declarada, autoridade alegada ou pressão comercial (princípios 5–7; R-13.35). Um teste reprovado **rebaixa** o `populationStatus` do escopo (§13.10).

### 14.2 Registro de riscos da Etapa 13 (`R-13.NN`)

Trinta e oito riscos específicos da ingestão, cada um com mitigação ancorada nas seções acima. Os riscos não se substituem aos da Etapa 11 (`R-NN`) nem aos do MVP (`R-MVP-NN`); o prefixo `R-13.` os mantém distintos.

| ID | Risco | Impacto | Mitigação |
|---|---|---|---|
| **R-13.01** | Ingestão em massa sem curadoria | grafo inflado com fatos não revisados; piso epistêmico cai | fluxo de 20 etapas obrigatório; sem caminho automático a `published`; volume pausa antes de baixar revisão (§5, §13.9) |
| **R-13.02** | Fonte C virando autoridade | claim sustentado por fonte fraca | `T-13.01`/`T-13.02`; C só `INDX`; `sourceTier` checado na revisão (§7, §3) |
| **R-13.03** | IA virando fonte factual | alucinação tratada como fato | `T-13.03`; invariante 13; IA só auxilia forma/triagem, rascunho herda `pending` (§5.3, §10.8) |
| **R-13.04** | Licença ausente | uso ilícito de expressão/asset | `T-13.06`; `LicenseScreeningRecord` obrigatório; default não entra; `legal-review` (§8, §6.3) |
| **R-13.05** | Asset NC reproduzido | violação de licença NC | `T-13.04`; NC nunca como expressão; só fato re-derivado (§8.10) |
| **R-13.06** | SA/ODbL contaminando o núcleo | contaminação viral do `core-store` | `T-13.05`; isolamento físico em `isolated-license-store`; exportação separada (§8.11, invariante 18) |
| **R-13.07** | Snapshot ausente | proveniência irreconstruível | `T-13.15`; snapshot obrigatório antes de extrair claims; `checksum`+`retrievedAt` (§9.1–§9.4) |
| **R-13.08** | Claim sem granularidade | claim composto/vago não verificável | claim atômico; granularidade ruim → `needs-rework` (§10.1) |
| **R-13.09** | Claim copiando texto protegido | reprodução de expressão | re-codificação obrigatória (§10.8); citação aponta ao `locator`, não reproduz; revisão editorial |
| **R-13.10** | Claim sem incerteza | falsa precisão | `T-13.08`; `confidenceLevel`/`evidenceLevel`/`UncertaintyProfile` obrigatórios; faixa quando a fonte dá faixa (§10.4, §11.2) |
| **R-13.11** | Tempo mal normalizado | data errada/anacrônica no eixo | `T-13.12`; conversão documentada (`conversionMethod`/`conversionNotes`); radiocarbono calibrado; offset só regimes 4–5 (§11.1–§11.2) |
| **R-13.12** | Paleoposição como localização atual | "México em 66 Ma" tratado como real | `T-13.23`; paleoposição rotulada; `AnachronismNotice`; usuário vê a geometria em uso (§11.5–§11.7) |
| **R-13.13** | `ModernCorrespondence` anacrônico | projeção da realidade atual ao passado | lente "o que hoje é…" rotulada; não projeta nação/fronteira atual ao passado (§11.5) |
| **R-13.14** | Controvérsia achatada | consenso falso; pluralismo perdido | `T-13.10`; controvérsia legítima → `ClaimSet`/`weightedClaimSets`; revisão científica/editorial (§10.5, Etapa 3.1) |
| **R-13.15** | Negacionismo tratado como lado | falsa equivalência | `T-13.11`; negacionismo só `rotulado-rejeitado` fora do `ClaimSet`; anti-falsa-equivalência (Etapa 3.1/5) |
| **R-13.16** | Conteúdo sensível sem revisão | dano editorial; descumprir Leis 10.639/11.645 | revisão humana obrigatória; nasce `pending`; `editorialReviewer`/`historicalReviewer` (§3, §10.7, requisito 25) |
| **R-13.17** | Geometrias proprietárias no núcleo | licença violada | `T-13.13`; GADM/OSM/MapBiomas tratados por decisão (`NAO`/`ISOLA`); licença/partição por geometria (§8, §11.6) |
| **R-13.18** | Placeholders virando final | demonstração exibida como conteúdo real | `T-13.21`; substituição por asset com `perAssetConfirmed`; senão `PENDENTE_*` não exibível (§12.8) |
| **R-13.19** | Ids duplicados | grafo fragmentado; ponteiros órfãos | `T-13.20`; ids estáveis preservados; versionar em vez de recriar; checagem de identidade (§12.4–§12.5) |
| **R-13.20** | Relação sem proveniência | aresta causal/temporal não auditável | `T-13.24`; `RelationshipDraft` exige `provenanceRef`; revisão (§6.7) |
| **R-13.21** | Revisão humana superficial | aprovação de baixa qualidade sob volume | `ReviewDecision` com `gatingReason`; competência por papel; amostragem/auditoria de revisões (§3, §9.11, §13.9) |
| **R-13.22** | Curador aprovando fora de competência | decisão sem qualificação | `T-13.22`; matriz de competência (§3.2); "negar vence"; escalonamento obrigatório |
| **R-13.23** | Pipeline virando gargalo | povoamento trava | filas por estado; paralelismo entre lotes independentes (§13.10); IA auxilia triagem (não decisão); priorização P0–P3 |
| **R-13.24** | Auditoria incompleta | rastreabilidade quebrada | `IngestionAuditTrail` por transição; cadeia artefato→…→licença (Etapa 11); auditoria é critério de aceite (§9, §13.9) |
| **R-13.25** | Cache não invalidado | derivado servindo fato revogado | `T-13.18`; `InvalidationRule` na etapa 20; cache carrega versões de origem; `cache não é verdade` (§5.1, invariante 2) |
| **R-13.26** | Output usando item ainda `pending` | camada externa exibindo não-fato | invariante 9/27; Output/UX/Matching só leem itens publicáveis; fronteiras de escrita (Etapa 11) |
| **R-13.27** | Ingestão criar currículo | confundir núcleo com BNCC/Planning | ingestão não escreve em currículo/Output/UX; BNCC anota na Etapa 6, não no pipeline (§1.2, limites) |
| **R-13.28** | BNCC usada como fonte factual | currículo tratado como autoridade de fato | BNCC nunca é `Source` A/B; `AUTO` apenas como documento curricular na Etapa 6 (§7.8, §13.5) |
| **R-13.29** | Ingestão quebrar o MVP | regressão nas três cenas | migração aditiva/versionada; cenas-gabarito inalteradas; testes `T-*` do MVP mantidos (§12, Etapa 12) |
| **R-13.30** | Ingestão quebrar performance | núcleo/derivados lentos sob volume | derivados reconstruíveis; orçamentos de performance da Etapa 11; `P3-scale` pausa se degradar (§13.9) |
| **R-13.31** | Expansão sem prioridade | esforço disperso; lacunas estruturais | lotes P0–P3 com dependências (§13); prioridade herdada da Etapa 4A; sequenciamento (§13.10) |
| **R-13.32** | Fonte viva muda | claim referenciando estado inexistente | snapshot datado + `checksum`; nova versão de `Source` ao mudar; claim aponta à versão usada (§9.5, §9.7) |
| **R-13.33** | Fonte sai do ar | proveniência inacessível | snapshot preservado como prova; `sourceAvailability` marcado; claim sobrevive na versão snapshotada (§9.6) |
| **R-13.34** | Tradução/adaptação altera o fato | erro factual introduzido ao adaptar forma | `forma muda; fato não`; adaptação muda só a forma; revisão confirma equivalência factual (§10.8, invariante 14) |
| **R-13.35** | Pressão comercial para publicar rápido | portões burlados por prazo | nenhum portão destravado por urgência/pressão; `legal-review` default não publica; promoção exige testes (§4.5, §8, §13.9) |
| **R-13.36** | Busca/embedding tratada como verdade | ponteiro confundido com fato | `busca/embedding não é verdade`; `carriesProvenance = false`; resposta reidrata o claim e seus rótulos (§1.4, invariante 3) |
| **R-13.37** | Depreciação excessiva apagando trilha | histórico perdido por "limpeza" | depreciar nunca apaga (§9.10); `T-13.16`; versões e snapshots permanecem recuperáveis |
| **R-13.38** | PII de aluno entrando pela ingestão | violação de LGPD/ECA | papéis de ingestão não operam com PII de aluno (§3); minimização máxima (Etapa 11); pipeline não coleta dado pessoal (limite) |

**[NORMATIVO]:** este registro é **vinculante** para a Etapa 14; cada risco tem teste, portão ou invariante associado, e a operação monitora os indicadores correspondentes (§15).

---

## 15. Encerramento e handoff para a Etapa 14

### 15.1 O que a Etapa 13 entrega

A Etapa 13 entrega o **`IngestionPopulationPipeline` completo em nível de arquitetura operacional**: a entidade conceitual do pipeline e sua relação com as Etapas 1/1.1/2/11/12 (Seção 1); 28 princípios de ingestão vinculantes (Seção 2); 10 papéis humanos de curadoria/revisão com competências e matriz de aprovação (Seção 3); os enums `ingestionStatus` e `populationStatus` com transições permitidas/proibidas e gatilhos de revisão/licença/fonte (Seção 4); o fluxo ponta a ponta de 20 etapas com entradas/saídas/responsáveis/bloqueios/artefatos/riscos (Seção 5); 12 templates conceituais de ingestão (Seção 6); a política de fontes A/B/C por 14 áreas/camadas (Seção 7); a aplicação operacional de licenças e isolamento físico, risco 0–5 (Seção 8); as regras de proveniência, snapshot e versionamento, com a regra de que correção cria versão e não apaga (Seção 9); as regras de extração/tipagem/re-codificação de claims (Seção 10); a normalização temporal e geoespacial com exemplos conceituais 1789/GOE/K-Pg (Seção 11); o plano de migração do seed do MVP para canônico, com tabela das três cenas (Seção 12); a estratégia de povoamento em nove lotes P0–P3 com critérios de aceite (Seção 13); e a matriz de QA (24 testes de invariante) com registro de 38 riscos (Seção 14).

### 15.2 O que a Etapa 13 **não** entrega

A Etapa 13 **não** entrega: código, API real, scraping real, downloads reais, banco real ou ingestão executada; conteúdo factual novo (nenhum claim foi criado — apenas o processo que os criará); milhares de itens povoados; alteração das cenas-gabarito; mapeamento de BNCC em massa ou tratamento de BNCC como fonte; coleta de PII de aluno; *analytics* operacional, LMS ou validação escolar/jurídica/comercial executada; e qualquer promessa de homologação MEC/PNLD. Esses itens ou são proibidos por natureza ou pertencem à Etapa 14 e à execução.

### 15.3 Invariantes que passam a ser vinculantes

A partir desta entrega, vinculam a operação (somando-se aos 30 invariantes da Etapa 11 e aos testes do MVP): **(i)** a ingestão é o único caminho de escrita factual (Seção 1); **(ii)** os 28 princípios da Seção 2; **(iii)** os 24 testes de invariante `T-13.NN` (Seção 14.1) como condição de promoção de estado; **(iv)** os portões de licença/fonte/revisão das Seções 3–8; **(v)** a regra de versionamento sem apagamento (Seção 9); **(vi)** a re-codificação obrigatória sem cópia de expressão (Seção 10.8); **(vii)** a preservação de `sourceTimeBasis` e a rotulagem de paleoposição/anacronismo (Seção 11); **(viii)** a migração aditiva e versionada do seed (Seção 12); **(ix)** o sequenciamento de lotes e o rebaixamento de `populationStatus` sob falha (Seção 13). Permanecem canônicas: **forma muda; fato não**; **score/cache/busca/embedding não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**.

### 15.4 Estados e templates que ficam oficiais

Ficam oficiais e estáveis para a Etapa 14: os enums `ingestionStatus` (14 valores) e `populationStatus` (6 valores) da Seção 4; os 12 templates da Seção 6 (`SourceIntakeRecord`, `DatasetSnapshotRecord`, `LicenseScreeningRecord`, `ClaimDraft`, `KnowledgeItemDraft`, `CitationRecord`, `RelationshipDraft`, `ClaimSetDraft`, `GeometryDraft`, `AssetIntakeRecord`, `ReviewDecision`, `PublicationDecision`); a entidade `IngestionPopulationPipeline` (Seção 1.6) e a `IngestionAuditTrail` (Seção 9). Alterá-los exige reabrir a Etapa 13.

### 15.5 Como a Etapa 14 deve usar o pipeline

A Etapa 14 (operação) opera **sobre** este pipeline sem reabrir suas fronteiras:

- **QA contínuo:** executa a matriz `T-13.NN` como portão automatizado de promoção; trata falha como bloqueio versionado, não apagamento.
- **Governança:** instrumenta os papéis da Seção 3 (turnos, fila, escalonamento, auditoria de revisões); aplica "negar vence"; mantém a matriz de competência.
- **Escala:** conduz `P3-scale` (Seção 13.9) com os mesmos portões; pausa antes de baixar o piso; respeita os orçamentos de performance da Etapa 11.
- **Analytics agregado:** mede **throughput, taxa de bloqueio, lead time por estado, cobertura por camada/lote** — sempre agregado e sem PII de aluno (minimização máxima); analytics é **observação da operação**, nunca fonte factual nem caminho de escrita no KC.
- **LMS e validação escolar/jurídica/comercial:** integra-se como **consumidor** do conteúdo publicável (lê itens `published`, respeita licença/atribuição/exportação), nunca como escritor de `Claim`/`Source`/`reviewStatus`; validação escolar/jurídica/comercial usa o conteúdo já curado, sem destravar portões.

### 15.6 O que a operação deve monitorar

**[NORMATIVO]** indicadores mínimos: itens por `ingestionStatus`/`populationStatus`; taxa de bloqueio por motivo (`gatingReason`); itens em `legal-review`/`blocked-license` e tempo de permanência; cobertura de snapshot e integridade de `checksum`; fontes vivas alteradas e fontes fora do ar (§9.5–§9.6); proporção de revisões escaladas e amostragem de qualidade de revisão (R-13.21); placeholders ativos remanescentes (§12.8); invalidação de cache/índice pós-decisão (T-13.18); e qualquer tentativa de escrita por camada não autorizada (fronteiras da Etapa 11).

### 15.7 Papéis humanos que precisam existir

Para operar, devem existir de fato (não apenas no papel): `sourceScout`, `ingestionCurator`, `licenseReviewer`, `scientificReviewer`, `historicalReviewer`, `editorialReviewer`, `legalReviewer`, `geoTemporalReviewer`, `accessibilityReviewer` e `pipelineAdmin` (Seção 3), acoplados aos papéis técnicos/curatoriais da Etapa 11 (§7.2) e estritamente separados dos papéis escolares (sem PII de aluno).

### 15.8 Pendências que seguem abertas

**[PENDÊNCIA]** para a Etapa 14/execução: calendários não-ocidentais como `sourceTimeBasis` adicionais (§11.4; Etapa 3Z); instrumentação concreta de filas, SLAs e ferramentas de revisão (tecnologias permanecem **[RECOMENDADO]**/**[ALTERNATIVA]**); definição operacional dos limiares de amostragem de auditoria de revisão (R-13.21); políticas finas de retenção/arquivamento de snapshots sob custo de armazenamento; e a expansão das fontes A/B por área conforme novos domínios entrem (cada nova fonte passa pela Etapa 1/1.1 antes de uso).

### 15.9 Critérios que autorizam passar para operação

A operação (Etapa 14) é autorizada quando: as três cenas-gabarito estão migradas a canônico sob `P0-canonical-scenes` (Seção 12/13.1); a matriz `T-13.NN` está implementada como portão e passa para o conteúdo P0; os 10 papéis existem e operam com competência e escalonamento; as quatro espinhas P1 têm critérios de aceite definidos e ao menos `pilot-populated`; o isolamento físico e a herança de licença em exportação/offline estão verificados (T-13.05/T-13.17); e a auditoria seed→canônico é contínua e recuperável.

### 15.10 Critérios que bloqueiam a operação

A operação é **bloqueada** enquanto: existir caminho de escrita factual fora do pipeline (fronteiras da Etapa 11 violadas); qualquer teste `T-13.NN` puder ser destravado por urgência/autoridade/pressão comercial (R-13.35); houver claim sem fonte A/B, sem tipagem, sem `reviewStatus` ou sem proveniência exibível como fato (T-13.01/07/08/09/14); houver NC como expressão ou SA/ODbL no núcleo (T-13.04/05); houver snapshot ausente ou mutável (T-13.15); houver placeholder publicado como final (T-13.21); ou houver risco do registro (Seção 14.2) sem teste/portão/invariante associado e monitorado.

---

*Documento de entrega da Etapa 13 — Pipeline real de ingestão, curadoria e povoamento do Knowledge Core (v1.0). Define a arquitetura operacional pela qual o Atlas do Tempo 3D deixa de depender de três cenas seedadas e passa a povoar o Knowledge Core com dados reais, auditáveis, versionados e licenciados, sob proveniência, revisão humana, publicabilidade, privacidade e soberania do núcleo, sem permitir que fonte fraca, licença incompatível, IA, cache, busca ou automação se tornem verdade factual. Nenhum código foi escrito, nenhuma fonte foi baixada, nenhum banco foi povoado e nenhuma cena-gabarito foi alterada. Vincula as Etapas seguintes e entrega à Etapa 14 um pipeline pronto para operar QA, governança, escala, analytics agregado, LMS e validação escolar/jurídica/comercial sem quebrar o núcleo. Em caso de dúvida de fonte, licença, data, geometria ou tipo de claim, marca-se `PENDENTE_*` — nunca se inventa precisão.*
