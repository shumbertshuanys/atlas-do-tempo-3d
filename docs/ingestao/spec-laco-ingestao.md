# Spec — Laço de ingestão assistida por IA com revisão tierizada (v0)

> Documento de trabalho da frente de ingestão (Chat 4; decisão D-20260707-02).
> Executa **D-20260703-03** (modelo C: IA/RAG só na ingestão) e instrumenta a
> prioridade (b) do `ESTADO.md`. Caminho no repo: `docs/ingestao/spec-laco-ingestao.md`
> (arquivo único versionado pelo git — R3). **Não altera** `db/ddl/` nem
> `db/read-layer/` (miolo provado): tudo aqui opera **antes** do corpus (staging
> no repo) ou **através** do caminho de carga existente. O Chat 5 implementa
> exatamente isto; divergência de implementação = nova entrada no `DECISOES.md`.

## 0. Objetivo e não-objetivos

**Objetivo:** um laço operável e mensurável — IA rascunha → validação automática
→ triagem de tier → revisão humana → promoção ao corpus — cujo produto primário
no Chat 5 é **o número que decide a economia do produto: minutos humanos por
item aprovado, por tier**.

**Não-objetivos do v0:** UI de revisão (CLI basta); qualquer mudança de esquema
no banco; `media_asset` (fica com a F-A.3 e seu portão de licença por asset);
automação de aprovação; cobertura de conteúdo (a medição usa poucos pacotes);
definição de equipe de papéis além do dono.

## 1. Definições (fixadas primeiro, por mandato da missão)

### 1.1 Pacote de ingestão — a unidade de revisão e de medição

Conjunto **indivisível** proposto pela IA, espelhando o Definition of Ready do
C2 (D-C2.7), contendo:

- **1** `knowledge_item` candidato (id, `item_type`, `domain`, `title`, eixo 3Z:
  `canonical_start/end/scalar`, `source_time_basis`, `display_time`,
  `time_precision`, `time_uncertainty`);
- **≥ 1** `claim` candidato (statement, `claim_type` da taxonomia de 10,
  `confidence`, `evidence_level`, perfil de incerteza);
- **≥ 1** `source` candidata (título, `authority_tier` proposto A/B/C, licença);
- **binding** claim→fonte com **localizador não-vazio** (página/URL/trecho) —
  vira `provenance_metadata` na promoção ([N1]);
- geometria ou correspondência moderna quando o item é localizável
  (paleo ⇒ marcado reconstrução, espelhando o CHECK do banco);
- relações afirmativas propostas (opcional; cada uma com binding próprio — [N1]);
- tag de sensibilidade **PG5 proposta** (`público` / `mediado` / `legal-review`,
  Leis 10.639/2003 e 11.645/2008) e **tier proposto**.

O manifesto registra `n_claims`, `n_fontes`, `n_relacoes` por pacote (para
normalizar a medição: pacotes não são todos do mesmo tamanho).

### 1.2 "Item revisado" — Tier 0

Pacote sobre o qual **todos os papéis aplicáveis** (mapa do C2 §5: científica /
historiográfica / editorial / geotemporal / licença / vieses / jurídica…,
derivados de camada + PG5) executaram o **checklist integral do §6.1** sobre
**cada claim e cada relação** e registraram decisão assinada (identidade +
timestamp **de ferramenta**). *Revisado* é o ato; *aprovado* é o desfecho quando
todos os papéis aprovam. Custo do item = soma de **todos** os papéis e **todas**
as passadas (re-revisão após devolução conta — retrabalho não some).

### 1.3 "Item revisado" — Tier 1

Pacote que, cumulativamente: (a) passou **100% das validações automáticas**
(§4); (b) pertence a um **lote fechado** cuja **amostra sorteada** (uniforme,
semente registrada no manifesto) recebeu o **checklist integral individual**
(papel único) com **zero defeito crítico**; (c) recebeu a decisão de lote
assinada por humano. O manifesto grava, por pacote, `revisao: individual |
por-lote` — honestidade sobre o que "revisado" significou para aquele item.

### 1.4 Desfechos

