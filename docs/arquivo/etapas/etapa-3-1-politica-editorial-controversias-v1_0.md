# Etapa 3.1 — Política Editorial de Controvérsias e Temas Sensíveis

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Microetapa editorial · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2) e a experiência espaçotemporal (Etapa 3) · 12/06/2026
**Natureza:** documento **editorial operacional**. É a pendência crítica que a Etapa 3 (item 10.2) deixou para ser resolvida **antes** da Etapa 4. Define as regras que governam `ClaimSet`, `consensusStatus`, interpretações historiográficas, hipóteses concorrentes, temas sensíveis, linguagem escolar, exposição de menores, moderação de mídia, recortes por faixa etária e uso de fontes. Conforme solicitado, **não** avança para a Etapa 4, **não** modela novos dados, **não** escreve código, **não** propõe MVP, **não** define UX final e **não** entra em currículo, professor ou plano de aula.
**O que herda e respeita:** D7 (honestidade epistêmica como estrutura), D8 (lente Brasil; Leis 10.639/2003 e 11.645/2008), D11 (fato × expressão; mídia com licença por asset; índices só reconciliam; curadoria humana), A3/Q5 (IA só auxiliar, rotulada, nunca fonte factual), R3/C3 (controvérsias com fontes visíveis e interpretações múltiplas), e os campos do KC já definidos na Etapa 2: o enum `claimType` (fato documentado / medição / inferência científica / estimativa / hipótese / controvérsia / interpretação historiográfica / reconstrução modelada / representação artística / aproximação didática), `confidenceLevel`, `evidenceLevel`, `ClaimSet`, `consensusStatus`, `reviewStatus` e os `natureLabel` de mídia. Da Etapa 1.1 herda o **invariante de exibição**: nada com `reviewStatus ∈ {pending, rejected, legal-review}` é exibível.

> **Escopo de autoridade deste documento.** Esta política governa **como** o conteúdo sensível é tipado, rotulado, revisado e exibido. Ela **não** decide o conteúdo factual em si (isso é da Etapa 4, sob curadoria e fontes A/B), **não** cria entidades novas (usa as da Etapa 2) e **não** desenha telas (a forma visual é da Etapa 10; aqui ficam os **requisitos**).

---

## Sumário

1. Princípios editoriais
2. Tipos de controvérsia
3. Regras para ClaimSet
4. Regras para temas históricos sensíveis
5. Regras para temas científicos sensíveis
6. Faixa etária e exposição escolar
7. Mídia e imagens sensíveis
8. Padrão de linguagem
9. Governança editorial
10. Exemplos obrigatórios
11. Impacto na Etapa 4

---

## 1. Princípios editoriais

### 1.1 Os dez princípios (PE-Ed1 a PE-Ed10)

1. **Honestidade epistêmica.** Todo conteúdo carrega, à vista, seu `claimType`, `confidenceLevel` e fonte (D7). A interface nunca dá a uma inferência a autoridade de um fato observado, nem a uma hipótese a de um consenso. Ausência de evidência é mostrada como ausência, nunca preenchida.
2. **Pluralidade historiográfica responsável.** Onde há interpretações acadêmicas legítimas concorrentes, elas aparecem lado a lado, cada uma com sua fonte e seu peso (`ClaimSet`). Pluralidade **não** é dar palco igual a tudo: ver PE-Ed5.
3. **Rigor científico.** Consenso científico é apresentado como consenso. Hipóteses em aberto são apresentadas como hipóteses. Pseudociência e negacionismo **não** entram como claims concorrentes do consenso (ver §2 e §5).
4. **Proteção de menores.** O produto é dirigido a estudantes, inclusive menores (LGPD/ECA). A escolha conservadora prevalece: na dúvida sobre exposição, **restringe-se, rotula-se ou exige-se mediação** do professor, nunca o contrário.
5. **Neutralidade institucional sem falsa equivalência.** O produto não toma partido político-partidário nem doutrinário; mas neutralidade **não** significa equivaler consenso a negação, fato a boato, ou ciência a pseudociência. Neutralidade é sobre **postura institucional**, não sobre **peso de evidência**.
6. **Separação entre fato, interpretação e opinião.** Três camadas distintas e visivelmente rotuladas: **fato** (documentado/medido), **interpretação** (historiográfica/científica, com fonte), **opinião** (que o produto, em regra, **não** emite institucionalmente). A `shortDescription` didática nunca é tratada como claim (Etapa 2).
7. **Transparência de fonte.** Toda afirmação relevante rastreia a uma fonte A/B (Etapa 1). Índices (Wikidata/Wikipedia/IA) jamais aparecem como autoridade — só reconciliam identidade nos bastidores (C1; Etapa 1.1, Q12).
8. **Adequação por faixa etária.** Profundidade, linguagem e mídia se ajustam à faixa (§6) **sem** alterar o fato subjacente: adapta-se a *forma*, nunca o *conteúdo factual* (A3/Q5 — a IA adapta linguagem sobre o conteúdo curado, não inventa).
9. **Linguagem não sensacionalista.** Sem dramatização gratuita, sem eufemismo que apague violência, sem julgamento moral raso sem contexto (§8).
10. **Respeito à BNCC/LDB e às Leis 10.639/2003 e 11.645/2008 sem transformar o KC em currículo.** As leis e a BNCC orientam **cobertura e cuidado** (história e cultura africana, afro-brasileira e indígena presentes e em simultaneidade), mas entram como camada de **conformidade e indexação por fora** (Etapa 2, §10) — o núcleo permanece universal.

### 1.2 Sete distinções que a política precisa manter sempre separadas

A operação editorial inteira depende de não confundir estes sete fenômenos. A confusão entre eles é a falha que esta política existe para impedir.

| Fenômeno | Definição operacional | Tratamento-base |
|---|---|---|
| **Controvérsia legítima** | Divergência real entre especialistas qualificados, sustentada por evidência de ambos os lados, sem resposta fechada. | Entra como `ClaimSet`; claims lado a lado com fonte e peso. |
| **Hipótese científica concorrente** | Explicação ainda não decidida dentro do método científico; coexiste com outras hipóteses sob teste. | `claimType = hipótese`; `consensusStatus = hipóteses concorrentes`; confiança média/baixa. |
| **Disputa historiográfica** | Leituras distintas de um mesmo passado por escolas/correntes (causas, ênfases, periodização, terminologia), todas com base documental. | `claimType = interpretação historiográfica`; `ClaimSet` com `consensusStatus = controvérsia historiográfica`. |
| **Negacionismo** | Rejeição de fato/consenso bem estabelecido **sem** evidência científica válida (negação do Holocausto, terraplanismo, negação da evolução ou das mudanças climáticas antrópicas). | **Não** é claim concorrente. Pode existir apenas como **objeto de estudo rotulado** (`consensusStatus = desinformação/negacionismo rejeitado`), nunca como alternativa equivalente ao consenso. |
| **Desinformação** | Informação falsa ou enganosa, deliberada ou não, sem lastro em fonte A/B. | Não entra como fato. Pode ser **tematizada** (ex.: "como circulou tal boato") sob revisão, sempre rotulada como falsa. |
| **Opinião política** | Juízo de valor político-partidário ou doutrinário sobre temas em disputa pública. | O produto **não** emite opinião institucional. Pode **descrever** posições de atores históricos com fonte, sem endossá-las. |
| **Conteúdo sensível** | Material que, independentemente de ser verdadeiro, pode chocar, traumatizar ou exigir maturidade (violência, escravidão, genocídio, corpos/vítimas). | Verdade não dispensa cuidado: entra com rotulagem, recorte por faixa etária e, quando necessário, mediação e ocultação por padrão (§6, §7). |

