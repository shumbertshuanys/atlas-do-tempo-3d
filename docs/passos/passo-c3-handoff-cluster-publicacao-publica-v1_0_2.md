# Passo C3 — Cluster de publicação pública (famílias F2/F5/F6)

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** handoff do Passo **C3** da Trilha C (governança). Caracteriza, **no nível de governança**, o que precisa ser verdade para um item/cena tornar-se **publicamente publicável**, cobrindo as famílias **F2** (fonte/licença por asset), **F5** (fundação escolar) e **F6** (jurídico/sensível vivo). No mesmo passo, **ratifica PG6** como **contrato visual normativo** (camada de UX / padrão-de-marca), amarrando-o à Etapa 10, e usa a **classificação de sensibilidade de PG5** (já operante como campo do DoR) para mostrar como se estima o *split* público/mediado de uma cena **antes do build**. Segue o protocolo um-passo-por-chat (Playbook §1) e o formato de 9 pontos + rodapé (Playbook §2).
**Abertura padrão:** estamos no passo **C3** do `estado-atual-e-roteiro`; contexto no projeto.
**Data:** 2026-06-21.

> **Guarda de leitura.** C3 **implementa** invariantes que já existem — não os emenda. Em especial: o **núcleo epistêmico de PG6 já é constitucional** (Constituição **Art. 7**) e **já operante** na fila (Playbook **§5.4**, não-automação da fronteira). O que C3 acrescenta é a **camada de contrato visual / padrão-de-marca** (como a fronteira e o mapa se apresentam na UX). Nada aqui pode ser lido como permissão para enfraquecer o **Art. 7** nem o **Art. 6**.

---

## 1. Objetivo

Caracterizar o **cluster de publicação pública** — o conjunto de condições que tornam um item/cena **publicamente publicável**, identificado em `analise-pendencias` §4 como o salto **fatia → MVP público** (acende F2, F4, F5, F6). Concretamente: (a) fixar, no nível de governança, o **terceiro portão** (publicabilidade pública) e distingui-lo dos dois que já existem — o **DoR** (entrada, PG4) e o **invariante de exibição** (`approved`, Art. 6); (b) caracterizar **F2** (P07 confirmação asset-level de fonte; P10 licença por asset) como **portão de qualquer coisa pública**; (c) caracterizar **F5** (offline; acessibilidade e-MAG/WCAG/LBI/ASES; LGPD/proteção de menores) e **F6** (DPIA/RIPD; *legal-review* de pessoas vivas/identificáveis e de itens como BR-07; ECA); (d) **ratificar PG6** como contrato visual normativo amarrado à Etapa 10; e (e) usar **PG5** para tornar o *split* público/mediado de uma cena **previsível antes do build**.

Resultado pretendido: o cluster de publicação pública fica **caracterizado em governança** e amarrado ao *readiness gate* **`ready-for-school`** (Etapa 14 §7.2); e **PG6** fica pronto para promoção a **[VIGENTE]** (a emitir, sob confirmação, no **Playbook v1.3**).

## 2. Escopo

**Dentro:**
- A definição do **portão de publicação pública** como **terceiro limiar**, distinto do DoR e de `approved` (Art. 6), e o achado de que **`approved` ≠ publicamente publicável**.
- A caracterização das três famílias como **camadas de condição**: **F2** (universal — todo asset público), **F5** (escopo — uso escolar) e **F6** (condicional — itens sensíveis/vivos), com **PG5 como roteador** das condições por item.
- A **ratificação de PG6** (contrato visual): `ClaimSet` com fronteira moral/factual explícita + resumo por faixa etária; mapa esquemático rotulado por padrão; fronteira histórica/paleo **nunca inventada** — amarrado às entidades da Etapa 10.
- A **estimativa de *split* público/mediado** por PG5, com ilustração nas cenas já modeladas (1789/4D, GOE/K-Pg, clima moderno, BR-07).
- O **acoplamento item → escopo**: o cluster por item alimenta o `ready-for-school` (E14 §7.2) por agregação.
- A **proposta documental** (Playbook v1.3 e/ou um documento de portão de publicação pública), **a confirmar antes de emitir**.

