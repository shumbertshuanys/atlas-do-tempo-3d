# Atlas do Tempo 3D — Memória do projeto

> Este arquivo é lido automaticamente pelo Claude Code no início de cada sessão.
> Ele é o **contrato de comportamento** do projeto: cada linha deve mudar como o agente age.
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
  não muda o piso epistêmico; ver Playbook §8). Selos persistem em todos os modos.
- **`seeded-demo` nunca vira corpus** e nunca é "fato". É demonstração — fonte não validada.
- **Paleogeografia / atmosfera antiga = sempre reconstrução**, com nota de incerteza (CHECK no banco).
- **Diferencie sempre** o tipo epistêmico: fato documentado · medição direta · inferência
  científica · proxy · reconstrução modelada · estimativa · hipótese · interpretação
  historiográfica · aproximação didática. Nunca apague essa distinção para "simplificar".
- **Sem falsa equivalência:** ClaimSets exibem leituras concorrentes com **pesos assimétricos**;
  "houve impacto" não é um lado em disputa só porque a *causa dominante* é debatida.

---

## 4. Estado atual (jun/2026) — Passo A4 concluído e verde

| Componente | Estado |
|---|---|
| Banco reificado (PostgreSQL 16 + PostGIS 3.4), 35 itens | ✅ reconstruível do DDL+migração |
| Camada de leitura gateada (função "O que acontecia no mundo?") | ✅ pública + curatorial |
| `verify.py` — invariantes T1–T10 | ✅ 10/10 |
| `test_a4.py` — simultaneidade gateada A4-T1..T10 | ✅ 10/10 |
| Frame 3D de produção (`frame/atlas-3d-frame-v1.html`) | ⚠️ **ainda usa espelho curado estático** (arrays `ITEMS`/`CLAIMSETS` hardcoded). **Não consome o banco ao vivo.** |

Sobre os artefatos em `db/`:

- **`db/ddl/` e `db/read-layer/`** (esquema reificado + camada de leitura gateada) permanecem
  **byte-idênticos** ao sandbox e **não foram tocados** — é o miolo provado. **Não reescrever.**
- **`db/migration/{migrate,verify,test_a4}.py`** receberam mudanças **só de portabilidade
  (Windows/Linux)** — caminho de saída relativo ao script, criação automática de `out/`, e stdout
  em UTF-8. **Sem alteração de lógica, semântica de teste ou esquema.**
- **"Reconstruível do bootstrap" está PROVADO em Windows e Linux:**
  `docker compose down -v && bash scripts/bootstrap.sh` fecha **10/10 + 10/10** em volume novo,
  sem contornos manuais.

A regra do miolo continua valendo: não reescreva `db/ddl/`/`db/read-layer/` "para melhorar" sem
antes rodar os testes e mantê-los verdes.

---

## 5. Próxima missão: A3 (produção 3D) + ligação ao vivo do frame

Detalhe completo em `docs/passos/passo-a4-leitura-simultaneidade-v1_0.md` (seção "Próximos passos").
Em resumo, **nesta ordem**:

1. **Bootstrap e confirme o verde** (`bash scripts/bootstrap.sh` → 10/10 + 10/10).
2. **A3 — produção 3D real:** assets/shaders/cosmos bem representados sobre o frame (é o que tem
   teto técnico no sandbox e por isso vive aqui no Claude Code).
3. **Ligação ao vivo:** expor as funções de leitura (`core.f_simultaneidade_publica` /
   `_curatorial`) por uma API mínima; o frame passa a **consumir a API** em vez dos arrays estáticos.
4. **Antes de ligar:** o frame tem 6 ClaimSets autorados, mas o corpus só modela **2**
   (`goe-ritmo`, `kpg-causa`). Modele os outros no corpus **ou** remova-os honestamente — não ligue
   ao vivo com divergência silenciosa.
5. **Adicione o domínio `clima`** ao frame: o banco tem 2 itens de clima, mas `DOMAINS` no frame
   não inclui `clima` — `DOMAINS[it.dom]` quebraria. Adicionar a `DOMAINS`, `lensOn` e à UI de lentes.
6. **Preserve o §8** (contrato visual) nos três renderizadores e o gating por construção.

---

## 6. Como rodar (setup)

**Pré-requisitos:** Docker + Docker Compose; Python 3.9+ no host.

```bash
bash scripts/bootstrap.sh
```

Isso: sobe Postgres+PostGIS num **volume persistente** (`atlas-pgdata` — resolve a perda de estado
entre sessões), aplica o DDL e a camada de leitura, migra os 35 itens, e roda `verify.py` +
`test_a4.py` (devem fechar **10/10 + 10/10**).

DSN fixo (casa com `docker-compose.yml`): `host=localhost port=5432 dbname=atlas user=atlas password=atlas`.

Consulta manual da função central:

```bash
# o que era simultâneo a 1789 (janela -212..-210 no eixo 3Z), todas as lentes:
docker compose exec db psql -U atlas -d atlas \
  -c "select id, title, item_type, epistemic_type, selo, is_fact from core.f_simultaneidade_publica(-212, -210, '{}');"
```

---

## 7. Mapa do repositório

```
db/ddl/            esquema reificado (DDL) — 001-esquema-reificado.sql
db/read-layer/     camada de leitura gateada — 010-leitura-simultaneidade.sql
db/migration/      migrate.py (carga 35 itens) · verify.py (T1–T10) · test_a4.py (A4-T1..T10)
db/reports/        relatórios verdes de referência (migration/verification/test_a4)
frame/             frame 3D de produção (alvo da ligação) + protótipo original
docs/governanca/   Constituição (v1_1) + Playbook (v1_3) + Prompt-mestre  ← LER antes de decidir
docs/passos/       handoffs por passo (mais recente: passo-a4)
docs/etapas/       corpus conceitual (Etapas 0–15 e sub-etapas)
docs/roteiro/      estado-atual, pendências, divergências, decisões
scripts/           bootstrap.sh
```

**Hierarquia de autoridade dos docs:** Constituição > Playbook > handoff do passo atual > etapas.
Em dúvida sobre uma regra, leia `docs/governanca/` antes de agir.

---

## 8. Regras de trabalho (herdadas do projeto)

- **Um passo por vez.** Cada passo termina com um **handoff curto** salvo em `docs/passos/`
  (formato de 9 pontos + rodapé "o que NÃO faz", como os 4Z/5Z do corpus).
- **Não reabra B1** (decisão do motor de banco) **nem B2** (reificação) — estão fechados.
- **Não promova conteúdo `seeded-demo` a corpus.** Conteúdo novo = tarefa de modelagem registrada;
  nunca deixe frame e corpus divergirem em silêncio.
- **Ao propor duas abordagens, explique ambas e deixe o humano escolher** — não tome decisão
  arquitetural sozinho.
- **Mudanças mínimas e cirúrgicas;** não refatore o que não foi pedido.
- **Antes de declarar pronto:** produza o artefato falsificável (PG1).
- **Commits por mudança lógica**, não um commit-monstro.
