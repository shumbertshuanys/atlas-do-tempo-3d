# Etapa 9 — Pedagogical Output Layer

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 9** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1) e o `ContentMatchingEngine` (Etapa 8, v1.0) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura conceitual** da camada de saída pedagógica. Define **somente a gramática dos artefatos pedagógicos** — os tipos, campos, contratos, regras de transformação, invariantes, fronteiras e riscos da conversão de um `MatchSet` revisado em material utilizável por professor e/ou estudante. Conforme solicitado, esta etapa **não** cria um plano de aula real para uma turma específica (apenas exemplos mínimos e esquemáticos); **não** cria `Claim`, `Source`, `Scene`, `ClaimSet`, `Relationship` nem qualquer conhecimento do núcleo; **não** altera `reviewStatus`, `publicabilityStatus`, `confidenceLevel`, `evidenceLevel`, `claimType`, `UncertaintyProfile`, `BNCCMapping`, `CurricularAlignment`, `PlanningProfile`, `ComplianceProfile`, `MatchScore` nem `ExclusionReason`; **não** reabre ranqueamento, elegibilidade, conformidade, planejamento nem verdade factual; **não** promove conteúdo `pending`; **não** usa IA como fonte factual; **não** inventa fatos; **não** substitui o professor; **não** promete homologação MEC nem aprovação PNLD; **não** trata recurso complementar como currículo oficial; **não** cria UX/telas finais (Etapa 10); **não** define stack técnica, persistência, versionamento ou APIs (Etapa 11); **não** propõe MVP (Etapa 12); **não** faz ingestão/povoamento (Etapa 13); **não** define operação, governança, QA, escala, analytics ou LMS (Etapa 14); e **não** usa dados pessoais reais de alunos.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Blocos ```txt``` são **dicionário conceitual, nunca código executável**. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6). "O Planning" = a `TeacherSchoolPlanningLayer` (Etapa 7). "O Matching" = o `ContentMatchingEngine` (Etapa 8). "O Output" = a `PedagogicalOutputLayer` definida na Seção 1.

> **Regra de fundação desta etapa.** O Output é **transformador de forma**, externo ao Knowledge Core. Ele nunca cria, edita ou altera conhecimento; nunca reabre seleção, conformidade ou verdade. Ele consome o `MatchSet` (Etapa 8) e o reorganiza em artefatos pedagógicos, **preservando integralmente** os rótulos de tipo de claim, confiança, evidência, incerteza, anacronismo, equivalência, publicabilidade, gating, mediação e acessibilidade que já vieram decididos a montante. A direção única de dependência permanece invertida: **Experience → Output → Matching → Planning → Compliance → Knowledge Core**. O Output aponta para dentro; o KC, a Compliance, o Planning e o Matching nunca apontam para o Output (Etapa 2, §10; P1/P2).

---

## Sumário

1. Definição da `PedagogicalOutputLayer`
2. Papel da camada na arquitetura geral
3. Entradas da camada de Output
4. Entidades conceituais da camada
5. Tipos de artefato pedagógico
6. Estrutura do `PedagogicalOutput`
7. Regras de transformação do `MatchSet` em saída
8. Relação com `PlanningProfile` e intenção docente
9. Relação com a `BrazilianEducationComplianceLayer`
10. Relação com o `ContentMatchingEngine`
11. Relação com `WhatWasHappeningAtMoment`, `MomentResult`, `Scene` v1.1 e dossiês
12. Adequação por faixa etária, linguagem, mediação e acessibilidade
13. Riscos pedagógicos, jurídicos, editoriais e operacionais
14. Fronteiras com as Etapas 10–14
15. Encerramento e handoff para a Etapa 10

---

## 1. Definição da `PedagogicalOutputLayer` (Tarefa 1)

### 1.1 Natureza

A **`PedagogicalOutputLayer`** é a **camada externa** que **transforma uma seleção curada, justificada e conforme — o `MatchSet` revisado da Etapa 8 — em artefatos pedagógicos utilizáveis por professor e/ou estudante**: plano de aula, roteiro de exploração, sequência didática, atividade orientada, perguntas de discussão, quiz, avaliação formativa, rubrica, material do aluno, guia do professor, roteiro de mediação, ficha de fonte/evidência, dossiê pedagógico, comparação antes/depois e síntese por faixa etária. Ela é a **dobradiça entre a seleção e a forma**: o Matching decide *o que entra e com qual papel*; o Output decide *em que forma pedagógica isso aparece*.

Três consequências estruturais, herdadas das etapas anteriores:

1. **É contingente, não universal.** Diferente do KC (universal e estável — Etapa 2, §10.2), um artefato pedagógico é sempre relativo a *um* `MatchSet`, *um* planejamento, *um* perfil de conformidade e *um* contexto de turma. Por isso o Output **nunca entra no núcleo**: vive por fora, como registro próprio que **aponta para** o `MatchSet`, as cenas, os dossiês, os claims e as fontes por identificador estável (P1/P2).
2. **É transformação de forma, não criação de conteúdo.** O Output **não cria nem altera** conhecimento. Ele lê o que o Matching já selecionou, **reorganiza** os itens em blocos pedagógicos, **adapta a linguagem** à faixa, **monta** a sequência e **preserva** a cadeia de referência e os rótulos epistêmicos. Toda criação/edição/aprovação de conteúdo permanece sob curadoria humana (Etapas 4x/13); toda decisão de seleção permanece do Matching (Etapa 8); toda decisão de conformidade permanece soberania da Compliance (Etapa 6) e da política editorial (Etapa 3.1).
3. **Existe apenas a jusante de uma seleção.** O Output **exige um `MatchSet` como entrada**. Não há saída pedagógica sem seleção prévia: o Output **não** vai ao KC selecionar conteúdo por conta própria, salvo para **resolver referências já presentes** no `MatchSet` (ex.: buscar o texto curto de um `Claim` que o `ClaimMatch` já referenciou). A exploração livre **pura** (`usoLivreExploratorio`, sem `PlanningProfile` e, portanto, sem `MatchSet` — E0 D3; E7 §2.1; E8 §1.1) **não passa pelo Output**: vai do KC à experiência sob o filtro de adequação da Compliance.

### 1.2 As perguntas que a camada responde

| # | Pergunta | O que produz |
|---|---|---|
| 1 | **Em qual forma pedagógica este `MatchSet` deve ser entregue?** | `outputType` + `OutputArtifact` |
| 2 | **Onde cada item selecionado entra no artefato?** | `artifactSections` (blocos com papel pedagógico) |
| 3 | **O que vai para o aluno e o que vai só para o professor?** | `studentFacingMode` + `visibilityClass` herdada |
| 4 | **Em que linguagem e profundidade isso aparece?** | `languageLevel` + `targetAgeRange` (sem alterar o fato) |
| 5 | **Como o conteúdo sensível é tratado no artefato?** | `sensitiveContentHandling` + `MediationScript` |
| 6 | **Como as fontes e a incerteza aparecem?** | `OutputCitationBundle` + `SourceEvidenceCard` + rótulos preservados |
| 7 | **O que é núcleo, o que é contexto, o que é enriquecimento?** | herança de `curricularRole` do Matching nos blocos |
| 8 | **A conformidade está resumida e respeitada no artefato?** | `OutputComplianceSummary` |
| 9 | **O artefato cabe no tempo e nas restrições do plano?** | ajuste de densidade + `OutputConstraintWarning` quando não couber |
| 10 | **De onde veio cada bloco (rastreabilidade)?** | `OutputAuditTrail` |

### 1.3 O que a camada **não** decide

O Output **não decide a verdade dos fatos**: não arbitra consenso, não pondera controvérsias, não rotula evidência, não promove cena a gabarito, não reordena a verdade do núcleo (KC, Etapa 3.1, curadoria). O Output **não refaz a seleção**: não recalcula `MatchScore`, não reabre `ExclusionReason`, não inclui itens que o Matching excluiu, não promove `enrichment` a `curricularCore` (Etapa 8). O Output **não redefine a conformidade**: aplica as regras da Compliance, sem afrouxá-las nem inventá-las (Etapa 6). O Output **não altera o planejamento**: preserva objetivo, série, disciplina, duração e profundidade do `PlanningProfile`, sem reescrevê-los (Etapa 7). A adaptação de linguagem organiza **a forma**; **forma não altera fato** (Seção 12).

### 1.4 O que a camada produz

A camada produz o **`PedagogicalOutput`** (Seção 6): um ou mais artefatos pedagógicos derivados de um único `MatchSet`, cada um com seu `outputType`, suas seções (`artifactSections`), seu pacote de citações (`OutputCitationBundle`), seu resumo de conformidade (`OutputComplianceSummary`), sua trilha de auditoria (`OutputAuditTrail`) e seu `outputStatus`. O `PedagogicalOutput` é o objeto que a **Etapa 10 (Design/UX)** recebe para que professor e estudante o **visualizem, editem, aprovem, exportem e naveguem**. O Output **para no artefato**; não desenha tela, não persiste dado, não define API (Seções 13 e 14).

---

## 2. Papel da camada na arquitetura geral (Tarefa 2)

### 2.1 Posição

```
Experience → OUTPUT (esta camada) → Matching → Planning → Compliance → Knowledge Core
        (cada camada aponta para dentro; o KC não conhece nenhuma delas)
```

O Output senta **entre** o Matching (que lhe entrega o `MatchSet` selecionado/justificado/conforme) e a futura Experience/UX (Etapa 10, que recebe o `PedagogicalOutput`). Para baixo, ele lê o `MatchSet` e, por referência, o KC, a Compliance, o Planning e a saída da função; para cima, alimenta a Etapa 10. Apagar o Output inteiro **não deixa campo órfão** a montante (teste de P2): o KC, a Compliance, o Planning e o `MatchSet` permanecem intactos.

### 2.2 O que o Output é (e o que não é)

| O Output é… | O Output **não** é… |
|---|---|
| **transformador de forma** de uma seleção curada | autor de fatos; nunca escreve `Claim`/`Source`/`Scene`/`reviewStatus` |
| **consumidor do `MatchSet`** (E8) | seletor de conteúdo bruto; não vai ao KC escolher por conta própria |
| **consumidor do planejamento** (`PlanningProfile`/intenção docente) | autor da intenção; não inventa objetivo, série nem duração |
| **consumidor da conformidade** (perfis e anotações da E6) | definidor de conformidade; não cria `AgeSuitability`/`SensitiveContentRule`/`BNCCMapping` |
| **montador de artefatos** (plano, roteiro, atividade, quiz, rubrica, material) | implementador de UX/telas (E10), stack/persistência (E11), MVP (E12), pipeline (E13) ou operação/LMS (E14) |
| **preservador de rastreabilidade e rótulos** | árbitro de verdade; não pondera consenso nem promove cena a gabarito |