**Fora (limites explícitos):**
- **Produzir os pareceres reais** — DPIA/RIPD, laudo ASES, parecer jurídico, evidência de piloto. Isso é **execução** (Etapa 14 §10); C3 **define o portão**, não fabrica seus insumos.
- **Números** — SLA por fila, percentuais de amostragem de auditoria, prazos, **limiar de proporção pública**. Seguem `[PENDÊNCIA]` de execução (E13/E14); a estimativa de *split* é **planejamento**, nunca alvo/SLA.
- **Código, protótipo, escolha de stack, decisão de dados.**
- **Reabertura de qualquer etapa**; alteração de **qualquer invariante** da Constituição (C3 **implementa**, não emenda).
- Qualquer leitura que **enfraqueça o Art. 7** (fronteira escrita à mão de PG6/§5.4) **ou o Art. 6** (`approved` continua **necessário, não suficiente** para o público).

## 3. Diagnóstico

O que o corpus e a fatia tornam executável **agora**:

1. **Há três portões, não dois.** O corpus já fixou o **DoR** (porta de **entrada** — PG4, Playbook §4.2) e o **invariante de exibição** (porta para virar **fato exibível** — Art. 6: `reviewStatus = approved`). Mas `analise-pendencias` §2 (F2) registra o achado decisivo: **mesmo os ~20 itens *publicáveis* de 1789 ainda têm `PENDENTE_CONFIRMACAO_FONTE`** — *"`approved` (pode exibir) ≠ fonte confirmada por asset. São portões distintos."* Logo existe um **terceiro limiar**, a **publicabilidade pública**, que `approved` **não** satisfaz sozinho. C3 o nomeia e caracteriza.
2. **F2 é o portão de qualquer coisa pública.** `analise-pendencias` §5.2: *"Confirmação de fonte por asset (F2) é pré-requisito até do 'público'."* O maquinário já existe: a Etapa 1.1 dá o código **CONF** (entra após confirmação por asset) e o Risco 2 (licença heterogênea por item → `reviewStatus = pending` até confirmar); a Etapa 11 §9.5 fixa **`perAssetConfirmed`** como condição de servir um asset de fonte heterogênea. Falta **declarar essa confirmação como portão do público**.
3. **F5 e F6 acendem no salto ao MVP público, não na fatia.** `analise-pendencias` §4: F5 (offline/acessibilidade/LGPD) e F6 (jurídico/sensível vivo) são **✗ no MVP público**, **—** na fatia. A Etapa 11 (§9.8, §11.8–11.10) e a Etapa 10 (§11.5) já fixam o piso de acessibilidade/offline; o **`ready-for-school`** da Etapa 14 §7.2 já **lista** ASES, DPIA/RIPD, auditoria de licença e auditoria de conteúdo sensível como critérios. C3 **amarra** o cluster por item a esse *gate* de escopo.
4. **PG5 já é porta de entrada e dá o roteamento.** O Passo C2 (D-C2.3) aplicou PG5 como **campo nº 3 do DoR**: a sensibilidade (`público`/`mediado`/`legal-review`, Leis 10.639/2003 e 11.645/2008) é classificada **na modelagem** e **define os papéis exigidos e o `pending` por padrão**. É exatamente o roteador que diz **quais condições do cluster** cada item precisa cumprir — e o que torna o *split* público/mediado **estimável antes do build**.
5. **O núcleo de PG6 já opera; falta o contrato visual.** Playbook §7 + §5.4: a fronteira *"sem equivalência"* de cada `ClaimSet` é **escrita à mão** (Art. 7), e o mapa esquemático é **epistemicamente superior** a fronteiras inventadas. A Etapa 10 já tem as **entidades de apresentação** (`EpistemicLabelView`, `UncertaintyLegend`, `EquivalenceWarningNotice`, `AnachronismNotice`, `paleoPositionPolicy`, `weightedClaimSets`, `ViewDegradationLadder`). Falta **promover** isso de prática a **padrão-de-marca normativo**.

Conclusão do diagnóstico: o cluster não precisa de tecnologia nova nem de decisão de dados; precisa de **um nome de portão, um roteador (PG5), um contrato visual (PG6) e um acoplamento ao `ready-for-school`** — tudo a partir de invariantes que já existem.

## 4. Decisões principais

