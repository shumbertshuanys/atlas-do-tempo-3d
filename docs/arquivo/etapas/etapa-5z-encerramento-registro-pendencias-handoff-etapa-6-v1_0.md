# Etapa 5Z — Encerramento da Etapa 5 e Registro Geral de Pendências

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Encerramento da **Etapa 5** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z) e a função `WhatWasHappeningAtMoment` (Etapa 5) · 12/06/2026
**Natureza desta etapa.** Documento de **encerramento, consolidação e controle de pendências**. Serve de **ponte** entre a Etapa 5 (função de consulta espaço-temporal) e a Etapa 6 (Brazilian Education Compliance Layer). Conforme solicitado, **não** resolve pendências, **não** cria cena nova, **não** povoa conteúdos, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo detalhado/professor/plano de aula, **não** desenha pipeline técnico completo, **não** reabre auditoria de fontes, **não** reabre política editorial e **não** reabre a modelagem do Knowledge Core (salvo para **registrar** pendências). Também **não** cria prompts da Etapa 6 dentro do documento.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores. Blocos ```txt``` são dicionário conceitual, nunca código. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5).

---

## Sumário

1. Resumo executivo da Etapa 5
2. Artefatos aprovados da Etapa 5
3. Decisões aprovadas
4. Padrões vinculantes para etapas futuras
5. Backlog geral de pendências estruturais
6. Classificação das pendências por urgência
7. O que NÃO bloqueia a Etapa 6
8. O que a Etapa 6 deve consumir
9. Fronteiras da Etapa 6
10. Riscos seguintes
11. Handoff para a Etapa 6
12. Próximos passos

---

## 1. Resumo executivo da Etapa 5 (Tarefa 1)

**Objetivo.** Generalizar a função central do produto — *"O que acontecia no mundo neste momento?"* — de cenas-instância (1789, 2,4 Ga, 66 Ma) para uma **capacidade reutilizável** do Knowledge Core, definindo conceitualmente como o sistema consulta tempo, espaço, camadas, claims, States, relações, publicabilidade e incerteza, e **produz** respostas e cenas reutilizáveis.

**O que foi entregue.** A capacidade `WhatWasHappeningAtMoment`, com: 13 tipos de consulta; o objeto de entrada `MomentQuery`; o objeto de saída `MomentResult`; as regras de normalização temporal (eixo canônico) e espacial (quatro mecanismos de geometria); seleção/ranqueamento com categorias de resultado; publicabilidade e gating (5 níveis + `gatingReason`); regras de anacronismo e anti-falsa-equivalência (`anachronismWarnings`/`equivalenceWarnings`); a mecânica de geração de `Scene` candidate; oito padrões de resposta por tipo de consulta; e dez modos de resultado.

**Decisão central.** A função é uma **capacidade de leitura do Knowledge Core**, não uma feature de UI nem um módulo de escrita. É a materialização da propriedade emergente já fixada na Etapa 2 (P7 / D4·A6): a simultaneidade é a **interseção dos índices temporal e espacial sobre claims tipados**.

**Como generaliza as cenas-gabarito.** As cenas 4D/4E/4G deixam de ser exercícios manuais e passam a ser **instâncias** do que a função produz: o mesmo motor de consulta gera, sob demanda, o corte de simultaneidade (histórico, profundo sem evento, profundo com evento) que antes era escrito à mão. Não se cria mais cena como exercício; define-se **como o sistema as produz**.

**Por que é leitura, não escrita.** A função **nunca** cria `KnowledgeItem`, `Claim`, `State`, `Relationship` ou `Source`, **não** altera `reviewStatus` e **não** publica nada automaticamente. Toda criação/edição/aprovação de conteúdo permanece sob curadoria humana (Etapas 4x/13). Isso preserva o invariante claim-first (Etapa 2) e o portão de ingestão (Etapa 1.1).

**Como usa `MomentQuery`.** Recebe um objeto único de entrada (texto livre, modo de consulta, foco, entradas temporal/espacial brutas, filtros de camada/confiança/claimType, modo de publicabilidade, faixa etária, modo de comparação, flags de incerteza/fontes/mídia, modo de saída) e infere/normaliza o que falta, **preservando o bruto**.

