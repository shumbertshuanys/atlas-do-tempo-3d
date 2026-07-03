# Etapa 7 — Teacher/School Planning Layer

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.1** (reconciliada com a Etapa 6 v1.0 — substitui o rascunho v1.0)
**Status:** Entrega da **Etapa 7** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z) e a **`BrazilianEducationComplianceLayer` (Etapa 6, baseline v1.0)** · 13/06/2026

**Natureza desta etapa.** Documento de **arquitetura conceitual** da camada de planejamento docente/escolar. Define **somente a estrutura conceitual do planejamento** — a *gramática de intenção pedagógica* —, não a saída pedagógica final. Conforme solicitado, esta etapa **não** cria plano de aula, atividade, quiz, rubrica, avaliação, material do aluno ou roteiro pedagógico final; **não** cria UX/telas; **não** propõe MVP; **não** define stack técnica; **não** escreve código; **não** cria o Content Matching Engine; **não** mapeia BNCC em massa; **não** cria nova cena; **não** povoa o Knowledge Core; **não** altera claims; **não** usa dados pessoais reais de alunos; **não** cria analytics de aprendizagem; **não** cria integração LMS; **não** promete homologação MEC nem aprovação PNLD; e **não** trata o recurso complementar como substituto do currículo.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Blocos ```txt``` são **dicionário conceitual, nunca código executável**. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6).

> **Nota de revisão (v1.1).** O documento integral da Etapa 6 foi analisado e esta versão **reconcilia** toda referência às suas entidades. Correções aplicadas em relação ao rascunho v1.0:
> 1. **`SchoolUseMode` (Etapa 6) tem cinco valores** — `teacher`/`student`/`free-exploration`/`projector`/`offline`. O rascunho havia criado dez `schoolUsageMode` que colidiam com essa entidade. Os dez modos passam a ser **`usageScenario`** (cenários pedagógicos finos da camada de planejamento) que **se aninham** sob um ou mais `schoolUseModeRefs` da Compliance (Seção 9).
> 2. **`AllowedUseContext` (Etapa 6) é a taxonomia de sete classes de papel curricular** por item/cena (`curricularCore`/`contextual`/`enrichment`/`freeExploration`/`teacherMediated`/`restricted`/`hidden`), não um "contexto de sala". O planejamento não o define por item; ele apenas **escolhe o escopo** (`curricularRoleScope`) — quais classes incluir na seleção (Seções 3, 6, 7).
> 3. **`ComplianceProfile` (Etapa 6) já agrega** `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef` e `policyRefs[]`. A seleção primária do planejamento passa a ser `complianceProfileRef`; série/componente apenas **refinam** (Seção 5).
> 4. **Entidades agora corretamente referenciadas/respeitadas** (nunca recriadas): `AgeSuitability`, `AccessibilityRequirement`, `SensitiveContentRule`, `LegalRequirement`, `BrazilianEducationConstraint`, `ComplianceAnnotation`, `CurricularAlignment`, `BNCCMapping`, `BNCCSkill`/`BNCCCompetency`/`BNCCKnowledgeObject` (Seções 4 e 6).
> 5. **Formas de campo alinhadas** às definições reais (ex.: `BNCCMapping` = `mappingId`/`skillCodeRef`/`knowledgeItemRefs[]`/…; `AgeLanguageProfile` carrega `bandRef`).
> O que se manteve do v1.0: a direção única de dependência; a natureza externa e somente-leitura/seleção da camada; a distinção alinhamento ≠ homologação ≠ PNLD; a preservação da simultaneidade global; e o modelo de anotação externa descartável.

---

## Sumário

1. Definição da `TeacherSchoolPlanningLayer`
2. Papel do professor, escola e coordenação pedagógica
3. Entradas do planejamento
4. Entidades conceituais da camada
5. `PlanningProfile` e modelo de anotação
6. Relação com a `BrazilianEducationComplianceLayer`
7. Relação com `WhatWasHappeningAtMoment`
8. Relação com `Scene` v1.1 e `MomentResult`
9. Modos e cenários de uso escolar
10. Profundidade, tempo disponível e nível da turma
11. Recorte local, regional e lente Brasil
12. Restrições escolares, acessibilidade e infraestrutura
13. Riscos educacionais, jurídicos e operacionais
14. Fronteiras com as Etapas 8–14
15. Próximos passos e handoff para a Etapa 8

---

## 1. Definição da `TeacherSchoolPlanningLayer` (Tarefa 1)

### 1.1 Natureza

A **`TeacherSchoolPlanningLayer`** é uma **camada externa ao Knowledge Core** que **traduz intenção pedagógica em parâmetros estruturados de consulta e filtragem**. É o ponto onde um agente humano da escola — professor, coordenação ou rede — declara *o que pretende ensinar, para quem, em qual contexto, com qual profundidade, sob quais restrições e com qual recorte* — e converte essa declaração em entradas legíveis pelas camadas a jusante (Compliance, Matching, Output, Experience).

Três consequências estruturais, herdadas das etapas anteriores:

1. **É contingente, não universal.** Diferente do KC (universal e estável), o planejamento varia por país, rede, escola, ano, turma e calendário. Por isso **nunca entra no núcleo** (Etapa 2, §10; P1/P2). Vive por fora, como registro próprio que **aponta para** o núcleo por ID estável.
2. **É leitura e seleção, não escrita.** A camada **não cria nem altera** `Claim`, `Source`, `Event`, `Process`, `State`, `Scene` ou qualquer conhecimento universal. Ela **seleciona, filtra, anota e parametriza** sobre a saída da função (`MomentResult`) e sobre os perfis e anotações da Compliance. Criação/edição/aprovação de conteúdo permanece sob curadoria humana (Etapas 4x/13).
3. **Respeita a direção única de dependência.**

```
Experience → Output → Matching → PLANNING → Compliance → Knowledge Core
```

A Planning aponta para a Compliance e para o KC (por `knowledgeItemId`/`claimId`); **o KC nunca aponta para a Planning** e a Compliance nunca depende dela. Apagar a camada de planejamento não deixa campo órfão a montante (teste de P2).

### 1.2 As nove perguntas que a camada responde

| # | Pergunta | O que captura |
|---|---|---|
| 1 | **Quem está planejando?** | papel do agente (professor, coordenação, escola, rede) — Seção 2 |
| 2 | **Para qual turma?** | etapa, ano/série, nível de prontidão **agregado** — `ClassContext` |
| 3 | **Em qual contexto escolar?** | público/privado, modo de uso, infraestrutura, calendário — `SchoolContext` |
| 4 | **Com qual objetivo?** | objetivo do professor e metas — `InstructionalGoal` |
| 5 | **Com qual profundidade?** | nível de profundidade e densidade — `DepthPreference` (Seção 10) |
| 6 | **Com quais restrições?** | tempo, recursos, acessibilidade, offline — `ResourceConstraint`/`PedagogicalConstraint` |
| 7 | **Com qual recorte curricular?** | qual `ComplianceProfile`/BNCC aplicar e qual escopo de papel curricular — `PlanningFilter` (Seção 6) |
| 8 | **Com qual recorte temporal/espacial/temático?** | janela de tempo, recorte geográfico, camadas 4A — Seção 7 |
| 9 | **Sob quais regras de conformidade?** | adequação etária, sensíveis, LGPD, acessibilidade — herdadas da Compliance |

### 1.3 O que a camada **não** decide

A camada **não decide a verdade dos fatos**. Não arbitra consenso científico, não pondera controvérsias, não rotula evidência e não promove cena a gabarito. Tudo isso pertence ao KC, à política editorial (Etapa 3.1) e à curadoria humana. A Planning organiza **intenção didática**; a verdade factual já está decidida e tipada a montante e é apenas **lida** sob os parâmetros do professor.

### 1.4 O que a camada produz

A camada produz o **`PlanningProfile`** (Seção 5), do qual derivam:

- **Conjunto de seleção de Compliance:** *quais* `ComplianceProfile`, `SchoolYearBand`, `SubjectArea`, `CurricularAlignment`/`BNCCMapping` e classes de `AllowedUseContext` (via `curricularRoleScope`) aplicar — **seleção, nunca redefinição**.
- **Uma ou mais `MomentQuery`** parametrizadas (Etapa 5).
- **Um `PlanningFilter`** que o Content Matching Engine (Etapa 8) usará para cruzar planejamento × Compliance × KC.

---

## 2. Papel do professor, escola e coordenação pedagógica (Tarefa 2)

### 2.1 Agentes e escopo de decisão

A camada distingue **seis figuras**; a **mediação final em sala pertence ao professor** (PE-Ed4; modo professor da Etapa 3.1).

| Agente | O que pode informar | O que lhe é reservado | Observação |
|---|---|---|---|
| **`professorIndividual`** | todos os campos do seu planejamento; objetivo, profundidade, recorte, tolerância a sensíveis dentro dos limites da faixa | a **mediação em sala** e a decisão pedagógica final; o ajuste ao perfil real da turma | mediador adulto responsável (modo professor) |
| **`coordenacaoPedagogica`** | planejamentos-modelo, recortes por etapa/componente, padrões de profundidade | definir **defaults institucionais**, sem sobrepor a mediação em sala | propõe; o professor adapta |
| **`escola`** | contexto escolar, infraestrutura, calendário; seleção de `ComplianceProfile`; restrições de acessibilidade | configurar o **contexto de uso** e a fundação (offline, hardware, LGPD) | configura o ambiente, não o conteúdo factual |
| **`redeDeEnsino`** | recortes regionais, defaults de etapa, políticas de uso (pública/privada) | padronizar **conformidade e recorte** em escala | nunca altera o KC; seleciona perfis |
| **`usoPublico` / `usoPrivado`** | flag institucional que herda requisitos distintos (Seção 12) | — | pública = fundação de offline/acessibilidade/LGPD (D10); privada = mais flexibilidade (D3) |
| **`usoLivreExploratorio`** | apenas faixa e contexto de exploração (sem planejamento curricular) | — | seleciona `SchoolUseMode = free-exploration`; **não passa pelo Matching** (D3) — ver §9 |

### 2.2 Precedência (aditiva e conservadora)

1. **Rede/escola** definem defaults e o **piso de conformidade** (faixa, sensíveis, LGPD, acessibilidade), via seleção de `ComplianceProfile`.
2. **Coordenação** propõe recortes e profundidade-modelo.
3. **Professor** adapta dentro desses limites e media em sala.
4. **Nenhum agente relaxa o piso de conformidade:** `sensitiveContentTolerance`, gating e adequação por faixa só podem ser **mais restritivos** que as `SensitiveContentRule`/`AgeSuitability` da Etapa 6 e a Etapa 3.1 (regra de ouro: na dúvida, sobe-se o cuidado).
5. **Uso livre exploratório** ignora o recorte curricular, mas **não** o filtro de faixa nem o invariante de exibição.

### 2.3 O professor como mediador, não como filtro automático

Os parâmetros informados **parametrizam** a consulta e a seleção; não geram, sozinhos, a aula. A `TeacherMediationRequirement` (Seção 4) é um marcador explícito de que certos conteúdos só são apresentáveis **com mediação humana** — transportado das `SensitiveContentRule`/`AgeSuitability` da Compliance; a camada apenas o registra.

---

## 3. Entradas do planejamento (Tarefa 3)

Matriz de campos de entrada. Cada campo declara **definição**, **exemplo**, **obrigatório/opcional**, **risco se mal usado** e **camada consumidora**. Todos os enums são listas controladas; nenhum campo cria, altera ou reclassifica conhecimento do núcleo. Os `*Ref` apontam para entidades **já definidas na Etapa 6**.

| Campo (`camelCase`) | Definição | Exemplo | Obrig./Opc. | Risco se mal usado | Camada consumidora |
|---|---|---|---|---|---|
| `complianceProfileRef` | seleciona um `ComplianceProfile` (carrega `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef`, `policyRefs[]`) | `prof:efII-publica-AA-offline` | **Obrigatório** | aplicar perfil incompatível com a turma | Compliance → Matching |
| `schoolYearBandRef` | refina a série dentro da etapa (`SchoolYearBand`) | `band:8-9ano` | Recomendado | desalinhar com o ano | Compliance → Matching |
| `subjectAreaRef` | componente/área (`SubjectArea`) | `subj:historia` | **Obrigatório** | recorte fora da disciplina | Compliance → Matching |
| `schoolTerm` | unidade do calendário escolar | `bimestre2` | Opcional | trilha temporalmente incoerente | Matching → Output (E9) |
| `lessonDuration` | tempo disponível (`TimeBudget`) | `50min` | Opcional | densidade incompatível com o tempo | Matching (Seção 10) |
| `theme` | tema declarado pelo professor (texto + tags) | `"Revolução Francesa"` | **Obrigatório** | tema vago gera correspondência ruidosa | Matching (Etapa 8) |
| `teacherObjective` | objetivo pedagógico em linguagem do professor | `"causas e simultaneidade global de 1789"` | Recomendado | objetivo ausente → seleção sem foco | Matching → Output (E9) |
| `learningGoalRefs` | metas via `CurricularAlignment`/`BNCCMapping` (apontam KC↔BNCC, c/ proveniência F1) | `[align:EF08HI06↔evt:revolucao-francesa]` | Opcional | citar código BNCC sem `provenanceRef` | Compliance → Matching |
| `depthLevel` | nível de profundidade (`DepthPreference`, Seção 10) | `standard` | Recomendado | profundidade incompatível com faixa/tempo | Matching (Seção 10) |
| `classReadinessLevel` | prontidão **agregada** da turma (nunca dado individual) | `heterogenea` | Opcional | rotular/perfilar alunos (LGPD Art. 14) | Matching (Seção 10) |
| `localContext` | contexto local da escola/turma (Seção 11) | `"Vitória/ES, escola pública"` | Opcional | recorte local apagar o resto do mundo | Compliance → Matching |
| `regionalFocus` | recorte geográfico de destaque (Seção 11) | `brasil` / `espiritoSanto` | Opcional | eurocentrismo ou apagamento invertido | função (`spatialInput`) |
| `curricularRoleScope` | quais classes de `AllowedUseContext` incluir na seleção | `[curricularCore, contextual, enrichment]` | Opcional | restringir a `curricularCore` e perder a simultaneidade | Compliance/Matching (Seções 6/9) |
| `schoolUseModeRefs` | um ou mais `SchoolUseMode` da Etapa 6 | `[student, projector]` | **Obrigatório** | confundir modo de uso com permissão de conteúdo | Compliance → Experience (E10) |
| `usageScenario` | cenário pedagógico fino que se aninha sob `schoolUseModeRefs` (Seção 9) | `classroomProjection` | Recomendado | escolher cenário incompatível com o recorte | Matching/Experience |
| `preferredSceneMode` | modo de apresentação (mapeia para `outputMode`, Seção 8) | `cenaCompleta` | Opcional | pedir modo incompatível com o recorte | função/Experience (Seção 8) |
| `sensitiveContentTolerance` | tolerância a sensíveis **relativa** às `SensitiveContentRule` (só endurece) | `padraoDaFaixa` | Opcional | relaxar gating além do permitido | Compliance/editorial (Seção 13) |
| `accessibilityNeeds` | necessidades que **disparam** `AccessibilityRequirement` (e-MAG/WCAG/LBI) | `[leituraDeTela, altoContraste]` | Recomendado | excluir alunos; descumprir LBI | Compliance → Experience (E10) |
| `availableResources` | recursos disponíveis (`ResourceConstraint`, Seção 12) | `[projetor, internetInstavel]` | Recomendado | propor experiência inviável | Matching → Experience |
| `offlineModeRequired` | exige funcionamento offline parcial (relaciona-se a `SchoolUseMode=offline`) | `true` | Opcional | depender de internet rápida (D10) | Experience/Pipeline (E13) |
| `assessmentIntent` | **intenção** de avaliação (não a avaliação em si) | `formativaLeve` | Opcional | confundir intenção com rubrica pronta (E9) | Output (Etapa 9) |
| `teacherNotes` | observações livres do professor | `"turma já viu Iluminismo"` | Opcional | nota textual tratada como claim factual | Matching → Output (E9) |