- **D-C3.1 — O portão de publicação pública é o *terceiro* limiar; `approved` é necessário, não suficiente.**
  Fica caracterizado um estado conceitual de **publicabilidade pública** (`publiclyPublishable`) que exige, **cumulativamente**: (i) `reviewStatus = approved` (Art. 6 — todas as revisões aplicáveis aprovadas, §5.3); **e** (ii) o **cluster público confirmado por item/asset** (F2 + F5 + F6, conforme a sensibilidade PG5). `approved` torna o item **exibível** (inclusive na fatia descartável e em vistas internas); **publicamente publicável** é o que pode entrar no **MVP público**. Os dois não se confundem.
  *Justificativa:* o achado de `analise-pendencias` §2/§5.2 (item publicável de 1789 com fonte ainda pendente) prova que `approved` e "fonte/licença confirmada por asset" são portões distintos. Nomear o terceiro limiar impede publicar o núcleo com citação ou licença ainda pendente.
  *Guarda crítica:* isto **não** cria invariante novo nem afrouxa o Art. 6 — **implementa** Arts. 6/9/11/14. O Art. 6 segue soberano: item `pending`/`legal-review`/`rejected` **não existe como fato** para o público; o cluster apenas acrescenta as condições de *publicação*, a jusante de `approved`.

- **D-C3.2 — F2 é o portão universal (P07 fonte + P10 licença), por asset.**
  Para um item/asset ser **publicamente publicável**, além de `approved`: (a) **fonte confirmada por asset** — `perAssetConfirmed = true` (P07; encerra `PENDENTE_CONFIRMACAO_FONTE`), não apenas *identificada* como exige o DoR; (b) **licença resolvida por asset** (P10) com `storagePartition` definitiva e `exportPolicy` coerente (Etapa 11 §9.4); (c) **expressão NC nunca pública** — só o **fato re-derivado de fonte livre** (Etapa 11 §9.6; Etapa 1.1 caso 2); (d) **SA/ODbL** só como **camada isolada**, com atribuição e ShareAlike honrados (Etapa 11 §9.7); quando o formato de exportação não puder honrar o ShareAlike, a exportação daquele material é **impedida**, não relaxada.
  *Justificativa:* F2 é, por `analise-pendencias` §5.2, pré-requisito **até do público**. O `LicenseComplianceService` (Etapa 11 §3.4) já é o **guardião único** de ingestão/exportação; C3 declara sua confirmação como portão do público.
  *Âncora constitucional:* Art. 5 (índice ≠ autoridade; toda fonte classificada), Art. 9 (na dúvida de fonte/licença → bloqueio), Art. 10 (proveniência como FK; aresta órfã impossível), Art. 11 (isolamento físico; licença governa expressão, não o fato recodificado).

- **D-C3.3 — F5 é o portão de fundação escolar (escopo).**
  Para **uso escolar público** de um escopo, valem (verificados como **auditorias de escopo** no `ready-for-school`, E14 §7.2): (a) **piso de acessibilidade** e-MAG/WCAG/LBI — equivalente textual de todo visual, navegação por teclado, foco visível, contraste, **redundância não-cromática**, movimento reduzido — **presente em todos os degraus**, inclusive offline e projetor (Etapa 11 §11.8–11.9; Etapa 10 §11.5); (b) **degradação graciosa** 3D→2D→estático→offline→projetor **preservando o piso epistêmico** (Art. 12; Etapa 11 §11.10; `ViewDegradationLadder` da Etapa 10 §7.2); (c) **pacote offline** que **não relaxa** licença/publicabilidade/mediação/papel (Etapa 11 §9.8); (d) **minimização máxima de dados de menores** — sem PII de aluno no núcleo, analytics agregado sem PII, dado de aluno jamais treina modelo nem gera fato (Art. 14; Etapa 11 §4.9).
  *Justificativa:* F5 **bloqueia o MVP real, não a fatia** (`analise-pendencias` §4); os pisos já são invariantes; C3 os agrega ao portão de escopo.
  *Limite:* o **laudo ASES** e a **DPIA/RIPD** são **execução** (E14 §10.2/§10.3); o portão os **exige como insumo**, mas C3 **não os produz**.

