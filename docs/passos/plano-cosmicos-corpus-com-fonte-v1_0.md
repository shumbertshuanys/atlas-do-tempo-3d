# Frente A — Cósmicos como corpus COM fonte · Handoff de planejamento

**Versão:** v1.0
**Data:** jun/2026
**Natureza:** handoff no formato de 9 pontos do Playbook §2. Esta sessão é de **PLANEJAMENTO — não escreve código**. A execução vai para o Claude Code (padrão de duas fases).
**Antecede:** execução no Claude Code (descoberta → portão humano → modelagem → testes).
**Sucede:** virada ao vivo + 3D real concluída e verde (`registro-execucao-a3-virada-3d.md`); frame consome `/momento/publico` via `fromEnvelope`; `atlas-model.js` é a fonte única do §8.
**Aterramento:** eixo canônico 3Z (`etapa-3z`, T0=2000 CE; Big Bang ≈ −1,38×10¹⁰; `sourceTimeBasis=Ga`) + Knowledge Core (`etapa-2`: `KnowledgeItem`/`Claim`/`Source`/`Citation`/`TimeRange`/`ProvenanceMetadata`; P3 proveniência, P8 incerteza tipada) + política editorial de controvérsias (`etapa-3.1`, que **governa o Big Bang** — item 11.2 da Etapa 2).

> **O problema, em uma frase:** os três teasers cósmicos do frame (`rep:bigbang`/`rep:galaxies`/`rep:sun`) estão marcados `prov:'corpus', rev:'approved'` **no frame**, mas **não existem no corpus** (35 itens). Contra a API pública, o estágio cósmico vem **vazio** — honesto, e exatamente a divergência que a virada deveria expor, não maquiar. Esta frente os transforma em **itens de corpus reais com fonte** — **nunca** por promoção de seeded, sempre por modelagem com claims fonteadas.

---

## 1. Objetivo

Preencher o estágio cósmico **com lastro de corpus e fonte**, de modo que a porta pública (e/ou a curatorial, conforme a decisão epistêmica) deixe de retornar vazio no tempo cósmico — preservando integralmente os invariantes (proveniência obrigatória, público nunca vaza não-fato, não-fato nunca exibido como fato, tempo profundo sempre reconstrução/esquemático) e **sem** tocar o miolo provado (`db/ddl/`, `010`). A virada extinguiu a divergência frame↔corpus por construção; aqui se **adiciona conteúdo fonteado** ao corpus pelo caminho já provado (`migrate.py` → `011` → serviço → `fromEnvelope`), validando-o como **template de ingestão**.

## 2. Escopo

**Fará (no Claude Code, após o portão humano):**
- **Descoberta (§6):** confirmar contra o DDL/corpus vivo — janela do estágio cósmico nos `STAGES`, `item_type`/`epistemic_type` admissíveis, tratamento de item **sem geometria terrestre** (`displayPoint` NULL), fontes por claim.
- **Proposta de tipagem epistêmica** por claim (tipo + `is_fact` + confiança + incerteza) → **tabela para assinatura humana** (o portão).
- **Modelar** os itens cósmicos como `KnowledgeItem` + `Claim` claim-first, cada um com `Source`/`Citation` e `provenance_ref` (NOT NULL), `TimeRange` canônico (`sourceTimeBasis=Ga`, `timeUncertainty`/`timePrecision`), `geometryRegime` rotulado "cósmico / sem geometria terrestre". **Adição** a `migrate.py` (como a fatia D-A3.1 adicionou `rev-francesa`), nunca reescrita do miolo.
- **Reconciliar o frame:** os teasers cósmicos passam a ser **desenhados a partir do envelope** (como todo o resto), não mais asseridos como corpus-sem-fonte; o **render do estágio segue procedural/esquemático** (R-V7) — o item ganha lastro, a cena continua reconstrução, nunca foto.
- **Testes falsificáveis novos** (`COSMO-T*`) + re-verde das suítes existentes.

**Não fará (ver Rodapé):** **não** promove `seeded-demo` a corpus nem a fato; **não** estende o eixo 3Z nem cria regime novo (o tempo cósmico já cabe); **não** reescreve `db/ddl/`/`010`/`011` (no máximo **adição** mínima se a descoberta exigir); **não** religa as 3 sensíveis (host `pending`); **não** transforma o estágio cósmico em foto; **não** dá palco a falsa equivalência (Big Bang × "teorias concorrentes" obsoletas).

