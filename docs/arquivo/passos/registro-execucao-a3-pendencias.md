# Registro de execução — A3, fatia das pendências (D-A3.1 + D-A3.2)

> Registro curto de fechamento do que foi **realmente executado**. Apenas a fatia das
> pendências do Passo A3 — **não** a API (D-A3.3..5) nem o 3D (D-A3.6..8).
> Plano: `docs/passos/passo-a3-plano-producao-3d-ligacao-ao-vivo-v1_0.md`.

## 1. Estado final

Fatia das pendências **concluída e verde**. Bootstrap fresh do zero
(`docker compose down -v && bash scripts/bootstrap.sh`): **verify 10/10 + test_a4 10/10**,
carga `claimsets 3 · membros 7 · total 42 · itens 35`.

| Commit | O quê |
|---|---|
| `75338c3` | D-A3.1: ClaimSet `rev-francesa` modelado no corpus + fixture T10 atualizado |
| `9ec5840` | D-A3.1 (frame): remove 3 ClaimSets de host pending + corrige bug `rev`; enfileira na revisão |
| `d84d2fa` | D-A3.2: lente `clima` + lookup tolerante de domínio |

**Artefatos falsificáveis:** contagem de ClaimSets no frame == corpus (**3 == 3**);
domínio desconhecido **não** quebra o frame (`out/_check_clima.js` 9/9, efêmero/gitignored);
itens de clima carregam rótulo epistêmico por-item (observável só ao vivo — frame estático
não tem itens de clima).

## 2. O que mudou em relação ao plano (decisões tomadas em execução)

1. **Conflito do fixture T10.** `verify.py` T10 assere igualdade com um inventário
   hard-coded (`claimsets:2, membros:4, total:39`). Modelar ClaimSet muda essas contagens.
   Resolvido (decisão do operador): o guardrail protege a **invariante** (`soma_ok`), não o
   inventário — D-A3.1 muda o inventário de propósito. Fixture atualizado **só** nessas três
   contagens (2→3, 4→7, 39→42); `soma_ok` e demais asserções intactas.
2. **Divergência frame↔corpus descoberta (bug do frame).** `evt:declaracao-direitos-1789`
   é `pending` (`mediado`) no corpus autoritativo, mas o frame o marcava `rev:'approved'`.
   O plano (§3) classificou `direitos-limites` como "host approved" por causa desse bug.
   Decisão (Opção A — corpus é autoritativo): modelar **só** `rev-francesa` no corpus
   (host approved, N=3); `direitos-limites` cai no balde dos sensíveis. Bug do frame
   corrigido (`approved`→`pending`; item segue exibido, gated). Portanto **3** ClaimSets
   foram à fila de revisão, não 2: `direitos-limites`, `inconfidencia`, `escravidao-central`
   (`docs/roteiro/fila-revisao-claimsets-sensiveis.md`, Trilha C / Playbook §5).
3. **Clima — descoberta corrigiu a premissa.** Os 2 itens de clima do banco
   (`state:clima-goe` = **hipótese**; `state:clima-pos-impacto-kpg` = **inferência-científica**)
   são **tempo profundo** (GOE ~2,4 Ga; K-Pg ~66 Ma), `pending`, selo **em-revisão**, gated
   (público = 0). **Não há item de clima moderno** — a hipótese do plano §6
   ("consenso × negacionismo") não se aplica. A lente nasce com os rótulos reais por-item;
   **sem** UI de consenso×negacionismo (confirmado pelo operador).

## 3. Pendências / o que esta fatia NÃO fez

- **API** (D-A3.3..5) e **3D** (D-A3.6..8): não iniciados (fora do escopo desta sessão).
- **3 ClaimSets na fila de revisão**: `direitos-limites`/`inconfidencia`/`escravidao-central`
  aguardam host aprovado via pipeline para reintegração (conteúdo preservado no histórico git).
- **Reconciliação ampla das 7 lentes canônicas**: fora do A3 (só `clima` foi adicionado).
- **Itens de clima no frame estático**: inexistentes; a lente só se popula ao vivo.
- `migrate.py`: **nenhum** `pub`/`review_status` de item foi alterado (declaracao-direitos
  **não** foi aprovado). `db/ddl/` e `db/read-layer/` intactos — só adição.

## 4. Notas de ambiente

- O `bootstrap.sh` só fecha verde em **volume novo** (DDL não-idempotente: `CREATE TABLE`
  sem `IF NOT EXISTS`). Re-rodar em volume já inicializado falha no passo 3.
- Reset de banco (`docker compose down -v`) é digitado pelo operador no prompt (deny mantido
  no `settings.json`). Verificação intermediária sem wipe: re-rodar `migrate.py` (idempotente)
  + suítes contra o banco vivo.
