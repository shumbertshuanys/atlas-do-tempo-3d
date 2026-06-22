# Etapa 10 — Design/UX 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 10** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8, v1.0) e a `PedagogicalOutputLayer` (Etapa 9, v1.0) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura conceitual de experiência e interação**. Define **somente a gramática da experiência/UX 3D** — os modos, vistas, estados de navegação, painéis, controles, rótulos, avisos, fluxos de revisão/aprovação/exportação, requisitos de acessibilidade, invariantes, fronteiras e riscos de **apresentar e operar** o que as camadas anteriores já decidiram. Conforme solicitado, esta etapa **não** desenha telas finais de alta fidelidade, layouts, componentes prontos nem fluxo concreto de implementação; **não** cria `Claim`, `Source`, `Citation`, `Scene`, `ClaimSet`, `Relationship`, `MomentResult` nem qualquer conhecimento do núcleo; **não** altera `reviewStatus`, `publicabilityStatus`, `publicabilityStatusRead`, `confidenceLevel`, `evidenceLevel`, `claimType`, `UncertaintyProfile`, `BNCCMapping`, `CurricularAlignment`, `PlanningProfile`, `ComplianceProfile`, `MatchScore`, `matchSetStatus`, `outputStatus` nem `sceneCompletenessLevel`; **não** reabre seleção, elegibilidade, conformidade, planejamento, forma do artefato nem verdade factual; **não** promove conteúdo `pending`/`legal-review`/`rejected`; **não** usa IA como fonte factual; **não** inventa fatos; **não** substitui o professor; **não** promete homologação MEC nem aprovação PNLD; **não** trata recurso complementar como currículo oficial; **não** define stack técnica, persistência, versionamento, APIs, cache/validade, permissões técnicas ou engenharia de privacidade (Etapa 11); **não** propõe MVP (Etapa 12); **não** faz ingestão/povoamento (Etapa 13); **não** define operação, governança, QA, escala, analytics ou LMS (Etapa 14); **não** define engine gráfica, biblioteca de timeline, motor 3D nem formato de arquivo; e **não** usa dados pessoais reais de alunos.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6). "O Planning" = a `TeacherSchoolPlanningLayer` (Etapa 7). "O Matching" = o `ContentMatchingEngine` (Etapa 8). "O Output" = a `PedagogicalOutputLayer` (Etapa 9). "A UX" = a `DesignUX3DLayer` definida na Seção 1.

> **Regra de fundação desta etapa.** A UX é **camada de apresentação e operação**, no topo da experiência, externa a tudo o que está a montante. Ela nunca cria, edita ou altera conhecimento; nunca reabre seleção, conformidade, planejamento, forma do artefato ou verdade; nunca relaxa rótulos epistêmicos, mediação ou visibilidade por papel. Ela consome o `PedagogicalOutput` (Etapa 9) e suas partes — `OutputArtifact`, `OutputSectionBlock`, `OutputCitationBundle`, `OutputComplianceSummary`, `OutputConstraintWarning`, `OutputAuditTrail` — além de `Scene` v1.1, `MomentResult` e referências ao KC, e os apresenta como **experiência navegável**, preservando integralmente os rótulos de tipo de claim, confiança, evidência, incerteza, anacronismo, equivalência, publicabilidade, gating, mediação e acessibilidade que já vieram decididos a montante. A direção única de dependência permanece invertida: **Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core**. A UX aponta para dentro; o Output, o Matching, o Planning, a Compliance e o KC nunca apontam para a UX (Etapa 2, §10; P1/P2).

---

## Sumário

1. Definição da `DesignUX3DLayer`
2. Papel da camada na arquitetura geral
3. Entradas da camada de UX
4. Entidades conceituais da camada
5. Modos de experiência
6. Timeline multiescala
7. Globo/mapa 3D e degradação para 2D/estático
8. Dossiês, cartões, fontes e evidência
9. Modos professor, estudante, projetor, offline e exploração livre
10. Revisão, edição, aprovação e exportação de artefatos
11. Visualização de incerteza, publicabilidade, gating, mediação e acessibilidade
12. Relação com `PedagogicalOutput`, `Scene` v1.1, `MomentResult` e `Knowledge Core`
13. Riscos de UX, educacionais, jurídicos, editoriais e operacionais
14. Fronteiras com as Etapas 11–14
15. Encerramento e handoff para a Etapa 11

---

## 1. Definição da `DesignUX3DLayer` (Tarefa 1)

### 1.1 Natureza

A **`DesignUX3DLayer`** é a **camada externa de experiência e interação** que **transforma um `PedagogicalOutput` revisado e conforme — o conjunto de artefatos da Etapa 9 — em uma experiência navegável que professor e estudante usam para visualizar, navegar, editar (a forma), aprovar e exportar** os artefatos pedagógicos, sempre apoiada em uma **timeline multiescala**, um **globo/mapa 3D** e um conjunto de painéis (dossiê, fonte/evidência), rótulos (epistêmicos, incerteza, gating) e controles (mediação, acessibilidade). Ela é a **dobradiça entre a forma e o uso**: o Output decide *em que forma pedagógica o conteúdo aparece*; a UX decide *como essa forma é apresentada, percorrida e operada* — sem nunca redecidir a forma, a seleção, a conformidade ou o fato.

Três consequências estruturais, herdadas das etapas anteriores:

1. **É de apresentação, não de conteúdo.** Diferente do KC (universal e estável — Etapa 2, §10.2) e até do Output (transformador de forma), a UX é puramente **a face navegável** do que já existe. Ela **nunca entra no núcleo nem reescreve o artefato**: vive por fora, como sessão e estado de visualização que **apontam para** o `PedagogicalOutput`, as cenas, os dossiês, os `MomentResult`, os claims e as fontes por identificador estável (P1/P2). Encerrar uma sessão de experiência não altera um único campo a montante.
2. **É contingente e descartável.** Uma `ExperienceSession` é sempre relativa a *um* `PedagogicalOutput`, *um* papel de quem visualiza (`ViewerRole`), *um* modo (`ExperienceMode`) e *um* perfil de acessibilidade. Removê-la não deixa rastro no Output, no Matching, no Planning, na Compliance ou no KC.
3. **É honesta por construção.** A UX **mostra** a honestidade epistêmica (PE-Ed1) em vez de escondê-la para "ficar bonita": rótulo de tipo de claim, confiança, evidência, fonte, incerteza, anacronismo, equivalência, gating e mediação acompanham o conteúdo em qualquer modo, com **redundância não-cromática** e **equivalente textual**.

### 1.2 As perguntas que a camada responde

- **Como** professor e estudante **veem** um artefato pedagógico (plano, dossiê, atividade, quiz, comparação, material do aluno) ancorado em tempo e espaço?
- **Como** a experiência **navega** por ano, período, evento, processo, State e região, preservando a **simultaneidade global** (D8)?
- **Como** o globo/mapa 3D **degrada** para 2D, estático, offline e projetor sem perder o **piso epistêmico**?
- **Como** a UI **apresenta fonte, evidência e incerteza** ("como sabemos isso") sem reproduzir indevidamente material (1.1)?
- **O que** o estudante vê, **o que** só o professor vê, **o que** exige mediação e **o que** nunca aparece ao aluno?
- **Como** o professor **revisa, edita a forma, comenta, aprova e exporta** um artefato, sem tocar claim, fonte, publicabilidade, gating, `MatchSet` ou conformidade?
- **Como** a experiência atende **acessibilidade** (e-MAG/WCAG/LBI) como fundação, não como enfeite (P24)?

### 1.3 O que a camada **não** decide

A UX **não** decide *o que é verdade* (KC/Etapa 2), *o que é conforme* (Compliance/Etapa 6), *o que o professor quer* (Planning/Etapa 7), *o que entra e com qual papel* (Matching/Etapa 8) nem *em que forma pedagógica isso aparece* (Output/Etapa 9). Ela decide **apresentação e operação** — e nada além disso.

### 1.4 O que a camada produz

Entidades de **experiência, externas e descartáveis** (Seção 4): a sessão (`ExperienceSession`), o estado de navegação (`NavigationState`), as vistas (`TimelineView`, `Globe3DView`, `Map2DView`, `StaticFallbackView`, `ProjectorModeView`, `OfflineModeView`, `ComparisonView`), os espaços de trabalho (`TeacherWorkspace`, `StudentWorkspace`, `FreeExplorationView`), o visualizador de saída (`PedagogicalOutputViewer`), os painéis (`DossierPanel`, `SourceEvidencePanel`), os rótulos/avisos (`EpistemicLabelView`, `UncertaintyLegend`, `GatingNotice`, `AnachronismNotice`, `EquivalenceWarningNotice`), os controles (`MediationControl`, `AccessibilityControl`), o editor e o fluxo (`ArtifactEditor`, `ApprovalWorkflow`, `ExportPackage`) e a trilha (`UXAuditTrail`). Nenhuma cria conteúdo; todas apresentam ou operam o que veio do Output.

---

## 2. Papel da camada na arquitetura geral (Tarefa 2)

### 2.1 Posição

A UX é o **topo** da cadeia. Recebe `PedagogicalOutput` (E9) — que por sua vez derivou de `MatchSet` (E8), de `PlanningProfile` (E7), de `ComplianceProfile` (E6), de `Scene` v1.1 (4H) e de `MomentResult` (E5), tudo ancorado em `Claim`/`Source` do KC (E2) — e o **apresenta**. A direção é única e invertida: **Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core**. Nada a montante conhece, importa ou depende da UX.

