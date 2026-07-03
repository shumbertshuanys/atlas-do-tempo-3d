# Passo A3 — Produção 3D real + ligação ao vivo do frame · Handoff de planejamento

**Versão:** v1.0
**Data:** jun/2026
**Antecede:** execução no Claude Code (esta sessão é de PLANEJAMENTO — não escreve código)
**Sucede:** A4 (fundação reificada + camada de leitura gateada, 10/10 + 10/10, Windows e Linux)
**Natureza:** handoff no formato de 9 pontos do Playbook §2. Fecha as oito decisões do A3 e fixa a ordem de execução e os artefatos falsificáveis de cada frente.

> **Nota (pós-execução da fatia de pendências):** três premissas deste plano foram superadas na
> execução e estão **corrigidas in loco** abaixo (marcadas como *[corrigido pós-execução]*):
> (i) R-A3.1 — a adição exige atualizar o fixture do T10; (ii) §6 — o banco só tem clima de
> tempo profundo, não há clima moderno; (iii) D-A3.1/§3 — `direitos-limites` tem host **pending**
> no corpus (o frame estava bugado), então o split real é 1 modelado + 3 na fila. Detalhe em
> `docs/passos/registro-execucao-a3-pendencias.md`.

---

## 1. Objetivo

Levar o frame de produção (`frame/atlas-3d-frame-v1.html`) de **espelho curado estático** a **experiência 3D real conectada ao banco ao vivo**, em três frentes que convergem: (a) produção 3D procedural dos três regimes-âncora com degradação 3D→2D→estático; (b) uma API mínima só-leitura que expõe a função "O que acontecia no mundo?" como envelope `MomentResult` completo; e (c) a reconciliação das duas divergências frame↔corpus que precisam cair **antes** de ligar ao vivo. Tudo preservando o gating por construção (A4) e o contrato visual §8 em todos os modos.

## 2. Escopo

**Fará (no Claude Code):**
- Reconciliar frame↔corpus (ClaimSets e domínio `clima`).
- Adicionar ao banco a função-envelope `MomentResult` **ao lado** das funções A4 provadas.
- Subir um serviço fino só-leitura com dois endpoints (público/curatorial) atrás de dois papéis de banco.
- Construir os três renderizadores (3D/2D/estático) sobre um `SceneModel` único com overlay §8 renderer-agnóstico, assets procedurais.
- Virar a fonte do `SceneModel` do array estático para a API.

**Não fará:** ver o Rodapé.

## 3. Diagnóstico

Três achados governam o plano:

- **As duas pendências são a mesma divergência em direções opostas.** ClaimSets: o frame autora **6**, o corpus modela **2** (`goe-ritmo`, `kpg-causa`) — frame à frente. Domínio `clima`: o banco tem 2 itens, o frame não tem a lente — corpus à frente. E os 4 ClaimSets extras **não são homogêneos**. ***[corrigido pós-execução]*** O **corpus é autoritativo sobre o frame**: apenas `rev-francesa` (host `evt:estados-gerais-1789`) tem host `approved`; `direitos-limites`, `inconfidencia` e `escravidao-central` têm host `pending` no corpus e **não** podem ser worked-examples públicos sem passar pela fila de revisão (Playbook §5; §5.4 — fronteira escrita à mão, nunca automatizada). *O plano original supôs `direitos-limites` como host `approved`; era um **bug do frame** (`evt:declaracao-direitos-1789` com `rev:'approved'` divergindo do corpus `mediado`→`pending`), corrigido na execução.* Split real: **1 modelado no corpus + 3 na fila**.
  - *Esta classe de divergência frame↔corpus se **extingue por construção** na ligação ao vivo (D-A3.3+): quando o frame consome a API/funções-envelope em vez de arrays estáticos, `review_status`/selo/`is_fact` passam a vir sempre do autoritativo — não há mais espelho manual para dessincronizar.*
