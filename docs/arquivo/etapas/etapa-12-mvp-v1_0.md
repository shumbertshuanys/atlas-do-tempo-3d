# Etapa 12 — MVP

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 12** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8, v1.0), a `PedagogicalOutputLayer` (Etapa 9, v1.0), a `DesignUX3DLayer` (Etapa 10, v1.0) e a `TechnicalArchitectureLayer` (Etapa 11, v1.0) · 14/06/2026

**Natureza desta etapa.** Documento de **recorte mínimo viável de produto e plano de implementação controlado**. Transforma a arquitetura conceitual e técnica acumulada (Etapas 0–11) em um **`MVPRelease`**: define o que o MVP precisa provar, qual fatia de conteúdo entra, quais fluxos de usuário entram, quais serviços técnicos entram no primeiro corte, quais bancos/índices/cache/armazenamentos serão usados, quais telas/vistas entram, quais artefatos pedagógicos entram, quais permissões entram, quais regras de privacidade/licença/offline entram, o que fica explicitamente fora, quais critérios objetivos indicam que o MVP funcionou e como ele prepara a Etapa 13 (ingestão/povoamento) e a Etapa 14 (operação/governança/QA/analytics/LMS). Conforme solicitado, esta etapa **pode** escolher tecnologias concretas, bibliotecas e arquitetura de implementação inicial, **desde que declare o estatuto da decisão** e **não quebre nenhum invariante da Etapa 11**. Esta etapa **não** escreve código; **não** implementa API real; **não** cria banco real; **não** faz ingestão real; **não** popula dados reais novos; **não** cria `Claim`/`Source`/`Citation`/`Scene`/`ClaimSet`/`Relationship`/`MomentResult`/`MatchSet`/`PedagogicalOutput` novos; **não** altera as cenas-gabarito; **não** mapeia BNCC em massa; **não** substitui a Etapa 13; **não** cria *analytics* operacional real; **não** cria LMS; **não** promete homologação MEC/PNLD; **não** usa dados pessoais reais de alunos; e **não** relaxa qualquer invariante da Etapa 11. Ela **pode** propor *stack* recomendada, módulos, priorização, sequência de entrega, critérios de aceite, plano de testes e escopo de protótipo.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6). "O Planning" = a `TeacherSchoolPlanningLayer` (Etapa 7). "O Matching" = o `ContentMatchingEngine` (Etapa 8). "O Output" = a `PedagogicalOutputLayer` (Etapa 9). "A UX" = a `DesignUX3DLayer` (Etapa 10). "A arquitetura técnica" = a `TechnicalArchitectureLayer` (Etapa 11). "O MVP" = o `MVPRelease` definido na Seção 1.

> **Convenção de estatuto das decisões (herdada da Etapa 11).** **[NORMATIVO]** = vinculante, não pode ser violado; **[RECOMENDADO]** = opção preferida, substituível por equivalente que preserve os invariantes; **[ALTERNATIVA]** = opção aceitável citada para comparação; **[PENDÊNCIA]** = decisão adiada (para a Etapa 13/14), registrada para ser carregada. Nomes de tecnologias concretas aparecem **sempre** como **[RECOMENDADO]** ou **[ALTERNATIVA]**, nunca como **[NORMATIVO]**: o normativo é a propriedade arquitetural; a tecnologia é o meio.

> **Regra central desta etapa.** O MVP deve ser **pequeno o suficiente para ser implementável**, mas **forte o suficiente para provar o diferencial do produto**. A pergunta que esta etapa responde: *"Qual é o menor produto funcional que prova a tese do Atlas do Tempo 3D sem violar conhecimento, licença, privacidade, acessibilidade, publicabilidade, versionamento e rastreabilidade?"* O MVP escolhe **o que entregar primeiro**; **jamais** relaxa uma garantia. Permanecem canônicas e invioláveis: **forma muda; fato não**; **score não é verdade**; **cache não é verdade**; **busca/embedding não é verdade**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**.

---

## Sumário

1. Definição do `MVPRelease`
2. Princípios e invariantes herdados da Etapa 11
3. Tese do MVP e métricas de sucesso
4. Recorte de conteúdo do MVP
5. Fluxos de usuário do MVP
6. Escopo funcional: entra, não entra e fica para depois
7. Escopo técnico do MVP e *stack* recomendada
8. Serviços da Etapa 11 incluídos no MVP
9. Dados, persistência e versionamento no MVP
10. UX e experiência mínima
11. Segurança, privacidade e papéis no MVP
12. Licenciamento, assets e fontes no MVP
13. Testes, QA e critérios de aceite
14. Riscos do MVP e mitigação
15. Encerramento e handoff para as Etapas 13 e 14

---

## 1. Definição do `MVPRelease` (Tarefa 1)

### 1.1 O que o MVP é

O **`MVPRelease`** é um **recorte controlado de produto**: a menor combinação de conteúdo, fluxos, serviços, vistas e artefatos que demonstra a **tese** do Atlas do Tempo 3D — navegar pelo tempo em múltiplas escalas, ver "o que acontecia no mundo neste momento", ligar timeline e globo, e descer de qualquer afirmação até `Claim`/`Source`/licença — preservando o piso epistêmico, a conformidade educacional, a privacidade por minimização e a acessibilidade em **todos** os modos. Ele usa as **três cenas-gabarito já construídas** (4D/4E/4G, consolidadas em 4H) como **corpus mínimo seedado** e atravessa a cadeia conceitual de ponta a ponta em pelo menos um fluxo de professor.

### 1.2 O que o MVP **não** é

O MVP **não é** o produto escolar pronto, **não é** um catálogo de conteúdo, **não é** uma demo comercial de alta fidelidade e **não é** o pipeline de ingestão. Ele **não** popula o KC com milhares de eventos; **não** mapeia a BNCC em massa; **não** coleta dados pessoais reais de alunos; **não** promete homologação MEC nem aprovação PNLD; **não** entrega operação contínua, *analytics* operacional ou LMS (Etapa 14); e **não** substitui o pipeline real de ingestão/povoamento (Etapa 13). O *dataset* seedado das três cenas **não é** ingestão real e **não** vira fonte factual: é insumo de demonstração, marcado como tal.

### 1.3 Por que o MVP não pode relaxar os invariantes da Etapa 11

A Etapa 11 separou três planos: **PlanoArquitetural** (Etapa 11), **PlanoImplementacao** (Etapas 12/13) e **PlanoOperacional** (Etapa 14). O MVP ocupa o início do PlanoImplementacao e **herda** o PlanoArquitetural sem poder afrouxá-lo: os 30 invariantes da Etapa 11 §13 são **[NORMATIVO]**. O MVP escolhe **o que** entregar (recorte), **nunca** **se** uma garantia vale. Um MVP que vazasse `pending`, exportasse expressão NC, misturasse ShareAlike no núcleo, servisse cache como fato, coletasse PII de menor ou quebrasse a acessibilidade não seria "um MVP imperfeito": seria uma violação que reabre a Etapa 11 (E11 §13, invariantes 25/26/30; R-26).

### 1.4 A tese que o MVP precisa provar

> *"É possível navegar por três regimes de tempo — histórico (1789), tempo profundo sem evento (GOE, 2,4 Ga) e tempo profundo com evento (K-Pg, 66 Ma) — usando timeline + globo/mapa + dossiê + artefato pedagógico, preservando fonte, incerteza, licença, publicabilidade e adequação por papel, e atravessando Planning → Matching → Output → UX em um fluxo de professor."*

O detalhamento dessa tese e suas métricas estão na Seção 3.

### 1.5 O limite entre MVP, protótipo, demo e produto escolar pronto

| Conceito | O que prova | O que NÃO é | Estatuto epistêmico |
|---|---|---|---|
| **Protótipo visual** | que uma tela/interação é viável | verificável; conforme; rastreável | descartável; pode ter dado falso rotulado |
| **Demo comercial** | que o produto encanta um público | técnico-pedagógico verificável | encenação; não prova invariantes |
| **`MVPRelease` (esta etapa)** | a **tese** com **garantias** verificáveis sobre corpus seedado | produto pronto; ingestão real; operação | **honesto por construção**: dado seedado rotulado, invariantes preservados |
| **Produto escolar pronto** | adoção em escola, com ingestão e operação reais | objeto desta etapa | conteúdo real, curado, sob operação/governança (E13/E14) |

**[NORMATIVO]:** o MVP não pode ser apresentado como produto escolar pronto, nem o *dataset* seedado como conteúdo real curado em escala. A distinção é exibida ao usuário (Seção 9.7) e registrada na auditoria (Seção 13).

### 1.6 Como o MVP se relaciona com as Etapas 13 e 14

O MVP **prepara** as duas etapas seguintes sem executá-las: deixa o `KnowledgeCoreService` com um **caminho de escrita único e fechado** (apenas seed manual + futuro pipeline), de modo que a Etapa 13 conecte o pipeline real **através** do portão de licenças da Etapa 1.1 sem reabrir fronteiras de escrita; e deixa os ganchos de auditoria, papéis e minimização prontos para que a Etapa 14 acrescente retenção/descarte, consentimento/controle escolar, DPIA, *analytics* agregado, integração LMS e QA pedagógico. O handoff formal está na Seção 15.

### 1.7 Como o MVP preserva a cadeia completa

**[NORMATIVO]** a direção única de dependência permanece a da Etapa 11, e o MVP a percorre inteira em pelo menos o Fluxo A:

```txt
Experience/UX  →  Output  →  Matching  →  Planning  →  Compliance  →  Knowledge Core  →  Sources/Provenance
   (E10)          (E9)        (E8)         (E7)          (E6)            (E2)              (E1/E1.1)
```

Cada seta é lida da esquerda para a direita (cada camada conhece a seguinte; nenhuma à direita conhece a anterior). Nenhum módulo a montante do KC recebe permissão de escrever fato, mesmo colapsado num monólito (Seção 7.2; E11 §3.1).

### 1.8 A entidade `MVPRelease`

```txt
MVPRelease = {
  releaseId,              # mvp:atlas-tempo-3d-v1
  title,                  # "Atlas do Tempo 3D — MVP v1 (três regimes de tempo)"
  thesisToProve,          # tese da Seção 1.4 (três regimes + cadeia professor + piso epistêmico)
  includedScenes,         # [scene:world-1789-french-revolution,
                          #  scene:earth-2-4ga-great-oxidation-event,
                          #  scene:earth-66ma-kpg-extinction]
  includedUserFlows,      # [flowA-professor, flowB-estudante, flowC-exploracao-livre, flowD-exportacao-projetor-estatico]
  includedServices,       # status por serviço (Seção 8): implementado-minimo | modulo-simplificado | stub | fora
  includedStorage,        # [relacional+geoespacial(PostGIS-classe), grafo-em-JSONB+arestas,
                          #  indice-temporal-canonico, busca-textual, cache-MomentResult/Scene,
                          #  object-storage(assets risco 0-1), isolated-license-store(separado, mesmo que vazio)]
  includedViews,          # [TimelineView, Globe3DView, Map2DView, StaticFallbackView, ProjectorModeView,
                          #  DossierPanel, SourceEvidencePanel, EpistemicLabelView, UncertaintyLegend,
                          #  GatingNotice, AnachronismNotice, EquivalenceWarningNotice, MediationControl,
                          #  AccessibilityControl, RoleSelector, ExportPackage(view)]
  includedOutputTypes,    # [lessonPlan, sceneDossier, studentMaterial]  (+ sourceAnalysis embutido)
  includedRoles,          # [teacher, student, curator/admin, publicViewer]
  excludedScope,          # ver Seção 6 (OUT-OF-SCOPE) — offline completo, LMS, analytics, BNCC em massa, etc.
  invariantCoverage,      # mapeamento invariante (E11 §13) → teste mínimo (Seção 2 / Seção 13)
  acceptanceCriteria,     # critérios objetivos de "MVP funcionou" (Seção 3 / Seção 13)
  handoffToIngestion,     # o que a Etapa 13 recebe (Seção 15)
  handoffToOperation      # o que a Etapa 14 recebe (Seção 15)
}
```

**[NORMATIVO]:** `MVPRelease` é uma **entidade de planejamento de produto**, externa a todo conteúdo. Ela **não** cria `Claim`/`Scene`/`Source`; **referencia** as três cenas seedadas por identificador e nada mais.

