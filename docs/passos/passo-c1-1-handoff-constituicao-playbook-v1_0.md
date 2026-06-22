# Passo C1.1 — Redação da Constituição e do Playbook (handoff)

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** entrega do Passo **C1.1** (Trilha C). Dá sequência ao **C1** (governança vigente) redigindo a **Constituição** e o **Playbook** como **dois documentos próprios**, a partir da estrutura do **C1 §5.1**. Cadência de handoff dos 4Z/5Z.
**Data:** 2026-06-21.

---

## 1. Objetivo
Transformar a estrutura ratificada no C1 (§5.1) em **dois documentos de governança vigentes e versionados**: a Constituição (invariantes duros) e o Playbook (procedimento), iniciando o changelog v1.0 de cada um.

## 2. Escopo
Redação dos dois documentos; população dos invariantes/procedimentos; início dos changelogs; tentativa de reconciliação verbatim de PG1–PG7 contra o HTML; registro das pendências e diferimentos.

## 3. Diagnóstico
- A estrutura do **C1 §5.1**, a régua de alocação (§5.2) e as decisões D-C1.1–D-C1.6 foram recuperadas do handoff do C1 e são o insumo autoritativo.
- Os invariantes a popular foram conferidos na fonte: **P1–P10** (Etapa 2 §1.2), **[N1]–[N5]** (Passo B1 §3.2, sobre a Etapa 11), **invariante de exibição** (Etapa 11, inv. 9 / §7.5), **tipagem epistêmica** (Etapa 2 P8; Etapa 3.1), e os reforços do **B2** (backbone `entity_node`; proveniência como FK; isolamento de licença; depreciação-não-apaga).
- **Achado de insumo (decisivo):** o HTML `revisao-politicas-regras-v0.html` **não está acessível** — ausente do diretório do projeto, dos uploads deste chat e de todo o ambiente. Confirmado por busca direta. Isso bate com o que o próprio C1 já registrara (R-C1.2/§9): o HTML é arquivo mantido **fora** do conhecimento do projeto.

## 4. Decisões principais
- **D-C1.1.1 — Proceder pela substância ratificada, não pelo texto literal.** Como o HTML é inacessível, a **reconciliação palavra a palavra de PG1–PG7 não foi executada**. Os documentos populam PG1/PG2 pela substância do C1 (suficiente para o ato de redigir/ratificar); a reconciliação verbatim segue **pendente** e está no changelog dos dois documentos. *Não inventar o texto literal é coerente com a Constituição (Art. 6, "nunca inventar").*
- **D-C1.1.2 — Constituição com 14 artigos em 7 títulos.** Tese (Art. 1), separação de camadas + direção única (Art. 2), P1–P10 (Art. 3), [N1]–[N5] (Art. 4), invariante de exibição (Art. 5), tipagem epistêmica (Art. 6), proveniência como FK (Art. 7), isolamento de licença (Art. 8), depreciação-não-apaga (Art. 9), PG1 (Art. 10), PG2 (Art. 11), régua (Art. 12), regra de emenda (Art. 13), desambiguação PG/P (Art. 14). Cada artigo traz origem e teste constitucional.
- **D-C1.1.3 — Playbook com estatuto por seção.** §1 protocolo um-passo-por-chat [VIGENTE], §2 formato de handoff [VIGENTE], §3 cadência de fatias + critério de "fatia fina o suficiente" [VIGENTE], §4 PG3/PG4 [DIFERIDO → C2], §5 fila de revisão [DIFERIDO → C2/F1], §6 recadência de fonte viva/SLAs/auditoria [DIFERIDO → E13/E14], §7 PG5/PG6 [A CARACTERIZAR].
- **D-C1.1.4 — PG5/PG6 ficam como espaços reservados.** Sua substância não está no corpus e o HTML é inacessível; preenchê-los por suposição violaria a tipagem epistêmica. Caracterização fica para C3 / anexação do HTML.
- **D-C1.1.5 — Changelog v1.0 iniciado em ambos**, no formato `versão | data | o que mudou | por quê | documento`, com a pendência verbatim registrada como linha própria.