### 2.2 O que a UX é (e o que não é)

| A UX **é** | A UX **não é** |
|---|---|
| Camada de **apresentação e operação** de artefatos já prontos | Origem de conteúdo, de seleção, de conformidade ou de verdade |
| **Navegação** no tempo, no espaço e entre artefatos | Reabertura de Output, Matching, Planning ou Compliance |
| **Honestidade epistêmica visível** (rótulos, incerteza, fonte) | Camada que esconde incerteza ou remove rótulos para "ficar bonita" |
| **Degradação graciosa** 3D → 2D → estático → offline → projetor | Experiência que só funciona com 3D ou só online |
| **Edição docente da forma** (ordem, notas, mediação) | Edição de claim, fonte, publicabilidade, gating, `MatchSet` ou conformidade |
| **Acessibilidade como fundação** (e-MAG/WCAG/LBI) | Acessibilidade como enfeite opcional |
| Stack-, engine- e implementação-agnóstica (conceitual) | Definição de tecnologia, biblioteca, banco, API ou formato (Etapa 11) |

### 2.3 Divisão de responsabilidades (quem apresenta o quê)

| Camada | Decide | A UX, em relação a ela |
|---|---|---|
| **KC (E2)** | a verdade factual, rótulos epistêmicos, incerteza | **exibe** claim/fonte/incerteza por REF; nunca cria nem altera |
| **Compliance (E6)** | faixa, acessibilidade, sensíveis, uso escolar, índice BNCC | **respeita e visualiza** `AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement`/`SchoolUseMode`/`AllowedUseContext`; nunca relaxa |
| **Planning (E7)** | objetivo, série, duração, profundidade, modo, recorte local | **exibe** a intenção rotulada como intenção; nunca a reescreve |
| **Matching (E8)** | o que entra, papel curricular, `visibilityClass`, publicabilidade | **apresenta** os itens no papel e na visibilidade herdados; nunca reordena papel nem reabre seleção |
| **Output (E9)** | a forma pedagógica (15 tipos), blocos, citação, mediação, faixa | **renderiza e opera** `OutputArtifact`/`OutputSectionBlock`/cartões/avisos; nunca redecide a forma nem o fato |
| **UX (E10)** | **modo, vista, navegação, painel, rótulo visível, controle, fluxo de revisão/aprovação/exportação, acessibilidade** | é a própria camada |

### 2.4 Os vinte invariantes da `DesignUX3DLayer` (não negociáveis)

Estes invariantes governam toda a camada e são referenciados ao longo do documento.

1. **A UX não cria conhecimento.** Todo conteúdo factual vem por REF do KC/Output; a camada nunca origina fato.
2. **A UX não altera claims, fontes ou cenas.** `Claim`, `Source`, `Citation`, `Scene`, `ClaimSet` permanecem intocados.
3. **A UX não reabre Output.** Não redecide forma, tipo, blocos nem citação do artefato.
4. **A UX não reabre Matching.** Não recalcula `MatchScore`, não muda `curricularRole`, não reinclui item excluído por porta dura.
5. **A UX não relaxa Compliance.** Faixa, sensíveis, acessibilidade e uso escolar só podem **endurecer** na apresentação, nunca afrouxar.
6. **A UX não altera Planning.** A intenção docente é exibida como intenção, jamais reescrita.
7. **A UX não esconde incerteza relevante.** `uncertaintyDisplayPolicy` nunca é "omitir"; faixa/margem aparece em qualquer modo.
8. **A UX não remove rótulos epistêmicos.** `claimType`/`confidenceLevel`/`evidenceLevel`/`displayWeight` acompanham o conteúdo sempre.
9. **A UX não expõe conteúdo sensível sem mediação.** `requiresMediation`/`SensitiveContentRule` gate antes da exibição ao aluno.
10. **A UX não mostra `pending`, `legal-review` nem `rejected` como fato.** Publicabilidade 1–5 é respeitada; estados não-publicáveis nunca viram conteúdo do aluno.
11. **A UX não transforma exploração livre em plano curricular.** `freeExploration` permanece exploração; nunca é apresentado como trilha homologada.
12. **A UX não trata BNCC como fonte factual nem como selo.** Índice BNCC é alinhamento, exibido como tal; nunca autoridade factual nem homologação.
13. **A UX não promete homologação MEC/PNLD.** Nenhum rótulo, selo ou texto sugere aprovação oficial.
14. **A UX não usa IA como fonte.** Adaptação de linguagem (a forma) não vira autoria de fato; nenhuma resposta de IA aparece como evidência.
15. **A UX preserva rastreabilidade visual até claims/fontes/cenas/dossiês.** De qualquer artefato exibido chega-se à evidência por REF, em qualquer modo.
16. **A UX oferece degradação 3D → 2D → estático sem perder o piso epistêmico.** Tempo, espaço, fontes, simultaneidade, dossiê e incerteza sobrevivem a cada degrau.
17. **A UX garante acessibilidade como requisito estrutural.** Equivalente textual, navegação por teclado, foco visível, redundância não-cromática (e-MAG/WCAG/LBI; P24).
18. **A UX separa claramente professor e estudante.** `visibilityClass`/`studentFacingMode`/`SchoolUseMode` definem o que cada papel vê.
19. **A UX registra trilha de auditoria.** `UXAuditTrail` registra modo, vista, navegação e operações de forma, por REF, sem alterar alvo.
20. **A UX permite edição docente apenas da forma, nunca da verdade factual.** Ordem, notas e mediação são editáveis; claim, fonte, publicabilidade, gating, `MatchSet` e conformidade não.

> **Síntese dos invariantes.** A UX é o lugar onde o produto **mostra honestamente** o que decidiu em todas as camadas anteriores e **opera com respeito** a essas decisões. Tudo o que ela pode mudar é **como se vê e como se percorre**; nunca **o que é verdade, o que é conforme, o que foi planejado, o que foi selecionado ou em que forma foi entregue**.

---

## 3. Entradas da camada de UX (Tarefa 3)

Matriz de campos de entrada. Cada campo declara **definição**, **origem**, **obrigatório/opcional**, **uso na UX** e **risco se mal usado**. Os `*Ref` apontam para entidades **já definidas** nas Etapas 2/5/6/7/8/9; a UX **não** as recria.

| Campo (`camelCase`) | Definição | Origem | Obrig./Opc. | Uso na UX | Risco se mal usado |
|---|---|---|---|---|---|
| `pedagogicalOutputRef` | REF ao `PedagogicalOutput` revisado/conforme | Output (E9) | **Obrigatório** | âncora de toda a sessão; sem ele não há experiência | apresentar experiência sem saída → conteúdo arbitrário/inventado |
| `outputStatusRead` | LIDO de `PedagogicalOutput.outputStatus` (Seção 12) | Output (E9) | **Obrigatório** | governa se a sessão exibe rascunho pedagógico ou pronto-para-uso | exibir `rascunhoPedagogico` como definitivo → falso pronto |
| `artifactRefs` | REFs aos `OutputArtifact` do conjunto | Output (E9) | **Obrigatório** | itens navegáveis no `PedagogicalOutputViewer` | apresentar artefato fora do papel/visibilidade herdados |
| `sectionBlockRefs` | REFs aos `OutputSectionBlock` (com `blockRole`, `visibilityClass`, `requiresMediation`) | Output (E9) | **Obrigatório** | unidades de exibição; herdam papel e visibilidade | mover bloco para papel/visibilidade incompatível |
| `outputComplianceSummaryRead` | LIDO do `OutputComplianceSummary` (faixa, sensíveis, acessibilidade, BNCC, uso escolar) | Output (E9)→Compliance (E6) | **Obrigatório** | piso de conformidade da experiência; governa modo/visibilidade | montar experiência fora do perfil da turma; relaxar piso |
| `outputCitationBundleRead` | LIDO dos `OutputCitationBundle` por artefato | Output (E9) | **Obrigatório** | alimenta `SourceEvidencePanel`; citação, jamais reprodução (1.1) | omitir fonte; reproduzir conteúdo licenciado |
| `outputConstraintWarningsRead` | LIDO dos `OutputConstraintWarning` (tempo/recurso/faixa) | Output (E9) | Opcional | exibe aviso de não-cabimento; nunca altera o plano | esconder o aviso; alterar o plano na UI |
| `sceneRefs` | REFs a `Scene` v1.1 usadas (com `timelineBehavior`/`globeBehavior`/`dossierBehavior`/`simultaneityBehavior`/`paleoPositionPolicy`/`gatingReason`/`sceneCompletenessLevel`) | função (E5)/curadoria (4x), via E8/E9 | Opcional | base de timeline, globo, dossiê e comparação | tratar `generatedSceneCandidate`/`gabarito-interno` como público |
| `momentResultRefs` | REFs a `MomentResult` consultados (simultaneidade, anacronismo, equivalência) | função (E5), via E8/E9 | Opcional | base de "o que acontecia no mundo" e da simultaneidade global | apagar simultaneidade ao "limpar" a tela |
| `dossierRefs` | REFs a dossiês usados | E5/E8/E9 | Opcional | base de `DossierPanel` | reescrever o dossiê em vez de exibi-lo |
| `claimRefs` | REFs a `Claim`/`ClaimSet`/`WeightedClaim` citados (com `claimType`/`confidenceLevel`/`evidenceLevel`/`displayWeight`/`UncertaintyProfile`) | KC (E2), via E8/E9 | **Obrigatório** | conteúdo factual citável; alimenta `EpistemicLabelView` | parafrasear/abreviar a ponto de mudar o fato |
| `sourceEvidenceCardRefs` | REFs a `SourceEvidenceCard` ("como sabemos isso") | Output (E9) | Recomendado | alimenta `SourceEvidencePanel` e o cartão "como sabemos" | omitir evidência; inventar atribuição |
| `mediationScriptRefs` | REFs a `MediationScript` (tema sensível) | Output (E9)→Compliance (E6) | Opcional | alimenta `MediationControl` no modo professor | exibir conteúdo sensível ao aluno sem mediação |
| `viewerRole` | papel de quem visualiza | sessão (UX) | **Obrigatório** | governa modo, visibilidade e workspace | dar ao aluno a face do professor |
| `experienceModeRequested` | modo de experiência pedido (Seção 5) | sessão (UX) | **Obrigatório** | define vistas, painéis e controles ativos | pedir modo incompatível com o papel/faixa |
| `accessibilityNeeds` | necessidades que disparam `AccessibilityRequirement` (e-MAG/WCAG/LBI) | Planning (E7)→Compliance (E6) | Recomendado | configura `AccessibilityControl` (equivalente textual, foco, redundância não-cromática, movimento reduzido) | excluir alunos; descumprir LBI |
| `deviceCapabilityRead` | LIDO: capacidade de apresentação do dispositivo (3D / 2D / estático / offline / projetor) | contexto de uso (D10) | Recomendado | escolhe o degrau do `ViewDegradationLadder` | forçar 3D em dispositivo incapaz; perder o piso epistêmico |

