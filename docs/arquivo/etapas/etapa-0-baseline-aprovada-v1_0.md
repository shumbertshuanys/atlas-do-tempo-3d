# Etapa 0 — Visão, Tese e Escopo do Produto

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Baseline aprovada · versão 1.0 · 12/06/2026
**Natureza do documento:** referência consolidada e saneada. Integra (a) a entrega original da Etapa 0, (b) os seis ajustes de aprovação (A1–A6) e (c) as respostas às perguntas críticas (Q1–Q6). Todas as etapas futuras (1–14) referenciam esta baseline. Alterações posteriores geram nova versão (v1.x) com registro.

---

## 1. Tese do produto

O produto é uma base universal **curada** de eventos, processos e conceitos — do Big Bang ao presente — navegável simultaneamente por tempo (linha do tempo multiescala) e espaço (globo/mapa 3D), em que cada afirmação carrega fonte, tipo de claim e nível de confiança. Sobre essa base, uma camada de conformidade brasileira (BNCC, LDB, LGPD, acessibilidade, faixa etária) e um motor de correspondência transformam o planejamento real do professor em aulas contextualizadas — mantendo sempre o mundo inteiro visível e navegável.

**Princípio central:** o conhecimento é universal; o currículo organiza o uso; o professor define o foco; a experiência visual mantém o mundo inteiro navegável. A grade define o foco da aula; nunca o limite do sistema.

---

## 2. Objetivo da Etapa 0

Fixar visão, tese e limites do produto antes de qualquer decisão de dados, design ou tecnologia, produzindo o documento que governa as Etapas 1 a 14: o que o produto é, para quem é, por que venceria, o que ele explicitamente não é, e quais decisões estruturantes precisam ser tomadas de saída porque condicionam todo o resto (modelo de tempo, postura epistêmica, sequência de público, restrições de hardware e conectividade escolar).

---

## 3. Escopo da Etapa 0

**Incluído:** tese; diagnóstico de problema, mercado e realidade escolar; públicos e sequenciamento; proposta de valor e diferenciais; arquitetura macro validada e refinada; não-objetivos; critérios de sucesso; política de IA generativa; riscos estratégicos; perguntas críticas (resolvidas); diretrizes recebidas para a Etapa 1.

**Excluído (etapas próprias):** auditoria de fontes (Etapa 1); modelagem de dados (2); timeline e globo (3); camadas de conteúdo (4); função de simultaneidade em detalhe (5); conformidade detalhada (6); planejamento docente (7); matching (8); saídas pedagógicas (9); design/UX (10); stack técnico (11); MVP (12); pipeline de ingestão (13); validação escolar, jurídica e comercial (14). Quando algo dessas etapas aparece aqui, é restrição ou hipótese a validar, nunca especificação.

---

## 4. Diagnóstico

### 4.1 O problema (três lacunas)

1. **Fragmentação tempo × espaço × fonte.** O ensino de História, Geografia e Ciências opera com materiais desconectados: a narrativa está no livro, o mapa em outra página, a fonte primária quase nunca aparece e o vídeo avulso não tem proveniência verificável.
2. **Cegueira de simultaneidade.** O aluno estuda a Revolução Francesa sem saber que, no mesmo 1789, a Inconfidência Mineira era desmantelada em Minas Gerais. A linha do tempo escolar é sequencial e eurocêntrica, enquanto as Leis 10.639/2003 e 11.645/2008 exigem história africana, afro-brasileira e indígena — que raramente aparece em paralelo cronológico com a história europeia. A função "o que acontecia no mundo neste momento?" ataca essa lacuna estruturalmente.
3. **Custo de preparação docente.** Contextualizar uma aula com mapas, fontes e simultaneidade exige hoje horas de garimpo que o professor não tem.

### 4.2 Mercado e concorrência

