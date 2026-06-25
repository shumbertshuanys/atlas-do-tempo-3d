# Passo A3 — Plano de execução da API só-leitura (D-A3.3/4/5) · Handoff de planejamento

**Versão:** v1.0
**Data:** jun/2026
**Antecede:** execução no Claude Code (esta sessão é de PLANEJAMENTO — não escreve código)
**Sucede:** A4 (fundação reificada + camada de leitura gateada, 10/10 + 10/10) e a fatia de pendências A3 (D-A3.1 + D-A3.2, concluída e verde — `registro-execucao-a3-pendencias.md`)
**Natureza:** handoff no formato de 9 pontos do Playbook §2. **Não reabre** as decisões da API (já tomadas em `passo-a3-plano-producao-3d-ligacao-ao-vivo-v1_0.md`); **detalha-as para execução** sob a disciplina "pronto = evidência" (PG1).

> **Decisão de forma ratificada nesta sessão:** o envelope é devolvido na **forma β** — uma linha com escalares tipados (`publicabilityStatus`, `gatingReason`, `gatingType`) + arrays JSONB (`items`, `claimSets`, `uncertaintyProfiles`, `anachronismWarnings`, `equivalenceWarnings`, `normalizedTimeRange`, `normalizedSpatialScope`, `hiddenSummary`). Escolhida por testabilidade dos três artefatos falsificáveis e por colar em "devolver o `MomentResult` completo".

---

## 1. Objetivo

Detalhar, para execução no Claude Code, a **API mínima só-leitura** que expõe a função "O que acontecia no mundo?" como envelope `MomentResult` completo: (a) as **funções-envelope** `core.f_momento_publico`/`_curatorial` **ao lado** das funções A4 provadas (adição, não reescrita); (b) o **serviço fino** só-leitura com dois endpoints; (c) o **portão por grant** com dois papéis de banco. Cada campo do envelope deriva do autoritativo; cada garantia vem com um teste que poderia ter falhado.

## 2. Escopo

**Fará (no Claude Code):**
- Criar `core.f_momento_publico`/`_curatorial` devolvendo o envelope `MomentResult` (forma β), reaproveitando `f_item_attribution`/`f_item_epistemics` do A4.
- Escrever os testes SQL A3-T1..T10 e os testes HTTP A3-HTTP-1..5.
- Subir um serviço fino só-leitura (2 endpoints, público/curatorial) atrás de dois papéis de banco (portão por *grant*, não `if` de runtime).

**Não fará:** ver o Rodapé. Em particular, **não** vira o frame ao vivo, **não** faz o 3D (D-A3.6..8) e **não** religa as 3 sensíveis (host `pending`).

## 3. Diagnóstico

- **"Ligar ao vivo" ≠ "trocar o array pela API".** A função A4 devolve um `t_simultaneidade_row` magro (`id, title, item_type, epistemic_type, selo, is_fact`); o §8 (Playbook) e o contrato `WhatWasHappeningAtMoment` (Etapa 5/Etapa 11 §6) exigem o envelope completo. O envelope tem de **nascer no banco**, derivado do autoritativo, não montado na camada HTTP (Etapa 11 §6.3 **[NORMATIVO]**: leitura factual nunca devolve "texto pelado").
- **A porta pública é gateada por construção.** `f_momento_publico` lê **só** de `v_publishable_public`; `is_fact = TRUE` e `selo = 'público'` são propriedade estrutural, como já provam A4-T1..T7 para `f_simultaneidade_publica`. O gating não é um `if`; é a fonte da função.
- **O conhecimento sincronizado dá os campos conceituais, não os identificadores SQL.** Antes de codar, é obrigatória uma **descoberta** (§6) que liga nome conceitual ↔ coluna/função reais — mesmo padrão de "descoberta vira planejamento" usado na fatia de clima do A3.

## 4. Decisões principais (já tomadas; aqui detalhadas)

