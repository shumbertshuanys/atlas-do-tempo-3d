# Etapa 8 — Content Matching Engine

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 8** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0) e a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura conceitual** do motor de correspondência de conteúdo. Define **somente a estrutura conceitual da seleção, exclusão, justificativa, ranqueamento e agrupamento** de conteúdos — a *gramática de correspondência* entre planejamento, conformidade e conhecimento. Conforme solicitado, esta etapa **não** cria plano de aula, roteiro, trilha pedagógica final, atividade, quiz, avaliação, rubrica nem material do aluno (Etapa 9); **não** cria UX/telas (Etapa 10); **não** define stack técnica nem persistência (Etapa 11); **não** propõe MVP (Etapa 12); **não** faz ingestão (Etapa 13); **não** cria cena nova; **não** promove cena a gabarito; **não** mapeia BNCC em massa; **não** altera `Claim`, `reviewStatus` ou `publicabilityStatus`; **não** usa IA como fonte factual; **não** usa dados pessoais reais de alunos; **não** cria analytics; **não** cria LMS; **não** relaxa LGPD, acessibilidade ou conteúdo sensível; **não** trata alinhamento BNCC como homologação MEC nem como aprovação PNLD; e **não** trata recurso complementar como substituto do currículo.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Blocos ```txt``` são **dicionário conceitual, nunca código executável**. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6). "O Planning" = a `TeacherSchoolPlanningLayer` (Etapa 7). "O Matching" = o `ContentMatchingEngine` definido na Seção 1.

> **Regra de fundação desta etapa.** O Matching é **leitor, seletor e ranqueador**, externo ao Knowledge Core. Ele nunca cria, edita ou altera `Claim`, `ClaimSet`, `Source`, `Citation`, `Event`, `Process`, `State`, `Relationship`, `Scene`, `reviewStatus`, `confidenceLevel`, `evidenceLevel`, `claimType`, `UncertaintyProfile` ou `ProvenanceMetadata`. A direção única de dependência permanece invertida: **Experience → Output → Matching → Planning → Compliance → Knowledge Core**. O Matching aponta para dentro; o KC nunca aponta para o Matching (Etapa 2, §10; P1/P2).

---

## Sumário

1. Definição do `ContentMatchingEngine`
2. Papel da camada na arquitetura geral
3. Entradas do motor de matching
4. Entidades conceituais da camada
5. `MatchingProfile`, `CandidatePool` e `MatchSet`
6. Regras de elegibilidade e exclusão
7. Sistema de pontuação e ranqueamento
8. Relação com `PlanningProfile` e `PlanningFilter`
9. Relação com a `BrazilianEducationComplianceLayer`
10. Relação com `WhatWasHappeningAtMoment`
11. Relação com `Scene` v1.1 e dossiês
12. Balanceamento curricular, epistêmico e de simultaneidade
13. Riscos educacionais, jurídicos, editoriais e operacionais
14. Fronteiras com as Etapas 9–14
15. Encerramento e handoff para a Etapa 9

---

## 1. Definição do `ContentMatchingEngine` (Tarefa 1)

### 1.1 Natureza

O **`ContentMatchingEngine`** é a **camada externa** que **transforma uma intenção pedagógica estruturada em um conjunto selecionado, justificado, auditável e conforme de conteúdos adequados**. Ele recebe o `PlanningProfile`/`PlanningFilter` da Etapa 7 e o cruza com o Knowledge Core, a `BrazilianEducationComplianceLayer`, o `MomentResult` da função e as cenas/dossiês de `Scene` v1.1, **selecionando, ranqueando, excluindo, justificando e agrupando** — cenas, momentos, claims, itens do KC, fontes, evidências, dossiês e recursos — para um planejamento específico.

Três consequências estruturais, herdadas das etapas anteriores:

1. **É contingente, não universal.** Diferente do KC (universal e estável — Etapa 2, §10.2), uma correspondência é sempre relativa a *um* planejamento, *um* perfil de conformidade e *um* contexto de turma. Por isso o Matching **nunca entra no núcleo**: vive por fora, como registro próprio que **aponta para** o KC por identificador estável (P1/P2).
2. **É leitura e seleção, não escrita.** O Matching **não cria nem altera** conhecimento. Ele lê o que a função e a curadoria já produziram, **seleciona** o que cabe, **rotula** o papel de cada item e **registra** por que incluiu ou excluiu. Toda criação/edição/aprovação de conteúdo permanece sob curadoria humana (Etapas 4x/13); toda decisão de conformidade permanece soberania da Compliance (Etapa 6) e da política editorial (Etapa 3.1).
3. **Existe apenas no fluxo do professor (D3).** A baseline fixou dois caminhos: o **fluxo do professor** (atravessa Compliance → Planning → Matching → Output → Experience) e a **exploração livre** (vai do KC direto à experiência, com a Compliance atuando apenas como filtro de adequação). O Matching **só existe no fluxo do professor** — ele exige um `PlanningProfile` como entrada. A exploração livre pura (`usoLivreExploratorio`, sem planejamento) **não passa pelo Matching** (Etapa 0, D3; Etapa 7, §2.1). A relação fina com esse caso está na Seção 10.

### 1.2 As perguntas que a camada responde

| # | Pergunta | O que produz |
|---|---|---|
| 1 | **Quais itens do KC são relevantes para este planejamento?** | `CandidatePool` + `MatchScore` por candidato |
| 2 | **Quais cenas ou momentos são adequados?** | `SceneMatch`/`MomentMatch` no `MatchSet` |
| 3 | **Quais claims podem ser usados?** | `ClaimMatch` elegíveis |
| 4 | **Quais claims devem ser excluídos?** | `ExclusionReason` em `excludedCandidates` |
| 5 | **Quais itens exigem mediação?** | `requiresMediation` + `TeacherMediationRequirement` repassada |
| 6 | **Quais itens são apenas contexto?** | `CurricularRoleAssignment = contextual` |
| 7 | **Quais itens são enriquecimento?** | `CurricularRoleAssignment = enrichment` |
| 8 | **Quais itens devem ficar ocultos?** | `visibilityClass = hidden` (invariante de exibição) |
| 9 | **Quais fontes/evidências sustentam a seleção?** | `SourceSupportSummary` |
| 10 | **Quais conteúdos respeitam idade, acessibilidade, LGPD, BNCC e política editorial?** | `ComplianceGateResult` |
| 11 | **Quais conteúdos cabem no tempo disponível e no modo de uso escolar?** | ranqueamento por compatibilidade de tempo/`usageScenario` |

### 1.3 O que a camada **não** decide

O Matching **não decide a verdade dos fatos**. Não arbitra consenso científico, não pondera controvérsias, não rotula evidência, não promove cena a gabarito e **não reordena a verdade do núcleo**. Tudo isso pertence ao KC, à política editorial (Etapa 3.1) e à curadoria humana. O Matching também **não redefine a conformidade**: ele aplica as regras da Compliance, sem afrouxá-las nem inventá-las. A pontuação organiza **relevância pedagógica**; **score não altera estatuto factual** (Seção 7).

### 1.4 O que a camada produz

A camada produz o **`MatchSet`** (Seção 5): o conjunto final de candidatos selecionados, ranqueados, justificados, classificados por papel curricular e aprovados nos portões de conformidade, acompanhado de `CoverageBalance`, `SourceSupportSummary` e `MatchingAuditTrail`. O `MatchSet` é o objeto que a **Etapa 9 (Pedagogical Output Layer)** recebe para gerar as saídas pedagógicas finais. O Matching **para no `MatchSet`**; não gera plano, atividade, quiz, rubrica ou material (Seções 13 e 14).

---

## 2. Papel da camada na arquitetura geral (Tarefa 2)

### 2.1 Posição

```
Experience → Output → MATCHING (esta camada) → Planning → Compliance → Knowledge Core
        (cada camada aponta para dentro; o KC não conhece nenhuma delas)
```

O Matching senta **entre** o Planning (que lhe entrega a intenção estruturada e o `PlanningFilter`) e o Output (que recebe o `MatchSet`). Para baixo, ele lê o Knowledge Core, a Compliance e a saída da função; para cima, alimenta a Etapa 9. Apagar o Matching inteiro **não deixa campo órfão** a montante (teste de P2): o KC, a Compliance e o `MomentResult` permanecem intactos.

### 2.2 O que o Matching é (e o que não é)

