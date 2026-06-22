# Playbook Operacional do Atlas do Tempo 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** documento de **procedimento operacional** — o **como-fazer**. É a metade que **muda com frequência** da separação ratificada em **PG7** (C1, D-C1.3). Sua contraparte é a **Constituição** (invariantes duros). O Playbook **implementa** os invariantes da Constituição; **nunca os afrouxa nem os contradiz**.
**Estatuto das cláusulas:** marcado por seção — **[VIGENTE]** (em uso agora), **[DIFERIDO]** (gancho registrado, dono e etapa indicados) ou **[DIFERIDO — substância conhecida]** (caracterizado, mas com ratificação operacional adiada). Mudança aqui é **esperada e rotineira**, sempre registrada no changelog.
**Origem:** redigido no Passo **C1.1** a partir da estrutura do **C1 §5.1**, sob o `registro-prototipo-e-protocolo-continuidade`, o `estado-atual-e-roteiro`, a `analise-pendencias-atuais`, a política editorial (Etapa 3.1), o pipeline (Etapa 13) e a operação/governança (Etapa 14).
**Versão:** **v1.1** — **Data:** 2026-06-21. (v1.0 → v1.1: PG5/PG6 caracterizados; PG3/PG4 afinados; referências à Constituição atualizadas; pendência verbatim fechada — ver changelog.)

> **Nota de reconciliação (v1.1).** O texto verbatim das propostas de governança foi **recuperado** do chat de autoria *"Análise e status do projeto"* (onde `revisao-politicas-regras-v0.html` foi gerado) e conferido. Isso **fechou** a pendência leve do v1.0 e permitiu **caracterizar PG5 e PG6** — que o v1.0 marcara, por engano, como "a caracterizar". As referências de artigo apontam agora à **Constituição v1.1**.

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

*Implementa:* PG1 (cada passo fecha por evidência), PG2 (cada passo é uma fatia), PG7 (handoff = registro anti-deriva). *Precedentes vivos:* encerramentos 4Z/5Z; Passos B1, B2 e C1.

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

---

## Seção 4 — Ganchos diferidos: PG3 e PG4 **[DIFERIDO → C2]**

Diferidos no Passo C1 (D-C1.4). **Registrados, não operantes.** Pertencem à conversão da fila de revisão em processo (**C2**, pendência F1). Redação **conferida verbatim** na reconciliação v1.1.

- **PG3 — Operar a governança em escala-fatia antes de escalar** *(estende Etapa 14)*. **Hoje:** a E14 especifica filas, SLAs e riscos para "depois do MVP e do pipeline real". **Fricção:** governança riquíssima que ainda não tocou um único item. **Proposta:** instanciar a **menor versão real** dos invariantes da E14 sobre os ~24 itens da fatia — `readinessStatus` aplicado de verdade, `gatingReason` anexado, uma fila de revisão real com esses itens. *"Operar 24 antes de 24 mil."* **Ganho:** a E14 prova que prende a realidade em pequena escala, antes do custo de escalar. *A ratificar em C2.*
- **PG4 — Um "Definition of Ready" para o item publicável** *(estende Etapas 2 + 3.1)*. **Hoje:** claim-first é regra, mas o **contrato mínimo** de entrada em revisão não está fixado como porta. **Fricção:** cada item exige claim tipado + fonte + texto por faixa etária + tag de sensibilidade + ClaimSet-com-fronteira se controverso; descobrir item a item é caro e tardio. **Proposta:** um **DoR** — campos mínimos obrigatórios — que um claim precisa cumprir para entrar na fila; **sem DoR, não entra**. **Ganho:** revisão previsível; o custo editorial aparece no planejamento, não na surpresa. *A ratificar em C2.* Complementa o "pronto = evidência" (PG1, que é a Definition of **Done**).

**[NORMATIVO]:** enquanto diferidos, PG3/PG4 **não** alteram o método vigente; seu diferimento é, em si, disciplina de PG7.

---

## Seção 5 — Fila de revisão como processo **[DIFERIDO → C2, pendência F1]**

Hoje a fila de revisão é **backlog sem dono nem cadência**; é o **caminho crítico de cobertura** quando o produto for ao público (`analise-pendencias` §5, F1). O C2 deve produzir:
1. **Dono** — quem conduz a fila (sem decidir mérito fora de competência).
2. **Cadência** — com que ritmo itens entram, são revisados e saem.
3. **Papéis de revisão** — científica, historiográfica, pedagógica, faixa etária, jurídica, acessibilidade, mídia, vieses (Etapa 3.1 §9; Etapa 14 §3) como **pré-requisito de publicação**.
4. **Não-automação da fronteira** — a fronteira "sem equivalência" de cada `ClaimSet` é **escrita à mão**; a fila não a automatiza.

**[NORMATIVO]:** nada nesta seção pode contornar o **invariante de exibição** (Constituição, Art. 6): item não revisado **não** vira fato por pressão de fila. E vale o **Art. 13** (QA bloqueia; escala não reduz revisão): capacidade insuficiente **pausa a admissão**, não rebaixa a revisão.

---

## Seção 6 — Recadência por fonte viva, SLAs e amostragem de auditoria **[DIFERIDO → quando operar, E13/E14]**

Procedimentos finos de operação, definidos **quando o pipeline operar** (Etapas 13/14). Registrados aqui como ganchos:
1. **Recheck de fonte viva** — cadência por classe de fonte (frequente para fontes vivas; periódica para estáveis); mudança de fonte **cria nova versão de `Source` + novo `DatasetSnapshot` imutável**; **jamais** atualização silenciosa (implementa Constituição, Art. 12).
2. **SLAs por fila** — prazos de atendimento por papel/fila; números são **[PENDÊNCIA]** de execução.
3. **Amostragem de auditoria** — limiares de amostragem de revisões e auditorias periódicas; trilha de decisão grava ator, data e `gatingReason`.
4. **Rollback versionado** — opera por **depreciação + restauração** da versão anterior; **nada é apagado** (implementa Constituição, Art. 12).

