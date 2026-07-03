# Etapa 4C — Normalização do Lote-Piloto e Entidades de Referência

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 4C · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial vinculante da Etapa 3.1, a arquitetura das camadas (Etapa 4A) e o lote-piloto P0 (Etapa 4B) · 12/06/2026
**Escopo desta etapa (e seus limites):** **normalização, correção e consolidação** do lote-piloto da Etapa 4B — **não** é expansão quantitativa. Transforma o lote em **padrão operacional** (gabarito) e cria os primeiros nós completos de `Concept`/`Entity`/`Place`/`Region`. Conforme solicitado, **não** cria lote massivo, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** desenha pipeline técnico, **não** expande para milhares de eventos, **não** usa Wikidata/Wikipedia como autoridade e **não** copia texto de fontes.

**O que herda e respeita.** Os 70 itens da Etapa 4B (62 da espinha SCI/HIST/BR/AFR/IND + 8 de cena SCENE), os vocabulários controlados das Etapas 2/3.1, o portão de licença da Etapa 1.1, o invariante de exibição (`reviewStatus ∈ {pending, legal-review, rejected}` ⇒ não exibível) e os ajustes de vocabulário propostos na Tarefa 7 da Etapa 4B.

> **Convenção.** Daqui em diante distinguem-se **`pilotCode`** (código editorial do lote: `SCI-01`, `HIST-15`, `BR-07`…) e **`knowledgeItemId`** (id permanente: `evt:big-bang`…). Aspas em claim = redação própria e didática (jamais transcrição de fonte).

---

## Sumário

1. Auditoria interna do lote 4B (Tarefa 1)
2. Normalização de ids e nomenclatura (Tarefa 2)
3. Concepts completos (Tarefa 3)
4. Entities completas (Tarefa 4)
5. Places e Regions completos (Tarefa 5)
6. Revisão de reviewStatus e publicabilidade (Tarefa 6)
7. Revisão dos ClaimSets (Tarefa 7)
8. Relationship graph revisado (Tarefa 8)
9. Gabarito ouro (Tarefa 9)
10. Relatório de normalização (Tarefa 10)
11. Próximos passos para a Etapa 4D (Tarefa 11)

---

## 1. Auditoria interna do lote 4B (Tarefa 1)

Auditoria executada item a item sobre os 70 registros. Os quinze pontos pedidos foram verificados; os achados materiais estão na tabela. Itens verificados **sem ocorrência** também são registrados (a ausência de erro é resultado de auditoria).

### 1.1 Verificações sem ocorrência (verde)

- **Ids duplicados:** nenhum (`pilotCode` e `knowledgeItemId` únicos nos 70).
- **Tipo × prefixo de id:** 100% consistente (todo `evt:`=Event, `proc:`=Process, `state:`=State, `concept:`=Concept, `ent:`=Entity).
- **Itens sem claim principal / claim temporal / fonte A/B / confidenceLevel / evidenceLevel / relationshipGraph:** nenhum — todos os 70 preenchem os campos mínimos.
- **Itens pending exibidos na simultaneidade:** nenhum — nenhum item `pending`/`legal-review` afirma aparecer; o invariante de exibição da Etapa 3.1 está respeitado.
- **Itens de risco editorial alto sem revisão humana:** nenhum — todos os itens `riscoEd alto/crítico` estão `pending`/`PENDENTE_REVISAO_HUMANA` (ver exceção BR-08 abaixo, que é borderline).

### 1.2 Achados materiais e correções

| # | Problema | Item afetado | Gravidade | Correção proposta | Status após correção |
|---|---|---|---|---|---|
| A1 | Referência quebrada: aponta para `IND-05`, inexistente | **IND-03** (`proc:resistencia-indigena`) | **Alta** (relação inválida) | Trocar alvo `IND-05` → **`IND-04`** (`permanencia-indigena-contemporanea`): a relação pretendida é resistência → permanência | **Corrigido** (ver R-graph §8) |
| A2 | Referência quebrada: aponta para `IND-05`, inexistente | **BR-08** (`evt:constituicao-1988-brasil`) | **Alta** | Trocar alvo `IND-05` → **`IND-04`**: a Constituição de 1988 reconhece direitos indígenas; a relação correta é com a permanência contemporânea | **Corrigido** |
| A3 | Estilo de referência a ClaimSet inconsistente: itens citam `CS-03`/`CS-04`…; a §6 da 4B define `CS3`/`CS4`… | SCI-11, SCI-21, SCI-22, HIST-02, HIST-13, HIST-15 (e notas) | **Média** (ambiguidade de id) | Adotar id canônico **`claimset:<tema>`** com `pilotCode` `CS1`…`CS7` (ver §2 e §7); referências passam a usar o `knowledgeItemId` | **Normalizado** |
| A4 | Prefixo fora do padrão: `ent:` em vez de `entity:` | **SCENE-07** (`ent:lavoisier`) | **Baixa** (cosmético, mas quebra a regra de prefixos) | Renomear → **`entity:lavoisier`** (mantém `pilotCode` SCENE-07) | **Normalizado** (ver §4) |
| A5 | `reviewStatus = approved` com `riscoEd médio-alto` e pendência condicional | **BR-08** (`evt:constituicao-1988-brasil`) | **Média** (publicabilidade) | Manter `approved` **apenas** para o núcleo factual (promulgação em 05/10/1988, fato documentado); qualquer overlay de disputa contemporânea exige revisão → rebaixar para `pending` | **Resolvido com ressalva** (ver §6) |
| A6 | Lacuna estrutural de tipos: pouquíssimos `Concept`/`Entity` e nenhum `Place`/`Region` como itens completos | lote inteiro | **Média** (cobertura de modelo) | Criar nós completos nas Tarefas 3–5 desta etapa | **Sanado nesta etapa** |
| A7 | Nós referenciados mas inexistentes como itens | `concept:tectonica-placas`, `concept:guerra-fria`, `concept:expansao-universo` | **Média** | Criar como `Concept` completos (Tarefa 3); `guerra-fria` entra como Concept novo | **Sanado** (tectônica e expansão na §3; guerra-fria adicionado) |
| A8 | Inconsistência camada × tipo: nenhuma crítica, mas `State` paleogeográfico (Pangeia) na camada 6 e `BiomeState` (Ediacara) na camada 9 convivem | SCI-16, SCI-19 | **Baixa** (aceitável) | Confirmar como **intencional** (camada principal ≠ subtipo de State); documentar | **Confirmado, sem mudança** |

**Correção destacada (pedida explicitamente):** a referência `IND-03 → IND-05` é corrigida para **`IND-03 → IND-04`**. A auditoria revelou **uma segunda ocorrência** do mesmo erro (`BR-08 → IND-05`), também corrigida para `IND-04`. Não se cria `IND-05`: não há item ausente real — era um id digitado errado em dois lugares.

---

## 2. Normalização de ids e nomenclatura (Tarefa 2)

### 2.1 Verdadeiro problema: dois identificadores diferentes coexistiam implicitamente

O lote 4B usava `SCI-01` como rótulo de bloco **e** `evt:big-bang` como id. São coisas distintas e devem ser **separadas formalmente**:

- **`pilotCode`** — código **editorial** do lote (sequencial, legível, ligado ao *lote* e à *espinha*): `SCI-01`, `HIST-15`, `BR-07`, `AFR-03`, `IND-04`, `SCENE-07`, `CS3`. Serve para curadoria e rastreio interno. **Não** é o identificador de grafo.
- **`knowledgeItemId`** — id **permanente e versionável** do nó no Knowledge Core, com prefixo de tipo. É o que o grafo, as relações e as fontes referenciam.

### 2.2 Prefixos canônicos (confirmados/ajustados)

| Prefixo | Tipo | Situação no 4B | Ação |
|---|---|---|---|
| `evt:` | Event | ok | manter |
| `proc:` | Process | ok | manter |
| `state:` | State | ok | manter |
| `concept:` | Concept | ok | manter |
| `entity:` | Entity | **`ent:` usado 1×** | **corrigir** `ent:lavoisier`→`entity:lavoisier` |
| `place:` | Place | inexistente | **introduzir** (Tarefa 5) |
| `region:` | Region | inexistente | **introduzir** (Tarefa 5) |
| `claimset:` | ClaimSet | citado como `CS-0x` | **introduzir** id canônico; `CSx` vira `pilotCode` |
| `rel:` | Relationship | arestas eram `R1`…`R20` | **introduzir** `rel:` para arestas reificadas; `Rn` vira `pilotCode` da aresta |
| `source:` | Source | fontes eram texto livre | **introduzir** `source:` para fontes reutilizáveis (ex.: `source:nasa`, `source:pbdb`) |

### 2.3 Estrutura de registro proposta (campos de identidade)

Cada nó do KC passa a carregar, no mínimo:

```
- pilotCode:        # código editorial do lote (ex.: SCI-01) — opcional, só para itens nascidos em lote-piloto
- knowledgeItemId:  # id permanente com prefixo de tipo (ex.: evt:big-bang)
- version:          # versão do registro (ex.: 1.0) — claims podem versionar independentemente
- canonicalLabel:   # rótulo preferencial exibível (ex.: "Big Bang")
- nameVariants:     # rótulos alternativos/idiomas/históricos (ex.: ["Grande Explosão"])
- status:           # ciclo de vida do registro: incompleto/rascunho/revisado/publicável/bloqueado (Etapa 4A)
                    #   — distinto de reviewStatus (pending/approved/legal-review/rejected), que é o portão de exibição
```