**Como retorna `MomentResult`.** Devolve `normalizedTimeRange`/`normalizedSpatialScope`, foco, itens principais, simultâneos, States de fundo, `ClaimSets`, `UncertaintyProfiles`, itens ocultos, sínteses de fonte/confiança, avisos de anacronismo/equivalência, `publicabilityStatus`+`gatingReason`, uma `Scene` candidata (quando couber) e sugestões de navegação. A saída alimenta timeline, globo/mapa, dossiê, `Scene` v1.1, comparação antes/depois e navegação.

**Como gera `Scene` candidate.** Quando o recorte tem coesão suficiente e o `outputMode` pede cena/dossiê, a função emite um `generatedSceneCandidate` que **referencia** itens por `knowledgeItemId` (jamais duplica) e segue os 34 campos do padrão `Scene` v1.1 — acionando `triggerItem`/`cascadeStructure`/`weightedClaimSets`/`paleoPositionPolicy` conforme o regime, e marcando maturidade (`rascunho`/`gabarito-interno`/publicável) e exibição (`publicabilityStatus`) separadamente. A função **não** promove cena a gabarito — isso é decisão de curadoria.

**Como respeita os invariantes.** `Scene` v1.1 é o molde de toda cena emitida; `canonicalTimeScalar` (T0 = 2000.0 CE ≈ J2000) é a base da interseção entre regimes; `sourceTimeBasis` é **preservado** (honestidade temporal, jamais sobrescrito); `reviewStatus`/`publicabilityStatus`/`gatingReason` aplicam o invariante de exibição (nada `pending`/`legal-review`/`rejected` aparece como fato ou na simultaneidade pública).

---

## 2. Artefatos aprovados da Etapa 5 (Tarefa 2)

| Artefato | Finalidade | Status | Relação com o Knowledge Core | Relação com `Scene` v1.1 | Vinculante? |
|---|---|---|---|---|---|
| **`WhatWasHappeningAtMoment`** | capacidade de leitura espaço-temporal que responde "o que acontecia neste momento?" | aprovado (baseline conceitual) | leitura pura dos índices/entidades do KC; nunca escreve | **produz** cenas sob o padrão | **Sim** |
| **`MomentQuery`** | objeto único de entrada da função | aprovado | normaliza para os índices do KC; não cria dado | alimenta `queryType`/`timeRange`/`spatialScope` da cena | **Sim** |
| **`MomentResult`** | objeto único de saída da função | aprovado | composição de itens do KC por referência | seus campos mapeiam para os da cena | **Sim** |
| **`generatedSceneCandidate`** | cena `Scene` v1.1 emitida pela função, quando há coesão | aprovado (mecânica; **nenhuma** cena criada) | referencia `knowledgeItemId`; não duplica | **é** uma `Scene` v1.1 candidata | **Sim** |
| **`anachronismWarnings`** | avisos de anacronismo do recorte | aprovado | deriva de `TimeRange`/`ModernCorrespondence`/`paleoPosition` | preenche/dialoga com `anachronismPolicy` | **Sim** |
| **`equivalenceWarnings`** | avisos anti-falsa-equivalência (adição ao exemplo do enunciado) | aprovado | deriva de `weightedClaimSets`/`ClaimSet` | acompanha `weightedClaimSets` da cena | **Sim** |
| **Categorias de resultado** | foco principal · simultâneos centrais · simultâneos contextuais · States de fundo · evidências · debates/`ClaimSets` · consequências · itens ocultos/mediados | aprovado | particiona itens do KC por relevância | organizam `centralItems`/`contextualItems`/`states`/… | **Sim** |
| **Modos de resultado** | resumo rápido · cena completa · dossiê · lista por região · lista por camada · comparação antes/depois · linha do tempo · globo/mapa · relatório interno de curadoria | aprovado | controlam o que se lê e expõe do KC | selecionam quanto da cena/itens é exibido | **Sim** |
| **Regras de seleção e ranqueamento** | pontuação por interseção/proximidade temporal-espacial, relação com foco, camada, confiança, diversidade (anti-eurocentrismo), anti-sobrecarga | aprovado | ordenam itens do KC; o invariante de exibição precede o ranking | definem `centralItems` × `contextualItems` | **Sim** |
| **Regras de gating/publicabilidade** | 5 níveis (publicável→bloqueada) + `gatingReason` (editorial/científico/licença/revisão-humana/geometria/mídia/fonte/legal) + modulação por faixa | aprovado | aplicam `reviewStatus`/riscos do KC | preenchem `publicabilityStatus`/`gatingReason` da cena | **Sim** |
| **Padrões de resposta por tipo de consulta** | gabaritos de resposta para 8 consultas-modelo (1789; território-Brasil-1789; 2,4 Ga; 66 Ma; antes/depois K-Pg; Revolução Industrial; clima moderno; cenário 2100) | aprovado | mapeiam entidades do KC por padrão | indicam que tipo de cena cada consulta gera | **Sim** (como referência, não como conteúdo) |

