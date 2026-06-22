# Registro de Divergências — Migração A3 (Fase 6)

> Gerado por `migrate.py` sobre o protótipo `atlas-prototipo-3d.html`, reconciliado contra o corpus.
> Uma divergência **não é um erro**: é uma dívida explícita, roteada a uma fase futura, sem jamais relaxar um invariante. O item permanece carregado e gateado; o que se registra é o que falta para ele subir de status.

## Panorama da carga

| métrica | valor |
|---|---|
| itens carregados | 35 |
| · proveniência corpus | 27 |
| · proveniência seeded-demo | 8 |
| review_status approved | 23 |
| review_status pending | 12 |
| claims de item | 35 |
| ClaimSets (claim-sobre-claims) | 2 |
| relações | 5 |
| geometrias | 14 |
| fontes | 24 |
| fontes por asset pendentes | 11 |
| arestas rejeitadas por [N1] | 0 |

**Total de divergências registradas: 22** (11 fonte-por-asset-pendente, 8 seeded-demo, 3 geometria-esquemática).

## Fonte por asset pendente (perAssetConfirmed=false)  (11)

- **Fase de resolução:** F2
- **Tratamento de gate:** Bloqueado no portão público F2 (§9.2) até a fonte por asset ser confirmada. Pode aparecer em curatorial conforme review_status.

| item | tarefa pendente |
|---|---|
| `evt:estados-gerais-1789` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `evt:queda-bastilha-1789` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `chem:co2-1789` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `proc:goe` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `proc:deposicao-bif` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:oceanos-ferruginosos` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:clima-goe` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:paleogeografia-2-4ga` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:clima-pos-impacto-kpg` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:oceanos-pos-impacto-kpg` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |
| `state:paleogeografia-66ma` | F2 — confirmar fonte por asset (perAssetConfirmed) antes de publicação pública (§9.2). |

## Proveniência semeada (seeded-demo) — não está no corpus  (8)

- **Fase de resolução:** F1/F2
- **Tratamento de gate:** Exibível em modo CURATORIAL com rótulo "demonstração — fonte não validada". EXCLUÍDO do cluster público (§9 exige proveniência de corpus). Nunca promover sem revisão.

| item | tarefa pendente |
|---|---|
| `chem:lavoisier-traite-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `chem:atmosfera-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `chem:co2-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `phys:terra-orbita-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `geo:andes-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `geo:alpes-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `life:grande-auk-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |
| `life:biosfera-1789` | F1/F2 — modelar conteúdo multidomínio real de 1789 contra o corpus, ou manter rebaixado; nunca promover a corpus sem revisão. |

## Geometria de tempo profundo esquemática (rótulo de reconstrução)  (3)

- **Fase de resolução:** F3
- **Tratamento de gate:** Renderizado SEMPRE como reconstrução (is_reconstruction=true; AnachronismNotice). Paleopolígono validado é dívida de FIDELIDADE, não de correção.

| item | tarefa pendente |
|---|---|
| `state:paleogeografia-2-4ga` | F3 — geometria de tempo profundo é esquemática/rótulo de reconstrução; paleopolígono validado é dívida de fidelidade, não de correção. |
| `evt:impacto-chicxulub` | F3 — geometria de tempo profundo é esquemática/rótulo de reconstrução; paleopolígono validado é dívida de fidelidade, não de correção. |
| `state:paleogeografia-66ma` | F3 — geometria de tempo profundo é esquemática/rótulo de reconstrução; paleopolígono validado é dívida de fidelidade, não de correção. |

## Invariante preservado na reconciliação

A coluna de proveniência (`provenance_status`) deriva **exclusivamente** do sinal `seeded:true` do protótipo: os 8 itens multidomínio de 1789 (química, física, geologia, biologia) são `seeded-demo`; os 27 itens de história/GOE/K-Pg são `corpus`. A migração **não inventou fontes** para os itens semeados — a proveniência deles é declaradamente "demonstração — fonte não validada contra o corpus" (B1 §6). Nenhuma aresta afirmativa foi carregada sem proveniência (`n1_rejected = 0`): [N1] valeu na carga, não só na consulta.