A regra-síntese: **controvérsia legítima e disputa historiográfica recebem pluralidade; negacionismo e desinformação recebem rótulo de rejeição; opinião política não é emitida; conteúdo sensível recebe cuidado mesmo quando é fato.**

---

## 2. Tipos de controvérsia

Para cada tipo: entra no KC? vira `ClaimSet`? exige revisão humana? exige linguagem adaptada por idade? pode ser exibido a estudantes? exige mediação do professor? como aparece no dossiê?

| Tipo | Entra no KC? | Vira ClaimSet? | Revisão humana? | Linguagem por idade? | Exibível a estudantes? | Mediação do professor? | Como aparece no dossiê |
|---|---|---|---|---|---|---|---|
| **Controvérsia científica real** | Sim | Sim | Sim (científica) | Sim | Sim | Recomendável | Claims concorrentes com fonte, confiança e `consensusStatus = debate acadêmico`/`hipóteses concorrentes`. |
| **Hipótese científica em aberto** | Sim | Sim (se houver concorrentes) | Sim | Sim | Sim | Não necessária | `claimType = hipótese`, confiança média/baixa, rótulo "em aberto". |
| **Disputa historiográfica** | Sim | Sim | Sim (historiográfica) | Sim | Sim | Recomendável | Interpretações lado a lado, cada uma com escola/fonte; sem "veredito". |
| **Disputa terminológica** | Sim | Sim (quando o termo carrega disputa) | Sim | Sim | Sim | Conforme tema | Nota terminológica; nomes alternativos com vigência e contexto (§8). |
| **Conflito de memória histórica** | Sim | Sim | Sim | Sim | Sim | Sim (alta sensibilidade) | Múltiplas memórias com fonte; respeito a vítimas; sem hierarquização gratuita de sofrimento. |
| **Tema politicamente sensível** | Sim, como descrição factual de atores/eventos | Conforme caso | Sim | Sim | Sim, sem opinião institucional | Sim | Descreve posições com fonte; o produto não endossa lado. |
| **Conteúdo violento** | Sim (o fato) | Não por si | Sim (mídia) | Sim | Conforme faixa (§6) | Sim para faixas menores | Texto factual; mídia gráfica ocultada por padrão e rotulada (§7). |
| **Conteúdo religioso/cultural** | Sim, como fenômeno histórico-cultural | Conforme caso | Sim | Sim | Sim | Conforme contexto | Descrição respeitosa de crenças/práticas como objeto de estudo; sem proselitismo nem ridicularização. |
| **Colonialismo / escravidão / povos indígenas** | Sim | Sim (interpretações + memórias) | **Sim, obrigatória** | Sim | Sim, com cuidado | **Sim** | Fato + interpretações + simultaneidade global; perspectivas dos povos afetados (§4). |
| **Racismo e discriminação** | Sim, como fenômeno histórico/social a explicar | Conforme caso | **Sim, obrigatória** | Sim | Sim, com cuidado | Sim | Explica o fenômeno; **nunca** reproduz discurso discriminatório como voz própria (§8). |
| **Guerra e genocídio** | Sim (o fato) | Conforme caso (causas/responsabilidades podem ser `ClaimSet`) | **Sim, obrigatória** | Sim | Conforme faixa | **Sim** | Fato com dignidade às vítimas; mídia gráfica restrita (§7); negação de genocídio = negacionismo (§5/§8). |
| **Temas contemporâneos polarizados** | Sim, como descrição factual com fonte | Conforme caso | Sim | Sim | Sim, sem opinião institucional | Sim | Posições descritas com fonte; consenso científico (quando houver) não é relativizado por polarização. |
| **Pseudociência e negacionismo** | **Apenas como objeto de estudo rotulado** | **Não como claim concorrente** | **Sim, obrigatória** | Sim | Sim, como tema de alfabetização científica | Sim | Aparece **descrito e rotulado** `desinformação/negacionismo rejeitado`, contraposto ao consenso; nunca equivalido a ele. |

Regra transversal: qualquer linha marcada com revisão **obrigatória** herda automaticamente `reviewStatus = pending` na entrada e **não é exibível** até aprovação humana (Etapa 1.1, §7.5; §9 abaixo).

---

## 3. Regras para ClaimSet

### 3.1 Quando usar um ClaimSet

Um `ClaimSet` é obrigatório (em vez de um único `Claim`) sempre que houver: interpretações concorrentes; hipóteses concorrentes; fontes divergentes sobre um mesmo ponto; controvérsia de nomenclatura; debate historiográfico; incerteza relevante de causa; ou conflito de memória. A regra prática: **se especialistas qualificados discordam com base em evidência, é `ClaimSet`, não escolha editorial.** O produto não "decide" a controvérsia; ele a **estrutura e a torna legível**.

Não se usa `ClaimSet` quando a divergência é entre consenso e negacionismo — aí há **um** claim (o consenso) e, separadamente e rotulado, o registro do negacionismo como objeto (§3.4).

### 3.2 Vocabulário de `consensusStatus`

Valores operacionais (a normalização final do enum é da Etapa 4/modelagem, mas a política fixa o significado):

| `consensusStatus` | Significado | Tratamento na exibição |
|---|---|---|
| **consenso amplo** | Praticamente toda a comunidade qualificada concorda. | Claim único, confiança alta; sem "outro lado" forjado. |
| **consenso majoritário** | Maioria qualificada concorda; existe minoria legítima. | Claim principal em destaque + minoria registrada com peso menor e fonte. |
| **debate acadêmico** | Divergência ativa, sem maioria clara. | Claims lado a lado, pesos comparáveis, fontes visíveis. |
| **hipóteses concorrentes** | Várias explicações sob teste, nenhuma fechada. | `claimType = hipótese` para cada; rótulo "em aberto". |
| **controvérsia historiográfica** | Leituras distintas de um passado, todas com base documental. | Interpretações por escola/corrente, cada uma atribuída. |
| **terminologia sensível** | A disputa é sobre o **nome** (ex.: "descobrimento" × "invasão"). | Nota terminológica; termos com contexto e vigência (§8). |
| **desinformação/negacionismo rejeitado** | Posição sem lastro científico que nega fato/consenso. | **Não** é claim concorrente; aparece rotulada como rejeitada, contraposta ao consenso. |
| **insuficiência de evidência** | Não há base suficiente para afirmar. | Mostra-se a lacuna; nada é inventado para preenchê-la. |

