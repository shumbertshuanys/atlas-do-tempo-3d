# Análise de pendências atuais — Atlas do Tempo

**Natureza:** registro vivo de pendências, reclassificado para a fronteira de **implementação** (não mais "bloqueia a Etapa 6?", como no 5Z). Ancorado no backlog P01–P30 (5Z §5), nas decisões `[PENDÊNCIA]` de E11–E15 e nas tags `PENDENTE_*` de conteúdo. Data: revisão atual.

> **Veredito de uma linha:** nada bloqueia a **fatia descartável** que vamos construir; um cluster específico gateia a **publicação pública**; e a **fila de revisão humana** é o verdadeiro caminho crítico — não de correção, mas de **cobertura**.

---

## 1. Panorama — três naturezas de pendência

| Natureza | O que é | Volume | Onde mora |
|---|---|---|---|
| **Backlog estrutural** | pendências de projeto P01–P30 | 30 | 5Z §5 |
| **Decisões adiadas** `[PENDÊNCIA]` | escolhas técnicas/comerciais deliberadamente diferidas | 45 | E11 (17), E12 (8), E13 (4), E14 (6), E15 (10) |
| **Tags de conteúdo** `PENDENTE_*` | instâncias item-a-item do backlog, no conteúdo | ~156 | lote-piloto 4B (64) + cenas 4C/4D/4E/4G + pipeline |

As três se cruzam: as **tags de conteúdo** são o *tamanho* das famílias do **backlog estrutural**; as **decisões adiadas** são *onde* cada família será resolvida.

### Tags de conteúdo por tipo (o tamanho real do trabalho)

| Tag | Qtd | Família | Item do backlog |
|---|---|---|---|
| `PENDENTE_CONFIRMACAO_FONTE` | 43 | fonte/licença | P07, P10 |
| `PENDENTE_REFINAMENTO_ESPACIAL` | 37 | geometria | P04, P05, P06 |
| `PENDENTE_REVISAO_HUMANA` | 29 | revisão (editorial/científica) | P01, P02, P14, P15 |
| `PENDENTE_REFINAMENTO_TEMPORAL` | 13 | precisão temporal | P27 + geral |
| `PENDENTE_CLAIMSET` | 11 | curadoria de debate | P02/P14 (editorial) |
| `PENDENTE_GEOMETRIA` | 8 | geometria | P04–P06 |
| `PENDENTE_CONFIRMACAO_OFICIAL` | 7 | texto oficial (BNCC) | resíduo E6/E8/E9 |
| `PENDENTE_LICENCA` | 4 | licença por asset | P10 |
| `PENDENTE_DATA` | 3 | precisão temporal | — |

---

## 2. Backlog estrutural P01–P30, agrupado em 7 famílias

Cada família traz os códigos do 5Z, o dono da resolução e o **gatilho** que a encerra.

### F1 · Fila de revisão humana (editorial + científica) — *o caminho crítico de cobertura*
**P01** (revisão científica das cenas profundas, ~18 itens K-Pg/GOE) · **P02** (revisão editorial dos sensíveis) · **P14** (escravidão, colonização, povos indígenas, ditadura, raça, evolução humana) · **P15** (clima moderno).
Volume no conteúdo: **29 `REVISAO_HUMANA` + 11 `CLAIMSET`**. Dono: governança editorial (3.1) + científica. Gatilho: revisão humana por papel, item a item. **Não automatiza** (a fronteira "sem equivalência" de cada ClaimSet é escrita à mão — confirmado na fatia).

### F2 · Fonte e licença por asset — *o portão de qualquer coisa pública*
**P07** (confirmação asset-level de fontes) · **P10** (licença por asset NC/SA/ODbL/proprietária).
Volume: **43 `CONFIRMACAO_FONTE` + 4 `LICENCA` + 7 `CONFIRMACAO_OFICIAL`**. Dono: curadoria/ingestão (E13) + jurídico (E14). Gatilho: confirmar proveniência e licença por item antes de publicar.
> **Achado importante:** mesmo os ~20 itens *publicáveis* de 1789 ainda têm `PENDENTE_CONFIRMACAO_FONTE`. `approved` (pode exibir) ≠ fonte confirmada por asset. São portões distintos.