> **`status` × `reviewStatus`.** `status` é a **maturidade de povoamento** (quão completo está o registro); `reviewStatus` é o **portão editorial de exibição**. Um item pode estar `status = publicável` e ainda assim `reviewStatus = pending` se for sensível. Os dois são mantidos.

### 2.4 Regra de estabilidade

`knowledgeItemId` é **imutável** após publicação (renomeações entram em `nameVariants`, nunca trocam o id). `pilotCode` pode ser aposentado quando o lote-piloto deixar de ser a unidade de trabalho. Sem remodelagem além disto.

---

## 3. Concepts completos (Tarefa 3)

Primeiros 25 `Concept` estruturantes. Regra aplicada: **um `Concept` explica uma ideia que conecta vários itens — não substitui o `Event`/`Process` correspondente.** Onde há um evento homônimo, o Concept é a *ideia* e o evento é a *ocorrência datada* (relação `explica`/`relacionado-a`). Formato compacto: cada bloco preenche os 13 campos pedidos.

**`concept:big-bang`** · Big Bang
- def: modelo do início da expansão do universo a partir de estado quente e denso. · camadaP: 1 Universo · rel.camadas: 2, 25.
- claims mín.: "É o modelo cosmológico padrão do início da expansão" (`inferência científica`, conf alta). · fonte: `source:nasa` (A) · conf: alta · evid: inferência indireta/multi-proxy.
- riscoEd: baixo-médio (alvo de negacionismo — tratado **fora** de ClaimSet). · rel. 4B: `explica` SCI-01 (`evt:big-bang`), `concept:expansao-universo`. · revisão humana: não. · ling. escolar: "início do universo **observável**", não "início de tudo"; distinguir modelo de certeza absoluta.

**`concept:expansao-universo`** · Expansão do universo
- def: o espaço entre galáxias aumenta com o tempo; base observacional do Big Bang. · camadaP: 1 · rel.camadas: 25.
- claims mín.: "O universo está em expansão" (`inferência científica`, conf alta). · fonte: `source:nasa` (A) · conf: alta · evid: observacional (redshift, CMB).
- riscoEd: baixo. · rel. 4B: `relacionado-a` SCI-01, SCI-02; `parte-de` `concept:big-bang`. · revisão: não. · ling.: a expansão **não** tem "centro"; evitar a imagem da bomba.

**`concept:inflacao-cosmica`** · Inflação cósmica
- def: hipótese de expansão exponencial brevíssima no universo primordial. · camadaP: 1 · rel.camadas: 25.
- claims mín.: "É uma **hipótese** dominante, não consenso fechado" (`hipótese`, conf média). · fonte: cosmologia revisada (A/B) · conf: média · evid: dado modelado.
- riscoEd: baixo. · rel. 4B: `relacionado-a` SCI-01 (claim separado, nunca fundido ao fato da expansão). · revisão: não. · ling.: exemplo escolar de "fronteira da ciência" — hipótese tipada como hipótese.

**`concept:acrecao-planetaria`** · Acreção planetária
- def: formação de planetas pelo acúmulo de matéria no disco protoplanetário. · camadaP: 2 Astronomia/SS · rel.camadas: 3.
- claims mín.: "Planetas formam-se por acreção" (`inferência científica`, conf alta). · fonte: `source:nasa` (A) · conf: alta · evid: dado modelado + observação de discos.
- riscoEd: baixo. · rel. 4B: `explica` SCI-05 (`proc:formacao-sistema-solar`), SCI-06 (`evt:formacao-terra`). · revisão: não. · ling.: planetas "se juntam aos poucos", não "aparecem prontos".

**`concept:diferenciacao-planetaria`** · Diferenciação planetária
- def: separação interna de um corpo em núcleo/manto/crosta por densidade. · camadaP: 3 Terra geológica · rel.camadas: 6.
- claims mín.: "Corpos planetários diferenciam-se por densidade" (`inferência científica`, conf alta). · fonte: USGS/literatura (A/B) · conf: alta · evid: multi-proxy.
- riscoEd: baixo. · rel. 4B: `explica` SCI-08 (`proc:diferenciacao-terra`). · revisão: não. · ling.: liga "estrutura interna da Terra" a um processo, não a um dado fixo.

**`concept:atmosfera-anoxica`** · Atmosfera anóxica
- def: atmosfera com pouco ou nenhum O₂ livre. · camadaP: 4 Atmosfera · rel.camadas: 5, 8.
- claims mín.: "A Terra teve longa fase atmosférica anóxica" (`inferência científica`, conf alta). · fonte: NOAA/NCEI Paleo (A) · conf: alta · evid: registro material (geoquímica).
- riscoEd: baixo. · rel. 4B: `explica` SCI-09 (`state:atmosfera-primitiva`); `predecessor-de` `concept:oxigenacao-atmosferica`. · revisão: não. · ling.: "o ar de hoje é resultado da vida", quebra a intuição de ar imutável.

**`concept:fotossintese-oxigenica`** · Fotossíntese oxigênica
- def: processo biológico que produz O₂ a partir de luz, água e CO₂. · camadaP: 8 Vida e evolução · rel.camadas: 4.
- claims mín.: "A fotossíntese oxigênica libera O₂" (`fato documentado`, conf alta). · fonte: PBDB/biologia revisada (A/B) · conf: alta · evid: observacional.
- riscoEd: baixo. · rel. 4B: `explica` SCI-12 (`proc:fotossintese-oxigenica`); `causa` `concept:oxigenacao-atmosferica`. · revisão: não. · ling.: a ideia (mecanismo) é distinta da ocorrência histórica (SCI-12).

**`concept:oxigenacao-atmosferica`** · Oxigenação atmosférica
- def: acúmulo de O₂ livre na atmosfera ao longo do tempo geológico. · camadaP: 4 Atmosfera · rel.camadas: 8.
- claims mín.: "O O₂ atmosférico subiu a partir do Paleoproterozoico" (`inferência científica`, conf alta). · fonte: NOAA Paleo (A) · conf: alta · evid: registro material.
- riscoEd: baixo. · rel. 4B: `explica` SCI-13 (`proc:goe`); `decorreu-de` `concept:fotossintese-oxigenica`. · revisão: não. · ling.: conecta micro-organismos a uma mudança planetária — escala.

**`concept:tectonica-placas`** · Tectônica de placas
- def: teoria do movimento das placas litosféricas sobre o manto. · camadaP: 6 Tectônica/paleogeografia · rel.camadas: 3, 7.
- claims mín.: "A litosfera é dividida em placas em movimento" (`inferência científica`/consenso, conf alta). · fonte: USGS/Macrostrat (A/B) · conf: alta · evid: multi-proxy.
- riscoEd: baixo. · rel. 4B: `explica` SCI-19 (`state:pangeia`); `relacionado-a` `concept:supercontinente`. · revisão: não. · ling.: "os continentes se movem" — explicar deriva sem mística.

**`concept:supercontinente`** · Supercontinente
- def: agregação da maior parte das massas continentais num só bloco. · camadaP: 6 · rel.camadas: 5.
- claims mín.: "A Terra teve vários supercontinentes (ciclo de Wilson)" (`reconstrução modelada`, conf alta na existência). · fonte: EarthByte/GPlates (A, CC BY) · conf: alta · evid: dado modelado.
- riscoEd: baixo. · rel. 4B: `explica` SCI-19 (Pangeia); `relacionado-a` `region:pangeia`, `region:rodinia`. · revisão: não. · ling.: reconstrução, **não** mapa observado; Pangeia não foi a única.

**`concept:evolucao-biologica`** · Evolução biológica
- def: mudança das características hereditárias das populações ao longo das gerações. · camadaP: 8 Vida e evolução · rel.camadas: 9, 10.
- claims mín.: "A evolução é o princípio unificador da biologia" (`fato documentado`/consenso, conf alta). · fonte: PBDB/Open Tree of Life (A) · conf: alta · evid: multi-proxy.
- riscoEd: **médio** (alvo de negacionismo — **fora** de ClaimSet) → revisão recomendada. · rel. 4B: `explica` SCI-22, SCI-23 e toda a camada 8. · revisão humana: **sim**. · ling.: evolução **não** é "progresso" nem "melhoria"; sem escada de seres.

**`concept:selecao-natural`** · Seleção natural
- def: mecanismo evolutivo de reprodução diferencial conforme o ambiente. · camadaP: 8 · rel.camadas: 9.
- claims mín.: "É um dos mecanismos centrais da evolução" (`fato documentado`, conf alta). · fonte: biologia revisada (A/B) · conf: alta · evid: observacional + experimental.
- riscoEd: médio (uso indevido em "darwinismo social" — repudiar). · rel. 4B: `parte-de` `concept:evolucao-biologica`. · revisão: **sim**. · ling.: jamais aplicar a "raças"/sociedades humanas como hierarquia.

**`concept:ancestralidade-comum`** · Ancestralidade comum
- def: descendência de todos os seres vivos a partir de ancestrais compartilhados. · camadaP: 8 · rel.camadas: 10.
- claims mín.: "Os seres vivos compartilham ancestralidade" (`inferência científica`, conf alta). · fonte: Open Tree of Life (A, aberto) · conf: alta · evid: multi-proxy (genética/fóssil).
- riscoEd: médio. · rel. 4B: `relacionado-a` SCI-23 (`evt:surgimento-homo-sapiens`). · revisão: **sim**. · ling.: **unidade** da espécie humana; diversidade ≠ hierarquia.

