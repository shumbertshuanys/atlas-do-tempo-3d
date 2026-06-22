# Playbook Operacional do Atlas do Tempo 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** documento de **procedimento operacional** — o **como-fazer**. É a metade que **muda com frequência** da separação ratificada em **PG7** (C1, D-C1.3). Sua contraparte é a **Constituição** (invariantes duros). O Playbook **implementa** os invariantes da Constituição; **nunca os afrouxa nem os contradiz**.
**Estatuto das cláusulas:** marcado por seção — **[VIGENTE]** (em uso agora), **[DIFERIDO]** (gancho registrado, dono e etapa indicados) ou **[DIFERIDO — substância conhecida]** (caracterizado, mas com ratificação operacional adiada). Mudança aqui é **esperada e rotineira**, sempre registrada no changelog.
**Origem:** redigido no Passo **C1.1** a partir da estrutura do **C1 §5.1**; **§4 e §5 promovidas a VIGENTE no Passo C2** (D-C2.1..8); **§7 (PG6) promovida a VIGENTE e §§8–9 acrescentadas no Passo C3** (D-C3.1..8). Sob o `registro-prototipo-e-protocolo-continuidade`, o `estado-atual-e-roteiro`, a `analise-pendencias-atuais`, a política editorial (Etapa 3.1), o portão de licença (Etapa 1.1), a UX (Etapa 10), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13) e a operação/governança (Etapa 14).
**Versão:** **v1.3** — **Data:** 2026-06-21. (v1.2 → v1.3: **PG6 sai de [DIFERIDO] e passa a [VIGENTE]** como **contrato visual de marca** — nova **§8**; acrescenta-se o **portão de publicação pública** F2/F5/F6 amarrado ao `ready-for-school` — nova **§9** — ver changelog.) **Supersede o v1.2.**

> **Nota de promoção (v1.3).** O Passo **C3** (cluster de publicação pública, famílias F2/F5/F6) fez duas coisas: **(a)** promoveu **PG6** a **[VIGENTE]** como **contrato visual normativo** (`ClaimSet` com fronteira moral/factual explícita + resumo por faixa etária; mapa esquemático rotulado por padrão; fronteira histórica/paleo nunca inventada; sobrevivência à degradação) — detalhado na nova **§8**; e **(b)** caracterizou o **portão de publicação pública** como **terceiro limiar** (a jusante do DoR e de `approved`), com F2 (universal), F5 (escopo) e F6 (condicional, roteada por PG5), amarrado ao `ready-for-school` (Etapa 14 §7.2) — detalhado na nova **§9**. O handoff do passo é `passo-c3-handoff-cluster-publicacao-publica-v1_0.md`.

> **Guarda de promoção (v1.3).** A promoção de PG6 **não** cria invariante novo: o **núcleo epistêmico** de PG6 **já é constitucional** (Constituição **Art. 7**) e **já operava** em §5.4 (não-automação da fronteira). A §8 acrescenta **apenas a camada de apresentação/marca** — a UX **apresenta** a fronteira, **nunca a gera**. Do mesmo modo, a §9 **implementa** Arts. 6/9/11/14 (não os afrouxa): `approved` segue **necessário, não suficiente** para o público.

> **Relação com a Constituição.** Sempre que uma cláusula deste Playbook tocar publicabilidade, proveniência, licença, tipagem epistêmica, exibição, qualidade ou privacidade, ela **remete** ao artigo correspondente da Constituição e **não pode** relaxá-lo. Em conflito, **a Constituição vence** e a cláusula do Playbook é corrigida.

---

## Preâmbulo — para que serve o Playbook

O Playbook é a memória viva do **método**: como abrimos e fechamos um passo, como provamos uma capacidade, como registramos o que ficou pendente. Iterá-lo rápido é uma **virtude** — é o que permite melhorar como revisamos, fatiamos e entregamos **sem risco de erodir** a Constituição. O changelog é o que impede a deriva: é o "documentar para não nos perdermos" tornado mecanismo (PG7).

**Régua de alocação (lembrete — Constituição, Art. 17):** se é número, SLA, cadência ou checklist, ou se pode melhorar sem ferir nenhuma propriedade do produto → **Playbook**. Se o produto deixa de ser o produto quando violado, ou se é propriedade epistêmica/proveniência/licença/exibição/qualidade/privacidade → **Constituição**.

---

## Seção 1 — Protocolo de continuidade: um passo por chat **[VIGENTE]**

Reconhecido formalmente no Passo C1 (D-C1.6) como **expressão operacional de PG1+PG2+PG7**, e **em vigor desde já**.

**Procedimento:**
1. **Um passo por chat.** Cada chat trata **um** passo do roteiro e é **nomeado** por ele (facilita reencontrar).
2. **Abertura padrão.** Todo chat **começa** declarando o passo e lendo o `estado-atual-e-roteiro`: *"estamos no passo X do estado-atual-e-roteiro; contexto no projeto."*
3. **Fechamento padrão.** Todo chat **termina** com um **handoff curto salvo no projeto** (o que foi decidido, o que ficou pendente, próximo passo) — no formato da Seção 2.
4. **Mesmo projeto, sempre.** Chats passados ficam pesquisáveis e o conhecimento é compartilhado. **Não criar projeto novo.** *(Esta sessão é prova viva: o `revisao-politicas-regras-v0.html` foi recuperado verbatim de um chat anterior do mesmo projeto.)*
5. **Arquivos executáveis não atravessam chats sozinhos.** Reenviar os `.html`/`.md` executáveis quando precisar editá-los — **mas** seu conteúdo é recuperável da conversa que os gerou.