- **D-C3.4 — F6 é o portão jurídico/sensível vivo (condicional, dirigido por PG5).**
  Itens que tocam **pessoas vivas/identificáveis**, **BR-07** (ditadura) e congêneres entram como **`reviewStatus = legal-review` por padrão** — e, por Art. 6, **não existem como fato para o público** até liberação. Para publicação pública desses itens: (a) **`legal-review` aprovado** pelo `legalReviewer`; (b) **auditoria de conteúdo sensível limpa** (E14 §7.2); (c) **fato × cenário × previsão separados** (Art. 7 — `claimType` distinto; `UncertaintyProfile` como faixa; ex.: clima moderno com cenário/modelo rotulado, Etapa 10 §12.3); (d) **ECA/LGPD** respeitados (Art. 14). A escolha conservadora prevalece (Etapa 3.1 §9.2): na dúvida, **restringe-se, rotula-se ou exige-se mediação**.
  *Justificativa:* F6 é **radar antes de qualquer piloto** (`analise-pendencias` §5.4); Etapa 3.1 §9.2 já obriga revisão humana para pessoas vivas/identificáveis e temas sensíveis.
  *Limite:* a **DPIA/RIPD** e o **parecer jurídico** reais são E14 §10.3; o `legalReviewer` **não é, e o documento não substitui, parecer de advogado**.

- **D-C3.5 — O cluster por item alimenta o `ready-for-school` por agregação (item → escopo).**
  O **cluster de publicação pública** é a **pré-condição por item/asset** (F2 sempre; F6 conforme PG5). O **`ready-for-school`** (E14 §7.2) é o **portão de escopo** que **agrega** esses itens e acrescenta as **auditorias de escopo**: P1 ao menos `partially-populated`, **laudo ASES aprovado**, **DPIA/RIPD revisada**, **auditoria de licença/exportação limpa**, **auditoria de conteúdo sensível limpa**, `T-PROF×ALUNO`, **nota anti-homologação** no viewer e no export, e evidência de piloto positiva. C3 **conecta** os dois níveis **sem fixar números** e **sem produzir as auditorias**.
  *Justificativa:* dá ao salto fatia → MVP público uma régua objetiva e já existente, em vez de um juízo *ad hoc*.

- **D-C3.6 — Ratificar PG6 como contrato visual normativo. [proposta: §7 + §8 do Playbook v1.3 → VIGENTE]**
  Ficam estabelecidas **duas cláusulas de contrato visual**, a dobrar no Playbook v1.3, **amarradas à Etapa 10**:
  **(a) Contrato visual do `ClaimSet`.** Toda controvérsia legítima se apresenta como `ClaimSet` com a **fronteira moral/factual explícita** (a fronteira *"sem equivalência"* **escrita à mão**, preservada de §5.4) **+ resumo por faixa etária**; pesos assimétricos visíveis (`weightedClaimSets`); **negacionismo rotulado-rejeitado, fora do par** (`EquivalenceWarningNotice`, Etapa 10 §11.4). A incerteza aparece como **faixa**, com **redundância não-cromática**, **nunca "omitir"** (`UncertaintyLegend`/`EpistemicLabelView`, §11.1).
  **(b) Contrato visual do mapa esquemático.** O mapa é **rotulado por padrão** como **reconstrução modelada**; **fronteira histórica/paleo nunca é inventada**; paleoposição é distinguida de localidade atual (`paleoPositionPolicy`/`ModernCorrespondence`/`AnachronismNotice`, Etapa 10 §7.1/§12.3). O mapa esquemático rotulado é **epistemicamente superior** a fronteiras inventadas — é **padrão público**, não dívida.
  **(c) Sobrevivência à degradação.** O contrato visual **sobrevive a todos os degraus** 3D→2D→estático→offline→projetor; nenhuma vista "desliga" rótulo epistêmico por desempenho ou estética (Art. 12; `ViewDegradationLadder`).
  *Justificativa:* eleva o diferencial de implícito a **padrão obrigatório** (PG6 verbatim, Playbook §7).
  *Guarda crítica:* o **núcleo epistêmico** de PG6 **já é Art. 7** e **já opera** em §5.4. C3 acrescenta **apenas a camada de apresentação/marca**: a UX **apresenta** a fronteira, **nunca a gera**. PG6 **não pode** ser lido como permissão para enfraquecer o Art. 7.

