# Etapa 14 — Operação, Governança, QA, Escala, Analytics Agregado, LMS e Validação

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 14** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8), a `PedagogicalOutputLayer` (Etapa 9), a `DesignUX3DLayer` (Etapa 10), a `TechnicalArchitectureLayer` (Etapa 11), o `MVPRelease` (Etapa 12) e o `IngestionPopulationPipeline` (Etapa 13) · 14/06/2026

**Natureza desta etapa.** Documento de **arquitetura operacional, governança e garantia de qualidade**. Define **como o produto opera depois do MVP e do pipeline real de ingestão** — como QA contínuo executa e bloqueia, como os dez papéis humanos são governados em filas/turnos/escalonamento/SLAs, como a escala de povoamento avança sem baixar o piso epistêmico, como analytics mede a operação sem coletar PII de aluno, como um LMS consome conteúdo publicável sem escrever fato, como a validação escolar/jurídica/comercial é conduzida sem prometer homologação, como incidentes são contidos e revertidos por versão, como fontes vivas e reprocessamento são versionados, e como a cobertura/lacunas/riscos são monitorados — **sem criar conhecimento novo, sem alterar claims, sem relaxar licenças, sem coletar PII de aluno e sem transformar analytics, LMS, cache, busca, IA ou dashboard em fonte factual**. Conforme solicitado, esta etapa **não** escreve código; **não** implementa ferramentas reais; **não** roda testes reais; **não** faz scraping; **não** baixa fontes; **não** popula banco; **não** cria novos `Claim`/`Source`/`Citation`/`Scene`/`Relationship`; **não** altera as cenas-gabarito; **não** altera a Etapa 13; **não** mapeia BNCC em massa; **não** trata BNCC como fonte factual; **não** coleta dados pessoais reais de alunos; **não** cria analytics individualizado de aluno; **não** cria um LMS próprio completo; **não** promete homologação MEC, aprovação PNLD ou validação jurídica definitiva; **não** permite que operação, comercial, escola, professor, LMS, IA, cache, busca ou dashboard escrevam fatos no Knowledge Core; e **não** permite que pressão comercial destrave item bloqueado. Ela **pode**, porém: definir a camada operacional, o programa de QA contínuo, o modelo de governança dos papéis, os estados/filas/SLAs/escalonamento, a estratégia de escala sob piso, o framework de analytics agregado, o contrato de integração LMS por consumo, o programa de validação por evidência, a gestão de incidentes e rollback versionado, a política de fontes vivas/reprocessamento, o monitoramento de cobertura, e o handoff para uma eventual Etapa 15 (plano comercial, piloto, parcerias, captação, procurement, go-to-market).

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Papéis humanos em `camelCase` (ex.: `ingestionCurator`). Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "O KC" = o Knowledge Core (Etapa 2). "O portão" = o checklist/portão de licenças da Etapa 1.1. "O pipeline" = o `IngestionPopulationPipeline` (Etapa 13). "A arquitetura técnica" = a `TechnicalArchitectureLayer` (Etapa 11). "O MVP" = o `MVPRelease` (Etapa 12). "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "A operação" = a `OperationalGovernanceLayer` definida na Seção 1. Referências cruzadas: "invariante N" = invariante técnico N da Etapa 11 (§13); "`T-13.NN`" = teste de invariante da Etapa 13 (§14.1); "`R-13.NN`" = risco da Etapa 13 (§14.2); "princípio N" = princípio de ingestão N da Etapa 13 (§2); "`T-*`" = teste de aceite do MVP (Etapa 12, §13).