*Implementa:* PG1 (cada passo fecha por evidência), PG2 (cada passo é uma fatia), PG7 (handoff = registro anti-deriva). *Precedentes vivos:* encerramentos 4Z/5Z; Passos B1, B2, C1, C1.1, C2 e C3.

---

## Seção 2 — Formato de handoff: 9 pontos + rodapé **[VIGENTE]**

Todo handoff segue a estrutura de **nove pontos** (do prompt-mestre, item 10) e fecha com o **rodapé** no estilo dos encerramentos 4Z/5Z.

**Os nove pontos:** (1) **Objetivo**; (2) **Escopo**; (3) **Diagnóstico**; (4) **Decisões principais** (numeradas, `D-XN`, com justificativa); (5) **Modelo conceitual** (sem código de aplicação); (6) **Fontes / insumos necessários** (insumos ausentes explicitados); (7) **Riscos** (`R-XN` com mitigação); (8) **Entregáveis**; (9) **Próximos passos** (por trilha, sem pular etapas).

**Rodapé (estilo 4Z/5Z):** um parágrafo que declara **sob quais etapas/passos** o documento se apoia, **o que ele NÃO faz** (limites explícitos), eventuais **insumos ausentes/pendências leves**, e o **próximo passo** na trilha.

*Implementa:* PG1/PG7. *Observação:* o rodapé "o que NÃO faz" é parte essencial — declarar limites é disciplina anti-escopo e anti-deriva.

---

## Seção 3 — Cadência de fatias e critério de "fatia fina o suficiente" **[VIGENTE]**

Operacionaliza **PG2** (Constituição, Art. 16).

**Procedimento:**
1. **Provar, não especificar.** Diante de uma capacidade incerta, a resposta padrão é **construir a fatia mais fina que a exibe ponta-a-ponta**, não escrever mais especificação.
2. **A fatia é descartável por desenho.** Serve para **ensinar o que falta** e **destravar a próxima decisão com evidência**; não precisa ser código de produção.
3. **Termina em artefato que abre e se clica** — não em documento. Um protótipo navegável, um esquema com *constraint* verificável, uma cena ponta-a-ponta, um teste que passa.
4. **Critério de "fina o suficiente":** a fatia é fina o suficiente quando **isola uma única decisão ou propriedade** e a exibe sem depender de partes ainda não construídas. Se exige construir três coisas para mostrar uma, **fatie mais**.
5. **Guarda de contrato (Constituição, Art. 16):** a fatia é *throwaway* — **não vira base nem entra no Knowledge Core**. Itens **semeados para demonstração** são **marcados** (`provenance_status`); protótipo e corpus **não divergem em silêncio**.

*Implementa:* PG1/PG2. *Precedentes:* fatia vertical de 1789; Incremento 2 (GOE/K-Pg); B1 (motor decidido com padrões reais do protótipo).

> **Articulação com a Seção 4 (v1.2).** A Seção 3 governa a fatia como **instrumento de prova** (provar uma capacidade e descartar). A Seção 4 (PG3) governa a fatia como **modo de operação** (rodar o processo real sobre os itens da fatia enquanto a cobertura cresce por fora). São compatíveis: a guarda *throwaway* do item nº 5 acima permanece soberana — operar o processo **não** promove o protótipo ao Knowledge Core.

---

## Seção 4 — PG3 e PG4: operação em escala-fatia e Definition of Ready **[VIGENTE]**

Ratificados no Passo **C2** (D-C2.1, D-C2.2, D-C2.7), convertendo os ganchos diferidos do C1 (D-C1.4) em procedimento vigente. Redação das propostas conferida verbatim na reconciliação v1.1.

### 4.1 PG3 — Operar a governança em escala-fatia antes de escalar *(estende Etapa 14)*

*Proposta (verbatim):* a E14 especifica filas, SLAs e riscos para "depois do MVP e do pipeline real"; a fricção é governança riquíssima que ainda não tocou um único item; instanciar a **menor versão real** dos invariantes da E14 sobre a fatia — *"operar 24 antes de 24 mil"*.

**Procedimento:**
1. **Modo padrão = operar a fatia.** Sobre a **fatia real de corpus** (os itens efetivamente em modelagem — 1789/4D, GOE/K-Pg/4E–4G; a ordem de grandeza dos ~24 itens da fatia), rodar a menor versão real do maquinário da Etapa 14: `readinessStatus` aplicado **de verdade**, `queueState` rastreado (§5.5), `gatingReason` anexado, e uma **fila de revisão real** com esses itens.
2. **Como uma fatia "entra em operação".** (a) seus itens estão **DoR-completos** (§4.2); (b) a fila roda sobre eles **sob os mesmos portões**; (c) a **cobertura cresce por fora** conforme novos itens DoR-completos são admitidos; (d) a **capacidade governa a admissão** (intake throttling, §5.2), **não** o afrouxamento de portão.
3. **Backlog não é bloqueio.** O **Art. 6** já oculta o não revisado: a fila limita **cobertura**, não **correção**. Um MVP pode sair só com o **núcleo publicável** enquanto a fila roda por fora (`analise-pendencias` §4).

**[NORMATIVO — guarda de contrato]:** operar a fatia **não a promove ao Knowledge Core**. PG3 opera o **processo** sobre itens reais; a fatia-protótipo segue *throwaway* (Constituição **Art. 16**/PG2); só vira canônico o item que passa pela revisão **via pipeline** — **nunca** por ter aparecido na fatia. PG3 não pode ser lido como permissão para enfraquecer PG2/Art. 16.

