# Constituição do Atlas do Tempo 3D

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Natureza:** documento de governança de **invariantes duros**. É a metade que **raramente muda** da separação ratificada em **PG7** (C1, D-C1.3). Reúne as propriedades sem as quais o produto deixa de ser o produto. Sua contraparte é o **Playbook Operacional** (procedimento, que muda com frequência).
**Estatuto:** **[NORMATIVO]** em sua totalidade. Cada artigo é vinculante para toda etapa que leia ou escreva o Knowledge Core e para todo passo de qualquer trilha.
**Origem:** redigido no Passo **C1.1** a partir da estrutura do **C1 §5.1**, sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14), a decisão de motor (Passo B1), a reificação (Passo B2) e a ratificação de governança (Passo C1).
**Versão:** **v1.1** — **Data:** 2026-06-21. (v1.0 → v1.1: errata de fidelidade — ver changelog.)

> **Nota de reconciliação (v1.1).** Esta versão foi conferida **palavra a palavra** contra o conteúdo de `revisao-politicas-regras-v0.html`, **recuperado verbatim** do chat de autoria *"Análise e status do projeto"* (onde o HTML foi originalmente gerado). A reconciliação **fechou** a pendência leve que o v1.0 carregava e revelou que o v1.0 **omitira** seis invariantes que já constavam do "piso epistêmico" daquele documento e já eram vinculantes no corpus (E11/E14/E1.1/E2). O v1.1 os **restaura** e afina a redação de PG1/PG2. **Nenhum artigo do v1.0 teve seu sentido alterado e nenhuma restrição genuinamente nova foi introduzida** — por isso é versão **menor** (errata), coerente com o Art. 18.

---

## Preâmbulo — o que esta Constituição é, e como ela muda

Esta Constituição existe para **impedir a deriva**: fixa o pequeno conjunto de propriedades que tornam o produto confiável, separadas do como-fazer que pode (e deve) evoluir. Ela é deliberadamente curta. **Tudo o que é procedimento, número, cadência, SLA ou checklist pertence ao Playbook, não aqui** (régua do Art. 17).

**Regra de emenda (Art. 18, antecipada):** um artigo só muda em **substância** por **versão maior**, com **justificativa forte**, e **nada muda em silêncio** — toda alteração é registrada no changelog. Correções de **fidelidade** (restaurar invariante já ratificado, corrigir transcrição) são versões **menores**, igualmente registradas.

**Desambiguação canônica (Art. 19, antecipada):** as propostas de **governança** são **PG1–PG7**; os princípios do **Knowledge Core** são **P1–P10** (Etapa 2). São sequências distintas. Onde este documento escreve "PG#", refere-se à governança; onde escreve "P#", refere-se ao Knowledge Core.

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

## TÍTULO III — Invariantes normativos da arquitetura ([N1]–[N5] e autoridade de fonte)

### Artigo 4 — Os cinco invariantes que constrangem qualquer motor e qualquer infraestrutura

**[NORMATIVO]** Independem de tecnologia. A propriedade vinculante é "**grafo tipado com proveniência por aresta**", **não** o produto de banco que a sustenta:

- **[N1] — Proveniência obrigatória por aresta e por claim.** Toda aresta **afirmativa** (`causou`, `influenciou`, `afetou`) e todo claim carregam `provenanceRef` + `reviewStatus`. Aresta afirmativa sem fonte A/B + `claimType` + confiança é **rejeitada**, nunca inserida à força (Etapa 2 §6.4).
- **[N2] — Assimetria autoritativo × derivado.** O autoritativo **nunca** depende de derivado para existir. Reconstruir todo índice/cache a partir do autoritativo é **sempre possível**; o caminho inverso é **proibido**. Daí: **"cache não é verdade"** e **"busca/embedding não é verdade"**.
- **[N3] — Isolamento físico de licença restritiva.** Geometrias e assets SA/ODbL/NC/proprietários **não** entram no índice/núcleo factual — vão para o `IsolatedLicenseStore` físico. Paleoposições são **sempre** rotuladas como reconstrução modelada.
- **[N4] — Índice ordena, não decide verdade.** O índice temporal (e qualquer índice) **ordena e seleciona**; **não** decide confiança nem publicabilidade — esses vêm **reidratados** do autoritativo a cada leitura.
- **[N5] — Camadas externas apontam por REF.** Conformidade, Planejamento, Matching, Saída e Experiência **apontam** ao núcleo por REF; **nenhuma** é gravada dentro do grafo factual.