> **Regra transversal de entradas.** Campos textuais herdados do Planning via Output (`theme`, `teacherObjective`, `teacherNotes`, `localContext`, `assessmentIntent`) e as notas do professor são **intenção**, nunca `Claim` factual. A UX os exibe sob rótulo explícito de "intenção do professor"; jamais os promove a fato. O conteúdo factual exibido vem **somente** de `claimRefs`/`sceneRefs`/`dossierRefs`/`momentResultRefs`/`outputCitationBundleRead` já presentes no `PedagogicalOutput`. **Nenhuma resposta de IA é exibida como fonte ou evidência** (invariante 14).

---

## 4. Entidades conceituais da camada (Tarefa 4)

Entidades **externas ao Knowledge Core, distintas das entidades da Compliance, do Planning, do Matching e do Output**. Nenhuma é, vira ou recria entidade do núcleo ou das Etapas 6/7/8/9. As entidades de UX **referenciam** as demais por ID; não as duplicam. Apagar qualquer uma delas não altera um único campo a montante.

| Entidade (`CamelCase`) | Papel | Para que aponta | Observação de fronteira |
|---|---|---|---|
| **`DesignUX3DLayer`** | a camada que apresenta e opera o `PedagogicalOutput` | `PedagogicalOutput`, `Scene`, `MomentResult`, KC | apresenta; nunca cria conteúdo |
| **`ExperienceSession`** | uma sessão de visualização/operação de uma saída | `pedagogicalOutputRef`, vistas, estado | externa e descartável; ver dicionário (Seção 4.1) |
| **`ExperienceMode`** | modo de experiência ativo (Seção 5) | a sessão | rótulo de modo; não cria conteúdo |
| **`ViewerRole`** | papel de quem visualiza | a sessão | `professor` \| `estudante` \| `coordenacaoPedagogica` \| `exploradorLivre` |
| **`NavigationState`** | estado de navegação no tempo/espaço/artefato | tempo, espaço, foco | onde a experiência "está"; não altera dados |
| **`TimelineView`** | vista da timeline multiescala (Seção 6) | itens por `canonicalTimeScalar`; `Scene.timelineBehavior` | renderiza tempo; não define biblioteca |
| **`Globe3DView`** | vista do globo 3D (Seção 7) | marcadores/overlays; `Scene.globeBehavior`; `paleoPositionPolicy` | renderiza espaço; não define engine |
| **`Map2DView`** | degradação 2D do globo (Seção 7) | mesmos REFs do globo | preserva piso epistêmico |
| **`StaticFallbackView`** | degradação estática (imagem + texto) (Seção 7) | mesmos REFs | sobrevive sem interação/3D |
| **`ProjectorModeView`** | vista para projeção em sala (Seção 9) | a sessão | alto contraste, baixa densidade; misto |
| **`OfflineModeView`** | vista offline/pacote local (Seção 9) | subconjunto pré-carregado | preserva fonte/incerteza offline |
| **`ComparisonView`** | vista de comparação A×B / antes-depois (Seção 7/12) | par de `Scene`/States; `weightedClaimSets` | confiança decaindo; sem falsa simetria |
| **`TeacherWorkspace`** | espaço de trabalho do professor (Seção 9/10) | aparato completo + edição de forma | só em `SchoolUseMode = teacher` |
| **`StudentWorkspace`** | espaço de trabalho do estudante (Seção 9) | face do aluno por faixa | nada `teacherOnly`/`pending`/sensível sem mediação |
| **`FreeExplorationView`** | exploração livre do atlas (Seção 9) | KC/cenas com filtro de adequação | exploração ≠ trilha curricular |
| **`PedagogicalOutputViewer`** | visualizador do `PedagogicalOutput` e seus artefatos | `OutputArtifact`/`OutputSectionBlock` | exibe; não reabre forma |
| **`ArtifactEditor`** | editor de **forma** do artefato (Seção 10) | `OutputArtifact` + `OutputRevisionNote` | edita ordem/nota/mediação; nunca claim/fonte/gating |
| **`ApprovalWorkflow`** | fluxo de revisão/aprovação docente (Seção 10) | estados de revisão da sessão | externo; não altera `reviewStatus` do KC |
| **`ExportPackage`** | conceito de empacotamento para exportação (Seção 10) | artefato + avisos obrigatórios | conceito; não gera arquivo/layout/stack |
| **`DossierPanel`** | painel de dossiê (Seção 8) | `Scene.dossierBehavior`/`dossierRefs` | exibe; não reescreve o dossiê |
| **`SourceEvidencePanel`** | painel de fonte/evidência (Seção 8) | `OutputCitationBundle`/`SourceEvidenceCard` | cita; jamais reproduz (1.1) |
| **`EpistemicLabelView`** | rótulo visível de tipo/confiança/evidência (Seção 11) | `claimType`/`confidenceLevel`/`evidenceLevel`/`displayWeight` | mostra honestidade; nunca a esconde |
| **`UncertaintyLegend`** | legenda de incerteza (Seção 11) | `UncertaintyProfile`/`timeUncertainty` | redundância não-cromática; nunca "omitir" |
| **`GatingNotice`** | aviso de gating/publicabilidade (Seção 11) | `gatingReason`/`publicabilityStatus` | não exibe `pending`/`rejected` como fato |
| **`MediationControl`** | controle de mediação de tema sensível (Seção 11) | `MediationScript`/`SensitiveContentRule`/`requiresMediation` | gate antes do aluno; o professor media |
| **`AccessibilityControl`** | controle de acessibilidade (Seção 11) | `AccessibilityRequirement` (e-MAG/WCAG/LBI) | fundação; equivalente textual, foco, contraste |
| **`AnachronismNotice`** | aviso de anacronismo (Seção 11/12) | `anachronismWarnings` (E5)/`anachronismPolicy` (Scene) | repassado; nunca suprimido |
| **`EquivalenceWarningNotice`** | aviso anti-falsa-equivalência (Seção 11/12) | `equivalenceWarnings`/`weightedClaimSets` | negacionismo rotulado-rejeitado, fora do par |
| **`ViewDegradationLadder`** | escada conceitual de degradação de vista (Seção 7) | os modos/vistas de 3D a estático/offline | encoda o piso epistêmico por degrau |
| **`UXAuditTrail`** | trilha de auditoria de modo/vista/navegação/operações de forma | refs de entrada + decisões de apresentação | externa e descartável; rastreabilidade integral |

> **`UXAuditTrail` × `OutputAuditTrail` × `MatchingAuditTrail` × `ComplianceAnnotation` × `PlanningAnnotation`.** A `ComplianceAnnotation` (E6) anota conformidade/legalidade; a `PlanningAnnotation` (E7) anota organização pedagógica do planejamento; a `MatchingAuditTrail` (E8) registra como a seleção foi calculada; a `OutputAuditTrail` (E9) registra como o artefato foi montado a partir da seleção; a `UXAuditTrail` (E10) registra **como a experiência foi apresentada e operada** (modo, vista, navegação, edição de forma, aprovação, exportação). As cinco são externas, apontam por ID e nunca editam o alvo; vivem em camadas diferentes e não se confundem.

> **`OutputRevisionNote` (E9) na UX.** A edição de forma feita no `ArtifactEditor` materializa-se como `OutputRevisionNote` (entidade da Etapa 9) — anotação humana descartável que **não altera** o `MatchSet`, o KC, a Compliance, a publicabilidade nem o gating. A UX não cria uma entidade de nota nova: ela **opera** a `OutputRevisionNote` já definida a montante.

### 4.1 `ExperienceSession` (dicionário conceitual)

