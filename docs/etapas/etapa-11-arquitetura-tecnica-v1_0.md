# Etapa 11 — Arquitetura Técnica

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 11** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6, v1.0), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8, v1.0), a `PedagogicalOutputLayer` (Etapa 9, v1.0) e a `DesignUX3DLayer` (Etapa 10, v1.0) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura técnica de referência**. Define **como o sistema será sustentado tecnicamente** — domínios e *bounded contexts*, persistência, versionamento, snapshots e validade, APIs internas e contratos, segurança/permissões/papéis, engenharia de privacidade (LGPD/ECA), isolamento físico de licenças restritivas, cache/índices/invalidação, sustentação técnica da timeline/globo 3D/2D/estático/projetor/offline, observabilidade e auditoria técnica — preservando integralmente proveniência, licenças, publicabilidade, acessibilidade, degradação 3D→2D→estático→offline e rastreabilidade até `Claim`/`Source`. Conforme solicitado, esta etapa **não** escreve código de aplicação; **não** implementa API real; **não** cria banco real; **não** propõe MVP nem escolhe o recorte mínimo (Etapa 12); **não** faz ingestão nem povoa dados reais (Etapa 13); **não** define operação, governança, QA pedagógico, analytics operacional, LMS nem validação escolar/jurídica/comercial (Etapa 14); **não** cria `Claim`, `Source`, `Citation`, `Scene`, `ClaimSet`, `Relationship`, `MomentResult`, `MatchSet`, `PedagogicalOutput` nem qualquer conhecimento do núcleo; **não** mapeia BNCC em massa; **não** altera verdade factual; **não** altera `reviewStatus`, `publicabilityStatus`, `claimType`, `confidenceLevel`, `evidenceLevel`, `MatchScore`, `matchSetStatus`, `outputStatus` nem `sceneCompletenessLevel`; **não** promete homologação MEC nem aprovação PNLD; **não** trata IA como fonte factual; **não** usa dados pessoais reais de alunos; e **não** trata recurso complementar como currículo oficial. Ela **pode**, porém, fixar **decisões técnicas conceituais e arquiteturais**, inclusive tecnologias **candidatas/recomendadas**, sempre marcando o estatuto de cada decisão (ver convenção de estatuto, abaixo).

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Serviços/domínios técnicos também em `CamelCase` (terminados em `Service` quando são serviços de aplicação). Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O KC" = o Knowledge Core (Etapa 2). "A Compliance" = a `BrazilianEducationComplianceLayer` (Etapa 6). "O Planning" = a `TeacherSchoolPlanningLayer` (Etapa 7). "O Matching" = o `ContentMatchingEngine` (Etapa 8). "O Output" = a `PedagogicalOutputLayer` (Etapa 9). "A UX" = a `DesignUX3DLayer` (Etapa 10). "A arquitetura técnica" = a `TechnicalArchitectureLayer` definida na Seção 1.

> **Convenção de estatuto das decisões.** Para não confundir arquitetura com implementação, cada decisão técnica deste documento traz um estatuto explícito: **[NORMATIVO]** = vinculante, não pode ser violado por MVP/ingestão/operação sem reabrir a etapa; **[RECOMENDADO]** = opção preferida, mas substituível por equivalente que preserve os invariantes; **[ALTERNATIVA]** = opção aceitável citada para comparação; **[PENDÊNCIA]** = decisão deliberadamente adiada para a Etapa 12/13/14, registrada para ser carregada. Nomes de tecnologias concretas aparecem **sempre** como **[RECOMENDADO]** ou **[ALTERNATIVA]**, nunca como **[NORMATIVO]**: o normativo é a propriedade arquitetural (ex.: "o núcleo é um grafo com proveniência por aresta"), não o produto que a realiza.

> **Regra de fundação desta etapa.** A `TechnicalArchitectureLayer` é a **camada de infraestrutura, serviços e sustentação técnica** — externa a todo o conteúdo e a toda a experiência. Ela **materializa** o que as camadas conceituais decidiram, mas **nunca cria, edita ou origina conhecimento**, e **nunca inverte a soberania do Knowledge Core**. A direção única de dependência permanece a mesma de todas as etapas anteriores, agora com a ponta de proveniência explícita: **Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core → Sources/Provenance**. A infraestrutura técnica pode ter serviços, bancos, caches, índices, filas, *storage* de mídia, APIs e camadas de apresentação distribuídos como convier à engenharia, mas **nenhuma decisão técnica pode permitir que UX, Output, Matching, Planning ou Compliance escrevam fatos no núcleo sem o pipeline/curadoria apropriados**, e **nenhum mecanismo derivado (cache, índice textual, índice vetorial, *embedding*, resposta de IA) pode substituir o grafo de claims como fonte de verdade**. A pergunta que esta etapa responde: *"Qual arquitetura técnica sustenta este produto sem quebrar proveniência, licenças, versionamento, privacidade, publicabilidade, acessibilidade, degradação 3D→2D→estático→offline e rastreabilidade até claims/fontes?"*

---

## Sumário

1. Definição da `TechnicalArchitectureLayer`
2. Papel da arquitetura técnica na cadeia geral
3. Domínios técnicos e *bounded contexts*
4. Modelo de persistência e bancos de dados
5. Versionamento, snapshots, validade e reprodutibilidade
6. APIs internas e contratos entre camadas
7. Segurança, permissões e papéis
8. Privacidade, LGPD, ECA e minimização de dados
9. Licenças, isolamento físico e assets
10. Cache, busca, índices e invalidação
11. Arquitetura para timeline, globo 3D, 2D, estático, projetor e offline
12. Auditoria, logs, rastreabilidade e observabilidade
13. Invariantes técnicos da Etapa 11
14. Riscos técnicos, jurídicos, educacionais e operacionais
15. Encerramento e handoff para a Etapa 12

---

## 1. Definição da `TechnicalArchitectureLayer` (Tarefa 1)

### 1.1 O que ela é

A **`TechnicalArchitectureLayer`** é a **camada de sustentação técnica** do produto: o conjunto de domínios, serviços, mecanismos de persistência, índices, caches, filas, *storage* de mídia, contratos de API, controles de acesso, mecanismos de privacidade, isolamento de licenças e estratégias de renderização/offline que **fazem o sistema existir e operar** sobre a arquitetura conceitual acumulada nas Etapas 0–10. Ela é a resposta à pergunta *"com o que isto roda, onde os dados ficam, como as camadas conversam e como nada disso quebra as garantias epistêmicas, jurídicas e de acessibilidade já fixadas"*.

Ela cobre quatro responsabilidades estruturais: **(a) persistir** — guardar com segurança o conteúdo autoritativo (KC), os artefatos derivados (cenas, momentos, correspondências, saídas) e os dados externos (perfis, planejamento, sessões, pacotes); **(b) servir** — expor o conteúdo às camadas a montante por contratos de leitura/escrita disciplinados; **(c) proteger** — garantir papel, permissão, privacidade, minimização e isolamento de licença em toda leitura, escrita, cache e exportação; e **(d) sustentar a experiência** — viabilizar timeline, globo 3D, degradação 2D/estático/projetor/offline e exportação preservando o piso epistêmico em qualquer modo.

### 1.2 O que ela **não** é

A `TechnicalArchitectureLayer` **não é** fonte de verdade factual, não é autoridade epistêmica e não é lugar onde se decide o que é fato. Ela **não** decide *o que é verdade* (KC/Etapa 2), *o que é conforme* (Compliance/Etapa 6), *o que o professor quer* (Planning/Etapa 7), *o que entra e com qual papel* (Matching/Etapa 8), *em que forma pedagógica isso aparece* (Output/Etapa 9) nem *como a experiência é apresentada* (UX/Etapa 10). Ela também **não** é a implementação concreta (código, esquema físico de banco, *deploy*), que pertence ao MVP (Etapa 12) e à operação (Etapa 14): é a **planta arquitetural** que essas etapas instanciam. E ela **não** é um atalho: nenhum serviço, cache ou índice criado aqui pode "produzir" um claim, "promover" um item `pending`/`legal-review`/`rejected` a fato, ou "fundir" um dado ShareAlike/ODbL no núcleo factual.

### 1.3 Por que ela é externa ao Knowledge Core

O KC é um **núcleo soberano** (Etapa 2, §1.1/§10): não conhece, não importa e não depende de nada das camadas externas. A `TechnicalArchitectureLayer` precisa, por construção, conhecer e operar todas as camadas — inclusive o KC — para hospedá-las. Por isso ela é **necessariamente externa** ao núcleo: se a infraestrutura fosse parte do núcleo, a soberania do KC dependeria de decisões de banco, cache e API, e a inversão de dependência quebraria. A relação correta é a mesma das demais camadas externas: a infraestrutura **aponta para dentro** (hospeda, indexa, serve, protege o KC por identificadores estáveis), e o KC **nunca aponta para a infraestrutura**. Trocar o banco, o motor de busca ou a CDN não muda um único `Claim`.

### 1.4 Como ela sustenta as camadas anteriores

A arquitetura técnica oferece a cada camada conceitual **exatamente o serviço de que ela precisa, sem poder de reabertura**: ao KC, persistência de grafo com proveniência e versionamento; à Compliance, persistência de perfis/índices que apontam para o KC; ao Planning, persistência de planejamento descartável; ao Matching, índices temporais/geoespaciais/temáticos e um cache de `MatchSet`; ao Output, persistência de `PedagogicalOutput` versionado e auditável; à UX, sessões, vistas, cache de tiles/3D, pacotes offline e exportação. Cada serviço respeita os limites de escrita da camada que serve (Seção 2), e a direção de dependência é preservada em todas as leituras e escritas.

### 1.5 Por que ela não pode virar fonte de verdade factual

Três mecanismos já fixados a tornam estruturalmente incapaz de virar fonte: **(1) o modelo claim-first** (Etapa 2, §3) — verdade só existe como `Claim` tipado e fonteado a uma `Source` A/B; um registro de cache, um documento de índice ou um *embedding* não são `Claim` e não têm `provenanceRef`, logo não podem ser consultados como verdade; **(2) o portão de ingestão** (Etapa 1.1) — nada entra no núcleo sem proveniência, licença, tipo de claim, confiança e `reviewStatus`, e a infraestrutura não tem caminho de escrita que contorne o portão; **(3) o invariante de exibição** — item com `reviewStatus ∈ {pending, legal-review, rejected}` não é exibível nem consultável como fato, e a infraestrutura é obrigada a respeitar esse estado em toda leitura, cache e exportação. A regra **cache não é verdade** e a regra **busca/embedding não é verdade** são, nesta etapa, invariantes técnicos (Seção 13).

### 1.6 Como ela preserva a direção única de dependência

A preservação é feita por **separação de domínios com escrita assimétrica** (Seção 3) e por **contratos de API que distinguem leitura de escrita e nomeiam a camada dona** (Seção 6). Nenhum serviço a montante (Experience, Output, Matching, Planning, Compliance) tem permissão de escrita no `KnowledgeCoreService`; o único caminho de escrita no KC é o pipeline de curadoria/ingestão (Etapa 1.1/Etapa 13), governado pelo `SourceProvenanceService` e pelo `LicenseComplianceService`. Cache e índices são **derivados unidirecionais** do conteúdo autoritativo: o conteúdo escreve no índice, o índice nunca escreve no conteúdo.

### 1.7 Como ela separa arquitetura conceitual, implementação e operação

Esta etapa fixa **três planos distintos**, e só ocupa o primeiro:

```txt
PlanoArquitetural   = decisões de estrutura e propriedade (esta Etapa 11)
                      # domínios, contratos, invariantes, isolamento, versionamento conceitual
PlanoImplementacao  = escolha concreta e código (Etapa 12 — MVP; Etapa 13 — ingestão)
                      # esquema físico, bibliotecas finais, deploy, recorte mínimo
PlanoOperacional    = execução contínua e governança (Etapa 14)
                      # SRE, custo, escala, QA, analytics, LMS, validação escolar/jurídica/comercial
```

A `TechnicalArchitectureLayer` entrega o `PlanoArquitetural`: propriedades que **devem** valer (NORMATIVO), opções que **convém** adotar (RECOMENDADO/ALTERNATIVA) e decisões que **ficam** para depois (PENDÊNCIA). Ela nunca preenche os outros dois planos.

### 1.8 O que esta camada produz (entidades técnicas)

Entidades de **infraestrutura, externas e derivadas** (detalhadas adiante): a própria `TechnicalArchitectureLayer`; os domínios/serviços da Seção 3; os contratos `ApiContract` (Seção 6); o modelo de papéis `AuthorizationPolicy`/`AccessRole` (Seção 7); as abstrações de armazenamento `StoragePartition`/`IsolatedLicenseStore`/`LicenseStorageBinding` (Seções 4 e 9); os derivados `DerivedIndex`/`CacheEntry`/`InvalidationRule` (Seção 10); os artefatos de distribuição `OfflinePackage` e a sustentação técnica de `ExportPackage` (Seções 5, 9 e 11); e a trilha `TechnicalAuditTrail` (Seção 12). Nenhuma cria conteúdo; todas hospedam, servem, protegem, derivam ou registram o que veio das camadas conceituais. Cada entidade nova é justificada por **não duplicar** entidade anterior (ver Seção 3.17 e os blocos de cada seção).

---

## 2. Papel da arquitetura técnica na cadeia geral (Tarefa 2)

### 2.1 A cadeia completa, com a ponta de proveniência

```txt
Experience/UX  →  Output  →  Matching  →  Planning  →  Compliance  →  Knowledge Core  →  Sources/Provenance
   (E10)          (E9)        (E8)         (E7)          (E6)            (E2)              (E1/E1.1)
   apresenta      forma       seleção      intenção      conformidade    verdade           origem + licença
```

A seta é **única e invertida**: cada camada conhece e depende da seguinte à direita; nenhuma camada à direita conhece, importa ou depende da que está à sua esquerda. A `TechnicalArchitectureLayer` é **ortogonal** a essa cadeia: ela não ocupa uma posição na seta, ela **sustenta a seta inteira**. Tecnicamente, isso significa que a infraestrutura pode ler qualquer camada para servi-la, mas só pode **escrever** onde a camada dona a autoriza, e a escrita no KC só ocorre pelo pipeline de proveniência (a ponta `Sources/Provenance`).

### 2.2 Quem pode ler cada camada

A leitura é hierárquica e segue a seta (cada camada lê as que estão à sua direita, nunca à esquerda), com a infraestrutura mediando:

| Camada de origem da leitura | Pode ler (por REF, via serviço) | Nunca lê |
|---|---|---|
| **UX (E10)** | `PedagogicalOutput` (E9), `Scene` v1.1, `MomentResult` (E5), e — por intermédio destes — refs ao KC | dados de outras sessões/turmas; conteúdo não autorizado ao papel |
| **Output (E9)** | `MatchSet` (E8), `Scene`/`MomentResult`, `ComplianceProfile` (E6), `Claim`/`Source` (E2) por REF | a UX; sessões; dados pessoais de aluno |
| **Matching (E8)** | índices do KC (temporal/geoespacial/temático), `ComplianceProfile`, `PlanningProfile` (E7) | o Output; a UX; conteúdo `pending`/`rejected` como elegível |
| **Planning (E7)** | `ComplianceProfile`, vocabulário do KC para referência | o Matching; o Output; o conteúdo autoritativo como editor |
| **Compliance (E6)** | KC por REF, para indexar/anotar | Planning; Matching; Output; UX |
| **Knowledge Core (E2)** | `Sources`/`Provenance` (somente via pipeline) | qualquer camada externa (soberania) |

A infraestrutura **impõe** essa matriz no `IdentityAccessService` (Seção 7): uma sessão de UX não recebe credencial para consultar diretamente o `KnowledgeCoreService` por caminhos de escrita, e o `MatchingService` não recebe credencial para escrever em `Claim`.

### 2.3 Quem pode escrever, e quais escritas são proibidas

