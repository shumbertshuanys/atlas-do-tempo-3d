# Nota de descoberta — API só-leitura (D-A3.3/4/5)

**Data:** jun/2026 · **Antecede:** `011-momento-envelope.sql` + `test_a3.py` + serviço/papéis
**Fonte:** leitura de `db/read-layer/010-leitura-simultaneidade.sql` + `db/ddl/001-esquema-reificado.sql`
+ consultas ao banco vivo (carga 42 verde). Liga **nome conceitual ↔ identificador SQL** (§6 do plano).

## 1. Nomes reais fixados (autoritativo)

| Conceito | Identificador SQL real |
|---|---|
| Linha de simultaneidade (A4) | `core.t_simultaneidade_row` (composto: `id,title,item_type,domain,epistemic_type,confidence,display_time,source_time_basis,time_precision,time_uncertainty,canonical_start/end/scalar,is_global,anachronism_note,attribution,provenance_status,review_status,selo,is_fact`) |
| Função pública A4 | `core.f_simultaneidade_publica(p_start,p_end,p_lenses)` → `SETOF t_simultaneidade_row` (lê **só** `v_publishable_public`; `selo='público'`, `is_fact=TRUE` por construção) |
| Função curatorial A4 | `core.f_simultaneidade_curatorial(...)` (lê `knowledge_item` com `review_status IN ('approved','pending')`, `ingestion_decision<>'blocked'`; selo por proveniência) |
| Atribuição | `core.f_item_attribution(p_item TEXT)` → `TEXT` (rótulo de fonte; "demonstração — fonte não validada" para seeded) |
| Epistemologia | `core.f_item_epistemics(p_item TEXT, OUT claim_type, OUT confidence)` — **não** devolve `evidence_level` |
| Views-portão | `core.v_publishable_public` (approved ∩ corpus ∩ `per_asset_source_confirmed`) · `core.v_displayable_curatorial` (approved ∩ não-blocked) |

**`evidence_level`** mora em `core.claim.evidence_level` (presente em todos os 35 itens); recuperável por join
`claim(subject_ref=item)`. **`provenance_ref`** é `core.claim.provenance_ref` **NOT NULL** ([N1]) → `attributionRef.provenanceRef`
não-nulo para todo item. `authority_tier` vem de `source.authority_tier` via `provenance_metadata`.

## 2. `geometryRegime` por item — regra de derivação (campo CONFIRMAR)

Não há coluna de regime; deriva-se de `core.geometry_version` (`is_paleo`/`is_reconstruction`) + `knowledge_item.is_global`:

- `geometry_version` com `is_paleo=true` → **`paleoPositions`** (só `evt:impacto-chicxulub` hoje)
- `geometry_version` sem paleo → **`modernGeometry`** (evento/processo em coordenada moderna)
- sem `geometry_version` → **`semLugarTerrestre`** (escopo planetário/global; 21 itens `is_global`)

Carga: 35 itens · **14** com `geometry_version` · **1** paleo · **21** globais.

`reconstructionFlag` = `epistemic_type = 'reconstrução-modelada'` **OU** `geometry_version.is_reconstruction`.
Cobre `paleogeografia-*` (sem geometria, mas `reconstrução-modelada`) e `chicxulub` (geometria paleo).

`uncertaintyDisplayPolicy` (nunca `omitir`, Playbook §8.1.4): **pública** → `sempreRotular` para
`{reconstrução-modelada,hipótese,estimativa,proxy,inferência-científica}`, senão `rótuloCompacto`;
**curatorial** → `aparatoCompleto`.

## 3. ClaimSets com host em `v_publishable_public` — **DIVERGÊNCIA do plano**

Consulta direta `claim_set ⋈ v_publishable_public`:

| ClaimSet | Host | Host público? | Porquê |
|---|---|---|---|
| `cset:kpg-causa` | `evt:impacto-chicxulub` | **SIM** | approved · corpus · `per_asset_source_confirmed=t` |
| `cset:goe-ritmo` | `proc:goe` | não | `per_asset_source_confirmed=f` (`srcPend=True`) |
| `cset:rev-francesa` | `evt:estados-gerais-1789` | não | `per_asset_source_confirmed=f` (`srcPend=True`) |

> **O plano (§5.5/A3-T8) assumia "1789→`rev-francesa`" como o exemplo público.** A carga real **falsifica**
> isso: o host de `rev-francesa` (`estados-gerais-1789`) **não** está em `v_publishable_public` porque tem
> fonte-por-asset pendente. Na janela 1789 a porta pública mostra só `concept:iluminismo` +
> `evt:posse-washington-1789` (2 itens; casa com A4-T1) e **zero** ClaimSets — prova **boa** do gating por host
> (§5.5): mesmo existindo no corpus e sendo simultâneo, o ClaimSet não vaza.
>
> **Ajuste (regra §6: "se a carga real divergir, o contrato se ajusta"):** a **invariante** testada por A3-T8
> permanece — *todo ClaimSet exibido na porta pública tem host em `items[]`/`v_publishable_public`* — mas o
> **exemplo positivo** passa a ser **`kpg-causa` na janela K-Pg** (host `chicxulub` é público e simultâneo;
> 6 itens públicos no K-Pg, incluindo o host). O caso 1789 vira **prova negativa** (claimSet não público não vaza).

## 4. Membros de ClaimSet — pesos (campo CONFIRMAR)

`claim_set_member` tem **um** `weight` (NUMERIC) + `stance` (TEXT) por membro; **não** a tripla
`evidence/scholarly/display` do contrato conceitual. `claim_set.resolution` é a **fronteira escrita à mão**
(§5.4 Playbook). Nenhum membro `rotulado-rejeitado` (negacionismo) está carregado.

> **Ajuste:** A3-T9 não fabrica três pesos (seria falsa precisão, fere a honestidade epistêmica). Testa o
> provável: **pesos assimétricos** (`max(weight) ≠ min(weight)` por conjunto) + **fronteira `resolution`
> presente e não-vazia** + nenhum "lado" negacionista. Pesos por conjunto: kpg-causa `0.82/0.30`,
> goe-ritmo `0.62/0.38`, rev-francesa `0.70/0.55/0.50` — todos assimétricos.

## 5. Decisões de forma derivadas para `011`

- Envelope = **forma β**: TYPE `core.t_momento` (uma linha) com escalares tipados (`porta`,
  `publicability_status`, `gating_reason`, `gating_type`) + arrays/objetos JSONB (`items`, `states`,
  `claim_sets`, `uncertainty_profiles`, `anachronism_warnings`, `equivalence_warnings`,
  `normalized_time_range`, `normalized_spatial_scope`, `hidden_summary`, `query`,
  `navigation_suggestions`, `generated_scene_candidate`). `RETURNS core.t_momento` (não `SETOF`).
- `f_momento_publico`/`_curatorial` **reusam** `f_simultaneidade_publica`/`_curatorial` como fonte de itens
  (gating por construção herdado do A4) + enriquecem cada item com os campos §8 via join a `claim`/`source`.
- **Portão por grant:** funções `SECURITY DEFINER` (dono = `atlas`); `REVOKE EXECUTE ... FROM PUBLIC`;
  `atlas_public` recebe EXECUTE **só** na pública; `atlas_curatorial` (autenticado) nas duas. Nenhum papel
  recebe escrita. (A3-HTTP-1 fica vermelho se alguém afrouxar — R-A3.7.)