| O Matching é… | O Matching **não** é… |
|---|---|
| **leitor dos índices do KC** (tempo, espaço, tema, tipo, confiança — Etapa 2, §10.3) | autor de fatos; nunca escreve `Claim`/`Source`/`Relationship` |
| **consumidor do planejamento** (`PlanningProfile`/`PlanningFilter`) | autor da intenção; não inventa objetivo nem tema |
| **consumidor da conformidade** (perfis e anotações da Etapa 6) | definidor de conformidade; não cria `AgeSuitability`/`SensitiveContentRule`/`BNCCMapping` |
| **seletor/ranqueador** de candidatos | árbitro de verdade; não pondera consenso nem promove cena a gabarito |
| **produtor de conjuntos candidatos** (`CandidatePool` → `MatchSet`) | gerador de plano/atividade/quiz/rubrica (Etapa 9) |
| **fornecedor da Etapa 9** | implementador de UX/stack/MVP/pipeline (Etapas 10–13) |

### 2.3 Divisão de responsabilidades (quem decide o quê)

| Camada | Decide | Não decide |
|---|---|---|
| **Knowledge Core (E2)** | o que é conhecimento (claims tipados, fonteados, com confiança/incerteza) | currículo, faixa, planejamento, seleção |
| **Compliance (E6)** | regras de conformidade (faixa, sensíveis, acessibilidade, alinhamento BNCC, modos, classes de uso) | a verdade do fato; a intenção do professor; a seleção final |
| **Planning (E7)** | a intenção pedagógica (objetivo, tema, recorte, profundidade, modo, escopo de papel) | a verdade; a conformidade; a seleção |
| **Matching (E8 — esta)** | **a seleção, a exclusão, o ranqueamento, o papel curricular de cada item e a justificativa** | a verdade; a conformidade; a saída pedagógica final |
| **Output (E9)** | a transformação do `MatchSet` em artefato pedagógico (plano, roteiro, atividade, quiz, rubrica, material) | a seleção (já dada); a verdade; a conformidade |

> **Síntese.** **Planning decide intenção; Compliance decide regras; o KC contém conhecimento; o Matching seleciona; o Output transforma a seleção em artefato pedagógico.** O Matching é a dobradiça que torna a intenção operável sobre o conhecimento, sem nunca tocar nem a intenção, nem as regras, nem os fatos.

---

## 3. Entradas do motor de matching (Tarefa 3)

Matriz de campos de entrada. Cada campo declara **definição**, **origem**, **obrigatório/opcional**, **uso no matching** e **risco se mal usado**. Os `*Ref` apontam para entidades **já definidas** nas Etapas 2/5/6/7; o Matching **não** as recria.

| Campo (`camelCase`) | Definição | Origem | Obrig./Opc. | Uso no matching | Risco se mal usado |
|---|---|---|---|---|---|
| `planningProfileRef` | REF ao `PlanningProfile` que originou a correspondência | Planning (E7) | **Obrigatório** | âncora de toda a seleção; sem ele não há Matching (D3) | rodar Matching sem intenção → seleção sem foco |
| `planningFilterRef` | REF ao `PlanningFilter` (filtros derivados do `PlanningProfile`) | Planning (E7) | **Obrigatório** | empacota os filtros aplicáveis ao `CandidatePool` | filtrar por critério que o professor não declarou |
| `complianceProfileRef` | REF ao `ComplianceProfile` (traz `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef`, `policyRefs[]`) | Compliance (E6), via Planning | **Obrigatório** | define o piso de conformidade de toda a seleção | aplicar perfil incompatível com a turma |
| `curricularRoleScope` | subconjunto de classes `AllowedUseContext` a incluir (`curricularCore`/`contextual`/`enrichment`/`freeExploration`) | Planning (E7) | Recomendado | decide quais papéis entram no `MatchSet` | restringir a `curricularCore` e perder a simultaneidade global |
| `schoolUseModeRefs` | um ou mais `SchoolUseMode` (`teacher`/`student`/`free-exploration`/`projector`/`offline`) | Compliance (E6), via Planning | **Obrigatório** | governa `visibilityClass` (ex.: relatório interno só em `teacher`) | confundir modo de uso com permissão de conteúdo |
| `usageScenario` | cenário pedagógico fino (10 valores — E7 §9) aninhado sob `schoolUseModeRefs` | Planning (E7) | Recomendado | modula gating, mediação e densidade | escolher cenário incompatível com o recorte |
| `preferredSceneMode` | modo de apresentação preferido (mapeia para `outputMode` da função) | Planning (E7) | Opcional | orienta qual forma de `SceneMatch`/`MomentMatch` priorizar | pedir modo incompatível com o recorte |
| `depthLevel` | nível de profundidade (`DepthPreference`: `introductory`…`interdisciplinary`) | Planning (E7) | Recomendado | calibra densidade e aparato sem alterar o fato | profundidade acima do teto da faixa |
| `lessonDuration` | tempo disponível (`TimeBudget`) | Planning (E7) | Opcional | limita quantidade de itens-âncora; foco em `mainItems` | densidade incompatível com o tempo |
| `regionalFocus` | recorte geográfico de destaque (`global`…`município`/`bioma`/`regiãoHistórica`) | Planning (E7) | Opcional | dimensão de relevância regional no ranqueamento | eurocentrismo ou apagamento invertido |
| `localContext` | contexto local da escola/turma (texto + tags) | Planning (E7) | Opcional | reforça relevância local; **intenção, nunca geografia do KC** | recorte local apagar o resto do mundo |
| `subjectAreaRef` | REF a `SubjectArea` (componente/área) | Compliance (E6), via Planning | **Obrigatório** | mapeia para `themeTags` do KC por correspondência | forçar disciplina como recorte único (o KC é interdisciplinar) |
| `schoolYearBandRef` | REF a `SchoolYearBand` (refina a série) | Compliance (E6), via Planning | Recomendado | adequação à série no ranqueamento | desalinhar com o ano |
| `learningGoalRefs` | metas via `CurricularAlignment`/`BNCCMapping` (com `provenanceRef` F1) | Compliance (E6), via Planning | Opcional | dimensão de alinhamento curricular **confirmado** | citar código BNCC sem `provenanceRef` |
| `curricularAlignmentRefs` | REFs a `CurricularAlignment`/`BNCCMapping` selecionados | Compliance (E6), via Planning | Opcional | reforça `curricularCore`; respeita `reviewStatus` | tratar alinhamento `pending` como definitivo |
| `bnccMappingRefs` | REFs a `BNCCMapping` (apontam KC↔BNCC) | Compliance (E6) | Opcional | conecta itens a habilidades; respeita `reviewStatus` | mapear BNCC em massa / inverter direção |
| `momentQuerySeed` | semente para gerar/parametrizar uma ou mais `MomentQuery` | derivado do `PlanningProfile` (E7 §5.3) | Recomendado | aciona a função para popular o `CandidatePool` | semente vaga → correspondência ruidosa |
| `candidateSceneRefs` | REFs a `Scene` v1.1 e/ou `generatedSceneCandidate` já disponíveis | função (E5) / curadoria (E4x) | Opcional | candidatos de cena pré-existentes | tratar `generatedSceneCandidate` como gabarito |
| `accessibilityNeeds` | necessidades que **disparam** `AccessibilityRequirement` (e-MAG/WCAG/LBI) | Planning (E7) → Compliance (E6) | Recomendado | porta dura de acessibilidade quando obrigatória | excluir alunos; descumprir LBI |
| `resourceConstraints` | restrições de recursos/infraestrutura (`ResourceConstraint`) | Planning (E7) | Recomendado | compatibilidade de mídia/recurso no ranqueamento | propor experiência inviável (D10) |
| `sensitiveContentTolerance` | tolerância a sensíveis **relativa** às `SensitiveContentRule` (`padraoDaFaixa`/`maisRestritivo`) | Planning (E7) | Opcional | só **endurece** o gating; nunca afrouxa | relaxar gating além do permitido |

> **Regra transversal de entradas.** Campos textuais do professor (`theme`, `teacherObjective`, `teacherNotes`, `localContext`) são **intenção**, nunca `Claim` factual. O Matching os usa para ranqueamento e organização, sob rótulo explícito de "intenção do professor" (Seção 8); jamais os promove a fato nem os escreve no KC.

---

## 4. Entidades conceituais da camada (Tarefa 4)

Entidades **externas ao Knowledge Core, distintas das entidades da Compliance e do Planning**. Nenhuma é, vira ou recria entidade do núcleo, da Etapa 6 ou da Etapa 7. As entidades de Matching **referenciam** as demais por ID; não as duplicam. Apagar qualquer uma delas não altera um único campo do KC.