### 4.2 PG4 — Definition of Ready (DoR): o contrato de entrada *(estende Etapas 2 + 3.1)*

*Proposta (verbatim):* claim-first é regra, mas o **contrato mínimo** de entrada em revisão não estava fixado como porta; um **DoR** — campos mínimos obrigatórios — que um claim precisa cumprir para entrar na fila; **sem DoR, não entra**. É a Definition of **Ready** (entrada); complementa o "pronto = evidência" de **PG1**, que é a Definition of **Done** (saída).

**Procedimento — os 8 campos obrigatórios para admissão (`queueState → queued`).** Todos devem **existir e estar tipados** (estado `PENDENTE_*` *declarado* é admissível; **silêncio não é**):
1. **Claim tipado** — `claimType` (taxonomia de 10 tipos) + `confidenceLevel` + `evidenceLevel` + `UncertaintyProfile` presentes *(Art. 7; claim-first da Etapa 2)*.
2. **Fonte identificada** — ao menos um `Source`/`provenanceRef` (aresta afirmativa órfã é **impossível de inserir** — Art. 7/Passo B2). Confirmação por asset (`perAssetConfirmed`) pode seguir `PENDENTE`, mas a fonte tem de estar **identificada**.
3. **Sensibilidade pré-classificada (PG5)** — tag aplicada **na modelagem**: `público` / `mediado` / `legal-review` (Leis 10.639/2003 e 11.645/2008). Define os papéis exigidos e o `pending` por padrão *(ver §7)*.
4. **Plano de exposição por faixa etária** — quais níveis mostram/ocultam/avisam (redação final pode ser pendente; **a forma se adapta, o fato não** — Art. 8).
5. **`ClaimSet` com fronteira, se controverso** — se a tag sinaliza controvérsia legítima, existe um `ClaimSet` com a fronteira "sem equivalência" **escrita à mão** (Art. 7; nunca automatizada — §5.4; apresentada conforme §8.1).
6. **Papel(éis) de revisão designado(s)** — quais dos 8 papéis (§5.3) precisam aprovar, derivado de **camada + sensibilidade**.
7. **Tempo/espaço declarados** — `timePrecision`/`timeUncertainty` e `geometryStatus` declarados (podem ser `PENDENTE_DATA`/`PENDENTE_GEOMETRIA`, mas **declarados** — nunca se inventa precisão; Art. 7/9).
8. **Triagem de licença iniciada** — `licenseRiskLevel` (0–5) pré-classificado e `storagePartition` provisória (`core`/`media`/`isolated`/`blocked`).

**[NORMATIVO]:** o DoR exige que o campo **exista e seja tipado**, **não** que esteja **finalizado** — finalização é a Definition of **Done** (PG1). **Sem DoR, não há admissão:** o item permanece a montante, na **modelagem** — não vira item-fantasma de backlog. *Implementa:* PG4 como porta de entrada; PG1 como porta de saída.

> **Articulação com a Seção 9 (v1.3).** O DoR (porta de **entrada**) e `approved` (porta para **fato exibível**, §5) **não bastam** para a **publicação pública**: esta exige o **cluster** da §9 (F2 sempre; F5 de escopo; F6 conforme PG5). Os campos do DoR que ficam `PENDENTE` (ex.: `perAssetConfirmed` no campo nº 2) são **exatamente** os que a §9 fecha antes de publicar.

---

## Seção 5 — Fila de revisão como processo **[VIGENTE]**

Ratificada no Passo **C2** (D-C2.4/5/6). A fila deixa de ser **backlog sem dono nem cadência** e passa a **processo operante** — o **caminho crítico de cobertura** (`analise-pendencias` §5, F1). Volume conhecido no conteúdo: **29 `PENDENTE_REVISAO_HUMANA` + 11 `PENDENTE_CLAIMSET`** (lote-piloto 4B + cenas).

### 5.1 Dono — papel-condutor, com não-poderes explícitos

O **dono da fila** é uma **função-condutora** (papel, não pessoa — Etapa 3.1 §9.1), que mapeia a `operationsLead`/`scaleCoordinator` (Etapa 14 §3) quando houver equipe; em escala-fatia, o mesmo operador sob o chapéu de governança.
- **Pode:** rotear o item à fila de competência correta; sequenciar o trabalho; rastrear `queueState`; anexar `gatingReason`; **pausar a admissão** quando a capacidade não comporta revisão com profundidade.
- **Não pode:** decidir **mérito fora de sua competência**; **conceder/dispensar** qualquer portão (`qaGateResult` **não tem** `waived`/`override`); **publicar** item com qualquer papel aplicável não aprovado; **automatizar** a fronteira do `ClaimSet` (§5.4).

### 5.2 Cadência — estrutural, sem números

1. **Puxada (*pull-based*).** Item só entra **DoR-completo** (§4.2); o que não está pronto permanece na modelagem.
2. **Opera a fatia primeiro.** A fila roda sobre os itens da fatia (PG3, §4.1) antes de escalar — prova o processo em pequena escala.
3. **Válvula de segurança = intake throttling (Etapa 14 §3.3).** Se a capacidade de revisão é insuficiente, a **admissão de novos itens é pausada** — **nunca** se aprova em lote nem se rebaixa a revisão; estourar um alvo de tempo **escala** (papel/função superior) e, persistindo, **pausa a admissão** do lote afetado.

