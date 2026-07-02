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

## 4. Estado atual (jul/2026) — frame AO VIVO + 3D real + estágio cósmico COM lastro (Frente A feita)

| Componente | Estado |
|---|---|
| Banco reificado (PostgreSQL 16 + PostGIS 3.4) — carga **47**: 40 itens · 3 ClaimSets · 7 membros · 21 fontes · 16 públicos | ✅ reconstruível do DDL+migração |
| Camada de leitura gateada (função "O que acontecia no mundo?") | ✅ pública + curatorial |
| **API só-leitura — envelope `MomentResult` (forma β):** `core.f_momento_publico`/`_curatorial` (`011-momento-envelope.sql`, **adição**; cada campo §8 do autoritativo, reusando os helpers A4) + serviço fino (`service/atlas_api.py`, 2 endpoints) + portão por grant (`db/roles/020-papeis-leitura.sql`, 2 papéis) | ✅ **existe, gateada e provada.** Ainda **NÃO** ligada ao frame. |
| `verify.py` — invariantes T1–T10 (inventário T10: itens **40** · total **47**; `soma_ok` intacto) | ✅ 10/10 |
| `test_a4.py` — simultaneidade gateada A4-T1..T10 (A4-T5 total público no eixo = **16**) | ✅ 10/10 |
| `test_a3.py` — envelope A3-T1..T10 (público nunca não-fato · todo item §8 · gating por host) | ✅ 10/10 |
| `test_a3_http.py` — portão/HTTP A3-HTTP-1..5 (grant sem EXECUTE na curatorial · sem credencial de escrita) | ✅ 5/5 |
| **Modelo puro do frame (`frame/atlas-model.js`):** fonte ÚNICA do §8 — `fromStaticArray`/`fromEnvelope` (mesmo `SceneModel`), `overlayFields`, produtores overlay→markup; `regimeLabel` (cena esquemática); `CT` inclui `medição-direta` hifenizado (Frente A). Framework-free, testável em node. | ✅ **D-A3.7/6/virada + Frente A** |
| **Frame 3D de produção (`frame/atlas-3d-frame-v1.html`) — AO VIVO.** Consome `service/atlas_api.py` (`/momento/publico`, papel `atlas_public`) via `fromEnvelope`; comutador de fonte array⇄API; gates re-mapeados a papel/endpoint (OFF→pública; ON→curatorial token/localhost); badge esquemático no 3D. Shaders/câmera intactos. | ✅ **virado** (fallback honesto ao espelho local se a API cair) |
| `frame/tests/` (node, framework-free) — `3D-T1..5` (degradação cruzada), `ASSET-T1..3` (cena esquemática, nunca foto), `LIVE-T1..4` (virada: público nunca vaza · gating por host · **cósmico com lastro** · cliente sem segredo), **`COSMO-T1..5`** (cósmico não-vazio · nunca fato-documentado · anti-seeded · sem geometria · zero ClaimSet) | ✅ **5/5 · 3/3 · 4/4 · 5/5** |

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
  **Extensão aditiva (D-A3.virada):** `f_item_envelope_core` agora expõe `displayPoint:{lat,lng}`
  (centróide PostGIS `ST_Y/ST_X` da `geometry_version`; NULL senão) — adição derivada do autoritativo,
  nenhuma chave §8 muda (A3-T3 checa presença). **Atenção ao reaplicar `011`:** o `DROP TYPE … CASCADE`
  recria as funções e **perde os grants de papel** — reaplicar `020` em seguida (o bootstrap já faz).
- **Config 12-factor (Opção A):** credenciais saem do código para `.env` (gitignored); `.env.example`
  documenta as 4 vars (`ATLAS_DB_PASSWORD`/`ATLAS_PUBLIC_PASSWORD`/`ATLAS_CURATORIAL_PASSWORD`/
  `ATLAS_CURATORIAL_TOKEN`). `docker-compose` interpola `${ATLAS_DB_PASSWORD:?}`; o serviço **recusa
  subir** sem var (exit 2). `db/roles/020` mantém senhas-dev de papel (homônimas, casadas pelo `.env`);
  gerenciador de segredos com rotação/auditoria (Opção B) fica para a **E14**.
- **Divergência da carga fixada na descoberta** (`docs/passos/nota-descoberta-a3-api-envelope.md`):
  só **`kpg-causa`** tem host em `v_publishable_public` (`chicxulub`); `rev-francesa`/`goe-ritmo` têm
  host com fonte-por-asset pendente → **não** vazam pela pública (gating por host, §5.5 do plano).
