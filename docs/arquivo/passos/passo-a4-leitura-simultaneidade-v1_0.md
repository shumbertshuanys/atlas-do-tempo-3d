# Passo A4 — Camada de leitura gateada + simultaneidade · Handoff

**Versão:** v1.0
**Data:** jun/2026
**Antecede:** A3 (produção 3D) + ligação ao vivo do frame, no Claude Code
**Natureza:** handoff de fechamento, no formato de 9 pontos do Playbook §2.

---

## 1. Objetivo

Reconstruir a **fundação de dados reificada** do Atlas e expor a função **"O que acontecia no
mundo neste momento?"** como uma **camada de leitura gateada** sobre as views, com **prova
falsificável** de que a porta pública nunca exibe não-fato. Preparar a passagem da **ligação ao
vivo do frame** para o ambiente certo (Claude Code), evitando produzir um artefato descartável.

## 2. Escopo

**Fez (concluído e verde nesta sessão):**
- **Fatia 1 — Banco reificado reconstruído** a partir do DDL + migração; 35 itens carregados.
- **Fatia 2 — Camada de leitura gateada:** funções de simultaneidade pública e curatorial sobre as
  views, com selo e `is_fact` derivados por construção.
- **Fatia 4 (PG1) — Artefato falsificável:** `verify.py` (invariantes T1–T10) **10/10** e
  `test_a4.py` (simultaneidade gateada A4-T1..T10) **10/10**.

**Não fez (por decisão desta sessão — "Opção A"):**
- **Fatia 3 — Ligação ao vivo do frame:** reposicionada para o Claude Code, junto com A3. **Não**
  se produziu um `atlas-3d-frame-a4.html` com dados embutidos em *build-time* (seria descartável).
- **Fatia 5 — Handoff:** é este documento.

## 3. Diagnóstico

A ligação real entre frame e dados é **runtime** (frontend → API → views gateadas → render), e
depende de **banco persistente, versionamento (git) e assets 3D reais** — exatamente o que o
sandbox de chat **não** oferece (o estado se perde a cada sessão; reconstruímos o banco do zero).
Isso é coerente com o roteiro já registrado (`docs/roteiro/estado-atual-e-roteiro_2.md`, passos
A2/A3): *"as representações cósmicas bem-feitas não cabem no sandbox… o lugar é o Claude Code"*.
Logo, parar a ligação aqui e migrar **evita um meio-passo build-time descartável** e preserva
intacto o que já está provado.

## 4. Decisões principais

- **D-A4.1 — Porta pública é gateada por construção.** `core.f_simultaneidade_publica` lê **só** de
  `core.v_publishable_public`; selo `'público'` e `is_fact = TRUE` sempre. É **impossível**, pela
  estrutura, que `pending` / `legal-review` / `seeded-demo` vazem pela porta pública. (Provado por
  A4-T1..T7.)
- **D-A4.2 — Porta curatorial é honesta sobre regime.** `core.f_simultaneidade_curatorial` vê
  itens `approved` + `pending` (exclui `legal-review`/`rejected`/`blocked`); os selos distinguem
  **fato** (corpus+approved) · **demonstração** (seeded) · **em-revisão** (pending). `seeded-demo`
  nunca recebe `is_fact = TRUE`.
- **D-A4.3 — Simultaneidade = OVERLAP no eixo 3Z.** Dois itens são simultâneos se
  `canonical_start ≤ p_end AND canonical_end ≥ p_start` (datum T0 = 2000 CE). Lente vazia/`{}` = todas
  as lentes; lente sem correspondência = conjunto vazio (vazio **é informação**).
- **D-A4.4 — Artefatos verificados entram byte-idênticos.** DDL, `migrate.py`, `verify.py`,
  `test_a4.py` e a SQL da camada de leitura vão ao repo **exatamente** como passaram verdes. DSN
  fixo em `localhost:5432` (casa com `docker-compose.yml`).
- **D-A4.5 — Ligação ao vivo do frame → Claude Code.** Reposicionada para junto de A3. Não se
  produz frame *build-time*.
- **D-A4.6 — Repositório local self-contained.** Criado para o Claude Code: Docker persistente
  (resolve a perda de estado), DDL + camada de leitura + migração + testes, corpus completo e
  `CLAUDE.md` como contrato operacional.

## 5. Modelo conceitual

- **Núcleo reificado:** `entity_node` + tabelas de `source` / `provenance_metadata` /
  `knowledge_item` / `claim` / `relationship` / `claim_set(_member)` / `geometry_version` /
  `media_asset`. `claim.provenance_ref` é **NOT NULL** ([N1]); arestas afirmativas idem (CHECK).
- **Isolamento de licença:** `media_asset` com *trigger* que isola *share-alike* e bloqueia
  NC-risco-4; *store* isolado em schema próprio, sem acesso do papel de serviço.
- **Cache derivado:** `derived_cache` sem FKs e sem proveniência ([N2] — derivado não carrega
  proveniência própria).
