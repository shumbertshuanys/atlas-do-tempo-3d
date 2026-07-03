# Playbook Operacional do Atlas do Tempo 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** documento de **procedimento operacional** — o **como-fazer**. É a metade que **muda com frequência** da separação ratificada em **PG7** (C1, D-C1.3). Sua contraparte é a **Constituição** (invariantes duros). O Playbook **implementa** os invariantes da Constituição; **nunca os afrouxa nem os contradiz**.
**Estatuto das cláusulas:** marcado por seção — **[VIGENTE]** (em uso agora), **[DIFERIDO]** (gancho registrado, dono e etapa indicados) ou **[A CARACTERIZAR]** (anotado, sem substância ratificada ainda). Mudança aqui é **esperada e rotineira**, sempre registrada no changelog.
**Origem:** redigido no Passo **C1.1** a partir da estrutura do **C1 §5.1**, sob o `registro-prototipo-e-protocolo-continuidade`, o `estado-atual-e-roteiro`, a `analise-pendencias-atuais`, a política editorial (Etapa 3.1), o pipeline (Etapa 13) e a operação/governança (Etapa 14).
**Versão:** v1.0 — **Data:** 2026-06-21.

> **Relação com a Constituição.** Sempre que uma cláusula deste Playbook tocar publicabilidade, proveniência, licença, tipagem epistêmica ou exibição, ela **remete** ao artigo correspondente da Constituição e **não pode** relaxá-lo. Em conflito, **a Constituição vence** e a cláusula do Playbook é corrigida.

---

## Preâmbulo — para que serve o Playbook

O Playbook é a memória viva do **método**: como abrimos e fechamos um passo, como provamos uma capacidade, como registramos o que ficou pendente. Iterá-lo rápido é uma **virtude** — é o que permite melhorar como revisamos, fatiamos e entregamos **sem risco de erodir** a Constituição. O changelog é o que impede a deriva: é o "documentar para não nos perdermos" tornado mecanismo (PG7).

**Régua de alocação (lembrete — Constituição, Art. 12):** se é número, SLA, cadência ou checklist, ou se pode melhorar sem ferir nenhuma propriedade do produto → **Playbook**. Se o produto deixa de ser o produto quando violado, ou se é propriedade epistêmica/proveniência/licença/exibição → **Constituição**.

---

## Seção 1 — Protocolo de continuidade: um passo por chat **[VIGENTE]**

Reconhecido formalmente no Passo C1 (D-C1.6) como **expressão operacional de PG1+PG2+PG7**, e **em vigor desde já**.

**Procedimento:**
1. **Um passo por chat.** Cada chat trata **um** passo do roteiro e é **nomeado** por ele (facilita reencontrar).
2. **Abertura padrão.** Todo chat **começa** declarando o passo e lendo o `estado-atual-e-roteiro`: *"estamos no passo X do estado-atual-e-roteiro; contexto no projeto."*
3. **Fechamento padrão.** Todo chat **termina** com um **handoff curto salvo no projeto** (o que foi decidido, o que ficou pendente, próximo passo) — no formato da Seção 2.
4. **Mesmo projeto, sempre.** Chats passados ficam pesquisáveis e o conhecimento é compartilhado. **Não criar projeto novo.**
5. **Arquivos executáveis não atravessam chats sozinhos.** Reenviar os `.html`/`.md` executáveis quando precisar editá-los (eles são guardados como arquivo, não no conhecimento do projeto).

*Implementa:* PG1 (cada passo fecha por evidência), PG2 (cada passo é uma fatia), PG7 (handoff = registro anti-deriva). *Precedentes vivos:* encerramentos 4Z/5Z; Passos B1, B2 e C1.

---

## Seção 2 — Formato de handoff: 9 pontos + rodapé **[VIGENTE]**

Todo handoff segue a estrutura de **nove pontos** (do prompt-mestre, item 10) e fecha com o **rodapé** no estilo dos encerramentos 4Z/5Z.

**Os nove pontos:**
1. **Objetivo** — o que o passo se propôs a fazer.
2. **Escopo** — o que está dentro.
3. **Diagnóstico** — o estado encontrado, o que mudou de entendimento.
4. **Decisões principais** — numeradas e rotuladas (p.ex. `D-XN`), com justificativa.
5. **Modelo conceitual** — estruturas, tabelas, esquemas (sem código de aplicação).
6. **Fontes / insumos necessários** — corpus e, quando aplicável, fontes externas citadas; **insumos ausentes explicitados**.
7. **Riscos** — `R-XN` com descrição e mitigação.
8. **Entregáveis** — lista do que o passo produz.
9. **Próximos passos** — o que vem a seguir, por trilha, sem pular etapas.