| ID | Decisão | Detalhe de execução |
|---|---|---|
| **D-A3.3** | Envelope no banco | `db/read-layer/011-momento-envelope.sql` (**adição**): TYPE composto (forma β) + `f_momento_publico`/`_curatorial`; cada campo derivado do autoritativo; reusa `f_item_attribution`/`f_item_epistemics`. `010` permanece intacto. |
| **D-A3.4** | Fronteira HTTP | Serviço fino, só-leitura, 2 endpoints (público/curatorial) que chamam as funções e serializam o envelope. **Sem** caminho de escrita; serviço **sem** credencial de escrita no banco. |
| **D-A3.5** | Portão por grant | `db/roles/020-papeis-leitura.sql`: `atlas_public` com `EXECUTE` **só** na função pública; `atlas_curatorial` atrás de autenticação. Portão é *grant*, não `if`. |
| **Forma β** | Retorno das funções | Ratificada nesta sessão (ver nota de cabeçalho). Alternativa α (`SETOF` por item + função companheira) **rejeitada** por exigir duas superfícies de gating e recomposição na borda. |

## 5. Modelo conceitual — o contrato do envelope

### 5.1 Princípio

Formato **único** pública × curatorial (D-A3.8): mesmos campos, mesma forma. Difere só (a) a **fonte** (`v_publishable_public` × `v_displayable_curatorial`) e (b) os **valores admissíveis** por porta. Isso é o que permite o `SceneModel` do frame ter um adaptador só e a virada ao vivo trocar **uma fonte**.

### 5.2 Contrato por item (campos §8 que TODO item carrega)

| Campo (por item) | Deriva de (autoritativo) | Invariante | Estatuto |
|---|---|---|---|
| `itemId`, `title`, `itemType` | `knowledge_item` / `entity_node` | identidade estável (ref, nunca duplica) | já em A4 |
| `epistemicType` (9 valores) | `f_item_epistemics` | "diferencie sempre o tipo epistêmico" | já em A4 |
| `confidenceLevel`, `evidenceLevel` | claim governante | rótulo de confiança presente (E11 §6.3) | **CONFIRMAR** |
| `selo` (pública: `público`; curatorial: `fato`/`demonstração`/`em-revisão`) | a função (porta) | selo persiste em todos os modos; `seeded-demo` nunca é fato | já em A4 |
| `isFact` | a view (pública: sempre `TRUE`) | não-fato nunca exibido como fato | já em A4 |
| `reviewStatus` | `knowledge_item.review_status` | invariante de exibição precede ranqueamento | derivável (pública = sempre `approved`) |
| `attributionRef` (fonte A/B + `provenance_ref`) | `f_item_attribution` | **[N1]** proveniência obrigatória (NOT NULL + CHECK) | derivável |
| `geometryRegime` (`modernGeometry`/`historicalGeometryVersions`/`paleoPositions`/`modernCorrespondence`/`semLugarTerrestre`) | `geometry_version`/State/regime | geometria por regime **rotulada**; nunca inventada | **CONFIRMAR** |
| `reconstructionFlag` | regime (tempo profundo → `TRUE`) | paleogeografia/atmosfera antiga = **sempre reconstrução** (CHECK no banco) | derivável |
| `uncertaintyDisplayPolicy` ∈ {`sempreRotular`,`rótuloCompacto`,`aparatoCompleto`} | `epistemicType`+`reviewStatus`+`ageLevelMode` | incerteza **nunca** `omitir` (Playbook §8.1.4) | política por porta (§5.4) |

### 5.3 Contrato de nível de resultado (agregados do `MomentResult`)

| Campo (resultado) | Conteúdo | Deriva de | Invariante / nota |
|---|---|---|---|
| `query` | eco da `MomentQuery` normalizada (+ inferências) | entrada | bruto preservado |
| `normalizedTimeRange` | `[canonicalStart, canonicalEnd]` + `displayTime` por regime + `sourceTimeBasis` | 3Z | nunca apaga datum nativo |
| `normalizedSpatialScope` | escopo + **geometria em uso, rotulada** | E5 §6 | rótulo de geometria sempre visível |
| `items[]` | array do contrato por item (§5.2) | funções-envelope | todos carregam §8 |
| `states[]` | States de fundo (subconjunto de `items` com `itemType = State`) | `knowledge_item` | em tempo profundo, States **dominam** |
| `claimSets[]` | controvérsias com **pesos assimétricos** (`evidence/scholarly/display`) + **fronteira escrita à mão** + `rotulado-rejeitado` **fora** do par | `claim_set`/`claim_set_member` | anti-falsa-equivalência; fronteira nunca automatizada (§5.4 Playbook); **gating por host** (§5.5) |
| `uncertaintyProfiles[]` | faixas/margens (não "lados") | `UncertaintyProfile` dos itens | incerteza = faixa · **CONFIRMAR** |
| `anachronismWarnings[]` | avisos de anacronismo do recorte | E5 §9 | `AnachronismNotice` presente sempre que o gatilho dispara |
| `equivalenceWarnings[]` | avisos anti-falsa-equivalência | E5 §9 | negacionismo = `rotulado-rejeitado`, nunca "lado" |
| `publicabilityStatus` (1–5) | agregação do gating dos itens **mostrados** | E5 §8 | pública mostra `1` para o conjunto exibido |
| `gatingReason` (+ `gatingType`: editorial · científico · licença · revisão-humana · geometria · mídia · fonte · legal) | riscos agregados | E5 §8 | explica o nível |
| `hiddenSummary` | **pública:** só contagem (se `includeHiddenSummary`); **curatorial:** lista | itens não exibíveis | `hiddenItems` **nunca** como fato |
| `navigationSuggestions` | vizinhos por tipo de relação | `RelationshipGraph` | derivável; pode ficar raso no A3 |
| `generatedSceneCandidate` | **vazio no A3** (ref opcional) | E5 §10 | função **não** cria cena automaticamente |