### 2.3 Divisão de responsabilidades (quem decide o quê)

| Camada | Decide | Não decide |
|---|---|---|
| **Knowledge Core (E2)** | o que é conhecimento (claims tipados, fonteados, com confiança/incerteza) | currículo, faixa, planejamento, seleção, forma pedagógica |
| **Compliance (E6)** | regras de conformidade (faixa, sensíveis, acessibilidade, alinhamento BNCC, modos, classes de uso) | a verdade do fato; a intenção; a seleção; a forma pedagógica |
| **Planning (E7)** | a intenção pedagógica (objetivo, tema, recorte, profundidade, modo) | a verdade; a conformidade; a seleção; a forma final |
| **Matching (E8)** | a seleção, a exclusão, o ranqueamento, o papel curricular e a justificativa | a verdade; a conformidade; a saída pedagógica final |
| **Output (E9 — esta)** | **a forma pedagógica do `MatchSet`: tipo de artefato, blocos, linguagem por faixa, citação, mediação e acessibilidade do artefato** | a verdade; a seleção; a conformidade; o planejamento; a UX/persistência |
| **Experience (E10)** | como o artefato é exibido, editado, aprovado, exportado e navegado | tudo o que está a montante |

> **Síntese.** **Planning decide intenção; Compliance decide regras; o KC contém conhecimento; o Matching seleciona; o Output dá forma pedagógica à seleção; a Experience exibe.** O Output é a dobradiça que torna a seleção utilizável em sala, sem nunca tocar nem a intenção, nem as regras, nem os fatos, nem a própria seleção.

---

## 3. Entradas da camada de Output (Tarefa 3)

Matriz de campos de entrada. Cada campo declara **definição**, **origem**, **obrigatório/opcional**, **uso no Output** e **risco se mal usado**. Os `*Ref` apontam para entidades **já definidas** nas Etapas 2/5/6/7/8; o Output **não** as recria.

| Campo (`camelCase`) | Definição | Origem | Obrig./Opc. | Uso no Output | Risco se mal usado |
|---|---|---|---|---|---|
| `matchSetRef` | REF ao `MatchSet` selecionado/justificado/conforme | Matching (E8) | **Obrigatório** | âncora de todo o artefato; sem ele não há Output | gerar saída sem seleção → conteúdo arbitrário/inventado |
| `matchSetStatusRead` | LIDO de `MatchSet.matchSetStatus` (Seção 7.1) | Matching (E8) | **Obrigatório** | governa se a saída é final ou rascunho pedagógico | tratar `revisadoPeloProfessor` como pronto → falso definitivo |
| `planningProfileRef` | REF ao `PlanningProfile` que originou a seleção | Planning (E7), via E8 | **Obrigatório** | preserva objetivo/série/duração/profundidade/modo | reescrever a intenção do professor |
| `complianceProfileRef` | REF ao `ComplianceProfile` (traz `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef`, `policyRefs[]`) | Compliance (E6), via E8 | **Obrigatório** | piso de conformidade do artefato; resume no `OutputComplianceSummary` | montar artefato fora do perfil da turma |
| `requestedOutputTypes` | quais artefatos gerar (Seção 5) | Output (`OutputRequest`) | **Obrigatório** | define quais `OutputArtifact` produzir | pedir tipo incompatível com o `MatchSet` (ex.: quiz sobre item só contextual) |
| `outputProfileRef` | REF ao `OutputProfile` (configuração da geração — Seção 4) | Output | Recomendado | empacota linguagem, citação, acessibilidade, tratamento de sensíveis | configurar saída mais permissiva que a Compliance |
| `selectedCandidatesRead` | LIDO de `MatchSet.selectedCandidates[]` (com `curricularRole`, `visibilityClass`, `requiresMediation`, `publicabilityStatus`, `gatingReason`) | Matching (E8) | **Obrigatório** | matéria-prima dos blocos; cada item vai a um `OutputSectionBlock` | mover item para bloco de papel incompatível |
| `excludedCandidatesRead` | LIDO de `MatchSet.excludedCandidates[]` (+ `relevantButExcluded`) | Matching (E8) | Opcional | informa `excludedContentPolicy` (transparência da ausência) | reincluir item excluído por porta dura |
| `coverageBalanceRead` | LIDO de `CoverageBalance` (E8 §12) | Matching (E8) | Recomendado | preserva simultaneidade global, lente Brasil, cobertura estrutural | apagar contexto/simultaneidade ao "limpar" o artefato |
| `sceneRefs` | REFs a `Scene` v1.1 / `generatedSceneCandidate` selecionadas (via `SceneMatch`) | função (E5)/curadoria (E4x), via E8 | Opcional | base de dossiê, exploração e comparação | tratar `generatedSceneCandidate` como gabarito |
| `dossierRefs` | REFs a dossiês selecionados (via `DossierMatch`) | E5/E8 | Opcional | base de `sceneDossier` e `sourceAnalysis` | reescrever o dossiê em vez de organizá-lo |
| `momentResultRefs` | REFs a `MomentResult` consultados (E5) | função (E5), via E8 | Opcional | base de "o que acontecia no mundo" e de simultaneidade no artefato | apagar simultaneidade ao escolarizar |
| `claimRefs` | REFs a `Claim`/`ClaimSet`/`WeightedClaim` elegíveis (via `ClaimMatch`) | KC (E2), via E8 | **Obrigatório** | conteúdo factual citável; preserva `claimType`/confiança/peso | parafrasear claim a ponto de mudar o fato |
| `sourceSupportRead` | LIDO de `SourceSupportSummary` (A/B por claim relevante) | E5/E8 | **Obrigatório** | alimenta `OutputCitationBundle` e `SourceEvidenceCard` | omitir fonte; inventar atribuição |
| `assessmentIntent` | intenção de avaliação declarada no Planning (E7) | Planning (E7) | Opcional | base de `QuizOutput`/`AssessmentOutput`/`RubricOutput` | avaliar fora do objetivo do plano (Seção 13, R-19) |
| `accessibilityNeeds` | necessidades que disparam `AccessibilityRequirement` (e-MAG/WCAG/LBI) | Planning (E7) → Compliance (E6) | Recomendado | requisito de acessibilidade do artefato (equivalente textual, redundância não-cromática) | excluir alunos; descumprir LBI |

> **Regra transversal de entradas.** Campos textuais do professor herdados do Planning (`theme`, `teacherObjective`, `teacherNotes`, `localContext`, `assessmentIntent`) são **intenção**, nunca `Claim` factual. O Output os usa para organizar e contextualizar o artefato, sob rótulo explícito de "intenção do professor"; jamais os promove a fato nem os escreve no KC. O conteúdo factual do artefato vem **somente** de `claimRefs`/`sceneRefs`/`dossierRefs`/`momentResultRefs` já presentes no `MatchSet`.

---

## 4. Entidades conceituais da camada (Tarefa 4)

Entidades **externas ao Knowledge Core, distintas das entidades da Compliance, do Planning e do Matching**. Nenhuma é, vira ou recria entidade do núcleo, da Etapa 6, da Etapa 7 ou da Etapa 8. As entidades de Output **referenciam** as demais por ID; não as duplicam. Apagar qualquer uma delas não altera um único campo do KC.

| Entidade (`CamelCase`) | Papel | Para que aponta | Observação de fronteira |
|---|---|---|---|
| **`PedagogicalOutputLayer`** | a camada que transforma `MatchSet` em artefatos pedagógicos | `MatchSet`, `PlanningProfile`, `ComplianceProfile` | transforma forma; nunca cria conteúdo |
| **`OutputProfile`** | consolida a **configuração** de uma geração de saída (linguagem, citação, acessibilidade, sensíveis) | parâmetros de forma | é a configuração; não é o artefato |
| **`OutputRequest`** | pedido de geração de um ou mais artefatos a partir de um `MatchSet` | `matchSetRef`, `requestedOutputTypes` | aciona o Output; não executa seleção |
| **`PedagogicalOutput`** | o **conjunto** de artefatos derivados de um único `MatchSet` | `OutputArtifact[]` | é o objeto entregue à Etapa 10 |
| **`OutputArtifact`** | **supertipo** de um artefato pedagógico individual | `artifactSections`, `claimRefs`, `sceneRefs` | os tipos específicos abaixo o especializam |
| **`OutputSectionBlock`** | um **bloco** do artefato, com papel pedagógico e visibilidade | itens do `MatchSet` por ID | unidade de montagem; herda `curricularRole`/`visibilityClass` |
| **`LessonPlanOutput`** | plano de aula (professor) | objetivo, sequência, blocos, mediação, avaliação | não promete homologação MEC/PNLD |
| **`SequencePlanOutput`** | sequência didática multi-aula (professor) | conjunto ordenado de `LessonPlanOutput`/blocos | preserva coerência temporal; não altera o plano |
| **`ExplorationGuideOutput`** | roteiro de exploração no atlas (misto) | cenas, momentos, navegação sugerida | preserva simultaneidade global (D8) |
| **`StudentMaterialOutput`** | material do aluno (estudante) | blocos voltados ao aluno | nunca expõe `teacherOnly`/`pending`/sensível sem mediação |
| **`TeacherGuideOutput`** | guia do professor (professor) | aparato completo, "como sabemos", notas de mediação | acesso ao aparato; não vaza ao aluno como fato |
| **`ActivityOutput`** | atividade orientada (misto/estudante) | tarefa baseada em itens centrais | não cria atividade sobre item só contextual |
| **`QuizOutput`** | quiz de checagem (misto/estudante) | itens factuais elegíveis | não avalia hipótese como fato (preserva `claimType`) |
| **`AssessmentOutput`** | avaliação formativa (professor/misto) | itens alinhados ao `assessmentIntent`/objetivo | sem base no objetivo do Planning → não gera |
| **`RubricOutput`** | rubrica de avaliação (professor) | critérios derivados do objetivo | não cria critério fora do objetivo |
| **`DiscussionPromptOutput`** | perguntas disparadoras de discussão (misto) | itens centrais/controvérsias legítimas | não transforma negacionismo em "lado" |
| **`SourceEvidenceCard`** | ficha de fonte/evidência ("como sabemos isso") | `Source`/`Citation`/`SourceSupportSummary` | nunca inventa atribuição; respeita licença |
| **`MediationScript`** | roteiro de mediação do professor para tema sensível | `SensitiveContentRule`/`TeacherMediationRequirement` | a camada registra; o professor media |
| **`AgeAdaptedExplanation`** | explicação adaptada à faixa (a forma, nunca o fato) | `Claim`/`ClaimSet` + `AgeLanguageProfile` | adapta linguagem; preserva rótulos epistêmicos |
| **`ComparisonOutput`** | comparação antes/depois ou A×B (misto) | par de `Scene`/States via relações | sem falsa simetria; confiança decaindo |
| **`HomeworkOutput`** | tarefa de casa (estudante, eventual offline) | itens conservadores | sensível restrito sem professor (sobe-se o cuidado) |
| **`ProjectBriefOutput`** | briefing de projeto interdisciplinar (misto) | itens de múltiplas camadas 4A | conforme o tema mais sensível |
| **`OutputCitationBundle`** | pacote de citações/atribuições do artefato | `Source`/`Citation`/`provenanceRef` | citação ≠ reprodução; respeita 1.1/licença |
| **`OutputComplianceSummary`** | resumo de conformidade aplicável ao artefato | `ComplianceProfile`/`AllowedUseContext`/`SchoolUseMode`/`AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement`/`BNCCMapping` | lê e resume; nunca redefine |
| **`OutputConstraintWarning`** | aviso de que o artefato não cabe na restrição do plano (tempo/recurso/faixa) | `TimeBudget`/`ResourceConstraint`/`AgeSuitability` | **avisa**, não modifica o plano (E7) |
| **`OutputRevisionNote`** | nota de revisão do professor sobre o artefato | o `OutputArtifact` | externa e descartável; não altera o `MatchSet` |
| **`OutputAuditTrail`** | trilha de auditoria de entradas, decisões de forma e referências | refs de entrada + decisões | externa e descartável; rastreabilidade integral |
| **`OutputStatus`** | maturidade do artefato (Seção 7.1) | o `OutputArtifact`/`PedagogicalOutput` | sexto eixo de maturidade independente |