### 3.3 Como exibir um ClaimSet

- **Claims lado a lado**, cada um com seu `claimType`, `confidenceLevel` e **fonte própria** (`Source`/`Citation`).
- **Por que uma visão é majoritária / minoritária:** o dossiê explicita o **peso relativo** (não apenas lista) — quando há maioria, ela é identificada como tal, com a base; a minoria legítima é registrada com sua base, sem ser apagada nem inflada.
- **Atribuição clara:** cada interpretação é atribuída a uma corrente/escola/autor com fonte, evitando o "alguns dizem" anônimo.
- **Sem veredito editorial** em controvérsia legítima: o produto não escolhe o vencedor; estrutura o debate.

### 3.4 Quando uma visão **não** deve receber equivalência

A pluralidade tem limite. **Não** se concede equivalência a uma posição quando ela é negacionismo/pseudociência (nega fato ou consenso sem evidência válida) — terraplanismo, negação da evolução, negação das mudanças climáticas antrópicas, negação do Holocausto/de genocídios. Nesses casos: há **um** claim sustentado (o consenso) e, se pedagogicamente útil (alfabetização científica/histórica), a posição negacionista aparece **descrita e rotulada** como `desinformação/negacionismo rejeitado`, **fora** do `ClaimSet` de claims legítimos, jamais como "o outro lado". Esta é a aplicação direta de PE-Ed5 (neutralidade sem falsa equivalência).

---

## 4. Regras para temas históricos sensíveis

Princípios transversais a todos os temas desta seção: **(a)** centralidade das perspectivas dos povos afetados, não só dos agentes dominantes; **(b)** simultaneidade global como antídoto ao eurocentrismo (D8; a função da Etapa 3, §4); **(c)** dignidade às vítimas; **(d)** fato + interpretação separados e ambos com fonte; **(e)** Leis 10.639/2003 e 11.645/2008 como exigência de **presença e protagonismo**, não de nota de rodapé.

| Tema | Cuidados de linguagem | Cuidados de imagem | Fontes preferenciais | Riscos de simplificação | Simultaneidade global | Antieurocentrismo / Leis 10.639 e 11.645 |
|---|---|---|---|---|---|---|
| **Colonização das Américas** | Evitar "descobrimento" sem contexto; nomear violência sem sensacionalismo; `ClaimSet` terminológico. | Sem glorificação de conquista; mapas históricos rotulados. | Historiografia revisada; WHG/Pleiades; fontes indígenas e de história da América. | Reduzir a "encontro" pacífico; apagar agência indígena. | Mostrar sociedades originárias **já presentes e complexas** em paralelo à chegada europeia. | Protagonismo dos povos originários; não tratar a América como "vazia" antes de 1492. |
| **1492** | Termo em `ClaimSet` ("descobrimento" × "invasão" × "encontro"), com contexto. | Iconografia de época rotulada como representação da época, não como fato neutro. | Historiografia plural; fontes ameríndias quando houver. | Marco único eurocêntrico; "início da história". | Ásia, África e Américas simultâneas em 1492 (Etapa 3, exemplo 4). | Anacronismo "Brasil" evitado via `ModernCorrespondence` rotulada (Etapa 3, §3.4). |
| **Escravidão** | "Pessoas escravizadas" (não "escravos"), reconhecendo humanidade; nomear o sistema sem eufemismo. | Imagens de violência ocultas por padrão, com rótulo e mediação; evitar espetáculo do sofrimento. | Fontes afro-brasileiras e africanistas; arquivos; historiografia da escravidão. | Naturalizar; reduzir africanos a vítimas passivas; apagar resistência. | Tráfico como sistema **atlântico** (África–América–Europa) simultâneo. | Lei 10.639: história e cultura afro-brasileira com **agência, resistência, quilombos**, não só servidão. |
| **Tráfico atlântico** | Nomear escala e responsabilidade sem números frios sem rosto; sem eufemismo logístico. | Diagramas históricos (navio negreiro) com rótulo e cuidado; ocultação por padrão de cenas gráficas. | Bases de dados do tráfico transatlântico (acadêmicas); historiografia. | "Comércio" asséptico; apagar a dimensão humana. | Conectar portos africanos, rotas e destinos americanos no globo. | Centralidade das sociedades africanas como sujeitos, não mercadoria. |
| **Povos indígenas no território brasileiro** | Etnônimos corretos e autodenominações; evitar "índio" genérico quando houver nome próprio; presente **e** passado profundo. | Respeito a imagens de rituais/pessoas; cautela com sacralidade; consentimento quando aplicável. | IPHAN; etno-historiografia; fontes indígenas; IBGE p/ território. | "Povos do passado"; homogeneizar centenas de povos distintos. | História indígena **profunda** (povoamento, sambaquis, marajoara — D8) em paralelo ao resto do mundo. | Lei 11.645: protagonismo e diversidade indígena, presença contemporânea, não extinção. |
| **História africana e afro-brasileira** | Reinos e sociedades africanas como civilizações complexas; evitar "África" monolítica. | Iconografia diversa; sem exotização. | Africanistas; SciELO; acervos; historiografia afro-brasileira. | Começar a história africana na escravidão. | Mali, Songhai, Etiópia, Grandes Lagos etc. simultâneos à Europa medieval/moderna. | Lei 10.639 como exigência de **cobertura estrutural**, não complementar. |
| **Genocídios** | Nomear como genocídio quando há consenso; responsabilidade com fonte; sem relativização. | Mídia gráfica ocultada por padrão; mediação obrigatória; dignidade às vítimas. | Documentação histórica revisada; órgãos de memória. | Equiparar vítima e algoz; "dois lados" onde há crime documentado. | Contexto regional e global do evento. | Negação de genocídio = negacionismo (§3.4), nunca claim concorrente. |
| **Ditaduras** | Nomear repressão, censura, tortura com fonte; distinguir fato documentado de disputa de interpretação. | Fotos de repressão com rótulo/cautela; propaganda do regime sempre **rotulada como propaganda** (§7). | Comissões da verdade, arquivos, historiografia. | "Havia dois lados iguais"; eufemismo ("anos de chumbo" sem conteúdo). | Contexto (ex.: ditaduras no Cone Sul, Guerra Fria) simultâneo. | Memória de vítimas; pluralidade só onde há disputa **legítima**, não sobre fatos de violência de Estado documentados. |
| **Guerras** | Causas como `ClaimSet` quando disputadas; fatos (datas, frentes) como fato documentado. | Violência gráfica restrita por faixa; sem heroificação da matança. | Historiografia militar e social; fontes de múltiplos lados. | Narrativa do vencedor como única; números sem vítimas humanas. | Frentes e impactos globais simultâneos. | Vozes dos colonizados/atingidos, não só das potências. |
| **Imperialismo** | Nomear dominação e exploração; distinguir discurso da época da análise atual. | Cartografia imperial rotulada como **perspectiva da potência**, não como neutra. | Historiografia pós-colonial e clássica em diálogo. | "Missão civilizatória" sem aspas críticas. | Mostrar metrópoles e colônias simultaneamente. | Perspectiva dos povos colonizados em primeiro plano. |
| **Racismo** | Explicar o fenômeno e sua construção histórica; **nunca** reproduzir termos racistas como voz do produto (§8). | Não reproduzir iconografia racista sem enquadramento crítico explícito. | Historiografia das relações raciais; fontes afro-brasileiras. | "Racismo é coisa do passado"; biologizar raça (ver §5). | Conexões diaspóricas e globais. | Leis 10.639/11.645 como combate ao racismo estrutural na narrativa. |
| **Migrações forçadas** | "Pessoas deslocadas/forçadas"; agência e sofrimento sem espetáculo. | Imagens com dignidade; evitar imagens de crianças vítimas sem mediação. | Historiografia das migrações; ACNUR/ONU p/ contexto. | Reduzir a estatística; apagar causa política. | Origens e destinos no globo simultâneos. | Diásporas africana e indígena centrais. |
| **Violência política** | Distinguir relato factual de juízo; contexto sem incitação. | Cenas violentas restritas/ocultas por padrão (§7). | Fontes plurais e revisadas. | Glorificar ou banalizar violência. | Contexto regional/global. | Sem endosso de qualquer lado (PE-Ed5). |
| **Religião e conflitos religiosos** | Crenças descritas com respeito como objeto de estudo; sem proselitismo nem zombaria; sem afirmar verdade de doutrina. | Imagens sacras com respeito; cautela com representações proibidas em certas tradições. | História das religiões; fontes confessionais como **objeto**, não autoridade factual. | Reduzir conflito a "religião causa guerra"; homogeneizar uma fé. | Múltiplas tradições simultâneas no globo. | Diversidade religiosa afro-brasileira e indígena reconhecida. |