- **Frente A — cósmicos como corpus COM fonte (jul/2026, FEITA).** 5 itens cósmicos entraram no
  `migrate.py` como **adição** (`evt:big-bang`, `state:cmb-recombinacao`, `proc:formacao-galaxias`,
  `evt:formacao-sistema-solar`, `proc:formacao-terra`), todos **corpus/approved/públicos**,
  `sourceTimeBasis=Ga`, **sem geometria** (global → `displayPoint` NULL, `geometryRegime
  semLugarTerrestre`), com `Source`/`provenance_ref` ([N1]). **Nenhum** é `fato-documentado`
  (o CMB é `medição-direta`; os demais `inferência-científica`); **sem ClaimSet** (etapa-3.1 §10.7).
  Aresta-ponte `proc:formacao-terra` —`precede`→ `proc:goe`. O estágio cósmico **deixou de vir
  vazio** na porta pública. Plano/tabela assinada: `docs/passos/plano-cosmicos-corpus-com-fonte-v1_0.md`
  + `docs/passos/nota-descoberta-cosmicos-frente-a.md`; handoff `registro-execucao-cosmicos-frente-a.md`.
  O `CT` do frame ganhou a chave hifenizada `medição-direta`; os teasers `rep:*` (sem lastro) foram
  substituídos, no espelho estático, pelos 5 itens reais do corpus.
- **"Reconstruível do bootstrap" está PROVADO em Windows e Linux:**
  `cp .env.example .env` (ajuste os valores) e então `docker compose down -v && bash scripts/bootstrap.sh`
  fecha **10/10 + 10/10 + 10/10 + 5/5** em volume novo (carga `claimsets 3 · membros 7 · total 47 ·
  itens 40 · fontes 21 · públicos 16`). O bootstrap **recusa seguir sem `.env`** (12-factor). Suítes
  do frame (node): `3D-T 5/5 · ASSET-T 3/3 · LIVE-T 4/4 · COSMO-T 5/5`.
- **3 ClaimSets de host `pending` foram removidos do frame** (`direitos-limites`, `inconfidencia`,
  `escravidao-central`) e enfileirados em `docs/roteiro/fila-revisao-claimsets-sensiveis.md`
  (Trilha C / Playbook §5) — aguardam host aprovado para reintegração; conteúdo preservado no git.

A regra do miolo continua valendo: não reescreva `db/ddl/`/`db/read-layer/` "para melhorar" sem
antes rodar os testes e mantê-los verdes.

---

## 5. Virada ao vivo + 3D real — FEITA. Próximas frentes.

Plano de execução em `docs/passos/passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md`; descoberta em
`docs/passos/nota-descoberta-a3-virada-3d.md`; handoff em `docs/passos/registro-execucao-a3-virada-3d.md`.

**Já feito (esta sessão):** **D-A3.7** (`SceneModel`/`overlayFields` puros; 3 renderizadores DESENHAM
o §8, não reconstroem) · **D-A3.6** (assets procedurais rotulados esquemáticos, nunca foto) ·
**D-A3.virada** (frame consome `/momento/publico` via `fromEnvelope`; comutador de fonte; gates→papel;
`displayPoint` aditivo em `011`) · **Config Opção A** (12-factor). Provado: `3D-T 5/5 · ASSET-T 3/3 ·
LIVE-T 4/4` + os quatro verdes do banco. A divergência frame↔corpus está **extinta por construção**.

**Frente A — cósmicos como corpus COM fonte: ✅ FEITA (jul/2026).** 5 âncoras (Abordagem 2) entraram
como corpus fonteado; o estágio cósmico **deixou de vir vazio** na porta pública, sem promover seeded,
sem foto, sem falsa equivalência. Provado: `COSMO-T 5/5` + re-verde de todas as suítes. Detalhe no §4 e
em `docs/passos/registro-execucao-cosmicos-frente-a.md`.

**Próximas frentes (não nesta sessão):**