`aprovado` (→ promoção §7) · `devolvido` (defeito sanável, motivo tipado →
volta a rascunho) · `rejeitado` (fora de escopo / fonte inexistente /
irrecuperável → arquivado) · `bloqueado-validacao` (falhou check automático).
No Tier 1: **1 defeito crítico em qualquer amostrado ⇒ o lote inteiro é
devolvido** — sem aprovação parcial, sem trocar o item defeituoso e seguir
(Art. 13). Sensibilidade descoberta em amostra ⇒ o pacote sai do lote, é
re-triado Tier 0 **e a regra de triagem (§5) ganha o caso**.

**Defeito crítico (lista fechada):** claim não sustentado pela fonte no
localizador citado; tipagem que **superestima** o estatuto epistêmico;
`authority_tier` indevido; PG5 subclassificada; tempo/geo errados; licença
errada. **Não-crítico** (corrigível na revisão, sem devolver): grafia,
formatação, `display_time`.

### 1.5 Cronometria — como itens/hora é medido, por tier

- Fonte de tempo: **exclusivamente timestamps gerados pela ferramenta** (CLI do
  Chat 5), gravados em `ingestao/manifest.jsonl` (**append-only**; evento, ator,
  papel, tier, pacote/lote, t). **Auto-relato é inadmissível** (PG1: evidência,
  não afirmação).
- Eventos mínimos: `pacote_gerado` (IA; registra custo de máquina à parte),
  `validacao` (pass|fail), `triagem_confirmada` (tier, ator),
  `sessao_inicio/fim` (papel), `pacote_aberto`, `pacote_decidido` (desfecho),
  `pausa_inicio/fim`, `lote_montado` (ids, semente, amostra), `lote_decidido`,
  `promovido` (hash do commit).
- **Tempo humano de um pacote (por papel)** = `pacote_decidido` −
  `pacote_aberto` − pausas contidas. Sessão interrompida sem decisão: o evento
  fica no log, a amostra de tempo é **descartada** da estatística.
- **Custo Tier 0 por item aprovado** = Σ tempos de todos os papéis, todas as
  passadas até `aprovado`.
- **Custo Tier 1 por item aprovado** = (Σ tempos dos pacotes amostrados +
  tempo de montagem e decisão do lote) ÷ itens aprovados do lote. Lote devolvido
  acumula seu tempo na coorte até a aprovação.
- Tempo de máquina (geração IA, validação) é registrado em coluna própria e
  **não entra** no número humano.

### 1.6 O número-decisor e as métricas do report

Por tier: **minutos humanos por item aprovado** (média **e** mediana, com n) —
o número-decisor; `itens/hora` = 60 ÷ média (derivado); `claims/hora`
(normalização por tamanho); taxa de devolução; defeitos críticos por categoria;
custo de máquina (informativo). **Anti-Goodhart (Art. 13):** o número existe
para decidir a economia do produto e para melhorar o **rascunho da IA**
(defeitos → melhor retrieval/prompt); ele **nunca** é meta de produtividade do
revisor, e **nunca** se encurta o checklist para subir o número.

## 2. O laço — estados e atores

```
rascunho (IA) ─► validado ─► triado (T0|T1) ─► em-revisão ─► aprovado ─► promovido
      ▲              │                              │
      │        bloqueado-validacao                  ├─► devolvido ──► rascunho (correção)
      └─────────────────────────────────────────────┘└─► rejeitado (arquivado)
```

Em Tier 0, `em-revisão` instancia a máquina do C2 (queued → in-progress →
escalated/returned/blocked → done), com os mesmos papéis e não-poderes do dono
da fila (D-C2.6). O C2 permanece histórico não-normativo; este spec absorve
dele apenas o esqueleto que o Tier 0 exige.

