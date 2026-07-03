# Frente A — Nota de descoberta (§6) + tabela de tipagem epistêmica

**Versão:** v1.0 · **Data:** jul/2026 · **Passo:** §9.1 do `plano-cosmicos-corpus-com-fonte-v1_0.md`
**Natureza:** read-only. Nenhum código de modelagem foi escrito. Saída = esta nota + a
**tabela proposta** (entrada do 🚦 portão humano F-A.4). **Não se modela antes da assinatura.**

---

## 0. Baseline verde (PG1) — evidência

Volume limpo (`docker compose down -v && bash scripts/bootstrap.sh`):
`verify 10/10 · test_a4 10/10 · test_a3 10/10 · test_a3_http 5/5`.
Carga: 35 itens · 27 corpus · 8 seeded · 42 claims (35 de item + 7 membros) · 3 ClaimSets ·
17 fontes · 11 publicáveis na porta pública. Baseline íntegro.

---

## 1. Janela do estágio cósmico (§6.1) — **OK, sem extensão de eixo**

- `STAGES` (`atlas-model.js`) já tem 3 estágios cósmicos (`kind:'cosmic'`): `bigbang` (−13,8e9),
  `galaxies` (−13,0e9), `sun` (−4,6e9) + `earth` (−4,5e9, regime geológico — a **ponte**).
- `stageForScalar` usa distância em `log10(|scalar|)` → cobre cósmico×terrestre sem privilegiar
  nenhum. Um item em −13,787e9 cai em `bigbang`; −4,567e9 cai em `sun`/`earth`.
- A coluna viva `canonical_scalar` é `DOUBLE PRECISION` e **já carrega magnitudes Ga**
  (`source_time_basis='Ga'` em **8 itens** do GOE). Nenhuma extensão de eixo, nenhum regime novo.

## 2. Enums vivos (§6.2) — **TEXT + CHECK, não enum nativo**

Não há `pg_enum`; são colunas `TEXT` (algumas com CHECK). Valores **vivos** hoje:

- **`knowledge_item.item_type`** (sem CHECK; comentário lista o vocabulário): `Event`(7), `Process`(7),
  `Concept`(2), `State`(14), `Species`(1), `Entity`(4). → **`Event` e `Process` disponíveis** para
  Big Bang/formações; `State` para o CMB/fundo, se preferir tratá-lo como estado.
- **`claim.claim_type`** (a tipagem epistêmica): vivos = `fato-documentado`(7), `inferência-científica`(11),
  `interpretação`(13), `proxy`(2), `reconstrução-modelada`(3), `estimativa`(4), `hipótese`(2).
  O comentário do DDL admite ainda `medição-direta`, `representação-artística`, `aproximação-didática`
  — **ausentes da carga** (não exercitados).
- **`claim.confidence`**: vivos `alta`/`média`/`baixa` (CHECK admite também `média-alta`/`média-baixa`).

> ⚠️ **ACHADO CRÍTICO (grafia de `medição-direta`).** O `claim_type` flui **cru** ao frame
> (`011` → `f_item_epistemics` → `epistemicType`; sem normalização). O mapa `CT` do frame
> (`atlas-model.js:25`) tem a chave **`'medição direta'` com ESPAÇO**, mas o DDL/convenção usa
> **`'medição-direta'` com HÍFEN** (como todos os outros tipos). Se um claim cósmico usar o hífen,
> o `ctOf` **não casa** e cai no **fail-loud vermelho** ("tipo desconhecido"). Consequência de decisão:
> se a tabela assinada usar `medição-direta`, é **obrigatória** uma correção mínima no frame
> (adicionar a chave hifenizada ao `CT`, mantendo o alias com espaço) — do contrário, evitar o tipo.
> Isso **não** ocorre com `inferência-científica`/`reconstrução-modelada` (já no `CT` e no conjunto
> `sempreRotular`).

## 3. Item sem geometria terrestre (§6.3) — **já é rotina; risco R3 menor que o previsto**

- `geometry_version` é tabela separada, `geom` nulável, ligada por `item_ref`. Um item **sem** linha
  em `geometry_version` é perfeitamente válido: **21 dos 35 itens já não têm geometria** (globais,
  conceitos, processos planetários).
