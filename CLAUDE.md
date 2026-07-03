# Atlas do Tempo 3D — Memória do projeto

> Este arquivo é lido automaticamente pelo Claude Code no início de cada sessão.
> Ele é o **contrato operacional estável** do projeto: o que é o projeto, invariantes,
> regras e como rodar. O **estado mutável** mora em `docs/ESTADO.md` (ler ao retomar);
> decisões em `docs/DECISOES.md` (log append-only).
> Responda sempre em **português do Brasil**.

---

## 1. O que é o projeto

Um **atlas temporal 3D** científico-histórico para a educação brasileira: linha do tempo no
topo, globo/mapa 3D no centro, navegação por ano/período/evento/região, e a função central
**"O que acontecia no mundo neste momento?"**.

**Princípio fundador (não inverter):** o sistema nasce de uma **base universal de conhecimento**,
não da grade curricular. A BNCC, o currículo e o planejamento do professor entram **depois**, como
camadas de aplicação/filtro. Conhecimento é universal; o currículo organiza o uso; o professor
define o foco; a experiência visual mantém o mundo inteiro navegável.

---

## 2. Regra suprema: PRONTO = EVIDÊNCIA (PG1)

Nada é "pronto" sem **pelo menos um artefato falsificável** — um teste ou consulta que **poderia
ter falhado e não falhou**. Não declare conclusão, não diga "funciona", sem produzir esse artefato.
Esta regra vale acima de qualquer pressa.

---

## 3. Invariantes inegociáveis (propriedade estrutural, não preferência)

Estas não são opiniões de estilo — são garantias estruturais já provadas no banco. Não as afrouxe.

- **[N1] Proveniência obrigatória:** toda *claim*/aresta afirmativa carrega `provenance_ref`
  (NOT NULL, com CHECK no banco). Sem fonte, não entra como afirmação.
- **Público nunca vaza não-fato:** a camada pública lê **só** de `core.v_publishable_public`;
  o selo é `'público'` e `is_fact = TRUE` **por construção**. É impossível um item `pending`,
  `legal-review` ou `seeded-demo` aparecer pela porta pública. (Provado por `test_a4.py`.)
- **Não-fato nunca é exibido *como* fato** em nenhum modo — 3D, 2D ou estático (degradação
  não muda o piso epistêmico). Selos persistem em todos os modos.
- **`seeded-demo` nunca vira corpus** e nunca é "fato". É demonstração — fonte não validada.
- **Paleogeografia / atmosfera antiga = sempre reconstrução**, com nota de incerteza (CHECK no banco).
- **Diferencie sempre** o tipo epistêmico: fato documentado · medição direta · inferência
  científica · proxy · reconstrução modelada · estimativa · hipótese · interpretação
  historiográfica · aproximação didática. Nunca apague essa distinção para "simplificar".
- **Sem falsa equivalência:** ClaimSets exibem leituras concorrentes com **pesos assimétricos**;
  "houve impacto" não é um lado em disputa só porque a *causa dominante* é debatida.

---

## 4. Regras estruturais R1–R8 (normativas desde 2026-07-03)

Fonte: `docs/DECISOES.md`, entrada D-20260703-02. Estas regras **revogam** as seções de
processo do playbook v1.3 e a prática de handoff/registro narrativo por passo
(D-20260703-01) — playbook, handoffs e etapas são histórico não-normativo em `docs/arquivo/`.

- **R1 — Fonte única de verdade.** O git é a verdade. Projeto claude.ai e
  memórias de chat são espelhos; em conflito, o repo vence.
- **R2 — Só quatro documentos vivos.** `README.md` (visitante, 5 min),
  `CLAUDE.md` (contrato operacional), `docs/ESTADO.md` (estado + próxima missão),
  `docs/DECISOES.md` (log de decisões). Todo o resto vive em `docs/arquivo/` como
  histórico não-normativo. Exceção operacional: filas de trabalho vivas
  (ex.: `docs/fila-revisao-claimsets-sensiveis.md`).
- **R3 — Fim do arquivo-por-versão.** Proibido criar `*-v1_1.md` novo: documento
  vivo é um arquivo só, versionado pelo git.
- **R4 — Fim do handoff/registro narrativo.** Execução → commit + report JSON de
  script. Decisão → entrada no `DECISOES.md`. Continuidade entre sessões → ler `ESTADO.md`.
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

---

## 5. Regras de trabalho permanentes

- **Não reabra B1** (decisão do motor de banco) **nem B2** (reificação) — estão fechados.
- **Miolo provado:** não reescreva `db/ddl/` nem `db/read-layer/` "para melhorar";
  qualquer mudança ali exige as suítes verdes antes e depois (PG1). Extensões entram
  como **adição** ao lado do provado (padrão `011`/`020`), nunca como reescrita.
- **Não promova conteúdo `seeded-demo` a corpus.** Conteúdo novo = tarefa de modelagem
  registrada; nunca deixe frame e corpus divergirem em silêncio.
- **Ao propor duas abordagens, explique ambas e deixe o humano escolher** — não tome
  decisão arquitetural sozinho.