## 3. Diagnóstico

Quatro achados governam o plano.

1. **O tempo cósmico não exige nada novo do eixo.** Pela `etapa-3z`, o eixo é contínuo em anos rel. a T0=2000; 1789 = −211 (daí a janela −212..−210 do CLAUDE.md). Logo Big Bang (~13,8 Ga) = `canonicalTimeScalar ≈ −1,3787×10¹⁰`, `sourceTimeBasis=Ga`, `displayTime="~13,8 Ga"`, offset de 50 anos descartado (ruído sob a incerteza). **Sem** extensão de eixo, **sem** regime novo. A descoberta só confirma a **janela do estágio cósmico** nos `STAGES` do frame e que a coluna numérica viva aceita a magnitude.

2. **A tipagem epistêmica é o ponto sensível — e não é livre.** Claims cósmicas **não** são "fato documentado": ninguém testemunhou o t=0. Elas se partem em dois grupos, e o invariante "não-fato nunca exibido como fato" + "público lê só `v_publishable_public` (`is_fact=true`, `selo='público'`)" obriga decidir **por claim**:
   - **bem medido / consenso forte** (idade do universo via CMB/Planck; idade do Sistema Solar via datação radiométrica de meteoritos) → `epistemic_type ≈ medição direta`/`inferência científica`, confiança alta, com incerteza → **candidato a `is_fact=true` público** (análogo a "houve impacto" no K-Pg ser fato);
   - **modelo-dependente / extrapolado** (a singularidade t=0; inflação; **timing/processo** de formação das primeiras galáxias — campo em mudança rápida com JWST) → `inferência científica`/`reconstrução modelada`/`hipótese`, confiança menor → pode **não** passar a porta pública estrita; aparece com selos (curatorial/reconstrução). **Esta partição é decisão humana** (a regra do projeto: agente não fixa status epistêmico sozinho). → portão do §9.

3. **Item cósmico é o primeiro item sem geometria terrestre.** Todo item do corpus até aqui tinha geometria; `displayPoint` nasceu como centróide PostGIS. O Big Bang **não tem lat/lng na Terra**. A descoberta confirma que `displayPoint = NULL` é tratado sem quebra, que `geometryRegime` **rotula honestamente** "cósmico / sem geometria terrestre", e que o frame **degrada** para a cena procedural **sem** marcador no globo (sem regressão aos marcadores terrestres). É o teste `COSMO-T4`.

4. **Sem falsa equivalência no Big Bang.** Modelá-lo como "Big Bang × estado estacionário" daria palco simétrico a uma visão obsoleta — viola o invariante de pesos assimétricos ("'houve impacto' não é um lado em disputa"). O **núcleo estabelecido** (expansão, CMB) entra como claim de alta confiança com incerteza, **não** como ClaimSet. Se algum ClaimSet se justificar, é uma controvérsia **real e estreita** — candidata: a **tensão de Hubble** (valor de H₀/idade, com pesos assimétricos) — e seria regida pela `etapa-3.1` + assinatura editorial, gateando por host como as demais (não vaza pública sem host público+fonteado).

## 4. Decisões principais

| ID | Decisão | Estado |
|---|---|---|
| **F-A.1** | Tempo cósmico no eixo 3Z existente (sem extensão, sem regime novo); `sourceTimeBasis=Ga`; incerteza obrigatória. | Fechada (deriva da `etapa-3z`). |
| **F-A.2** | Itens cósmicos são `KnowledgeItem`+`Claim` claim-first **com `Source`/`Citation` e `provenance_ref`**; **adição** a `migrate.py`. Seeded **nunca** promovido. | Fechada (invariante N1/P3). |
| **F-A.3** | Render do estágio cósmico permanece **procedural/esquemático** (R-V7); o lastro de corpus **não** vira foto. Mídia real (fotos de telescópio NASA, PD) é **opcional e adiada** — se entrar, `natureLabel` correto (foto × mapa/gráfico do CMB × reconstrução). | Fechada. |
| **F-A.4** | Tipagem epistêmica + `is_fact` por claim (quais passam a porta pública; quais ficam reconstrução/curatorial; se há ClaimSet) → **tabela proposta na descoberta, assinada pelo humano** antes de modelar. | **Portão humano** (§9 passo 2). |
| **F-A.fork** | **Escopo do mini-corpus cósmico.** Abordagem 1 (substituição fiel mínima) × Abordagem 2 (mini-corpus cósmico coerente). Detalhada em §5.3; ambas honestas, ambas fonteadas, nenhuma promove seeded. | **Fechada → Abordagem 2** (mini-corpus coerente; escolha do humano, jun/2026). |

