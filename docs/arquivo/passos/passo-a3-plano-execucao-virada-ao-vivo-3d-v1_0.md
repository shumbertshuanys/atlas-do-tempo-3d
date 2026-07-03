# Passo A3 — Plano de execução da virada ao vivo + 3D real (D-A3.6..8 + a virada) · Handoff de planejamento

**Versão:** v1.0
**Data:** jun/2026
**Antecede:** execução no Claude Code (esta sessão é de PLANEJAMENTO — **não escreve código**, como foi o plano da API)
**Sucede:** API só-leitura (D-A3.3/4/5) concluída e verde — envelope `MomentResult` (forma β), serviço fino, portão por grant; provada `A3-T1..10` + `A3-HTTP-1..5` (`registro-execucao-a3-api-so-leitura.md` + `nota-descoberta-a3-api-envelope.md`).
**Natureza:** handoff no formato de 9 pontos do Playbook §2. **Não reabre** D-A3.6/7/8 (já tomadas em `passo-a3-plano-producao-3d-ligacao-ao-vivo-v1_0.md`); **detalha-as para execução** sob "pronto = evidência" (PG1).

> **O que fecha nesta sessão (os 4 pontos pedidos):** (1) o formato exato do `SceneModel` + o adaptador que faz **array estático** e **envelope β da API** caírem no mesmo formato; (2) o contrato do **overlay §8** e dos **3 renderizadores**, com o **teste cruzado** que prova rótulo/fronteira-de-ClaimSet/anacronismo/equivalente-textual idênticos em 3D/2D/estático; (3) a **virada ao vivo** (frame consome o endpoint PÚBLICO de `service/atlas_api.py`, papel `atlas_public`) + a **decisão de segredos** (12-factor mínimo × gerenciador) — **decidida: Opção A, 12-factor mínimo**; (4) a **ordem de execução** no Claude Code e o artefato/handoff final.

---

## 1. Objetivo

Levar `frame/atlas-3d-frame-v1.html` de **espelho curado estático** a **experiência 3D real ligada ao banco ao vivo**, executando as três decisões de 3D já tomadas (D-A3.6 assets procedurais; D-A3.7 modelo único + overlay §8 renderer-agnóstico; D-A3.8 escopo + adaptador) e a **virada de fonte** (array → endpoint público), **sem tocar o miolo provado do banco** e preservando o contrato visual §8 e o gating por construção em todo degrau. A API que extingue a divergência frame↔corpus por construção **já existe e está verde**; aqui se constrói o consumidor e se troca **uma fonte só**.

## 2. Escopo

**Fará (no Claude Code):**
- Refatorar o frame para um **`SceneModel` único** + **`overlayFields` puro** (§8) consumidos por **três renderizadores** (3D/2D/estático), todos funções do modelo — **sem** cada renderizador reconstruir o §8.
- Escrever o **adaptador de duas bocas**: `fromStaticArray(ITEMS, CLAIMSETS, stage)` **e** `fromEnvelope(momentResult, stage)`, ambos devolvendo o **mesmo** `SceneModel`.
- Consolidar os **assets procedurais/shader-first** dos três regimes-âncora (cosmos; Terra profunda GOE/K-Pg; globo 1789), self-contained, **esquemáticos rotulados** no tempo profundo.
- **Virar a fonte** do `SceneModel`: o frame passa a consumir `service/atlas_api.py` (`/momento/publico`, papel `atlas_public`) no lugar dos arrays `ITEMS`/`CLAIMSETS`.
- Testes falsificáveis novos do frente-end (`3D-T1..5` de degradação cruzada + `LIVE-T1..4` de virada) e a decisão de **config/segredos**.

**Não fará:** ver o Rodapé. Em particular, **não** reescreve `db/ddl/`/`db/read-layer/010`/`011` (a virada é do **frame**; o banco só recebe, *se a descoberta exigir*, **uma extensão aditiva mínima de coordenada** — §6 nº 1); **não** promove `seeded-demo` a corpus; **não** religa as 3 sensíveis (host `pending`); **não** embute segredo curatorial no cliente.

## 3. Diagnóstico

Quatro achados governam o plano — três herdados, um **novo, levantado nesta leitura**.