- O conceito "globo 3D + timeline" está sendo validado internacionalmente, mas de forma frágil. O **Globe of History** (lançado em 2025) cobre ~6.000 anos com ~15.000 eventos montados por pipeline de IA sobre Wikipedia/Wikidata, com verificação automatizada e checagens manuais pontuais — em beta, cobertura regional desigual, somente desktop. Valida a demanda e expõe exatamente a fraqueza que este projeto proíbe: Wikipedia/IA como autoridade final.
- **Geacron** (plano educacional pago com Terra 3D e timelines comparativas), **TimeMaps** (mais de mil mapas com enciclopédia escolar), **Omniatlas** e **Ostellus**: anglófonos, restritos à história registrada (sem tempo profundo), sem tipagem de incerteza, sem camada curricular brasileira.
- Precedente de mortalidade: o **ChronoZoom** (Microsoft Research/Berkeley), pioneiro de timelines de Big History, foi descontinuado — o risco real é sustentar curadoria, não construir visualização.
- No Brasil, o setor de edtechs é grande mas concentrado em outro lugar: **467 edtechs ativas** mapeadas (Liga Ventures, 2025), com maiores categorias em capacitação profissional (12,4%) e educação corporativa (11,8%); o Brasil concentra ~47% das edtechs da América Latina (Distrito, 2025).
- **Lacuna de mercado:** nenhum player, nacional ou estrangeiro, combina tempo profundo (13,8 bilhões de anos) + globo navegável + proveniência com nível de confiança + camada de aplicação à educação brasileira. A categoria está aberta.

### 4.3 Realidade da escola brasileira (restrições de projeto)

- **46,018 milhões** de matrículas na educação básica em **178,76 mil escolas** públicas e privadas; ~**2,4 milhões de professores**; 25,8 milhões de matrículas só no ensino fundamental (INEP/MEC, Censo Escolar 2025).
- Conectividade melhorou — internet em 94,5% das escolas (era 82,8% em 2021) — mas apenas **~70% têm internet adequada para uso pedagógico** (eram 45%), com maior gargalo na região Norte, mesmo após R$ 3 bilhões investidos entre 2023 e 2025 (Censo Escolar 2025).
- Precariedade docente relevante: na rede pública, ~1,13 milhão de efetivos contra ~813 mil temporários, que costumam atuar em condições mais precárias (Censo Escolar 2025).

**Consequências de projeto:** degradação progressiva (3D → 2D → estático) e pacotes offline são requisitos de fundação; o produto precisa economizar tempo do professor em minutos, ou não será adotado.

### 4.4 Implicação central

O difícil deste produto não é renderizar um globo — CesiumJS, three.js e dados do GPlates/EarthByte resolvem render e paleogeografia. O fosso competitivo é o trio: (a) grafo de conhecimento curado com proveniência e incerteza tipada; (b) indexação BNCC e motor de correspondência com o planejamento real do professor; (c) experiência que funciona no hardware e na conexão da escola brasileira real.

---

## 5. Decisões aprovadas (D1–D11, com ajustes incorporados)

- **D1 — Categoria e posicionamento.** Atlas espaçotemporal de conhecimento com camada de aplicação pedagógica: recurso educacional digital complementar, objeto de aprendizagem e ferramenta de apoio ao professor. Nunca substituto de currículo, livro didático ou LMS.

- **D2 — Arquitetura knowledge-first com duas camadas transversais.** As seis camadas originais (Knowledge Core → Conformidade → Planejamento → Matching → Saída pedagógica → Experiência) são mantidas, acrescidas de duas transversais: **Governança editorial e proveniência** (curadoria humana, classificação de fontes, versionamento de claims) e **Privacidade, segurança e telemetria** (LGPD, dados de menores, analytics ético).

- **D3 — Duplo caminho de consumo.** A conformidade atua como filtro/serviço (linguagem por idade, adequação etária), não como portão sequencial: o fluxo do professor atravessa todas as camadas; a exploração livre vai do Knowledge Core direto à experiência. O Content Matching Engine existe apenas no fluxo do professor.

- **D4 — Coração técnico: consulta espaçotemporal.** O ativo central é a capacidade de consulta tempo × espaço × tema × nível de confiança. *Reforçado pelo ajuste A6:* "o que acontecia no mundo neste momento?" é **capacidade nativa do Knowledge Core**, que influencia o modelo de dados desde a origem; a feature visual é uma vista dessa capacidade, não um módulo à parte.

