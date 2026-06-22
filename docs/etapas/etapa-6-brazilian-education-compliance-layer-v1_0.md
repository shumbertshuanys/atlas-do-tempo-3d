# Etapa 6 — Brazilian Education Compliance Layer

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da **Etapa 6** · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, o datum canônico da Etapa 3Z, a política editorial vinculante da Etapa 3.1, as camadas/cenas/`Scene` v1.1 (4A–4H), o handoff da Etapa 4 (4Z), a função `WhatWasHappeningAtMoment` (Etapa 5) e o backlog geral (5Z) · 13/06/2026

**Escopo desta etapa (e seus limites):** definir **conceitualmente** a camada de conformidade educacional brasileira — uma camada **externa** ao Knowledge Core que **anota, filtra, restringe, orienta e indexa**, sem nunca criar conhecimento universal nem alterar claims científicos/históricos. Conforme solicitado, esta etapa **não** cria cena nova, **não** povoa conteúdos, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** cria planejamento do professor, **não** cria planos de aula/quizzes/rubricas, **não** cria LMS, **não** cria Content Matching Engine, **não** faz pipeline de ingestão, **não** mapeia massivamente códigos BNCC, **não** promete homologação automática pelo MEC, **não** confunde alinhamento à BNCC com aprovação no PNLD, **não** trata a BNCC como origem do conteúdo e **não** contamina o Knowledge Core com campos curriculares internos.

**O que herda e respeita.** A direção única de dependência (Etapa 2, Tarefa 10 — as camadas externas apontam para o KC; o KC nunca aponta para fora); o claim-first e a proveniência obrigatória (Etapa 2 / 1.1); o invariante de exibição (nada `pending`/`legal-review`/`rejected` aparece como fato ou na simultaneidade — 1.1/3.1); os cinco níveis de exposição por faixa e as oito revisões da política editorial (3.1 §6/§9); o `Scene` v1.1 (34 campos — 4H §2); os contratos `MomentQuery`/`MomentResult` com `ageLevelMode`/`publicabilityMode`/`layerFilters` já existentes (Etapa 5); `anachronismWarnings`/`equivalenceWarnings`, `publicabilityStatus`/`gatingReason` (4H/5); a lente Brasil (`ModernCorrespondence`, D8); e o backlog do Grupo 2 (5Z §6), endereçado aqui **como requisito**, não pré-resolvido.

> **Convenção de leitura.** Entidades em `CamelCase`; campos em `camelCase`; enums como listas de valores. Blocos ```txt``` são **dicionário conceitual de campos**, nunca código executável. "A função" = a capacidade `WhatWasHappeningAtMoment` (Etapa 5). "KC" = Knowledge Core. "A camada" = a `BrazilianEducationComplianceLayer` definida na Seção 1.
>
> **Disciplina de fonte (regra desta etapa).** Diferentemente das etapas anteriores, esta exige **texto normativo confirmado em fonte oficial**: não se afirma obrigação legal de memória, não se cita código BNCC sem fonte, não se afirma "homologado pelo MEC" sem base. Quando há dúvida sobre o texto exato, marca-se `PENDENTE_CONFIRMACAO_OFICIAL`. A matriz de fontes (Seção 2) registra nome, órgão, URL, data de acesso e status de cada referência.

---

## Sumário

1. Definição da camada de conformidade brasileira (`BrazilianEducationComplianceLayer`)
2. Matriz de fontes oficiais e normativas
3. Papel da BNCC e entidades de indexação
4. LDB e natureza do produto
5. LGPD e proteção de menores
6. Acessibilidade e uso escolar
7. Faixa etária, linguagem e exposição
8. Conteúdos sensíveis e Leis 10.639/2003 e 11.645/2008
9. Conteúdo fora da grade: exploração livre e aprofundamento
10. Modelo de anotação de conformidade
11. Relação com `WhatWasHappeningAtMoment`
12. Escolas públicas e privadas
13. Riscos jurídicos, educacionais e comerciais
14. Fronteiras com etapas futuras
15. Próximos passos para a Etapa 7

---

## 1. Definição da camada de conformidade brasileira (Tarefa 1)

### 1.1 O que é

A `BrazilianEducationComplianceLayer` é a camada **externa** que torna o produto **compatível com a educação brasileira** — BNCC, LDB, LGPD, ECA, acessibilidade (e-MAG/WCAG/LBI), Leis 10.639/2003 e 11.645/2008, proteção de menores e uso escolar responsável — **sem** transformar o currículo em origem do conhecimento e **sem** contaminar o Knowledge Core.

Ela não é parte do núcleo. É uma camada de **leitura, anotação, indexação, restrição e orientação** que se acopla por fora, pela mesma direção única de dependência já fixada na Etapa 2 (Tarefa 10):

```
   Experience → Output → Matching → Planning → COMPLIANCE (esta camada) → Knowledge Core
        (cada camada aponta para dentro; o KC não conhece nenhuma delas)
```

### 1.2 Objetivo e função

| Aspecto | Definição |
|---|---|
| **Objetivo** | Permitir que o mesmo Knowledge Core universal seja usado de forma **legalmente conforme, pedagogicamente adequada e segura** na educação básica brasileira, preservando a tese da Etapa 0 (conhecimento universal primeiro; currículo organiza o uso; professor define foco; o mundo inteiro permanece navegável). |
| **Função** | Quatro verbos, **todos externos**: **anotar** (acrescentar metadados de conformidade que apontam para `knowledgeItemId`/`claimId`/`Scene`/`MomentResult`), **filtrar** (selecionar o que é exibível por faixa/contexto sobre a saída da função), **restringir** (impor mediação/ocultação/aviso por faixa etária e tema sensível), **orientar** (sinalizar alinhamento BNCC, adequação etária, requisitos de acessibilidade e necessidade de revisão). |
| **Entradas (consome)** | (a) o KC por `knowledgeItemId`/`claimId`; (b) o `MomentResult` e o `generatedSceneCandidate` (Etapa 5); (c) o `Scene` v1.1 (4H); (d) os cinco níveis de exposição e as oito revisões da política editorial (3.1); (e) o invariante de exibição e os limites de licença (1.1); (f) o `canonicalTimeScalar` (3Z); (g) `publicabilityStatus`/`gatingReason`/`anachronismWarnings`/`equivalenceWarnings`; (h) o **texto normativo oficial** brasileiro (Seção 2). |
| **Saídas (produz)** | Entidades de anotação externas (Seção 10): `ComplianceProfile`, `ComplianceAnnotation`, `CurricularAlignment`, `AgeSuitability`, `AccessibilityRequirement`, `SensitiveContentRule`, `LegalRequirement`, `BrazilianEducationConstraint`, `SchoolUseMode`, `AllowedUseContext`; e um **índice BNCC** (Seção 3) — todas apontando para o KC/saída por identificador. |

### 1.3 O que a camada **nunca** faz

- **Nunca** cria, edita ou completa `Claim`, `ClaimSet`, `Source`, `Citation`, `Event`, `Process`, `State`, `Relationship` ou qualquer fato.
- **Nunca** altera `claimType`, `confidenceLevel`, `evidenceLevel`, `UncertaintyProfile`, `reviewStatus` ou `ProvenanceMetadata`.
- **Nunca** transforma a BNCC em origem do conteúdo (a BNCC **referencia** o KC; não o cria — P1/P2 da Etapa 2).
- **Nunca** insere campo curricular, de série, de aluno ou de aula dentro do KC.
- **Nunca** relaxa o invariante de exibição: se um item está `pending`/`legal-review`/`rejected`, a camada não o "libera".
- **Nunca** converte exploração livre em obrigação curricular (preserva o duplo caminho — D3).

### 1.4 Como se conecta a cada peça do sistema

- **Ao Knowledge Core.** Leitura pura por `knowledgeItemId`/`claimId`. A camada mantém **seus próprios registros** que apontam para o núcleo (ex.: um `BNCCMapping` liga uma habilidade a itens do KC); o KC não sabe que esses registros existem. Apagar a camada inteira não deixa campo órfão no núcleo (teste de P2).
- **À função `WhatWasHappeningAtMoment`.** A camada é **leitora/anotadora do `MomentResult`** (detalhe na Seção 11). Ela **usa** os campos `ageLevelMode` e `publicabilityMode` que a função **já** expõe (Etapa 5 §3) — **não os redefine** — e acrescenta tags de conformidade sobre os itens já retornados, sem reordenar a verdade do núcleo.
- **Ao `Scene` v1.1.** A cena já traz `centralItems`/`contextualItems`/`sensitiveItems`/`hiddenItems`/`reviewStatus`/`publicabilityStatus`/`gatingReason` — classificações **editoriais/estruturais**. A camada **acrescenta por fora** a leitura **curricular e etária** (curricularCore/contextual/enrichment/freeExploration/teacherMediated/restricted/hidden — Seção 9) como anotação que aponta para o `id` da cena, sem editar a cena.
- **Ao futuro Teacher/School Planning Layer (Etapa 7).** O planejamento do professor (ano, disciplina, bimestre, temas, objetivos, profundidade) entrará na Etapa 7 e **alimentará** os filtros desta camada (ex.: "qual `EducationStage`/`SubjectArea` aplicar"). A camada fornece a **gramática de conformidade**; a Etapa 7 fornece o **foco prático**.
- **Ao futuro Pedagogical Output Layer (Etapa 9).** Planos, atividades, quizzes e rubricas (Etapa 9) **consumirão** as anotações desta camada (alinhamento BNCC, adequação etária, mediação obrigatória) para montar saídas conformes — sempre citando claims do KC, nunca inventando fatos (A3/Q5).