> **Convenção de estatuto das decisões (herdada das Etapas 11/12/13).** **[NORMATIVO]** = vinculante, não pode ser violado sem reabrir a etapa; **[RECOMENDADO]** = opção preferida, substituível por equivalente que preserve os invariantes; **[ALTERNATIVA]** = opção aceitável citada para comparação; **[PENDÊNCIA]** = decisão deliberadamente adiada (para a Etapa 15 ou para a execução), registrada para ser carregada. Nomes de tecnologias, padrões de mercado e números concretos (SLAs, percentuais de amostragem, cadências), quando aparecem, são sempre **[RECOMENDADO]**/**[ALTERNATIVA]**, nunca **[NORMATIVO]**: o normativo é a propriedade operacional (ex.: "QA bloqueia, não sugere"), não o valor que a realiza.

> **Regra central desta etapa.** A operação **serve ao núcleo; não o governa**. A `OperationalGovernanceLayer` é o conjunto disciplinado de QA, governança, filas, auditoria, escala, analytics, integração e validação que **mantém o pipeline (E13) funcionando e o conteúdo publicável (E11/E12) sendo consumido** — sem nunca virar caminho de escrita factual nem afrouxar uma garantia. A pergunta que esta etapa responde: *"Como o Atlas do Tempo 3D opera, audita, escala e valida em produção — medindo a si mesmo, integrando-se a LMS e preparando o mercado — sem permitir que volume, prazo, pressão comercial, automação, analytics, cache, busca, IA ou um sistema externo se tornem verdade factual, relaxem licença ou exponham dados de menores?"* Quatro frases-síntese governam todo o documento: **QA bloqueia, não sugere**; **escala nunca reduz revisão**; **analytics mede a operação, nunca o aluno individualmente**; **LMS consome conteúdo publicável, não escreve fato**. E, abrangendo tudo: **qualquer dúvida de fonte, licença, claim, data, geometria, sensibilidade, acessibilidade ou privacidade resulta em bloqueio/revisão, nunca em publicação automática.** Permanecem canônicas e invioláveis: **forma muda; fato não**; **score não é verdade**; **cache não é verdade**; **busca/embedding não é verdade**; **dashboard/relatório não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**; **correção cria versão, nunca apaga**.

---

## Sumário

1. Definição da `OperationalGovernanceLayer`
2. Princípios operacionais
3. Papéis, governança e responsabilidades
4. Estados operacionais, filas e SLAs
5. QA contínuo e execução dos testes `T-13.NN`
6. Auditoria, trilhas de decisão e relatórios
7. Escala de povoamento e controle de qualidade
8. Analytics agregado sem PII
9. Integração LMS e exportações controladas
10. Validação escolar, jurídica e comercial
11. Gestão de incidentes e rollback versionado
12. Atualização de fontes vivas, snapshots e reprocessamento
13. Monitoramento de cobertura, lacunas e riscos
14. Riscos operacionais e mitigação
15. Encerramento e handoff para a Etapa 15

---

## 1. Definição da `OperationalGovernanceLayer`

### 1.1 O que a operação é

A **`OperationalGovernanceLayer`** é a **camada operacional do produto**: o conjunto disciplinado de programas de QA, modelo de governança de papéis, estados/filas/SLAs, auditoria, política de escala, framework de analytics agregado, contrato de integração LMS, programa de validação e gestão de incidentes por meio do qual o Atlas do Tempo 3D **opera em produção de forma governada, testável, auditável e escalável**. Ela é a contraparte operacional de três peças já fixadas: o **pipeline (E13)**, que define como o fato entra no núcleo; a **arquitetura técnica (E11)**, que define onde e sob quais invariantes; e o **MVP (E12)**, que define o recorte mínimo verificável. Onde a Etapa 13 define **por qual processo e por quais mãos** o conteúdo entra, a Etapa 14 define **como esse processo é mantido em pé, medido, auditado, escalado e validado** ao longo do tempo, sem que a operação se torne ela própria uma fonte.

A operação é o **PlanoOperacional** anunciado e reservado desde a Etapa 11 (invariante 30; §15): um plano **separado** do PlanoArquitetural (E11) e do PlanoImplementacao (E12/E13), que **herda** e **não pode afrouxar** nenhum invariante dos planos anteriores. Ela ocupa exatamente o espaço que o MVP lhe entregou (E12, §15.5) e que a Etapa 13 lhe transferiu (E13, §15.5): QA contínuo sobre a matriz `T-13.NN`, governança dos dez papéis, condução de `P3-scale`, analytics operacional agregado, integração LMS com identidade separada e validação escolar/jurídica/comercial — inclusive qualquer decisão sobre PNLD/compra pública.

### 1.2 O que a operação **não** é

A operação **não é** uma fonte de verdade: ela não "produz" nem "corrige" fatos; ela governa o processo que os faz atravessar sob curadoria. Ela **não é** um caminho de escrita no KC — analytics, LMS, dashboard, cache, busca e IA permanecem **leitores/derivados**, jamais escritores de `Claim`/`Source`/`Citation`/`Relationship`/`reviewStatus`/`publicabilityStatus`/`confidenceLevel`/`claimType` (invariantes 4–8/13/20; princípios 20/21/26). Ela **não é** um LMS próprio completo, um repositório de PII de aluno, um motor de analytics individualizado, nem um selo de homologação: ela **integra-se** a um LMS por consumo (Seção 9), mede a operação de forma **agregada e sem PII** (Seção 8) e **valida por evidência**, sem prometer homologação MEC/PNLD nem validação jurídica definitiva (Seção 10). E ela **não** reabre as fronteiras de escrita da Etapa 11 nem destrava por urgência, autoridade ou pressão comercial qualquer portão do pipeline (princípio 5/6/7; R-13.35; R-14.04).

### 1.3 Por que a operação serve ao núcleo e não o governa

A direção única de dependência (E11, §2; invariantes 4–8/20/25) **não se inverte na operação**. A operação observa, mede, agenda, escalona, audita e valida — todas ações de **leitura, governança de processo e composição de evidência**, nenhuma de **escrita factual**. Três mecanismos herdados a tornam estruturalmente incapaz de virar fonte: **(1)** o caminho de escrita factual é **único e fechado** (E11, §6; E12, §1.6) e passa exclusivamente pelo pipeline (E13, §1.3) — a operação não tem porta de escrita no KC; **(2)** o invariante de exibição (invariante 9) vale em toda vista/cache/índice/export/offline e a operação é obrigada a respeitá-lo, não a contorná-lo; **(3)** todo derivado que a operação produz (métrica, relatório, dashboard, pacote LMS) tem `originClass = derivado`, `carriesProvenance = false` quando aplicável, é reconstruível e **nunca** é consultado como fato (invariantes 2/3/26). A operação **decide sobre o processo** (filas, turnos, prioridade, escala, incidente); **nunca decide sobre o fato** (isso é dos revisores de mérito do pipeline) nem sobre a publicabilidade (isso é do invariante de exibição + revisão humana).

### 1.4 Relação com as etapas anteriores (síntese)

| Etapa | O que a operação herda e respeita |
|---|---|
| **1 / 1.1** | níveis A/B/C; risco de licença 0–5; códigos `AUTO`/`ATRIB`/`ISOLA`/`FATO`/`REVH`/`CONF`/`COMER`/`NAO`/`INDX`; *hard stops*; toda fonte nova passa pelo portão antes de uso, mesmo sob escala |
| **2** | claim-first; proveniência obrigatória; incerteza tipada; `DatasetSnapshot`/`LicenseProfile`/`ReviewStatus`; KC soberano |
| **3Z / 3.1** | datum canônico; `sourceTimeBasis` preservado; controvérsia → `ClaimSet`; negacionismo fora do `ClaimSet`; temas sensíveis com revisão humana obrigatória |
| **4A–4H / 4Z** | 25 camadas e prioridade P0–P3; `Scene` v1.1; `cascadeStructure`/`weightedClaimSets`/`paleoPositionPolicy`; cenas-gabarito **inalteráveis**; critérios de publicabilidade |
| **5 / 5Z** | `WhatWasHappeningAtMoment`/`MomentQuery`/`MomentResult`; `publicabilityStatus`; `gatingReason`; `hiddenItems` nunca como fato; `anachronismWarnings`/`equivalenceWarnings`; anti-falsa-equivalência |
| **6** | `BNCCMapping`/`CurricularAlignment` como **alinhamento** externo, nunca selo; BNCC nunca é fonte factual; nota anti-homologação |
| **7 / 8 / 9 / 10** | direção única; Planning/Matching/Output/UX são leitores/anotadores; `score não é verdade`; Output compõe forma; UX apresenta |
| **11** | lojas físicas (`core-store`/`media-store`/`isolated-license-store`/`blocked`); RBAC+ABAC com 11 papéis; `TechnicalAuditTrail`; `dataMinimizationClass`; 30 invariantes; cadeia de rastreabilidade; minimização de PII de menor |
| **12** | `MVPRelease`; testes `T-*` como critério de aceite; seed marcado como `seed-MVP`; ganchos de auditoria/acessibilidade/minimização prontos para operação |
| **13** | `IngestionPopulationPipeline`; 28 princípios; 10 papéis; `ingestionStatus`/`populationStatus`; 12 templates; 24 testes `T-13.NN`; 38 riscos `R-13.NN`; lotes P0–P3; `IngestionAuditTrail` |

### 1.5 A entidade conceitual da operação

```txt
OperationalGovernanceLayer = {
  layerId,
  scope,                      # opera o pipeline (E13) e serve o consumo (E11/E12); jamais currículo/PII/escrita factual
  qaProgram,                  # QA contínuo: executa T-13.NN + T-* + invariantes E11 como PORTÕES (Seção 5)
  qaTrackModel,               # separação dos 6 tracks de QA (factual/técnico/pedagógico/jurídico/acessibilidade/privacidade)
  governanceModel,            # turnos, filas, escalonamento e competência dos 10 papéis de ingestão (Seção 3)
  operationalStateModel,      # readinessStatus, queueState, SLAs, escalonamento (Seção 4)
  auditProgram,               # trilhas de decisão, amostragem de revisões, auditorias periódicas, relatórios (Seção 6)
  scaleControlPolicy,         # condução de P3-scale sob piso epistêmico; readiness gates (Seção 7)
  aggregateAnalyticsPolicy,   # OperationalMetric agregada; minimização máxima; SEM PII de aluno; nunca fonte (Seção 8)
  lmsIntegrationPolicy,       # LMSIntegrationContract: consumo/exportação de publicável; nunca escrita factual (Seção 9)
  validationProgram,          # validação escolar/jurídica/comercial por EVIDÊNCIA; sem promessa MEC/PNLD (Seção 10)
  incidentResponsePolicy,     # detecção, contenção, rollback VERSIONADO, post-mortem (Seção 11)
  liveSourcePolicy,           # recheck de fonte viva, snapshot, reprocessamento versionado (Seção 12)
  coverageMonitoringPolicy,   # CoverageMatrix por 8 dimensões; lacuna sinalizada, nunca preenchida por IA (Seção 13)
  operationalRiskRegister,    # R-14.NN com mitigação e indicador associado (Seção 14)
  handoffToGoToMarket         # o que a Etapa 15 recebe (Seção 15)
}
```

**[NORMATIVO]:** `OperationalGovernanceLayer` é uma **entidade de governança de processo**, externa a todo conteúdo. Ela **não** cria, edita ou deprecia `Claim`/`Source`/`Scene` por si; ela **agenda, mede, audita e governa** o processo (E13) que o faz, e **consome** o conteúdo publicável (E11/E12). `handoffToGoToMarket` entrega evidência e prontidão, **não** autoriza relaxar invariante. O `scope` jamais inclui currículo (BNCC), planejamento (Planning) ou PII de aluno.

---

## 2. Princípios operacionais

Os princípios abaixo são **[NORMATIVO]** e vinculantes. Eles consolidam, no plano operacional, as garantias das Etapas 11/12/13. Nenhuma fila, papel, automação, métrica, integração, prazo ou pressão comercial pode violá-los; uma ação operacional que colida com qualquer um deles é **barrada** e tratada como incidente (Seção 11).

1. **A operação serve ao núcleo; não o governa.** A operação governa o **processo** (E13) e **consome** o conteúdo (E11/E12); jamais origina, edita ou deprecia fato por conta própria (invariantes 1/4–8/25; §1.3).
2. **QA bloqueia, não sugere.** Um teste de invariante reprovado é um **bloqueio rígido** que barra a promoção de estado e devolve o item ao estado seguro; não existe "modo aviso", nem campo de *override*, nem exceção por conveniência (E13, §14; invariante 9; §5).
3. **Escala nunca reduz revisão.** `degradação nunca remove o piso epistêmico`: sob volume, a escala **pausa** antes de baixar a profundidade de revisão, a amostragem de auditoria ou qualquer portão (E13, §13.9; princípio 28; §7).
4. **Nenhuma pressão destrava portão.** Urgência, prazo de procurement, autoridade alegada ou pressão comercial **nunca** destravam um item `blocked-license`/`legal-review`/`rejected`/`pending` nem fazem passar um teste reprovado (R-13.35; R-14.04/R-14.34).
5. **A operação não escreve fato.** Analytics, LMS, dashboard, cache, busca e IA são leitores/derivados; nenhum grava `Claim`/`Source`/`Citation`/`Relationship`/`reviewStatus`/`publicabilityStatus`/`confidenceLevel`/`claimType` (invariantes 4–8/13/20; princípios 20/21/26).
6. **A operação não reabre fronteira de escrita.** As fronteiras da Etapa 11 (§2.3/§6; invariante 20) são imutáveis na operação; um caminho de escrita factual fora do pipeline é, por definição, um incidente crítico (Seção 11; R-14.26).
7. **Analytics mede a operação, nunca o aluno individualmente.** As métricas observam throughput, gargalo, cobertura e qualidade do **processo e do conteúdo**; telemetria individual de aluno permanece **proibida** (invariantes 12/21; R-13.38; R-14.06; §8).
8. **Sem PII de aluno em qualquer trilha operacional.** Nenhuma fila, log, métrica, relatório, integração ou validação coleta ou retém dado pessoal de menor; `dataMinimizationClass` é sempre `SEM-PII`/`AGREGADO`/`PSEUDONIMIZADO` (invariante 21; LGPD/ECA; §8/§10).
9. **LMS consome publicável; nunca escreve fato.** A integração lê itens `published`, respeita licença/atribuição/exportação e nunca funde PII ao núcleo nem grava no KC (invariantes 12/15/20; R-29; §9).
10. **Dúvida resulta em bloqueio/revisão, nunca em publicação automática.** Toda dúvida de fonte, licença, data, geometria, sensibilidade, acessibilidade ou privacidade marca `PENDENTE_*`/escala ao revisor competente — jamais publica por inércia (E13, §14, §22; princípio 25; §11).
11. **Correção é nova versão; nada é apagado.** Rollback opera por **depreciação + restauração** da versão anterior preservada; a trilha do que foi exibido antes da correção sobrevive (invariantes 16/29; `T-13.16`/`T-13.37`; §11/§12).
12. **Fonte viva muda → nova versão + snapshot; nunca atualização silenciosa.** Mudança de fonte cria nova versão de `Source` e novo `DatasetSnapshot`; o claim aponta à versão usada; fonte fora do ar preserva o snapshot como prova (`R-13.32`/`R-13.33`; `T-13.15`; §12).
13. **Cobertura é descrição, não licença para baixar o piso.** Medir lacunas orienta priorização (lotes P0–P3); uma lacuna **nunca** é preenchida por IA, heurística ou fonte C — apenas por fonte A/B sob o pipeline (princípios 1/2/3; R-14.22/R-14.23; §13).
14. **Dashboard, relatório, cache, busca e score não são verdade.** Nenhum derivado de observabilidade é consultado como fato nem promove item `pending` a fato (invariantes 2/3/6/26; R-14.27; §6/§8).
15. **Negar vence em conflito; ninguém aprova fora de competência.** A matriz de competência (E13, §3.2) é vinculante na operação; sob pressão de fila, a regra "negar vence" se aplica (`T-13.22`; R-13.22; R-14.25; §3).
16. **Validação produz evidência, não promessa.** Pilotos, laudos e auditorias geram **evidência datada e versionada**; a operação não promete homologação MEC, aprovação PNLD nem validação jurídica definitiva (invariante 7; R-23; R-14.09/R-14.10; §10).
17. **Toda decisão operacional que toque publicabilidade registra `gatingReason` e ator.** Promoção, bloqueio, rollback, despublicação e reprocessamento são auditáveis à curadoria — nunca silenciosos (princípio 25; invariante 16; §6/§11).
18. **Acessibilidade e privacidade são portões de QA, não etapas opcionais.** `acessibilidade não é opcional` (e-MAG/WCAG/LBI) e a minimização de PII são **tracks de QA bloqueantes**, com os mesmos efeitos do QA factual (invariantes 21/23; `T-A11Y`/`T-PII`; §5).
19. **Incidente que toque fato/licença/sensível/menor escala imediatamente e, se necessário, despublica antes de investigar.** A contenção precede a análise de causa-raiz; o invariante de exibição é restabelecido primeiro (§11).
20. **Offline/degradação não relaxa nada que a política fecharia online.** A operação herda os invariantes 11/22: a ausência de rede e a queda de modo (3D→2D→estático→offline→projetor) preservam licença, publicabilidade, papel e piso epistêmico.
21. **SLA organiza, não autoriza atalho.** Um SLA estourado **escala ou pausa a admissão (intake)** — nunca pula um portão nem publica sem revisão (princípio 2/4; §4).
22. **Toda fonte nova passa pela Etapa 1/1.1 antes de uso, mesmo sob escala.** A pressão por cobertura não cria atalho de ingestão de fonte não auditada (`R-13.01`; princípio 22; §7/§13).

> **Regra-síntese dos princípios.** A operação **mantém o pipeline funcionando e o conteúdo publicável sendo consumido**, medindo a si mesma e ao conteúdo de forma agregada e sem PII, integrando-se a sistemas externos como **leitora**, e validando por **evidência** — sem nunca virar caminho de escrita, sem nunca destravar por pressão, sem nunca confundir derivado (métrica, relatório, cache, busca, IA, score) com fato, e sem nunca apagar a trilha do que foi exibido. Quando houver dúvida, **bloqueia-se ou revisa-se** (Seção 11) — nunca se publica por inércia.

---

## 3. Papéis, governança e responsabilidades

### 3.1 Os dez papéis sob governança contínua

A operação **não cria papéis novos de mérito**: ela **governa em produção** os dez papéis humanos do pipeline (E13, §3) — `sourceScout`, `ingestionCurator`, `licenseReviewer`, `scientificReviewer`, `historicalReviewer`, `editorialReviewer`, `legalReviewer`, `geoTemporalReviewer`, `accessibilityReviewer`, `pipelineAdmin` — acoplados aos papéis técnicos da Etapa 11 (§7.2) e **estritamente separados** dos papéis escolares/de leitura (`teacher`, `schoolCoordinator`, `student`, `guardianOrResponsibleAdult`, `publicViewer`, `offlineViewer` — E11, §7.7). **[NORMATIVO]:** nenhum papel de ingestão opera com PII de aluno; nenhum papel escolar recebe credencial de escrita no KC. **Negar vence em conflito.** Ninguém aprova fora de sua competência (`T-13.22`; R-13.22).

A operação acrescenta **funções de governança de processo** (não de mérito), que organizam o trabalho dos dez papéis sem decidir sobre fato/licença/publicabilidade:

```txt
operationalGovernanceFunction = [
  operationsLead,        # coordena turnos, filas, prioridade de lotes, capacidade; não decide mérito
  qaConductor,           # opera o programa de QA contínuo (Seção 5); declara bloqueio quando um teste reprova
  auditLead,             # conduz amostragem, auditorias periódicas, trilhas de decisão e relatórios (Seção 6)
  incidentCommander,     # coordena resposta a incidente e rollback versionado (Seção 11); papel rotativo de plantão
  dataProtectionSteward, # zela por minimização/SEM-PII em analytics/LMS/validação (Seções 8–10); apoia o legalReviewer
  scaleCoordinator       # conduz P3-scale; aplica readiness gates; pausa a escala antes de baixar o piso (Seção 7)
]
```

**[NORMATIVO]:** essas funções **governam o processo**, jamais o mérito. `qaConductor` **declara** o bloqueio que o teste já determinou — não tem poder de aprovar/dispensar; `incidentCommander` coordena contenção/rollback, mas a decisão de re-publicar volta ao revisor de mérito competente; `dataProtectionSteward` apoia o `legalReviewer` na conformidade, sem virar editor; `operationsLead`/`scaleCoordinator` priorizam e sequenciam, sem destravar portão (princípio 4/21). Uma mesma pessoa pode acumular função de governança **e** papel de mérito, **desde que** não aprove a si própria nem fora de sua competência (segregação de funções; R-14.25/R-14.31).

### 3.2 Matriz de governança (quem governa o quê, sem decidir mérito)

| Função | Governa | Nunca decide | Escalona para |
|---|---|---|---|
| `operationsLead` | turnos, capacidade, prioridade de lote, fila | mérito; licença; publicabilidade | `scaleCoordinator`/`pipelineAdmin` |
| `qaConductor` | execução do QA; declaração de bloqueio | aprovação/dispensa de teste; mérito | revisor de mérito competente / `incidentCommander` |
| `auditLead` | amostragem, auditoria periódica, relatório | mérito; publicação | `legalReviewer` (achado jurídico) / `incidentCommander` |
| `incidentCommander` | contenção, rollback versionado, post-mortem | re-publicação de mérito | revisor competente / `legalReviewer` (LGPD/ECA) |
| `dataProtectionSteward` | minimização, SEM-PII, DPIA operacional | mérito factual | `legalReviewer` |
| `scaleCoordinator` | condução de `P3-scale`; readiness gates | mérito; destrave de portão | `pipelineAdmin` / `operationsLead` |

**[NORMATIVO]:** toda ação de governança que toque publicabilidade (bloqueio declarado, despublicação, rollback, pausa de escala) grava ator, data e `gatingReason` na trilha (Seção 6; invariante 16; princípio 25). A matriz de **competência de mérito** permanece a da Etapa 13 (§3.2), inalterada.

### 3.3 Capacidade, turnos e cobertura de plantão

**[RECOMENDADO]** a operação mantém **capacidade suficiente** para que nenhum portão seja burlado por falta de gente: filas dimensionadas por papel, turnos com cobertura para temas sensíveis (revisão humana obrigatória — princípio 19), e **plantão de incidente** (`incidentCommander` rotativo) para conter vazamento de `pending`/licença/PII fora do horário comercial. **[NORMATIVO]:** se a capacidade for insuficiente para revisar com profundidade, a **admissão de novos itens é pausada** (intake throttling) e a escala recua — nunca se aprova em lote sem revisão (princípio 2/3/21; R-13.21; R-14.02/R-14.30). Burnout/turnover de revisores é risco monitorado (R-14.30) com indicador de carga por papel (Seção 8).

---

## 4. Estados operacionais, filas e SLAs

A operação controla **três objetos de estado**, ortogonais aos `ingestionStatus`/`populationStatus` do pipeline (E13, §4) e que **não os substituem**: o **estado de prontidão de um escopo** (`readinessStatus`), o **estado de um item numa fila operacional** (`queueState`) e o **estado de um incidente** (`incidentSeverity`/`incidentStatus`, detalhados na Seção 11).

### 4.1 Enums de estado operacional

```txt
readinessStatus = [               # maturidade operacional de um escopo (camada/lote/recorte) para uso
  not-ready,                      # abaixo do piso operacional; QA/auditoria/papéis ainda não verdes
  ready-for-pilot,                # pronto para piloto controlado (sem PII real de aluno)
  ready-for-school,              # pronto para uso escolar (acessibilidade/privacidade/licença auditadas)
  ready-for-scale,               # pronto para escala (P1 em produção; throughput sem queda de revisão)
  blocked                         # bloqueado: invariante/teste violável por pressão, ou vazamento detectado
]

queueState = [                    # estado de um item dentro de uma fila operacional
  queued,                         # aguardando atendimento
  in-progress,                    # em atendimento pelo papel competente
  escalated,                      # escalado (dúvida/competência/risco) ao papel/função superior
  blocked,                        # bloqueado por teste/portão (devolve ao estado seguro do pipeline)
  returned,                       # devolvido para correção (mapeia a needs-rework no pipeline)
  done                            # concluído (transição de ingestionStatus efetuada conforme E13)
]

qaGateResult = [ pass, fail ]     # SEM "waived"/"override": um teste reprovado bloqueia (princípio 2)
```

**[NORMATIVO]:** `qaGateResult` tem **dois** valores. Não existe `waived`, `override`, `accepted-with-risk` ou equivalente; QA bloqueia, não sugere. `readinessStatus` é declarado pelo `scaleCoordinator`/`operationsLead` **a partir de critérios objetivos** (Seção 7), nunca por prazo (R-14.35).

### 4.2 Filas operacionais

```txt
operationalQueue = [
  intake-queue,                 # propostas de fonte e itens novos (sourceScout/ingestionCurator)
  license-queue,                # triagem de licença/risco 0–5 (licenseReviewer)
  scientific-review-queue,      # mérito científico (scientificReviewer)
  historical-review-queue,      # mérito historiográfico (historicalReviewer)
  editorial-review-queue,       # tema sensível/controvérsia/mediação (editorialReviewer)
  legal-review-queue,           # risco jurídico/LGPD/contrato (legalReviewer)
  geotemporal-review-queue,     # tempo/espaço/datum/geometria (geoTemporalReviewer)
  accessibility-review-queue,   # equivalente textual/e-MAG/WCAG/LBI (accessibilityReviewer)
  publication-queue,            # consolidação e publicação (ingestionCurator, após todas as revisões)
  live-source-recheck-queue,    # recheck de fonte viva / fonte fora do ar (Seção 12)
  audit-sampling-queue,         # amostras para auditoria de qualidade de revisão (Seção 6)
  incident-queue                # incidentes em contenção/rollback (Seção 11)
]
```

**[NORMATIVO]:** cada fila atende a um **papel de competência** (E13, §3). A fila **organiza** o trabalho; ela **não** cria atalho de aprovação. Um item de tema sensível (princípio 19) **não** sai da `publication-queue` sem a aprovação registrada do revisor competente. Itens em `legal-review-queue` têm *default* **não publica** (princípio 4).

### 4.3 Matriz de SLAs (organizam, não autorizam atalho)

Os SLAs abaixo são **[RECOMENDADO]** (alvos de tempo de resposta para evitar gargalo); os números concretos são **[PENDÊNCIA]** da execução, calibrados por capacidade. **[NORMATIVO]:** estourar um SLA **nunca** destrava um portão; ele **escala** (ao papel/função superior) e, persistindo, **pausa a admissão (intake)** do lote afetado (princípio 21; R-14.03).

| Fila | Alvo de 1ª resposta [REC] | Prioridade | Ação ao estourar o SLA |
|---|---|---|---|
| `incident-queue` (sev1/sev2) | imediata / horas | máxima | `incidentCommander` aciona plantão; contenção antes da análise (§11) |
| `legal-review-queue` | dias úteis | alta | escala a `pipelineAdmin`/operação; *default* não publica |
| `editorial-review-queue` (sensível) | dias úteis | alta | escala; item permanece `pending`; nunca publica sem revisão |
| `license-queue` | dias úteis | alta | escala a `legalReviewer` (risco 5/sem-licença); *default* não entra |
| `scientific/historical/geotemporal-review-queue` | dias úteis | média | escala ao revisor de competência; item fica `needs-rework`/`pending` |
| `accessibility-review-queue` | dias úteis | média | escala; item visual sem equivalente textual não publica |
| `intake-queue` | dias úteis | média | aplica *throttling*; prioriza por lote (P0→P3) |
| `publication-queue` | dias úteis | média | aguarda todas as revisões; nunca consolida com revisão pendente |
| `live-source-recheck-queue` | por cadência da fonte | conforme classe | escala; mantém versão snapshotada como verdade vigente (§12) |
| `audit-sampling-queue` | por ciclo de auditoria | baixa | reprograma; baixa amostragem **nunca** é compensada com menos revisão (princípio 3) |

### 4.4 Escalonamento (negar vence)

**[NORMATIVO]** o escalonamento é obrigatório, não opcional: dúvida de competência → ao papel competente; risco jurídico/LGPD → `legalReviewer`; tema de máxima sensibilidade → revisão conjunta (E13, §3.2); incidente que toque fato/licença/PII/menor → `incidentCommander` + `legalReviewer` (§11). Em **qualquer** conflito não resolvido, **negar vence**: o item permanece no estado seguro (`pending`/`needs-rework`/`blocked-license`/`legal-review`) até decisão competente registrada (princípio 15; R-14.25).

---

## 5. QA contínuo e execução dos testes `T-13.NN`

### 5.1 O que o programa de QA é

O **`qaProgram`** é a execução **contínua e bloqueante** das suítes de invariante já fixadas — os **24 testes `T-13.NN`** (E13, §14.1), os **testes `T-*` do MVP** (E12, §13) e os **30 invariantes técnicos** (E11, §13) — como **portões de promoção** de `ingestionStatus`/`populationStatus`/`readinessStatus`. **[NORMATIVO]:** o QA **bloqueia, não sugere** (princípio 2). Um teste reprovado (`qaGateResult = fail`) **barra** a transição, devolve o item ao estado seguro (`needs-rework`/`blocked-license`/`legal-review`) **versionado** (nunca por apagamento — §11/§12) e **rebaixa** o `populationStatus` do escopo afetado (E13, §13.10). Não há *override*, *waiver* nem "publicar com risco aceito".

### 5.2 As três cadências de QA

```txt
qaCadence = [
  per-item-gate,     # a cada transição de ingestionStatus (E13, §4.2): os testes do item rodam como portão
  per-batch-gate,    # a cada promoção de populationStatus de um lote (E13, §13): a suíte do escopo roda
  periodic-regression # ciclos periódicos de regressão + amostragem de auditoria (Seção 6) sobre o publicado
]
```

**[NORMATIVO]:** a cadência `periodic-regression` reexecuta sobre o **conteúdo já publicado** os testes que detectam deriva (vazamento de `pending`, cache obsoleto, snapshot mutado, paleoposição como atual, equivalente textual ausente), porque o mundo muda (fonte viva, licença, consenso) e um item correto ontem pode precisar de rollback hoje (§11/§12). A regressão **não** introduz fato; ela **detecta** quando o publicado deixou de satisfazer um invariante e **dispara** rollback/revisão.

### 5.3 Os seis tracks de QA (separados e todos bloqueantes)

**[NORMATIVO]** o QA é organizado em **seis tracks separados**, cada um com dono de competência e poder de **bloquear** independentemente. Um item só é publicável quando **todos** os tracks aplicáveis estão verdes; reprovar em qualquer track basta para bloquear (princípio 2/18).

| `qaTrack` | O que valida | Testes/invariantes principais | Dono(s) | Bloqueia |
|---|---|---|---|---|
| `qaFactual` | fonte A/B; tipagem; incerteza; controvérsia/`ClaimSet`; negacionismo fora; tempo/espaço; relação com proveniência | `T-13.01/02/03/07/08/09/10/11/12/13/20/23/24`; `T-FACTUAL`/`T-GOE`/`T-KPG`/`T-SIM-1789`/`T-DATUM` | `scientificReviewer`, `historicalReviewer`, `geoTemporalReviewer`, `editorialReviewer` | publicação de qualquer fato sem fonte/tipagem/incerteza válidas |
| `qaTechnical` | imutabilidade de snapshot; versionamento sem apagamento; invalidação de cache/índice; sincronização; reconstrutibilidade de derivado | `T-13.15/16/18`; `T-CACHE`/`T-DERIVADO`/`T-SYNC`; invariantes 2/3/26/28 | `pipelineAdmin`, `qaConductor` | promoção com snapshot mutável, cache não invalidado ou versões divergentes |
| `qaPedagogical` | adequação de **forma** do Output (E9); faixa etária; alinhamento exibido como alinhamento; face professor × aluno | `T-PROF×ALUNO`; `T-HOMOLOGA`; invariantes 5/7 | `editorialReviewer` (forma) + evidência de piloto (§10) | exibição de forma inadequada à faixa ou alinhamento apresentado como selo |
| `qaLegal` | licença por asset; NC nunca como expressão; SA/ODbL isolado; herança de licença em export/offline; LGPD/ECA; nota anti-homologação | `T-13.04/05/06/17`; `T-NC`/`T-SA`/`T-EXPORT`/`T-HOMOLOGA`; invariantes 10/11/17/18/19/27 | `licenseReviewer`, `legalReviewer` | publicação/exportação com licença violada ou homologação prometida |
| `qaAccessibility` | equivalente textual com mesma informação e rótulos; `natureLabel`; redundância não-cromática; teclado/foco/contraste | `T-A11Y`; `T-13` (acessibilidade na ingestão); invariante 23 | `accessibilityReviewer` | publicação de item visual sem equivalente textual adequado |
| `qaPrivacy` | ausência de PII de aluno no KC e nas trilhas; minimização; analytics agregado; identidade separada no LMS | `T-PII`; `T-LOG`; invariantes 12/21; `R-13.38` | `dataProtectionSteward` + `legalReviewer` | qualquer coleta/retenção de PII de menor em conteúdo, log, métrica ou integração |

### 5.4 Execução dos 24 testes `T-13.NN` como portão contínuo

A tabela liga **cada** teste `T-13.NN` (E13, §14.1) ao seu gatilho operacional, à cadência, à ação em caso de falha e ao track responsável. **[NORMATIVO]:** nenhum desses testes é destravado por urgência, autoridade ou pressão comercial (princípio 4; R-13.35); a falha **rebaixa** o `populationStatus` (E13, §13.10).

| Teste | Gatilho (cadência) | Falha → ação | Track |
|---|---|---|---|
| `T-13.01` fonte A/B | `claim-drafted → approved-for-kc` (per-item) | bloqueio; `needs-rework`; `gatingReason="fonte A/B ausente"` | `qaFactual` |
| `T-13.02` Wikipedia/Wikidata ≠ autoridade | toda classificação de fonte (per-item) | bloqueio; aceito só como `INDX` | `qaFactual` |
| `T-13.03` IA ≠ fonte | toda extração com proveniência (per-item) | bloqueio; IA sem `sourceTier`; rascunho `pending` | `qaFactual` |
| `T-13.04` NC ≠ expressão | `→ published` de asset risco 4 (per-item/per-batch) | `blocked-license`; só fato re-derivado | `qaLegal` |
| `T-13.05` SA/ODbL isolado | entrada de SA/ODbL (per-item; regressão no `core-store`) | redireciona a `isolated-license-store` | `qaLegal` |
| `T-13.06` asset sem licença | `AssetIntakeRecord` (per-item) | não servido; `pending`/`blocked-license` | `qaLegal` |
| `T-13.07` sem `claimType` | `→ metadata-complete` (per-item) | bloqueio; `needs-rework` | `qaFactual` |
| `T-13.08` sem incerteza | `→ metadata-complete` (per-item) | bloqueio; `needs-rework` | `qaFactual` |
| `T-13.09` sem `reviewStatus` | criação do item (per-item) | bloqueio; nasce `pending` | `qaFactual` |
| `T-13.10` controvérsia sem `ClaimSet` | revisão de mérito (per-item) | bloqueio; exige `weightedClaimSets` | `qaFactual` |
| `T-13.11` negacionismo como lado | revisão editorial (per-item) | bloqueio; só `rotulado-rejeitado` fora do `ClaimSet` | `qaFactual` |
| `T-13.12` tempo sem `sourceTimeBasis` | normalização temporal (per-item) | bloqueio; `PENDENTE_DATA` | `qaFactual` |
| `T-13.13` geometria sem licença/status | tratamento espacial (per-item) | bloqueio; `PENDENTE_GEOMETRIA` | `qaFactual`+`qaLegal` |
| `T-13.14` `pending` não exibível | toda leitura/cache/índice/export/offline (regressão) | não exibido como fato; incidente se vazar (§11) | `qaTechnical`+`qaPrivacy` |
| `T-13.15` snapshot imutável | tentativa de editar snapshot (per-item/regressão) | rejeitada; cria novo snapshot/versão | `qaTechnical` |
| `T-13.16` depreciação não apaga | `→ deprecated` (per-item) | versão anterior preservada; só sai de exibição | `qaTechnical` |
| `T-13.17` export herda licença | export/offline (per-item/per-batch) | herda licença/atribuição; isolados fora de pacote aberto | `qaLegal` |
| `T-13.18` cache/índice invalidado | `approved`/`rejected`/`deprecated` (per-item/regressão) | `InvalidationRule` dispara; derivado reconstruído | `qaTechnical` |
| `T-13.19` seed ≠ ingestão | contagem/exibição de item `seed-MVP` (per-batch) | bloqueio; exige reingestão pela E13 §5 | `qaFactual` |
| `T-13.20` de-duplicação na migração | dois claims iguais (per-batch) | versiona (`supersedes`); 1 claim por fato | `qaFactual` |
| `T-13.21` placeholder ≠ final | publicação de placeholder (per-item) | bloqueio; `PENDENTE_*` não exibível | `qaLegal`+`qaFactual` |
| `T-13.22` revisão na competência | aprovação fora de competência (per-item) | rejeitada; "negar vence" | governança (§3) |
| `T-13.23` paleoposição ≠ coordenada moderna | marcador de tempo profundo (per-item) | bloqueio; exige `paleoPositions`+`AnachronismNotice` | `qaFactual` |
| `T-13.24` relação com proveniência | criação de `Relationship` (per-item) | bloqueio; relação herda exigência de proveniência | `qaFactual` |

### 5.5 O que o QA contínuo **não** faz

O QA contínuo **não** roda testes reais nesta etapa (limite de natureza): ele **define** a disciplina pela qual a execução (fora desta etapa) os operará como portões. Ele **não** introduz fato, **não** corrige claim por automação, **não** "passa" item por prazo, **não** transforma a suíte em recomendação e **não** abre exceção. Ele **não** substitui a revisão humana de mérito (E13, §4.4): a automação **prepara** e **mede**; o humano competente **decide o mérito**; o teste de invariante **barra** o que viola a estrutura.

---

## 6. Auditoria, trilhas de decisão e relatórios

### 6.1 O programa de auditoria

O **`auditProgram`** estende — sem substituir — a `IngestionAuditTrail` (E13, §9) e a `TechnicalAuditTrail` (E11, §12), consolidando: **trilhas de decisão** (quem decidiu o quê, quando, com que `gatingReason` e sobre qual versão), **amostragem de qualidade de revisão** (R-13.21), **auditorias periódicas** por domínio, e **relatórios executivos agregados**. **[NORMATIVO]:** a evidência de auditoria é **referencial e versionada** (invariante 16/21) — comprova o cumprimento sem virar repositório de PII (E11, §12).

```txt
OperationalAuditProgram = {
  decisionTrail,        # toda decisão de mérito/governança: ator, papel, data, gatingReason, versão, transição
  reviewSamplingPolicy, # amostragem da qualidade de revisão (sensíveis: cobertura total; demais: amostra)
  periodicAudits,       # ciclos por domínio (licença, fonte, sensível, acessibilidade, privacidade, publicabilidade)
  traceabilityChain,    # artefato → bloco → cena/momento → claim → fonte → licença (E11, §12)
  executiveReporting,   # relatórios agregados, anti-homologação, SEM PII (Seção 6.4)
  auditRetention        # retenção referencial/versionada; nunca apaga prova do que foi exibido (T-13.37; invariante 16)
}
```

### 6.2 Amostragem de qualidade de revisão

**[NORMATIVO]** itens de **tema sensível** (princípio 19) têm **revisão competente registrada e auditável em 100%** — não há amostragem que os dispense. **[RECOMENDADO]** itens não-sensíveis têm uma **amostra aleatória** re-auditada por um segundo revisor de competência (percentual concreto **[PENDÊNCIA]**, calibrado por capacidade — E13, §15.8). **[NORMATIVO]:** baixar a amostragem por falta de capacidade **nunca** é compensado aprovando mais itens sem revisão; a alternativa é **pausar a admissão** (princípio 3; R-14.24). O resultado da amostragem alimenta o indicador de "qualidade de revisão" (Seção 8) e, ao detectar aprovação indevida, dispara rollback (§11).

### 6.3 Auditorias periódicas por domínio

| Auditoria | Verifica | Base | Achado → ação |
|---|---|---|---|
| **Licença/IP** | partição física correta; NC fora de expressão; SA/ODbL isolado; atribuição; herança em export/offline | `T-13.04/05/06/17`; invariantes 17–19/27 | incidente de licença (§11); rollback de exibição/export |
| **Fonte/disponibilidade** | `checksum` íntegro; fonte viva alterada; fonte fora do ar; `sourceAvailability` | `T-13.15`; `R-13.32/33`; §12 | recheck/reprocessamento versionado (§12) |
| **Conteúdo sensível** | revisão obrigatória concluída; mediação; Leis 10.639/11.645 cobertas; negacionismo fora do `ClaimSet` | E3.1; princípios 17–19 | despublicar e re-revisar (§11) |
| **Acessibilidade (ASES)** | equivalente textual; teclado/foco/contraste; redundância não-cromática | `T-A11Y`; invariante 23 | bloqueio de exibição até correção; laudo (§10) |
| **Privacidade (DPIA/RIPD)** | ausência de PII de aluno; minimização; identidade separada; analytics agregado | `T-PII`/`T-LOG`; invariantes 12/21 | incidente de privacidade (§11); revisão jurídica |
| **Publicabilidade** | `pending`/`legal-review`/`rejected`/`hiddenItems`/`teacherOnly` não exibíveis em nenhum caminho | `T-13.14`; `T-PENDING`/`T-TEACHERONLY`; invariante 9 | incidente de publicabilidade (§11); rollback imediato |
| **Fronteira de escrita** | nenhuma escrita factual fora do pipeline | `T-FRONTEIRA/T-API`; invariante 20 | incidente crítico (§11); revisão de arquitetura |

### 6.4 Relatórios executivos

**[NORMATIVO]** os relatórios executivos são **agregados, anti-homologação e SEM PII**. Eles reportam saúde operacional (throughput, gargalo, cobertura, qualidade de revisão, incidentes) e nunca: (a) identificam alunos; (b) apresentam alinhamento BNCC como selo MEC/PNLD (invariante 7; R-23); (c) tratam um número de dashboard como fato sobre o mundo (princípio 14; R-14.27). **[RECOMENDADO]:** cadência mensal/trimestral, com um painel operacional contínuo cujos números são **derivados reconstruíveis** (invariante 26), nunca autoritativos.

---

## 7. Escala de povoamento e controle de qualidade

### 7.1 Como a escala avança sem baixar o piso

A escala é a condução de **`P3-scale`** (E13, §13.9) **somente depois** de a espinha (P1) e os padrões (P0/P2) estarem sólidos, sob os **mesmos portões**. **[NORMATIVO]:** a escala **pausa antes de baixar o piso** — `degradação nunca remove o piso epistêmico` (princípio 3/28). O `scaleCoordinator` conduz; o QA contínuo (Seção 5) e a auditoria (Seção 6) **bloqueiam** a promoção quando a qualidade de revisão cai, a auditoria fica incompleta ou um invariante é cedido por velocidade (R-13.22/R-13.24/R-13.35; R-14.02/R-14.28/R-14.35). Toda **fonte nova** entra apenas após passar pela Etapa 1/1.1 (princípio 22; R-13.01).

### 7.2 Critérios objetivos de prontidão (readiness gates)

A matriz abaixo é **[NORMATIVO]**: cada `readinessStatus` exige **critérios objetivos**, não prazo (R-14.35). Os critérios são cumulativos (cada nível exige o anterior).

| `readinessStatus` | Critérios objetivos (todos exigidos) |
|---|---|
| `blocked` | qualquer invariante/teste `T-13.NN`/`T-*` puder ser destravado por urgência/autoridade/pressão (R-13.35); **ou** vazamento de `pending`/`hiddenItems`/`teacherOnly` como fato; **ou** NC como expressão / SA/ODbL no núcleo; **ou** caminho de escrita factual fora do pipeline; **ou** PII de aluno coletada; **ou** risco do registro (Seções 13/14) sem teste/portão/indicador associado (espelha E13, §15.10) |
| `not-ready` | escopo abaixo de `pilot-populated`; **ou** algum dos 6 tracks de QA não verde; **ou** cadeia de auditoria seed→canônico incompleta; **ou** algum dos 10 papéis ausente |
| `ready-for-pilot` | as três cenas-gabarito migradas a canônico sob `P0-canonical-scenes` (E13, §12/13.1); matriz `T-13.NN` ativa como portão e **verde** para P0; os **6 tracks** verdes para o escopo; **10 papéis** existem e operam com competência/escalonamento; analytics agregado ativo **sem PII**; piloto controlado **sem PII real de aluno** (E12, §11.2); resposta a incidente + rollback versionado definidos (§11) |
| `ready-for-school` | `ready-for-pilot` **+** espinhas P1 ao menos `partially-populated` para o escopo ofertado; **laudo de acessibilidade (ASES)** aprovado; **DPIA/RIPD** revisada pelo `legalReviewer`; auditoria de licença/exportação limpa; auditoria de conteúdo sensível limpa; `T-PROF×ALUNO` verificado; **nota anti-homologação** presente no viewer e no export (invariante 7; R-23); evidência de piloto positiva (§10) |
| `ready-for-scale` | `ready-for-school` **+** espinhas P1 `production-populated` para o escopo; padrões P2 provados; **throughput sustentado sem queda de profundidade de revisão** (auditado — §6); desempenho dentro dos orçamentos da Etapa 11; monitoramento de cobertura ativo com lacunas **priorizadas, não preenchidas por suposição** (§13); MTTR de incidente dentro dos alvos; nenhum risco `R-14.NN` sem mitigação/indicador |

**[NORMATIVO]:** rebaixamento é automático — a falha de qualquer teste de invariante (Seção 5) ou de qualquer auditoria (Seção 6) **rebaixa** o `readinessStatus`/`populationStatus` do escopo e bloqueia sua promoção até a correção **versionada** (E13, §13.10; §11), nunca por apagamento.

### 7.3 Anti-Goodhart: throughput não compra qualidade

**[NORMATIVO]** nenhuma meta de throughput, cobertura ou prazo justifica reprovar menos, revisar mais raso ou aprovar em lote (R-14.02/R-14.28). O indicador de qualidade de revisão (Seção 8) é **soberano** sobre o indicador de velocidade: se a qualidade cair, a velocidade recua. A escala é **escopo a escopo** e **contínua**, enquanto os critérios se sustentarem (E13, §13.9/§13.10).

---

## 8. Analytics agregado sem PII

### 8.1 O que o analytics é (e o que jamais é)

O **`aggregateAnalyticsPolicy`** define a **observação agregada da operação, da cobertura, dos gargalos e da qualidade** — para gerir o produto, não os alunos. **[NORMATIVO]:** analytics **mede a operação, nunca o aluno individualmente** (princípio 7); ele **não** coleta nem retém PII de menor (princípio 8; invariantes 12/21; `R-13.38`); ele **não** é fonte factual nem caminho de escrita no KC (princípio 5/14; R-14.05/R-14.06/R-14.27). Toda métrica é **derivada reconstruível** (`originClass = derivado`; invariante 26) com `dataMinimizationClass ∈ {SEM-PII, PSEUDONIMIZADO, AGREGADO}` — e, para qualquer coisa que toque uso escolar, **`AGREGADO`** (dados de turma agregados, E11, §8), nunca telemetria individual de aluno (R-28).

```txt
OperationalMetric = {
  metricId,
  metricFamily,         # ingestao | qualidade | cobertura | licenca | fonte | incidente | desempenho | uso-agregado
  aggregationLevel,     # processo | conteudo | escopo | turma-agregada (NUNCA aluno individual)
  dataMinimizationClass,# SEM-PII | PSEUDONIMIZADO | AGREGADO
  originClass,          # SEMPRE derivado (reconstruível; não autoritativo; não fonte)
  carriesProvenance,    # false (métrica não é claim; não responde fato)
  computedFromVersions  # versões de conteúdo/processo que originaram a métrica (auditável)
}
```

### 8.2 Matriz de indicadores mínimos

**[NORMATIVO]** os indicadores mínimos abaixo consolidam o que a Etapa 13 (§15.6) mandou monitorar e o que a operação acrescenta. Todos são **agregados** e **SEM PII**.

| Indicador | Família | O que mede | Origem | Risco coberto |
|---|---|---|---|---|
| Itens por `ingestionStatus`/`populationStatus` | ingestao | distribuição do funil de ingestão | E13, §4 | R-13.23; R-14.02 |
| Taxa de bloqueio por `gatingReason` | qualidade | por que itens são barrados | E13, §14; §5 | R-13.21/35; R-14.01/04 |
| *Lead time* por estado | ingestao | gargalo por etapa/fila | §4 | R-13.23; R-14.32 |
| Itens em `legal-review`/`blocked-license` e permanência | licenca | acúmulo jurídico/licença | §4; E13, §8 | R-13.04/35; R-14.34 |
| Cobertura de snapshot e integridade de `checksum` | fonte | proveniência reconstruível | E13, §9; §12 | R-13.07/32/33; R-14.15 |
| Fontes vivas alteradas e fontes fora do ar | fonte | deriva/indisponibilidade de fonte | §12 | R-13.32/33; R-14.13/14 |
| Proporção de revisões escaladas | qualidade | carga de competência/dúvida | §3/§6 | R-13.22; R-14.25 |
| Amostragem de qualidade de revisão | qualidade | aprovação rasa sob volume | §6.2 | R-13.21; R-14.24/30 |
| Placeholders ativos remanescentes | cobertura | demonstração exibida como real | E13, §12.8 | R-13.18; R-14.20 |
| Invalidação de cache/índice pós-decisão | desempenho | derivado obsoleto servindo fato | `T-13.18` | R-13.25; R-14.16 |
| Tentativas de escrita por camada não autorizada | qualidade | violação de fronteira (E11) | invariante 20 | R-13.26; R-14.26 |
| Cobertura por camada/região/período/fonte/risco/`reviewStatus` | cobertura | lacunas estruturais (§13) | §13 | R-13.31; R-14.22/23 |
| Carga por papel/fila (e indicadores de turnover) | qualidade | sustentabilidade da revisão | §3.3 | R-14.30 |
| MTTR e contagem de incidentes por tipo | incidente | saúde operacional/segurança | §11 | R-14.17–21/32 |
| Desempenho (degradação, orçamentos E11) | desempenho | viabilidade sob hardware modesto | E11, §11 | R-13.30; R-14.28 |
| Uso **agregado** por turma/escola (se houver) | uso-agregado | adoção, sem identificar aluno | E11, §8 | R-13.38; R-14.05/06 |

### 8.3 O que o analytics **não** mede

**[NORMATIVO]** o analytics **não** mede: aluno identificável; desempenho individual de estudante; trilha de cliques pessoal; nem qualquer coisa que exija PII de menor. Ele **não** treina modelo com dado de aluno (E11, §8) e **não** vira evidência factual. Métricas de uso, quando existirem, são **AGREGADAS por turma/escola** sob a base legal da escola (LGPD/ECA), e o produto **não** constrói o caderneta/boletim do aluno (isso é do LMS/escola — Seção 9).

---

## 9. Integração LMS e exportações controladas

### 9.1 O LMS como consumidor, nunca escritor

A **`lmsIntegrationPolicy`** trata um LMS (Moodle-classe, Google Classroom-classe, plataformas estaduais/municipais) como **consumidor de conteúdo publicável** — um leitor externo, como UX/Output (E10/E9) e o `publicViewer`/`offlineViewer` (E11, §7.7). **[NORMATIVO]:** o LMS **consome publicável, não escreve fato** (princípio 9): ele lê **apenas** itens `published` (`reviewStatus = approved`, publicabilidade satisfeita — invariante 9), respeita **licença/atribuição/exportação** (invariantes 10/11/17/27) e **nunca** grava `Claim`/`Source`/`reviewStatus`/`publicabilityStatus` no KC (invariante 20; R-29). A operação **não constrói um LMS próprio completo** (limite); ela **integra-se** a um LMS existente.

```txt
LMSIntegrationContract = {
  contractId,
  direction,            # SOMENTE saída: o KC/produto EXPORTA conteúdo publicável; nunca importa fato
  consumes,             # itens published + OutputArtifact (E9) + ExportPackage (E11, §9)
  respects,             # LicenseProfile, atribuição, exportPolicy, visibilityClass, ageBand, mediação, nota anti-homologação
  identitySeparation,   # PII de aluno fica no LMS/escola; NUNCA flui ao KC; identidade × sessão × pedagógico separados
  writeToKnowledgeCore, # SEMPRE proibido (invariante 20)
  standards             # [REC]/[ALT]: LTI, SCORM, xAPI — sob a restrição de identidade separada (Seção 9.3)
}
```

### 9.2 Exportações controladas

**[NORMATIVO]** toda exportação para o LMS é um `ExportPackage`/`OfflinePackage` (E11, §9) que **embute** citação, incerteza, mediação, atribuição e **nota anti-homologação** (invariantes 10/14/16; `T-EXPORT`/`T-HOMOLOGA`; R-23) e **respeita a matriz de licença por `licenseRiskLevel`**: expressão NC **nunca** é exportada (invariante 19; `T-NC`); SA/ODbL **só** com atribuição/share-alike honrados e **fora** de pacote aberto (invariantes 18/27; `T-SA`). Todo pacote exportado é **auditável** (invariante 16): registra as versões de conteúdo que o compõem, permitindo rollback (§11) e reconstrução.

### 9.3 Identidade separada e padrões de LMS

**[NORMATIVO]** a separação **identidade × sessão × pedagógico** (E11, §8; R-29) é mantida na integração: o LMS pode registrar progresso/nota **no seu próprio domínio**, sob a base legal e a responsabilidade LGPD da **escola** — mas **nenhuma PII de aluno flui ao KC** e o produto **não** constrói o boletim. **[RECOMENDADO]/[ALTERNATIVA]:** LTI/SCORM para entrega de conteúdo; xAPI **apenas** se as *statements* permanecerem **fora do KC**, pseudonimizadas/agregadas e sob a base legal da escola (R-14.36). SSO/OAuth escolar é **[PENDÊNCIA]** de execução (E11, §7; R-14), sob o invariante de que a sessão respeita papel/faixa e nunca vaza identidade de menor.

### 9.4 O que a integração **não** faz

**[NORMATIVO]** a integração **não**: importa fato de LMS para o KC; aceita correção de claim vinda do LMS; coleta PII de aluno no núcleo; exporta expressão NC ou SA/ODbL fora do permitido; nem apresenta alinhamento como selo. Qualquer tentativa de escrita do LMS no KC é **incidente de fronteira** (§11; invariante 20).

---

## 10. Validação escolar, jurídica e comercial

### 10.1 Validação por evidência, não por promessa

O **`validationProgram`** conduz três trilhas de validação que **produzem evidência datada e versionada**, não selos. **[NORMATIVO]:** a operação **não** promete homologação MEC, aprovação PNLD nem validação jurídica definitiva (princípio 16; invariante 7; R-23; R-14.09/R-14.10). A validação **usa o conteúdo já curado** (publicável) e **não destrava portões** (princípio 4): pressão comercial/escolar **nunca** publica item bloqueado nem dispensa revisão.

```txt
ValidationEvidence = {
  evidenceId,
  track,                # escolar | juridica | comercial
  artifactRef,          # piloto, laudo, parecer, relatório — versionado e datado
  scope,                # a que escopo/lote/versão a evidência se refere
  claimAboutProduct,    # afirmação SOBRE O PRODUTO (não sobre o mundo); nunca um claim factual no KC
  validityWindow,       # evidência é de um ponto no tempo; expira/atualiza
  doesNotImply          # NÃO implica homologação MEC/PNLD nem validação jurídica definitiva (texto fixo)
}
```

### 10.2 Trilha escolar/pedagógica

**[RECOMENDADO]** piloto controlado com professores e turmas (sem PII real de aluno — E12, §11.2; ou sob base legal da escola e dados **agregados**): usabilidade, reconhecimento do diferencial sem confundir com currículo oficial (E12, §15.6), adequação por faixa, e **laudo de acessibilidade (ASES)** (invariante 23; `T-A11Y`). **[NORMATIVO]:** o alinhamento BNCC é exibido **como alinhamento `pending`** (E6; `T-HOMOLOGA`), nunca como aprovação; a evidência de piloto é insumo do `readiness-for-school` (Seção 7), não um selo.

### 10.3 Trilha jurídica

**[RECOMENDADO]** sob orientação do `legalReviewer` (que não é, e o documento não substitui, parecer de advogado): **DPIA/RIPD** (LGPD), conformidade ECA/proteção de menores, **auditoria de licença/IP** (invariantes 17–19/27), e acessibilidade legal (LBI). **[NORMATIVO]:** a trilha jurídica produz **evidência de conformidade de um ponto no tempo**, não uma "validação jurídica definitiva" (R-14.10); decisões de notificação a titular/autoridade em caso de incidente de dados são avaliadas **caso a caso** sob orientação jurídica, sem a operação presumir ou prometer um resultado específico (§11).

### 10.4 Trilha comercial / procurement

**[RECOMENDADO]** preparar o produto para **procurement público/privado** (compra pública, adoção por rede/escola): documentação de conformidade (acessibilidade, LGPD, licença), evidência de piloto, e materiais que descrevem o produto como **recurso educacional digital complementar** (E0/E6), **nunca** como substituto obrigatório do currículo nem como item homologado. **[NORMATIVO]:** procurement **não** é exceção aos portões (R-14.34): prazo de edital ou interesse comercial **nunca** publica item bloqueado nem dispensa revisão (princípio 4). Qualquer referência a PNLD/MEC é **explicitamente** "não homologado" (R-23; invariante 7). Conflito de interesse comercial na curadoria é risco monitorado (R-14.31) com segregação de funções (§3.1).

### 10.5 O que a validação **não** faz

**[NORMATIVO]** a validação **não**: executa o piloto/laudo/parecer real (limite desta etapa — define o programa); promete homologação/aprovação/validação definitiva; coleta PII real de aluno sem base legal (R-14.37); nem usa pressão comercial para destravar portão. Ela **define** as trilhas, os critérios e a forma da evidência; a execução é posterior (Etapa 15/execução).

---

## 11. Gestão de incidentes e rollback versionado

### 11.1 Princípio de incidente: conter primeiro, investigar depois, reverter por versão

A **`incidentResponsePolicy`** trata desvios operacionais. **[NORMATIVO]:** incidente que toque **fato, licença, conteúdo sensível ou menor** escala **imediatamente** e, se necessário, **despublica antes de investigar** (princípio 19) — o invariante de exibição (invariante 9) é restabelecido primeiro. **Rollback é versionado**: opera por **depreciação + restauração** da versão anterior preservada; **nada é apagado** (princípio 11; invariantes 16/29; `T-13.16`/`T-13.37`).

```txt
incidentSeverity = [ sev1-critical, sev2-high, sev3-moderate, sev4-low ]
incidentStatus   = [ detected, triaged, contained, mitigated, resolved, post-mortem-done ]

IncidentRecord = {
  incidentId, type, severity, status,
  detectedBy,            # auditoria/regressão/QA/relato; data
  affectedVersions,      # versões de conteúdo/derivados afetadas
  containment,           # ação imediata (despublicar, isolar, invalidar cache, recolher export)
  rollback,              # RollbackAction (Seção 11.3)
  rootCauseOwner,        # papel competente para a análise de causa-raiz
  linkedTestRiskInvariant,# T-13.NN / T-* / R-13.NN / R-14.NN / invariante associado
  notificationAssessment,# avaliação de dever de comunicação (LGPD/ECA) sob orientação do legalReviewer
  gatingReason           # registrado e auditável (princípio 17)
}

RollbackAction = {
  incidentRef, affectedVersions,
  action,                # deprecate-and-restore-prior | hide-pending-recheck | recall-export | invalidate-cache
  restoredVersionRef,    # versão anterior preservada que volta a vigorar (nunca apagamento)
  auditEntryRef, gatingReason
}
```

### 11.2 Matriz de incidentes e resposta

**[NORMATIVO]** a matriz liga cada incidente operacional ao gatilho de detecção, à severidade típica, à contenção imediata, ao rollback versionado e ao teste/risco/invariante associado.

| Incidente | Detecção | Sev. típica | Contenção imediata | Rollback versionado | Teste/Risco/Invariante |
|---|---|---|---|---|---|
| **Licença** (NC/SA/proprietário servido/exportado indevidamente; asset sem licença publicado) | auditoria de licença; regressão | sev1/sev2 | despublicar/recolher export; isolar asset | `recall-export` + `deprecate-and-restore-prior` | `T-13.04/05/06/17`; R-13.05/06; R-14.08; invariantes 17–19/27 |
| **Fonte fora do ar** | recheck (§12); `checksum`/disponibilidade | sev3 | marcar `sourceAvailability`; manter versão snapshotada | claim sobrevive na versão snapshotada | `R-13.33`; R-14.14; `T-13.15` |
| **Snapshot inválido** (corrompido/`checksum` falho/mutado) | regressão; auditoria de fonte | sev2 | bloquear uso do snapshot; congelar escopo | criar **novo** snapshot/versão; `deprecate-and-restore-prior` | `T-13.15`; R-13.07; R-14.15; invariante 28 |
| **Cache obsoleto** (fato vencido/revogado servido) | `T-13.18`; regressão | sev2 | `invalidate-cache`; reconstruir derivado | derivado reconstruído da versão vigente | `T-13.18`/`T-CACHE`; R-13.25; R-14.16; invariantes 2/26 |
| **Item sensível publicado indevidamente** (sem revisão/mediação) | auditoria de sensível; relato | sev1 | despublicar imediatamente; voltar a `pending` | re-revisão competente antes de re-publicar | E3.1; princípio 19; R-13.16; R-14.17 |
| **Bug de publicabilidade** (`pending`/`hiddenItems`/`teacherOnly` vazando como fato) | `T-13.14`; `T-PENDING`/`T-TEACHERONLY` | sev1 | restabelecer invariante de exibição; bloquear caminho | `hide-pending-recheck`; corrigir regra; revalidar | `T-13.14`; R-03/R-04; R-14.18; invariante 9 |
| **Erro de claim** (fato incorreto/tipagem/incerteza errada) | auditoria factual; relato; nova evidência | sev2/sev3 | despublicar item afetado | correção como **nova versão** (`supersedes`); anterior deprecada | `T-13.01/07/08/10`; R-13.34; R-14.19; invariantes 14/29 |
| **Erro de geometria** (paleoposição como atual; anacronismo; sem licença/status) | `T-13.13/23`; auditoria espacial | sev2/sev3 | despublicar geometria; exigir rótulo/`AnachronismNotice` | `deprecate-and-restore-prior` da geometria | `T-13.13/23`; R-13.12/13/17; R-14.20; invariante 22 |
| **Erro de acessibilidade** (sem equivalente textual; cor único canal; falha de teclado) | `T-A11Y`; auditoria ASES | sev2/sev3 | bloquear exibição do item até correção | re-publicar após equivalente textual adequado | `T-A11Y`; R-37; R-14.21; invariante 23 |
| **Vazamento de PII de aluno** (LGPD/ECA) | auditoria de privacidade; relato | sev1 | conter exposição; isolar dado; acionar `legalReviewer` | remover do fluxo; avaliar notificação (§11.4) | `T-PII`; invariantes 12/21; R-13.38; R-14.05/36/37 |
| **Escrita indevida no KC** (camada não autorizada) | `T-FRONTEIRA/T-API`; tentativa logada | sev1 | bloquear caminho de escrita; isolar | reverter qualquer gravação indevida por versão | invariante 20; R-13.26; R-14.26 |

### 11.3 Rollback versionado (nunca apagamento)

**[NORMATIVO]** o rollback **deprecia** a versão problemática e **restaura** a versão anterior preservada (`deprecate-and-restore-prior`), ou **oculta** o item pendente de recheck (`hide-pending-recheck`), ou **recolhe** o export comprometido (`recall-export`), ou **invalida** o cache (`invalidate-cache`) — sempre registrando `gatingReason` e a versão restaurada (`T-13.16`/`T-13.37`; invariantes 16/29). A trilha do que foi exibido **antes** da correção **sobrevive** para auditoria (princípio 11; R-13.37; R-14.12). Depreciação **excessiva** ("limpeza" que apaga histórico) é, ela própria, incidente (R-14.12).

### 11.4 Notificação e dever legal

**[NORMATIVO]** em incidentes de dados pessoais, o `legalReviewer` (apoiado pelo `dataProtectionSteward`) **avalia**, sob a LGPD/ECA, eventual dever de comunicação ao titular e à autoridade competente, **caso a caso**. A operação **não** presume nem promete um resultado específico de notificação, prazo ou consequência (consistente com o estatuto de "evidência, não promessa" — §10; princípio 16). O `IncidentRecord` registra a avaliação (`notificationAssessment`), não uma garantia.

### 11.5 Post-mortem e prevenção

**[RECOMENDADO]** todo incidente sev1/sev2 gera **post-mortem sem culpabilização** (`post-mortem-done`), com causa-raiz, ação preventiva e, quando aplicável, **novo teste/indicador** que detecte recorrência (alimentando as Seções 5/8). **[NORMATIVO]:** nenhuma ação preventiva pode "resolver" um incidente **relaxando** o invariante que o conteve (invariante 30; E13, §15.10).

---

## 12. Atualização de fontes vivas, snapshots e reprocessamento

### 12.1 Fontes vivas mudam; o produto não as segue cegamente

A **`liveSourcePolicy`** trata o fato de que fontes vivas mudam (`R-13.32`) e fontes adormecem ou saem do ar (`R-13.33`). **[NORMATIVO]:** mudança de fonte **cria nova versão de `Source` e novo `DatasetSnapshot`** (imutável — `T-13.15`; invariante 28); o claim **aponta à versão usada** (E13, §9.5/§9.7); **jamais** há atualização silenciosa (princípio 12; R-14.13). Fonte fora do ar **preserva o snapshot como prova** e marca `sourceAvailability`; o claim **sobrevive na versão snapshotada** (R-14.14).

```txt
LiveSourceRecheck = {
  recheckId, sourceRef, sourceClass,   # classe define a cadência (viva/oficial/estável)
  recheckCadence,                       # [REC]: frequente para fontes vivas; periódica para estáveis
  detectedChange,                       # diferença de checksum/conteúdo/versão da fonte
  action                                # new-snapshot+new-source-version | mark-unavailable | no-change
}

ReprocessingJob = {
  jobId, trigger,                       # mudança de fonte | correção de método | nova evidência | regressão
  affectedClaims,                       # claims que referenciam a versão anterior (via provenanceRef)
  reEntryStep,                          # ponto de reentrada no fluxo de 20 etapas da E13 (§5)
  versioning,                           # ADITIVO e VERSIONADO; supersedes; nunca sobrescrita em massa
  reReviewRequired,                     # revisão humana competente re-confirma o mérito
  cacheInvalidation                     # InvalidationRule dispara (T-13.18)
}
```

### 12.2 Reprocessamento versionado

**[NORMATIVO]** o reprocessamento é **aditivo e versionado**: ao mudar a fonte (ou o método de conversão/calibração, ou ao surgir nova evidência), os claims afetados **reentram pelo fluxo da Etapa 13 (§5)** a partir do passo apropriado, são **re-revisados** pelo papel competente e **versionados** (`supersedes`) — a versão anterior é **deprecada, nunca apagada** (`T-13.16`; invariante 29). De-duplicação evita ids duplicados (`T-13.20`; R-13.19; R-14.33). Reprocessamento **em massa** que quebre versionamento/ids é incidente (R-14.33). Ao concluir, cache/índice são invalidados (`T-13.18`).

### 12.3 Retenção e arquivamento de snapshots

**[NORMATIVO]** snapshots que comprovam **o que foi exibido** são preservados (referencial/versionado — invariante 16; `T-13.37`), mesmo sob custo de armazenamento; "limpeza" que apague essa prova é proibida (R-13.37; R-14.29). **[PENDÊNCIA]:** políticas finas de retenção/arquivamento (camadas de armazenamento frio, prazos por classe de snapshot) ficam para a execução (E13, §15.8), sob o invariante de que a prova do exibido nunca se perde.

---

## 13. Monitoramento de cobertura, lacunas e riscos

### 13.1 A matriz de cobertura

A **`coverageMonitoringPolicy`** monitora a cobertura do KC ao longo de **oito dimensões**, para orientar a priorização (lotes P0–P3 da E13, §13). **[NORMATIVO]:** cobertura é **descrição, não licença para baixar o piso** (princípio 13); uma lacuna é **sinalizada e priorizada**, **nunca** preenchida por IA, heurística ou fonte C (R-14.22/R-14.23); só fonte A/B sob o pipeline a preenche (princípios 1/2/3).

```txt
CoverageMatrix = {
  byLayer,            # as 25 camadas (E4A); cobertura e profundidade por camada
  byRegion,           # recorte espacial (Brasil/mundo); evitar eurocentrismo (E3.1)
  byPeriod,           # os 7 regimes temporais (E3Z); do tempo profundo ao contemporâneo
  bySource,           # dependência por fonte; redundância vs fonte única (R-14.38)
  byEditorialRisk,    # itens sensíveis vs cobertura/mediação (E3.1)
  byScientificRisk,   # inferência/reconstrução vs medição; incerteza alta
  byLicenseRisk,      # distribuição por risco 0–5; isolados vs núcleo
  byReviewStatus      # publicável vs pending/legal-review/rejected; gargalo de revisão
}

CoverageGap = {
  gapId, dimension, scope,
  prioritization,     # liga ao lote P0–P3 (E13, §13); herda prioridade da E4A
  resolutionPath,     # SEMPRE: fonte A/B sob o pipeline (E13); NUNCA IA/heurística/fonte C
  status              # aberto | priorizado | em-ingestao | coberto
}
```

### 13.2 Lacuna não é preenchida por suposição

**[NORMATIVO]** ao detectar lacuna, a operação **prioriza** (alimentando os lotes da E13) e **sinaliza** (`PENDENTE_*`/`CoverageGap`); ela **não** preenche com texto de IA, estimativa não fonteada ou fonte C como autoridade (R-14.22/R-14.23; princípios 1/2/3/13). A ausência de cobertura é **honesta**: a função (E5) já exclui o não contemporâneo e nomeia `gatingReason`/`hiddenItems`; a operação não "inventa" cobertura para parecer completa.

### 13.3 Mapa de calor de riscos

**[RECOMENDADO]** a operação mantém um **mapa de calor** agregando o estado dos riscos `R-13.NN` (E13, §14.2) e `R-14.NN` (Seção 14) com seus indicadores (Seção 8). **[NORMATIVO]:** todo risco do registro tem **teste, portão ou invariante associado e indicador monitorado** (E13, §14.2; §14 aqui); risco sem teste/indicador associado **bloqueia** a prontidão (`blocked` — Seção 7; E13, §15.10).

---

## 14. Riscos operacionais e mitigação

Trinta e oito riscos específicos da operação, cada um com mitigação ancorada nas seções acima e com indicador associado (Seção 8). Os riscos **não** substituem os da Etapa 11 (`R-NN`), do MVP (`R-MVP-NN`) nem da ingestão (`R-13.NN`); o prefixo `R-14.` os mantém distintos.

| ID | Risco | Impacto | Mitigação |
|---|---|---|---|
| **R-14.01** | QA virando "sugestão" | invariante violado por conveniência | QA bloqueia, não sugere; `qaGateResult` sem `waived`/`override`; falha rebaixa estado (§5; princípio 2) |
| **R-14.02** | Escala reduzindo profundidade de revisão | piso epistêmico cai sob volume | escala pausa antes de baixar revisão; qualidade soberana sobre velocidade (§7.3; princípio 3) |
| **R-14.03** | SLA estourado destravando portão | atalho por prazo | SLA escala/pausa intake, nunca pula portão (§4.3; princípio 21) |
| **R-14.04** | Pressão comercial destravando item bloqueado | publicação ilegítima | nenhuma pressão destrava; `legal-review` *default* não publica (§10.4; princípio 4; R-13.35) |
| **R-14.05** | Analytics capturando PII de aluno | violação LGPD/ECA | `dataMinimizationClass` SEM-PII/AGREGADO; sem PII de menor (§8; invariantes 12/21) |
| **R-14.06** | Analytics individualizando aluno | telemetria individual proibida | métrica mede operação/conteúdo; uso só AGREGADO por turma (§8; princípio 7; R-28) |
| **R-14.07** | LMS escrevendo fato no KC | fronteira violada | LMS só consome publicável; `writeToKnowledgeCore` proibido (§9; invariante 20; R-29) |
| **R-14.08** | LMS exportando NC/SA fora do permitido | violação de licença | matriz de licença por export; NC nunca; SA/ODbL fora de pacote aberto (§9.2; invariantes 18/19/27) |
| **R-14.09** | Validação prometendo homologação MEC/PNLD | promessa falsa | validação é evidência, não selo; nota anti-homologação (§10; invariante 7; R-23) |
| **R-14.10** | "Validação jurídica definitiva" prometida | promessa falsa | evidência de ponto no tempo; não substitui parecer; `doesNotImply` (§10.3) |
| **R-14.11** | Incidente sem rollback versionado | correção por apagamento | rollback deprecia+restaura; nunca apaga (§11.3; `T-13.16`; invariante 29) |
| **R-14.12** | Rollback/limpeza apagando trilha | histórico perdido | depreciar nunca apaga; prova do exibido preservada (§11.3/§12.3; `T-13.37`) |
| **R-14.13** | Fonte viva atualizada silenciosamente | claim referenciando estado inexistente | nova versão+snapshot; claim aponta à versão usada (§12; princípio 12; R-13.32) |
| **R-14.14** | Fonte fora do ar quebrando proveniência | proveniência inacessível | snapshot preservado como prova; `sourceAvailability` (§12; R-13.33) |
| **R-14.15** | Snapshot inválido servindo como prova | proveniência corrompida | `checksum`; snapshot imutável; novo snapshot ao falhar (§11.2/§12; `T-13.15`) |
| **R-14.16** | Cache obsoleto servindo fato vencido | derivado servindo fato revogado | `InvalidationRule`; `cache não é verdade` (§11.2; `T-13.18`; invariantes 2/26) |
| **R-14.17** | Item sensível publicado sem revisão | dano editorial; descumprir Leis 10.639/11.645 | revisão obrigatória; despublica e re-revisa (§11.2; E3.1; princípio 19) |
| **R-14.18** | Bug de publicabilidade vazando `pending`/`hiddenItems` | não-fato exibido como fato | invariante de exibição restabelecido primeiro (§11.2; `T-13.14`; invariante 9) |
| **R-14.19** | Erro de claim publicado | fato incorreto exposto | correção como nova versão; anterior deprecada (§11.2; R-13.34; invariante 14) |
| **R-14.20** | Erro de geometria/paleoposição | anacronismo exibido como real | rótulo/`AnachronismNotice`; despublica e corrige (§11.2; `T-13.23`; invariante 22) |
| **R-14.21** | Erro de acessibilidade | exclusão de usuário | bloqueia exibição até equivalente textual (§11.2; `T-A11Y`; invariante 23) |
| **R-14.22** | Cobertura virando justificativa para baixar piso | lacuna preenchida por suposição | cobertura é descrição; lacuna priorizada, não preenchida (§13.2; princípio 13) |
| **R-14.23** | Lacuna preenchida por IA/heurística | fato sem fonte A/B | `resolutionPath` sempre fonte A/B sob pipeline; nunca IA/fonte C (§13; princípios 1/2/3) |
| **R-14.24** | Amostragem de revisão insuficiente | aprovação rasa não detectada | sensíveis 100%; amostra dos demais; baixar amostra pausa intake (§6.2; R-13.21) |
| **R-14.25** | Papel operando fora de competência sob pressão de fila | decisão sem qualificação | matriz de competência; "negar vence" (§3; `T-13.22`; R-13.22) |
| **R-14.26** | Operação reabrindo fronteira de escrita | escrita factual fora do pipeline | fronteiras E11 imutáveis; tentativa é incidente crítico (§11.2; invariante 20) |
| **R-14.27** | Dashboard/relatório tratado como fato | derivado confundido com verdade | `dashboard não é verdade`; métrica `carriesProvenance=false` (§6.4/§8; princípio 14) |
| **R-14.28** | Throughput priorizado sobre qualidade (Goodhart) | qualidade sacrificada por meta | qualidade soberana sobre velocidade; anti-Goodhart (§7.3) |
| **R-14.29** | Retenção/descarte apagando prova | auditoria impossível | prova do exibido preservada; retenção fina é PENDÊNCIA sob esse piso (§12.3; `T-13.37`) |
| **R-14.30** | Burnout/turnover degradando QA | revisão perde profundidade | capacidade/turnos; indicador de carga; intake pausa se faltar gente (§3.3) |
| **R-14.31** | Conflito de interesse comercial na curadoria | viés/destrave indevido | segregação de funções; comercial não decide mérito (§3.1/§10.4) |
| **R-14.32** | Escalonamento de incidente lento | dano prolongado | plantão `incidentCommander`; sev1/sev2 com 1ª resposta imediata (§4.3/§11) |
| **R-14.33** | Reprocessamento em massa quebrando versionamento/ids | grafo fragmentado | reprocessamento aditivo/versionado; `supersedes`; de-duplicação (§12.2; `T-13.20`) |
| **R-14.34** | Procurement empurrando prazo que fura portão | edital/contrato burla revisão | procurement não é exceção; portões mantidos (§10.4; princípio 4) |
| **R-14.35** | "Ready-for-scale" declarado por prazo | escala sem qualidade | readiness por critério objetivo, não prazo (§7.2; princípio 2/3) |
| **R-14.36** | LMS/SSO vazando identidade de menor | violação LGPD/ECA | identidade separada; xAPI fora do KC/pseudonimizado; SSO sob invariante de papel (§9.3) |
| **R-14.37** | Piloto coletando PII real de aluno sem base legal | violação LGPD/ECA | piloto sem PII real ou sob base legal da escola e dados agregados (§10.2/§10.5) |
| **R-14.38** | Dependência de fonte única sem redundância | fragilidade de proveniência | monitorar `bySource`; buscar redundância A/B; snapshot preserva o vigente (§13.1; §12) |

**[NORMATIVO]:** este registro é **vinculante**; cada risco tem teste, portão ou invariante associado e um indicador monitorado (§8). Nenhum risco é "resolvido" relaxando o invariante que o contém (invariante 30; E13, §15.10).

---

## 15. Encerramento e handoff para a Etapa 15

### 15.1 O que a Etapa 14 entrega

A Etapa 14 entrega a **`OperationalGovernanceLayer` completa em nível de arquitetura operacional**: a definição da camada e sua relação com as Etapas 11/12/13 (Seção 1); **22 princípios operacionais** vinculantes (Seção 2); a **governança dos dez papéis** com seis funções de governança de processo e a matriz de governança (Seção 3); os enums operacionais `readinessStatus`/`queueState`/`qaGateResult`, as doze filas operacionais, a matriz de SLAs e o escalonamento "negar vence" (Seção 4); o **programa de QA contínuo** com três cadências, seis tracks separados e a execução dos **24 testes `T-13.NN`** (mais `T-*` do MVP e os 30 invariantes da E11) como **portões bloqueantes** (Seção 5); o **programa de auditoria** com trilhas de decisão, amostragem de qualidade de revisão, sete auditorias periódicas, cadeia de rastreabilidade e relatórios executivos agregados (Seção 6); a **estratégia de escala** com a matriz de prontidão objetiva (`ready-for-pilot`/`ready-for-school`/`ready-for-scale`/`blocked`) e o princípio anti-Goodhart (Seção 7); o **framework de analytics agregado** com `OperationalMetric` e a matriz de indicadores mínimos, sempre **SEM PII** (Seção 8); o **contrato de integração LMS** por consumo/exportação controlada com identidade separada (Seção 9); o **programa de validação** escolar/jurídica/comercial por **evidência**, sem prometer homologação (Seção 10); a **gestão de incidentes** com enums de severidade/status, `IncidentRecord`/`RollbackAction`, a matriz de incidentes e resposta e o rollback **versionado** (Seção 11); a **política de fontes vivas e reprocessamento versionado** com `LiveSourceRecheck`/`ReprocessingJob` (Seção 12); o **monitoramento de cobertura** com `CoverageMatrix`/`CoverageGap` em oito dimensões e o mapa de calor de riscos (Seção 13); e a **matriz de 38 riscos operacionais `R-14.NN`** com mitigação (Seção 14).

### 15.2 O que a Etapa 14 **não** entrega

A Etapa 14 **não** entrega: código, ferramentas reais, testes executados, scraping, downloads, banco povoado ou ingestão executada; conteúdo factual novo (nenhum claim/fonte/cena criado ou alterado); alteração da Etapa 13 ou das cenas-gabarito; mapeamento de BNCC em massa ou tratamento de BNCC como fonte; coleta de PII real de aluno; analytics individualizado de aluno; um LMS próprio completo; piloto/laudo/parecer real executado; nem promessa de homologação MEC, aprovação PNLD ou validação jurídica definitiva. Esses itens ou são proibidos por natureza ou pertencem à Etapa 15 e à execução.

### 15.3 Invariantes que passam a ser vinculantes

A partir desta entrega, vinculam a operação (somando-se aos 30 invariantes da E11, aos testes `T-*` do MVP e aos 28 princípios / 24 testes `T-13.NN` / 38 riscos `R-13.NN` da E13): **(i)** a operação serve ao núcleo e não o governa (Seção 1); **(ii)** os 22 princípios operacionais (Seção 2); **(iii)** QA bloqueia, não sugere — `qaGateResult` sem *override*/*waiver* (Seção 5); **(iv)** os seis tracks de QA como portões independentes e bloqueantes (Seção 5.3); **(v)** a matriz de prontidão objetiva e o rebaixamento automático sob falha (Seção 7); **(vi)** analytics agregado SEM PII, nunca fonte (Seção 8); **(vii)** LMS como consumidor, nunca escritor, com identidade separada (Seção 9); **(viii)** validação por evidência, sem promessa de homologação (Seção 10); **(ix)** rollback versionado, nunca apagamento (Seção 11); **(x)** fonte viva → nova versão+snapshot, reprocessamento aditivo/versionado (Seção 12); **(xi)** cobertura é descrição, lacuna nunca preenchida por suposição (Seção 13). Permanecem canônicas: **forma muda; fato não**; **score/cache/busca/embedding/dashboard não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**; **correção cria versão, nunca apaga**.