| Entidade (`CamelCase`) | Papel | Para que aponta | Observação de fronteira |
|---|---|---|---|
| **`MatchingProfile`** | consolida a configuração de uma correspondência para um `PlanningProfile` | `planningProfileRef`, `planningFilterRef`, `complianceProfileRef` | é a configuração do motor; não é o resultado |
| **`CandidatePool`** | conjunto **bruto** de candidatos extraídos do KC, da função e de cenas/momentos | `KnowledgeItem`/`Claim`/`Scene`/`MomentResult` por ID | pré-seleção; nada ainda foi rotulado nem excluído por gate |
| **`MatchCandidate`** | um candidato individual (cena, momento, claim, item, fonte, mídia, dossiê) | um alvo no KC/função/cena | unidade da seleção; carrega tipo (`candidateType`) |
| **`MatchSet`** | conjunto **final** selecionado, ranqueado, justificado e classificado por papel | `selectedCandidates`/`excludedCandidates` | é o objeto entregue à Etapa 9 |
| **`MatchScore`** | pontuação multidimensional de um candidato | dimensões da Seção 7 | **não** altera verdade factual; ordena relevância |
| **`EligibilityGate`** | porta dura de elegibilidade (aprovado/reprovado/condicional) | `reviewStatus`/`publicabilityStatus`/licença/fonte/faixa | precede o ranqueamento (Seção 6) |
| **`ExclusionReason`** | motivo tipado de exclusão de um candidato | o candidato excluído | torna a exclusão **auditável**, nunca silenciosa |
| **`SelectionRationale`** | justificativa de **por que** um candidato foi incluído e com qual papel | o candidato selecionado | transparência da inclusão |
| **`CoverageBalance`** | matriz de balanceamento da seleção (Seção 12) | o `MatchSet` como um todo | mede currículo × contexto × simultaneidade × diversidade |
| **`ComplianceGateResult`** | resultado agregado dos portões de conformidade para um candidato | `AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement`/`AllowedUseContext`/`LegalRequirement` | lê a Compliance; nunca a redefine |
| **`CurricularRoleAssignment`** | papel curricular **atribuído** a um candidato dentro do `MatchSet` | `AllowedUseContext.contextClass` + `curricularRoleScope` | **derivado** da classe da Compliance; nunca a sobrescreve |
| **`SceneMatch`** | candidato de **cena** selecionado, com modo e papel | `Scene` v1.1 / `generatedSceneCandidate` | não cria nem promove cena (Seção 11) |
| **`MomentMatch`** | candidato de **momento** selecionado a partir de um `MomentResult` | `MomentResult` (E5) | seleciona o que cabe; não altera a função |
| **`ClaimMatch`** | candidato de **claim** elegível, com seu estatuto preservado | `Claim`/`ClaimSet`/`WeightedClaim` | preserva `claimType`/`confidenceLevel`/peso |
| **`SourceSupportSummary`** | síntese de proveniência A/B que sustenta a seleção | `Source`/`Citation`/`sourceSummary` (E5) | resume "como sabemos"; não inventa atribuição |
| **`DossierMatch`** | candidato de **dossiê** selecionado (foco + claims + relações + "como sabemos") | dossiê derivado de `Scene`/`MomentResult` | não escreve o dossiê; seleciona e ordena (Seção 11) |
| **`MatchingAuditTrail`** | trilha de auditoria de entradas, portões, scores e decisões | refs de entrada + decisões | externa e descartável; registra inclusões/exclusões e itens relevantes excluídos |

> **`MatchingAuditTrail` × `ComplianceAnnotation` × `PlanningAnnotation`.** A `ComplianceAnnotation` (E6) anota **conformidade/legalidade**; a `PlanningAnnotation` (E7) anota **organização pedagógica**; a `MatchingAuditTrail` (E8) registra **como a seleção foi calculada e justificada**. As três são externas, apontam por ID e nunca editam o alvo; vivem em camadas diferentes e não se confundem.

---

## 5. `MatchingProfile`, `CandidatePool` e `MatchSet` (Tarefa 5)

Dicionários conceituais — **não são código**. Os `*Ref` apontam para entidades das Etapas 2/5/6/7.

### 5.1 `MatchingProfile`

Objeto que consolida a configuração do matching para um `PlanningProfile`. É a *entrada de configuração* do motor, distinta do resultado.

```txt
MatchingProfile = {
  matchingProfileId,
  planningProfileRef,          # REF ao PlanningProfile (E7) — âncora obrigatória (D3)
  planningFilterRef,           # REF ao PlanningFilter (E7)
  complianceProfileRef,        # REF ao ComplianceProfile (E6) — piso de conformidade
  curricularRoleScope,         # subconjunto de {curricularCore, contextual, enrichment, freeExploration}
  schoolUseModeRefs,           # subconjunto de {teacher, student, free-exploration, projector, offline}
  usageScenario,               # cenário pedagógico fino (10 valores — E7 §9)
  preferredSceneMode,          # mapeia para outputMode da função (E5 §12)
  depthLevel,                  # DepthPreference (E7 §10)
  timeBudgetRef,               # TimeBudget / lessonDuration (E7)
  regionalFocus,               # recorte de destaque (E7 §11)
  localContextRef,             # contexto local (intenção, não geografia do KC)
  subjectAreaRef,              # SubjectArea (E6)
  schoolYearBandRef,           # SchoolYearBand (E6)
  learningGoalRefs,            # metas via CurricularAlignment/BNCCMapping (com provenanceRef F1)
  curricularAlignmentRefs,     # CurricularAlignment selecionadas (respeita reviewStatus)
  bnccMappingRefs,             # BNCCMapping selecionados (respeita reviewStatus)
  momentQuerySeeds,            # sementes de MomentQuery a acionar (E5)
  candidateSceneRefs,          # Scene v1.1 / generatedSceneCandidate disponíveis
  accessibilityNeeds,          # dispara AccessibilityRequirement (E6 §6)
  resourceConstraintsRef,      # ResourceConstraint (E7 §12)
  sensitiveContentTolerance,   # padraoDaFaixa | maisRestritivo (NUNCA "mais permissivo")
  scoringPolicyRef             # pesos conceituais aplicáveis (Seção 7) — configuração, não verdade
}
```

### 5.2 `CandidatePool`

Conjunto **bruto** de candidatos extraídos do KC, da função e de cenas/momentos, **antes** de portões e ranqueamento. Pode conter itens que serão excluídos por gate; nada aqui é "aprovado" ainda.

```txt
CandidatePool = {
  candidatePoolId,
  matchingProfileRef,          # de qual MatchingProfile nasceu
  sourceOfCandidates,          # como o pool foi populado: { momentResultRefs[], sceneRefs[], graphTraversalRefs[], directKnowledgeItemRefs[] }
  candidates[],                # lista de MatchCandidate (ver 5.3) — BRUTOS
  poolCoverageNote,            # nota de cobertura bruta (camadas/regiões tocadas) — diagnóstico, não decisão
  pendingFlags                 # marcadores de itens não exibíveis presentes no pool (para transparência, nunca exibição)
}

MatchCandidate = {
  candidateId,
  candidateType,               # sceneCandidate | momentCandidate | claimCandidate | knowledgeItemCandidate
                               #   | sourceCandidate | mediaCandidate | mapCandidate | dossierCandidate | relationshipCandidate
  targetRef,                   # knowledgeItemId | claimId | sceneId | momentResultId | sourceId | mediaAssetId | mapAssetId
  rawRelevanceSignals,         # sinais brutos (interseção temporal/espacial, relação no grafo, camada 4A)
  inheritedReviewStatus,       # LIDO do KC/Scene (não alterável)
  inheritedPublicability,      # LIDO do MomentResult/Scene (não alterável)
  inheritedClaimType,          # LIDO do Claim (não alterável)
  inheritedConfidence,         # LIDO do Claim (não alterável)
  inheritedEvidence,           # LIDO do Claim (não alterável)
  allowedUseContextRef         # LIDO da Compliance (classe AllowedUseContext do item/cena)
}
```

### 5.3 `MatchSet`

Conjunto **final** selecionado, ranqueado, justificado e classificado por papel curricular, aprovado nos portões de conformidade. É o objeto que a Etapa 9 recebe.