- **"Ligar ao vivo" não é "trocar o array pela API".** A função A4 devolve um `t_simultaneidade_row` magro (`id, title, item_type, epistemic_type, selo, is_fact`); o §8 e o contrato `WhatWasHappeningAtMoment` (Etapa 11) exigem o envelope completo (incerteza-como-faixa, fronteira de `ClaimSet` com pesos assimétricos, anacronismo, atribuição, geometria por regime, `publicabilityStatus`, `gatingReason`). O envelope tem de nascer **no banco** (derivado do autoritativo), não montado na camada de aplicação.
- **O §8 não pode morar dentro de nenhum renderizador.** Se os rótulos epistêmicos forem desenhados pelo three.js, somem quando o 3D some — o que a §8.3 proíbe. Logo o contrato visual é um **overlay renderer-agnóstico** acima de um `SceneModel` único, e os três renderizadores são funções puras desse modelo. Além disso, paleogeografia é **sempre reconstrução rotulada** (§8.2): nada de Terra fotorrealista anacrônica no tempo profundo.

Ordem de decisão escolhida nesta sessão: **pendências → API → 3D**, porque as duas primeiras gateiam a ligação ao vivo e o 3D pode correr em paralelo via adaptador.

## 4. Decisões principais

| ID | Decisão |
|---|---|
| **D-A3.1** | **ClaimSets — reconciliação assimétrica.** ***[corrigido pós-execução]*** Modelar no corpus (`claim_set` + `claim_set_member`, fronteira manual) só `rev-francesa` (único com host `approved`). Remover do frame `direitos-limites`, `inconfidencia` e `escravidao-central` enquanto hosts forem `pending`; registrá-los como tarefa na fila de revisão (Trilha C). *(O plano supôs `direitos-limites` `approved`; era bug do frame — host é `pending` no corpus.)* |
| **D-A3.2** | **Clima — robusta.** Adicionar `clima` a `DOMAINS`/`lensOn`/UI **e** trocar `DOMAINS[it.dom]` por *lookup* tolerante (domínio desconhecido → rótulo neutro com aviso, sem quebrar). Reconciliação ampla das 7 lentes canônicas fica fora do A3. |
| **D-A3.3** | **Envelope no banco.** Criar `core.f_momento_publico`/`_curatorial` **ao lado** das funções A4 (que ficam intactas), devolvendo o `MomentResult` completo, cada campo derivado do autoritativo. É adição, não reescrita do miolo. |
| **D-A3.4** | **Fronteira HTTP.** Serviço fino, só-leitura, escrito à mão (FastAPI/Node mínimo); dois endpoints que chamam as funções e serializam o envelope. Sem caminho de escrita. |
| **D-A3.5** | **Portão na API.** Dois endpoints + dois papéis de banco. Papel público com `EXECUTE` só na função pública; curatorial atrás de autenticação. Portão é *grant*, não `if` de runtime. |
| **D-A3.6** | **Assets procedural/shader-first.** Cosmos, Terra profunda e globo de 1789 por shaders e geometria procedural; self-contained, sem pipeline de asset externo, sem ônus de licença, esquemático por padrão no tempo profundo. |
| **D-A3.7** | **Degradação por modelo único.** Um `SceneModel` alimenta `render3D`/`render2D`/`renderStatic` (puros); o overlay §8 é renderer-agnóstico, montado por cima de qualquer degrau. *Fallback* sem WebGL cai para 2D/estático. |
| **D-A3.8** | **Escopo + adaptador.** Tratamento completo dos três regimes-âncora (cósmico Big Bang→Sol; Terra profunda GOE e K-Pg; histórico 1789) sobre os 7 STAGES. O `SceneModel` tem formato **compatível com o array estático e com o envelope da API** — o 3D constrói-se contra o array e a virada ao vivo troca uma fonte só. |

## 5. Modelo conceitual

- **`SceneModel`** = envelope `MomentResult` (D-A3.3) + metadados de apresentação (estágio, câmera, regime). Fonte única dos três renderizadores e do overlay §8. Formato idêntico vindo do array estático ou da API.
- **Overlay §8** (renderer-agnóstico): rótulos de tipo/confiança, incerteza-como-faixa com redundância não-cromática, fronteira de `ClaimSet` com pesos assimétricos, `AnachronismNotice`, atribuição, equivalente textual. Presente em **todo** degrau.
- **Funções-envelope** `f_momento_publico`/`_curatorial`: derivam selo/`is_fact`/`epistemic_type`/atribuição do item-claim → proveniência → fonte (reaproveitam `f_item_attribution`/`f_item_epistemics` do A4); aplicam o invariante de exibição e o anti-falsa-equivalência; nunca expõem `hiddenItems` como fato.
- **Dois papéis de banco**: `atlas_public` (EXECUTE só na função pública) e `atlas_curatorial` (autenticado). Portão por *grant*.

