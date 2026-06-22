# Passo C2 — Fila de revisão como processo (pendência F1)

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** handoff do Passo **C2** da Trilha C (governança). Ratifica **PG3** e **PG4** no nível operacional, **aplica PG5** como porta de entrada, e converte a **fila de revisão** de *backlog* em **processo** — preenchendo as **Seções 4 e 5 do Playbook** (hoje [DIFERIDO → C2]). Segue o protocolo um-passo-por-chat (Playbook §1) e o formato de 9 pontos + rodapé (Playbook §2).
**Abertura padrão:** estamos no passo **C2** do `estado-atual-e-roteiro`; contexto no projeto.
**Data:** 2026-06-21.

---

## 1. Objetivo

Transformar a **fila de revisão humana** — identificada como o **caminho crítico de cobertura** (`analise-pendencias` §5, família **F1**) — de um *backlog sem dono nem cadência* em um **processo operante**, sem afrouxar nenhum invariante. Concretamente: (a) **ratificar PG3** (operar a governança em escala-fatia antes de escalar), (b) **ratificar PG4** (um *Definition of Ready* para o item publicável), (c) **aplicar PG5** (pré-classificar sensibilidade na modelagem) como campo de entrada, e (d) **definir dono, cadência e papéis** da fila como pré-requisito de publicação.

Resultado pretendido: as **Seções 4 e 5 do Playbook** saem de `[DIFERIDO]` e passam a `[VIGENTE]`.

## 2. Escopo

**Dentro:**
- Definição operacional de **PG3** (como uma fatia "entra em operação" sem que o backlog vire bloqueio).
- O **contrato de entrada** PG4 — o *Definition of Ready* (DoR) com seus campos mínimos obrigatórios.
- A **graduação de PG5** de "caracterizado/diferido" para **aplicado como porta** (campo do DoR).
- A **fila de revisão como processo**: dono (papel + não-poderes), cadência (estrutural), os 8 papéis de revisão como pré-requisito, e a não-automação da fronteira.
- A **máquina de estados** da fila (modelo conceitual, sem código).

**Fora (limites explícitos):**
- **Números** de SLA, percentuais de amostragem de auditoria, prazos por fila — seguem `[PENDÊNCIA]` de execução (E13/E14).
- Código, protótipo, escolha de stack, decisão de dados.
- Reabertura de qualquer etapa; alteração de qualquer invariante da Constituição (C2 **implementa**, não emenda).
- Caracterização do **contrato visual** de PG6 (camada de UX) — fica para **C3** / Etapa 10.

## 3. Diagnóstico

O que o corpus e a fatia ensinaram, e que torna C2 executável **agora**:

1. **A fila é o caminho crítico de cobertura, não de correção.** O **invariante de exibição** (Constituição **Art. 6**) já oculta todo item não revisado: enquanto `reviewStatus ∈ {pending, legal-review, rejected}`, o item **não existe como fato** em nenhuma vista, índice, exportação ou na simultaneidade. Logo, o backlog limita **quanto** o produto cobre, nunca **se** o que aparece está correto (`analise-pendencias` §4: F1 é △ no MVP, ✗ só na escala).
2. **O backlog tem tamanho conhecido.** No conteúdo: **29 `PENDENTE_REVISAO_HUMANA` + 11 `PENDENTE_CLAIMSET`** (lote-piloto 4B + cenas). Famílias do backlog: **P01** (científica das cenas profundas, ~18 itens K-Pg/GOE), **P02** (editorial dos sensíveis), **P14** (colonização, escravidão, povos indígenas, ditadura, raça, evolução humana), **P15** (clima moderno).
3. **A máquina de estados já existe — falta operá-la.** A Etapa 14 (§4) já define `readinessStatus`, `queueState`, `qaGateResult` (sem `waived`/`override`), as **12 filas operacionais** (§4.2) e a regra de **intake throttling** (§3.3: capacidade insuficiente **pausa a admissão**, nunca aprova em lote). Os **8 papéis de revisão** já estão na política editorial (Etapa 3.1 §9) e mapeados aos papéis de ingestão (Etapa 13 §3). C2 não inventa esse maquinário: **instancia a menor versão real dele**.
4. **A fronteira do `ClaimSet` é manual por desenho.** A fatia confirmou: a fronteira "sem equivalência" de cada controvérsia é **escrita à mão** — é o *moat* epistêmico (PG6/Art. 7). A fila **roteia e rastreia**; ela **não gera** a fronteira.
5. **PG5 estava caracterizado mas diferido.** A reconciliação verbatim (C1.1 v1.1) fixou sua substância: **pré-classificar sensibilidade na hora da modelagem**, não na revisão. C2 é o momento de **aplicá-lo** — é exatamente o campo que torna o backlog de revisão e o *split* público/mediado **previsíveis antes do build**.