### 5.4 Pública × curatorial sobre o mesmo contrato

- **`f_momento_publico`** (lê `v_publishable_public`) — por construção: todo `isFact = TRUE`, `selo = 'público'`, `reviewStatus = 'approved'`; `gatingReason` de item nulo; `publicabilityStatus` do exibido = `1`; `hiddenSummary` no máximo contagem; default `uncertaintyDisplayPolicy = rótuloCompacto` (estudante: compacto, mas presente).
- **`f_momento_curatorial`** (lê `v_displayable_curatorial`; approved + pending; exclui `legal-review`/`rejected`/`blocked`) — `isFact` `TRUE`/`FALSE`; `selo ∈ {fato, demonstração, em-revisão}`; `seeded-demo` **nunca** `isFact = TRUE`; `hiddenSummary` pode listar; default `uncertaintyDisplayPolicy = aparatoCompleto`.

### 5.5 Gating de `ClaimSet` por host

"Público nunca vaza não-fato" aplicado a controvérsias: **um `ClaimSet` cujo item-host não está em `v_publishable_public` não aparece pela porta pública**, mesmo existindo no corpus. Hoje só `rev-francesa` tem host `approved`; as 3 sensíveis estão na fila; `goe-ritmo`/`kpg-causa` dependem de seus hosts (a confirmar na descoberta). O contrato deriva `claimSets[]` **filtrando pelo host na própria view da porta** — não por lista paralela.

## 6. Fontes necessárias

Nenhuma fonte externa nova. Apoia-se em: Etapa 5 (`MomentQuery`/`MomentResult`, §8 gating, §9 anacronismo/equivalência), Etapa 11 §6 (catálogo de contratos; §6.3 **[NORMATIVO]**), Playbook §8 (contrato visual de marca), A4 (`f_simultaneidade_*`, `f_item_attribution`/`f_item_epistemics`, views gateadas), Constituição Arts. 7 e 12.

**Descoberta obrigatória antes de codar (liga nome conceitual ↔ identificador SQL):** ler `db/read-layer/010-leitura-simultaneidade.sql` + DDL e confirmar — (1) assinatura/colunas reais de `t_simultaneidade_row` e das funções A4; (2) o que `f_item_attribution`/`f_item_epistemics` realmente devolvem (`confidence`/`evidence` separados? `provenance_ref`?); (3) quais `ClaimSet` têm host em `v_publishable_public`; (4) como recuperar `geometryRegime` por item. Os campos **CONFIRMAR** acima dependem disso; se a carga real divergir, o contrato se ajusta e o teste correspondente **deve falhar** até o ajuste.

## 7. Riscos

- **R-A3.3 — A função-envelope vaza lógica de gating errada.** *Mitig.:* A3-T2/T3/T7/T8 espelhando `test_a4`; cada campo derivado do autoritativo; `hiddenItems` nunca como fato.
- **R-A3.7 — Papel público recebe `EXECUTE` na curatorial por descuido de config.** *Mitig.:* A3-HTTP-1 (teste de *grant* negativo) fica vermelho se alguém afrouxar.
- **R-A3.9 (novo) — Envelope nasce com nome de coluna errado** por divergência entre conhecimento sincronizado e SQL real. *Mitig.:* descoberta obrigatória (§6) **antes** de escrever `011`; campos `CONFIRMAR` isolados.
- **R-A3.10 (novo) — ClaimSet de host pending vaza publicamente.** *Mitig.:* A3-T8 (gating por host na porta pública).