- **D-C3.7 — PG5 estima o *split* público/mediado antes do build.**
  Como a sensibilidade é classificada **na modelagem** (DoR campo nº 3), o **roteamento** é conhecido **antes** de construir a cena: `público` (publicável após F2; + F5 de escopo) · `mediado` (exige `MediationControl` e revisão editorial; **não** chega ao aluno sem mediação — Etapa 10 §11.3) · `legal-review` (default **não** público; exige F6). Contar os itens por etiqueta PG5 e cruzar com o estado F2 dá a **proporção pública estimada da cena antes do build**. *"Descoberta vira planejamento."* (Ilustração na Seção 5.)
  *Justificativa:* torna o custo editorial e o *split* **previsíveis no planejamento, não na surpresa** (PG5 verbatim; D-C2.3).
  *Limite:* a proporção é **estimativa de planejamento**, **não** alvo nem SLA (Art. 17); o número-limiar de "% pública aceitável" segue `[PENDÊNCIA]` de execução.

- **D-C3.8 — Consequência documental (proposta, a confirmar).**
  Recomenda-se emitir o **Playbook v1.3** dobrando: **PG6 → [VIGENTE]** como contrato visual (§7 atualizada + nova **§8 "Contrato visual de marca"**), e uma **§9 "Portão de publicação pública"** que fixa o cluster F2+F5+F6 como procedimento amarrado ao `ready-for-school` (E14 §7.2), **sem números**. Alternativa: manter o Playbook em §7 e emitir um **documento próprio de portão de publicação pública**. **Recomendo a via integrada** (um documento, um changelog, coerente com a dobra do C2 no v1.2). **A emitir somente após sua confirmação** (ver Seção 9).

## 5. Modelo conceitual

**Os três portões (sem código de aplicação):**

```
DoR (PG4, §4.2)          Art. 6 / approved (§5.3)      Cluster público (C3)             ready-for-school (E14 §7.2)
porta de ENTRADA     →   porta para FATO EXIBÍVEL  →   condição de PUBLICAÇÃO       →   portão de ESCOPO
8 campos tipados         todas as revisões              F2 (sempre) + F5 (escopo)        agrega itens + auditorias
(silêncio não passa)     aplicáveis aprovadas           + F6 (se sensível/vivo)          (ASES, DPIA, licença,
                         = EXIBÍVEL (inclui fatia)      por item/asset                    sensível, nota anti-homolog.)
                                                        = PUBLICAMENTE PUBLICÁVEL         = PRONTO P/ ESCOLA (escopo)
```

**PG5 como roteador do cluster (a sensibilidade decide as condições por item):**

```
etiqueta PG5 (DoR campo nº 3)        condições do cluster público
──────────────────────────────      ───────────────────────────────────────────────────────
público            → F2 (perAssetConfirmed + licença/partição/export)  [+ F5 de escopo]
mediado            → F2  +  MediationControl + revisão editorial  (não vai ao aluno sem mediação)
legal-review       → F2  +  F6 (legalReviewer + DPIA + auditoria sensível)   — default NÃO público
```

**Estimativa de *split* antes do build (ilustração nas cenas já modeladas — qualitativa, sem números):**

| Cena | Sensibilidade dominante (PG5) | *Split* esperado **antes do build** | Gargalo do público |
|---|---|---|---|
| **1789 / 4D (França)** | editorial; itens das Leis 10.639/11.645 (escravidão, colonização, indígenas) → `mediado` | núcleo `público` + parcela `mediado` | **F2** (mesmo os ~20 publicáveis têm `PENDENTE_CONFIRMACAO_FONTE`) |
| **GOE / ~2,4 Ga · K-Pg / ~66 Ma** | científica → majoritariamente `público` após revisão científica (P01) | alto `público`, com **rótulo de reconstrução** obrigatório (PG6-b) | **revisão científica** (P01) + F2 |
| **Clima moderno** | `público`, mas com `EquivalenceWarningNotice` (consenso ≠ negação) | `público` com cenário/modelo **rotulado** (D-C3.4c) | rotulagem fato × cenário × previsão (Art. 7) |
| **BR-07 (ditadura)** | pessoas vivas/identificáveis → `legal-review` por padrão | **não** público até F6 liberar | **F6** (`legal-review` + DPIA + auditoria sensível) |

**[NORMATIVO]:** nada nesta seção contorna o **Art. 6** — `mediado` e `legal-review` **não** vazam ao público/aluno como fato; `mediado` só chega ao aluno **sob mediação** (Etapa 10 §11.3); `legal-review` **não existe como fato** ao público até liberação. O **Art. 7/§5.4** permanece soberano: a fronteira do `ClaimSet` é **escrita à mão**; o contrato visual de PG6 a **apresenta**, não a **gera**.

## 6. Fontes / insumos necessários