> **`OutputAuditTrail` × `MatchingAuditTrail` × `ComplianceAnnotation` × `PlanningAnnotation`.** A `ComplianceAnnotation` (E6) anota **conformidade/legalidade**; a `PlanningAnnotation` (E7) anota **organização pedagógica do planejamento**; a `MatchingAuditTrail` (E8) registra **como a seleção foi calculada e justificada**; a `OutputAuditTrail` (E9) registra **como o artefato foi montado a partir da seleção**. As quatro são externas, apontam por ID e nunca editam o alvo; vivem em camadas diferentes e não se confundem.

> **`OutputRevisionNote` × `OutputAuditTrail`.** A `OutputRevisionNote` é a anotação **humana** do professor sobre um artefato (ajuste de ordem, observação de mediação, marca de "revisar"); a `OutputAuditTrail` é o registro **automático** de proveniência do artefato. Nenhuma altera o `MatchSet`, o KC ou a Compliance; ambas são descartáveis (removê-las não deixa rastro a montante).

---

## 5. Tipos de artefato pedagógico (Tarefa 5)

### 5.1 Taxonomia de `outputType` (lista controlada)

`lessonPlan` · `sequencePlan` · `explorationGuide` · `teacherGuide` · `studentMaterial` · `activity` · `quiz` · `formativeAssessment` · `rubric` · `discussionPrompts` · `sourceAnalysis` · `sceneDossier` · `comparisonOutput` · `homework` · `projectBrief`.

### 5.2 Tabela de tipos: destinatário, base no `MatchSet` e cautelas

| `outputType` | Destinatário | Entidade que o realiza | Base preferencial no `MatchSet` | Cautela principal |
|---|---|---|---|---|
| `lessonPlan` | **Professor** | `LessonPlanOutput` | itens `curricularCore` (foco) + `contextual` | não parecer definitivo demais; não prometer BNCC/MEC |
| `sequencePlan` | **Professor** | `SequencePlanOutput` | múltiplos focos ordenados; `schoolTerm` | não inventar progressão fora do plano |
| `explorationGuide` | **Misto** | `ExplorationGuideOutput` | `momentResultRefs` + `SceneMatch`; simultaneidade | preservar o mundo navegável (D8); não escolarizar demais |
| `teacherGuide` | **Professor** | `TeacherGuideOutput` | aparato completo + `sourceAnalysis` + mediação | conteúdo `teacherOnly` nunca vaza ao aluno |
| `studentMaterial` | **Estudante** | `StudentMaterialOutput` | itens `visívelAoAluno`; linguagem por faixa | nada `teacherOnly`/`pending`/sensível sem mediação |
| `activity` | **Misto/Estudante** | `ActivityOutput` | itens centrais com base factual sólida | não basear atividade em item só contextual/enrichment |
| `quiz` | **Misto/Estudante** | `QuizOutput` | claims `fato documentado`/`medição direta` elegíveis | não cobrar hipótese/estimativa como fato fechado |
| `formativeAssessment` | **Professor/Misto** | `AssessmentOutput` | itens alinhados ao `assessmentIntent`/objetivo | sem objetivo do Planning → não gerar |
| `rubric` | **Professor** | `RubricOutput` | critérios derivados do objetivo + competências | não criar critério fora do objetivo |
| `discussionPrompts` | **Misto** | `DiscussionPromptOutput` | itens centrais + `ClaimSet` legítimos | controvérsia legítima ≠ falsa equivalência |
| `sourceAnalysis` | **Misto** | `SourceEvidenceCard` + `OutputCitationBundle` | `SourceSupportSummary` + evidências | citar, nunca reproduzir (1.1); preservar `evidenceLevel` |
| `sceneDossier` | **Misto** | `SceneDossier` via `DossierMatch` + cartões | dossiês selecionados; "como sabemos" | preservar incerteza/anacronismo; não reescrever o dossiê |
| `comparisonOutput` | **Misto** | `ComparisonOutput` | par de cenas/States via relações | confiança decaindo; sem determinismo |
| `homework` | **Estudante** | `HomeworkOutput` | itens conservadores; eventual offline | sensível restrito sem professor; cuidado redobrado |
| `projectBrief` | **Misto** | `ProjectBriefOutput` | itens de múltiplas camadas 4A | conforme o tema mais sensível do conjunto |

### 5.3 Classificação por público

| Classe | Tipos | Regra |
|---|---|---|
| **Para professor** | `lessonPlan`, `sequencePlan`, `teacherGuide`, `rubric` | podem conter o **aparato completo** (fontes integrais, `ClaimSet` integral, notas de mediação, mídia sensível para preparação sob licença); só acessíveis em `SchoolUseMode = teacher`; **nunca** exibidos ao aluno como fato (E3.1 §9; E6 §7). |
| **Para estudante** | `studentMaterial`, `homework` | linguagem, exposição e mídia **conforme a faixa**; conteúdo gráfico oculto por padrão; sensível só `teacherMediated`/`restricted` conforme a faixa; nada `teacherOnly`/`pending`/`legal-review`/`rejected`. |
| **Mistos** | `explorationGuide`, `activity`, `quiz`, `formativeAssessment`, `discussionPrompts`, `sourceAnalysis`, `sceneDossier`, `comparisonOutput`, `projectBrief` | possuem **face do professor** (preparação/mediação) e **face do aluno** (uso em sala), separadas por `studentFacingMode` e `visibilityClass`; a face do aluno respeita a faixa, a face do professor carrega o aparato. |

> **Os 15 tipos da taxonomia ≠ as 27 entidades.** Os tipos `sequencePlan`, `sourceAnalysis`, `sceneDossier`, `comparisonOutput`, `homework` e `projectBrief` são realizados por especializações de `OutputArtifact` (`SequencePlanOutput`, etc.) e/ou pela composição de `SourceEvidenceCard`, `OutputCitationBundle` e `DossierMatch`. O `outputType` é o **rótulo de forma**; a entidade é a **estrutura**. Nenhum tipo cria conteúdo: todos reorganizam o `MatchSet`.

---

## 6. Estrutura do `PedagogicalOutput` (Tarefa 6)

Dicionários conceituais — **não são código**. Os `*Ref` apontam para entidades das Etapas 2/5/6/7/8.

### 6.1 `OutputProfile` (configuração da geração)

```txt
OutputProfile = {
  outputProfileId,
  schoolUseModeRefs,          # subconjunto de {teacher, student, free-exploration, projector, offline} (E6) — LIDO/herdado
  targetEducationStage,       # LIDO do ComplianceProfile.stageRef (E6) — não redefinido
  targetAgeRange,             # LIDO do AgeLanguageProfile via ComplianceProfile.ageProfileRef (E6)
  languageLevel,              # 6-8 | 9-11 | 12-14 | 15-17 | professor (E3.1 §6 / E6 §7) — só pode endurecer
  studentFacingMode,          # voltadoAoProfessor | voltadoAoAluno | misto
  teacherMediationLevel,      # nenhuma | baixa | media | alta | obrigatoria (derivado de SensitiveContentRule/usageScenario)
  sourceCitationPolicy,       # sempreVisível | dossieApenas | professorApenas | conformeProfundidade
  sensitiveContentHandling,   # ocultar | mediarPeloProfessor | exibirComAviso | apenasNoGuiaDoProfessor
  excludedContentPolicy,      # silenciar | registrarAusência | ofereçerComoEnriquecimentoForaDeBanda (sem reincluir excluído por porta dura)
  accessibilityRequirements,  # REFs a AccessibilityRequirement (E6) — equivalente textual, redundância não-cromática, etc.
  uncertaintyDisplayPolicy,   # sempreRotular | rótuloCompacto | aparatoCompleto (NUNCA "omitir")
  outputDensityPreference     # enxuto | padrão | aprofundado (relacionado a TimeBudget; não altera a verdade)
}
```

### 6.2 `OutputRequest` (pedido de geração)

```txt
OutputRequest = {
  outputRequestId,
  matchSetRef,                # REF ao MatchSet (E8) — âncora obrigatória
  matchSetStatusRead,         # LIDO: rascunho | calculadoPeloMotor | revisadoPeloProfessor | prontoParaOutput (Seção 7.1)
  requestedOutputTypes,       # subconjunto da taxonomia (Seção 5)
  outputProfileRef,           # REF ao OutputProfile (6.1)
  requestedBy,                # professorIndividual | coordenacaoPedagogica | escola | redeDeEnsino (E7 §2)
  generationNote              # intenção/observação (nunca claim factual)
}
```

### 6.3 `PedagogicalOutput` (conjunto entregue) e `OutputArtifact`