Conclusão do diagnóstico: a fila não precisa de tecnologia nova nem de decisão de dados; precisa de **dono, contrato de entrada e cadência** amarrados aos invariantes que já existem.

## 4. Decisões principais

- **D-C2.1 — Ratificar PG3 (operar em escala-fatia). [§4 PG3 → VIGENTE]**
  O **modo padrão de operação** passa a ser instanciar a **menor versão real** dos invariantes da Etapa 14 sobre a **fatia real de corpus** (os itens efetivamente em modelagem — 1789/4D, GOE/K-Pg/4E-4G; a ordem de grandeza dos ~24 itens da fatia): `readinessStatus` aplicado **de verdade**, `queueState` rastreado, `gatingReason` anexado, e uma **fila de revisão real** com esses itens. Lema operacional: *"operar 24 antes de operar 24 mil"*. O backlog **não vira bloqueio** porque o **Art. 6** já oculta o não revisado — a fila limita **cobertura**, não **correção**, e um MVP pode sair só com o núcleo publicável enquanto a fila roda por fora.
  *Justificativa:* prova que a governança prende a realidade em pequena escala **antes** do custo de escalar (`analise-pendencias` §5.1; PG3 verbatim).
  *Guarda crítica (não confundir com PG2):* PG3 opera o **processo** sobre itens reais; **não promove** o protótipo descartável nem seu conteúdo semeado ao Knowledge Core. A fatia-protótipo **continua *throwaway*** (Constituição **Art. 16**); só vira canônico o item que **passa pela revisão via pipeline** — nunca por ter aparecido na fatia.

- **D-C2.2 — Ratificar PG4 (Definition of Ready). [§4 PG4 → VIGENTE]**
  Fica estabelecido o **contrato de entrada** da fila: um conjunto de **campos mínimos obrigatórios** que um claim/item precisa cumprir para **entrar** em revisão (`queueState → queued`). **Sem DoR, não há admissão** — o item permanece a montante, na modelagem, e **não** vira item-fantasma de backlog. Os campos estão na D-C2.7 (modelo).
  *Justificativa:* a fatia mostrou que cada item exige claim tipado + fonte + texto por faixa + tag de sensibilidade + ClaimSet-com-fronteira se controverso; **descobrir isso item a item é caro e tardio**. O DoR faz o custo editorial **aparecer no planejamento, não na surpresa** (PG4 verbatim).
  *Relação com PG1:* DoR é a **Definition of *Ready*** (porta de entrada); complementa — não substitui — o "pronto = evidência" de PG1, que é a **Definition of *Done*** (porta de saída).

- **D-C2.3 — Aplicar PG5 como campo do DoR. [PG5: caracterizado → aplicado]**
  A **pré-classificação de sensibilidade na modelagem** (taxonomia das Leis 10.639/2003 e 11.645/2008: `público` / `mediado` / `legal-review`) passa a ser o **campo nº 3 do DoR** (D-C2.7). É ele que define **quais papéis de revisão** o item exige e se entra como `pending` por padrão.
  *Justificativa:* "descoberta" vira "planejamento" — dá para **estimar quanto de uma cena nasce público** antes de construí-la (PG5 verbatim). PG5 deixa de ser anotação e vira porta operante.

- **D-C2.4 — Converter a fila em processo. [§5 → VIGENTE]**
  A fila ganha **(a) dono** (papel-condutor, com não-poderes explícitos — D-C2.6), **(b) cadência** (estrutural, *pull-based*, com *intake throttling* — D-C2.5), **(c) papéis** (os 8 papéis de revisão da Etapa 3.1 §9, mapeados às filas da Etapa 14 §4.2 e à competência da Etapa 13 §3, como **pré-requisito de publicação**), e **(d) não-automação da fronteira** (a fronteira "sem equivalência" de cada `ClaimSet` é escrita à mão; a fila não a automatiza).
  *Justificativa:* é a substância exata pedida pela Seção 5 do Playbook e pela pendência F1.