- **Views:** `v_displayable_curatorial` (approved ∩ admitido = 23) e `v_publishable_public`
  (approved ∩ corpus ∩ fonte-confirmada = 11).
- **Camada de leitura:** TYPE `t_simultaneidade_row` + `f_simultaneidade_publica(_em)` e
  `f_simultaneidade_curatorial(_em)`, com `f_item_attribution` / `f_item_epistemics` derivando
  fonte e tipo epistêmico do item-claim → proveniência → fonte.

## 6. Fontes necessárias

Nenhuma fonte externa nova. O passo se apoia no próprio corpus: datum 3Z
(`docs/etapas/etapa-3z-…`), motor B1 (`docs/passos/passo-b1-…`), reificação B2
(`docs/passos/passo-b2-…`), `docs/passos/handoff-a3-final.md`, Constituição v1.1 e Playbook v1.3
(`docs/governanca/`). Conteúdo `seeded-demo` permanece marcado como demonstração — fonte não validada.

## 7. Riscos

- **R-A4.1 — Sandbox não persiste.** *Mitigado:* `docker-compose.yml` com volume nomeado
  (`atlas-pgdata`) no repo; `bootstrap.sh` reproduz o estado verde em um comando.
- **R-A4.2 — Ligação build-time seria descartável.** *Mitigado:* adiada para runtime no Claude Code.
- **R-A4.3 — Divergência de ClaimSets.** O frame autora **6** ClaimSets; o corpus modela **2**
  (`goe-ritmo` host `proc:goe`, `kpg-causa` host `evt:impacto-chicxulub`). *Ação:* antes de ligar
  ao vivo, modelar os 4 extras no corpus **ou** removê-los — não ligar com divergência silenciosa.
- **R-A4.4 — Domínio `clima` ausente no frame.** O banco tem 2 itens de clima; o `DOMAINS` do
  frame não inclui `clima`, então `DOMAINS[it.dom]` quebraria. *Ação:* adicionar `clima` a
  `DOMAINS`, `lensOn` e à UI de lentes ao ligar.
- **R-A4.5 — Dependência de Python host.** `migrate.py`/`verify.py`/`test_a4.py` rodam no host e
  exigem `psycopg2-binary`. *Mitigado:* `bootstrap.sh` instala via `db/requirements.txt`.

## 8. Entregáveis

No repositório `atlas-do-tempo-3d/`:

- `db/ddl/001-esquema-reificado.sql`
- `db/read-layer/010-leitura-simultaneidade.sql`
- `db/migration/migrate.py` · `db/migration/verify.py` (10/10) · `db/migration/test_a4.py` (10/10)
- `db/reports/{migration_report,verification_report,test_a4_report}.json`
- `docker-compose.yml` (Postgres 16 + PostGIS 3.4, persistente) · `scripts/bootstrap.sh`
- `CLAUDE.md` · `README.md` · `.gitignore` · `.env.example` · `db/requirements.txt` ·
  `.claude/settings.json`
- `frame/atlas-3d-frame-v1.html` (alvo da ligação) · `frame/atlas-prototipo-3d.html`
- `docs/` — corpus completo (etapas, passos, governança, roteiro) +
  `docs/passos/verification_report_spec-a3.json` (especificação dos testes T1–T10)
- Este handoff (`docs/passos/passo-a4-leitura-simultaneidade-v1_0.md`)

## 9. Próximos passos (no Claude Code)

1. **Bootstrap e confirmar verde:** `bash scripts/bootstrap.sh` → `verify.py` 10/10 e `test_a4.py`
   10/10. Sem isso, não avançar.
2. **A3 — produção 3D real:** assets/shaders/cosmos bem representados sobre `frame/atlas-3d-frame-v1.html`.
3. **API mínima de leitura:** expor `core.f_simultaneidade_publica`/`_curatorial` por um endpoint;
   o frame passa a **consumir a API** no lugar dos arrays estáticos `ITEMS`/`CLAIMSETS`.
4. **Reconciliar antes de ligar:** modelar no corpus os 4 ClaimSets que hoje só vivem no frame
   (R-A4.3) e adicionar o domínio `clima` (R-A4.4).
5. **Preservar §8** (contrato visual) nos três renderizadores (3D/2D/estático) e o gating por
   construção — não-fato nunca exibido como fato.

---

## Rodapé — o que este passo NÃO faz

- **NÃO reabre** o motor de banco (B1) nem a reificação (B2) — propriedade estrutural fechada.
- **NÃO promove** conteúdo `seeded-demo` a corpus, nem o exibe como fato.
- **NÃO liga** o frame ao vivo (reposicionado para o Claude Code) **nem** produz frame *build-time*.
- **NÃO publica** conteúdo semeado como fato — a porta pública é gateada **por construção**, e isso
  está **provado** (não apenas afirmado).
- **NÃO modela** os 4 ClaimSets extras do frame — vira tarefa registrada de modelagem (Trilha B).
- **NÃO cria** camadas de usuário/escola — fora do MVP enxuto.