### 1.5 Posição perante o duplo caminho de consumo (D3)

A Etapa 0 fixou dois caminhos: o **fluxo do professor** (atravessa Compliance → Planning → Matching → Output → Experience) e a **exploração livre** (vai do KC direto à experiência, com a conformidade atuando **apenas** como filtro de adequação — idade/linguagem/sensibilidade). Esta camada respeita ambos:

- no **fluxo do professor**, ela aplica alinhamento curricular + adequação etária + acessibilidade + mediação;
- na **exploração livre**, ela aplica **somente** o filtro de adequação (faixa, sensibilidade, acessibilidade), **sem** travar por grade — o aluno pode navegar o mundo inteiro no mesmo momento, dentro do que é adequado à sua faixa.

---

## 2. Matriz de fontes oficiais e normativas (Tarefa 2)

Classificação de status: **oficial** = norma/portal de órgão competente; **complementar** = norma derivada/diretriz que apoia a aplicação; **interpretativo** = guia/orientação que ajuda a aplicar, sem força de lei própria; **pendente** = a confirmar (`PENDENTE_CONFIRMACAO_OFICIAL`). Data de acesso de todas: **13/06/2026**.

| # | Fonte | Órgão | Tipo | Status | URL | Uso no projeto | Risco de interpretação | Obrigatória/Recomendável |
|---|---|---|---|---|---|---|---|---|
| F1 | **BNCC — Base Nacional Comum Curricular** (portal e documentos homologados) | MEC / CNE | Base curricular normativa | oficial | https://basenacionalcomum.mec.gov.br/ · https://www.gov.br/mec/pt-br/cne/base-nacional-comum-curricular-bncc | Indexação curricular externa (Seção 3); referência para `BNCCMapping`/`CurricularAlignment` | Tratar a BNCC como **origem** do conteúdo; mapear códigos sem o texto homologado | Obrigatória (alinhamento) |
| F2 | **Resolução CNE/CP nº 2, de 22/12/2017** (institui a BNCC — EI/EF) | CNE | Resolução | oficial | https://www.gov.br/mec/pt-br/cne/base-nacional-comum-curricular-bncc | Marco de homologação EI/EF (20/12/2017) | Confundir resolução com homologação automática do produto | Obrigatória (referência) |
| F3 | **Resolução CNE/CP nº 4, de 17/12/2018** (institui a BNCC — Ensino Médio) | CNE | Resolução | oficial | https://www.gov.br/mec/pt-br/cne/base-nacional-comum-curricular-bncc | Marco de homologação do EM (14/12/2018) | — | Obrigatória (referência) |
| F4 | **LDB — Lei nº 9.394, de 20/12/1996** | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/leis/l9394.htm | Natureza do produto (Seção 4); Art. 26 (base comum + parte diversificada); Art. 26-A | Ler "recurso complementar" como "currículo" | Obrigatória |
| F5 | **Lei nº 10.639, de 9/01/2003** (História e Cultura Afro-Brasileira; altera a LDB, Art. 26-A) | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.639.htm | Cobertura/protagonismo afro-brasileiro e africano (Seção 8) | Tratar como nota de rodapé em vez de cobertura estrutural | Obrigatória |
| F6 | **Lei nº 11.645, de 10/03/2008** (História e Cultura Afro-Brasileira e Indígena; altera o Art. 26-A) | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11645.htm | Cobertura/protagonismo indígena (Seção 8) | Apagamento ou homogeneização indígena | Obrigatória |
| F7 | **DCN — Educação das Relações Étnico-Raciais** (Resolução CNE/CP nº 1/2004 + Parecer CNE/CP nº 3/2004) | CNE | Diretriz | complementar | http://portal.mec.gov.br/dmdocuments/cnecp_003.pdf | Orienta linguagem antirracista e abordagem (Seção 8) | Aplicar sem o texto da norma | Recomendável (forte) |
| F8 | **LGPD — Lei nº 13.709, de 14/08/2018** (esp. Art. 14 — dados de crianças e adolescentes) | Presidência / Congresso / ANPD | Lei | oficial | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | Proteção de menores e dados (Seção 5) | Coletar dados de aluno; ignorar consentimento parental/minimização | Obrigatória |
| F9 | **ECA — Lei nº 8.069, de 13/07/1990** | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/leis/l8069.htm | Define criança (até 12 incompletos) e adolescente (12–18); proteção integral | Confundir faixa etária legal com faixa pedagógica | Obrigatória |
| F10 | **Marco Civil da Internet — Lei nº 12.965, de 23/04/2014** | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm | Guarda de logs/registros e privacidade (Seção 5) | — | Obrigatória |
| F11 | **e-MAG — Modelo de Acessibilidade em Governo Eletrônico (v3.1; Portaria SLTI/MP nº 3/2007)** | gov.br / Governo Digital | Guia técnico | oficial (vinculante para sítios gov.; referência para o produto) | https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade · https://emag.governoeletronico.gov.br/ | Requisitos de acessibilidade (Seção 6) | Confundir referência técnica com homologação | Recomendável (e exigível em compra pública) |
| F12 | **WCAG 2.x — Web Content Accessibility Guidelines** | W3C/WAI | Referência técnica internacional | complementar | https://www.w3.org/WAI/standards-guidelines/wcag/ | Base internacional de acessibilidade web (Seção 6) | — | Recomendável |
| F13 | **LBI — Lei nº 13.146, de 6/07/2015** (Lei Brasileira de Inclusão; acessibilidade de sítios — Art. 63) | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm | Obrigação legal de acessibilidade digital (Seção 6) | — | Obrigatória |
| F14 | **Decreto nº 5.296, de 2/12/2004** (regulamenta acessibilidade) | Presidência | Decreto | oficial | https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm | Base regulatória de acessibilidade (Seção 6) | — | Obrigatória (poder público) |
| F15 | **PNLD — Programa Nacional do Livro e do Material Didático** (portal e plataforma de avaliação) | MEC (SEB) / FNDE | Programa público | oficial | https://www.gov.br/mec/pt-br/pnld · https://pnld-avaliacao.mec.gov.br/ | **Diferenciar** alinhamento à BNCC de aprovação no PNLD (Seções 4 e 13) | Prometer "aprovado pelo PNLD"; confundir programa com alinhamento | Recomendável (apenas como referência) |
| F16 | **PNED — Política Nacional de Educação Digital — Lei nº 14.533, de 11/01/2023** | Presidência / Congresso | Lei | oficial | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14533.htm | Posicionamento como recurso educacional digital; fomento a repositórios (Seção 4) | Atribuir obrigações curriculares vetadas | Recomendável (contexto) |
| F17 | **ANPD — orientações sobre tratamento de dados de crianças e adolescentes** | ANPD | Guia orientativo | interpretativo / `PENDENTE_CONFIRMACAO_OFICIAL` (confirmar URL e versão vigente) | https://www.gov.br/anpd/ | Apoio à interpretação do Art. 14 da LGPD (Seção 5) | Tratar guia como lei; usar versão desatualizada | Recomendável |
| F18 | **DCN — Educação Escolar Indígena e Educação Escolar Quilombola** (Parecer CNE/CEB nº 16/2012 e correlatas) | CNE | Diretriz | complementar / `PENDENTE_CONFIRMACAO_OFICIAL` (consolidar referências vigentes) | http://portal.mec.gov.br/ | Cobertura de povos indígenas e comunidades quilombolas (Seção 8) | Aplicar sem texto vigente | Recomendável |

> **Regra de uso da matriz.** Toda anotação de conformidade que dependa de obrigação legal **cita** a fonte correspondente (F1–F18) em seu campo `legalBasisRef`. Sem fonte oficial, a anotação nasce `PENDENTE_CONFIRMACAO_OFICIAL` e **não** é tratada como obrigação. Itens marcados `PENDENTE_CONFIRMACAO_OFICIAL` exigem leitura do texto vigente antes de virarem requisito firme.

---

## 3. Papel da BNCC e entidades de indexação (Tarefa 3)