## 5. Modelo conceitual

### 5.1 Forma de cada item cósmico (dicionário, não código)

Cada âncora vira um `KnowledgeItem` com pelo menos:

```txt
ItemCósmico = {
  id,                  # ex.: evt:big-bang  /  proc:formacao-galaxias  /  evt:formacao-sistema-solar
  item_type,           # Event | Process  (confirmar enum vivo na descoberta)
  title, displayTime,  # "Big Bang" · "~13,8 Ga"
  TimeRange: {
    canonicalScalar/Start/End,   # anos rel. T0=2000  (Big Bang ≈ −1,3787e10)
    sourceTimeBasis: 'Ga',
    timePrecision: 'Ga',
    timeUncertainty,             # ± da fonte (ex.: idade do universo 13,787 ± 0,020 Ga)
    temporalConfidence,
    conversionMethod: 'Ga→anos', conversionNotes
  },
  geometryRegime,       # "cósmico / sem geometria terrestre";  displayPoint = NULL
  Claim (claim-first): {
    epistemic_type,     # medição direta | inferência científica | reconstrução modelada | hipótese  (a assinar, §9)
    is_fact,            # TRUE só se passa a porta pública (a assinar)
    confidence,         # alta | média | baixa  (vocab vivo, hifenizado)
    provenance_ref      # NOT NULL → Source/Citation
  },
  Source/Citation,      # NASA/ESA/Planck/peer-reviewed; licença por asset (etapa-1.1)
  selo,                 # 'público' (se is_fact) | curatorial/reconstrução
  Relationships         # ex.: formacao-sistema-solar → (precede) GOE −2,4 Ga (ponte ao tempo profundo terrestre)
}
```

O `SceneModel`/`overlayFields` **não muda**: o item cósmico flui pelo `fromEnvelope` como qualquer outro; o §8 o desenha com seu selo e incerteza nos 3 degraus.

### 5.2 Alvos de modelagem e fontes (a **confirmar na curadoria**, não fatos finais aqui)

| Âncora | Alvo temporal | Tipo epistêmico (proposto) | Fonte candidata |
|---|---|---|---|
| Big Bang / idade do universo | ~13,8 Ga (13,787 ± 0,020) | medição direta (CMB) → inferência da idade; t=0 = extrapolação | ESA Planck 2018; NASA WMAP; peer-reviewed |
| CMB / recombinação *(Abord. 2)* | ~13,8 Ga (≈ +380 ka após o início) | medição direta (o CMB é observado) | ESA Planck; NASA |
| Primeiras estrelas/galáxias *(Abord. 2)* | ~13,5–13 Ga | inferência científica; **confiança média** (JWST, campo em evolução) | NASA/ESA (JWST); peer-reviewed |
| Formação do Sistema Solar / Sol | ~4,567 Ga | medição direta (radiométrica de meteoritos) + inferência; confiança alta | NASA; peer-reviewed (datação de CAIs) |
| Formação da Terra *(Abord. 2, ponte)* | ~4,54 Ga | medição direta + inferência; confiança alta | USGS; peer-reviewed (zircões/meteoritos) |

> Nota de honestidade de mídia: o Big Bang **não tem fotografia**; o CMB é um **mapa de dados** (`natureLabel = mapa/gráfico`, medição), não foto. Uma imagem de galáxia de Hubble/JWST **é** foto (`fotografia`, PD NASA) — mas só entra **se** optarmos por mídia (F-A.3: adiada). "Impressão artística do universo primitivo" é **reconstrução**, rotulada como tal, nunca como registro.

### 5.3 O fork de escopo (F-A.fork) — **as duas abordagens** · DECISÃO: **Abordagem 2**

> **DECISÃO (jun/2026): Abordagem 2 — mini-corpus cósmico coerente.** Com ela, as cinco/seis âncoras de §5.2 (inclusive as marcadas "(Abord. 2)") entram **todas** em escopo. As duas abordagens seguem documentadas abaixo para o registro.