## 6. Fontes necessárias

Nenhuma fonte externa nova. O passo se apoia no corpus: Etapa 5 (contrato `MomentQuery`/`MomentResult`), Etapa 10 (degradação, `ViewDegradationLadder`, invariante 16, `EquivalenceWarningNotice`), Etapa 11 (§6 contratos de leitura factual; §11.8–11.10 sustentação 3D/2D/estático; "API não escreve fato"), Playbook §8 (contrato visual) e §5 (fila de revisão), Constituição Arts. 7 e 12, recentragem (lentes canônicas), A4 (`f_simultaneidade_*`, views gateadas).

**Descoberta obrigatória antes de implementar D-A3.2:** ler em `db/migration/migrate.py`/DDL a **identidade, o `epistemic_type` e o `selo` dos 2 itens de clima** do banco — não estão sincronizados neste conhecimento e a lente clima precisa nascer com o rótulo certo. ***[corrigido pós-execução]*** Resultado da descoberta: o banco só tem clima de **tempo profundo** — `state:clima-goe` (**hipótese**, GOE ~2,4 Ga) e `state:clima-pos-impacto-kpg` (**inferência-científica**, K-Pg ~66 Ma), ambos `pending`, selo **em-revisão**, gated (público = 0). **Não há item de clima moderno**, logo a premissa "consenso × negacionismo-rejeitado" **não se aplica** ao corpus atual; a lente nasce com esses rótulos por-item e **sem** UI de consenso×negacionismo.

## 7. Riscos

- **R-A3.1 — Modelar ClaimSet quebra o verde A4.** ***[corrigido pós-execução]*** A adição **não** mantém o verde sozinha: `verify.py` T10 assere igualdade com um **inventário hard-coded** (`claimsets`/`claims_membros`/`claims_total`), que muda com o ClaimSet novo. *Mitig.:* modelar como **adição** **e** atualizar o fixture do T10 **só** nessas contagens — a invariante estrutural `soma_ok` (`claims_total == itens + membros`) permanece intacta (o guardrail protege a invariante, não o inventário). O fixture vem da **intenção** (N planejado); se a carga real não bater, o T10 **deve falhar**. Rodar `bootstrap.sh` e confirmar 10/10 + 10/10 **antes** de avançar para a API.
- **R-A3.2 — Os 3 ClaimSets de host pending removidos do frame caem no esquecimento.** *Mitig.:* registrá-los como tarefa explícita e rastreada na fila de revisão (Trilha C §5; `docs/roteiro/fila-revisao-claimsets-sensiveis.md`); não some sem rastro.
- **R-A3.3 — A função-envelope vaza lógica de gating errada.** *Mitig.:* testes A3-T* espelhando `test_a4`; cada campo derivado do autoritativo; `hiddenItems` nunca como fato.
- **R-A3.4 — §8 embutido num renderizador morre na degradação.** *Mitig.:* overlay renderer-agnóstico (D-A3.7); teste cruzado entre degraus.
- **R-A3.5 — Fotorrealismo anacrônico no tempo profundo.** *Mitig.:* procedural/esquemático rotulado por padrão (D-A3.6; §8.2).
- **R-A3.6 — Frame quebra com o conjunto aberto do banco ao vivo (`clima` é só o 1º sintoma).** *Mitig.:* *lookup* tolerante (D-A3.2 robusta).
- **R-A3.7 — Papel público recebe `EXECUTE` na função curatorial por descuido de config.** *Mitig.:* teste de *grant* que falha se alguém afrouxar (parte do artefato HTTP).
- **R-A3.8 — 3D contra array e contra API divergem na virada.** *Mitig.:* `SceneModel` de formato único compatível com ambos; virada = troca de uma fonte.