### 3.1 O papel correto da BNCC

A BNCC é um documento **de caráter normativo** que define as aprendizagens essenciais de toda a educação básica e, por força da LDB (Lei 9.394/1996), deve **nortear os currículos** das redes públicas e privadas (F1/F4). Três consequências para o projeto:

1. **A BNCC não é a origem do conteúdo.** O conhecimento existe no Knowledge Core independentemente dela: o fato de o Jurássico começar em ~201,4 Ma ou de a Queda da Bastilha ser de 14/07/1789 não vem da BNCC. A BNCC pode mudar; o KC permanece (P1/P2).
2. **A BNCC é camada de conformidade, indexação e orientação.** Ela **aponta para** `knowledgeItemId`, `claimId`, `Scene` e `MomentResult` por referência externa — nunca o contrário.
3. **A própria BNCC distingue aprendizagem de método.** O documento oficial estabelece que as habilidades **não** descrevem condutas do professor nem induzem metodologias; essas escolhas pertencem aos **currículos e projetos pedagógicos** de cada rede/escola. Isso confirma a tese do projeto: o conhecimento é universal, **o currículo organiza o uso, o professor define o foco**. Conteúdos fora da grade podem existir como exploração livre, contexto ou aprofundamento (Seção 9), sem virar obrigação curricular.

A estrutura documentada da BNCC (F1) é: **10 competências gerais** (transversais a toda a educação básica) → **competências específicas** (por área e componente) → **habilidades** (ligadas a **objetos de conhecimento**), além dos **campos de experiência** na Educação Infantil. Cada habilidade tem um **código alfanumérico** padronizado: etapa (`EF`/`EM`/`EI`) + ano ou bloco de anos + componente/área (ex.: `HI` História, `GE` Geografia, `CI` Ciências) + número sequencial (ex.: `EF04MA10` = 10ª habilidade de Matemática do 4º ano). No Ensino Médio, o código usa o par `13` ("qualquer série"), a sigla da área (`CHS`, `CNT`, `LGG`, `MAT`, `LP`) e a competência específica + sequência.

### 3.2 Entidades conceituais externas (vivem na camada, não no KC)

> **Regra vinculante (Tarefa 3).** Esta etapa **não** mapeia códigos BNCC em massa. Define o **modelo** e as **regras de mapeamento**. O mapeamento concreto é trabalho de curadoria curricular posterior, sempre com proveniência (o texto homologado da BNCC, F1) e `reviewStatus`.

| Entidade | Finalidade | Campos mínimos | Relação com o KC | Fonte oficial | Status de revisão | Risco se mal usada |
|---|---|---|---|---|---|---|
| `BNCCCompetency` | Representar uma das 10 competências gerais (ou específica de área) | `competencyId`, `scope` (geral/área), `area?`, `officialText`, `legalBasisRef` (F1) | Não referencia o KC diretamente; agrega `BNCCSkill` | F1 | `pending` até conferência com texto homologado | Resumir/parafrasear o texto oficial como se fosse o oficial |
| `BNCCSkill` | Representar uma habilidade (código alfanumérico) | `skillCode` (ex.: `EF08HI06`), `stage`, `yearOrBlock`, `componentOrArea`, `officialText`, `relatedKnowledgeObjects[]`, `legalBasisRef` (F1) | Indireta: via `BNCCMapping` | F1 | `pending` (texto e código exigem confirmação) | Citar código sem o texto homologado |
| `BNCCKnowledgeObject` | Objeto de conhecimento associado a habilidades | `knowledgeObjectId`, `label`, `componentOrArea`, `skills[]` | Indireta: ponte temática para `themeTags` do KC | F1 | `pending` | Confundir objeto de conhecimento (currículo) com `Concept` (KC) |
| `BNCCMapping` | **Ligar** uma `BNCCSkill` a itens do KC (`knowledgeItemId`/`claimId`/`Scene`) | `mappingId`, `skillCodeRef`, `knowledgeItemRefs[]`, `claimRefs[]?`, `sceneRefs[]?`, `mappingRationale`, `provenanceRef` (F1), `reviewStatus` | **Aponta para** o KC; o KC não conhece o mapeamento | F1 | `pending` (curadoria curricular) | Inverter a direção (fazer o KC depender da BNCC) |
| `EducationStage` | Etapa escolar (EI, EF I, EF II, EM) | `stageId`, `label`, `ageRangeApprox`, `legalBasisRef` (F4) | Nenhuma (qualifica anotações) | F4 | aprovável | Tratar etapa como filtro absoluto da exploração livre |
| `SchoolYearBand` | Faixa de ano/série (ex.: 8º–9º ano) | `bandId`, `stageRef`, `yearsCovered`, `ageRangeApprox` | Nenhuma | F4 | aprovável | — |
| `SubjectArea` | Área/componente (História, Geografia, Ciências, …) | `subjectId`, `label`, `bnccAreaRef?` | Mapeia para `themeTags` do KC por correspondência, não por contaminação | F1/F4 | aprovável | Forçar disciplina como recorte único (o KC é interdisciplinar) |
| `AgeLanguageProfile` | Perfil de linguagem/profundidade por faixa (consome 3.1 §6) | `profileId`, `bandRef`, `language`, `depth`, `abstraction`, `mediaExposure`, `mediationRules`, `editorialPolicyRef` (3.1) | Modula a **saída** (via `ageLevelMode`), nunca o claim | 3.1 + F4 | aprovável | Alterar o fato em vez da forma |
| `ComplianceAnnotation` | Anotação genérica de conformidade que aponta para o KC/saída | `annotationId`, `targetRef` (`knowledgeItemId`/`claimId`/`Scene`/`MomentResult`), `annotationType`, `payload`, `legalBasisRef?`, `reviewStatus` | **Aponta para** o KC/saída; nunca o edita | F1–F18 conforme o tipo | conforme o tipo | Usar a anotação para "corrigir" um claim |

---

## 4. LDB e natureza do produto (Tarefa 4)

### 4.1 O que a LDB exige, em termos gerais

A LDB (Lei 9.394/1996, F4) estabelece, no **Art. 26**, que os currículos da educação infantil, do ensino fundamental e do ensino médio devem ter uma **base nacional comum**, a ser **complementada**, em cada sistema e escola, por uma **parte diversificada** exigida pelas características regionais e locais da sociedade, da cultura, da economia e dos educandos; o **Art. 26-A** (com a redação das Leis 10.639/2003 e 11.645/2008) torna obrigatório o estudo de história e cultura afro-brasileira e indígena no fundamental e no médio, em escolas públicas e privadas. O **currículo concreto** é construído por cada rede/escola; a BNCC é o **parâmetro** comum (F1).

### 4.2 Como o produto deve ser posicionado

Conforme D1 da Etapa 0, o produto é tratado como **recurso de apoio**, nunca como currículo. Posicionamentos válidos e simultâneos:

- **recurso educacional digital complementar** (alinhado ao fomento da PNED — F16);
- **atlas científico-histórico** espaçotemporal;
- **objeto digital de aprendizagem**;
- **ferramenta interdisciplinar** e **de apoio ao professor**;
- **material paradidático digital**, quando aplicável.

E **não** como: substituto integral do currículo, do livro didático, do professor, da avaliação oficial ou da decisão pedagógica/jurídica da escola.

O produto serve **aos dois lados** do Art. 26: por um lado, **indexa-se à base comum** (BNCC, via `BNCCMapping`); por outro, **alimenta a parte diversificada** e o recorte local — a lente Brasil (`ModernCorrespondence`, D8), a exploração livre e o aprofundamento regional.

### 4.3 Por que alinhamento ≠ homologação ≠ aprovação no PNLD

Três coisas distintas, que a comunicação do produto **não** pode embaralhar:

- **Alinhamento à BNCC** é uma propriedade de **conteúdo/indexação**: o produto referencia habilidades e competências (Seção 3). Não exige ato do MEC.
- **Homologação pelo MEC** é um **ato normativo** (ex.: as Resoluções CNE/CP que instituíram a BNCC — F2/F3). O produto **não** é homologado por estar alinhado; nem promete sê-lo.
- **Aprovação no PNLD** é a passagem por um **processo público específico** (F15): inscrição em edital, avaliação pedagógica coordenada pela SEB/MEC em parceria com o FNDE, habilitação, Guia do PNLD e escolha pelas escolas. Há editais que incluem **Recursos Educacionais Digitais (RED)**. Estar alinhado à BNCC **não** equivale a estar aprovado no PNLD; a participação no PNLD, se buscada, é decisão e processo da Etapa 14, **sem** promessa de aprovação.

### 4.4 Uso por escolas públicas e privadas (visão geral; detalhe na Seção 12)