---

## 2. Princípios e invariantes herdados da Etapa 11 (Tarefa 2)

Os invariantes abaixo são **bloqueadores** do MVP: cada um restringe o que o MVP **pode** fazer e traz um **teste mínimo de conformidade** (detalhado na Seção 13). A numeração entre parênteses é a da Etapa 11 §13.

| Invariante (E11 §13) | Como impacta o MVP | O que o MVP **não pode** fazer | Teste mínimo de conformidade |
|---|---|---|---|
| **Arquitetura não cria fato (1)** | o seed das 3 cenas é insumo, não verdade nova; o único caminho de escrita no núcleo é seed manual fechado + futuro pipeline | gerar fato por código, cache, índice ou IA; abrir caminho de escrita a montante | T-FACTUAL: nenhum `Claim` exibido sem `provenanceRef` rastreável a uma `Source` seedada |
| **Cache não é fonte (2)** | `CacheEntry` carrega `inputVersionSet` e `originClass = derivado` | servir derivado vencido/revogado como fato | T-CACHE: invalidar ao marcar um item `rejected`; o item some do cache |
| **Busca/embedding não é fonte (3)** | busca textual devolve **ponteiros**; índice vetorial fica **fora** do MVP | "responder um fato" pela busca; tratar similaridade como evidência | T-BUSCA: resultado de busca reidrata `claimType`/`confidence`; nunca "texto pelado" |
| **IA não é fonte factual (13)** | IA, se usada, só adapta **forma** (linguagem por faixa), rotulada, sem virar claim | gravar saída de IA como `Claim`/evidência; exibir geração como fato | T-IA: nenhuma saída de IA tem `provenanceRef`; adaptação de linguagem é rotulada |
| **Score não é verdade (6)** | `MatchScore` ordena relevância no Fluxo A; nunca altera claim/`reviewStatus` | usar score como critério de exibição factual; reescrever papel curricular | T-SCORE: dois `MatchScore` distintos sobre o mesmo claim não mudam seu `confidenceLevel` |
| **Forma muda; fato não (14)** | Output/UX/exportação mudam apresentação; nunca o conteúdo do claim ou a incerteza | suprimir citação/incerteza para "ficar limpo"; editar fato ao montar artefato | T-FORMA: o mesmo claim em `lessonPlan`, `studentMaterial` e dossiê mantém `claimType`/`confidence`/fonte |
| **pending/legal-review/rejected não aparece como fato (9)** | o invariante de exibição vale em vista, cache, índice e exportação | exibir item gated a aluno/público; cachear/indexar/exportar gated como fato | T-PENDING: item `pending` semeado nunca chega ao `student`/`publicViewer` (nem como cache/busca/export) |
| **Offline não relaxa licença/publicabilidade/papel/mediação (11)** | offline completo fica **fora** do MVP-MUST; o piso de "sem rede" é o `StaticFallbackView` | tratar ausência de rede como brecha de acesso; empacotar `teacherOnly`/`pending` | T-OFFLINE: o degrau estático aplica a mesma política de papel/faixa que o online |
| **Dados de aluno não entram no KC (12)** | o MVP opera **sem PII real de aluno**; Planning é sobre turma/série/disciplina | gravar identidade de aluno no núcleo; cruzar identidade com pedagógico | T-PII: nenhuma tabela do KC/seed contém campo de identidade de aluno |
| **Logs minimizam dados pessoais (21)** | `TechnicalAuditTrail` registra referência+versão; `dataMinimizationClass` obrigatório | despejar conteúdo sensível ou PII em log | T-LOG: amostra de logs sem PII de menor em claro; classe de minimização presente |
| **Exportação respeita licença e preserva fonte/incerteza (10/16)** | `ExportPackagingService` embute fonte/incerteza/mediação/atribuição e bloqueia o proibido | exportar figura "solta"; exportar expressão NC/SA fora do permitido | T-EXPORT: todo `ExportPackage` carrega citação+incerteza+aviso e respeita licença |
| **Degradação preserva o piso epistêmico (22)** | a escada 3D → 2D → estático mantém fonte/incerteza/natureza em cada degrau | "desligar" rótulos para ganhar desempenho/estética | T-DEGRADA: 2D e estático exibem os mesmos rótulos epistêmicos do 3D |
| **Acessibilidade não é opcional (23)** | equivalente textual, teclado, foco, contraste e redundância não-cromática são MUST | tratar acessibilidade como enfeite ou pós-MVP | T-A11Y: cada vista tem equivalente textual e a cor nunca é o único canal |
| **ShareAlike/ODbL fisicamente isolado (18)** | mapa-base do MVP é PD (Natural Earth), não OSM; SA/ODbL, se entrarem, vão ao `isolated-license-store` | misturar OSM/MapBiomas/Wikipedia no `core-store`/`media-store` | T-SA: nenhum asset SA/ODbL no *bucket* do núcleo; isolamento verificável |
| **NC não entra como expressão (19)** | nenhuma expressão *non-commercial* no MVP; só o **fato recodificado** com fonte própria | reproduzir asset NC (Deep Time Maps, GADM, Seshat) como expressão | T-NC: nenhum asset com `licenseRiskLevel ≥ 4` servido como expressão |
| **API não permite escrita indevida (20)** | contratos do MVP distinguem leitura/escrita; só o pipeline escreve fato | dar a UX/Output/Matching/Planning poder de escrever `Claim`/`reviewStatus` | T-API: tentativa de escrita no KC por serviço a montante é negada e logada |
| **UX/Output/Matching/Compliance/Planning não escrevem no KC (4/5/6/7/8)** | mesmo colapsados no monólito, esses módulos não ganham fronteira de escrita no núcleo | colapsar fronteiras de escrita ao colapsar serviços | T-FRONTEIRA: módulo de Matching não tem credencial de escrita em `Claim` |
| **Sincronização nunca serve versões divergentes (28)** | timeline e globo compartilham `NavigationState` e a mesma versão de conteúdo | mostrar o globo de uma versão com a timeline de outra | T-SYNC: mover o tempo move o espaço sobre a mesma versão |
| **`sourceTimeBasis` nunca é apagado (29)** | o tempo nativo de cada cena (dia/Ga/Ma) é preservado ao lado do `canonicalTimeScalar` | apagar o datum nativo ao derivar o escalar canônico | T-DATUM: cada item temporal exibe `sourceTimeBasis` + escalar derivado |
| **Derivado é reconstruível e não carrega proveniência (26)** | índices/caches do MVP são reconstruíveis a partir do seed autoritativo | tratar índice/cache como origem de verdade | T-DERIVADO: apagar e reconstruir todos os índices/caches não muda nenhum fato |
| **Isolamento de licença vale em todo o caminho (27)** | o isolamento é honrado também em cache, busca, exportação e degrau estático | "vazar" SA/ODbL/NC por um caminho derivado | T-ISOL-CAMINHO: nenhum derivado mistura expressão isolada com o núcleo |
| **A stack não substitui a arquitetura conceitual (24)** | toda tecnologia do MVP é `[RECOMENDADO]`/`[ALTERNATIVA]`; o normativo é a propriedade | tratar uma escolha de produto como invariante | T-STACK: trocar a engine/banco do MVP não muda nenhum `Claim` |

**[NORMATIVO]:** esta tabela é **piso**, não teto. Qualquer funcionalidade do MVP que colida com um destes invariantes é cortada do recorte antes de qualquer entrega; nenhum critério de aceite (Seção 13) pode ser satisfeito por meio de uma violação.

---

## 3. Tese do MVP e métricas de sucesso (Tarefa 3)

### 3.1 A tese, decomposta

A tese da Seção 1.4 decompõe-se em **dez provas** que o MVP deve sustentar (espelham os dez itens da regra central da Etapa 12):

```txt
P1  navegação multiescala no tempo (histórico ↔ Ma ↔ Ga no mesmo eixo canônico)
P2  simultaneidade "o que acontecia no mundo neste momento?" (MomentQuery → MomentResult)
P3  relação timeline ↔ globo/mapa (NavigationState compartilhado, mesma versão)
P4  rastreabilidade artefato → bloco → cena/momento → claim → fonte → licença
P5  distinção fato × inferência × hipótese × reconstrução × incerteza × mediação (rótulos visíveis)
P6  cadeia professor Planning → Matching → Output → UX em um fluxo real (1789)
P7  exploração livre com filtro de adequação (sem grade, sem teacherOnly ao aluno)
P8  degradação 3D → 2D → estático sem perder o piso epistêmico
P9  isolamento de licenças restritivas (SA/ODbL isolado; NC fora; mapa-base PD)
P10 privacidade por minimização (zero PII real de aluno)
```

### 3.2 Métricas de sucesso

Critérios de **avaliação do MVP** — não *analytics* operacional (que é da Etapa 14). São observáveis em revisão controlada, com as três cenas seedadas e usuários de teste sem PII real.

| Classe | Métrica | Critério de sucesso (MVP) |
|---|---|---|
| **Funcional** | P1–P3 executáveis nas 3 cenas | navegar 1789, GOE e K-Pg na timeline; acionar a função em cada uma; timeline e globo sincronizados na mesma versão |
| **Funcional** | P6 ponta a ponta | um `PlanningProfile` de 1789 gera `MatchSet` → `PedagogicalOutput` (`lessonPlan`+`sceneDossier`) visualizável em modo professor |
| **Pedagógica** | P5 visível | em cada cena, um avaliador identifica corretamente o `claimType`/incerteza/mediação a partir da própria interface (sem consultar este documento) |
| **Pedagógica** | adequação por papel | o `student` não acessa nenhum item `teacherOnly`/`pending`/sensível-sem-mediação nas 3 cenas |
| **Técnica** | reconstrutibilidade | apagar e reconstruir índices/caches a partir do seed não altera nenhum `Claim` (T-DERIVADO) |
| **Técnica** | invalidação | marcar um item seedado como `rejected` o remove de toda vista/cache/busca/exportação em uma operação (T-CACHE/T-PENDING) |
| **Rastreabilidade** | P4 íntegra | de qualquer `OutputArtifact` exportado chega-se a `Claim`→`Source`→`LicenseProfile` em todos os modos (T-EXPORT) |
| **Acessibilidade** | P-A11Y | 100% das vistas com equivalente textual; teclado e foco operáveis; contraste e redundância não-cromática presentes (T-A11Y) |
| **Licença** | P9 íntegra | zero asset SA/ODbL no núcleo; zero expressão NC; mapa-base PD; atribuição presente onde exigida (T-SA/T-NC) |
| **Privacidade** | P10 íntegra | zero campo de identidade de aluno em qualquer *store*; logs sem PII de menor (T-PII/T-LOG) |
| **Desempenho** | piso de acesso | a versão 2D/estática carrega e fica interativa em hardware escolar modesto e conexão instável; sem WebGL, degrada sem quebrar |
| **Usabilidade (qualitativa)** | clareza do diferencial | em teste qualitativo com professores de teste, a maioria reconhece a simultaneidade e a rastreabilidade como o diferencial — sem confundir o MVP com currículo oficial/PNLD |

**[NORMATIVO]:** nenhuma métrica é satisfeita por relaxar um invariante; uma "boa nota" obtida escondendo incerteza, vazando `pending` ou coletando PII é **falha**, não sucesso (E11 §13; R-26/R-28).

### 3.3 O que estas métricas não são

Não são KPIs de produto, não são métricas de engajamento, não são telemetria individual de estudante e não medem adoção comercial. São **critérios de verificação da tese e das garantias** sobre um corpus controlado. A medição operacional real (agregada, pseudonimizada, sob minimização) é **[PENDÊNCIA]** explícita da Etapa 14 (E11 §12.5; R-28).

---

## 4. Recorte de conteúdo do MVP (Tarefa 4)

### 4.1 O corpus mínimo: as três cenas-gabarito

**[NORMATIVO]** o MVP usa exatamente as **três cenas-gabarito** já construídas (4D/4E/4G) e consolidadas na `Scene` v1.1 (4H), **sem criar conteúdo novo**:

```txt
includedScenes = [
  scene:world-1789-french-revolution,     # histórico (documental) — simultaneidade humana
  scene:earth-2-4ga-great-oxidation-event, # tempo profundo SEM evento — States/Process dominantes
  scene:earth-66ma-kpg-extinction          # tempo profundo COM evento — híbrido (gatilho→cascata)
]
```