### 15.4 Estados e entidades que ficam oficiais

Ficam oficiais e estáveis para a Etapa 15: os enums `readinessStatus` (5 valores), `queueState` (6 valores), `qaGateResult` (2 valores, sem *override*), `incidentSeverity` (4) e `incidentStatus` (6) da Seção 4/§11; as doze `operationalQueue`; os seis `qaTrack`; as seis `operationalGovernanceFunction`; e as entidades `OperationalGovernanceLayer`, `OperationalAuditProgram`, `OperationalMetric`, `LMSIntegrationContract`, `ValidationEvidence`, `IncidentRecord`, `RollbackAction`, `LiveSourceRecheck`, `ReprocessingJob`, `CoverageMatrix` e `CoverageGap`. Alterá-los exige reabrir a Etapa 14.

### 15.5 O que a Etapa 15 (plano comercial / go-to-market) deve receber

```txt
para a Etapa 15 = {
  a matriz de prontidão objetiva (ready-for-pilot/school/scale/blocked) como gate de qualquer oferta,
  a evidência de validação (escolar/jurídica/comercial) como insumo de proposta — NUNCA como selo MEC/PNLD,
  o framework de analytics AGREGADO (adoção por turma/escola) sem PII de aluno, para métricas de negócio,
  o contrato de integração LMS (consumo/exportação) como caminho técnico de distribuição,
  a base de procurement público/privado com a nota anti-homologação e o estatuto de recurso COMPLEMENTAR,
  o registro de riscos R-14.NN e o mapa de calor como due diligence operacional para parceria/captação,
  a regra inegociável de que comercial/procurement NUNCA destrava portão nem dispensa revisão (princípio 4)
}
```