- **"Virar ao vivo" extingue a divergência frame↔corpus por construção — e a expõe.** Quando a fonte vira a função-envelope, `review_status`/`selo`/`is_fact` passam a vir **sempre** do autoritativo: não há mais espelho manual para dessincronizar. **Mas** a porta pública é deliberadamente magra. Pela `nota-descoberta-a3-api-envelope.md`: na janela **1789** a porta pública mostra **só** `concept:iluminismo` + `evt:posse-washington-1789` (2 itens) e **zero** ClaimSets (o host de `rev-francesa` tem fonte-por-asset pendente → não vaza); só em **K-Pg** a porta é rica (6 itens públicos, incluindo o host `chicxulub`, + o ClaimSet `kpg-causa`). Logo a vista pública ao vivo é **heterogênea por estágio** — rica no K-Pg, magra em 1789/GOE. Isso é **honesto e é informação** ("nada conhecido neste instante por estas lentes — e isso é informação", já no frame), mas significa que **a riqueza atual do frame é, na prática, uma vista curatorial** (mostra `pending`/`seeded-demo` com selos via `gate.pending`/`gate.seeded` ligados). **Resolução proposta (§5.5):** preservar os toggles `gate.*` re-mapeando-os de *filtro-de-superset-no-cliente* para *seleção de papel/endpoint* — público por padrão (gating por construção), curatorial só em localhost com token. As duas faces já existem (dois endpoints, dois papéis); não se cria nada novo.
- **`seeded-demo` nunca é corpus; logo a virada revela o que era só-frame.** ***[achado novo]*** Os três teasers cósmicos do frame (`rep:bigbang`/`rep:galaxies`/`rep:sun`) estão marcados `prov:'corpus', rev:'approved'` **no frame**, mas **pode não haver lastro no corpus** (os 35 itens da carga). Se não houver, o **estágio cósmico fica vazio contra a API pública** — exatamente a divergência que a virada deve expor, não maquiar. Idem para os quatro itens `seeded-demo` de 1789 (Lavoisier, mecânica celeste, Andes, arau-gigante): por construção **somem** da porta pública. É **descoberta obrigatória** (§6 nº 2) confirmar o lastro cósmico antes de virar.
- **O §8 não pode morar dentro de nenhum renderizador.** Hoje cada caminho de render do frame reconstrói o §8 por conta própria: `updateLabels3D`/`buildLabel` (3D), `draw2D`/`drawChip` (2D), `renderStatic` (estático), `renderDetailBody`/`renderClaimset` (painel). Três fontes de verdade que **podem derivar** — viola a §8.3 (o contrato tem de sobreviver idêntico à degradação) e o Art. 12. A correção é um **único** `overlayFields(item) → OverlayModel` puro, consumido pelos três renderizadores; cada renderizador **desenha** o OverlayModel, **nunca o gera**.
- **A apresentação não está no envelope; o adaptador a injeta.** O envelope β devolve itens + ClaimSets + tempo/espaço normalizados + avisos + agregados de gating. Ele **não** carrega `stage`/`câmera`/`regime` (cósmico×terrestre) — isso é metadado de apresentação dos `STAGES` do frame (datum 3Z; `cam`/`kind`/`scalar`). O `SceneModel` = **envelope (corpus) + apresentação (frame)**; o adaptador **liga** cada item ao estágio por uma função pura `stageForScalar(canonical_scalar)`, derivada do tempo, **não** do corpus.

Ordem escolhida: **modelo único + overlay (D-A3.7) → assets (D-A3.6) → virada de fonte → config/segredos**. O 3D corre **contra o array** desde já (D-A3.8); a virada troca uma fonte só.

## 4. Decisões principais (já tomadas; aqui detalhadas para execução)

| ID | Decisão | Detalhe de execução |
|---|---|---|
| **D-A3.6** | Assets procedural/shader-first | Cosmos, Terra profunda e globo 1789 por shaders/geometria procedural (o GLSL já existe no frame — `GLSL_NOISE`, materiais de Terra/atmosfera); **consolidar e rotular**. Self-contained, sem pipeline externo, **sem ônus de licença**, **esquemático rotulado** por padrão no tempo profundo (§8.2; Art. 7). |
| **D-A3.7** | Degradação por modelo único | Um `SceneModel` (§5.1) alimenta `render3D`/`render2D`/`renderStatic` **puros**; o **overlay §8** (`overlayFields`, §5.3) é renderer-agnóstico, montado por cima de **qualquer** degrau. Sem WebGL cai a 2D→estático **sem perda** (Art. 12; E11 §11.10). |
| **D-A3.8** | Escopo + adaptador | Três regimes-âncora sobre os 7 `STAGES`. `SceneModel` de **formato compatível com o array estático E com o envelope β** (§5.2): o 3D constrói-se contra o array; a virada troca uma fonte. |
| **D-A3.7a** *(detalhe)* | Vínculo item↔estágio | Função pura `stageForScalar(scalar)` mapeia o `canonical_scalar` do item ao estágio dos `STAGES` (apresentação, **não** corpus). A janela do scrubber → estágio ativo → janela canônica `[start,end]` → consulta. |
| **D-A3.virada** *(detalhe)* | Re-mapeamento dos toggles `gate.*` | `gate.pending`/`gate.seeded` deixam de filtrar superset no cliente e passam a **selecionar papel/endpoint**: ambos OFF → `/momento/publico` (`atlas_public`; gating por construção); ON → `/momento/curatorial` (token; **só** localhost/rede interna até E14). |
| **D-A3.segredos** | Config que gateia sair de localhost | **DECIDIDA: Opção A (12-factor mínimo)** — `.env` gitignored + `.env.example` + interpolação no `docker-compose` + serviço que recusa subir sem var (§5.6). **B** (gerenciador de segredos) agendada para E14. |