*Origem:* Etapa 11; consolidados como [N1]–[N5] no Passo B1 §3.2. *Teste constitucional:* qualquer infraestrutura, cache, índice ou IA que "produza" claim, "promova" item não publicável a fato, ou "funda" dado restritivo no núcleo viola [N1]/[N2]/[N3].

### Artigo 5 — Wikidata é índice, não autoridade; toda fonte é classificada  ◄ *restaurado v1.1*

**[NORMATIVO]** Wikidata — e qualquer agregador, índice textual, busca ou *embedding* — serve para **encontrar e ligar** itens, **nunca** como **autoridade factual**. Toda fonte é **classificada** por confiabilidade, licença, tipo de dado e uso recomendado. Item recuperado por índice é **reidratado** com `claimType`/`confidence`/`reviewStatus` antes de exibir.

*Origem:* piso epistêmico do `revisao-politicas-regras-v0` (PG-piso, restaurado na reconciliação v1.1); Etapa 1/1.1; coerente com [N2]/[N4]. *Teste constitucional:* tratar Wikidata/embedding como autoridade, ou exibir item de índice sem reidratar, viola o artigo.

---

## TÍTULO IV — O regime epistêmico

### Artigo 6 — Invariante de exibição

**[NORMATIVO]** Item com `reviewStatus ∈ {pending, legal-review, rejected}` (ou `ingestionDecision = blocked`) **não é exibível nem consultável como fato** — em **nenhuma** vista, cache, índice, exportação ou pacote offline, para **nenhum** papel não-curatorial. Não entra em nenhum derivado exibível (`MomentResult`/`MatchSet`/`PedagogicalOutput`). O `gatingReason` é exibível **à curadoria**; ao público, o item simplesmente **não existe como fato**. **Publicação é função de estado, não de boa vontade.** Tópico sensível/controverso/NC/sem licença entra como `reviewStatus = pending` por padrão.

*Origem:* Etapa 1.1; Etapa 2 (regra de publicação); Etapa 11, invariante 9 e §7.5. *Teste constitucional:* o vazamento de um único item `pending`/`legal-review`/`rejected` como fato — inclusive na simultaneidade — é violação direta.

### Artigo 7 — Tipagem epistêmica obrigatória

**[NORMATIVO]** Nenhuma verdade existe fora de um `Claim` **tipado**. Todo claim importante carrega, de forma **exibível**: `claimType` (fato documentado, medição direta, inferência científica, estimativa, hipótese, controvérsia, interpretação historiográfica, reconstrução modelada, representação artística, aproximação didática), `confidenceLevel`, `evidenceLevel` e `UncertaintyProfile` (incerteza como **faixa**, não como "lados"). Claim de tipo `inferência`/`hipótese`/`controvérsia`/`reconstrução` **sem rótulo visível não publica**. Controvérsia legítima é modelada como `ClaimSet` (lados discretos, com pesos assimétricos); negacionismo **não** é um "lado" e fica fora do conjunto. **Nunca se inventa** precisão, geometria ou paleomapa.

*Origem:* Etapa 2 (P8; modelo claim-first); Etapa 3.1 (sete distinções contra falsa equivalência; `ClaimSet`/`consensusStatus`). *Teste constitucional:* exibir inferência/reconstrução como fato, ou dar a negacionismo o estatuto de "lado", viola este artigo.

### Artigo 8 — Forma muda, fato não  ◄ *restaurado v1.1*

**[NORMATIVO]** Linguagem, faixa etária, mídia e apresentação **se adaptam** ao público e ao canal; o `Claim` **não**. A adaptação ocorre sempre na **saída/experiência**, jamais alterando o claim do núcleo.

*Origem:* piso epistêmico do `revisao-politicas-regras-v0` (restaurado v1.1); Etapa 9/10 (adaptação na saída); Art. 2 (direção única). *Teste constitucional:* alterar um claim para "adequá-lo" a uma faixa ou a um canal viola o artigo — adapta-se a forma, nunca o fato.

### Artigo 9 — Regra de ouro: na dúvida, bloqueio/revisão  ◄ *restaurado v1.1*

**[NORMATIVO]** **Qualquer dúvida** de fonte, licença, claim, data, geometria, sensibilidade, acessibilidade ou privacidade resulta em **bloqueio/revisão — nunca em publicação automática.** Soberana sobre conveniência, prazo ou pressão.