---

## 5. Regras para temas científicos sensíveis

Princípio reitor: **consenso científico é apresentado como consenso; incerteza legítima é mostrada sem enfraquecer o consenso; pseudociência/negacionismo não recebe equivalência** (PE-Ed3, PE-Ed5). A incerteza interna de um campo (ex.: detalhes de um mecanismo) **não** é o mesmo que dúvida sobre o fato central — a interface separa as duas coisas.

| Tema | Consenso científico | O que pode ser hipótese | Pseudociência / negacionismo | Evitar falsa equivalência | Incerteza legítima sem enfraquecer consenso | Linguagem escolar |
|---|---|---|---|---|---|---|
| **Big Bang** | Universo em expansão a partir de estado quente e denso há ~13,8 Ga (inferência científica de alta confiança). | Mecanismos dos primeiros instantes (inflação), detalhes pré-Planck. | "Não houve Big Bang" sem evidência; criacionismo como ciência. | Não opor "teoria religiosa" como alternativa científica equivalente. | A idade tem `±`; a inflação é hipótese — **separadas** do fato da expansão (Etapa 2, §9.1). | Pode-se dizer "melhor explicação científica atual", com a incerteza própria. |
| **Evolução** | Evolução por seleção natural e ancestralidade comum: consenso amplo. | Detalhes de ritmo, mecanismos específicos, relações de parentesco finas. | "Design inteligente"/criacionismo como ciência; negação da evolução. | Não tratar criacionismo como claim concorrente da evolução. | Debates internos (gradualismo × equilíbrio pontuado) são **dentro** do consenso evolutivo. | Evolução como fato científico; debates internos como ciência viva. |
| **Origem da vida** | A vida surgiu na Terra primitiva por processos naturais (consenso de que ocorreu). | **Como** exatamente (mundo de RNA, fontes hidrotermais etc.): `hipóteses concorrentes`. | Negar abiogênese natural sem base. | O "como" estar aberto não reabre o "se". | `consensusStatus = hipóteses concorrentes` para o mecanismo; alta confiança no fato de que a vida surgiu. | "Cientistas investigam várias hipóteses sobre como a vida começou." |
| **Idade da Terra** | ~4,54 Ga (medição radiométrica): consenso amplo, alta confiança. | Refinamentos de margem. | "Terra jovem" (milhares de anos): negacionismo. | Não equivaler Terra jovem ao dado radiométrico. | Margem de erro pequena, explicitada. | Fato com `±`; método (datação radiométrica) explicável. |
| **Mudanças climáticas** | Aquecimento global é real e majoritariamente causado por ação humana: consenso científico robusto. | Magnitude exata de projeções, sensibilidade climática fina. | Negação do aquecimento ou da causa antrópica: negacionismo. | **Não** dar palco igual a "céticos" do consenso (PE-Ed5). | Faixas de projeção (IPCC) são incerteza **dentro** do consenso, não dúvida sobre a causa. | Consenso afirmado; incerteza de cenários mostrada como faixa, não como dúvida do fato. |
| **Vacinas e saúde pública** | Segurança e eficácia das vacinas aprovadas: consenso médico. | Pesquisa de fronteira sobre novas formulações. | Antivacina/"vacina causa autismo": desinformação rejeitada. | Não equivaler estudo fraudado a evidência. | Efeitos adversos reais e raros são informados **com** sua frequência, sem alarmismo. | Linguagem de saúde pública responsável; evitar gerar medo. **Cautela redobrada**: tema de saúde com risco real de dano. |
| **Genética** | Hereditariedade, DNA, base molecular: consenso. | Fronteiras (epigenética fina, poligenia complexa). | Determinismo genético simplista; eugenia. | Não tratar "genes definem destino" como ciência. | Complexidade gene-ambiente mostrada. | Cuidado com determinismo; nunca insinuar hierarquia entre grupos. |
| **Raça e ciência** | "Raça" **não** é categoria biológica válida; é construção social (consenso da genética e da antropologia). | — | Racialismo científico, frenologia, "raças com QI diferente": pseudociência histórica e atual. | **Jamais** apresentar racismo científico como hipótese válida; só como **objeto histórico rotulado**. | Variação genética humana é contínua e não se organiza em "raças". | Explicar por que a ciência refuta o conceito biológico de raça; combater, não reproduzir. **Revisão obrigatória.** |
| **Inteligência artificial** | Definições técnicas e capacidades atuais documentadas. | Trajetórias futuras, riscos, "consciência": especulação/hipótese. | Hype e pânico sem base como fato. | Não vender ficção como fato técnico. | Incerteza sobre futuro explicitada como tal. | Distinguir o que IA **faz hoje** do que se **especula**. |
| **Energia nuclear** | Física nuclear; fatos de acidentes (Chernobyl, Fukushima) documentados. | Avaliações de risco/custo-benefício energético: debate legítimo com valores. | Mitos sem base (ambos os lados). | Separar fato físico de **opinião** sobre política energética (o produto não opina). | Riscos e benefícios com fonte; trade-offs explicitados. | Fato técnico separado de debate político. |
| **Pandemias** | Epidemiologia básica; fatos históricos de pandemias documentados. | Modelos prospectivos, origens ainda investigadas (quando for o caso). | Negacionismo sanitário; curas milagrosas; teorias conspiratórias. | Não equivaler conspiração a investigação científica. | Incerteza de origem/modelo mostrada sem alimentar conspiração. | Responsável; sem pânico; **cautela** por proximidade com saúde e trauma recente. |
| **Impactos ambientais** | Desmatamento, extinção, poluição como fenômenos documentados (INPE/MapBiomas/IBGE p/ Brasil). | Projeções e atribuições finas. | Negação de impacto documentado. | Não relativizar dado de monitoramento. | Margem dos dados de sensoriamento mostrada. | Fato ambiental com fonte; sem catastrofismo nem minimização. |

