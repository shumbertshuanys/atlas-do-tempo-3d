# Etapa 15 — Plano Comercial, Implantação Piloto, Parcerias, Captação, Procurement Público/Privado e Go-to-Market

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Versão:** **v1.0**
**Status:** Entrega da **Etapa 15** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão de ingestão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5), o encerramento da Etapa 5 (5Z), a `BrazilianEducationComplianceLayer` (Etapa 6), a `TeacherSchoolPlanningLayer` (Etapa 7, v1.1), o `ContentMatchingEngine` (Etapa 8), a `PedagogicalOutputLayer` (Etapa 9), a `DesignUX3DLayer` (Etapa 10), a `TechnicalArchitectureLayer` (Etapa 11), o `MVPRelease` (Etapa 12), o `IngestionPopulationPipeline` (Etapa 13) e a `OperationalGovernanceLayer` (Etapa 14) · 14/06/2026

**Natureza desta etapa.** Documento de **estratégia comercial, implantação e go-to-market**. Define **como o produto entra no mercado depois do MVP (E12), do pipeline real de ingestão (E13) e da camada operacional de governança (E14)** — como a arquitetura acumulada vira proposta de valor, pilotos, parcerias, captação e vendas públicas/privadas — **sem criar conhecimento novo, sem alterar claims, sem relaxar licenças, sem coletar PII de aluno, sem prometer homologação e sem permitir que pressão comercial destrave qualquer portão**. Conforme solicitado, esta etapa **não** escreve código; **não** implementa CRM; **não** cria contrato jurídico definitivo; **não** simula edital real específico sem fonte oficial; **não** promete homologação MEC, aprovação PNLD ou validação jurídica definitiva; **não** cria `Claim`/`Source`/`Citation`/`Scene`/`Relationship` nem conteúdo factual novo; **não** altera o Knowledge Core; **não** altera a Etapa 14; **não** permite que comercial/procurement destrave item bloqueado; **não** coleta PII de aluno; **não** cria analytics individualizado de aluno; **não** vende alinhamento BNCC como selo oficial; **não** vende o produto como currículo obrigatório nem como substituto de professor; **não** oculta incerteza, fonte, licença ou publicabilidade; **não** permite white-label que remova rótulos epistêmicos, fontes, licenças, acessibilidade ou nota anti-homologação; e **não** permite que parceiro externo escreva fatos no Knowledge Core. Ela **pode**, porém: definir a camada estratégico-comercial, os princípios e limites de mercado, a proposta de valor e o posicionamento, os ICPs/personas institucionais, os modelos de implantação e pacotes, o programa de pilotos sem PII, os modelos de parceria, a tese de captação e os marcos de tração, a base de procurement público/privado, a precificação conceitual e o modelo de receita, os materiais comerciais e o discurso de venda responsável, as métricas comerciais agregadas, o registro de riscos comerciais, os critérios de prontidão comercial e o handoff para uma eventual Etapa 16 (implantação real, execução de piloto, negociação, documentos comerciais, captação, contratos e cronograma).

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores controladas. Papéis humanos em `camelCase` (ex.: `commercialLead`). Blocos ```txt``` são **dicionário conceitual, nunca código executável** nem especificação de implementação. "O KC" = o Knowledge Core (Etapa 2). "O portão" = o checklist/portão de licenças da Etapa 1.1. "O pipeline" = o `IngestionPopulationPipeline` (Etapa 13). "A arquitetura técnica" = a `TechnicalArchitectureLayer` (Etapa 11). "O MVP" = o `MVPRelease` (Etapa 12). "A operação" = a `OperationalGovernanceLayer` (Etapa 14). "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "O comercial" = a `CommercialGoToMarketLayer` definida na Seção 1. Referências cruzadas: "invariante N" = invariante técnico N da Etapa 11 (§13); "`T-13.NN`" = teste de invariante da Etapa 13 (§14.1); "`R-13.NN`" = risco da Etapa 13 (§14.2); "`R-14.NN`" = risco operacional da Etapa 14 (§14); "princípio operacional N" = princípio da Etapa 14 (§2); "`readinessStatus`" = enum de prontidão da Etapa 14 (§7.2); "nota anti-homologação" = exigência de exibir, em viewer e export, que o produto **não** é homologado pelo MEC nem aprovado no PNLD (E6; invariante 7).

> **Convenção de estatuto das decisões (herdada das Etapas 11/12/13/14).** **[NORMATIVO]** = vinculante, não pode ser violado sem reabrir a etapa; **[RECOMENDADO]** = opção preferida, substituível por equivalente que preserve os invariantes; **[ALTERNATIVA]** = opção aceitável citada para comparação; **[PENDÊNCIA]** = decisão deliberadamente adiada (para a Etapa 16 ou para a execução), registrada para ser carregada. Nomes de canais, modelos de negócio e **números concretos** (preços, tickets, metas de receita, prazos de venda, percentuais de desconto), quando aparecem, são sempre **[RECOMENDADO]**/**[ALTERNATIVA]**/**[PENDÊNCIA]**, nunca **[NORMATIVO]**: o normativo é a propriedade comercial (ex.: "procurement não destrava portão"), não o valor que a realiza.

> **Regra central desta etapa.** O comercial **vende o produto; não governa o núcleo**. A `CommercialGoToMarketLayer` é o conjunto disciplinado de posicionamento, oferta, parceria, captação e procurement que **leva ao mercado o conteúdo publicável (E11/E12) e a operação madura (E14)** — sem nunca virar caminho de escrita factual, sem afrouxar uma garantia e sem comprar exceção a um portão. A pergunta que esta etapa responde: *"Como o Atlas do Tempo 3D entra no mercado — posicionando-se, vendendo, fazendo pilotos, parcerias, captação e procurement público/privado — sem que prazo de edital, interesse de investidor, pressão de cliente, contrato de parceiro ou promessa de venda se tornem verdade factual, relaxem licença, exponham dados de menor ou destravem um item bloqueado?"* Seis frases-síntese governam todo o documento: **comercial vende, não governa**; **procurement não destrava portão**; **piloto não coleta PII de aluno**; **métricas comerciais são agregadas**; **BNCC é alinhamento, não selo**; **validação é evidência, não promessa**. E, abrangendo tudo: **qualquer pressão de mercado que tente violar QA, licença, privacidade, acessibilidade, publicabilidade ou revisão humana resulta em bloqueio, nunca em exceção.** Permanecem canônicas e invioláveis: **forma muda; fato não**; **score não é verdade**; **cache não é verdade**; **busca/embedding não é verdade**; **dashboard/relatório não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**; **correção cria versão, nunca apaga**. A elas a Etapa 15 acrescenta: **preço não compra destravamento**; **proteção de menor é piso, não recurso de venda**; **honestidade epistêmica é diferencial, não defeito a esconder**.

---

## Sumário

1. Definição da `CommercialGoToMarketLayer`
2. Princípios comerciais e limites de mercado
3. Proposta de valor e posicionamento
4. Segmentos, ICPs e personas institucionais
5. Modelos de implantação e pacotes comerciais
6. Pilotos escolares e validação de mercado
7. Parcerias estratégicas
8. Captação e tese de investimento
9. Procurement público e privado
10. Precificação conceitual e modelo de receita
11. Materiais comerciais, demonstrações e discurso de venda
12. Métricas comerciais permitidas e analytics agregado
13. Riscos comerciais, jurídicos, pedagógicos e reputacionais
14. Critérios de prontidão comercial e bloqueios
15. Encerramento e handoff para a Etapa 16

---

## 1. Definição da `CommercialGoToMarketLayer`

### 1.1 O que o comercial é

A **`CommercialGoToMarketLayer`** é a **camada estratégico-comercial do produto**: o conjunto disciplinado de posicionamento, segmentação, oferta, implantação, parceria, captação, procurement e materiais comerciais por meio do qual o Atlas do Tempo 3D **chega ao mercado de forma governada, honesta e auditável**. Ela é a contraparte de mercado de três peças já fixadas: o **conteúdo publicável** (E11/E12) — o que se pode mostrar e exportar; a **operação madura** (E14) — a prontidão objetiva que autoriza ofertar; e a **conformidade educacional** (E6) — o que se pode e o que não se pode afirmar perante a educação brasileira. Onde a Etapa 14 define **como o produto opera, mede-se e se valida em produção**, a Etapa 15 define **como esse produto pronto é levado ao cliente, ao parceiro, ao investidor e ao comprador público/privado** — sem que o ato de vender se torne, ele próprio, um caminho de escrita no núcleo nem uma exceção a um portão.

O comercial é o último dos quatro planos anunciados desde a Etapa 11 (invariante 30): o **PlanoComercial**, separado do PlanoArquitetural (E11), do PlanoImplementacao (E12/E13) e do PlanoOperacional (E14), que **herda** e **não pode afrouxar** nenhum invariante dos planos anteriores. Ele ocupa exatamente o espaço que a Etapa 14 lhe transferiu (E14, §15.5): a matriz de prontidão objetiva como gate de qualquer oferta; a evidência de validação como insumo de proposta — **nunca** como selo MEC/PNLD; o framework de analytics **agregado** sem PII como base de métricas de negócio; o contrato de integração LMS como caminho técnico de distribuição; a base de procurement com a nota anti-homologação e o estatuto de recurso **complementar**; o registro de riscos como *due diligence*; e a regra inegociável de que **comercial/procurement nunca destrava portão nem dispensa revisão** (princípio operacional 4).

### 1.2 O que o comercial **não** é

O comercial **não é** uma fonte de verdade: ele não "produz", "corrige" nem "completa" fatos; ele **comunica e vende** o que a curadoria já fez atravessar sob proveniência. Ele **não é** um caminho de escrita no KC — vendedor, parceiro, investidor, comprador público, CRM, peça de marketing e material de demo permanecem **leitores de conteúdo publicável**, jamais escritores de `Claim`/`Source`/`Citation`/`Relationship`/`reviewStatus`/`publicabilityStatus`/`confidenceLevel`/`claimType` (invariantes 4–8/13/20; princípio operacional 5). Ele **não é** uma exceção aos portões: nenhum prazo de edital, interesse de investidor, pressão de cliente ou cláusula de contrato destrava um item `blocked-license`/`legal-review`/`rejected`/`pending` nem faz passar um teste reprovado (princípio operacional 4; R-13.35; R-14.04/R-14.34). Ele **não é** um selo de homologação: ele **posiciona** o produto como recurso educacional digital **complementar** (E0/E6), exibe alinhamento BNCC **como alinhamento** (nunca aprovação) e **valida por evidência**, sem prometer homologação MEC, aprovação PNLD nem validação jurídica definitiva (E14, §10; invariante 7). E ele **não é** um coletor de dados de aluno: nenhum piloto, demo, métrica comercial ou material de venda coleta ou retém PII de menor (princípios operacionais 7/8; invariante 21).

### 1.3 Por que o comercial vende sem governar

A direção única de dependência (E11, §2; invariantes 4–8/20/25) **não se inverte no comercial**, exatamente como não se inverteu na operação (E14, §1.3). O comercial observa a prontidão, compõe propostas, negocia, distribui e reporta — todas ações de **leitura, comunicação e governança de relação de mercado**, nenhuma de **escrita factual**. Três mecanismos herdados o tornam estruturalmente incapaz de virar fonte ou exceção: **(1)** o caminho de escrita factual é **único e fechado** (E11, §6; E13, §1.3) e o comercial não tem porta de escrita no KC — nem o vendedor, nem o parceiro, nem o cliente; **(2)** o invariante de exibição (invariante 9) e a nota anti-homologação (invariante 7) valem em **toda** vista, demo, export, pacote LMS e material comercial, e o comercial é obrigado a respeitá-los, não a contorná-los; **(3)** todo derivado comercial (proposta, pitch, métrica de tração, dashboard de vendas) tem `originClass = derivado`, é reconstruível e **nunca** é consultado como fato (invariantes 2/3/26; princípio operacional 14). O comercial **decide sobre a relação de mercado** (oferta, preço, parceria, canal, captação); **nunca decide sobre o fato** (isso é dos revisores de mérito do pipeline), nem sobre a publicabilidade (isso é do invariante de exibição + revisão humana), nem sobre a prontidão (isso é da operação — E14, §7).

