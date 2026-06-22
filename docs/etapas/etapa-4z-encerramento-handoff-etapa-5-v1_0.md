# Etapa 4Z — Encerramento da Etapa 4 e Handoff para a Etapa 5

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Encerramento da **Etapa 4** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3 e a política editorial vinculante da Etapa 3.1 · 12/06/2026
**Escopo desta etapa (e seus limites):** **fechar formalmente a Etapa 4** — consolidar decisões, fixar artefatos aprovados, declarar os padrões que passam a ser **vinculantes**, e carregar as pendências para as próximas etapas. Conforme solicitado, **não** cria cena nova, **não** povoa conteúdos, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** reabre auditoria de fontes (1/1.1) e **não** reabre política editorial (3.1).

---

## Sumário

1. Resumo executivo da Etapa 4
2. Documentos produzidos (4A–4H)
3. Decisões aprovadas
4. Padrões vinculantes para etapas futuras
5. Cenas-gabarito aprovadas
6. State Types oficiais
7. Padrão `Scene` v1.1
8. Checklist operacional de criação de cenas
9. Pendências estruturais ainda abertas
10. O que NÃO deve mais ser resolvido dentro da Etapa 4
11. Handoff para a Etapa 5

---

## 1. Resumo executivo da Etapa 4

A Etapa 4 transformou a arquitetura de camadas científicas e históricas (4A) em **método operacional comprovado**. Partiu de um lote-piloto auditável (4B), normalizou-o e criou os nós de referência (4C), e então **provou a função central do produto em três regimes distintos** por meio de cenas ponta-a-ponta:

- **1789** (4D) — simultaneidade **histórica** (gating editorial);
- **2,4 Ga / GOE** (4E) — simultaneidade **planetária profunda** (gating científico, sem documentos);
- **66 Ma / K-Pg** (4G) — cena **híbrida** (evento pontual + sistema terrestre).

Entre e após as cenas, a Etapa 4 **consolidou o método**: extraiu o padrão genérico de `Scene` e revisou os `State Types` (4F), e fechou os refinamentos revelados pela cena híbrida no padrão `Scene` **v1.1** (4H). O resultado é um **método reproduzível**: qualquer cena futura (Big Bang, 1492, Revolução Industrial, clima moderno, Cambriano…) segue um padrão claro, uma checklist e critérios de publicabilidade.

**A Etapa 4 cumpriu seu papel.** Há padrão, há gabaritos, há tipos oficiais — e a função "O que acontecia no mundo neste momento?" foi demonstrada concretamente em três escalas de tempo.

---

## 2. Documentos produzidos (4A–4H)

| Doc | Título | Papel | Status |
|---|---|---|---|
| **4A** | Arquitetura das camadas científicas e históricas | baseline das 25 camadas | aprovado |
| **4B** | Lote-piloto P0 do Knowledge Core | 70 itens-piloto + 7 ClaimSets + cena 1789 inicial | aprovado |
| **4C** | Normalização e entidades de referência | auditoria, ids, 26 Concepts, 21 Entities, 25 Places/Regions | aprovado |
| **4D** | Cena canônica de 1789 ponta-a-ponta | cena histórica (simultaneidade global) | aprovado |
| **4E** | Cena de tempo profundo / GOE (2,4 Ga) | cena de tempo profundo sem evento | aprovado |
| **4F** | Padrão genérico de `Scene` + `State Types` | método genérico + decisão de tipos | aprovado |
| **4G** | Cena canônica K-Pg (66 Ma) | cena híbrida + 1ª instância de `OceanographicState` | aprovado |
| **4H** | Consolidação pós-três cenas / `Scene` v1.1 | padrão v1.1 + cascadeStructure + ClaimSet com peso + paleoPosition | aprovado |
| **4Z** | Encerramento e handoff (este documento) | fecha a Etapa 4, entrega para a Etapa 5 | — |

---

## 3. Decisões aprovadas

1. **Padrão genérico de `Scene`** (4F) — a cena é **consulta materializada**, não duplica conteúdo. **Atualizado para v1.1** (4H).
2. **`OceanographicState` criado** (4F, aprovado) e **instanciado oficialmente** (4G) — 11º `State Type`.
3. **`GeochemicalState` NÃO criado** — geoquímica vive como `evidenceClaims` + campos redox dos States existentes.
4. **`EarthSystemState` NÃO criado** — é agregação **virtual** da própria `Scene`.
5. **`cascadeStructure`** (4H) — encadeamento gatilho→efeitos, com `confidenceByStage` que **decai**; obrigatório em cenas híbridas/extinção.
6. **`ClaimSet` com peso por claim** (`WeightedClaim`, 4H) — pesos assimétricos **sem** falsa equivalência; negacionismo sempre `rotulado-rejeitado` fora do ClaimSet.
7. **`paleoPosition` em `Place`** (4H) — distingue localidade atual de paleoposição em tempo profundo.
8. **Separação `pilotCode` × `knowledgeItemId`** e prefixos canônicos (4C).
9. **5 níveis de publicabilidade + `gatingReason`** (4F/4H) — bastam; o tipo de gating (editorial/científico/licença/…) é nomeado.
10. **Disciplina ClaimSet × UncertaintyProfile** (4E em diante) — lados discretos × faixas.
11. **Três cenas confirmadas como cena-gabarito** (4H).