```txt
MatchSet = {
  matchingId,
  planningProfileRef,          # a qual planejamento atende
  candidatePoolRefs,           # de quais CandidatePool derivou
  selectedCandidates[],        # ver SelectedCandidate abaixo
  excludedCandidates[],        # ver ExcludedCandidate abaixo (exclusão SEMPRE justificada)
  coverageBalance,             # CoverageBalance (Seção 12)
  sourceSupportSummary,        # SourceSupportSummary do conjunto (A/B por claim relevante)
  auditTrail,                  # MatchingAuditTrail (externo, descartável)
  matchSetStatus               # rascunho | calculado | revisadoPeloProfessor | prontoParaOutput
}

SelectedCandidate = {
  candidateRef,                # REF ao MatchCandidate
  matchScore,                  # MatchScore multidimensional (Seção 7)
  selectionRationale,          # por que entrou e com qual papel
  curricularRole,              # CurricularRoleAssignment: curricularCore | contextual | enrichment | freeExploration
                               #   (derivado de AllowedUseContext + curricularRoleScope; nunca sobrescreve a classe)
  visibilityClass,             # teacherOnly | teacherMediated | internalReviewOnly | contextualOnly | enrichmentOnly | visívelAoAluno
  requiresMediation,           # true | false — transporta TeacherMediationRequirement (E7) / SensitiveContentRule.mediation (E6)
  complianceGateResult,        # ComplianceGateResult (Seção 9)
  publicabilityStatus,         # LIDO (1–5) do MomentResult/Scene — repassado, nunca alterado
  gatingReason,                # LIDO (editorial/científico/licença/revisão-humana/geometria/mídia/fonte/legal) — repassado
  sourceSupportRef             # SourceSupportSummary do candidato
}

ExcludedCandidate = {
  candidateRef,
  exclusionReason,             # ExclusionReason tipado (Seção 6)
  relevantButExcluded,         # true | false — se era relevante mas caiu em porta dura (entra em CoverageBalance.excludedButRelevantItems)
  exclusionNote                # nota auditável (transparência sobre a ausência; nunca expõe conteúdo pending)
}
```

> **Cinco eixos de maturidade independentes.** `matchSetStatus` governa a **correspondência** (artefato do Matching); **não** se confunde com (a) `planningReviewStatus` (planejamento — E7); (b) `reviewStatus` do KC/Compliance (publicação de conteúdo); (c) `publicabilityStatus` (exibição da `Scene`/momento); (d) `sceneCompletenessLevel` (maturidade da cena como artefato de método — 4H). O Matching só escreve no primeiro.

---

## 6. Regras de elegibilidade e exclusão (Tarefa 6)

A elegibilidade obedece a três tempos, herdados da função (E5 §8): **(1) invariante de exibição → (2) gating por contexto → (3) modulação por faixa**. O invariante de exibição **precede** o ranqueamento — o não exibível **não compete** (E5 §7). Portas duras (`EligibilityGate`) excluem; o ranqueamento só opera sobre o que passou.

### 6.1 Portas duras (exclusão automática)

| Porta (`gateType`) | Condição de exclusão para exibição pública | Base |
|---|---|---|
| `reviewStatusGate` | `reviewStatus = rejected` | E2 §7.6; E5 §8 |
| `reviewStatusGate` | `reviewStatus = legal-review` (não exibível como fato; ex.: pessoas vivas) | E6 §5.4; E5 §8 |
| `reviewStatusGate` | `reviewStatus = pending` usado **como fato exibível** | invariante de exibição (1.1/3.1) |
| `publicabilityGate` | `publicabilityStatus = 5 (bloqueada)` | 4F/4H §8; E5 §8 |
| `licenseGate` | licença incompatível (`nonCommercial` como expressão; `shareAlike` atravessando o núcleo; asset `allowedUse = blocked`) | 1.1; E2 §7.2/§7.3 |
| `sourceSupportGate` | claim **sem fonte A/B** (`authorityType ∉ {primary, aggregator}`) | hard stop 1 da 1.1; E2 §7.1 |
| `sensitiveContentGate` | item sensível **oculto para a faixa** (`AgeSuitability.hiddenInBands`) | E6 §7/§8 |
| `mediaGate` | mídia **sem licença confirmada** ou sem `natureLabel` | E2 §7; 4H §8 |
| `sensitiveContentGate` | item que **viola** `SensitiveContentRule` (default oculto sem mediação/revisão) | E6 §8; E3.1 §7 |
| `ageSuitabilityGate` | item que **viola** `AgeSuitability` para a faixa do `ComplianceProfile` | E6 §7 |
| `accessibilityGate` | item **inacessível** quando há requisito **obrigatório** de acessibilidade (LBI) | E6 §6 |
| `curricularAlignmentGate` | `BNCCMapping`/`CurricularAlignment` com `reviewStatus` **não aprovado** usado como **alinhamento definitivo** | E6 §3.2/§13; E7 R-15 |
| `equivalenceGate` | conteúdo com **falsa equivalência** (negacionismo como "lado") | E5 §9; E3.1 §1/§5 |
| `claimTypeGate` | conteúdo que **confunde fato, cenário, previsão e opinião** | P28; E5 §11 Ex.7/8; E6 §11 Ex.4 |

> **Exclusão nunca é silenciosa.** Toda exclusão por porta dura gera um `ExcludedCandidate` com `exclusionReason`. Quando o item era **relevante** mas caiu por gate (ex.: sensível oculto para a faixa, ou `pending`), ele é marcado `relevantButExcluded = true` e contabilizado em `CoverageBalance.excludedButRelevantItems` — transparência sobre a ausência (análoga ao `includeHiddenSummary` da função, E5 §3), **sem** revelar conteúdo não exibível.

### 6.2 `exclusionReasonType` (lista controlada)

`rejeitado` · `emRevisaoHumana` · `emRevisaoLegal` · `pendingComoFato` · `bloqueada` · `licençaIncompatível` · `semFonteAB` · `sensívelOcultoParaFaixa` · `violaSensitiveContentRule` · `inadequadoÀIdade` · `inacessívelComRequisitoObrigatório` · `mídiaSemLicença` · `alinhamentoBNCCNãoAprovado` · `falsaEquivalência` · `confusãoFatoCenárioPrevisão` · `foraDoEscopoCurricular` *(soft — ver 6.4)* · `foraDoTempoDisponível` *(soft)* · `redundanteComItemMelhorRanqueado` *(soft)*.

### 6.3 Candidatos que aparecem **apenas** sob restrição (`visibilityClass`)

Nem todo candidato elegível é exibível ao aluno como conteúdo central. O Matching atribui uma `visibilityClass`, derivada de `AllowedUseContext` (E6 §9), `SchoolUseMode`/`usageScenario` (E6/E7) e `SensitiveContentRule`/`AgeSuitability`:

| `visibilityClass` | Significado | Quando se aplica |
|---|---|---|
| `teacherOnly` | apenas em `SchoolUseMode = teacher` (preparação) | aparato de preparação; nunca exibido ao aluno como fato |
| `teacherMediated` | exibível **com mediação humana** | tema sensível conforme a faixa (E6 §8; E7 §4 `TeacherMediationRequirement`) |
| `internalReviewOnly` | apenas em relatório interno de curadoria | itens `pending`/de risco; contabilizáveis, nunca como fato público |
| `contextualOnly` | aparece **só como contexto**, não como foco | simultâneos contextuais (E5 §7); `AllowedUseContext = contextual` |
| `enrichmentOnly` | aparece **só como enriquecimento opcional** | aprofundamento; `AllowedUseContext = enrichment` |
| `hidden` | **não exibível** | invariante de exibição (`pending`/`legal-review`/`rejected`; `publicabilityStatus = 5`) |

### 6.4 Exclusões **soft** (rebaixamento, não porta dura)

`foraDoEscopoCurricular`, `foraDoTempoDisponível` e `redundanteComItemMelhorRanqueado` **não** são portas duras: elas **rebaixam** o candidato no ranqueamento ou o movem para `contextualOnly`/`enrichmentOnly`, **nunca o apagam por estar fora da grade**. Conteúdo fora da grade permanece acessível como contexto/enriquecimento/exploração (D3; E6 §9; E7 §11.2). Reduzir por tempo é **redução de cobertura**, jamais de honestidade: corta-se contexto, não rótulo (E7 §10.2).

---

## 7. Sistema de pontuação e ranqueamento (Tarefa 7)

O Matching pontua candidatos por dimensões combinadas (não lexicográficas), com **pesos conceituais** — não números finais rígidos. Algumas linhas são **portas** (Seção 6) que **precedem** o score; aparecem aqui marcadas como `porta` para completude, mas **não somam pontos**: gatam. O ranqueamento serve à **relevância curada** (E2 §6.3; E5 §7), não a despejar tudo que coincide.

