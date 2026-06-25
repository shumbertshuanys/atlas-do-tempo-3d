# Nota de descoberta — virada ao vivo + 3D real (D-A3.6..8 + virada)

**Data:** jun/2026 · **Antecede:** refactor `SceneModel`/`overlayFields` + `fromEnvelope` + virada
**Fonte:** leitura de `db/read-layer/011-momento-envelope.sql` + `frame/atlas-3d-frame-v1.html`
+ consultas ao banco vivo (carga 42 verde, bootstrap fresh nesta sessão: 10/10+10/10+10/10+5/5).
Responde os 5 pontos de descoberta obrigatória do plano (§6). Regra: **se a carga real divergir,
o contrato se ajusta e o teste correspondente falha até o ajuste.**

## §6 nº 1 — O envelope expõe ponto lon/lat por item? **NÃO.**

`core.f_item_envelope_core` devolve **só `geometryRegime`** (`paleoPositions`/`modernGeometry`/
`semLugarTerrestre`) — **não** projeta o ponto. Verificado no item georreferenciado `evt:impacto-chicxulub`
(porta pública): traz `geometryRegime:"paleoPositions"`, `reconstructionFlag:true`, `anachronismNote`, mas
**nenhum** `lat`/`lng`. O frame precisa do ponto (`draw2D` e `item3DPos` usam `it.lat`/`it.lng`).

A geometria existe e é **projetável**: `core.geometry_version.geom` é `POINT` para os 14 itens
georreferenciados, com centróides limpos (ex.: chicxulub `21.30, -89.50`; bastilha `48.86, 2.35`).

> **Contingência (autorizada pelo plano §6 nº 1 / Rodapé):** **extensão aditiva mínima** em `011` —
> `f_item_envelope_core` passa a expor `displayPoint:{lat,lng}` projetando `ST_Y/ST_X(ST_Centroid(geom))`
> para itens com `geometry_version`, `null` senão. É **adição** derivada do autoritativo (não reescreve o
> miolo); itens sem geometria caem na **órbita por hash** (comportamento atual preservado). A aplicar no
> passo da virada, com teste do ponto (chicxulub cai no lugar certo no 2D ao vivo). Os quatro verdes
> existentes não dependem de `displayPoint` → permanecem verdes.

## §6 nº 2 — Os cósmicos `rep:bigbang`/`rep:galaxies`/`rep:sun` existem no corpus? **NÃO.**

Consulta por id/título (`bigbang|galax|sun|cosm|rep:` / `big bang|galáx|estrela|sol|cosm`) → **0 linhas**
entre os 35 itens. Os três teasers cósmicos do frame são **só-frame** (marcados `prov:'corpus'` no array,
mas **sem lastro** no corpus autoritativo) — o **achado novo** do plano (§3) **confirmado**.