| Ator | Pode | Nunca pode |
|---|---|---|
| **IA (rascunho + retrieval)** | Gerar pacotes DoR-completos; propor PG5 e tier; propor fontes candidatas | Escrever `review_status` / `provenance_status` / `per_asset_source_confirmed` (**campos inexistentes no formato de rascunho**); escrever `claim_set.resolution` (obrigatoriamente vazio); tocar o Postgres; aprovar; promover |
| **Validador automático** | Bloquear pacote (pass\|fail) | `waived`/`override` (não existem — Art. 13) |
| **Triador (humano)** | Confirmar tier ao montar lote; **endurecer** T1→T0 sem justificativa | Afrouxar T0→T1 sem justificativa registrada no manifesto |
| **Revisor por papel (humano)** | Decidir mérito no seu papel; corrigir não-críticos; escrever a `resolution` de ClaimSet à mão | Aprovar fora da sua competência; aprovar lote com defeito crítico |
| **Promotor (humano)** | Executar a materialização (§7), com identidade registrada | Promover pacote não-`aprovado` (teste negativo obrigatório) |

**Intake throttling (Art. 13):** se `em-revisão` acumular acima da capacidade
declarada (v0: **30 pacotes**), a **geração de rascunhos pausa** — a escala
recua; a revisão nunca afina.

## 3. O que a IA produz — e o que ela estruturalmente não escreve

O rascunho é um JSON por pacote em `ingestao/rascunhos/` (formato exato: Chat 5),
com os 8 campos do DoR como **proposta**. Estruturalmente garantido, não só
prometido:

1. O formato de rascunho **não possui** os campos `review_status`,
   `provenance_status`, `per_asset_source_confirmed` — a IA não tem onde
   escrevê-los; eles nascem na promoção (§7), por ato humano.
2. `claim_set.resolution` (a fronteira "sem equivalência") existe no formato
   mas o validador exige-a **vazia** no rascunho; ela só é preenchida **à mão
   pelo revisor competente** durante a revisão (Art. 7; C2 §5.4). ClaimSet
   proposto ⇒ tier 0 obrigatório.
3. Retrieval usa Wikidata/índices/busca **só para achar e ligar** (Art. 5); a
   fonte citada no binding tem de ser a **autoridade real** (a que o revisor
   abrirá no checklist), nunca o agregador.
4. `provenance_status` na promoção é sempre `corpus` — este laço **não cria**
   `seeded-demo`.

## 4. Validação automática (QA bloqueia — lista fechada v0)

1. Schema do pacote válido; vocabulários fechados iguais aos do DDL
   (`item_type`, `claim_type` × 10, `confidence` × 5, `authority_tier` A/B/C).
2. Campos proibidos ausentes/vazios (§3.1–3.2).
3. Binding: todo claim e toda relação afirmativa referenciam ≥ 1 fonte do
   pacote **com localizador não-vazio** ([N1] antecipado ao rascunho).
4. Eixo 3Z: `canonical_start ≤ canonical_end`; `scalar` dentro do intervalo;
   `source_time_basis` no vocabulário; precisão declarada; **incerteza
   declarada sempre que a precisão não é exata** (nunca número seco).
5. Geo: se localizável, geometria válida **ou** correspondência moderna
   declarada; `paleo ⇒ reconstrução` (espelha o CHECK do banco).
6. Colisão de id: inexistente no corpus (`ITENS`/carga promovida) e nos pacotes
   abertos; padrão `^[a-z]+:[a-z0-9\-]+$`.
7. Sem PII de pessoa viva não-pública, sem dado de menor (Art. 14); pessoa viva
   citada ⇒ tier 0 forçado.

Falha em qualquer check ⇒ `bloqueado-validacao`, volta a rascunho. **Sem
exceção, sem override** (Art. 13).

## 5. Triagem de tier (conservadora; na dúvida, Tier 0 — Art. 9)

**Elegível a Tier 1 somente se TODAS:** PG5 = `público`; sem ClaimSet; **todos**
os claims com `claim_type` ∈ {`fato-documentado`, `medição-direta`}; **todas**
as fontes `authority_tier = A`; sem pessoa viva; sem reconstrução/paleo (na
prática, tempo profundo já cai pela regra de `claim_type`); licença da fonte
sem restrição de uso. **Qualquer outra coisa — inclusive dúvida — é Tier 0.**
A IA propõe; o humano confirma na montagem do lote (evento no manifesto).
Sensibilidade descoberta depois, em qualquer estágio ⇒ pacote vira T0 e esta
seção ganha o caso (lista viva, versionada pelo git).