---

## 3. Decisões aprovadas da Etapa 5 (Tarefa 3)

1. **A função é leitura, não escrita.**
2. **A função não cria `Claim`, `Event`, `State`, `Relationship` nem `Source`.**
3. **A função não altera `reviewStatus`.**
4. **A função não publica automaticamente nada** (toda publicação passa por curadoria humana).
5. **A função pode gerar `Scene` candidate, mas não cena-gabarito** (gabarito é decisão de curadoria, sob os 12 critérios da 4H §9).
6. **A função deve respeitar `canonicalTimeScalar`** (T0 = 2000.0 CE ≈ J2000) como base da interseção entre regimes.
7. **A função deve preservar `sourceTimeBasis`** (datum nativo nunca apagado; conversão é lente aditiva).
8. **A função deve respeitar `timePrecision` e `timeUncertainty`** (sem inventar precisão; faixa difusa aparece como faixa).
9. **A função deve aplicar `reviewStatus`, `publicabilityStatus` e `gatingReason`** (invariante de exibição absoluto).
10. **A função deve produzir `anachronismWarnings`.**
11. **A função deve produzir `equivalenceWarnings`.**
12. **A função deve distinguir consenso, hipótese, controvérsia e negacionismo** (consenso tipado como consenso; negacionismo `rotulado-rejeitado` fora do `ClaimSet`).
13. **A função deve usar `weightedClaimSets` quando necessário** (pesos assimétricos sem falsa equivalência).
14. **A função deve usar `ModernCorrespondence` e `paleoPosition` corretamente** (lente moderna no histórico; paleoposição rotulada no profundo; localidade de evidência ≠ posição antiga).
15. **A função deve ocultar ou mediar itens `pending`, sensíveis ou cientificamente frágeis** (com `gatingReason` e modulação por faixa).

> Estas decisões **passam a ser vinculantes** para todas as etapas que leiam o Knowledge Core (6 em diante). Nenhuma pode ser relaxada por conveniência de UI, pipeline ou currículo.

---

## 4. Padrões vinculantes para etapas futuras (Tarefa 4)

| Padrão | Veio de | Por que é vinculante | Etapa(s) futura(s) que consome(m) |
|---|---|---|---|
| **`Scene` v1.1** | 4F/4H | molde único de toda cena (34 campos); evita reinvenção e garante honestidade epistêmica | 6 (referência), 9 (saída pedagógica), 10 (experiência) |
| **`MomentQuery`** | 5 | contrato de entrada da função central | 6, 7, 8 (como leitores externos) |
| **`MomentResult`** | 5 | contrato de saída da função central; interface de leitura do KC | 6, 8, 9, 10 |
| **`canonicalTimeScalar`** | 3Z | único eixo que liga cósmico→futuro; base de interseção | 6, 8, 10, 13 |
| **`sourceTimeBasis`** | 3Z | honestidade temporal; datum nativo nunca apagado | 6, 13 |
| **`TimeRange`** | 2/3Z | posiciona todo item no eixo único, com precisão/incerteza | 6, 8, 10, 13 |
| **Claim-first** | 2 | nenhuma verdade fora de `Claim` tipado e fonteado | 6, 9 (saídas citam claims), 13 |
| **`ProvenanceMetadata`** | 1.1/2 | toda entidade factual carrega proveniência; sem proveniência não há fato | 6, 13, 14 |
| **`LicenseProfile`** | 1.1/2 | licença rastreada por asset; isolamento SA/ODbL | 11 (fronteira física), 13, 14 |
| **`reviewStatus`** | 1.1/2 | portão de exibição (pending/legal-review/rejected não aparece) | 6, 9, 10 |
| **`publicabilityStatus`** | 4F/4H | 5 níveis de exibição agregada | 6, 9, 10 |
| **`gatingReason`** | 4H | nomeia o porquê do gating (editorial/científico/…) | 6, 9, 10 |
| **`WeightedClaim`** | 4H | pesos assimétricos sem falsa equivalência; negacionismo fora do conjunto | 6, 9 |
| **`ClaimSet`** | 2/3.1 | controvérsia legítima como lados discretos | 6, 9 |
| **`UncertaintyProfile`** | 2 | incerteza como faixa, não "lados" | 6, 9, 10 |
| **`ModernCorrespondence`** | 2/4C/4D | lente "o que hoje é…" sem anacronismo (lente Brasil, D8) | 6, 7, 8, 10 |
| **`paleoPosition`** | 4H | localidade atual × paleoposição em tempo profundo | 10, 13 |
| **`cascadeStructure`** | 4G/4H | encadeamento gatilho→efeitos com confiança decaindo | 9, 10 |
| **`OceanographicState`** | 4F/4G | 11º State Type oficial, confirmado na prática | 4x (povoamento), 10 |
| **`anachronismWarnings`** | 4D/4E/4G/5 | impede anacronismo (Brasil-nação, paleomapa como fato…) | 6, 9, 10 |
| **`equivalenceWarnings`** | 5 | impede falsa equivalência (negacionismo como "lado") | 6, 9, 10 |