**Abordagem 1 — Substituição fiel mínima (3 itens, 1:1 dos teasers).**
Modela exatamente Big Bang, formação de galáxias e formação do Sol/Sistema Solar como **3** itens de corpus com fonte. Espelha o que o frame já mostra, agora com lastro.
- *A favor:* menor modelagem e curadoria; menor risco; mais rápido; paridade frame↔corpus óbvia; valida o pipeline de "adicionar item fonteado" com a menor mudança possível; portão humano leve (3 itens).
- *Contra:* linha cósmica esparsa (3 pontos em ~13,8 Ga, com vão de ~9 Ga entre Sol e o resto); "galáxias" como **um** item é epistemicamente grosso (formação galáctica é um processo de Ga, difícil fontear como claim única); sem ponte explícita ao tempo profundo terrestre.

**Abordagem 2 — Mini-corpus cósmico coerente (5–6 itens + ponte).**
Modela âncoras navegáveis: Big Bang, CMB/recombinação, primeiras estrelas/galáxias, formação do Sistema Solar/Sol e **formação da Terra (~4,54 Ga)** — que faz a **ponte** para a cena GOE existente (−2,4 Ga).
- *A favor:* linha cósmica de fato navegável; ponte limpa cósmico→Terra profunda; respostas mais ricas de "o que acontecia?" no tempo cósmico; cada âncora fonteada e tipada **individualmente** (resolve o "galáxias grosso" partindo em Event/Process bem definidos).
- *Contra:* mais modelagem, mais curadoria, portão humano maior (5–6 itens); um pouco mais de descoberta (representar um processo de ~Ga com bordas difusas; CMB como Event × State); superfície marginalmente maior — mas **toda** dentro do pipeline provado.

**Recomendação (não decisão):** se o objetivo é um estágio cósmico satisfatório e uma ponte limpa ao tempo profundo, **Abordagem 2** rende muito mais por pouco mais de trabalho e evita o "galáxias grosso". Se a prioridade é a **menor mudança validada primeiro**, **Abordagem 1** — e estender depois é o **mesmo** pipeline. **Escolha feita: Abordagem 2** (registro acima).

## 6. Descoberta (a rodar no Claude Code, antes de modelar)

1. **Janela do estágio cósmico** nos `STAGES` (`atlas-model.js`): confirmar que `stageForScalar(−1,38e10)` cai no estágio cósmico; confirmar que a coluna numérica viva aceita a magnitude.
2. **Enums vivos:** `item_type`/`eventKind` (Event × Process para Big Bang/formações) e `epistemic_type` (valores hifenizados, conforme a descoberta da virada). Mapear cada claim ao tipo certo.
3. **Item sem geometria terrestre:** confirmar que o esquema admite item **sem** `geometry_version` (ou com sentinela "cósmico"), que `displayPoint=NULL` flui sem quebra, e que `geometryRegime` rotula honestamente.
4. **Fontes por claim:** localizar e confirmar `Source`/`Citation` + **licença por asset** (checklist `etapa-1.1`); NASA/ESA são PD/abertas; papers peer-reviewed = citação, **nunca** reprodução.
5. **ClaimSet?** Consultar `etapa-3.1` sobre o Big Bang: há controvérsia real a destacar (candidata: tensão de Hubble) ou é claim única com incerteza? Se ClaimSet, gateia por host como as demais.
6. **Varredura anti-seeded:** confirmar que não há item `seeded-demo` cósmico a ser promovido por engano; os novos itens são **novos**, com fonte; reconciliar o marcador `prov:'corpus'` dos teasers (o frame deixa de afirmar corpus-sem-fonte).

→ Saída: **nota de descoberta curta** + a **tabela de tipagem epistêmica proposta** (entrada do portão).

## 7. Riscos