| Serviço escritor | Escreve (autoritativo ou derivado) | Proibido escrever |
|---|---|---|
| **Pipeline de ingestão/curadoria** (E13, via `SourceProvenanceService`/`LicenseComplianceService`) | `KnowledgeItem`, `Claim`, `ClaimSet`, `Relationship`, `Source`, `Citation`, `MediaAsset`, `MapAsset`, `GeometryVersion`, `DatasetSnapshot`, `ProvenanceMetadata`, `reviewStatus` | nada fora do KC e da governança de fonte |
| **`BrazilianComplianceService`** | `ComplianceProfile`, `BNCCMapping`, `CurricularAlignment`, `AllowedUseContext`, `SchoolUseMode`, `AgeSuitability`, `SensitiveContentRule`, `AccessibilityRequirement` (tudo apontando para o KC) | qualquer campo do KC; `Claim`; verdade factual |
| **`PlanningService`** | `PlanningProfile`, `usageScenario` (descartáveis, externos) | KC; Compliance; `MatchSet`; Output |
| **`MatchingService`** | `MatchSet`, `MatchScore`, `MatchingAuditTrail`, `matchSetStatus` | `Claim`; `AllowedUseContext`; `reviewStatus`; `publicabilityStatus` |
| **`PedagogicalOutputService`** | `PedagogicalOutput`, `OutputArtifact`, `OutputSectionBlock`, `OutputCitationBundle`, `OutputComplianceSummary`, `OutputConstraintWarning`, `OutputAuditTrail`, `OutputRevisionNote`, `outputStatus` | `Claim`; `MatchScore`; `ComplianceProfile`; `reviewStatus` |
| **`ExperienceSessionService`** | `ExperienceSession`, `NavigationState`, estados de vista, `UXAuditTrail`, status de `ApprovalWorkflow` da sessão | `PedagogicalOutput` (conteúdo); `MatchSet`; KC; Compliance |
| **`CacheInvalidationService`** | `CacheEntry`, `DerivedIndex` (derivados) | qualquer dado autoritativo |
| **`AssetMediaService`** | binários de mídia/mapas/tiles e seus metadados técnicos | `claimType`; `confidenceLevel`; natureza epistêmica do asset (vem da curadoria) |
| **`ExportPackagingService`** / **`OfflinePackageService`** | `ExportPackage`, `OfflinePackage` (montagens derivadas, com avisos) | conteúdo autoritativo; rótulos epistêmicos; licença |

**Proibições absolutas (NORMATIVO):** nenhuma camada a montante do KC escreve `Claim`/`Source`/`Citation`/`Relationship`/`reviewStatus`; nenhum serviço derivado (cache/índice) escreve dado autoritativo; nenhum serviço externo escreve `publicabilityStatus`, `confidenceLevel`, `evidenceLevel` ou `claimType`. Toda escrita autoritativa no núcleo passa pelo pipeline da Etapa 1.1/Etapa 13.

### 2.4 Quais escritas exigem curadoria humana

Seguem obrigatoriamente por revisão humana antes de qualquer publicação (herdado de 1.1/3.1): a entrada de qualquer `Claim`, `Source`, `Citation`, `Relationship` afirmativa (causal/interpretativa), `MediaAsset`/`MapAsset`, `GeometryVersion`; a transição de `reviewStatus` para `approved`; a publicação de cena (`sceneCompletenessLevel` → `publicável`) e de qualquer item de tema sensível/controverso. A infraestrutura **não automatiza** essas transições: o `SourceProvenanceService` e o `AuditTrailService` apenas registram quem revisou, quando e com que nota; a decisão é do `curator`/`scientificReviewer`/`editorialReviewer`/`legalReviewer` (Seção 7).

### 2.5 Onde entram bancos, índices, caches, filas, storage e pacotes offline

```txt
ConteudoAutoritativo  → grafo de conhecimento (KC) + storage de assets + governança/proveniência
DadosExternos         → store relacional/documental (Compliance, Planning, sessões, outputs, perfis)
IndicesDerivados      → índice temporal canônico, índice geoespacial, índice textual, (opcional) índice vetorial
Caches                → cache de consulta temporal, de MomentResult, de Scene, de tiles/3D, de outputs, offline
Filas                 → ingestão assíncrona, geração de candidatos, exportação, invalidação de cache
StorageDeMidia        → object storage de mídia/mapas + IsolatedLicenseStore separado (SA/ODbL/NC/proprietário)
PacotesOffline        → OfflinePackage versionado, assinado, com validade e licença respeitada
```

Cada um aparece na seção própria (4, 5, 9, 10, 11). A regra que os atravessa: **índices e caches são derivados do conteúdo autoritativo, nunca o contrário**; e o `IsolatedLicenseStore` é **fisicamente separado** do núcleo factual (Seção 9).

### 2.6 Como evitar que cache, busca textual ou IA substituam o grafo de claims

Por quatro barreiras técnicas **[NORMATIVO]**: **(1) tipagem de origem** — toda resposta servida carrega a origem (`autoritativo` | `derivado` | `cache`), e só `autoritativo` (um `Claim` com `provenanceRef`) é "verdade"; **(2) ausência de proveniência no derivado** — `CacheEntry`, `DerivedIndex` e *embeddings* não recebem `provenanceRef` nem `claimType`, logo não passam pelo contrato de leitura factual; **(3) reidratação obrigatória** — qualquer exibição de conteúdo factual reidrata `claimType`/`confidenceLevel`/`evidenceLevel`/`reviewStatus`/`publicabilityStatus` a partir do autoritativo, mesmo quando o *layout* veio do cache (a forma pode ser cacheada; o status epistêmico é sempre reconferido); **(4) IA não-factual por contrato** — o sistema pode usar IA para adaptar linguagem (forma), buscar/sugerir navegação ou auxiliar curadoria, mas nenhuma saída de IA é gravada como `Claim` nem servida como evidência; ela entra, quando entra, como narrativa rotulada com `reviewStatus = pending` até curadoria humana (Etapa 2, §3.3; A3/Q5). As regras **cache não é verdade**, **busca/embedding não é verdade** e **IA não é fonte factual** valem em toda a stack.

---

## 3. Domínios técnicos e *bounded contexts* (Tarefa 3)

### 3.1 Princípio de divisão

O sistema é dividido em **domínios técnicos** (*bounded contexts*) que correspondem, um a um, às camadas e funções conceituais já fixadas — para que **a fronteira de escrita do software coincida com a fronteira de autoridade do conteúdo**. Cada domínio tem um **agregado dono**, uma **fronteira de escrita** e um conjunto de **dependências permitidas** (sempre na direção da seta). Domínios não compartilham banco autoritativo: comunicam-se por contrato (Seção 6) e por REF estável. **[NORMATIVO]:** a fronteira de escrita de cada serviço é a sua camada; nenhum serviço escreve no agregado de outro.

> A separação em quinze serviços é **lógica/arquitetural**, não uma imposição de quinze processos ou bancos físicos. O MVP (Etapa 12) pode colapsar vários em um monólito modular; o que **não** pode é colapsar as **fronteiras de escrita** — o módulo de Matching, mesmo dentro do mesmo processo, não ganha permissão de escrever `Claim`.

### 3.2 `KnowledgeCoreService`
- **Responsabilidade.** Guardar e servir o grafo factual: `KnowledgeItem`, `Claim`, `ClaimSet`, `Relationship`, `Scene`, e os objetos de valor temporais/geoespaciais/epistêmicos. É o coração soberano.
- **Lê.** `Source`/`Citation`/`ProvenanceMetadata` (via `SourceProvenanceService`) e a própria estrutura do grafo.
- **Escreve.** O grafo factual e `reviewStatus` — **somente** quando acionado pelo pipeline de curadoria/ingestão.
- **Nunca escreve.** Perfis de Compliance, planejamento, `MatchSet`, `PedagogicalOutput`, sessões, cache.
- **Dependências permitidas.** `SourceProvenanceService`, `LicenseComplianceService` (na ingestão). Não depende de nenhuma camada externa.
- **Risco se mal desenhado.** Se aceitar escrita de fora do pipeline, perde a soberania e a proveniência; se misturar conteúdo SA/ODbL no grafo, contamina o núcleo (Seção 9).

### 3.3 `SourceProvenanceService`
- **Responsabilidade.** Custodiar `Source`, `Citation`, `ProvenanceMetadata`, `DatasetSnapshot` e a cadeia de proveniência; garantir que todo `Claim` rastreie a uma fonte A/B.
- **Lê.** Fontes externas (na ingestão) e o próprio registro de proveniência.
- **Escreve.** `Source`, `Citation`, `ProvenanceMetadata`, `DatasetSnapshot`.
- **Nunca escreve.** `Claim` "sozinho" (claim sem este serviço não tem proveniência, mas o conteúdo do claim é do `KnowledgeCoreService`); nada de camadas externas.
- **Dependências permitidas.** `LicenseComplianceService`.
- **Risco se mal desenhado.** Proveniência frouxa abre porta a "Wikipedia/IA como autoridade" (proibido por 1.1/A3); snapshot ausente quebra reprodutibilidade (Seção 5).

### 3.4 `LicenseComplianceService`
- **Responsabilidade.** Aplicar o portão da Etapa 1.1: classificar `licenseRiskLevel` (0–5), decidir `ingestionDecision`/`allowedUse`, exigir atribuição, marcar isolamento e bloquear o que não pode entrar. É o guardião jurídico-técnico da ingestão e da exportação.
- **Lê.** `ProvenanceMetadata`, `LicenseProfile`, política da Etapa 1.1.
- **Escreve.** `LicenseProfile`, `LicenseStorageBinding`, decisões de `allowedUse`/`ingestionDecision` e marcações de isolamento.
- **Nunca escreve.** `Claim` factual; verdade; rótulos epistêmicos.
- **Dependências permitidas.** Nenhuma a montante; é consultado por `ExportPackagingService` e `OfflinePackageService`.
- **Risco se mal desenhado.** Falha aqui contamina o núcleo com SA/ODbL, exporta NC indevidamente ou perde atribuição obrigatória (Seção 9, R-05/R-06).

### 3.5 `SceneMomentService`
- **Responsabilidade.** Servir `Scene` v1.1 (4H) e operar a função `WhatWasHappeningAtMoment` (E5): receber `MomentQuery`, montar `MomentResult` por interseção dos índices temporal/geoespacial/temático sobre claims tipados.
- **Lê.** Índices do KC (via `KnowledgeCoreService` e `DerivedIndex`), `AllowedUseContext` (E6).
- **Escreve.** `MomentResult` (derivado, cacheável e versionável — Seção 5); `generatedSceneCandidate` apenas como candidato com `sceneCompletenessLevel = rascunho`/`reviewStatus = pending`.
- **Nunca escreve.** `Claim`; `reviewStatus = approved`; `publicabilityStatus`; promoção de candidato a cena pública.
- **Dependências permitidas.** `KnowledgeCoreService`, `BrazilianComplianceService` (para `AllowedUseContext`), `CacheInvalidationService`.
- **Risco se mal desenhado.** Se "esquecer" o invariante de exibição, vaza `pending`/`hiddenItems` na simultaneidade; se tratar `generatedSceneCandidate` como publicável, fura a curadoria (R-03/R-29 das etapas).

### 3.6 `BrazilianComplianceService`
- **Responsabilidade.** Custodiar a `BrazilianEducationComplianceLayer` (E6): `ComplianceProfile`, `BNCCMapping`, `CurricularAlignment`, `AllowedUseContext`, `SchoolUseMode`, `AgeSuitability`, `SensitiveContentRule`, `AccessibilityRequirement` — tudo apontando para o KC, nunca dentro dele.
- **Lê.** KC por REF (para indexar/anotar); texto normativo (BNCC/LDB/LGPD) como dado de conformidade.
- **Escreve.** As entidades de Compliance acima.
- **Nunca escreve.** `Claim`; verdade factual; `MatchScore`; `outputStatus`.
- **Dependências permitidas.** `KnowledgeCoreService` (leitura por REF).
- **Risco se mal desenhado.** Se gravar índice BNCC dentro do KC, viola a universalidade (P1/P2); se tratar alinhamento como selo, sugere homologação (proibido).

### 3.7 `PlanningService`
- **Responsabilidade.** Receber e guardar o planejamento docente/escolar (E7): `PlanningProfile`, `usageScenario`, recorte local, profundidade, formato — dados **descartáveis e externos**.
- **Lê.** `ComplianceProfile` (para aninhar `usageScenario` sob `schoolUseModeRefs`), vocabulário do KC.
- **Escreve.** `PlanningProfile`, `usageScenario`.
- **Nunca escreve.** KC; Compliance; `MatchSet`; Output.
- **Dependências permitidas.** `BrazilianComplianceService`.
- **Risco se mal desenhado.** Se persistir dados pessoais de aluno no planejamento, viola minimização (Seção 8); se forçar exibição de conteúdo bloqueado, fura o invariante de publicabilidade.

### 3.8 `MatchingService`
- **Responsabilidade.** Operar o `ContentMatchingEngine` (E8): cruzar `PlanningProfile`×KC/Compliance, calcular `MatchScore` multidimensional, montar `MatchSet`, registrar `MatchingAuditTrail`, gerir `matchSetStatus`.
- **Lê.** Índices do KC, `ComplianceProfile`, `PlanningProfile`.
- **Escreve.** `MatchSet`, `MatchScore`, `MatchingAuditTrail`, `matchSetStatus`.
- **Nunca escreve.** `Claim`; `AllowedUseContext`; `reviewStatus`; `publicabilityStatus`; `curricularRole` da Compliance (só **deriva** `curricularRoleScope`).
- **Dependências permitidas.** `KnowledgeCoreService`, `BrazilianComplianceService`, `PlanningService`, `CacheInvalidationService`.
- **Risco se mal desenhado.** Se reescrever papel curricular ou reincluir item excluído por porta dura, fura a Compliance; **score não é verdade** — se o `MatchScore` virar critério de exibição factual, confunde relevância com confiança (R-08).

### 3.9 `PedagogicalOutputService`
- **Responsabilidade.** Operar a `PedagogicalOutputLayer` (E9): transformar `MatchSet` em `PedagogicalOutput` e suas partes (`OutputArtifact`, `OutputSectionBlock`, `OutputCitationBundle`, `OutputComplianceSummary`, `OutputConstraintWarning`, `OutputAuditTrail`, `OutputRevisionNote`), gerir `outputStatus`.
- **Lê.** `MatchSet`, `Scene`/`MomentResult`, `ComplianceProfile`, `Claim`/`Source` por REF.
- **Escreve.** As entidades de Output acima.
- **Nunca escreve.** `Claim`; `MatchScore`; `ComplianceProfile`; `reviewStatus`; `publicabilityStatus`.
- **Dependências permitidas.** `MatchingService`, `SceneMomentService`, `BrazilianComplianceService`, `KnowledgeCoreService` (leitura por REF).
- **Risco se mal desenhado.** **forma muda; fato não** — se a montagem do artefato alterar o conteúdo do claim ou suprimir citação/incerteza, quebra a regra de ouro; se exportar sem `OutputCitationBundle`, perde rastreabilidade.

### 3.10 `ExperienceSessionService`
- **Responsabilidade.** Operar a `DesignUX3DLayer` (E10): criar/gerir `ExperienceSession`, `NavigationState`, estados de vista (timeline/globo/2D/estático/projetor/offline), status de `ApprovalWorkflow` da sessão, `UXAuditTrail`.
- **Lê.** `PedagogicalOutput` e suas partes, `Scene`/`MomentResult` (por REF).
- **Escreve.** `ExperienceSession`, `NavigationState`, estados de vista, `UXAuditTrail` — **externos e descartáveis**.
- **Nunca escreve.** Conteúdo de `PedagogicalOutput`; `MatchSet`; KC; Compliance; `reviewStatus` do KC (o `approvalWorkflowStatus` é externo).
- **Dependências permitidas.** `PedagogicalOutputService`, `SceneMomentService`, `AssetMediaService`, `CacheInvalidationService`, `IdentityAccessService`.
- **Risco se mal desenhado.** Se relaxar `visibilityClass`/faixa/sensível, expõe conteúdo indevido ao aluno; se persistir PII de aluno na sessão, viola LGPD/ECA (Seção 8).

### 3.11 `AssetMediaService`
- **Responsabilidade.** Guardar e servir binários: `MediaAsset`, `MapAsset`, tiles, modelos 3D, imagens estáticas — com seus metadados técnicos (formato, resolução, LOD) e a marcação de licença/`natureLabel` herdada da curadoria.
- **Lê.** `LicenseProfile`/`allowedUse` do asset (via `LicenseComplianceService`).
- **Escreve.** Binários e metadados técnicos; **nunca** `natureLabel`/`claimType`/`confidenceLevel`, que vêm da curadoria.
- **Nunca escreve.** Verdade factual; natureza epistêmica do asset; fundir SA/ODbL no *bucket* do núcleo.
- **Dependências permitidas.** `LicenseComplianceService`, `IsolatedLicenseStore` (para assets restritos).
- **Risco se mal desenhado.** Servir asset NC como expressão pública, ou misturar SA/ODbL no *storage* não isolado (Seção 9).