> **Regra transversal de entradas.** Campos textuais (`theme`, `teacherObjective`, `teacherNotes`) **nunca** são tratados como `Claim` factual nem entram no KC. São intenção do professor, usados para ranqueamento e organização, sob rótulo explícito de "intenção do professor".

---

## 4. Entidades conceituais da camada (Tarefa 4)

Entidades **externas ao Knowledge Core e distintas das entidades da Compliance**. Nenhuma é, vira ou recria entidade do núcleo ou da Etapa 6. As entidades de planejamento **referenciam** as de conformidade; não as duplicam.

| Entidade (`CamelCase`) | Papel | Para que aponta | Observação de fronteira |
|---|---|---|---|
| **`PlanningProfile`** | artefato central que consolida o planejamento (Seção 5) | agrega as demais; produz parâmetros p/ Compliance e Matching | é o objeto que a Etapa 8 recebe |
| **`TeacherIntent`** | intenção pedagógica (objetivo, tema, notas) | `theme`, `teacherObjective`, `learningGoalRefs` | intenção, nunca fato |
| **`SchoolContext`** | contexto institucional (público/privado, calendário, infraestrutura) | seleciona `ComplianceProfile` e `SchoolUseMode` (Compliance) | define ambiente, não conteúdo |
| **`ClassContext`** | contexto **agregado** da turma (etapa, ano, prontidão) | `EducationStage`/`SchoolYearBand` (Compliance) | **sem dado pessoal de aluno** (LGPD Art. 14) |
| **`InstructionalGoal`** | meta de aprendizagem estruturada | `CurricularAlignment`/`BNCCMapping`→`BNCCSkill` (Compliance) | meta ≠ gabarito factual |
| **`DepthPreference`** | profundidade e densidade (Seção 10) | parametriza `MomentQuery`/Matching | não altera claims; modula seleção |
| **`TimeBudget`** | orçamento de tempo da aula/trilha | parametriza densidade (Seção 10) | tempo curto reduz densidade, não verdade |
| **`LocalContext`** | recorte local/regional e contexto da escola (Seção 11) | `regionalFocus`/`localContext`; `spatialInput`/`ModernCorrespondence` | destaca, não apaga o mundo (D8) |
| **`ResourceConstraint`** | restrições de recursos/infraestrutura (Seção 12) | requisitos p/ Experience/Pipeline; `SchoolUseMode=projector/offline` | viabilidade técnica real (D10) |
| **`PedagogicalConstraint`** | restrições pedagógicas | **referencia/respeita** `BrazilianEducationConstraint`, `SensitiveContentRule`, `AgeSuitability`, `LegalRequirement` (Compliance) | só endurece o piso; não recria as regras |
| **`PlanningAnnotation`** | anotação **pedagógica** sobre a saída (ordem na trilha, destaque, nota de mediação) | anota `MomentResult`/`Scene` por ID | distinta da `ComplianceAnnotation`; nunca altera o alvo |
| **`PlanningFilter`** | filtros derivados do `PlanningProfile` | consumido pelo Content Matching Engine (E8) | filtra por fora; não muda o índice |
| **`TeacherMediationRequirement`** | marcador de exigência de mediação humana | transporta `SensitiveContentRule.mediation`/`AgeSuitability.mediationRequired` | a camada registra; o professor media |

> **`PlanningAnnotation` × `ComplianceAnnotation`.** A `ComplianceAnnotation` (Etapa 6) anota **conformidade/legalidade** (adequação etária, alinhamento BNCC, mediação obrigatória, base legal). A `PlanningAnnotation` (Etapa 7) anota **organização pedagógica** (ordem na trilha, foco, nota do professor). Ambas são externas, apontam por ID e nunca editam o alvo; vivem em camadas diferentes e não se confundem.

---

## 5. `PlanningProfile` e modelo de anotação (Tarefa 5)

### 5.1 Dicionário conceitual do `PlanningProfile`

Dicionário conceitual — **não é código**. Organiza as entradas (Seção 3) em quinze blocos e produz parâmetros para a Compliance e a Matching. Os `*Ref` apontam para entidades da Etapa 6.

```txt
PlanningProfile = {

  // 1. identidade do planejamento
  planningId,
  authoredBy,                 # professorIndividual | coordenacaoPedagogica | escola | redeDeEnsino
  planningTitle,

  // 2. seleção de conformidade (entidades da Etapa 6 — REFERENCIADAS, nunca criadas)
  complianceProfileRef,       # REF a ComplianceProfile → traz stageRef, region?, accessibilityLevel, ageProfileRef, policyRefs[]
  schoolYearBandRef,          # REF a SchoolYearBand → refina a série dentro da etapa do ComplianceProfile
  subjectAreaRef,             # REF a SubjectArea → componente/área (mapeia para themeTags do KC por correspondência)
  // educationStage e ageLanguageProfile chegam pelo ComplianceProfile; só podem ser sobrepostos para MAIS restrição

  // 3. recorte curricular fino
  curricularRoleScope,        # quais classes de AllowedUseContext incluir: subconjunto de
                              #   {curricularCore, contextual, enrichment, freeExploration}
                              #   (teacherMediated/restricted/hidden são governados pela Compliance, não escolhidos aqui)
  curricularAlignmentRefs,    # REFs a CurricularAlignment / BNCCMapping (KC↔BNCC, com provenanceRef F1) — selecionadas
  learningGoalRefs,           # metas via bnccSkillRef (ex.: EF08HI06) através de CurricularAlignment/BNCCMapping

  // 4. recorte temporal
  timeWindow,                 # janela bruta desejada (ano | faixa | período | Ma/Ga | ano-cenário)
  schoolTerm,                 # unidade do calendário (bimestre/trimestre/unidade), quando houver

  // 5. recorte espacial
  regionalFocus,              # global | continente | país | estado | município | bioma | regiãoHistórica
  modernCorrespondencePref,   # preferência por lente "o que hoje é…" (ModernCorrespondence, D8)

  // 6. recorte temático
  thematicLayers,             # camadas 4A a priorizar/excluir (ciência, política, economia, ambiente, cultura, tecnologia…)
  theme,                      # tema textual do professor (intenção, nunca claim)

  // 7. profundidade (DepthPreference — Seção 10)
  depthLevel,                 # introductory | standard | deepDive | sourceAnalysis | comparative | interdisciplinary
  densityPreference,          # densidade desejada (relacionada a TimeBudget; não altera a verdade)

  // 8. adequação etária (vem da Compliance; só pode endurecer)
  // o AgeLanguageProfile é obtido via ComplianceProfile.ageProfileRef → deriva ageLevelMode da função
  ageSuitabilityOverride,     # APENAS para subir o cuidado (nunca afrouxar AgeSuitability/SensitiveContentRule da Etapa 6)
  classReadinessLevel,        # AGREGADO: homogenea | heterogenea | avançada | emRecuperacao (sem dado pessoal)

  // 9. tolerância a sensíveis (relativa às SensitiveContentRule da Etapa 6)
  sensitiveContentTolerance,  # padraoDaFaixa | maisRestritivo   (NUNCA "mais permissivo")

  // 10. exigência de mediação
  mediationRequirementRefs,   # transporta SensitiveContentRule.mediation / AgeSuitability.mediationRequired

  // 11. acessibilidade (fundação — seleciona/dispara AccessibilityRequirement da Etapa 6)
  accessibilityNeeds,         # leituraDeTela | altoContraste | legendas | linguagemSimples | navegacaoPorTeclado | reducaoDeMovimento | …

  // 12. recursos e infraestrutura (Seção 12)
  availableResources,         # projetor | laboratorioInformatica | celularDoProfessor | internetInstavel | …
  offlineModeRequired,        # true | false → relaciona-se a SchoolUseMode = offline / projector

  // 13. modo e cenário de uso (Seção 9)
  schoolUseModeRefs,          # REFs a SchoolUseMode (Etapa 6): subconjunto de {teacher, student, free-exploration, projector, offline}
  usageScenario,              # cenário pedagógico fino (10 valores — Seção 9) que se aninha sob schoolUseModeRefs
  preferredSceneMode,         # mapeia para outputMode da função (Seção 8)

  // 14. observações e intenção
  teacherNotes,               # texto livre (intenção/contexto; nunca claim factual)
  assessmentIntent,           # intenção de avaliação (NÃO a avaliação pronta — Etapa 9)

  // 15. status de revisão do planejamento
  planningReviewStatus        # rascunho | revisadoPelaCoordenacao | prontoParaUso
}
```