### 4.2 Por que três cenas bastam para provar a tese

Cada cena cobre um **regime temporal** e um **perfil de risco** distintos, e juntas exercitam todos os mecanismos da `Scene` v1.1 que o MVP precisa demonstrar:

| Mecanismo a provar | 1789 (A) | GOE 2,4 Ga (B) | K-Pg 66 Ma (C) |
|---|---|---|---|
| Regime temporal | histórico (dia/mês/ano) | geológico profundo (Ga, faixa) | geológico profundo + evento pontual (Ma) — **híbrido** |
| Simultaneidade histórica (P2) | **sim** (mundo humano ao mesmo tempo) | planeta (sistemas) | planeta em crise encadeada |
| Tempo profundo sem evento | — | **sim** (oxigenação gradual, **zero Event**) | — |
| Cena híbrida: evento + Process + State | — | — | **sim** (`triggerItem` + cascata) |
| Gating editorial | **sim** (escravidão/colonização/indígenas) | — | — |
| Gating científico | — | **sim** (paleogeografia/magnitude) | **sim** (peso do Deccan, inverno/incêndios) |
| Incerteza temporal | baixa | **alta** | **alta** |
| Incerteza espacial / paleogeografia (`paleoPositionPolicy`) | fronteiras históricas de 1789 | continentes pré-modernos (esquemático) | **paleoposição** (Chicxulub/Yucatán ≠ posição em 66 Ma) |
| `ModernCorrespondence` (lente "o que hoje é…") | **sim** (Brasil/EUA/Qing hoje) | aplicável a evidências | aplicável (México em 66 Ma ⇒ anacronismo) |
| Dossiê ("como sabemos disso") | 15 blocos (simultaneidade) | 18 blocos (proxies) | 20 blocos (sistema + evidência) |
| `claimSets` | controvérsias historiográficas/terminologia | debates científicos | debates científicos **com peso** |
| `weightedClaimSets` (anti-falsa-equivalência) | causas concorrentes coexistentes | — | **impacto ≫ Deccan; negacionismo rotulado-rejeitado** |
| `cascadeStructure` (gatilho→cascata) | mini-cascatas locais (não principal) | cascata lenta/difusa (sem gatilho) | **cascata canônica** com `confidenceByStage` decaindo |
| `paleoPositionPolicy` | trivial/histórico | esquemático | **crítico** (default reconstrução modelada) |

**Conclusão:** as três cenas, juntas, provam P1–P9 sem expansão do KC. 1789 prova simultaneidade histórica, `ModernCorrespondence` e gating **editorial**; GOE prova tempo profundo sem evento, `ClaimSet`×`UncertaintyProfile`, States dominantes e o globo esquemático; K-Pg prova a cena híbrida, `cascadeStructure`, `weightedClaimSets` e `paleoPositionPolicy`. P10 (privacidade) e P-A11Y são transversais e independem de mais conteúdo.

### 4.3 Estatuto do conteúdo no MVP

**[NORMATIVO]** as três cenas entram como **`sceneCompletenessLevel = gabarito-interno`** e **`publicabilityStatus` parcial** (Nível 2; a B pode chegar a 2→3 na paleogeografia), exatamente como aprovado em 4H §8/§9 — **sem alteração**. O MVP **respeita** esses estados: o que está `pending`/mediado nas cenas continua gated; o que é publicável é exibido com seus rótulos. O `gatingReason` de cada cena (editorial em A; científico+geometria em B e C) é exibido à curadoria e respeitado para aluno/público.

### 4.4 O que **não** entra no conteúdo do MVP

```txt
OUT (conteúdo) = {
  expansão massiva do KC (milhares de Event/Process/State),
  todos os períodos históricos / todas as eras geológicas,
  todos os componentes curriculares,
  mapeamento BNCC em massa (BNCCMapping/CurricularAlignment permanecem pending; só alinhamento exibido),
  dados reais de escolas e de alunos,
  quaisquer assets proprietários / NC como expressão (Deep Time Maps, GADM, Seshat, ACLED, scans Rumsey),
  qualquer Claim/Source/Scene NOVO (a Etapa 12 não povoa nem cria conteúdo),
  qualquer alteração às três cenas-gabarito
}
```

**[NORMATIVO]:** o *dataset* seedado das três cenas **não substitui** o pipeline de ingestão da Etapa 13 e **não** é tratado como conteúdo real curado em escala. A Seção 9 fixa como o seed é marcado, versionado e auditado para que ninguém o confunda com ingestão (R-MVP-06/R-MVP-07).

---

## 5. Fluxos de usuário do MVP (Tarefa 5)

O MVP entrega **quatro fluxos**. Para cada um: entrada, passos, entidades acionadas, serviços acionados, resultado, riscos e critérios de aceite.

### 5.1 Fluxo A — Professor planejando aula (Planning → Matching → Output → UX)

- **Entrada.** Um `teacher` (modo controlado, sem PII de aluno) cria um planejamento simples sobre **Revolução Francesa / 1789**: série/etapa, disciplina (História), `depthLevel`, `usageScenario`, recorte regional opcional, `TimeBudget`.
- **Passos.**
  1. O professor preenche um `PlanningProfile` (sem dado pessoal de aluno).
  2. O Matching cruza o `PlanningProfile` × corpus seedado × `ComplianceProfile`, calcula `MatchScore` multidimensional e monta um `MatchSet` (com `curricularRole`: França/1789 = `curricularCore`; outras regiões de 1789 = `contextual`/`enrichment`).
  3. O Output transforma o `MatchSet` em `PedagogicalOutput` com `lessonPlan` + `sceneDossier` (e, opcionalmente, `studentMaterial`), preservando `OutputCitationBundle`, incerteza e `OutputComplianceSummary`.
  4. A UX abre uma `ExperienceSession` em `teacherMode`: timeline + globo + dossiê + painel de fonte/evidência + rótulos epistêmicos.
- **Entidades acionadas.** `PlanningProfile`, `usageScenario`, `MatchSet`/`MatchScore`/`MatchingAuditTrail`, `PedagogicalOutput`/`OutputArtifact`/`OutputSectionBlock`/`OutputCitationBundle`/`OutputComplianceSummary`/`OutputAuditTrail`, `ExperienceSession`/`NavigationState`/`UXAuditTrail`, `Scene` (1789), `MomentResult` (de 1789).
- **Serviços acionados.** `PlanningService`, `MatchingService`, `PedagogicalOutputService`, `SceneMomentService`, `BrazilianComplianceService`, `KnowledgeCoreService` (leitura por REF), `IdentityAccessService`, `AuditTrailService`, `CacheInvalidationService`.
- **Resultado.** Um `PedagogicalOutput` de 1789 visualizável em modo professor, com fonte/incerteza/mediação e nota explícita **"alinhamento BNCC ≠ homologação ≠ PNLD"**.
- **Riscos.** `MatchScore` virar critério de verdade (R-MVP-13); artefato suprimir citação/incerteza (R-MVP-12); `teacherOnly` vazar (coberto por ABAC); planejamento capturar PII (R-MVP-21).
- **Critérios de aceite.** Cadeia completa executa; `OutputCitationBundle` presente em cada bloco factual; nenhum item `pending` no artefato como fato; nota anti-homologação presente; nenhum campo de identidade de aluno no `PlanningProfile`.

### 5.2 Fluxo B — Estudante explorando cena (timeline + globo + dossiê com filtro por faixa)

- **Entrada.** Um `student` (faixa derivada de `ComplianceProfile.ageProfileRef`, sem PII) abre uma das três cenas.
- **Passos.**
  1. A UX abre `ExperienceSession` em `studentMode` com `studentFacingMode = voltadoAoAluno`.
  2. O estudante navega na `TimelineView` e no `Globe3DView`/`Map2DView`; clica em itens; abre o `DossierPanel` ("como sabemos disso").
  3. ABAC filtra `visibilityClass`: `teacherOnly`/`internalReviewOnly`/`pending`/sensível-sem-mediação **não** aparecem; `sensitiveItems` só com mediação conforme faixa; `hiddenItems` no máximo como contagem.
- **Entidades acionadas.** `Scene`, `MomentResult`, `OutputSectionBlock` (face do aluno), `DossierPanel`, `EpistemicLabelView`, `UncertaintyLegend`, `AnachronismNotice`, `NavigationState`.
- **Serviços acionados.** `SceneMomentService`, `BrazilianComplianceService`, `ExperienceSessionService`, `IdentityAccessService`, `CacheInvalidationService`, `AssetMediaService`, `AuditTrailService`.
- **Resultado.** Exploração navegável e adequada à faixa, com rótulos epistêmicos visíveis e sem conteúdo restrito.
- **Riscos.** Vazar `teacherOnly`/`pending` (R-MVP-17/R-MVP-03); UX esconder incerteza por estética (R-MVP-05); estudante ver conteúdo sensível sem mediação (R-MVP-17).
- **Critérios de aceite.** Nenhum item `teacherOnly`/`pending` acessível ao `student` nas 3 cenas; rótulos epistêmicos sempre presentes quando há claim; mediação aplicada onde a faixa exige.

### 5.3 Fluxo C — Exploração livre ("o que acontecia neste momento?")

- **Entrada.** Um `student`/`publicViewer` escolhe **um ano/idade/evento** e aciona a função, **sem** passar por Matching/Output (não há planejamento).
- **Passos.**
  1. A UX monta uma `MomentQuery` (por ano, por idade geológica, ou por evento foco) com `ageLevelMode`/`publicabilityMode`/`layerFilters` derivados do contexto.
  2. A função retorna um `MomentResult`: foco, simultâneos centrais/contextuais, States, `claimSets`/`weightedClaims`, `uncertaintyProfiles`, `hiddenItems` (só contagem em público), `anachronismWarnings`, `equivalenceWarnings`, `publicabilityStatus`/`gatingReason`, `navigationSuggestions`.
  3. A UX apresenta o resultado em `FreeExplorationView`, com a simultaneidade global coerente entre timeline e globo.
- **Entidades acionadas.** `MomentQuery`, `MomentResult`, `Scene` (quando o foco coincide com uma cena), `WeightedClaim`, `UncertaintyProfile`, `EquivalenceWarningNotice`.
- **Serviços acionados.** `SceneMomentService`, `BrazilianComplianceService`, `ExperienceSessionService`, `IdentityAccessService`, `CacheInvalidationService`, `AuditTrailService`.
- **Resultado.** Resposta a "o que acontecia no mundo neste momento?" com filtro de adequação, sem currículo e sem trilha pedagógica.
- **Riscos.** Exploração livre virar obrigação curricular (proibido — E6 §9); `hiddenItems` vazarem como fato (R-MVP-03); falsa simetria em `weightedClaimSets` (negacionismo como "lado") (R-MVP-15/R-MVP-30).
- **Critérios de aceite.** A função roda sem Matching/Output; `hiddenItems` nunca expostos como fato; negacionismo aparece **rotulado-rejeitado**, fora do `ClaimSet`; simultaneidade coerente timeline↔globo.

### 5.4 Fluxo D — Exportação / Projetor / Estático

- **Entrada.** Um `teacher` exporta ou projeta um artefato (plano, dossiê ou material do aluno) gerado no Fluxo A, ou usa o degrau estático em sala sem rede.
- **Passos.**
  1. A UX aciona o `ExportPackagingService` (ou o `ProjectorModeView`/`StaticFallbackView`).
  2. O serviço monta o `ExportPackage` embutindo **fonte/citação**, **rótulo epistêmico + incerteza**, **aviso de mediação** (se há sensível), **aviso de anacronismo/equivalência** (se aplicável) e a nota **"alinhamento BNCC ≠ homologação ≠ PNLD"**.
  3. O `LicenseComplianceService` revalida a licença: o que a licença não permite é **bloqueado**; o que é risco 0–1 é exportável com atribuição.