- **D-C2.5 — Cadência sem números.**
  A cadência é definida **estruturalmente**, não numericamente: a fila é **puxada** (item só entra DoR-completo); roda **primeiro sobre a fatia** (PG3); e tem como válvula de segurança o **intake throttling** da Etapa 14 §3.3 — *capacidade insuficiente **pausa a admissão**, nunca rebaixa a revisão nem aprova em lote*. Os **números** de SLA por fila e os percentuais de amostragem de auditoria permanecem **[PENDÊNCIA]** de execução (E13/E14).
  *Justificativa:* respeita a régua de alocação (Constituição **Art. 17**): número/SLA/cadência-fina são do Playbook *quando o pipeline operar* — fixá-los agora seria escopo de execução, não de governança.

- **D-C2.6 — O dono é um papel, não uma pessoa, com não-poderes explícitos.**
  O **dono da fila** é uma **função-condutora** (mapeia a `operationsLead`/`scaleCoordinator` da Etapa 14 §3 quando houver equipe; em escala-fatia, o mesmo operador sob o chapéu de governança). **Pode:** rotear o item à fila de competência correta, sequenciar o trabalho, rastrear `queueState`, anexar `gatingReason`, e **pausar a admissão** quando a capacidade não comporta revisão com profundidade. **Não pode:** decidir mérito fora de sua competência; **conceder/dispensar** qualquer portão (`qaGateResult` **não tem** `waived`/`override`); publicar item com qualquer papel aplicável não aprovado; **automatizar** a fronteira do `ClaimSet`.
  *Justificativa:* "revisões são **papéis**, não necessariamente pessoas" (Etapa 3.1 §9.1); concentrar condução **sem** concentrar mérito evita que a fila vire atalho de aprovação.

- **D-C2.7 — Definition of Ready: os 8 campos.** (modelo na Seção 5)
  Para um claim/item ser **admitido** à fila, todos os campos abaixo devem **existir e estar tipados** (podem estar em estado `PENDENTE_*` *declarado*, mas nunca silenciosos):
  1. **Claim tipado** — `claimType` (da taxonomia de 10 tipos) + `confidenceLevel` + `evidenceLevel` + `UncertaintyProfile` presentes (Art. 7; claim-first da Etapa 2).
  2. **Fonte identificada** — ao menos um `Source`/`provenanceRef` (aresta afirmativa órfã é **impossível de inserir** — Art. 7/Passo B2). Confirmação por asset (`perAssetConfirmed`) pode seguir `PENDENTE`, mas a fonte tem de estar **identificada**.
  3. **Sensibilidade pré-classificada (PG5)** — tag aplicada na modelagem: `público` / `mediado` / `legal-review` (Leis 10.639/11.645). Define os papéis exigidos e o `pending` por padrão.
  4. **Plano de exposição por faixa etária** — quais níveis mostram/ocultam/avisam (a redação final pode ser pendente; **a forma se adapta, o fato não** — Art. 8).
  5. **`ClaimSet` com fronteira, se controverso** — se a tag sinaliza controvérsia legítima, existe um `ClaimSet` com a fronteira "sem equivalência" **escrita à mão** (Art. 7; nunca automatizada).
  6. **Papel(éis) de revisão designado(s)** — quais dos 8 papéis precisam aprovar, derivado de camada + sensibilidade.
  7. **Tempo/espaço declarados** — `timePrecision`/`timeUncertainty` e `geometryStatus` declarados (podem ser `PENDENTE_DATA`/`PENDENTE_GEOMETRIA`, mas **declarados** — nunca se inventa precisão; Art. 7/9).
  8. **Triagem de licença iniciada** — `licenseRiskLevel` (0–5) pré-classificado e `storagePartition` provisória (`core`/`media`/`isolated`/`blocked`).
  *Justificativa:* o DoR exige que o campo **exista e seja tipado**, não que esteja **finalizado** — finalização é a *Definition of Done* (PG1). Isso impede que o DoR vire portão burocrático que trava trabalho legítimo (ver R-C2.3).

- **D-C2.8 — Consequência documental: Playbook → v1.2.**
  As decisões acima reescrevem o **§4** (PG3/PG4 → VIGENTE) e o **§5** (fila → VIGENTE) do Playbook. A emenda gera **Playbook v1.2**, com linha de changelog própria. (Emitir na sequência — ver Seção 9.)

## 5. Modelo conceitual

**Relação entre os contratos (sem código de aplicação):**

```
DoR (Definition of Ready)  ─ porta de ENTRADA ─►  FILA (processo)  ─ porta de SAÍDA ─►  Definition of Done (PG1)
   8 campos tipados              admissão            8 papéis/competência       "pronto = evidência"
   (D-C2.7)                  (queueState=queued)     (Etapa 3.1 §9 / 14 §4.2)    reviewStatus=approved
```