> **Três eixos de maturidade independentes.** `planningReviewStatus` governa o **planejamento** (artefato do professor); **não** se confunde com o `reviewStatus` do KC/Compliance (publicação de conteúdo) nem com `sceneCompletenessLevel`/`publicabilityStatus` da `Scene`. A camada de planejamento só escreve no primeiro.

### 5.2 Modelo de anotação (`PlanningAnnotation`)

```txt
PlanningAnnotation = {
  annotationId,
  planningId,                 # a qual PlanningProfile pertence
  targetRef,                  # knowledgeItemId | claimId | sceneId — o alvo no KC/saída (apontado, não copiado)
  annotationType,             # destaque | nota-de-mediação | recorte-de-foco | ordem-na-trilha | rótulo-de-relevância
  annotationPayload,          # conteúdo da anotação (texto do professor / parâmetro de organização)
  visibilityScope,            # quem vê: professor | turma | coordenação
  doesNotAlterTarget          # invariante FIXO = true (a anotação jamais modifica claim/fonte/cena nem a anotação de conformidade)
}
```

A anotação é **externa e descartável**: removê-la não deixa rastro no KC nem na Compliance. Organiza a leitura (ordem na trilha, destaque, nota de mediação), nunca a verdade nem a conformidade.

### 5.3 Produção de parâmetros

A partir do `PlanningProfile`, a camada deriva:

- **Conjunto de seleção de Compliance** — `complianceProfileRef` (primário) + `schoolYearBandRef`/`subjectAreaRef`/`curricularAlignmentRefs`/`learningGoalRefs` + `curricularRoleScope` — dizendo à Etapa 6 *quais perfis e classes aplicar*.
- **Uma ou mais `MomentQuery`** — de `timeWindow`, `regionalFocus`, `thematicLayers`, `depthLevel`, `ageLevelMode` (derivado de `ComplianceProfile.ageProfileRef`), `publicabilityMode` (derivado de `usageScenario`/`schoolUseModeRefs`) e `preferredSceneMode`→`outputMode` (Seção 7).
- **Um `PlanningFilter`** — empacotamento dos filtros (incl. `curricularRoleScope` e refs de Compliance) para o Content Matching Engine cruzar planejamento × Compliance × KC (Etapa 8).

---

## 6. Relação com a `BrazilianEducationComplianceLayer` (Tarefa 6)

### 6.1 Princípio: a Planning **seleciona**, a Compliance **define**

A `TeacherSchoolPlanningLayer` **consome** os perfis, anotações e entidades da Etapa 6; **não os cria nem os redefine**. O professor não inventa faixa etária, contexto de uso, requisito de acessibilidade nem regra de sensível: ele **escolhe quais perfis/classes já definidos se aplicam**. A definição é soberania da Compliance e da política editorial (Etapa 3.1).

### 6.2 O que a Planning consome de cada entidade da Compliance

| Entidade da Compliance (Etapa 6) | Forma (campos reais) | Como a Planning a consome | O que a Planning **não** faz |
|---|---|---|---|
| **`ComplianceProfile`** | `profileId`, `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef`, `policyRefs[]` | seleção **primária** via `complianceProfileRef`; traz etapa/região/acessibilidade/perfil etário | não edita o perfil nem cria exceções permissivas |
| **`EducationStage`** | `stageId`, `label`, `ageRangeApprox`, `legalBasisRef` | recebido via `ComplianceProfile.stageRef` | não cria etapa; não usa etapa como trava da exploração livre |
| **`SchoolYearBand`** | `bandId`, `stageRef`, `yearsCovered`, `ageRangeApprox` | refina a série via `schoolYearBandRef` | não redefine a faixa de anos |
| **`SubjectArea`** | `subjectId`, `label`, `bnccAreaRef?` | seleção via `subjectAreaRef` | não força a disciplina como recorte único (o KC é interdisciplinar) |
| **`AgeLanguageProfile`** | `profileId`, `bandRef`, `language`, `depth`, `abstraction`, `mediaExposure`, `mediationRules`, `editorialPolicyRef` | obtido via `ComplianceProfile.ageProfileRef`; daí deriva o `ageLevelMode` | não redefine os 5 níveis de exposição (3.1 §6) |
| **`AllowedUseContext`** | `contextId`, `targetRef`, `contextClass` (7 classes) | **escolhe o escopo** (`curricularRoleScope`) de quais classes incluir | não define a classe **por item** (isso é da Compliance/Matching) |
| **`SchoolUseMode`** | `modeId`, `mode` ∈ {teacher, student, free-exploration, projector, offline} | seleciona via `schoolUseModeRefs`; `usageScenario` se aninha sob ela | não cria modo novo; não mistura modo com permissão de conteúdo |
| **`CurricularAlignment`** | `alignmentId`, `targetRef`, `bnccSkillRef`/`bnccCompetencyRef`, `rationale`, `provenanceRef`, `reviewStatus` | referencia alinhamentos existentes via `curricularAlignmentRefs` | **não cria alinhamento**; não promete homologação/PNLD |
| **`BNCCMapping`** | `mappingId`, `skillCodeRef`, `knowledgeItemRefs[]`, `claimRefs[]?`, `sceneRefs[]?`, `mappingRationale`, `provenanceRef`, `reviewStatus` | referencia mapeamentos existentes (apontam ao KC) | **não mapeia BNCC em massa**; não referencia mapeamento sem `provenanceRef` (F1) |
| **`AgeSuitability`** | `suitabilityId`, `targetRef`, `bandRef`, `exposureLevel`, `mediationRequired`, `hiddenInBands[]` | **respeita** por item; pode subir o cuidado via `ageSuitabilityOverride` | não rebaixa a exigência; não altera o fato |
| **`SensitiveContentRule`** | `ruleId`, `topic`, `targetRef`, `mediation`, `defaultHidden`, `reviewRolesRequired[]`, `legalBasisRef?` | `sensitiveContentTolerance` opera **relativo** a ela (só endurece) | não relaxa mediação/ocultação; não apaga (media) |
| **`AccessibilityRequirement`** | `requirementId`, `targetRef?`, `wcagRef?`, `emagRef?`, `description` | `accessibilityNeeds` **dispara/seleciona** requisitos | não cria UX; não trata como enfeite (e-MAG/WCAG/LBI são fundação) |
| **`LegalRequirement`** | `requirementId`, `targetRef?`, `legalBasisRef`, `obligation`, `reviewStatus` | **respeita** (LGPD Art. 14, LBI Art. 63, Marco Civil) | não inventa obrigação; não coleta dado de aluno |
| **`BrazilianEducationConstraint`** | `constraintId`, `scope`, `description`, `policyRef` | **respeita** (ex.: cobertura afro/indígena estrutural na área de História) | não viola a cobertura obrigatória; não a trata como opcional |
| **`ComplianceAnnotation`** | `annotationId`, `targetRef`, `annotationType`, `payload`, `legalBasisRef?`, `reviewStatus` | **lê** anotações de conformidade sobre a saída | não as edita; usa `PlanningAnnotation` própria para organização |

### 6.3 Distinções herdadas que a Planning deve preservar