## 5. Modelo conceitual

### 5.1 `SceneModel` — o formato exato (dicionário conceitual, não código)

> Forma derivada do envelope `MomentResult` (β) **+** metadados de apresentação. **Idêntico** vindo do array ou da API — é o que permite **um adaptador só** e a virada trocar **uma fonte**.

```txt
SceneModel = {
  source,                 # 'static-array' | 'api-public' | 'api-curatorial'  (proveniência da FONTE; auditável)
  porta,                  # 'publico' | 'curatorial'  (eco do envelope; governa valores admissíveis)
  stage,                  # APRESENTAÇÃO (do frame, NÃO do corpus): {id, name, disp, regime, scalar, cam, kind}
  query,                  # eco do pedido: janela canônica [start,end] + lentes ativas
  normalizedTimeRange,    # do envelope β: [canonicalStart, canonicalEnd] + displayTime por regime + sourceTimeBasis
  normalizedSpatialScope, # do envelope β: escopo + geometria em uso, rotulada
  items[],                # cada item = SceneItem (§5.2)
  claimSets[],            # do envelope β: fronteira manual + pesos assimétricos; público = filtrado por host
  warnings: {anachronism[], equivalence[]},   # AnachronismNotice / EquivalenceWarningNotice (E5 §9; E10 §11.4)
  publicabilityStatus,    # 1–5 (público do conjunto exibido = 1)
  gatingReason, gatingType,
  hiddenSummary           # público: SÓ contagem; curatorial: lista — nunca como fato
}

SceneItem = {
  itemId, title, itemType,
  epistemicType,          # VOCAB CANÔNICO do corpus (espaço: "fato documentado", "inferência científica", …)
  confidenceLevel, evidenceLevel,            # confidence: f_item_epistemics; evidence: core.claim.evidence_level
  selo, isFact, reviewStatus,                # selo persiste em todo modo; público = is_fact TRUE / approved
  uncertaintyRange,       # [start,end] canônico — a FAIXA (nunca um ponto); §8.1.4
  uncertaintyDisplayPolicy,                  # ∈ {sempreRotular, rótuloCompacto, aparatoCompleto} — NUNCA "omitir"
  geometryRegime,         # modernGeometry | paleoPositions | semLugarTerrestre | (modernCorrespondence | historicalGeometryVersions)
  reconstructionFlag,     # tempo profundo / paleo → true (§8.2; CHECK no banco)
  displayPoint,           # {lat,lng} | null  ← CONFIRMAR que o envelope expõe (§6 nº 1)
  attributionRef: {label, provenanceRef, authorityTier},   # [N1] provenanceRef NOT NULL
  claimSetRef,            # id do ClaimSet hospedado, se houver
  presentationStage       # = stageForScalar(canonical_scalar) — apresentação, não corpus
}
```

### 5.2 O adaptador de duas bocas — mesmo alvo a partir de duas fontes

`fromStaticArray` e `fromEnvelope` são **puros e framework-free** (testáveis em node, sem DOM). Mapa de campos (origem → alvo normalizado):

| `SceneItem` (alvo) | `fromStaticArray` (chaves do frame) | `fromEnvelope` (campos β) | Nota |
|---|---|---|---|
| `itemId`/`title`/`itemType` | `it.id`/`it.title`/(derivar) | `itemId`/`title`/`itemType` | identidade estável |
| `epistemicType` | `it.ct` **(hifenizado)** → **normalizar** | `epistemicType` (canônico) | **ver tabela de normalização abaixo** |
| `confidenceLevel` | `it.conf` (`alta`/`média`/`baixa`) | `confidenceLevel` (vocab **CONFIRMAR** §6 nº 3) | pips = `confPips` |
| `evidenceLevel` | (ausente no frame) | `evidenceLevel` (**CONFIRMAR** §6 nº 4) | opcional na exibição |
| `selo`/`isFact`/`reviewStatus` | derivar de `it.prov`/`it.rev` | `selo`/`isFact`/`reviewStatus` | público = `público`/TRUE/`approved` |
| `uncertaintyRange` | `it.u` `[min,max]` | `[canonicalStart,canonicalEnd]` do item | sempre faixa |
| `uncertaintyDisplayPolicy` | derivar de `it.ct`/`it.rev` | já no envelope (por porta) | nunca `omitir` |
| `geometryRegime` | `it.global?semLugarTerrestre:(it.recon?paleoPositions:modernGeometry)` | `geometryRegime` | regra da descoberta §2 |
| `reconstructionFlag` | `it.recon || it.caveat` | `reconstructionFlag` | tempo profundo → true |
| `displayPoint` | `{it.lat,it.lng}` ou null | **CONFIRMAR** (§6 nº 1) | sem ponto → órbita por hash |
| `attributionRef` | `{it.src, —, it.tier}` | `attributionRef` (label/provenanceRef/tier) | [N1] |
| `claimSetRef` | `it.claimset` | id do ClaimSet (host em `items`) | público filtra por host |
| `presentationStage` | `it.stage` (já fixo) | `stageForScalar(scalar)` | apresentação |