**[NORMATIVO]:** os **números** — SLAs por fila, percentuais de amostragem de auditoria, prazos — permanecem **[PENDÊNCIA]** de execução (E13/E14), calibrados por capacidade (régua do Art. 17). Defini-los aqui agora seria escopo de execução, não de governança.

### 5.3 Papéis de revisão — pré-requisito de publicação

Os **8 papéis** da política editorial (Etapa 3.1 §9), mapeados às filas operacionais (Etapa 14 §4.2) e à competência de mérito (Etapa 13 §3). Um item de tema sensível **não** sai da `publication-queue` sem a aprovação registrada do papel competente.

| Papel (E3.1 §9) | Fila operacional (E14 §4.2) | Pode aprovar (E13 §3) |
|---|---|---|
| Científica | `scientific-review-queue` | mérito científico (camadas científicas) |
| Historiográfica | `historical-review-queue` | mérito histórico/historiográfico |
| Pedagógica/faixa | (no fluxo editorial) | profundidade/linguagem/exposição por faixa |
| Editorial (sensível/controvérsia) | `editorial-review-queue` | `consensusStatus`/`editorialNote`/mediação |
| Jurídica/LGPD | `legal-review-queue` *(default: não publica)* | `legal-review`/licença/risco vivo |
| Licença | `license-queue` | `licenseRiskLevel`/`storagePartition` |
| Geotemporal | `geotemporal-review-queue` | tempo/espaço/datum/geometria |
| Acessibilidade | `accessibility-review-queue` | equivalente textual/e-MAG/WCAG/LBI |
| Vieses | (transversal ao editorial) | eurocentrismo/estereótipo/falsa equivalência |

Consolidação e publicação: `publication-queue`, **só após todas** as revisões aplicáveis.

### 5.4 Não-automação da fronteira

A fronteira **"sem equivalência"** de cada `ClaimSet` é **escrita à mão**; a fila **roteia e rastreia**, ela **não gera** a fronteira. É o *moat* epistêmico (PG6 / Constituição Art. 7) — confirmado na fatia. Nenhum ganho de cadência justifica automatizá-la. *(A apresentação dessa fronteira na UX é regida pelo contrato visual da §8; apresentar não é gerar.)*

### 5.5 Máquina de estados da fila

Instancia `queueState` (Etapa 14 §4.1) sobre a fatia:

```
[modelagem]
   │  (item NÃO DoR-completo permanece aqui; não é backlog, é trabalho a montante)
   ▼  DoR-completo (§4.2)? ── não ──► volta à modelagem
   │           (sim)
   ▼
queued ──► in-progress ──► [revisões por papel competente, conforme sensibilidade — §5.3]
   │            │              ├─ científica / historiográfica / editorial
   │            │              ├─ jurídica (default: NÃO publica) / geotemporal
   │            │              └─ acessibilidade / licença / vieses
   │            │
   │            ├─ dúvida/competência/risco ──► escalated ──► papel/função superior
   │            ├─ reprova ──────────────────► returned (= needs-rework no pipeline)
   │            └─ teste/portão falha ───────► blocked (rebaixamento automático; versionado)
   │
   ▼  todas as revisões aplicáveis aprovadas
publication-queue ──► done  ⇒  reviewStatus = approved  ⇒  EXIBÍVEL
```

**[NORMATIVO]:** nada nesta seção pode contornar o **invariante de exibição** (Constituição, **Art. 6**): item não revisado **não** vira fato por pressão de fila, em nenhuma vista, índice, exportação ou na simultaneidade. Vale o **Art. 13** (QA bloqueia; escala não reduz revisão): capacidade insuficiente **pausa a admissão**, não rebaixa a revisão. `returned`/`blocked` operam por **depreciação + correção versionada** (**Art. 12**); **nada é apagado**.

> **Articulação com a Seção 9 (v1.3).** `reviewStatus = approved` torna o item **exibível** (inclusive na fatia e em vistas internas); é **condição necessária, não suficiente** para a **publicação pública** — esta acrescenta o cluster F2/F5/F6 da §9. *"`approved` ≠ publicamente publicável"* (`analise-pendencias` §2).

---

## Seção 6 — Recadência por fonte viva, SLAs e amostragem de auditoria **[DIFERIDO → quando operar, E13/E14]**

Procedimentos finos de operação, definidos **quando o pipeline operar** (Etapas 13/14). Registrados aqui como ganchos:
1. **Recheck de fonte viva** — cadência por classe de fonte (frequente para fontes vivas; periódica para estáveis); mudança de fonte **cria nova versão de `Source` + novo `DatasetSnapshot` imutável**; **jamais** atualização silenciosa (implementa Constituição, Art. 12).
2. **SLAs por fila** — prazos de atendimento por papel/fila; números são **[PENDÊNCIA]** de execução *(cadência estrutural já vigente em §5.2; aqui ficam apenas os números)*.
3. **Amostragem de auditoria** — limiares de amostragem de revisões e auditorias periódicas; trilha de decisão grava ator, data e `gatingReason`.
4. **Rollback versionado** — opera por **depreciação + restauração** da versão anterior; **nada é apagado** (implementa Constituição, Art. 12).

**[NORMATIVO]:** `qaGateResult` tem **dois** valores (`pass`/`fail`) — **sem** `waived`/`override`. QA **bloqueia**, não sugere. Nenhum SLA ou cadência destrava portão. Estes são os **mecanismos** do invariante constitucional **Art. 13**; o invariante é soberano, os números são do Playbook.

---