```txt
ExperienceSession = {
  experienceSessionId,
  viewerRole,                 # professor | estudante | coordenacaoPedagogica | exploradorLivre
  experienceMode,             # um valor de ExperienceMode (Seção 5)
  pedagogicalOutputRef,       # REF ao PedagogicalOutput (E9) — âncora obrigatória
  activeArtifactRef,          # REF ao OutputArtifact em foco (E9)
  activeSceneRef,             # REF à Scene v1.1 em foco (E5/4H), quando há
  activeMomentResultRef,      # REF ao MomentResult em foco (E5), quando há
  activeTimelineRange,        # recorte temporal ativo (canonicalTimeScalar + displayTime por regime)
  activeSpatialScope,         # recorte espacial ativo (região/escopo rotulado)
  navigationState,            # NavigationState (Seção 4.2)
  displayedOutputSections,    # subconjunto de OutputSectionBlock exibidos (respeita visibilityClass/papel)
  visibleEpistemicLabels,     # rótulos epistêmicos visíveis (claimType/confidence/evidence/displayWeight) — nunca vazio quando há claim
  activeGatingNotices,        # GatingNotice ativos (gatingReason/publicabilityStatus) — pending/rejected nunca como fato
  activeMediationControls,    # MediationControl ativos (MediationScript/SensitiveContentRule)
  accessibilityProfile,       # AccessibilityControl ativo (equivalente textual, foco, redundância não-cromática, movimento reduzido)
  offlineAvailabilityStatus,  # disponível | parcial | indisponível (offline) — preserva piso epistêmico
  projectorModeStatus,        # ativo | inativo (modo projetor)
  exportOptions,              # ExportPackage(s) disponíveis (conceito; sem gerar arquivo)
  approvalWorkflowStatus,     # estado de revisão/aprovação na UX (Seção 10) — externo ao reviewStatus do KC
  uxAuditTrail                # UXAuditTrail (externo, descartável)
}
```

> **Invariante de sessão.** `visibleEpistemicLabels` **nunca** é vazio quando o conteúdo exibido tem claim; `activeGatingNotices` **nunca** rebaixa um item `pending`/`legal-review`/`rejected` a fato; `accessibilityProfile` **sempre** existe (acessibilidade é fundação — P24); e o conjunto exibido em `displayedOutputSections` **sempre** respeita `viewerRole`/`visibilityClass`/`studentFacingMode`.

### 4.2 `NavigationState`, `ViewDegradationLadder` e os avisos (dicionários conceituais)

```txt
NavigationState = {
  navStateId,
  temporalFocus,              # ponto/recorte no eixo (canonicalTimeScalar), exibido por displayTime
  temporalRegime,            # cósmico | profundo (Ga/Ma) | histórico (BCE/CE) | contemporâneo | projetivo
  spatialFocus,              # região/escopo ativo (rotulado: atual × paleoposição quando aplicável)
  focusEntityRef,            # Event | Process | State | Scene | OutputArtifact em foco
  activeLayers,              # camadas 4A ativadas na vista (LIDAS; não criadas)
  simultaneityVisible,       # bool — a simultaneidade global está exibida? (D8; default = sim)
  breadcrumbTrail,           # trilha de navegação (para voltar; não altera dados)
  comparisonPair             # par A×B quando em ComparisonView (opcional)
}

ViewDegradationLadder = {
  ladderId,
  rungs[],                    # ordem: Globe3DView → Map2DView → StaticFallbackView → OfflineModeView/ProjectorModeView
  epistemicFloor,             # piso preservado em TODO degrau: tempo, espaço, fontes, simultaneidade, dossiê, incerteza
  selectionPolicy,            # escolhe o degrau por deviceCapabilityRead/accessibilityProfile/contexto de sala
  textualEquivalentAlways     # invariante FIXO = true (equivalente textual em qualquer degrau — e-MAG/WCAG/LBI)
}

GatingNotice = {
  noticeId,
  targetRef,                  # OutputSectionBlock/Scene/claim a que o aviso se refere
  publicabilityStatusRead,    # LIDO (1–5) — repassado, nunca alterado
  gatingReasonRead,           # LIDO (editorial | científico | licença | revisão-humana | geometria | mídia | fonte | legal)
  visibilityForRole,          # como o item aparece por papel (oculto | resumo | aparato) — pending/rejected nunca como fato ao aluno
  noticeText                  # texto do aviso na linguagem da faixa (a forma; o fato/estado não muda)
}

AnachronismNotice = {
  noticeId,
  targetRef,                  # item/cena/recorte a que se refere
  anachronismWarningRead,     # LIDO de MomentResult/Scene (E5 §9) — repassado, nunca suprimido
  noticeText                  # ex.: "fronteiras atuais sobre o passado"; "paleoposição ≠ localidade atual"
}

EquivalenceWarningNotice = {
  noticeId,
  targetRef,                  # par/ClaimSet a que se refere
  equivalenceWarningRead,     # LIDO (E5 §9) — repassado
  weightedClaimSetRead,       # LIDO: weightedClaimSets (Scene v1.1) — peso por claim preservado
  noticeText                  # consenso ≠ negação; pluralidade ≠ palco igual a tudo (PE-Ed5)
}
```

---

## 5. Modos de experiência (Tarefa 5)

### 5.1 Taxonomia de `experienceMode` (lista controlada)

`teacherMode` · `studentMode` · `projectorMode` · `offlineMode` · `freeExplorationMode` · `guidedExplorationMode` · `artifactReviewMode` · `sourceEvidenceMode` · `dossierMode` · `comparisonMode`.

### 5.2 Tabela de modos: público, vistas/painéis e cautela

| `experienceMode` | Público | Vistas/painéis ativos | Cautela principal |
|---|---|---|---|
| `teacherMode` | **Professor** | aparato completo: `TeacherWorkspace`, `SourceEvidencePanel`, `MediationControl`, `EpistemicLabelView`, `GatingNotice` | aparato `teacherOnly` nunca vaza ao aluno |
| `studentMode` | **Estudante** | `StudentWorkspace`, face do aluno por faixa; rótulos compactos visíveis | nada `teacherOnly`/`pending`/sensível sem mediação |
| `projectorMode` | **Misto (sala)** | `ProjectorModeView` (alto contraste, baixa densidade), timeline + globo | legibilidade à distância; não perder fonte/incerteza |
| `offlineMode` | **Misto** | `OfflineModeView` (pacote local), piso epistêmico preservado | sincronizar nada do aluno; preservar fonte offline |
| `freeExplorationMode` | **Misto** | `FreeExplorationView`, KC/cenas com filtro de adequação | exploração ≠ trilha curricular (invariante 11) |
| `guidedExplorationMode` | **Misto** | `ExplorationGuideOutput` conduzindo timeline/globo/dossiê | guiado pela saída; preservar simultaneidade (D8) |
| `artifactReviewMode` | **Professor** | `ArtifactEditor`, `ApprovalWorkflow`, `OutputRevisionNote` | edita só a forma; nunca claim/fonte/gating |
| `sourceEvidenceMode` | **Misto** | `SourceEvidencePanel`, "como sabemos isso", `EpistemicLabelView` | citar, nunca reproduzir (1.1) |
| `dossierMode` | **Misto** | `DossierPanel` (15/18/20 blocos conforme a cena) | preservar incerteza/anacronismo; não reescrever |
| `comparisonMode` | **Misto** | `ComparisonView` (A×B/antes-depois), `weightedClaimSets` | confiança decaindo; sem falsa simetria |

### 5.3 Classificação por público

| Classe | Modos | Regra |
|---|---|---|
| **Para professor** | `teacherMode`, `artifactReviewMode` | acesso ao **aparato completo** (fontes integrais, `ClaimSet` integral, notas de mediação, mídia sensível para preparação sob licença) e à **edição de forma**; só em `SchoolUseMode = teacher`; **nunca** exibidos ao aluno como fato (E3.1 §9; E6 §7). |
| **Para estudante** | `studentMode` | linguagem, exposição e mídia **conforme a faixa**; conteúdo gráfico oculto por padrão; sensível só `teacherMediated`/`restricted` conforme a faixa; nada `teacherOnly`/`pending`/`legal-review`/`rejected`. |
| **Mistos** | `projectorMode`, `offlineMode`, `freeExplorationMode`, `guidedExplorationMode`, `sourceEvidenceMode`, `dossierMode`, `comparisonMode` | possuem **face do professor** (preparação/mediação/aparato) e **face do aluno** (uso em sala), separadas por `studentFacingMode` e `visibilityClass`; a face do aluno respeita a faixa, a face do professor carrega o aparato. |

> **Os 10 modos ≠ as 30 entidades.** O `experienceMode` é o **rótulo de configuração** que liga vistas, painéis e controles; as entidades são as **estruturas** que cada modo ativa. Nenhum modo cria conteúdo: todos apresentam e operam o `PedagogicalOutput` e suas referências. Um mesmo `OutputArtifact` pode ser percorrido em vários modos; o modo muda **a apresentação**, nunca **a forma decidida pelo Output** nem **o fato decidido pelo KC**.

---

## 6. Timeline multiescala (Tarefa 6)

A UX **renderiza** a timeline multiescala herdada da Etapa 3 e do eixo canônico da Etapa 3Z. Ela não inventa eixo, datum, precisão nem incerteza; **apresenta** o que o KC/3Z fixaram e o que `Scene.timelineBehavior` e `MomentResult` trouxeram.

### 6.1 Regimes e eixo

- **Cobertura:** do **Big Bang ao presente** e ao **futuro projetivo** (rotulado como cenário/modelo).
- **Eixo de ordenação:** `canonicalTimeScalar` (anos relativos a `T0 = 2000.0 CE`, alinhado a J2000; negativo = passado, positivo = futuro) — serve **à máquina** (ordenar/intersectar); **nunca** é a linguagem de exibição.
- **Exibição por regime (`displayTime`):** regime **profundo** em **Ga/Ma**; regime **histórico** em **BCE/CE**; regime **contemporâneo** em data/ISO; regime **projetivo** em ano de cenário. A UX **nunca** exibe um número seco na linguagem de outro regime (exibir "1789" como "0,0000002 Ma" ou "~66 Ma" como "66.000.000 a.C." **mente sobre a precisão**).
- **`sourceTimeBasis` preservado:** o datum nativo da fonte (BP1950, calBP, radiocarbonBP, J2000, gregorianCE, ISO8601, Ma, Ga, scenarioYear) é mostrado quando relevante; o ¹⁴C bruto **nunca** é exibido como calendário sem calibração.