### 15.6 O que a operação deve monitorar (síntese)

**[NORMATIVO]** indicadores mínimos (Seção 8.2): funil por `ingestionStatus`/`populationStatus`; taxa de bloqueio por `gatingReason`; *lead time* e gargalo por fila; acúmulo em `legal-review`/`blocked-license`; integridade de `checksum` e cobertura de snapshot; fontes vivas alteradas/fora do ar; revisões escaladas e amostragem de qualidade de revisão; placeholders ativos; invalidação de cache/índice pós-decisão; tentativas de escrita por camada não autorizada; cobertura por camada/região/período/fonte/risco editorial/risco científico/risco de licença/`reviewStatus`; carga por papel e turnover; MTTR e incidentes por tipo; desempenho/degradação; e uso **agregado** por turma/escola — tudo SEM PII de aluno.

### 15.7 Papéis e funções que precisam existir

Para operar, devem existir de fato (não apenas no papel): os **dez papéis de ingestão** (E13, §3) e as **seis funções de governança de processo** desta etapa (`operationsLead`, `qaConductor`, `auditLead`, `incidentCommander`, `dataProtectionSteward`, `scaleCoordinator` — Seção 3), acoplados aos papéis técnicos/curatoriais da E11 (§7.2) e **estritamente separados** dos papéis escolares/de leitura (sem PII de aluno; sem credencial de escrita no KC).