- **Públicas:** uso como recurso complementar conforme a autonomia da rede; requisitos técnicos mínimos (offline parcial, modo projetor, acessibilidade, hardware modesto — D10/A2) tratados como fundação; eventual aquisição pública (incl. PNLD) **sem** promessa de aprovação.
- **Privadas:** flexibilidade curricular, sistemas de ensino e projetos interdisciplinares; a BNCC é **base mínima**, não **limite máximo** (a exploração livre e o aprofundamento são diferenciais).

### 4.5 Cuidados de comunicação comercial (não prometer)

Não afirmar: "homologado pelo MEC"; "aprovado pelo PNLD"; "substitui o professor"; "substitui o currículo"; "dispensa avaliação pedagógica/jurídica". Afirmações permitidas (com base): "alinhado à BNCC" (quando houver `BNCCMapping` revisado); "recurso educacional digital complementar"; "compatível com a educação básica brasileira" (no sentido desta etapa). Risco e mitigação consolidados na Seção 13.

---

## 5. LGPD e proteção de menores (Tarefa 5)

### 5.1 O regime legal (fonte oficial)

A LGPD (Lei 13.709/2018, F8) trata, no **Art. 14**, dos dados de crianças e adolescentes. Em paráfrase dos comandos centrais (texto integral em F8): o tratamento deve atender ao **melhor interesse** da criança/adolescente; o tratamento de dados de **crianças** exige **consentimento específico e em destaque** de ao menos um dos pais/responsável (§1); os controladores devem manter **pública** a informação sobre tipos de dados, uso e exercício de direitos (§2); há exceção restrita para contatar os pais ou para proteção, sem armazenamento e sem repasse a terceiros (§3); é **vedado condicionar** a participação em jogos/aplicações ao fornecimento de dados **além do estritamente necessário** — princípio de **minimização** (§4); o controlador deve **verificar** razoavelmente o consentimento (§5); e as informações devem ser **simples, claras e acessíveis** (§6). O **ECA** (Lei 8.069/1990, F9) define **criança** (até 12 anos incompletos) e **adolescente** (12 a 18). A interpretação do Art. 14 é apoiada por orientações da **ANPD** (F17) e dialoga com o **Marco Civil** (F10, guarda de registros) e a **LBI** (F13). A capacidade civil dos maiores de 16 também é tema correlato.

### 5.2 Princípio de fundação: o KC não contém dado pessoal de aluno

Reafirmando a Etapa 2 (§10) e a transversal de privacidade da Etapa 0 (D2): **o Knowledge Core não armazena dados pessoais de estudante**. Pessoas **históricas** são conhecimento (`Entity`); **pessoas vivas/identificáveis** exigem `legalReview` (Seção 5.4). Nenhum dado de aluno, turma, matrícula, desempenho, navegação ou resposta entra no núcleo.

### 5.3 Onde cada dado pertence (requisitos conceituais)

| Dado | Pertence a | Tratamento conceitual |
|---|---|---|
| Dados de **estudantes** (inclui menores) | Camadas de aplicação futuras (Planning/Output/Experience) + transversal de privacidade | Fora do KC; base legal definida; minimização; consentimento parental p/ crianças (§1); melhor interesse (caput) |
| Dados de **professores** | Camadas de aplicação | Fora do KC; base legal; minimização |
| Dados de **escolas** | Camadas de aplicação | Fora do KC; contrato/base legal |
| Idade/faixa etária | Aplicação | Usada como **parâmetro de adequação** (`ageLevelMode`), idealmente sem coletar idade exata quando o uso for coletivo/mediado |
| Registros de uso, analytics, histórico de navegação, respostas geradas | Telemetria ética (transversal) | Minimização, retenção definida, finalidade explícita; sem perfilamento de menor além do necessário |
| Personalização | Aplicação futura | Decisão de E11/E12; para menores, cautela redobrada |
| Uso de IA (assistente pedagógico/linguagem) | Output Layer (E9) | Sempre **rotulada**; nunca fonte factual; nunca cria/edita claim (A3/Q5); não treina com dados de menores sem base e revisão |

### 5.4 O que exige `legalReview`

- **Pessoas vivas e eventos contemporâneos** (P26 do backlog) — `legalReview` obrigatório; itens como a ditadura militar brasileira migram para `legal-review` (3.1 §10.10).
- Qualquer **dado pessoal** que, por erro de modelagem, ameace entrar no KC.
- Qualquer **mídia** que toque pessoas identificáveis sem base/licença.

### 5.5 O que evitar no MVP e o que fica para etapas futuras

- **Evitar no MVP:** coletar dados de aluno; criar contas de menores sem base legal e consentimento; analytics intrusivo; personalização baseada em perfil de menor.
- **Decisões de E11 (arquitetura)/E12 (MVP)/E14 (jurídico/comercial):** base legal e fluxo de consentimento; modelo de contas (escola como controladora? operadora?); retenção, exclusão, segurança, logs (Marco Civil); DPIA/Relatório de Impacto quando aplicável; eventual uso de IA com salvaguardas para menores.

> **Regra-síntese (Tarefa 5).** O Knowledge Core é **universal e impessoal**; LGPD e proteção de menores são **requisitos de fundação** das camadas de aplicação, endereçados aqui como requisitos (P25) e detalhados na arquitetura/jurídico.

---

## 6. Acessibilidade e uso escolar (Tarefa 6)

### 6.1 Referências (fonte oficial)

Acessibilidade digital no Brasil ancora-se em: **e-MAG** (Modelo de Acessibilidade em Governo Eletrônico, v3.1, institucionalizado pela Portaria SLTI/MP nº 3/2007 — F11), **alinhado** ao **WCAG** do W3C (F12) mas com padrões próprios para o contexto brasileiro; **LBI** (Lei 13.146/2015 — F13), que torna a acessibilidade de sítios/aplicações uma **obrigação legal**; e o **Decreto 5.296/2004** (F14). O e-MAG é **vinculante para sítios do governo** e **exigível em compras públicas**; para o produto, é **referência técnica** somada à obrigação da LBI.

### 6.2 Requisitos conceituais de acessibilidade

| Requisito | Descrição | Vínculo |
|---|---|---|
| Leitores de tela | Estrutura semântica, `alt`/descrições, ARIA quando necessário | e-MAG/WCAG/LBI |
| Navegação por teclado | Foco visível (borda ≥ 2px), ordem lógica, sem armadilhas de foco | e-MAG/WCAG |
| Contraste | Razões de contraste mínimas; texto legível | WCAG |
| Legendas e transcrições | Para vídeo/áudio | WCAG/LBI |
| **Descrição textual de mapas e cenas** | Toda `Scene`/globo/mapa tem equivalente textual (o que aconteceu, onde, quando, com que confiança) | e-MAG/WCAG + Etapa 3 |
| Movimento reduzido | Respeitar `prefers-reduced-motion`; alternativa estática | WCAG |
| Modo 2D / estático / projetor | Degradação progressiva (3D → 2D → cartões) e modo projetor | Etapa 3 / D10 |
| Hardware modesto / conexão instável / offline parcial | Funcionar fora de banda larga; pacotes offline | D10/A2 (P22/P23) |
| Linguagem clara | Texto adequado por faixa (Seção 7) | e-MAG (linguagem simples) |
| **Rótulos não dependentes só de cor** | Os rótulos epistêmicos (fato/inferência/hipótese/reconstrução; níveis de confiança) usam **redundância não-cromática** (ícone/forma/texto), não apenas cor | Etapa 3 §8.3 / 3.1 |

### 6.3 Conexão com as decisões da Etapa 3

A Etapa 3 já definiu os modos de degradação: **3D completo → 2D → estático → offline parcial → modo projetor**, preservando, em qualquer modo, o **mínimo de tempo, espaço, fontes, simultaneidade, dossiê e incerteza**. A camada de conformidade **transforma isso em requisito de aceitação**: nenhuma vista pode descartar a equivalência textual nem os rótulos com redundância não-cromática; a acessibilidade é **fundação**, não enfeite (P24).

> **Limite (Tarefa 6).** Esta seção define **requisitos**, não telas. A UX final (foco, layout, componentes acessíveis concretos) é da Etapa 10; a verificação técnica (e-MAG/WCAG, ASES) e a auditoria de acessibilidade são da Etapa 11/14.

---

## 7. Faixa etária, linguagem e exposição (Tarefa 7)

### 7.1 Consumo da política editorial (3.1) e mapeamento etário

A camada **consome** os cinco níveis de exposição da Etapa 3.1 (§6) e os **mapeia** para `EducationStage`/`SchoolYearBand` brasileiros, via `AgeLanguageProfile`. Respeita D9 (V1 foca **EF II + EM**; arquitetura nasce universal, então EI e EF I já ficam previstos).