## 6. Revisão humana

### 6.1 Checklist integral (o ato de revisar tem conteúdo fixo — senão a cronometria mede coisas diferentes)

Por claim/relação: (1) a fonte **abre** e **sustenta** o statement no
localizador citado; (2) `authority_tier` correto; (3) `claim_type` correto — o
**mais fraco** compatível com a evidência, nunca promovido; (4)
`confidence`/`evidence_level` coerentes; (5) tempo (3Z, precisão, incerteza)
correto — precisão nunca inventada; (6) geo/correspondência moderna corretos;
(7) PG5 correta; (8) licença da fonte compatível com o uso; (9) relação:
direção e tipo sustentados; (10) ClaimSet: `resolution` escrita à mão pelo
revisor competente, pesos assimétricos conferidos (sem falsa equivalência).

### 6.2 Tier 0

Todos os papéis aplicáveis executam o §6.1 em **passes separados e cronometrados
por papel** — no v0 o dono veste os chapéus, mas os tempos por papel são
medidos individualmente (o custo por papel é o dado que dimensiona a equipe
futura). **Limite declarado:** para PG5 ∈ {`mediado`, `legal-review`} (temas
P14/10.639/11.645 etc.), o dono **não é** papel competente de mérito
historiográfico/jurídico; ver §7 para a consequência.

### 6.3 Tier 1

Lote de **10–25** pacotes 100% validados e confirmados na triagem. Amostra
sorteada com semente registrada: **calibração = 50% (piso 5)** até acumular
≥ 100 pacotes T1 medidos **e** zero defeito crítico amostral nos últimos 3
lotes; depois **20% (piso 5)**. Mudança desses números = entrada no
`DECISOES.md`, nunca silenciosa. Decisão de lote é ato humano assinado.

## 7. Promoção ao corpus (git primeiro; banco derivado — R1)

Só pacote `aprovado` promove, por comando humano com identidade registrada.
A promoção **materializa no repositório** (arquivo de carga consumido pelo
caminho de migração — formato exato: Chat 5, aditivo ao lado de `ITENS`, sem
tocar o DDL), de modo que `down -v` + `bootstrap` **reproduz o corpus com os
promovidos**. Promover só no banco vivo é proibido: o git é a verdade (R1).

`review_status` gravado na promoção:

- **`approved`** — quando todos os papéis competentes aplicáveis aprovaram
  (Tier 1; Tier 0 com PG5 = `público`).
- **`pending`** — pacotes Tier 0 com PG5 ∈ {`mediado`, `legal-review`}
  **enquanto não houver papel competente designado** (designação = entrada no
  `DECISOES.md`). Eles entram no corpus gateados e **juntam-se à fila viva**
  (`docs/fila-revisao-claimsets-sensiveis.md`) — mesmo padrão dos 3 ClaimSets
  pendentes. Art. 6 garante: `pending` não existe como fato para o público.

Isto satisfaz o "sempre entrando como `pending` com portão humano" de
D-20260703-03 na sua substância: nada rascunhado por IA **existe no core** antes
de um ato humano, e o sensível permanece `pending` até mérito competente.
(Alternativa considerada e descartada: gravar tudo como `pending` e aprovar em
segundo ato no banco — sem tabela de histórico de revisão no DDL, o segundo ato
não deixa trilha adicional; a trilha real é manifesto + commit.)

**Commit de promoção (R6):** carga + reports regenerados + README (contagens)
**no mesmo commit**; suítes re-verdes. **Armadilha conhecida:** `test_a4` pina
o total público (= 16 hoje) e `verify`/README pinam 40/47 — promover itens
exige atualizar esses pinos **junto**, no mesmo commit, com o report como
evidência (é exatamente o que R6 manda).

## 8. Report de medição (o artefato do Chat 5 — PG1)