**Tabela de normalização de vocabulário epistêmico (achado concreto — o frame e o corpus divergem):**

| Frame `it.ct` (hifenizado) | Corpus `epistemic_type` (canônico) |
|---|---|
| `fato-documentado` | `fato documentado` |
| `inferência-científica` | `inferência científica` |
| `reconstrução-modelada` | `reconstrução modelada` |
| `interpretação` | `interpretação historiográfica` |
| `proxy` / `estimativa` / `hipótese` | idem |
| *(corpus tem também)* | `medição direta`, `aproximação didática` |

> O adaptador deve **re-chavear a tabela `CT`/`ctOf` do frame para o vocabulário canônico** (ou normalizar na entrada). Manter o glifo+nome+cor por tipo (redundância não-cromática) — só a **chave** muda. **Falha de teste** se um item vindo da API cair em `ctOf` desconhecido (hoje cai silenciosamente em `hipótese` — `it.ct → CT[t] || CT['hipótese']`), o que **mente sobre o tipo**.

**Equivalência de fonte (artefato falsificável do adaptador):** a **forma** do `SceneModel`/`SceneItem` (chaves obrigatórias presentes, enums válidos) é **idêntica** independentemente de `source`; e, para os **itens públicos presentes em ambas** as fontes numa janela fixa, os campos normalizados **coincidem**. (Não se exige array == API — a virada **substitui** o array; o que se prova é que o **contrato** é o mesmo e que os itens públicos batem.)

### 5.3 O overlay §8 — `overlayFields` puro (fonte única do contrato visual)

`overlayFields(item, porta) → OverlayModel`. **Único** lugar onde o §8 nasce; os três renderizadores **desenham** o OverlayModel.

```txt
OverlayModel = {
  typeLabel: {glyph, name, color},     # do epistemicType; redundância NÃO-cromática (glifo + nome + cor)
  confidence: {pips, word},
  uncertaintyBand: {start, end, asRange:true},   # SEMPRE faixa; §8.1.4
  seals: ['seeded-demo' | 'em-revisão' | (nenhum)],  # selo persiste em todo modo
  attribution: {label, tier, provenanceRef},
  anachronismNotice: text | null,      # se reconstructionFlag/caveat (E10 §7.1; §8.2)
  claimSetBoundary: {tema, sides:[{stmt, weight}], noeq} | null,  # fronteira MANUAL + pesos assimétricos
  textualEquivalent: string            # "o quê / onde / quando / com que confiança" — existe em TODO degrau
}
```

Mapa **campo §8 → o que vira em cada degrau** (todos a partir do **mesmo** OverlayModel):

| Campo §8 (OverlayModel) | 3D (`render3D`) | 2D (`render2D`) | Estático (`renderStatic`) |
|---|---|---|---|
| `typeLabel` (glifo+nome+cor) | pino + bandeira HTML projetada | chip/pino no canvas | `typechip` na lista |
| `confidence` (pips) | mini-rótulo "conf. X" | pip/rótulo no chip | linha "confiança" |
| `uncertaintyBand` (faixa) | barra no painel de detalhe | faixa textual no rótulo | linha "faixa A a B (nunca um ponto)" |
| `seals` | ponto seeded/pending no pino | ponto seeded/pending | badge "seeded-demo"/"em revisão" |
| `attribution` | "fonte: … · tier" (detalhe) | rótulo de fonte | linha "fonte" |
| `anachronismNotice` | `notice anachro` (detalhe) | marca "reconstrução" no pino | linha "lugar … · reconstrução (anacronismo)" |
| `claimSetBoundary` | `renderClaimset` (detalhe) | "claimset: … pesos assimétricos" | linha "claimset … sem equivalência forçada" |
| `textualEquivalent` | descrição acessível do item | idem (e-MAG/WCAG/LBI) | **é o próprio cartão** |

### 5.4 Os três renderizadores como funções puras do modelo + degradação