### 3.12 `ExportPackagingService`
- **Responsabilidade.** Sustentar tecnicamente o `ExportPackage` (E10): montar exportação de artefato (plano, dossiê, atividade, relatório, imagem) preservando citação, incerteza, mediação e avisos, e **bloqueando** exportação quando a licença não permite.
- **Lê.** `PedagogicalOutput`, `OutputCitationBundle`, `OutputConstraintWarning`, `LicenseProfile`/`allowedUse`.
- **Escreve.** `ExportPackage` (montagem derivada, com avisos obrigatórios).
- **Nunca escreve.** Conteúdo autoritativo; rótulos epistêmicos; licença.
- **Dependências permitidas.** `PedagogicalOutputService`, `LicenseComplianceService`, `AssetMediaService`.
- **Risco se mal desenhado.** Exportar sem fonte/incerteza/mediação, ou exportar expressão NC/SA fora do permitido (R-06/R-17/R-18).

### 3.13 `IdentityAccessService`
- **Responsabilidade.** Autenticação e autorização: papéis (`AccessRole`), políticas (`AuthorizationPolicy`), visibilidade por camada e por `visibilityClass`, bloqueio de `teacherOnly`/`internalReviewOnly`, permissões em modo offline.
- **Lê.** `AccessRole`/`AuthorizationPolicy`; atributos de contexto (papel, faixa, modo).
- **Escreve.** Sessões de identidade, concessões/decisões de acesso, tokens.
- **Nunca escreve.** Conteúdo; verdade; `reviewStatus`; `publicabilityStatus`.
- **Dependências permitidas.** É transversal; consultado por todos os serviços.
- **Risco se mal desenhado.** Permissão mal configurada vaza `pending`/`teacherOnly`; autenticação fraca permite acesso indevido de menor a conteúdo restrito (R-13/R-14/R-15).

### 3.14 `AuditTrailService`
- **Responsabilidade.** Registrar a `TechnicalAuditTrail` e correlacioná-la, por REF, às trilhas conceituais (`OutputAuditTrail`, `MatchingAuditTrail`, `UXAuditTrail`, `ComplianceAnnotation`, `PlanningAnnotation`): acessos, mudanças, exportações, cache, licença, erros — com minimização de PII.
- **Lê.** Eventos de todos os serviços.
- **Escreve.** `TechnicalAuditTrail` (append-only).
- **Nunca escreve.** Conteúdo; verdade; nem captura conteúdo sensível/PII indevido (Seção 8/12).
- **Dependências permitidas.** Transversal.
- **Risco se mal desenhado.** Log capturando PII de menor (R-13); ausência de trilha impede auditoria jurídica (R-22).

### 3.15 `CacheInvalidationService`
- **Responsabilidade.** Gerir `CacheEntry` e `DerivedIndex` e suas `InvalidationRule`: cachear consulta temporal, `MomentResult`, `Scene`, tiles/3D, outputs e pacotes offline; **invalidar** ao mudar `Claim`/`Source`/`LicenseProfile`/`reviewStatus`/`publicabilityStatus`.
- **Lê.** Versões e *checksums* do conteúdo autoritativo (para detectar *staleness*).
- **Escreve.** `CacheEntry`, `DerivedIndex`, `InvalidationRule` — **derivados**.
- **Nunca escreve.** Dado autoritativo; `Claim`; rótulos epistêmicos.
- **Dependências permitidas.** Leitura de versão de todos os serviços de conteúdo.
- **Risco se mal desenhado.** **cache não é verdade** — cache desatualizado serve item revogado/`rejected` como fato (R-01/R-02); índice vetorial tratado como fonte (R-07).

### 3.16 `OfflinePackageService`
- **Responsabilidade.** Montar `OfflinePackage`: subconjunto pré-carregado para uso sem rede (sala sem internet, projetor), versionado, assinado, com validade, **respeitando licença, publicabilidade, mediação e papel**.
- **Lê.** `PedagogicalOutput`/`Scene` autorizados, `LicenseProfile`/`allowedUse`, `AccessRole`.
- **Escreve.** `OfflinePackage` (derivado, versionado, com validade).
- **Nunca escreve.** Conteúdo autoritativo; rótulos epistêmicos; licença.
- **Dependências permitidas.** `PedagogicalOutputService`, `SceneMomentService`, `LicenseComplianceService`, `IdentityAccessService`.
- **Risco se mal desenhado.** **offline não pode relaxar licença, publicabilidade, mediação ou papel** — pacote vencido serve fato desatualizado (R-11); pacote com conteúdo restrito vaza ao aluno (R-30); pacote com expressão NC/SA viola licença (R-06).

### 3.17 Justificativa das entidades técnicas novas (não duplicação)

| Entidade nova | Por que não duplica entidade anterior |
|---|---|
| **`TechnicalArchitectureLayer`** | É a camada de infraestrutura; nenhuma camada anterior (KC..UX) modela infraestrutura. |
| Os 15 `…Service` | São *bounded contexts* de software, não entidades de conteúdo; nomeiam **fronteiras de escrita**, que nenhuma etapa anterior fixou. |
| **`ApiContract`** (Seção 6) | É o contrato de comunicação entre serviços; não existe equivalente conceitual nas camadas. |
| **`AccessRole`/`AuthorizationPolicy`** (Seção 7) | Materializam papéis técnicos; os papéis conceituais (curator, teacher…) existiam, mas sem o modelo de permissão técnica. |
| **`StoragePartition`/`IsolatedLicenseStore`/`LicenseStorageBinding`** (Seções 4/9) | Resolvem o isolamento **físico** pendente desde 1.1/2; `allowedUse`/`LicenseProfile` diziam *o que* isolar, não *onde/como*. |
| **`DerivedIndex`/`CacheEntry`/`InvalidationRule`** (Seção 10) | São derivados técnicos; não há entidade de cache/índice nas camadas conceituais. |
| **`OfflinePackage`** (Seções 5/11) | Distinto de `OfflineModeView` (E10, uma **vista**) e de `ExportPackage` (E10, conceito de **exportação**): é o **artefato físico de distribuição offline**, versionado e assinado. |
| **`TechnicalAuditTrail`** (Seção 12) | Distinto de `OutputAuditTrail`/`MatchingAuditTrail`/`UXAuditTrail`: registra o **plano de infraestrutura** (acesso, cache, licença, erro), não a montagem de conteúdo/experiência. |
| **`DatasetSnapshot`** | **Não é nova** — vem da Etapa 2 (§Família F); aqui apenas ganha papel técnico de reprodutibilidade (Seção 5). |

---

## 4. Modelo de persistência e bancos de dados (Tarefa 4)

### 4.1 Decisão de fundo

A persistência separa **dado autoritativo** (o KC e sua proveniência — a única "verdade") de **dado derivado** (índices, caches, `MomentResult`, `MatchSet`) e de **dado externo** (Compliance, Planning, sessões, outputs, pacotes). **[NORMATIVO]:** o autoritativo nunca depende do derivado para existir; reconstruir todos os índices e caches a partir do autoritativo é sempre possível, e o caminho inverso (índice/cache reconstruindo o autoritativo) é proibido. Essa assimetria é o que mantém **cache não é verdade** e **busca/embedding não é verdade** como propriedades estruturais, não promessas.

### 4.2 Núcleo factual: grafo com proveniência por aresta

**[NORMATIVO]** O KC é um **grafo de conhecimento** em que itens (`KnowledgeItem` e subtipos), claims (`Claim`/`ClaimSet`) e relações (`Relationship`) são vértices/arestas tipados, e em que **toda aresta afirmativa e todo claim carregam proveniência** (`provenanceRef`) e estado de revisão (`reviewStatus`). A propriedade vinculante é "grafo tipado com proveniência por aresta", não a tecnologia. **[RECOMENDADO]** um *triplestore* RDF com grafos nomeados / RDF* (proveniência por *statement* é nativa e casa com a citação por claim) **ou** um banco de grafo de propriedades (property graph) com proveniência modelada como propriedade obrigatória de aresta. **[ALTERNATIVA]** um relacional com tabelas de aresta e proveniência, aceitável se o desempenho de travessia (Seção 14, R-33) for resolvido. **[PENDÊNCIA]** a escolha final (RDF × property graph × relacional) é da Etapa 12.

### 4.3 Camadas externas: relacional/documental

**[RECOMENDADO]** um banco **relacional** (PostgreSQL-classe) para `ComplianceProfile`/`BNCCMapping`/`CurricularAlignment`/`AllowedUseContext`/`SchoolUseMode`/`AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement` (E6), `PlanningProfile`/`usageScenario` (E7), `MatchSet`/`MatchScore`/`MatchingAuditTrail` (E8), `PedagogicalOutput` e partes (E9), `ExperienceSession`/`NavigationState`/`UXAuditTrail` (E10) e perfis/identidade. **[ALTERNATIVA]** um *store* documental para `PedagogicalOutput`/`Scene` (estruturas aninhadas), aceitável desde que preserve REF estável e versionamento. **[NORMATIVO]:** esses dados **apontam** para o KC por REF; nenhum deles é gravado dentro do grafo factual.

### 4.4 Índice geoespacial

**[NORMATIVO]** há um índice geoespacial de primeira classe para `GeometryVersion`/`modernGeometry`/`historicalGeometryVersions`/`paleoPositions` e `ModernCorrespondence` (Etapa 2, §5; 4H §5), que sustenta a seleção espacial da função (E5) e o globo/mapa (E10). **[RECOMENDADO]** uma extensão geoespacial sobre o relacional (PostGIS-classe) para geometrias modernas/históricas vetoriais. **[NORMATIVO]:** geometrias de fontes ShareAlike/ODbL (OSM/MapBiomas) **não** entram nesse índice junto ao núcleo — vão para o `IsolatedLicenseStore` (Seção 9); paleoposições são **sempre** rotuladas como reconstrução modelada (não fato de localização exata).

### 4.5 Índice temporal/canônico

**[NORMATIVO]** há um índice sobre o **escalar temporal canônico** (`canonicalTimeScalar`, com o datum fixo da Etapa 3Z) que ordena e intersecta qualquer item do Big Bang ao presente/projetivo, preservando `sourceTimeBasis` (o tempo nativo da fonte nunca é apagado). **[RECOMENDADO]** um índice ordenado (B-tree-classe) sobre o escalar, com os regimes (cósmico/profundo Ga-Ma/histórico BCE-CE/contemporâneo/projetivo) como faces de exibição (`displayTime`). **[NORMATIVO]:** o índice ordena e seleciona; ele **não** decide confiança nem publicabilidade — esses vêm reidratados do autoritativo.

### 4.6 Busca textual/semântica sem virar fonte factual

**[NORMATIVO]** pode haver busca para **encontrar** itens (não para afirmar fatos). **[RECOMENDADO]** um índice textual invertido (OpenSearch/Elasticsearch-classe) sobre rótulos/descrições/`statement` para busca por palavra. **[ALTERNATIVA/PENDÊNCIA]** um índice **vetorial/semântico** (busca por similaridade) **somente** se adotado com a barreira da Seção 10: o *embedding* é um ponteiro para itens, **nunca** um `Claim`; não recebe `provenanceRef`; e qualquer item recuperado por ele é reidratado com `claimType`/`confidence`/`reviewStatus`/`publicabilityStatus` antes de exibir. A decisão de adotar busca vetorial fica para a Etapa 12. **[NORMATIVO]:** **busca/embedding não é verdade**.

### 4.7 Storage de mídia e mapas

**[RECOMENDADO]** *object storage* (S3-classe) para `MediaAsset`/`MapAsset`/tiles/modelos 3D/imagens estáticas, com CDN à frente para tiles e estáticos (Seção 10/11). **[NORMATIVO]:** o `natureLabel` (fotografia/mapa/gráfico/reconstrução/simulação/representação artística/aproximação didática — D7) e a licença viajam como metadados do asset e governam a exibição; o *storage* serve o binário, mas a UX exibe a natureza.

### 4.8 Storage isolado para assets/dados com licença restritiva

**[NORMATIVO]** há um `IsolatedLicenseStore` **fisicamente separado** (outro *bucket*/namespace/esquema, com fronteira de processo e de acesso) para conteúdo ShareAlike/ODbL/NC/proprietário, detalhado na Seção 9. O núcleo factual **nunca** lê desse *store* para compor `Claim`; quando muito, a UX exibe a camada isolada **ao lado** do núcleo, com atribuição e sem fusão.

### 4.9 Separação entre dados universais, escolares, sessões e pacotes

**[NORMATIVO]** quatro domínios de dado nunca se misturam no mesmo agregado: **(1) universais** (KC + proveniência); **(2) escolares** (Compliance/Planning/Matching/Output — perfis e artefatos pedagógicos, sem PII de aluno por padrão); **(3) sessões/identidade** (UX/identidade — efêmeros, minimizados); **(4) pacotes** (export/offline — derivados, versionados, com validade e licença). Essa separação sustenta a privacidade (Seção 8) e a reprodutibilidade (Seção 5).

### 4.10 Dado autoritativo × índice derivado

| Propriedade | Dado autoritativo | Índice/derivado |
|---|---|---|
| Tem `provenanceRef`? | Sim (obrigatório) | Não |
| Tem `claimType`/`confidence`/`reviewStatus`? | Sim | Não (reidratados na leitura) |
| Pode ser "verdade"? | Sim | **Não** |
| É reconstruível a partir do outro? | Não a partir do índice | Sim a partir do autoritativo |
| Escreve no outro? | Escreve no índice | **Nunca** escreve no autoritativo |

### 4.11 Tabela — tipo de dado → armazenamento recomendado → motivo → risco

| Tipo de dado | Armazenamento recomendado | Motivo | Risco se mal alocado |
|---|---|---|---|
| `KnowledgeItem`/`Claim`/`ClaimSet`/`Relationship`/`Scene` | Grafo com proveniência por aresta (RDF*/property graph) | Travessia, simultaneidade, proveniência nativa | Perda de proveniência; travessia lenta (R-33) |
| `Source`/`Citation`/`ProvenanceMetadata`/`DatasetSnapshot` | Junto ao grafo + registro de proveniência versionado | Toda verdade rastreia à fonte | Claim órfão de fonte (proibido por 1.1) |
| `ComplianceProfile`/`BNCCMapping`/`AllowedUseContext`/`SchoolUseMode` | Relacional (aponta ao KC por REF) | Indexação curricular externa ao núcleo | Índice dentro do KC viola universalidade (P1) |
| `PlanningProfile`/`usageScenario` | Relacional/documental, descartável | Planejamento externo e efêmero | PII de aluno no planejamento (R-13) |
| `MatchSet`/`MatchScore`/`MatchingAuditTrail` | Relacional + cache (Seção 10) | Derivado de planejamento×KC | Tratar score como verdade (R-08) |
| `PedagogicalOutput`/`OutputArtifact`/`OutputCitationBundle` | Relacional/documental, versionado | Artefato auditável e reprodutível | Export sem citação (R-17) |
| `ExperienceSession`/`NavigationState`/`UXAuditTrail` | Relacional/efêmero, minimizado | Sessão externa e descartável | PII de aluno na sessão (R-13) |
| `GeometryVersion`/`modernGeometry`/`paleoPositions` (núcleo) | Índice geoespacial (PostGIS-classe) | Seleção espacial e globo | Paleomapa como fato (R-10) |
| Geometrias SA/ODbL (OSM/MapBiomas) | `IsolatedLicenseStore` separado | Isolamento físico obrigatório | Contaminação do núcleo (R-05) |
| `MediaAsset`/`MapAsset`/tiles/3D livres | Object storage + CDN | Servir binário em escala | Servir NC como expressão (R-06) |
| Assets NC/proprietários | `IsolatedLicenseStore`/bloqueado | NC não entra como expressão | Exportar NC (R-06) |
| Índice textual | Motor de busca textual | Encontrar itens por palavra | Busca omitindo incerteza (R-09) |
| Índice vetorial (se adotado) | Vector store isolado, sem proveniência | Encontrar por similaridade | Embedding como verdade (R-07) |
| `CacheEntry`/`DerivedIndex` | Cache em memória (Redis-classe) + CDN | Desempenho | Cache servindo item revogado (R-02) |
| `OfflinePackage`/`ExportPackage` | Object storage versionado/assinado, com validade | Distribuição com licença respeitada | Offline relaxando licença/papel (R-30) |
| `AccessRole`/`AuthorizationPolicy` | Store de identidade dedicado | Autorização transversal | Permissão mal configurada (R-15) |
| `TechnicalAuditTrail` | Log append-only, minimizado | Rastreabilidade e evidência | Log com PII de menor (R-13) |