**Máquina de estados da fila** (instancia `queueState` da Etapa 14 §4.1 sobre a fatia):

```
[modelagem]
   │  (item NÃO DoR-completo permanece aqui; não é backlog, é trabalho a montante)
   ▼  DoR-completo? ── não ──► volta à modelagem
   │           (sim)
   ▼
queued ──► in-progress ──► [revisões por papel competente, conforme sensibilidade]
   │            │              ├─ scientific / historical / editorial
   │            │              ├─ legal (default: NÃO publica) / geotemporal
   │            │              └─ accessibility / license / vieses
   │            │
   │            ├─ dúvida/competência/risco ──► escalated ──► papel/função superior
   │            ├─ reprova ──────────────────► returned (= needs-rework no pipeline)
   │            └─ teste/portão falha ───────► blocked (rebaixamento automático; versionado)
   │
   ▼  todas as revisões aplicáveis aprovadas
publication-queue ──► done  ⇒  reviewStatus = approved  ⇒  EXIBÍVEL
```

**Invariantes que governam a máquina (soberanos sobre a fila):**
- **Art. 6** — item em `pending`/`legal-review`/`rejected` **não vira fato por pressão de fila**, em nenhuma vista, índice, exportação ou na simultaneidade.
- **Art. 13** — `qaGateResult ∈ {pass, fail}`, **sem** `waived`/`override`; QA **bloqueia**, não sugere. Nenhum SLA destrava portão. **Escala não reduz revisão** — capacidade insuficiente **pausa a admissão** (intake throttling).
- **Art. 12** — `returned`/`blocked` operam por **depreciação + correção versionada**; **nada é apagado**.
- **Art. 16** — operar a fatia **não** a promove ao KC; a fatia segue *throwaway*.

**Mapa dos 8 papéis → filas → competência** (já existentes; C2 os amarra):

| Papel de revisão (E3.1 §9) | Fila operacional (E14 §4.2) | Pode aprovar (E13 §3) |
|---|---|---|
| Científica | `scientific-review-queue` | mérito científico de camadas científicas |
| Historiográfica | `historical-review-queue` | mérito histórico/historiográfico |
| Pedagógica/faixa | (no fluxo editorial) | profundidade/linguagem/exposição por faixa |
| Editorial (sensível/controvérsia) | `editorial-review-queue` | `consensusStatus`/`editorialNote`/mediação |
| Jurídica/LGPD | `legal-review-queue` *(default: não publica)* | `legal-review`/licença/risco vivo |
| Licença | `license-queue` | `licenseRiskLevel`/`storagePartition` |
| Geotemporal | `geotemporal-review-queue` | tempo/espaço/datum/geometria |
| Acessibilidade | `accessibility-review-queue` | equivalente textual/e-MAG/WCAG/LBI |
| Vieses | (transversal ao editorial) | eurocentrismo/estereótipo/falsa equivalência |

Consolidação e publicação: `publication-queue` (só após **todas** as revisões aplicáveis).

## 6. Fontes / insumos necessários

Corpus interno (autoritativo): **Constituição v1.1** (Arts. 6, 7, 8, 9, 12, 13, 16, 17); **Playbook v1.1** (§4 PG3/PG4; §5 fila; §7 PG5); **Etapa 3.1** (§9 fluxo e 8 papéis; §9.2 conteúdos de revisão obrigatória); **Etapa 13** (§3 dez papéis de ingestão e matriz de competência); **Etapa 14** (§3.3 intake throttling; §4 estados/filas/SLAs; §7.2 readiness gates); **`analise-pendencias`** (§4 matriz "o que bloqueia o quê"; §5.1 elevar F1; família F1); **`estado-atual-e-roteiro`** (fatia descartável de ~24 itens; coerência protótipo×corpus); **Passos B2** (`entity_node`; proveniência como FK) e **C1/C1.1** (D-C1.4 diferimento; reconciliação verbatim de PG3/PG4/PG5).

**Insumo ausente / pendência registrada:** nenhum bloqueante. Os **números** de SLA/amostragem (E13/E14) e a **caracterização visual de PG6** (Etapa 10/C3) são deliberadamente diferidos, não ausências de insumo.