### 6.2 Zoom e comportamento por tipo

- **Zoom logarítmico/conceitual:** a navegação cruza dezenas de ordens de magnitude (de 13,8 Ga a um dia) com transição **conceitual** entre regimes; a UI **rotula a mudança de regime** em vez de fingir um contínuo linear ilegível.
- **Comportamentos visuais distintos** (de `Scene.timelineBehavior` e do tipo no KC): **`Event`** = marcador pontual; **`Process`** = barra/extensão com **bordas difusas**; **`State`** = faixa de fundo (condição do sistema). A `cascadeStructure` (Scene v1.1) aparece como **sequência logo após o `triggerItem`**, com **barras de incerteza crescentes** e **gradiente de confiança por estágio** (sem seta determinista).
- **Precisão e incerteza temporais:** `timePrecision` (Ga|Ma|ka|século|década|ano|mês|dia|cenário) governa a granularidade visual; `timeUncertainty`/`UncertaintyProfile` aparece como **faixa/margem** (não ponto cravado), com **rótulo de precisão** e **redundância não-cromática** (`UncertaintyLegend`). Um item de borda difusa "aparece" no momento consultado **com a ressalva de incerteza**.

### 6.3 Ligações

- **Com `MomentResult`:** os itens são posicionados por `canonicalTimeScalar` e exibidos por `displayTime`; `mainItems` ancoram o foco; `simultaneousItems` mantêm a **simultaneidade global** visível.
- **Com `Scene` v1.1:** `timelineBehavior` define como cada cena se comporta no eixo; `paleoPositionPolicy` lembra que posição **atual ≠ paleoposição** quando a cena é de tempo profundo.
- **Com `PedagogicalOutput`:** cada `OutputSectionBlock` com âncora temporal liga-se ao ponto/recorte correspondente; um plano de aula sobre 1789 foca −211 (≈ 1789), mas a timeline **continua permitindo** ver o que coexistia (D8).

> **Invariante de timeline.** A simultaneidade global **nunca** é apagada ao "escolarizar" a vista (invariante e D8). A UX pode **focar** um recorte (a aula), mas o resto do mundo no mesmo momento permanece **navegável**. A timeline não vira um slideshow linear de slides fixos (R-05): ela é eixo navegável em qualquer modo. **Esta seção não define tecnologia, biblioteca de timeline nem formato de renderização** (Etapa 11).

---

## 7. Globo/mapa 3D e degradação para 2D/estático (Tarefa 7)

A UX **renderiza** a representação espacial herdada da Etapa 3 e o comportamento de `Scene.globeBehavior`/`simultaneityBehavior`. Ela não inventa geometria, fronteira nem paleogeografia; **apresenta** o que veio rotulado a montante.

### 7.1 Globo como representação principal

- **`Globe3DView`** é a representação espacial principal: marcadores de **evento** (`Event`), **overlays de State** (condições do sistema), **camadas 4A ativadas** (LIDAS), e o **recorte espacial** ativo (`activeSpatialScope`).
- **Paleogeografia rotulada como reconstrução modelada:** toda paleogeografia carrega rótulo explícito de **reconstrução modelada** (não "foto", não certeza). O **`paleoPositionPolicy`** (Scene v1.1) distingue **localidade atual** de **paleoposição** — ex.: Chicxulub está **hoje** no Yucatán, mas sua **paleoposição** em 66 Ma é outra; a `ModernCorrespondence` liga o lugar antigo ao lugar atual **sem** sugerir que "México" existia em 66 Ma (`AnachronismNotice`).
- **Marcadores, overlays e itens sensíveis/ocultos:** marcadores de evento e overlays de State respeitam `visibilityClass`; `sensitiveItems` exigem `MediationControl`; `hiddenItems` **não** são exibidos como fato — no máximo entram como **contagem/resumo** conforme modo e publicabilidade (nunca `pending`/`rejected` ao aluno).

### 7.2 Degradação graciosa (`ViewDegradationLadder`)

A alternância obedece a escada **`Globe3DView` → `Map2DView` → `StaticFallbackView`**, com **`OfflineModeView`** e **`ProjectorModeView`** como variações de contexto. A escada é escolhida por `deviceCapabilityRead`, `accessibilityProfile` e contexto de sala.

| Degrau | O que é | Piso epistêmico preservado |
|---|---|---|
| `Globe3DView` | globo 3D interativo | tempo, espaço, fontes, simultaneidade, dossiê, incerteza |
| `Map2DView` | mapa 2D (sem 3D) | **idem** — mesmos REFs, mesma honestidade |
| `StaticFallbackView` | imagem + **equivalente textual** | **idem** — funciona sem interação/3D |
| `ProjectorModeView` | projeção em sala (alto contraste, baixa densidade) | **idem** — legível à distância |
| `OfflineModeView` | pacote local pré-carregado | **idem** — fonte/incerteza disponíveis offline |

> **Invariante de degradação (invariante 16).** **Nenhum degrau perde o piso epistêmico**: tempo, espaço, fontes, simultaneidade, dossiê e incerteza sobrevivem a 2D, ao estático, ao offline e ao projetor. A UX **não pode** depender de 3D para existir (R-15), nem deixar de funcionar em projetor (R-16) ou offline (R-17). O **equivalente textual** do globo/mapa existe em **todo** degrau (`textualEquivalentAlways = true`; e-MAG/WCAG/LBI; P24).

### 7.3 Acessibilidade espacial

Para quem **não usa interação 3D** (leitor de tela, navegação por teclado, movimento reduzido), o globo/mapa tem **equivalente textual completo**: o que aconteceu, **onde**, **quando** e **com que confiança** (E6 §6; descrição textual de mapas e cenas). A vista respeita `prefers-reduced-motion` (alternativa estática), foco visível e **redundância não-cromática** (a posição/confiança nunca é codificada **só** por cor — R-14).

> **Esta seção não define engine gráfica, motor 3D, projeção cartográfica nem stack** (Etapa 11). Define **o que a representação espacial precisa apresentar e como precisa degradar**, conceitualmente.

---

## 8. Dossiês, cartões, fontes e evidência (Tarefa 8)

A UX **exibe** a evidência; nunca a cria nem a reescreve. Os painéis materializam "como sabemos isso" preservando a cadeia de referência até `Claim`/`Source`.

### 8.1 `DossierPanel`

Renderiza `Scene.dossierBehavior`/`dossierRefs` (15 blocos para simultaneidade humana; 18 para "como sabemos" em tempo profundo; 20 para sistema + "como sabemos"), preservando **incerteza**, **anacronismo** e **simultaneidade**. O painel **organiza** o dossiê; **não** o reescreve (R do Output herdado). Blocos sensíveis passam por `MediationControl`.

### 8.2 `SourceEvidencePanel` e os cartões

Renderiza `OutputCitationBundle` e `SourceEvidenceCard`. Cada cartão exibe:

- **`targetClaimRefs`** — os claims que o cartão sustenta;
- **`evidenceLevelRead`** — observação direta | medição instrumental | documento primário | dado modelado | inferência indireta | testemunho secundário (LIDO, E2);
- **`howWeKnow`** — síntese "como sabemos disso" na linguagem da faixa (a forma; o fato não muda);
- **`citationRefs`** — atribuição a `Citation`/`Source` — **jamais reprodução** (1.1);
- **`licenseNoteRead`** — respeito a licença e ao isolamento ShareAlike;
- **`uncertaintyNote`** — faixa/margem preservada (não "lado").

### 8.3 `ClaimSet`, `WeightedClaimSet` e `UncertaintyProfile` na UI

- **`ClaimSet`** legítimo (controvérsia/disputa historiográfica) é exibido **lado a lado**, cada claim com fonte e peso (PE-Ed2).
- **`WeightedClaimSet`** (Scene v1.1) carrega **peso por claim** (`displayWeight`): claims concorrentes **não** recebem o mesmo destaque visual quando seu estatuto difere (K-Pg: impacto ≫ Deccan; clima: consenso vs negacionismo **rejeitado**) — `EquivalenceWarningNotice` impede a falsa simetria (R-13).
- **`UncertaintyProfile`** aparece como **faixa/margem** com `UncertaintyLegend`, nunca como número seco.

### 8.4 Distinção epistêmica visível

A UI **mostra honestidade epistêmica** (PE-Ed1/D7), distinguindo visivelmente:

| Rótulo (`EpistemicLabelView`) | Como aparece |
|---|---|
| **fato documentado / medição direta** | rótulo de fato; alta confiança |
| **inferência científica** | rótulo de inferência; nunca com autoridade de fato observado |
| **estimativa / hipótese** | rótulo de hipótese/estimativa; confiança média/baixa |
| **controvérsia / interpretação historiográfica** | `ClaimSet` lado a lado, com peso e fonte |
| **reconstrução modelada** | rótulo de reconstrução (paleogeografia, paleoatmosfera) — **nunca "foto"** (R-02/R-03) |
| **aproximação didática** | rótulo de aproximação; `shortDescription` **nunca** tratada como claim |
| **negacionismo / desinformação** | rótulo de **rejeição**; objeto de estudo, **nunca** lado equivalente |