### 15.8 Pendências que seguem abertas

**[PENDÊNCIA]** para a Etapa 15/execução: números concretos de SLA por fila (§4.3) e percentuais de amostragem de auditoria de revisão (§6.2), calibrados por capacidade; cadências concretas de recheck de fonte viva e políticas finas de retenção/arquivamento de snapshots sob custo (§12.3); mecanismo concreto de SSO/OAuth escolar e a decisão sobre xAPI/SCORM/LTI na integração LMS (§9.3; E11, §7); execução real do piloto, do laudo ASES, da DPIA/RIPD e dos pareceres jurídicos (§10); calendários não-ocidentais como `sourceTimeBasis` adicionais (herdada — E3Z; E13, §11.4); e a expansão de fontes A/B por área, cada nova fonte passando pela Etapa 1/1.1 antes de uso (§7/§13).

### 15.9 Critérios que autorizam passar para a Etapa 15

A Etapa 15 (plano comercial / implantação piloto / parcerias / captação / procurement / go-to-market) é autorizada quando: ao menos um escopo atinge `ready-for-pilot` sob critérios objetivos (Seção 7); a matriz `T-13.NN` opera como portão bloqueante e os seis tracks de QA estão verdes para esse escopo (Seção 5); os dez papéis e as seis funções de governança existem e operam (Seção 3); o analytics agregado está ativo SEM PII (Seção 8); a gestão de incidentes e o rollback versionado estão definidos (Seção 11); e a integração LMS e o programa de validação estão definidos como **consumo/evidência**, sem prometer homologação (Seções 9/10).

