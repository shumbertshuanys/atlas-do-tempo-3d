# Atlas do Tempo 3D

Plataforma educacional científico-histórica: um **atlas temporal 3D** (linha do tempo + globo/mapa)
com a função central **"O que acontecia no mundo neste momento?"**, construído sobre uma **base
universal de conhecimento** com proveniência e gating epistêmico — depois aplicável à educação
brasileira (BNCC como camada de conformidade, não como origem do conteúdo).

> **Antes de qualquer trabalho:** leia o [`CLAUDE.md`](./CLAUDE.md). Ele é a constituição operacional
> do projeto (regras, invariantes, estado atual e próxima missão) e é carregado automaticamente
> pelo Claude Code.

## Subir o projeto

Pré-requisitos: **Docker + Docker Compose** e **Python 3.9+**.

```bash
bash scripts/bootstrap.sh
```

Esse comando sobe o banco (Postgres 16 + PostGIS 3.4, em volume persistente), aplica o esquema e a
camada de leitura, migra os 35 itens e roda as suítes de teste. **Sucesso = `verify.py` 10/10 e
`test_a4.py` 10/10.**

Consulta da função central (exemplo — simultâneos a 1789):

```bash
docker compose exec db psql -U atlas -d atlas \
  -c "select id, title, selo, is_fact from core.f_simultaneidade_publica(-212, -210, '{}');"
```

## Mapa do repositório

| Caminho | Conteúdo |
|---|---|
| `CLAUDE.md` | Constituição operacional (ler primeiro) |
| `db/ddl/` | Esquema reificado (DDL) |
| `db/read-layer/` | Camada de leitura gateada (função de simultaneidade) |
| `db/migration/` | `migrate.py` (carga) · `verify.py` (T1–T10) · `test_a4.py` (A4-T1..T10) |
| `db/reports/` | Relatórios verdes de referência |
| `frame/` | Frame 3D de produção (alvo da próxima ligação) + protótipo original |
| `docs/ESTADO.md` | **Vivo** — estado atual + próxima missão (ler ao retomar) |
| `docs/DECISOES.md` | **Vivo** — log de decisões (append-only) |
| `docs/fila-revisao-claimsets-sensiveis.md` | **Vivo** — fila de revisão humana (Tier 0) |
| `docs/governanca/` | **Vivo** — Constituição v1.1 |
| `docs/arquivo/` | Histórico não-normativo: `etapas/` · `passos/` · `governanca/` (playbooks, constituição v1.0, prompt-mestre) · `roteiro/` · `auditorias/` |
| `docker-compose.yml` | Banco local persistente |
| `scripts/bootstrap.sh` | Setup reproduzível |

## Estado atual

Passo **A4 concluído e verde**: banco reificado (35 itens) + camada de leitura gateada da função
"O que acontecia no mundo?". O frame 3D de produção ainda usa um **espelho curado estático** e
**não** consome o banco ao vivo — essa ligação (junto com a produção 3D real, passo **A3**) é a
próxima missão, detalhada em `docs/passos/passo-a4-leitura-simultaneidade-v1_0.md`.

## Princípios não-negociáveis (resumo)

- **Pronto = evidência** (PG1): nada é concluído sem um artefato falsificável.
- **Proveniência obrigatória** em toda afirmação ([N1], com CHECK no banco).
- **O público nunca exibe não-fato** — garantido por construção na camada de leitura (provado).
- **`seeded-demo` nunca vira corpus** e nunca é "fato".
- **Sem falsa equivalência** entre leituras de peso desigual.

(Versão completa e vinculante em `CLAUDE.md` e `docs/governanca/`.)