```txt
PedagogicalOutput = {
  pedagogicalOutputId,
  matchSetRef,                # de qual MatchSet derivou (E8)
  planningProfileRef,         # qual planejamento atende (E7)
  complianceProfileRef,       # piso de conformidade (E6)
  artifacts[],                # lista de OutputArtifact (ver abaixo)
  outputComplianceSummary,    # OutputComplianceSummary do conjunto (Seção 9)
  outputAuditTrail,           # OutputAuditTrail (externo, descartável)
  outputStatus                # rascunhoPedagogico | revisadoPeloProfessor | prontoParaUso | arquivado (Seção 7.1)
}

OutputArtifact = {            # supertipo; os tipos da Seção 5 o especializam
  outputId,
  outputType,                 # um valor da taxonomia (Seção 5)
  matchSetRef,                # REF ao MatchSet (E8)
  planningProfileRef,         # REF ao PlanningProfile (E7)
  complianceProfileRef,       # REF ao ComplianceProfile (E6)
  allowedUseContextRef,       # LIDO: classe(s) AllowedUseContext dos itens-base (E6 §9) — herdado, nunca redefinido
  schoolUseMode,              # LIDO/herdado: subconjunto de SchoolUseMode (E6) que governa visibilidade
  targetEducationStage,       # LIDO do ComplianceProfile (E6)
  targetAgeRange,             # LIDO do AgeLanguageProfile (E6)
  subjectArea,                # LIDO de SubjectArea (E6) — componente/área
  estimatedDuration,          # estimativa relativa ao TimeBudget do plano (E7) — não altera o plano
  teacherMediationLevel,      # nenhuma | baixa | media | alta | obrigatoria (herdado de SensitiveContentRule/E7)
  studentFacingMode,          # voltadoAoProfessor | voltadoAoAluno | misto
  languageLevel,              # faixa de linguagem (E3.1 §6 / E6 §7) — a forma, nunca o fato
  accessibilityRequirements,  # REFs a AccessibilityRequirement (E6)
  sourceCitationPolicy,       # como as fontes aparecem (6.1)
  artifactSections,           # lista de OutputSectionBlock (6.4) — a espinha do artefato
  claimRefs,                  # REFs a Claim/ClaimSet/WeightedClaim citados (E2) — preserva claimType/confiança/peso
  sceneRefs,                  # REFs a Scene v1.1 / generatedSceneCandidate usados (E5/4H) — LIDOS
  momentResultRefs,           # REFs a MomentResult usados (E5)
  dossierRefs,                # REFs a dossiês usados (E5/E8)
  outputCitationBundle,       # OutputCitationBundle do artefato (Seção 11)
  excludedContentPolicy,      # como itens excluídos são tratados (transparência; sem reinclusão indevida)
  sensitiveContentHandling,   # ocultar | mediarPeloProfessor | exibirComAviso | apenasNoGuiaDoProfessor
  constraintWarnings,         # lista de OutputConstraintWarning quando o artefato não cabe na restrição (Seção 8)
  outputStatus,               # rascunhoPedagogico | revisadoPeloProfessor | prontoParaUso | arquivado
  outputAuditTrail            # OutputAuditTrail do artefato
}
```

### 6.4 `OutputSectionBlock` (bloco do artefato)

```txt
OutputSectionBlock = {
  blockId,
  blockRole,                  # explicacaoPrincipal | contexto | aprofundamentoOpcional | mediacao
                              #   | fonteEvidencia | atividade | avaliacao | comparacao | sinteseFaixaEtaria
                              #   | simultaneidadeGlobal | perguntaDisparadora
  sourceCurricularRole,       # LIDO do MatchSet: curricularCore | contextual | enrichment | freeExploration
  visibilityClass,            # LIDO/herdado: teacherOnly | teacherMediated | internalReviewOnly
                              #   | contextualOnly | enrichmentOnly | visívelAoAluno | hidden (E8 §6.3)
  requiresMediation,          # LIDO do MatchSet (transporta SensitiveContentRule.mediation / AgeSuitability)
  claimRefs,                  # REFs aos claims que o bloco usa (preserva rótulos)
  sceneRefs,                  # REFs às cenas/dossiês que o bloco usa
  epistemicLabelsRead,        # LIDOS: claimType, confidenceLevel, evidenceLevel, UncertaintyProfile (E2) — preservados
  anachronismWarningsRead,    # LIDOS do MomentResult/Scene — repassados (E5 §9)
  equivalenceWarningsRead,    # LIDOS — repassados; negacionismo fica rotulado-rejeitado, fora do ClaimSet
  publicabilityStatusRead,    # LIDO (1–5) — repassado, nunca alterado
  gatingReasonRead,           # LIDO (editorial/científico/licença/revisão-humana/geometria/mídia/fonte/legal) — repassado
  languageLevel,              # linguagem do bloco (a forma)
  accessibilityNotes,         # equivalente textual, rótulo não-cromático, alternativa estática (E6 §6)
  ageAdaptedExplanationRef,   # REF a AgeAdaptedExplanation, quando há adaptação de linguagem
  mediationScriptRef          # REF a MediationScript, quando requiresMediation = true
}
```

### 6.5 `SourceEvidenceCard`, `MediationScript` e `AgeAdaptedExplanation`

```txt
SourceEvidenceCard = {
  cardId,
  targetClaimRefs,            # claims que o cartão sustenta
  sourceSupportRef,           # SourceSupportSummary (A/B) — LIDO (E5/E8)
  evidenceLevelRead,          # observação direta | medição instrumental | documento primário
                              #   | dado modelado | inferência indireta | testemunho secundário (E2) — LIDO
  howWeKnow,                  # síntese "como sabemos disso" em linguagem da faixa (a forma; o fato não muda)
  citationRefs,               # REFs a Citation/Source (atribuição; jamais reprodução — 1.1)
  licenseNoteRead,            # LIDO de LicenseProfile/natureLabel — respeita licença e isolamento ShareAlike
  uncertaintyNote             # faixa/margem preservada (não "lado")
}

MediationScript = {
  scriptId,
  topic,                      # tema sensível (escravidão, colonização, genocídio, ditadura, raça e ciência…)
  sensitiveContentRuleRef,    # REF a SensitiveContentRule (E6 §8) — LIDO, nunca redefinido
  mediationGuidance,          # roteiro para o professor mediar (agência/resistência; dignidade; sem espetáculo)
  ageBand,                    # faixa para a qual a mediação é orientada
  hiddenMediaNote,            # o que fica oculto por padrão e por quê (revelação mediada)
  reviewRolesRequiredRead     # LIDO: papéis de revisão exigidos (E6) — repassado
}

AgeAdaptedExplanation = {
  explanationId,
  sourceClaimRefs,            # claims explicados (preserva claimType/confiança)
  ageBand,                    # 6-8 | 9-11 | 12-14 | 15-17 | professor
  adaptedText,                # texto adaptado à faixa — A FORMA, NUNCA O FATO (PE-Ed8)
  preservedLabels,            # rótulos epistêmicos mantidos visíveis (fato/inferência/hipótese/reconstrução)
  simplificationNote          # o que foi simplificado e o que NÃO pode ser simplificado (incerteza relevante)
}
```

### 6.6 `OutputComplianceSummary`, `OutputConstraintWarning`, `OutputAuditTrail` e `OutputRevisionNote`

```txt
OutputComplianceSummary = {
  summaryId,
  complianceProfileRef,       # REF ao ComplianceProfile (E6) — LIDO
  ageSuitabilityRead,         # LIDO: AgeSuitability dos itens (E6 §7) — repassado
  sensitiveContentRulesRead,  # LIDO: SensitiveContentRule aplicáveis (E6 §8)
  accessibilityRequirementsRead, # LIDO: AccessibilityRequirement (E6 §6)
  bnccMappingRefsRead,        # LIDO: BNCCMapping/CurricularAlignment (E6 §3) — respeita reviewStatus/provenanceRef (F1)
  curricularAlignmentNote,    # nota: alinhamento ≠ homologação ≠ PNLD (E6 §4.3)
  schoolUseModeRead,          # LIDO: SchoolUseMode aplicável (E6)
  allowedUseContextRead       # LIDO: classes AllowedUseContext dos itens (E6 §9)
}

OutputConstraintWarning = {
  warningId,
  warningType,                # excedeTempoDisponível | excedeRecursoDisponível | densidadeAlémDaFaixa
                              #   | requerMaisAcessibilidadeQueOPlano | excedeProfundidadeDaFaixa
  affectedArtifactRef,        # qual OutputArtifact não coube
  constraintRefRead,          # LIDO: TimeBudget | ResourceConstraint | AgeSuitability (E7/E6)
  recommendation,             # sugestão de redução de COBERTURA (corta contexto, nunca rótulo/incerteza)
  doesNotAlterPlan            # invariante FIXO = true (o aviso jamais modifica o PlanningProfile — E7)
}

OutputAuditTrail = {
  trailId,
  outputId,                   # a qual OutputArtifact pertence
  matchSetRef,                # de qual MatchSet derivou
  blockProvenance[],          # para cada OutputSectionBlock: de qual SelectedCandidate/claim/cena veio
  transformationsApplied,     # adaptações de linguagem/ordem/densidade aplicadas (sem alteração de fato)
  preservedLabelsCheck,       # checagem de que rótulos epistêmicos/anacronismo/gating foram preservados
  excludedItemsTransparency,  # registro de itens relevantes excluídos (espelha CoverageBalance.excludedButRelevantItems)
  doesNotAlterUpstream        # invariante FIXO = true (não altera KC/Compliance/Planning/Matching)
}

OutputRevisionNote = {
  noteId,
  outputId,                   # a qual OutputArtifact pertence
  authoredBy,                 # professor | coordenacaoPedagogica
  noteType,                   # ajuste-de-ordem | nota-de-mediação | marca-de-revisar | recorte-de-foco | observação
  notePayload,                # texto do professor (intenção; nunca claim)
  doesNotAlterTarget          # invariante FIXO = true (não altera o MatchSet, o KC nem a Compliance)
}
```

---

## 7. Regras de transformação do `MatchSet` em saída (Tarefa 7)

### 7.1 Eixo de consumo: `matchSetStatus` e `outputStatus`

**Decisão herdada e ajustada da Etapa 8.** A Etapa 8 mantém o campo `matchSetStatus`; a Etapa 9 **ajusta o vocabulário** para:

```txt
matchSetStatus := rascunho | calculadoPeloMotor | revisadoPeloProfessor | prontoParaOutput
```

(O valor `calculado` do dicionário original da Etapa 8, §5.3, lê-se agora **`calculadoPeloMotor`**; os demais valores permanecem.)

Regra de consumo do Output:

| `matchSetStatus` lido | O Output… | `outputStatus` resultante |
|---|---|---|
| `rascunho` | **não** gera artefato (seleção ainda em construção) | — |
| `calculadoPeloMotor` | **não** gera artefato como final; pode no máximo prévia interna de curadoria | `rascunhoPedagogico` (apenas `internalReviewOnly`) |
| `revisadoPeloProfessor` | gera artefato, **marcado como rascunho pedagógico** | `rascunhoPedagogico` |
| `prontoParaOutput` | gera artefato pedagógico (candidato a final, sujeito à revisão do professor na E10) | `prontoParaUso` (após revisão) |

> **Seis eixos de maturidade independentes.** `outputStatus` governa o **artefato pedagógico** (artefato do Output); **não** se confunde com (a) `matchSetStatus` (correspondência — E8); (b) `planningReviewStatus` (planejamento — E7); (c) `reviewStatus` do KC/Compliance (publicação de conteúdo); (d) `publicabilityStatus` (exibição da `Scene`/momento, 1–5); (e) `sceneCompletenessLevel` (maturidade da cena como artefato de método — 4H). O Output só escreve no primeiro. **Validade, cache e versionamento** não são eixos desta etapa; se necessário, tratam-se como **pendência futura** (Etapa 11), não como eixo central aqui.

### 7.2 O princípio: o Matching seleciona; o Output dá forma

O Matching já entregou, para cada item, **o que ele é no `MatchSet`**: `curricularRole`, `visibilityClass`, `requiresMediation`, `publicabilityStatus`, `gatingReason`, `matchScore`, `selectionRationale` e o `SourceSupportSummary`. O Output **não reabre nenhuma dessas decisões**; ele as **lê** e decide **onde cada item entra no artefato e em que forma**. A regra prática é a correspondência papel → bloco:

| O Matching diz… | O Output decide… |
|---|---|
| "este item é **central** (`curricularCore`)" | entra no bloco `explicacaoPrincipal` do artefato |
| "este item é **contexto** (`contextual`)" | entra no bloco `contexto`/`simultaneidadeGlobal`, não como foco |
| "este item é **enriquecimento** (`enrichment`)" | entra como `aprofundamentoOpcional`, sinalizado como extra |
| "este item **exige mediação** (`requiresMediation`)" | entra no `TeacherGuideOutput`/`MediationScript`, **não** diretamente no material do aluno |
| "este item é **`teacherOnly`**" | entra só na face do professor; nunca no `studentMaterial` |
| "este item tem **`gatingReason = científico`** e incerteza alta" | aparece **rotulado** (hipótese como hipótese, faixa como faixa), nunca ocultado por ser incerto |
| "este item foi **excluído por porta dura**" | **não** aparece; entra só como transparência da ausência conforme `excludedContentPolicy` |

### 7.3 Invariantes de transformação (não negociáveis)

A Etapa 9 fixa os seguintes invariantes. Aparecem aqui consolidados e são referenciados pelas demais seções.

1. **Output não decide verdade factual.** A verdade já está decidida e tipada no KC; o Output apenas a apresenta.
2. **Output não seleciona conteúdo bruto; consome `MatchSet`.** Vai ao KC só para resolver referências já presentes na seleção.
3. **Output não relaxa compliance.** Aplica as regras da Etapa 6; só pode endurecer (na dúvida, sobe-se o cuidado — PE-Ed4).
4. **Output não transforma BNCC em fonte factual.** A BNCC indexa; o conhecimento existe sem ela (P1/P2).
5. **Output não trata recurso complementar como currículo oficial.** Atlas é recurso digital complementar (E6 §4), não substituto da grade.
6. **Output não substitui o professor.** O artefato apoia a mediação; a decisão pedagógica final é do professor (PE-Ed4).
7. **Output não expõe conteúdo sensível sem mediação quando a Compliance exigir.** `requiresMediation` vira `MediationScript`/face do professor.
8. **Output não exibe itens `pending`, `legal-review` ou `rejected` como fato.** Invariante de exibição absoluto (1.1/3.1).
9. **Output sempre preserva rastreabilidade** para claims, fontes, cenas, dossiês, `MomentResult` e `MatchSet` (via `OutputAuditTrail`).
10. **Output adapta linguagem, não altera o fato** (PE-Ed8): a forma muda com a faixa; o claim e seus rótulos não.
11. **Output distingue** fato documentado, interpretação historiográfica, hipótese, reconstrução modelada e aproximação didática (os `claimType` da Etapa 2, preservados).
12. **Output deixa claro** quando algo é **contexto**, **enriquecimento** ou **núcleo curricular** (herança de `curricularRole`/`AllowedUseContext`).
13. **Output respeita acessibilidade e uso escolar** (e-MAG/WCAG/LBI; equivalente textual; redundância não-cromática — E6 §6).
14. **Output nunca trata IA como fonte** (A3/Q5): conteúdo de IA, se houver, é rotulado e jamais é claim factual.
15. **Output registra trilha de auditoria** (`OutputAuditTrail`), com proveniência por bloco e checagem de preservação de rótulos.

### 7.4 O que a transformação **nunca** faz

- não **promove** `enrichment`/`contextual` a `curricularCore` (papel é decisão do Matching/Compliance);
- não **reinclui** item caído em porta dura (`reviewStatusGate`/`publicabilityGate`/`licenseGate`/`sensitiveContentGate`/… — E8 §6.1);
- não **remove** `gatingReason`, `anachronismWarnings` nem `equivalenceWarnings`;
- não **apaga** simultaneidade global nem a lente Brasil ao "enxugar" o artefato (D8; `CoverageBalance`);
- não **reescreve** o dossiê, o `MomentResult` nem a `Scene`; **organiza** e **cita**;
- não **funde** fato, cenário e previsão (P28) — preserva a separação que a função já fez (E5 §11 Ex.7/8);
- não **comprime a verdade** sob restrição de tempo: corta **cobertura/contexto**, nunca **rótulo/incerteza** (E7 §10.2).

---

## 8. Relação com `PlanningProfile` e intenção docente (Tarefa 8)

### 8.1 O que o Output preserva do planejamento

O Output **usa** o `PlanningProfile` (E7 §5), via `MatchSet`, para **preservar a intenção docente** no artefato — sem reescrevê-la:

| Elemento do Planning (E7) | Como o Output o preserva |
|---|---|
| `teacherObjective` | enquadra o artefato; vira o "objetivo da aula" do `LessonPlanOutput` (intenção, não claim) |
| `theme` | organiza o foco do artefato em torno do tema declarado |
| `schoolYearBandRef` / `complianceProfileRef` | fixa `targetEducationStage`/`targetAgeRange`/`languageLevel` do artefato |
| `subjectAreaRef` | informa `subjectArea`; **não** trava o caráter interdisciplinar dos blocos de contexto |
| `depthLevel` (`DepthPreference`) | calibra densidade/aparato dos blocos (introductory…interdisciplinary), dentro do teto da faixa |
| `lessonDuration` (`TimeBudget`) | informa `estimatedDuration`; sob tempo curto, foco em blocos `explicacaoPrincipal` |
| `regionalFocus` / `localContext` | destaca o recorte no artefato **sem** apagar a simultaneidade global (D8) |
| `usageScenario` / `schoolUseModeRefs` | governa `studentFacingMode` e a visibilidade dos blocos |
| `preferredSceneMode` | orienta o `outputType` (ex.: `dossie` → `sceneDossier`; `comparacaoAntesDepois` → `comparisonOutput`) |
| `assessmentIntent` | base de `QuizOutput`/`AssessmentOutput`/`RubricOutput` (intenção de avaliação, não a avaliação pronta — agora produzida aqui) |
| `teacherNotes` | contextualiza; rótulo "intenção do professor"; nunca vira fato |

### 8.2 Quando o artefato não cabe no plano

Se a saída **não couber** no tempo, no recurso ou na faixa do plano, o Output **não modifica o planejamento** (que é soberano da Etapa 7). Ele registra um **`OutputConstraintWarning`** (Seção 6.6) com `doesNotAlterPlan = true`, descrevendo o conflito e recomendando **redução de cobertura** (cortar contexto/enriquecimento), **jamais** redução de honestidade (cortar rótulo, incerteza ou fonte). Exemplos:

- plano de 50 min com `MatchSet` denso → `OutputConstraintWarning(excedeTempoDisponível)` + recomendação de manter `explicacaoPrincipal` e mover `contexto`/`enrichment` para `aprofundamentoOpcional`;
- `depthLevel = sourceAnalysis` para faixa 9–11 → `OutputConstraintWarning(excedeProfundidadeDaFaixa)` + recomendação de compactar o aparato sem suprimir o rótulo de evidência;
- artefato sem equivalente textual onde a acessibilidade é obrigatória → `OutputConstraintWarning(requerMaisAcessibilidadeQueOPlano)`.

> **O Output respeita a soberania do Planning.** Ele **propõe** ajustes via aviso e via `outputDensityPreference`; **não** reescreve `teacherObjective`, `lessonDuration`, `depthLevel` nem qualquer campo do `PlanningProfile`. Quem ajusta o plano é o professor (na Etapa 10), de posse do aviso.

---

## 9. Relação com a `BrazilianEducationComplianceLayer` (Tarefa 9)

### 9.1 Como o Output usa cada entidade da Compliance

O Output **consome** os perfis e anotações da Etapa 6; **não os cria nem os redefine**. Ele resume a conformidade no artefato (`OutputComplianceSummary`) e a respeita em cada bloco.

| Entidade da Compliance (E6) | Como o Output a usa | O que o Output **não** faz |
|---|---|---|
| `ComplianceProfile` | piso de conformidade do artefato (etapa/região/acessibilidade/perfil etário) | não edita o perfil nem cria exceções permissivas |
| `AgeLanguageProfile` | deriva `languageLevel`/`targetAgeRange`; calibra `AgeAdaptedExplanation` | não redefine os 5 níveis de exposição (E3.1 §6) |
| `AllowedUseContext` | herda a classe curricular por item → papel do bloco | **não redefine a classe**; não promove `enrichment` a núcleo |
| `AgeSuitability` | porta de adequação etária + mediação por faixa no artefato | não rebaixa a exigência; não altera o fato |
| `SensitiveContentRule` | gera `MediationScript`; define `sensitiveContentHandling` | não relaxa mediação/ocultação; não apaga (media) |
| `AccessibilityRequirement` | requisito de acessibilidade do artefato (equivalente textual, redundância não-cromática) | não cria UX; não trata como enfeite |
| `LegalRequirement` | respeita obrigações (LGPD Art. 14, LBI Art. 63, Marco Civil) | não inventa obrigação; não coleta dado de aluno |
| `BrazilianEducationConstraint` | preserva cobertura estrutural (afro/indígena) nos blocos | não viola a cobertura obrigatória; não a trata como opcional |
| `CurricularAlignment` | resume alinhamento **confirmado** (respeita `reviewStatus`) no `OutputComplianceSummary` | **não cria alinhamento**; não promete homologação/PNLD |
| `BNCCMapping` | conecta blocos a habilidades (respeita `reviewStatus`/`provenanceRef` F1) | **não mapeia BNCC em massa**; não inverte a direção |
| `SchoolUseMode` | governa `studentFacingMode` e visibilidade dos blocos | não cria modo; não mistura modo com permissão de conteúdo |
| `ComplianceAnnotation` | lê anotações de conformidade sobre os itens | não as edita; usa `OutputAuditTrail` própria |