| Dimensão | O que mede | Natureza | Peso conceitual | Fonte do dado |
|---|---|---|---|---|
| Aderência ao tema | proximidade ao `theme`/`themeTags` | score | **crítico** | Planning + KC |
| Aderência ao objetivo do professor | ajuste ao `teacherObjective` | score | **crítico** | Planning |
| Alinhamento curricular **confirmado** | `CurricularAlignment`/`BNCCMapping` com `reviewStatus` aprovado | score | alto | Compliance |
| Adequação à etapa/série | ajuste a `EducationStage`/`SchoolYearBand` | score | alto | Compliance |
| Adequação etária | compatibilidade com `AgeSuitability`/`AgeLanguageProfile` | porta + modificador | crítico | Compliance |
| Adequação ao `usageScenario` | ajuste ao cenário pedagógico fino | score | médio | Planning |
| Papel em `AllowedUseContext` | classe do item dentro do `curricularRoleScope` | modificador | alto | Compliance |
| Publicabilidade | `publicabilityStatus` (1–5) | porta | crítico | função/Scene |
| Confiança | `confidenceLevel` do claim | score | alto | KC |
| Evidência | `evidenceLevel` do claim | score | alto | KC |
| Proveniência | força do `SourceSupportSummary` (A/B) | porta + score | crítico | KC |
| Acessibilidade | atendimento a `AccessibilityRequirement` | porta (se obrigatória) + score | crítico | Compliance |
| Disponibilidade de mídia/recurso | `MediaAsset`/`MapAsset` licenciados + `ResourceConstraint` | modificador | médio | KC + Planning |
| Compatibilidade com tempo disponível | ajuste a `TimeBudget`/`lessonDuration` | modificador | médio | Planning |
| Compatibilidade com profundidade | ajuste a `DepthPreference` | modificador | médio | Planning |
| Relevância regional/local | ajuste a `regionalFocus`/`localContext` | score | médio | Planning |
| Preservação da simultaneidade global | contribuição à cobertura simultânea (D8) | bônus de balanceamento | alto | função (E5) |
| Diversidade de camadas | cobertura de camadas 4A distintas | bônus de balanceamento | médio | KC (4A) |
| Cobertura África/diáspora/povos indígenas | presença estrutural quando aplicável (Leis 10.639/11.645) | bônus de balanceamento | **alto** | Compliance + KC |
| Risco editorial | `editorialRisk` do item/cena | penalidade + mediação | alto | E3.1/Scene |
| Risco científico | `scientificRisk` (incerteza alta) | penalidade (não exclusão; rótulo) | médio | Scene |
| Risco jurídico | `LegalRequirement`/`legal-review` | porta | crítico | Compliance |
| Risco de licença | `licenseRisk` do asset | porta | crítico | KC (1.1) |
| Valor de "como sabemos isso" | densidade de evidência/`sourceSummary` | bônus | alto (em `sourceAnalysis`) | função/Scene |
| Conexão com `RelationshipGraph` | riqueza de relações curadas (`contemporâneo-de`, `causou`…) | bônus | médio | KC (grafo) |

> **Score não é verdade.** A pontuação **ordena relevância pedagógica**; **não altera** `claimType`, `confidenceLevel`, `evidenceLevel`, peso de `WeightedClaim` nem estatuto factual. Um fato documentado com score baixo continua fato; uma hipótese com score alto continua hipótese. O ranqueamento muda **o que aparece primeiro**, nunca **o que é verdade**.

> **Incerteza não rebaixa por ser incerteza.** Itens de alto risco científico **não** são ocultados por incerteza — são **rotulados** (hipótese como hipótese, faixa como faixa — E5 §8.3). A penalidade de risco científico ajusta destaque/mediação, jamais suprime o rótulo nem o item legítimo.

---

## 8. Relação com `PlanningProfile` e `PlanningFilter` (Tarefa 8)

### 8.1 Como o Matching consome o planejamento

O Matching lê o `PlanningProfile`/`PlanningFilter` (E7 §5) e o converte em configuração (`MatchingProfile`) e critérios de ranqueamento, **sem reinterpretar a intenção como fato**.

| Campo do Planning (E7) | Como o Matching o consome |
|---|---|
| `teacherObjective` | dimensão de "aderência ao objetivo" (score crítico) — intenção, não claim |
| `theme` | aderência temática + sementes de `MomentQuery` (`themeTags`) |
| `learningGoalRefs` | alinhamento curricular **confirmado** (respeita `reviewStatus` e `provenanceRef`) |
| `schoolYearBandRef` | adequação à série |
| `subjectAreaRef` | mapeamento para `themeTags`; **não** trava o KC interdisciplinar |
| `depthLevel` | calibra densidade/aparato; opera dentro do teto da faixa |
| `lessonDuration` | limita itens-âncora; foco em `mainItems` sob tempo curto |
| `regionalFocus` | relevância regional + parametriza `spatialInput` da função |
| `curricularRoleScope` | quais classes `AllowedUseContext` entram no `MatchSet` |
| `schoolUseModeRefs` | governa `visibilityClass` |
| `usageScenario` | modula gating, mediação e densidade |
| `accessibilityNeeds` | porta dura de acessibilidade quando obrigatória |
| `availableResources` | compatibilidade de mídia/recurso |
| `sensitiveContentTolerance` | só **endurece** o gating de sensíveis |

### 8.2 Intenção não é fato (regra vinculante)

O Matching **não reinterpreta a intenção do professor como verdade**. Campos textuais (`theme`, `teacherObjective`, `teacherNotes`, `localContext`) são **intenção declarada**, usada para ranqueamento e organização, sempre sob rótulo "intenção do professor". O Matching **nunca**:

- transforma uma nota do professor em `Claim` factual;
- escreve qualquer campo no KC;
- deixa a intenção sobrepor o estatuto epistêmico de um item (um objetivo do professor não torna uma hipótese um consenso);
- usa a intenção para **afrouxar** gating de faixa, sensíveis, acessibilidade ou licença (a intenção só pode **endurecer**, via `sensitiveContentTolerance`).

---

## 9. Relação com a `BrazilianEducationComplianceLayer` (Tarefa 9)

### 9.1 Como o Matching usa cada entidade da Compliance

O Matching **consome** os perfis e anotações da Etapa 6; **não os cria nem os redefine**. Ele lê a conformidade e a aplica sobre os candidatos.

| Entidade da Compliance (E6) | Como o Matching a usa | O que o Matching **não** faz |
|---|---|---|
| `ComplianceProfile` | piso de conformidade de toda a seleção (etapa/região/acessibilidade/perfil etário) | não edita o perfil nem cria exceções permissivas |
| `AgeLanguageProfile` | deriva `ageLevelMode`; calibra densidade/linguagem/mídia | não redefine os 5 níveis de exposição (E3.1 §6) |
| `AllowedUseContext` | fonte da classe curricular por item (7 classes) | **não redefine a classe**; só **atribui papel** dentro do `curricularRoleScope` |
| `AgeSuitability` | porta de adequação etária + mediação por faixa | não rebaixa a exigência; não altera o fato |
| `SensitiveContentRule` | porta de sensíveis (default oculto/mediação/revisão) | não relaxa mediação/ocultação; não apaga (media) |
| `AccessibilityRequirement` | porta dura quando obrigatória (LBI) | não cria UX; não trata como enfeite |
| `LegalRequirement` | porta jurídica (LGPD Art. 14, LBI Art. 63, Marco Civil) | não inventa obrigação; não coleta dado de aluno |
| `BrazilianEducationConstraint` | exige cobertura estrutural (afro/indígena) no balanceamento | não viola a cobertura obrigatória; não a trata como opcional |
| `CurricularAlignment` | dimensão de alinhamento **confirmado** (respeita `reviewStatus`) | **não cria alinhamento**; não promete homologação/PNLD |
| `BNCCMapping` | conecta itens a habilidades (respeita `reviewStatus`/`provenanceRef`) | **não mapeia BNCC em massa**; não inverte a direção |
| `ComplianceAnnotation` | lê anotações de conformidade sobre a saída | não as edita; usa `MatchingAuditTrail` própria |
| `SchoolUseMode` | governa `visibilityClass` | não cria modo; não mistura modo com permissão de conteúdo |

### 9.2 Regras obrigatórias

1. **O Matching não redefine a Compliance.** Ele aplica as regras da Etapa 6; não as cria, edita nem afrouxa.
2. **Não inventa alinhamento BNCC.** Só usa `CurricularAlignment`/`BNCCMapping` existentes, com `provenanceRef` (F1).
3. **Não transforma a BNCC em fonte do conteúdo.** A BNCC referencia o KC; o conhecimento existe independentemente dela (P1/P2; E6 §3.1).
4. **Não trata `BNCCMapping`/`CurricularAlignment` `pending` como definitivo.** Alinhamento não aprovado é porta dura para uso como alinhamento definitivo (Seção 6; E6 §3.2/§13).
5. **Não permite que o professor relaxe sensíveis.** `sensitiveContentTolerance` só **endurece**; o piso da Etapa 6 e da Etapa 3.1 é inviolável (regra de ouro: na dúvida, sobe-se o cuidado — PE-Ed4).
6. **Não apaga conteúdo fora da grade.** Conteúdo fora do `curricularRoleScope` vira `contextual`/`enrichment`, nunca exclusão por estar fora da grade (D3; E6 §9).
7. **Não confunde `AllowedUseContext` com modo de sala.** A classe curricular (papel do item) e o `SchoolUseMode` (modo de entrega/uso) são eixos distintos; o Matching os combina sem misturá-los.

