# Constituição do Atlas do Tempo 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** documento de governança de **invariantes duros**. É a metade que **raramente muda** da separação ratificada em **PG7** (C1, D-C1.3). Reúne as propriedades sem as quais o produto deixa de ser o produto. Sua contraparte é o **Playbook Operacional** (procedimento, que muda com frequência).
**Estatuto:** **[NORMATIVO]** em sua totalidade. Cada artigo é vinculante para toda etapa que leia ou escreva o Knowledge Core e para todo passo de qualquer trilha.
**Origem:** redigido no Passo **C1.1** a partir da estrutura do **C1 §5.1**, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14), a decisão de motor (Passo B1), a reificação (Passo B2) e a ratificação de governança (Passo C1).
**Versão:** v1.0 — **Data:** 2026-06-21.

> **Nota de insumo (honestidade — herdada do C1, R-C1.2/§9).** Esta Constituição popula seus artigos pela **substância ratificada no C1**, reconstruída de múltiplas referências convergentes do corpus. O **texto verbatim** das propostas de governança vive em `revisao-politicas-regras-v0.html`, **arquivo mantido fora do conhecimento do projeto** e **não acessível** no chat que redigiu este documento (confirmado: ausente do diretório do projeto, dos uploads e de todo o ambiente). A **reconciliação palavra a palavra de PG1–PG7 contra o HTML** segue **pendente** e está registrada no changelog; se ao anexar o HTML houver divergência, a substância de PG1/PG2 aqui é ajustada por emenda (Art. 13).

---

## Preâmbulo — o que esta Constituição é, e como ela muda

Esta Constituição existe para **impedir a deriva**: fixa o pequeno conjunto de propriedades que tornam o produto confiável, separadas do como-fazer que pode (e deve) evoluir. Ela é deliberadamente curta. **Tudo o que é procedimento, número, cadência, SLA ou checklist pertence ao Playbook, não aqui** (régua do Art. 12).

**Regra de emenda (Art. 13, antecipada):** um artigo só muda por **versão maior**, com **justificativa forte**, e **nada muda em silêncio** — toda alteração é registrada no changelog. A facilidade de iterar é uma virtude do Playbook; a estabilidade é a virtude desta Constituição.

**Desambiguação canônica (Art. 14, antecipada):** as propostas de **governança** são **PG1–PG7**; os princípios do **Knowledge Core** são **P1–P10** (Etapa 2). São sequências distintas. Onde este documento escreve "PG#", refere-se à governança; onde escreve "P#", refere-se ao Knowledge Core.

---

## TÍTULO I — Natureza e tese

### Artigo 1 — A tese (atlas tridimensional do espaço-tempo do conhecimento)

**[NORMATIVO]** O produto é um **atlas tridimensional do espaço-tempo do conhecimento**: para um **ponto no espaço** + um **instante no tempo** + uma **lente de domínio**, ele devolve **o que se sabe ali**, com fonte e nível de confiança. "O que acontecia no mundo neste momento?" é uma **lente** (eventos/história) sobre esse atlas, não o todo.

O **esqueleto é o tempo**; sobre ele aplica-se a **lente de domínio**; só então vêm os **eventos do domínio** — sempre nessa ordem. **Todo instante é atravessado por todas as lentes**; a lente **filtra** o instante, não troca de instante. **Lente vazia é informação** (p.ex., a lente história em 2,4 Ga retorna vazio, e isso é um dado).

*Origem:* Etapa 0; Decisão de re-centragem da tese. *Teste constitucional:* se o sistema passar a nascer da grade curricular, ou se uma lente deixar de poder retornar vazio honestamente, a tese foi violada.

### Artigo 2 — Separação de camadas e direção única de dependência