**[NORMATIVO]:** `qaGateResult` tem **dois** valores (`pass`/`fail`) — **sem** `waived`/`override`. QA **bloqueia**, não sugere. Nenhum SLA ou cadência destrava portão. Estes são os **mecanismos** do invariante constitucional **Art. 13**; o invariante é soberano, os números são do Playbook.

---

## Seção 7 — PG5 e PG6: caracterizados **[DIFERIDO — substância conhecida]**

**Correção v1.1:** o v1.0 marcara PG5/PG6 como "a caracterizar" por ausência do texto. Com a recuperação verbatim, eles estão **caracterizados** abaixo. Permanecem **diferidos** para ratificação operacional (não entram em vigor agora), mas a substância está fixada.

- **PG5 — Pré-classificar sensibilidade na modelagem, não na revisão** *(estende Etapas 2 + 3.1)*. **Hoje:** a sensibilidade (Leis 10.639/11.645) é tratada **na revisão**; uma proporção grande dos itens cai em `pending` e se descobre um a um. **Fricção:** o *split* público/mediado de uma cena só é conhecido **depois** de construí-la. **Proposta:** uma **taxonomia de sensibilidade aplicada na hora da modelagem** → o backlog de revisão e a proporção pública passam a ser **previsíveis antes do build**. **Ganho:** "descoberta" vira "planejamento". *Diferido — a aplicar/ratificar **ao retomar a modelagem de cenas** (liga-se a C2/F1).*
- **PG6 — ClaimSet e mapa esquemático viram contratos normativos de marca** *(estende Etapas 3.1 + 10)*. **Hoje:** "sem equivalência" e "mapa esquemático" existem como prática e descrição conceitual. **Fricção:** ambos são **decisões de produto**, não detalhes — a fronteira escrita à mão do `ClaimSet` é o *moat*; o mapa esquemático é epistemicamente **superior** a fronteiras inventadas. **Proposta:** elevá-los a **regra normativa com contrato visual** — `ClaimSet` sempre com fronteira moral/factual explícita + resumo por faixa etária; mapa esquemático rotulado por padrão, fronteira histórica **nunca inventada**. **Ganho:** o diferencial deixa de ser implícito e vira padrão obrigatório. *Diferido → **C3** (cluster público) e à camada de **UX** (Etapa 10).*

**[NORMATIVO]:** o **núcleo epistêmico** de PG6 (ClaimSet sempre com fronteira; nunca inventar geometria/fronteira) **já é constitucional** — Constituição, Art. 7. O que PG6 adiciona, e o que fica diferido, é a camada de **contrato visual / padrão-de-marca** (como isso se apresenta na UX), própria do Playbook/Etapa 10. PG6 não pode, em hipótese alguma, ser lido como permissão para enfraquecer o Art. 7.

---

## Changelog

| Versão | Data | O que mudou | Por quê | Documento |
|---|---|---|---|---|
| **v1.1** | 2026-06-21 | **§7 reescrita:** PG5 e PG6 deixam de ser "[A CARACTERIZAR]" e passam a **caracterizados** (redação verbatim recuperada), reclassificados **[DIFERIDO — substância conhecida]**; PG6 cruza-referência a Constituição Art. 7. **§4 afinada:** PG3 (operar a E14 em escala-fatia, "operar 24 antes de 24 mil") e PG4 (DoR, "sem DoR, não entra") ganham a redação verbatim. **Referências cruzadas atualizadas** à Constituição v1.1 (Art. 6 exibição, Art. 12 versionamento/degradação, Art. 13 QA, Art. 16/17 PG2/régua). **§1 e §3** registram a recuperação do arquivo como prova viva do protocolo. | A recuperação verbatim do `revisao-politicas-regras-v0.html` corrigiu o engano do v1.0 (PG5/PG6 ditos não-caracterizados) e fechou a pendência. | Playbook |
| **v1.1** | 2026-06-21 | **Pendência resolvida:** reconciliação verbatim de PG1–PG7 **fechada**. Resíduo não-normativo (CSS, cabeçalho do HTML, linha "Ganho" de PG7) não recuperado e sem efeito sobre o procedimento. | Encerrar honestamente a pendência do v1.0. | Playbook |
| **v1.0** | 2026-06-21 | Criação do Playbook como documento próprio, a partir da estrutura do C1 §5.1 (§§1–7: protocolo um-passo-por-chat, formato de handoff, cadência de fatias, PG3/PG4 diferidos, fila de revisão, recadência de fonte viva, PG5/PG6). | Executar o Passo C1.1. | Playbook |

---

*Documento de governança do Passo C1.1 (v1.1), sob o `registro-prototipo-e-protocolo-continuidade`, o `estado-atual-e-roteiro`, a `analise-pendencias-atuais`, a política editorial (Etapa 3.1), o pipeline (Etapa 13), a operação/governança (Etapa 14) e os Passos B1, B2 e C1. Caracteriza PG5/PG6 com a redação verbatim recuperada, afina PG3/PG4, atualiza as referências à Constituição v1.1 e encerra a pendência de reconciliação verbatim. Não altera nenhum invariante da Constituição (apenas a implementa), não reabre nenhuma etapa, não ratifica PG3/PG4/PG5/PG6 (seguem diferidos), não define os números de SLA/cadência (execução, E13/E14), não escreve código, não decide dados. Próximo passo na Trilha C, quando solicitado: C2 — fila de revisão como processo (ratifica PG3/PG4 e aplica PG5 no nível operacional). Supersede o v1.0.*