---

## 5. Versionamento, snapshots, validade e reprodutibilidade (Tarefa 5)

### 5.1 Por que versionar

Uma plataforma educacional precisa que **um material usado em sala possa ser auditado depois**: saber qual `Claim`, qual `Source`, qual versão da cena e qual snapshot de dataset sustentavam o que o professor mostrou. **[NORMATIVO]:** todo artefato exibível ou exportável é versionado de modo a permitir reconstrução posterior do que foi visto, com a proveniência e a incerteza daquele momento.

### 5.2 O que se versiona, e como

| Artefato | Estratégia de versão | Imutável? |
|---|---|---|
| `KnowledgeItem` | `versionInfo` com histórico; cada mudança gera nova versão referenciável | Versão publicada: sim |
| `Claim` | Versionado; correção factual cria nova versão, preservando a anterior para auditoria | Versão publicada: sim |
| `Source`/`Citation` | Versionado; vinculado a `DatasetSnapshot` | Sim |
| `DatasetSnapshot` | **Imutável por definição** (`snapshotId`, `checksum`, `snapshotDate`) | **Sim (NORMATIVO)** |
| `Scene` v1.1 | Versionada; `sceneCompletenessLevel` e conteúdo versionados juntos | Versão publicada: sim |
| `MomentResult` | Derivado versionado: registra a versão dos itens e índices usados | Sim (cópia do momento) |
| `MatchSet` | Versionado: registra versão do `PlanningProfile`, do KC e da Compliance usados | Sim |
| `PedagogicalOutput` | Versionado: âncora de auditoria do material; cada exportação fixa uma versão | Sim |
| `ExportPackage` | Imutável e datado: "fotografia" do material exportado, com avisos | **Sim** |
| `OfflinePackage` | Imutável, assinado, com validade; substituição cria nova versão | **Sim** |

### 5.3 Imutabilidade de snapshots

**[NORMATIVO]** `DatasetSnapshot` é **imutável**: uma vez congelada uma versão de fonte (com `checksum`), ela nunca é alterada — fontes que mudam ou "adormecem" (C4/R7 da Etapa 1) geram **novo** snapshot, e o antigo permanece para reprodutibilidade. Um `Claim` cita o snapshot exato que o sustentava; auditar o material no futuro é seguir a cadeia `PedagogicalOutput` → `Claim` → `Citation` → `DatasetSnapshot`.

### 5.4 Versão de conteúdo × versão de renderização

**[NORMATIVO]** distinguem-se duas versões independentes: **versão de conteúdo** (o `Claim`/`Scene`/`PedagogicalOutput` — o *que* é dito) e **versão de renderização** (o *layout*, o tile, o pacote — *como* é mostrado). Atualizar a engine 3D, o tema visual ou o formato de tile muda a versão de renderização **sem** tocar a versão de conteúdo; corrigir um fato muda a versão de conteúdo e **invalida** as renderizações derivadas (Seção 10). A regra **forma muda; fato não** reaparece aqui como **versionamento separado de forma e fato**.

### 5.5 Validade e cache de `MomentResult`, `MatchSet` e `PedagogicalOutput`

**[NORMATIVO]** esses três são **derivados cacheáveis com validade**, não verdades persistentes: o cache guarda uma resposta com a **versão** dos insumos; quando um insumo muda (claim/source/license/`reviewStatus`/`publicabilityStatus`/perfil), a entrada é **invalidada** (Seção 10). **[RECOMENDADO]** validade por dependência (invalida-se pelo grafo de dependências), preferível a validade por tempo fixo; TTL pode complementar para custo. **[NORMATIVO]:** servir um derivado vencido como fato é violação (R-01/R-02).

### 5.6 Quando invalidar × quando preservar por reprodutibilidade

Há uma tensão deliberada: **operação** quer invalidar o que mudou; **auditoria escolar** quer preservar o que foi usado. Resolve-se separando os dois: **[NORMATIVO]** o cache **operacional** (o que se serve agora) é invalidado ao mudar o insumo; o registro **de auditoria** (o que foi servido então) é **preservado imutável** como versão datada do `PedagogicalOutput`/`ExportPackage`. Invalidar o cache nunca apaga o registro de auditoria.

### 5.7 Registro de `sourceTimeBasis`

**[NORMATIVO]** toda versão de item temporal registra `sourceTimeBasis` (Etapa 3Z) — o tempo nativo da fonte (ex.: "12.000 ¹⁴C BP", `scenarioYear`) — ao lado do `canonicalTimeScalar` derivado, que é marcado como derivado e **nunca** apaga o nativo. Auditar o tempo de um material no futuro exige saber **como a fonte mediu o tempo**, não só o escalar canônico.

### 5.8 Como garantir auditabilidade futura de um material exportado

**[NORMATIVO]** todo `ExportPackage`/`OfflinePackage` carrega: a versão do `PedagogicalOutput`; as versões dos `Claim`/`Scene`/`MomentResult` referenciados; os `DatasetSnapshot` por trás das `Citation`; os avisos (incerteza, anacronismo, equivalência, mediação) e a atribuição de licença vigentes; e a data/assinatura da exportação. Com isso, um revisor (escolar, científico ou jurídico) reconstrói, meses depois, **exatamente** o que foi mostrado e com que proveniência — sem depender do acesso ao vivo às fontes (antifragilidade, C4/R7).

---

## 6. APIs internas e contratos entre camadas (Tarefa 6)

### 6.1 O que é um contrato aqui

Um `ApiContract` é a **especificação conceitual** da conversa entre dois domínios: o que entra, o que sai, qual camada é **dona** da escrita, se a operação é **leitura** ou **escrita**, e quais **invariantes** ela deve respeitar. **[NORMATIVO]:** os contratos codificam a direção de dependência — um contrato de escrita só existe na camada dona; nenhum contrato dá a uma camada a montante o poder de escrever no agregado de outra. Nada aqui é implementação (sem verbos HTTP, sem esquema de payload): é o dicionário de contratos.

```txt
ApiContract = {
  contractId,
  ownerService,          # serviço dono da escrita/agregado
  operationKind,         # leitura | escrita
  inputSummary,          # o que entra (conceitual)
  outputSummary,         # o que sai (conceitual)
  callableBy,            # quais serviços podem chamar (respeita a seta)
  invariantsEnforced,    # invariantes que a operação deve preservar
  sideEffectClass        # nenhum | derivado | autoritativo (escrita no núcleo só pelo pipeline)
}
```

### 6.2 Catálogo conceitual de contratos

| Contrato | Entrada | Saída | Camada dona | L/E | Invariantes que respeita | Riscos |
|---|---|---|---|---|---|---|
| **Consulta ao KC** | REF de item/claim, filtros | `KnowledgeItem`/`Claim` com `claimType`/`confidence`/`evidence`/`reviewStatus`/`provenance` | KC (E2) | Leitura | só `approved`/publicável como fato; proveniência sempre anexada | vazar `pending` (R-03) |
| **Consulta temporal** | intervalo no `canonicalTimeScalar` | itens cujo `TimeRange` intersecta, com `sourceTimeBasis` | KC (E2) | Leitura | nunca apaga datum nativo; incerteza temporal preservada | erro de datum (R-32) |
| **Consulta geoespacial** | recorte espacial (moderno/histórico/paleo) | itens por geometria, com geometria escolhida rotulada | KC (E2) | Leitura | paleoposição rotulada como reconstrução; SA/ODbL isolado | paleomapa como fato (R-10); erro geoespacial (R-34) |
| **`WhatWasHappeningAtMoment`** | `MomentQuery` (ano/período/evento/região/camada) | `MomentResult` (foco, simultâneos, States, claimSets, incerteza, avisos, `publicabilityStatus`, `gatingReason`) | função sobre KC (E5) | Leitura (deriva `MomentResult`) | invariante de exibição; `hiddenItems` nunca como fato; anti-falsa-equivalência | vazar `hiddenItems`; falsa simetria |
| **Leitura de `Scene` v1.1** | REF de cena + papel/modo | `Scene` (34 campos) respeitando `sceneCompletenessLevel`/`publicabilityStatus` | `SceneMomentService` (4H/E5) | Leitura | `rascunho`/`gabarito-interno` não vai ao aluno como fato | cena interna pública (R-03) |
| **Leitura de `ComplianceProfile`** | REF de item/contexto | `AllowedUseContext`/`AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement`/`BNCCMapping` | Compliance (E6) | Leitura | alinhamento ≠ selo; faixa/sensível só endurece | alinhamento como homologação (R-23) |
| **Criar/ler `PlanningProfile`** | série/disciplina/recorte/profundidade/`usageScenario` | `PlanningProfile` persistido | Planning (E7) | Escrita (externa) + Leitura | sem PII de aluno; `usageScenario` aninha sob `schoolUseModeRefs` | PII no planejamento (R-13) |
| **Criar/ler `MatchSet`** | `PlanningProfile` + filtros | `MatchSet`/`MatchScore`/`matchSetStatus`/`MatchingAuditTrail` | Matching (E8) | Escrita (derivada) + Leitura | **score não é verdade**; não altera claim/`reviewStatus`; respeita porta dura | score como verdade (R-08) |
| **Criar/ler `PedagogicalOutput`** | `MatchSet` + forma escolhida | `PedagogicalOutput`/`OutputArtifact`/`OutputCitationBundle`/`outputStatus`/`OutputAuditTrail` | Output (E9) | Escrita + Leitura | **forma muda; fato não**; citação/incerteza/mediação preservadas | export sem citação (R-17) |
| **Criar/ler `ExperienceSession`** | `pedagogicalOutputRef` + papel + modo + acessibilidade | `ExperienceSession`/`NavigationState`/estados de vista/`UXAuditTrail` | UX (E10) | Escrita (externa) + Leitura | respeita papel/`visibilityClass`/faixa; rótulos epistêmicos visíveis; sem PII | expor `teacherOnly` ao aluno (R-04) |
| **Exportação** | REF de artefato + opções | `ExportPackage` (com avisos) **ou** bloqueio por licença | `ExportPackagingService` | Escrita (derivada) | preserva fonte/incerteza/mediação; **respeita licença** | NC exportado (R-06); export sem fonte (R-17) |
| **Pacote offline** | REF de conteúdo autorizado + escopo | `OfflinePackage` (versionado/assinado/validade) | `OfflinePackageService` | Escrita (derivada) | **offline não relaxa licença/publicabilidade/mediação/papel** | offline desatualizado (R-11); restrito vazado (R-30) |
| **Auditoria** | janela/filtro + papel autorizado | `TechnicalAuditTrail` correlacionada às trilhas conceituais | `AuditTrailService` | Leitura (append-only na escrita) | minimização de PII; rastreabilidade integral | log com PII (R-13); sem trilha (R-22) |

### 6.3 Regra transversal dos contratos

**[NORMATIVO]** todo contrato de **leitura factual** devolve o conteúdo **com** seus rótulos epistêmicos (`claimType`/`confidenceLevel`/`evidenceLevel`), seu `reviewStatus`/`publicabilityStatus`, sua incerteza e sua proveniência — nunca o "texto pelado". Todo contrato de **escrita derivada** (cache/índice/MatchSet/Output/Session/Export/Offline) tem `sideEffectClass` `derivado` ou `autoritativo`-apenas-no-pipeline, e **nunca** grava `Claim`/`reviewStatus`/`publicabilityStatus`/`confidenceLevel`/`claimType`. Um contrato que permitisse escrita indevida é, por definição, um *bug* de arquitetura (Seção 13, invariante 20).

---

## 7. Segurança, permissões e papéis (Tarefa 7)

### 7.1 RBAC + ABAC

**[NORMATIVO]** a autorização combina **RBAC** (papel define o conjunto base de permissões) com **ABAC** (atributos refinam: faixa etária do público, `SchoolUseMode`/`usageScenario` ativo, `visibilityClass` do conteúdo, `reviewStatus`/`publicabilityStatus`, modo online/offline, escopo da turma/escola). RBAC sozinho não basta porque a mesma operação ("ver este item") depende do **atributo do conteúdo** (sensível? `teacherOnly`? `pending`?) e do **contexto** (aluno em sala × professor preparando). **[RECOMENDADO]** política declarativa avaliada por um ponto central no `IdentityAccessService`.

```txt
AccessRole = {
  roleId,
  role,                 # systemAdmin | curator | scientificReviewer | editorialReviewer
                        # | legalReviewer | teacher | schoolCoordinator | student
                        # | guardianOrResponsibleAdult | publicViewer | offlineViewer
  layerScope,           # camadas que o papel pode ler/escrever (respeita a seta)
  writeBoundary         # agregado(s) em que pode escrever (vazio para papéis de leitura)
}

AuthorizationPolicy = {
  policyId,
  appliesToRole,
  resourceClass,        # KC | Compliance | Planning | Matching | Output | Session | Asset | Export | Offline | Audit
  attributeConditions,  # ABAC: ageBand, schoolUseMode, visibilityClass, reviewStatus, publicabilityStatus, online/offline, turmaScope
  effect                # permitir | negar (negar vence em conflito)
}
```

### 7.2 Permissões por camada e por papel (síntese)

| Papel | Lê | Escreve | Nunca acessa |
|---|---|---|---|
| `systemAdmin` | infraestrutura, logs técnicos | configuração técnica, papéis | conteúdo factual como editor; PII de aluno como conteúdo |
| `curator` | KC, fontes, fila de ingestão | `KnowledgeItem`/`Claim`/`Relationship`/`reviewStatus` (via pipeline) | dados pessoais de aluno; sessões |
| `scientificReviewer` | claims, evidências, incerteza | aprovação científica (`reviewStatus`) | Compliance/Planning/Output/UX |
| `editorialReviewer` | claims sensíveis/controversos, `ClaimSet`, mediação | aprovação editorial (`reviewStatus`, `editorialNote`) | verdade factual sem revisor científico |
| `legalReviewer` | proveniência, licença, casos de risco | decisão de `legal-review`/licença | conteúdo pedagógico como editor |
| `teacher` | Output completo, `teacherOnly`, mediação, fonte/incerteza | edição **de forma** (`OutputRevisionNote`), `PlanningProfile`, aprovação na sessão | `Claim`/`reviewStatus`/`MatchScore`; `internalReviewOnly`; PII de outros |
| `schoolCoordinator` | dados agregados de turma/escola, planejamento | configuração escolar, `PlanningProfile` da escola | conteúdo factual como editor; PII individual de aluno por padrão |
| `student` | face do aluno por faixa (Output `studentFacing`) | anotação local efêmera (se houver), nada autoritativo | `teacherOnly`/`internalReviewOnly`/`pending`/sensível-sem-mediação |
| `guardianOrResponsibleAdult` | (se aplicável) visão de acompanhamento agregada | nada de conteúdo | conteúdo restrito; PII de outros alunos |
| `publicViewer` | conteúdo público publicável (exploração livre) | nada | `teacherOnly`/`internalReviewOnly`/`pending`/sensível-sem-mediação |
| `offlineViewer` | subconjunto do `OfflinePackage` autorizado | nada autoritativo | conteúdo restrito não incluído; tudo que a licença/papel não permitem |

### 7.3 Visibilidade professor × estudante

**[NORMATIVO]** a separação herdada de E6/E8/E9/E10 é imposta tecnicamente por ABAC sobre `visibilityClass`: **`studentFacing`** chega ao aluno por faixa; **`teacherOnly`** nunca aparece ao aluno (nem em cache, índice, exportação ou offline); **`internalReviewOnly`** nunca sai do círculo de curadoria/revisão; **`excludedButRelevant`** fica como referência interna do Matching, jamais exibido. O ponto de decisão é único: a mesma política vale online, offline e na exportação.

### 7.4 Bloqueio de `teacherOnly` e `internalReviewOnly`