1. **Alinhamento BNCC ≠ homologação MEC ≠ aprovação PNLD** (Etapa 6 §4.3). O `curricularAlignmentRefs` indexa; **não** declara homologação. Nenhum campo/rótulo do planejamento pode sugerir homologação/PNLD (Seção 13, R-10).
2. **Conteúdo fora da grade permanece acessível.** O recorte define **foco**, não **limite** (D3). `curricularRoleScope` deve, por padrão, incluir `contextual`/`enrichment`/`freeExploration` para preservar a simultaneidade global; conteúdo fora da grade aparece como contexto/exploração/aprofundamento, nunca apagado.
3. **A adequação por faixa modula forma, nunca fato** (PE-Ed8; Etapa 6 §7). Selecionar/herdar `AgeLanguageProfile` muda profundidade, linguagem e mídia; **jamais** altera o `Claim`.

### 6.4 Direção de dependência reafirmada

```
PlanningProfile → (seleciona) → ComplianceProfile/SchoolYearBand/SubjectArea/AllowedUseContext/SchoolUseMode/
                                 CurricularAlignment/BNCCMapping/AgeSuitability/SensitiveContentRule/AccessibilityRequirement
              → (apontam por ID) → Knowledge Core
```

A Compliance **não conhece** o `PlanningProfile`; o KC **não conhece** nenhum dos dois. A seta é sempre de fora para dentro.

---

## 7. Relação com `WhatWasHappeningAtMoment` (Tarefa 7)

### 7.1 O planejamento **parametriza**, não altera a função

A camada gera uma ou mais **`MomentQuery`** a partir do `PlanningProfile`. **Não modifica** a função, seus 13 tipos de consulta, sua normalização, seu gating ou seus invariantes. Mapeamento conceitual:

| Campo do `PlanningProfile` | Campo da `MomentQuery` (Etapa 5) |
|---|---|
| `theme` + `subjectAreaRef` | `queryText` + inferência de `queryMode` |
| `timeWindow` / `schoolTerm` | `timeInput` (bruto, preservado) |
| `regionalFocus` / `modernCorrespondencePref` | `spatialInput` (incl. lente "o que hoje é…") |
| `thematicLayers` | `layerFilters` (camadas 4A a incluir/excluir) |
| `depthLevel` / `densityPreference` | influencia seleção/ranqueamento (não cria campo novo) |
| `ComplianceProfile.ageProfileRef` (`AgeLanguageProfile`) | `ageLevelMode` (modula profundidade/linguagem/mídia) |
| `usageScenario` / `schoolUseModeRefs` | `publicabilityMode` (`público` em sala/estudante; `interno-curadoria` em preparação) |
| `preferredSceneMode` | `outputMode` (um dos 10 modos — Seção 8) |
| (debate/evidência desejados) | `includeUncertainty`/`includeSources` conforme objetivo |

> `curricularRoleScope` **não** é campo da `MomentQuery` — a função não conhece papel curricular. Ele é aplicado **depois**, pelo `PlanningFilter`/Matching/Compliance sobre o `MomentResult` (classes `AllowedUseContext`). A função entrega o mundo; a Compliance/Matching rotula o que é `curricularCore`/`contextual`/`enrichment`.

### 7.2 Exemplos conceituais (alinhados aos exemplos da Etapa 6 §11)

**Ex. 1 — História, 8º/9º ano (12–14), Revolução Francesa com simultaneidade global.**
`subjectAreaRef = historia`; `queryText = "Revolução Francesa"`; `queryMode` inferido = período/simultaneidade; `timeInput = 1789`; `spatialInput = global` com `regionalFocus = europa` em destaque e lente Brasil ligada; `layerFilters = {política, economia, ciência, cultura}`; `ageLevelMode = 12–14`; `curricularRoleScope = [curricularCore, contextual, enrichment]`; `outputMode = cenaCompleta`. Resultado (Etapa 6 §11, Ex.1): França/1789 como `curricularCore`; Inconfidência Mineira, EUA, Lavoisier como `contextual`; escravidão/colonização `teacherMediated`; mídia gráfica oculta < 15; `anachronismWarnings` ("Brasil = colônia, via `ModernCorrespondence`").

**Ex. 2 — Ciências, Ensino Médio (15–17), GOE em linguagem adequada.**
`queryText = "Grande Oxidação"`; `queryMode = tempo profundo sem evento`; `timeInput ≈ 2,4 Ga`; `includeUncertainty = true`. A função entrega `AtmosphereState`/`OceanographicState` em destaque, paleogeografia **rotulada** como reconstrução modelada (não "foto"), confiança que decai com a idade — a Planning só pediu profundidade e faixa.

**Ex. 3 — Geografia/Ciências, Ensino Médio, clima moderno com fato × cenário × previsão.**
`queryText = "mudança climática"`; combina séries recentes (medição) com tipo 13 (projetivo, `sourceTimeBasis = scenarioYear`). A função separa **fato físico**, **cenário** (modelo) e **previsão** (faixa, não número cravado); `equivalenceWarnings` mantêm negacionismo fora do `ClaimSet`. A Planning pede a separação (P28) e a faixa; não decide o cenário.

**Ex. 4 — Recorte Brasil/ES ou local.**
`regionalFocus = espiritoSanto`; `localContext = "Vitória/ES, escola pública"`; `modernCorrespondencePref = true`; `outputMode = listaPorRegiao`. Destaca o ES **sem apagar** o restante do mundo no mesmo tempo (Seção 11; Etapa 6 §11.2).

**Ex. 5 — Exploração livre mediada (consulta de aluno sobre tema sensível).**
`schoolUseModeRefs = [free-exploration]`; `usageScenario = freeExplorationWithAgeGate`; `ageLevelMode = 9–11`. **Sem recorte curricular** (D3): vai do KC à experiência sob filtro de faixa e invariante de exibição. Aparece o **fato** em linguagem adequada, com agência/resistência e simultaneidade; sensível `teacherMediated`/`restricted` conforme a faixa; `pending`/`legal-review` (pessoas vivas) não aparece (Etapa 6 §11, Ex.5).

### 7.3 Invariantes preservados

Em todos os casos, a `MomentQuery` respeita os limites da função (Etapa 5 §13): não inventa dados, não exibe `pending` como fato, não trata IA como fonte, não cria falsa equivalência e não promove cena a gabarito. A Planning **não pode** afrouxar nenhum desses limites.

---

## 8. Relação com `Scene` v1.1 e `MomentResult` (Tarefa 8)

### 8.1 O planejamento **solicita modos**, não cria cena

Via `preferredSceneMode`, mapeando para o `outputMode` da função (Etapa 5 §12). A camada **não cria `Scene` nova**, **não duplica** itens e **não promove** cena a `gabarito-interno` (decisão de curadoria — 4H §9).

| `preferredSceneMode` (Planning) | `outputMode` (função) | Quando o professor escolhe |
|---|---|---|
| `cenaCompleta` | Cena completa (`generatedSceneCandidate`, 34 campos) | recorte coeso para exploração em sala |
| `cenaResumida` | Resumo rápido | abertura/encerramento curto de aula |
| `dossie` | Dossiê | aprofundamento de um foco com "como sabemos" |
| `comparacaoAntesDepois` | Comparação antes/depois | mostrar transição em torno de um evento |
| `listaPorCamada` | Lista por camada | recorte temático (ciência, política…) |
| `listaPorRegiao` | Lista por região | comparar geografias no mesmo tempo |
| `linhaDoTempo` | Linha do tempo | navegação temporal de uma trilha |
| `globoMapa` | Globo/mapa | navegação espacial |
| `relatorioInternoCuradoria` | Relatório interno de curadoria | **só** preparação do professor; nunca exibido ao aluno como fato |

### 8.2 Limites sobre a `Scene`

1. A camada **lê** `Scene` v1.1 (incl. `sceneCompletenessLevel`, `publicabilityStatus`, `gatingReason`) para decidir o que é apresentável; **não escreve** nesses campos.
2. Cena com `publicabilityStatus = 5 (bloqueada)` ou com itens `pending`/`legal-review` **não** é apresentada ao aluno — o planejamento não força exibição (invariante absoluto, 1.1/3.1; Etapa 6 §11.1d).
3. O `relatorioInternoCuradoria` só é acessível em `SchoolUseMode = teacher` (modo professor); seu conteúdo `pending`/de risco **nunca** vaza para o aluno como fato.
4. O `gatingReason` da cena, quando exige mediação, é transportado pela `TeacherMediationRequirement`; a camada o registra, o professor o medeia.