> **Invariantes transversais herdados** (não negociáveis): direção única de dependência (camadas externas apontam para o KC; o KC nunca aponta para fora); Wikidata/IA só como índice, nunca autoridade; nada `pending`/`legal-review`/`rejected` exibível; "não inventar" precisão/geometria/paleomapa.

---

## 5. Backlog geral de pendências estruturais (Tarefa 5)

Consolidação das pendências surgidas nas Etapas 1–5. **Urgência** usa quatro rótulos alinhados à Seção 6: **Bloqueante-E6** · **Durante-E6** · **Pré-MVP** · **Futura**. **Bloqueia E6?** responde apenas ao *início* da Etapa 6.

| # | Pendência | Origem | Risco | Urgência | Resolução provável | Bloqueia E6? | Observação |
|---|---|---|---|---|---|---|---|
| P01 | Revisão científica dos itens `pending` das cenas profundas | 4E/4G/4Z | médio (científico) | Pré-MVP→Futura | revisão científica/curadoria | **Não** | ~18 itens K-Pg + GOE (magnitude, paleogeografia, pesos, mecanismos) |
| P02 | Revisão editorial dos itens sensíveis | 3.1/4D/4Z | alto (editorial) | Durante-E6 | governança editorial (3.1) | **Não** | insumo da E6 (faixa/mediação); Leis 10.639/11.645 |
| P03 | Revisão jurídica quando aplicável | 1.1/3.1/4B | alto (jurídico) | Durante-E6 | revisão jurídica/LGPD | **Não** | BR-07 (ditadura) migra para `legal-review` |
| P04 | Geometrias históricas pendentes | 4C/4D/4Z | médio | Pré-MVP | curadoria espacial | **Não** | fronteiras de 1789; `PENDENTE_REFINAMENTO_ESPACIAL`; globo esquemático cobre o vazio |
| P05 | Geometrias paleogeográficas pendentes | 4E/4G | médio | Pré-MVP | curadoria espacial (GPlates/EarthByte) | **Não** | crátons 2,4 Ga; sempre `reconstrução modelada` rotulada |
| P06 | `paleoPositions` pendentes | 4G/4H | médio | Pré-MVP | curadoria espacial | **Não** | Chicxulub/Deccan em 66 Ma |
| P07 | Confirmação asset-level de fontes | 1.1/4B/4Z | alto (licença) | Pré-MVP | curadoria/ingestão (13) | **Não** | `PENDENTE_CONFIRMACAO_FONTE`; preenche `sourceTimeBasis`/`conversionMethod` |
| P08 | Reificação completa de `Source` | 2/4G/4Z | médio | Pré-MVP | modelagem operacional/ingestão (13) | **Não** | proveniência por claim |
| P09 | Reificação completa de `MediaAsset` | 2/4G/4Z | médio | Pré-MVP | ingestão de mídia (13) | **Não** | `natureLabel`/licença-por-asset; IA rotulada; mídia ilustra, não prova |
| P10 | Licença por asset | 1.1 | alto (jurídico) | Pré-MVP→Futura | curadoria/jurídico (14) | **Não** | NC/SA/ODbL/proprietária tratadas por asset |
| P11 | Isolamento de camadas ShareAlike/ODbL | 1.1/2 | alto (jurídico) | Pré-MVP | **arquitetura técnica (11)** | **Não** | princípio fixado; fronteira física pendente (MapBiomas SA, OSM ODbL) |
| P12 | Itens `Concept`/`Entity`/`Place`/`Region` incompletos | 4C | baixo-médio | Pré-MVP | povoamento/curadoria (4x) | **Não** | adensamento estrutural |
| P13 | Places de evidência a criar (Gubbio, Hell Creek, seções da camada-limite) | 4G/4H/4Z | baixo | Pré-MVP | povoamento + revisão científica | **Não** | "onde encontramos hoje" ≠ paleoposição |
| P14 | Revisão de sensíveis: escravidão, colonização, povos indígenas, ditadura, raça, evolução humana | 3.1/4B/4D | alto (editorial/jurídico) | Durante-E6 | governança editorial + jurídico | **Não** | insumo central da E6; Leis 10.639/11.645; LGPD |
| P15 | Revisão da camada de mudanças climáticas modernas | 3.1/4C/5 | médio-alto (científico+editorial) | Durante-E6 | governança científica/editorial | **Não** | consenso tipado como consenso; negacionismo fora do `ClaimSet` |
| P16 | Cenas futuras (Big Bang, clima moderno, 1492, Rev. Industrial, Cambriano, Apollo 11) | 4H/4Z | baixo | Futura | criação de cenas sob `Scene` v1.1 (4x) | **Não** | cobrem tipos da taxonomia ainda não exercitados |
| P17 | Regras de atualização de dados contemporâneos | 2 (§11)/0 | médio | Futura | **pipeline (13)** | **Não** | dados OWID/IBGE na ponta presente |
| P18 | Cadência de atualização por fonte | 2 (§11.5) | médio | Futura | **pipeline (13)** | **Não** | versionamento de `DatasetSnapshot` |
| P19 | Integração futura com pipeline de ingestão | 0/2/13 | médio | Futura | **Etapa 13** | **Não** | — |
| P20 | Integração futura com UX/UI | 0/3/10 | médio | Futura | **Etapa 10** | **Não** | a forma visual é da E10 |
| P21 | Integração futura com MVP | 0 (Q6)/12 | médio | Futura | **Etapa 12** | **Não** | três cenários (mínimo/intermediário/robusto) |
| P22 | Modo offline e performance escolar | 0 (D10/A2) | médio-alto (fundação) | Pré-MVP | Etapas 10–12 | **Não** | requisito de fundação; a E6 o **registra** como requisito de uso escolar |
| P23 | Hardware escolar modesto | 0 (D10/A2) | médio | Pré-MVP | Etapas 10–12 | **Não** | degradação progressiva (3D→2D→cartões) |
| P24 | Acessibilidade e e-MAG/WCAG | 0 (D10)/3 (§8.3) | alto (conformidade) | Durante-E6 | **a E6 define requisitos**; aplicação na 10 | **Não** | rótulos epistêmicos com redundância não-cromática |
| P25 | LGPD e proteção de menores | 0 (D10)/1.1/3.1 | alto (jurídico) | Durante-E6 | **objeto central da E6**; aplicação transversal | **Não** | não bloqueia o *início*, mas é tema-núcleo da E6 |
| P26 | Pessoas vivas e eventos contemporâneos | 2 (§11.7)/1.1/4B | alto (jurídico/LGPD) | Durante-E6 | revisão jurídica + governança | **Não** | `legal-review` obrigatório |
| P27 | Dados projetivos/futuros | 3Z/5 | médio (científico/comunicação) | Pré-MVP→Futura | curadoria + UX | **Não** | `sourceTimeBasis = scenarioYear`; sempre rotulado |
| P28 | Separação entre fato, cenário e previsão | 3Z/3.1/5 | médio-alto (editorial) | Durante-E6 | **vinculante já**; modulação por faixa é da E6 | **Não** | projeção nunca exibida como previsão certa |
| P29 | Validação com especialistas | 0 (D11)/14 | médio | Futura | **Etapa 14** | **Não** | parcerias (universidades/museus) |
| P30 | Validação com professores | 0/14 | médio | Futura | **Etapa 14** | **Não** | validação de uso em sala |