### 9.2 Regras obrigatórias

1. **O Output não redefine a Compliance.** Resume e respeita; não cria, edita nem afrouxa.
2. **Não inventa alinhamento BNCC.** Só cita `CurricularAlignment`/`BNCCMapping` existentes, com `provenanceRef` (F1) e `reviewStatus` respeitado.
3. **Não transforma a BNCC em fonte do conteúdo.** A BNCC referencia o KC; o conhecimento existe sem ela (invariante 4).
4. **Não trata `BNCCMapping`/`CurricularAlignment` `pending` como definitivo.** Alinhamento não aprovado é citado como **provisório**, nunca como definitivo (E6 §3.2/§13).
5. **Não permite que o professor relaxe sensíveis pelo artefato.** `sensitiveContentHandling`/`teacherMediationLevel` só **endurecem**; o piso da Etapa 6 e da 3.1 é inviolável.
6. **Não apaga conteúdo fora da grade.** Conteúdo `contextual`/`enrichment` aparece como contexto/aprofundamento, nunca suprimido por estar fora da grade (D3; E6 §9).
7. **Não confunde `AllowedUseContext` com modo de sala.** A classe curricular (papel do bloco) e o `SchoolUseMode` (modo de entrega/uso) são eixos distintos, combinados sem mistura.

> **Alinhamento ≠ homologação ≠ PNLD.** O Output preserva a distinção da Etapa 6 (§4.3): o `OutputComplianceSummary` pode dizer "alinhado à habilidade X (a confirmar)"; **nunca** "homologado pelo MEC" nem "aprovado no PNLD". Nenhum campo do `PedagogicalOutput` pode sugerir homologação/PNLD (Seção 13, R-7).

---

## 10. Relação com o `ContentMatchingEngine` (Tarefa 10)

### 10.1 O que o Matching produziu e o Output consome

O Matching (Etapa 8) entregou um conjunto de artefatos de seleção que o Output **lê para decidir forma**, nunca para refazer seleção:

| Saída do Matching (E8) | Como o Output a consome |
|---|---|
| `MatchSet` | âncora de todo o artefato; `matchSetStatus` governa final × rascunho (Seção 7.1) |
| `SelectedCandidate` (com `curricularRole`/`visibilityClass`/`requiresMediation`) | matéria-prima dos `OutputSectionBlock`; papel → bloco (Seção 7.2) |
| `SceneMatch` | base de `explorationGuide`, `sceneDossier`, `comparisonOutput` (preserva `publicabilityStatus`/`gatingReason`) |
| `DossierMatch` | base de `sceneDossier`/`sourceAnalysis` (organiza blocos; não reescreve) |
| `ClaimMatch` | conteúdo factual citável (preserva `claimType`/`confidenceLevel`/`displayWeight`) |
| `CoverageBalance` | preserva simultaneidade global, lente Brasil, cobertura estrutural, diversidade de camadas no artefato |
| `ExclusionReason` / `excludedButRelevantItems` | informa `excludedContentPolicy` (transparência da ausência; sem reinclusão) |
| `SourceSupportSummary` | alimenta `OutputCitationBundle` e `SourceEvidenceCard` |
| `MatchingAuditTrail` | referenciada pela `OutputAuditTrail` para a cadeia completa de proveniência |

### 10.2 A divisão fina: forma × seleção

A Etapa 8 deixou exemplos canônicos da divisão; a Etapa 9 os completa do lado da forma:

- Matching diz "este item é **central**" → Output diz "este item entra no **bloco de explicação principal**".
- Matching diz "este item **exige mediação**" → Output diz "este item entra no **roteiro do professor** (`MediationScript`), não diretamente no material do aluno".
- Matching diz "este item é **enrichment**" → Output diz "este item entra como **aprofundamento opcional**".
- Matching diz "este item é **contexto simultâneo**" → Output diz "este item entra no bloco de **simultaneidade global**, preservando o que coexistia no mundo".
- Matching diz "este item caiu em **porta dura**" → Output diz "este item **não aparece**; registra-se apenas a ausência conforme a política, sem revelar conteúdo não exibível".

> **O Output não reabre o Matching.** Não recalcula `MatchScore`, não cria `MatchCandidate`, não altera `CurricularRoleAssignment`, não reabre `ComplianceGateResult`, não inclui `excludedCandidates`. Reabrir a seleção sem autorização é violação de fronteira (Seção 13, R-22). Se a seleção estiver inadequada, o caminho é **revisar o `MatchSet` na Etapa 8**, não contorná-lo no Output.

---

## 11. Relação com `WhatWasHappeningAtMoment`, `MomentResult`, `Scene` v1.1 e dossiês (Tarefa 11)

### 11.1 O que o artefato pode usar

A saída pedagógica pode usar, **sempre por referência e sempre preservando os rótulos**, os objetos que a função e a curadoria produziram e que o Matching selecionou:

| Objeto (E5/E4F/4H/E8) | Como o Output o usa | O que preserva |
|---|---|---|
| `MomentResult` (E5 §4) | base de "o que acontecia no mundo neste momento" no artefato | `mainItems`/`simultaneousItems`/`states` com seus papéis |
| `mainItems` | viram blocos `explicacaoPrincipal` | foco; `confidenceSummary` |
| `simultaneousItems` | viram blocos `simultaneidadeGlobal`/`contexto` | a simultaneidade real (D8) |
| `states` / 11 `State Types` | viram contexto do momento (pano de fundo) | `claimType` (quase sempre inferência/reconstrução em tempo profundo) |
| `hiddenItems` | **nunca** entram como fato; só contagem/transparência | invariante de exibição |
| `anachronismWarnings` | **repassados** ao artefato (ex.: "Brasil = colônia em 1789") | aviso integral (E5 §9) |
| `equivalenceWarnings` | **repassados**; negacionismo fica `rotulado-rejeitado`, fora do `ClaimSet` | anti-falsa-equivalência (E5 §9; E3.1 §5) |
| `generatedSceneCandidate` (E5/4H) | base de `explorationGuide`/`sceneDossier` | **nunca** tratado como gabarito |
| `Scene` v1.1 (34 campos — 4H §2) | base de dossiê/exploração/comparação | `publicabilityStatus`/`sceneCompletenessLevel`/`gatingReason` LIDOS |
| `centralItems`/`contextualItems`/`sensitiveItems`/`hiddenItems` (Scene) | mapeiam-se aos blocos por papel | sensível → `MediationScript`; hidden → não aparece |
| `claimSets`/`weightedClaimSets` (4H §4) | viram blocos de debate legítimo | `displayWeight` (`primário`/`secundário`/`nota`/`rotulado-rejeitado`) preservado |
| `uncertaintyProfiles` (E2) | viram nota de incerteza no bloco | faixa/margem, nunca "lado" |
| `cascadeStructure` (4H §3) | vira a espinha de um `comparisonOutput`/dossiê de consequências | `confidenceByStage` decaindo; sem determinismo |
| `paleoPositionPolicy` (4H §5) | repassada no bloco do lugar | marcador na paleoposição rotulada, não na coordenada atual |
| `sourceSummary` (E5/4H) | alimenta `SourceEvidenceCard`/`OutputCitationBundle` | "como sabemos"; sem inventar atribuição |
| `MediaAsset`/`MapAsset` (E2) | usados só se licenciados, com `natureLabel` | fotografia/mapa/gráfico/reconstrução/simulação/representação artística/aproximação didática |

### 11.2 Regras sobre cenas e dossiês

1. **O Output não cria cena nem dossiê.** Criação é da função (`generatedSceneCandidate`) e da curadoria (E4x/E5 §10); seleção é do Matching (E8 §11). O Output **organiza e cita**.
2. **Não promove cena a gabarito.** `gabarito-interno` é decisão de curadoria (12 critérios, 4H §9).
3. **Não altera `sceneCompletenessLevel` nem `publicabilityStatus`.** Lê e repassa; cena `bloqueada` (5) ou com itens `pending`/`legal-review` **não** entra no artefato do aluno (invariante absoluto).
4. **Não remove `gatingReason`.** O motivo do gating é transportado; a mediação exigida vira `MediationScript`/`teacherMediationLevel`.
5. **Não oculta incerteza para parecer mais didático.** `UncertaintyProfile`, `claimSets`/`weightedClaimSets` e rótulos epistêmicos são preservados; reduzir profundidade corta **cobertura**, nunca **rótulo** (Seção 7.4).
6. **Não funde fato, cenário e previsão.** Em clima moderno, o artefato mantém a separação da função: consenso como consenso, projeção como faixa, negacionismo `rotulado-rejeitado` fora do `ClaimSet` (P28; E5 §11 Ex.4/7/8).

### 11.3 Exemplos conceituais (alinhados aos das Etapas 5/6/7/8)

> Exemplos **mínimos e esquemáticos** — a Etapa 9 não cria plano de aula real para turma específica.

- **Ex. 1 — Revolução Francesa, 8º/9º ano (12–14).** `MatchSet` traz França/1789 como `curricularCore`; Inconfidência Mineira/EUA/Lavoisier como `contextual`; escravidão/colonização como `teacherMediated`. O Output monta um `lessonPlan` com blocos: `explicacaoPrincipal` (1789), `simultaneidadeGlobal` (os três paralelos), `mediacao` (escravidão → `MediationScript`, só na face do professor), e um `OutputComplianceSummary` citando a habilidade de História (provisória, F1). Mídia gráfica fica oculta < 15; `anachronismWarnings` ("Brasil = colônia") repassados.
- **Ex. 2 — GOE em ~2,4 Ga, Ensino Médio (15–17).** O Output monta um `sceneDossier` com bloco `fonteEvidencia` ("como sabemos": proxies geoquímicos), `SourceEvidenceCard` com `evidenceLevel = dado modelado`, e `AgeAdaptedExplanation` que **preserva** o rótulo `inferência científica`/`reconstrução modelada` e a nota de incerteza (paleogeografia rotulada, não "foto").
- **Ex. 3 — K-Pg em ~66 Ma, EF II (12–14).** O Output monta um `comparisonOutput` (antes/depois) sobre a `cascadeStructure`, com `confidenceByStage` decaindo do impacto (alta) aos incêndios (baixa); o bloco do lugar usa a paleoposição rotulada (não Yucatán atual); impacto ≫ Deccan preservado pelo `displayWeight` (sem falsa equivalência).
- **Ex. 4 — Clima moderno, Geografia/Ciências (EM): `quiz`.** O Output gera um `quiz` **apenas** sobre o **fato físico medido** (séries) e sobre a compreensão de que projeção é **faixa**; **não** cobra cenário como previsão certa nem trata negacionismo como "lado" (que fica `rotulado-rejeitado`, fora do `ClaimSet`). Itens que misturam fato/cenário/previsão **não** entram (herança do `claimTypeGate`, E8 §6).
- **Ex. 5 — Recorte Brasil/ES, `explorationGuide`.** O Output destaca o ES sem apagar o restante do mundo no mesmo tempo: blocos do ES como foco; o que coexistia em outras regiões como `simultaneidadeGlobal` a um clique; lente Brasil e história profunda indígena preservadas (D8; Leis 10.639/11.645).

