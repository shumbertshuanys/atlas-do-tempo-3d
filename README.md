# Atlas do Tempo 3D

Plataforma educacional científico-histórica: um **atlas temporal 3D** (linha do tempo + globo/mapa)
com a função central **"O que acontecia no mundo neste momento?"**, construído sobre uma **base
universal de conhecimento** com proveniência e gating epistêmico — depois aplicável à educação
brasileira (BNCC como camada de conformidade, não como origem do conteúdo).

> **Antes de qualquer trabalho:** leia o [`CLAUDE.md`](./CLAUDE.md). Ele é a constituição operacional
> do projeto (regras, invariantes, estado atual e próxima missão) e é carregado automaticamente
> pelo Claude Code.

## Subir o projeto

Pré-requisitos: **Docker + Docker Compose**, **Python 3.9+** e **Node** (suítes do frame).

```bash
cp .env.example .env     # credenciais locais (12-factor, gitignored) — ajuste os valores
bash scripts/bootstrap.sh
```

Esse comando sobe o banco (Postgres 16 + PostGIS 3.4, em volume persistente), aplica o esquema, a
camada de leitura, o envelope e os papéis, migra a carga real (**40 itens · 47 claims · 3 ClaimSets ·
16 públicos**) e roda as suítes de teste. **Sucesso = `verify.py` 10/10 · `test_a4.py` 10/10 ·
`test_a3.py` 10/10 · `test_a3_http.py` 5/5**, mais as suítes do frame
(`node frame/tests/test_3d.js` etc.: **3D-T 5/5 · ASSET-T 3/3 · LIVE-T 4/4 · COSMO-T 5/5**).

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
| `db/migration/` | `migrate.py` (carga) · `verify.py` (T1–T10) · `test_a4.py` (A4-T1..T10) · `test_a3.py` (A3-T1..T10) · `test_a3_http.py` (A3-HTTP-1..5) |
| `db/reports/` | Relatórios verdes de referência |
| `frame/` | Frame 3D de produção (alvo da próxima ligação) + protótipo original |
| `docs/ESTADO.md` | **Vivo** — estado atual + próxima missão (ler ao retomar) |
| `docs/DECISOES.md` | **Vivo** — log de decisões (append-only) |
| `docs/fila-revisao-claimsets-sensiveis.md` | **Vivo** — fila de revisão humana (Tier 0) |
| `docs/validacao/` | **Vivo** — kit de validação de demanda (demo, entrevista, fichas) |
| `docs/governanca/` | **Vivo** — Constituição v1.1 |
| `docs/arquivo/` | Histórico não-normativo: `etapas/` · `passos/` · `governanca/` (playbooks, constituição v1.0, prompt-mestre) · `roteiro/` · `auditorias/` |
| `docker-compose.yml` | Banco local persistente |
| `scripts/bootstrap.sh` | Setup reproduzível |

## Estado atual

O estado vivo (o que está construído, dívidas e a próxima missão) mora em
[`docs/ESTADO.md`](./docs/ESTADO.md) — resumo: banco reificado com a carga 40/47, frame 3D **ao
vivo** consumindo a API só-leitura (`/momento/publico`), estágio cósmico com lastro (Frente A).

## Princípios não-negociáveis (resumo)

- **Pronto = evidência** (PG1): nada é concluído sem um artefato falsificável.
- **Proveniência obrigatória** em toda afirmação ([N1], com CHECK no banco).
- **O público nunca exibe não-fato** — garantido por construção na camada de leitura (provado).
- **`seeded-demo` nunca vira corpus** e nunca é "fato".
- **Sem falsa equivalência** entre leituras de peso desigual.

(Versão completa e vinculante em `CLAUDE.md` e `docs/governanca/`.)