### F3 · Geometria histórica e paleogeográfica — *não bloqueia, mas limita fidelidade*
**P04** (fronteiras de 1789) · **P05** (paleogeografia, crátons 2,4 Ga) · **P06** (`paleoPositions`, Chicxulub/Deccan 66 Ma).
Volume: **37 `REFINAMENTO_ESPACIAL` + 8 `GEOMETRIA`**. Dono: curadoria espacial (GPlates/EarthByte). Gatilho: geometria validada. **Coberto pelo mapa esquemático rotulado** — a fatia provou que isso é decisão de design, não dívida.

### F4 · Reificação e isolamento técnico — *parte resolve com a decisão de banco*
**P08** (reificar `Source`) · **P09** (reificar `MediaAsset`, `natureLabel`/licença) · **P11** (isolamento físico SA/ODbL — já é arquitetura na E11).
Dono: arquitetura/ingestão (E11/E13). Gatilho: o esquema real do grafo + os dois stores (núcleo / `IsolatedLicenseStore`). **É exatamente o que a decisão de motor de banco começa a fechar.**

### F5 · Fundação de uso escolar — *bloqueia MVP real, não a fatia*
**P22** (offline/performance) · **P23** (hardware modesto) · **P24** (acessibilidade e-MAG/WCAG) · **P25** (LGPD/proteção de menores).
Dono: E10–E12 (técnico) + E14 (laudo). Gatilho: degradação 3D→2D→estático, ganchos de acessibilidade, DPIA/ASES.

### F6 · Jurídico e conteúdo sensível vivo — *radar antes de qualquer piloto*
**P03** (revisão jurídica; BR-07 ditadura → `legal-review`) · **P26** (pessoas vivas/contemporâneo, `legal-review` obrigatório) · **P28** (separar fato × cenário × previsão) · **P27** (dados projetivos).
Dono: jurídico + governança. Gatilho: pareceres reais (DPIA/RIPD), `legal-review` por item.

### F7 · Integração, povoamento e validação — *futuro, por etapa própria*
**P12/P13** (itens e Places de evidência incompletos) · **P16** (novas cenas) · **P17/P18** (atualização/cadência de fonte — pipeline) · **P19** (pipeline) · **P20** (UX) · **P21** (MVP) · **P29/P30** (validação com especialistas/professores).
Dono: a etapa correspondente. Gatilho: a própria etapa ser executada.

---

## 3. Decisões adiadas `[PENDÊNCIA]` (45) — resumo por etapa

- **E11 (17):** sobretudo a **escolha do motor do grafo** (RDF* × property graph × relacional → E12), autenticação concreta, índice vetorial sim/não, retenção/descarte, analytics agregado, LMS, DPIA, laudo ASES, e o resíduo `BNCCMapping` (pending até texto homologado).
- **E12 (8):** confirma que o MVP **não** decide o que a E11 deixou para E13/E14; SSO/OAuth, pseudônimos de sessão, OSM isolado, índice vetorial — todos diferidos.
- **E13 (4):** cadência concreta de recadência por fonte viva; calendários não-ocidentais como `sourceTimeBasis`; instrumentação de filas/SLAs/ferramentas; limiares de amostragem de auditoria.
- **E14 (6):** SLAs por fila, amostragem de auditoria, recheck/retenção de snapshots, SSO escolar, xAPI/SCORM/LTI, execução real (piloto, ASES, DPIA, pareceres).
- **E15 (10):** todos os **números** (preço/ticket/receita, TAM/SAM/SOM), dossiês de procurement sobre editais reais, CRM, white-label, SLAs comerciais.