**[NORMATIVO]** dois bloqueios duros: (a) sessão de `student`/`publicViewer`/`offlineViewer` **nunca** recebe item `teacherOnly`, mesmo que referenciado por um artefato — o serviço filtra antes de servir, cachear ou empacotar; (b) item `internalReviewOnly` só é acessível a `curator`/`*Reviewer` e jamais entra em `MatchSet`/`PedagogicalOutput`/`ExportPackage`/`OfflinePackage`. Filtragem na borda (não confiar no cliente para esconder) é obrigatória.

### 7.5 Proteção contra vazamento de `pending`/`legal-review`/`rejected`

**[NORMATIVO]** o invariante de exibição (1.1/3.1) é imposto em **toda** leitura factual: item com `reviewStatus ∈ {pending, legal-review, rejected}` não é servido como fato a nenhum papel não-curatorial, não é cacheado como fato, não é indexado para busca pública, não entra em derivado (MomentResult/MatchSet/Output) como conteúdo exibível, e não é empacotado para offline/export. O `gatingReason` é exibível à curadoria; ao público, o item simplesmente **não existe como fato**.

### 7.6 Trilha de auditoria de acesso

**[NORMATIVO]** todo acesso a conteúdo restrito (`teacherOnly`/`internalReviewOnly`/`pending`) e toda decisão de autorização sensível são registrados na `TechnicalAuditTrail` (Seção 12), com minimização de PII (quem, quando, qual classe de recurso — sem despejar conteúdo sensível no log). Acesso negado também é registrado (para detecção de tentativa indevida).

### 7.7 Separação entre usuário escolar e curador

**[NORMATIVO]** os papéis de **curadoria/revisão** (curator, scientific/editorial/legal reviewer) e os papéis **escolares** (teacher, coordinator, student, guardian) vivem em planos separados: o usuário escolar nunca recebe credencial de escrita no KC; o curador nunca opera com dados pessoais de aluno. Os dois mundos se encontram apenas no **conteúdo já publicado** — o professor consome o que a curadoria aprovou, sem poder reabrir a verdade.

### 7.8 Permissões em modo offline

**[NORMATIVO]** o `OfflinePackage` carrega **a política de acesso embutida**: o `offlineViewer` só vê o que seu papel/faixa permitia online, e nada `teacherOnly`/`internalReviewOnly`/`pending` é incluído no pacote. Offline **não** é uma brecha: a ausência de rede não pode "abrir" conteúdo que a política fecharia online (Seção 8/9; invariantes 11/12).

---

## 8. Privacidade, LGPD, ECA e minimização de dados (Tarefa 8)

### 8.1 Princípio: o núcleo não precisa de PII de aluno

**[NORMATIVO]** o Knowledge Core e toda a produção de conteúdo (Compliance/Planning/Matching/Output) funcionam **sem nenhum dado pessoal real de aluno**. Conhecimento é universal; planejamento é sobre turma/série/disciplina, não sobre indivíduos identificados. Logo, a arquitetura **não coleta PII de aluno para operar o produto**; quando muito, opera com **dados agregados de turma** (Seção 8.3). Isso é privacidade por design (LGPD Art. 6º; minimização), não uma camada adicional.

### 8.2 Minimização por padrão

**[NORMATIVO]** coleta-se o **mínimo**: nenhum dado pessoal é coletado a menos que estritamente necessário para uma função explicitamente solicitada, e sempre na menor granularidade que a função exige. Campos pessoais não são "guardados por garantia". O padrão de qualquer formulário/sessão/planejamento é **sem PII de aluno**; PII só entra por exceção justificada (e mesmo então fora do KC, Seção 8.4).

### 8.3 Dados agregados de turma

**[RECOMENDADO]** quando houver necessidade pedagógica (ex.: "a turma X usa o recorte local Y"), trabalhar com **agregados não identificáveis** (contagens, perfis de turma), nunca com registros por aluno. Agregados de turma vivem no domínio escolar (Seção 4.9), separados de identidade.

### 8.4 Separação entre dados pedagógicos, de sessão e de identidade

**[NORMATIVO]** três domínios de dado pessoal/quase-pessoal permanecem fisicamente separados: **(1) dados pedagógicos** (planejamento, outputs — sem PII por padrão); **(2) dados de sessão** (navegação, estado de vista — efêmeros, minimizados, descartáveis); **(3) dados de identidade** (autenticação — no `IdentityAccessService`, isolado). Nenhum dos três é gravado no KC; nenhum cruza com os outros sem base legal.

### 8.5 Privacidade de menores

**[NORMATIVO]** **menores exigem minimização máxima de dados** (LGPD Art. 14; ECA; melhor interesse da criança). Para usuários presumidamente menores: nenhum dado pessoal sensível; nenhum perfilamento; nenhuma publicidade/rastreamento; logs sem PII de menor; e qualquer tratamento excepcional exige consentimento/controle do responsável ou da escola (Seção 8.9). Na dúvida sobre a idade do público, aplica-se o regime mais protetivo.

### 8.6 Retenção e descarte

**[NORMATIVO]** dados de sessão são **efêmeros** (retidos pelo tempo da função e descartados); pacotes offline têm **validade** e expiram; dados pedagógicos seguem a necessidade da escola, com política de retenção/descarte definida. **[PENDÊNCIA]** prazos concretos de retenção e o fluxo de descarte/expurgo são decisão da operação/jurídico (Etapa 14), dentro deste princípio.

### 8.7 Pseudonimização quando aplicável

**[RECOMENDADO]** quando algum identificador for inevitável (ex.: distinguir sessões da mesma turma), usar **pseudônimos** desacoplados da identidade real, com a tabela de correspondência (se existir) isolada no `IdentityAccessService` e nunca em logs/derivados. O conteúdo e os derivados operam sobre pseudônimos, não sobre PII.

### 8.8 Logs sem conteúdo sensível indevido

**[NORMATIVO]** logs e `TechnicalAuditTrail` registram **eventos** (quem-papel, quando, qual classe de recurso, qual decisão), **não** conteúdo sensível nem PII de menor. Não se despeja em log o texto de um tema sensível, dados de saúde/origem/religião de um aluno, nem identificadores diretos. Observabilidade é sobre o sistema, não sobre a pessoa (Seção 12.7).

### 8.9 Consentimento e controle escolar

**[NORMATIVO]** quando algum tratamento de dado pessoal for excepcionalmente necessário, o **controle é da escola/responsável**, com base legal adequada (LGPD), e o aluno não é tratado como titular de coleta direta sem essa mediação. **[PENDÊNCIA]** o desenho concreto de consentimento/controle (termos, painel do responsável, base legal por caso) é da Etapa 14.

### 8.10 Proibição de usar dados de aluno para treinar modelo ou gerar fato

**[NORMATIVO]** dados de aluno **nunca** entram no KC, **nunca** viram `Claim`, e **nunca** são usados para treinar/afinar modelo nem para gerar conteúdo factual. A regra **dados de aluno não entram no KC** e a regra **IA não é fonte factual** se reforçam: nem o conteúdo do aluno alimenta a verdade, nem a IA produz verdade.

### 8.11 Personalização local × analytics operacional

**[NORMATIVO]** distinguem-se **personalização local** (preferências de exibição na própria sessão/dispositivo — acessibilidade, idioma, recorte — efêmeras e não enviadas como perfil) de **analytics operacional** (telemetria de uso agregada para operar/melhorar o produto). A primeira é permitida e minimizada; o segundo **não é criado nesta etapa** e, quando existir, será **agregado, sem PII de menor e sem perfilamento individual**. **[PENDÊNCIA]** o analytics operacional é da Etapa 14, sob estes limites.

### 8.12 O que fica para a Etapa 14

**[PENDÊNCIA]** prazos de retenção/descarte, fluxo de consentimento/controle escolar, desenho de analytics operacional agregado, integração LMS (mantendo identidade e conteúdo separados — R-29), DPIA/relatório de impacto, e validação jurídica final. A Etapa 11 fixa os **princípios e as fronteiras**; a operacionalização é da Etapa 14, sem poder relaxá-los.

---

## 9. Licenças, isolamento físico e assets (Tarefa 9)

### 9.1 O problema herdado, resolvido tecnicamente

Desde a Etapa 1/1.1 e a Etapa 2, ficou pendente **onde e como** isolar fisicamente o que é ShareAlike/ODbL/NC/proprietário, e como separar o **fato recodificado** (livre) da **expressão licenciada** (governada). A Etapa 11 resolve isso com três mecanismos: o `IsolatedLicenseStore` (armazenamento fisicamente separado), o `LicenseStorageBinding` (vínculo por asset entre licença e local de armazenamento) e o `LicenseComplianceService` como **guardião único** de ingestão e exportação. A regra **licença governa expressão/asset, não o fato recodificado** é o eixo: um limite cronoestratigráfico do ICS (fato) entra livre no núcleo; o **gráfico** do ICS (expressão NC) não entra.

### 9.2 Isolamento físico de ShareAlike/ODbL/NC/proprietário

**[NORMATIVO]** conteúdo `shareAlikeRequired` (CC BY-SA/ODbL), `nonCommercial` (NC) e `proprietário` reside em `IsolatedLicenseStore` **fisicamente separado** do núcleo factual: outro *bucket*/namespace de object storage e/ou outro esquema/instância de banco, com fronteira de processo e de acesso. **[NORMATIVO]:** o `KnowledgeCoreService` **não** tem caminho de leitura para compor `Claim` a partir desse *store*; isolamento **não** remove a obrigação da licença (NC continua NC onde estiver — nota 2 da Etapa 1.1).

### 9.3 Separação entre fato recodificado e expressão licenciada

**[NORMATIVO]** na ingestão, o `LicenseComplianceService` separa: **(a)** o **fato** (re-codificável, com atribuição de origem do fato) → pode ir ao núcleo como `Claim` (`allowedUse = knowledge-core`); **(b)** a **expressão** (texto, imagem, gráfico, geometria sob licença) → governada pela licença, indo para `media-dossier`, `isolated-layer`, `index-only` ou `blocked`. O núcleo guarda o fato; a expressão SA/ODbL fica isolada; a expressão NC não entra como expressão.

### 9.4 Storage por asset e `LicenseProfile`

**[NORMATIVO]** cada asset (`MediaAsset`/`MapAsset`/`GeometryVersion`/dado tabular) carrega seu `LicenseProfile` (Etapa 2) e seu `ProvenanceMetadata` (Etapa 1.1), e seu local de armazenamento é determinado por `LicenseStorageBinding`:

```txt
LicenseStorageBinding = {
  bindingId,
  assetRef,                # MediaAsset | MapAsset | GeometryVersion | dado tabular
  licenseProfileRef,       # LicenseProfile (Etapa 2)
  provenanceRef,           # ProvenanceMetadata (Etapa 1.1)
  storagePartition,        # core-store | media-store | isolated-license-store | blocked
  exportPolicy,            # exportável | exportável-com-atribuição | nao-exportável | bloqueado
  attributionText,         # crédito pronto (quando exigido) — viaja com o asset
  perAssetConfirmed        # confirmação por asset (Risco 2: Commons/Europeana)
}
```

### 9.5 Confirmação por asset

**[NORMATIVO]** para fontes de licença **heterogênea por item** (Wikimedia Commons, Europeana/DPLA, GBIF — Risco 2 da Etapa 1.1), `perAssetConfirmed` deve ser verdadeiro antes do uso: o curador confirma a licença **daquele** arquivo; até lá, `reviewStatus = pending` e o asset não é servido.

### 9.6 Bloqueio de reprodução de expressão NC

**[NORMATIVO]** expressão NC (`nonCommercial = true`) **nunca** é servida como expressão pública nem incluída em `ExportPackage`/`OfflinePackage`; só o **fato re-derivado de fonte livre** pode aparecer. O `ExportPackagingService` e o `OfflinePackageService` consultam o `LicenseComplianceService` e **bloqueiam** a saída de qualquer asset com `exportPolicy ∈ {nao-exportável, bloqueado}`.

### 9.7 Camada isolada para dados SA/ODbL e exportação

**[NORMATIVO]** dados SA/ODbL (OSM/MapBiomas) ficam no `IsolatedLicenseStore` e, quando exibidos, aparecem como **camada isolada** ao lado do núcleo, com atribuição (ex.: "© OpenStreetMap contributors"). **[NORMATIVO]:** exportação que incluiria material SA/ODbL só é permitida se respeitar o ShareAlike e a atribuição; quando o formato de exportação não puder honrar o ShareAlike, a exportação daquele material é **impedida** (não "relaxada").

### 9.8 Pacote offline respeitando licença

**[NORMATIVO]** o `OfflinePackage` herda **integralmente** as restrições de licença: nada NC/proprietário como expressão; SA/ODbL só com atribuição e ShareAlike honrados; atribuição obrigatória embutida no pacote. **offline não pode relaxar licença** — a ausência de rede não cria direito de uso.

### 9.9 Atribuição obrigatória

**[NORMATIVO]** quando `attributionRequired = true`, o `attributionText` viaja com o asset por todo o caminho — exibição, cache, exportação, offline — e nunca é descartado por "limpeza de tela" ou compactação de pacote.

### 9.10 Diferença entre mídia, mapa, dado tabular, geometria e claim

**[NORMATIVO]** cinco naturezas com tratamento distinto: **`MediaAsset`** (imagem/vídeo/áudio/ilustração — licença por asset, `natureLabel`); **`MapAsset`** (imagem de mapa — distinta da geometria); **dado tabular** (séries/indicadores — licença da fonte, fato re-codificável); **`GeometryVersion`** (dado vetorial — SA/ODbL isolado; geoBoundaries/Natural Earth livres); **`Claim`** (fato — livre, no núcleo, com proveniência). Confundir geometria (dado) com mapa (imagem) ou tratar expressão como fato é erro de ingestão que o portão impede.

### 9.11 Matriz técnica — `licenseRiskLevel` 0–5 → armazenamento → exportação → risco

| `licenseRiskLevel` | Exemplos (Etapa 1.1) | Estratégia de armazenamento | Estratégia de exportação | Risco se mal tratado |
|---|---|---|---|---|
| **0 — Livre** | PD, CC0, fato recodificado, texto legal BR (NASA, Natural Earth, BNCC) | `core-store`/`media-store` (núcleo/mídia) | exportável; atribuição opcional (boa prática) | baixo; registrar proveniência |
| **1 — Atribuição** | CC BY (Macrostrat, PBDB, geoBoundaries, OWID próprio) | `core-store`/`media-store` com `attributionText` | exportável-com-atribuição (crédito embutido) | perder atribuição na exportação (R-09/R-17) |
| **2 — Por item** | Wikimedia Commons, Europeana/DPLA, GBIF | `media-store` **após** `perAssetConfirmed`; até lá `pending` | exportável conforme licença confirmada | servir item não confirmado (R-05) |
| **3 — ShareAlike/ODbL** | OSM, MapBiomas, texto de Wikipedia | **`isolated-license-store`** (físico, separado) | só se ShareAlike + atribuição honrados; senão **impedida** | contaminar o núcleo (R-05) |
| **4 — Não-comercial** | Seshat, GADM, gráfico ICS, scans David Rumsey | **não entra como expressão**; só **fato** no núcleo; expressão `blocked` | **não-exportável** como expressão; só o fato re-derivado | exportar NC (R-06) |
| **5 — Proprietária/comercial** | ACLED, Deep Time Maps | `blocked` sem contrato; com contrato, `isolated-license-store` sob termos | bloqueada sem contrato; conforme contrato com ele | uso sem contrato; vazamento contratual (R-06) |

> **[NORMATIVO]:** a matriz é imposta pelo `LicenseComplianceService` na **ingestão** (onde o item entra) e revalidada na **exportação/offline** (onde o item sai). Risco 3+ nunca toca o `core-store`; Risco 4+ nunca sai como expressão.

---

## 10. Cache, busca, índices e invalidação (Tarefa 10)

### 10.1 Regra de ouro do cache

**[NORMATIVO]** **cache não é verdade**. Todo `CacheEntry` é um **derivado** que carrega a **versão dos insumos** que o originaram; ele acelera a entrega, mas a verdade continua no autoritativo. Toda leitura factual reidrata `reviewStatus`/`publicabilityStatus`/`claimType`/`confidence` do autoritativo, mesmo quando o *layout* veio do cache (a forma cacheia; o status epistêmico se reconfere).