**`concept:revolucao-agricola`** · Revolução agrícola (Neolítica)
- def: transição de caça-coleta para agricultura e pastoreio, em vários centros. · camadaP: 12 Civilizações · rel.camadas: 11, 14.
- claims mín.: "A agricultura surgiu de forma independente em vários lugares" (`interpretação`/fato, conf alta). · fonte: arqueologia revisada (A/B) · conf: alta · evid: registro material.
- riscoEd: médio (eurocentrismo/difusionismo). · rel. 4B: `explica` HIST-03 (`proc:revolucao-neolitica`). · revisão: sim. · ling.: **múltiplos centros**, não invenção única que "se espalhou".

**`concept:civilizacao`** · Civilização
- def: forma de organização social complexa (cidades, instituições, divisão do trabalho). · camadaP: 12 · rel.camadas: 13, 17.
- claims mín.: "É um conceito analítico, não um selo de superioridade" (`interpretação historiográfica`). · fonte: historiografia (A/B) · conf: média · evid: documental.
- riscoEd: **alto** (hierarquia "civilizado × primitivo"). · rel. 4B: `explica` HIST-06..11, BR-02, IND-01. · revisão: **sim**. · ling.: nunca "povos sem civilização"; sociedades diferentes, não inferiores.

**`concept:estado`** · Estado
- def: organização política com território, autoridade e instituições. · camadaP: 13 Política · rel.camadas: 12, 14.
- claims mín.: "É uma forma histórica de organização política, não universal nem eterna" (`interpretação`). · fonte: historiografia/ciência política (A/B) · conf: média · evid: documental.
- riscoEd: médio. · rel. 4B: `explica` SCENE-02, SCENE-03, SCENE-04, HIST-09. · revisão: sim. · ling.: distinguir Estado de nação e de governo.

**`concept:imperio`** · Império
- def: Estado que domina outros povos/territórios sob um centro. · camadaP: 13 · rel.camadas: 19, 21.
- claims mín.: "Impérios envolvem dominação e desigualdade entre centro e periferias" (`interpretação`). · fonte: historiografia (A/B) · conf: média · evid: documental.
- riscoEd: **alto** (glorificação/colonial). · rel. 4B: `explica` HIST-09, HIST-10, SCENE-03, SCENE-04, AFR-01. · revisão: **sim**. · ling.: nomear a dominação; não romantizar "grandeza imperial".

**`concept:colonialismo`** · Colonialismo
- def: dominação política, econômica e cultural de territórios e povos por uma potência externa. · camadaP: 13 · rel.camadas: 21, 22, 20.
- claims mín.: "É um sistema histórico de dominação e exploração" (`interpretação historiográfica`, conf alta). · fonte: historiografia plural (A/B); fontes indígenas/africanas · conf: alta · evid: documental + oral.
- riscoEd: **alto** (Leis 10.639/11.645). · rel. 4B: `explica` HIST-12, HIST-13, BR-04, IND-02. · revisão: **sim**. · ling.: centrar agência dos colonizados; não eufemizar ("expansão", "descobrimento" sem contexto).

**`concept:escravidao`** · Escravidão
- def: sistema de redução de seres humanos à condição de propriedade e trabalho forçado. · camadaP: 14 Economia · rel.camadas: 21, 20.
- claims mín.: "Foi um sistema de violência e exploração de pessoas" (`fato documentado`/`interpretação`, conf alta). · fonte: bases do tráfico/historiografia (A/B) · conf: alta · evid: documental + registro material.
- riscoEd: **crítico** (Lei 10.639; dignidade das vítimas). · rel. 4B: `explica` AFR-03, AFR-04, HIST-18, BR-05. · revisão: **sim (obrigatória)**. · ling.: "pessoas escravizadas" (não "escravos"); jamais naturalizar; centrar humanidade e resistência.

**`concept:diaspora`** · Diáspora
- def: dispersão forçada ou massiva de um povo para fora de seu território de origem. · camadaP: 21 África · rel.camadas: 20, 17.
- claims mín.: "A diáspora africana resultou em grande parte do tráfico atlântico" (`interpretação`, conf alta). · fonte: historiografia da diáspora (A/B) · conf: alta · evid: documental.
- riscoEd: **alto** (Lei 10.639). · rel. 4B: `explica` AFR-05, AFR-06. · revisão: **sim**. · ling.: diáspora como **agência e cultura**, não só perda.

**`concept:revolucao-politica`** · Revolução política
- def: transformação profunda e relativamente rápida da ordem política e social. · camadaP: 13 Política · rel.camadas: 17, 19.
- claims mín.: "Revoluções têm causas múltiplas e disputadas" (`interpretação historiográfica`). · fonte: historiografia (A/B) · conf: média · evid: documental.
- riscoEd: médio (leituras unicausais/ideológicas). · rel. 4B: `explica` HIST-15, HIST-16, BR-06, SCENE-02. · revisão: sim. · ling.: apresentar causas como debate (ver `claimset:causas-revolucao-francesa`), não veredito.

**`concept:industrializacao`** · Industrialização
- def: transição para produção mecanizada e economia industrial. · camadaP: 16 Tecnologia · rel.camadas: 14, 5.
- claims mín.: "Transformou economia, sociedade e ambiente" (`interpretação`, conf alta). · fonte: OWID/historiografia (A/B) · conf: alta · evid: documental + dado quantitativo.
- riscoEd: médio. · rel. 4B: `explica` HIST-17; `causa` `concept:mudanca-climatica-antropica`. · revisão: sim. · ling.: ganhos e custos (trabalho, ambiente) lado a lado.

**`concept:mudanca-climatica-antropica`** · Mudança climática antrópica
- def: alteração do clima causada por atividades humanas, sobretudo emissões de gases-estufa. · camadaP: 5 Clima · rel.camadas: 16, 23.
- claims mín.: "O aquecimento atual é real e majoritariamente antrópico" (`inferência científica`, **consenso amplo**, conf alta). · fonte: NOAA/NASA GISS/IPCC (dados; figuras recriadas) · conf: alta · evid: medição instrumental + multi-proxy.
- riscoEd: **alto** (negacionismo). · rel. 4B: `explica` HIST-21; ancora `claimset:mudancas-climaticas`. · revisão: **sim**. · ling.: consenso é consenso; incerteza é de **projeção**, não do fato; negacionismo **fora** de ClaimSet.

**`concept:modern-correspondence`** · ModernCorrespondence
- def: relação que liga um lugar/entidade histórica à sua correspondência geográfica atual (ex.: "território→Minas Gerais"). · camadaP: 25 Fontes/meta · rel.camadas: 20, 6.
- claims mín.: "Permite localizar o passado em referências atuais sem anacronismo" (mecanismo do modelo). · fonte: **modelo interno do KC (Etapa 2)** · conf: alta · evid: definição de modelo.
- riscoEd: médio (anacronismo se mal usado). · rel. 4B: usado por HIST-16, BR-03, BR-05, SCENE-02. · revisão: não (mas curadoria atenta). · ling.: "o lugar que **hoje** chamamos de…"; nunca projetar fronteiras atuais ao passado.

**`concept:simultaneidade-historica`** · Simultaneidade histórica
- def: propriedade de recuperar tudo o que ocorria no mundo num mesmo instante, via interseção de índices. · camadaP: 25 · rel.camadas: 23.
- claims mín.: "A simultaneidade emerge dos índices espaço-temporais, não é um módulo à parte" (mecanismo, Etapa 2 P7). · fonte: **modelo interno do KC (Etapa 2)** · conf: alta · evid: definição de modelo.
- riscoEd: médio (falsa equivalência entre eventos). · rel. 4B: realizada pela cena de 1789 (SCENE-01..08). · revisão: não. · ling.: "o que acontecia ao mesmo tempo", sem hierarquizar regiões.

> **Concept adicional criado para sanar A7:** **`concept:guerra-fria`** · Guerra Fria — def: disputa geopolítica EUA×URSS (~1947–1991). camadaP: 13 · rel.camadas: 16, 19. claim mín.: "Estruturou a política e a tecnologia da 2ª metade do séc. XX" (`interpretação`, conf alta). fonte: historiografia (A/B). riscoEd: médio. rel. 4B: `explica`/contextualiza HIST-19 (`evt:apollo-11`). revisão: sim. ling.: bipolaridade sem reduzir o "Sul global" a coadjuvante.

---

## 4. Entities completas (Tarefa 4)

Primeiros 20 `Entity` (+ `entity:lavoisier`, normalizado de SCENE-07). Regra aplicada: a `Entity` é o **ator/objeto durável**; o `State` é sua **condição num momento** (ex.: `entity:imperio-otomano` ↔ `state:imperio-otomano-1789`). Para **grupos humanos sensíveis** aplica-se a Etapa 3.1: linguagem cuidadosa, revisão humana e **agência** (nunca objeto passivo).

**`entity:universo-observavel`** · Universo observável
- tipo: entidade cósmica · desc: a porção do universo de que podemos receber luz. · TimeRange: ~13,8 Ga–presente · Place/Region: —.
- claims mín.: "Tem ~13,8 Ga de idade" (`inferência científica`, alta). · fonte: `source:nasa` (A) · conf: alta · evid: multi-proxy. · riscoEd: baixo.
- rel. 4B: `relacionado-a` SCI-01, `concept:expansao-universo`. · nomenclatura: "observável" é parte do nome — evita afirmar sobre o que não se observa.