> **Consequência:** o estágio cósmico fica **vazio na porta pública ao vivo** — exatamente a divergência que a
> virada deve **expor, não maquiar**. **Decisão (sem promover seeded):** manter os 3 teasers **só na face
> curatorial/estática**, rotulados como **representação de cena** (`repr:true`, já há o aviso "Representação
> de cena" no frame); a face **pública** mostra "Nada conhecido neste instante por estas lentes — e isso é
> informação" no regime cósmico. Virar os cósmicos em corpus é **tarefa de modelagem com fonte** (registrada),
> nunca promoção. *Artefato:* `LIVE` confirma cósmico público vazio; curatorial/estático preserva os teasers.

## §6 nº 3 — Vocabulário de `confidence`. **`alta` / `média` / `baixa`.**

`f_item_epistemics(...).confidence` ∈ `{alta, média, baixa}` — **idêntico** ao `it.conf` do frame.
**Nenhum mapa necessário**; `confPips` (`alta:3, média:2, baixa:1`) e `shortConf` aplicam-se direto.

## §6 nº 4 — `evidence_level` no envelope? **SIM**, como texto descritivo.

O envelope **já expõe** `evidenceLevel` (join a `core.claim`). **Mas não é um nível/enum** — é texto
descritivo da evidência (ex.: `"geoquímica (irídio)"`, `"cratera, anomalia de irídio, esférulas, camada-limite"`).
O frame **não** tem campo equivalente hoje. **Decisão:** exibição **opcional** (linha "evidência" quando
presente); o piso §8 não depende dele. Sem fabricar nível onde só há descrição.

## §6 nº 5 — `epistemicType`/`displayTime` usam vocab canônico? **SIM — e falsifica a tabela do plano §5.2.**

`f_item_epistemics(...).claim_type` (= `epistemicType`) é **hifenizado** no corpus:
`fato-documentado`, `inferência-científica`, `reconstrução-modelada`, `interpretação`, `proxy`,
`estimativa`, `hipótese` (11 pares tipo×confiança distintos na carga).

> **DIVERGÊNCIA do plano §5.2:** a tabela de normalização do plano assumia que o corpus usa **espaço**
> (`fato documentado`, `inferência científica`, `interpretação historiográfica`). **Falso.** O corpus usa as
> **mesmas chaves hifenizadas** que o `CT` do frame (`frame/...html:268-276`). **Consequência:** a normalização
> de vocabulário é **identidade** para a carga atual — **nenhum re-chaveamento** é necessário; o `CT`/`ctOf`
> do frame já casa com `epistemicType` da API.
>
> **O guarda fail-loud do plano (R-V2) permanece necessário:** o schema permite `medição direta` e
> `aproximação didática` (não presentes na carga de 35). Se a API um dia devolver um tipo fora do `CT`, o
> adaptador deve **falhar alto** — **não** cair em silêncio para `hipótese` (`CT[t] || CT['hipótese']` hoje
> **mente** sobre o tipo). O teste `3D-T`/`LIVE` falha se um tipo desconhecido for absorvido sem erro.

`displayTime` é texto livre por regime (`"~66 Ma"`, `"5 de maio de 1789"`, `"séc. XVII–XVIII"`); o frame
usa `STAGES[].disp` + `formatYear(scalar)` para o eixo — `displayTime` do item entra como rótulo do "quando".

## Resumo dos ajustes de contrato vindos da carga real

| # | Premissa do plano | Carga real | Ajuste |
|---|---|---|---|
| 1 | envelope pode ter ponto | só `geometryRegime` | **extensão aditiva `displayPoint` em `011`** (passo virada) |
| 2 | cósmicos talvez no corpus | **ausentes** | cósmico público vazio (honesto); teasers só curatorial/estático |
| 3 | confiança a confirmar | `alta/média/baixa` | identidade, sem mapa |
| 4 | evidence a confirmar | texto descritivo (não enum) | exibição opcional, sem fabricar nível |
| 5 | corpus usa espaço (§5.2) | **hifenizado, = frame** | normalização = identidade; **guarda fail-loud mantido** |

## Carga viva fixada (janelas dos testes `LIVE-*`)

| Janela canônica | Porta pública | ClaimSets públicos |
|---|---|---|
| K-Pg `[-66.05e6, -65.95e6]` | **6 itens** (anomalia-iridio, aves, dinossauros-nao-avianos, impacto-chicxulub, extincao-kpg, recuperacao-ecologica-pos-kpg) | **`cset:kpg-causa`** (host `chicxulub` público) |
| 1789 `[-210.7, -210.4]` | **2 itens** (`concept:iluminismo`, `evt:posse-washington-1789`); 14 ocultos | **zero** (`rev-francesa` não vaza — host `estados-gerais-1789` com fonte-por-asset pendente) |
| Cósmico (`< -4.6e9`) | **0 itens** (sem lastro) | — |

> Curatorial 1789 (mesma janela) = 16 itens + `cset:rev-francesa` — é onde a riqueza atual do frame
> honestamente pertence (re-mapeamento dos toggles `gate.*` → papel/endpoint, §5.5 do plano).