- **D5 — Escopo por espinha dorsal, não por enciclopédia.** Largura total (Big Bang ao presente) com profundidade seletiva. *Conforme ajuste A5:* a ordem de grandeza de 150–300 nós estruturantes e 1.500–3.000 eventos curados é **hipótese de trabalho, não congelada** — será validada nas Etapas 1 e 2. "Completude" significa cobertura estrutural, nunca exaustividade.

- **D6 — Modelo de tempo híbrido.** Tempo profundo pela escala cronoestratigráfica internacional (ICS); tempo histórico por datas calendárias com intervalos e incerteza explícita; navegação multiescala (zoom logarítmico de bilhões de anos a um dia). Decisão estruturante: afeta modelo de dados, timeline e matching.

- **D7 — Honestidade epistêmica como feature visível.** Todo claim carrega tipo (fato documentado, medição, inferência, estimativa, hipótese, controvérsia, interpretação historiográfica) e nível de confiança exibidos na interface; toda mídia carrega natureza (fotografia, mapa, gráfico, reconstrução científica, simulação, representação artística, aproximação didática). Diferencial direto contra pipelines Wikipedia/IA.

- **D8 — Lente Brasil estrutural.** Toda janela temporal deve poder responder "e no território que hoje é o Brasil?", incluindo história profunda indígena (povoamento das Américas, sambaquis, cultura marajoara), em conformidade com as Leis 10.639/2003 e 11.645/2008.

- **D9 — Sequência de público e universalidade do modelo.** *Atualizada pelos ajustes A1/Q1:* V1 prioriza professores de **História, Geografia e Ciências** do **Fundamental II + Ensino Médio**, em uso mediado em sala; porém a arquitetura **nasce universal**, já preparada para Física, Química, Biologia, Matemática, Filosofia e Sociologia. O MVP pode ser recortado; o modelo conceitual, não. Aluno autônomo, famílias, museus e secretarias entram em ondas posteriores.

- **D10 — Postura técnica macro com escola pública como fundação.** *Atualizada pelos ajustes A2/Q2:* web-first com degradação progressiva (globo 3D → mapa 2D → cartões estáticos) e pacotes offline. **Offline parcial, acessibilidade, LGPD, computadores modestos e modo projetor são requisitos de fundação**, ainda que a entrada comercial inicial ocorra por escolas privadas e sistemas de ensino.

- **D11 — Conteúdo, licenças, curadoria e IA.** Prioridade a domínio público, Creative Commons e dados abertos, com licença rastreada por asset. Wikidata permanece como índice/ponte de identificadores, não como autoridade. *Conforme Q3:* pipeline desenhado para **curadoria humana mínima interna + parcerias institucionais** (universidades, museus, professores, especialistas); a curadoria nunca depende exclusivamente de IA. Política de IA generativa detalhada na seção 7.

---

## 6. Ajustes de aprovação incorporados (A1–A6)

| ID | Ajuste | Onde foi incorporado |
|----|--------|----------------------|
| A1 | V1 prioriza História/Geografia/Ciências, mas a arquitetura nasce universal (Física, Química, Biologia, Matemática, Filosofia, Sociologia). MVP recortável; modelo conceitual, não. | D9 |
| A2 | Requisitos de escola pública (offline parcial, acessibilidade, LGPD, hardware modesto, modo projetor) são fundação, não pendência futura. | D10; critérios de sucesso (§8.4) |
| A3 | IA generativa somente como camada auxiliar; nunca fonte factual. Usos permitidos e vedações detalhados. | Seção 7 |
| A4 | Nome não decidido agora; manter "Atlas do Tempo 3D" e "Linha do Tempo Total" como provisórios; INPI/naming na etapa jurídico-comercial. | §13 (pendências, Etapa 14) |
| A5 | Espinha dorsal (150–300 nós / 1.500–3.000 eventos) é hipótese; validar nas Etapas 1 e 2; não congelar. | D5 |
| A6 | "O que acontecia no mundo neste momento?" é capacidade central do Knowledge Core, influenciando o modelo de dados desde o início. | D4; Etapas 2 e 5 |

---

## 7. Política de IA generativa (consolidada — A3/Q5)

**Usos permitidos** (sempre operando sobre conteúdo curado do Knowledge Core, com fontes rastreáveis e rotulagem adequada):