### 1.4 Relação com as etapas anteriores (síntese)

| Etapa | O que o comercial herda e respeita |
|---|---|
| **0** | tese, posicionamento (recurso educacional digital **complementar**, objeto de aprendizagem, apoio ao professor — D1); não-objetivos (nunca substituto de currículo/livro/LMS); honestidade epistêmica como **feature visível** (D7); cobertura **estrutural, não exaustiva** (D5) |
| **1 / 1.1** | níveis A/B/C; risco de licença 0–5; códigos `AUTO`/`ATRIB`/`ISOLA`/`FATO`/`REVH`/`CONF`/`COMER`/`NAO`/`INDX`; **uso comercial só conforme a licença** (código `COMER`); fonte de parceiro passa pelo portão antes de uso |
| **2** | claim-first; proveniência obrigatória; incerteza tipada; KC soberano; nada que o comercial faça cria/edita claim |
| **3Z / 3.1** | datum canônico; controvérsia → `ClaimSet`; negacionismo fora do `ClaimSet`; **incerteza nunca é escondida para vender** |
| **4A–4H / 4Z** | 25 camadas; `Scene` v1.1; cenas-gabarito **inalteráveis**; critérios de publicabilidade definem o que a demo pode mostrar |
| **5 / 5Z** | `WhatWasHappeningAtMoment` como diferencial central de produto; `gatingReason`/`hiddenItems` nunca como fato em demo; anti-falsa-equivalência |
| **6** | `BNCCMapping`/`CurricularAlignment` como **alinhamento** externo, nunca selo; afirmações permitidas vs proibidas (§8 desta etapa); nota anti-homologação; estatuto de recurso complementar perante a LDB |
| **7 / 8 / 9 / 10** | Planning/Matching/Output/UX como leitores/anotadores; a demo usa a UX (E10) e as saídas (E9) sem virar fonte; `score não é verdade` |
| **11** | lojas físicas; RBAC+ABAC; `dataMinimizationClass`; 30 invariantes; **nota anti-homologação (invariante 7)**; **minimização de PII de menor (invariante 21)**; o comercial é mais um leitor sob a fronteira de escrita única (invariante 20) |
| **12** | `MVPRelease`; testes `T-*`; seed marcado como `seed-MVP` — **a demo nunca apresenta seed/placeholder como conteúdo real** (R-13.18) |
| **13** | `IngestionPopulationPipeline`; 28 princípios; **fonte/conteúdo de parceiro entra exclusivamente pelo pipeline e pelo portão E1/1.1** (princípio de ingestão 22; R-13.01); `R-13.NN` como insumo de *due diligence* |
| **14** | `readinessStatus` (gate de oferta); `ValidationEvidence` (`doesNotImply`); `OperationalMetric`/analytics **agregado sem PII**; `LMSIntegrationContract`; programa de validação por evidência; `R-14.NN` e mapa de calor como *due diligence* operacional; **procurement não é exceção (R-14.34); pressão comercial não destrava (R-14.04)** |

### 1.5 A entidade conceitual do comercial

```txt
CommercialGoToMarketLayer = {
  layerId,
  scope,                       # leva ao mercado o publicável (E11/E12) sob a prontidão (E14); jamais escreve fato, jamais coleta PII de aluno
  positioningPolicy,           # recurso educacional digital COMPLEMENTAR; honestidade epistêmica como diferencial (Seção 3)
  valuePropositionModel,       # ValuePropositionMap por segmento; o que se promete e o que NÃO se promete (Seção 3)
  segmentationModel,           # MarketSegmentProfile/ICPProfile/InstitutionalPersona (Seção 4)
  deploymentModel,             # DeploymentPackage por deploymentTier; o que cada pacote inclui e exclui (Seção 5)
  pilotProgram,                # PilotProgram SEM PII real de aluno; evidência alimenta readinessStatus (Seção 6)
  partnershipModel,            # PartnershipModel por partnershipType; parceiro NUNCA escreve fato no KC (Seção 7)
  fundraisingModel,            # InvestmentThesis/FundingMilestone; due diligence = registro de riscos; captação não compra exceção (Seção 8)
  procurementModel,            # ProcurementDossier/ProcurementRequirement; procurement NÃO destrava portão; nota anti-homologação (Seção 9)
  pricingModel,                # PricingModel CONCEITUAL; números são [PENDÊNCIA]; preço não compra destravamento (Seção 10)
  collateralModel,             # CommercialCollateral + ResponsibleMarketingPolicy; demo usa publicável (Seção 11)
  commercialMetricsPolicy,     # CommercialMetric herda OperationalMetric; AGREGADO; SEM PII; nunca fonte (Seção 12)
  commercialRiskRegister,      # R-15.NN com mitigação e indicador associado (Seção 13)
  commercialReadinessPolicy,   # readinessStatus como gate de oferta; bloqueios (Seção 14)
  handoffToExecution           # o que a Etapa 16 recebe (Seção 15)
}
```

**[NORMATIVO]:** `CommercialGoToMarketLayer` é uma **entidade de governança de relação de mercado**, externa a todo conteúdo. Ela **não** cria, edita ou deprecia `Claim`/`Source`/`Scene` por si; ela **posiciona, oferta, negocia, distribui e reporta**, sempre **lendo** o conteúdo publicável (E11/E12) e a prontidão (E14). `handoffToExecution` entrega plano e prontidão, **não** autoriza relaxar invariante. O `scope` jamais inclui escrita factual, currículo como selo, nem PII de aluno.

---

## 2. Princípios comerciais e limites de mercado

Os princípios abaixo são **[NORMATIVO]** e vinculantes. Eles consolidam, no plano comercial, as garantias das Etapas 0/1/6/11/14. Nenhuma oferta, parceria, captação, cláusula de procurement, peça de marketing, meta de receita ou pressão de cliente pode violá-los; uma ação comercial que colida com qualquer um deles é **barrada** e, se já em curso, tratada como incidente sob a política da Etapa 14 (E14, §11).

1. **Comercial vende; não governa.** O comercial **leva ao mercado** o conteúdo publicável (E11/E12) e a operação madura (E14); jamais origina, edita ou deprecia fato por conta própria (invariantes 1/4–8/25; §1.3).
2. **Procurement não destrava portão.** Prazo de edital, urgência de contrato, autoridade do comprador ou interesse comercial **nunca** destravam um item `blocked-license`/`legal-review`/`rejected`/`pending` nem fazem passar um teste reprovado (princípio operacional 4; R-13.35; R-14.04/R-14.34).
3. **Piloto não coleta PII de aluno.** Todo piloto roda **sem PII real de aluno** ou, havendo escola real, **apenas sob a base legal da escola e com dados agregados** (princípios operacionais 7/8; R-14.37; invariante 21).
4. **Métrica comercial é agregada e sem PII.** Toda métrica de negócio é **derivada reconstruível**, **agregada** por turma/escola/escopo, **nunca** individualiza aluno e **nunca** é fonte factual (princípios operacionais 5/7/14; invariantes 12/21/26).
5. **Parceiro não escreve fato no KC.** Conteúdo, fonte ou dado de parceiro entra **exclusivamente pelo portão (E1/1.1) e pelo pipeline (E13)**, sob curadoria e revisão humana; nenhum parceiro tem porta de escrita no KC (princípio de ingestão 22; R-13.01; invariante 20).
6. **White-label não remove garantia.** Nenhuma customização de marca remove rótulo epistêmico, fonte, incerteza, citação, acessibilidade, mediação de tema sensível nem nota anti-homologação (invariantes 7/9/10/14/23; Seção 5.4).
7. **BNCC é alinhamento, não selo.** O alinhamento é exibido **como alinhamento** (`BNCCMapping`/`CurricularAlignment`); jamais como homologação MEC ou aprovação PNLD (invariante 7; E6; R-23; R-14.09).
8. **Validação é evidência, não promessa.** Toda validação (escolar/jurídica/comercial) produz **evidência datada e versionada** (`ValidationEvidence`/`doesNotImply`); nunca promete homologação, aprovação ou validação jurídica definitiva (E14, §10; R-14.09/R-14.10).
9. **Nenhuma venda oculta incerteza, fonte, licença ou publicabilidade.** A **honestidade epistêmica é diferencial visível** (E0, D7), não um defeito a esconder: demo, proposta e marketing exibem tipo de claim, confiança, natureza de mídia, fonte e licença (invariantes 9/10/14).
10. **Não se promete cobertura total do conhecimento.** A cobertura é **estrutural, não exaustiva** (E0, D5); a `CoverageMatrix` (E14, §13) **descreve**, não promete completude; vender "todo o conhecimento" é proibido (R-15.10).
11. **Não se vende como substituto de professor nem de currículo.** O produto é **recurso educacional digital complementar** (E0/E6); afirmar substituição de currículo, livro didático, LMS ou professor é proibido (E6, §13; R-15.11).
12. **Preço não compra destravamento.** Gratuidade, desconto, contrato ou patrocínio **nunca** relaxam QA, licença, privacidade, acessibilidade, publicabilidade ou revisão humana (princípio operacional 4; Seção 10; R-15.12).
13. **A prontidão é da operação; o comercial a lê.** O `readinessStatus` é definido pela operação (E14, §7) e **lido** pelo comercial como gate de oferta; o comercial **não** seta nem eleva prontidão (Seção 14; R-15.13).
14. **Conflito de interesse fica fora da curadoria.** Quem vende, capta ou negocia **não decide o mérito** de claim/cena/publicabilidade; há segregação de funções (E14, §3.1; R-14.31; R-15.14).
15. **Captação não compra exceção.** Investidor, board ou marco de tração **não** destravam portão; a *due diligence* é o registro de riscos (R-11/R-13/R-14/R-15) e o mapa de calor, não uma promessa de relaxar invariante (Seção 8; R-15.15).
16. **Demo usa publicável; nunca placeholder como real.** A demonstração usa conteúdo `published` e seed **marcado** (`seed-MVP`); jamais apresenta placeholder/seed como conteúdo real do mundo (R-13.18; E12; R-15.16).
17. **Distribuição comercial respeita licença e atribuição.** Toda exportação/pacote comercial/LMS embute citação, incerteza, mediação, atribuição e nota anti-homologação, e respeita a matriz de licença por `licenseRiskLevel` (expressão NC nunca exportada; SA/ODbL fora de pacote aberto) (E14, §9.2; invariantes 17–19/27).
18. **Marketing é responsável: afirmação tem base; proibição é absoluta.** Só se afirma o que há base para afirmar (E6); as proibições de marketing (Seção 11.2) são absolutas e não admitem "licença poética" comercial (R-15.18).
19. **Proteção de menor é piso, não recurso de venda.** A minimização máxima de dados de menor (LGPD/ECA; invariante 21) é fundação inegociável; jamais se vende "perfil do aluno", "engajamento individual" ou "analytics de estudante" (R-15.05/R-15.06).
20. **Pressão de mercado que colide com garantia é barrada, não excecionada.** Qualquer pressão (cliente, edital, investidor, parceiro, prazo) que tente violar QA, licença, privacidade, acessibilidade, publicabilidade ou revisão humana é **barrada** e, se em curso, tratada como **incidente** (E14, §11); ela **nunca** vira exceção (princípio operacional 4; R-15.20).