---

## 4. Padrões vinculantes para etapas futuras

A partir do encerramento da Etapa 4, **passam a ser vinculantes**:

- **`Scene` v1.1** como modelo de toda cena (§7).
- **Os 11 `State Types` oficiais** (§6) — nenhum novo tipo sem reabertura controlada justificada.
- **Checklist operacional de 25 itens** (§8) — aplicada **antes** de criar qualquer cena.
- **Invariante de exibição** (herdado da 3.1): nada `pending`/`legal-review`/`rejected` aparece como fato.
- **Disciplina anti-falsa-equivalência** via `weightedClaimSets`: consenso é consenso; negacionismo é objeto rotulado, nunca "lado".
- **Padrão de evidência "como sabemos disso"**: toda cena (documental ou proxy) expõe a cadeia de inferência; mídia **ilustra**, nunca **prova**.
- **Política de anacronismo** explícita por cena (ModernCorrespondence no histórico; paleoPosition no profundo; exclusão de itens fora do período).
- **"Não inventar"**: nem precisão, nem paleomapa, nem composição/fronteira sem fonte — usar flags `PENDENTE_*`.

---

## 5. Cenas-gabarito aprovadas

| Cena | `knowledgeItemId` | Tipo exemplificado | Padrão que ensina |
|---|---|---|---|
| **1789** | `scene:world-1789-french-revolution` | simultaneidade global histórica | ModernCorrespondence; gating editorial; três paralelos (Brasil/África/indígenas) |
| **2,4 Ga / GOE** | `scene:earth-2-4ga-great-oxidation-event` | tempo profundo sem evento | evidência sem documentos; ClaimSet×UncertaintyProfile; States dominantes; zero Event |
| **66 Ma / K-Pg** | `scene:earth-66ma-kpg-extinction` | tempo profundo com evento / extinção | cascadeStructure; ClaimSet com peso; paleoPosition; OceanographicState oficial |

As três são **`gabarito-interno`** e **parcialmente publicáveis** (Nível 2) — exemplares de método, com pendências de revisão registradas.

---

## 6. State Types oficiais

Onze tipos oficiais (10 da Etapa 2 + `OceanographicState` da 4F):

`AtmosphereState` · `TectonicState` · `PaleogeographicState` · `ClimateState` · **`OceanographicState`** · `BiomeState` · `CivilizationState` · `TechnologyState` · `PopulationState` · `CulturalState` · `EconomicState`.

**Não oficializados** (decisão registrada): `GeochemicalState` (= evidência + campos redox) e `EarthSystemState` (= agregação virtual da `Scene`).

---

## 7. Padrão `Scene` v1.1

Referência canônica: **Etapa 4H, §2** (definição completa) e **4F, §2** (campos herdados). Campos:

```txt
Scene = {
  // herdados (v1.0 / 4F)
  id, title, focusItem, queryType, timeRange, timePrecision, spatialScope,
  activatedLayers, centralItems, contextualItems, sensitiveItems, hiddenItems,
  claimSets, uncertaintyProfiles, states, sources, evidenceProfile,
  editorialRisk, scientificRisk, licenseRisk, reviewStatus,
  timelineBehavior, globeBehavior, dossierBehavior, simultaneityBehavior,
  anachronismPolicy, publicabilityStatus,
  // novos (v1.1 / 4H)
  triggerItem, cascadeStructure, weightedClaimSets, paleoPositionPolicy,
  scenePatternType, gatingReason, sceneCompletenessLevel
}
```

Estruturas auxiliares aprovadas (4H): `CascadeStructure`, `WeightedClaim`, `PaleoPosition` + `Place` atualizado.

---

## 8. Checklist operacional de criação de cenas

Referência canônica: **Etapa 4H, §7** (25 perguntas). Resumo dos grupos:

- **Foco e tempo** (1–3): foco, regime temporal, precisão possível.
- **Estrutura v1.1** (4–9): triggerItem? cascadeStructure? Place/Region? paleoPosition? States? camadas?
- **Claims e evidência** (10–14): claims principais, evidências ("como sabemos"), ClaimSet, peso?, UncertaintyProfile.
- **Riscos** (15–17): editorial, científico, licença.
- **Exibição** (18–22): pending, oculto/mediado (`gatingReason`), publicabilityStatus, anacronismos, fontes a confirmar.
- **Validação final** (23–25): simultaneidade real? cabe no globo/timeline? dossiê explica "como sabemos"?