**`entity:sistema-solar`** · Sistema Solar
- tipo: sistema astronômico · desc: o Sol e os corpos a ele gravitacionalmente ligados. · TimeRange: ~4,57 Ga–presente · Place/Region: —.
- claims mín.: "Formou-se há ~4,57 Ga" (`inferência científica`, alta). · fonte: `source:nasa` (A) · conf: alta · evid: medição (meteoritos). · riscoEd: baixo.
- rel. 4B: `relacionado-a` SCI-05. · nomenclatura: nomes de corpos via IAU (autoridade de nomes).

**`entity:sol`** · Sol
- tipo: estrela · desc: a estrela central do Sistema Solar. · TimeRange: ~4,6 Ga–presente · Place/Region: —.
- claims mín.: "É uma estrela de sequência principal" (`fato documentado`, alta). · fonte: `source:nasa` (A) · conf: alta · evid: observacional. · riscoEd: baixo.
- rel. 4B: `parte-de` `entity:sistema-solar`; `relacionado-a` SCI-05. · nomenclatura: —.

**`entity:terra`** · Terra
- tipo: planeta · desc: o terceiro planeta do Sistema Solar, suporte da vida conhecida. · TimeRange: ~4,54 Ga–presente · Place/Region: —.
- claims mín.: "Formou-se há ~4,54 Ga" (`inferência científica`, alta). · fonte: `source:nasa`/Macrostrat (A) · conf: alta · evid: medição. · riscoEd: baixo (idade da Terra alvo de negacionismo, fora de ClaimSet).
- rel. 4B: `relacionado-a` SCI-06, SCI-08..10; `parte-de` `entity:sistema-solar`. · nomenclatura: —.

**`entity:lua`** · Lua
- tipo: satélite natural · desc: o satélite natural da Terra. · TimeRange: ~4,5 Ga–presente · Place/Region: —.
- claims mín.: "Formou-se há ~4,5 Ga" (`inferência científica`, alta). · fonte: `source:nasa` (A) · conf: alta · evid: medição. · riscoEd: baixo.
- rel. 4B: `relacionado-a` SCI-07; `localizado-em` `region:sistema-terra-lua`. · nomenclatura: —.

**`entity:genero-homo`** · Gênero *Homo*
- tipo: táxon biológico · desc: o gênero que inclui o ser humano e parentes extintos. · TimeRange: ~2,8 Ma–presente · Place/Region: origem africana.
- claims mín.: "Surgiu na África há ~2,8–2,5 Ma" (`inferência científica`, média-alta). · fonte: paleoantropologia (A/B) · conf: média-alta · evid: registro material. · riscoEd: **alto** (raça/ciência).
- rel. 4B: `explica`/`relacionado-a` SCI-22; `predecessor-de` `entity:homo-sapiens`. · revisão: **sim**. · nomenclatura: itálico no nome científico; sem hierarquia entre espécies.

**`entity:homo-sapiens`** · *Homo sapiens*
- tipo: espécie biológica (e grupo humano) · desc: a espécie humana atual. · TimeRange: ~300 ka–presente · Place/Region: origem africana.
- claims mín.: "Surgiu na África há ~300 ka" (`inferência científica`, média-alta). · fonte: paleoantropologia/paleogenética (A/B) · conf: média-alta · evid: registro material + genética. · riscoEd: **alto**.
- rel. 4B: `sucessor-de` `entity:genero-homo`; `relacionado-a` SCI-23, HIST-01. · revisão: **sim**. · nomenclatura: **unidade da espécie**; diversidade humana não é hierarquia; sem "raças biológicas".

**`entity:cianobacterias`** · Cianobactérias
- tipo: grupo de microrganismos · desc: bactérias fotossintetizantes produtoras de O₂. · TimeRange: ~Arqueano–presente · Place/Region: global.
- claims mín.: "Sua fotossíntese contribuiu para a oxigenação da atmosfera" (`inferência científica`, alta). · fonte: PBDB/biologia (A/B) · conf: alta · evid: registro material. · riscoEd: baixo.
- rel. 4B: `relacionado-a` SCI-12, SCI-13; `explica` `concept:oxigenacao-atmosferica`. · nomenclatura: —.

**`entity:dinossauros-nao-avianos`** · Dinossauros não-avianos
- tipo: grupo biológico (parafilético usual) · desc: dinossauros, exceto as aves, extintos no K-Pg. · TimeRange: ~Triássico–66 Ma · Place/Region: global.
- claims mín.: "Extinguiram-se no evento K-Pg (~66 Ma)" (`inferência científica`, alta). · fonte: PBDB (A) · conf: alta · evid: registro material (fóssil). · riscoEd: baixo.
- rel. 4B: `afetado-por` SCI-21 (`evt:extincao-kpg`). · nomenclatura: "não-avianos" é essencial (aves **são** dinossauros).

**`entity:franca`** · França
- tipo: Estado/nação (ator histórico) · desc: Estado europeu, palco da Revolução de 1789. · TimeRange: (formação medieval)–presente · Place/Region: Europa Ocidental.
- claims mín.: "Foi o palco da Revolução Francesa (1789–1799)" (`fato documentado`, alta). · fonte: historiografia (A/B) · conf: alta · evid: documental. · riscoEd: baixo-médio.
- rel. 4B: `localizado-em` `region:franca-1789`; `relacionado-a` HIST-15, SCENE-01. · nomenclatura: distinguir a entidade durável (França) do `state` de 1789.

**`entity:estados-unidos`** · Estados Unidos
- tipo: Estado/nação · desc: país norte-americano; governo constitucional desde 1789. · TimeRange: 1776/1789–presente · Place/Region: América do Norte.
- claims mín.: "Iniciou seu governo constitucional em 1789" (`fato documentado`, alta). · fonte: arquivos/historiografia (A/B) · conf: alta · evid: documental. · riscoEd: baixo.
- rel. 4B: `relacionado-a` SCENE-02; `localizado-em` `region:america-norte-1789`. · nomenclatura: —.

**`entity:imperio-otomano`** · Império Otomano
- tipo: Estado imperial (ator histórico) · desc: império plurirreligioso entre Ásia, Europa e África (~1299–1922). · TimeRange: ~1299–1922 · Place/Region: Anatólia/Bálcãs/Levante/N. África.
- claims mín.: "Existiu como grande potência até o início do séc. XX" (`fato documentado`, alta). · fonte: historiografia (A/B) · conf: alta · evid: documental. · riscoEd: médio.
- rel. 4B: condição em 1789 = `state:imperio-otomano-1789` (SCENE-03). · revisão: sim. · nomenclatura: evitar leitura orientalista; centrar complexidade própria.

**`entity:china-qing`** · China Qing
- tipo: Estado imperial · desc: última dinastia imperial chinesa (1644–1912). · TimeRange: 1644–1912 · Place/Region: Ásia Oriental.
- claims mín.: "Foi um dos maiores Estados e economias do mundo no séc. XVIII" (`fato`+`interpretação`, média-alta). · fonte: historiografia/OWID (A/B) · conf: média-alta · evid: documental. · riscoEd: médio.
- rel. 4B: condição em 1789 = `state:china-qing-1789` (SCENE-04). · revisão: sim. · nomenclatura: "Qing", não apenas "China imperial".

**`entity:imperio-mali`** · Império do Mali
- tipo: Estado imperial africano · desc: império da África Ocidental (~séc. XIII–XVII), centro de comércio e saber. · TimeRange: ~1235–~1600 · Place/Region: África Ocidental/Sahel.
- claims mín.: "Foi grande potência comercial e cultural da África Ocidental" (`interpretação`/fato, alta). · fonte: historiografia africana (A/B) · conf: alta · evid: documental + oral. · riscoEd: **alto** (Lei 10.639).
- rel. 4B: `explica`/condição = HIST-10 (`state:imperio-mali`); `localizado-em` `region:africa-ocidental`, `region:sahel`. · revisão: **sim**. · nomenclatura: África como protagonista, com fontes orais reconhecidas como evidência.

**`entity:portugal`** · Portugal
- tipo: Estado/nação · desc: reino ibérico, protagonista da expansão marítima. · TimeRange: ~1139–presente · Place/Region: Península Ibérica.
- claims mín.: "Liderou a expansão marítima do séc. XV" (`fato documentado`, alta). · fonte: historiografia (A/B) · conf: alta · evid: documental. · riscoEd: **alto** (colonialismo).
- rel. 4B: `relacionado-a` HIST-12, BR-04. · revisão: **sim**. · nomenclatura: nomear a dominação colonial; não heroicizar "descobrimentos".

**`entity:espanha`** · Espanha
- tipo: Estado/nação · desc: reino ibérico, potência colonial nas Américas. · TimeRange: ~1492–presente (unificação) · Place/Region: Península Ibérica.
- claims mín.: "Patrocinou a travessia de 1492 e a colonização da América" (`fato documentado`, alta). · fonte: historiografia (A/B) · conf: alta · evid: documental. · riscoEd: **alto** (colonialismo).
- rel. 4B: `relacionado-a` HIST-13, IND-02. · revisão: **sim**. · nomenclatura: idem Portugal; centrar povos originários.

**`entity:povos-indigenas-brasil`** · Povos indígenas no território hoje brasileiro
- tipo: **grupo humano (sensível)** · desc: centenas de povos, línguas e culturas originárias, antes de 1500 e até hoje. · TimeRange: pré-1500–presente · Place/Region: território hoje brasileiro.
- claims mín.: "São povos diversos, agentes históricos, presentes antes e depois de 1500" (`fato documentado`/`interpretação`, alta). · fonte: etno-historiografia, IPHAN, **fontes indígenas** (A/B) · conf: alta · evid: documental + registro material + **tradição/registro oral**. · riscoEd: **crítico** (Lei 11.645).
- rel. 4B: `relacionado-a` BR-03, IND-01..IND-04. · revisão: **sim (obrigatória)**. · nomenclatura: **pluralidade** (povos, não "o índio"); agência, não vítimas passivas; presente **e** passado; autodenominações quando possível.