## 8. Entregáveis (no repo, após execução)

- `db/read-layer/011-momento-envelope.sql` (funções-envelope, **adição**).
- Migração de adição do ClaimSet modelado (`rev-francesa` — único com host `approved`).
- `frame/atlas-3d-frame-v1.html` atualizado: lente `clima` + *lookup* tolerante; 3 ClaimSets de host pending removidos; `SceneModel` + overlay §8 + três renderizadores; assets procedurais dos 3 regimes; fonte comutável estático↔API.
- Serviço fino só-leitura (2 endpoints) + config dos 2 papéis de banco.
- Testes novos: SQL A3-T* (envelope) + teste de nível HTTP (gating + *grant* + campos §8) + teste de degradação cruzada.
- Tarefas registradas na fila de revisão para `inconfidencia` e `escravidao-central`.
- `CLAUDE.md` atualizado (tabela de estado: frame deixa de ser "espelho estático").
- Este handoff em `docs/passos/`.

## 9. Próximos passos (ordem de execução no Claude Code)

1. **Bootstrap e confirmar verde** (`bash scripts/bootstrap.sh` → 10/10 + 10/10). Sem isso, não avançar (PG1).
2. **Pendências (gateiam a ligação):**
   a. Descoberta: ler identidade/`epistemic_type`/`selo` dos 2 itens de clima.
   b. D-A3.1: modelar `rev-francesa` no corpus (único host `approved`); remover do frame os 3 de host pending (`direitos-limites`/`inconfidencia`/`escravidao-central`); registrar tarefas de revisão. **Atualizar fixture do T10 e re-rodar bootstrap → 10/10 + 10/10** (R-A3.1).
   c. D-A3.2: lente `clima` + *lookup* tolerante.
3. **API:** D-A3.3 (funções-envelope + testes A3-T*) → D-A3.4/D-A3.5 (serviço fino, 2 endpoints, 2 papéis + teste HTTP de gating/*grant*/campos §8).
4. **3D (em paralelo desde já, contra o array via `SceneModel`):** D-A3.7 (modelo único + overlay §8 + 3 renderizadores) → D-A3.6 (assets procedurais dos 3 regimes) → teste de degradação cruzada.
5. **Virada ao vivo:** comutar a fonte do `SceneModel` do array para a API. Ponto de convergência das frentes 3 e 4.
6. **Preservar §8 e o gating por construção** em todos os degraus; **commits por mudança lógica**, não um commit-monstro.

**Artefatos falsificáveis ("pronto = evidência"):**
- *Pendências:* contagem de `ClaimSets` no frame == corpus; itens de clima renderizam com o rótulo epistêmico correto; domínio desconhecido **não** quebra o frame.
- *API:* endpoint público nunca retorna `is_fact = false`/`pending`/`seeded-demo`; papel público **sem** `EXECUTE` na função curatorial; todo item retornado carrega os campos §8 obrigatórios.
- *3D:* rótulos e fronteira de `ClaimSet` idênticos em 3D/2D/estático para o mesmo momento; nenhum item de tempo profundo sem "reconstrução modelada"; equivalente textual em todos os degraus; sem WebGL cai a 2D/estático sem perda.

---

## Rodapé — o que este passo NÃO faz

- **NÃO reabre** B1 (motor de banco) nem B2 (reificação); **NÃO reescreve** `db/ddl/`/`db/read-layer/` provados — só **adiciona** (envelope ao lado das funções A4).
- **NÃO promove** `seeded-demo` a corpus nem a fato.
- **NÃO publica** os 3 ClaimSets de host pending (`direitos-limites`, `inconfidencia`, `escravidao-central`) — ficam na fila de revisão (Trilha C) até host aprovado.
- **NÃO faz** a reconciliação ampla das 7 lentes canônicas (só adiciona `clima`).
- **NÃO usa** assets com licença restritiva (procedural) nem fotorrealismo anacrônico no tempo profundo.
- **NÃO cria** camadas de usuário/escola — fora do MVP enxuto.
- **NÃO desliga** a honestidade epistêmica em nenhum degrau de degradação (§8.3).