---

## 6. Faixa etária e exposição escolar

A política define **cinco níveis de exposição**. O eixo etário modula *profundidade, linguagem e mídia* — **nunca** o fato em si (PE-Ed8). O recorte alinha-se a D9 (V1 foca Fundamental II + Ensino Médio; arquitetura nasce universal, então as faixas menores já ficam previstas para ondas posteriores). A distinção **modo estudante × modo professor** é editorial aqui (a forma é da Etapa 10).

| Nível | Profundidade | Linguagem | Imagens permitidas | Temas que exigem mediação | Ocultação parcial por padrão | Temas que exigem aviso |
|---|---|---|---|---|---|---|
| **6–8 anos** | Noções concretas, narrativa simples; sem números abstratos grandes sem âncora. | Muito acessível, frases curtas, sem jargão. | Apenas imagens não gráficas; nada de violência/morte explícita. | Qualquer tema sensível (escravidão, guerra) só com forte mediação e enquadramento. | Violência, escravidão gráfica, morte, sexualidade: ocultas. | Qualquer tema de sofrimento. |
| **9–11 anos** | Causas e consequências simples; primeira simultaneidade. | Acessível, com termos sensíveis explicados ao introduzir. | Imagens históricas suaves, rotuladas; nada gráfico. | Escravidão, colonização, genocídio: mediação. | Mídia gráfica de violência/corpos: oculta. | Temas de violência e discriminação. |
| **12–14 anos** | Processos, interpretações iniciais, `ClaimSet` simplificado. | Termos sensíveis explicados; introduz disputa terminológica. | Imagens históricas com rótulo; gráfico forte ainda oculto por padrão. | Genocídio, tortura, violência sexual: mediação obrigatória. | Cenas gráficas explícitas: ocultas por padrão (revelação mediada). | Violência, racismo, conteúdo religioso sensível. |
| **15–17 anos** | Complexidade plena adequada à escola; controvérsias com pluralidade. | Próxima da acadêmica, ainda didática; nomeia violência com responsabilidade. | Imagens históricas, inclusive difíceis, **com rótulo e contexto**; gráfico extremo ainda mediado. | Genocídio e violência extrema: aviso + contexto; mediação recomendada. | Gráfico extremo: aviso de conteúdo antes de exibir. | Trauma, violência extrema, temas contemporâneos polarizados. |
| **Professor / pesquisador** | Completa, com aparato de fontes, `ClaimSet` integral, notas editoriais. | Acadêmica; acesso a todo o aparato crítico. | Acesso pleno a mídia (com rótulos e licença), inclusive material sensível para preparação. | — (é quem media) | Nada oculto por padrão, mas tudo rotulado. | Notas de mediação para uso em sala. |

**Modo estudante × modo professor (regra editorial):**
- **Modo estudante:** profundidade, linguagem e mídia conforme a faixa selecionada; conteúdo gráfico ocultado por padrão; controvérsias apresentadas no grau adequado; avisos de conteúdo ativos.
- **Modo professor:** acesso ao **aparato completo** — todas as fontes, `ClaimSet` integral, notas editoriais, mídia sensível para preparação, e **sugestões de mediação**. O professor é tratado como mediador adulto responsável (não como aluno), mas continua sob as regras de licença e de não reprodução de discurso de ódio.

Regra de ouro de faixa: **na dúvida sobre adequação, sobe-se o nível de cuidado** (mais mediação, mais aviso, ocultação por padrão) — nunca se assume maturidade não confirmada (PE-Ed4).

---

## 7. Mídia e imagens em temas sensíveis

Toda mídia já carrega, da Etapa 2/1.1: `natureLabel` (fotografia / mapa / gráfico / reconstrução científica / simulação / representação artística / aproximação didática), licença por asset e `reviewStatus`. Esta seção define o **regime de uso** por tipo sensível. Mídia de violência **nunca** é decoração; só entra quando tem função pedagógica e com o menor dano possível.

| Tipo de mídia | Quando usar | Quando evitar | Ocultar por padrão? | Mediação do professor? | Como rotular | Licença e contexto |
|---|---|---|---|---|---|---|
| **Imagens históricas (gerais)** | Quando documentam o tema com valor pedagógico. | Quando substituíveis por opção menos sensível sem perda. | Não, se não gráficas. | Conforme faixa. | `natureLabel` + data/origem; "imagem de época". | Licença por asset; PD preferível; atribuição exibida. |
| **Fotografias de guerra** | Faixas maiores, com contexto e propósito. | Faixas menores; uso gratuito. | Sim (gráficas). | Sim para <15; aviso para 15–17. | "Fotografia · conteúdo sensível"; data/autor. | Verificar direitos; cautela com vítimas identificáveis. |
| **Violência (geral)** | Só com função pedagógica clara. | Sempre que possível evitar o gráfico. | Sim. | Sim. | Aviso de conteúdo + `natureLabel`. | Licença + nota de contexto. |
| **Escravidão** | Para evidenciar o sistema, com dignidade. | Espetáculo do sofrimento; imagem como choque gratuito. | Sim (cenas gráficas). | Sim. | "Imagem histórica · conteúdo sensível"; enquadramento crítico. | PD/arquivo; contexto obrigatório. |
| **Corpos / vítimas** | Excepcional, faixas maiores, com forte justificativa. | Regra geral: evitar identificação de vítimas. | **Sim, sempre.** | **Sim, sempre.** | Aviso forte; respeito à dignidade. | Direitos de imagem/post-mortem; revisão jurídica se identificável. |
| **Propaganda política** | Como **objeto de estudo**, para análise crítica. | Nunca como informação neutra. | Não, mas **sempre rotulada**. | Recomendável. | **"Propaganda — material de [regime/ator], exibido para análise crítica."** | Licença + contexto histórico obrigatório. |
| **Símbolos de regimes autoritários** | Apenas em contexto histórico-educacional, rotulado. | Qualquer uso que possa ser lido como exibição/endosso. | Sim, com revelação contextualizada. | Sim. | Rótulo explícito de contexto histórico; nunca isolado. | Atenção a leis e a sensibilidades; revisão obrigatória. |
| **Imagens religiosas** | Como objeto de estudo, com respeito. | Uso que zombe ou que viole proibições de representação de uma tradição. | Conforme tradição/sensibilidade. | Conforme contexto. | "Imagem religiosa · contexto"; respeito. | Direitos + sensibilidade cultural. |
| **Imagens geradas por IA** | Só quando não há alternativa documental e com função didática. | Como "fotografia" ou "evidência"; em temas factuais sensíveis. | Conforme tema. | Sim. | **"Representação artística / aproximação didática gerada por IA"** (Etapa 1.1, caso 8). | `reviewStatus = pending` até revisão humana; nunca fonte. |
| **Reconstruções artísticas** | Para ilustrar (ex.: cena pré-histórica), rotuladas. | Como registro/fato. | Não, se rotuladas. | Não necessária. | `natureLabel = representação artística`; "interpretação do artista". | Licença do asset. |
| **Mapas com fronteiras disputadas** | Quando a disputa é o tema, como `ClaimSet` cartográfico. | Apresentar uma fronteira disputada como única verdade. | Não, mas com nota de disputa. | Recomendável. | "Fronteira disputada — ver perspectivas"; `GeometryVersion` + data. | Licença; isolar SA/ODbL (L2); evitar tomar partido territorial. |