> **Invariante de evidência.** A UI **nunca esconde incerteza para ficar bonita** (R-01), **nunca remove o rótulo epistêmico** (invariante 8), **nunca transforma reconstrução modelada em foto** (R-02) e **nunca perde a fonte/citação** — nem no modo estudante (R-19), nem no exportado (R-20), nem offline. Citação **≠** reprodução: o conteúdo licenciado é **referenciado**, não copiado (1.1).

---

## 9. Modos professor, estudante, projetor, offline e exploração livre (Tarefa 9)

### 9.1 O que cada papel vê

| Aspecto | Professor (`teacherMode`/`TeacherWorkspace`) | Estudante (`studentMode`/`StudentWorkspace`) |
|---|---|---|
| **Aparato (fontes integrais, `ClaimSet` integral, mediação)** | **vê** (preparação) | **não vê** (só o que é `visívelAoAluno`) |
| **Conteúdo `teacherOnly`/`internalReviewOnly`** | **vê** | **nunca** (R-07) |
| **Conteúdo sensível** | vê para preparar; media | só `teacherMediated`/`restricted` conforme a faixa; gráfico oculto por padrão (R-06) |
| **`pending`/`legal-review`/`rejected`** | vê como **status**, não como fato | **nunca** como fato (R-23) |
| **Edição de forma** | **pode** (Seção 10) | **não pode** |
| **Linguagem** | nível `professor` | nível por faixa (6-8 / 9-11 / 12-14 / 15-17), sem infantilizar EM (R-22) |
| **Fonte/incerteza** | aparato completo | rótulo compacto **sempre visível** (R-19) |

A separação obedece a `visibilityClass` (`teacherOnly` | `teacherMediated` | `internalReviewOnly` | `contextualOnly` | `enrichmentOnly` | `visívelAoAluno` | `hidden`), `studentFacingMode` (`voltadoAoProfessor` | `voltadoAoAluno` | `misto`), `teacherMediationLevel` (`nenhuma` | `baixa` | `media` | `alta` | `obrigatoria`), `SensitiveContentRule`, `MediationScript`, `AgeSuitability` e `AllowedUseContext` — todos **herdados**, nunca redefinidos.

### 9.2 Modo projetor (`ProjectorModeView`)

Misto, para a sala: **alto contraste**, **baixa densidade**, foco em timeline + globo + um bloco por vez; **preserva fonte e incerteza** (não vira pôster sem aparato). A face exibida segue o papel de quem opera (professor) e o que pode ser visto coletivamente; conteúdo sensível só com `MediationControl`.

### 9.3 Modo offline (`OfflineModeView`)

Misto: subconjunto **pré-carregado** que preserva o **piso epistêmico** (fonte, incerteza, dossiê, simultaneidade mínima). Conteúdo sensível em `homework` offline sobe o cuidado (sem professor presente, restringe-se mais — herdado de E9). **Nenhum dado pessoal de aluno** é capturado ou sincronizado (R-28; LGPD Art. 14/ECA).

### 9.4 Exploração livre (`FreeExplorationView`)

Misto: percorre o KC/cenas com **filtro de adequação** por faixa (E6 §9: `freeExploration`), **sem grade**. É **exploração**, **não trilha curricular** (invariante 11; R-24): a UI **não** rotula a exploração como plano homologado, não a indexa como cobertura BNCC obrigatória e mantém a simultaneidade global (D8). Conteúdo fora da grade pode aparecer como **contexto, aprofundamento, comparação ou simultaneidade** — nunca como núcleo curricular sem o Planning (R-12).

---

## 10. Revisão, edição, aprovação e exportação de artefatos (Tarefa 10)

### 10.1 `TeacherWorkspace` e `ArtifactEditor`

O **`TeacherWorkspace`** é o espaço onde o professor revisa o `PedagogicalOutput`. O **`ArtifactEditor`** permite editar **apenas a forma**:

| O professor **pode** editar (forma) | O professor **não pode** editar (verdade/regra) |
|---|---|
| ordem dos `OutputSectionBlock` | `Claim`, `Source`, `Citation` (conteúdo factual) — R-08 |
| notas e comentários (`OutputRevisionNote`) | `claimType`/`confidenceLevel`/`evidenceLevel`/`UncertaintyProfile` |
| nível de mediação a aplicar **dentro do permitido** | `publicabilityStatus`/`gatingReason` — R-09 |
| recorte de foco (qual bloco destacar) | `MatchSet`/`MatchScore`/`curricularRole` |
| densidade/linguagem **dentro da faixa** (sem relaxar) | `ComplianceProfile`/`AllowedUseContext`/`SensitiveContentRule` |
| marca de "revisar" | `BNCCMapping`/`CurricularAlignment` (índice; não vira selo) — R-10 |

> **Regra de edição (invariante 20).** A edição docente é **da forma, nunca da verdade factual**. Reordenar, anotar e ajustar mediação produz `OutputRevisionNote` (entidade E9, descartável) — **não** altera o `MatchSet`, o KC, a Compliance, a publicabilidade nem o gating. O professor **não pode burlar a Compliance** pela UI (R-09): tentar expor conteúdo sensível sem mediação, rebaixar faixa ou revelar `teacherOnly` ao aluno é **bloqueado** pela camada.

### 10.2 `ApprovalWorkflow`

Fluxo **externo e descartável** de revisão/aprovação **na UX** (estados de revisão visual: rascunho de revisão → em revisão → revisado pelo professor → aprovado para uso na turma). Estes estados são da **sessão**; **não** alteram o `reviewStatus`/`publicabilityStatus` do KC nem o `outputStatus` do Output (invariante 19). O `approvalWorkflowStatus` da `ExperienceSession` registra o ponto do fluxo.

### 10.3 `ExportPackage`

**Conceito** de empacotamento de um artefato para uso fora da experiência (PDF/impresso/apresentação/pacote offline). A Etapa 10 **define o conceito e as regras**, **não gera** arquivos, layouts finais, slides nem stack (isso é Etapa 11/14).

> **Regra de exportação.** Todo `ExportPackage` **carrega obrigatoriamente** (a) a **fonte/citação** (R-20), (b) o **rótulo epistêmico e a incerteza**, (c) o **aviso de mediação** quando há conteúdo sensível (R-25), (d) o **aviso de anacronismo/equivalência** quando aplicável, e (e) a nota de que **alinhamento BNCC ≠ homologação ≠ PNLD** (R-11). Exportação **nunca** remove o piso epistêmico nem transforma `freeExploration` em trilha curricular (R-24). Nenhum pacote captura dado pessoal de aluno (R-28).

---

## 11. Visualização de incerteza, publicabilidade, gating, mediação e acessibilidade (Tarefa 11)

### 11.1 Incerteza (`UncertaintyLegend`/`EpistemicLabelView`)

`uncertaintyDisplayPolicy` ∈ {`sempreRotular`, `rótuloCompacto`, `aparatoCompleto`} — **nunca "omitir"** (invariante 7). A incerteza aparece como **faixa/margem** com **redundância não-cromática** (forma + texto + posição, **não só cor** — R-14). No modo estudante o rótulo é **compacto**, mas **presente**; no modo professor, o aparato é completo.

### 11.2 Publicabilidade e gating (`GatingNotice`)

`publicabilityStatus` (1–5) e `gatingReason` (editorial | científico | licença | revisão-humana | geometria | mídia | fonte | legal) são **LIDOS e repassados**, nunca alterados. Itens `pending`/`legal-review`/`rejected` **nunca** aparecem como **fato** (invariante 10; R-23): no máximo como **status** no modo professor. `sceneCompletenessLevel` (`rascunho` | `gabarito-interno` | `publicável`) é respeitado — uma cena `gabarito-interno` **não** é exibida ao aluno como pública.

### 11.3 Mediação (`MediationControl`)

Conteúdo sensível (escravidão, colonização, genocídio, ditadura, raça e ciência, evolução humana, mudanças climáticas, pandemias) só chega ao aluno **sob mediação**: o `MediationControl` materializa o `MediationScript`, mantém `hiddenMediaNote` (o que fica oculto por padrão), respeita `teacherMediationLevel` e **gate antes** da exibição (invariante 9; R-06). A escolha conservadora prevalece (PE-Ed4): na dúvida, **restringe-se, rotula-se ou exige-se mediação**.

### 11.4 Anacronismo e falsa equivalência

`AnachronismNotice` e `EquivalenceWarningNotice` repassam `anachronismWarnings`/`equivalenceWarnings` (E5 §9) e o peso de `weightedClaimSets`. A UI **nunca** suprime o aviso de anacronismo (fronteiras atuais sobre o passado; paleoposição ≠ atual) nem cria **falsa equivalência visual** (R-13): negacionismo e desinformação recebem **rótulo de rejeição**, fora do par de claims (PE-Ed3/PE-Ed5).

### 11.5 Acessibilidade como fundação (`AccessibilityControl`)

A acessibilidade é **requisito estrutural** (invariante 17; P24; e-MAG/WCAG/LBI), não opção:

| Requisito | Exibição conceitual |
|---|---|
| **Equivalente textual** | globo/mapa **e** timeline têm descrição textual (o que/onde/quando/confiança) — R-18 |
| **Navegação por teclado** | sem depender de mouse; sem armadilhas de foco |
| **Foco visível** | borda ≥ 2px; ordem lógica de leitura |
| **Redundância não-cromática** | rótulos nunca **só** por cor (R-14) |
| **Leitura por sequência lógica** | ordem semântica clara para leitor de tela |
| **Modo estático** | `StaticFallbackView` acessível; respeita `prefers-reduced-motion` |
| **Modo projetor acessível** | alto contraste, baixa densidade legível |
| **Legendas/transcrições** | para vídeo/áudio |
| **Controle de densidade** | reduz overload cognitivo (R-21) sem perder fonte/incerteza |

