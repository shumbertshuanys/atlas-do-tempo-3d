# DECISÕES — Atlas do Tempo 3D

> Log append-only (regra R2). Nunca editar entrada antiga; correção = nova entrada
> que revoga a anterior. Formato: D-AAAAMMDD-NN · decisão · porquê · o que revoga.

---

## D-20260702-01 — Auditoria técnica externa do projeto

**Decisão:** aceitar o resultado da auditoria (claude.ai, jul/2026) como base do
replanejamento. Síntese: núcleo epistêmico (esquema reificado, invariantes como
CHECK/FK, gating por construção) está correto e verificado — preservar intacto;
o aparato conceitual (15 etapas, playbook, handoffs, ~20 mil linhas de markdown
para ~2,3 mil de código e 40 itens) está superdimensionado — congelar; os dois
riscos de vida ou morte estão abertos: demanda não validada e escala de conteúdo.
**Registro completo:** `docs/arquivo/auditorias/auditoria-jul-2026.md`.
**Revoga:** nada; fundamenta as entradas seguintes.

## D-20260703-01 — Congelamento das etapas conceituais e fim dos documentos de processo

**Decisão:** Etapas 0–15 estão CONCLUÍDAS COMO CONCEITO e CONGELADAS. Proibido
produzir novo documento de etapa, playbook, handoff ou registro narrativo de
execução. Execução se registra em commit + report gerado por script; decisão se
registra aqui em 5–10 linhas. As camadas educacionais (Etapas 6–9) reabrem
somente com demanda validada (Chat 3+).
**Porquê:** razão prosa/código de ~9:1; o processo estava consumindo o produto.
**Revoga:** o fluxo "trabalhe por etapas" das instruções v1 e a prática de
handoff/encerramento por sessão.

## D-20260703-02 — Regras estruturais R1–R8 (normativas a partir desta data)

**Decisão:** adotar as regras abaixo; serão gravadas no `CLAUDE.md` no Chat 2,
revogando as seções correspondentes do playbook v1.3. Até lá, este registro é a
fonte normativa.

- **R1 — Fonte única de verdade.** O git é a verdade. Projeto claude.ai e
  memórias de chat são espelhos; em conflito, o repo vence.
- **R2 — Só quatro documentos vivos.** `README.md` (visitante, 5 min),
  `CLAUDE.md` (contrato operacional), `docs/ESTADO.md` (estado + próxima missão),
  `docs/DECISOES.md` (este log). Todo o resto vive em `docs/arquivo/` como
  histórico não-normativo. Exceção operacional: filas de trabalho vivas
  (ex.: `docs/fila-revisao-claimsets-sensiveis.md`).
- **R3 — Fim do arquivo-por-versão.** Proibido criar `*-v1_1.md` novo: documento
  vivo é um arquivo só, versionado pelo git.
- **R4 — Fim do handoff/registro narrativo.** Execução → commit + report JSON de
  script. Decisão → entrada aqui. Continuidade entre sessões → ler `ESTADO.md`.
- **R5 — Commits lógicos com formato fixo.** `tipo(escopo): resumo` em PT-BR;
  tipos: `dados | esquema | leitura | frame | api | docs | infra | teste`.
  Um commit = uma mudança lógica.
- **R6 — Evidência viaja com a mudança.** Commit que altera carga/esquema/leitura
  inclui NO MESMO COMMIT os reports regenerados e o README ajustado. Código,
  relatório e README divergentes = commit inválido.
- **R7 — Anti-inflação.** Nenhum documento conceitual novo sem pedido explícito
  do dono. Métrica de saúde: markdown novo ≤ código+dados novos no período.
- **R8 — Sincronização de espelhos.** Sessão que alterar documento vivo no repo
  atualiza a cópia no projeto claude.ai antes de encerrar (≤6 arquivos, 2 min).

**Revoga:** seções de processo do playbook v1.3 (que passa a histórico em
`docs/arquivo/`).

## D-20260703-03 — Modelo C: IA/RAG somente na ingestão; revisão tierizada

**Decisão:** adotar o modelo híbrido. O runtime responde EXCLUSIVAMENTE do banco
canônico gateado; LLM+recuperação atuam como assistentes de INGESTÃO (achar
fontes candidatas, rascunhar claims/tipagem/correspondência moderna), sempre
entrando como `pending` com portão humano. Tierização da revisão:
**Tier 0** (sensível, contestado, tempo profundo, ClaimSets, pessoas vivas) =
revisão humana especializada plena, fronteira escrita à mão;
**Tier 1** (fato consensual, bem documentado, fonte A) = IA rascunha, validação
automática de binding fonte↔claim + amostragem humana.
**Porquê:** RAG em tempo de consulta não garante proveniência, gating nem
não-falsa-equivalência — passivo jurídico em produto para menores; revisão
humana plena universal não escala (40 itens consumiram o projeto).
**Revoga:** a exigência implícita de fluxo humano pleno (20 etapas) para TODO
item da Etapa 13; o piso Tier 0 permanece integral.

## D-20260703-04 — Instruções do projeto claude.ai v2.1 e hierarquia de contexto

**Decisão:** substituídas as instruções v1 pela v2.1 (identidade estável +
invariantes + ponteiros; sem roteiro de etapas). Hierarquia de contexto:
instruções = o que é estável; arquivos do projeto = espelhos dos vivos;
repo = verdade completa, clonado em chats de decisão/execução.
**Revoga:** instruções v1 ("prompt-mestre", arquivada no repo) e o formato
obrigatório de resposta em 9 seções.

## D-20260703-05 — Consolidação documental e limpeza do projeto claude.ai

**Decisão:** criar `docs/ESTADO.md` e `docs/DECISOES.md`; mover histórico para
`docs/arquivo/` (etapas, passos, playbooks, constituição v1.0, roteiro absorvido
pelo ESTADO.md); commitar os 2 órfãos (`encerramento-*.md`); manter viva a
Constituição v1.1. Projeto claude.ai reduzido a ≤6 espelhos: ESTADO.md,
DECISOES.md, CLAUDE.md, constituição v1.1, auditoria-jul-2026.md, fila de
claimsets sensíveis.
**Porquê:** 70 arquivos no projeto faziam a busca devolver regra revogada
(4 playbooks, 2 constituições) e o espelho do CLAUDE.md já divergia 465 linhas
do repo.
**Revoga:** a prática de espelhar todo o histórico no projeto claude.ai.