Regra transversal de mídia: **nenhum** asset sensível é exibido sem `natureLabel`, sem licença válida e sem passar pela revisão de mídia (§9). Asset sem licença declarada **não existe** para a vista (invariante).

---

## 8. Padrão de linguagem

### 8.1 O que a linguagem deve evitar

- **Sensacionalismo** (dramatização, superlativos gratuitos, "chocante", "você não vai acreditar").
- **Julgamento moral simplista sem contexto** (rotular pessoas/povos do passado com categorias atuais sem explicar o contexto).
- **Eufemismos que apagam violência** ("mão de obra" para pessoas escravizadas; "pacificação" para massacre; "comércio" asséptico para tráfico humano).
- **Termos anacrônicos sem explicação** (usar conceitos atuais para períodos onde não existiam, sem nota).
- **Linguagem discriminatória** — o produto **explica** o racismo/discriminação como fenômeno, mas **nunca** adota termos racistas/discriminatórios como voz própria; quando precisa citar um termo histórico ofensivo, fá-lo **entre aspas, datado e enquadrado criticamente**.
- **Falsa neutralidade** (omitir responsabilidade documentada em nome de "imparcialidade"; "houve excessos de ambos os lados" onde há crime documentado de um lado).
- **Falsa equivalência** entre consenso e negacionismo, entre fato e boato.

### 8.2 Como tratar termos sensíveis e disputados

- **Explicar ao introduzir:** todo termo sensível ou técnico recebe, na primeira aparição na faixa adequada, uma explicação curta e não condescendente.
- **Termos históricos hoje inadequados:** exibidos **com aspas, data e nota** ("o termo usado à época era X; hoje considera-se inadequado por Y"). Nunca naturalizados.
- **Nomes coloniais × nomes indígenas/originários:** privilegiar autodenominações e etnônimos corretos; quando o nome colonial for necessário para a busca histórica, registrá-lo como **variante datada** (`nameVariants[]` com vigência — Etapa 2), com o nome originário em primeiro plano.
- **Disputa terminológica:** quando o nome **é** a controvérsia ("descobrimento" × "invasão" × "encontro"; "guerra" × "genocídio" quando há disputa legítima), usa-se `ClaimSet` com `consensusStatus = terminologia sensível`, apresentando os termos com seus contextos — sem impor um único rótulo como neutro.
- **Preferência por linguagem que reconhece humanidade e agência:** "pessoas escravizadas", "povos originários", "pessoas deslocadas".

### 8.3 Estudante × professor (linguagem)

- **Para o estudante:** clareza adequada à faixa, termos explicados, sem perder a verdade; o grau de complexidade da controvérsia é dosado por faixa (§6), mas a controvérsia **não é escondida** quando relevante — é apresentada no nível certo.
- **Para o professor:** registro mais técnico, com o aparato historiográfico/científico completo, notas editoriais e sugestões de como abordar o tema em sala (mediação) — sempre sob as mesmas regras anti-discriminação.

---

## 9. Governança editorial

### 9.1 Fluxo de revisão

Conteúdo sensível atravessa um fluxo de revisão **antes** de tornar-se exibível. As revisões são **papéis**, não necessariamente pessoas distintas; um item pode exigir vários. O `reviewStatus` (Etapa 1.1) é o estado que governa a publicação.

```
Item/claim sensível entra (reviewStatus = pending)
        │
        ▼
[1] Revisão científica ........ consenso × hipótese × pseudociência corretos? (§5)
[2] Revisão historiográfica .... interpretações e atribuições corretas? (§4)
[3] Revisão pedagógica ......... profundidade/linguagem por faixa adequadas? (§6/§8)
[4] Revisão de faixa etária .... exposição, ocultação e avisos corretos? (§6)
[5] Revisão jurídica/licença ... licença por asset, direitos, LGPD/menores? (Etapa 1.1)
[6] Revisão de acessibilidade .. rótulos epistêmicos com redundância não-cromática? (Etapa 3, §8.3)
[7] Revisão de mídia ........... natureLabel, ocultação, propaganda rotulada? (§7)
[8] Revisão de vieses .......... eurocentrismo, estereótipo, falsa equivalência? (§4/§8)
        │
        ▼
Todas aprovadas → reviewStatus = approved → exibível
Qualquer reprovação → volta a pending/legal-review → NÃO exibível
```

O invariante permanece: enquanto `reviewStatus ∈ {pending, rejected, legal-review}`, o item **não é renderizável** por nenhuma vista da Etapa 3, **nem aparece na simultaneidade** (Etapa 1.1, §7.5; Etapa 3, §1.3/PE10).

### 9.2 Conteúdos que **nunca** podem ser publicados sem revisão humana

- Qualquer tema das tabelas de §2, §4 e §5 marcado com revisão **obrigatória** (colonização, escravidão, povos indígenas, genocídio, ditadura, racismo, raça e ciência, vacinas/saúde, pandemias).
- Qualquer **`ClaimSet`** (controvérsia, por definição, exige curadoria).
- Qualquer mídia de **violência, corpos/vítimas, propaganda, símbolos autoritários, imagem religiosa sensível** e **toda imagem/texto gerado por IA**.
- Qualquer item que toque **menores** de forma sensível, ou **pessoas vivas/identificáveis** (LGPD/R4; Etapa 2, item 11.7).
- Qualquer item cuja **licença** não esteja confirmada (Etapa 1.1) ou que envolva fonte de **risco 4/5**.

Curadoria é humana e apoiada por parcerias institucionais (universidades, museus, especialistas, professores — Q3/D11), concentrada onde dói: controvérsia, NC/licença heterogênea, rotulagem de inferência e temas das Leis 10.639/11.645.

---

## 10. Exemplos obrigatórios

Para cada exemplo: tipo de controvérsia/sensibilidade; como entra no KC; se vira `ClaimSet`; fontes preferenciais; linguagem recomendada; restrições de mídia; faixa etária; nota editorial.