> **Limite (Tarefa 11).** Esta seção define **requisitos conceituais** de acessibilidade, **não** telas, componentes acessíveis concretos nem verificação técnica (e-MAG/WCAG, ASES). A implementação e a auditoria de acessibilidade são da Etapa 11/14.

---

## 12. Relação com `PedagogicalOutput`, `Scene` v1.1, `MomentResult` e `Knowledge Core` (Tarefa 12)

### 12.1 O que a UX pode usar (e como)

| Origem | A UX **usa** | A UX **nunca** |
|---|---|---|
| **`PedagogicalOutput`/`OutputArtifact`/`OutputSectionBlock`** | renderiza no `PedagogicalOutputViewer`; respeita `blockRole`/`visibilityClass`/`requiresMediation` | reabre a forma; recria artefato; muda tipo |
| **`OutputCitationBundle`/`SourceEvidenceCard`** | exibe fonte/evidência no `SourceEvidencePanel` | reproduz conteúdo licenciado (1.1); inventa atribuição |
| **`OutputComplianceSummary`** | configura modo/visibilidade/acessibilidade | relaxa faixa/sensíveis/acessibilidade |
| **`OutputConstraintWarning`** | exibe aviso de não-cabimento | altera o plano (E7) |
| **`Scene` v1.1** | renderiza `timelineBehavior`/`globeBehavior`/`dossierBehavior`/`simultaneityBehavior`; respeita `paleoPositionPolicy`/`gatingReason`/`sceneCompletenessLevel` | promove `generatedSceneCandidate`/`gabarito-interno` a público; reescreve a cena |
| **`MomentResult`** | exibe simultaneidade, anacronismo, equivalência | apaga simultaneidade; suprime aviso |
| **`Knowledge Core`** | cita `Claim`/`Source`/`ClaimSet`/`WeightedClaim` por REF, com rótulos | cria/edita claim, fonte, relação |

### 12.2 Regras sobre cenas, dossiês e o KC

- A UX **organiza e apresenta**; o conteúdo factual vem **somente** por REF. Ela **não volta ao KC para criar conteúdo novo** (regra de fundação).
- `sceneCompletenessLevel` e `publicabilityStatus` são **respeitados**: o que é `rascunho`/`gabarito-interno`/`pending`/`rejected` **não** é exibido ao aluno como fato.
- Rastreabilidade visual: de qualquer artefato exibido chega-se ao `OutputSectionBlock` → claim/cena/dossiê/fonte (invariante 15), em **qualquer** modo.

### 12.3 Exemplos conceituais (alinhados aos das Etapas 5/6/7/8/9)

| Recorte | Como a UX apresenta | Cautela exibida |
|---|---|---|
| **1789 (França)** | timeline foca −211 (≈1789); globo foca a França + marcadores; **simultaneidade**: Brasil colonial, EUA pós-independência, ciência/economia coevas; `gatingReason = editorial` | `AnachronismNotice` (fronteiras/nações atuais); não apagar indígenas/escravizados (Leis 10.639/11.645) |
| **GOE / ~2,4 Ga** | timeline em **Ga** (faixa, bordas difusas); globo **esquemático** (paleomapa rotulado como reconstrução); `OceanographicState`/`AtmosphereState` como overlays | reconstrução **≠ foto** (R-02); `paleoPositionPolicy` (continentes ≠ atuais); `gatingReason = científico` |
| **K-Pg / ~66 Ma** | `triggerItem` (impacto) + **`cascadeStructure`** com gradiente de confiança; globo com propagação **didática** (rótulo); `weightedClaimSets` (impacto ≫ Deccan) | sem determinismo; `paleoPositionPolicy` ("México" não existia em 66 Ma); aves ≠ todos dinossauros |
| **Clima moderno** | timeline contemporânea + projeção (cenário/modelo rotulado); globo com `States` climáticos | **consenso ≠ negação** (`EquivalenceWarningNotice`; negacionismo rotulado-rejeitado, fora do par) |
| **Recorte Brasil/ES (local)** | lente regional sobre o recorte do Planning; simultaneidade global preservada | recorte local **≠** apagamento do mundo (D8); contexto ≠ núcleo (R-12) |

---

## 13. Riscos de UX, educacionais, jurídicos, editoriais e operacionais (Tarefa 13)

| # | Risco | Mitigação |
|---|---|---|
| **R-01** | UX esconder incerteza para ficar bonita | `uncertaintyDisplayPolicy` nunca "omitir"; `UncertaintyLegend` sempre presente (invariante 7; Seção 11.1) |
| **R-02** | UX transformar reconstrução modelada em "foto" | `EpistemicLabelView` rotula "reconstrução modelada"; nunca "foto" (Seção 8.4; Seção 7.1) |
| **R-03** | UX mostrar paleogeografia como certeza | `paleoPositionPolicy` + rótulo de reconstrução; `ModernCorrespondence` distingue atual × paleoposição (Seção 7.1) |
| **R-04** | UX apagar simultaneidade global | `simultaneityVisible = sim` por padrão; foco não suprime o mundo coevo (D8; Seção 6.3) |
| **R-05** | UX virar slideshow linear e perder navegação | timeline + globo navegáveis em qualquer modo; modo não congela o eixo (Seção 6.3) |
| **R-06** | UX expor conteúdo sensível ao aluno | `MediationControl` gate antes; gráfico oculto por padrão; escolha conservadora (PE-Ed4; invariante 9) |
| **R-07** | UX vazar conteúdo `teacherOnly` | `visibilityClass`/`SchoolUseMode = teacher`; face do aluno nunca recebe aparato (Seção 9.1) |
| **R-08** | UX permitir professor editar claim | `ArtifactEditor` edita só a forma; claim/fonte bloqueados (invariante 20; Seção 10.1) |
| **R-09** | UX permitir professor burlar compliance | piso da Compliance só endurece; tentativa de relaxar faixa/sensível/visibilidade é bloqueada (invariante 5) |
| **R-10** | UX tratar BNCC como selo oficial | índice BNCC exibido como **alinhamento**, com nota "alinhamento ≠ homologação ≠ PNLD" (invariante 12) |
| **R-11** | UX sugerir aprovação MEC/PNLD | nenhum selo/texto de homologação; nota explícita no viewer e no `ExportPackage` (invariante 13; Seção 10.3) |
| **R-12** | UX confundir contexto com núcleo curricular | `curricularRole` herdado e exibido; contexto/enriquecimento rotulado como tal (Seção 9.4; Seção 12.3) |
| **R-13** | UX gerar falsa equivalência visual | `EquivalenceWarningNotice` + `weightedClaimSets`; negacionismo rotulado-rejeitado, fora do par (PE-Ed5; Seção 8.3) |
| **R-14** | UX usar só cor para confiança/incerteza | redundância não-cromática (forma + texto + posição) obrigatória (e-MAG/WCAG; Seção 11.5) |
| **R-15** | UX não funcionar sem 3D | `ViewDegradationLadder`: 2D e estático preservam o piso epistêmico (invariante 16; Seção 7.2) |
| **R-16** | UX não funcionar em projetor | `ProjectorModeView` (alto contraste, baixa densidade) preserva fonte/incerteza (Seção 9.2) |
| **R-17** | UX não funcionar offline | `OfflineModeView` (pacote local) preserva o piso epistêmico (Seção 9.3) |
| **R-18** | UX ser inacessível para leitor de tela | equivalente textual de globo/mapa **e** timeline; navegação por teclado; foco visível (P24; Seção 11.5) |
| **R-19** | UX perder fonte/citação no modo estudante | rótulo compacto de fonte/incerteza **sempre visível** ao aluno (Seção 8; Seção 9.1) |
| **R-20** | UX perder fonte/citação no modo exportado | `ExportPackage` carrega fonte/citação obrigatoriamente (Seção 10.3) |
| **R-21** | UX criar overload cognitivo | controle de densidade; aparato sob demanda; faixa de linguagem respeitada (Seção 11.5) |
| **R-22** | UX infantilizar demais conteúdo de EM | `languageLevel` por faixa (15-17 ≠ 6-8); profundidade adequada ao EM (E6 §7; Seção 9.1) |
| **R-23** | UX mostrar `pending` como fato | publicabilidade 1–5 respeitada; `pending`/`legal-review`/`rejected` nunca como fato ao aluno (invariante 10; Seção 11.2) |
| **R-24** | UX transformar free exploration em trilha curricular | exploração rotulada como exploração; sem indexação BNCC obrigatória nem selo (invariante 11; Seção 9.4) |
| **R-25** | UX permitir exportar material sem aviso de mediação | `ExportPackage` exige aviso de mediação quando há sensível (Seção 10.3) |
| **R-26** | UX apagar cobertura afro/indígena ao "limpar" a tela | cobertura das Leis 10.639/11.645 como `curricularCore` estrutural, não nota de rodapé; simultaneidade preservada (Seção 12.3) |
| **R-27** | UX tratar IA como fonte | adaptação de linguagem (forma) ≠ autoria de fato; nenhuma resposta de IA como evidência (invariante 14; Seção 3) |
| **R-28** | UX capturar dados pessoais de aluno indevidamente | nada de PII de aluno na sessão/offline/exportação; minimização (LGPD Art. 14/ECA); fica para a engenharia de privacidade da Etapa 11 |
| **R-29** | UX exibir `gabarito-interno`/`generatedSceneCandidate` como público | `sceneCompletenessLevel`/`reviewStatus` respeitados; não-publicável não chega ao aluno (Seção 11.2; Seção 12.2) |
| **R-30** | UX quebrar a rastreabilidade até a evidência | trilha visual artefato → bloco → claim/cena/dossiê/fonte preservada em todo modo (invariante 15; Seção 12.2) |