**[NORMATIVO]** O sistema tem **seis camadas** que **nunca se fundem**: (1) **Knowledge Core** universal; (2) **Conformidade educacional brasileira**; (3) **Planejamento do professor/escola**; (4) **Motor de correspondência** (Matching); (5) **Saída pedagógica**; (6) **Experiência/UX**. O conhecimento é universal; o currículo organiza o uso; o professor define o foco; a experiência mantém o mundo navegável.

**A dependência aponta sempre para o núcleo:** Experiência → Saída → Matching → Planejamento → Conformidade → **Knowledge Core** → Fontes/Proveniência. O núcleo **não tem nenhuma referência de saída** para as camadas externas. Apagar qualquer camada externa **não deixa campo órfão** no núcleo. As camadas externas consultam o núcleo **por REF**, aplicando seus filtros (BNCC, recorte regional, faixa etária) **por fora**.

*Origem:* Prompt-mestre (item 4 e item 12); Etapa 2 §10; Etapa 11 (cadeia de camadas); [N5] (Art. 4). *Teste constitucional:* se uma camada externa for gravada dentro do grafo factual, ou se o núcleo passar a referenciar BNCC/série/aula, a separação foi violada.

---

## TÍTULO II — Princípios do Knowledge Core (P1–P10)

### Artigo 3 — Os dez princípios do núcleo

**[NORMATIVO]** O Knowledge Core obedece aos dez princípios da Etapa 2 (§1.2), aqui incorporados como invariantes:

| # | Princípio | Conteúdo vinculante |
|---|---|---|
| **P1** | Universalidade | O núcleo modela conhecimento, não currículo. Nenhuma entidade do núcleo referencia BNCC, série, disciplina ou aula. A indexação curricular é anotação externa (Etapa 6), nunca campo do núcleo. |
| **P2** | Independência da BNCC | A BNCC é consumidora do núcleo, não componente dele. Remover a BNCC inteira não muda um único campo do núcleo. |
| **P3** | Rastreabilidade por fonte | Toda entidade factual carrega `ProvenanceMetadata`. Não existe "entidade sem proveniência". |
| **P4** | Orientação a claim | A unidade atômica de verdade é o `Claim` tipado e fonteado, não o parágrafo de texto. Narrativa é camada derivada que **cita** claims. |
| **P5** | Temporalidade nativa | Todo item posicionável no tempo carrega `TimeRange` num eixo único de Ga a um dia. O tempo é índice de primeira classe. |
| **P6** | Geoespacialidade nativa | Todo item localizável carrega geometria versionada no tempo e correspondência com o território atual. O espaço é índice de primeira classe. |
| **P7** | Simultaneidade emergente | Por P5 + P6, "o que acontecia no mundo neste momento?" é a **interseção** dos índices temporal e espacial — não um módulo à parte. |
| **P8** | Incerteza tipada | Todo claim carrega `ClaimType`, `ConfidenceLevel`, `EvidenceLevel` e `UncertaintyProfile`. Fato, medição, inferência, estimativa, hipótese, controvérsia, interpretação historiográfica, reconstrução e representação são **valores distintos e exibíveis**. |
| **P9** | Tempo profundo e histórico no mesmo eixo | Idade geológica (Ma/Ga) e data calendárica (BCE/CE) coexistem num eixo canônico ordenável, com precisão e incerteza próprias de cada regime. |
| **P10** | Pronto para estados e mídia | O núcleo modela **estados** de sistemas (atmosfera, tectônica, clima, civilização, economia…) ao longo do tempo, e **mídia** com regime de licença isolado por asset. |

*Origem:* Etapa 2 §1.2. *Teste constitucional:* a violação de qualquer P# desnatura o núcleo; P1/P2 em especial são o que impede a contaminação curricular.

---

## TÍTULO III — Invariantes normativos da arquitetura ([N1]–[N5])

### Artigo 4 — Os cinco invariantes que constrangem qualquer motor e qualquer infraestrutura

**[NORMATIVO]** Independem de tecnologia. A propriedade vinculante é "**grafo tipado com proveniência por aresta**", **não** o produto de banco que a sustenta:

- **[N1] — Proveniência obrigatória por aresta e por claim.** Toda aresta **afirmativa** (`causou`, `influenciou`, `afetou`) e todo claim carregam `provenanceRef` + `reviewStatus`. Aresta afirmativa sem fonte A/B + `claimType` + confiança é **rejeitada**, nunca inserida à força (Etapa 2 §6.4).
- **[N2] — Assimetria autoritativo × derivado.** O autoritativo **nunca** depende de derivado para existir. Reconstruir todo índice/cache a partir do autoritativo é **sempre possível**; o caminho inverso é **proibido**. Daí: **"cache não é verdade"** e **"busca/embedding não é verdade"**.
- **[N3] — Isolamento físico de licença restritiva.** Geometrias e assets SA/ODbL/NC/proprietários **não** entram no índice/núcleo factual — vão para o `IsolatedLicenseStore` físico. Paleoposições são **sempre** rotuladas como reconstrução modelada.
- **[N4] — Índice ordena, não decide verdade.** O índice temporal (e qualquer índice) **ordena e seleciona**; **não** decide confiança nem publicabilidade — esses vêm **reidratados** do autoritativo a cada leitura.
- **[N5] — Camadas externas apontam por REF.** Conformidade, Planejamento, Matching, Saída e Experiência **apontam** ao núcleo por REF; **nenhuma** é gravada dentro do grafo factual.

*Origem:* Etapa 11; consolidados como [N1]–[N5] no Passo B1 §3.2. *Teste constitucional:* qualquer infraestrutura, cache, índice ou IA que "produza" claim, "promova" item não publicável a fato, ou "funda" dado restritivo no núcleo viola [N1]/[N2]/[N3].

---

## TÍTULO IV — O regime epistêmico

### Artigo 5 — Invariante de exibição

**[NORMATIVO]** Item com `reviewStatus ∈ {pending, legal-review, rejected}` (ou `ingestionDecision = blocked`) **não é exibível nem consultável como fato** — em **nenhuma** vista, cache, índice, exportação ou pacote offline, para **nenhum** papel não-curatorial. Não entra em nenhum derivado exibível (`MomentResult`/`MatchSet`/`PedagogicalOutput`). O `gatingReason` é exibível **à curadoria**; ao público, o item simplesmente **não existe como fato**. **Publicação é função de estado, não de boa vontade.** Tópico sensível/controverso/NC/sem licença entra como `reviewStatus = pending` por padrão.

*Origem:* Etapa 1.1; Etapa 2 (regra de publicação); Etapa 11, invariante 9 e §7.5. *Teste constitucional:* o vazamento de um único item `pending`/`legal-review`/`rejected` como fato — inclusive na simultaneidade — é violação direta.

### Artigo 6 — Tipagem epistêmica obrigatória

**[NORMATIVO]** Nenhuma verdade existe fora de um `Claim` **tipado**. Todo claim importante carrega, de forma **exibível**: `claimType` (fato documentado, medição direta, inferência científica, estimativa, hipótese, controvérsia, interpretação historiográfica, reconstrução modelada, representação artística, aproximação didática), `confidenceLevel`, `evidenceLevel` e `UncertaintyProfile` (incerteza como **faixa**, não como "lados"). Claim de tipo `inferência`/`hipótese`/`controvérsia`/`reconstrução` **sem rótulo visível não publica**. Controvérsia legítima é modelada como `ClaimSet` (lados discretos, com pesos assimétricos); negacionismo **não** é um "lado" e fica fora do conjunto. **Nunca se inventa** precisão, geometria ou paleomapa.

*Origem:* Etapa 2 (P8; modelo claim-first); Etapa 3.1 (sete distinções contra falsa equivalência; `ClaimSet`/`consensusStatus`). *Teste constitucional:* exibir inferência/reconstrução como fato, ou dar a negacionismo o estatuto de "lado", viola este artigo.