| Perfil (3.1) | Etapa BR aproximada | Linguagem | Profundidade / abstração | Exposição de imagem |
|---|---|---|---|---|
| 6–8 anos | Educação Infantil / início EF I | Muito acessível, frases curtas, sem jargão | Noções concretas; sem números abstratos grandes sem âncora | Apenas não-gráfica; sem violência/morte explícita |
| 9–11 anos | EF I | Acessível; termos sensíveis explicados ao introduzir | Causas/consequências simples; primeira simultaneidade | Históricas suaves, rotuladas; nada gráfico |
| 12–14 anos | EF II | Termos sensíveis explicados; introduz disputa terminológica | Processos; `ClaimSet` simplificado | Históricas rotuladas; gráfico forte oculto por padrão |
| 15–17 anos | Ensino Médio | Próxima da acadêmica, ainda didática | Complexidade plena adequada à escola; pluralidade | Difíceis com rótulo/contexto; gráfico extremo ainda mediado |
| Professor/pesquisador | Docente | Acadêmica; aparato crítico completo | Integral; `ClaimSet` integral, notas editoriais | Acesso pleno (com rótulos e licença), p/ preparação |

### 7.2 Tratamento por tema, por faixa (modula a forma, nunca o fato)

Para cada faixa, a camada define **linguagem, exposição, mediação obrigatória, itens ocultos/resumidos e itens só em modo professor** — sempre **sobre a forma**, jamais alterando o fato (PE-Ed8). Diretrizes herdadas de 3.1:

| Tema | 6–8 | 9–11 | 12–14 (EF II) | 15–17 (EM) | Professor |
|---|---|---|---|---|---|
| Violência histórica | Oculta | Suave, mediada | Rotulada; gráfico oculto | Difícil com aviso/contexto | Pleno |
| Escravidão | Noção, forte mediação | Mediação; "pessoas escravizadas" | Sistema + resistência; gráfico oculto | Pluralidade; gráfico só com aviso (15+) | Aparato + mediação sugerida |
| Povos indígenas | Diversidade/presença, concreto | Etnônimos; presente e passado | Profundidade; disputa de povoamento como hipótese | Pluralidade; agência | Pleno |
| Raça e ciência | — (idade-apropriado) | Combater estereótipo | Explicar por que "raça" não é categoria biológica | Idem, com aparato | **Revisão obrigatória** |
| Evolução humana | Noção de mudança | Fato; sem hierarquia | Fato + debates internos | Idem, vigilância anti-racista | Pleno |
| Mudanças climáticas | Noção concreta | Causa humana, simples | Consenso afirmado; incerteza como faixa | Projeções como faixa, sem falsa equivalência | Aparato (IPCC etc.) |
| Ditaduras e política | — | Contexto simples | Repressão nomeada com fonte; mediação | Pluralidade só onde legítima | Aparato; **`legal-review`** p/ pessoas vivas |

### 7.3 Como a faixa opera tecnicamente

A modulação ocorre **sobre a saída** via `ageLevelMode` da `MomentQuery` (Etapa 5) — a função já modula profundidade/linguagem/mídia por faixa; a camada acrescenta as regras brasileiras (mediação obrigatória por tema sensível, itens ocultos por faixa) como `AgeSuitability`/`SensitiveContentRule`. A **adaptação de linguagem** por faixa é feita pela camada auxiliar de IA **sobre o conteúdo curado**, rotulada, sem inventar fatos (A3/Q5).

> **Regra de ouro (Tarefa 7).** A faixa etária modula **linguagem e exposição**; **não altera** o fato histórico/científico. Na dúvida, **sobe-se o nível de cuidado** (mais mediação, mais aviso, ocultação por padrão) — nunca se assume maturidade não confirmada (PE-Ed4).

---

## 8. Conteúdos sensíveis e Leis 10.639/2003 e 11.645/2008 (Tarefa 8)

### 8.1 Base legal (fonte oficial)

A **Lei 10.639/2003** (F5) alterou a LDB (Art. 26-A) para tornar **obrigatório** o estudo de **História e Cultura Afro-Brasileira**, e instituiu o **20 de novembro** como Dia da Consciência Negra no calendário escolar. A **Lei 11.645/2008** (F6) ampliou a obrigatoriedade para incluir a **História e Cultura Indígena** e fixou (em paráfrase do Art. 26-A) que, em escolas **públicas e privadas** de ensino fundamental e médio, o conteúdo abrange a história da África e dos africanos, a luta de negros e povos indígenas no Brasil, e suas contribuições sociais, econômicas e políticas, ministrado **ao longo de todo o currículo**, em especial em arte, literatura e história brasileiras. As **DCN das Relações Étnico-Raciais** (Resolução CNE/CP nº 1/2004 — F7) e as diretrizes de **Educação Escolar Indígena/Quilombola** (F18) orientam a aplicação.

### 8.2 Como a camada trata conteúdos sensíveis

Estes temas — história/cultura afro-brasileira, africana, diáspora, escravidão, racismo, povos indígenas, colonização, violência colonial, genocídios, ditaduras, religião, guerra, raça e ciência, evolução humana, mudanças climáticas, pandemias, eventos contemporâneos — já têm **tratamento factual e editorial** definido na Etapa 3.1 (§4, §5, §10) e populado na Etapa 4 sob aquela política. **A camada de conformidade não recria isso**; ela **(a)** marca a **cobertura obrigatória** (Leis 10.639/11.645) como requisito curricular via `CurricularAlignment`/`SensitiveContentRule`, e **(b)** aciona o **fluxo de revisão** (3.1 §9) e o invariante de exibição.

Diretrizes (herdadas de 3.1, ancoradas nas leis):

- **Evitar eurocentrismo:** a função `WhatWasHappeningAtMoment` é o antídoto estrutural — mostra África, Ásia, Américas e povos indígenas **em simultaneidade** com a Europa, não como nota de rodapé.
- **Evitar apagamento indígena:** etnônimos e autodenominações; presença **contemporânea** e **história profunda** (povoamento, sambaquis, marajoara — D8); não "povos do passado".
- **Evitar naturalizar a escravidão:** "pessoas escravizadas"; nomear o sistema sem eufemismo; protagonismo, resistência e quilombos (Lei 10.639).
- **Evitar falsa equivalência:** negacionismo (incl. negação de genocídio) **não** é "lado"; entra como objeto rotulado-rejeitado, fora do `ClaimSet` (3.1 §3.4; `equivalenceWarnings`).
- **Preservar agência histórica:** povos afetados como **sujeitos**, não apenas vítimas.
- **Fontes orais/tradições:** reconhecidas como evidência legítima, com `evidenceLevel` próprio e atribuição.
- **Termos históricos hoje problemáticos:** exibidos com aspas, data e nota ("o termo usado à época era X; hoje considera-se inadequado por Y"); nomes coloniais como `nameVariants[]` datadas, com o nome originário em primeiro plano.
- **Modulação por idade:** Seção 7 (a forma muda; o fato não).
- **Mediação do professor:** obrigatória para colonização, escravidão, povos indígenas, genocídio, ditadura, racismo nas faixas menores (3.1 §2/§4).
- **Revisão humana/jurídica:** obrigatória para os temas marcados em 3.1 (escravidão, colonização, povos indígenas, ditadura, raça e ciência) e `legal-review` para pessoas vivas/contemporâneo (P14/P26).

### 8.3 Efeito de conformidade

As Leis 10.639/11.645 transformam-se, na camada, em **exigência de cobertura e protagonismo**: ao indexar as áreas de História/Geografia/Cultura, a camada marca os itens afro-brasileiros, africanos e indígenas como `curricularCore` onde aplicável (não `enrichment` opcional) e exige que a presença/agência desses conteúdos seja **estrutural** — coerente com 3.1 §11.5 e com a função de simultaneidade.

---

## 9. Conteúdo fora da grade: exploração livre e aprofundamento (Tarefa 9)

### 9.1 O princípio

O sistema permite que aluno/professor naveguem **o mundo inteiro no mesmo momento** histórico/científico, mesmo que nem tudo esteja na grade daquele ano. Isso é diferencial do produto (D8/A6) e **não** pode virar obrigação curricular. A camada distingue **sete classes de contexto de uso** (`AllowedUseContext`), aplicadas por **anotação externa** sobre itens e cenas:

| Classe (`AllowedUseContext`) | Significado | Efeito |
|---|---|---|
| `curricularCore` | Conteúdo central da grade/etapa (incl. cobertura obrigatória das Leis 10.639/11.645) | Indexado à BNCC; recomendado no fluxo do professor |
| `contextual` | Contexto que enriquece o foco (o que mais acontecia no mundo naquele momento) | Aparece como contexto; não vira obrigação |
| `enrichment` | Aprofundamento opcional para quem quiser ir além | Disponível; sinalizado como extra |
| `freeExploration` | Navegação autônoma do aluno/professor | Vai do KC à experiência só com filtro de adequação |
| `teacherMediated` | Requer mediação do professor (tema sensível/faixa) | Exibição condicionada à mediação |
| `restricted` | Restrito por idade/revisão (aguardando revisão ou inadequado à etapa) | Oculto/indisponível na faixa |
| `hidden` | Não exibível (invariante de exibição: `pending`/`legal-review`/`rejected`) | Nunca aparece como fato |