## 7. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| **R-C2.1** | PG3 "operar na fatia" ser lido como **promover o protótipo descartável ao KC**, ferindo PG2/Art. 16 | D-C2.1 distingue **processo** (sobre itens reais) de **conteúdo** (protótipo *throwaway*); promoção a canônico só via pipeline, após revisão — nunca por estar na fatia |
| **R-C2.2** | "Dono/cadência" virar autoridade para **dispensar portão** sob pressão de prazo | D-C2.6 fixa **não-poderes**; `qaGateResult` sem `waived`; **Art. 13** soberano; intake throttling **pausa admissão** em vez de rebaixar revisão |
| **R-C2.3** | DoR virar **portão burocrático** que trava trabalho legítimo (rigidez excessiva) | D-C2.7: DoR exige o campo **existir e ser tipado**, não estar **finalizado**; estados `PENDENTE_*` *declarados* são admissíveis; finalização é a *Done* (PG1), não a *Ready* |
| **R-C2.4** | Fixar **números de SLA** prematuramente (escopo de execução vazando para governança) | D-C2.5: cadência **estrutural**; números explicitamente **[PENDÊNCIA]** de E13/E14; Art. 17 (régua) aplicada |
| **R-C2.5** | A **fronteira do `ClaimSet`** ser automatizada conforme a fila escala | §5.4 reafirmado (não-automação); a fronteira "sem equivalência" é **escrita à mão**; a fila **roteia e rastreia**, não **gera** a fronteira (Art. 7) |
| **R-C2.6** | Falsa sensação de prontidão por "fila operando" enquanto papéis reais não existem | Os papéis são **pré-requisito de publicação**; a Etapa 14 §7.2 mantém os *readiness gates* objetivos (papel ausente ⇒ `not-ready`), não destravados por C2 |

## 8. Entregáveis

1. **Este handoff** (`passo-c2-handoff-fila-revisao-processo-v1_0.md`) — registro do passo, decisões `D-C2.1..8`, modelo conceitual, riscos.
2. **Texto operacional ratificado** das Seções 4 e 5 do Playbook (PG3/PG4 → VIGENTE; fila → VIGENTE), contido nas Seções 4–5 deste handoff e pronto para ser dobrado no **Playbook v1.2**.
3. **O DoR de 8 campos** (D-C2.7) e a **máquina de estados da fila** (Seção 5) como modelo conceitual — sem código.
4. **(A emitir na sequência)** **Playbook v1.2** consolidado, com §4/§5 vigentes e changelog.

## 9. Próximos passos

- **Emitir o Playbook v1.2** dobrando §4 (PG3/PG4 → VIGENTE) e §5 (fila → VIGENTE), com linha de changelog `v1.2` e nota de que **supersede o v1.1**. *(Faço a seguir, quando você confirmar; é um passo de fechamento documental.)*
- **C3 — cluster de publicação pública** (F2 fonte/licença · F5 fundação escolar · F6 jurídico/LGPD): caracterizar o **contrato visual de PG6** com a UX (Etapa 10) e usar a classificação de **PG5 já operante** para estimar o *split* público/mediado das cenas.
- **Quando o pipeline operar (E13/E14):** fixar os **números** de SLA por fila e os percentuais de amostragem de auditoria que C2 deixou `[PENDÊNCIA]`.
- **Operacional permanente:** cada chat sob a **Constituição v1.1 + o Playbook (v1.2 após emissão)** — um passo, por evidência, com handoff salvo; não criar projeto novo.

---

*Documento de governança do Passo C2, sob a Constituição v1.1 (Arts. 6, 7, 8, 9, 12, 13, 16, 17), o Playbook v1.1 (§§4, 5, 7), a política editorial (Etapa 3.1 §9), o pipeline (Etapa 13 §3) e a operação/governança (Etapa 14 §3.3/§4/§7.2), e os Passos B2, C1 e C1.1. Ratifica PG3 e PG4 e aplica PG5 no nível operacional, e converte a fila de revisão de backlog em processo (dono, cadência estrutural, 8 papéis como pré-requisito de publicação, fronteira não automatizada), preenchendo as Seções 4 e 5 do Playbook. Não altera nenhum invariante da Constituição (apenas a implementa), não reabre nenhuma etapa, não fixa números de SLA/amostragem (seguem [PENDÊNCIA] de E13/E14), não caracteriza o contrato visual de PG6 (→ C3/Etapa 10), não escreve código e não decide dados. Guarda crítica: operar a fatia não a promove ao Knowledge Core — a fatia-protótipo segue throwaway (Art. 16); só vira canônico o item que passa pela revisão via pipeline. Próximo passo na Trilha C, quando solicitado: emitir o Playbook v1.2 (§4/§5 vigentes) e, depois, C3 — cluster de publicação pública.*