---

## TÍTULO V — Proveniência, licença e versionamento (reforçados pelo Passo B2)

### Artigo 7 — Proveniência por aresta/claim como chave estrangeira real

**[NORMATIVO]** A proveniência **deixa de ser convenção e é imposta no esquema** como **FK real**, sobre um backbone único de reificação (`entity_node`: uma IRI interna estável por entidade endereçável — item, aresta, claim, source, media_asset, claim_set). Uma **aresta afirmativa órfã** (sem proveniência) é **impossível de inserir**. Isto fecha estruturalmente o risco de [N1] virar convenção frágil.

*Origem:* Etapa 11 §4.2; Passo B2 (backbone `entity_node`; D-B2.2). *Teste constitucional:* se for possível inserir uma aresta afirmativa sem `provenanceRef`, o artigo foi violado.

### Artigo 8 — Isolamento físico de licença SA/ODbL/NC

**[NORMATIVO]** Conteúdo ShareAlike/ODbL/NC/proprietário vive em `IsolatedLicenseStore` **fisicamente separado** (esquema/bucket/namespace próprio, com fronteira de processo e de acesso), **desde já, mesmo vazio**. O núcleo factual **nunca** lê desse store para compor `Claim`. `MediaAsset` é primeira classe, com `natureLabel` + licença + partição; a relação asset→fato é aresta (separa o **asset**, governado pela licença, do **fato**, recodificável). Expressão NC **não** é exportada fora do permitido.

*Origem:* Etapa 1.1; Etapa 2 (fato × expressão); Etapa 11 §9; Passo B2 (P09/P11; D-B2.4). *Teste constitucional:* qualquer caminho de leitura do núcleo ao store isolado, ou qualquer fusão de dado restritivo no núcleo, viola o artigo.

### Artigo 9 — Correção não apaga o passado

**[NORMATIVO]** Corrigir é **aditivo e versionado**: ao mudar a fonte, o método ou a evidência, cria-se **nova versão** e a anterior é **deprecada, nunca apagada** (`supersedes`). A prova do que foi exibido é preservada (`DatasetSnapshot` imutável). Rollback opera por **depreciação + restauração** da versão anterior; nada é sobrescrito em massa.

*Origem:* Etapa 13 §9.10; Etapa 14 (rollback versionado); Passo B2 (D-B2.6, herdado da E13). *Teste constitucional:* apagar ou sobrescrever uma versão anterior — ou perder a prova do que foi exibido — viola o artigo.

---

## TÍTULO VI — Governança ratificada (PG1, PG2)

### Artigo 10 — PG1: pronto = evidência

**[NORMATIVO]** "**Pronto**" (Definition of Done) significa **demonstrado por evidência**, nunca **afirmado**. Evidência é um **artefato, fatia ou verificação** que **exibe** a propriedade reivindicada — um protótipo navegável, um esquema com *constraint*, uma cena ponta-a-ponta, um teste. Marcar uma caixa **não** é evidência. Afirmar "está pronto" sem artefato **não fecha** um passo.

*Origem:* Passo C1, D-C1.1 (ratificado); cadência evidence-first do `estado-atual-e-roteiro`; anti-Goodhart da Etapa 14. *Vigência:* desde C1.

### Artigo 11 — PG2: fatias como instrumento

**[NORMATIVO]** A **fatia vertical fina** é a unidade de progresso e de prova. Uma capacidade se prova construindo-a **ponta-a-ponta** (mesmo descartável), não escrevendo mais especificação. A fatia é **instrumento, não produto**: serve para **ensinar o que falta** e **destravar a próxima decisão com evidência**.

*Origem:* Passo C1, D-C1.2 (ratificado); precedentes — fatia de 1789 (gating epistêmico), Incremento 2 GOE/K-Pg (multidomínio no tempo profundo), Passo B1 (motor decidido com padrões reais do protótipo). *Vigência:* desde C1.