**Regra de bloqueio:** falhar em (13) equivalência indevida, (19) gating não declarado, (21) anacronismo não tratado ou (25) "como sabemos" ausente → a cena **não** avança.

---

## 9. Pendências estruturais ainda abertas

Registradas, **sem resolver agora**:

1. **Datum do eixo temporal:** 1950 BP × J2000 — decisão da Etapa 3; necessária para integrar cenas históricas e profundas no mesmo eixo.
2. **Revisão científica** dos itens `pending` das cenas profundas (magnitude, paleogeografia, pesos causais, mecanismos).
3. **Revisão editorial** dos itens sensíveis (escravidão, colonização, povos indígenas; Leis 10.639/11.645) — incl. migração de BR-07 (ditadura) para `legal-review`.
4. **Geometria histórica/paleogeográfica** pendente (`PENDENTE_REFINAMENTO_ESPACIAL`): fronteiras de 1789, crátons de 2,4 Ga, paleoposições de 66 Ma.
5. **Criação futura de novas cenas** (Big Bang, clima moderno, 1492, Revolução Industrial, Cambriano…) — sob o padrão v1.1.
6. **Reificação de `Source` e `MediaAsset`** (proveniência por claim; `natureLabel`/licença-por-asset; rotular IA).
7. **Confirmação asset-level de fontes** (`PENDENTE_CONFIRMACAO_FONTE`).
8. **Integração futura com pipeline de ingestão** (Etapa 13).
9. **Itens de tipo a completar:** Places de evidência (Gubbio, Hell Creek), nós `Concept`/`Entity` referenciados, dangling refs já corrigidos.

---

## 10. O que NÃO deve mais ser resolvido dentro da Etapa 4

A Etapa 4 está **encerrada**. **Não** se deve, sob o rótulo "Etapa 4":

- criar novas cenas ou povoar novos lotes;
- escrever código, propor MVP ou definir stack;
- desenhar UX final ou pipeline técnico;
- entrar em currículo, professor ou plano de aula;
- reabrir auditoria de fontes (1/1.1) ou política editorial (3.1);
- reabrir modelagem (Etapa 2) além dos refinamentos já aprovados (v1.1; `OceanographicState`);
- resolver as pendências da §9 — elas pertencem a etapas próprias (Etapa 3 para o datum; etapas de revisão/ingestão para o resto).

---

## 11. Handoff para a Etapa 5

A Etapa 4 entrega à Etapa 5 um **método maduro e três cenas-gabarito** que já realizam, na prática, a função "O que acontecia no mundo neste momento?" em três regimes de tempo. A Etapa 5 deve **generalizar essa função** de instâncias (cenas) para uma **capacidade reutilizável**.

**Documentos da Etapa 4 que a Etapa 5 deve consumir (prioridade):**
1. **4H** — `Scene` v1.1, `cascadeStructure`, `weightedClaimSets`, `paleoPosition`, checklist, critérios de cena-gabarito *(referência primária)*.
2. **4F** — padrão genérico de `Scene`, taxonomia de cenas, matriz tipo de tempo × representação, `State Types`, critérios de publicabilidade.
3. **4D / 4E / 4G** — as três cenas-gabarito, como **exemplos trabalhados** da função de simultaneidade nos três regimes.
4. **4A** (camadas) e **4C** (nós de referência) — o substrato sobre o qual a função opera.

---

## Encerramento

- **Etapa 4 encerrada.** Método consolidado, padrões vinculantes fixados, três cenas-gabarito aprovadas, `State Types` oficiais definidos, pendências estruturais registradas.
- **Etapa 5 recomendada.** Etapa 5 — Função **"O que acontecia no mundo neste momento?"**.
- **Objetivo da Etapa 5:** generalizar a função de simultaneidade — de cenas-instância (4D/4E/4G) para uma **capacidade reutilizável** do Knowledge Core: a lógica de consulta espaço-temporal que **produz** cenas a partir do `Scene` v1.1, com navegação ("outro lugar/período", "comparar antes/depois", "ver consequências"), respeitando simultaneidade, incerteza, pesos e anacronismo — **sem** ainda entrar em UX final, código ou pipeline.
- **Documentos da Etapa 4 a consumir pela Etapa 5:** **4H** e **4F** (padrão e método) como referência primária; **4D / 4E / 4G** (cenas-gabarito) como exemplos; **4A / 4C** como substrato.

---

*Documento de encerramento da Etapa 4, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A–4H). Fecha formalmente a Etapa 4: resumo executivo, lista dos documentos 4A–4H, decisões aprovadas, padrões vinculantes, três cenas-gabarito, 11 State Types oficiais, padrão `Scene` v1.1, checklist operacional, pendências estruturais registradas (sem resolver) e handoff para a Etapa 5. Não cria cena nova, não povoa conteúdos, não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não reabre auditoria de fontes nem política editorial. Etapa 4 encerrada; Etapa 5 — Função "O que acontecia no mundo neste momento?" — recomendada.*