```txt
CacheEntry = {
  cacheKey,
  derivedKind,           # consulta-temporal | momentResult | scene | tile | output | offline-fragment
  inputVersionSet,       # versões dos insumos (claim/source/scene/profile/license) que originaram a entrada
  payloadRef,            # o derivado servido (layout/tile/resultado)
  originClass,           # SEMPRE 'derivado' (nunca 'autoritativo')
  invalidationRuleRef
}

DerivedIndex = {
  indexId,
  indexKind,             # temporal | geoespacial | textual | vetorial(opcional)
  sourceOfTruthRef,      # aponta para o autoritativo (unidirecional)
  carriesProvenance,     # SEMPRE false (índice não é fonte)
  rebuildableFromSource  # SEMPRE true
}

InvalidationRule = {
  ruleId,
  triggersOn             # claimChanged | sourceChanged | licenseChanged | reviewStatusChanged | publicabilityChanged | profileChanged
}
```

### 10.2 Cache de consulta temporal

**[RECOMENDADO]** cachear resultados de consulta por intervalo no `canonicalTimeScalar` (recortes frequentes da timeline), invalidando quando itens daquele intervalo mudam de versão ou de `reviewStatus`/`publicabilityStatus`.

### 10.3 Cache de `MomentResult`

**[RECOMENDADO]** cachear `MomentResult` por `MomentQuery` normalizada, **com** a versão dos itens/States/claimSets usados. **[NORMATIVO]:** invalidar ao mudar qualquer item do recorte, especialmente se um item passar a `pending`/`rejected` (o cache não pode continuar mostrando o que foi despublicado — R-02).

### 10.4 Cache de `Scene`

**[RECOMENDADO]** cachear a montagem de exibição da `Scene` v1.1 por versão de cena + papel/modo. **[NORMATIVO]:** invalidar ao mudar a cena, seu `sceneCompletenessLevel`/`publicabilityStatus` ou qualquer claim referenciado.

### 10.5 Cache de tiles/mapas/3D

**[RECOMENDADO]** CDN para tiles raster/vetor, modelos 3D e imagens estáticas (alto volume, baixa mutabilidade). **[NORMATIVO]:** tiles de camada isolada SA/ODbL servem com atribuição e do `IsolatedLicenseStore`, nunca misturados ao núcleo; paleomapas são marcados como reconstrução (não fato — R-10).

### 10.6 Cache de outputs

**[RECOMENDADO]** cachear renderização de `PedagogicalOutput` por versão. **[NORMATIVO]:** o cache guarda a **forma**; `OutputCitationBundle`/incerteza/mediação são reidratados; nunca se cacheia um output "sem fonte" (R-17).

### 10.7 Cache offline

**[NORMATIVO]** o `OfflinePackage` é o "cache" do offline: versionado, com validade, e invalidável por substituição. Um pacote vencido **avisa** que pode estar desatualizado e/ou expira; ele nunca finge ser a versão atual (R-11).

### 10.8 Invalidação por mudança de claim/source/license/reviewStatus/publicability

**[NORMATIVO]** a `InvalidationRule` dispara invalidação em cascata pelo grafo de dependências quando muda: `Claim`, `Source`, `LicenseProfile`, `reviewStatus`, `publicabilityStatus` ou perfil (Compliance/Planning). Mudança que **despublica** ou **revoga** um item invalida **imediatamente** todo derivado que o exibia como fato (cache, MomentResult, Output, e marca pacotes offline para atualização). **[RECOMENDADO]** invalidação orientada a eventos (o autoritativo emite o evento de mudança; os derivados reagem), preferível a varredura periódica.

### 10.9 Busca textual

**[RECOMENDADO]** índice textual invertido sobre rótulos/descrições/`statement` para **encontrar** itens. **[NORMATIVO]:** a busca devolve **ponteiros** para itens, e a exibição reidrata os rótulos epistêmicos; a busca **nunca** "responde um fato" sem passar pelo autoritativo (R-09). Resultados respeitam `visibilityClass`/`reviewStatus` (busca de aluno não acha `teacherOnly`/`pending`).

### 10.10 Busca vetorial/semântica (se adotada)

**[ALTERNATIVA/PENDÊNCIA]** se adotada, o índice vetorial é um `DerivedIndex` com `carriesProvenance = false`: serve para similaridade/descoberta, **nunca** como fonte. **[NORMATIVO]:** **busca/embedding não é verdade** — proíbe-se tratar *embedding* como evidência, gerar "fato" por recuperação semântica, ou exibir resultado vetorial sem reidratar `claimType`/`confidence`/`reviewStatus`. A decisão de adotar é da Etapa 12.

### 10.11 Índice derivado × dado autoritativo (reforço)

**[NORMATIVO]** já fixado na Seção 4.10: índice/cache não tem proveniência, é reconstruível a partir do autoritativo, e nunca escreve no autoritativo. Esta seção apenas adiciona o **mecanismo de invalidação** que mantém o derivado coerente com a verdade.

### 10.12 Auditoria da versão retornada

**[NORMATIVO]** toda resposta servida (autoritativa ou de cache) registra, na `TechnicalAuditTrail`, **qual versão** do conteúdo foi entregue e se veio do autoritativo ou do cache — para que uma auditoria futura saiba não só *o que* foi mostrado, mas *de qual versão e por qual caminho* (Seção 12).

---

## 11. Arquitetura para timeline, globo 3D, 2D, estático, projetor e offline (Tarefa 11)

### 11.1 Separação entre engine e dados autoritativos

**[NORMATIVO]** a engine de renderização (timeline, globo 3D, mapa 2D) é **apresentação**, separada do dado autoritativo: ela consome `Scene`/`MomentResult`/itens por REF e os desenha, mas **nunca** os edita. Trocar a engine não muda um `Claim`. A engine recebe **dados já rotulados** (claimType/confiança/incerteza/`natureLabel`/atribuição) e é **obrigada** a exibir esses rótulos — a engine não pode "desligar" a honestidade epistêmica para ganhar desempenho ou estética.

### 11.2 Tiles e LOD

**[RECOMENDADO]** servir o globo/mapa por **tiles** (raster e/ou vetor) com **níveis de detalhe (LOD)** progressivos, via CDN, para desempenho em hardware modesto. **[NORMATIVO]:** o LOD reduz **detalhe visual**, nunca o **piso epistêmico** — um globo de baixa resolução ainda mostra fonte, incerteza e natureza do dado.

### 11.3 Paleogeografia e `paleoPositionPolicy`

**[NORMATIVO]** posições paleogeográficas (reconstruções GPlates/EarthByte) são servidas como **reconstrução modelada**, regidas pela `paleoPositionPolicy` e por `ModernCorrespondence` (Etapa 2/4H): a UX nunca apresenta paleoposição como localização exata/fato, e o globo as marca como modelo com incerteza. Dados de reconstrução são CC BY (atribuição); a expressão de mapas NC (Deep Time Maps) não entra.

### 11.4 Degradação 3D → 2D → estático → offline/projetor

**[NORMATIVO]** a `ViewDegradationLadder` (E10) é sustentada tecnicamente como **degraus que preservam o piso epistêmico**:

| Degrau | Gatilho técnico | O que muda | O que **nunca** muda |
|---|---|---|---|
| **3D** (globo WebGL) | `deviceCapability` alto, WebGL disponível | riqueza visual, interação espacial | fonte, incerteza, natureza, rótulos |
| **2D** (mapa) | sem GPU suficiente / preferência | projeção plana, menos interação | o mesmo conteúdo factual e rótulos |
| **Estático** (imagem + texto) | sem WebGL / movimento reduzido / impressão | imagem + equivalente textual | citação, incerteza, mediação, atribuição |
| **Offline** (`OfflinePackage`) | sem rede | subconjunto pré-carregado | licença, publicabilidade, papel, piso epistêmico |
| **Projetor** | sala/projeção | alto contraste, baixa densidade | legibilidade dos rótulos e avisos |

**[NORMATIVO]:** **degradação técnica nunca remove o piso epistêmico** — cada degrau abaixo do 3D mantém fonte, incerteza, natureza do dado, mediação e atribuição.

### 11.5 Desempenho em hardware escolar modesto

**[NORMATIVO]** o produto deve funcionar em hardware escolar modesto e conexões instáveis: por isso a degradação graciosa, os tiles/LOD, o cache, os pacotes offline e o **fallback sem WebGL** são obrigatórios, não opcionais. **[RECOMENDADO]** orçamento de desempenho (peso de página, tempo até interação) com a versão 2D/estática como linha de base garantida.

### 11.6 Pacotes offline

**[NORMATIVO]** o `OfflinePackage` (Seções 5/9) viabiliza sala sem internet: versionado, assinado, com validade, com política de acesso e licença embutidas, e com o piso epistêmico preservado. É a forma técnica de levar o atlas a contextos sem rede sem relaxar nenhuma garantia.

### 11.7 Modo projetor

**[NORMATIVO]** o `ProjectorModeView` (E10) é sustentado com alto contraste, baixa densidade e legibilidade de rótulos a distância; é misto (sala inteira vê), respeita faixa/mediação e não expõe conteúdo `teacherOnly` na projeção ao aluno sem mediação.

### 11.8 Acessibilidade técnica

**[NORMATIVO]** **acessibilidade não é opcional** (e-MAG/WCAG/LBI — P24): a stack garante equivalente textual para todo visual, navegação por teclado, foco visível, contraste adequado, redundância não-cromática (cor nunca é o único canal), e movimento reduzido quando solicitado. A acessibilidade vale em **todos** os degraus, inclusive offline e projetor.

### 11.9 Equivalentes textuais

**[NORMATIVO]** todo conteúdo visual (globo, mapa, tile, imagem, gráfico, modelo 3D) tem **equivalente textual** que carrega a mesma informação factual e os mesmos rótulos epistêmicos — para leitores de tela, para o degrau estático e para a auditoria.

### 11.10 Fallback sem WebGL

**[NORMATIVO]** sem WebGL/GPU, o sistema **degrada para 2D e depois estático**, nunca quebra: o conteúdo, os rótulos e a navegação temporal continuam disponíveis. WebGL é um luxo de apresentação, não um requisito de acesso ao conhecimento.

### 11.11 Sincronização entre timeline e globo

**[NORMATIVO]** timeline e globo compartilham o **mesmo estado de navegação** (`NavigationState` — E10): mover o tempo move o espaço e vice-versa, mantendo a **simultaneidade global** (D8) — "o que acontecia no mundo neste momento" é coerente entre as duas vistas. **[NORMATIVO]:** a sincronização nunca pode quebrar a versão (mostrar o globo de uma versão e a timeline de outra — R-31): ambas referenciam a mesma versão de conteúdo.

### 11.12 Comparação temporal

**[NORMATIVO]** o `ComparisonView` (E10, A×B / antes-depois) opera sobre `weightedClaimSets` com confiança decaindo e **sem falsa simetria**: a engine apresenta as leituras com seus pesos/fontes, e negacionismo rotulado-rejeitado fica **fora** do par (E5/3.1).

### 11.13 Exportação de imagens/relatórios sem perder citação/incerteza

**[NORMATIVO]** ao exportar uma imagem do globo/timeline ou um relatório, o `ExportPackagingService` embute **fonte, incerteza, natureza do dado, mediação e atribuição**; uma figura exportada nunca vira "imagem solta sem proveniência". A regra **forma muda; fato não** vale também na exportação visual.

### 11.14 Recomendações técnicas conceituais por frente (não decisão final)

| Frente | [RECOMENDADO] | [ALTERNATIVA] | Observação |
|---|---|---|---|
| **Timeline multiescala** | timeline própria sobre canvas/SVG (controle do escalar canônico e dos regimes) | biblioteca de timeline de terceiros adaptada | a régua Ga↔dia e a incerteza são específicas; provável construção própria |
| **Globo/mapa 3D** | engine de globo geoespacial (Cesium/3D Tiles-classe) | biblioteca de camadas geo (deck.gl-classe) sobre WebGL | precisa honrar paleoposição rotulada e degradar para 2D |
| **Mapa 2D / geoespacial de exibição** | renderizador de tiles vetor/raster (MapLibre-classe) | renderizador estático server-side para o degrau estático | base garantida sem GPU |
| **Renderização estática** | imagem + equivalente textual gerados server-side | snapshot estático do 2D | é o piso de acesso (acessibilidade/offline/impressão) |
| **Offline** | `OfflinePackage` assinado com cache local (sem APIs externas) | app empacotado para sala | preserva licença/papel/piso epistêmico |

**[PENDÊNCIA]:** a escolha final de cada biblioteca/engine/formato é da Etapa 12 (MVP), guiada por estas recomendações e obrigada a preservar os invariantes desta etapa.

---

## 12. Auditoria, logs, rastreabilidade e observabilidade (Tarefa 12)

A Etapa 11 já distribuiu, ao longo das Seções 2–11, a obrigação de auditoria por todas as camadas. Esta seção consolida o **plano de auditoria técnica** num único lugar: define a trilha técnica transversal, a relaciona com as trilhas conceituais herdadas, especifica os tipos de log, fixa a cadeia de rastreabilidade e separa **observabilidade** (saúde técnica) de **vigilância** (que esta arquitetura recusa).

### 12.1 `TechnicalAuditTrail` — a trilha técnica transversal

**[NORMATIVO]** o `AuditTrailService` (Seção 3) mantém a `TechnicalAuditTrail`: o registro técnico de **quem/qual serviço fez o quê, sobre qual versão, sob qual política, com qual resultado** — distinto das trilhas de conteúdo porque audita a **infraestrutura e o acesso**, não o mérito pedagógico, de seleção ou factual. Justificativa de não duplicação (Seção 3.17): `OutputAuditTrail`, `MatchingAuditTrail` e `UXAuditTrail` auditam **decisões internas de suas camadas** (como o output foi montado, como o score foi calculado, como a sessão navegou); a `TechnicalAuditTrail` audita **a camada técnica** (acesso, mudança, exportação, cache, licença, erro) e **costura** as demais numa cadeia única de rastreabilidade.

```txt
TechnicalAuditTrail = {
  auditId,
  occurredAt,              # timestamp técnico (UTC), distinto do tempo histórico do conteúdo
  actorRef,                # papel/serviço que agiu (pseudonimizado para usuário escolar — Seção 8)
  actorClass,              # systemAdmin | curator | reviewer | teacher | schoolCoordinator | student | publicViewer | offlineViewer | service
  eventClass,              # acesso | mudanca | exportacao | cache | licenca | erro | permissao
  targetRef,               # artefato/recurso afetado (por referência e versão, nunca o conteúdo sensível embutido)
  contentVersionRef,       # versão de conteúdo envolvida (reprodutibilidade — Seção 5)
  policyApplied,           # AuthorizationPolicy/contexto que autorizou ou negou (Seção 7)
  outcome,                 # autorizado | negado | sucesso | falha | invalidado
  reasonRef,               # gatingReason/licenseRiskLevel/reviewStatus pertinente, quando aplicável
  dataMinimizationClass    # SEM-PII | PSEUDONIMIZADO | AGREGADO  (Seção 8 — nunca PII de menor em claro)
}
```

**[NORMATIVO]:** a `TechnicalAuditTrail` registra **referências e versões**, nunca o conteúdo sensível em si nem PII de menor em claro (R-13); ela é a evidência de que uma garantia foi cumprida, não um repositório paralelo de dados pessoais ou de conteúdo restrito.

### 12.2 Relação com as trilhas conceituais herdadas

| Trilha | Camada dona | O que audita | Relação com a `TechnicalAuditTrail` |
|---|---|---|---|
| `OutputAuditTrail` (E9) | Output | como o `PedagogicalOutput` foi montado, citado, revisado e aprovado | a técnica registra **quando/quem** exportou/serviu/versionou o output; não reescreve a trilha do Output |
| `MatchingAuditTrail` (E8) | Matching | por que um `MatchScore` foi calculado e como o `MatchSet` foi revisado | a técnica registra **acesso e versão** do MatchSet servido; o porquê do score permanece no Matching |
| `UXAuditTrail` (E10) | UX | como a `ExperienceSession` navegou, mediou, degradou e exportou | a técnica registra **acesso/permissão/exportação** da sessão; o relato de experiência permanece na UX |
| `MatchingAuditTrail`/`OutputAuditTrail`/`UXAuditTrail` em conjunto | — | mérito de seleção, forma e experiência | a `TechnicalAuditTrail` é a **espinha** que liga acesso → versão → política, permitindo reconstruir o caminho técnico sem invadir o mérito das demais |