---

## TÍTULO VII — Da emenda e da relação com o Playbook

### Artigo 12 — Régua de alocação (o que é constitucional)

**[NORMATIVO]** Uma cláusula pertence a esta Constituição se, e somente se, responde "Constituição" na régua:

| Pergunta | Vai para |
|---|---|
| O produto deixa de ser o produto se isto for violado? | **Constituição** |
| Isto pode melhorar/mudar sem ferir nenhuma propriedade do produto? | **Playbook** |
| Isto é um número, um SLA, uma cadência, um checklist? | **Playbook** |
| Isto é uma propriedade epistêmica, de proveniência, de licença ou de exibição? | **Constituição** |

*Origem:* Passo C1 §5.2.

### Artigo 13 — Regra de emenda

**[NORMATIVO]** Esta Constituição muda **apenas por versão maior** (v2.0, v3.0…), com **justificativa forte** registrada. **Nada muda em silêncio:** toda alteração entra no changelog (`versão | data | o que mudou | por quê | documento`). Procedimento que se descubra ser, na verdade, propriedade-que-define-o-produto **migra para cá** por emenda; cláusula daqui que se descubra ser mero como-fazer **migra para o Playbook** por emenda — em ambos os casos com registro. A iteração rotineira pertence ao Playbook; esta Constituição privilegia a estabilidade.

*Origem:* Passo C1, D-C1.3.

### Artigo 14 — Desambiguação de numeração

**[NORMATIVO]** **Governança = PG1–PG7; Knowledge Core = P1–P10.** A nomenclatura canônica das propostas de governança é **PG#**. O choque de numeração com os princípios do Knowledge Core fica **registrado, não silenciado**.

*Origem:* Passo C1, D-C1.5.

---

## Changelog

| Versão | Data | O que mudou | Por quê | Documento |
|---|---|---|---|---|
| **v1.0** | 2026-06-21 | Criação da Constituição como documento próprio, a partir da estrutura do C1 §5.1. Populados os Títulos I–VII: tese (Art. 1), separação de camadas + direção única (Art. 2), P1–P10 do Knowledge Core (Art. 3), [N1]–[N5] (Art. 4), invariante de exibição (Art. 5), tipagem epistêmica (Art. 6), proveniência por aresta como FK (Art. 7), isolamento de licença SA/ODbL/NC (Art. 8), depreciação-não-apaga (Art. 9), PG1 (Art. 10) e PG2 (Art. 11) ratificados, régua de alocação (Art. 12), regra de emenda (Art. 13) e desambiguação PG/P (Art. 14). | Executar o Passo C1.1: transformar a estrutura ratificada no C1 em documento de governança vigente, iniciando o registro versionado. | Constituição |
| — | — | **Pendência leve registrada:** reconciliação **verbatim** de PG1–PG7 contra `revisao-politicas-regras-v0.html`. O HTML é arquivo fora do conhecimento do projeto e não estava acessível no chat de redação. Quando anexado, conferir PG1/PG2 palavra a palavra contra os Arts. 10–11; havendo divergência, emendar (Art. 13) e registrar aqui. | Honestidade de insumo (herdada de C1, R-C1.2/§9): ratificou-se pela substância, não pelo texto literal. | Constituição |

---

*Documento de governança do Passo C1.1, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14), e os Passos B1 (motor), B2 (reificação) e C1 (ratificação). Redige a Constituição a partir da estrutura do C1 §5.1 e popula seus invariantes. Não altera nenhum invariante do corpus (apenas os reúne e fixa), não reabre nenhuma etapa, não ratifica PG3/PG4/PG5/PG6 (diferidos — ver Playbook), não escreve código, não decide dados, não redige o Playbook (documento irmão) nem o handoff (passo de fechamento). Pendência leve carregada: reconciliação verbatim de PG1–PG7 contra `revisao-politicas-regras-v0.html`, a executar quando o arquivo for anexado.*