**Limites de mercado (síntese [NORMATIVO]).** O comercial **não** escreve código; **não** implementa CRM; **não** redige contrato jurídico definitivo; **não** simula edital real específico sem fonte oficial; **não** promete homologação MEC/PNLD nem validação jurídica definitiva; **não** cria claim/conteúdo novo; **não** altera o KC nem a Etapa 14; **não** destrava item bloqueado; **não** coleta PII de aluno; **não** cria analytics individualizado; **não** vende alinhamento como selo, currículo obrigatório ou substituto de professor; **não** oculta incerteza/fonte/licença/publicabilidade; e **não** permite white-label que remova rótulo epistêmico, fonte, licença, acessibilidade ou nota anti-homologação.

---

## 3. Proposta de valor e posicionamento

### 3.1 Posicionamento canônico

**[NORMATIVO]** o produto é posicionado **exatamente** como na Etapa 0 (D1) e na Etapa 6: **atlas espaçotemporal de conhecimento com camada de aplicação pedagógica — recurso educacional digital complementar, objeto de aprendizagem e ferramenta de apoio ao professor**. Nunca substituto de currículo, livro didático, professor ou LMS. As afirmações **permitidas** (com base — E6, §13) são: "recurso educacional digital complementar"; "alinhado à BNCC" (somente quando houver `BNCCMapping` revisado para o escopo ofertado); "compatível com a educação básica brasileira" (no sentido da Etapa 6); "acessível" (somente com laudo ASES — E14, §10.2). As afirmações **proibidas** (Seção 11.2) são: "homologado pelo MEC"; "aprovado pelo PNLD"; "substitui o professor/o currículo/o livro"; "dispensa avaliação pedagógica/jurídica"; "cobre todo o conhecimento"; "fonte definitiva".

### 3.2 Diferenciais de produto (o que sustenta a proposta)

A proposta de valor não se apoia em "mais conteúdo", e sim em **propriedades estruturais** que os concorrentes (pipelines Wikipedia/IA, enciclopédias, bancos de questões, LMS) tipicamente **não** oferecem:

1. **Honestidade epistêmica como feature visível (E0, D7).** Todo claim carrega tipo (fato documentado, medição, inferência, estimativa, hipótese, controvérsia, interpretação historiográfica) e nível de confiança; toda mídia carrega natureza (fotografia, mapa, gráfico, reconstrução científica, simulação, representação artística, aproximação didática). É o diferencial direto contra conteúdo gerado por IA sem proveniência.
2. **Simultaneidade global navegável — `WhatWasHappeningAtMoment` (E5).** Selecionar um momento e ver o que acontecia em outras regiões e camadas (político, científico, econômico, cultural, tecnológico, ambiental), com anti-falsa-equivalência e `gatingReason` honesto. É a pergunta central do produto e o que nenhuma timeline plana entrega.
3. **Atlas espaçotemporal 3D (E3/E10).** Timeline superior + globo/mapa 3D + navegação por ano/período/evento/região, com dossiês, fontes e incerteza na interface.
4. **Proveniência ponta a ponta (E2/E11).** Cada item rastreável até fonte e licença — auditável, reconstruível, versionado.
5. **Interdisciplinaridade real (E4A, 25 camadas).** Do tempo profundo ao contemporâneo, ciência e história na mesma base, atendendo a várias áreas do conhecimento.
6. **Conformidade educacional desenhada (E6).** Alinhamento BNCC como indexação, modulação por faixa etária (a forma muda, o fato não), cobertura das Leis 10.639/11.645, acessibilidade e LGPD como fundação.
7. **Viabilidade escolar concreta (E0/E10/E11).** Degradação progressiva, modo projetor, offline parcial, hardware modesto — pensado para a escola pública e privada real.

### 3.3 Contexto de mercado (insumo, não promessa)

**[RECOMENDADO]** como pano de fundo, e **estritamente como dado de baseline da Etapa 0** (não como claim novo desta etapa): o setor brasileiro de edtech foi mapeado em **467 edtechs ativas** (Liga Ventures, 2025), com o Brasil concentrando cerca de **47% das edtechs da América Latina** (Distrito, 2025) — um mercado grande, porém concentrado em capacitação profissional/corporativa, com **lacuna** justamente em conteúdo científico-histórico interdisciplinar com proveniência. **[PENDÊNCIA]:** dimensionamento de mercado (TAM/SAM/SOM), número de escolas/redes endereçáveis por segmento e tamanho de orçamento público/privado por canal ficam para a Etapa 16/execução, com pesquisa de fonte oficial atualizada — esta etapa **não** fabrica números de mercado.

### 3.4 Matriz de proposta de valor (`ValuePropositionMap`)

**[NORMATIVO]** a matriz liga cada segmento à dor, ao valor entregue, ao diferencial que o sustenta, à prova permitida e — coluna inegociável — ao **que NÃO se promete**.

| Segmento | Dor principal | Valor entregue | Diferencial que sustenta | Prova permitida | O que NÃO se promete |
|---|---|---|---|---|---|
| **Escola privada** | conteúdo digital diferenciado, interdisciplinar e confiável | atlas 3D + simultaneidade + honestidade epistêmica como vitrine pedagógica | D7, E5, E10 | demo com publicável; laudo ASES; alinhamento BNCC `pending` | homologação; substituição de currículo/professor |
| **Rede pública / secretaria** | recurso complementar acessível, com LGPD e viável em hardware modesto | base científico-histórica complementar, acessível, offline parcial, agregada por turma | E6, E11, acessibilidade | memorial de conformidade; evidência de piloto agregada | aprovação PNLD; obrigatoriedade curricular; analytics de aluno |
| **Museu / centro de ciência** | experiência expositiva temporal/espacial confiável | atlas 3D como camada de exposição digital com proveniência | E3, E10, E2 | demo; proveniência; licenças honradas | exclusividade de fato; reescrita de acervo no KC |
| **Editora** | enriquecer catálogo com camada digital interdisciplinar | conteúdo publicável licenciado e indexável; integração por export | E2, E11, `ExportPackage` | matriz de licenças; demo | homologação; reescrita de claim por demanda editorial |
| **Edtech / LMS** | conteúdo confiável para integrar via consumo | `LMSIntegrationContract`: consumo de publicável, identidade separada | E14 §9 | contrato de integração; demo | escrita no KC; PII de aluno no núcleo |
| **Fundação / financiador** | impacto educacional mensurável e íntegro | cobertura, qualidade e adoção **agregadas**; honestidade epistêmica auditável | E14 §8/§13 | métricas agregadas; mapa de cobertura | métricas individuais de aluno; promessa de homologação |
| **Universidade / instituição científica** | base curada para extensão/pesquisa/divulgação com proveniência | parceria de fonte/validação científica sob o pipeline | E1/1.1, E13 | proveniência; revisão por pares como fonte A/B | escrita direta no KC; autoria que burle curadoria |

> **[NORMATIVO]:** a coluna "O que NÃO se promete" é **vinculante** em toda proposta, demo e contrato; suprimi-la é violação da Seção 11.2 e risco R-15.18/R-15.09.

---

## 4. Segmentos, ICPs e personas institucionais

### 4.1 O enum de segmentos

```txt
segmentType = [
  private-school,          # escola privada (unidade ou grupo)
  public-network,          # rede pública municipal/estadual
  secretariat,             # secretaria de educação (municipal/estadual)
  museum,                  # museu / centro de ciência / planetário
  edtech,                  # edtech / plataforma / LMS que integra por consumo
  publisher,               # editora educacional
  foundation,              # fundação / instituto / financiador de impacto
  university,              # universidade (extensão/pesquisa/formação docente)
  scientific-institution   # instituição científica (fonte A/B sob o pipeline)
]
```

**[NORMATIVO]:** segmento é **classificação comercial**, não credencial de escrita: nenhum `segmentType` confere porta de escrita no KC. Instituição científica/universidade entra como **fonte** apenas pelo portão (E1/1.1) e pelo pipeline (E13), nunca por convênio comercial direto.

### 4.2 A entidade de segmento/ICP

```txt
MarketSegmentProfile = {
  segmentId, segmentType,
  buyer,                  # quem compra (instituição); quem assina
  economicBuyer,          # quem detém orçamento (diretoria/secretaria/conselho)
  decisionMaker,          # quem decide pedagogicamente (coordenação/curadoria/curadoria de acervo)
  influencer,             # professor, bibliotecário, curador, pesquisador
  primaryPain,            # dor central que o produto endereça
  buyingTrigger,          # gatilho de compra (início de ano, edital, projeto, exposição, mostra)
  legalBasisForData,      # base legal de qualquer dado (sempre da ESCOLA/instituição; produto não detém PII de aluno)
  salesCycleClass,        # curto | medio | longo (público tende a longo) — duração concreta é [PENDÊNCIA]
  commonObjection,        # objeção típica
  minReadinessToOffer,    # readinessStatus mínimo para ofertar a este segmento (Seção 14)
  forbiddenClaimRisk      # afirmação proibida mais provável neste segmento (Seção 11.2)
}

ICPProfile = {            # perfil de cliente ideal: o subconjunto de MarketSegmentProfile com maior fit
  icpId, segmentRef,
  fitCriteria,            # por que é ideal (dor aguda + diferencial decisivo + viabilidade técnica)
  disqualifiers,          # o que torna NÃO-ideal (ex.: exige homologação como condição; exige PII de aluno)
  entryMotion             # piloto | demo | export/integração | parceria de fonte (NUNCA escrita no KC)
}

InstitutionalPersona = {
  personaId, segmentRef, role,   # ex.: coordenadorPedagogico, secretarioAdjunto, curadorMuseu, gestorEdital
  goals, constraints,            # objetivos e restrições (orçamento, LGPD, acessibilidade, autonomia da rede)
  whatConvinces,                 # evidência que convence (demo, laudo, memorial, piloto agregado)
  whatBreaksTrust                # o que quebra a confiança (promessa falsa de homologação; PII de aluno; incerteza escondida)
}
```

### 4.3 Matriz de segmentos / ICP

**[NORMATIVO]** a matriz orienta priorização e discurso; a coluna `minReadinessToOffer` é **gate** (Seção 14) e a coluna "base legal de dados" é sempre **da instituição**, nunca do produto.