## Seção 7 — PG5 e PG6 **[PG5 APLICADO → §4 · PG6 APLICADO → §8 (contrato visual)]**

**Correção v1.1:** o v1.0 marcara PG5/PG6 como "a caracterizar" por ausência do texto; a recuperação verbatim os **caracterizou**. **Atualização v1.2:** **PG5 foi aplicado** (Passo C2, D-C2.3). **Atualização v1.3:** **PG6 foi aplicado** (Passo C3, D-C3.6) como **contrato visual de marca** — detalhado na **§8**.

- **PG5 — Pré-classificar sensibilidade na modelagem, não na revisão** *(estende Etapas 2 + 3.1)*. **Hoje:** a sensibilidade (Leis 10.639/11.645) era tratada **na revisão**; uma proporção grande dos itens caía em `pending` e se descobria um a um. **Fricção:** o *split* público/mediado de uma cena só era conhecido **depois** de construí-la. **Proposta:** uma **taxonomia de sensibilidade aplicada na hora da modelagem** → backlog de revisão e proporção pública **previsíveis antes do build**. **Ganho:** "descoberta" vira "planejamento". **✓ APLICADO em C2 (D-C2.3)** como **campo nº 3 do DoR** (§4.2): a sensibilidade pré-classificada na modelagem é **porta de entrada** da fila — define papéis exigidos e `pending` por padrão. **Uso ampliado em C3 (§9.5):** PG5 é também o **roteador** das condições do cluster de publicação pública e a base da **estimativa de *split*** antes do build.
- **PG6 — ClaimSet e mapa esquemático viram contratos normativos de marca** *(estende Etapas 3.1 + 10)*. **Hoje:** "sem equivalência" e "mapa esquemático" existem como prática e descrição conceitual. **Fricção:** ambos são **decisões de produto**, não detalhes — a fronteira escrita à mão do `ClaimSet` é o *moat*; o mapa esquemático é epistemicamente **superior** a fronteiras inventadas. **Proposta:** elevá-los a **regra normativa com contrato visual** — `ClaimSet` sempre com fronteira moral/factual explícita + resumo por faixa etária; mapa esquemático rotulado por padrão, fronteira histórica **nunca inventada**. **Ganho:** o diferencial deixa de ser implícito e vira padrão obrigatório. **✓ APLICADO em C3 (D-C3.6)** — contrato visual detalhado na **§8**, amarrado às entidades da Etapa 10.

**[NORMATIVO]:** o **núcleo epistêmico** de PG6 (ClaimSet sempre com fronteira; nunca inventar geometria/fronteira) **já é constitucional** — Constituição, Art. 7 — e **já operante** na fila (§5.4). O que a §8 adiciona é a camada de **contrato visual / padrão-de-marca** (como a fronteira e o mapa se apresentam na UX). PG6 não pode, em hipótese alguma, ser lido como permissão para enfraquecer o Art. 7.

---

## Seção 8 — Contrato visual de marca (PG6) **[VIGENTE]**

Ratificada no Passo **C3** (D-C3.6). Promove **PG6** de diferido a **vigente** como **contrato visual normativo**, amarrado às entidades de apresentação da **Etapa 10**. **Não** é invariante novo: **implementa** os Arts. 7 e 12 da Constituição e o §5.4 deste Playbook. A regra-mãe: **a UX apresenta a honestidade epistêmica; nunca a gera nem a esconde.**

### 8.1 Contrato visual do `ClaimSet`

Toda controvérsia legítima (e somente ela) apresenta-se como `ClaimSet`, com:
1. **Fronteira moral/factual explícita.** A fronteira *"sem equivalência"* — **escrita à mão** (§5.4; Art. 7) — é **mostrada**, não diluída. Negacionismo/desinformação recebem **rótulo de rejeição** e ficam **fora do par** de claims (`EquivalenceWarningNotice`, Etapa 10 §11.4); a UI **nunca** cria **falsa equivalência visual**.
2. **Pesos assimétricos visíveis.** `weightedClaimSets` aparece com confiança/peso por lado (ex.: impacto ≫ Deccan no K-Pg); sem simetria visual entre lados de peso desigual (Etapa 10 §12.3).
3. **Resumo por faixa etária.** Acompanha o `ClaimSet` um **resumo adaptado por faixa** — a **forma** se adapta (linguagem/profundidade), o **fato/`Claim` não** (Art. 8). O resumo **não** substitui a fronteira manual; é apresentação da mesma fronteira.
4. **Incerteza como faixa, nunca "omitir".** `uncertaintyDisplayPolicy ∈ {sempreRotular, rótuloCompacto, aparatoCompleto}` — **jamais "omitir"** (Etapa 10 §11.1). A incerteza aparece como **faixa/margem**, com **redundância não-cromática** (forma + texto + posição, não só cor). No modo estudante o rótulo é **compacto, mas presente**; no modo professor, **aparato completo** (`UncertaintyLegend`/`EpistemicLabelView`).

### 8.2 Contrato visual do mapa esquemático