1. adaptação de linguagem por faixa etária;
2. geração de roteiro de aula;
3. geração de quiz;
4. sugestão de atividade;
5. resumo didático;
6. reorganização pedagógica.

**Vedações e salvaguardas:**

- fatos, datas, claims e fontes vêm **exclusivamente** do Knowledge Core, nunca da IA;
- nenhum conteúdo gerado entra no Knowledge Core sem curadoria humana;
- toda saída assistida por IA é rotulada como tal para o usuário;
- a IA não cria, altera nem "completa" fontes, níveis de confiança ou claims;
- qualquer ampliação de uso de IA é decisão formal de baseline, não acréscimo silencioso.

---

## 8. Modelo conceitual

### 8.1 Arquitetura macro (v0.2)

```
                 ┌─────────────────────────────────────────┐
                 │            KNOWLEDGE CORE               │  núcleo
                 │     base universal de conhecimento      │
                 └───────────────────┬─────────────────────┘
        exploração livre │           │  fluxo do professor
        (conformidade    │           ▼
        atua como        │  ┌─────────────────────────────┐
        filtro: idade,   │  │  CONFORMIDADE EDUCACIONAL   │
        adequação)       │  │ BNCC · LDB · LGPD · acessib.│
                         │  └──────────────┬──────────────┘
                         │                 ▼
                         │  ┌─────────────────────────────┐
                         │  │  PLANEJAMENTO DO PROFESSOR  │
                         │  │  grade real · temas · metas │
                         │  └──────────────┬──────────────┘
                         │                 ▼
                         │  ┌─────────────────────────────┐
                         │  │   CONTENT MATCHING ENGINE   │
                         │  │ planejamento × conhecimento │
                         │  └──────────────┬──────────────┘
                         │                 ▼
                         │  ┌─────────────────────────────┐
                         │  │      SAÍDA PEDAGÓGICA       │
                         │  │ planos · atividades · aval. │
                         │  └──────────────┬──────────────┘
                         ▼                 ▼
                 ┌─────────────────────────────────────────┐
                 │         CAMADA DE EXPERIÊNCIA           │
                 │  timeline + globo 3D · modos professor, │
                 │       estudante e exploração livre      │
                 └─────────────────────────────────────────┘

   TRANSVERSAIS A TODAS AS CAMADAS:
   · Governança editorial e proveniência (curadoria, fontes, versões)
   · Privacidade, segurança e telemetria (LGPD, menores)
```

**Notas de leitura:** a conformidade incide na exploração livre apenas como filtro (linguagem por faixa etária, adequação de conteúdo), preservando o princípio de que a grade define o foco, não o universo. O Content Matching Engine só existe no fluxo do professor. As camadas transversais permeiam todas as demais: nada entra no Knowledge Core sem fonte classificada e claim tipado; nada é armazenado ou medido fora das regras de privacidade.

### 8.2 Cena canônica (teste de produto)

Professora de História do 8º ano abre a aula sobre a Revolução Francesa. O globo centra em Paris, a timeline em 1789; o dossiê da Queda da Bastilha aparece com fontes e o rótulo "fato documentado". Ela aciona "o que acontecia no mundo neste momento?": Minas Gerais acende com a Inconfidência Mineira (fato documentado), os Estados Unidos com o primeiro governo sob a nova Constituição (fato documentado), e a camada de ciência mostra Lavoisier publicando o *Traité élémentaire de chimie* no mesmo ano. Um aluno arrasta a timeline até 2,4 bilhões de anos atrás: o globo troca para uma reconstrução paleogeográfica rotulada como tal, com nota de incerteza, exibindo o Grande Evento de Oxidação como inferência científica. Uma única cena exercita os três diferenciais — simultaneidade, tempo profundo e honestidade epistêmica — e os dois caminhos de consumo.

### 8.3 Personas

- **Primária (V1):** professor(a) de História/Geografia/Ciências do Fundamental II e Ensino Médio, com pouco tempo de planejamento e equipamento variável.
- **Compradora:** coordenação pedagógica/direção de escola privada ou sistema de ensino.
- **Posteriores:** estudante de 11–17 anos (uso mediado em V1, autônomo depois); secretarias de educação; famílias; museus e instituições científicas como canal de parceria e co-curadoria.