| Segmento | Comprador / decisor | Dor → gatilho | Base legal de dados | Ciclo | Objeção típica → resposta | `minReadinessToOffer` |
|---|---|---|---|---|---|---|
| **Escola privada** | mantenedora / coordenação pedagógica | diferenciação digital → início de ano/feira | da escola; produto sem PII de aluno | médio | "é homologado?" → "não; é recurso **complementar** alinhado à BNCC" | `ready-for-school` |
| **Rede pública** | secretaria / equipe pedagógica | recurso acessível e viável → projeto/programa | da rede; dados **agregados** | longo | "substitui o material?" → "complementa; não substitui currículo/livro" | `ready-for-school` |
| **Secretaria** | gestor de orçamento / técnico | adoção em escala com conformidade → edital | da secretaria; agregado | longo | "tem selo MEC/PNLD?" → "não; conformidade documentada, não homologação" | `ready-for-scale` |
| **Museu / centro de ciência** | direção / curadoria | exposição temporal confiável → nova mostra | da instituição; sem PII de visitante individual | médio | "podemos editar o acervo?" → "curadoria via pipeline; sem escrita direta no KC" | `ready-for-pilot` |
| **Editora** | direção editorial | catálogo digital interdisciplinar → ciclo editorial | contratual; sem PII de aluno | médio | "reescrevem sob demanda?" → "não; mérito é da curadoria; forma é negociável" | `ready-for-school` |
| **Edtech / LMS** | produto / parcerias | conteúdo confiável integrável → roadmap | identidade **separada**; PII fica no LMS | médio | "vocês recebem nossos dados de aluno?" → "não; consumo de publicável, sem PII no KC" | `ready-for-school` |
| **Fundação / financiador** | programa / investimento de impacto | impacto íntegro e mensurável → ciclo de grant | agregado; sem PII de menor | longo | "medem o aluno?" → "métrica **agregada**; nunca individual" | `ready-for-pilot` |
| **Universidade** | extensão / pesquisa / formação | base curada para divulgação/formação → projeto | acadêmica; sem PII de menor | longo | "podemos publicar direto?" → "como **fonte** pelo portão/pipeline, sob revisão" | `ready-for-pilot` |
| **Instituição científica** | direção científica | colaboração de fonte com proveniência → convênio | acadêmica/institucional | longo | "entramos como autores no sistema?" → "como **fonte A/B**; curadoria preserva proveniência" | `ready-for-pilot` |

### 4.4 Disqualificadores universais

**[NORMATIVO]** independem do segmento e **desqualificam** a venda (ou exigem reenquadramento honesto): cliente que **condiciona a compra a um selo de homologação MEC/PNLD** (não há selo — só conformidade documentada); cliente que **exige PII individual de aluno** no produto (proibido — invariante 21); cliente que **exige esconder incerteza/fonte/licença** para "ficar mais vendável" (viola D7/invariantes 9/10/14); cliente que **exige escrita direta no KC** por parceiro/editora/universidade (viola invariante 20); cliente que **exige white-label sem rótulos epistêmicos/nota anti-homologação** (viola Seção 5.4). Nesses casos, a resposta correta é **reenquadrar o que o produto é** ou **declinar**, nunca ceder a garantia (R-15.09/R-15.11/R-15.06/R-15.05).

---

## 5. Modelos de implantação e pacotes comerciais

### 5.1 O enum de níveis de implantação

```txt
deploymentTier = [
  pilot,                  # piloto controlado, escopo mínimo, SEM PII real de aluno (Seção 6)
  single-school,          # escola individual
  network,                # rede/secretaria (múltiplas escolas)
  museum,                 # uso expositivo institucional
  institutional-use,      # fundação/universidade/instituição (extensão, formação, divulgação)
  controlled-white-label  # marca do parceiro SOB restrições inegociáveis (Seção 5.4)
]
```

### 5.2 A entidade de pacote

```txt
DeploymentPackage = {
  packageId, deploymentTier,
  scopeCovered,           # quais camadas/regiões/períodos do publicável (E11/E12) o pacote entrega
  requiredReadiness,      # readinessStatus exigido para ofertar este pacote (Seção 14) — GATE
  includes,               # acesso ao viewer, export controlado, integração LMS, modo professor/projetor, offline parcial
  excludes,               # SEMPRE exclui: escrita no KC, PII de aluno, selo de homologação, remoção de rótulo epistêmico
  dataResponsibility,     # PII (se houver) é da instituição; produto agregado/SEM-PII (E14, §8/§9)
  licenseExportProfile,   # respeita matriz de licença por licenseRiskLevel; NC nunca; SA/ODbL fora de pacote aberto (E14, §9.2)
  accessibilityBaseline,  # laudo ASES como condição de ready-for-school+ (E14, §10.2)
  antiHomologationNote    # presente no viewer e no export (invariante 7) — inegociável
}
```

### 5.3 Matriz de modelos comerciais

**[NORMATIVO]** a coluna "exclui (sempre)" é inegociável em todos os pacotes; a coluna `requiredReadiness` é **gate** (Seção 14).

| Pacote (`deploymentTier`) | Escopo / inclui | `requiredReadiness` | Base de dados | Licença/export | Exclui (sempre) |
|---|---|---|---|---|---|
| **`pilot`** | escopo mínimo (cenas-gabarito + P0/P1 parcial); viewer + modo professor | `ready-for-pilot` | sem PII real; ou agregado da escola | export interno auditável | escrita no KC; PII de aluno; selo; cobrança plena |
| **`single-school`** | espinha P1 ofertada; viewer, modo projetor, offline parcial, export | `ready-for-school` | da escola; agregado | matriz de licença honrada | escrita no KC; PII de aluno; selo; remoção de rótulo |
| **`network`** | múltiplas escolas; gestão agregada por turma/escola; integração LMS | `ready-for-school` | da rede; **agregado** | export + LMS controlado | escrita no KC; PII de aluno; analytics individual; selo |
| **`museum`** | camadas/regiões expositivas; modo exploração; proveniência visível | `ready-for-pilot` | sem PII de visitante individual | licenças de mídia honradas | edição do acervo no KC; reescrita de claim |
| **`institutional-use`** | escopo para extensão/formação/divulgação; export | `ready-for-pilot` | acadêmica; sem PII de menor | atribuição/SA honrados | escrita no KC; autoria que burle curadoria |
| **`controlled-white-label`** | marca do parceiro na **apresentação**; conteúdo e garantias do KC | `ready-for-scale` | do parceiro/instituição; sem PII de aluno no KC | matriz de licença honrada | remoção de rótulo epistêmico/fonte/licença/acessibilidade/nota anti-homologação; escrita no KC |

### 5.4 White-label controlado: o que pode e o que **nunca** pode

**[NORMATIVO]** o white-label customiza **apresentação** (marca, cores, nome de produto, agrupamento de conteúdo, idioma de interface), **dentro** dos limites da camada de apresentação (E10) e da arquitetura técnica (E11). Ele **nunca** pode: **(a)** remover ou ocultar rótulo epistêmico (tipo de claim, confiança, natureza de mídia); **(b)** remover fonte, citação ou atribuição (invariantes 10/14; matriz de licença E14, §9.2); **(c)** remover a nota anti-homologação (invariante 7; R-23); **(d)** remover recursos de acessibilidade ou o laudo correspondente (invariante 23); **(e)** remover mediação de tema sensível (E3.1; princípio operacional 19); **(f)** obter porta de escrita no KC (invariante 20); **(g)** apresentar alinhamento BNCC como selo do parceiro; **(h)** exportar expressão NC ou SA/ODbL fora do permitido (invariantes 18/19/27). **[NORMATIVO]:** um white-label que viole qualquer um de (a)–(h) é **bloqueado**; tentativa de removê-los em produção é **incidente** (E14, §11; R-15.06).

### 5.5 O que os pacotes **não** fazem

**[NORMATIVO]** nenhum pacote: vende escrita no KC; vende PII de aluno ou "perfil do estudante"; vende selo de homologação; remove garantia epistêmica/licença/acessibilidade/nota anti-homologação; nem dispensa a prontidão exigida (`requiredReadiness`). O pacote **embala acesso e forma**; jamais **vende o fato como mercadoria editável** nem **o aluno como dado**.

---

## 6. Pilotos escolares e validação de mercado

### 6.1 O que o piloto é (e o que jamais coleta)

O **`PilotProgram`** é a execução controlada que **gera evidência de mercado** (usabilidade, fit pedagógico, reconhecimento do diferencial, adequação por faixa) e **alimenta** o `readinessStatus` (E14, §7) e a `ValidationEvidence` (E14, §10). **[NORMATIVO]:** o piloto roda **sem PII real de aluno** (E12, §11.2) ou, havendo escola real, **apenas sob a base legal da escola e com dados agregados** (E14, §10.2; R-14.37); ele **não** constrói perfil de aluno, **não** coleta telemetria individual e **não** destrava portão por "necessidade do piloto" (princípios operacionais 4/7/8; princípio comercial 3).

```txt
PilotProgram = {
  pilotId, scope,                 # escopo/lote/versão objeto do piloto (cenas-gabarito + P0/P1 conforme readiness)
  participantClass,               # professores/turmas/curadores; NUNCA aluno identificável individualmente
  dataPosture,                    # SEM-PII real OU agregado-sob-base-legal-da-escola (nunca PII de menor no produto)
  successCriteria,                # usabilidade, fit, reconhecimento do diferencial SEM confundir com currículo (E12, §15.6)
  accessibilityCheck,             # laudo ASES como condição de leitura escolar (E14, §10.2)
  bnccDisplay,                    # alinhamento exibido como ALINHAMENTO pending (E6); nunca como aprovação
  evidenceProduced,               # vira ValidationEvidence (E14, §10) — datada, versionada, doesNotImply
  feedsReadiness,                 # alimenta ready-for-school (E14, §7.2); NÃO seta prontidão por si
  gateRespect                     # piloto respeita TODOS os portões; não publica item bloqueado (princípio 4)
}
```

### 6.2 Como rodar piloto sem violar privacidade

**[NORMATIVO]** três posturas de dados, em ordem de preferência: **(1)** piloto **sem PII real** — turmas de demonstração, dados sintéticos/seed marcado (`seed-MVP`), feedback qualitativo de professores sem identificar aluno; **(2)** piloto com escola real sob a **base legal da escola**, com **dados agregados por turma** (LGPD/ECA — E14, §8), sem que qualquer PII de aluno flua ao produto; **(3)** nunca uma postura que colete PII individual de menor no produto (proibida — invariante 21; R-14.37). A identidade × sessão × pedagógico permanece **separada** (E11, §8): se houver LMS no piloto, a PII fica no LMS/escola (E14, §9.3).

### 6.3 Critérios de sucesso de mercado (sem confundir com mérito factual)

**[NORMATIVO]** o sucesso do piloto mede **adoção, usabilidade e fit** — **agregados** —, nunca o desempenho individual do aluno e nunca a "veracidade" do conteúdo (a verdade é da curadoria, não do piloto). Sinais permitidos: professores reconhecem o diferencial sem confundir com currículo oficial; a faixa etária encontra a linguagem adequada (a forma muda, o fato não — E6); a acessibilidade funciona (laudo ASES); a navegação temporal/espacial e a função `WhatWasHappeningAtMoment` são compreendidas. **[NORMATIVO]:** evidência de piloto é **insumo** de `ready-for-school` (E14, §7.2), **não** um selo, e **não** autoriza vender homologação (R-14.09).

### 6.4 O que o piloto **não** faz

**[NORMATIVO]** o piloto **não**: coleta PII real de aluno sem base legal; constrói perfil/boletim de estudante; destrava item bloqueado por urgência do piloto; transforma feedback comercial em correção de claim sem passar pelo pipeline/revisão (E13); nem é apresentado como "validação MEC". Ele **define e produz evidência de mercado**; a verdade factual segue intocada no KC.

---

## 7. Parcerias estratégicas

### 7.1 Princípio de parceria: parceiro não escreve fato

**[NORMATIVO]** toda parceria é desenhada sob a regra inegociável de que **parceiro não escreve fato no KC** (princípio comercial 5; invariante 20). Conteúdo, fonte, dado ou correção vindos de qualquer parceiro entram **exclusivamente** pelo portão de licenças (E1/1.1) e pelo pipeline (E13), sob curadoria e revisão humana de mérito; nenhum convênio, contrato ou patrocínio cria uma porta de escrita paralela. A direção única de dependência (E11, §2) **não se inverte por parceria**.