---

## 12. Adequação por faixa etária, linguagem, mediação e acessibilidade (Tarefa 12)

### 12.1 A forma muda; o fato não (PE-Ed8)

O Output adapta **linguagem, profundidade, exposição de mídia e densidade** por faixa, **sempre preservando o fato e seus rótulos**. A `AgeAdaptedExplanation` (Seção 6.5) é o veículo: ela reescreve o **texto** do bloco para a faixa, mas mantém visíveis os rótulos epistêmicos (`fato documentado`/`inferência`/`hipótese`/`reconstrução modelada`) e a incerteza relevante.

| Faixa (E3.1 §6 / E6 §7) | Linguagem do artefato | Profundidade/aparato | Exposição de mídia | Sensíveis |
|---|---|---|---|---|
| **6–8** | muito acessível, frases curtas, sem jargão | noções concretas; `ClaimSet` ausente/muito simplificado | só não-gráfica | ocultos; forte mediação |
| **9–11** | acessível; termos sensíveis explicados ao introduzir | causas/consequências simples; primeira simultaneidade | históricas suaves, rotuladas | mediação; "pessoas escravizadas" |
| **12–14 (EF II)** | termos sensíveis explicados; introduz disputa terminológica | processos; `ClaimSet` simplificado | históricas rotuladas; gráfico forte oculto | sistema + resistência; gráfico oculto |
| **15–17 (EM)** | próxima da acadêmica, ainda didática | complexidade plena; pluralidade | difíceis com rótulo/contexto; gráfico extremo mediado | aviso + contexto; mediação recomendada |
| **Professor/pesquisador** | acadêmica; aparato crítico completo | integral; `ClaimSet` integral; notas editoriais | acesso pleno (com rótulos/licença) para preparação | é quem media; aparato completo |

> **Regra de ouro.** Quanto **menor** a presença do professor (`homework`, exploração com gate), **maior** o nível de cuidado padrão do artefato (mais ocultação, mais aviso) — coerente com PE-Ed4 e com `usageScenario` da Etapa 7 (§9).

### 12.2 Mediação

O `MediationScript` (Seção 6.5) transporta a `SensitiveContentRule`/`TeacherMediationRequirement` para o artefato: ele orienta o professor a mediar (agência e resistência; dignidade às vítimas; sem espetáculo do sofrimento), declara o que fica oculto por padrão (revelação mediada) e repassa os `reviewRolesRequired`. O Output **registra**; o professor **media**. Itens `requiresMediation` **nunca** entram diretamente no `studentMaterial` — vão à face do professor.

### 12.3 Acessibilidade

A acessibilidade é **fundação, não enfeite** (E6 §6; P24). Todo artefato com mídia/cena/mapa carrega, via `AccessibilityRequirement`, o **equivalente textual** (o que aconteceu, onde, quando, com que confiança) e usa **redundância não-cromática** nos rótulos epistêmicos (ícone/forma/texto, não só cor — E3 §8.3). O Output define **requisitos** de acessibilidade do artefato; a implementação concreta (foco visível, ordem de leitura, componentes acessíveis, verificação e-MAG/WCAG/ASES) é da Etapa 10/11. Quando a acessibilidade obrigatória não é atendida pelo material disponível, dispara-se `OutputConstraintWarning(requerMaisAcessibilidadeQueOPlano)`.

### 12.4 LGPD e personalização

O Output **não personaliza por dado pessoal de aluno**. A adaptação é por **faixa agregada** (`AgeLanguageProfile`) e por **nível agregado da turma** (`classReadinessLevel` — `homogenea`/`heterogenea`/`avançada`/`emRecuperacao`), nunca por perfil individual (LGPD Art. 14 §4 — minimização; E6 §5). Personalização baseada em perfil de menor é decisão futura, com cautela redobrada (Etapas 11/14), e não entra nesta etapa.

---

## 13. Riscos pedagógicos, jurídicos, editoriais e operacionais (Tarefa 13)

| # | Risco | Mitigação |
|---|---|---|
| **R-1** | **Plano de aula parecer definitivo demais** | `outputStatus` (rascunho × pronto); `revisadoPeloProfessor` → `rascunhoPedagogico`; revisão do professor na E10 (Seção 7.1) |
| **R-2** | **Output inventar fato** | invariante 1/2: verdade vem do KC; conteúdo factual só de `claimRefs`/`sceneRefs` já no `MatchSet` (Seção 7.3) |
| **R-3** | **Output ocultar incerteza para parecer didático** | invariante 10/11; `epistemicLabelsRead` preservados; `uncertaintyDisplayPolicy` nunca "omitir" (Seções 6.4/11.2) |
| **R-4** | **Output apagar simultaneidade global** | `CoverageBalance` preservado; blocos `simultaneidadeGlobal`; reduzir tempo corta cobertura, não simultaneidade (D8; Seção 7.4) |
| **R-5** | **Output escolarizar demais o KC universal** | foco curricular é âncora, não limite; contexto/enriquecimento preservados (E6 §9; Seção 9.2) |
| **R-6** | **Output virar currículo oficial** | invariante 5: recurso complementar, nunca substituto da grade (E6 §4) |
| **R-7** | **Output prometer aderência BNCC/MEC/PNLD** | alinhamento ≠ homologação ≠ PNLD; `OutputComplianceSummary` nunca declara homologação (E6 §4.3; Seção 9.2) |
| **R-8** | **Output expor conteúdo sensível sem mediação** | invariante 7; `requiresMediation` → `MediationScript`/face do professor; nunca no `studentMaterial` (Seção 12.2) |
| **R-9** | **Output gerar atividade inadequada à faixa** | `targetAgeRange`/`languageLevel` herdados; `AgeAdaptedExplanation`; `OutputConstraintWarning(excedeProfundidadeDaFaixa)` (Seção 12.1) |
| **R-10** | **Output transformar item `enrichment` em núcleo obrigatório** | papel é decisão do Matching/Compliance; Output não promove `enrichment` a `curricularCore` (Seção 7.4) |
| **R-11** | **Output tratar contexto como claim central** | `sourceCurricularRole` herdado; `contextual` → bloco de contexto, não de explicação principal (Seção 7.2) |
| **R-12** | **Output simplificar demais controvérsia legítima** | `claimSets`/`weightedClaimSets` preservados com `displayWeight`; pluralidade mantida (E3.1; Seção 11) |
| **R-13** | **Output criar falsa equivalência** | `equivalenceWarnings` repassados; negacionismo `rotulado-rejeitado` fora do `ClaimSet` (E3.1 §5; E5 §9) |
| **R-14** | **Output usar IA como fonte** | invariante 14: IA é `authorityType = index`, nunca claim factual; conteúdo de IA rotulado (A3/Q5; E2 §IA) |
| **R-15** | **Output omitir fontes** | `OutputCitationBundle`/`SourceEvidenceCard` obrigatórios; `sourceCitationPolicy` nunca "ocultar fonte" (Seção 11) |
| **R-16** | **Output perder rastreabilidade** | invariante 9/15; `OutputAuditTrail` com `blockProvenance` e `doesNotAlterUpstream = true` (Seção 6.6) |
| **R-17** | **Output ignorar acessibilidade** | invariante 13; `AccessibilityRequirement`; equivalente textual; redundância não-cromática; LBI Art. 63 (Seção 12.3) |
| **R-18** | **Output violar LGPD por personalização indevida** | sem dado pessoal de aluno; adaptação só por faixa/turma agregada (LGPD Art. 14 §4; Seção 12.4) |
| **R-19** | **Output criar avaliação sem base no objetivo do Planning** | `AssessmentOutput`/`RubricOutput` exigem `assessmentIntent`/objetivo; sem base → não geram (Seções 5/8) |
| **R-20** | **Output gerar quiz sobre conteúdo apenas contextual** | `quiz`/`activity` baseiam-se em itens `curricularCore` com base factual sólida; não em `contextual`/`enrichment` (Seção 5.2) |
| **R-21** | **Output reabrir o Matching sem autorização** | fronteira rígida: Output não recalcula `MatchScore`, não inclui excluídos, não altera papel (Seção 10.2) |
| **R-22** | **Output tratar `pending`/`legal-review`/`rejected` como publicável** | invariante 8: invariante de exibição absoluto (1.1/3.1); itens não exibíveis nunca entram como fato (Seções 7/11.2) |
| **R-23** | **Output substituir a autonomia docente** | invariante 6: artefato apoia, não decide; `OutputRevisionNote`; mediação final é do professor (PE-Ed4) |
| **R-24** | **Output reproduzir texto de fonte (violação de licença/direito autoral)** | citação ≠ reprodução; `OutputCitationBundle` atribui sem copiar; respeita `LicenseProfile`/isolamento ShareAlike (1.1; E2 §7) |
| **R-25** | **Output fundir fato, cenário e previsão** | P28 preservado; `claimTypeGate` herdado do Matching exclui mistura; função já separou (Seção 11.2) |
| **R-26** | **Output modificar o plano ao não caber no tempo** | `OutputConstraintWarning` com `doesNotAlterPlan = true`; recomenda cortar cobertura, não o plano (Seção 8.2) |
| **R-27** | **Output apagar cobertura afro/indígena ao enxugar** | `BrazilianEducationConstraint`/`CoverageBalance` preservados; cobertura estrutural, não nota de rodapé (Leis 10.639/11.645; Seção 9) |
| **R-28** | **Output vazar aparato `teacherOnly` ao aluno** | `visibilityClass` herdada; `teacherOnly`/`internalReviewOnly` só na face do professor (`SchoolUseMode = teacher`) (Seção 5.3) |