### 8.3 Consumo do `MomentResult`

A camada consome os campos do `MomentResult` (Etapa 5 §4) apenas para **organizar e anotar**: usa `mainItems`/`simultaneousItems` para montar a ordem da trilha; respeita `publicabilityStatus`/`gatingReason`/`hiddenItems`; e preserva `anachronismWarnings`/`equivalenceWarnings` como avisos a repassar. Tudo via `PlanningAnnotation` externa (Seção 5.2), sem alterar o resultado nem as `ComplianceAnnotation`.

---

## 9. Modos e cenários de uso escolar (Tarefa 9)

### 9.1 Dois níveis: `SchoolUseMode` (Compliance) e `usageScenario` (Planning)

A Etapa 6 já define **`SchoolUseMode`** com cinco valores — `teacher`, `student`, `free-exploration`, `projector`, `offline`. A camada de planejamento **não redefine** esses modos; ela introduz **`usageScenario`**, cenários pedagógicos finos que **se aninham** sob um ou mais `schoolUseModeRefs`. Cada cenário declara objetivo, restrições, relação com sensíveis, necessidade de mediação e o(s) `SchoolUseMode` que seleciona.

| `usageScenario` (Planning) | Aninha sob `SchoolUseMode` | `publicabilityMode` | Objetivo | Relação com sensíveis | Mediação |
|---|---|---|---|---|---|
| **`teacherPreparation`** | `teacher` | interno-curadoria → público | preparar a aula com aparato completo | acesso ao aparato (sensível p/ preparação, sob licença) | n/a (é quem media) |
| **`classroomProjection`** | `projector` (+ `teacher`) | público | projetar para a turma | sensível conforme faixa; gráfico oculto por padrão | **alta** |
| **`guidedStudentExploration`** | `student` | público | exploração guiada pelo professor | mediação obrigatória onde a 3.1/6 exige | **alta** |
| **`freeExplorationWithAgeGate`** | `free-exploration` | público | exploração livre do aluno | **sem recorte curricular** (D3); gating por faixa | **média** |
| **`homeworkSupport`** | `student` (eventual `offline`) | público | apoio a tarefa de casa | conservador; sensível restrito sem professor | **baixa→média** (sobe-se o cuidado) |
| **`assessmentPreparation`** | `teacher` | interno-curadoria → público | preparar avaliação (intenção) | conforme faixa | **média** |
| **`interdisciplinaryProject`** | `student`/`teacher` | público | projeto entre componentes | conforme o tema mais sensível | **alta** |
| **`remedialReview`** | `student` | público | revisão/recuperação | conservador | **alta** |
| **`enrichment`** | `student`/`free-exploration` | público | aprofundamento/enriquecimento | pluralidade conforme faixa (12+/15+) | **média** |
| **`localHistoryConnection`** | `student`/`teacher` | público | conectar com história local (Seção 11) | sensíveis locais sob Leis 10.639/11.645 | **alta** |

> **Modos de entrega.** `projector` e `offline` são `SchoolUseMode` de **entrega** (D10) que se combinam com `teacher`/`student`/`free-exploration` — por isso `schoolUseModeRefs` é uma **lista** (ex.: `[student, projector, offline]`). `availableResources`/`offlineModeRequired` (Seção 12) reforçam essa seleção.

> **Regra de fundação.** Quanto **menor** a presença do professor (`homeworkSupport`, `freeExplorationWithAgeGate`), **maior** o nível de cuidado padrão (mais ocultação, mais aviso) — coerente com PE-Ed4.

---

## 10. Profundidade, tempo disponível e nível da turma (Tarefa 10)

### 10.1 Profundidade que modula seleção, nunca o fato

`depthLevel` **modula seleção e densidade** — quantos itens, quanto aparato, qual grau de controvérsia — **sem alterar o `Claim`** (PE-Ed8). Um fato documentado permanece fato em `introductory` e em `sourceAnalysis`; muda quanto dele se mostra e com qual aparato.

| `depthLevel` | O que prioriza | Densidade típica | Aparato de fontes/controvérsia |
|---|---|---|---|
| **`introductory`** | noções concretas, narrativa simples | baixa | mínimo; `ClaimSet` ausente ou muito simplificado |
| **`standard`** | causas e consequências simples; primeira simultaneidade | média | termos sensíveis explicados; `ClaimSet` simplificado |
| **`deepDive`** | processos e interpretações | média-alta | `ClaimSet` presente; relações `causou`/`possibilitou` |
| **`sourceAnalysis`** | "como sabemos disso" (evidência/proxy) | alta no aparato | `sourceSummary`/evidências em destaque |
| **`comparative`** | comparação (antes/depois; A×B) | conforme par | `comparisonMode` ativo; sem falsa simetria |
| **`interdisciplinary`** | conexões entre camadas 4A/componentes | alta em amplitude | conexões intercamada sinalizadas |

> A profundidade é coerente com a coluna "Profundidade/abstração" do mapeamento etário da Etapa 6 §7.1: ela **opera dentro** do que a faixa permite, jamais ultrapassando o teto de exposição da `AgeLanguageProfile`.

### 10.2 Tempo disponível afeta densidade, não verdade

`lessonDuration`/`TimeBudget` afetam **quanto** se seleciona e com **qual densidade**, nunca a verdade nem a profundidade epistêmica de cada item exibido:

- **Tempo curto (ex.: 50 min)** → menos itens-âncora, `outputMode` enxuto, foco em `mainItems`; sem comprimir a verdade ou suprimir incerteza relevante.
- **Tempo amplo (trilha)** → mais simultâneos contextuais, dossiês, comparações.
- A redução por tempo é **redução de cobertura**, jamais de honestidade: corta-se contexto, não rótulo.

### 10.3 Nível da turma é agregado, nunca individual

`classReadinessLevel` descreve a turma de forma **agregada** (`homogenea`/`heterogenea`/`avançada`/`emRecuperacao`) e calibra densidade/profundidade. **Não é dado pessoal de aluno** e **não pode** perfilar indivíduos (LGPD Art. 14 §4 — minimização; Etapa 6 §5; Seção 13, R-3). Turma heterogênea sugere camadas de profundidade coexistindo (base `standard` com aprofundamentos opcionais), não rotulagem de alunos.

---

## 11. Recorte local, regional e lente Brasil (Tarefa 11)

### 11.1 Granularidade do recorte

A escola/professor informa recorte em vários níveis, todos referenciando `Place`/`Region`/`ModernCorrespondence` do KC por ID (nunca criando geografia):

| Nível | Campo/valor | Mecanismo no KC |
|---|---|---|
| **País** | `regionalFocus = brasil` | `Region` + `modernGeometry` |
| **Estado** | `regionalFocus = espiritoSanto` | `Region` (recorte administrativo atual, via IBGE) |
| **Município** | `localContext = "Vitória/ES"` | `Place`/`Region` atual |
| **Bioma** | `regionalFocus = mataAtlantica` | `BiomeState`/`Region` ecológica |
| **Região histórica** | `regionalFocus = capitaniaDoEspiritoSanto` | `historicalGeometryVersions` (datada) |
| **Território atual** | (qualquer) | `ModernCorrespondence` — a lente "o que hoje é…" (D8) |
| **Correspondência moderna** | `modernCorrespondencePref = true` | `ModernCorrespondence` rotulada (evita anacronismo) |
| **Contexto da escola** | `localContext` (texto + tags) | intenção do professor; não é geografia do KC |

### 11.2 Destaque, não apagamento (simultaneidade global preservada)

O recorte local **destaca e organiza**; **não apaga o resto do mundo** (D3/D8; Etapa 6 §9/§11.2). A grade e o recorte definem **foco**, não **universo**. Recorte local vira `spatialInput` com destaque, mas `outputMode = listaPorRegiao`/`globoMapa` **mantém o mundo navegável no mesmo tempo**, e `curricularRoleScope` deve incluir `contextual`/`enrichment`/`freeExploration` para o que coexistia em outras regiões permanecer a um clique.