```txt
partnershipType = [
  content,                 # parceiro fornece CONTEÚDO (entra como fonte pelo portão/pipeline; nunca escreve direto)
  pedagogical-validation,  # parceiro VALIDA pedagogicamente (gera ValidationEvidence; não homologa)
  scientific-source,       # parceiro é FONTE científica A/B (sob E1/1.1; proveniência preservada)
  distribution,            # parceiro DISTRIBUI (consumo de publicável; respeita licença/atribuição/nota anti-homologação)
  technology,              # parceiro de TECNOLOGIA/integração (LMS/infra; identidade separada; sem escrita factual)
  financing,               # parceiro FINANCIA (grant/investimento; não compra exceção a portão)
  institutional            # parceiro INSTITUCIONAL (museu/universidade/secretaria; cooperação sem escrita no KC)
]

PartnershipModel = {
  partnershipId, partnershipType, partner,
  partnerDoes,             # o que o parceiro FAZ
  partnerNeverDoes,        # o que o parceiro NUNCA faz (escrever fato; impor selo; exigir PII de aluno; remover rótulo)
  entryPath,               # COMO entra: portão (E1/1.1) + pipeline (E13) para conteúdo/fonte; consumo (E14, §9) para distribuição
  provenanceLicense,       # proveniência e licença preservadas; uso comercial só sob código COMER (E1.1)
  reviewOwnership,         # mérito é SEMPRE da curadoria/revisão humana, nunca do parceiro
  conflictOfInterest,      # segregação: parceiro não decide publicabilidade/mérito (E14, §3.1; R-14.31)
  exitAndVersioning        # término não apaga proveniência; conteúdo curado permanece versionado (invariante 16/29)
}
```

### 7.2 Matriz de parceria

**[NORMATIVO]** as colunas "nunca faz" e "como entra no fluxo" são inegociáveis.

| Tipo (`partnershipType`) | O parceiro faz | O parceiro **nunca** faz | Como entra no fluxo | Proveniência / licença |
|---|---|---|---|---|
| **`content`** | oferece conteúdo/acervo | escreve direto no KC; impõe versão; exige esconder fonte | portão (E1/1.1) → pipeline (E13) → revisão humana | fonte registrada; licença/uso comercial sob `COMER` |
| **`pedagogical-validation`** | testa fit pedagógico; emite parecer | declara "homologado"; destrava portão | gera `ValidationEvidence` (E14, §10); `doesNotImply` | parecer datado/versionado; não selo |
| **`scientific-source`** | fornece dado/estudo revisado | vira "autor" com escrita no KC; burla curadoria | entra como **fonte A/B** pelo portão (E1/1.1) | proveniência preservada; revisão por pares como nível A/B |
| **`distribution`** | distribui/integra para alcance | exporta NC/SA fora do permitido; remove nota anti-homologação | consumo de publicável (E14, §9); `ExportPackage` | atribuição/SA honrados; nota anti-homologação embutida |
| **`technology`** | integra LMS/infra | recebe PII de aluno no KC; escreve fato | `LMSIntegrationContract` (E14, §9); identidade separada | sem PII no KC; sessão respeita papel/faixa |
| **`financing`** | financia (grant/equity) | compra exceção a portão; impõe relaxar garantia | tese/marcos (Seção 8); *due diligence* = riscos | governança; segregação comercial × mérito |
| **`institutional`** | coopera (mostra/extensão/programa) | exige escrita no KC; impõe selo | convênio de **uso/cooperação**; conteúdo via pipeline | cooperação sem porta de escrita; proveniência intacta |

### 7.3 Conflito de interesse e governança da parceria

**[NORMATIVO]** quem negocia/recebe a parceria **não decide o mérito** do conteúdo (segregação de funções — E14, §3.1; R-14.31). Um parceiro de financiamento ou de conteúdo **não** pode, por força de contrato, fazer publicar item bloqueado, suprimir incerteza, alterar `claimType`/`confidenceLevel` ou impor um `ClaimSet` enviesado. Qualquer cláusula contratual que tente isso é **inválida perante os invariantes** e a tentativa de execução é **incidente** (E14, §11; R-15.14).

### 7.4 O que a parceria **não** faz

**[NORMATIVO]** a parceria **não**: abre porta de escrita no KC; converte parceiro em fonte de verdade fora do pipeline; permite selo de homologação; permite remover rótulo/fonte/licença/nota anti-homologação; nem permite PII de aluno no núcleo. Ela **amplia alcance, conteúdo curado, validação e distribuição** — sempre sob os mesmos portões.

---

## 8. Captação e tese de investimento

### 8.1 Tese de investimento (sem comprar exceção)

O **`InvestmentThesis`** estrutura por que o produto merece capital — **sem** que captação compre exceção a portão (princípio comercial 15). **[NORMATIVO]:** a *due diligence* do produto é o **registro de riscos** (`R-11/R-13/R-14/R-15`) e o **mapa de calor** (E14, §13.3), apresentados com honestidade; um investidor ou board **não** destrava item bloqueado, não impõe relaxar invariante e não exige PII de aluno como "ativo de dados".

```txt
InvestmentThesis = {
  thesisId,
  problem,                # lacuna: conteúdo científico-histórico interdisciplinar com proveniência (E0)
  solution,              # atlas espaçotemporal 3D + simultaneidade + honestidade epistêmica (Seção 3)
  whyNow,                # maturidade técnica (E11/E12), pipeline (E13) e operação (E14) prontos
  moat,                  # proveniência ponta a ponta + curadoria + simultaneidade + conformidade (difícil de copiar com IA crua)
  businessModel,         # licença institucional/rede/museu/white-label; grant; integração (Seção 10)
  tractionMilestones,    # FundingMilestone ligados a readinessStatus e adoção AGREGADA (Seção 8.2)
  useOfFunds,            # curadoria, fonte, acessibilidade, infra, validação — NÃO "comprar destravamento"
  governance,            # segregação comercial × mérito; invariantes inegociáveis; QA bloqueia (E14, §3/§5)
  dueDiligence,          # registro de riscos R-NN + mapa de calor; conformidade documentada (não selo)
  whatWeNeverPromise     # homologação MEC/PNLD; validação jurídica definitiva; PII de aluno como ativo; cobertura total
}
```

### 8.2 Marcos de tração (ligados à prontidão, não a vaidade)

**[NORMATIVO]** marcos de tração usam **métricas agregadas permitidas** (Seção 12) e a **prontidão objetiva** (E14, §7), nunca métricas de vaidade que escondam o piso epistêmico. Números concretos são **[PENDÊNCIA]** (Etapa 16/execução).

| Marco (`FundingMilestone`) | Sinal objetivo | Métrica permitida | Não é |
|---|---|---|---|
| **Prontidão de piloto** | escopo em `ready-for-pilot` (E14, §7.2) | cobertura P0; QA verde | "validado pelo MEC" |
| **Prontidão escolar** | escopo em `ready-for-school`; laudo ASES; DPIA revisada | adoção agregada por escola; piloto positivo | aprovação PNLD |
| **Prontidão de escala** | escopo em `ready-for-scale`; throughput sustentado sem queda de revisão | adoção agregada por rede; retenção institucional | "selo" |
| **Eficiência de curadoria** | lote P1/P2 sob piso, sem baixar revisão (anti-Goodhart — E14, §7.3) | itens publicáveis por ciclo; qualidade de revisão | "mais conteúdo a qualquer custo" |
| **Conformidade comprovada** | memoriais de privacidade/acessibilidade/licença atualizados | incidentes de privacidade/licença = 0 ou tratados/versionados | "validação jurídica definitiva" |

### 8.3 Uso de recursos e governança de captação

**[NORMATIVO]** o uso de recursos prioriza o que **sustenta o piso**: curadoria e revisão humana, aquisição de fontes A/B (sob portão), acessibilidade (ASES/LBI), infraestrutura sob os orçamentos da E11, e validação por evidência. **[NORMATIVO]:** nenhum recurso é alocado para "comprar destravamento", "acelerar publicação pulando revisão" ou "coletar dados de aluno"; a governança mantém **segregação** entre quem capta/vende e quem decide mérito (E14, §3.1; R-14.31), e os invariantes permanecem inegociáveis perante investidor/board (R-15.15).

### 8.4 O que a captação **não** faz

**[NORMATIVO]** a captação **não**: promete homologação/validação definitiva a investidores; oferece PII de aluno como ativo de dados; aceita cláusula que relaxe QA/licença/privacidade/revisão; nem transforma marco de tração em pressão para destravar portão. Ela **financia o crescimento sob as garantias**, não contra elas.

---

## 9. Procurement público e privado

### 9.1 Princípio de procurement: não destrava portão

**[NORMATIVO]** procurement (compra pública e adoção privada por rede/escola/instituição) é preparado **sem furar portão** (princípio comercial 2; R-14.34). Prazo de edital, urgência de contrato ou interesse comercial **nunca** publicam item bloqueado, dispensam revisão ou removem garantia. Toda referência a PNLD/MEC é **explicitamente** "não homologado" (invariante 7; R-23). **[NORMATIVO/LIMITE]:** esta etapa **define o modelo de dossiê** e os tipos de requisito; ela **não simula um edital real específico sem fonte oficial** — a leitura e o atendimento de um edital concreto pertencem à Etapa 16/execução, com base no texto oficial vigente.

```txt
procurementChannel = [
  public-bid,            # licitação/edital público
  direct-public,         # contratação pública direta/dispensa (quando cabível, sob norma)
  private-adoption,      # adoção privada por escola/grupo/instituição
  foundation-grant       # aquisição/financiamento via fundação/edital de fomento
]

ProcurementDossier = {
  dossierId, channel,
  productStatement,      # recurso educacional digital COMPLEMENTAR (E0/E6); nunca currículo obrigatório/substituto
  complianceMatrix,      # acessibilidade (e-MAG/WCAG/LBI), LGPD (DPIA/RIPD), segurança, licença/IP, anti-homologação
  evidenceRefs,          # ValidationEvidence (E14, §10); laudos/memoriais; piloto agregado
  antiHomologationNote,  # texto fixo: não homologado pelo MEC, não aprovado no PNLD (invariante 7)
  dataPosture,           # produto SEM PII de aluno; dados agregados; identidade separada (E14, §8/§9)
  gateStatement,         # declaração de que NENHUM portão é dispensado por prazo/edital (princípio 2; R-14.34)
  sourceOfRequirements   # SEMPRE o texto OFICIAL do edital/norma; nunca suposição (limite desta etapa)
}

ProcurementRequirement = {
  requirementId, dossierRef, category,  # acessibilidade | privacidade | seguranca | licenca | pedagogico | tecnico
  howMet,                # como o produto atende (com evidência/memorial)
  gatingImpact,          # se "não atendido" => NÃO se promete atendimento; corrige-se sob os portões, não se finge
  forbiddenShortcut      # atalho proibido associado (ex.: "declarar homologação"; "dispensar revisão por prazo")
}
```

### 9.2 Matriz de procurement

**[NORMATIVO]** a coluna "portão que **não** se fura" é inegociável; a coluna "nota anti-homologação" é obrigatória em todo dossiê.

| Canal (`procurementChannel`) | Requisito típico | Evidência permitida | Portão que **não** se fura | Nota anti-homologação |
|---|---|---|---|---|
| **`public-bid`** | acessibilidade, LGPD, licença, técnica | memoriais; laudo ASES; DPIA; `ValidationEvidence` | revisão humana; licença; publicabilidade; PII | obrigatória no dossiê e no produto |
| **`direct-public`** | conformidade documentada; viabilidade | memoriais; evidência de piloto agregado | revisão; licença; privacidade | obrigatória |
| **`private-adoption`** | fit pedagógico; segurança; LGPD | demo; piloto agregado; matriz de licença | revisão; privacidade; rótulo epistêmico | obrigatória |
| **`foundation-grant`** | impacto íntegro; conformidade; transparência | métricas agregadas; mapa de cobertura; riscos | revisão; PII; "métrica individual" | obrigatória |