- **Entidades acionadas.** `ExportPackage`, `OutputCitationBundle`, `OutputConstraintWarning`, `LicenseProfile`, `ProjectorModeView`, `StaticFallbackView`.
- **Serviços acionados.** `ExportPackagingService`, `PedagogicalOutputService`, `LicenseComplianceService`, `AssetMediaService`, `IdentityAccessService`, `AuditTrailService`.
- **Resultado.** Artefato exportado/projetado/estático que preserva o piso epistêmico e a atribuição, com bloqueio do que a licença não permite.
- **Riscos.** Exportar figura "solta" sem fonte (R-MVP-10); exportar NC/SA fora do permitido (R-MVP-25); projeção expor `teacherOnly` ao aluno sem mediação (R-MVP-17); offline incluído cedo demais (R-MVP-19).
- **Critérios de aceite.** Todo `ExportPackage` carrega citação+incerteza+aviso; exportação de expressão NC/SA proibida é bloqueada e logada; modo projetor mantém legibilidade dos rótulos; o degrau estático preserva os rótulos e a política de papel.

### 5.5 O que os quatro fluxos juntos provam

| Prova (Seção 3.1) | A | B | C | D |
|---|---|---|---|---|
| P1 navegação multiescala | ✓ | ✓ | ✓ | — |
| P2 simultaneidade | ✓ | ✓ | ✓ | — |
| P3 timeline ↔ globo | ✓ | ✓ | ✓ | — |
| P4 rastreabilidade | ✓ | ✓ | ✓ | ✓ |
| P5 distinção epistêmica | ✓ | ✓ | ✓ | ✓ |
| P6 cadeia professor | ✓ | — | — | parcial |
| P7 exploração livre c/ filtro | — | parcial | ✓ | — |
| P8 degradação c/ piso | ✓ | ✓ | ✓ | ✓ |
| P9 isolamento de licença | ✓ | ✓ | ✓ | ✓ |
| P10 privacidade | ✓ | ✓ | ✓ | ✓ |

---

## 6. Escopo funcional: entra, não entra e fica para depois (Tarefa 6)

Matriz `MVP-MUST` (obrigatório no primeiro corte), `MVP-SHOULD` (entra se couber sem atrasar o MUST), `MVP-COULD` (desejável; pode ficar para a iteração seguinte) e `OUT-OF-SCOPE` (fora do MVP). **O MVP é realista: nem tudo é MUST.**

| Frente | MVP-MUST | MVP-SHOULD | MVP-COULD | OUT-OF-SCOPE |
|---|---|---|---|---|
| **Timeline** | multiescala básica nos 3 regimes (histórico/Ma/Ga) no eixo canônico; `sourceTimeBasis` visível | barras de incerteza por item; zoom por regime | mini-cascata na timeline (1789) | régua editável pelo usuário; anotação colaborativa |
| **Globo/mapa** | `Map2DView` com base PD (Natural Earth) + `Globe3DView` quando há WebGL; marcadores por `visibilityClass` | paleoposição rotulada (K-Pg) no globo; halo/esquemático (GOE) | animação didática de cascata espacial (K-Pg) | edição de geometrias; camadas SA/ODbL ao vivo |
| **Dossiê** | `DossierPanel` "como sabemos disso" nas 3 cenas | cartões de evidência por claim | dossiê comparativo entre cenas | edição rica de dossiê pelo usuário |
| **WhatWasHappeningAtMoment** | `MomentQuery`→`MomentResult` por ano/idade/evento; `hiddenItems` só contagem em público | `navigationSuggestions`; antes/depois (K-Pg) | "por consequências" (cascata do K-Pg) | geração de cena pública a partir de candidato |
| **Planning** | `PlanningProfile` de 1789 sem PII; `usageScenario` | `DepthPreference`/`TimeBudget` modulando densidade | recorte local (`ModernCorrespondence` Brasil) | planejamento de rede/escola em massa |
| **Matching** | `MatchSet`/`MatchScore` no Fluxo A (1789); porta dura de publicabilidade | `CoverageBalance`/`SourceSupportSummary` | `curricularRoleScope` ajustável | matching sobre KC massivo |
| **Output** | `lessonPlan` + `sceneDossier` (1789); `OutputCitationBundle`/`OutputComplianceSummary` | `studentMaterial` por faixa; `OutputConstraintWarning` | `sourceAnalysis` destacado; `comparisonOutput` | quiz/avaliação/rubrica completos; edição rica |
| **UX** | `teacherMode`/`studentMode`/`freeExplorationMode`; rótulos/avisos; `RoleSelector` | `projectorMode`; `comparisonMode` (K-Pg) | `guidedExplorationMode` | todos os modos da Etapa 10; colaboração multiusuário |
| **Exportação** | `ExportPackage` com fonte/incerteza/mediação/atribuição; bloqueio por licença | export PDF + PNG do globo/timeline | export de pacote multi-artefato | export white-label; integração de impressão escolar |
| **Offline** | — (piso de "sem rede" = `StaticFallbackView`) | — | `OfflinePackage` mínimo, versionado/assinado, de 1 cena | offline completo das 3 cenas; app empacotado |
| **Projetor** | `ProjectorModeView` legível (alto contraste, baixa densidade) | mediação na projeção | — | controle remoto/scanner de sala |
| **Busca** | busca textual por rótulo/`statement` devolvendo **ponteiros**; respeita `visibilityClass` | filtros por camada/tempo | — | busca vetorial/semântica (índice vetorial) |
| **Login** | modo controlado por papel, **sem PII real de aluno** | troca de papel para demonstração | pseudônimos de sessão de turma | SSO/OAuth real; cadastro de alunos |
| **Permissões** | RBAC+ABAC simplificado (4 papéis); bloqueio de `teacherOnly`/`pending` | log de acesso negado | políticas declarativas refináveis | papéis de rede/secretaria; delegação fina |
| **Curadoria** | seed manual fechado das 3 cenas (read-only ao público) | visão de curadoria de `gatingReason` | fila de revisão de demonstração | pipeline curatorial completo (E13) |
| **Ingestão** | — (seed manual, não pipeline) | — | esqueleto do contrato de ingestão (sem rodar) | ingestão real de fontes (E13) |
| **BNCC** | exibir `BNCCMapping`/`CurricularAlignment` **como alinhamento `pending`** | nota anti-homologação no viewer e no export | 1–2 alinhamentos de 1789 confirmados como demonstração | mapeamento BNCC em massa; selo curricular |
| **Analytics** | — | — | contadores agregados de demonstração (sem PII) | *analytics* operacional real (E14) |
| **LMS** | — | — | — | qualquer integração LMS (E14) |
| **Acessibilidade** | equivalente textual; teclado; foco; contraste; redundância não-cromática; movimento reduzido | legendas/descrições nos assets | — | laudo formal ASES (E14) |
| **Licença** | só risco 0–1 como expressão; NC fora; SA/ODbL isolado; `LicenseProfile` por asset; atribuição | tela "fonte/licença deste conteúdo" ao usuário | confirmação por asset de demonstração | contratos comerciais (risco 5) |
| **Privacidade** | zero PII real de aluno; logs minimizados; identidade × sessão × pedagógico separados | pseudonimização de sessão | — | DPIA formal; fluxo de consentimento (E14) |
| **Auditoria** | `TechnicalAuditTrail` append-only; logs de acesso/mudança/exportação/cache/licença | trilha de versão servida | painel de auditoria de demonstração | observabilidade/SRE de produção (E14) |

**[NORMATIVO]:** itens `OUT-OF-SCOPE` não são "proibidos para sempre" — são **fora do MVP**. Nenhum item `MVP-SHOULD`/`MVP-COULD` pode ser promovido a MUST se isso exigir relaxar um invariante ou atrasar a prova da tese (Seção 3).

---

## 7. Escopo técnico do MVP e *stack* recomendada (Tarefa 7)

### 7.1 Princípio da escolha técnica

**[NORMATIVO]** toda tecnologia abaixo é `[RECOMENDADO]`/`[ALTERNATIVA]`; o **normativo** é a propriedade arquitetural da Etapa 11 (autoritativo × derivado; proveniência por aresta; isolamento físico de licença; degradação com piso epistêmico). **Trocar qualquer produto não pode mudar um `Claim`.** A regra de bolso: **escolher o mais simples que prove a tese sem ferir invariante e que evolua sem reescrita** (E11 §1.7/§14, R-21/R-25).

### 7.2 Arquitetura de implementação: monólito modular

**[RECOMENDADO]** um **monólito modular** (um processo, um *deploy*), com os 15 *bounded contexts* da Etapa 11 como **módulos internos** de fronteiras de escrita preservadas — não microserviços. **Por que é suficiente:** o MVP tem um corpus pequeno e quatro fluxos; microserviços só adicionariam custo operacional sem provar nada da tese. **Qual invariante preserva:** E11 §3.1 — "a separação em quinze serviços é lógica; o MVP pode colapsar vários em um monólito, mas **não** pode colapsar as **fronteiras de escrita**". O módulo de Matching, mesmo no mesmo processo, **não** ganha credencial de escrita em `Claim` (invariantes 4–8/20). **Risco:** alguém "encurtar caminho" e deixar um módulo a montante escrever no núcleo (R-MVP-03/R-MVP-16) — mitigado por um único ponto de escrita no `KnowledgeCoreService` e por verificação de fronteira nos contratos (Seção 13, T-FRONTEIRA/T-API). **Quando evoluir:** extrair serviços para processos próprios quando volume/escala da Etapa 14 exigir.

### 7.3 *Stack* recomendada por frente

| Frente | [RECOMENDADO] | [ALTERNATIVA] | Por que basta para o MVP | Invariante que preserva | Risco que cria | Quando evoluir/substituir |
|---|---|---|---|---|---|---|
| **Frontend** | aplicação web em React/TypeScript (Next.js-classe) | SPA com Vite/React | uma base web cobre os 4 fluxos e os modos professor/estudante/projetor | 4/14/15/23 (apresenta; não escreve fato; acessível) | acoplamento a framework (R-MVP-27) | app nativo/empacotado só se a operação (E14) exigir |
| **Timeline** | componente próprio sobre Canvas/SVG | biblioteca de timeline de terceiros adaptada | a régua Ga↔dia e a incerteza são específicas; controle próprio do escalar canônico | 28/29 (mesma versão; `sourceTimeBasis`) | esforço de construção (R-MVP-04) | abstrair quando houver mais regimes/itens |
| **Globo 3D** | engine de globo geoespacial (Cesium/3D Tiles-classe) | deck.gl-classe sobre WebGL | honra paleoposição rotulada e degrada para 2D | 22/28 (piso epistêmico; sincronização) | 3D atrasar o MVP (R-MVP-04) | trocar se o orçamento de desempenho pedir |
| **Mapa 2D (piso garantido)** | MapLibre GL com base **Natural Earth (PD, risco 0)** | renderizador estático server-side | base sem GPU; evita ShareAlike do OSM no MVP | 18/22 (SA isolado; degradação) | esquecer atribuição de base (baixo c/ PD) | adicionar OSM **isolado** só com plano de atribuição/SA |
| **Renderização estática** | imagem + equivalente textual gerados server-side | snapshot estático do 2D | é o piso de acesso (a11y/offline/impressão) | 22/23 (piso; acessibilidade) | divergência visual do 2D | gerar sob demanda quando o catálogo crescer |
| **Backend/API interna** | monólito modular em TypeScript/Node **ou** Python/FastAPI | Go/serviço único | API interna simples cobre os contratos do MVP | 20 (sem escrita indevida) | API frouxa permitir escrita reversa (R-MVP-16) | versionar contratos antes de abrir a terceiros |
| **Banco relacional + geoespacial** | **PostgreSQL + PostGIS** | relacional gerenciado equivalente | guarda camadas externas e índice geoespacial num só motor | 26/34 (derivado reconstruível; geoespacial) | sobrecarregar um só banco | separar bancos por classe na escala (E14) |
| **Grafo do KC (inicial)** | **tabelas de aresta + JSONB** no PostgreSQL, com `provenanceRef` obrigatório por aresta | *triplestore* RDF*/property graph | o corpus de 3 cenas não exige banco de grafo dedicado; preserva "proveniência por aresta" | 1/26 (não cria fato; reconstruível) | travessia/proveniência custarem em escala (R-MVP-03/E11 R-33) | migrar para grafo dedicado quando a travessia pesar (E13/E14) |
| **Índice temporal** | coluna `canonicalTimeScalar` + índice B-tree; `sourceTimeBasis` preservado | índice de intervalos dedicado | recortes da timeline sobre poucos itens | 29 (`sourceTimeBasis`) | erro de datum (E11 R-32) | índice de intervalos quando o volume crescer |
| **Índice geoespacial** | GIST do PostGIS | índice geoespacial dedicado | `ModernCorrespondence`/paleoposição das 3 cenas | 18 (SA isolado) | erro de CRS (E11 R-34) | serviço geoespacial próprio na escala |
| **Busca textual** | full-text do PostgreSQL (tsvector) devolvendo **ponteiros** | motor de busca dedicado | encontrar itens nas 3 cenas; reidrata rótulos | 3/9 (busca não é fonte; respeita gating) | busca "responder fato" (R-MVP-22) | motor dedicado quando o catálogo crescer |
| **Busca vetorial/semântica** | **fora do MVP** | — | desnecessária para 3 cenas; risco de virar "fonte" | 3/13 (embedding/IA não é fonte) | adoção prematura (R-MVP-23) | avaliar na Etapa 13/14 como `DerivedIndex` (`carriesProvenance=false`) |
| **Cache** | cache em processo/Redis-classe para `MomentResult`/`Scene` com `inputVersionSet` | cache HTTP/CDN para tiles/estático | acelera as consultas frequentes das 3 cenas | 2/26/27 (cache não é fonte; isolado) | cache servir item revogado (R-MVP-01) | CDN para tiles/3D na escala |
| **Object storage** | S3-classe (MinIO local em dev) para assets risco 0–1 | armazenamento de arquivos do provedor | guarda assets/tiles próprios e PD/CC | 17/18/27 (licença por asset; isolado) | asset "órfão de licença" (R-MVP-24) | CDN + LOD na escala (E11 R-36) |
| **`isolated-license-store`** | *bucket*/esquema **separado** (mesmo que vazio no MVP) | partição física distinta | garante o lugar físico do isolamento desde já | 18/27 (isolamento em todo o caminho) | "esquecer" de criar e misturar depois | manter separado sempre; nunca fundir |
| **Autenticação/autorização** | sessão por papel em **modo controlado**, sem PII real de aluno | autenticação local mínima | os 4 papéis e o ABAC bastam para os fluxos | 12/15/21 (sem PII; papel; log mínimo) | login complexo demais (R-MVP-14) | SSO/OAuth é **[PENDÊNCIA]** da Etapa 14 |
| **Auditoria/logs** | tabela append-only (`TechnicalAuditTrail`) + logs estruturados com `dataMinimizationClass` | coletor de logs gerenciado | registra acesso/mudança/exportação/cache/licença | 16/21 (auditável; PII mínima) | log capturar PII (R-MVP-21) | observabilidade de produção na Etapa 14 |
| **Exportação** | empacotamento server-side (HTML/PDF/PNG) com proveniência embutida | exportação client-side controlada | preserva fonte/incerteza/atribuição e bloqueia o proibido | 10/16 (licença; auditável) | export sem fonte (R-MVP-10) | formatos adicionais sob demanda |
| **Pacote offline** | **fora do MVP-MUST** (piso = estático); `OfflinePackage` mínimo só como `MVP-COULD` | app empacotado para sala | sem rede já é coberto pelo degrau estático | 11 (offline não relaxa garantias) | offline cedo demais (R-MVP-19) | `OfflinePackage` assinado/validade quando a sala sem rede for prioridade |