### 11.3 Lente Brasil e antieurocentrismo

A **lente Brasil** (D8) garante a pergunta "e no território que hoje é o Brasil?", **incluindo a história profunda indígena** (povoamento, sambaquis, marajoara), sob as **Leis 10.639/2003 e 11.645/2008** (Etapa 6 §8). O recorte local **não pode**:

- apagar África e povos indígenas (centralidade e protagonismo, não nota de rodapé — `BrazilianEducationConstraint` marca a cobertura como estrutural);
- reintroduzir eurocentrismo (marco eurocêntrico único como "início da história");
- inverter o erro, apagando o restante do mundo ao hipervalorizar o local.

A camada **não decide** essa cobertura — ela é garantida pelo KC, pela política editorial e pelas `BrazilianEducationConstraint`/`SensitiveContentRule` da Compliance; a Planning apenas **não pode** parametrizar um recorte que as viole.

---

## 12. Restrições escolares, acessibilidade e infraestrutura (Tarefa 12)

### 12.1 Acessibilidade e LGPD como fundação

Coerente com D10 e com a Compliance (Etapa 6 §5/§6), **acessibilidade (e-MAG/WCAG/LBI) e LGPD/proteção de menores não são opções**: são requisitos de fundação. A camada trabalha com turma **agregada**, sem dado pessoal de aluno, e dispara `AccessibilityRequirement` para a Experience (E10). `accessibilityNeeds` **seleciona** requisitos já definidos pela Compliance; não os inventa.

### 12.2 Modelagem de restrições

```txt
ResourceConstraint = {
  connectivity,        # internetAdequada | internetInstavel | semInternet
  displayDevice,       # projetor | laboratorioInformatica | celularDoProfessor | tvSmart | nenhum
  offlineModeRequired, # true | false (pacotes offline — D10) → SchoolUseMode = offline
  hardwareTier,        # modesto | medio | avancado (degradação 3D→2D→estático)
  classSize            # faixa de tamanho da turma (agregado; uso coletivo frequente em escola pública)
}

PedagogicalConstraint = {
  classHeterogeneity,        # homogenea | heterogenea (relaciona-se a classReadinessLevel)
  timePressure,              # tempoCurto | tempoAmplo
  accessibilityNeeds,        # dispara AccessibilityRequirement (Etapa 6 §6.2)
  institutionalType,         # escolaPublica | escolaPrivada
  mediationRequirementRefs,  # respeita SensitiveContentRule/AgeSuitability (Etapa 6)
  educationConstraintRefs    # respeita BrazilianEducationConstraint (ex.: cobertura afro/indígena estrutural)
}
```

### 12.3 Tabela de restrições típicas e implicações

| Restrição declarada | Implicação | `SchoolUseMode`/entidade | Etapa que resolve |
|---|---|---|---|
| **Internet instável** | preferir pacotes offline; degradar 3D→2D→cartões | `offline` | Experience (E10)/Pipeline (E13) |
| **Projetor apenas** | uma tela conduzida pelo professor | `projector` (+`teacher`) | Experience (E10) |
| **Celular do professor** | layout mínimo; baixa densidade visual | `projector`/`teacher` | Experience (E10) |
| **Laboratório de informática** | exploração guiada por aluno viável | `student` | Experience (E10) |
| **Necessidades de acessibilidade** | requisito e-MAG/WCAG/LBI; rótulos não-cromáticos (3.1 §8.3) | `AccessibilityRequirement` | Compliance/Experience |
| **Modo offline** | conteúdo pré-empacotado; sem rede em tempo real | `offline` | Pipeline (E13) |
| **Tempo curto** | `outputMode` enxuto; foco em `mainItems` (Seção 10.2) | — | Matching (E8) |
| **Turma heterogênea** | camadas de profundidade coexistindo (Seção 10.3) | — | Matching (E8) |
| **Escola pública** | fundação: offline/acessibilidade/LGPD/hardware modesto; uso coletivo | `ComplianceProfile` (região pública) | transversal |
| **Escola privada** | mais flexibilidade; BNCC como base mínima, não limite máximo | `ComplianceProfile` (privada) | transversal |

> A camada **declara** e **repassa**; não implementa nada técnico (sem UX, stack, MVP, pipeline). A resolução real cabe às Etapas 10–13.

---

## 13. Riscos educacionais, jurídicos e operacionais (Tarefa 13)

| # | Risco | Mitigação |
|---|---|---|
| **R-1** | **Recurso usado como currículo substituto** | reafirmar D1 (Etapa 6 §4.2): recurso **complementar**, nunca substituto; o recorte define foco, não substitui a grade |
| **R-2** | **Planejamento virar output pedagógico final** | fronteira rígida com a Etapa 9: a Etapa 7 só define **estrutura de intenção**; `assessmentIntent` ≠ avaliação |
| **R-3** | **Coleta indevida de dados de alunos** | LGPD Art. 14 como fundação (Etapa 6 §5); turma **agregada**; sem analytics de aprendizagem nesta camada |
| **R-4** | **Exposição inadequada de conteúdo sensível** | invariante de exibição + `SensitiveContentRule` + `AgeSuitability` + mediação por faixa (3.1/6); `sensitiveContentTolerance` só endurece |
| **R-5** | **Falsa equivalência** | herdar `weightedClaimSets`/`equivalenceWarnings`; negacionismo `rotulado-rejeitado` fora do `ClaimSet`; a camada não pode reponderar |
| **R-6** | **Apagamento de África / povos indígenas** | Leis 10.639/11.645 como cobertura estrutural via `BrazilianEducationConstraint` (Etapa 6 §8.3); recorte local não pode apagar (Seção 11) |
| **R-7** | **Eurocentrismo** | simultaneidade global preservada (D8); marco eurocêntrico único bloqueado; lente Brasil sempre disponível |
| **R-8** | **Excesso de conteúdo** | `depthLevel` + `TimeBudget` controlam densidade (Seção 10); foco em `mainItems` sob tempo curto |
| **R-9** | **Desalinhamento BNCC** | `curricularAlignmentRefs`/`learningGoalRefs` apontam a `CurricularAlignment`/`BNCCMapping` **com `provenanceRef` (F1)**; sem fonte, não referencia; não mapear em massa |
| **R-10** | **Promessa indevida de homologação MEC/PNLD** | declarar: alinhamento ≠ homologação ≠ PNLD (Etapa 6 §4.3/§4.5); nenhum campo/rótulo sugere homologação |
| **R-11** | **Baixa acessibilidade** | e-MAG/WCAG/LBI como fundação; `accessibilityNeeds` dispara `AccessibilityRequirement` (Etapa 6 §6) |
| **R-12** | **Dependência de internet rápida** | `offlineModeRequired` + `SchoolUseMode=offline/projector` + degradação progressiva (D10) |
| **R-13** | **Uso de IA sem controle** | IA jamais é fonte factual (A3/Q5; 1.1; Etapa 6 §5.3); a camada não invoca IA para criar fato; adaptação de linguagem opera sobre conteúdo curado, rotulada |
| **R-14** | **Confusão entre fato, interpretação, cenário e previsão** | herdar `claimType` (D7) e a separação fato × cenário × previsão (P28; Etapa 6 §11, Ex.4) |
| **R-15** | **~~Divergência de contrato com a Etapa 6~~ — RESOLVIDO** | a Etapa 6 v1.0 foi lida na íntegra; todas as entidades referenciadas foram reconciliadas nesta v1.1. **Residual:** `BNCCMapping`/`CurricularAlignment` permanecem `pending` até confirmação curatorial com o texto homologado (regra da Etapa 6 §3.2/§13) — a Planning os **referencia**, não os resolve |

---

## 14. Fronteiras com as Etapas 8–14 (Tarefa 14)