> **Alinhamento ≠ homologação ≠ PNLD.** O Matching preserva a distinção da Etapa 6 (§4.3): referenciar `CurricularAlignment` indexa; **não** declara homologação MEC nem aprovação PNLD. Nenhum campo do `MatchSet` pode sugerir homologação/PNLD (Seção 13).

---

## 10. Relação com `WhatWasHappeningAtMoment` (Tarefa 10)

### 10.1 O Matching aciona e consome a função

A função (E5) entrega **o mundo consultado**; o Matching **seleciona o que cabe no planejamento**. O Matching pode **acionar** a função (via `momentQuerySeeds` derivadas do `PlanningProfile`, E7 §5.3) e **consumir** o `MomentResult`, **sem alterá-la** — não modifica seus 13 tipos de consulta, sua normalização, seu gating nem seus invariantes (E5 §13).

| Campo do `MomentResult` (E5 §4) | Como o Matching o consome |
|---|---|
| `mainItems` | candidatos de **foco** → tendem a `curricularCore` |
| `simultaneousItems` | candidatos **simultâneos** → `contextual`/`enrichment` conforme escopo e relevância |
| `backgroundStates` / `states` | States de fundo → contexto do momento (`contextual`) |
| `hiddenItems` | **nunca** exibidos; entram só como contagem/transparência (`internalReviewOnly`/`excludedButRelevant`) |
| `sourceSummary` | alimenta `SourceSupportSummary` |
| `confidenceSummary` | informa o ranqueamento (confiança/evidência) |
| `anachronismWarnings` | **repassados** integralmente ao `MatchSet` |
| `equivalenceWarnings` | **repassados**; mantêm negacionismo fora do `ClaimSet` |
| `generatedSceneCandidate` | candidato de cena (vira `SceneMatch`; ver Seção 11) |

### 10.2 Exemplos conceituais (alinhados aos da função, E5 §11, e da Compliance, E6 §11)

**Ex. 1 — Revolução Francesa em 1789 (História, 8º/9º ano, 12–14).** A função devolve França/1789 (foco), Inconfidência Mineira/EUA/Lavoisier (simultâneos), States econômicos/populacionais, e `anachronismWarnings` ("Brasil = colônia, via `ModernCorrespondence`"). O Matching seleciona França/1789 como `curricularCore`; Inconfidência Mineira/EUA/Lavoisier como `contextual`; escravidão/colonização como `teacherMediated`; mídia gráfica como `hidden` < 15; e repassa os warnings. `gatingReason = editorial`.

**Ex. 2 — GOE em ~2,4 Ga (Ciências, Ensino Médio, 15–17).** A função devolve `AtmosphereState`/`OceanographicState` em destaque, paleogeografia **rotulada** como reconstrução modelada (não "foto"), confiança que decai com a idade, zero `Event`. O Matching seleciona States e o `Process` GOE como foco; "como sabemos" (proxies) como `sourceAnalysis`; preserva os rótulos de incerteza. `gatingReason = científico + geometria`.

**Ex. 3 — K-Pg em ~66 Ma (Ciências, EF II, 12–14).** A função devolve o `Event`-gatilho (impacto Chicxulub), `cascadeStructure`, States (Bio/Atm/Ocean), paleoposições rotuladas, `weightedClaimSets` (impacto ≫ Deccan). O Matching seleciona o gatilho e a cascata como foco; respeita os pesos (sem falsa equivalência); marca reconstruções `representação artística`; o marcador fica na **paleoposição**, não na coordenada atual. `gatingReason = científico`.

**Ex. 4 — Clima moderno (Geografia/Ciências, EM): fato × cenário × previsão.** A função separa **fato físico** (séries medidas), **cenário** (modelo RCP/SSP) e **previsão** (faixa, não número cravado); `equivalenceWarnings` mantêm negacionismo fora do `ClaimSet`. O Matching seleciona preservando essa separação (P28): o consenso entra `primário`; as faixas de projeção, `secundário`; o negacionismo, `rotulado-rejeitado`, fora do `ClaimSet`. O `claimTypeGate` (Seção 6) **exclui** qualquer candidato que misture fato, cenário e previsão.

**Ex. 5 — Recorte Brasil/ES ou local.** `regionalFocus = espiritoSanto`; `localContext = "Vitória/ES, escola pública"`. O Matching destaca o ES **sem apagar** o restante do mundo no mesmo tempo: itens do ES recebem relevância regional alta; o que coexistia em outras regiões permanece a um clique como `contextual`/`enrichment` (D8; E7 §11.2). A lente Brasil inclui a história profunda indígena sob as Leis 10.639/11.645.

**Ex. 6 — Exploração livre mediada (D3).** Aqui a fronteira é fina. A **exploração livre pura** (aluno, sem `PlanningProfile`) **não passa pelo Matching**: vai do KC à experiência só com o filtro de adequação da Compliance (E0 D3; E7 §2.1). Quando o professor **curou** uma sessão de exploração (`usageScenario = freeExplorationWithAgeGate` dentro de um `PlanningProfile`), o Matching **pode** prepará-la — mas **não** pode impor gating curricular que suprima conteúdo fora da grade: por definição, esse cenário **não tem recorte curricular** (E7 §7.2 Ex.5). Aparece o **fato** em linguagem adequada, com agência/resistência e simultaneidade; sensível `teacherMediated`/`restricted` conforme a faixa; `pending`/`legal-review` não aparece.

> **Invariante de todos os exemplos.** O Matching respeita os limites da função: não inventa dados, não exibe `pending` como fato, não trata IA como fonte, não cria falsa equivalência e não promove cena a gabarito (E5 §13). O Matching **não pode afrouxar** nenhum desses limites.

---

## 11. Relação com `Scene` v1.1 e dossiês (Tarefa 11)

### 11.1 O que o Matching seleciona

O Matching **lê** e **seleciona** — nunca cria nem altera — cenas, candidatas de cena e dossiês, com seus claimsets, States, cascatas e políticas espaciais.

| Objeto (E4F/4H/5) | Como o Matching o trata |
|---|---|
| `Scene` v1.1 existente | candidata de cena (`SceneMatch`); lê `sceneCompletenessLevel`/`publicabilityStatus`/`gatingReason` |
| `generatedSceneCandidate` | candidata de cena; **nunca** tratada como gabarito |
| dossiês | candidatos de dossiê (`DossierMatch`); seleciona e ordena blocos |
| `claimSets` / `weightedClaimSets` | `ClaimMatch` com peso preservado; respeita `displayWeight` |
| `states` / 11 `State Types` | candidatos de contexto do momento |
| `cascadeStructure` | seleciona a cascata como foco quando há `triggerItem`; preserva `confidenceByStage` decaindo |
| `paleoPositionPolicy` | repassa a política; o marcador fica na paleoposição rotulada |
| `sourceSummary` | alimenta `SourceSupportSummary` |
| `MediaAsset`/`MapAsset` | seleciona apenas assets licenciados, com `natureLabel` |

### 11.2 `SceneMatch` e `DossierMatch`

```txt
SceneMatch = {
  sceneMatchId,
  sceneRef,                    # REF a Scene v1.1 ou generatedSceneCandidate (E5/4H)
  selectedOutputMode,          # mapeado de preferredSceneMode (E7 §8) → outputMode (E5 §12)
  scenePatternTypeRead,        # LIDO da cena (histórica pontual … contemporânea … evidência/proxy — 4H §6)
  curricularRole,              # curricularCore | contextual | enrichment | freeExploration (derivado)
  visibilityClass,             # teacherOnly | teacherMediated | … | hidden
  requiresMediation,
  publicabilityStatusRead,     # LIDO (1–5) — NUNCA alterado
  sceneCompletenessLevelRead,  # LIDO (rascunho | gabarito-interno | publicável) — NUNCA alterado
  gatingReasonRead,            # LIDO (editorial/científico/…) — NUNCA removido
  selectedClaimSetRefs,        # subconjunto de claimSets/weightedClaimSets selecionados (peso preservado)
  selectedStateRefs,           # States selecionados
  cascadeSelected,             # true | false (e qual cascadeStructure, se houver)
  paleoPositionPolicyRead,     # LIDO — repassado
  sourceSupportRef,            # SourceSupportSummary da cena
  matchScore,
  selectionRationale
}

DossierMatch = {
  dossierMatchId,
  dossierSourceRef,            # de qual Scene/MomentResult o dossiê deriva
  selectedBlocks,              # blocos selecionados/ordenados (foco, simultaneidade, "como sabemos", consequências)
  evidenceEmphasis,            # ênfase em evidência conforme depthLevel (sourceAnalysis ↑)
  curricularRole,
  visibilityClass,
  requiresMediation,
  publicabilityStatusRead,     # LIDO — repassado
  gatingReasonRead,            # LIDO — repassado
  sourceSupportRef,
  matchScore,
  selectionRationale
}
```