**Rodapé (estilo 4Z/5Z):** um parágrafo que declara **sob quais etapas/passos** o documento se apoia, **o que ele NÃO faz** (limites explícitos), eventuais **insumos ausentes/pendências leves**, e o **próximo passo** na trilha.

*Implementa:* PG1/PG7. *Observação:* o rodapé "o que NÃO faz" é parte essencial — declarar limites é disciplina anti-escopo e anti-deriva.

---

## Seção 3 — Cadência de fatias e critério de "fatia fina o suficiente" **[VIGENTE]**

Operacionaliza **PG2** (Constituição, Art. 11).

**Procedimento:**
1. **Provar, não especificar.** Diante de uma capacidade incerta, a resposta padrão é **construir a fatia mais fina que a exibe ponta-a-ponta**, não escrever mais especificação.
2. **A fatia é descartável por desenho.** Serve para **ensinar o que falta** e **destravar a próxima decisão com evidência**; não precisa ser código de produção.
3. **Termina em artefato que abre e se clica** — não em documento. Um protótipo navegável, um esquema com *constraint* verificável, uma cena ponta-a-ponta, um teste que passa.
4. **Critério de "fina o suficiente":** a fatia é fina o suficiente quando **isola uma única decisão ou propriedade** e a exibe sem depender de partes ainda não construídas. Se exige construir três coisas para mostrar uma, **fatie mais**.
5. **Coerência protótipo × corpus.** Itens **semeados para demonstração** (não pertencentes ao corpus) são **marcados como tal**; protótipo e corpus **não divergem em silêncio** (`provenance_status` obrigatório; registro de divergência).

*Implementa:* PG1/PG2. *Precedentes:* fatia vertical de 1789; Incremento 2 (GOE/K-Pg); B1 (motor decidido com padrões reais do protótipo).

---

## Seção 4 — Ganchos diferidos: PG3 e PG4 **[DIFERIDO → C2]**

Diferidos no Passo C1 (D-C1.4). **Registrados, não operantes.** Pertencem à conversão da fila de revisão em processo (**C2**, pendência F1).

- **PG3 — operar na fatia.** *Substância prevista:* tornar a fatia não só instrumento de prova, mas o **modo padrão de operação** (trabalhar dentro de um recorte fino enquanto a cobertura cresce por fora). *A ratificar em C2*, com definição operacional de como uma fatia "entra em operação" sem que o backlog vire bloqueio. *Liga-se a:* o achado de que a **fila de revisão precisa virar processo, não backlog** (`analise-pendencias` §5).
- **PG4 — Definition of Ready (DoR).** *Substância prevista:* um **checklist de prontidão de entrada** — o que um item/fatia precisa ter para **começar** a ser trabalhado (proveniência mínima, fonte identificada, tipo de claim previsto, papel de revisão designado). *A ratificar em C2*, como contrato de entrada do trabalho, complementar ao "pronto = evidência" (que é a Definition of Done, já vigente em PG1).

**[NORMATIVO]:** enquanto diferidos, PG3/PG4 **não** alteram o método vigente; seu diferimento é, em si, disciplina de PG7 (registrar o que ainda não se decidiu).

---

## Seção 5 — Fila de revisão como processo **[DIFERIDO → C2, pendência F1]**

Hoje a fila de revisão é **backlog sem dono nem cadência**; é o **caminho crítico de cobertura** quando o produto for ao público (`analise-pendencias` §5, F1). O C2 deve produzir:
1. **Dono** — quem conduz a fila (sem decidir mérito fora de competência).
2. **Cadência** — com que ritmo itens entram, são revisados e saem.
3. **Papéis de revisão** — científica, historiográfica, pedagógica, faixa etária, jurídica, acessibilidade, mídia, vieses (Etapa 3.1 §9; Etapa 14 §3) como **pré-requisito de publicação**.
4. **Não-automação da fronteira** — a fronteira "sem equivalência" de cada `ClaimSet` é **escrita à mão**; a fila não a automatiza.

**[NORMATIVO]:** nada nesta seção pode contornar o **invariante de exibição** (Constituição, Art. 5): item não revisado **não** vira fato por pressão de fila.

---