1. **F-A.3 — mídia cósmica real: PLANEJADA E ASSINADA (execução pendente; frente imediata, E14 em seguida).**
   Forks travados: **técnica A** (envelope `011` estende `media[]`, padrão aditivo do `displayPoint`;
   reaplicar `020` após o `CASCADE`) · **cadência 5 de uma vez** · **CMB reforçado com claim-sobre-asset**.
   `natureLabel` por asset: **Big Bang = `representação-artística`** (sem foto, §10.7) · **CMB = `mapa`**
   (medição visualizada; casa com `medição-direta`) · **galáxias = `fotografia`** (deep field real, legenda
   de *look-back time*) · **sistema solar = `fotografia`** (disco protoplanetário **análogo**, legenda "não
   o nosso Sol") · **Terra = `representação-artística`**. Distribuição: **2 foto · 1 mapa · 2 reconstrução**.
   Guardrails inegociáveis: cena **sempre esquemática** (asset só no dossiê, **nunca** textura;
   ASSET-T/COSMO-T4/R-V7) · **licença por asset** no portão da Etapa 1.1 (PD/CC-BY → `media-store`) ·
   **anti-seeded** (aresta `representa` com proveniência) · suíte nova **`MEDIA-T1..5`** + re-verde de tudo
   em volume novo. **Execução começa pela sub-checagem read-only do DDL** (`media_asset` já reificada?
   `nature_label`/`license_profile_ref`/`storage_partition` + aresta `representa`?). Docs:
   `docs/passos/plano-cosmicos-midia-real-f-a3-v1_0.md` +
   `docs/passos/f-a3-decisoes-assinadas-handoff-execucao-v1_0.md` (o registro traz o prompt de retomada).
   **Ainda aberto (opcional, pós-F-A.3):** tensão de Hubble como controvérsia estreita (host
   público+fonteado), se a `etapa-3.1` justificar. **Nunca** promover seeded; **nunca** virar foto.
2. **Reintegrar as 3 sensíveis** (`direitos-limites`, `inconfidencia`, `escravidao-central`) quando o
   host sair de `pending` (Trilha C; `docs/roteiro/fila-revisao-claimsets-sensiveis.md`). **Não** religar
   ao vivo enquanto host for `pending`.
3. **E14 — segredos Opção B** (gerenciador com rotação/auditoria/RIPD) + auth real da porta curatorial
   (hoje token só localhost).
4. **Preservar sempre:** §8 idêntico nos 3 degraus; gating por construção; cena de tempo profundo
   sempre esquemática/reconstrução.

---

## 6. Como rodar (setup)

**Pré-requisitos:** Docker + Docker Compose; Python 3.9+ no host; Node (para as suítes do frame).

```bash
cp .env.example .env     # 12-factor: credenciais locais (gitignored). Ajuste os valores.
bash scripts/bootstrap.sh
```

Isso: **carrega `.env`** (recusa seguir sem ele), sobe Postgres+PostGIS num **volume persistente**
(`atlas-pgdata`), aplica o DDL + camada de leitura (`010`) + envelope (`011`) + papéis (`020`), migra a
carga (`claimsets 3 · membros 7 · total 47 · itens 40`), e roda `verify` + `test_a4` + `test_a3` +
`test_a3_http` (devem fechar **10/10 + 10/10 + 10/10 + 5/5**).

Credenciais vêm do `.env` (ver `.env.example`): `ATLAS_DB_PASSWORD` (usuário `atlas`),
`ATLAS_PUBLIC_PASSWORD`/`ATLAS_CURATORIAL_PASSWORD` (papéis de `020`), `ATLAS_CURATORIAL_TOKEN` (header).

Suítes do frame (node, sem build): `node frame/tests/test_3d.js` · `test_assets.js` · `test_live.js` ·
`test_cosmo.js` (**5/5 · 3/3 · 4/4 · 5/5**). As `LIVE-T`/`COSMO-T` rodam sobre fixtures reais em
`frame/tests/fixtures/`.

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
db/ddl/            esquema reificado (DDL) — 001-esquema-reificado.sql
db/read-layer/     camada de leitura gateada — 010-leitura-simultaneidade.sql · 011-momento-envelope.sql (envelope MomentResult, adição)
db/roles/          papéis de leitura — 020-papeis-leitura.sql (atlas_public / atlas_curatorial; portão por grant)
db/migration/      migrate.py (carga 42) · verify.py (T1–T10) · test_a4.py (A4-T1..T10) · test_a3.py (A3-T1..T10) · test_a3_http.py (A3-HTTP-1..5)
db/reports/        relatórios verdes de referência (migration/verification/test_a4/test_a3/test_a3_http)
service/           atlas_api.py — serviço fino só-leitura (2 endpoints; recusa subir sem var)
frame/             atlas-model.js (modelo puro: fonte única do §8) · atlas-3d-frame-v1.html (frame AO VIVO) · tests/ (3D-T/ASSET-T/LIVE-T/COSMO-T + fixtures/) · protótipo original
.env.example       modelo das 4 vars (12-factor); copie para .env (gitignored)
docs/governanca/   Constituição (v1_1) + Playbook (v1_3) + Prompt-mestre  ← LER antes de decidir
docs/passos/       handoffs por passo (mais recente: plano-cosmicos-midia-real-f-a3 + f-a3-decisoes-assinadas-handoff-execucao — planejamento F-A.3 assinado, execução pendente)
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