### 10.1 — 1492 / Expansões marítimas
- **Tipo.** Disputa terminológica + conflito de memória + sensibilidade colonial.
- **No KC.** `Event`/`Process` com `TimeRange` 1492; lugares via WHG/Pleiades; territórios via `GeometryVersion`.
- **ClaimSet?** Sim — terminológico ("descobrimento" × "invasão" × "encontro"), `consensusStatus = terminologia sensível`.
- **Fontes.** Historiografia plural; fontes ameríndias; WHG.
- **Linguagem.** Termo em disputa apresentado com contexto; evitar marco eurocêntrico único.
- **Mídia.** Iconografia de época **rotulada** como representação da época; mapas com `GeometryVersion`; `ModernCorrespondence` do Brasil como referência rotulada (anacronismo evitado).
- **Faixa.** 9+ com mediação; pluralidade plena 15–17.
- **Nota editorial.** Mostrar Américas, África e Ásia simultâneas (Etapa 3, exemplo 4); povos originários já presentes e complexos.

### 10.2 — Colonização do Brasil
- **Tipo.** Sensibilidade colonial + conflito de memória.
- **No KC.** `Process` (colonização) + `Event`s; `CivilizationState` indígena; IBGE p/ território.
- **ClaimSet?** Sim, em interpretações (natureza/violência do processo) e termos.
- **Fontes.** Historiografia brasileira; etno-história; IPHAN; fontes indígenas.
- **Linguagem.** Nomear violência e agência indígena; evitar "civilização chegando ao vazio".
- **Mídia.** Imagens de violência ocultas por padrão; mapas rotulados.
- **Faixa.** 9+ com mediação; 12+ com disputa terminológica.
- **Nota editorial.** Lei 11.645: protagonismo e diversidade indígena; resistência, não só sujeição.

### 10.3 — Escravidão e tráfico atlântico
- **Tipo.** Conteúdo sensível (violência sistêmica) + sensibilidade racial.
- **No KC.** `Process` (sistema escravista/tráfico) com rotas como `Relationship`; portos como `Place`.
- **ClaimSet?** Em causas/escala pode haver interpretação; o **fato** do sistema é fato documentado.
- **Fontes.** Bases acadêmicas do tráfico transatlântico; historiografia afro-brasileira; arquivos.
- **Linguagem.** "Pessoas escravizadas"; sem eufemismo ("comércio"); nomear resistência (quilombos).
- **Mídia.** Cenas gráficas ocultas por padrão, rotuladas, mediadas; sem espetáculo do sofrimento.
- **Faixa.** 9+ com mediação forte; gráfico só 15+ com aviso.
- **Nota editorial.** Lei 10.639: África como origem de civilizações; agência e cultura afro-brasileira centrais. **Revisão obrigatória.**

### 10.4 — Povos indígenas no território brasileiro
- **Tipo.** Sensibilidade cultural + risco de simplificação/homogeneização.
- **No KC.** `CivilizationState` e `Event`/`Process` de história profunda (povoamento, sambaquis, marajoara — D8); presença contemporânea.
- **ClaimSet?** Onde houver disputa de datação/rota de povoamento (ex.: cronologias concorrentes) → `hipóteses concorrentes`.
- **Fontes.** Etno-historiografia; arqueologia; IPHAN; IBGE; fontes indígenas.
- **Linguagem.** Etnônimos e autodenominações; evitar "índio" genérico; presente **e** passado.
- **Mídia.** Respeito a sacralidade; cautela/consentimento com imagens de pessoas e rituais.
- **Faixa.** Todas, com profundidade crescente.
- **Nota editorial.** Lei 11.645: diversidade (centenas de povos), presença atual, não "povos do passado".

### 10.5 — Revolução Francesa e violência política
- **Tipo.** Disputa historiográfica (causas) + conteúdo violento (Terror).
- **No KC.** `Process` 1789–1799 + `Event`s pontuais; Paris como `Place`.
- **ClaimSet?** Sim — **causas** como `interpretação historiográfica`; fatos datados como fato documentado.
- **Fontes.** Historiografia revisada; arquivos; fontes primárias de época.
- **Linguagem.** Distinguir fato (datas, eventos) de interpretação (causas/significado); nomear violência do Terror sem heroificar nem demonizar.
- **Mídia.** Gravuras de execução rotuladas; gráfico forte mediado para <15.
- **Faixa.** 12+ para o Terror com cuidado; pluralidade 15–17.
- **Nota editorial.** Simultaneidade: Inconfidência Mineira, EUA, Lavoisier (Etapa 3, exemplo 1).

### 10.6 — K-Pg: impacto versus vulcanismo
- **Tipo.** Hipóteses científicas concorrentes (atribuição causal).
- **No KC.** `Process` de extinção; ocorrências PBDB; `PaleogeographicState` rotulado.
- **ClaimSet?** Sim — `consensusStatus = debate acadêmico`/`hipóteses concorrentes` (impacto Chicxulub × vulcanismo do Decão × combinação); a **extinção em si** é fato inferido de alta confiança.
- **Fontes.** PBDB (CC BY); NOAA/NCEI Paleo; EarthByte; literatura revisada.
- **Linguagem.** Separar o **fato** (houve extinção em massa) da **causa** (em debate); confiança alta no fato, média na atribuição fina.
- **Mídia.** Reconstruções rotuladas `representação artística`/`reconstrução modelada`; nada como "fotografia".
- **Faixa.** Todas; ótimo caso de alfabetização científica (como a ciência debate).
- **Nota editorial.** Modelo exemplar de incerteza legítima **dentro** de um fato consolidado.

### 10.7 — Big Bang
- **Tipo.** Consenso científico com incerteza interna + alvo de negacionismo.
- **No KC.** `Event`/`Process` `evt:big-bang`; sem localização (`SpatialUncertainty`); ~13,8 Ga ± .
- **ClaimSet?** A expansão é claim único (alta confiança); a **inflação** é claim separado `hipótese` (Etapa 2, §9.1). Criacionismo **não** é claim concorrente (§3.4).
- **Fontes.** NASA (PD); cosmologia revisada.
- **Linguagem.** "Melhor explicação científica atual" com a incerteza própria; sem opor "explicação religiosa" como ciência.
- **Mídia.** Ilustrações `representação artística`/`reconstrução modelada`; nenhuma "foto" do evento.
- **Faixa.** Todas, com profundidade crescente.
- **Nota editorial.** Separar o fato da expansão (alta confiança) dos mecanismos iniciais (hipótese).

### 10.8 — Evolução humana
- **Tipo.** Consenso (evolução) com debates internos + alvo de negacionismo + risco de uso racista.
- **No KC.** `Process` evolutivo; `Species`/`Entity` (táxons); ocorrências e datações.
- **ClaimSet?** Em relações de parentesco/datas finas → `debate acadêmico`. Criacionismo **não** é claim concorrente.
- **Fontes.** Paleoantropologia revisada; PBDB; Open Tree of Life (CC0).
- **Linguagem.** Evolução como fato; debates internos como ciência viva; **vigilância anti-racista** — jamais insinuar hierarquia entre populações humanas (cruza com §5 "raça e ciência").
- **Mídia.** Reconstruções de hominíneos rotuladas `representação artística`; cuidado com iconografia que sugira "progresso linear".
- **Faixa.** Todas.
- **Nota editorial.** Combater determinismo e racialismo; **revisão obrigatória** no cruzamento com raça.