## 8. Entregáveis (no repo, após execução)

- `db/read-layer/011-momento-envelope.sql` (funções-envelope, **adição**).
- `db/migration/test_a3.py` (A3-T1..T10) + `db/reports/test_a3_report.json`.
- Serviço fino só-leitura (2 endpoints) + `db/roles/020-papeis-leitura.sql` (2 papéis) + teste HTTP (A3-HTTP-1..5) + relatório.
- `CLAUDE.md` atualizado (a API existe, gateada e provada; virada ao vivo + 3D = próxima frente).
- Este handoff em `docs/passos/`.

## 9. Próximos passos (ordem de execução no Claude Code)

0. **Bootstrap fresh + verde:** `docker compose down -v && bash scripts/bootstrap.sh` → `verify` 10/10 + `test_a4` 10/10. Sem isso, não avança (PG1).
1. **Descoberta (§6):** ler `010` + DDL; fixar nomes reais; mapear `geometryRegime`; listar ClaimSets com host em `v_publishable_public`. Nota curta de descoberta.
2. **D-A3.3:** `011-momento-envelope.sql` (adição) — TYPE β + `f_momento_publico`/`_curatorial`, cada campo do autoritativo, reusando helpers A4. **Não** tocar `010`.
3. **`test_a3.py`** (espelha `test_a4.py`): A3-T1..T10 → 10/10. Relatório `db/reports/test_a3_report.json`.
4. **Re-bootstrap fresh** → `verify` 10/10 + `test_a4` 10/10 + `test_a3` 10/10.
5. **D-A3.4/D-A3.5:** serviço fino (2 endpoints) + `020-papeis-leitura.sql` (2 papéis). Testes A3-HTTP-1..5 verdes + relatório.
6. **`CLAUDE.md`** atualizado.
7. **Handoff** em `docs/passos/`.
8. **Commits por mudança lógica:** (a) envelope SQL, (b) `test_a3`, (c) serviço+papéis+HTTP, (d) `CLAUDE.md`+handoff.

### Especificação dos testes falsificáveis

**Camada SQL — `test_a3.py` (formato de relatório igual ao `verify`/`test_a4`):**

| # | Tipo | Assere | Falha se | Porta |
|---|---|---|---|---|
| A3-T1 | estrutural | função devolve 1 linha: escalares tipados + arrays JSONB esperados | falta chave/coluna ou retorna `SETOF` | ambas |
| A3-T2 | positivo (i) | janela que cruza itens gated → todo item com `isFact=true`, `selo='público'`; nada `pending`/`legal-review`/`rejected`/`seeded` | fonte trocada p/ view curatorial → não-fato vaza | pública |
| A3-T3 | positivo (iii) | cada item tem todas as chaves §8 não-nulas | item vem "pelado" | ambas |
| A3-T4 | positivo | `uncertaintyDisplayPolicy` em enum válido; nunca `omitir` | item com `omitir`/fora do enum | ambas |
| A3-T5 | positivo [N1] | todo item tem `attributionRef.provenance_ref` | item afirmativo sem proveniência | ambas |
| A3-T6 | positivo | janela tempo profundo → item paleo com `reconstructionFlag=true` e `epistemicType ∉ {fato documentado, medição direta}` | paleomapa como fato | curatorial |
| A3-T7 | positivo | `seeded` nunca `isFact=true`; `pending`→`em-revisão`/`isFact=false`; corpus+approved→`fato`/`isFact=true` | seeded como fato | curatorial |
| A3-T8 | positivo | na pública, todo `claimSet` tem host em `items[]`/`v_publishable_public` (1789→`rev-francesa`) | ClaimSet de host `pending` vaza | pública |
| A3-T9 | positivo | `claimSet` com pesos `evidence/scholarly/display` + fronteira; `rotulado-rejeitado` fora do par | pesos simétricos/achatados ou negacionismo como lado | ambas |
| A3-T10 | estrutural | `items`(pública) ⊆ `items`(curatorial); lente sem match → array vazio, sem erro | pública traz item ausente na curatorial, ou vazio vira exceção | ambas |