### 9.3 Conformidade exigível e a nota anti-homologação

**[NORMATIVO]** o dossiê apresenta conformidade **documentada**, não selos: **acessibilidade** (laudo ASES; e-MAG/WCAG/LBI — invariante 23); **privacidade** (DPIA/RIPD sob LGPD/ECA; produto sem PII de aluno; minimização — invariante 21; E14, §10.3); **segurança** (RBAC+ABAC, isolamento físico, trilha de auditoria — E11); **licença/IP** (matriz por `licenseRiskLevel`; NC fora de expressão; SA/ODbL isolado — invariantes 17–19/27); e **pedagógico** (alinhamento BNCC `pending` como **alinhamento** — E6). **[NORMATIVO]:** a **nota anti-homologação** acompanha o dossiê e o produto entregue (invariante 7; R-23); afirmar "homologado pelo MEC" ou "aprovado no PNLD" em proposta/edital é violação grave (R-15.09).

### 9.4 O que o procurement **não** faz

**[NORMATIVO]** o procurement **não**: declara homologação/aprovação que não existe; aceita prazo de edital como justificativa para pular revisão/portão (R-14.34); promete PII de aluno ou analytics individual; nem simula atendimento a requisito não atendido — corrige-se sob os portões e **declara honestamente** o estado. Ele **prepara o produto para ser comprado sob conformidade real**, não sob promessa.

---

## 10. Precificação conceitual e modelo de receita

### 10.1 Princípios de precificação (conceito, não número)

**[NORMATIVO]** a precificação é **conceitual** nesta etapa: define eixos e modelos; **números concretos** (tickets, mensalidades, valores por escola/aluno-agregado/rede, descontos, metas de receita) são **[PENDÊNCIA]** (Etapa 16/execução, com pesquisa de mercado de fonte oficial). **[NORMATIVO]:** **preço não compra destravamento** (princípio comercial 12) — nenhum desconto, gratuidade, patrocínio ou contrato relaxa QA, licença, privacidade, acessibilidade, publicabilidade ou revisão; e nenhuma modalidade de preço se baseia em **PII de aluno** (sem "preço por perfil de estudante" — invariante 21).

```txt
pricingModelType = [
  per-school-license,      # licença por escola/unidade
  per-network-tier,        # faixa por rede/secretaria (por nº de escolas/turmas — AGREGADO, nunca por aluno identificado)
  institutional-license,   # licença institucional (museu/universidade/fundação)
  integration-license,     # licença de integração/consumo por LMS/edtech (E14, §9)
  grant-funded,            # financiado por fomento/fundação (acesso gratuito/subsidiado a redes)
  white-label-license      # licença de white-label CONTROLADO (Seção 5.4)
]

PricingModel = {
  modelId, pricingModelType,
  valueBasis,            # base de valor: escopo/acesso/integração/alcance — NUNCA PII de aluno
  publicVsPrivate,       # público (orçamento/edital, ciclos longos) vs privado (assinatura/projeto)
  freemiumOrPilot,       # piloto/camada gratuita NÃO relaxa garantia; é amostra do publicável (E12)
  accessibilityFloor,    # acessibilidade nunca é "recurso premium": é piso (invariante 23)
  numbers                # [PENDÊNCIA]: valores concretos — Etapa 16/execução
}
```

### 10.2 Eixos de receita

**[RECOMENDADO]** receita por **licença** (escola/rede/instituição), por **integração/consumo** (LMS/edtech — E14, §9), por **white-label controlado** (Seção 5.4) e por **fomento** (grant que subsidia acesso de redes públicas). **[NORMATIVO]:** **público** tende a ciclo longo e orçamento/edital (Seção 9); **privado** tende a assinatura/projeto; ambos sob a regra de que **conformidade e garantia não são "plano premium"** — acessibilidade, proveniência, incerteza e nota anti-homologação existem em **todos** os planos (invariantes 7/9/10/23).

### 10.3 O que a precificação **não** faz

**[NORMATIVO]** a precificação **não**: congela números (são `[PENDÊNCIA]`); cria modalidade baseada em PII de aluno; transforma desconto/gratuidade em destravamento de portão; nem coloca acessibilidade/garantia epistêmica atrás de paywall. Ela **define como o valor é capturado**, sem nunca capturar o aluno como dado nem vender a dispensa de uma garantia.

---

## 11. Materiais comerciais, demonstrações e discurso de venda

### 11.1 Materiais comerciais permitidos

**[NORMATIVO]** os materiais comerciais são **derivados** (`originClass = derivado`), reconstruíveis e honestos; nenhum deles é fonte factual nem caminho de escrita no KC (princípios operacionais 5/14).

```txt
CommercialCollateral = {
  collateralId, kind,    # demo | pitch-deck | one-pager | technical-proposal | compliance-matrix
                         #        | privacy-memo | accessibility-memo | license-memo
  usesPublishedOnly,     # demo/peças usam conteúdo published + seed MARCADO (seed-MVP); nunca placeholder como real (R-13.18)
  showsEpistemics,       # exibe tipo de claim/confiança/natureza de mídia/fonte/licença (D7; invariantes 9/10/14)
  showsAntiHomologation, # nota anti-homologação presente (invariante 7)
  claimsArePermitted,    # toda afirmação está na lista permitida (Seção 11.2); proibidas são bloqueadas
  noPII,                 # nenhum material expõe PII de aluno (invariante 21)
  versioned              # peças datadas/versionadas; números são [PENDÊNCIA] (Seção 10)
}
```

Materiais previstos: **demo** (conteúdo publicável + seed marcado), **pitch deck** (tese — Seção 8), **one-pager**, **proposta técnica**, **matriz de conformidade** (Seção 9), **memorial de privacidade** (DPIA — E14, §10.3), **memorial de acessibilidade** (ASES — E14, §10.2) e **memorial de licenças** (matriz por `licenseRiskLevel` — E14, §9.2).

### 11.2 Marketing responsável: afirmações permitidas × proibidas

**[NORMATIVO]** a tabela é vinculante em **todo** material, demo, proposta, pitch e contrato.

| Permitido (com base) | Proibido (absoluto) |
|---|---|
| "recurso educacional digital **complementar**" (E0/E6) | "homologado pelo MEC" |
| "**alinhado à BNCC**" — só com `BNCCMapping` revisado para o escopo | "aprovado pelo PNLD" / "selo MEC/PNLD" |
| "compatível com a educação básica brasileira" (sentido da E6) | "substitui o professor / o currículo / o livro" |
| "**acessível**" — só com laudo ASES (E14, §10.2) | "dispensa avaliação pedagógica/jurídica" |
| "conteúdo com **proveniência e incerteza visíveis**" (D7) | "cobre **todo** o conhecimento" / "completo" |
| "função **'O que acontecia no mundo neste momento?'**" (E5) | "fonte **definitiva**" / "verdade final" |
| "uso **agregado** por turma/escola" (E14, §8) | "analytics do aluno" / "perfil/engajamento individual do estudante" |
| "**validação por evidência**" datada/versionada (E14, §10) | "validação jurídica **definitiva**" / "garantia legal" |

### 11.3 Demonstração honesta

**[NORMATIVO]** a demo usa **conteúdo publicável** (`published`) e **seed marcado** (`seed-MVP`); ela **nunca** apresenta placeholder/seed como conteúdo real do mundo (R-13.18; princípio comercial 16), **nunca** esconde `gatingReason`/`hiddenItems`/incerteza para "impressionar" e **nunca** exibe expressão NC ou item `pending`/`legal-review`/`teacherOnly` fora do permitido (invariante 9; E14, §9.2). A força da demo é justamente a **honestidade epistêmica** e a **simultaneidade** — mostrar como o produto **mostra a incerteza e a fonte**, não escondê-las.

### 11.4 O que os materiais **não** fazem

**[NORMATIVO]** os materiais **não**: afirmam homologação/aprovação/validação definitiva; expõem PII de aluno; apresentam seed/placeholder como real; escondem incerteza/fonte/licença; nem prometem cobertura total. Eles **comunicam o que o produto é**, sob a lista permitida, com proveniência visível.

---

## 12. Métricas comerciais permitidas e analytics agregado

### 12.1 O que a métrica comercial é (e jamais é)

A **`commercialMetricsPolicy`** define a observação **agregada** do negócio — adoção, retenção institucional, cobertura, qualidade, incidentes, SLA. **[NORMATIVO]:** toda `CommercialMetric` **herda** a `OperationalMetric` (E14, §8): é **derivada reconstruível** (`originClass = derivado`), **agregada** (`aggregationLevel ∈ {processo, conteudo, escopo, turma-agregada}` — **nunca aluno individual**), com `dataMinimizationClass ∈ {SEM-PII, PSEUDONIMIZADO, AGREGADO}`, e **nunca** é fonte factual nem caminho de escrita no KC (princípios operacionais 5/7/14; invariantes 12/21/26; R-14.05/R-14.06/R-14.27).

```txt
CommercialMetric = {
  metricId,
  metricFamily,          # adocao | retencao | cobertura | qualidade | incidente | sla | receita-agregada
  aggregationLevel,      # processo | conteudo | escopo | turma-agregada (NUNCA aluno individual)
  dataMinimizationClass, # SEM-PII | PSEUDONIMIZADO | AGREGADO
  originClass,           # SEMPRE derivado (reconstruível; não autoritativo; não fonte)
  carriesProvenance,     # false (métrica de negócio não é claim)
  computedFromVersions   # versões de conteúdo/processo/uso agregado que a originaram (auditável)
}
```

### 12.2 Matriz de métricas permitidas e proibidas

**[NORMATIVO]** a coluna "proibido" é absoluta.

| Permitido (agregado) | Família | O que mede | Proibido (absoluto) |
|---|---|---|---|
| Adoção por escola/rede | adocao | nº de escolas/turmas ativas (agregado) | nº/identidade de alunos individuais |
| Retenção institucional | retencao | renovação/permanência por instituição | retenção/churn por aluno |
| Uso agregado por turma | adocao | sessões/uso por turma (agregado) | trilha de cliques pessoal do aluno |
| Cobertura ofertável | cobertura | camadas/regiões/períodos publicáveis (E14, §13) | "cobertura total" como promessa |
| Qualidade/conformidade | qualidade | incidentes de licença/privacidade; qualidade de revisão (E14, §6) | desempenho/nota individual do estudante |
| Incidentes/SLA | incidente/sla | MTTR; SLA de suporte/operação (E14, §11) | exposição de PII em log para "medir engajamento" |
| Receita agregada | receita-agregada | receita por segmento/canal (agregado) | receita atribuída a perfil de aluno |
| Pipeline comercial | adocao | funil de oportunidades por segmento (CRM externo, sem PII de menor) | dados de menor no CRM |

### 12.3 O que o analytics comercial **não** mede

**[NORMATIVO]** o analytics comercial **não** mede: aluno identificável; desempenho/nota individual; trilha pessoal; nem qualquer coisa que exija PII de menor. Ele **não** treina modelo com dado de aluno (E11, §8), **não** vira evidência factual e **não** constrói boletim/perfil de estudante (isso é do LMS/escola — E14, §9). Qualquer métrica que toque uso escolar é **AGREGADA por turma/escola** sob a base legal da instituição (R-28; R-14.05/R-14.06).

---