> **Leitura do backlog:** **nenhuma** pendência bloqueia o *início* da Etapa 6. As de maior peso para a E6 são **insumos** (P02, P03, P14, P15, P24, P25, P26, P28) — a camada de conformidade as **endereça como requisitos**, não precisa tê-las resolvidas para começar.

---

## 6. Classificação das pendências por urgência (Tarefa 6)

**Grupo 1 — Bloqueantes antes da Etapa 6.** **Nenhuma.** A Etapa 6 é uma camada **conceitual de conformidade** que consome o Knowledge Core e a função `WhatWasHappeningAtMoment` **por referência** (leitora externa). Ela não depende de conteúdo povoado, geometria final, fontes confirmadas ou camadas a jusante para definir *como* o produto se mantém compatível com a educação brasileira.

**Grupo 2 — Importantes durante a Etapa 6** (endereçar como **requisitos**, não pré-resolver): P02, P03, P14 (revisão editorial/jurídica de sensíveis — a E6 define as regras de exposição e mediação); P15 (camada de clima moderno — a E6 define o tratamento de tema científico sensível); P24 (acessibilidade e-MAG/WCAG); P25 (LGPD e proteção de menores); P26 (pessoas vivas/contemporâneo); P28 (separação fato × cenário × previsão por faixa).