1. **Rotulado por padrão.** Todo mapa/globo de tempo profundo ou de fronteiras é apresentado com **rótulo explícito de reconstrução modelada** (não "foto", não certeza).
2. **Fronteira histórica/paleo nunca inventada.** Onde a geometria não está validada, o **mapa esquemático rotulado** é a apresentação correta — **superior** a fronteiras inventadas. A geometria pendente (F3) limita **fidelidade**, **não correção** (`analise-pendencias` §3/§5.3); o esquemático rotulado é **padrão público**, não dívida.
3. **Paleoposição ≠ localidade atual.** `paleoPositionPolicy` distingue **localidade atual** de **paleoposição**; a `ModernCorrespondence` liga o lugar antigo ao atual **sem** sugerir anacronismo (ex.: "México" não existia em 66 Ma) — `AnachronismNotice` sempre presente (Etapa 10 §7.1/§12.3). A UI **nunca** suprime o aviso de anacronismo.
4. **Fronteira disputada como tema.** Fronteira territorial em disputa é apresentada como `ClaimSet` cartográfico ("ver perspectivas"), **nunca** como única verdade; SA/ODbL isolada (Etapa 3.1 §7; Etapa 11 §9.7).

### 8.3 Sobrevivência à degradação

**[NORMATIVO]** o contrato visual **sobrevive a todos os degraus** da `ViewDegradationLadder` (3D → 2D → estático → offline → projetor): rótulos de tipo/confiança/incerteza/atribuição, fronteira do `ClaimSet`, aviso de anacronismo e equivalente textual **acompanham o conteúdo em qualquer modo** (Constituição Art. 12; Etapa 10 §7.2; Etapa 11 §11.8–11.10). Nenhuma vista "desliga" a honestidade epistêmica por desempenho ou estética.

### 8.4 Guarda normativa da seção

**[NORMATIVO]** a §8 **implementa** Arts. 7 e 12 e o §5.4 — **não os afrouxa**. A UX **apresenta** a fronteira (§5.4) e os rótulos (Art. 7), **nunca os gera**; o resumo por faixa (§8.1.3) **não** dilui a fronteira manual nem altera o `Claim` (Art. 8). Qualquer vista que esconda incerteza, remova rótulo epistêmico, crie falsa equivalência visual, exiba reconstrução como foto/fato, invente fronteira/paleomapa, ou suprima o aviso de anacronismo **viola** o contrato — e, sob ele, o artigo constitucional correspondente. **PG6/§8 não pode ser lido como permissão para enfraquecer o Art. 7.**

---

## Seção 9 — Portão de publicação pública (F2/F5/F6) **[VIGENTE]**