## 5. Modelo conceitual
Dois documentos + um changelog cada, sob a régua do Art. 12:
```
CONSTITUIÇÃO (raramente muda) ── Títulos I–VII, Arts. 1–14 ── changelog
PLAYBOOK     (muda sempre)     ── §§1–7 (vigente/diferido/a caracterizar) ── changelog
relação: Playbook IMPLEMENTA a Constituição; em conflito, a Constituição vence.
```

## 6. Fontes / insumos
Corpus: C1 (§5.1/§5.2; D-C1.1–D-C1.6), Etapa 2 (§1.2; P8; §10), Etapa 3.1, Etapa 11 (inv. 9; §4.2; §7.5; §9), Etapa 13/14 (versionamento, rollback, QA gates), Passos B1 (§3.2 [N1]–[N5]) e B2 (`entity_node`; D-B2.2/4/6), `registro-prototipo`, `estado-atual-e-roteiro`, `analise-pendencias`.
**Insumo ausente:** `revisao-politicas-regras-v0.html` (texto verbatim PG1–PG7).

## 7. Riscos
| Risco | Descrição | Mitigação |
|---|---|---|
| R-C1.1.1 | Ratificar/redigir **sem o texto verbatim** e divergir do original | Pendência verbatim registrada nos dois changelogs; emenda (Art. 13) prevista ao anexar o HTML |
| R-C1.1.2 | PG5/PG6 serem preenchidos por suposição | Mantidos como [A CARACTERIZAR]; "nunca inventar" (Art. 6) |
| R-C1.1.3 | Constituição inchar (procedimento virar invariante) | Régua do Art. 12 aplicada artigo a artigo; como-fazer foi para o Playbook |
| R-C1.1.4 | Documentos derivarem em silêncio | Changelog obrigatório em ambos; nada muda sem registro |

## 8. Entregáveis
1. **`constituicao-atlas-do-tempo-3d-v1_0.md`** — 14 artigos, 7 títulos, changelog v1.0.
2. **`playbook-operacional-atlas-do-tempo-3d-v1_0.md`** — 7 seções com estatuto, changelog v1.0.
3. **Este handoff** — registro do passo, pendências e próximos passos.

## 9. Próximos passos
- **Reconciliação verbatim (quando o HTML for anexado):** conferir PG1/PG2 palavra a palavra contra os Arts. 10–11; caracterizar PG5/PG6; emendar e registrar nos changelogs se houver divergência.
- **C2 — fila de revisão como processo** (F1): ratifica **PG3** (operar na fatia) e **PG4** (Definition of Ready) no nível operacional; define dono, cadência e papéis (preenche §4 e §5 do Playbook).
- **C3 — cluster de publicação pública** (F2/F5/F6): caracteriza PG5/PG6 se ainda pendentes.
- **Operacional permanente:** seguir rodando **cada chat sob a Constituição + o Playbook** — um passo, por evidência, com handoff salvo.

---

*Documento de entrega do Passo C1.1, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14) e os Passos B1, B2 e C1. Redige a Constituição e o Playbook como documentos próprios a partir da estrutura do C1 §5.1, popula seus invariantes/procedimentos e inicia o changelog v1.0 de cada um. Não altera nenhum invariante do corpus (apenas os reúne e fixa), não reabre nenhuma etapa, não ratifica PG3/PG4 nem caracteriza PG5/PG6, não define números de SLA/cadência, não escreve código e não decide dados. Pendência leve carregada e registrada nos dois changelogs: reconciliação verbatim de PG1–PG7 contra `revisao-politicas-regras-v0.html`, inacessível no chat de redação — a executar quando o arquivo for anexado. Próximo passo na Trilha C, quando solicitado: C2 — fila de revisão como processo.*
