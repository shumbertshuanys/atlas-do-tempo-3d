# Fila de revisão — ClaimSets sensíveis removidos do frame (D-A3.1)

> Registro rastreável (R-A3.2: "não some sem rastro") dos ClaimSets retirados do frame
> em D-A3.1 por terem **host `pending`** no corpus autoritativo. Processo: Passo C2
> (`docs/passos/passo-c2-handoff-fila-revisao-processo-v1_0.md`), Playbook §5, Trilha C.
> **Não** são publicáveis enquanto o host não for aprovado via pipeline (Constituição Art. 6).

## Contexto

D-A3.1 (split do Passo A3): ClaimSet com **host `approved`** → modelar no corpus; com
**host `pending`** → fila de revisão. Modelado no corpus apenas `rev-francesa`
(host `evt:estados-gerais-1789`, approved). Os três abaixo têm host `pending` e ficam aqui.

Correção de bug associada: o frame marcava `evt:declaracao-direitos-1789` como
`rev:'approved'`, divergindo do corpus (`mediado` → `pending`). Corrigido para `pending`
no mesmo passo — o item segue exibido, porém gated.

## Itens enfileirados (`queueState`: queued — aguardando revisão por papel competente)

| ClaimSet | Host | Host `review_status` (corpus) | Sensibilidade (PG5) | Papéis de revisão exigidos (C2 §5) |
|---|---|---|---|---|
| `direitos-limites` — "Universalidade declarada × alcance real (1789)" | `evt:declaracao-direitos-1789` | `pending` (mediado) | P14 (exclusões: mulheres, escravizados, não-proprietários) | editorial, historiográfica, vieses |
| `inconfidencia` — "Leituras da Inconfidência Mineira" | `evt:inconfidencia-mineira` | `pending` | P14 (interpretação historiográfica) | historiográfica, editorial, vieses |
| `escravidao-central` — "Centralidade da escravidão no período" | `proc:trafico-atlantico` | `pending` | P14 (escravidão — Lei 10.639/2003) | editorial, historiográfica, vieses |

Conteúdo autorado (temas, leituras/pesos, fronteira "sem equivalência") preservado no
histórico git do frame (`frame/atlas-3d-frame-v1.html`, antes de D-A3.1) — insumo para a
modelagem quando entrarem em revisão. A fronteira é **escrita à mão** (C2 §5.4 / Art. 7);
a fila roteia e rastreia, não gera a fronteira.

## Condição de saída (Definition of Done — PG1)

Cada ClaimSet só retorna ao frame/corpus quando **o host for aprovado** (todas as revisões
aplicáveis aprovadas → `reviewStatus = approved`) e o ClaimSet for modelado no corpus
(`claim_set` + `claim_set_member`, fronteira manual), espelhando o padrão de `rev-francesa`.
Até lá: não exibir como fato, não publicar (Art. 6, gating por construção do A4).

## Itens do laço de ingestão promovidos como `pending` (rodada 1 — 2026-07-09)

Pacotes Tier 0 (PG5 `mediado`) da primeira rodada do laço de ingestão assistida,
promovidos pelo dono a `pending` porque **os papéis competentes P14 não estão
designados** (D-20260708-01): sensível promove no máximo a `pending` e entra nesta
fila. O `promover` não escreve aqui — este registro é o rastro (R-A3.2).

| Pacote | Item (corpus) | Título | Sensibilidade (PG5) | Papéis de revisão exigidos |
|---|---|---|---|---|
| `pkg-t0-males` | `evt:levante-dos-males-1835` | Levante dos Malês | `mediado` — P14 (história afro-brasileira e religiões de matriz africana; Leis 10.639/2003 e 11.645/2008) | historiográfica, editorial, vieses |
| `pkg-t0-chibata` | `evt:revolta-da-chibata-1910` | Revolta da Chibata | `mediado` — P14 (história afro-brasileira; Lei 10.639/2003) | historiográfica, editorial, vieses |
| `pkg-t0-lei-aurea` | `evt:lei-aurea-1888` | Lei Áurea (abolição da escravidão) | `mediado` — P14 (escravidão e racismo estrutural; Leis 10.639/2003 e 11.645/2008) | historiográfica, editorial, vieses |

Condição de saída destes três: designação dos papéis P14 por entrada no
`DECISOES.md` + checklist §6.1 integral por todos os papéis aplicáveis (spec do
laço, T0) → só então `review_status = approved` e publicação. Até lá: existem no
corpus como `pending`, invisíveis na porta pública por construção (A4/T5).