### 11.3 Regras sobre a `Scene`

1. **O Matching não cria cena.** Criação é da função (`generatedSceneCandidate`) e da curadoria (E4x/E5 §10).
2. **Não promove cena a gabarito.** `gabarito-interno` é decisão de curadoria (12 critérios, 4H §9).
3. **Não altera `sceneCompletenessLevel`.** Lê e repassa; nunca escreve.
4. **Não altera `publicabilityStatus`.** Lê e repassa; cena `bloqueada` (5) ou com itens `pending`/`legal-review` **não** é apresentada ao aluno (invariante absoluto).
5. **Não remove `gatingReason`.** O motivo do gating é transportado integralmente; a mediação exigida vira `requiresMediation`.
6. **Não oculta incerteza para parecer mais didático.** `UncertaintyProfile`, `claimSets`/`weightedClaimSets` e rótulos epistêmicos são preservados; reduzir profundidade (`depthLevel`) corta **cobertura**, nunca **rótulo** (E7 §10).

---

## 12. Balanceamento curricular, epistêmico e de simultaneidade (Tarefa 12)

### 12.1 Critérios de balanceamento

O Matching equilibra a seleção em vários eixos, de modo que o `MatchSet` não vire nem uma lista eurocêntrica, nem um amontoado fora de foco, nem uma narrativa que esconde incerteza:

- **foco curricular** (`curricularCore`) preservado como âncora, sem virar limite;
- **contexto simultâneo** preservado (D8) — o mundo no mesmo tempo permanece a um clique;
- **exploração livre** e **enriquecimento** disponíveis para o que está fora da grade;
- **mediação** marcada onde a faixa/sensível exige (`requiresMediation`);
- **diversidade geográfica** e **diversidade de camadas** (4A) — evitar monocultura temática;
- **lente Brasil** sempre disponível (D8), incluindo história profunda indígena;
- **África/diáspora** e **povos indígenas** como cobertura **estrutural** (Leis 10.639/11.645; E6 §8.3), não nota de rodapé;
- **história local** valorizada sem apagar o restante do mundo;
- **tempo profundo** e **ciência moderna** ambos representáveis no mesmo eixo;
- **fontes e evidências** ("como sabemos") presentes conforme profundidade;
- **incerteza** preservada como faixa; **controvérsia legítima** como `ClaimSet` com peso;
- **prevenção de falsa equivalência** — negacionismo `rotulado-rejeitado`, fora do `ClaimSet`.

### 12.2 `CoverageBalance`

```txt
CoverageBalance = {
  coverageBalanceId,
  matchingRef,                     # a qual MatchSet pertence
  curricularCoverage,              # quão bem o foco curricular foi coberto
  contextualCoverage,              # presença de simultâneos contextuais
  enrichmentCoverage,              # presença de aprofundamento opcional
  freeExplorationAvailability,     # o mundo permanece navegável no mesmo tempo? (D8)
  regionalBalance,                 # diversidade geográfica; lente Brasil; antieurocentrismo
  layerBalance,                    # diversidade de camadas 4A
  evidenceBalance,                 # presença de "como sabemos" / fontes A/B
  sensitiveContentHandling,        # sensíveis mediados/rotulados, nunca apagados nem liberados indevidamente
  accessibilityCoverage,           # requisitos de acessibilidade atendidos
  sourceDiversity,                 # variedade de fontes A/B sustentando a seleção
  africaDiasporaIndigenousCoverage,# cobertura estrutural (Leis 10.639/11.645) quando aplicável
  excludedButRelevantItems         # itens relevantes excluídos por porta dura, contabilizados (transparência)
}
```

> **O balanceamento não inventa cobertura.** Se o KC ainda não tem itens suficientes para uma região/camada, o `CoverageBalance` **registra a lacuna** (e o `MatchingAuditTrail` a expõe) — o Matching **não cria** itens para "preencher" o equilíbrio. A cobertura estrutural é garantida pelo KC, pela política editorial e pelas `BrazilianEducationConstraint`; o Matching **mede e sinaliza**, não fabrica.

---

## 13. Riscos educacionais, jurídicos, editoriais e operacionais (Tarefa 13)

| # | Risco | Mitigação |
|---|---|---|
| **R-1** | **Matching virar autor de conteúdo** | regra de fundação: leitor/seletor/ranqueador; nunca escreve `Claim`/`Source`/`Scene`/`reviewStatus` (Seção 1) |
| **R-2** | **Score confundido com verdade** | invariante "score não altera estatuto factual" (Seção 7); `claimType`/confiança preservados |
| **R-3** | **BNCC virar origem do conhecimento** | a BNCC referencia o KC; o conhecimento existe sem ela (P1/P2; Seção 9) |
| **R-4** | **Alinhamento `pending` virar definitivo** | `curricularAlignmentGate` exclui uso de mapeamento não aprovado como alinhamento definitivo (Seção 6) |
| **R-5** | **Conteúdo sensível liberado indevidamente** | `sensitiveContentGate`/`ageSuitabilityGate` + `SensitiveContentRule`/`AgeSuitability`; `sensitiveContentTolerance` só endurece |
| **R-6** | **Professor relaxar mediação** | mediação é piso da Compliance/Etapa 3.1; o Matching só **endurece**; `requiresMediation` transporta a exigência |
| **R-7** | **Falsa equivalência** | `equivalenceGate` + `weightedClaimSets`; negacionismo `rotulado-rejeitado` fora do `ClaimSet` (E5 §9) |
| **R-8** | **Eurocentrismo** | simultaneidade global preservada (D8); lente Brasil sempre disponível; bônus de balanceamento |
| **R-9** | **Apagamento de África / povos indígenas** | Leis 10.639/11.645 como cobertura estrutural via `BrazilianEducationConstraint` (E6 §8.3); `CoverageBalance` mede |
| **R-10** | **Excesso de conteúdo** | `depthLevel` + `TimeBudget` controlam densidade; foco em `mainItems` sob tempo curto (Seção 7) |
| **R-11** | **Perda da simultaneidade global** | `freeExplorationAvailability`/`regionalBalance` no `CoverageBalance`; exclusões fora da grade são **soft**, não duras (Seção 6.4) |
| **R-12** | **Item relevante excluído sem justificativa** | exclusão **sempre** gera `ExclusionReason`; `excludedButRelevantItems` torna a ausência transparente (Seção 6.1) |
| **R-13** | **Uso de mídia sem licença** | `licenseGate`/`mediaGate`: só assets licenciados, com `natureLabel` (1.1; E2 §7) |
| **R-14** | **Dependência de internet rápida** | `resourceConstraints` + `SchoolUseMode = offline/projector` no ranqueamento; degradação declarada (D10) |
| **R-15** | **Acessibilidade insuficiente** | `accessibilityGate` quando obrigatória (LBI); `accessibilityNeeds` dispara `AccessibilityRequirement` (E6 §6) |
| **R-16** | **Dado de aluno usado no ranqueamento** | turma **agregada** (E7); LGPD Art. 14 como fundação; **nenhum** dado pessoal entra no Matching (E6 §5) |
| **R-17** | **IA usada como fonte factual** | IA jamais é fonte (A3/Q5; 1.1; E6 §5.3); o Matching seleciona conteúdo curado, não invoca IA para criar fato |
| **R-18** | **Clima moderno misturando fato, cenário e previsão** | `claimTypeGate` exclui mistura (P28; Seção 6); a função já separa as três (E5 §11 Ex.7/8) |
| **R-19** | **Pessoas vivas sem `legal-review`** | `reviewStatusGate` exclui `legal-review` da exibição como fato (E6 §5.4) |
| **R-20** | **Matching gerar plano de aula antes da Etapa 9** | fronteira rígida: o Matching para no `MatchSet`; plano/atividade/quiz/rubrica/material são da Etapa 9 (Seções 1, 14) |
| **R-21** | **Promessa indevida de homologação MEC/PNLD** | alinhamento ≠ homologação ≠ PNLD (E6 §4.3); nenhum campo do `MatchSet` sugere homologação |
| **R-22** | **`AllowedUseContext` confundido com modo de sala** | classe curricular e `SchoolUseMode` são eixos distintos, combinados sem mistura (Seção 9.2) |