**Grupo 3 — Necessárias antes de MVP/protótipo:** P04, P05, P06 (geometrias/paleoposições); P07 (confirmação asset-level); P08, P09 (reificação de `Source`/`MediaAsset`); P10 (licença por asset); P11 (isolamento SA/ODbL — arquitetura, Etapa 11); P12, P13 (itens e Places de evidência incompletos); P22, P23 (offline/hardware); P27 (dados projetivos, refinamento).

**Grupo 4 — Podem ficar para fases futuras:** P01 (revisão científica completa das cenas profundas — necessária antes da **publicação pública** dessas cenas, não antes da E6); P16 (cenas futuras); P17, P18 (atualização/cadência — pipeline); P19 (pipeline); P20 (UX); P21 (MVP); P29, P30 (validação com especialistas/professores).

**Direto ao ponto:**
- **O que precisa ser resolvido agora:** nada — a Etapa 6 está desbloqueada.
- **O que precisa apenas ser registrado (e endereçado como requisito durante a E6):** os itens do Grupo 2.
- **O que pode ficar para depois:** os Grupos 3 e 4, carregados como backlog vivo.

---

## 7. O que NÃO bloqueia a Etapa 6 (Tarefa 7)

As pendências abaixo **não** impedem o início da Etapa 6, com a respectiva justificativa:

| Não bloqueia | Por quê |
|---|---|
| **Revisão científica completa dos itens `pending`** | a E6 define **regras de conformidade**, não valida ciência; itens incertos já são gerenciados por `reviewStatus`/`gatingReason` |
| **Geometria final das cenas** | conformidade não depende de geometria; globo esquemático rotulado cobre o vazio |
| **Novas cenas** | a E6 indexa o que existe; não precisa de novas cenas para definir compatibilidade |
| **Pipeline de ingestão** | a E6 é conceitual; ingestão é Etapa 13 |
| **Confirmação asset-level de todas as fontes** | a E6 não publica conteúdo; licença por asset é pré-requisito de **publicação/ingestão**, não de conformidade conceitual |
| **UX/UI final** | a forma visual é da Etapa 10; a E6 fixa **requisitos**, não telas |
| **MVP** | recorte de produto é Etapa 12 |
| **Stack técnica** | decisão da Etapa 11 |
| **Planos de aula** | a E6 **não** entra em plano de aula (é da Output Layer, Etapa 9) |
| **Content Matching Engine** | é Etapa 8, leitor externo posterior |
| **Teacher Planning Layer** | é Etapa 7, posterior |
| **Pedagogical Output Layer** | é Etapa 9, posterior |

**Justificativa geral.** A Etapa 6 mapeia **obrigações legais e pedagógicas gerais** e define **como o currículo brasileiro referencia o Knowledge Core sem contaminá-lo** — pela direção única de dependência já fixada (Etapa 2, Tarefa 10). Como ela opera por **anotação/indexação externa sobre a saída da função** (`MomentResult`) e por **referência ao KC por `knowledgeItemId`**, não precisa de conteúdo final, geometria final, fontes confirmadas, pipeline, UX, MVP ou camadas a jusante. Tudo isso é carregado como backlog sem impedir a definição da conformidade.

---

## 8. O que a Etapa 6 deve consumir (Tarefa 8)

A **Etapa 6 — Brazilian Education Compliance Layer** deve consumir:

- **Knowledge Core (Etapa 2)** — as entidades, o claim-first e a direção única de dependência (a BNCC aponta para o KC, nunca o contrário);
- **Função `WhatWasHappeningAtMoment` (Etapa 5)** — os contratos `MomentQuery`/`MomentResult` como **interface de leitura**; a conformidade anota/filtra **sobre a saída**;
- **`Scene` v1.1 (Etapa 4H)** — o molde de cena que a experiência e as saídas pedagógicas reaproveitarão;
- **Política editorial (Etapa 3.1)** — os cinco níveis de exposição por faixa, o fluxo de governança e as regras de tema sensível;
- **Licenças e portão de ingestão (Etapa 1.1)** — o invariante de exibição e os limites de licença/proveniência;
- **Datum temporal (Etapa 3Z)** — `canonicalTimeScalar` e exibição por regime;
- **Padrões de publicabilidade** — 5 níveis + `gatingReason`;
- **Warnings de anacronismo/equivalência** — `anachronismWarnings`/`equivalenceWarnings`;
- **Backlog de pendências estruturais** (Seção 5) — para endereçar os itens do Grupo 2 como requisitos.

A Etapa 6 deve definir **como o sistema se mantém compatível** com: **BNCC**; **LDB**; **Educação Infantil, Ensino Fundamental e Ensino Médio** (na medida aplicável, respeitando D9 — V1 foca Fundamental II + Ensino Médio, arquitetura universal); **escolas públicas**; **escolas privadas**; **linguagem por faixa etária**; **acessibilidade**; **LGPD**; **proteção de menores**; **uso escolar responsável**; **conteúdo sensível**; e **conteúdo fora da grade como exploração livre/aprofundamento**.

---

## 9. Fronteiras da Etapa 6 (Tarefa 9)

**A Etapa 6 deve:**
- definir a camada de conformidade educacional brasileira;
- mapear obrigações legais e pedagógicas **gerais**;
- definir a relação com **BNCC, LDB, LGPD e acessibilidade**;
- definir como o produto pode ser usado como **recurso educacional digital complementar**;
- definir **linguagem por faixa etária**;
- definir **regras de exposição de conteúdo sensível**;
- definir como o **currículo brasileiro referencia o Knowledge Core sem contaminá-lo**.

**A Etapa 6 não deve:**
- criar planejamento específico do professor (Etapa 7);
- criar planos de aula, quizzes ou rubricas (Etapa 9);
- criar LMS;
- criar UX final (Etapa 10);
- definir stack técnica (Etapa 11);
- criar MVP (Etapa 12);
- fazer ingestão de dados (Etapa 13);
- popular novas cenas (Etapas 4x);
- substituir revisão jurídica;
- prometer homologação automática pelo MEC.

---

## 10. Riscos seguintes (Tarefa 10)

| Risco | Mitigação |
|---|---|
| **Interpretar BNCC como origem do conteúdo** | reafirmar P1/P2: conhecimento é universal; BNCC é **anotação externa**, nunca origem nem campo do núcleo |
| **Misturar currículo com Knowledge Core** | direção única de dependência (Etapa 2, Tarefa 10); a conformidade aponta para `knowledgeItemId`, o KC não conhece a BNCC |
| **Mapear códigos BNCC sem fonte oficial** | usar **documentos oficiais BNCC/MEC** como fonte; `BNCCMapping` carrega proveniência; sem fonte oficial, não mapeia |
| **Tratar conformidade como homologação MEC** | declarar explicitamente: alinhamento ≠ homologação; o produto é **recurso complementar**, não material homologado |
| **Ignorar LGPD** | LGPD/proteção de menores como tema-núcleo da E6; dados de aluno fora do KC; `legal-review` para pessoas vivas |
| **Ignorar acessibilidade** | e-MAG/WCAG como requisito de conformidade; rótulos com redundância não-cromática (herdado da Etapa 3 §8.3) |
| **Ignorar faixa etária** | reusar os 5 níveis de exposição da 3.1; `ageLevelMode` da função modula profundidade/linguagem/mídia, nunca o fato |
| **Expor conteúdo sensível sem mediação** | invariante de exibição + `gatingReason` + mediação obrigatória por faixa; nada `pending`/`legal-review` aparece |
| **Transformar exploração livre em obrigação curricular** | preservar o duplo caminho (D3): exploração livre vai do KC à experiência **sem** passar pelo filtro curricular; a grade define foco, não limite |
| **Prometer adoção pública sem requisitos de escola pública** | tratar offline parcial, acessibilidade, LGPD, hardware modesto e modo projetor como **fundação** (D10/A2), registrados no backlog |
| **Deixar escolas privadas sem flexibilidade** | a conformidade é **indexação/serviço**, não trava; escolas privadas mantêm flexibilidade de uso (D3) |
| **Confundir alinhamento curricular com material aprovado pelo PNLD** | declarar que alinhamento à BNCC **não** equivale a aprovação no PNLD; PNLD é processo próprio, fora do escopo da E6 |