- **R1 — Excesso epistêmico:** apresentar cosmologia modelo-dependente (t=0, inflação, timing de 1ªs galáxias) como fato. *Mitigação:* tipagem + `is_fact` por claim; **assinatura humana**; só o bem-medido passa a porta pública.
- **R2 — Promoção acidental de seeded:** reusar o `prov:'corpus'` dos teasers em vez de criar itens fonteados. *Mitigação:* itens novos com `provenance_ref` (o CHECK NOT NULL **obriga** fonte); teasers reconciliados para desenhar do envelope.
- **R3 — Item sem geometria quebra suposições:** lógica que assumia geometria/`displayPoint` em todo item. *Mitigação:* descoberta confirma NULL; `geometryRegime` cósmico; frame degrada a esquemático sem marcador (`COSMO-T4`).
- **R4 — Falsa equivalência:** Big Bang como "teorias concorrentes". *Mitigação:* núcleo estabelecido = claim de alta confiança, **não** ClaimSet; se houver, só controvérsia real e estreita com pesos assimétricos, regida pela `etapa-3.1`.
- **R5 — Falsa precisão temporal:** cravar "13,8 Ga" sem incerteza. *Mitigação:* `timeUncertainty`/`timePrecision` obrigatórios (já é regra 3Z); exibir "~13,8 Ga (±0,02)".
- **R6 — Licença de mídia:** ingerir imagem não-PD ou rotular impressão artística como foto. *Mitigação:* confirmação por asset (`etapa-1.1`); `natureLabel` correto; **mídia adiada** nesta frente (estágio é procedural).

## 8. Entregáveis

**Desta sessão (planejamento):** este handoff, com o fork de escopo e o portão epistêmico embutidos.

**Da execução (Claude Code), na ordem do §9:**
- Nota de descoberta + **tabela de tipagem epistêmica assinada**.
- Itens cósmicos + `Source`/`Citation` no `migrate.py` (**adição**; carga 35 → 35+N, fontes +M; fixtures de inventário atualizadas como no precedente D-A3.1, com `soma_ok` e demais asserções **intactas**).
- Frame reconciliado (teasers desenhados do envelope; estágio procedural/esquemático preservado).
- Testes `COSMO-T*` verdes + re-verde de `verify`/`test_a4`/`test_a3`/`test_a3_http` + suítes do frame.
- `CLAUDE.md` atualizado (§4 carga; §5 frente 1 → feita) + handoff de execução.

### Testes falsificáveis (`COSMO-T*`)

| # | Assere | Falha se |
|---|---|---|
| COSMO-T1 | a janela cósmica **deixa de vir vazia** na porta correta (pública para os claims `is_fact`; curatorial para os reconstrução) — retorna os itens fonteados | estágio cósmico segue vazio onde deveria ter lastro |
| COSMO-T2 | **nenhum** item cósmico é exibido como "fato documentado"; `epistemic_type` correto + incerteza presente nos **3 degraus** (3D/2D/estático) | algum claim cósmico aparece como fato seco / perde incerteza em algum degrau |
| COSMO-T3 | **todo** item cósmico tem `provenance_ref`; **nenhum** tem `selo='seeded-demo'` (prova negativa anti-promoção) | entra item cósmico sem fonte ou promovido de seeded |
| COSMO-T4 | item sem geometria terrestre: `displayPoint=NULL` tratado; estágio cósmico **esquemático**, sem marcador no globo, sem regressão | NULL quebra o render / cena cósmica vira foto / aparece marcador terrestre espúrio |
| COSMO-T5 | (se ClaimSet) gateia por host como as demais; (se não) **zero** ClaimSet cósmico de falsa equivalência | "teoria concorrente" obsoleta ganha palco simétrico / ClaimSet cósmico vaza sem host |

## 9. Próximos passos (ordem de execução no Claude Code)

0. **PG1 — verde fresh, sem exceção:** `docker compose down -v && bash scripts/bootstrap.sh` → `verify` 10/10 + `test_a4` 10/10 + `test_a3` 10/10 + `test_a3_http` 5/5. Sem isso, não avança.
1. **Descoberta (§6):** rodar as consultas; nota curta + **tabela de tipagem epistêmica proposta**.
2. **🚦 PORTÃO HUMANO (F-A.4):** assinar a tabela — quais claims são `is_fact=true` públicos × quais ficam reconstrução/curatorial; se há ClaimSet (e qual, sob a `etapa-3.1`). **Não modela antes desta assinatura.**
3. **Modelar (escopo da F-A.fork escolhida):** itens + `Source`/`Citation` em `migrate.py` (adição); `provenance_ref`, `epistemic_type`, `TimeRange` (canônico + `Ga` + incerteza), `geometryRegime` cósmico. Mudança **cirúrgica** no miolo (idealmente zero; no máximo adição mínima se a descoberta exigir).
4. **Reconciliar o frame:** teasers cósmicos do envelope; render do estágio **procedural/esquemático** (R-V7) preservado.
5. **Testes:** `COSMO-T1..5` verdes; re-verde das suítes; fixtures de inventário atualizadas (precedente D-A3.1; invariantes intactas).
6. **`CLAUDE.md`** atualizado + handoff curto.
7. **Commits por mudança lógica:** (a) descoberta+tabela, (b) itens+fontes na migração, (c) reconciliação do frame, (d) `COSMO-T*`, (e) `CLAUDE.md`+handoff. **Nunca** commit-monstro.