### 8.4 Critérios de sucesso (norte — a refinar na Etapa 12)

1. O professor monta uma aula contextualizada, com fontes, em até 15 minutos.
2. O aluno consegue responder, usando o sistema, o que acontecia em pelo menos três outras regiões do mundo durante o evento estudado.
3. 100% dos itens da espinha dorsal com fonte classificada e claim tipado — sem exceção.
4. A experiência mínima (mesmo que 2D) funciona em computador escolar modesto, em conexão limitada ou offline parcial, com modo projetor e acessibilidade desde a fundação.

### 8.5 Não-objetivos (válidos para V1 e, em vários casos, permanentes)

- Não é LMS nem diário de classe.
- Não é rede social.
- Não é tutor-chatbot como produto central.
- Não é enciclopédia exaustiva.
- Não é VR-first.
- Não substitui avaliação oficial nem material didático adotado.
- Não trata a plataforma como substituto obrigatório do currículo escolar.

---

## 9. Fontes (visão geral — auditoria completa na Etapa 1)

- **Universais científicas e históricas:** NASA, ESA, JPL, NASA Exoplanet Archive, International Commission on Stratigraphy (ICS), GPlates/EarthByte, NOAA/NCEI, Paleobiology Database, Macrostrat, USGS, World Historical Gazetteer, PeriodO, Seshat, Our World in Data, artigos revisados por pares; Wikidata apenas como índice.
- **Brasileiras:** IBGE, INPE, MapBiomas, CPRM/SGB, Arquivo Nacional, Biblioteca Nacional, museus e bibliotecas digitais, documentos oficiais BNCC/MEC, INEP (Censo Escolar).
- **Jurídico-normativas e de contexto escolar:** LGPD, LDB, ECA, Leis 10.639/2003 e 11.645/2008, Marco Civil da Internet, Política Nacional de Educação Digital (Lei 14.533/2023); pesquisas TIC Educação (Cetic.br) e materiais do CIEB para infraestrutura e adoção.

Toda fonte será classificada na Etapa 1 conforme as dimensões da seção 12.

---

## 10. Riscos (R1–R9)

| ID | Risco | Prob. × Impacto | Mitigação principal |
|----|-------|-----------------|---------------------|
| R1 | Explosão do custo de curadoria (risco nº 1) | Alta × Alto | Espinha dorsal (D5), profundidade sob demanda, pipeline editorial priorizado, parcerias institucionais |
| R2 | Hardware e conectividade escolar (~30% sem internet pedagógica adequada) | Alta × Alto | Degradação progressiva, pacotes offline, modo projetor (D10) |
| R3 | Controvérsias de conteúdo (evolução, Big Bang, colonização, escravidão, povos indígenas) | Média × Alto | Tipagem de claims, fontes visíveis, interpretações historiográficas múltiplas, política editorial escrita antes da Etapa 4 |
| R4 | Jurídico e conformidade (LGPD/menores, direitos de imagem, acessibilidade e-MAG/WCAG) | Média × Alto | Privacy by design (Etapa 11), licença rastreada por asset, acessibilidade como requisito de aceitação |
| R5 | Adoção docente (sobrecarga, alta proporção de temporários) | Alta × Médio | Valor percebido em minutos, aulas prontas ajustáveis, modo projetor de um clique |
| R6 | Ciclo de venda no setor público | Alta × Médio | Receita inicial em escolas privadas/sistemas de ensino; público como segunda onda (validar na Etapa 14) |
| R7 | Sustentabilidade técnica (precedente ChronoZoom) | Média × Alto | Núcleo enxuto, padrões abertos, dados desacoplados da visualização |
| R8 | Deriva de escopo ("universal" = infinito) | Alta × Médio | Não-objetivos versionados (§8.5); ampliações como decisão formal |
| R9 | Contaminação por fontes fracas ou conteúdo gerado | Média × Alto | Curadoria humana obrigatória, Wikidata só índice, rotulagem de apoio de IA (§7) |

---

## 11. Perguntas críticas — resolvidas (Q1–Q6)