Script gera `ingestao/reports/medicao-ingestao.json` a partir do manifesto:
por tier, as métricas do §1.6, com n, período e hash do manifesto. Report é
commitado junto de cada rodada (R6). Nenhuma meta numérica a priori: o Chat 5
**mede**, o dono decide com o número na mão (entrada no `DECISOES.md`).

## 9. Mapa de guardrails

| Invariante | Mecanismo neste laço |
|---|---|
| [N1] proveniência | Binding com localizador exigido já no rascunho (§4.3); FK real na promoção |
| [N2] autoritativo × derivado | Staging vive fora do core; corpus reconstruível do git; banco é derivado |
| Art. 5 índice ≠ autoridade | Retrieval só descobre; binding cita a autoridade real (§3.3) |
| Art. 6 exibição | Rascunho nem existe no core; sensível promove no máximo a `pending` |
| Art. 7 tipagem / fronteira | Vocabulários fechados; `resolution` só à mão (§3.2, §6.1.10) |
| Art. 9 regra de ouro | Dúvida ⇒ Tier 0 (§5); dúvida na revisão ⇒ devolver, nunca aprovar |
| Art. 13 QA bloqueia; escala não reduz revisão | Validação pass\|fail sem override; lote inteiro devolve; intake throttling (§2) |
| Art. 14 menores | Check de PII (§4.7); analytics do laço mede o processo, não pessoas |
| D-20260703-03 | Tiers como definidos; IA só na ingestão; runtime intocado |
| "IA nunca escreve claim/source/reviewStatus" | Estrutural (campos inexistentes no formato) + processual (promoção humana) + teste negativo (§10) |
| R1/R6/R7 | Promoção via git com reports no mesmo commit; este spec é o único documento novo |

## 10. Definition of Done do Chat 5 (evidência que fecha — PG1)

1. CLI mínima: `rascunhar` (IA) · `validar` · `triar` · `revisar` (cronômetro) ·
   `promover` · `medir` — operando sobre `ingestao/` + manifesto append-only.
2. **≥ 1 lote Tier 1 (≥ 10 pacotes)** e **≥ 3 pacotes Tier 0** medidos ponta a
   ponta com timestamps reais de revisão do dono.
3. `ingestao/reports/medicao-ingestao.json` commitado, com minutos/item
   aprovado por tier.
4. **Teste negativo:** tentar `promover` pacote não-`aprovado` **falha**; campo
   `review_status` presente num rascunho **reprova a validação** (no espírito
   do T1 do `verify.py`).
5. Suítes existentes re-verdes com pinos de contagem atualizados **no mesmo
   commit** dos reports (R6): `verify` 10/10 · `test_a4` · `test_a3` 10/10 ·
   HTTP 5/5 · frame 3D-T/ASSET-T/LIVE-T/COSMO-T.
6. Zero linha alterada em `db/ddl/` e `db/read-layer/`.

Sugestão de alvos da rodada de medição (uma linha, sem virar curadoria): T1 —
efemérides consensuais fonte A, `gregorianCE` (ex.: 14-bis 1906, cabo
transatlântico 1866, eclipse de Sobral 1919 como `medição-direta`); T0 — 2–3
alvos da fatia Brasil (ex.: Lei Áurea 1888 ⇒ PG5 `mediado` por tema, mesmo
sendo fato documentado — bom teste da triagem por tema), que já adiantam o
Chat 6 e, se sensíveis, entram como `pending` na fila viva.

## 11. Parâmetros v0 e pontos abertos ao dono

**Parâmetros v0** (mudança = entrada no `DECISOES.md`): lote T1 = 10–25;
amostra = 50% calibração → 20% regime (piso 5); throttling = 30 pacotes em
revisão; diretório `ingestao/` na raiz (Chat 5 pode realocar, registrando).

**Abertos ao dono (decidir no início do Chat 5):**
1. **Amostragem inicial** — confirma 50%→20% ou prefere 100% no primeiríssimo
   lote (mede o teto de custo antes de amostrar)?
2. **Designação de papéis competentes para PG5 ≠ público** — sem ela, todo
   sensível para em `pending` (coerente com a dívida 1; mas trava `approved`
   de qualquer tema P14, inclusive na fatia Brasil do Chat 6).