**`entity:africanos-escravizados-afrodescendentes`** · Pessoas africanas escravizadas e afrodescendentes (grupo histórico)
- tipo: **grupo humano (sensível)** · desc: pessoas escravizadas trazidas à força e seus descendentes, agentes de cultura e resistência. · TimeRange: séc. XVI–presente · Place/Region: África→Américas (mundo atlântico).
- claims mín.: "Foram sujeitos de cultura, trabalho e resistência, não objetos" (`fato documentado`/`interpretação`, alta). · fonte: historiografia da escravidão/diáspora, **fontes afro-brasileiras** (A/B) · conf: alta · evid: documental + **tradição/registro oral**. · riscoEd: **crítico** (Lei 10.639).
- rel. 4B: `relacionado-a` AFR-03..AFR-06, HIST-18, BR-05. · revisão: **sim (obrigatória)**. · nomenclatura: "pessoas escravizadas" (a escravidão é condição imposta, não identidade); centrar humanidade, agência e quilombos.

**`entity:nasa`** · NASA
- tipo: organização (instituição) · desc: agência espacial dos EUA; fonte primária P0 do projeto. · TimeRange: 1958–presente · Place/Region: EUA.
- claims mín.: "É agência espacial e fonte de dados de domínio público" (`fato documentado`, alta). · fonte: própria/arquivos (A) · conf: alta · evid: documental. · riscoEd: baixo.
- rel. 4B: provê dados para SCI-01..10, HIST-19; corresponde a `source:nasa`. · nomenclatura: distinguir a **Entity** (organização) da **Source** (`source:nasa`).

**`entity:world-wide-web`** · World Wide Web
- tipo: artefato técnico/sistema · desc: sistema de documentos interligados na Internet (1989–1991). · TimeRange: 1989–presente · Place/Region: CERN→global.
- claims mín.: "Foi proposta por Tim Berners-Lee em 1989; primeiro site em 1991" (`fato documentado`, alta). · fonte: CERN/arquivos (A) · conf: alta · evid: documental. · riscoEd: baixo.
- rel. 4B: `explica`/condição = HIST-20 (`evt:criacao-www`). · nomenclatura: distinguir Web de Internet.

**`entity:lavoisier`** *(normalizado de SCENE-07; era `ent:lavoisier`)* · Antoine-Laurent de Lavoisier
- tipo: pessoa · desc: químico francês (1743–1794), figura central da química moderna. · TimeRange: 1743–1794 · Place/Region: França.
- claims mín.: "Figura central da química moderna" (`fato documentado`, alta). · fonte: história da ciência (A/B); VIAF só reconciliação (C/INDX) · conf: alta · evid: documental. · riscoEd: baixo.
- rel. 4B: `participou-de` SCENE-01 (`evt:lavoisier-traite-1789`). · nomenclatura: VIAF/Wikidata **apenas** reconciliam id; nunca afirmam claims.

---

## 5. Places e Regions completos (Tarefa 5)

Primeiros nós `Place` (pontuais/locais) e `Region` (áreas). Regra aplicada: **não se inventa geometria** — sem geometria validada, `geometryStatus = pendente` e flag `PENDENTE_REFINAMENTO_ESPACIAL`. `geometryStatus ∈ {real, histórico, inferido, moderno, paleogeográfico, pendente}`. Fontes de geometria "verdes": Natural Earth (PD), geoBoundaries (aberto), IBGE (aberto), GPlates/EarthByte (CC BY) para paleogeografia. Pleiades (CC BY) para lugares antigos.

### 5.1 Places

**`place:paris`** · Paris · variantes: ["Lutécia"] · TimeRange validade: atual (núcleo histórico antigo) · geometryStatus: **moderno** (real) · ModernCorr: — · SpatialUncertainty: baixa · fonte: Natural Earth/geoBoundaries (A) · riscoEd: baixo · riscoLic: 0–1 · rel. 4B: `local-de` HIST-15, SCENE-01.

**`place:versalhes`** · Versalhes · variantes: ["Versailles"] · TimeRange: atual (palácio séc. XVII) · geometryStatus: **moderno** · ModernCorr: — · SpatialUncertainty: baixa · fonte: Natural Earth (A) · riscoEd: baixo · riscoLic: 0–1 · rel. 4B: `local-de` HIST-15 (corte/Estados Gerais).

**`place:ouro-preto`** · Ouro Preto · variantes: ["Vila Rica"] · TimeRange: Vila Rica (colonial)→Ouro Preto (atual) · geometryStatus: **moderno** + **histórico** (nome) · ModernCorr: Vila Rica → Ouro Preto/MG · SpatialUncertainty: baixa · fonte: IBGE (A, aberto) · riscoEd: médio (escravidão/ouro) · riscoLic: 1 · rel. 4B: `local-de` BR-05, HIST-16.

**`place:washington-dc`** · Washington, D.C. · variantes: ["District of Columbia"] · TimeRange: fundada 1790 (**em 1789 a capital era Nova York**) · geometryStatus: **moderno** · ModernCorr: — · SpatialUncertainty: baixa · fonte: Natural Earth (A) · riscoEd: baixo · riscoLic: 0 · rel. 4B: relacionado a SCENE-02 *(nota: o governo de 1789 instalou-se em Nova York; registrar para evitar anacronismo)*.

**`place:tombuctu`** · Tombuctu · variantes: ["Timbuktu", "Timbouctou"] · TimeRange: florescimento medieval–atual · geometryStatus: **moderno** + **histórico** · ModernCorr: cidade no atual Mali · SpatialUncertainty: baixa · fonte: geoBoundaries/Pleiades (A) · riscoEd: alto (Lei 10.639; centro de saber africano) · riscoLic: 1 · rel. 4B: `local-de` HIST-10 (Mali), AFR-02.

**`place:chicxulub`** · Cratera de Chicxulub · variantes: ["Chicxulub crater"] · TimeRange: impacto ~66 Ma · geometryStatus: **inferido** (estrutura soterrada; geofísica) · ModernCorr: península de Yucatán, México · SpatialUncertainty: média (extensão da cratera) · fonte: USGS/geociências (A/B) · riscoEd: baixo · riscoLic: 1 · rel. 4B: `local-de` SCI-21 (`evt:extincao-kpg`).

**`place:caribe`** · Caribe · variantes: ["Antilhas", "Mar das Caraíbas"] · TimeRange: atual/histórico · geometryStatus: **moderno** (área marítima) · ModernCorr: — · SpatialUncertainty: média (limites difusos) · fonte: Natural Earth (A) · riscoEd: alto (1492/colonização/escravidão) · riscoLic: 0–1 · rel. 4B: `relacionado-a` HIST-13, AFR-05.

**`place:lisboa`** · Lisboa · variantes: ["Olisipo"] · TimeRange: atual (antiga) · geometryStatus: **moderno** · ModernCorr: — · SpatialUncertainty: baixa · fonte: Natural Earth (A) · riscoEd: médio (expansão/colonialismo) · riscoLic: 0–1 · rel. 4B: `local-de` HIST-12 (expansão portuguesa).

**`place:roma`** · Roma · variantes: ["Roma Antiga", "Urbe"] · TimeRange: fundação tradicional 753 a.C.–atual · geometryStatus: **moderno** + **histórico** · ModernCorr: cidade na Itália · SpatialUncertainty: baixa (cidade); a *extensão imperial* é Region à parte · fonte: Pleiades (A, CC BY) · riscoEd: baixo · riscoLic: 1 · rel. 4B: `local-de` HIST-09 (`state:roma-antiga`).

**`place:atenas`** · Atenas · variantes: ["Athína"] · TimeRange: antiga–atual · geometryStatus: **moderno** + **histórico** · ModernCorr: cidade na Grécia · SpatialUncertainty: baixa · fonte: Pleiades (A) · riscoEd: baixo · riscoLic: 1 · rel. 4B: `local-de` HIST-08 (`state:grecia-antiga`).

**`place:meca`** · Meca · variantes: ["Makkah"] · TimeRange: antiga–atual · geometryStatus: **moderno** + **histórico** · ModernCorr: cidade na Arábia Saudita · SpatialUncertainty: baixa · fonte: geoBoundaries (A) · riscoEd: médio (tema religioso — respeito) · riscoLic: 1 · rel. 4B: `relacionado-a` HIST-11 (mundo islâmico medieval).

**`place:jebel-irhoud`** · Jebel Irhoud · variantes: ["Adrar n Ighoud"] · TimeRange: sítio ~300 ka · geometryStatus: **real** (sítio arqueológico, Marrocos) · ModernCorr: Marrocos · SpatialUncertainty: baixa (sítio) · fonte: paleoantropologia (A/B) · riscoEd: alto (origem humana/raça) · riscoLic: 1 · rel. 4B: `evidência-de` SCI-23 (`evt:surgimento-homo-sapiens`).

**`place:jack-hills`** · Jack Hills · variantes: [] · TimeRange: sítio (zircões ~4,4 Ga) · geometryStatus: **real** (sítio, Austrália Ocidental) · ModernCorr: Austrália · SpatialUncertainty: baixa · fonte: geociências (A/B) · riscoEd: baixo · riscoLic: 1 · rel. 4B: `evidência-de` SCI-10 (`evt:formacao-oceanos`).