---

## Rodapé — o que este passo NÃO faz

- **NÃO escreve código** (é planejamento); a execução vai para o Claude Code.
- **NÃO promove** `seeded-demo` a corpus nem a fato; os cósmicos só viram corpus **com fonte** (modelagem), nunca por promoção.
- **NÃO estende** o eixo 3Z nem cria regime novo — o tempo cósmico já cabe (`canonicalTimeScalar` em anos rel. T0=2000).
- **NÃO reescreve** `db/ddl/`/`010`/`011` provados — no máximo **adição** mínima se a descoberta exigir.
- **NÃO religa** as 3 sensíveis (`direitos-limites`/`inconfidencia`/`escravidao-central`) — host `pending`, seguem na fila (Trilha C).
- **NÃO transforma** o estágio cósmico em fotografia; tempo profundo segue esquemático/reconstrução (R-V7).
- **NÃO dá palco** a falsa equivalência (Big Bang × visões obsoletas); núcleo estabelecido = claim de alta confiança com incerteza.
- **NÃO fixa** status epistêmico sozinho — a tabela de tipagem é assinada pelo humano (passo 2).

---

## Prompt para a próxima sessão (EXECUÇÃO no Claude Code)

> Atlas do Tempo 3D — EXECUÇÃO da Frente A (cósmicos como corpus COM fonte). Plano fechado em
> `docs/passos/plano-cosmicos-corpus-com-fonte-v1_0.md`. Esta sessão **escreve código** (corpus/migração + reconciliação do frame; banco só recebe adição mínima se a descoberta exigir).
>
> Comece pelo verde, sem exceção (PG1):
>   `docker compose down -v && bash scripts/bootstrap.sh` → confirme 10/10 + 10/10 + 10/10 + 5/5.
>
> Escopo escolhido pelo humano (F-A.fork): **Abordagem 2 — mini-corpus cósmico coerente** (Big Bang · CMB/recombinação · 1ªs estrelas/galáxias · Sistema Solar/Sol · formação da Terra → ponte à cena GOE).
>
> Depois, **um passo por vez**, na ordem do §9:
>   1. Descoberta (§6): janela do estágio cósmico? enums vivos (item_type/epistemic_type)? item sem geometria (displayPoint NULL)? fontes por claim? ClaimSet sob a etapa-3.1? anti-seeded? → nota curta + **tabela de tipagem epistêmica**.
>   2. 🚦 PARE no portão humano: a tabela precisa ser **assinada** antes de modelar.
>   3. Modelar itens + Source/Citation em migrate.py (adição); provenance_ref, epistemic_type, TimeRange (Ga + incerteza), geometryRegime cósmico.
>   4. Reconciliar o frame (teasers do envelope; estágio procedural/esquemático).
>   5. COSMO-T1..5 verdes + re-verde das suítes; fixtures de inventário atualizadas (invariantes intactas).
>   6. CLAUDE.md atualizado + handoff curto.
>
> Disciplina: PRONTO = EVIDÊNCIA em cada degrau; commits por mudança lógica; mudança **cirúrgica** no miolo; NÃO promova seeded a corpus; NÃO religue as 3 sensíveis; NÃO transforme o estágio cósmico em foto; NÃO dê palco a falsa equivalência; NÃO fixe status epistêmico sem a assinatura humana.
> Artefatos que provam a frente: COSMO-T1 (cósmico deixa de vir vazio onde tem lastro), COSMO-T2 (nenhum cósmico como fato seco; incerteza nos 3 degraus), COSMO-T3 (anti-promoção: todo cósmico com fonte, nenhum seeded), COSMO-T4 (item sem geometria; estágio esquemático sem regressão).