### 9.2 Exemplo canônico

Professor ensina **Revolução Francesa** no 8º/9º ano. A camada marca:

- **`curricularCore`**: França e 1789 (foco da aula; indexado à BNCC de História — `BNCCMapping` revisado);
- **`contextual`**: Inconfidência Mineira, EUA sob a nova Constituição, Lavoisier (ciência), economia atlântica de 1789;
- **`enrichment` / `freeExploration`**: Brasil colonial, África (reinos contemporâneos), China Qing, Império Otomano, povos indígenas das Américas em 1789;
- **`teacherMediated`**: itens sensíveis (escravidão/colonização) conforme a faixa;
- nada disso **obriga** a turma — é **contexto/exploração**, preservando a grade como **foco**, não **limite**.

> **Regra (Tarefa 9).** Exploração livre **≠** obrigação curricular. A grade define o **foco** da aula; o sistema mantém o **universo** navegável. A marcação é **anotação externa** (`AllowedUseContext`), nunca campo do KC.

---

## 10. Modelo de anotação de conformidade (Tarefa 10)

Todas as entidades abaixo **vivem na camada de conformidade**, apontam para o KC/saída por identificador e **nunca** alteram claims.

| Entidade | Finalidade | Campos principais | Relação (aponta para) | Fonte oficial | `reviewStatus` | Risco | Exemplo |
|---|---|---|---|---|---|---|---|
| `ComplianceProfile` | Perfil de conformidade aplicável a um contexto (rede/escola/etapa) | `profileId`, `stageRef`, `region?`, `accessibilityLevel`, `ageProfileRef`, `policyRefs[]` | `EducationStage`, `AgeLanguageProfile` | F1/F4/F11/F13 | aprovável | Tratar perfil como trava da exploração livre | "Perfil EF II, rede pública, e-MAG/WCAG AA, offline parcial" |
| `ComplianceAnnotation` | Anotação genérica sobre item/claim/cena/resultado | `annotationId`, `targetRef`, `annotationType`, `payload`, `legalBasisRef?`, `reviewStatus` | `knowledgeItemId`/`claimId`/`Scene`/`MomentResult` | conforme tipo | conforme tipo | "Corrigir" um claim por anotação | Marca de mediação obrigatória num item de escravidão |
| `CurricularAlignment` | Alinhamento a habilidade/competência BNCC | `alignmentId`, `targetRef`, `bnccSkillRef`/`bnccCompetencyRef`, `rationale`, `provenanceRef` (F1), `reviewStatus` | KC + `BNCCSkill`/`BNCCCompetency` | F1 | `pending` (curadoria) | Mapear código sem texto oficial | `evt:revolucao-francesa` ↔ habilidade de História do 8º ano (a confirmar) |
| `AgeSuitability` | Adequação etária de um item/cena | `suitabilityId`, `targetRef`, `bandRef`, `exposureLevel`, `mediationRequired`, `hiddenInBands[]` | KC/`Scene` + `SchoolYearBand` | 3.1 + F4/F9 | aprovável | Confundir adequação com alteração de fato | "Cena 1789: 12+ com mediação; gráfico do Terror oculto < 15" |
| `AccessibilityRequirement` | Requisito de acessibilidade aplicável | `requirementId`, `targetRef?`, `wcagRef?`, `emagRef?`, `description` | KC/`Scene`/UI (E10) | F11/F12/F13/F14 | aprovável | Tratar como enfeite opcional | "Mapa exige equivalente textual + rótulo não-cromático" |
| `SensitiveContentRule` | Regra de tratamento de conteúdo sensível | `ruleId`, `topic`, `targetRef`, `mediation`, `defaultHidden`, `reviewRolesRequired[]`, `legalBasisRef?` | KC/`Scene` | 3.1 + F5/F6/F7 | `pending` p/ temas obrigatoriamente revisados | Apagar em vez de mediar | "Tráfico atlântico: cenas gráficas ocultas por padrão; revisão obrigatória" |
| `LegalRequirement` | Obrigação legal aplicável (com base) | `requirementId`, `targetRef?`, `legalBasisRef` (F4–F18), `obligation`, `reviewStatus` | KC/saída/UI | F4–F18 | conforme | Inventar obrigação sem fonte | "Acessibilidade de sítio (LBI Art. 63)" |
| `BrazilianEducationConstraint` | Restrição educacional brasileira (não-legal, pedagógica/normativa) | `constraintId`, `scope`, `description`, `policyRef` | saída/contexto | F1/3.1 | aprovável | Tratar restrição pedagógica como lei | "Cobertura afro/indígena estrutural na área de História" |
| `SchoolUseMode` | Modo de uso escolar | `modeId`, `mode` (`teacher`/`student`/`free-exploration`/`projector`/`offline`) | experiência (E10) | D10/Etapa 3 | aprovável | Misturar modo com permissão de conteúdo | "Modo estudante EF II: gráfico oculto por padrão" |
| `AllowedUseContext` | Classe de contexto de uso (Seção 9) | `contextId`, `targetRef`, `contextClass` (curricularCore/contextual/enrichment/freeExploration/teacherMediated/restricted/hidden) | KC/`Scene`/`MomentResult` | 3.1/F1 | conforme | Transformar contexto em obrigação | "1789: França = curricularCore; Qing = contextual" |

> **Regra (Tarefa 10).** Essas entidades são **anotação/indexação externa**. Apagá-las não altera um único campo do Knowledge Core. Nenhuma delas é fonte de fato; quando dependem de obrigação legal, carregam `legalBasisRef` para uma fonte da Seção 2.

---

## 11. Relação com `WhatWasHappeningAtMoment` (Tarefa 11)

### 11.1 Como a camada consome o `MomentResult`

A função (Etapa 5) retorna um `MomentResult` (foco, simultâneos centrais/contextuais, States, `ClaimSets`/`WeightedClaim`, `UncertaintyProfiles`, `hiddenItems`, `anachronismWarnings`, `equivalenceWarnings`, `publicabilityStatus`/`gatingReason`, `generatedSceneCandidate`, `navigationSuggestions`) e **já** recebe `ageLevelMode`/`publicabilityMode`/`layerFilters` na `MomentQuery`. A camada de conformidade é **leitora/anotadora externa**: ela **(a)** seleciona o `ageLevelMode`/`publicabilityMode` adequados ao contexto (perfil/etapa); **(b)** aplica, **sobre os itens já retornados**, as anotações `AgeSuitability`/`SensitiveContentRule`/`AccessibilityRequirement`/`AllowedUseContext`/`CurricularAlignment`; **(c)** repassa os `anachronismWarnings`/`equivalenceWarnings` já presentes e acrescenta avisos de mediação; **(d)** **respeita** o invariante de exibição (não revela `pending`/`legal-review`/`rejected`). Ela **não** reordena a verdade do núcleo nem altera claims; apenas **filtra e rotula a saída**.

### 11.2 Preservação da exploração universal

A camada **não** transforma currículo em limite absoluto: itens fora da grade permanecem acessíveis como `contextual`/`enrichment`/`freeExploration`, dentro do que é **adequado à faixa**. O currículo orienta o que é `curricularCore`; nunca apaga o resto.

### 11.3 Exemplos obrigatórios

**Exemplo 1 — "O que acontecia no mundo em 1789?" para Ensino Fundamental II (12–14)**
- **Aparece:** Queda da Bastilha (fato documentado); Inconfidência Mineira; EUA sob a nova Constituição; Lavoisier (ciência); States econômicos/populacionais.
- **`curricularCore`:** França/1789 (História EF II, via `BNCCMapping`).
- **`contextual`:** Brasil colonial, EUA, ciência, economia atlântica.
- **Mediado:** escravidão/colonização que aparecerem (mediação obrigatória nessa faixa).
- **Oculto:** mídia gráfica de violência (gráfico forte oculto por padrão < 15); itens `pending`.
- **Warnings:** `anachronismWarnings` ("Brasil não era Estado-nação; colônia, via `ModernCorrespondence`"); `equivalenceWarnings` se surgir negacionismo.
- **Fontes/revisões:** A/B; revisão editorial dos sensíveis (P14); geometrias de 1789 podem estar `PENDENTE_REFINAMENTO_ESPACIAL` (globo esquemático cobre).