- **Q1 — Recorte etário/disciplinar:** confirmado Fundamental II + Ensino Médio, foco inicial em História, Geografia e Ciências; modelo nasce preparado para todas as áreas. → incorporado em D9.
- **Q2 — Estratégia comercial:** entrada por escolas privadas e sistemas de ensino, com requisitos de escola pública considerados desde o início. → incorporado em D10.
- **Q3 — Curadoria:** pipeline assume curadoria humana mínima interna + parcerias institucionais (universidades, museus, professores, especialistas); nunca exclusivamente IA. → incorporado em D11.
- **Q4 — Naming:** sem decisão agora; manter os dois nomes provisórios; verificação INPI/naming na etapa jurídico-comercial. → pendência da Etapa 14.
- **Q5 — IA generativa:** permitida apenas como assistente pedagógico e de linguagem, nunca como fonte factual; toda geração baseada no conteúdo curado. → consolidado na seção 7.
- **Q6 — Prazo/orçamento de MVP:** sem restrição fechada; a **Etapa 12 deverá propor três cenários: MVP mínimo, MVP intermediário e MVP robusto**. → pendência da Etapa 12.

---

## 12. Diretrizes recebidas para a Etapa 1 — Auditoria de fontes universais

A Etapa 1 (executada somente mediante solicitação) deverá classificar cada fonte por:

1. área de conhecimento;
2. confiabilidade;
3. licença;
4. tipo de dado;
5. formato/API;
6. cobertura temporal;
7. cobertura geográfica;
8. possibilidade de automação;
9. necessidade de curadoria humana;
10. risco de uso educacional;
11. prioridade para o Knowledge Core.

---

## 13. Governança do documento, pendências e próximos passos

- **Governança:** esta é a baseline v1.0 da Etapa 0, aprovada. Alterações futuras geram v1.x com registro de mudança; ampliações de escopo são decisões formais.
- **Pendências herdadas:** validação dos números da espinha dorsal (Etapas 1 e 2 — A5); três cenários de MVP (Etapa 12 — Q6); naming e verificação INPI (Etapa 14 — A4); política editorial de controvérsias escrita antes da Etapa 4 (R3).
- **Próximo passo:** Etapa 1 — Auditoria de fontes universais, quando solicitada, seguindo integralmente as dimensões da seção 12 e as decisões D5, D6, D7, D8 e D11.

---

## Referências consultadas na Etapa 0

- INEP/MEC. *Censo Escolar da Educação Básica 2025 — Notas Estatísticas.* <https://download.inep.gov.br/publicacoes/institucionais/estatisticas_e_indicadores/notas_estatisticas_censo_escolar_da_educacao_basica_2025.pdf>
- Consed. *Censo registra queda de matrículas na educação básica* (fev/2026). <https://www.consed.org.br/noticia/censo-registra-queda-de-matriculas-na-educacao-basica>
- Jeduca. *Censo Escolar 2025: para ir além da cobertura dos números gerais* (fev/2026). <https://jeduca.org.br/noticia/censo-escolar-2025-para-ir-alem-da-cobertura-dos-numeros-gerais>
- Conecta Professores. *Professores e escolas: veja os principais dados do Censo Escolar 2025* (mar/2026). <https://conectaprofessores.com/2026/03/12/professores-e-escolas-veja-os-principais-dados-do-censo-escolar-2025/>
- Liga Ventures / Startup Scanner. *Startup Landscape: Edtechs 2025.* <https://liga.ventures/insights/follow-on/startup-landscape-edtechs-2025/>
- Distrito. *EdTech Report 2025.* <https://materiais.distrito.me/edtech-report-2025>
- Análises de terceiros sobre o Globe of History: Complete AI Training (nov/2025) <https://completeaitraining.com/ai-tools/globe-of-history/>; Outils-TICE (abr/2026) <https://outilstice.com/en/2026/04/globe-of-history-carte-interactive-histoire-classe/>
- Sites oficiais: Geacron, TimeMaps (<https://timemaps.com/>), Omniatlas (<https://omniatlas.com/>), Ostellus Atlas (<https://atlas.ostellus.com/>)

*Nota: dados de mercado e censo citados conforme divulgação pública até jun/2026; números sujeitos a atualização na Etapa 14.*