## 13. Riscos comerciais, jurídicos, pedagógicos e reputacionais

Trinta e seis riscos específicos do comercial, cada um com mitigação ancorada nas seções acima e com indicador associado (Seção 12 / E14, §8). Os riscos **não** substituem os da Etapa 11 (`R-NN`), do MVP (`R-MVP-NN`), da ingestão (`R-13.NN`) nem da operação (`R-14.NN`); o prefixo `R-15.` os mantém distintos.

| ID | Risco | Impacto | Mitigação |
|---|---|---|---|
| **R-15.01** | Comercial tentando "corrigir/incluir" fato para fechar venda | escrita factual fora do pipeline | comercial vende, não governa; sem porta de escrita (§1.3/§2; invariante 20) |
| **R-15.02** | Procurement furando portão por prazo de edital | publicação ilegítima sob pressão | procurement não destrava; portões mantidos (§9; princípio 2; R-14.34) |
| **R-15.03** | Piloto coletando PII real de aluno | violação LGPD/ECA | piloto sem PII real ou agregado sob base legal da escola (§6.2; R-14.37) |
| **R-15.04** | Parceiro escrevendo fato no KC por contrato | fronteira de escrita violada | parceiro entra só pelo portão/pipeline; cláusula inválida (§7; invariante 20; R-13.01) |
| **R-15.05** | Venda de "perfil/engajamento do aluno" como produto | PII de menor monetizada | proteção de menor é piso; métrica só agregada (§2/§12; invariante 21) |
| **R-15.06** | White-label removendo rótulo/fonte/licença/nota anti-homologação | garantia epistêmica destruída | white-label não remove garantia; violação = bloqueio/incidente (§5.4) |
| **R-15.07** | Alinhamento BNCC vendido como selo MEC/PNLD | promessa falsa de homologação | BNCC é alinhamento, não selo; nota anti-homologação (§3/§9; invariante 7; R-23) |
| **R-15.08** | "Validação jurídica/MEC definitiva" prometida em proposta | promessa falsa | validação é evidência datada; `doesNotImply` (§8/§9; R-14.09/R-14.10) |
| **R-15.09** | Afirmação de marketing fora da lista permitida | reputação/dano jurídico | tabela permitido×proibido vinculante (§11.2; princípio 18) |
| **R-15.10** | Promessa de "cobrir todo o conhecimento" | expectativa falsa; perda de confiança | cobertura é estrutural, não exaustiva; `CoverageMatrix` descreve (§3/§2; E0 D5) |
| **R-15.11** | Venda como substituto de professor/currículo/livro | descumprimento do posicionamento | recurso complementar; afirmação proibida (§3/§11.2; E6) |
| **R-15.12** | Desconto/gratuidade usado para destravar portão | garantia relaxada por preço | preço não compra destravamento (§10; princípio 12) |
| **R-15.13** | Comercial declarando prontidão que a operação não deu | oferta acima do `readinessStatus` | prontidão é da operação; comercial só lê o gate (§14; princípio 13; R-14.35) |
| **R-15.14** | Conflito de interesse: quem vende decide mérito | viés/destrave indevido | segregação de funções; comercial não decide publicabilidade (§7.3; R-14.31) |
| **R-15.15** | Investidor/board impondo relaxar invariante | núcleo capturado por capital | captação não compra exceção; due diligence = riscos (§8.3; invariante 30) |
| **R-15.16** | Demo apresentando seed/placeholder como real | demonstração enganosa | demo usa publicável + seed marcado (§11.3; R-13.18) |
| **R-15.17** | Demo escondendo incerteza/`gatingReason` para impressionar | honestidade epistêmica violada | demo exibe incerteza/fonte; isso É o diferencial (§11.3; D7; invariante 9) |
| **R-15.18** | Material comercial suprimindo "o que NÃO se promete" | expectativa falsa contratual | coluna inegociável em proposta/demo/contrato (§3.4/§11.2) |
| **R-15.19** | Export comercial vazando NC/SA fora do permitido | violação de licença | matriz de licença no export; NC nunca; SA/ODbL isolado (§5/§9; invariantes 18/19/27; R-14.08) |
| **R-15.20** | Pressão de cliente forçando publicar item bloqueado | publicação ilegítima | pressão é barrada; vira incidente, não exceção (§2; princípio 20; E14, §11) |
| **R-15.21** | Cláusula contratual exigindo apagar conteúdo/trilha | histórico/proveniência perdidos | correção é versionada; nada se apaga (§7.1; invariantes 16/29; R-14.12) |
| **R-15.22** | Parceiro de financiamento impondo `ClaimSet` enviesado | viés editorial comprado | mérito é da curadoria; segregação; controvérsia → `ClaimSet` neutro (§7.3; E3.1) |
| **R-15.23** | Métrica de tração de vaidade escondendo piso baixo | decisão de investimento enganosa | marcos ligados a `readinessStatus`/qualidade; anti-Goodhart (§8.2; E14, §7.3) |
| **R-15.24** | CRM/peça comercial armazenando PII de menor | violação LGPD/ECA | CRM externo sem PII de menor; sem dado de aluno no funil (§12.2; invariante 21) |
| **R-15.25** | LMS/edtech parceiro escrevendo fato ou recebendo PII no KC | fronteira/privacidade violadas | consumo de publicável; identidade separada; sem escrita (§7/§12; E14, §9; R-14.07/R-14.36) |
| **R-15.26** | Edital simulado sem fonte oficial tratado como real | desinformação/erro comercial | define modelo de dossiê; edital concreto só com texto oficial (§9.1; limite) |
| **R-15.27** | Acessibilidade tratada como "plano premium" | exclusão de usuário; risco legal (LBI) | acessibilidade é piso em todos os planos (§10.2; invariante 23) |
| **R-15.28** | Promessa pública específica (PNLD/edital) sem base | risco jurídico/reputacional | só afirmações permitidas; nota anti-homologação; sem promessa de resultado (§9.3/§11.2) |
| **R-15.29** | White-label do parceiro removendo mediação de tema sensível | dano editorial; descumprir Leis 10.639/11.645 | mediação preservada no white-label; violação = bloqueio (§5.4; E3.1; princípio op. 19) |
| **R-15.30** | "Exclusividade de fato" prometida a cliente/museu | KC tratado como propriedade editável | proveniência é soberana; exclusividade só de **apresentação/licença**, não do fato (§3.4/§5) |
| **R-15.31** | Venda condicionada a esconder fonte para "proteger IP" | proveniência suprimida | fonte/citação sempre visíveis; IP do parceiro é de marca/forma, não do fato (§5.4; invariantes 10/14) |
| **R-15.32** | Meta de receita pressionando escala sem qualidade | piso epistêmico cai por receita | qualidade soberana; `ready-for-scale` por critério, não meta (§8.2/§14; R-14.35/R-14.28) |
| **R-15.33** | Contrato de distribuição sem nota anti-homologação no produto entregue | promessa implícita de homologação | nota anti-homologação embutida em todo pacote/export (§5/§9; invariante 7; R-23) |
| **R-15.34** | Comercial transformando feedback em correção sem pipeline | claim alterado fora de revisão | feedback vira pedido de ingestão; correção pelo pipeline/revisão (§6.4; E13) |
| **R-15.35** | Parceiro institucional exigindo "autoria" com escrita no KC | fronteira violada por prestígio | universidade/instituição entra como **fonte** sob portão; sem escrita (§7.2; invariante 20) |
| **R-15.36** | Oferta a segmento abaixo do `minReadinessToOffer` | produto imaturo vendido | matriz de segmentos define gate; oferta bloqueada até prontidão (§4.3/§14; princípio 13) |

**[NORMATIVO]:** este registro é **vinculante**; cada risco tem teste, portão ou invariante associado e um indicador monitorado (Seção 12 / E14, §8). Nenhum risco é "resolvido" relaxando o invariante que o contém (invariante 30; E13/E14, §15.10).

---

## 14. Critérios de prontidão comercial e bloqueios

### 14.1 A prontidão comercial **lê** a prontidão da operação

**[NORMATIVO]** o comercial **não cria** um enum de prontidão próprio: ele **reutiliza** o `readinessStatus` da operação (E14, §7.2) como **gate de oferta**. A prontidão é determinada pela operação/QA (E14); o comercial a **lê** e decide **o que pode ser ofertado**, nunca a eleva nem a contorna (princípio comercial 13; R-15.13/R-15.36). O rebaixamento automático da operação (E14, §7.2) **rebaixa também a autorização comercial**: se um escopo cai de `ready-for-school` para `not-ready`/`blocked`, as ofertas correspondentes ficam **suspensas** até a correção versionada.

### 14.2 Matriz de autorização comercial por `readinessStatus`

**[NORMATIVO]** o que se pode ofertar em cada nível (cumulativo: cada nível exige o anterior).

| `readinessStatus` | O que se PODE ofertar | O que NÃO se pode ofertar | Evidência exigida |
|---|---|---|---|
| `blocked` | **nada** | qualquer oferta, demo paga, piloto, parceria de distribuição | — (corrigir sob os portões primeiro) |
| `not-ready` | conversas exploratórias; carta de intenção **sem** promessa de entrega | piloto; venda; contrato; demo apresentando incompleto como completo | registro de riscos transparente |
| `ready-for-pilot` | **piloto** (`pilot`/`museum`/`institutional-use`) sem PII real; demo honesta | venda escolar plena; escala; white-label | QA verde P0; 10 papéis operando; analytics agregado sem PII (E14, §7.2) |
| `ready-for-school` | **venda a escola/rede** (`single-school`/`network`); integração LMS | escala plena; white-label de escala | laudo ASES; DPIA revisada; piloto positivo; nota anti-homologação (E14, §7.2) |
| `ready-for-scale` | **escala** (rede ampla); **white-label controlado** (§5.4); procurement de escala | qualquer item que viole §2 (sempre) | throughput sustentado sem queda de revisão; cobertura monitorada; MTTR no alvo (E14, §7.2) |

### 14.3 Bloqueios comerciais

**[NORMATIVO]** uma oferta/parceria/captação/procurement é **bloqueada** enquanto: existir caminho de escrita factual fora do pipeline (fronteiras E11 — invariante 20); qualquer portão puder ser destravado por urgência/autoridade/pressão comercial (princípio 2; R-13.35; R-14.04/R-14.34); a oferta exceder o `readinessStatus` do escopo (§14.2; R-15.36); houver promessa de homologação MEC/PNLD ou validação jurídica definitiva (R-15.07/R-15.08); o piloto coletar PII de aluno sem base legal (R-15.03); a métrica individualizar aluno (R-15.05); o white-label remover garantia epistêmica/licença/acessibilidade/nota anti-homologação (R-15.06/R-15.29); o parceiro obtiver porta de escrita no KC (R-15.04/R-15.35); o material afirmar fora da lista permitida ou suprimir "o que não se promete" (R-15.09/R-15.18); ou houver risco do registro (Seção 13) sem teste/portão/invariante associado e monitorado (espelha E14, §15.10).

### 14.4 Rebaixamento e suspensão de oferta

**[NORMATIVO]** se um incidente (E14, §11) rebaixar a prontidão de um escopo, as ofertas/contratos em curso para esse escopo são **suspensos** até a correção **versionada** (nunca por apagamento); a comunicação ao cliente é **honesta** sobre o estado, sem prometer prazo de "destravamento" que dependeria de furar portão (princípio 2; R-14.04). A suspensão comercial é uma consequência da governança, não uma falha a esconder.

---

## 15. Encerramento e handoff para a Etapa 16

### 15.1 O que a Etapa 15 entrega