### 5.2 Regions

**`region:franca-1789`** · França em 1789 · variantes: ["Reino da França (1789)"] · TimeRange validade: 1789 · geometryStatus: **histórico** `PENDENTE_REFINAMENTO_ESPACIAL` (fronteiras de 1789 a validar) · ModernCorr: França atual · SpatialUncertainty: média · fonte: Natural Earth histórico/historiografia (A/B) · riscoEd: baixo · riscoLic: 0–1 · rel. 4B: `palco-de` HIST-15; condição de `entity:franca`.

**`region:capitania-minas-gerais`** · Capitania de Minas Gerais · variantes: ["Minas colonial"] · TimeRange: ~1720–1822 · geometryStatus: **histórico** `PENDENTE_REFINAMENTO_ESPACIAL` · ModernCorr: estado de Minas Gerais (`concept:modern-correspondence`) · SpatialUncertainty: média · fonte: IBGE/Arquivo Nacional (A) · riscoEd: médio (ouro/escravidão) · riscoLic: 1 · rel. 4B: `palco-de` BR-05, HIST-16.

**`region:territorio-brasil-atual`** · Território que hoje corresponde ao Brasil · variantes: ["Brasil (recorte moderno)"] · TimeRange: moderno (usado como referência p/ o passado) · geometryStatus: **moderno** · ModernCorr: Brasil · SpatialUncertainty: baixa · fonte: IBGE/geoBoundaries (A, aberto) · riscoEd: alto (anacronismo se projetado ao passado) · riscoLic: 1 · rel. 4B: referência de BR-01..03, IND-01..04 via `concept:modern-correspondence`.

**`region:america-norte-1789`** · América do Norte em 1789 · variantes: [] · TimeRange: 1789 · geometryStatus: **histórico** `PENDENTE_REFINAMENTO_ESPACIAL` · ModernCorr: EUA/Canadá/México atuais · SpatialUncertainty: alta (fronteiras coloniais difusas) · fonte: Natural Earth histórico (A/B) · riscoEd: médio (apagamento indígena) · riscoLic: 0–1 · rel. 4B: contexto de SCENE-02; **não** apagar territórios indígenas.

**`region:africa-ocidental`** · África Ocidental · variantes: [] · TimeRange: histórico/atual · geometryStatus: **moderno** (região), **fronteira difusa** · ModernCorr: — · SpatialUncertainty: alta · fonte: Natural Earth/geoBoundaries (A) · riscoEd: alto (Lei 10.639) · riscoLic: 0–1 · rel. 4B: `contém`/contexto de HIST-10, AFR-02, SCENE-05.

**`region:sahel`** · Sahel · variantes: [] · TimeRange: histórico/atual (faixa ecológica) · geometryStatus: **moderno** (região climática), **fronteira difusa** · ModernCorr: — · SpatialUncertainty: alta · fonte: Natural Earth (A) · riscoEd: médio · riscoLic: 0 · rel. 4B: contexto de HIST-10 (Mali), AFR-02 (rotas transaarianas).

**`region:china-qing`** · China Qing (extensão) · variantes: ["Império Qing"] · TimeRange: 1644–1912 · geometryStatus: **histórico** `PENDENTE_REFINAMENTO_ESPACIAL` · ModernCorr: China atual (aprox.) · SpatialUncertainty: média-alta · fonte: historiografia (A/B) · riscoEd: médio · riscoLic: 1 · rel. 4B: condição = SCENE-04; `entity:china-qing`.

**`region:mundo-atlantico`** · Mundo atlântico · variantes: ["sistema atlântico"] · TimeRange: ~séc. XV–XIX · geometryStatus: **inferido** (recorte analítico, sem fronteira) · ModernCorr: — · SpatialUncertainty: alta (conceitual) · fonte: historiografia (A/B) · riscoEd: alto (tráfico/escravidão) · riscoLic: 0 · rel. 4B: contexto de AFR-03, AFR-05, SCENE-06.

**`region:beringia`** · Beríngia · variantes: ["ponte terrestre de Bering"] · TimeRange: Pleistoceno (emersa) · geometryStatus: **paleogeográfico**/**inferido** `PENDENTE_REFINAMENTO_ESPACIAL` · ModernCorr: estreito de Bering (atual) · SpatialUncertainty: alta · fonte: NOAA Paleo/geociências (A/B) · riscoEd: médio (povoamento das Américas — ver CS6) · riscoLic: 1 · rel. 4B: contexto de HIST-02 (`proc:povoamento-americas`).

**`region:pangeia`** · Pangeia · variantes: ["supercontinente Pangeia"] · TimeRange: ~335–175 Ma · geometryStatus: **paleogeográfico** (reconstrução GPlates) · ModernCorr: — (continentes atuais derivam dela) · SpatialUncertainty: alta (posições finas) · fonte: EarthByte/GPlates (A, CC BY) · riscoEd: baixo · riscoLic: 1 (Deep Time Maps proibido) · rel. 4B: é o `state:pangeia` (SCI-19) em forma de Region; `relacionado-a` `concept:supercontinente`.

**`region:rodinia`** · Rodinia · variantes: [] · TimeRange: ~1,1 Ga–~750 Ma · geometryStatus: **paleogeográfico** `PENDENTE_REFINAMENTO_ESPACIAL` (reconstrução de **alta** incerteza) · ModernCorr: — · SpatialUncertainty: muito alta · fonte: EarthByte/GPlates (A, CC BY) · riscoEd: baixo · riscoLic: 1 · rel. 4B: `relacionado-a` `concept:supercontinente` (predecessor de Pangeia).

**`region:sistema-terra-lua`** · Sistema Terra-Lua · variantes: [] · TimeRange: ~4,5 Ga–presente · geometryStatus: **não-geográfico** (astronômico; sem geometria de superfície) · ModernCorr: — · SpatialUncertainty: N/A · fonte: `source:nasa` (A) · riscoEd: baixo · riscoLic: 0 · rel. 4B: contexto de SCI-07 (`evt:formacao-lua`), `entity:lua`.

---

## 6. Revisão de reviewStatus e publicabilidade (Tarefa 6)

Os 70 itens da espinha/cena foram reclassificados em **quatro grupos** (classificação mecânica + correção editorial). A regra-mãe: **nenhum item sensível** (colonização, escravidão, povos indígenas, raça/ciência, ditadura, clima) é **publicável** sem a revisão humana aplicável; e nada com `reviewStatus ∈ {pending, legal-review, rejected}` aparece na simultaneidade.

| Grupo | Qtd. | Critério | Exemplos | Por que (ainda) não aparece na simultaneidade | O que falta p/ mudar de status |
|---|---|---|---|---|---|
| **1 · Publicável como gabarito** | **~33** | `approved`, baixo risco, sem pendência de refinamento | SCI-01 (Big Bang), SCI-13 (GOE), SCI-19 (Pangeia), SCI-21 (K-Pg), HIST-19 (Apollo), HIST-20 (WWW), HIST-14 (Rev. Científica), SCENE-01/07/08 (Lavoisier/Iluminismo) | **Aparecem** — são exibíveis | nada (já servem de gabarito) |
| **2 · Revisado conceitualmente, não exibível** | **~11** | conceito sólido, mas falta refinamento temporal/espacial ou confirmação de fonte | SCI-03 (1ªs estrelas), SCI-07 (Lua), SCI-10 (oceanos), SCI-14 (eucariontes), AFR-01 (Axum), SCENE-03/04 (Otomano/Qing 1789) | retidos por `PENDENTE_REFINAMENTO_*`/`PENDENTE_CONFIRMACAO_FONTE` — exibir número não confirmado seria inventar precisão | fechar a faixa/datum ou confirmar o asset da fonte |
| **3 · Pending por revisão humana** | **~23** | sensível (Leis 10.639/11.645; colonização, escravidão, indígenas, clima, 1492, causas de revolução) | HIST-13 (1492), HIST-15 (Rev. Francesa), HIST-18 (abolição), HIST-21 (clima), BR-01..05, AFR-04/05/06, IND-01/03/04, SCENE-05/06 | invariante de exibição: temas sensíveis não exibíveis sem revisão humana aplicável | revisão humana (histórica/pedagógica/vieses; oral quando indígena/afro) concluída |
| **4 · Bloqueado / legal-review / incompleto** | **~3** | bloqueio mais forte (jurídico ou raça+ciência) | **BR-07** (ditadura → `legal-review`, LGPD/pessoas vivas); **SCI-22/SCI-23** (gênero *Homo*/*sapiens* → bloqueados até revisão científica especializada por cruzarem **raça**) | risco jurídico (LGPD) ou risco de uso racista exige trava reforçada | parecer jurídico (BR-07); revisão científica especializada + nota antirracista (SCI-22/23) |

**Observações de correção sobre o 4B:**
- **BR-08** (Constituição 1988) estava `approved` com risco médio-alto (achado A5). Decisão: o **núcleo factual** (promulgação em 05/10/1988) permanece publicável (Grupo 1/2); qualquer **overlay de disputa contemporânea** entra como `pending`. Registrado.
- **Nenhum item está "incompleto"** no sentido de faltar campo — a auditoria confirmou os 25 campos em todos. "Bloqueado" aqui = trava editorial/jurídica, não registro faltante.
- **Itens científicos sensíveis** (evolução humana) **não** ganham passe livre por serem "ciência": o cruzamento com **raça** os mantém fora da exibição até revisão (Grupo 4), conforme Etapa 3.1.

---