*Origem:* regra de ouro do `revisao-politicas-regras-v0` (restaurada v1.1); Etapa 14. *Teste constitucional:* publicar automaticamente sob dúvida em qualquer dessas dimensões viola o artigo.

---

## TÍTULO V — Proveniência, licença e versionamento (reforçados pelo Passo B2)

### Artigo 10 — Proveniência por aresta/claim como chave estrangeira real

**[NORMATIVO]** A proveniência **deixa de ser convenção e é imposta no esquema** como **FK real**, sobre um backbone único de reificação (`entity_node`: uma IRI interna estável por entidade endereçável — item, aresta, claim, source, media_asset, claim_set). Uma **aresta afirmativa órfã** (sem proveniência) é **impossível de inserir**. Isto fecha estruturalmente o risco de [N1] virar convenção frágil.

*Origem:* Etapa 11 §4.2; Passo B2 (backbone `entity_node`; D-B2.2). *Teste constitucional:* se for possível inserir uma aresta afirmativa sem `provenanceRef`, o artigo foi violado.

### Artigo 11 — Isolamento físico de licença SA/ODbL/NC

**[NORMATIVO]** Conteúdo ShareAlike/ODbL/NC/proprietário vive em `IsolatedLicenseStore` **fisicamente separado** (esquema/bucket/namespace próprio, com fronteira de processo e de acesso), **desde já, mesmo vazio**. O núcleo factual **nunca** lê desse store para compor `Claim`. `MediaAsset` é primeira classe, com `natureLabel` + licença + partição; a relação asset→fato é aresta (separa o **asset**, governado pela licença, do **fato**, recodificável). Expressão NC **não** é exportada fora do permitido. **A licença governa a expressão/asset, nunca o fato recodificado.**

*Origem:* Etapa 1.1; Etapa 2 (fato × expressão); Etapa 11 §9; Passo B2 (P09/P11; D-B2.4); piso epistêmico do `revisao-politicas-regras-v0` (cláusula "licença governa expressão, não o fato" — confirmada na reconciliação v1.1). *Teste constitucional:* qualquer caminho de leitura do núcleo ao store isolado, qualquer fusão de dado restritivo no núcleo, ou tratar o fato recodificado como se fosse governado pela licença da expressão, viola o artigo.

### Artigo 12 — Correção não apaga o passado; degradação não remove o piso  ◄ *expandido v1.1*

**[NORMATIVO]** Corrigir é **aditivo e versionado**: ao mudar a fonte, o método ou a evidência, cria-se **nova versão** e a anterior é **deprecada, nunca apagada** (`supersedes`). A prova do que foi exibido é preservada (`DatasetSnapshot` imutável). Rollback opera por **depreciação + restauração** da versão anterior; nada é sobrescrito em massa.

**A degradação graciosa nunca remove o piso epistêmico** *(restaurado v1.1)*: a escada **3D → 2D → estático → offline → projetor** preserva sempre os rótulos de tipo/confiança/incerteza/atribuição; nenhuma vista "desliga" a honestidade epistêmica por desempenho ou estética.

*Origem:* Etapa 13 §9.10; Etapa 14 (rollback versionado); Passo B2 (D-B2.6); Etapa 10/11 (degradação graciosa); piso epistêmico do `revisao-politicas-regras-v0` (restaurado v1.1). *Teste constitucional:* apagar/sobrescrever versão anterior, perder a prova do exibido, ou uma vista degradada que suprima rótulo epistêmico, viola o artigo.

---

## TÍTULO VI — Qualidade e privacidade como piso  ◄ *título novo v1.1*

### Artigo 13 — QA bloqueia, não sugere; escala nunca reduz revisão  ◄ *restaurado v1.1*

**[NORMATIVO]** O controle de qualidade **bloqueia**; não "sugere" nem "recomenda com risco aceito". **Não existe `waived`/`override`**: um teste reprovado **barra**. E a **escala nunca reduz a profundidade de revisão** — se a capacidade é insuficiente, a admissão de novos itens **pausa** (intake throttling) e a escala recua; jamais se aprova em lote sem revisão.

