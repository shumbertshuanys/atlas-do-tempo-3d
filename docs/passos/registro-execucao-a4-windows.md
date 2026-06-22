# Registro de execução — A4 (portabilidade Windows/Linux)

> Registro curto de fechamento do que foi **realmente executado** nesta sessão.
> Complementa o handoff de planejamento `passo-a4-leitura-simultaneidade-v1_0.md`.

## 1. Estado final

A4 **encerrado** e **reproduzível em Windows e Linux**.

| Commit | O quê |
|---|---|
| `0cd231d` | A4: fundação de dados + camada de leitura + handoff |
| `cf6c878` | fix: portabilidade Windows/Linux do bootstrap (sem mudança de lógica) |
| `9451a5e` | Merge `--no-ff` da fix em `master` |

**PG1 fechado:** `docker compose down -v && bash scripts/bootstrap.sh` em volume novo
fecha **10/10 (verify.py) + 10/10 (test_a4.py)**, sem contornos manuais.

## 2. O que mudou em relação ao handoff planejado

O bootstrap original só rodava em Linux. Foram necessárias **5 correções de portabilidade
não previstas** no handoff — todas na camada de execução, **só portabilidade**:

1. **`python3` vs `python`** — no Windows o `python3` no PATH é o *stub da Microsoft Store*
   (não executa). O `bootstrap.sh` agora valida **execução real** do interpretador, não só
   presença no PATH, e cai para `python` quando preciso.
2. **Race da 1ª-init do Postgres** — o passo de espera checava o *socket Unix*, que responde
   já no servidor temporário do entrypoint (que depois reinicia), matando o passo seguinte com
   *"database system is shutting down"*. Resolvido checando prontidão **via TCP**
   (`pg_isready -h 127.0.0.1`), que só responde quando o servidor real sobe.
3. **`OUT_DIR` relativo ao script + `makedirs`** — os relatórios escreviam em caminho absoluto
   do sandbox (`/home/claude/atlas-a4/out/`) / relativo ao cwd. Agora o diretório de saída é
   relativo ao próprio script e criado automaticamente.
4. **stdout UTF-8 via `reconfigure`** — o `print` do relatório quebrava em consoles cp1252
   (Windows) ao imprimir `∩`/`⊂`/`⟂`. Resolvido com `sys.stdout.reconfigure(encoding="utf-8")`.
5. **`/out/` no `.gitignore`** — saída regenerável fora de `db/reports/`, não vai ao git.

**Escopo estritamente de portabilidade:** `db/ddl/` e `db/read-layer/` permanecem
**intactos / byte-idênticos** ao sandbox. **Nenhuma** mudança de lógica, esquema ou semântica
de teste — `migrate/verify/test_a4` mudaram só em caminho de saída e encoding de stdout.

## 3. Lições para a próxima sessão

- **Ambiente-alvo:** Windows + Git Bash + Docker Desktop.
- **Sempre validar execução real do interpretador**, não só presença no PATH (o stub da Store
  passa em `command -v` mas não roda).
- **Reset de banco** é `! docker compose down -v` digitado no prompt. O `deny` no
  `settings.json` bloqueia o agente **de propósito** — manter essa trava.

## 4. Pendências que ressurgem ANTES de ligar o frame ao banco (A3)

- **Modelar ou remover** os 4 ClaimSets que só existem no frame (o corpus modela 2:
  `goe-ritmo`, `kpg-causa`; o frame autora 6). Não ligar ao vivo com divergência silenciosa.
- **Adicionar o domínio `clima`** ao frame (`DOMAINS`, `lensOn` e UI de lentes) — o banco tem
  2 itens de clima e hoje `DOMAINS[it.dom]` quebraria.