---

## 14. Fronteiras com as Etapas 10–14 (Tarefa 14)

| Etapa | Papel | Onde a Etapa 9 termina |
|---|---|---|
| **Etapa 10 — Design/UX 3D** | desenha **como** professor e estudante visualizam, editam, aprovam, exportam e navegam os artefatos (timeline, globo, popups, modos professor/estudante/exploração livre); implementação concreta de acessibilidade | a Etapa 9 entrega a **gramática dos artefatos** (`PedagogicalOutput`); **não** desenha telas, componentes nem fluxo de edição/aprovação/exportação |
| **Etapa 11 — Arquitetura técnica** | persistência, versionamento, **cache/validade** do artefato, APIs, permissões, engenharia de privacidade (LGPD/menores), isolamento físico de licenças SA/ODbL | a Etapa 9 é conceitual; **não** define stack, banco, versionamento nem API; validade/cache ficam como pendência (Seção 7.1) |
| **Etapa 12 — MVP** | escolhe o **recorte mínimo** de tipos de artefato para o primeiro corte | a Etapa 9 não propõe MVP |
| **Etapa 13 — Pipeline de ingestão** | alimenta os candidatos com **dados reais**, snapshots, validação e confirmação de licença por asset | a Etapa 9 só **consome** seleção; não faz ingestão nem povoa |
| **Etapa 14 — Operação, governança, QA e escala** | testa com professores, escola, jurídico e comercial; **analytics**, **LMS**, QA pedagógico, decisão sobre PNLD/compra pública | a Etapa 9 não cria analytics/LMS, não opera, não valida nem promete adoção/homologação |

> A Etapa 9 **não executa** nenhuma dessas. Ela entrega a gramática dos artefatos pedagógicos e o `PedagogicalOutput`; tudo a montante e a jusante pertence às etapas próprias.

---

## 15. Encerramento e handoff para a Etapa 10 (Tarefa 15)

### 15.1 O que esta etapa entrega

A Etapa 9 entrega a **arquitetura conceitual da `PedagogicalOutputLayer`**: a definição da camada como **transformadora de uma seleção curada em artefatos pedagógicos utilizáveis**, externa ao Knowledge Core; sua posição na direção única de dependência (entre a Experience e o Matching); a matriz de entradas (com `matchSetRef` como âncora e `matchSetStatus` como eixo de consumo); vinte e sete entidades conceituais externas e distintas das do KC, da Compliance, do Planning e do Matching (incluindo `PedagogicalOutput`, `OutputProfile`, `OutputRequest`, `OutputArtifact`, `OutputSectionBlock`, `LessonPlanOutput`, `SequencePlanOutput`, `ExplorationGuideOutput`, `StudentMaterialOutput`, `TeacherGuideOutput`, `ActivityOutput`, `QuizOutput`, `AssessmentOutput`, `RubricOutput`, `DiscussionPromptOutput`, `ComparisonOutput`, `HomeworkOutput`, `ProjectBriefOutput`, `SourceEvidenceCard`, `MediationScript`, `AgeAdaptedExplanation`, `OutputCitationBundle`, `OutputComplianceSummary`, `OutputConstraintWarning`, `OutputRevisionNote`, `OutputAuditTrail`, `OutputStatus`); a taxonomia de quinze `outputType` com classificação por público (professor/estudante/misto); os dicionários conceituais de `OutputProfile`/`OutputRequest`/`PedagogicalOutput`/`OutputArtifact`/`OutputSectionBlock`/cartões/avisos/trilhas; o ajuste do vocabulário de `matchSetStatus` para `rascunho | calculadoPeloMotor | revisadoPeloProfessor | prontoParaOutput` e a regra de consumo (final × rascunho pedagógico); os quinze invariantes de transformação; a relação de **preservação da intenção** com o Planning (com `OutputConstraintWarning` em vez de modificação do plano); a relação de **resumo e respeito** com a Compliance (sem redefini-la, sem inventar BNCC, sem prometer homologação/PNLD); a relação de **consumo, nunca de reabertura** com o Matching; a relação de **organização e citação** com a função, o `MomentResult`, a `Scene` v1.1 e os dossiês (preservando incerteza, anacronismo, equivalência, gating e publicabilidade), com exemplos esquemáticos (1789; GOE; K-Pg; clima moderno; recorte Brasil/ES); a adequação por faixa, linguagem, mediação e acessibilidade (a forma muda, o fato não); e vinte e oito riscos com mitigação. Nada aqui cria conteúdo, UX, stack, MVP, ingestão, cena nova, dossiê novo ou mapeamento BNCC em massa; nada altera claims, `reviewStatus` ou publicabilidade; nada usa IA como fonte factual ou dado pessoal de aluno; nada relaxa LGPD, acessibilidade ou conteúdo sensível; nada promete homologação MEC/PNLD; e nada trata recurso complementar como substituto do currículo.

### 15.2 O que a Etapa 10 deverá fazer

A **Etapa 10 — Design/UX 3D** receberá o `PedagogicalOutput` e desenhará **como professor e estudante irão visualizar, editar, aprovar, exportar e navegar** esses artefatos — em uma experiência que mantém, em qualquer modo (3D → 2D → estático → offline → projetor), o **mínimo de timeline, globo/mapa, simultaneidade global, fontes, incerteza e dossiê**, e que materializa a acessibilidade (foco visível, equivalente textual, redundância não-cromática) e os modos professor/estudante/exploração livre. A Etapa 10 deve **respeitar** os rótulos epistêmicos, a mediação, a visibilidade por papel e a cadeia de referência que a Etapa 9 preservou — sem reabrir a forma, a seleção, a conformidade ou a verdade.

### 15.3 O que a Etapa 9 ainda **não** fez (e por quê)

Não desenhou UX, telas, edição, aprovação nem exportação (Etapa 10); não definiu stack, persistência, versionamento, cache/validade nem API (Etapa 11); não propôs MVP (Etapa 12); não fez ingestão nem povoou (Etapa 13); não criou analytics, LMS, QA operacional, nem validou/prometeu adoção/homologação (Etapa 14); não criou cena, dossiê, `Claim`, `Source` nem qualquer conhecimento; não promoveu cena a gabarito; não mapeou BNCC em massa; não alterou `reviewStatus`/`publicabilidade`/`MatchScore`; não usou IA como fonte factual; não usou dado pessoal de aluno; e não relaxou LGPD, acessibilidade nem conteúdo sensível. Tudo isso é contingente ou pertence a etapas próprias; o Output permanece **transformador de forma** externo ao núcleo.

---

## Encerramento e handoff

Esta etapa (v1.0) entrega a **arquitetura conceitual da Pedagogical Output Layer**: a definição da camada como transformadora que **converte um `MatchSet` revisado em artefatos pedagógicos utilizáveis** — plano de aula, sequência didática, roteiro de exploração, guia do professor, material do aluno, atividade, quiz, avaliação formativa, rubrica, perguntas de discussão, análise de fonte, dossiê de cena, comparação, tarefa de casa e briefing de projeto —, preservando a cadeia de referência para claims, fontes, cenas, dossiês, `MomentResult` e `MatchSet` e mantendo intactos os rótulos de tipo de claim, confiança, evidência, incerteza, anacronismo, equivalência, publicabilidade, gating, mediação e acessibilidade; sua posição entre a Experience e o Matching; a matriz de entradas; as vinte e sete entidades conceituais externas; os dicionários de `OutputProfile`/`OutputRequest`/`PedagogicalOutput`/`OutputArtifact`/`OutputSectionBlock` e dos cartões, avisos e trilhas; o ajuste de `matchSetStatus` (`rascunho | calculadoPeloMotor | revisadoPeloProfessor | prontoParaOutput`) e a regra de consumo (final × rascunho pedagógico), com `outputStatus` como sexto eixo de maturidade independente; a taxonomia de quinze tipos com classificação por público; os quinze invariantes de transformação; a relação de preservação com o Planning (com `OutputConstraintWarning` em vez de alterar o plano); a relação de resumo e respeito com a Compliance (sem redefini-la, sem inventar BNCC, sem prometer homologação/PNLD, sem apagar conteúdo fora da grade, sem confundir `AllowedUseContext` com modo de sala); a relação de consumo — nunca de reabertura — com o Matching; a relação de organização e citação com a função, o `MomentResult`, a `Scene` v1.1 e os dossiês (sem criar cena, sem reescrever dossiê, sem promover gabarito, sem alterar `sceneCompletenessLevel`/`publicabilityStatus`, sem remover `gatingReason`, sem ocultar incerteza, sem fundir fato/cenário/previsão); a adequação por faixa, linguagem, mediação e acessibilidade (a forma muda, o fato não); e vinte e oito riscos com mitigação. Nada aqui cria conteúdo, UX, stack, MVP, ingestão, cena nova ou mapeamento BNCC em massa; nada altera claims, `reviewStatus` ou publicabilidade; nada usa IA como fonte factual ou dado pessoal de aluno; nada relaxa LGPD, acessibilidade ou conteúdo sensível; nada promete homologação MEC/PNLD; e nada trata recurso complementar como substituto do currículo. A direção única de dependência permanece invertida: Experience → **Output** → Matching → Planning → Compliance → Knowledge Core.

**Handoff:** com a Etapa 9 (v1.0) aprovada, a **Etapa 10 — Design/UX 3D** pode ser executada, recebendo o `PedagogicalOutput` desta camada e desenhando como professor e estudante irão visualizar, editar, aprovar, exportar e navegar esses artefatos — preservando timeline, globo/mapa, simultaneidade global, fontes, incerteza, dossiê, acessibilidade e os modos professor/estudante/exploração livre, e respeitando os rótulos epistêmicos, a mediação, a visibilidade por papel e a rastreabilidade que a Etapa 9 entregou, sem reabrir a forma, a seleção, a conformidade ou a verdade. O resíduo curatorial herdado das Etapas 6/8 permanece: os `BNCCMapping`/`CurricularAlignment` concretos seguem `pending` até confirmação com o texto homologado (F1) — o Output os **referencia, resume e respeita o `reviewStatus`**, sem resolvê-los.

*Documento de entrega da Etapa 9 (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8). Define somente a gramática dos artefatos pedagógicos. Não modela novos dados do núcleo, não escreve código, não propõe MVP, não define stack, não desenha UX final, não cria cena nova, não cria dossiê novo, não promove cena a gabarito, não mapeia BNCC em massa, não povoa o Knowledge Core, não altera claims, não usa IA como fonte factual e não usa dados pessoais reais de alunos. Próxima etapa, quando solicitada: Etapa 10 — Design/UX 3D.*