Corpus interno (autoritativo): **Constituição v1.1** (Arts. 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17); **Playbook v1.2** (§2 formato; §4.2 DoR/PG5; §5.3 papéis; §5.4 não-automação; §7 PG6); **Etapa 1.1** (checklist/portão; matriz de decisão — códigos CONF/ISOLA/FATO/NAO; Risco 0–5; metadados de proveniência/licença); **Etapa 3.1** (§7 regime de mídia sensível e `natureLabel`; §9.1 fluxo e 8 papéis; §9.2 revisão humana obrigatória — pessoas vivas/identificáveis, sensíveis); **Etapa 10** (entidades de apresentação; §7.1 paleoposição rotulada; §11.1–11.5 incerteza/gating/mediação/anacronismo/acessibilidade; §12.3 exemplos por cena; invariante 13 anti-homologação); **Etapa 11** (§3.4 `LicenseComplianceService`; §4.9 separação de domínios de dado; §9 isolamento físico/`perAssetConfirmed`/`exportPolicy`; §11.8–11.10 acessibilidade/equivalente textual/fallback sem WebGL); **Etapa 14** (§7.2 *readiness gates*, sobretudo `ready-for-school`; §10 validação por evidência — ASES/DPIA/parecer como execução; §15.10 critérios de bloqueio); **`analise-pendencias`** (§2 famílias F2/F5/F6 e o achado `approved` ≠ fonte por asset; §4 matriz "o que bloqueia o quê"; §5.2/§5.4); **`estado-atual-e-roteiro`** (§4 Trilha C; cluster de publicação pública); **Passos C1/C1.1/C2** (separação Constituição/Playbook; DoR; PG5 aplicado).

**Insumos ausentes / pendências registradas:** nenhum bloqueante de governança. São **deliberadamente diferidos** (execução, E13/E14, não ausência de insumo): os **pareceres reais** (DPIA/RIPD, laudo ASES, parecer jurídico, evidência de piloto — E14 §10) e os **números** (SLA por fila, amostragem de auditoria, **limiar de proporção pública** — E13/E14, régua do Art. 17).

## 7. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| **R-C3.1** | O portão público ser lido como **invariante novo** ou como **afrouxamento do Art. 6** ("`approved` basta") | D-C3.1: C3 **implementa** Arts. 6/9/11/14; `approved` é **necessário, não suficiente**; o portão é **procedimento** (Playbook), não restrição constitucional nova; Art. 6 segue soberano |
| **R-C3.2** | O contrato visual de PG6 virar permissão para **enfraquecer o Art. 7** ("o visual basta; dispensar a fronteira escrita à mão") | D-C3.6/guarda: §5.4 (não-automação) e Art. 7 **soberanos**; a UX **apresenta** a fronteira, **nunca a gera**; o resumo por faixa **não** substitui a fronteira manual |
| **R-C3.3** | C3 **produzir os pareceres** (ASES/DPIA/parecer) — *scope creep* para execução | D-C3.3/D-C3.4: pareceres são E14 §10; o portão os **exige como insumo**, **não os fabrica**; `legalReviewer` não substitui advogado |
| **R-C3.4** | **Fixar números** (SLA, amostragem, **% pública**) prematuramente | D-C3.7/§2: cadência/números seguem `[PENDÊNCIA]` E13/E14; a estimativa de *split* é **planejamento**, **não** alvo/SLA (Art. 17) |
| **R-C3.5** | O **mapa esquemático** ser tratado como **dívida** (F3), não como **virtude epistêmica** | D-C3.6-b: mapa esquemático rotulado é **superior** a fronteiras inventadas — **padrão público**; F3 limita **fidelidade**, não **correção** (`analise-pendencias` §3 / §5.3) |
| **R-C3.6** | **Nota anti-homologação** ser perdida no público/export, sugerindo aprovação MEC/PNLD | E14 §7.2/§10 exigem a nota no **viewer e no export**; Etapa 10 invariante 13 (UX nunca promete MEC/PNLD); E14 §15.10 (bloqueio se prometer homologação) |
| **R-C3.7** | Item **`mediado`/`legal-review`** vazar ao público/aluno por aplicar o portão só a itens `público` | Art. 6 oculta `legal-review`; `mediado` exige `MediationControl` (Etapa 10 §11.3) e é **mediado pelo professor**, nunca exibido ao aluno como público sem mediação; PG5 roteia por item (D-C3.7) |
| **R-C3.8** | **Expressão NC/SA** chegar ao público/export indevidamente | D-C3.2: NC nunca pública (só fato re-derivado — Etapa 11 §9.6); SA/ODbL só isolada com ShareAlike honrado, e exportação **impedida** quando o formato não honra (Etapa 11 §9.7); `exportPolicy` no `LicenseStorageBinding` |

