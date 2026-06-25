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

## 4. Estado atual (jun/2026) — API só-leitura (D-A3.3/4/5) verde + gateada

| Componente | Estado |
|---|---|
| Banco reificado (PostgreSQL 16 + PostGIS 3.4) — carga **42**: 35 itens · 3 ClaimSets · 7 membros | ✅ reconstruível do DDL+migração |
| Camada de leitura gateada (função "O que acontecia no mundo?") | ✅ pública + curatorial |
| **API só-leitura — envelope `MomentResult` (forma β):** `core.f_momento_publico`/`_curatorial` (`011-momento-envelope.sql`, **adição**; cada campo §8 do autoritativo, reusando os helpers A4) + serviço fino (`service/atlas_api.py`, 2 endpoints) + portão por grant (`db/roles/020-papeis-leitura.sql`, 2 papéis) | ✅ **existe, gateada e provada.** Ainda **NÃO** ligada ao frame. |
| `verify.py` — invariantes T1–T10 (fixture T10: 2→3, 4→7, 39→42; `soma_ok` intacto) | ✅ 10/10 |
| `test_a4.py` — simultaneidade gateada A4-T1..T10 | ✅ 10/10 |
| `test_a3.py` — envelope A3-T1..T10 (público nunca não-fato · todo item §8 · gating por host) | ✅ 10/10 |
| `test_a3_http.py` — portão/HTTP A3-HTTP-1..5 (grant sem EXECUTE na curatorial · sem credencial de escrita) | ✅ 5/5 |
| Frame 3D de produção (`frame/atlas-3d-frame-v1.html`) | ⚠️ **ainda NÃO ao vivo.** D-A3.1: ClaimSets frame == corpus (**3 == 3**); D-A3.2: lente `clima` + lookup tolerante. Consome arrays `ITEMS`/`CLAIMSETS` **estáticos** — a API já existe (acima), mas a **virada ao vivo** é a próxima frente. |

Sobre os artefatos em `db/`:

- **`db/ddl/` e `db/read-layer/`** (esquema reificado + camada de leitura gateada) permanecem
  **byte-idênticos** ao sandbox e **não foram tocados** — é o miolo provado. **Não reescrever.**
- **`db/migration/*.py`** receberam **(a)** portabilidade Windows/Linux (caminho de saída relativo
  ao script, criação automática de `out/`, stdout UTF-8) e **(b)** a fatia D-A3.1: `migrate.py`
  ganhou o ClaimSet `rev-francesa` (adição) e `verify.py` teve o **inventário** do fixture T10
  atualizado (2→3 ClaimSets, 4→7 membros, 39→42 total). **A invariante `soma_ok` e as demais
  asserções continuam intactas** — o guardrail protege a invariante, não o inventário.
- **`db/read-layer/011-momento-envelope.sql` + `db/roles/020-papeis-leitura.sql` + `service/`**
  são **adição** (D-A3.3/4/5): o envelope nasce no banco, derivado do autoritativo, ao lado das
  funções A4 — **não reescrevem** o miolo. Funções SECURITY DEFINER + `REVOKE EXECUTE FROM PUBLIC`;
  o portão é o GRANT (papéis `atlas_public`/`atlas_curatorial`), não `if` de runtime.
- **Divergência da carga fixada na descoberta** (`docs/passos/nota-descoberta-a3-api-envelope.md`):
  só **`kpg-causa`** tem host em `v_publishable_public` (`chicxulub`); `rev-francesa`/`goe-ritmo` têm
  host com fonte-por-asset pendente → **não** vazam pela pública (gating por host, §5.5 do plano).
- **"Reconstruível do bootstrap" está PROVADO em Windows e Linux:**
  `docker compose down -v && bash scripts/bootstrap.sh` fecha **10/10 + 10/10 + 10/10 + 5/5** em
  volume novo (carga `claimsets 3 · membros 7 · total 42 · itens 35`), sem contornos manuais.
- **3 ClaimSets de host `pending` foram removidos do frame** (`direitos-limites`, `inconfidencia`,
  `escravidao-central`) e enfileirados em `docs/roteiro/fila-revisao-claimsets-sensiveis.md`
  (Trilha C / Playbook §5) — aguardam host aprovado para reintegração; conteúdo preservado no git.

A regra do miolo continua valendo: não reescreva `db/ddl/`/`db/read-layer/` "para melhorar" sem
antes rodar os testes e mantê-los verdes.