**[NORMATIVO]:** as trilhas **não se sobrescrevem**. Cada uma é fonte da verdade do seu próprio domínio; a técnica as **referencia** por id/versão para compor a rastreabilidade ponta a ponta, jamais as edita.

### 12.3 Tipos de log

**[NORMATIVO]** o sistema mantém, no mínimo, as seguintes classes de log, todas sob a regra de minimização da Seção 8:

- **Logs de acesso** — quem/qual papel acessou qual recurso, sob qual `AuthorizationPolicy`, com `outcome` autorizado/negado (base da defesa contra R-03/R-04/R-13/R-14/R-15).
- **Logs de mudança** — toda transição de versão de conteúdo autoritativo (claim/fonte/cena) e de configuração técnica, com ator e política (reprodutibilidade — Seção 5).
- **Logs de exportação** — todo `ExportPackage`/`OfflinePackage` gerado: o que continha (por referência e versão), qual licença aplicada, quais avisos de mediação/atribuição embutidos (defesa contra R-06/R-17/R-18/R-30).
- **Logs de cache** — qual versão de derivado foi servida e quando foi invalidada (auditoria de versão retornada — Seção 10; defesa contra R-01/R-02).
- **Logs de licença** — toda decisão de armazenamento/exportação por `licenseRiskLevel`, confirmação por asset e bloqueio de expressão NC/SA (Seção 9; defesa contra R-05/R-06).
- **Logs de erro** — falhas técnicas e degradações acionadas, **sem** capturar conteúdo sensível nem PII de menor no payload do erro (defesa contra R-13).
- **Logs de permissão** — mudanças em papéis/políticas e tentativas negadas (defesa contra R-15).

### 12.4 Cadeia de rastreabilidade

**[NORMATIVO]** a arquitetura técnica garante a cadeia completa, em qualquer modo (online, offline, exportado, projetor):

> **artefato → bloco → cena/momento → claim → fonte → licença**

Concretamente: de um `OutputArtifact` exportado chega-se ao `OutputSectionBlock`, dele à `Scene`/`MomentResult` que o originou, dela aos `Claim`/`ClaimSet` referenciados, deles às `Source`/`Citation` e, por fim, ao `LicenseProfile`/`ProvenanceMetadata` do material. **[NORMATIVO]:** essa cadeia **não pode ser quebrada** por cache (Seção 10), por exportação (R-17), por offline (R-30) nem por sincronização de versão (R-31); um material sem caminho de volta à evidência é, por definição, um defeito de arquitetura.

### 12.5 Observabilidade técnica sem capturar dados indevidos

**[NORMATIVO]** observabilidade (latência, taxa de erro, saturação, validade de cache, integridade de pacote, disponibilidade do degrau estático) é **saúde da infraestrutura**, não vigilância do aluno. **[NORMATIVO]:** métricas e *traces* são **agregados ou pseudonimizados**, nunca contêm PII de menor em claro e nunca reconstroem trajetória individual de estudante para fim operacional — isso seria *analytics* operacional, que é **[PENDÊNCIA]** explícita da Etapa 14 (R-28). A separação da Seção 8 (identidade × sessão × pedagógico) vale também para a telemetria.

### 12.6 Evidências para revisão jurídica e de compliance

**[NORMATIVO]** a `TechnicalAuditTrail` mais os logs de licença/exportação/mudança constituem o **dossiê de evidência** para o `legalReviewer` e para auditoria de conformidade: permitem demonstrar que um item `legal-review`/`rejected` nunca foi exibido como fato (invariante de exibição), que expressão NC/SA nunca foi exportada fora do permitido, que o consentimento/controle escolar (quando definido na Etapa 14) foi respeitado, e que a minimização de dados de menores foi observada. **[NORMATIVO]:** essa evidência é **referencial e versionada** — comprova o cumprimento sem virar repositório de PII.

### 12.7 Auditoria de acessibilidade futura

**[RECOMENDADO]** registrar, de forma auditável, a presença de equivalente textual, navegação por teclado, contraste e redundância não-cromática por vista/artefato, preparando a **auditoria técnica de acessibilidade** (ASES/e-MAG) que a Etapa 14 conduzirá. **[PENDÊNCIA]:** a auditoria de acessibilidade formal, os testes com tecnologia assistiva e o laudo são da Etapa 14; a Etapa 11 garante apenas que os **ganchos de auditoria** existam e que **acessibilidade não seja opcional** (R-37) na fundação técnica.

---

## 13. Invariantes técnicos da Etapa 11 (Tarefa 13)

Os invariantes abaixo são **[NORMATIVO]** e **inegociáveis**: nenhuma implementação (Etapa 12), nenhum pipeline de ingestão (Etapa 13) e nenhuma operação (Etapa 14) pode violá-los sem reabrir formalmente esta etapa. Eles consolidam, num só lugar, as garantias distribuídas pelas Seções 1–12. A numeração é estável e referenciada em outras seções.

1. **A arquitetura não cria fato.** Infraestrutura, serviços, bancos, caches e índices **materializam e servem** conhecimento; nenhum deles **origina** verdade factual. Fato só nasce do pipeline de curadoria sobre o Knowledge Core (Seções 1–2).
2. **Cache não é fonte.** `cache não é verdade`: todo `CacheEntry` tem `originClass = derivado`, carrega o conjunto de versões que o originou e é descartável; servir derivado vencido como fato é violação (Seção 10; R-01/R-02).
3. **Índice semântico não é fonte.** `busca/embedding não é verdade`: índices textual e vetorial devolvem **ponteiros** para o autoritativo, têm `carriesProvenance = false` e são reconstruíveis; *embedding*/IA jamais respondem um fato sem reidratar o claim e seus rótulos (Seção 10; R-07/R-09).
4. **UX não escreve no Knowledge Core.** A `DesignUX3DLayer` apresenta e opera; nunca grava `Claim`/`reviewStatus`/`publicabilityStatus` (Seções 2, 7; E10).
5. **Output não escreve no Knowledge Core.** A `PedagogicalOutputLayer` compõe forma sobre conteúdo aprovado; nunca altera o núcleo (Seções 2, 6; E9).
6. **Matching não altera claim.** O `ContentMatchingEngine` calcula relevância (`MatchScore`); `score não é verdade` e nunca reescreve claim/`reviewStatus` (Seções 2, 6; E8; R-08).
7. **Compliance não altera claim.** A `BrazilianEducationComplianceLayer` só **endurece** (faixa/sensível/visibilidade); alinhamento não é selo e nunca edita fato (Seções 2, 6; E6; R-23).
8. **Planning não altera claim.** A `TeacherSchoolPlanningLayer` organiza intenção pedagógica; nunca escreve no núcleo (Seções 2, 6; E7).
9. **`pending`/`legal-review`/`rejected` não aparece como fato.** Invariante de exibição: itens nesses estados nunca chegam ao aluno/público como fato — em nenhuma vista, cache, índice, exportação ou pacote offline (Seções 5, 7, 10; R-03).
10. **Exportação respeita licença.** Nenhum `ExportPackage` reproduz expressão que a licença não permite; fonte, incerteza, mediação e atribuição são embutidas (Seção 9; R-06/R-17/R-18).
11. **Pacote offline respeita licença, publicabilidade, mediação e papel.** `offline não pode relaxar licença, publicabilidade, mediação ou papel`: o `OfflinePackage` leva a política embutida e nada `teacherOnly`/`internalReviewOnly`/`pending`; a ausência de rede nunca abre o que a política fecharia online (Seções 8, 9; R-11/R-30).
12. **Dados de aluno não entram no Knowledge Core.** O núcleo não precisa e não recebe PII de aluno; identidade/sessão/pedagógico ficam separados e minimizados (Seção 8; R-13).
13. **IA não é fonte factual.** Modelos podem ajudar a adaptar **forma** (linguagem, layout); nenhuma saída de IA é tratada como evidência ou claim (Seções 2, 8; E10; R-07).
14. **Toda exibição pública preserva fonte e incerteza.** `forma muda; fato não`: qualquer leitura factual sai com `claimType`/`confidenceLevel`/`evidenceLevel`, proveniência e estado de revisão — nunca o "texto pelado" (Seções 6, 10; R-09/R-17).
15. **Toda sessão respeita papel e permissão.** RBAC+ABAC sobre `ViewerRole`/`visibilityClass`/`SchoolUseMode` governa cada acesso, online ou offline (Seção 7; R-04/R-15).
16. **Toda versão exportada é auditável.** Todo `ExportPackage`/`OfflinePackage` registra as versões de conteúdo que o compõem, permitindo reconstrução e auditoria posteriores (Seções 5, 12; R-22).
17. **Todo asset tem licença por asset.** Cada `MediaAsset`/`MapAsset`/`GeometryVersion` carrega `LicenseProfile`/`ProvenanceMetadata` e um `LicenseStorageBinding`; não há asset "órfão de licença" (Seção 9; R-06).
18. **ShareAlike/ODbL fica fisicamente isolado.** `licença governa expressão/asset, não o fato recodificado`: SA/ODbL vivem no `IsolatedLicenseStore`, nunca misturados ao núcleo, com atribuição e *share-alike* preservados na exportação (Seção 9; R-05).
19. **NC não entra como expressão.** Conteúdo *non-commercial* nunca é reproduzido como expressão no produto; quando muito, o **fato recodificado** entra com fonte própria, sem o asset (Seção 9; R-06).
20. **API não permite escrita indevida.** Nenhum `ApiContract` permite que UX/Output/Matching/Planning/Compliance gravem `Claim`/`reviewStatus`/`publicabilityStatus`/`confidenceLevel`/`claimType`; escrita autoritativa só pelo pipeline (Seção 6; R-16).
21. **Logs minimizam dados pessoais.** A `TechnicalAuditTrail` e todos os logs registram referências e versões com `dataMinimizationClass`; nunca PII de menor em claro (Seções 8, 12; R-13).
22. **Fallback preserva o piso epistêmico.** `degradação técnica nunca remove o piso epistêmico`: 3D → 2D → estático → offline → projetor mantém fonte, incerteza, natureza do dado, mediação e atribuição em cada degrau (Seção 11; R-19).
23. **Acessibilidade não é opcional.** e-MAG/WCAG/LBI são fundação: equivalente textual, teclado, foco visível, contraste e redundância não-cromática valem em todos os modos (Seção 11; R-37).
24. **A stack não substitui a arquitetura conceitual.** Toda tecnologia nomeada é `[RECOMENDADO]`/`[ALTERNATIVA]`; o normativo é a propriedade arquitetural, e trocar de produto não pode quebrar invariante (Seções 1, 4, 11; R-21/R-25).
25. **A Etapa 11 não propõe MVP.** Esta etapa fixa o **PlanoArquitetural**; recorte mínimo (E12), povoamento (E13) e operação (E14) são planos distintos e posteriores (Seções 1, 15; R-26).
26. **Derivado é reconstruível e não carrega proveniência.** Todo índice/cache é reconstruível a partir do autoritativo e nunca é a origem da proveniência; perder um derivado nunca perde verdade (Seção 10).
27. **O isolamento de licença vale em todo o caminho.** O isolamento físico de SA/ODbL/NC/proprietário é honrado também em cache, índice, exportação e offline — não só no *storage* primário (Seções 9, 10, 11; R-05/R-06).
28. **A sincronização nunca serve versões divergentes.** Timeline e globo compartilham `NavigationState` e a mesma versão de conteúdo; nunca se exibe o globo de uma versão com a timeline de outra (Seção 11; R-31).
29. **`sourceTimeBasis` nunca é apagado.** A base temporal nativa de cada fonte é preservada; `canonicalTimeScalar` é **derivado** com datum fixo (E3Z) e auditável, nunca sobrescreve a base original (Seções 5, 11; R-32).
30. **Nenhum plano relaxa invariante de outro.** PlanoArquitetural, PlanoImplementacao e PlanoOperacional são separados, mas a implementação e a operação **herdam** e não podem afrouxar nenhum invariante desta etapa (Seções 1, 15; R-26).

---

## 14. Riscos técnicos, jurídicos, educacionais e operacionais (Tarefa 14)

A tabela consolida os riscos referenciados ao longo das Seções 1–13. Os códigos `R-01`…`R-37` são estáveis e citados em outras seções. Cada risco traz a mitigação arquitetural correspondente; toda mitigação remete a um invariante (Seção 13) e/ou a uma decisão `[NORMATIVO]`.