---

## 11. Handoff para a Etapa 6 (Tarefa 11)

- **Etapa 5 encerrada.** A função central foi generalizada de cenas-instância para a capacidade reutilizável `WhatWasHappeningAtMoment`; artefatos, decisões e padrões vinculantes fixados.
- **Função `WhatWasHappeningAtMoment` aprovada** como baseline conceitual da consulta espaço-temporal.
- **Backlog geral registrado** (30 pendências, Seção 5), classificado por urgência (Seção 6).
- **Pendências não bloqueantes carregadas** — **nenhuma** trava o início da Etapa 6; os itens do Grupo 2 são endereçados como requisitos.
- **Etapa 6 recomendada:** **Brazilian Education Compliance Layer**.
- **Objetivo da Etapa 6:** definir **como o sistema se mantém compatível com a educação brasileira** (BNCC, LDB, LGPD, acessibilidade, faixa etária, proteção de menores, uso escolar responsável) **sem contaminar o Knowledge Core** — a conformidade entra como **camada de leitura/anotação/indexação externa** sobre o KC e a saída da função, preservando a direção única de dependência.
- **Documentos que a Etapa 6 deve consumir:** Etapa 2 (KC), Etapa 5 (função + `MomentQuery`/`MomentResult`), Etapa 4H (`Scene` v1.1), Etapa 3.1 (política editorial), Etapa 1.1 (licenças/portão), Etapa 3Z (datum), padrões de publicabilidade, `anachronismWarnings`/`equivalenceWarnings`, e este backlog (Seção 5).
- **Limites da Etapa 6:** os da Seção 9 — sem plano de aula, quiz, rubrica, LMS, UX final, stack, MVP, ingestão, novas cenas; sem substituir revisão jurídica; sem prometer homologação MEC.

---

## 12. Próximos passos (Tarefa 12)

- **Imediato:** com a Etapa 5Z, a **Etapa 5 está formalmente encerrada**, a função central aprovada, as pendências registradas e classificadas, e a **Etapa 6 desbloqueada**. O risco de perda de decisões foi reduzido pela consolidação de artefatos, decisões e padrões vinculantes.
- **Quando solicitada, executar a Etapa 6 — Brazilian Education Compliance Layer**, consumindo exatamente o que a Seção 8 lista e respeitando as fronteiras da Seção 9.
- **Sequência subsequente** (sem pular etapas, mediante solicitação): Etapa 7 (Teacher/School Planning Layer) → 8 (Content Matching Engine) → 9 (Pedagogical Output Layer) → 10 (Design/UX 3D) → 11 (Arquitetura técnica) → 12 (MVP) → 13 (Pipeline de ingestão) → 14 (Validação escolar, jurídica e comercial).
- **Backlog como documento vivo:** a Seção 5 deve ser revisitada ao fim de cada etapa, movendo pendências entre grupos à medida que forem resolvidas ou se aproximarem do MVP/pipeline/publicação. Pendências do Grupo 2 devem ser **endereçadas como requisitos** dentro da Etapa 6; as dos Grupos 3 e 4 permanecem carregadas até suas etapas próprias.

---

*Documento de encerramento da Etapa 5, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5). Consolida: resumo executivo da Etapa 5; 11 artefatos conceituais aprovados; 15 decisões aprovadas; 21 padrões vinculantes (com origem, justificativa e consumidor futuro); backlog geral de 30 pendências estruturais (com descrição, origem, risco, urgência, etapa de resolução, se bloqueia a Etapa 6 e observação); classificação das pendências em quatro grupos de urgência; o que não bloqueia a Etapa 6 (com justificativa); o que a Etapa 6 deve consumir; as fronteiras da Etapa 6; doze riscos seguintes com mitigação; o handoff para a Etapa 6; e os próximos passos. Não resolve pendências, não cria cena nova, não povoa conteúdos, não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não desenha pipeline técnico, não reabre auditoria de fontes nem política editorial, não cria prompts da Etapa 6. Etapa 5 formalmente encerrada; função central aprovada; pendências estruturais registradas e classificadas; Etapa 6 — Brazilian Education Compliance Layer — desbloqueada.*
