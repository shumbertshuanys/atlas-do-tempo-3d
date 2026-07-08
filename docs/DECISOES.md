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

## D-20260703-06 — (retroativa) Virada ao vivo do frame 3D

**Decisão:** o frame de produção (`frame/atlas-3d-frame-v1.html`) consome a API
só-leitura (`/momento/publico`, papel `atlas_public`) via `fromEnvelope`; gates
da UI re-mapeados a papel/endpoint (OFF→porta pública; ON→curatorial, token só
localhost); comutador de fonte array⇄API com fallback honesto ao espelho
estático se a API cair. Executada em jun–jul/2026 (D-A3.virada).
**Porquê:** extinguir por construção a divergência frame↔corpus.
**Evidência:** LIVE-T 4/4. **Revoga:** o espelho estático como fonte primária
do frame (permanece só como fallback/offline).

## D-20260703-07 — (retroativa) Cósmicos como corpus com fonte (Abordagem 2)

**Decisão:** 5 âncoras cósmicas (`evt:big-bang`, `state:cmb-recombinacao`,
`proc:formacao-galaxias`, `evt:formacao-sistema-solar`, `proc:formacao-terra`)
entram no `migrate.py` como corpus/approved/públicos, com fonte ([N1]),
`sourceTimeBasis=Ga`, sem geometria terrestre; nenhum é `fato-documentado`
(CMB = `medição-direta`; demais = `inferência-científica`); sem ClaimSet.
**Porquê:** o estágio cósmico vinha vazio na porta pública; teasers `rep:*`
sem lastro violavam o piso epistêmico.
**Evidência:** COSMO-T 5/5 + re-verde das demais suítes.
**Revoga:** os teasers `rep:*` sem fonte no espelho estático.

## D-20260703-08 — (retroativa) F-A.3 (mídia cósmica real) assinada; execução pendente

**Decisão:** aprovado o plano da mídia cósmica real: envelope `011` estende
`media[]` (padrão aditivo); cadência 5 de uma vez; CMB reforçado com
claim-sobre-asset; `natureLabel` por asset (Big Bang/Terra =
`representação-artística` · CMB = `mapa` · galáxias/sistema solar =
`fotografia` com legendas de look-back/análogo); licença por asset no portão;
cena sempre esquemática (asset só no dossiê, nunca textura); suíte `MEDIA-T1..5`.
Execução começa por sub-checagem read-only do DDL.
**Docs:** `docs/arquivo/passos/plano-cosmicos-midia-real-f-a3-v1_0.md` e
`docs/arquivo/passos/f-a3-decisoes-assinadas-handoff-execucao-v1_0.md`.
**Revoga:** nada; frente técnica seguinte.

## D-20260703-09 — (retroativa) Segredos Opção A (12-factor); Opção B adiada para E14

**Decisão:** credenciais saem do código para `.env` gitignored (`.env.example`
documenta as 4 vars); `docker-compose` interpola `${ATLAS_DB_PASSWORD:?}`;
bootstrap e serviço RECUSAM subir sem as vars. Gerenciador de segredos com
rotação/auditoria/RIPD (Opção B) e auth real da porta curatorial ficam para a
E14.
**Porquê:** tirar segredo do código já; rotação/auditoria exigem
infraestrutura que o MVP enxuto ainda não justifica.
**Revoga:** senhas embutidas em código/compose.

## D-20260703-10 — Revogação do achado "histórico git = 1 commit-monstro"

**Decisão:** revogar a dívida "histórico git = 1 commit-monstro" — era **falso
positivo de clone raso** (`--depth 1`): o clone usado pela auditoria só via o
commit `3c37714` ("Snapshot..."); o histórico real do repo já era composto de
commits lógicos anteriores (ex.: `b16af7e`, `8ffc802`, `375b09f`, `8005767`).
Nada a corrigir no histórico; R5/R6 seguem valendo daqui em diante.
**Corrige especificamente:** a dívida 2 do `docs/ESTADO.md` (versão de
2026-07-03, Chat 1) e o achado "Histórico git = 1 commit-monstro" da auditoria
arquivada em `docs/arquivo/auditorias/auditoria-jul-2026.md` — a auditoria NÃO
é editada (documento histórico, não-normativo); esta entrada é a correção.
**Revoga:** a dívida 2 do ESTADO.md de 2026-07-03 e o achado correspondente da
auditoria.

## D-20260707-01 — Kit de validação de demanda (Chat 3); critérios pré-registrados

**Decisão:** adotado o kit de validação com professores reais em `docs/validacao/`
(roteiro de demo de 10 min sobre o frame, guia de entrevista semiestruturada,
critérios de sinal/invalidação, perfil-alvo dos 5, ficha-template + consolidado).
A demo roda na porta PÚBLICA por padrão (Caminho A); face curatorial só-pending
(Caminho B) é opcional, local, e nunca liga seeded. Critérios de invalidação ficam
PRÉ-REGISTRADOS antes das conversas: em caso ambíguo, as camadas educacionais
(Etapas 6–9) NÃO reabrem; vereditos separados para tese/função central × camadas.
O veredito pós-conversas entra como nova entrada aqui, com as 5 fichas de
`docs/validacao/` como evidência (PG1).
**Porquê:** demanda não validada é o risco nº 1 (auditoria jul/2026); fixar o
critério antes das conversas evita mover a trave depois (anti-Goodhart).
**Revoga:** nada. Instrumenta a prioridade (a) do ESTADO.md.

## D-20260707-02 — Spec do laço de ingestão assistida (Tier 0/1)

**Decisão:** adotar `docs/ingestao/spec-laco-ingestao.md` (Chat 4) como desenho
normativo do laço IA-rascunha → humano-revisa, executando D-20260703-03. Fixa:
pacote de ingestão como unidade; "item revisado" por tier (T0 = checklist
integral por todos os papéis aplicáveis; T1 = 100% de validação automática +
amostra do lote com zero defeito crítico, lote inteiro devolve em falha);
cronometria só por timestamps de ferramenta em manifesto append-only;
número-decisor = **minutos humanos por item aprovado, por tier**; validação
automática que BLOQUEIA (Art. 13); triagem conservadora com PG5 — na dúvida,
Tier 0 (Art. 9); promoção humana que materializa na **carga do repo** (banco
permanece derivado do git — R1); IA estruturalmente impedida de escrever
`claim`/`source`/`review_status` (campos inexistentes no formato de rascunho +
teste negativo). Sensível (PG5 ≠ `público`) só chega a `approved` com papel
competente designado por entrada aqui; até lá promove no máximo a `pending` e
junta-se à fila viva.
**Revoga:** nada; instrumenta D-20260703-03 e destrava o Chat 5 (implementação
v0 + medição de itens/hora).