## Seção 6 — Recadência por fonte viva, SLAs e amostragem de auditoria **[DIFERIDO → quando operar, E13/E14]**

Procedimentos finos de operação, definidos **quando o pipeline operar** (Etapas 13/14). Registrados aqui como ganchos:
1. **Recheck de fonte viva** — cadência por classe de fonte (frequente para fontes vivas; periódica para estáveis); mudança de fonte **cria nova versão de `Source` + novo `DatasetSnapshot` imutável**; **jamais** atualização silenciosa (implementa Constituição, Art. 9).
2. **SLAs por fila** — prazos de atendimento por papel/fila; números são **[PENDÊNCIA]** de execução.
3. **Amostragem de auditoria** — limiares de amostragem de revisões e auditorias periódicas; trilha de decisão grava ator, data e `gatingReason`.
4. **Rollback versionado** — opera por **depreciação + restauração** da versão anterior; **nada é apagado** (implementa Constituição, Art. 9).

**[NORMATIVO]:** `qaGateResult` tem **dois** valores (`pass`/`fail`) — **sem** `waived`/`override`. QA **bloqueia**, não sugere. Nenhum SLA ou cadência destrava portão.

---

## Seção 7 — Ganchos não caracterizados: PG5 e PG6 **[A CARACTERIZAR]**

Anotados no Passo C1 (D-C1.4) como **não ratificados** até serem caracterizados / o cluster de publicação pública (**C3**) entrar.

**[NORMATIVO — honestidade]:** a **substância** de PG5 e PG6 **não está fixada no corpus**, e o texto verbatim das propostas (`revisao-politicas-regras-v0.html`) **não estava acessível** no chat de redação. Por isso **não se inventa** o conteúdo de PG5/PG6 aqui: ficam como **espaços reservados** a preencher quando (a) o HTML for anexado e/ou (b) o C3 caracterizá-los. Registrar a lacuna é disciplina de PG7; preenchê-la por suposição violaria a tipagem epistêmica e o "nunca inventar" da Constituição.

---

## Changelog

| Versão | Data | O que mudou | Por quê | Documento |
|---|---|---|---|---|
| **v1.0** | 2026-06-21 | Criação do Playbook como documento próprio, a partir da estrutura do C1 §5.1. Populadas as Seções: protocolo um-passo-por-chat (§1, vigente — reconhecido em C1/D-C1.6), formato de handoff de 9 pontos + rodapé (§2, vigente), cadência de fatias e critério de "fatia fina o suficiente" (§3, vigente), ganchos diferidos PG3/PG4 (§4 → C2), fila de revisão como processo (§5 → C2/F1), recadência de fonte viva/SLAs/auditoria (§6 → E13/E14), e PG5/PG6 a caracterizar (§7). | Executar o Passo C1.1: transformar a estrutura ratificada no C1 em procedimento de governança vigente, iniciando o registro versionado e separando o que é vigente do que é diferido/a caracterizar. | Playbook |
| — | — | **Pendência leve registrada:** reconciliação **verbatim** de PG1–PG7 contra `revisao-politicas-regras-v0.html` (HTML fora do conhecimento, não acessível no chat de redação). Afeta sobretudo §4 (PG3/PG4) e §7 (PG5/PG6), cuja substância depende do texto literal. Quando anexado, caracterizar/ajustar e registrar aqui. | Honestidade de insumo (herdada de C1, R-C1.2/§9). | Playbook |

---

*Documento de governança do Passo C1.1, sob o `registro-prototipo-e-protocolo-continuidade`, o `estado-atual-e-roteiro`, a `analise-pendencias-atuais`, a política editorial (Etapa 3.1), o pipeline (Etapa 13), a operação/governança (Etapa 14) e os Passos B1, B2 e C1. Redige o Playbook a partir da estrutura do C1 §5.1 e popula seus procedimentos. Não altera nenhum invariante da Constituição (apenas a implementa), não reabre nenhuma etapa, não ratifica PG3/PG4 (diferidos → C2) nem caracteriza PG5/PG6 (a caracterizar → C3/HTML), não define os números de SLA/cadência (execução, E13/E14), não escreve código, não decide dados, e não redige a Constituição (documento irmão) nem o handoff (passo de fechamento). Pendência leve carregada: reconciliação verbatim de PG1–PG7 contra `revisao-politicas-regras-v0.html`. Próximo passo na Trilha C, quando solicitado: C2 — fila de revisão como processo (ratifica PG3/PG4 no nível operacional).*