A Etapa 15 entrega o **`CommercialGoToMarketLayer` completo em nível de plano comercial/go-to-market**: a definição da camada e sua relação com as Etapas 0/1/6/11/14 (Seção 1); **20 princípios comerciais** vinculantes e os limites de mercado (Seção 2); a **proposta de valor e o posicionamento** canônico (recurso complementar; honestidade epistêmica como diferencial) com a `ValuePropositionMap` e a coluna inegociável "o que NÃO se promete" (Seção 3); os **segmentos/ICPs/personas** com o enum `segmentType`, as entidades `MarketSegmentProfile`/`ICPProfile`/`InstitutionalPersona`, a matriz de segmentos e os disqualificadores universais (Seção 4); os **modelos de implantação e pacotes** com o enum `deploymentTier`, a entidade `DeploymentPackage`, a matriz de modelos comerciais e as regras de **white-label controlado** (Seção 5); o **programa de pilotos** sem PII com `PilotProgram` e as três posturas de dados (Seção 6); as **parcerias** com o enum `partnershipType`, a entidade `PartnershipModel`, a matriz de parceria e a regra "parceiro não escreve fato" (Seção 7); a **captação** com `InvestmentThesis`/`FundingMilestone`, marcos ligados à prontidão e a regra "captação não compra exceção" (Seção 8); o **procurement** com o enum `procurementChannel`, as entidades `ProcurementDossier`/`ProcurementRequirement`, a matriz de procurement e a nota anti-homologação (Seção 9); a **precificação conceitual** com o enum `pricingModelType`, a entidade `PricingModel` e a regra "preço não compra destravamento" (Seção 10); os **materiais comerciais** com `CommercialCollateral`, a tabela permitido×proibido de marketing e a demonstração honesta (Seção 11); as **métricas comerciais agregadas** com `CommercialMetric` herdando `OperationalMetric` e a matriz permitido×proibido (Seção 12); a **matriz de 36 riscos comerciais `R-15.NN`** com mitigação (Seção 13); e os **critérios de prontidão comercial** que **leem** o `readinessStatus` da operação como gate, com a matriz de autorização e os bloqueios (Seção 14).

### 15.2 O que a Etapa 15 **não** entrega

A Etapa 15 **não** entrega: código, CRM implementado, contrato jurídico definitivo, edital real simulado sem fonte oficial, números de preço/receita fixados; conteúdo factual novo (nenhum claim/fonte/cena criado ou alterado); alteração do KC ou da Etapa 14; promessa de homologação MEC, aprovação PNLD ou validação jurídica definitiva; coleta de PII real de aluno; analytics individualizado; white-label que remova garantias; nem qualquer mecanismo pelo qual comercial/procurement/parceiro/investidor destrave um portão. Esses itens ou são proibidos por natureza ou pertencem à Etapa 16 e à execução.

### 15.3 Invariantes que passam a ser vinculantes

A partir desta entrega, vinculam o comercial (somando-se aos 30 invariantes da E11, aos `T-*` do MVP, aos 28 princípios/24 testes `T-13.NN`/38 riscos `R-13.NN` da E13 e aos 22 princípios/6 funções de governança/38 riscos `R-14.NN` da E14): **(i)** comercial vende, não governa (Seção 1); **(ii)** os 20 princípios comerciais (Seção 2); **(iii)** posicionamento como recurso complementar e honestidade epistêmica como diferencial, com "o que NÃO se promete" inegociável (Seção 3); **(iv)** `minReadinessToOffer` por segmento (Seção 4); **(v)** white-label não remove garantia epistêmica/licença/acessibilidade/nota anti-homologação (Seção 5.4); **(vi)** piloto sem PII de aluno (Seção 6); **(vii)** parceiro não escreve fato no KC (Seção 7); **(viii)** captação não compra exceção (Seção 8); **(ix)** procurement não destrava portão; nota anti-homologação obrigatória (Seção 9); **(x)** preço não compra destravamento; acessibilidade é piso, não premium (Seção 10); **(xi)** materiais usam publicável e só afirmações permitidas (Seção 11); **(xii)** métrica comercial agregada, sem PII, nunca fonte (Seção 12); **(xiii)** prontidão comercial lê o `readinessStatus` da operação, nunca o eleva (Seção 14). Permanecem canônicas: **forma muda; fato não**; **score/cache/busca/embedding/dashboard não é verdade**; **IA não é fonte factual**; **licença governa expressão/asset, não o fato recodificado**; **menores exigem minimização máxima de dados**; **offline não relaxa garantias**; **degradação nunca remove o piso epistêmico**; **correção cria versão, nunca apaga**; e — novas — **preço não compra destravamento**; **proteção de menor é piso, não recurso de venda**; **honestidade epistêmica é diferencial, não defeito a esconder**.

### 15.4 Estados e entidades que ficam oficiais

Ficam oficiais e estáveis para a Etapa 16: os enums `segmentType` (9 valores), `deploymentTier` (6), `partnershipType` (7), `procurementChannel` (4) e `pricingModelType` (6); a **reutilização** do `readinessStatus` (E14) como gate de oferta (sem novo enum de prontidão); e as entidades `CommercialGoToMarketLayer`, `ValuePropositionMap`, `MarketSegmentProfile`, `ICPProfile`, `InstitutionalPersona`, `DeploymentPackage`, `PilotProgram`, `PartnershipModel`, `InvestmentThesis`, `FundingMilestone`, `ProcurementDossier`, `ProcurementRequirement`, `PricingModel`, `CommercialCollateral` e `CommercialMetric`. Alterá-los exige reabrir a Etapa 15.

### 15.5 O que a Etapa 16 (implantação / execução comercial) deve receber

```txt
para a Etapa 16 = {
  a matriz de autorização comercial por readinessStatus (Seção 14) como gate de TODA oferta/contrato,
  a ValuePropositionMap e a lista permitido×proibido de marketing (Seções 3/11.2) como base de discurso,
  a matriz de segmentos/ICP com minReadinessToOffer (Seção 4) para priorização e pipeline,
  os modelos de pacote/white-label controlado (Seção 5) como base de proposta — sem remover garantia,
  o PilotProgram sem PII (Seção 6) como protocolo de execução de piloto real,
  os modelos de parceria (Seção 7) com a regra "parceiro entra pelo portão/pipeline; nunca escreve fato",
  a InvestmentThesis/FundingMilestone (Seção 8) ligadas à prontidão, para captação real,
  o ProcurementDossier/ProcurementRequirement (Seção 9) — a serem instanciados sobre TEXTO OFICIAL de edital,
  os eixos de PricingModel (Seção 10) — números a fixar com pesquisa de mercado de fonte oficial,
  o registro R-15.NN + mapa de calor (Seção 13 + E14, §13.3) como due diligence comercial,
  a regra inegociável de que comercial/procurement/parceiro/investidor NUNCA destrava portão (princípio 2/15; R-14.04/R-14.34)
}
```

### 15.6 Pendências que seguem abertas

**[PENDÊNCIA]** para a Etapa 16/execução: números concretos de preço/ticket/receita por segmento e canal (§10); dimensionamento de mercado (TAM/SAM/SOM) e nº de instituições endereçáveis por segmento, com fonte oficial atualizada (§3.3); instanciação de dossiês de procurement sobre **editais reais com texto oficial** (§9.1); escolha de CRM e ferramentas comerciais (sem PII de menor — §12.2); execução real de pilotos, captação, negociações e contratos (limite desta etapa); modelo concreto de white-label por parceiro, dentro das restrições inegociáveis (§5.4); e a calibração de SLAs comerciais/suporte (herdada — E14, §15.8).

### 15.7 Critérios que autorizam passar para a Etapa 16

A Etapa 16 (implantação real / execução de piloto / negociação / documentos comerciais / captação / contratos / cronograma) é autorizada quando: ao menos um escopo está em `ready-for-pilot` sob a operação (E14, §7) e a matriz de autorização comercial (§14.2) está fixada como gate; a `ValuePropositionMap` e a tabela permitido×proibido (§3/§11.2) estão estabelecidas; a matriz de segmentos com `minReadinessToOffer` existe (§4); o `PilotProgram` sem PII está definido como protocolo (§6); os modelos de parceria/captação/procurement estão definidos sob suas regras inegociáveis (§7/§8/§9); a precificação conceitual e o registro `R-15.NN` estão prontos (§10/§13); e está cristalino que comercial vende sem governar, que procurement não destrava portão, que piloto não coleta PII, que parceiro não escreve fato, que white-label não remove garantia, que BNCC é alinhamento e que validação é evidência.

### 15.8 Critérios que bloqueiam a passagem

A passagem é **bloqueada** enquanto: existir caminho de escrita factual fora do pipeline (fronteiras E11 violadas — invariante 20); qualquer portão puder ser destravado por urgência/autoridade/pressão comercial/edital/investidor (princípio 2/15; R-13.35; R-14.04/R-14.34); a prontidão comercial puder ser **elevada pelo comercial** em vez de lida da operação (R-15.13/R-15.36); houver promessa de homologação MEC/PNLD ou validação jurídica definitiva (R-15.07/R-15.08); o piloto/CRM/métrica coletar ou individualizar PII de aluno (R-15.03/R-15.05/R-15.24); o white-label remover garantia epistêmica/licença/acessibilidade/mediação/nota anti-homologação (R-15.06/R-15.29); o parceiro/instituição obtiver porta de escrita no KC (R-15.04/R-15.35); o material afirmar fora da lista permitida ou suprimir "o que não se promete" (R-15.09/R-15.18); ou houver risco do registro (Seção 13) sem teste/portão/invariante associado e monitorado (espelha E14, §15.10).

---

*Documento de entrega da Etapa 15 — Plano Comercial, Implantação Piloto, Parcerias, Captação, Procurement Público/Privado e Go-to-Market (v1.0), sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z, 6, 7, 8, 9, 10, 11, 12, 13, 14). Define a `CommercialGoToMarketLayer`: os 20 princípios comerciais e os limites de mercado, o posicionamento como recurso educacional digital complementar com honestidade epistêmica como diferencial e a `ValuePropositionMap`, os segmentos/ICPs/personas com `minReadinessToOffer`, os modelos de implantação/pacotes e o white-label controlado, o programa de pilotos sem PII, os modelos de parceria sob a regra "parceiro não escreve fato", a tese de captação com marcos ligados à prontidão, a base de procurement com a nota anti-homologação, a precificação conceitual, os materiais comerciais e a demonstração honesta, as métricas comerciais agregadas, a matriz de 36 riscos `R-15.NN` e os critérios de prontidão comercial que leem o `readinessStatus` da operação como gate. Não escreve código, não implementa CRM, não cria contrato definitivo, não simula edital real sem fonte oficial, não promete homologação MEC/PNLD nem validação jurídica definitiva, não cria claims, não altera o KC nem a Etapa 14, não destrava portão por pressão comercial, não coleta PII de aluno, não cria analytics individualizado, não vende alinhamento BNCC como selo, currículo obrigatório ou substituto de professor, não oculta incerteza/fonte/licença/publicabilidade e não permite white-label que remova garantia. Comercial vende, não governa; procurement não destrava portão; piloto não coleta PII; métricas comerciais são agregadas; parceiro não escreve fato; BNCC é alinhamento, não selo; validação é evidência, não promessa; preço não compra destravamento; e qualquer pressão de mercado que tente violar QA, licença, privacidade, acessibilidade, publicabilidade ou revisão humana resulta em bloqueio, nunca em exceção. Próxima etapa, quando solicitada: Etapa 16 — Implantação real, execução de piloto, negociação, documentos comerciais, captação, contratos e cronograma.*