Padrão: **quase toda decisão concreta de tecnologia, número e execução foi diferida de propósito** — o normativo é sempre a propriedade, nunca o produto/valor.

---

## 4. Reclassificação — o que bloqueia o quê

A matriz que importa agora. ✗ = bloqueia · △ = molda, mas não bloqueia · — = irrelevante nesta fronteira.

| Família | Fatia (descartável, 24 itens) | MVP público (recorte E12) | Escala / publicação ampla |
|---|---|---|---|
| F1 · Revisão humana | — (gating já oculta o sensível) | △ (limita cobertura, não correção) | ✗ (cobertura é o produto) |
| F2 · Fonte/licença por asset | — (dados já modelados) | ✗ (nada público sem proveniência+licença) | ✗ |
| F3 · Geometria | — (esquemático) | △ (esquemático cobre; limita fidelidade) | △ (3D/globo dependem) |
| F4 · Reificação/isolamento | △ (começamos a fechar) | ✗ (núcleo + store isolado reais) | ✗ |
| F5 · Fundação escolar | — | ✗ (offline/acessibilidade/LGPD) | ✗ |
| F6 · Jurídico/sensível vivo | — | ✗ p/ itens vivos; — p/ 1789 | ✗ |
| F7 · Integração/validação | — | — | ✗ (pipeline, validação) |

**Leitura:** a fatia está **destravada** — é o ponto inteiro de construí-la agora. O salto fatia → **MVP público** acende F2, F4, F5, F6. O salto MVP → **escala** acende F1 e F7. O gênio do invariante de exibição: dá para lançar um MVP só com o núcleo publicável **sem** estar bloqueado pela fila de revisão — o backlog limita **cobertura**, não **correção**.

---

## 5. Sinais que eu elevaria (dado o que a fatia ensinou)

1. **A fila de revisão (F1) precisa virar processo operante, não backlog.** É humana, não automatiza, e hoje está sem dono/cadência. É o caminho crítico de cobertura — e é exatamente o que as propostas de governança P3 (operar na fatia) e P4 (Definition of Ready) começam a endereçar.
2. **Confirmação de fonte por asset (F2) é pré-requisito até do "público".** Distinguir `approved` de fonte-confirmada evita publicar o núcleo de 1789 com citação ainda pendente.
3. **Geometria (F3) é deferível com tranquilidade** — o esquemático é epistemicamente correto. Não deixar virar bloqueio fantasma do MVP.
4. **O cluster jurídico (F6) tem de estar no radar antes de qualquer piloto com escola** (menores → DPIA, `legal-review` de BR-07 e de pessoas vivas). Não toca a fatia, mas trava implantação real.
5. **A decisão de motor de banco (E11→E12) não é risco — é a próxima decisão.** Resolvê-la em escala-fatia começa a fechar F4 (reificação) sem custo de escala.

---

## 6. Sequenciamento contra as etapas de implementação propostas

| Etapa de implementação | Pendências que resolve/pressiona | Pendências que **não** precisa resolver |
|---|---|---|
| **A · Ratificar governança** (P1/P2/P7) | nenhuma do backlog — destrava *como* seguimos | todas (é meta, barata) |
| **B · Decidir motor + banco em escala-fatia** (P3) | inicia F4 (P08 reificação); exercita F1/F2 como contrato (P4 DoR) | F2 completo, F3, F5, F6 (fatia é descartável) |
| **C · (futuro) Segunda cena no motor real** | prova reúso; expande F1/F2/F3 ao próximo recorte | F5/F6 (ainda não é público) |
| **D · (futuro) Caminho ao MVP público** | aciona F2, F4, F5, F6 | F7 (escala) |

**Conclusão prática:** as etapas A e B estão **inteiramente desbloqueadas**. Nenhuma pendência impede começar; o que as pendências fazem é definir o que precisa ser convertido de "registro" para "processo" quando formos da fatia ao público — e a primeira delas (a fila de revisão) já tem proposta de governança esperando ratificação.