### 15.10 Critérios que bloqueiam a passagem

A passagem é **bloqueada** enquanto: existir caminho de escrita factual fora do pipeline (fronteiras da E11 violadas); qualquer teste `T-13.NN`/`T-*` puder ser destravado por urgência/autoridade/pressão comercial (R-13.35; R-14.04/34); QA puder operar como "sugestão" (R-14.01); a escala puder ser declarada `ready-for-scale` por prazo e não por critério (R-14.35); analytics coletar PII de aluno ou individualizar estudante (R-14.05/06); o LMS puder escrever fato no KC ou exportar NC/SA fora do permitido (R-14.07/08); a validação prometer homologação MEC/PNLD ou validação jurídica definitiva (R-14.09/10); algum incidente puder ser "resolvido" por apagamento (R-14.11/12); uma lacuna de cobertura puder ser preenchida por suposição (R-14.22/23); ou houver risco do registro (Seções 13/14) sem teste/portão/invariante associado e monitorado.

---

*Documento de entrega da Etapa 14 — Operação, Governança, QA, Escala, Analytics Agregado, LMS e Validação (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8, 9, 10, 11, 12, 13). Define a `OperationalGovernanceLayer`: os 22 princípios operacionais, a governança dos dez papéis e as seis funções de processo, os estados/filas/SLAs/escalonamento, o programa de QA contínuo (três cadências, seis tracks, os 24 testes `T-13.NN` como portões bloqueantes), o programa de auditoria (trilhas, amostragem, auditorias periódicas, relatórios agregados), a estratégia de escala com a matriz de prontidão objetiva, o framework de analytics agregado SEM PII, o contrato de integração LMS por consumo, o programa de validação por evidência, a gestão de incidentes com rollback versionado, a política de fontes vivas e reprocessamento versionado, o monitoramento de cobertura em oito dimensões e a matriz de 38 riscos operacionais `R-14.NN`. Não escreve código, não implementa ferramentas reais, não roda testes reais, não faz scraping, não baixa fontes, não popula banco, não cria claims, não altera as cenas-gabarito, não altera a Etapa 13, não mapeia BNCC em massa, não trata BNCC como fonte, não coleta PII de aluno, não cria analytics individualizado, não cria LMS próprio completo, não promete homologação MEC/PNLD nem validação jurídica definitiva, não permite que operação/comercial/escola/professor/LMS/IA/cache/busca/dashboard escrevam fatos no KC e não permite que pressão comercial destrave item bloqueado. A operação serve ao núcleo, não o governa; QA bloqueia, não sugere; escala nunca reduz revisão; analytics mede a operação, não alunos individualmente; LMS consome conteúdo publicável, não escreve fato; e qualquer dúvida de fonte, licença, claim, data, geometria, sensibilidade, acessibilidade ou privacidade resulta em bloqueio/revisão, nunca em publicação automática. Próxima etapa, quando solicitada: Etapa 15 — Plano comercial, implantação piloto, parcerias, captação, procurement público/privado e estratégia de go-to-market.*