## 7. Revisão dos ClaimSets (Tarefa 7)

Os 7 ClaimSets do 4B recebem id canônico `claimset:<tema>` (`pilotCode` CS1…CS7) e a decisão **ClaimSet × UncertaintyProfile**. Regra reafirmada: **mudanças climáticas NÃO é um ClaimSet entre consenso e negacionismo** — o ClaimSet só carrega **incerteza interna legítima** (cenários, projeções, sensibilidade).

| pilotCode | `claimset:` id | Tema | consensusStatus | ClaimSet ou UncertaintyProfile? | reviewStatus | Impacto na exibição |
|---|---|---|---|---|---|---|
| CS1 | `claimset:causas-revolucao-francesa` | Causas da Rev. Francesa | controvérsia historiográfica | **ClaimSet** (causas concorrentes legítimas, com peso) | pending | exibe pluralidade de causas; não elege "a" causa |
| CS2 | `claimset:1492-terminologia` | "descobrimento/invasão/encontro" | terminologia sensível | **ClaimSet** (termos com contexto) | pending (obrigatória) | apresenta termos lado a lado; nenhum como "neutro" |
| CS3 | `claimset:origem-da-vida` | Mecanismo da origem da vida | hipóteses concorrentes | **ClaimSet** (hipóteses); o **fato** "vida cedo ~3,5 Ga" sai do ClaimSet (consenso) | pending | hipóteses como hipóteses; fato separado |
| CS4 | `claimset:k-pg-causa` | K-Pg: impacto/vulcanismo/combinação | hipóteses concorrentes (convergindo p/ combinação) | **ClaimSet** + `UncertaintyProfile` no **peso** da combinação | pending | extinção (~66 Ma) é fato; causa é ClaimSet |
| CS5 | `claimset:clima-projecoes` | Clima: **incerteza interna de projeção** | consenso amplo (núcleo) **+** debate acadêmico (projeções) | **Núcleo = claim único de consenso + `UncertaintyProfile`**; ClaimSet **apenas** para sensibilidade/cenários | pending | **negacionismo fora**; o ClaimSet nunca opõe consenso × negação |
| CS6 | `claimset:povoamento-americas` | Cronologias/rotas do povoamento | hipóteses concorrentes | **ClaimSet** (cronologias e rotas) | pending (obrigatória) | cronologias abertas lado a lado; respeita perspectivas indígenas |
| CS7 | `claimset:evolucao-humana-fina` | Topologia/hibridização/origem do *sapiens* | debate acadêmico / hipóteses concorrentes | **Misto**: `UncertaintyProfile` para datas/topologia; **ClaimSet** só p/ modelos discretos (multirregional × africano-com-estrutura) | pending (obrigatória) | evolução = fato; detalhes = debate; **nunca** vira hierarquia |

**Posições SEM equivalência (reafirmadas, fora de todo ClaimSet):** criacionismo/desenho inteligente (CS3); negação do aquecimento ou de sua causa antrópica (CS5); pseudoarqueologia sem lastro (CS6); qualquer hierarquização racial (CS7); negação da violência colonial (CS2). Essas posições são **objetos rotulados como rejeitados**, nunca "lados".

**Decisão de vocabulário (CS5):** modelar o núcleo do clima como **um claim de consenso com `UncertaintyProfile`** (faixas), e usar `ClaimSet` **somente** para o debate interno de projeção. Isso impede estruturalmente a falsa equivalência consenso × negacionismo.

---

## 8. Relationship graph revisado (Tarefa 8)

Malha ampliada para conectar os novos `Concept`/`Entity`/`Place`/`Region`/`ClaimSet`/`Source` aos itens 4B, com as duas correções de referência aplicadas. Arestas afirmativas (`causou`/`influenciou`/`possibilitou`) **são claims** (têm evidência/confiança). `rel:` = id da aresta reificada; `Rn` = `pilotCode`.

| relId | sourceItem | relationshipType | targetItem | evidence | conf | reviewStatus | obs. |
|---|---|---|---|---|---|---|---|
| rel:R01 | SCI-12 `proc:fotossintese-oxigenica` | causou | SCI-13 `proc:goe` | registro material | alta | approved | cadeia obrigatória |
| rel:R03 | SCI-21 `evt:extincao-kpg` | causou | `entity:dinossauros-nao-avianos` (extinção) | registro material | alta | approved | fato; causa em `claimset:k-pg-causa` |
| rel:R11 | IND-02 `proc:contato-violencia-colonial` | causou | IND-03 `proc:resistencia-indigena` | documental | alta | pending | sensível |
| **rel:R21** | **IND-03** `proc:resistencia-indigena` | **predecessor-de** | **IND-04** `permanencia-indigena-contemporanea` | documental + oral | alta | pending | **corrige A1** (era IND-05) |
| **rel:R22** | **BR-08** `evt:constituicao-1988-brasil` | **relacionado-a** | **IND-04** `permanencia-indigena-contemporanea` | documental | alta | pending | **corrige A2** (era IND-05) |
| rel:R23 | `concept:tectonica-placas` | explica | SCI-19 `state:pangeia` | dado modelado | alta | approved | **Concept → State/Process** |
| rel:R24 | `concept:fotossintese-oxigenica` | explica | SCI-12 `proc:fotossintese-oxigenica` | observacional | alta | approved | Concept → Process (ideia × ocorrência) |
| rel:R25 | `concept:colonialismo` | explica | BR-04 `evt:chegada-portuguesa-brasil` | documental | alta | pending | Concept → Event (sensível) |
| rel:R26 | `concept:mudanca-climatica-antropica` | explica | HIST-21 `proc:mudancas-climaticas-modernas` | medição instrumental | alta | pending | Concept → Process |
| rel:R27 | `entity:cianobacterias` | participou-de | SCI-12 `proc:fotossintese-oxigenica` | registro material | alta | approved | **Entity → Process** |
| rel:R28 | `entity:dinossauros-nao-avianos` | afetado-por | SCI-21 `evt:extincao-kpg` | registro material | alta | approved | Entity → Event |
| rel:R29 | `entity:franca` | participou-de | HIST-15 `proc:revolucao-francesa` | documental | alta | pending | Entity → Process |
| rel:R30 | `entity:lavoisier` | participou-de | SCENE-01 `evt:lavoisier-traite-1789` | documental | alta | approved | Entity(pessoa) → Event |
| rel:R31 | `entity:povos-indigenas-brasil` | agente-de | IND-03 `proc:resistencia-indigena` | documental + oral | alta | pending | **agência**, não objeto passivo |
| rel:R32 | `place:chicxulub` | local-de | SCI-21 `evt:extincao-kpg` | inferido (geofísica) | alta | approved | **Place → Event** |
| rel:R33 | `place:paris` | local-de | HIST-15 `proc:revolucao-francesa` | documental | alta | pending | Place → Process |
| rel:R34 | `place:jebel-irhoud` | evidência-de | SCI-23 `evt:surgimento-homo-sapiens` | registro material | média-alta | legal/blocked | Place → Event (sensível, G4) |
| rel:R35 | `region:pangeia` | corresponde-a | SCI-19 `state:pangeia` | dado modelado | alta | approved | **Region → State** |
| rel:R36 | `region:franca-1789` | contém | SCENE-?(França 1789) / HIST-15 | documental | alta | pending | Region → State/Process |
| rel:R37 | `concept:modern-correspondence` | aplica-se-a | `region:capitania-minas-gerais` → MG | definição de modelo | alta | approved | **ModernCorrespondence → Region** |
| rel:R38 | `region:capitania-minas-gerais` | modernCorrespondence | `place:ouro-preto`/MG atual | documental | alta | pending | ModernCorr → Place |
| rel:R39 | `claimset:causas-revolucao-francesa` | qualifica | HIST-15 `proc:revolucao-francesa` | — (estrutural) | — | pending | **ClaimSet → Process** |
| rel:R40 | `claimset:k-pg-causa` | qualifica | SCI-21 `evt:extincao-kpg` | — (estrutural) | — | pending | ClaimSet → Event |
| rel:R41 | `source:nasa` | sustenta-claim | SCI-01 (claim principal) | — (proveniência) | alta | approved | **Source → Claim** |
| rel:R42 | `source:pbdb` | sustenta-claim | SCI-21 (claim principal) | — (proveniência) | alta | approved | Source → Claim |
| rel:R43 | `mediaasset:placeholder-pangeia` | ilustra | SCI-19 `state:pangeia` | natureLabel `reconstrução científica` | — | pending | **MediaAsset placeholder → Item** (não é evidência) |
| rel:R44 | `concept:guerra-fria` | contextualiza | HIST-19 `evt:apollo-11` | documental | alta | pending | sana nó referenciado |
| rel:R45 | HIST-16 `evt:inconfidencia-mineira` | contemporâneo-de | HIST-15 `proc:revolucao-francesa` | índice temporal | — | pending | cadeia obrigatória (mantida) |

> Arestas R02, R04–R10, R12–R20 do 4B permanecem válidas (não repetidas aqui). **Links inválidos removidos:** as duas referências a `IND-05` (substituídas por R21/R22). **MediaAsset** entra só como `ilustra`/`placeholder`, **nunca** `evidência-de` (mídia não é prova factual).

---

## 9. Gabarito ouro (Tarefa 9)

Doze itens eleitos como **gabarito ouro** — padrão para povoamentos futuros. Para cada: por que é gabarito · campos exemplares · pendências · padrão que ensina · publicável?