- `render3D(sceneModel, overlay)`: shaders/geometria procedural (D-A3.6) + rótulos HTML projetados a partir do OverlayModel. **Não** reconstrói §8.
- `render2D(sceneModel, overlay)`: projeção esquemática (equirretangular), pinos/chips a partir do OverlayModel.
- `renderStatic(sceneModel, overlay)`: lista HTML/CSS — o **piso de acesso** (acessibilidade/offline/impressão); o `textualEquivalent` **é** o conteúdo.
- **Degradação (Art. 12; E11 §11.4/§11.10):** sem WebGL → `render2D` → `renderStatic`, **sem perder nenhum campo do OverlayModel**. O frame já degrada para 2D na ausência de THREE (`start()`); a refatoração mantém isso e garante que o piso epistêmico (tipo/confiança/incerteza/fonte/selos/fronteira/anacronismo/equivalente-textual) sobrevive a cada degrau.

### 5.5 A virada ao vivo — frame → endpoint público

- **Fluxo:** mover o tempo → `currentT` → estágio(s) vivo(s) (`stageWeights`) → **janela canônica** `[start,end]` (dos `scalar` dos `STAGES`) → `fetch('/momento/publico?start=…&end=…')` → envelope β → `fromEnvelope(…, stage)` → `SceneModel` → render. A função-envelope lê **só** `v_publishable_public` → o gating é **propriedade da fonte**, não `if` de cliente.
- **A divergência frame↔corpus se extingue por construção:** é **impossível** o `SceneModel`-vindo-da-API conter item que não exista no corpus (a fonte é a função-envelope). O teste `LIVE-T3` falha se aparecer item órfão (sinal de fonte ainda misturada com array).
- **Re-mapeamento dos toggles `gate.*`** (preserva a affordance, troca o significado): ambos OFF → `/momento/publico` (`atlas_public`); ON → `/momento/curatorial` (token; **só** localhost/rede interna). Assim a riqueza atual do frame (selos de `pending`/`seeded-demo`, ClaimSets não-públicos) **não se perde** — migra para a face curatorial, que é onde ela honestamente pertence; a face pública fica magra **e honesta** (1789 = 2 itens, 0 ClaimSets; K-Pg = rico).
- **As 3 sensíveis** (`direitos-limites`, `inconfidencia`, `escravidao-central`) **não** se religam ao vivo — host `pending`, seguem na fila (Trilha C). Por construção, nem a porta pública nem a curatorial-aprovada as exibem como fato.

### 5.6 Decisão de segredos/config — **DECIDIDA: Opção A (12-factor mínimo)**

A virada do **público** usa só `atlas_public` (sem segredo no cliente). O que gateia a virada **sair de localhost** (push de repo já conta como compartilhado) é como as credenciais dos papéis (`020`) e o DSN dev homônimo deixam de ser versionados.

- **Opção A — 12-factor mínimo (RECOMENDADO para o MVP).** `.env` no `.gitignore`; `.env.example` com placeholders; `docker-compose` interpolando `${ATLAS_PUBLIC_PASSWORD}` etc.; o serviço **recusa subir** sem a variável (**erra alto, não silenciosamente**). Público usa `atlas_public`; o curatorial fica em localhost/rede interna até a E14 definir auth real. **Evidência falsificável:** `git grep password=atlas` **não acha** fora de `.env.example`/docs; subir o serviço sem a var → erro explícito.
- **Opção B — Gerenciador de segredos (Vault/secret manager, com rotação/auditoria).** Pertence à **Etapa 14** (operação/DPIA): rotação, auditoria e RIPD. Overhead de infra desproporcional ao MVP enxuto agora.

> **Decisão tomada: Opção A** (12-factor mínimo). **B** fica agendada para a **E14** (rotação/auditoria/RIPD), não para o MVP.

**Recorte concreto de A (execução do passo 5):**

- **Variáveis externalizadas** (hoje hard-coded como `atlas`): `ATLAS_DB_PASSWORD` (app/migração), `ATLAS_PUBLIC_PASSWORD` (`atlas_public`), `ATLAS_CURATORIAL_PASSWORD` (`atlas_curatorial`), `ATLAS_CURATORIAL_TOKEN` (header `X-Atlas-Auth`).
- **`.env.example`** (commitado, com placeholders) lista as quatro; **`.env`** (no `.gitignore`, com valores **dev**) alimenta `bootstrap.sh`/migração/testes.
- **`docker-compose.yml`** passa a interpolar `${ATLAS_DB_PASSWORD}` etc. no lugar de `atlas`.
- **`service/atlas_api.py`** lê as variáveis do ambiente e **recusa subir** (sai com mensagem clara) se uma obrigatória estiver ausente — **não** faz fallback silencioso para `atlas`.
- **Face pública** usa só `atlas_public` (sem segredo no cliente); a **curatorial** (token) fica em **localhost/rede interna** até a E14 definir auth real.