## 8. Entregáveis

1. **Este handoff** (`passo-c3-handoff-cluster-publicacao-publica-v1_0.md`) — registro do passo, decisões `D-C3.1..8`, modelo conceitual dos três portões, riscos.
2. **A caracterização do portão de publicação pública** — o terceiro limiar (`approved` ≠ publicamente publicável), as três famílias como camadas de condição (F2 universal · F5 escopo · F6 condicional) e **PG5 como roteador**, contidas nas Seções 4–5 e prontas para dobrar no Playbook v1.3.
3. **O texto de ratificação de PG6** (contrato visual — D-C3.6), pronto para promover a **[VIGENTE]** no Playbook v1.3.
4. **O método de estimativa de *split*** público/mediado por PG5 (Seção 5), com a ilustração nas cenas já modeladas.
5. **O acoplamento item → escopo** ao `ready-for-school` (E14 §7.2), como régua objetiva do salto fatia → MVP público.
6. **(A emitir, sob confirmação)** **Playbook v1.3** — PG6 → [VIGENTE] (contrato visual) + seção do portão de publicação pública, com changelog e nota de que **supersede o v1.2**.

## 9. Próximos passos

- **Confirmar a via documental e emitir o Playbook v1.3** dobrando **PG6 → [VIGENTE]** (contrato visual, §7 + nova §8) e a **seção do portão de publicação pública** (cluster F2+F5+F6 amarrado ao `ready-for-school`, sem números), com linha de changelog `v1.3` e nota de superseção do v1.2. *(Faço a seguir, quando você confirmar; é passo de fechamento documental. Decisão pendente sua: **via integrada** (Playbook v1.3, recomendada) **ou** **documento próprio** de portão.)*
- **Quando o pipeline/operação correrem (E13/E14):** produzir os **pareceres reais** (laudo ASES, DPIA/RIPD, parecer jurídico, evidência de piloto — E14 §10) e fixar os **números** que C3 deixou `[PENDÊNCIA]` (SLA por fila, amostragem de auditoria, **limiar de proporção pública**).
- **Trilhas A/B em paralelo:** o cluster **gateia o caminho público**, **não** a fatia nem a decisão de motor (B1) — A1 (Incremento 2: GOE/K-Pg) e B1/A3 (inflexão para produção) seguem desbloqueados (`estado-atual-e-roteiro` §5).
- **Operacional permanente:** cada chat sob a **Constituição v1.1 + o Playbook (v1.3 após emissão)** — um passo, por evidência, com handoff salvo; não criar projeto novo.

---

*Documento de governança do Passo **C3**, sob a Constituição v1.1 (Arts. 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17), o Playbook v1.2 (§2, §4.2, §5.3, §5.4, §7), a Etapa 1.1 (portão de licença/ingestão), a Etapa 3.1 (§7 mídia; §9 papéis), a Etapa 10 (Design/UX 3D), a Etapa 11 (§3.4/§9 licença; §11.8–11.10 acessibilidade) e a Etapa 14 (§7.2 `ready-for-school`; §10 execução), e os Passos C1, C1.1 e C2. Caracteriza o **cluster de publicação pública** como terceiro limiar (`approved` ≠ publicamente publicável), define F2 (universal), F5 (escopo) e F6 (condicional, roteada por PG5), ratifica **PG6 como contrato visual** e amarra o cluster ao `ready-for-school`. **Não produz** os pareceres reais (DPIA/RIPD, laudo ASES, parecer jurídico — execução, E14 §10); **não fixa** números (SLA, amostragem, % pública); **não escreve** código nem **decide** dados; **não reabre** etapa; **não altera** nenhum invariante da Constituição (apenas a implementa); e **não pode** ser lido como permissão para enfraquecer o Art. 7 (fronteira escrita à mão de PG6/§5.4) nem o Art. 6 (`approved` segue necessário, não suficiente). Próximo passo na Trilha C, sob confirmação: emitir o **Playbook v1.3** (PG6 → VIGENTE; portão de publicação pública).*