**Exemplo 2 — "O que acontecia na Terra há 2,4 Ga?" para Ensino Médio (15–17)**
- **Aparece:** Grande Evento de Oxidação (`Process`, inferência/reconstrução modelada); `AtmosphereState`/`OceanographicState`; nenhum `Event` pontual.
- **`curricularCore`/`enrichment`:** conforme a unidade temática de Ciências; tempo profundo é forte caso de alfabetização científica.
- **Contextual:** "como sabemos" (proxies geoquímicos).
- **Oculto:** nada gráfico; sem itens sensíveis humanos.
- **Warnings:** paleogeografia **sempre rotulada** como `reconstrução modelada`, com incerteza (não "foto"); `anachronismWarnings` (sem países; paleomapa ≠ fato).
- **Fontes/revisões:** revisão científica de magnitude/paleogeografia (P01/P05); confiança que decai com a idade.

**Exemplo 3 — "O que acontecia em 66 Ma?" para Ensino Fundamental II (12–14)**
- **Aparece:** impacto de Chicxulub (`Event`-gatilho); extinção K-Pg (`Process`, alta confiança no fato); `cascadeStructure` (gatilho→efeitos); paleoposições rotuladas.
- **`curricularCore`/`enrichment`:** conforme Ciências EF II.
- **`ClaimSet` com peso:** impacto ≫ vulcanismo do Decão (sem falsa equivalência); a **extinção** é fato inferido, a **causa fina** é debate.
- **Oculto:** nada sensível humano; reconstruções rotuladas `representação artística`.
- **Warnings:** "México" em 66 Ma é anacronismo; marcador na **paleoposição**, não na coordenada atual.
- **Fontes/revisões:** revisão científica de pesos/paleoposições (P01/P06).

**Exemplo 4 — "Mudanças climáticas modernas" para Ensino Médio (15–17)**
- **Aparece:** consenso (aquecimento real e majoritariamente antrópico) afirmado como consenso; séries (medição); projeções como **faixa** (cenários/sensibilidade).
- **`curricularCore`:** alta relevância para Ciências/Geografia do EM; forte missão educativa.
- **`WeightedClaim`:** consenso (primário) + debate interno de projeções (secundário) + negacionismo **rotulado-rejeitado fora do `ClaimSet`**.
- **Oculto:** nada gráfico humano; gráficos **recriados dos dados** (não a figura alheia — licença).
- **Warnings:** `equivalenceWarnings` (negacionismo ≠ lado); separação **fato × cenário × previsão** (P28) — projeção **nunca** exibida como previsão certa.
- **Fontes/revisões:** NOAA/NASA/Copernicus/IPCC (termos próprios, recriar visual); INPE/MapBiomas p/ Brasil; revisão científica/editorial (P15).

**Exemplo 5 — Consulta livre de aluno sobre tema sensível (ex.: escravidão, violência política)**
- **Aparece:** o **fato** documentado, em linguagem adequada à faixa; resistência/agência; simultaneidade global.
- **`contextual`/`freeExploration`:** o aluno pode navegar; a camada aplica **só** o filtro de adequação (não a grade).
- **Mediado/`teacherMediated`:** se a faixa exigir, a exibição é condicionada à mediação; cenas gráficas ocultas por padrão.
- **Oculto/`restricted`:** mídia gráfica abaixo da faixa; itens `pending`/`legal-review` (ex.: pessoas vivas) **não** aparecem.
- **Warnings:** sem eufemismo; termos problemáticos com nota; negacionismo rotulado.
- **Fontes/revisões:** A/B; revisão obrigatória dos sensíveis (P14); `legal-review` se tocar pessoas vivas (P26).

---

## 12. Escolas públicas e privadas (Tarefa 12)

### 12.1 Escolas públicas (requisitos conceituais)

Hardware modesto; **modo projetor**; **offline parcial**; **acessibilidade** (e-MAG/WCAG/LBI); **LGPD** e proteção de menores; gestão de usuários e **uso coletivo** (frequentemente um equipamento para a turma); **rede instável**; **controle de conteúdo sensível** (mediação por faixa); **alinhamento à BNCC**; e a **possibilidade futura** de aquisição pública (incl. PNLD) — **sem** prometer aprovação (F15). A entrada comercial pode começar pelo setor privado (D10/Q2), mas os requisitos de escola pública são **fundação** (D10/A2), não pendência.

### 12.2 Escolas privadas (requisitos conceituais)

Flexibilidade curricular; **sistemas de ensino**; **projetos interdisciplinares**; **aprofundamento** e **trilhas próprias**; personalização futura (com cautela de LGPD/menores); controle por escola/professor; e **comunicação clara** de que a **BNCC é base mínima, não limite máximo** — a exploração livre e o aprofundamento são diferenciais, não desvios.

### 12.3 Requisitos comuns

Segurança; privacidade (LGPD); acessibilidade; **fontes** visíveis e incerteza tipada; **linguagem por idade**; **controle de mídia** (`natureLabel`, ocultação por padrão, propaganda sempre rotulada); e os três modos de uso (`SchoolUseMode`): **modo professor** (aparato completo), **modo estudante** (adequação por faixa) e **modo exploração livre** (filtro de adequação, sem grade).

---

## 13. Riscos jurídicos, educacionais e comerciais (Tarefa 13)

| Risco | Consequência | Mitigação | Etapa futura |
|---|---|---|---|
| Afirmar homologação MEC indevida | Sanção/credibilidade; propaganda enganosa | Declarar alinhamento ≠ homologação; sem ato do MEC por estar alinhado | E14 (jurídico/comercial) |
| Prometer aprovação PNLD | Propaganda enganosa; frustração de compra pública | PNLD é processo próprio (F15); só buscar via edital, sem promessa | E14 |
| Usar códigos BNCC sem fonte | Indexação incorreta; risco editorial | `BNCCMapping` com `provenanceRef` (F1) + `reviewStatus`; sem fonte, não mapeia | E6/E7 (curadoria curricular) |
| Tratar BNCC como origem do conteúdo | Quebra a tese; amarra o KC à BNCC | Reafirmar P1/P2; BNCC referencia o KC | (vinculante) |
| Misturar currículo com Knowledge Core | KC não-reutilizável; contaminação | Direção única de dependência (Etapa 2 §10); anotação externa | E11 (fronteira física) |
| Não cumprir LGPD | Sanção ANPD; dano a menores | KC sem dado de aluno; minimização; consentimento parental; `legal-review` | E11/E12/E14 |
| Expor menores a conteúdo inadequado | Dano; responsabilidade | Cinco níveis (3.1); mediação obrigatória; ocultação por padrão; invariante de exibição | E9/E10 |
| Ignorar acessibilidade | Exclusão; descumprimento da LBI | e-MAG/WCAG/LBI como requisito de aceitação; rótulos não-cromáticos | E10/E11/E14 |
| Não diferenciar fato/projeção/opinião | Desinformação; perda de credibilidade | `claimType`/`WeightedClaim`; separação fato × cenário × previsão (P28) | (vinculante) |
| Tratar negacionismo como "lado" | Falsa equivalência; dano educativo | Negacionismo rotulado-rejeitado fora do `ClaimSet` (3.1 §3.4); `equivalenceWarnings` | (vinculante) |
| Apagar história africana/indígena | Descumprir Leis 10.639/11.645; eurocentrismo | Cobertura estrutural + protagonismo; simultaneidade (função) | E4x/E9 |
| Usar mídia sem licença | Risco autoral | Licença por asset (1.1); gráficos recriados dos dados; IA rotulada | E13/E14 |
| Vender a escolas públicas sem requisitos mínimos | Inviabilidade técnica; má reputação | Offline parcial, projetor, acessibilidade, hardware modesto como fundação | E10/E12/E14 |
| Criar dependência de internet rápida | Exclusão de redes precárias | Degradação progressiva + pacotes offline (D10) | E10/E12 |
| Usar IA sem controle | Fato inventado; risco a menores | IA só auxiliar, rotulada, nunca fonte factual (A3/Q5); curadoria humana | E9/E11 |
| Coletar dados excessivos de alunos | Violação de minimização (LGPD Art. 14 §4) | Minimização; preferir uso mediado/coletivo sem dados pessoais | E11/E12 |

---

## 14. Fronteiras com etapas futuras (Tarefa 14)