---

## 14. Fronteiras com as Etapas 9–14 (Tarefa 14)

| Etapa | Papel | Onde a Etapa 8 termina |
|---|---|---|
| **Etapa 9 — Pedagogical Output Layer** | **recebe** o `MatchSet` e o transforma em plano de aula, roteiro, trilha, atividade, quiz, avaliação, rubrica, guia do professor e material do aluno | a Etapa 8 entrega o `MatchSet` selecionado/justificado; **não** gera nenhum desses artefatos |
| **Etapa 10 — Design/UX 3D** | mostra os resultados em interface (timeline, globo, popups, modos professor/estudante/exploração livre); implementação concreta de acessibilidade | a Etapa 8 é conceitual; **não** desenha telas |
| **Etapa 11 — Arquitetura técnica** | implementa o motor, APIs, permissões, engenharia de privacidade (LGPD/menores) e **isolamento físico** de licenças SA/ODbL | a Etapa 8 não define stack, persistência nem implementação |
| **Etapa 12 — MVP** | escolhe o **recorte mínimo** do Matching para o primeiro corte | a Etapa 8 não propõe MVP |
| **Etapa 13 — Pipeline de ingestão** | alimenta os candidatos com **dados reais**, snapshots, validação e confirmação de licença por asset | a Etapa 8 só **consome** candidatos; não faz ingestão |
| **Etapa 14 — Validação escolar, jurídica e comercial** | testa com professores, escola, jurídico e comercial; decide sobre PNLD/compra pública | a Etapa 8 não valida nem promete adoção/homologação |

> A Etapa 8 **não executa** nenhuma dessas. Ela entrega a gramática de correspondência e o `MatchSet`; tudo a montante e a jusante pertence às etapas próprias.

---

## 15. Encerramento e handoff para a Etapa 9 (Tarefa 15)

### 15.1 O que esta etapa entrega

A Etapa 8 entrega a **arquitetura conceitual do `ContentMatchingEngine`**: a definição da camada como tradutora de **intenção pedagógica estruturada em seleção justificada e conforme**; sua posição na direção única de dependência; a matriz de entradas; dezessete entidades conceituais externas (incluindo `MatchingProfile`, `CandidatePool`, `MatchCandidate`, `MatchSet`, `MatchScore`, `EligibilityGate`, `ExclusionReason`, `SelectionRationale`, `CoverageBalance`, `ComplianceGateResult`, `CurricularRoleAssignment`, `SceneMatch`, `MomentMatch`, `ClaimMatch`, `SourceSupportSummary`, `DossierMatch`, `MatchingAuditTrail`); os dicionários conceituais de `MatchingProfile`/`CandidatePool`/`MatchSet`; as portas duras de elegibilidade e os motivos de exclusão tipados; as classes de visibilidade; o sistema de pontuação com pesos conceituais (e o invariante "score não é verdade"); a relação de **consumo** com o Planning (intenção, nunca fato); a relação de **aplicação** com a Compliance (sem redefini-la); a relação de **acionamento/consumo** com a função (o mundo consultado × o que cabe no planejamento), com seis exemplos; a relação de **seleção** com `Scene` v1.1 e dossiês (sem criar cena nem promover gabarito); a matriz `CoverageBalance` de balanceamento curricular/epistêmico/de simultaneidade; vinte e dois riscos com mitigação; e as fronteiras com as Etapas 9–14.

### 15.2 O que a Etapa 9 deverá fazer

A **Etapa 9 — Pedagogical Output Layer** receberá o `MatchSet` e criará as saídas pedagógicas finais — plano de aula, roteiro, trilha, atividade, quiz, avaliação, rubrica, material do aluno e guia do professor. A Etapa 9 deve **citar claims do KC**, **respeitar o `MatchSet`** e **preservar** fontes, incerteza, publicabilidade, mediação e acessibilidade — sem inventar fatos (A3/Q5) e sem reabrir a seleção, a conformidade ou a verdade.

### 15.3 O que a Etapa 8 ainda **não** fez (e por quê)

Não criou plano de aula, roteiro, trilha, atividade, quiz, avaliação, rubrica ou material do aluno (Etapa 9); não desenhou UX (Etapa 10); não definiu stack (Etapa 11); não propôs MVP (Etapa 12); não fez ingestão (Etapa 13); não validou nem prometeu adoção/homologação (Etapa 14); não criou cena nem promoveu gabarito; não mapeou BNCC em massa; não alterou `Claim`/`reviewStatus`/`publicabilidade`; não usou IA como fonte factual; não usou dado pessoal de aluno; não criou analytics/LMS; e não relaxou LGPD, acessibilidade nem conteúdo sensível. Tudo isso é contingente ou pertence a etapas próprias; o Matching permanece **leitor, seletor e ranqueador** externo ao núcleo.

---

## Encerramento e handoff

Esta etapa (v1.0) entrega a **arquitetura conceitual do Content Matching Engine**: a definição da camada como motor que **seleciona, ranqueia, exclui, justifica e agrupa** conteúdos adequados a um planejamento, transformando o `PlanningProfile`/`PlanningFilter` em um `MatchSet` selecionado, ranqueado, justificado, auditável e conforme; sua posição entre o Output e o Planning; a matriz de entradas; as dezessete entidades conceituais externas e distintas das do KC, da Compliance e do Planning; os dicionários de `MatchingProfile`/`CandidatePool`/`MatchSet`; as portas duras de elegibilidade (invariante de exibição precedendo o ranqueamento), os motivos de exclusão tipados e as classes de visibilidade; o sistema de pontuação multidimensional com pesos conceituais e o invariante "score não altera estatuto factual"; a relação de consumo com o Planning (intenção, nunca claim); a relação de aplicação com a Compliance (sem redefini-la, sem inventar BNCC, sem tratar `pending` como definitivo, sem relaxar sensíveis, sem apagar conteúdo fora da grade, sem confundir `AllowedUseContext` com modo de sala); a relação de acionamento/consumo com a função `WhatWasHappeningAtMoment` (o mundo consultado × o que cabe no planejamento), com seis exemplos (1789; GOE em 2,4 Ga; K-Pg em 66 Ma; clima moderno com fato × cenário × previsão; recorte Brasil/ES; exploração livre mediada, com a ressalva D3 de que a exploração livre **pura** não passa pelo Matching); a relação de seleção com `Scene` v1.1 e dossiês (`SceneMatch`/`DossierMatch`, sem criar cena, sem promover gabarito, sem alterar `sceneCompletenessLevel`/`publicabilityStatus`, sem remover `gatingReason`, sem ocultar incerteza); a matriz `CoverageBalance` de balanceamento curricular, epistêmico e de simultaneidade (com cobertura estrutural de África/diáspora/povos indígenas e itens relevantes excluídos contabilizados); vinte e dois riscos com mitigação; e as fronteiras com as Etapas 9–14. Nada aqui cria saída pedagógica, UX, stack, MVP, ingestão, cena nova ou mapeamento BNCC em massa; nada altera claims, `reviewStatus` ou publicabilidade; nada usa IA como fonte factual ou dado pessoal de aluno; nada relaxa LGPD, acessibilidade ou conteúdo sensível; nada promete homologação MEC/PNLD; e nada trata recurso complementar como substituto do currículo. A direção única de dependência permanece invertida: Experience → Output → **Matching** → Planning → Compliance → Knowledge Core.

**Handoff:** com a Etapa 8 (v1.0) aprovada, a **Etapa 9 — Pedagogical Output Layer** pode ser executada, recebendo o `MatchSet` deste motor e transformando-o em plano de aula, roteiro, trilha, atividade, quiz, avaliação, rubrica, guia do professor e material do aluno — citando claims do KC, respeitando o `MatchSet` e preservando fontes, incerteza, publicabilidade, mediação e acessibilidade, sem reabrir a seleção, a conformidade ou a verdade. O resíduo curatorial herdado da Etapa 6 permanece: os `BNCCMapping`/`CurricularAlignment` concretos seguem `pending` até confirmação com o texto homologado (F1) — o Matching os **referencia e respeita o `reviewStatus`**, sem resolvê-los.

*Documento de entrega da Etapa 8 (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7). Define somente a estrutura conceitual do motor de correspondência de conteúdo. Não modela novos dados do núcleo, não escreve código, não propõe MVP, não define stack, não desenha UX final, não cria saída pedagógica, não cria cena nova, não promove cena a gabarito, não mapeia BNCC em massa, não povoa o Knowledge Core, não altera claims e não usa dados pessoais reais de alunos. Próxima etapa, quando solicitada: Etapa 9 — Pedagogical Output Layer.*