---

## 5. Próxima missão: virada ao vivo (frame → API) + 3D em paralelo

Plano de produção em `docs/passos/passo-a3-plano-producao-3d-ligacao-ao-vivo-v1_0.md` (9 pontos);
plano de execução da API em `docs/passos/passo-a3-plano-execucao-api-so-leitura-v1_0.md`; registro
de execução em `docs/passos/registro-execucao-a3-api-so-leitura.md` (+ nota de descoberta).

**Já feito:** D-A3.1/D-A3.2 (reconciliação dos ClaimSets + lente `clima`) e **D-A3.3/4/5 (API
só-leitura)** — envelope `MomentResult` no banco, serviço fino, portão por grant; **provada**
(A3-T1..10 + A3-HTTP-1..5). A divergência frame↔corpus que gateava a ligação **caiu**, e a API que a
extingue por construção **existe**.

**Próxima missão, nesta ordem:**

1. **Bootstrap e confirme o verde** (`bash scripts/bootstrap.sh` → 10/10 + 10/10 + 10/10 + 5/5) antes de avançar (PG1).
2. **Virada ao vivo (próxima frente):** o frame passa a **consumir a API** (`service/atlas_api.py` →
   `core.f_momento_publico`) em vez dos arrays estáticos. A classe de divergência frame↔corpus se
   **extingue por construção** quando `review_status`/selo/`is_fact` vêm sempre do autoritativo.
3. **3D real (D-A3.6..8), em paralelo desde já contra o array via `SceneModel`:** modelo único +
   overlay §8 renderer-agnóstico + 3 renderizadores (3D/2D/estático) + assets procedurais dos 3
   regimes-âncora. A virada ao vivo troca **uma fonte só**.
4. **Preserve o §8** (contrato visual) nos três renderizadores e o gating por construção em todo degrau.

> As 3 sensíveis (`direitos-limites`, `inconfidencia`, `escravidao-central`) **não** se religam ao
> vivo enquanto host for `pending`; seguem na fila de revisão (Trilha C). Não publicar sem host aprovado.

---

## 6. Como rodar (setup)

**Pré-requisitos:** Docker + Docker Compose; Python 3.9+ no host.

```bash
bash scripts/bootstrap.sh
```

Isso: sobe Postgres+PostGIS num **volume persistente** (`atlas-pgdata` — resolve a perda de estado
entre sessões), aplica o DDL + camada de leitura (`010`) + envelope (`011`) + papéis (`020`), migra a
carga (`claimsets 3 · membros 7 · total 42 · itens 35`), e roda `verify` + `test_a4` + `test_a3` +
`test_a3_http` (devem fechar **10/10 + 10/10 + 10/10 + 5/5**).

DSN fixo (casa com `docker-compose.yml`): `host=localhost port=5432 dbname=atlas user=atlas password=atlas`.
Papéis de leitura (D-A3.5): `atlas_public` / `atlas_curatorial` (senhas locais homônimas; ver `020`).

Subir o serviço só-leitura (D-A3.4) e consultar o envelope:

```bash
# em um terminal: python service/atlas_api.py  (bind 127.0.0.1:8765)
curl "http://127.0.0.1:8765/momento/publico?start=-66050000&end=-65950000"
# porta curatorial exige header: -H "X-Atlas-Auth: $ATLAS_CURATORIAL_TOKEN"
```

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
db/read-layer/     camada de leitura gateada — 010-leitura-simultaneidade.sql · 011-momento-envelope.sql (envelope MomentResult, adição)
db/roles/          papéis de leitura — 020-papeis-leitura.sql (atlas_public / atlas_curatorial; portão por grant)
db/migration/      migrate.py (carga 42) · verify.py (T1–T10) · test_a4.py (A4-T1..T10) · test_a3.py (A3-T1..T10) · test_a3_http.py (A3-HTTP-1..5)
db/reports/        relatórios verdes de referência (migration/verification/test_a4/test_a3/test_a3_http)
service/           atlas_api.py — serviço fino só-leitura (2 endpoints, público/curatorial)
frame/             frame 3D de produção (alvo da ligação) + protótipo original
docs/governanca/   Constituição (v1_1) + Playbook (v1_3) + Prompt-mestre  ← LER antes de decidir
docs/passos/       handoffs por passo (mais recente: registro-execucao-a3-api-so-leitura + nota-descoberta-a3-api-envelope)
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