### 7.4 O que o escopo técnico **não** faz

**[NORMATIVO]** o escopo técnico do MVP **não escreve código** nesta etapa (a implementação é a execução do MVP, não este documento), **não cria banco real**, **não roda ingestão**, **não decide produto final** onde a Etapa 11 deixou `[PENDÊNCIA]` que pertence à Etapa 13/14, e **não** adota índice vetorial. As escolhas acima são o **recorte recomendado** que orienta a construção do MVP preservando os 30 invariantes.

---

## 8. Serviços da Etapa 11 incluídos no MVP (Tarefa 8)

A Etapa 11 definiu **15 serviços**. O MVP os classifica em **implementado-mínimo**, **módulo-simplificado**, **stub** ou **fora**. Mesmo colapsados no monólito (Seção 7.2), **as fronteiras de escrita são preservadas**.

| Serviço | Status no MVP | Implementação mínima | O que fica fora | Risco | Critério de aceite |
|---|---|---|---|---|---|
| **`KnowledgeCoreService`** | implementado-mínimo | servir (read-only) o grafo seedado das 3 cenas; **um único** caminho de escrita (seed manual fechado) | escrita por qualquer camada a montante; ingestão real | escrita reversa fura a soberania (R-MVP-03/16) | nenhuma escrita no KC fora do seed; toda leitura traz rótulos+proveniência |
| **`SourceProvenanceService`** | implementado-mínimo | servir `Source`/`Citation`/`ProvenanceMetadata`/`DatasetSnapshot` das 3 cenas | curadoria de novas fontes; pipeline | claim sem proveniência (R-MVP-08) | todo `Claim` exibido rastreia a uma `Source` A/B seedada |
| **`LicenseComplianceService`** | implementado-mínimo | aplicar a matriz risco 0–5 na exibição/exportação; permitir só 0–1 como expressão; bloquear NC; marcar isolamento | confirmação por asset em escala; contratos | NC/SA vazar por export (R-MVP-25) | exportação de expressão proibida é bloqueada e logada |
| **`SceneMomentService`** | **implementado** (diferencial) | servir `Scene` v1.1 das 3 cenas e operar `WhatWasHappeningAtMoment` (`MomentQuery`→`MomentResult`) | geração de cena pública a partir de candidato | vazar `hiddenItems`/`pending` (R-MVP-03) | função roda nas 3 cenas; `hiddenItems` só contagem em público |
| **`BrazilianComplianceService`** | módulo-simplificado | servir `AllowedUseContext`/`AgeSuitability`/`SensitiveContentRule`/`SchoolUseMode` seedados das 3 cenas; exibir `BNCCMapping` como alinhamento `pending` | mapeamento BNCC em massa; selo | alinhamento parecer homologação (R-MVP-16) | adequação/sensível aplicados; nota anti-homologação presente |
| **`PlanningService`** | implementado-mínimo | criar/ler `PlanningProfile` de 1789 sem PII; `usageScenario` aninhado em `schoolUseModeRefs` | planejamento de rede/escola em massa | PII no planejamento (R-MVP-21) | `PlanningProfile` sem campo de identidade de aluno |
| **`MatchingService`** | implementado-mínimo | cruzar `PlanningProfile`×corpus×Compliance; `MatchScore`; `MatchSet`; `MatchingAuditTrail`; porta dura | matching sobre KC massivo | score virar verdade (R-MVP-13) | `MatchScore` não altera `confidenceLevel`/`reviewStatus` |
| **`PedagogicalOutputService`** | implementado-mínimo | gerar `lessonPlan`+`sceneDossier` (e `studentMaterial`) de 1789 com `OutputCitationBundle`/`OutputComplianceSummary` | quiz/avaliação/rubrica completos; edição rica | artefato suprimir citação/incerteza (R-MVP-12) | cada bloco factual carrega citação; incerteza preservada |
| **`ExperienceSessionService`** | **implementado** | `ExperienceSession`/`NavigationState`/estados de vista; `teacherMode`/`studentMode`/`freeExplorationMode`/`projectorMode` | colaboração multiusuário; todos os modos da E10 | relaxar `visibilityClass`/faixa (R-MVP-17) | sessão respeita papel/faixa; rótulos sempre visíveis |
| **`AssetMediaService`** | módulo-simplificado | servir assets risco 0–1 (Natural Earth, próprios, CC); tiles; `LicenseStorageBinding` por asset | assets pesados em escala; CDN/LOD completo | asset órfão de licença (R-MVP-24) | nenhum asset sem `LicenseProfile`; nada SA/ODbL no núcleo |
| **`ExportPackagingService`** | implementado-mínimo | montar `ExportPackage` com fonte/incerteza/mediação/atribuição; bloquear por licença | formatos avançados; white-label | export sem fonte (R-MVP-10) | todo `ExportPackage` carrega citação+incerteza+aviso |
| **`IdentityAccessService`** | módulo-simplificado | RBAC+ABAC para `teacher`/`student`/`curator|admin`/`publicViewer`; modo controlado sem PII real | SSO/OAuth; cadastro de alunos | autenticação frágil/PII (R-MVP-14/21) | bloqueio de `teacherOnly`/`pending`; zero PII real |
| **`AuditTrailService`** | implementado-mínimo | `TechnicalAuditTrail` append-only; logs de acesso/mudança/exportação/cache/licença com minimização | observabilidade/SRE de produção | log com PII (R-MVP-21) | logs sem PII de menor; `dataMinimizationClass` presente |
| **`CacheInvalidationService`** | implementado-mínimo | cache de `MomentResult`/`Scene` com `inputVersionSet`; invalidar em `reviewStatusChanged`/`publicabilityChanged` | invalidação orientada a eventos em escala | cache servir item revogado (R-MVP-01) | marcar item `rejected` o remove do cache imediatamente |
| **`OfflinePackageService`** | **fora** (ou stub) | nenhuma no MVP-MUST; piso de "sem rede" é o `StaticFallbackView`; `OfflinePackage` mínimo só como `MVP-COULD` | offline completo das 3 cenas | offline cedo demais (R-MVP-19) | se entrar como COULD: pacote versionado/assinado, sem `teacherOnly`/`pending` |

**Resumo:** **2 implementados** (`SceneMomentService`, `ExperienceSessionService` — o coração da experiência), **8 implementados-mínimos** (núcleo, proveniência, licença, planning, matching, output, export, cache, auditoria), **3 módulos-simplificados** (compliance, assets, identidade), **1 fora/stub** (offline). A priorização concentra esforço no diferencial (simultaneidade + experiência) e na cadeia de garantias, e adia o que não prova a tese.

---

## 9. Dados, persistência e versionamento no MVP (Tarefa 9)

### 9.1 Como o MVP guarda cada coisa

| Dado | Onde (MVP) | Classe | Versionado? | Invalidação | Auditoria |
|---|---|---|---|---|---|
| **Cenas (`Scene` v1.1)** | grafo em tabelas+JSONB (3 cenas seedadas) | autoritativo (seedado) | por versão de cena | ao mudar a cena/`sceneCompletenessLevel`/`publicabilityStatus` | log de mudança |
| **Claims/ClaimSets/Relationships** | grafo (arestas com `provenanceRef`) | autoritativo (seedado) | por versão de claim | ao mudar claim/`reviewStatus` | log de mudança |
| **Fontes/Citações** | relacional + `DatasetSnapshot` imutável | autoritativo (seedado) | snapshot imutável | nunca apaga snapshot | log de mudança |
| **Licenças (`LicenseProfile`/`LicenseStorageBinding`)** | relacional + binding por asset | autoritativo (seedado) | por versão de perfil | ao mudar licença | log de licença |
| **`MomentResult`** | cache com `inputVersionSet` | derivado | com versão dos insumos | ao mudar qualquer item do recorte | log de cache |
| **`MatchSet`/`MatchScore`** | relacional/documental | derivado (externo) | por versão | ao mudar insumo/perfil | `MatchingAuditTrail` + log técnico |
| **`PedagogicalOutput`** | relacional/documental | derivado (externo) | por versão (preserva forma; reidrata fonte/incerteza) | ao mudar `MatchSet`/cena referenciada | `OutputAuditTrail` + log técnico |
| **`ExperienceSession`/`NavigationState`** | armazenamento de sessão | externo, efêmero | não (descartável) | expira ao fim da sessão | `UXAuditTrail` + log de acesso |
| **`ExportPackage`** | object storage + registro de versão | derivado (com avisos) | imutável como registro de auditoria | invalidação operacional ≠ apagar o registro | log de exportação |
| **Logs (`TechnicalAuditTrail`)** | tabela append-only | técnico | append-only (imutável) | nunca apaga | é a própria auditoria |
| **Assets/tiles** | object storage (risco 0–1) + `isolated-license-store` (separado) | binários + metadados técnicos | por versão de asset | ao substituir asset | log de licença |

### 9.2 O que é autoritativo, derivado, simulado e seedado

