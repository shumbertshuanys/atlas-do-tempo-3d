# Passo C1.1 — Addendum: recuperação verbatim + emenda de fidelidade v1.1

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** addendum ao handoff do Passo **C1.1**. Registra (a) a **recuperação verbatim** do `revisao-politicas-regras-v0.html` e (b) a **emenda de fidelidade v1.1** da Constituição e do Playbook que dela resultou. Cadência de handoff dos 4Z/5Z.
**Data:** 2026-06-21.

---

## 1. O que aconteceu

A pergunta "dá para reconstituir o arquivo pendente?" levou a uma busca no histórico do projeto. **Achado:** o `revisao-politicas-regras-v0.html` **não estava perdido** — foi gerado por mim no chat de autoria *"Análise e status do projeto"* (21 jun). Seu conteúdo foi **recuperado verbatim** de lá: os dez invariantes do piso epistêmico, a regra de ouro, os sete cartões PG1–PG7 (Hoje/Fricção/Proposta/Ganho), os riscos, os próximos passos e o rodapé.

**Resíduo não recuperado** (e por isso o arquivo reconstituído é "content-faithful, estilo refeito"): o CSS original, o cabeçalho/diagnóstico de abertura, e a linha "Ganho" do cartão PG7. **Nada disso é normativo** — não afeta a governança.

## 2. O que a reconciliação revelou

1. **PG5 e PG6 ESTAVAM definidos** no original — o v1.0 os marcara, por engano, como "a caracterizar":
   - **PG5** — pré-classificar sensibilidade (Leis 10.639/11.645) **na modelagem**, não na revisão.
   - **PG6** — `ClaimSet` + mapa esquemático como **contratos normativos com contrato visual** (fronteira sempre explícita; mapa rotulado; fronteira nunca inventada).
2. **O "piso epistêmico" do original listava invariantes que o v1.0 da Constituição não transcrevera** — embora já vinculantes em E11/E14/E1.1/E2: Wikidata-índice-não-autoridade; forma-muda-fato-não; regra de ouro (na dúvida, bloqueio); QA-bloqueia/escala-não-reduz-revisão; minimização-máxima-de-menores; degradação-não-remove-o-piso.
3. **PG1/PG2 conferem**, com afinações verbatim: PG1 = "≥ 1 artefato **falsificável**"; PG2 = guarda *throwaway* ("não vira base nem entra no KC").

## 3. Decisões

- **D-C1.1.6 — Reconstituir o arquivo, rotulado.** Emitido `revisao-politicas-regras-v0-reconstituido.html` (estático, sem JS), com **banner de proveniência** declarando o que é verbatim e o que foi refeito. Não sobrescreve o "v0" original.
- **D-C1.1.7 — Emenda de fidelidade v1.1, não substantiva.** Os invariantes restaurados **já eram ratificados** (constavam do piso do documento de origem) e **já vinculantes** no corpus; o v1.0 apenas não os transcreveu. Logo é **versão menor** (errata), coerente com a Constituição Art. 18 — **nenhum artigo teve o sentido alterado, nenhuma restrição nova foi introduzida**.
- **D-C1.1.8 — Pendência verbatim encerrada.** A reconciliação palavra-a-palavra de PG1–PG7 (aberta no v1.0) está **fechada**.

## 4. Entregáveis

1. **`revisao-politicas-regras-v0-reconstituido.html`** — o arquivo reconstituído (conteúdo verbatim, estilo refeito, banner de proveniência).
2. **`constituicao-atlas-do-tempo-3d-v1_1.md`** — 19 artigos; Título VI novo (qualidade/privacidade); Arts. 5, 8, 9, 13, 14 restaurados + Art. 12 expandido; PG1/PG2 afinados; mapa de renumeração v1.0→v1.1 no changelog. **Supersede o v1.0.**
3. **`playbook-operacional-atlas-do-tempo-3d-v1_1.md`** — §7 com PG5/PG6 caracterizados; §4 PG3/PG4 afinados; referências à Constituição v1.1; pendência fechada. **Supersede o v1.0.**
4. **Este addendum.**

## 5. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| R-C1.1.5 | v1.0 e v1.1 coexistirem no projeto e confundirem | v1.1 **supersede** v1.0 explicitamente; substituir os arquivos v1.0 pelos v1.1 |
| R-C1.1.6 | Renumeração dos artigos quebrar referências do handoff C1.1 (v1.0) | Mapa de renumeração v1.0→v1.1 no changelog da Constituição |
| R-C1.1.7 | "Errata v1.1" ser lida como afrouxamento | Ao contrário: a v1.1 **acrescenta** rigor (privacidade de menores, QA bloqueia); nenhum invariante foi relaxado |

## 6. Próximos passos

- **Substituir** no projeto os arquivos v1.0 da Constituição e do Playbook pelos **v1.1**; guardar o `...-reconstituido.html` como arquivo (não no conhecimento, como qualquer protótipo).
- **C2 — Fila de revisão como processo** (F1): ratifica **PG3/PG4** e aplica **PG5** no nível operacional; define dono, cadência e papéis.
- **C3 — Cluster de publicação pública** (F2/F5/F6): caracteriza/ratifica **PG6** com a UX (Etapa 10).
- **Operacional permanente:** cada chat sob a **Constituição v1.1 + o Playbook v1.1** — um passo, por evidência, com handoff salvo.

---

*Addendum ao handoff do Passo C1.1, sob a baseline v1.0 (Etapa 0), a política editorial (Etapa 3.1), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14) e os Passos B1, B2 e C1. Registra a recuperação verbatim do `revisao-politicas-regras-v0.html` a partir do chat de autoria e a emenda de fidelidade v1.1 da Constituição e do Playbook (invariantes de piso restaurados, PG5/PG6 caracterizados, PG1/PG2 afinados, pendência verbatim encerrada). Não introduz invariante novo nem altera o sentido de nenhum artigo (versão menor, Constituição Art. 18); não reabre etapa; não ratifica PG3/PG4/PG5/PG6 (seguem diferidos); não escreve código; não decide dados. Próximo passo na Trilha C, quando solicitado: C2 — fila de revisão como processo.*