Ratificada no Passo **C3** (D-C3.1..5, D-C3.7). Caracteriza o **terceiro limiar** do conteúdo — a **publicabilidade pública** — distinto do **DoR** (entrada, §4.2) e de `approved`/**Art. 6** (fato exibível, §5). **Não** é invariante novo: **implementa** os Arts. 6, 9, 11 e 14. Os **números** (SLA, amostragem, limiar de proporção pública) e os **pareceres reais** (DPIA/RIPD, laudo ASES, parecer jurídico, evidência de piloto) seguem **[PENDÊNCIA]** de execução (E13/E14 §10).

### 9.1 Os três portões — `approved` ≠ publicamente publicável

```
DoR (§4.2)            Art. 6 / approved (§5)        Cluster público (§9)            ready-for-school (E14 §7.2)
porta de ENTRADA  →   porta p/ FATO EXIBÍVEL    →   condição de PUBLICAÇÃO      →   portão de ESCOPO
8 campos tipados      todas as revisões              F2 (sempre) + F5 (escopo)       agrega itens + auditorias
                      aplicáveis aprovadas           + F6 (se sensível/vivo)         de escopo (ASES, DPIA,
                      = EXIBÍVEL (inclui fatia)      por item/asset                   licença, sensível, nota
                                                     = PUBLICAMENTE PUBLICÁVEL        anti-homologação)
```

**[NORMATIVO]** `publiclyPublishable` exige, **cumulativamente**: (i) `reviewStatus = approved` (§5); **e** (ii) o **cluster público confirmado por item/asset** (§9.2–§9.4, conforme a sensibilidade PG5). `approved` permanece **necessário, não suficiente** para o público (Art. 6 soberano).

### 9.2 F2 — portão universal (fonte + licença por asset)

Todo item/asset público, além de `approved`:
1. **Fonte confirmada por asset** — `perAssetConfirmed = true` (P07; encerra `PENDENTE_CONFIRMACAO_FONTE`), **não** apenas *identificada* como exige o DoR (campo nº 2). *(Achado: mesmo os ~20 itens publicáveis de 1789 ainda têm fonte pendente por asset — `analise-pendencias` §2.)*
2. **Licença resolvida por asset** — `licenseRiskLevel`/`license` confirmados, `storagePartition` definitiva e `exportPolicy` coerente (Etapa 11 §9.4; código **CONF** da Etapa 1.1; Risco 2 → confirmar antes de servir, §9.5 da E11).
3. **Expressão NC nunca pública** — só o **fato re-derivado de fonte livre** (Etapa 11 §9.6; Etapa 1.1 caso 2).
4. **SA/ODbL só isolada** — camada isolada, atribuição e ShareAlike honrados; exportação **impedida** (não relaxada) quando o formato não puder honrar o ShareAlike (Etapa 11 §9.7).

*Implementa:* Arts. 5 (índice ≠ autoridade), 9 (na dúvida → bloqueio), 10 (proveniência como FK), 11 (isolamento; licença governa expressão, não o fato). *Guardião técnico:* `LicenseComplianceService` (Etapa 11 §3.4).

### 9.3 F5 — fundação escolar (escopo)

Para **uso escolar público** de um escopo (verificado como **auditoria de escopo** no `ready-for-school`):
1. **Piso de acessibilidade** e-MAG/WCAG/LBI — equivalente textual de todo visual, navegação por teclado, foco visível, contraste, **redundância não-cromática**, movimento reduzido — **em todos os degraus**, inclusive offline e projetor (Etapa 11 §11.8–11.9; Etapa 10 §11.5).
2. **Degradação graciosa** 3D→2D→estático→offline→projetor **preservando o piso epistêmico** (Art. 12; Etapa 11 §11.10; §8.3 deste Playbook).
3. **Pacote offline** que **não relaxa** licença/publicabilidade/mediação/papel (Etapa 11 §9.8).
4. **Minimização máxima de dados de menores** — sem PII de aluno no núcleo; analytics agregado sem PII; dado de aluno jamais treina modelo nem gera fato (Art. 14; Etapa 11 §4.9).

**[NORMATIVO]** o **laudo ASES** e a **DPIA/RIPD** são **execução** (E14 §10.2/§10.3); o portão os **exige como insumo** no `ready-for-school`, **não os produz**.

### 9.4 F6 — jurídico/sensível vivo (condicional, roteado por PG5)

Itens que tocam **pessoas vivas/identificáveis**, **BR-07** (ditadura) e congêneres entram como **`reviewStatus = legal-review` por padrão** — e, por Art. 6, **não existem como fato para o público** até liberação. Para publicá-los:
1. **`legal-review` aprovado** pelo `legalReviewer` *(que não é, e o documento não substitui, parecer de advogado)*.
2. **Auditoria de conteúdo sensível limpa** (E14 §7.2).
3. **Fato × cenário × previsão separados** (Art. 7 — `claimType` distinto; `UncertaintyProfile` como faixa; ex.: clima moderno com cenário/modelo rotulado).
4. **ECA/LGPD** respeitados (Art. 14). Na dúvida, **restringe-se, rotula-se ou exige-se mediação** (Etapa 3.1 §9.2).

**[NORMATIVO]** a **DPIA/RIPD** e o **parecer jurídico** reais são E14 §10.3 (execução), não produto da §9.

### 9.5 PG5 como roteador e estimativa de *split* antes do build

A etiqueta PG5 (DoR campo nº 3) **decide as condições do cluster** por item e torna o *split* **previsível antes de construir a cena**:

```
etiqueta PG5            condições do cluster público
─────────────────       ───────────────────────────────────────────────────────
público          → F2  [+ F5 de escopo]
mediado          → F2  + MediationControl + revisão editorial  (não vai ao aluno sem mediação — Etapa 10 §11.3)
legal-review     → F2  + F6 (legalReviewer + DPIA + auditoria sensível)   — default NÃO público
```

Contar os itens por etiqueta e cruzar com o estado F2 dá a **proporção pública estimada da cena antes do build** — *"descoberta vira planejamento"* (D-C2.3/D-C3.7).

**[NORMATIVO]** a proporção é **estimativa de planejamento**, **não** alvo nem SLA (Art. 17); o limiar de "% pública aceitável" é **[PENDÊNCIA]** de execução. Art. 6 segue soberano: `mediado` só chega ao aluno **sob mediação**; `legal-review` **não existe como fato** ao público até liberação.

### 9.6 Acoplamento item → escopo (`ready-for-school`, E14 §7.2)

O **cluster** (§9.2–§9.4) é a **pré-condição por item/asset**. O **`ready-for-school`** é o **portão de escopo** que **agrega** esses itens e acrescenta as **auditorias de escopo**: P1 ao menos `partially-populated`, **laudo ASES aprovado**, **DPIA/RIPD revisada**, **auditoria de licença/exportação limpa**, **auditoria de conteúdo sensível limpa**, `T-PROF×ALUNO`, **nota anti-homologação** no viewer e no export, e evidência de piloto positiva. O salto **fatia → MVP público** mede-se por esse *gate* objetivo, **sem** fixar números aqui e **sem** produzir as auditorias.

### 9.7 Guarda normativa da seção

**[NORMATIVO]** a §9 **implementa** Arts. 6/9/11/14 — **não os afrouxa**. Em particular: (a) `approved` é necessário, **não suficiente** (Art. 6 soberano); (b) item `mediado`/`legal-review` **não vaza** ao público/aluno como fato (R-C3.7); (c) expressão NC/SA **não** sai ao público/export indevidamente (R-C3.8; Etapa 11 §9.6/§9.7); (d) a **nota anti-homologação** nunca é perdida no público/export (E14 §7.2/§10; Etapa 10 invariante 13). Procurement/prazo/pressão comercial **nunca** destravam o portão (E14 §10.4/§15.10).

---

## Changelog

| Versão | Data | O que mudou | Por quê | Documento |
|---|---|---|---|---|
| **v1.3** | 2026-06-21 | **Nova §9 — Portão de publicação pública [VIGENTE]:** caracteriza o **terceiro limiar** (`approved` ≠ publicamente publicável), com **F2** (universal — fonte + licença por asset), **F5** (escopo — acessibilidade/offline/menores) e **F6** (condicional — jurídico/sensível vivo), **PG5 como roteador** e estimativa de *split* antes do build, e o **acoplamento item → escopo** ao `ready-for-school` (E14 §7.2). Números e pareceres reais permanecem **[PENDÊNCIA]** de execução. **§4.2 e §5.5** ganham nota de articulação com a §9. | Executar o Passo **C3** (cluster de publicação pública, F2/F5/F6): caracterizar, em governança, o que torna um item/cena publicamente publicável, amarrando o maquinário já existente (Etapa 1.1, Etapa 11 §3.4/§9/§11.8–11.10, Etapa 14 §7.2/§10) sem fixar números nem afrouxar invariante. | Playbook |
| **v1.3** | 2026-06-21 | **§7 atualizada + nova §8 — Contrato visual de marca (PG6) [VIGENTE]:** **PG6** passa de **[DIFERIDO]** a **APLICADO** como contrato visual — `ClaimSet` com fronteira moral/factual explícita + resumo por faixa etária + pesos assimétricos + incerteza como faixa (§8.1); mapa esquemático rotulado por padrão, fronteira/paleo nunca inventada, paleoposição ≠ atual (§8.2); sobrevivência do contrato à degradação 3D→2D→estático→offline→projetor (§8.3); guarda normativa de que a UX **apresenta**, nunca **gera** (§8.4). Amarrado às entidades da Etapa 10. | Promover PG6 a vigente como padrão-de-marca, elevando o diferencial de implícito a obrigatório, sem criar invariante novo: o núcleo epistêmico já é Art. 7 + §5.4. | Playbook |
| **v1.2** | 2026-06-21 | **§4 promovida a [VIGENTE]:** PG3 (operação em escala-fatia — modo padrão, "como uma fatia entra em operação", guarda de contrato contra promoção ao KC) e PG4 (DoR — os **8 campos obrigatórios** de admissão; "sem DoR, não há admissão") deixam de ser ganchos diferidos e passam a procedimento operante. **§5 promovida a [VIGENTE]:** fila de revisão vira processo — **dono** com não-poderes (§5.1), **cadência estrutural** com intake throttling e números deixados [PENDÊNCIA] (§5.2), **8 papéis** mapeados a filas/competência (§5.3), **não-automação da fronteira** (§5.4) e **máquina de estados** (§5.5). **§3** ganha nota de articulação com §4 (fatia-prova × fatia-operação). | Executar o Passo **C2** (fila de revisão como processo, F1): converter os ganchos diferidos do C1 (D-C1.4) em governança operante, amarrando o maquinário já existente da E14 (§3.3/§4) e os papéis da E3.1 §9 / E13 §3, sem fixar números nem afrouxar invariante. | Playbook |
| **v1.2** | 2026-06-21 | **§7 atualizada:** **PG5** passa de "[DIFERIDO — substância conhecida]" a **APLICADO** (campo nº 3 do DoR, §4.2). **PG6** segue diferido (→ C3/Etapa 10), com nota de que seu **núcleo de não-automação** já está operante em §5.4. Cabeçalho, origem e estatuto atualizados; supersede o v1.1. | Refletir a aplicação de PG5 e a operação parcial do núcleo de PG6 decididas em C2. | Playbook |
| **v1.1** | 2026-06-21 | **§7 reescrita:** PG5 e PG6 deixam de ser "[A CARACTERIZAR]" e passam a **caracterizados** (redação verbatim recuperada), reclassificados **[DIFERIDO — substância conhecida]**; PG6 cruza-referência a Constituição Art. 7. **§4 afinada:** PG3 ("operar 24 antes de 24 mil") e PG4 ("sem DoR, não entra") ganham a redação verbatim. **Referências cruzadas atualizadas** à Constituição v1.1. **§1 e §3** registram a recuperação do arquivo como prova viva do protocolo. | A recuperação verbatim do `revisao-politicas-regras-v0.html` corrigiu o engano do v1.0 e fechou a pendência. | Playbook |
| **v1.1** | 2026-06-21 | **Pendência resolvida:** reconciliação verbatim de PG1–PG7 **fechada**. Resíduo não-normativo (CSS, cabeçalho do HTML, linha "Ganho" de PG7) não recuperado e sem efeito sobre o procedimento. | Encerrar honestamente a pendência do v1.0. | Playbook |
| **v1.0** | 2026-06-21 | Criação do Playbook como documento próprio, a partir da estrutura do C1 §5.1 (§§1–7: protocolo um-passo-por-chat, formato de handoff, cadência de fatias, PG3/PG4 diferidos, fila de revisão, recadência de fonte viva, PG5/PG6). | Executar o Passo C1.1. | Playbook |

---

*Documento de governança, versão **v1.3**, promovido no Passo **C3** sob a Constituição v1.1 (Arts. 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17), o portão de licença (Etapa 1.1), a política editorial (Etapa 3.1 §7/§9), a UX (Etapa 10), a arquitetura técnica (Etapa 11 §3.4/§9/§11.8–11.10), a operação/governança (Etapa 14 §7.2/§10) e os Passos B2, C1, C1.1 e C2. Promove **PG6** a [VIGENTE] como **contrato visual de marca** (nova §8) e acrescenta o **portão de publicação pública** F2/F5/F6 amarrado ao `ready-for-school` (nova §9), preservando §1–§7 e a numeração existente. Não altera nenhum invariante da Constituição (apenas a implementa), não reabre nenhuma etapa, não fixa números de SLA/amostragem/proporção pública (seguem [PENDÊNCIA] de E13/E14), não produz os pareceres reais (DPIA/RIPD, laudo ASES, parecer jurídico — execução, E14 §10), não escreve código e não decide dados. Guarda crítica: a §8 **apresenta** a fronteira, nunca a **gera** (Art. 7/§5.4 soberanos); a §9 mantém `approved` como **necessário, não suficiente** para o público (Art. 6 soberano). Supersede o v1.2. Próximo passo na Trilha C, quando solicitado: conforme o `estado-atual-e-roteiro` (Trilhas A/B correm em paralelo; o cluster gateia o caminho público, não a fatia nem a decisão de motor).*