```txt
autoritativo (única "verdade")  = grafo do KC + proveniência (Source/Citation/DatasetSnapshot) + LicenseProfile
                                  — no MVP, SEEDADO MANUALMENTE a partir das 3 cenas-gabarito já aprovadas
derivado (reconstruível)        = índices (temporal/geoespacial/textual), caches (MomentResult/Scene),
                                  MatchSet, PedagogicalOutput, ExportPackage
externo/descartável             = PlanningProfile, ExperienceSession, NavigationState, UXAuditTrail
simulado (apenas demonstração)  = usuários de teste (sem PII real), papéis de demonstração,
                                  eventuais placeholders de asset rotulados como tais
exige ingestão real (Etapa 13)  = qualquer Claim/Source/Scene NOVO; assets reais que substituam placeholders;
                                  confirmação por asset em escala; séries de dados; novas regiões/períodos
```

**[NORMATIVO]:** o seed das 3 cenas é **autoritativo dentro do MVP** apenas porque já passou pela curadoria das Etapas 4D/4E/4G; ele **não** é ingestão e **não** autoriza criar conteúdo novo nesta etapa. Tudo que for além das 3 cenas é da Etapa 13.

### 9.3 Versionamento

**[RECOMENDADO]** versionar por conteúdo (cada `Claim`/`Scene`/`Source` tem versão) e separar **versão de conteúdo** de **versão de renderização** (a forma cacheia; o status epistêmico se reconfere) — E11 §5. O `DatasetSnapshot` por trás de cada `Citation` é **imutável**. O `canonicalTimeScalar` é derivado com datum fixo (E3Z) e **nunca** apaga o `sourceTimeBasis` nativo (invariante 29).

### 9.4 Invalidação

**[NORMATIVO]** a `InvalidationRule` dispara ao mudar `Claim`/`Source`/`LicenseProfile`/`reviewStatus`/`publicabilityStatus`/perfil. No MVP, a regra crítica é: marcar um item seedado como `rejected`/`pending` **invalida imediatamente** todo derivado que o exibia como fato (cache, `MomentResult`, `Output`) — testável (Seção 13, T-CACHE/T-PENDING). Invalidar o cache **operacional** nunca apaga o **registro de auditoria** do que foi servido (E11 §5.6).

### 9.5 Auditoria

**[NORMATIVO]** a `TechnicalAuditTrail` registra, por **referência e versão** (nunca conteúdo sensível/PII em claro), qual versão foi servida e por qual caminho (autoritativo × cache). A cadeia **artefato → bloco → cena/momento → claim → fonte → licença** é preservada em todos os modos do MVP (E11 §12.4).

### 9.6 Reprodutibilidade do material exportado

**[NORMATIVO]** todo `ExportPackage` do MVP carrega a versão do `PedagogicalOutput`, as versões dos `Claim`/`Scene`/`MomentResult` referenciados, os `DatasetSnapshot` por trás das `Citation`, os avisos vigentes e a atribuição de licença, mais data/assinatura — para que uma revisão futura reconstrua exatamente o que foi mostrado (E11 §5.8).

### 9.7 Como o MVP impede confundir seed com ingestão

**[NORMATIVO]** três barreiras: **(1)** o seed é marcado com um `DatasetSnapshot` de origem "seed-MVP-cenas-gabarito" e exibido como tal na visão de curadoria; **(2)** o caminho de escrita do `KnowledgeCoreService` aceita **apenas** o seed fechado (a porta da ingestão real fica desligada no MVP — E13 a liga **através** do portão da Etapa 1.1); **(3)** a interface e a documentação do MVP declaram que o conteúdo é um corpus de demonstração de três cenas, **não** um catálogo curado em escala (Seção 1.5; R-MVP-06/R-MVP-07).

---

## 10. UX e experiência mínima (Tarefa 10)

### 10.1 O que entra visualmente

| Elemento | Estatuto | Comportamento mínimo no MVP |
|---|---|---|
| **`TimelineView` multiescala** | MUST | navegação nos 3 regimes (histórico/Ma/Ga) no eixo canônico; `sourceTimeBasis` visível; ligada ao globo |
| **`Globe3DView`** | MUST (quando há WebGL) | globo com marcadores por `visibilityClass`; paleoposição rotulada (K-Pg); degrada para 2D |
| **`Map2DView`** | MUST | mapa com base **Natural Earth (PD)**; piso garantido sem GPU |
| **`StaticFallbackView`** | MUST | imagem + equivalente textual; piso de acesso (a11y/sem rede/impressão) |
| **`ProjectorModeView`** | MUST | alto contraste, baixa densidade, rótulos legíveis à distância |
| **`DossierPanel`** | MUST | dossiê "como sabemos disso" das 3 cenas |
| **`SourceEvidencePanel`** | MUST | fonte/evidência por claim; **cita, jamais reproduz** (1.1) |
| **`EpistemicLabelView`** | MUST | rótulo de `claimType`/`confidenceLevel`/`evidenceLevel` sempre que há claim |
| **`UncertaintyLegend`** | MUST | leitura da incerteza (faixa ≠ lados) |
| **`AnachronismNotice`** | MUST | aviso de anacronismo (ex.: "México" em 66 Ma; nações atuais em 1789) |
| **`EquivalenceWarningNotice`** | MUST | aviso anti-falsa-equivalência (negacionismo rotulado-rejeitado fora do `ClaimSet`) |
| **`MediationControl`** | MUST | mediação obrigatória para conteúdo sensível conforme faixa |
| **`AccessibilityControl`** | MUST | teclado, foco visível, contraste, movimento reduzido, redundância não-cromática |
| **`RoleSelector`** (seletor de papel) | MUST | alternar professor/estudante (modo controlado, sem PII) |
| **`ExportPackage` (vista)** | MUST | acionar exportação/projeção preservando fonte/incerteza/atribuição |
| **`ComparisonView`** | SHOULD | A×B / antes-depois sobre `weightedClaimSets` (K-Pg), confiança decaindo, sem falsa simetria |
| **`FreeExplorationView`** | MUST | "o que acontecia neste momento?" sem grade, com filtro de adequação |

A escada de degradação do MVP segue a `ViewDegradationLadder`: **`Globe3DView` → `Map2DView` → `StaticFallbackView`**, com `ProjectorModeView` como variação de contexto. **[NORMATIVO]:** cada degrau preserva fonte, incerteza, natureza do dado, mediação e atribuição (invariante 22).

### 10.2 O que **não** entra na UX do MVP

```txt
OUT (UX) = {
  design final de alta fidelidade completo,
  todos os modos da Etapa 10 (ex.: guidedExplorationMode, dossierMode dedicado),
  edição rica de artefatos (ArtifactEditor completo),
  colaboração multiusuário,
  offline completo (apenas StaticFallbackView no MVP-MUST),
  analytics de uso / telemetria individual,
  animações elaboradas que sugiram determinismo na cascata (visualizationNotes proíbem)
}
```

### 10.3 Regra de honestidade visual

**[NORMATIVO]** a UX **mostra** a honestidade epistêmica; nunca a esconde por estética. `visibleEpistemicLabels` nunca é vazio quando há claim; `activeGatingNotices` nunca rebaixa `pending`/`legal-review`/`rejected` a fato; `accessibilityProfile` sempre existe; o conjunto exibido sempre respeita `viewerRole`/`visibilityClass`/`studentFacingMode` (E10 §4.1; R-MVP-05).

---

## 11. Segurança, privacidade e papéis no MVP (Tarefa 11)

### 11.1 Papéis mínimos

```txt
includedRoles = {
  teacher,            # aparato completo; cria PlanningProfile; edita FORMA; aprova na sessão; vê teacherOnly/mediação
  student,            # face do aluno por faixa; nunca teacherOnly/internalReviewOnly/pending/sensível-sem-mediação
  curator | admin,    # vê o seed e o gatingReason; opera o seed manual fechado; NÃO opera PII de aluno
  publicViewer        # conteúdo público publicável (exploração livre); nada restrito
}
```

S�o um subconjunto dos 11 papéis da Etapa 11 §7.2, suficiente para os quatro fluxos. Papéis de rede/secretaria, `guardianOrResponsibleAdult` e `offlineViewer` ficam **fora** do MVP-MUST.

### 11.2 Login: modo controlado, sem PII real

**[RECOMENDADO]** o MVP usa **autenticação em modo controlado** por papel (contas de demonstração), **sem coletar dados pessoais reais de alunos**. SSO/OAuth e cadastro real são **[PENDÊNCIA]** da Etapa 14 (E11 §7, R-14). **[NORMATIVO]:** mesmo no modo controlado, a sessão respeita papel e `visibilityClass` (invariante 15).

### 11.3 Bloqueio de `teacherOnly` e de `pending`/`legal-review`/`rejected`

**[NORMATIVO]** dois bloqueios duros, impostos por ABAC **na borda** (nunca confiando no cliente para esconder): **(a)** sessão de `student`/`publicViewer` **nunca** recebe item `teacherOnly`/`internalReviewOnly`, mesmo referenciado por um artefato; **(b)** item `pending`/`legal-review`/`rejected` **nunca** é servido como fato a papel não-curatorial, nem cacheado/indexado/exportado como fato (invariantes 9/15; R-MVP-03/R-MVP-17). O `gatingReason` é exibível à curadoria; ao público, o item **não existe como fato**.

### 11.4 Como evitar dados pessoais reais de alunos

**[NORMATIVO]** **menores exigem minimização máxima de dados**: o MVP opera **sem PII real de aluno**; `PlanningProfile` é sobre turma/série/disciplina; `ExperienceSession` é efêmera; identidade × sessão × pedagógico ficam **separados** e nenhum cruza com o outro; nada de perfilamento, publicidade ou rastreamento (invariantes 12/21; LGPD Art. 14; ECA). **[RECOMENDADO]** pseudônimos de sessão de turma, se necessário distinguir sessões, com a tabela de correspondência (se existir) isolada — **[PENDÊNCIA]** de detalhe na Etapa 14.

### 11.5 Auditoria de acesso

**[NORMATIVO]** todo acesso a conteúdo restrito e toda decisão de autorização sensível são registrados na `TechnicalAuditTrail` com `dataMinimizationClass` (quem-papel, quando, qual classe de recurso — sem conteúdo sensível/PII em claro); acesso **negado** também é registrado (detecção de tentativa indevida) — invariante 21; R-MVP-20.

### 11.6 Exportação e papéis

**[NORMATIVO]** a exportação respeita o papel: o `ExportPackage` de um `teacher` pode conter aparato de professor; um pacote destinado ao aluno **não** carrega `teacherOnly`/`pending`; e nenhum pacote captura dado pessoal de aluno (E10 §10.3; R-MVP-25/R-MVP-21).

### 11.7 RBAC + ABAC simplificado

**[NORMATIVO]** a autorização combina **RBAC** (o papel define o conjunto base) com **ABAC** (atributos refinam: faixa, `SchoolUseMode`/`usageScenario`, `visibilityClass`, `reviewStatus`/`publicabilityStatus`, online/estático). "Negar vence em conflito." O ponto de decisão é **único** e vale para vista, cache, busca, exportação e degrau estático (invariante 15; E11 §7.1).

---

## 12. Licenciamento, assets e fontes no MVP (Tarefa 12)

### 12.1 Política mínima de licenças

**[NORMATIVO]** no MVP público:

```txt
licença (MVP) = {
  usar SOMENTE fontes/assets risco 0–1 como EXPRESSÃO,
  proibir qualquer expressão NC (risco ≥ 4),
  bloquear conteúdo proprietário sem contrato (risco 5),
  isolar fisicamente qualquer SA/ODbL (risco 3) no isolated-license-store, se usado,
  registrar LicenseProfile + LicenseStorageBinding por asset,
  registrar atribuição (attributionText) onde a licença exige,
  confirmar licença por asset (perAssetConfirmed) antes de servir risco 2,
  exportar APENAS o que a licença permite,
  separar o FATO recodificado (com fonte própria) da EXPRESSÃO licenciada
}
```

Isto instancia a matriz `licenseRiskLevel 0–5` da Etapa 11 §9.11 e os invariantes 17/18/19/27.

### 12.2 Decisão-chave: mapa-base de domínio público

**[RECOMENDADO/NORMATIVO no efeito]** o MVP usa **Natural Earth (PD, risco 0)** como base do `Map2DView`/`Globe3DView`, **em vez do OpenStreetMap (risco 3, ShareAlike/ODbL)**. **Por quê:** mantém o MVP público inteiramente em risco 0–1, evitando as obrigações de *share-alike*/atribuição do OSM no primeiro corte e o risco de contaminar o núcleo. OSM, se entrar, entra **isolado** no `isolated-license-store`, com plano de atribuição/SA — **[PENDÊNCIA]** posterior. Paleogeografia (GPlates/EarthByte, **CC BY = risco 1**) é usada **com atribuição** e rotulada como **reconstrução modelada** (`paleoPositionPolicy`); **Deep Time Maps (NC) não entra** como expressão (invariantes 18/19; E11 R-10).