- O envelope (`011`) já trata: `displayPoint = NULL` (sem centróide) e
  `geometryRegime = 'semLugarTerrestre'` quando não há geometria. O frame já consome NULL
  (`mapEnvelopeItem`/`buildSceneItemFromStatic`). → **Item cósmico não é o primeiro sem geometria**;
  o `displayPoint NULL` já é exercitado. Sem mudança de esquema. `COSMO-T4` vira teste do **render**
  (estágio esquemático, sem marcador no globo), não do banco.

## 4. Fontes por claim (§6.4) — **padrão aditivo mapeado**

- Não existe tabela "Citation"; a proveniência é `source` → `provenance_metadata` → `claim.provenance_ref`
  (`NOT NULL`, [N1]). `migrate.py` é **data-driven**: cada item é um `dict` em `ITENS`; `source_for()`
  faz dedup por string de fonte; `provenance_metadata` e `claim` são criados por item.
- Campos do dict que governam gating: `pub` (`'publicável'`→`approved` / `'mediado'`→`pending`);
  `srcPend` (⇒ `per_asset_source_confirmed = NOT srcPend`); `seeded` (⇒ `provenance_status`).
- **Porta pública exige** `review_status='approved'` **∩** `provenance_status='corpus'` **∩**
  `per_asset_source_confirmed=true` (= `pub='publicável'` **e** `srcPend=False` **e** não-seeded).
- **Licença de mídia:** nenhuma mídia nesta frente (estágio procedural, F-A.3). Fontes NASA/ESA (PD)
  entram como **citação textual** (`source`), nunca reprodução de asset.

## 5. ClaimSet? (§6.5) — **NÃO, por autoridade da `etapa-3.1 §10.7`**

Texto autoritativo (§10.7): Big Bang = "consenso científico com incerteza interna"; **a expansão é
claim único (alta confiança)**; a inflação seria claim `hipótese` separado; **criacionismo não é claim
concorrente**. Logo: **zero ClaimSet cósmico** nesta frente (satisfaz `COSMO-T5` por construção). A
"tensão de Hubble" que o plano levantou como candidata **não** é exigida pela `etapa-3.1` → **adiada**
(se um dia entrar, é controvérsia real e estreita, com pesos assimétricos e host público+fonteado).

## 6. Anti-seeded (§6.6) — **limpo**

- **0 itens cósmicos no DB** (busca por `bigbang|galax|cosmo|cmb|sol|sistema-solar|universo`).
- Os 8 `seeded-demo` são **todos de 1789** (`lavoisier`, `atmosfera-1789`, `co2-1789`, `terra-orbita`,
  `andes`, `alpes`, `grande-auk`, `biosfera`). Nenhum cósmico → **nada a promover**.
- Os teasers `rep:bigbang`/`rep:galaxies`/`rep:sun` existem **só no array do frame** (`ITEMS`,
  `prov:'corpus'` "de fachada", sem lastro no banco). A reconciliação (passo 4) os fará **desenhados
  do envelope** — os novos itens cósmicos são **novos, com fonte**, nunca promoção dos teasers.

---

## 7. Semântica de `is_fact` para o cósmico — leia antes de assinar

`is_fact=true` na porta pública **não** significa "exibido como *fato documentado*". Significa
"publicamente afirmável como estabelecido". O **rótulo epistêmico** (`epistemicType`) continua
comunicando a natureza (inferência científica / medição direta / reconstrução) **e a incerteza é
sempre exibida**. Assim, a "idade do universo" pode ser `is_fact=true` **com** `epistemicType =
inferência-científica` + faixa de incerteza — exatamente como "houve impacto" é fato no K-Pg enquanto
o *peso causal* é debatido. **Nenhum** claim cósmico usa `fato-documentado` (ninguém testemunhou t=0)
→ satisfaz `COSMO-T2`.

---

## 8. 🚦 TABELA DE TIPAGEM EPISTÊMICA — **ASSINADA (humano, jul/2026)**

