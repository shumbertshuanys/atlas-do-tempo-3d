# Estado atual e roteiro — Atlas do Tempo

**Natureza:** registro de estado + roteiro (âncora anti-perda). Complementa, sem substituir, a *Decisão de re-centragem da tese* e a *Análise de pendências atuais*. Segue a cadência evidence-first (governança P1) e serve ao pedido de "documentar para não nos perdermos" (governança P7). Data: revisão atual.

---

## 1. Onde estamos

- **Corpus conceitual:** completo — 28 documentos, Etapas 0–15, todos aprovados.
- **Tese:** re-centrada e documentada — *atlas tridimensional do espaço-tempo do conhecimento* (ponto no espaço + tempo + domínio → o que se sabe ali). "O que acontecia no mundo" é só a lente de eventos/história.
- **Governança:** revisão proposta (P1–P7), aguardando ratificação.
- **Pendências:** mapeadas e reclassificadas (backlog P01–P30 + 45 decisões `[PENDÊNCIA]` + ~156 tags de conteúdo). Nada bloqueia o protótipo; o cluster de publicação pública está identificado.
- **Protótipo:** construído **como rascunho** — prova a alma navegável, multiescala e multidomínio. Modelo de domínio-por-item corrigido (a lente filtra dentro do instante; lente vazia é informação).

---

## 2. Artefatos desta sessão (catálogo)

| Artefato | O que é | Status |
|---|---|---|
| `atlas-prototipo-3d.html` | Protótipo 3D: cosmos↔Terra dirigido pelo eixo do tempo; 1789 multidomínio; GOE/K-Pg posicionados | rascunho (sandbox) |
| `atlas-mvp-incremento-1.html` | Incremento 1 (frame 2D): eixo Ga→hoje, lente, globo esquemático, dossiê | rascunho |
| `atlas-1789-fatia-vertical.html` | Fatia vertical da cena 1789 (prova do gating epistêmico) | rascunho |
| `decisao-recentragem-tese-mvp-enxuto.md` | Decisão: tese re-centrada + escopo do MVP enxuto + plano de incrementos | vigente |
| `analise-pendencias-atuais.md` | Registro reclassificado de todas as pendências | vigente |
| `revisao-politicas-regras-v0.html` | Revisão de governança (P1–P7) | proposta, aguarda ratificação |
| `arquitetura-dados-diagrama.html` | Diagrama do modelo de persistência (núcleo-grafo + derivados + isolamento) | referência |

> **Nota de coerência:** os itens de química/física/geologia/vida de 1789 no protótipo são **semeados para demonstração** — não estão no corpus (a 4D é só história). Conteúdo multidomínio real é tarefa de modelagem (pendências F1/F2). Protótipo e corpus não devem divergir em silêncio.

---

## 3. Requisitos registrados (do usuário)

- **Esqueleto = tempo;** depois a **lente de domínio;** depois os **eventos do domínio**. Sempre nessa ordem.
- **Todo instante é atravessado por todas as lentes;** a lente filtra o instante, não troca de instante. **Lente vazia é informação** (ex.: história em 2,4 Ga).
- **Representações cósmicas bem-feitas** (requisito de fidelidade, para a produção): Big Bang, formação de estrelas, galáxias, formação da Terra e sua geologia precisam estar **bem representados** — não o esquemático atual.
- **"Bonito" = a interface do produto** (UI/UX 3D), não relatórios.
- **MVP enxuto:** vista única de exploração livre; sem versão estudante/professor, sem grade; gating sempre operando. Camadas de escola/usuário são upgrades.

---

## 4. Roteiro — três trilhas

### Trilha A — Experiência (protótipo → produto)
- **A1 · Incremento 2 (próximo passo recomendado):** povoar **GOE** (2,4 Ga, química/atmosfera) e **K-Pg** (66 Ma, geologia/vida) com itens reais, fiéis ao 4E/4G — o tempo profundo ganha a mesma riqueza multidomínio que 1789 tem agora. Ainda no sandbox, fidelidade de rascunho.
- **A2 · Teto do sandbox = inflexão para produção.** As representações cósmicas bem-feitas (requisito do §3) **não** cabem no sandbox. Esse é o gatilho para migrar.
- **A3 · Produção no Claude Code:** three.js completo, assets e shaders reais, cosmos/galáxias/Terra bem representados, navegação cinematográfica por estágios, e a degradação 3D→2D→estático. É aqui que a "puta interface" se constrói de verdade.

### Trilha B — Dados / fundação (deixar de ser descartável)
- **B1 · Decisão do motor de banco** (RDF* × property graph × relacional) — resolve a `[PENDÊNCIA]` E11→E12, agora **com os padrões reais de consulta do protótipo como evidência** (governança P3). Os dados do protótipo já são um *graph-seed* claim-first.
- **B2 · Reificação** de `Source` / `Claim` / `MediaAsset` (pendência F4) — o esquema para onde os dados do protótipo migram.

### Trilha C — Governança / conteúdo (a disciplina que evita a perda)
- **C1 · Ratificar P1/P2/P7** (meta, barato) — fixa "pronto = evidência", fatias como instrumento, e a separação Constituição/Playbook com changelog (o próprio antídoto contra se perder).
- **C2 · Fila de revisão como processo** (pendência F1) — caminho crítico de cobertura quando formos ao público.
- **C3 · Cluster de publicação pública** (F2 fonte/licença · F5 fundação escolar · F6 jurídico/LGPD) — adiado até sair do protótipo, mas no radar.

---

## 5. Sequência recomendada

1. **A1 — Incremento 2** agora (completa a prova multidomínio no tempo profundo; barato, no sandbox).
2. **Inflexão:** **B1** (decidir o motor) + **A3** (migrar para o Claude Code) — porque as representações cósmicas e a base real só existem fora do sandbox.
3. **Trilha C corre em paralelo** o tempo todo (ratificar P1/P7 já; o resto conforme avança para o público).

---

## 6. O que NÃO fazer (anti-perda)

- Não tentar **polir o cosmos no sandbox** — há um teto técnico; o lugar é o Claude Code.
- Não **publicar conteúdo semeado** sem a revisão do corpus.
- Não **construir camadas de usuário/escola** antes da alma estar pronta.
- Não deixar **protótipo e corpus divergirem** — cada conteúdo novo vira tarefa de modelagem registrada.

---

## 7. Âncora de coerência com o corpus

| Passo | Etapa / documento do corpus |
|---|---|
| A1 Incremento 2 | Etapas 4E (GOE) · 4G (K-Pg) · 5 (função) · 10 (UX) |
| A3 Produção 3D | Etapas 10 (Design/UX 3D) · 11 (Arquitetura) |
| B1 Motor de banco | Etapa 11 §4 → 12 (decisão diferida) |
| B2 Reificação | Etapas 2 (Knowledge Core) · 13 (pipeline) |
| C1 Governança | Revisão P1–P7 · Prompt-mestre |
| C2 Revisão | Etapas 3.1 (editorial) · 14 (operação) |
| C3 Publicação pública | Etapas 6 (compliance) · 11 · 14 |