> **Guarda PG1 (não-negociável):** A **não pode quebrar** os quatro verdes. O `down -v && bootstrap.sh` deve seguir fechando **10/10 + 10/10 + 10/10 + 5/5** — por isso `.env` (gitignored, valores dev) é a fonte de credencial do bootstrap/testes, e `.env.example` é só o template. A guarda "recusa subir sem var" vale para o **serviço**, não para travar o bootstrap de um clone fresco que copiou `.env.example` → `.env`.

> **Evidência falsificável do passo 5:** (i) `git grep password=atlas` (e os tokens) **não acha** nada fora de `.env.example`/docs; (ii) subir `service/atlas_api.py` com uma variável obrigatória **ausente** → **erro explícito** (não sobe em silêncio com default); (iii) o bootstrap fresco segue **10/10 + 10/10 + 10/10 + 5/5**.

## 6. Fontes necessárias — descoberta obrigatória antes de virar

Nenhuma fonte externa nova. Apoia-se em: Etapa 5 (`MomentQuery`/`MomentResult`), Etapa 10 (`ViewDegradationLadder`, invariante 16, `EquivalenceWarningNotice`, §7/§11), Etapa 11 §11.8–11.10, Playbook §8, Constituição Arts. 7 e 12, A4, e a API β já entregue.

**Liga nome conceitual ↔ identificador real (rodar contra o banco vivo / `011-momento-envelope.sql` antes de codar):**

1. **O envelope `core.t_momento` `items[]` expõe um ponto de exibição (lon/lat) para itens georreferenciados, ou só `geometryRegime`?** O frame precisa do ponto (`item3DPos`/`draw2D`). **Se só o regime:** contingência = **extensão aditiva mínima** em `011` projetando o centróide PostGIS (`ST_Y/ST_X`) para itens com `geometry_version` (não reescreve o miolo; é adição derivada do autoritativo). *Artefato:* o item georreferenciado (ex.: `chicxulub`) cai no ponto certo no 2D ao vivo.
2. **Os cósmicos de representação (`rep:bigbang`/`rep:galaxies`/`rep:sun`) existem no corpus (entre os 35), com que id/`epistemic_type`/`selo`?** **Se NÃO:** o estágio cósmico fica **vazio** na porta pública. Contingência: ou **modelar os 3 como corpus** (tarefa de modelagem registrada, **com fonte** — nunca promover seeded), ou aceitar o cósmico vazio no público e manter os teasers **só** na face curatorial/estática, rotulados como representação. *Artefato:* a consulta da janela cósmica retorna (ou não) os itens — e o frame reflete a verdade.
3. **Vocabulário de `confidence`** retornado por `f_item_epistemics` (`alta/média/baixa`? `high/medium/low`? numérico?) — o adaptador precisa do mapa exato para os pips. *Artefato:* pips corretos para um item conhecido.
4. **`evidence_level`** (mora em `core.claim.evidence_level`) — o envelope o expõe por item, ou só `confidence`? Se não, recuperar por join no envelope **ou** exibir só confiança. (A `nota-descoberta` confirma que `f_item_epistemics` **não** devolve evidence.)
5. **`displayTime`/`epistemicType` do envelope usam o vocabulário canônico** (espaço) — confirmar para alinhar a tabela de normalização (§5.2).

> Regra (igual à da API): **se a carga real divergir, o contrato se ajusta e o teste correspondente deve falhar até o ajuste.** Registrar uma **nota de descoberta curta** antes de codar.

## 7. Riscos

- **R-V1 — §8 reconstruído por renderizador diverge na degradação.** *Mitig.:* `overlayFields` único + `3D-T1` (igualdade do OverlayModel entre modos).
- **R-V2 — Item da API cai em `ctOf` desconhecido** (vira `hipótese` em silêncio → mente sobre o tipo). *Mitig.:* normalização de vocabulário (§5.2) + teste que falha em tipo desconhecido.
- **R-V3 — Frame georreferenciado sem coordenada na API** → tudo degrada para órbita por hash. *Mitig.:* descoberta §6 nº 1 + extensão aditiva de centróide se preciso; `LIVE`/2D testa o ponto.
- **R-V4 — Estágio cósmico vazio ao vivo** (rep:* só-frame). *Mitig.:* descoberta §6 nº 2; decisão explícita (modelar com fonte × manter na face curatorial); **não** promover seeded.
- **R-V5 — Vista pública magra lida como "bug"** (1789 = 2 itens, 0 ClaimSets). *Mitig.:* é **correto** (gating por host); o re-mapeamento dos toggles (§5.5) preserva a riqueza na face curatorial; a UI rotula "nada conhecido … e isso é informação".
- **R-V6 — Segredo curatorial vaza para o cliente público.** *Mitig.:* público usa só `atlas_public`; curatorial só localhost com token; `LIVE-T4` + `git grep` limpo.
- **R-V7 — Fotorrealismo anacrônico no tempo profundo.** *Mitig.:* procedural/esquemático rotulado por padrão (D-A3.6; §8.2; Art. 7).
- **R-V8 — Refatoração mexe no que não foi pedido** (shaders, física do globo). *Mitig.:* mudança **mínima e cirúrgica** — só a **origem dos dados** (SceneModel) e a **origem do §8** (overlay); shaders/câmera intactos.