| Código | Risco | Mitigação arquitetural |
|---|---|---|
| **R-01** | Cache desatualizado servindo fato vencido | `CacheEntry` com `inputVersionSet` e `InvalidationRule`; `cache não é verdade`; invalidação por mudança de claim/source/versão (Seção 10; invariante 2) |
| **R-02** | Cache servindo item revogado/`rejected` como fato | invalidação imediata por `reviewStatusChanged`/`publicabilityChanged`; um item despublicado some do cache; auditoria de versão servida (Seção 10; invariantes 2/9) |
| **R-03** | Vazamento de `pending`/`legal-review`/`rejected` (e `hiddenItems`) como fato | invariante de exibição imposto por ABAC em toda vista/cache/índice/export/offline; estados não exibíveis nunca chegam ao aluno/público (Seções 5, 7, 10; invariante 9) |
| **R-04** | Vazamento de `teacherOnly` ao aluno | `visibilityClass`/`SchoolUseMode = teacher`; a face do aluno nunca recebe aparato `teacherOnly`; vale online e offline (Seção 7; invariante 15) |
| **R-05** | Licença ShareAlike/ODbL contaminando o núcleo | `IsolatedLicenseStore` + `LicenseStorageBinding`; `licença governa expressão/asset, não o fato`; SA/ODbL nunca misturados ao KC (Seção 9; invariantes 18/27) |
| **R-06** | NC/expressão exportada ou empacotada indevidamente | bloqueio de reprodução de expressão NC; matriz `licenseRiskLevel → exportação`; export/offline respeitam licença (Seção 9; invariantes 10/11/19) |
| **R-07** | *Embedding*/índice vetorial tratado como verdade/fonte | índice vetorial é `[ALTERNATIVA]`/`[PENDÊNCIA]`, `carriesProvenance = false`, devolve ponteiros; IA nunca é fonte factual (Seção 10; invariantes 3/13) |
| **R-08** | `MatchScore` (relevância) virando critério de exibição factual | `score não é verdade`; Matching não altera claim; relevância nunca vira confiança (Seção 6; invariantes 6/14; E8) |
| **R-09** | Busca textual omitindo incerteza ("respondendo um fato") | busca devolve ponteiros e a exibição reidrata `claimType`/`confidenceLevel`/proveniência; nunca "texto pelado" (Seção 10; invariantes 3/14) |
| **R-10** | Paleomapa tratado como fato | paleogeografia rotulada como `reconstrução modelada` via `paleoPositionPolicy`; tiles isolados com atribuição; nunca apresentada como medição (Seção 11; invariante 22; E10) |
| **R-11** | Pacote offline desatualizado | `OfflinePackage` versionado, assinado, com validade; pacote vencido **avisa** e/ou expira, nunca finge ser a versão atual (Seções 5, 9; invariante 11) |
| **R-12** | Globo 3D sugerindo precisão espacial falsa | rótulos de incerteza espacial e de natureza do dado; redundância não-cromática; reconstrução marcada como tal; degradação preserva o rótulo (Seção 11; invariantes 14/22) |
| **R-13** | Logs/telemetria capturando PII de menor | `dataMinimizationClass` (SEM-PII/PSEUDONIMIZADO/AGREGADO); `menores exigem minimização máxima de dados`; payload de erro sem conteúdo sensível (Seções 8, 12; invariante 21) |
| **R-14** | Autenticação fraca permitindo acesso indevido | `IdentityAccessService` com autenticação forte por papel; **[PENDÊNCIA]** de mecanismo concreto para E12/E14, sob o invariante de que sessão respeita papel (Seção 7; invariante 15) |
| **R-15** | Permissão mal configurada | `AuthorizationPolicy` declarativa e auditável; ponto de decisão único (online/offline/export); logs de permissão e negação (Seções 7, 12; invariante 15) |
| **R-16** | API permitindo escrita indevida no núcleo | `ApiContract` com `sideEffectClass`; escrita autoritativa só pelo pipeline; camadas externas só leem o KC (Seção 6; invariante 20) |
| **R-17** | Exportação sem fonte/incerteza | `ExportPackagingService` embute `OutputCitationBundle`/incerteza/mediação/atribuição; figura/relatório nunca vira material "solto" (Seções 9, 11; invariantes 10/14) |
| **R-18** | Exportação sem mediação (ou expressão NC/SA fora do permitido) | aviso de mediação obrigatório quando há sensível; matriz de exportação por `licenseRiskLevel`; `forma muda; fato não` na exportação visual (Seção 9; invariantes 10/22) |
| **R-19** | UX sem fallback (quebra sem 3D) | `ViewDegradationLadder` 3D → 2D → estático; o conteúdo e a navegação temporal sobrevivem sem WebGL (Seção 11; invariante 22) |
| **R-20** | Hardware escolar insuficiente | tiles/LOD, cache, pacotes offline, fallback estático e orçamento de desempenho com a versão 2D/estática como linha de base garantida (Seção 11; invariante 22) |
| **R-21** | *Vendor lock-in* | toda tecnologia é `[RECOMENDADO]`/`[ALTERNATIVA]` sobre uma propriedade arquitetural `[NORMATIVO]`; substituível sem quebrar invariante; formatos abertos preferidos (Seções 1, 4, 11; invariante 24) |
| **R-22** | Ausência de trilha de auditoria | `TechnicalAuditTrail` + logs de acesso/mudança/exportação/cache/licença; toda versão exportada é auditável (Seção 12; invariante 16) |
| **R-23** | Confusão entre homologação e alinhamento | `BNCCMapping`/`CurricularAlignment` exibidos como **alinhamento**, nunca como selo MEC/PNLD; nota explícita no viewer e no `ExportPackage` (Seção 6; invariante 7; E6/E10) |
| **R-24** | Custo de infraestrutura insustentável | derivados reconstruíveis e descartáveis, *storage* por classe de dado, degradação que reduz carga, formatos abertos; decisão de escala é **[PENDÊNCIA]** da Etapa 14 (Seções 4, 10; invariante 26) |
| **R-25** | Engenharia violar a direção de dependência | direção `Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core → Sources/Provenance` imposta por contratos e permissões; escrita reversa é *bug* (Seções 1, 2, 6; invariantes 4–8/20) |
| **R-26** | MVP futuro cortar invariantes | os 30 invariantes são `[NORMATIVO]`; o recorte mínimo da Etapa 12 escolhe **o que** entregar, nunca **relaxar** uma garantia (Seções 1, 15; invariantes 25/30) |
| **R-27** | Ingestão futura burlar o portão de licenças | o `ingestionDecision`/portão da Etapa 1.1 é vinculante; a Etapa 13 popula **através** do portão, com confirmação por asset; nada entra sem `LicenseProfile` (Seção 9; invariantes 17/18; E1.1) |
| **R-28** | *Analytics* futuro capturar dado pessoal | observabilidade é agregada/pseudonimizada; *analytics* operacional individual é **[PENDÊNCIA]** explícita da Etapa 14, sob minimização e separação de identidade (Seções 8, 12; invariante 21) |
| **R-29** | LMS futuro misturar identidade e conteúdo | separação identidade × sessão × pedagógico mantida na integração; o LMS recebe conteúdo por referência, nunca funde PII ao núcleo; **[PENDÊNCIA]** de desenho na Etapa 14 (Seção 8; invariantes 12/15) |
| **R-30** | Offline permitindo acesso a conteúdo restrito | política embutida no `OfflinePackage`; o `offlineViewer` só vê o que o papel permitia online; nada restrito é empacotado (Seções 8, 9; invariante 11) |
| **R-31** | Sincronização quebrando versão | timeline e globo referenciam a **mesma** versão de conteúdo via `NavigationState`; nunca versões divergentes entre as vistas (Seção 11; invariante 28) |
| **R-32** | Erro de datum temporal | `canonicalTimeScalar` derivado com datum fixo (E3Z) e auditável; `sourceTimeBasis` nativo nunca apagado; conversões registradas (Seções 5, 11; invariante 29) |
| **R-33** | Desempenho do grafo (travessia/proveniência por aresta) | grafo `[RECOMENDADO]` para o núcleo com índices de travessia; `[ALTERNATIVA]` relacional com tabelas de aresta se a travessia for resolvida; derivados aliviam leitura (Seção 4; invariantes 1/26) |
| **R-34** | Erro geoespacial em `ModernCorrespondence` | índice geoespacial dedicado (PostGIS-classe); correspondência moderna rotulada e auditável; transformações de CRS registradas (Seções 4, 11; invariante 29; E10) |
| **R-35** | Erro de *timezone*/calendário | tempo técnico (UTC) separado do tempo histórico do conteúdo; calendários históricos tratados no `displayTime`, nunca confundidos com o `occurredAt` técnico (Seções 5, 12; invariante 29) |
| **R-36** | Escalabilidade de assets 3D/tiles | *object storage* (S3-classe) + CDN para tiles/3D, com LOD e cache; assets pesados servidos por referência e versão, fora do banco autoritativo (Seções 4, 10, 11; invariante 26) |
| **R-37** | Falha de acessibilidade técnica | `acessibilidade não é opcional` (e-MAG/WCAG/LBI): equivalente textual, teclado, foco, contraste e redundância não-cromática em todo degrau; ganchos de auditoria preparados (Seção 11; invariante 23) |

**[NORMATIVO]:** esta lista é **mínima e viva** — a Etapa 12 (MVP), a Etapa 13 (ingestão) e a Etapa 14 (operação) herdam estes riscos e suas mitigações, e nenhuma delas pode "resolver" um risco **relaxando** o invariante que o contém.

---

## 15. Encerramento e handoff para a Etapa 12 (Tarefa 15)

### 15.1 O que esta etapa entrega

A Etapa 11 entrega a **arquitetura técnica de referência** da `TechnicalArchitectureLayer`: a definição da camada como **infraestrutura, serviços, persistência, versionamento, segurança, privacidade, APIs, cache e isolamento de licenças** — externa a todo conteúdo e a toda experiência, que **materializa** o que as camadas conceituais decidiram sem **nunca** criar conhecimento nem inverter a soberania do Knowledge Core; a separação explícita de três planos (**PlanoArquitetural** desta etapa, **PlanoImplementacao** da Etapa 12/13 e **PlanoOperacional** da Etapa 14) e a convenção de estatuto das decisões (**[NORMATIVO]**/**[RECOMENDADO]**/**[ALTERNATIVA]**/**[PENDÊNCIA]**), com tecnologias concretas sempre como recomendação ou alternativa e nunca como norma; o papel técnico na cadeia completa **Experience/UX → Output → Matching → Planning → Compliance → Knowledge Core → Sources/Provenance**, com as matrizes de leitura/escrita, as escritas proibidas, as escritas que exigem curadoria humana e as barreiras que impedem cache, busca textual, *embedding* ou IA de substituir o grafo de claims; quinze domínios técnicos / *bounded contexts* (`KnowledgeCoreService`, `SourceProvenanceService`, `LicenseComplianceService`, `SceneMomentService`, `BrazilianComplianceService`, `PlanningService`, `MatchingService`, `PedagogicalOutputService`, `ExperienceSessionService`, `AssetMediaService`, `ExportPackagingService`, `IdentityAccessService`, `AuditTrailService`, `CacheInvalidationService`, `OfflinePackageService`), cada um com responsabilidade, leituras, escritas, escritas proibidas, dependências e riscos, mais a justificativa de não duplicação das entidades técnicas novas; um modelo de persistência conceitual (grafo com proveniência por aresta para o núcleo, relacional/documental para camadas externas, índice geoespacial, índice temporal canônico, busca textual/semântica que não vira fonte, *object storage* de mídia, `IsolatedLicenseStore` para licenças restritivas) com a separação entre dado autoritativo e índice derivado e a tabela tipo de dado → armazenamento → motivo → risco; o regime de versionamento, `DatasetSnapshot` imutável, versão de conteúdo × versão de renderização, validade/cache e invalidação de `MomentResult`/`MatchSet`/`PedagogicalOutput`, registro de `sourceTimeBasis` e auditabilidade do material exportado; uma arquitetura de APIs internas com treze contratos conceituais (entrada, saída, camada dona, leitura/escrita, riscos e invariantes), todos sob a regra de que **nenhuma escrita autoritativa ocorre fora do pipeline**; um modelo de segurança RBAC+ABAC com onze papéis, a imposição da visibilidade professor × estudante, o bloqueio de `teacherOnly`/`internalReviewOnly`, a proteção de `pending`/`legal-review`/`rejected`, a trilha de acesso e as permissões em modo offline; a engenharia de privacidade (LGPD/ECA): núcleo sem PII de aluno, minimização por padrão, dados agregados de turma, separação identidade × sessão × pedagógico, minimização máxima para menores, pseudonimização, logs sem conteúdo sensível e a proibição de usar dados de aluno para treinar modelo ou gerar fato; a resolução técnica do problema de licenças pendente desde a Etapa 1/1.1/2 — isolamento físico de ShareAlike/ODbL/NC/proprietário, separação entre fato recodificado e expressão licenciada, *storage* por asset com `LicenseProfile`/`LicenseStorageBinding`, confirmação por asset, bloqueio de expressão NC e a matriz `licenseRiskLevel 0–5 → armazenamento → exportação → risco`; o regime de cache/busca/índices/invalidação com `CacheEntry`/`DerivedIndex`/`InvalidationRule`, invalidação por claim/source/license/`reviewStatus`/`publicabilidade` e a recusa do *embedding* como fonte; a sustentação técnica da timeline, do globo 3D, do 2D, do estático, do projetor e do offline, com separação engine × dados, tiles/LOD, `paleoPositionPolicy`, a escada de degradação **3D → 2D → estático → offline → projetor** preservando o piso epistêmico, desempenho em hardware modesto, acessibilidade técnica (e-MAG/WCAG/LBI), equivalentes textuais, *fallback* sem WebGL, sincronização timeline↔globo na mesma versão e exportação que não perde citação/incerteza, com uma recomendação técnica conceitual por frente; o plano de auditoria (`TechnicalAuditTrail` e sua relação com `OutputAuditTrail`/`MatchingAuditTrail`/`UXAuditTrail`), os tipos de log, a cadeia de rastreabilidade **artefato → bloco → cena/momento → claim → fonte → licença** e a observabilidade sem vigilância; **trinta invariantes técnicos** e **trinta e sete riscos com mitigação**. Nada aqui escreve código de aplicação, implementa API real, cria banco real, propõe MVP, popula dados reais, cria claim/cena, mapeia BNCC em massa, altera verdade factual ou qualquer enum de estado (`reviewStatus`/`publicabilityStatus`/`claimType`/`confidenceLevel`/`evidenceLevel`/`MatchScore`/`matchSetStatus`/`outputStatus`/`sceneCompletenessLevel`), promete homologação MEC/PNLD, cria *analytics* operacional, define operação comercial, usa PII real de aluno ou trata IA como fonte factual. A direção única de dependência permanece preservada.

### 15.2 O que a Etapa 12 deverá fazer

A **Etapa 12 — MVP** receberá esta arquitetura técnica de referência e escolherá o **recorte mínimo viável**: quais serviços, quais bancos/índices, quais contratos de API, quais vistas/modos e qual fatia de conteúdo entram no primeiro corte — **escolhendo o que entregar primeiro, jamais relaxando um invariante** (Seção 13). É na Etapa 12 que as **[PENDÊNCIAS]** técnicas desta etapa começam a ser decididas: a escolha final de banco/grafo, de engine de globo, de biblioteca de timeline, de renderizador 2D/estático, de mecanismo de busca (e se haverá índice vetorial), de formato de `ExportPackage`/`OfflinePackage` e do mecanismo concreto de autenticação. A **Etapa 13 — Pipeline de ingestão/povoamento** alimentará o núcleo com dados reais **através** do portão de licenças da Etapa 1.1 (confirmação por asset, `DatasetSnapshot`, `LicenseProfile`), sem burlar o portão (R-27). A **Etapa 14 — Operação, governança, QA e escala** definirá retenção/descarte, fluxo de consentimento/controle escolar, DPIA/relatório de impacto, *analytics* operacional agregado, integração LMS (mantendo identidade e conteúdo separados — R-29), QA pedagógico, auditoria técnica de acessibilidade (ASES) e a validação escolar/jurídica/comercial — incluindo qualquer decisão sobre PNLD/compra pública.

### 15.3 O que a Etapa 11 ainda **não** fez (e por quê)

Não escreveu código, não implementou API real, não criou banco real e não desenhou o esquema físico final (Etapa 12/13); não escolheu o recorte do MVP nem fixou produto/biblioteca/engine/formato — tudo permaneceu como `[RECOMENDADO]`/`[ALTERNATIVA]`/`[PENDÊNCIA]` (Etapa 12); não fez ingestão nem povoou o núcleo, não criou `Claim`/`Source`/`Scene` nem qualquer conhecimento (Etapa 13); não criou *analytics* operacional, não desenhou o LMS, não fixou retenção/descarte, não produziu DPIA, não conduziu auditoria de acessibilidade nem validou/prometeu adoção ou homologação (Etapa 14); não alterou `reviewStatus`/`publicabilidade`/`claimType`/`confidenceLevel`/`evidenceLevel`/`MatchScore`/`matchSetStatus`/`outputStatus`/`sceneCompletenessLevel`; não usou IA como fonte factual; e não usou dado pessoal real de aluno. Tudo isso é contingente ou pertence a etapas próprias; a arquitetura técnica permanece **camada de sustentação** externa ao núcleo, que materializa sem originar.

### 15.4 Decisões vinculantes, recomendações e pendências a carregar

**[NORMATIVO] — vinculante:** a existência e a fronteira da `TechnicalArchitectureLayer`; a direção de dependência e as escritas proibidas; a separação dos três planos; as propriedades arquiteturais de persistência (autoritativo × derivado; proveniência por aresta; `IsolatedLicenseStore`); a imutabilidade de `DatasetSnapshot` e a auditabilidade de todo material exportado; a regra de que nenhuma API escreve fato fora do pipeline; o modelo RBAC+ABAC e a imposição de visibilidade/papel online e offline; a engenharia de privacidade e a minimização máxima para menores; o isolamento físico de licenças e a matriz por `licenseRiskLevel`; a recusa de cache/busca/*embedding*/IA como fonte; a escada de degradação com piso epistêmico e a acessibilidade como fundação; a cadeia de rastreabilidade; e os trinta invariantes da Seção 13.

**[RECOMENDADO]/[ALTERNATIVA] — preferências substituíveis:** os nomes de tecnologias por frente (grafo/relacional, PostGIS-classe, Cesium/3D Tiles-classe, MapLibre-classe, *object storage* S3-classe, RDF*/*property graph*), aceitáveis enquanto preservarem os invariantes.

**[PENDÊNCIA] — a carregar:** escolha final de cada produto/biblioteca/engine/formato (E12); mecanismo concreto de autenticação (E12/E14); adoção ou não de índice vetorial (E12); retenção/descarte, consentimento/controle escolar, DPIA, *analytics* operacional agregado e integração LMS (E14); auditoria formal de acessibilidade — ASES (E14); e o resíduo curatorial herdado das Etapas 6/8/9 — os `BNCCMapping`/`CurricularAlignment` concretos seguem `pending` até confirmação com o texto homologado, e esta etapa apenas **os exibe como alinhamento e respeita o `reviewStatus`**, sem resolvê-los.

**Handoff:** com a Etapa 11 (v1.0) aprovada, a **Etapa 12 — MVP** pode ser executada, recebendo uma arquitetura técnica suficientemente clara para escolher o recorte mínimo viável **sem quebrar invariantes** — preservando a soberania do Knowledge Core, a direção única de dependência, a proveniência até a fonte, o isolamento físico de licenças, o versionamento e a auditabilidade, a engenharia de privacidade e a minimização para menores, a degradação graciosa com piso epistêmico, a acessibilidade como fundação e a recusa de qualquer derivado (cache, índice, *embedding*, IA) como fonte de verdade.

*Documento de entrega da Etapa 11 (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8, 9, 10). Define somente a arquitetura técnica de referência. Não escreve código, não implementa API real, não cria banco real, não propõe MVP, não escolhe produto/biblioteca/engine/formato final, não faz ingestão, não popula o Knowledge Core, não cria claim/cena, não mapeia BNCC, não altera verdade factual nem qualquer enum de estado, não promete homologação MEC/PNLD, não cria analytics operacional, não define operação comercial, não usa IA como fonte factual e não usa dados pessoais reais de alunos. Próxima etapa, quando solicitada: Etapa 12 — MVP.*