- **Etapa 7 — Teacher/School Planning Layer.** O professor/escola informa **ano, série, disciplina, bimestre, temas, objetivos, profundidade, nível da turma, recorte local**. Esse planejamento **alimenta** os filtros desta camada (qual `EducationStage`/`SubjectArea`/`ComplianceProfile` aplicar). A Etapa 6 fornece a **gramática**; a Etapa 7, o **foco prático**.
- **Etapa 8 — Content Matching Engine.** Motor que cruza os temas do professor com o KC e com as anotações desta camada (alinhamento BNCC, adequação etária, contexto de uso) — para o núcleo, é **mais um leitor** dos índices (Etapa 2 §10).
- **Etapa 9 — Pedagogical Output Layer.** Planos de aula, atividades, quizzes, avaliações, rubricas — **consomem** as anotações desta camada e **citam** claims do KC; IA só auxiliar (A3/Q5).
- **Etapa 10 — Design/UX 3D.** Experiência visual, modos professor/estudante/exploração livre, globo/timeline finais e a **implementação concreta** da acessibilidade (e-MAG/WCAG) que aqui ficou como requisito.
- **Etapa 11 — Arquitetura técnica.** Stack, banco, API, **isolamento físico** de licenças SA/ODbL, segurança, e a **engenharia de privacidade** (LGPD/menores) — base legal, consentimento, retenção, logs.
- **Etapa 12 — MVP.** Recorte inicial e protótipo (três cenários — Q6); decide o que da conformidade entra no primeiro corte.
- **Etapa 13 — Pipeline de ingestão.** Ingestão, validação, atualização, versionamento; confirmação de licença por asset (que preenche `sourceTimeBasis`/`conversionMethod`).
- **Etapa 14 — Validação escolar, jurídica e comercial.** Especialistas, professores, pilotos, revisão jurídica (LGPD/autoral), e a decisão sobre PNLD/compra pública — **sem** promessa de aprovação.

> **O que a Etapa 6 não fez (e por quê):** não criou planejamento do professor (E7), planos/quizzes/rubricas (E9), LMS, Content Matching Engine (E8), UX final (E10), stack (E11), MVP (E12), pipeline (E13) nem novas cenas (E4x); não substituiu revisão jurídica; não prometeu homologação MEC nem aprovação PNLD; não mapeou códigos BNCC em massa. Definiu **como o sistema pode ser desenhado para ser compatível** com a educação brasileira.

---

## 15. Próximos passos para a Etapa 7 (Tarefa 15)

1. **Executar a Etapa 7 — Teacher/School Planning Layer** (quando solicitada): modelar como o professor/escola informa ano, série, disciplina, bimestre, temas, objetivos, profundidade, nível da turma, formato de aula, recursos desejados e **recorte local** — sempre **fora** do KC, alimentando os filtros desta camada.
2. **Consumir desta etapa:** `ComplianceProfile`, `EducationStage`/`SchoolYearBand`/`SubjectArea`, `AgeLanguageProfile`, `AllowedUseContext`, `CurricularAlignment`/`BNCCMapping`, e os requisitos de acessibilidade/LGPD — como **gramática** sobre a qual o planejamento opera.
3. **Endereçar os itens do Grupo 2 do backlog (5Z §6) que se aproximam:** revisão editorial/jurídica de sensíveis (P02/P03/P14), camada de clima (P15), acessibilidade (P24), LGPD/menores (P25), pessoas vivas (P26), separação fato × cenário × previsão (P28) — agora como **requisitos do fluxo do professor**.
4. **Manter o backlog como documento vivo:** mover pendências entre grupos conforme se aproximam do MVP/pipeline/publicação.
5. **Sequência subsequente (sem pular etapas, mediante solicitação):** E7 → E8 (Content Matching Engine) → E9 (Pedagogical Output) → E10 (Design/UX) → E11 (Arquitetura) → E12 (MVP) → E13 (Pipeline) → E14 (Validação).

---

## Encerramento e handoff

A Etapa 6 entrega a definição conceitual da **`BrazilianEducationComplianceLayer`** — uma camada **externa** ao Knowledge Core que **anota, filtra, restringe, orienta e indexa**, preservando a direção única de dependência, o claim-first, a proveniência obrigatória e o invariante de exibição. Entrega: a definição da camada e suas conexões (KC, função, `Scene` v1.1, futuras Planning/Output); a **matriz de fontes oficiais** verificadas (BNCC/MEC, LDB, LGPD, ECA, Leis 10.639/11.645, e-MAG/LBI/WCAG, PNLD/FNDE, PNED, Marco Civil); o **papel da BNCC** e as entidades de indexação (`BNCCCompetency`/`BNCCSkill`/`BNCCKnowledgeObject`/`BNCCMapping`/`EducationStage`/`SchoolYearBand`/`SubjectArea`/`AgeLanguageProfile`/`ComplianceAnnotation`); o **posicionamento perante a LDB** (recurso complementar; alinhamento ≠ homologação ≠ PNLD); os **requisitos de LGPD/proteção de menores** (KC sem dado de aluno; Art. 14; `legal-review`); os **requisitos de acessibilidade e uso escolar** (e-MAG/WCAG/LBI; degradação progressiva; rótulos não-cromáticos); a **modulação por faixa etária** (cinco níveis de 3.1 mapeados às etapas brasileiras; a forma muda, o fato não); o **tratamento de conteúdos sensíveis e das Leis 10.639/11.645** (cobertura estrutural, protagonismo, antieurocentrismo, revisão obrigatória); as **regras de conteúdo fora da grade** (`curricularCore`/`contextual`/`enrichment`/`freeExploration`/`teacherMediated`/`restricted`/`hidden`); o **modelo de anotação de conformidade** (10 entidades externas); a **relação com `WhatWasHappeningAtMoment`** (cinco exemplos); os **requisitos para escolas públicas e privadas**; os **riscos** com mitigação; as **fronteiras** com E7–E14; e os **próximos passos** para a Etapa 7.

Esta etapa **não** diz que o sistema está "homologado". Ela define **como o sistema pode ser desenhado para ser compatível** com a educação brasileira — mantendo as diferenças obrigatórias: alinhamento à BNCC ≠ homologação MEC; alinhamento curricular ≠ aprovação PNLD; recurso complementar ≠ substituto do currículo; exploração livre ≠ obrigação curricular; faixa etária modula linguagem/exposição, não altera fatos; a BNCC referencia o Knowledge Core, não o cria; LGPD e acessibilidade são requisitos de fundação, não enfeites; conteúdo sensível exige mediação/revisão, não apagamento.

*Documento de entrega da Etapa 6, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3Z, 3.1, 4A–4H, 4Z, 5, 5Z). Define a `BrazilianEducationComplianceLayer` como camada externa de leitura/anotação/indexação sobre o Knowledge Core e a saída da função `WhatWasHappeningAtMoment`. Não cria cena nova, não povoa conteúdos, não escreve código, não propõe MVP, não define stack, não avança para UX final, não cria planejamento do professor/planos de aula/quizzes/rubricas/LMS/Content Matching Engine, não faz pipeline de ingestão, não mapeia códigos BNCC em massa, não substitui revisão jurídica e não promete homologação MEC nem aprovação PNLD. Próxima etapa, quando solicitada: Etapa 7 — Teacher/School Planning Layer.*

---

### Fontes oficiais consultadas (acesso em 13/06/2026)

- BNCC — Base Nacional Comum Curricular (MEC/CNE): <https://basenacionalcomum.mec.gov.br/> · <https://www.gov.br/mec/pt-br/cne/base-nacional-comum-curricular-bncc> (homologação EI/EF em 20/12/2017, Resolução CNE/CP nº 2/2017; Ensino Médio em 14/12/2018, Resolução CNE/CP nº 4/2018).
- LDB — Lei nº 9.394/1996 (Planalto): <https://www.planalto.gov.br/ccivil_03/leis/l9394.htm> (Art. 26; Art. 26-A).
- Lei nº 10.639/2003 (Planalto): <https://www.planalto.gov.br/ccivil_03/leis/2003/l10.639.htm>.
- Lei nº 11.645/2008 (Planalto): <https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11645.htm>.
- LGPD — Lei nº 13.709/2018 (Planalto), Art. 14: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>.
- ECA — Lei nº 8.069/1990 (Planalto): <https://www.planalto.gov.br/ccivil_03/leis/l8069.htm>.
- Marco Civil da Internet — Lei nº 12.965/2014 (Planalto): <https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm>.
- LBI — Lei nº 13.146/2015 (Planalto): <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm>.
- Decreto nº 5.296/2004 (Planalto): <https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm>.
- e-MAG — Modelo de Acessibilidade em Governo Eletrônico (gov.br/Governo Digital): <https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade> · <https://emag.governoeletronico.gov.br/>.
- WCAG (W3C/WAI): <https://www.w3.org/WAI/standards-guidelines/wcag/>.
- PNLD — Programa Nacional do Livro e do Material Didático (MEC/FNDE): <https://www.gov.br/mec/pt-br/pnld> · <https://pnld-avaliacao.mec.gov.br/>.
- PNED — Política Nacional de Educação Digital — Lei nº 14.533/2023 (Planalto): <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14533.htm>.
- ANPD (orientações sobre dados de crianças e adolescentes — confirmar URL/versão vigente): <https://www.gov.br/anpd/>.

*Nota: textos normativos citados em paráfrase; o teor integral consta nas fontes acima. Itens marcados `PENDENTE_CONFIRMACAO_OFICIAL` exigem leitura do texto vigente antes de virarem requisito firme. Datas e versões sujeitas a reverificação na Etapa 14.*