**Camada HTTP — serviço fino:**

| # | Tipo | Assere | Falha se |
|---|---|---|---|
| A3-HTTP-1 | negativo (deve falhar) | `atlas_public` chamando `f_momento_curatorial` → permission denied | a chamada suceder (alguém deu `EXECUTE`) |
| A3-HTTP-2 | positivo | `atlas_public` chama `f_momento_publico` → sucesso + envelope | grant apertado demais quebra o legítimo |
| A3-HTTP-3 | positivo | GET público → JSON com agregados tipados + `items[]` §8; nenhum `isFact=false` | serialização perde campo ou vaza não-fato |
| A3-HTTP-4 | negativo | nenhuma rota de escrita; método de escrita → 405/404; serviço sem credencial de escrita | existe caminho de escrita |
| A3-HTTP-5 | positivo | curatorial sem credencial → 401/403; com credencial → envelope curatorial | curatorial abre sem auth |

---

## Rodapé — o que este passo NÃO faz

- **NÃO reabre** B1/B2 nem reescreve `db/ddl/`/`db/read-layer/010` provados — só **adiciona** (`011`, `020`, `test_a3`, serviço).
- **NÃO vira** o frame ao vivo (próxima frente) **nem** faz o 3D (D-A3.6..8).
- **NÃO promove** `seeded-demo` a corpus nem a fato.
- **NÃO publica** as 3 sensíveis (`direitos-limites`, `inconfidencia`, `escravidao-central`) — host `pending`, seguem na fila (Trilha C).
- **NÃO cria** caminho de escrita na API; **NÃO** dá ao serviço credencial de escrita no banco.
- **NÃO desliga** a honestidade epistêmica (§8.3) — o envelope carrega os campos §8 por construção, em ambas as portas.

---

## Prompt para o próximo passo (sessão de EXECUÇÃO no Claude Code)

> Atlas do Tempo 3D — EXECUÇÃO da API só-leitura (D-A3.3/4/5), forma β. Plano fechado em
> `docs/passos/passo-a3-plano-execucao-api-so-leitura-v1_0.md`. Esta sessão **escreve código**.
>
> Comece pelo verde, sem exceção (PG1):
>   `docker compose down -v && bash scripts/bootstrap.sh` → confirme `verify` 10/10 + `test_a4` 10/10.
>
> Depois, **um passo por vez**, na ordem do §9 do plano:
>   1. Descoberta (§6): leia `db/read-layer/010-leitura-simultaneidade.sql` + DDL e fixe os nomes
>      reais (`t_simultaneidade_row`, `f_item_attribution`, `f_item_epistemics`, views); mapeie
>      `geometryRegime` por item; liste quais ClaimSets têm host em `v_publishable_public`. Registre
>      uma nota de descoberta curta.
>   2. D-A3.3: crie `db/read-layer/011-momento-envelope.sql` (ADIÇÃO) — TYPE composto forma β +
>      `core.f_momento_publico`/`_curatorial`, cada campo derivado do autoritativo, reusando os
>      helpers A4. NÃO toque em `010`.
>   3. `db/migration/test_a3.py` (espelha `test_a4.py`): A3-T1..T10. Rode → 10/10. Gere
>      `db/reports/test_a3_report.json`.
>   4. Re-bootstrap fresh → `verify` 10/10 + `test_a4` 10/10 + `test_a3` 10/10.
>   5. D-A3.4/D-A3.5: serviço fino só-leitura (2 endpoints, público/curatorial) +
>      `db/roles/020-papeis-leitura.sql` (`atlas_public` com EXECUTE só na pública; `atlas_curatorial`
>      autenticado). Rode A3-HTTP-1..5 verdes + relatório.
>   6. Atualize `CLAUDE.md` (a API existe, gateada e provada; virada ao vivo + 3D = próxima frente).
>   7. Handoff curto em `docs/passos/`.
>
> Disciplina: PRONTO = EVIDÊNCIA em cada degrau; commits por mudança lógica (não commit-monstro);
> NÃO vire o frame ao vivo nem inicie o 3D nesta sessão; NÃO religue as 3 sensíveis (host pending).
> Os três artefatos que provam a API: A3-T2 (público nunca não-fato), A3-HTTP-1 (grant sem EXECUTE
> na curatorial), A3-T3 (todo item com campos §8).