- **Mudanças mínimas e cirúrgicas;** não refatore o que não foi pedido.
- **Etapas 0–15 estão CONGELADAS como conceito** (D-20260703-01). Proibido produzir novo
  documento de etapa/playbook/handoff. Camadas educacionais (Etapas 6–9) só reabrem com
  demanda validada.

---

## 6. Como rodar (setup)

**Pré-requisitos:** Docker + Docker Compose; Python 3.9+ no host; Node (para as suítes do frame).

```bash
cp .env.example .env     # 12-factor: credenciais locais (gitignored). Ajuste os valores.
bash scripts/bootstrap.sh
```

Isso: **carrega `.env`** (recusa seguir sem ele), sobe Postgres+PostGIS num **volume persistente**
(`atlas-pgdata`), aplica o DDL + camada de leitura (`010`) + envelope (`011`) + papéis (`020`), migra a
carga real (**40 itens · 47 claims · 3 ClaimSets · 16 públicos**), e roda `verify` + `test_a4` +
`test_a3` + `test_a3_http` (devem fechar **10/10 + 10/10 + 10/10 + 5/5**).

Credenciais vêm do `.env` (ver `.env.example`): `ATLAS_DB_PASSWORD` (usuário `atlas`),
`ATLAS_PUBLIC_PASSWORD`/`ATLAS_CURATORIAL_PASSWORD` (papéis de `020`), `ATLAS_CURATORIAL_TOKEN` (header).
Gerenciador de segredos com rotação/auditoria (Opção B) fica para a **E14**.

**Atenção ao reaplicar `011-momento-envelope.sql`:** o `DROP TYPE … CASCADE` recria as funções e
**perde os grants de papel** — reaplique `020` em seguida (o bootstrap já faz isso na ordem certa).

Suítes do frame (node, sem build): `node frame/tests/test_3d.js` · `test_assets.js` · `test_live.js` ·
`test_cosmo.js` (**3D-T 5/5 · ASSET-T 3/3 · LIVE-T 4/4 · COSMO-T 5/5**).

Subir o serviço só-leitura e consultar o envelope (precisa das vars do `.env` no ambiente):

```bash
set -a; . ./.env; set +a
python service/atlas_api.py    # bind 127.0.0.1:8765; RECUSA subir sem as vars obrigatórias
curl "http://127.0.0.1:8765/momento/publico?start=-66050000&end=-65950000"
# porta curatorial exige header: -H "X-Atlas-Auth: $ATLAS_CURATORIAL_TOKEN"
```

O frame (`frame/atlas-3d-frame-v1.html`) consome `/momento/publico` por padrão; sem serviço, cai ao
espelho estático local. A face curatorial (gates ON) exige token e **só** localhost
(`window.ATLAS_CURATORIAL_TOKEN`) — segredo **nunca** embutido no cliente.

Consulta manual da função central:

```bash
# o que era simultâneo a 1789 (janela -212..-210 no eixo 3Z), todas as lentes:
docker compose exec db psql -U atlas -d atlas \
  -c "select id, title, item_type, epistemic_type, selo, is_fact from core.f_simultaneidade_publica(-212, -210, '{}');"
```

---

## 7. Mapa do repositório

```
db/ddl/            esquema reificado (DDL) — 001-esquema-reificado.sql — MIOLO PROVADO
db/read-layer/     camada de leitura gateada — 010-leitura-simultaneidade.sql · 011-momento-envelope.sql — MIOLO PROVADO
db/roles/          papéis de leitura — 020-papeis-leitura.sql (atlas_public / atlas_curatorial; portão por grant)
db/migration/      migrate.py (carga) · verify.py (T1–T10) · test_a4.py · test_a3.py · test_a3_http.py
db/reports/        relatórios verdes de referência (regenerar e commitar JUNTO com a mudança — R6)
service/           atlas_api.py — serviço fino só-leitura (2 endpoints; recusa subir sem var)
frame/             atlas-model.js (modelo puro: fonte única do §8) · atlas-3d-frame-v1.html (AO VIVO) · tests/ · protótipo original
docs/ESTADO.md     VIVO — estado atual + próxima missão (ler ao retomar)
docs/DECISOES.md   VIVO — log de decisões (append-only)
docs/fila-revisao-claimsets-sensiveis.md   VIVO — fila de revisão humana (Tier 0)
docs/governanca/   Constituição v1.1 (viva)
docs/arquivo/      histórico NÃO-NORMATIVO — etapas/ · passos/ · governanca/ (playbooks, constituição v1.0, prompt-mestre) · roteiro/ · auditorias/
scripts/           bootstrap.sh
.env.example       modelo das 4 vars (12-factor); copie para .env (gitignored)
```

**Hierarquia de autoridade:** Constituição v1.1 (`docs/governanca/`) > este `CLAUDE.md` >
`docs/ESTADO.md`/`docs/DECISOES.md` > `docs/arquivo/` (histórico, não-normativo).
Em conflito entre qualquer espelho e o repo, **o repo vence** (R1).