### 12.3 Quais assets entram e seus estatutos

| Asset | Origem/estatuto | Papel no MVP |
|---|---|---|
| Base cartográfica | Natural Earth (PD, risco 0) | base do 2D/3D |
| Reconstrução paleogeográfica (K-Pg/GOE) | GPlates/EarthByte (CC BY, risco 1) | overlay **rotulado como reconstrução**, com atribuição |
| Dados/fatos das 3 cenas | recodificados de fontes A/B (fato, não expressão) | claims com fonte própria |
| Ilustrações/diagramas didáticos | **representações próprias** (risco 0) | dossiê/timeline; nunca cópia de fonte |
| Imagens de catálogo restrito | placeholders rotulados **ou** ausentes | substituídos por representação própria; **confirmação por asset** fica para a Etapa 13 |
| Qualquer asset NC/proprietário | **bloqueado** como expressão | apenas o fato recodificado, se houver fonte própria |

**[NORMATIVO]:** nenhum asset entra **órfão de licença**; todo asset tem `LicenseProfile`/`LicenseStorageBinding`. Placeholders são **rotulados** e listados como pendência de substituição na Etapa 13 (R-MVP-08).

### 12.4 Como o MVP mostra fonte/licença ao usuário

**[RECOMENDADO]** uma vista "fonte/licença deste conteúdo" acessível a partir do `SourceEvidencePanel` e do `ExportPackage`, exibindo `Source`/`Citation`/atribuição e a natureza do asset (`natureLabel`: fotografia/mapa/gráfico/reconstrução/simulação/representação artística/aproximação didática). **[NORMATIVO]:** citar **nunca** é reproduzir (1.1); o painel cita e atribui, não republica material licenciado.

### 12.5 O que exige substituição na Etapa 13

```txt
substituir na Etapa 13 = {
  placeholders por assets reais com confirmação por asset (perAssetConfirmed),
  qualquer base/overlay que se queira em risco 2+ (com licença confirmada e, se SA/ODbL, isolada),
  séries de dados reais (ex.: clima) que uma 4ª cena venha a exigir,
  expansão de fontes além das 3 cenas — sempre ATRAVÉS do portão da Etapa 1.1
}
```

---

## 13. Testes, QA e critérios de aceite (Tarefa 13)

Matriz de testes do MVP. Cada teste: objetivo, procedimento conceitual, resultado esperado, risco coberto. (Os códigos `T-*` foram introduzidos na Seção 2.)

| Teste | Objetivo | Procedimento conceitual | Resultado esperado | Risco coberto |
|---|---|---|---|---|
| **T-FACTUAL (cadeia)** | provar P4 | de um `OutputArtifact` exportado, descer a `OutputSectionBlock`→`Scene`/`MomentResult`→`Claim`→`Source`→`LicenseProfile` | cadeia íntegra; nenhum `Claim` sem `provenanceRef` | R-MVP-08/10 |
| **T-PROF×ALUNO** | provar adequação por papel | abrir as 3 cenas como `teacher` e como `student` | `student` não vê nenhum `teacherOnly`/`pending`/sensível-sem-mediação | R-MVP-17 |
| **T-PENDING** | invariante de exibição | marcar (no seed) um item como `pending` e consultá-lo como `student`/`publicViewer` e via cache/busca/export | o item não aparece como fato em nenhum caminho | R-MVP-03 |
| **T-TEACHERONLY** | bloqueio de borda | referenciar um item `teacherOnly` num artefato visto pelo aluno | o item é filtrado antes de servir/cachear/empacotar | R-MVP-17 |
| **T-EXPORT** | exportação com proveniência | exportar plano/dossiê/material | `ExportPackage` carrega citação+incerteza+mediação+atribuição+nota anti-homologação | R-MVP-10/16/25 |
| **T-NC** | bloqueio de NC | tentar exportar/servir um asset risco ≥ 4 como expressão | bloqueado e logado | R-MVP-25 |
| **T-SA** | isolamento SA/ODbL | inspecionar o *store* do núcleo | nenhum asset SA/ODbL no `core-store`/`media-store`; isolamento verificável | R-MVP-24 |
| **T-CACHE** | cache não é verdade | invalidar `MomentResult`/`Scene` ao mudar versão/`reviewStatus` | derivado vencido não é servido como fato | R-MVP-01 |
| **T-DERIVADO** | reconstrutibilidade | apagar e reconstruir índices/caches a partir do seed | nenhum `Claim` muda | R-MVP-02/E11-26 |
| **T-DEGRADA** | piso epistêmico na degradação | forçar 2D e estático (sem WebGL) | mesmos rótulos epistêmicos do 3D; navegação temporal sobrevive | R-MVP-18/19 |
| **T-A11Y** | acessibilidade mínima | navegar por teclado; ler equivalentes textuais; checar contraste/redundância | toda vista acessível; cor nunca é o único canal | R-MVP-09 |
| **T-PII** | ausência de PII de aluno | inspecionar todos os *stores* e o KC | nenhum campo de identidade de aluno; KC sem PII | R-MVP-21 |
| **T-LOG (cache não é verdade)** | minimização + versão servida | amostrar `TechnicalAuditTrail` | versão servida registrada; sem PII de menor; classe de minimização presente | R-MVP-21/01 |
| **T-BUSCA (busca não é verdade)** | busca devolve ponteiros | buscar um termo e abrir o resultado | resultado reidrata `claimType`/`confidence`; respeita `visibilityClass`; nunca "texto pelado" | R-MVP-22 |
| **T-SCORE (score não é verdade)** | relevância ≠ confiança | comparar dois `MatchScore` sobre o mesmo claim | `confidenceLevel`/`reviewStatus` do claim inalterados | R-MVP-13 |
| **T-SIM-1789 (simultaneidade)** | provar P2 (histórico) | acionar a função em 1789 | retorna simultâneos centrais/contextuais (Brasil/EUA/Qing…) com `ModernCorrespondence` rotulada; sem anacronismo de nação | R-MVP-28 |
| **T-GOE (incerteza científica)** | tempo profundo sem evento | abrir GOE | **zero Event**; States/Process dominantes; `UncertaintyProfile` alto; paleogeografia rotulada como reconstrução | R-MVP-29 |
| **T-KPG (cascata + peso)** | cena híbrida | abrir K-Pg | `triggerItem`→`cascadeStructure` com `confidenceByStage` decaindo; `weightedClaimSets` (impacto **primário** ≫ Deccan **secundário**; negacionismo **rotulado-rejeitado** fora do `ClaimSet`); `paleoPositionPolicy` ativa | R-MVP-15/30 |
| **T-SYNC** | sincronização sem versão divergente | mover o tempo e observar o globo | timeline e globo na mesma versão de conteúdo | E11-28 |
| **T-DATUM** | `sourceTimeBasis` preservado | inspecionar itens das 3 cenas | tempo nativo (dia/Ga/Ma) preservado ao lado do `canonicalTimeScalar` | E11-29 |
| **T-FRONTEIRA/T-API** | escrita indevida bloqueada | tentar escrever no KC a partir de um módulo a montante | negado e logado; só o seed/pipeline escreve | R-MVP-16 |
| **T-HOMOLOGA** | alinhamento ≠ homologação | abrir um `BNCCMapping` e exportar | exibido como **alinhamento `pending`**; nota anti-homologação no viewer e no export | R-MVP-16 |

**[NORMATIVO]:** estes testes são **critérios de aceite do MVP**: o MVP só é considerado "funcionando" quando todos passam. Falha em qualquer teste de invariante (T-PENDING, T-NC, T-SA, T-PII, T-CACHE, T-BUSCA, T-SCORE, T-EXPORT, T-A11Y, T-FRONTEIRA) **bloqueia** a entrega, independentemente das métricas funcionais.

---

## 14. Riscos do MVP e mitigação (Tarefa 14)

Pelo menos **31 riscos específicos do MVP** (códigos `R-MVP-01`…`R-MVP-31`), mais concretos que os da Etapa 11 e cruzados com ela onde aplicável. Cada risco tem mitigação.

| Código | Risco do MVP | Mitigação |
|---|---|---|
| **R-MVP-01** | Cache servir item revogado/`rejected` como fato | `CacheEntry` com `inputVersionSet`; invalidação imediata em `reviewStatusChanged` (T-CACHE; E11 invariante 2) |
| **R-MVP-02** | Índice/cache simplificado virar "fonte" | derivados reconstruíveis, `carriesProvenance=false`; reidratação obrigatória (T-DERIVADO; invariante 26) |
| **R-MVP-03** | Vazamento de `pending`/`teacherOnly`/`hiddenItems` | ABAC na borda; invariante de exibição em vista/cache/busca/export (T-PENDING/T-TEACHERONLY; invariantes 9/15) |
| **R-MVP-04** | 3D atrasar todo o MVP | 3D é MUST **só** quando há WebGL; piso garantido é 2D/estático; timeline própria desacoplada do globo (Seção 7.3) |
| **R-MVP-05** | UX bonita esconder incerteza | regra de honestidade visual (Seção 10.3); rótulos/avisos sempre presentes; T-A11Y/T-FACTUAL (invariante 14) |
| **R-MVP-06** | *Dataset* manual parecer ingestão real | seed marcado com `DatasetSnapshot` "seed-MVP"; porta de ingestão desligada; aviso na interface (Seção 9.7) |
| **R-MVP-07** | Seed de cena virar fonte factual nova | o seed é apenas as 3 cenas já curadas; nenhum `Claim` novo; caminho de escrita fechado (Seções 4.4/9.2) |
| **R-MVP-08** | Placeholders virarem produto final | placeholders rotulados e listados como pendência de substituição na Etapa 13 (Seção 12.3) |
| **R-MVP-09** | Falta de acessibilidade | a11y é MUST: equivalente textual, teclado, foco, contraste, redundância não-cromática (T-A11Y; invariante 23) |
| **R-MVP-10** | Exportação sem fonte/incerteza | `ExportPackagingService` embute citação+incerteza+mediação+atribuição (T-EXPORT; invariantes 10/16) |
| **R-MVP-11** | Licença mal registrada | `LicenseProfile`/`LicenseStorageBinding` por asset; confirmação por asset para risco 2 (Seção 12; invariante 17) |
| **R-MVP-12** | Output suprimir citação/incerteza ("forma muda fato também") | `forma muda; fato não`: o mesmo claim mantém `claimType`/`confidence`/fonte em todos os artefatos (T-FORMA; invariante 14) |
| **R-MVP-13** | `MatchScore` virar critério de verdade | `score não é verdade`; Matching não altera claim/`reviewStatus` (T-SCORE; invariante 6) |
| **R-MVP-14** | Login complexo demais (atrasa/insegura) | autenticação em **modo controlado** por papel, sem PII real; SSO é `[PENDÊNCIA]` da Etapa 14 (Seção 11.2) |
| **R-MVP-15** | Falsa equivalência em `weightedClaimSets` | peso assimétrico explícito; negacionismo `rotulado-rejeitado` fora do `ClaimSet` (T-KPG; E5/3.1) |
| **R-MVP-16** | API/monólito permitir escrita indevida no núcleo | fronteiras de escrita preservadas mesmo no monólito; único ponto de escrita; alinhamento ≠ homologação (T-FRONTEIRA/T-API/T-HOMOLOGA; invariante 20) |
| **R-MVP-17** | Estudante ver conteúdo sensível/`teacherOnly` sem mediação | `visibilityClass`/`SchoolUseMode`/`MediationControl` por faixa; bloqueio de borda (T-PROF×ALUNO/T-TEACHERONLY; invariante 15) |
| **R-MVP-18** | Degradação remover o piso epistêmico | a `ViewDegradationLadder` mantém rótulos em 2D/estático/projetor (T-DEGRADA; invariante 22) |
| **R-MVP-19** | Offline incluído cedo demais | offline **fora** do MUST; piso de "sem rede" é o `StaticFallbackView`; `OfflinePackage` só como COULD, versionado/assinado (Seção 6; invariante 11) |
| **R-MVP-20** | Ausência de auditoria | `TechnicalAuditTrail` append-only; logs de acesso/mudança/exportação/cache/licença; acesso negado registrado (Seção 11.5; invariante 16) |
| **R-MVP-21** | Coleta acidental de PII de aluno | zero PII real; identidade × sessão × pedagógico separados; logs minimizados (T-PII/T-LOG; invariantes 12/21) |
| **R-MVP-22** | Busca semântica prematura / busca "responder fato" | índice vetorial **fora** do MVP; busca textual devolve ponteiros e reidrata rótulos (T-BUSCA; invariante 3) |
| **R-MVP-23** | Adotar índice vetorial sem necessidade | desnecessário para 3 cenas; decisão de adotar fica para E13/E14 como `DerivedIndex` `carriesProvenance=false` (Seção 7.3) |
| **R-MVP-24** | Uso indevido de mapa/asset (SA/ODbL no núcleo) | mapa-base PD (Natural Earth); SA/ODbL isolado; nenhum asset órfão de licença (T-SA; invariantes 17/18/27) |
| **R-MVP-25** | Exportar/projetar expressão NC/SA fora do permitido | revalidação de licença na exportação; bloqueio + log; só o fato recodificado entra (T-NC/T-EXPORT; invariantes 10/19) |
| **R-MVP-26** | Professor achar que é currículo oficial | rótulo "recurso educacional digital complementar"; nota anti-homologação no viewer/export (Seção 5.1; E6) |
| **R-MVP-27** | Stack dependente demais de fornecedor (lock-in) | tecnologias `[RECOMENDADO]`/`[ALTERNATIVA]` sobre propriedade `[NORMATIVO]`; formatos abertos; PostGIS/MapLibre/Cesium substituíveis (invariante 24; E11 R-21) |
| **R-MVP-28** | Escolher stack que dificulte o grafo futuro | grafo em tabelas+JSONB com `provenanceRef` por aresta **preserva** a propriedade "proveniência por aresta"; migração para grafo dedicado prevista (Seção 7.3; E11 R-33) |
| **R-MVP-29** | Cenas-gabarito não bastarem para teste pedagógico | as 3 cenas cobrem 3 regimes + 3 perfis de risco; teste qualitativo com professores valida a leitura (Seções 4.2/3.2; R-MVP-31) |
| **R-MVP-30** | MVP fraco demais para provar a tese | os 4 fluxos cobrem P1–P10; o diferencial (simultaneidade + rastreabilidade + 3 regimes) é o foco do esforço (Seções 3/5/8) |
| **R-MVP-31** | Falta de validação com professor / confundir demo comercial com MVP técnico-pedagógico | teste qualitativo com professores de teste (sem PII); a entrega é técnico-pedagógica verificável, não encenação comercial (Seções 1.5/3.2) |