## 8. Entregáveis (no repo, após execução)

- `frame/atlas-3d-frame-v1.html` refatorado: `SceneModel` + `overlayFields` puro + 3 renderizadores como funções do modelo; adaptador de duas bocas (`fromStaticArray`/`fromEnvelope`); toggles `gate.*` re-mapeados para papel/endpoint; comutador de fonte (array↔API); assets procedurais dos 3 regimes consolidados e rotulados.
- Testes do frente-end: `3D-T1..5` (degradação cruzada) + `LIVE-T1..4` (virada) — harness **headless/framework-free** sobre as funções puras (node), com extração de texto para os renderizadores; relatório no padrão verde.
- (Contingente, §6 nº 1) extensão aditiva mínima de coordenada em `011` + teste do ponto.
- (Contingente, §6 nº 2) tarefa de modelagem registrada para os cósmicos, **com fonte**, **ou** decisão de mantê-los na face curatorial.
- Config/segredos conforme a opção escolhida (§5.6): `.env.example`, `.gitignore`, interpolação no `docker-compose`, serviço que recusa subir sem var.
- `CLAUDE.md` atualizado (frame deixa de ser "espelho estático"; passa a "ao vivo contra a API pública via `SceneModel`").
- Este handoff + a nota de descoberta em `docs/passos/`.

## 9. Próximos passos (ordem de execução no Claude Code)

0. **Bootstrap fresh + verde, sem exceção (PG1):** `docker compose down -v && bash scripts/bootstrap.sh` → `verify` 10/10 + `test_a4` 10/10 + `test_a3` 10/10 + `test_a3_http` 5/5. Sem isso, não avança.
1. **Descoberta (§6):** rodar as consultas; fixar coordenada/cósmicos/vocab de confiança; **nota de descoberta curta**.
2. **D-A3.7 — modelo único + overlay:** extrair `fromStaticArray` + `overlayFields` (puros, framework-free); reescrever os 3 renderizadores para **desenhar** o OverlayModel (sem reconstruir §8). **Fonte = array (ainda).** Rodar `3D-T1..5` → verdes. *(Mudança cirúrgica: shaders/câmera/física intactos.)*
3. **D-A3.6 — assets procedurais:** consolidar e **rotular** cosmos/Terra-profunda/globo-1789 (esquemático no tempo profundo). Re-rodar `3D-T1..5` + confirmar **sem-WebGL** cai a 2D→estático sem perda.
4. **Virada ao vivo:** implementar `fromEnvelope` + comutador de fonte (`currentT → janela canônica → /momento/publico → envelope → fromEnvelope`); re-mapear os toggles `gate.*` para papel/endpoint. Rodar `LIVE-T1..4` → verdes. *(A API já está verde; troca-se uma fonte só.)*
5. **Config/segredos:** aplicar a opção **escolhida** (A ou B, §5.6). *Artefato:* `git grep` limpo; serviço recusa subir sem var.
6. **`CLAUDE.md`** atualizado.
7. **Handoff curto** em `docs/passos/`.
8. **Commits por mudança lógica:** (a) refactor SceneModel+overlay, (b) `3D-T*`, (c) assets procedurais, (d) `fromEnvelope`+virada+`LIVE-T*`, (e) config/segredos, (f) `CLAUDE.md`+handoff. **Nunca** commit-monstro.

### Especificação dos testes falsificáveis

**`3D-T*` — degradação cruzada (sobre as funções puras + extração de texto dos renderizadores):**

| # | Assere | Falha se |
|---|---|---|
| 3D-T1 | para um momento fixo (ex.: K-Pg), `overlayFields(it)` é **profundamente igual** independentemente de `mode∈{3d,2d,static}` | algum renderizador deriva §8 por conta própria |
| 3D-T2 | `textualEquivalent` de cada item é **não-vazio** em 3D, 2D e estático (`textualEquivalentAlways`) | algum degrau não tem equivalente textual |
| 3D-T3 | a fronteira do ClaimSet (tema+lados+pesos+noeq) é **idêntica** nos 3 degraus; pesos assimétricos preservados; nenhum lado negacionista | um degrau achata pesos / omite a fronteira / dá palco a negacionismo |
| 3D-T4 | todo item de tempo profundo carrega `reconstructionFlag` + `AnachronismNotice` nos 3 degraus; nenhum como foto/fato | falta o aviso em algum degrau (ex.: paleomapa como foto) |
| 3D-T5 | forçando WebGL indisponível, cai a 2D→estático **sem perder** nenhum campo do OverlayModel | a ausência de WebGL remove rótulo/fonte/incerteza ou quebra |