| Etapa | Papel | Onde a Etapa 7 termina |
|---|---|---|
| **Etapa 8 — Content Matching Engine** | **cruza** `PlanningProfile`/`PlanningFilter` + Compliance + KC para **selecionar** conteúdos, cenas, claims, momentos e recursos | a Etapa 7 entrega a gramática de intenção; **não** cruza nem ranqueia |
| **Etapa 9 — Pedagogical Output Layer** | **transforma** a seleção em plano de aula, roteiro, trilha, atividade, quiz, avaliação, rubrica, guia e material | a Etapa 7 declara `assessmentIntent`/objetivo; **não** gera esses artefatos |
| **Etapa 10 — Design/UX 3D** | modos professor/estudante/exploração livre, telas, timeline, globo, popups; implementação concreta de acessibilidade | a Etapa 7 declara `preferredSceneMode`/`accessibilityNeeds`; **não** desenha interface |
| **Etapa 11 — Arquitetura técnica** | stack, banco, API, isolamento físico de licenças, engenharia de privacidade (LGPD/menores) | a Etapa 7 é conceitual; **não** define stack nem persistência |
| **Etapa 12 — MVP** | recorte mínimo viável | a Etapa 7 não propõe MVP |
| **Etapa 13 — Pipeline de ingestão** | ingestão real, pacotes offline, licença asset-level | a Etapa 7 só **declara** `offlineModeRequired`/restrições; não implementa |
| **Etapa 14 — Validação escolar, jurídica e comercial** | validação com escolas, revisão jurídica, modelo comercial, decisão sobre PNLD | a Etapa 7 não promete adoção, homologação nem valida juridicamente |

---

## 15. Próximos passos e handoff para a Etapa 8 (Tarefa 15)

### 15.1 O que esta etapa entrega

A Etapa 7 (v1.1) entrega a **gramática de intenção pedagógica** do professor/escola, **reconciliada com a Etapa 6 v1.0**: a `TeacherSchoolPlanningLayer` como camada externa; os papéis dos agentes; a matriz de entradas; treze entidades conceituais distintas das da Compliance; o `PlanningProfile` (quinze blocos) que **seleciona** `ComplianceProfile`/`SchoolUseMode`/`AllowedUseContext` e referencia `CurricularAlignment`/`BNCCMapping`; o modelo de `PlanningAnnotation` externa; a **parametrização** (não alteração) da função; a **solicitação de modos** de `Scene` v1.1/`MomentResult`; os dois níveis de uso (`SchoolUseMode` × `usageScenario`); a modulação de profundidade/tempo/nível-da-turma agregado; o recorte local sob simultaneidade global e Leis 10.639/11.645; as restrições de acessibilidade/infraestrutura como fundação; quinze riscos com mitigação; e as fronteiras com as Etapas 8–14.

### 15.2 O que a Etapa 8 deverá fazer

A **Etapa 8 — Content Matching Engine** deverá **receber** o `PlanningProfile`/`PlanningFilter` e **cruzá-lo** com o Knowledge Core e a `BrazilianEducationComplianceLayer` para **selecionar** conteúdos, cenas, claims, momentos e recursos — considerando aderência temática, etapa, componente, profundidade, confiabilidade, disponibilidade visual, fontes, BNCC (via `BNCCMapping`/`CurricularAlignment`), recorte regional, escopo de papel curricular (`curricularRoleScope` sobre as classes `AllowedUseContext`), eventos simultâneos e conceitos relacionados. O motor é, para o núcleo, **apenas mais um leitor dos índices** (Etapa 2 §10).

### 15.3 O que a Etapa 8 ainda **não** deverá fazer

Não criar plano de aula, roteiro, atividade, quiz, rubrica ou material do aluno (isso é da **Etapa 9**). Também não desenha UX, não define stack, não propõe MVP, não faz ingestão, não povoa o KC e não altera claims.

### 15.4 Estado da reconciliação

A pendência R-15 do rascunho v1.0 está **resolvida**: o documento da Etapa 6 foi lido integralmente e as entidades (`ComplianceProfile`, `EducationStage`, `SchoolYearBand`, `SubjectArea`, `AgeLanguageProfile`, `AllowedUseContext`, `SchoolUseMode`, `CurricularAlignment`, `BNCCMapping`, `AgeSuitability`, `SensitiveContentRule`, `AccessibilityRequirement`, `LegalRequirement`, `BrazilianEducationConstraint`, `ComplianceAnnotation`, `BNCCSkill`/`BNCCCompetency`/`BNCCKnowledgeObject`) foram referenciadas pelas suas formas reais. O único resíduo é curatorial e pertence à Etapa 6: os `BNCCMapping`/`CurricularAlignment` concretos nascem `pending` até confirmação com o texto homologado (F1) — a Etapa 7 e a Etapa 8 os **referenciam e respeitam o `reviewStatus`**, sem resolvê-los.

---

## Encerramento e handoff

Esta etapa (v1.1) entrega a **arquitetura conceitual da Teacher/School Planning Layer**, reconciliada com a `BrazilianEducationComplianceLayer` (Etapa 6 v1.0): a definição da camada como tradutora de intenção pedagógica em parâmetros estruturados de consulta e filtragem; os papéis de professor, coordenação, escola, rede e uso livre, com mediação final reservada ao professor; a matriz de entradas; as treze entidades conceituais externas e distintas das de conformidade; o `PlanningProfile` (quinze blocos) que **seleciona** `ComplianceProfile`/`SchoolUseMode`/`AllowedUseContext` e referencia `CurricularAlignment`/`BNCCMapping` pelas suas formas reais; o modelo de `PlanningAnnotation` externa e descartável, distinta da `ComplianceAnnotation`; a relação de **seleção** com a Compliance (preservando alinhamento ≠ homologação ≠ PNLD, conteúdo fora da grade via `curricularRoleScope`, e adequação por faixa que modula forma e nunca o fato); a **parametrização** da função sem alterá-la, com cinco exemplos alinhados aos da Etapa 6 §11; a **solicitação de modos** de `Scene` v1.1/`MomentResult` sem criar cena nem promover gabarito; os dois níveis de uso (`SchoolUseMode` com cinco valores × `usageScenario` com dez); a modulação de profundidade, tempo e nível-da-turma agregado; o recorte local sob simultaneidade global, lente Brasil e Leis 10.639/2003 e 11.645/2008; as restrições de acessibilidade/infraestrutura como fundação (D10); quinze riscos com mitigação; e as fronteiras com as Etapas 8–14. Nada aqui cria plano de aula, atividade, quiz, rubrica, avaliação ou material do aluno; nada cria UX, stack, MVP, código, Content Matching Engine, cena nova ou mapeamento BNCC em massa; nada povoa o Knowledge Core, altera claims, usa dado pessoal de aluno, cria analytics/LMS ou promete homologação MEC/PNLD; nada usa IA como fonte factual. A direção única de dependência permanece invertida: Experience → Output → Matching → **Planning** → Compliance → Knowledge Core.

**Handoff:** com a Etapa 7 (v1.1) reconciliada e aprovada, a **Etapa 8 — Content Matching Engine** pode ser executada, recebendo o `PlanningProfile`/`PlanningFilter` desta camada e cruzando-o com o Knowledge Core e a `BrazilianEducationComplianceLayer` para selecionar conteúdos, cenas, claims, momentos e recursos adequados — **sem** ainda criar plano de aula final (Etapa 9). A reconciliação de entidades está concluída; resta apenas o resíduo curatorial dos `BNCCMapping`/`CurricularAlignment`, que permanecem `pending` por regra da Etapa 6.

*Documento de entrega da Etapa 7 (v1.1, reconciliada com a Etapa 6 v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6). Define somente a estrutura conceitual do planejamento docente/escolar. Não modela novos dados do núcleo, não escreve código, não propõe MVP, não define stack, não desenha UX final, não cria saída pedagógica, não cria o motor de correspondência, não mapeia BNCC em massa, não cria cena nova, não povoa o Knowledge Core, não altera claims e não usa dados pessoais reais de alunos. Próxima etapa, quando solicitada: Etapa 8 — Content Matching Engine.*