**[NORMATIVO]:** nenhuma mitigação "resolve" um risco **relaxando** o invariante que o contém (E11 §14, R-26). Riscos da Etapa 11 (R-01…R-37) permanecem herdados; estes 31 são os **específicos do recorte de MVP**.

---

## 15. Encerramento e handoff para as Etapas 13 e 14 (Tarefa 15)

### 15.1 O que o MVP entrega

O `MVPRelease` (Seção 1) entrega um **recorte mínimo viável verificável**: as **três cenas-gabarito** seedadas (1789, GOE, K-Pg) cobrindo os três regimes de tempo; **quatro fluxos** (professor com a cadeia Planning→Matching→Output→UX; estudante; exploração livre; exportação/projetor/estático); **quinze serviços priorizados** (2 implementados, 8 implementados-mínimos, 3 simplificados, 1 fora/stub) com **fronteiras de escrita preservadas** mesmo no monólito modular; uma **persistência** que separa autoritativo (grafo seedado com proveniência por aresta) de derivado (índices/caches/MatchSet/Output/Export) e de externo/efêmero (Planning/Session), com versionamento, invalidação e auditoria; uma **UX mínima** com timeline multiescala, globo 3D, mapa 2D com base PD, degrau estático, projetor, dossiê, painel de fonte/evidência e todos os rótulos/avisos epistêmicos; um **modelo de segurança/privacidade** RBAC+ABAC com quatro papéis, modo controlado sem PII real de aluno, bloqueio de `teacherOnly`/`pending` e auditoria minimizada; uma **política de licenças** que usa só risco 0–1 como expressão, isola SA/ODbL, bloqueia NC, registra licença/atribuição por asset e exporta apenas o permitido; uma **matriz de testes** que é também o critério de aceite; e **31 riscos de MVP** com mitigação. Tudo isso **sem** escrever código, criar banco real, rodar ingestão, criar conteúdo novo, alterar as cenas-gabarito, mapear BNCC em massa, usar PII real ou relaxar qualquer invariante da Etapa 11.

### 15.2 O que o MVP **não** entrega

Não entrega produto escolar pronto; não entrega ingestão/povoamento real (Etapa 13); não entrega operação contínua, governança, *analytics* operacional, LMS, retenção/descarte, DPIA, consentimento/controle escolar nem laudo de acessibilidade formal (Etapa 14); não entrega offline completo, busca semântica, quiz/avaliação/rubrica completos, edição rica de artefatos nem colaboração multiusuário; não entrega mapeamento BNCC em massa nem qualquer selo curricular; e não entrega homologação MEC/PNLD.

### 15.3 Decisões técnicas tomadas × provisórias

```txt
TOMADAS (recorte do MVP, sob estatuto declarado):
  - monólito modular com fronteiras de escrita preservadas               [RECOMENDADO]
  - grafo do KC em tabelas+JSONB com provenanceRef por aresta             [RECOMENDADO]
  - PostgreSQL + PostGIS (relacional + geoespacial)                       [RECOMENDADO]
  - mapa-base Natural Earth (PD); OSM só isolado e depois                 [RECOMENDADO/efeito NORMATIVO de isolamento]
  - globo Cesium/3D-Tiles-classe + MapLibre 2D + estático server-side     [RECOMENDADO]
  - timeline própria sobre Canvas/SVG                                     [RECOMENDADO]
  - busca textual (tsvector) devolvendo ponteiros; SEM índice vetorial    [RECOMENDADO / fora]
  - cache de MomentResult/Scene com inputVersionSet                       [RECOMENDADO]
  - autenticação em modo controlado, sem PII real                         [RECOMENDADO]
  - offline fora do MUST; piso de "sem rede" = StaticFallbackView         [RECOMENDADO]

PROVISÓRIAS / A DECIDIR DEPOIS:
  - escolha final entre TypeScript/Node e Python/FastAPI no backend       [PENDÊNCIA E12-exec/E14]
  - migração para grafo dedicado (RDF*/property graph)                    [PENDÊNCIA E13/E14]
  - adoção (ou não) de índice vetorial como DerivedIndex                  [PENDÊNCIA E13/E14]
  - SSO/OAuth e cadastro real                                             [PENDÊNCIA E14]
  - OfflinePackage assinado/validade como entrega                         [PENDÊNCIA E12-iteração/E14]
  - formato final de ExportPackage/OfflinePackage                         [PENDÊNCIA E12-exec]
```

### 15.4 O que a Etapa 13 (ingestão/povoamento) deve receber

```txt
para a Etapa 13 = {
  o KnowledgeCoreService com UM caminho de escrita fechado, pronto para ligar o pipeline
    ATRAVÉS do portão de licenças da Etapa 1.1 (perAssetConfirmed, DatasetSnapshot, LicenseProfile),
  a marcação clara de seed-MVP × ingestão (Seção 9.7), para não confundir corpus de demonstração com povoamento,
  a lista de placeholders a substituir por assets reais com confirmação por asset (Seção 12.5),
  a propriedade "proveniência por aresta" a preservar ao migrar de tabelas+JSONB para grafo dedicado,
  o isolated-license-store já separado, para receber SA/ODbL/NC/proprietário sem contaminar o núcleo,
  os índices (temporal/geoespacial/textual) como derivados reconstruíveis a reindexar sobre o conteúdo real
}
```

### 15.5 O que a Etapa 14 (operação/governança/QA/analytics/LMS) deve receber

```txt
para a Etapa 14 = {
  os ganchos de auditoria (TechnicalAuditTrail) e de acessibilidade prontos para QA e laudo ASES,
  os papéis e o RBAC+ABAC a estender (rede/secretaria, guardian, offlineViewer, SSO/OAuth),
  a separação identidade × sessão × pedagógico a manter na integração LMS (conteúdo por referência, nunca PII no núcleo),
  a base para retenção/descarte, consentimento/controle escolar e DPIA (princípios fixados; prazos a definir),
  a base para analytics OPERACIONAL agregado/pseudonimizado (telemetria individual continua proibida),
  o orçamento de desempenho e a degradação como linha de base para escala e custo,
  a decisão sobre PNLD/compra pública e validação escolar/jurídica/comercial
}
```

### 15.6 Critérios que autorizam avançar após o MVP

**[NORMATIVO]** avança-se para a Etapa 13 quando **todos** os testes de invariante da Seção 13 passam (T-PENDING, T-NC, T-SA, T-PII, T-CACHE, T-BUSCA, T-SCORE, T-EXPORT, T-A11Y, T-FRONTEIRA) **e** os quatro fluxos demonstram P1–P10 sobre as três cenas, **e** o teste qualitativo com professores confirma que o diferencial é reconhecível sem confundir o MVP com currículo oficial.

### 15.7 Critérios que bloqueiam o avanço

**[NORMATIVO]** bloqueia-se o avanço se: qualquer item `pending`/`teacherOnly`/`hiddenItems` vazar como fato; qualquer expressão NC/SA for servida/exportada indevidamente; qualquer PII real de aluno for coletada; o cache/busca/score for tratado como verdade; a degradação remover o piso epistêmico; a acessibilidade falhar; ou o seed for confundido com ingestão real.

### 15.8 Pendências a carregar

```txt
pendências (E12 → adiante) = {
  resíduo curatorial herdado (E6/E8/E9): BNCCMapping/CurricularAlignment seguem `pending`;
    o MVP só EXIBE como alinhamento e respeita o reviewStatus, sem resolvê-los,
  datum do eixo temporal (E3Z) confirmado e aplicado às 3 cenas no mesmo eixo,
  escolha final de backend, grafo dedicado, índice vetorial, SSO, formato de pacote (Seção 15.3),
  OfflinePackage como entrega (se priorizado),
  substituição de placeholders e confirmação por asset (E13),
  retenção/descarte, DPIA, consentimento, analytics agregado, LMS e laudo ASES (E14)
}
```

### 15.9 Handoff

Com a **Etapa 12 (v1.0)** aprovada, a construção do MVP pode ser executada e, em seguida, a **Etapa 13 — Pipeline real de ingestão/povoamento** e a **Etapa 14 — Operação/governança/QA/analytics/LMS/validação** podem ser conduzidas, recebendo um recorte mínimo viável que **preserva** a soberania do Knowledge Core, a direção única de dependência, a proveniência até a fonte, o isolamento físico de licenças, o versionamento e a auditabilidade, a engenharia de privacidade e a minimização para menores, a degradação graciosa com piso epistêmico, a acessibilidade como fundação e a recusa de qualquer derivado (cache, índice, *embedding*, IA) como fonte de verdade.

---

*Documento de entrega da Etapa 12 (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8, 9, 10, 11). Define somente o recorte mínimo viável de produto (`MVPRelease`), a stack recomendada, a priorização dos quinze serviços, os quatro fluxos, a matriz de escopo, a persistência/versionamento, a UX mínima, a segurança/privacidade/papéis, a política de licenças, a matriz de testes/critérios de aceite, os trinta e um riscos de MVP e o handoff. Não escreve código, não implementa API real, não cria banco real, não faz ingestão real, não popula dados reais novos, não cria claim/cena/fonte novos, não altera as cenas-gabarito, não mapeia BNCC em massa, não cria analytics operacional, não cria LMS, não promete homologação MEC/PNLD, não usa dados pessoais reais de alunos e não relaxa nenhum invariante da Etapa 11. Próximas etapas, quando solicitadas: Etapa 13 — Pipeline real de ingestão/povoamento; Etapa 14 — Operação, governança, QA, analytics, LMS e validação escolar/jurídica/comercial.*