**`LIVE-T*` — virada ao vivo (frame contra `/momento/publico`):**

| # | Assere | Falha se |
|---|---|---|
| LIVE-T1 | janela K-Pg traz só itens públicos (`isFact=true`, `selo='público'`) + ClaimSet `kpg-causa`; nada `pending`/`seeded`/`legal-review` | vaza não-fato (regressão do gating por construção) |
| LIVE-T2 | janela 1789 traz só `iluminismo` + `posse-washington` e **zero** ClaimSets (prova negativa do gating por host: `rev-francesa` não vaza) | `rev-francesa` aparece publicamente |
| LIVE-T3 | nenhum item do `SceneModel`-da-API é órfão do corpus (impossível por construção) | aparece item órfão (fonte ainda misturada com array) |
| LIVE-T4 | o frame público sobe e funciona com só `atlas_public`, **sem** segredo curatorial no cliente | o frame embute credencial / exige curatorial para a face pública |

---

## Rodapé — o que este passo NÃO faz

- **NÃO reabre** B1/B2 nem D-A3.6/7/8; **NÃO reescreve** `db/ddl/`/`db/read-layer/010`/`011` provados — a virada é do **frame**; o banco só recebe, *se a descoberta exigir*, **uma extensão aditiva mínima de coordenada** (§6 nº 1).
- **NÃO promove** `seeded-demo` a corpus nem a fato; os cósmicos só viram corpus **com fonte** (tarefa de modelagem), nunca por promoção.
- **NÃO religa** as 3 sensíveis (`direitos-limites`/`inconfidencia`/`escravidao-central`) — host `pending`, seguem na fila (Trilha C).
- **NÃO embute** segredo curatorial no cliente; a face curatorial fica em localhost/rede interna até a E14 definir auth.
- **NÃO desliga** o §8 em nenhum degrau de degradação (§8.3; Art. 12) — o contrato visual sobrevive idêntico de 3D a estático/offline/projetor.
- **NÃO cria** camadas de usuário/escola — fora do MVP enxuto.

---

## Prompt para a próxima sessão (EXECUÇÃO no Claude Code)

> Atlas do Tempo 3D — EXECUÇÃO da virada ao vivo + 3D real (D-A3.6..8 + a virada). Plano fechado em
> `docs/passos/passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md`. Esta sessão **escreve código** (no frame; o banco só recebe extensão aditiva de coordenada *se a descoberta exigir*).
>
> Comece pelo verde, sem exceção (PG1):
>   `docker compose down -v && bash scripts/bootstrap.sh` → confirme 10/10 + 10/10 + 10/10 + 5/5.
>
> Decisão de segredos já tomada pelo humano: **Opção A — 12-factor mínimo** (`.env` gitignored + `.env.example` + interpolação no `docker-compose` + serviço que recusa subir sem var; B fica para a E14) — aplicar no passo 5, sem quebrar os quatro verdes (guarda PG1, §5.6).
>
> Depois, **um passo por vez**, na ordem do §9:
>   1. Descoberta (§6): coordenada no envelope? cósmicos no corpus? vocab de `confidence`? Nota curta.
>   2. D-A3.7: `fromStaticArray` + `overlayFields` puros; 3 renderizadores **desenham** o OverlayModel (não reconstroem §8). Fonte = array. `3D-T1..5` verdes.
>   3. D-A3.6: assets procedurais dos 3 regimes, esquemáticos rotulados no tempo profundo. Re-rodar `3D-T*` + sem-WebGL.
>   4. Virada: `fromEnvelope` + comutador de fonte + toggles `gate.*` → papel/endpoint. `LIVE-T1..4` verdes.
>   5. Config/segredos (opção escolhida). `git grep` limpo; serviço recusa subir sem var.
>   6. `CLAUDE.md` atualizado (frame ao vivo, não mais espelho estático). 7. Handoff curto.
>
> Disciplina: PRONTO = EVIDÊNCIA em cada degrau; commits por mudança lógica; mudança **cirúrgica** (shaders/câmera intactos); NÃO promova seeded a corpus; NÃO religue as 3 sensíveis; NÃO embuta segredo curatorial no cliente; NÃO desligue o §8 em nenhum degrau.
> Os artefatos que provam a virada: `3D-T1` (overlay §8 idêntico entre modos), `LIVE-T1`+`LIVE-T2` (público nunca vaza não-fato; gating por host), `LIVE-T4` (sem segredo no cliente).