1. **SCI-01 `evt:big-bang`** — *por quê:* separa fato (expansão ~13,8 Ga) de hipótese (inflação) e trata negacionismo fora de ClaimSet. *Exemplar:* claimType, uncertaintyProfile, riscoEd. *Pendências:* nenhuma material. *Ensina:* consenso tipado como consenso. *Publicável:* **sim**.
2. **SCI-13 `proc:goe`** — *por quê:* cadeia causal (fotossíntese→GOE) com fonte; "como sabemos". *Exemplar:* rel[] causal, evidence. *Pendências:* atribuição causal fina (UncertaintyProfile). *Ensina:* causalidade como claim. *Publicável:* **sim**.
3. **SCI-19 `state:pangeia`** — *por quê:* reconstrução **rotulada** (não mapa observado), troca de globo. *Exemplar:* claimType `reconstrução modelada`, natureLabel, licença CC BY. *Pendências:* posições finas (alta incerteza). *Ensina:* reconstrução ≠ observação. *Publicável:* **sim** (rotulado).
4. **SCI-21 `evt:extincao-kpg`** — *por quê:* fato (extinção) separado de causa (ClaimSet). *Exemplar:* Place (Chicxulub), ClaimSet. *Pendências:* peso impacto×vulcanismo. *Ensina:* fato × atribuição. *Publicável:* **sim** (fato); causa via ClaimSet.
5. **HIST-15 `proc:revolucao-francesa`** — *por quê:* eventos como fato, causas como ClaimSet, âncora da cena 1789. *Exemplar:* `claimset:`, simultaneidade. *Pendências:* revisão histórica. *Ensina:* não fechar o mundo ao redor do foco. *Publicável:* **após revisão** (Grupo 3).
6. **HIST-16 `evt:inconfidencia-mineira`** — *por quê:* `modernCorrespondence` (território→MG) e contemporaneidade com a Rev. Francesa sem anacronismo. *Exemplar:* ModernCorrespondence, contemporâneo-de. *Pendências:* revisão Brasil. *Ensina:* simultaneidade Brasil↔mundo. *Publicável:* **após revisão**.
7. **HIST-10 `state:imperio-mali`** — *por quê:* África estrutural e protagonista (Lei 10.639), com **fontes orais** como evidência. *Exemplar:* evidenceLevel oral, riscoEd alto. *Pendências:* revisão + datum. *Ensina:* antieurocentrismo com rigor. *Publicável:* **após revisão**.
8. **HIST-02 `proc:povoamento-americas`** — *por quê:* cronologias concorrentes em ClaimSet, respeito a perspectivas indígenas (Lei 11.645). *Exemplar:* `claimset:`, uncertaintyProfile. *Pendências:* datas abertas. *Ensina:* incerteza sem inventar precisão. *Publicável:* **após revisão**.
9. **HIST-18 `evt:abolicao-brasil`** — *por quê:* tema crítico (escravidão) com dignidade e agência; "pessoas escravizadas". *Exemplar:* riscoEd crítico, linguagem. *Pendências:* revisão obrigatória. *Ensina:* sensibilidade Lei 10.639. *Publicável:* **após revisão** (Grupo 3).
10. **HIST-19 `evt:apollo-11`** — *por quê:* marco factual limpo, ligável a `concept:guerra-fria`. *Exemplar:* fonte A, rel contextual. *Pendências:* nenhuma material. *Ensina:* contexto sem perder o fato. *Publicável:* **sim**.
11. **HIST-21 `proc:mudancas-climaticas-modernas`** — *por quê:* consenso + `UncertaintyProfile` de projeção; negacionismo fora. *Exemplar:* CS5, claimType. *Pendências:* revisão; figuras recriadas. *Ensina:* incerteza sem falsa equivalência. *Publicável:* **após revisão**.
12. **Cena 1789 (SCENE-01..08 + HIST-15/16, AFR-03, IND-01/03)** — *por quê:* prova a simultaneidade global com Brasil/África/indígenas na cena. *Exemplar:* simultaneityBehavior, três paralelos. *Pendências:* itens sensíveis da cena pendentes. *Ensina:* o "mundo ao mesmo tempo". *Publicável:* **parcial** (núcleo factual sim; recortes sensíveis após revisão).

> **Uso interno × público:** itens 1–4 e 10 são gabarito **publicável**; 5–9, 11 e 12 são gabarito de **padrão** (referência interna até a revisão humana), valiosos para ensinar a estrutura mesmo antes de exibíveis.

---

## 10. Relatório de normalização (Tarefa 10)

1. **Problemas corrigidos:** 2 referências quebradas a `IND-05` (→ `IND-04`, em IND-03 e BR-08); prefixo `ent:`→`entity:` (Lavoisier); estilo de id de ClaimSet (`CS-0x`→`claimset:`+`pilotCode`); BR-08 `approved`→núcleo factual com overlay sensível em `pending`.
2. **Inconsistências ainda pendentes:** geometrias históricas/paleogeográficas marcadas `PENDENTE_REFINAMENTO_ESPACIAL` (França 1789, Capitania MG, América do Norte 1789, China Qing, Beríngia, Rodinia); datum do eixo temporal (1950 BP × J2000) **ainda em aberto** (decisão da Etapa 3, não resolvida aqui).
3. **Novos Concepts:** **26** (`concept:big-bang` … `concept:simultaneidade-historica` + `concept:guerra-fria`).
4. **Novas Entities:** **21** (20 da lista + `entity:lavoisier` normalizado), incluindo 2 grupos humanos sensíveis com regra Etapa 3.1.
5. **Novos Places/Regions:** **13 Places + 12 Regions** = 25, com `geometryStatus` explícito e sem geometria inventada.
6. **ClaimSets revisados:** **7**, com id canônico e decisão ClaimSet×UncertaintyProfile; CS5 (clima) blindado contra falsa equivalência.
7. **Relationship graph revisado:** +25 arestas novas (R21–R45) cobrindo Concept/Entity/Place/Region/ClaimSet/Source/MediaAsset→Item; 2 links inválidos removidos.
8. **Itens publicáveis:** ~33 (Grupo 1) + núcleo de ~11 do Grupo 2 quando o refinamento fechar.
9. **Itens pending:** ~23 (Grupo 3, sensíveis) + ~11 (Grupo 2, refinamento).
10. **Itens bloqueados:** ~3 (BR-07 `legal-review`; SCI-22/23 evolução humana até revisão científica especializada).
11. **Decisões de vocabulário:** confirmados prefixos canônicos (`evt/proc/state/concept/entity/place/region/claimset/rel/source`); separação `pilotCode` × `knowledgeItemId`; `status` (maturidade) × `reviewStatus` (exibição); `evidenceLevel` inclui `tradição/registro oral`; geometryStatus de 6 valores; `claimset:` substitui `CS-0x`.
12. **O que muda para a 4D:** o lote 4B vira **padrão operacional** — há gabarito ouro, nós de referência completos (Concept/Entity/Place/Region), grafo consistente e regras de publicabilidade. A 4D pode **povoar com método**, reusando esses nós como âncoras, sem reabrir modelagem.

---

## 11. Próximos passos para a Etapa 4D (Tarefa 11)

A Etapa 4C entregou **normalização e consolidação** (não expansão). A **Etapa 4D**, quando solicitada, deve:

1. **Povoar o segundo lote com método**, reusando os nós de referência (Concepts/Entities/Places/Regions) como âncoras — ainda **estrutural**, não enciclopédico, com os três paralelos crescendo junto.
2. **Concluir o fluxo de revisão humana** dos ~23 itens do Grupo 3 e dos bloqueados do Grupo 4 (parecer jurídico de BR-07; revisão científica/antirracista de SCI-22/23), aplicando os papéis da Etapa 3.1.
3. **Fechar os `PENDENTE_REFINAMENTO_ESPACIAL`** com geometrias validadas (Natural Earth histórico, GPlates) — sem inventar fronteiras.
4. **Reificar `Source` e `MediaAsset`** como nós próprios (`source:`/`mediaasset:`), ligando cada claim à sua proveniência e cada mídia ao seu `natureLabel`/licença-por-asset (primeira leva da camada 24).
5. **Validar o gabarito ouro em escala**: usar os 12 itens como teste de cada novo lote (todo item novo deve "passar no gabarito").
6. **Escalar à modelagem** (não resolver na 4D) as duas questões estruturais reabertas: `OceanographicState` dedicado? datum do eixo (1950 BP × J2000)?

**O que a 4D explicitamente NÃO deve fazer:** povoar milhares de eventos; escrever código; propor MVP/stack; desenhar UX final; entrar em currículo/professor/plano de aula; desenhar pipeline técnico; reabrir auditoria de fontes (Etapas 1/1.1), modelagem (Etapa 2) ou política editorial (Etapa 3.1).

---

*Documento de entrega da Etapa 4C, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A, 4B). Entrega a normalização e consolidação do lote-piloto P0: auditoria interna (2 referências quebradas corrigidas, prefixos e ids de ClaimSet normalizados), separação `pilotCode`×`knowledgeItemId`, 26 Concepts, 21 Entities e 25 Places/Regions completos, reclassificação de publicabilidade em 4 grupos, revisão dos 7 ClaimSets (clima blindado contra falsa equivalência), relationship graph ampliado e 12 itens de gabarito ouro. Não cria lote massivo, não escreve código, não propõe MVP, não define stack, não avança para UX final e não entra em currículo/professor/plano de aula. Próxima etapa, quando solicitada: Etapa 4D — povoamento metódico com os nós de referência como âncoras, conclusão de revisões e reificação de Source/MediaAsset.*