### 10.9 — Mudanças climáticas
- **Tipo.** Consenso científico robusto + alvo de negacionismo + tema polarizado.
- **No KC.** `ClimateState` moderno (medição) e profundo (inferência); séries de indicadores.
- **ClaimSet?** **Não** entre consenso e negação (sem equivalência, §3.4). Sim para incerteza **interna** (faixas de projeção/sensibilidade) como debate dentro do consenso.
- **Fontes.** NOAA/NCEI, NASA GISS, Berkeley Earth, Copernicus, IPCC (figuras com termos próprios — recriar visualização); INPE/MapBiomas p/ Brasil.
- **Linguagem.** Afirmar o consenso (real e antrópico); mostrar incerteza de cenários como **faixa**, não como dúvida do fato; sem catastrofismo nem minimização.
- **Mídia.** Gráficos recriados a partir dos dados (não a figura alheia); mapas de monitoramento rotulados.
- **Faixa.** Todas; medição moderna vs. inferência profunda explicitada.
- **Nota editorial.** Caso-modelo de "incerteza sem falsa equivalência" (PE-Ed5).

### 10.10 — Ditadura militar brasileira
- **Tipo.** Tema politicamente sensível + conflito de memória + violência de Estado documentada.
- **No KC.** `Process` (período) + `Event`s; atores como `Entity`; fontes de comissões da verdade.
- **ClaimSet?** Sim em **interpretações legítimas** (avaliações historiográficas); **não** sobre fatos documentados de repressão/tortura — estes são fato documentado, não "um dos lados".
- **Fontes.** Comissão Nacional da Verdade, arquivos, historiografia revisada.
- **Linguagem.** Nomear censura, repressão e tortura com fonte; evitar eufemismo e falsa simetria; descrever posições de atores **com fonte**, sem opinião institucional do produto.
- **Mídia.** Fotos de repressão rotuladas/cautelosas; **propaganda do regime sempre rotulada como propaganda** (§7).
- **Faixa.** 12+ com mediação; pluralidade interpretativa 15–17.
- **Nota editorial.** Memória das vítimas; pluralidade apenas onde a disputa é legítima, não sobre crimes documentados. **Revisão obrigatória** (jurídica e historiográfica; cuidado com pessoas vivas/identificáveis — LGPD).

---

## 11. Impacto na Etapa 4

Esta política **condiciona** a Etapa 4 (camadas científicas e históricas) de forma vinculante. Antes de popular qualquer camada, a Etapa 4 passa a operar sob estas obrigações:

1. **Toda controvérsia legítima nasce como `ClaimSet`.** A Etapa 4 não pode "resolver" uma controvérsia escolhendo um claim; deve estruturá-la com `consensusStatus` (§3), claims atribuídos e pesos. Isso vale especialmente para os casos 10.1, 10.5, 10.6, 10.8.
2. **Negacionismo e pseudociência nunca entram como claim concorrente.** Entram apenas como **objeto rotulado** (`desinformação/negacionismo rejeitado`), fora dos `ClaimSet` legítimos (§3.4, §5). A Etapa 4 não cria equivalência.
3. **Consenso é tipado como consenso; incerteza interna é separada do fato.** Ao popular ciência (§5), a Etapa 4 separa o fato consolidado (alta confiança) dos mecanismos/projeções em aberto (hipótese/faixa) — como nos casos Big Bang, origem da vida, K-Pg, clima.
4. **Temas das tabelas §2/§4/§5 marcados com revisão obrigatória entram com `reviewStatus = pending`** e só se tornam exibíveis após o fluxo de §9. A Etapa 4 trata isso como invariante, não como etapa opcional.
5. **Leis 10.639/2003 e 11.645/2008 viram exigência de cobertura e protagonismo**, não complemento: ao montar as camadas Civilizações, Política, Cultura e Brasil, a Etapa 4 garante presença e agência de história/cultura africana, afro-brasileira e indígena, em **simultaneidade** com a europeia (cruza com a função da Etapa 3, §4).
6. **A camada de mídia segue o regime de §7**: `natureLabel` obrigatório, ocultação por padrão de conteúdo gráfico, propaganda sempre rotulada, IA sempre rotulada e revisada, licença por asset confirmada — coerente com a meta-camada Mídia da Etapa 3 (§5.2).
7. **A linguagem de povoamento das camadas segue §8**: sem eufemismo, sem anacronismo não explicado, sem reprodução de discurso discriminatório como voz própria, com termos sensíveis explicados e nomes originários em primeiro plano (`nameVariants[]` datadas).
8. **A faixa etária (§6) condiciona a granularidade de exposição**, não o fato: a Etapa 4 popula o conteúdo factual uma vez e marca os **níveis de exposição/ocultação/aviso** por faixa, deixando a adaptação de linguagem para a camada auxiliar (IA rotulada, sobre conteúdo curado — A3/Q5).
9. **A governança de §9 define a porta de entrada da Etapa 4**: nenhum item sensível é dado como "pronto" sem as revisões aplicáveis aprovadas. Os papéis de revisão (científica, historiográfica, pedagógica, faixa, jurídica, acessibilidade, mídia, vieses) são pré-requisito de publicação.

Em síntese: a Etapa 4 deixa de ser uma tarefa de "preencher fatos" e passa a ser uma tarefa de **preencher fatos tipados, atribuídos, rotulados, recortados por faixa e revisados**, sob esta política. A pendência crítica que a Etapa 3 apontou (item 10.2) está, com este documento, resolvida e pronta para reger o povoamento das camadas.

---

## Encerramento e handoff

Esta microetapa entrega a **política editorial operacional** que faltava: princípios (incluindo as sete distinções que impedem falsa equivalência), uma tipologia de controvérsias com decisão de entrada para cada uma, as regras de `ClaimSet`/`consensusStatus`, o tratamento de temas históricos e científicos sensíveis, os cinco níveis de exposição por faixa etária, o regime de mídia sensível, o padrão de linguagem, o fluxo de governança com os conteúdos de revisão obrigatória, dez exemplos aplicados e o impacto vinculante sobre a Etapa 4. Nada aqui modela novos dados, escreve código, propõe MVP, define UX final ou entra em currículo/professor.

**Handoff:** com a Etapa 3.1 aprovada, a **Etapa 4 (camadas científicas e históricas)** pode ser executada, populando as camadas e os States da Etapa 3 sob esta política — `ClaimSet` para controvérsia legítima, rótulo de rejeição para negacionismo, consenso tipado como consenso, revisão humana obrigatória onde indicado, e Leis 10.639/11.645 como cobertura estrutural.

*Documento de entrega da Etapa 3.1, sob a baseline v1.0, a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2) e a experiência da Etapa 3. Não modela dados, não contém código, não propõe MVP, não define UX final nem entra em currículo/professor.*