*Origem:* piso epistêmico do `revisao-politicas-regras-v0` (restaurado v1.1); Etapa 14 (`qaGateResult` ∈ {pass, fail}; anti-Goodhart; intake throttling). Os **mecanismos operacionais** (o enum, SLAs, amostragem de auditoria) vivem no **Playbook §6**, sob este invariante. *Teste constitucional:* qualquer `waived`/`override`, ou aprovação em lote por falta de gente/tempo, viola o artigo.

### Artigo 14 — Minimização máxima de dados de menores  ◄ *restaurado v1.1*

**[NORMATIVO]** Para menores, vale a **minimização máxima de dados**: o núcleo **não** contém PII de aluno; o analytics mede **operação, não o aluno** (agregado, sem PII, jamais individualizado); dados de aluno **nunca** treinam modelo nem geram fato. É invariante de privacidade (LGPD/ECA) e condição de uso escolar.

*Origem:* piso epistêmico do `revisao-politicas-regras-v0` (restaurado v1.1); Etapa 11 (engenharia de privacidade); Etapa 14 (analytics agregado, sem PII). *Teste constitucional:* PII de menor no núcleo, analytics individualizado de aluno, ou uso de dado de aluno para treino/geração de fato, viola o artigo.

---

## TÍTULO VII — Governança ratificada (PG1, PG2)

### Artigo 15 — PG1: pronto = evidência  ◄ *afinado v1.1*

**[NORMATIVO]** "**Pronto**" (Definition of Done) significa **demonstrado por evidência**, nunca **afirmado**. Evidência é **≥ 1 artefato falsificável** que **mostra uma regra prendendo algo real** — um teste que passa, um registro povoado, uma saída renderizada, uma cena ponta-a-ponta, um esquema com *constraint*. Marcar uma caixa **não** é evidência. Afirmar "está pronto" sem artefato **não fecha** um passo.

*Origem:* Passo C1, D-C1.1 (ratificado); redação verbatim de PG1 conferida na reconciliação v1.1 ("≥ 1 artefato falsificável"); cadência evidence-first do `estado-atual-e-roteiro`; anti-Goodhart da Etapa 14. *Vigência:* desde C1.

### Artigo 16 — PG2: fatias como instrumento  ◄ *afinado v1.1*

**[NORMATIVO]** A **fatia vertical fina** é a unidade de progresso e de prova. Uma capacidade se prova construindo-a **ponta-a-ponta** (mesmo descartável), não escrevendo mais especificação. A fatia é **instrumento, não produto**: serve para **ensinar o que falta** e **destravar a próxima decisão com evidência**.

**Guarda (verbatim de PG2, confirmada v1.1):** a fatia **não pode virar produto nem entrar no Knowledge Core** — é *throwaway* por contrato (sem banco/auth, fiel aos dados, descartável). Vigiar scope creep.

*Origem:* Passo C1, D-C1.2 (ratificado); redação verbatim de PG2 conferida na reconciliação v1.1; precedentes — fatia de 1789, Incremento 2 GOE/K-Pg, Passo B1. *Vigência:* desde C1.

---

## TÍTULO VIII — Da emenda e da relação com o Playbook

### Artigo 17 — Régua de alocação (o que é constitucional)

**[NORMATIVO]** Uma cláusula pertence a esta Constituição se, e somente se, responde "Constituição" na régua:

| Pergunta | Vai para |
|---|---|
| O produto deixa de ser o produto se isto for violado? | **Constituição** |
| Isto pode melhorar/mudar sem ferir nenhuma propriedade do produto? | **Playbook** |
| Isto é um número, um SLA, uma cadência, um checklist? | **Playbook** |
| Isto é uma propriedade epistêmica, de proveniência, de licença, de exibição, de qualidade ou de privacidade? | **Constituição** |

*Origem:* Passo C1 §5.2 (linha de qualidade/privacidade explicitada na reconciliação v1.1, para acomodar os Arts. 13–14).

### Artigo 18 — Regra de emenda

**[NORMATIVO]** Esta Constituição muda em **substância** **apenas por versão maior** (v2.0, v3.0…), com **justificativa forte** registrada. **Correções de fidelidade** — restaurar invariante já ratificado, corrigir transcrição, afinar redação sem alterar sentido — são versões **menores** (v1.1, v1.2…). Em ambos os casos, **nada muda em silêncio:** toda alteração entra no changelog (`versão | data | o que mudou | por quê | documento`). Procedimento que se descubra ser propriedade-que-define-o-produto **migra para cá** por emenda; cláusula daqui que se descubra ser mero como-fazer **migra para o Playbook** por emenda — sempre com registro.