Escopo F-A.fork = **Abordagem 2** (5 âncoras + ponte). Colunas de decisão: `claim_type`,
`confidence`, `pub` (→`review_status`), `srcPend` (→`per_asset_source_confirmed`) e a **porta
resultante**. Valores de tempo/fonte são propostas de curadoria (a confirmar na modelagem).

| # | id | item_type | Tempo (Ga) | **claim_type** | **conf.** | **pub** | **srcPend** | **Porta resultante** | Fonte |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `evt:big-bang` | Event | ~13,787 ±0,020 | `inferência-científica` | alta | publicável | False | **PÚBLICA** (is_fact, rótulo "inferência", ± exibido) | NASA/ESA — Planck 2018 (PD) |
| 2 | `state:cmb-recombinacao` | State | ~13,8 (≈+380 ka) | **`medição-direta`** | alta | publicável | False | **PÚBLICA** | NASA/ESA — Planck 2018 (PD) |
| 3 | `proc:formacao-galaxias` | Process | ~13,5–13,0 | `inferência-científica` | **média** | publicável | False | **PÚBLICA** (conf. média + faixa ampla) | NASA/ESA — JWST (PD); peer-reviewed |
| 4 | `evt:formacao-sistema-solar` | Event | ~4,567 | `inferência-científica` | alta | publicável | False | **PÚBLICA** | NASA — datação de CAIs (PD); peer-reviewed |
| 5 | `proc:formacao-terra` | Process | ~4,54 | `inferência-científica` | alta | publicável | False | **PÚBLICA** + ponte→`proc:goe` | USGS — zircões/meteoritos (PD); peer-reviewed |

**Relação de ponte:** `proc:formacao-terra` —`precede`→ `proc:goe` (−2,4 Ga), aresta afirmativa com
proveniência ([N1]), ligando o mini-corpus cósmico ao tempo profundo terrestre já existente.

### Decisões assinadas (humano, jul/2026):

- **D1 — Tipo do CMB (item 2): ✅ `medição-direta` + correção do `CT` do frame** (adicionar a chave
  hifenizada `'medição-direta'` ao `CT`, mantendo o alias com espaço). É o tipo correto e conserta a
  inconsistência latente de §2.
- **D2 — Porta das galáxias (item 3): ✅ PÚBLICA** com `confidence=média` + faixa de incerteza ampla.
- **D3 — Itens 1, 4, 5: ✅ PÚBLICA/is_fact** com `inferência-científica`+alta, incerteza exibida.
- **D4 — Sem ClaimSet cósmico: ✅** (por `etapa-3.1 §10.7`); tensão de Hubble **adiada**.
- **D5 — `fato-documentado` proibido para todo cósmico: ✅**.

> Com a assinatura, a execução segue: (b) modelar os 5 itens + fontes em `migrate.py` (adição) + fix
> do `CT`, (c) reconciliar o frame, (d) escrever `COSMO-T1..5`, (e) re-verdejar tudo e atualizar
> fixtures/inventário/CLAUDE.md — commits por mudança lógica.

### Impacto de inventário previsto (para atualizar `verify.py`/`test_a4.py`, invariantes intactas)

| métrica | antes | depois |
|---|---|---|
| itens | 35 | **40** |
| corpus | 27 | **32** |
| approved | 23 | **28** |
| claims_de_item | 35 | **40** |
| claims_total | 42 | **47** |
| relações / arestas afirmativas | 5 | **6** (ponte) |
| fontes | 17 | **21** (4 novas; itens 1–2 compartilham Planck) |
| publicável (porta pública) | 11 | **16** |
| exibível curatorial | 23 | **28** |
| seeded / pending / claimsets / membros / geometrias | 8 / 12 / 3 / 7 / 14 | **inalterados** |

As janelas de teste A3 (1789, GOE −2,4 Ga, K-Pg −66 Ma) **não** contêm as épocas cósmicas
(−13,8 Ga e −4,5 Ga), logo `test_a3` fica intacto; só mudam os totais "todo o eixo" do `test_a4`
(11→16) e o inventário do `verify.py`. `COSMO-T1` cobre a nova janela cósmica.