---

## 14. Fronteiras com as Etapas 11–14 (Tarefa 14)

| Etapa | Papel | Onde a Etapa 10 termina |
|---|---|---|
| **Etapa 11 — Arquitetura técnica** | persistência, versionamento, **cache/validade**, APIs, **permissões e segurança** técnicas, **engenharia de privacidade** (LGPD/menores), isolamento físico de licenças SA/ODbL, escolha de engine/biblioteca/formato | a Etapa 10 é conceitual; **não** define stack, banco, API, versionamento, cache, motor 3D, biblioteca de timeline nem formato de exportação |
| **Etapa 12 — MVP** | escolhe o **recorte mínimo** de modos/vistas/artefatos para o primeiro corte | a Etapa 10 não propõe MVP |
| **Etapa 13 — Pipeline de ingestão** | alimenta os candidatos com **dados reais**, snapshots, validação e confirmação de licença por asset | a Etapa 10 só **apresenta** o que já existe; não faz ingestão nem povoa |
| **Etapa 14 — Operação, governança, QA e escala** | testa com professores, escola, jurídico e comercial; **analytics**, **LMS**, QA pedagógico, auditoria de acessibilidade (ASES), decisão sobre PNLD/compra pública | a Etapa 10 não cria analytics/LMS, não opera, não valida nem promete adoção/homologação |

> A Etapa 10 **não executa** nenhuma dessas. Ela entrega a **gramática conceitual da experiência/UX 3D**; tudo a montante e a jusante pertence às etapas próprias.

---

## 15. Encerramento e handoff para a Etapa 11 (Tarefa 15)

### 15.1 O que esta etapa entrega

A Etapa 10 entrega a **arquitetura conceitual da `DesignUX3DLayer`**: a definição da camada como **apresentação e operação** do `PedagogicalOutput`, no topo da experiência, externa ao Knowledge Core; sua posição na direção única de dependência (acima do Output); a matriz de entradas (com `pedagogicalOutputRef` como âncora e `outputStatus`/`deviceCapability` governando exibição e degradação); trinta entidades conceituais externas e distintas das do KC, da Compliance, do Planning, do Matching e do Output (incluindo `DesignUX3DLayer`, `ExperienceSession`, `ExperienceMode`, `ViewerRole`, `NavigationState`, `TimelineView`, `Globe3DView`, `Map2DView`, `StaticFallbackView`, `ProjectorModeView`, `OfflineModeView`, `ComparisonView`, `TeacherWorkspace`, `StudentWorkspace`, `FreeExplorationView`, `PedagogicalOutputViewer`, `ArtifactEditor`, `ApprovalWorkflow`, `ExportPackage`, `DossierPanel`, `SourceEvidencePanel`, `EpistemicLabelView`, `UncertaintyLegend`, `GatingNotice`, `MediationControl`, `AccessibilityControl`, `AnachronismNotice`, `EquivalenceWarningNotice`, `ViewDegradationLadder` e `UXAuditTrail`); os dicionários conceituais de `ExperienceSession`/`NavigationState`/`ViewDegradationLadder`/`GatingNotice`/`AnachronismNotice`/`EquivalenceWarningNotice`; a taxonomia de dez `experienceMode` com classificação por público (professor/estudante/misto); os vinte invariantes da camada; a timeline multiescala (Big Bang ao presente e ao projetivo; regime profundo em Ga/Ma, histórico em BCE/CE, contemporâneo e projetivo; `canonicalTimeScalar` para ordenar e `displayTime` para exibir; comportamentos distintos de `Event`/`Process`/`State`/`cascadeStructure`; incerteza temporal rotulada; simultaneidade preservada); o globo/mapa 3D e a escada de degradação 3D → 2D → estático → offline → projetor com **piso epistêmico** preservado e paleogeografia rotulada como reconstrução modelada (`paleoPositionPolicy`/`ModernCorrespondence`); os painéis de dossiê, fonte e evidência com honestidade epistêmica visível (`EpistemicLabelView`, `UncertaintyLegend`, distinção fato/inferência/hipótese/interpretação/reconstrução/aproximação/negacionismo-rejeitado); a separação professor/estudante por `visibilityClass`/`studentFacingMode`/`teacherMediationLevel`/`SensitiveContentRule`/`MediationScript`/`AgeSuitability`/`AllowedUseContext`; os modos projetor, offline e exploração livre; a revisão/edição/aprovação/exportação (edição **só da forma**, `OutputRevisionNote`, `ApprovalWorkflow` externo, `ExportPackage` conceitual com avisos obrigatórios); a acessibilidade como fundação (e-MAG/WCAG/LBI); a relação de apresentação — nunca de reabertura — com o Output, a `Scene` v1.1, o `MomentResult` e o KC (com exemplos: 1789; GOE; K-Pg; clima moderno; recorte Brasil/ES); e trinta riscos com mitigação. Nada aqui cria conteúdo, stack, MVP, ingestão, cena nova, dossiê novo, claim, fonte ou mapeamento BNCC; nada altera claims, `reviewStatus`, `publicabilityStatus`, `matchSetStatus`, `outputStatus` ou `sceneCompletenessLevel`; nada usa IA como fonte factual ou dado pessoal de aluno; nada relaxa LGPD, acessibilidade ou conteúdo sensível; nada promete homologação MEC/PNLD; e nada trata recurso complementar como substituto do currículo. A direção única de dependência permanece invertida: **Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core**.

### 15.2 O que a Etapa 11 deverá fazer

A **Etapa 11 — Arquitetura técnica** receberá a gramática conceitual da experiência e definirá a **fundação técnica** que a sustenta: **persistência** (de sessões, anotações de forma, pacotes de exportação e estados de aprovação — tudo externo e descartável, sem contaminar o KC), **versionamento**, **cache e validade** dos artefatos e das vistas, **APIs**, **permissões e segurança** técnicas, **engenharia de privacidade** (LGPD Art. 14/ECA, minimização de dados de menores), **isolamento físico** de licenças ShareAlike/ODbL, e a escolha de **engine 3D, biblioteca de timeline, projeção cartográfica e formato de exportação** — sem reabrir a forma, a seleção, a conformidade ou a verdade, e preservando os vinte invariantes e o piso epistêmico desta camada em qualquer modo (3D → 2D → estático → offline → projetor).

### 15.3 O que a Etapa 10 ainda **não** fez (e por quê)

Não definiu stack, persistência, versionamento, cache/validade, APIs, permissões técnicas, segurança técnica, engenharia de privacidade, engine 3D, biblioteca de timeline nem formato de exportação (Etapa 11); não propôs MVP (Etapa 12); não fez ingestão nem povoou (Etapa 13); não criou analytics, LMS, QA operacional, auditoria técnica de acessibilidade (ASES) nem validou/prometeu adoção/homologação (Etapa 14); não desenhou telas finais de alta fidelidade, layouts, componentes prontos nem fluxo concreto de implementação; não criou cena, dossiê, `Claim`, `Source` nem qualquer conhecimento; não promoveu cena/`gabarito-interno`/`generatedSceneCandidate` a público; não mapeou BNCC; não alterou `reviewStatus`/`publicabilidade`/`matchSetStatus`/`outputStatus`/`sceneCompletenessLevel`/`MatchScore`; não usou IA como fonte factual; não usou dado pessoal de aluno; e não relaxou LGPD, acessibilidade nem conteúdo sensível. Tudo isso é contingente ou pertence a etapas próprias; a UX permanece **camada de apresentação e operação** externa ao núcleo.

**Handoff:** com a Etapa 10 (v1.0) aprovada, a **Etapa 11 — Arquitetura técnica** pode ser executada, recebendo a gramática conceitual da experiência/UX 3D desta camada e definindo a arquitetura técnica, a persistência, o versionamento, as APIs, as permissões, a segurança, a privacidade e o cache/validade que a sustentam — preservando os vinte invariantes, o piso epistêmico, a degradação graciosa, a separação professor/estudante, a acessibilidade como fundação e a rastreabilidade até claims/fontes/cenas/dossiês, sem reabrir a forma, a seleção, a conformidade ou a verdade. O resíduo curatorial herdado das Etapas 6/8/9 permanece: os `BNCCMapping`/`CurricularAlignment` concretos seguem `pending` até confirmação com o texto homologado (F1) — a UX os **exibe como alinhamento, resume e respeita o `reviewStatus`**, sem resolvê-los nem transformá-los em selo.

*Documento de entrega da Etapa 10 (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8, 9). Define somente a gramática conceitual da experiência/UX 3D. Não modela novos dados do núcleo, não escreve código, não propõe MVP, não define stack, não define engine 3D nem biblioteca de timeline, não desenha telas finais de alta fidelidade, não cria cena nova, não cria dossiê novo, não promove cena a público, não mapeia BNCC, não povoa o Knowledge Core, não altera claims, não usa IA como fonte factual e não usa dados pessoais reais de alunos. Próxima etapa, quando solicitada: Etapa 11 — Arquitetura técnica.*