*Origem:* Passo C1, D-C1.3; distinção fidelidade × substância explicitada na reconciliação v1.1 (que é, ela própria, uma versão menor).

### Artigo 19 — Desambiguação de numeração

**[NORMATIVO]** **Governança = PG1–PG7; Knowledge Core = P1–P10.** A nomenclatura canônica das propostas de governança é **PG#**. O choque de numeração com os princípios do Knowledge Core fica **registrado, não silenciado**.

*Origem:* Passo C1, D-C1.5.

---

## Changelog

| Versão | Data | O que mudou | Por quê | Documento |
|---|---|---|---|---|
| **v1.1** | 2026-06-21 | **Errata de fidelidade** após reconciliação verbatim contra `revisao-politicas-regras-v0.html` (recuperado do chat de autoria). **Restaurados** seis invariantes do piso epistêmico omitidos no v1.0: Wikidata-índice-não-autoridade (Art. 5), forma-muda-fato-não (Art. 8), regra de ouro na-dúvida-bloqueio (Art. 9), degradação-não-remove-o-piso (expansão do Art. 12), QA-bloqueia/escala-não-reduz-revisão (Art. 13) e minimização-máxima-de-menores (Art. 14). **Afinados** PG1 (Art. 15, "≥ 1 artefato falsificável") e PG2 (Art. 16, guarda *throwaway*/não-entra-no-KC) com a redação verbatim. **Reorganização** em 19 artigos (novo Título VI — qualidade/privacidade). Régua (Art. 17) e regra de emenda (Art. 18) ganharam a linha qualidade/privacidade e a distinção fidelidade × substância. | A reconciliação revelou que o v1.0 não transcrevera invariantes já ratificados no piso do documento de origem e já vinculantes em E11/E14/E1.1/E2. Restaurá-los é fidelidade, não substância nova — daí versão menor (Art. 18). | Constituição |
| **v1.1** | 2026-06-21 | **Pendência resolvida:** a reconciliação verbatim de PG1–PG7 (aberta no v1.0) está **fechada** — o conteúdo normativo foi recuperado e conferido. Resíduo **não-normativo** (CSS original, cabeçalho/diagnóstico de abertura do HTML, a linha "Ganho" do cartão PG7) não foi recuperado e **não afeta** a governança. | Encerrar honestamente a pendência registrada no v1.0. | Constituição |
| | | **Mapa de renumeração v1.0 → v1.1** (referências externas ao v1.0 devem usar este mapa): Art.1→1, 2→2, 3→3, 4→4, **(novo 5)**, 5→6, 6→7, **(novo 8)**, **(novo 9)**, 7→10, 8→11, 9→12, **(novo 13)**, **(novo 14)**, 10→15, 11→16, 12→17, 13→18, 14→19. | Preservar rastreabilidade após a reorganização. | Constituição |
| **v1.0** | 2026-06-21 | Criação da Constituição como documento próprio, a partir da estrutura do C1 §5.1 (Títulos I–VII; tese, separação de camadas, P1–P10, [N1]–[N5], invariante de exibição, tipagem epistêmica, proveniência como FK, isolamento de licença, depreciação-não-apaga, PG1, PG2, régua, regra de emenda, desambiguação). | Executar o Passo C1.1. | Constituição |

---

*Documento de governança do Passo C1.1 (v1.1 — errata de fidelidade), sob a baseline v1.0 (Etapa 0), a modelagem do Knowledge Core (Etapa 2), a política editorial (Etapa 3.1), o datum temporal (Etapa 3Z), a arquitetura técnica (Etapa 11), o pipeline (Etapa 13), a operação/governança (Etapa 14), e os Passos B1, B2 e C1. Reconcilia a Constituição contra o texto verbatim recuperado de `revisao-politicas-regras-v0.html`, restaura os invariantes de piso omitidos no v1.0 e afina PG1/PG2 — sem alterar o sentido de nenhum artigo do v1.0 e sem introduzir restrição nova (por isso versão menor, Art. 18). Não reabre nenhuma etapa, não ratifica PG3/PG4/PG5/PG6 (diferidos — ver Playbook), não escreve código, não decide dados. A pendência de reconciliação verbatim está **encerrada**; resíduo não-normativo (CSS, cabeçalho, uma linha de PG7) não afeta a governança. Supersede o v1.0.*
