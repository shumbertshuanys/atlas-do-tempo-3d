# Etapa 1 — Auditoria de Fontes Universais

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da Etapa 1 · sob a baseline v1.0 (Etapa 0 aprovada) · 12/06/2026
**Escopo desta etapa (e seus limites):** esta etapa **apenas audita e classifica fontes**. Conforme solicitado, ela **não** modela dados, **não** propõe MVP, **não** escreve código e **não** avança para arquitetura técnica. A modelagem do Knowledge Core é trabalho da Etapa 2; o desenho de pipeline/ingestão é posterior. O que segue é insumo de decisão para essas etapas.
**Decisões da baseline que orientam a auditoria:** D5 (espinha dorsal de 150–300 nós / 1.500–3.000 eventos como hipótese a validar aqui), D6/D7 (o que auditar primeiro), D11 (prioridade a domínio público, Creative Commons e dados abertos; licença rastreada por asset; Wikidata como índice, nunca autoridade; curadoria humana mínima + parcerias), A6/D4 ("o que acontecia no mundo neste momento?" como capacidade central, que exige tempo × espaço × confiança em cada item).

---

## 0. Princípio organizador da auditoria

Antes do mapa e da tabela, três distinções que determinam *como* cada fonte pode ser usada — e que dissolvem várias "restrições" aparentes.

### 0.1 Fato × expressão × objeto digitalizado

A pergunta "esta fonte é utilizável?" quase nunca tem resposta única. Ela se decompõe em três camadas jurídicas distintas:

- **Fato** — uma idade de limite estratigráfico, a data de uma batalha, uma contagem populacional, uma coordenada. **Fatos não são protegíveis por direito autoral.** Podem sempre ser **re-codificados** no nosso próprio modelo, com **atribuição** à fonte como boa prática científica (não como obrigação legal). *Exemplo:* não se pode "copiar" o gráfico da Tabela Cronoestratigráfica do ICS sem respeitar a licença dele, mas o fato de o Jurássico começar em ~201,4 Ma é livre.
- **Expressão** — um gráfico específico, um parágrafo de prosa, um mapa estilizado, uma figura. **É protegível** e governada pela licença da fonte. Aqui é onde NC (não-comercial), ShareAlike e licenças proprietárias mordem.
- **Objeto digitalizado de obra em domínio público** — um mapa do século XVIII é PD, mas o *scan* de um provedor pode vir com termos NC. Para obras em domínio público, **prefira o provedor que declara PD/CC0** em vez do provedor que reivindica restrição sobre a digitalização.

**Consequência operacional:** o que o Knowledge Core ingere, em sua espinha dorsal, são **fatos tipados com proveniência** — não as expressões alheias. Isso é coerente com o diferencial de "honestidade epistêmica" e com D11. Fontes NC (Seshat, GADM, gráfico do ICS, scans do David Rumsey) deixam de ser bloqueio total e passam a ser "use o fato, não a expressão; e, para PD, troque de provedor".

### 0.2 Três níveis de confiabilidade (e a regra do índice)

A baseline já fixou a regra inegociável: **Wikidata, Wikipedia e IA ajudam a localizar e reconciliar dados, mas nunca são autoridade final.** Operacionalizo isso como três níveis, usados em toda a tabela:

- **A — Autoridade primária:** a instituição científica ou oficial que *gera* o dado (NASA, USGS, IBGE, ICS, Pleiades).
- **B — Agregador/compilador confiável:** reúne fontes A com curadoria e proveniência rastreável (Our World in Data, Macrostrat, World Historical Gazetteer, World Bank).
- **C — Índice/ponte:** localiza, desambigua e conecta identificadores, mas **não afirma fatos** (Wikidata, Wikipedia, DBpedia, VIAF, IA generativa).

Toda *claim* na espinha dorsal precisa rastrear até uma fonte **A** ou **B**. Fontes **C** só resolvem "onde está o dado" e "este 'Paris' é o mesmo 'Paris'", jamais "o dado é este".

---

## 1. Mapa das fontes (por camada)

Visão organizada nas doze camadas pedidas. Para cada camada: as autoridades centrais, o que entregam e seu papel. (A classificação dimensão a dimensão está na Seção 2; a licença de cada uma, na Seção 2 e nos riscos da Seção 5.)

### Camada 1 — Universo e astronomia
Âncoras do início da linha do tempo (Big Bang ~13,8 Ga, formação do Sistema Solar, eventos cósmicos) e o "céu" navegável.
- **NASA** (Open Data Portal, JPL, NASA Image and Video Library) — autoridade primária, domínio público. Eventos cósmicos, efemérides, imageria.
- **NASA Exoplanet Archive** (IPAC/Caltech) — catálogo de exoplanetas; dado público.
- **ESA** (incl. ESA/Hubble, ESASky, **missão Gaia**) — autoridade europeia; atenção: licença **CC BY-SA IGO** (ShareAlike).
- **CDS Strasbourg** (SIMBAD, VizieR) — catálogos estelares agregados; reuso com citação.
- **IAU** — autoridade de **nomenclatura** (nomes de corpos, estrelas); **Minor Planet Center** — órbitas de corpos menores.

### Camada 2 — Geologia e escala do tempo
A **espinha do eixo de tempo profundo** — a régua sobre a qual tudo se posiciona.
- **ICS — International Chronostratigraphic Chart** (IUGS) — **a autoridade** sobre nomes e idades de éons/eras/períodos/épocas/idades. O *gráfico* é CC BY-NC-SA; os *fatos* (nomes + idades de limite) são livres → re-codificar e atribuir.
- **Macrostrat** (UW-Madison) — **CC BY 4.0**, com API; entrega a escala de tempo internacional de forma legível por máquina + colunas geológicas. **Veículo aberto preferencial** para a régua do tempo.
- **USGS** — domínio público; dados geológicos, minerais, riscos.

### Camada 3 — Atmosfera e clima
Estados climáticos ao longo do tempo (do Grande Evento de Oxidação às glaciações e ao clima moderno).
- **NOAA / NCEI** (incl. Paleoclimatology) — domínio público; séries e paleoclima.
- **NASA GISS** (GISTEMP) — domínio público; temperatura global moderna.
- **Copernicus / ECMWF (ERA5)** — licença Copernicus (reuso amplo com atribuição).
- **Berkeley Earth** — CC BY; reconstrução de temperatura.
- **IPCC** — síntese de referência; **figuras** com termos próprios (verificar antes de reproduzir expressão).
*Nota epistêmica:* clima de tempo profundo é **inferência modelada** → exige rótulo, nunca "fato".

### Camada 4 — Tectônica e paleogeografia
A **morfologia do globo no tempo profundo** — continentes rotacionados por idade.
- **GPlates** (software, GPL) + **dados EarthByte** (**CC BY 3.0**) — reconstruções de placas e modelos de rotação. Núcleo aberto da paleogeografia.
- **GPlates Web Service / pyGPlates** — acesso programático.
- **PALEOMAP / Scotese** — mapas paleogeográficos clássicos; termos a confirmar (preferir EarthByte como rota aberta).
- **Deep Time Maps** — **proprietário/licenciado** (uso restrito).
*Nota epistêmica:* toda reconstrução aqui é **modelo** → rotular como tal, com nota de incerteza.

### Camada 5 — Evolução da vida e paleobiologia
Surgimento/extinção de táxons, extinções em massa — os "eventos biológicos" do tempo profundo.
- **Paleobiology Database (PBDB)** — **CC BY 4.0**, API robusta; ocorrências fósseis globais.
- **GBIF** — mediado, **licença por dataset** (CC0 / CC BY / CC BY-NC) → filtrar para CC0/CC BY.
- **Open Tree of Life** — árvore sintética (CC0).
- **Macrostrat** — ligação litologia/fóssil/tempo (CC BY).
- **Fossilworks** — interface a dados PBDB (CC BY), porém projeto **dormante** (risco de manutenção).

### Camada 6 — História humana e civilizações
Eventos, povos, lugares e pessoas da história registrada — a base da **simultaneidade** na era humana.
- **Pleiades** — **CC BY**; gazetteer autoritativo do mundo antigo.
- **World Historical Gazetteer (WHG)** — agregador; estrutura **CC BY**, datasets contribuídos com **licença variável** (CC BY / CC BY-NC) → filtrar por dataset.
- **PeriodO** — definições de períodos (gazetteer temporal); aberto (confirmar CC0).
- **Pelagios / Peripleo / Nomisma / ToposText** — *linked data* de lugares, moedas e textos antigos (CC BY).
- **Seshat: Global History Databank** — **CC BY-NC-SA** → **restrito** (ver Seção 4); só fatos re-deriváveis via curadoria.
- **Wikidata** (CC0) e **Wikipedia** (CC BY-SA) — **índice/localização apenas**, nunca autoridade.

### Camada 7 — Eventos contemporâneos
A ponta "presente" da linha do tempo: indicadores e fatos recentes/correntes.
- **Our World in Data** — **CC BY** (próprio); terceiros pela licença original → checar por indicador.
- **World Bank Open Data** — **CC BY 4.0** (uso comercial permitido).
- **UN / UNESCO / WHO (GHO)** — geralmente abertos com atribuição (por dataset).
- **GDELT** — metadados de eventos a partir de notícias globais; usar a **camada de evento/metadado** (o texto dos artigos é de terceiros).
- **ACLED** — **licença comercial obrigatória** + cláusula anti-substituto → **restrito/excluído** sem licença (ver Seção 4).

### Camada 8 — Dados geográficos e regionais (base cartográfica)
O **eixo espaço** em todas as escalas — a base do globo.
- **Natural Earth** — **domínio público**; base vetorial (países, costas, físico).
- **OpenStreetMap** — **ODbL** (ShareAlike de banco derivado → isolar); geografia detalhada.
- **geoBoundaries** (William & Mary) — **CC BY 4.0**; fronteiras administrativas abertas (**substituto do GADM**).
- **GeoNames** — CC BY; gazetteer global de topônimos.
- **GADM** — **CC BY-NC** → **restrito** (substituir por geoBoundaries/Natural Earth/OSM).
- **USGS GNIS** (PD), **Copernicus DEM / NASA SRTM** (elevação).

### Camada 9 — Brasil
A camada nacional de que dependem a conformidade (BNCC/LDB/LGPD) e a simultaneidade ("Inconfidência Mineira em 1789").
- **IBGE** — **aberto** (Decreto 8.777/2016 + LAI); estatísticas públicas e cartografia (malhas, biomas) com atribuição; microdados não desidentificados são **restritos** (Sala de Acesso a Dados Restritos).
- **INEP/MEC** — dados educacionais abertos (já usados na Etapa 0).
- **IPEA / IPEADATA**, **dados.gov.br** — abertos.
- **MapBiomas** — **CC BY-SA** (ShareAlike → cautela); uso e cobertura do solo.
- **IPHAN**, **Biblioteca Nacional Digital / Hemeroteca Digital** — por item; muito PD, parte restrita.
- **SciELO** — artigos frequentemente CC BY.

### Camada 10 — Fontes curriculares e jurídicas
A camada de **conformidade** (não é "conhecimento", é o filtro). Auditada porque define regras de indexação.
- **BNCC** (MEC), **LDB** (Lei 9.394/96), **LGPD** (Lei 13.709/18), **legislação no Planalto** — **textos legais/normativos não são protegidos por direito autoral** no Brasil (Lei 9.610/98, art. 8) → uso livre.
- **e-MAG / WCAG (W3C)** — padrões de acessibilidade (licença de documento do W3C, reuso com condições).

### Camada 11 — Mídia, imagens, mapas, vídeos e acervos
Ativos visuais para os dossiês (imagens de época, mapas históricos, imageria científica). **Heterogeneidade máxima de licença** → portão por asset.
- **Wikimedia Commons** — por arquivo (PD/CC0/CC BY/CC BY-SA) → filtrar.
- **The Met Open Access** e **Smithsonian Open Access** — **CC0** para obras PD.
- **Library of Congress, Internet Archive, NYPL, Biodiversity Heritage Library** — por item; muito PD.
- **Europeana / DPLA** — *rights statements* por item (mix PD/CC/em copyright) → filtrar.
- **David Rumsey Map Collection** — **CC BY-NC-SA** → **restrito**; para originais PD, buscar provedor PD-explícito.
- **Old Maps Online** — agregador/índice (aponta para os direitos das instituições hospedeiras).

### Camada 12 — Índices / pontes (não-autoridade)
A "ponte de identificadores" da D11 — **encontram e reconciliam, nunca afirmam**.
- **Wikidata** (CC0) — reconciliação de identificadores, ligação entre fontes, localização.
- **Wikipedia** (CC BY-SA) / **DBpedia** (CC BY-SA) — orientação/localização.
- **VIAF** — reconciliação de identidade de pessoas/entidades.
- **IA generativa** (Claude etc.) — conforme A3/Q5: linguagem/orientação apenas; **nunca** fonte factual; nada entra no Knowledge Core sem curadoria humana.

---

## 2. Tabela de classificação (11 dimensões)

**Legenda dos códigos**

- **Confiab.:** **A** autoridade primária · **B** agregador confiável · **C** índice/ponte (não-autoridade).
- **Licença:** **PD** domínio público · **CC0** · **CC BY** · **CC BY-SA** (⚠ ShareAlike) · **ODbL** (⚠ ShareAlike de banco) · **CC BY-NC / NC-SA** (⛔ não-comercial) · **Propr.** proprietária/comercial (⛔) · **Fato** (conteúdo factual não protegível, re-codificável) · **Item** (heterogênea, verificar por asset).
- **Automação** (ingestão programática) e **Curadoria** (esforço humano necessário): **Alta / Média / Baixa**.
- **Risco edu.** (controvérsia, sensibilidade ou risco de ler inferência como fato): **Baixo / Médio / Alto**.
- **Prioridade KC:** **P0** espinha dorsal v1 · **P1** expansão prioritária · **P2** aprofundamento sob demanda · **R** restrita (só fato/curadoria) · **I** índice apenas · **X** descartada para ingestão.

### Tabela A — Camadas científicas de tempo profundo (1–5)

| Fonte | Área | Confiab. | Licença | Tipo de dado | Formato/API | Cob. temporal | Cob. geo | Automação | Curadoria | Risco edu. | Prior. KC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NASA (Open Data/JPL/Image Lib.) | Universo | A | PD | tabular/imagem/efemérides | API REST, dumps | 13,8 Ga–hoje | Global | Alta | Baixa | Baixo | **P0** |
| NASA Exoplanet Archive | Universo | A | PD/livre | tabular | API, TAP | atual | Global | Alta | Baixa | Baixo | P1 |
| ESA (Hubble/Gaia/ESASky) | Universo | A | CC BY-SA IGO ⚠ | tabular/imagem | API, dumps | 13,8 Ga–hoje | Global | Alta | Média | Baixo | P1 |
| CDS (SIMBAD/VizieR) | Universo | B | reuso c/ citação | linked/tabular | API, VO | atual | Global | Alta | Baixa | Baixo | P2 |
| IAU (nomenclatura) | Universo | A | Fato | nomenclatura | listas/PDF | atemporal | Global | Média | Média | Baixo | P1 |
| **ICS Chronostratigraphic Chart** | Geologia/tempo | A | gráfico NC-SA ⛔ / **Fato** livre | escala/nomenclatura | PDF, OWL | tempo profundo | Global | Média | Média | Baixo | **P0** (via fato) |
| **Macrostrat** | Geologia/tempo | B | CC BY | escala/coluna geol. | **API REST** | tempo profundo | Global (+NA) | Alta | Baixa | Baixo | **P0** |
| USGS | Geologia | A | PD | tabular/vetorial/raster | API, dumps | tempo profundo–hoje | Global (foco EUA) | Alta | Baixa | Baixo | P1 |
| NOAA / NCEI (+Paleo) | Atmosfera/clima | A | PD | tabular/raster | API, dumps | tempo profundo–hoje | Global | Alta | Média | Médio | P1 |
| NASA GISS (GISTEMP) | Clima | A | PD | tabular | dumps | moderno | Global | Alta | Baixa | Médio | P2 |
| Copernicus / ERA5 | Clima | A | Copernicus (c/ atrib.) | raster/tabular | API | moderno | Global | Alta | Média | Médio | P2 |
| Berkeley Earth | Clima | B | CC BY | tabular | dumps | moderno | Global | Alta | Baixa | Médio | P2 |
| IPCC (relatórios) | Clima | A/B | texto livre / figuras Item | texto/figura | PDF | moderno–futuro | Global | Baixa | Alta | **Alto** | P2 |
| **GPlates + EarthByte** | Tectônica/paleogeo | A | software GPL / dados **CC BY 3.0** | modelo/vetorial | pyGPlates, Web Service | tempo profundo | Global | Alta | Média | Médio (modelo) | **P0** |
| PALEOMAP / Scotese | Paleogeografia | A/B | a confirmar | raster/mapa | imagens | tempo profundo | Global | Média | Média | Médio | R/P2 |
| Deep Time Maps | Paleogeografia | B | **Propr.** ⛔ | mapa | imagens | tempo profundo | Global | Baixa | Alta | Médio | **R** |
| **Paleobiology Database** | Paleobiologia | A | CC BY 4.0 | ocorrências/tabular | **API REST** | Fanerozoico | Global | Alta | Média | Baixo | **P0** |
| GBIF | Paleobiologia/biodiv. | B | **por dataset** (CC0/BY/NC) | ocorrências | API | tempo profundo–hoje | Global | Alta | Alta (filtrar) | Baixo | P1 (filtrado) |
| Open Tree of Life | Evolução | B | CC0 | árvore/grafo | API, dumps | tempo profundo | Global | Alta | Média | Baixo | P2 |
| Fossilworks | Paleobiologia | B | CC BY (via PBDB) | tabular | dump | Fanerozoico | Global | Baixa (dormante) | Média | Baixo | P2 |

### Tabela B — História humana e eventos contemporâneos (6–7)

| Fonte | Área | Confiab. | Licença | Tipo de dado | Formato/API | Cob. temporal | Cob. geo | Automação | Curadoria | Risco edu. | Prior. KC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Pleiades** | História antiga | A | CC BY | gazetteer/linked | dumps, API | Antiguidade | Global (mediterr.) | Alta | Média | Médio | **P0** |
| **World Historical Gazetteer** | História | B | estrutura CC BY / datasets **variável** | gazetteer/linked | API, dumps | toda a história | Global | Alta | Alta (filtrar) | Médio | **P0** (filtrado) |
| PeriodO | História (períodos) | B | aberto (confirmar CC0) | gazetteer temporal | dumps, API | toda a história | Global | Alta | Média | Médio | P1 |
| Pelagios / Peripleo / Nomisma | História antiga | B | CC BY | linked data | API, dumps | Antiguidade | Global | Alta | Média | Baixo | P2 |
| ToposText | História antiga | B | Item | texto/lugares | dumps | Antiguidade | Mediterr. | Média | Média | Baixo | P2 |
| **Seshat Global History Databank** | História/civilizações | A | **CC BY-NC-SA** ⛔ | tabular/codificado | dumps | Neolítico–moderno | Global | Média | Alta | **Alto** | **R** |
| Our World in Data | Contemporâneo | B | **CC BY** (próprio) / terceiros Item | tabular | API, dumps | moderno–hoje | Global | Alta | Média | Médio | P1 |
| World Bank Open Data | Contemporâneo | A/B | **CC BY 4.0** | tabular | **API** | moderno–hoje | Global | Alta | Baixa | Baixo | P1 |
| UN / UNESCO / WHO (GHO) | Contemporâneo | A | por dataset (c/ atrib.) | tabular | API, dumps | moderno–hoje | Global | Alta | Média | Médio | P2 |
| GDELT | Eventos correntes | B | metadado livre / texto de terceiros | eventos/metadado | API, BigQuery | 1979–hoje | Global | Alta | Alta | **Alto** | P2 |
| **ACLED** | Conflitos correntes | A | **licença comercial** ⛔ + anti-substituto | eventos/tabular | API (registro) | 1997–hoje | Global | Alta | Alta | **Alto** | **R/X** |

### Tabela C — Geografia base (8) e Brasil (9)

| Fonte | Área | Confiab. | Licença | Tipo de dado | Formato/API | Cob. temporal | Cob. geo | Automação | Curadoria | Risco edu. | Prior. KC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Natural Earth** | Geografia base | A/B | **PD** | vetorial | shapefile/GeoJSON | atemporal (base) | Global | Alta | Baixa | Baixo | **P0** |
| OpenStreetMap | Geografia detalhada | B | **ODbL** ⚠ | vetorial | API, dumps | atual | Global | Alta | Média | Baixo | P1 (isolar) |
| **geoBoundaries** | Fronteiras admin. | A/B | **CC BY 4.0** | vetorial | dumps, API | moderno | Global | Alta | Baixa | Médio | **P0** |
| GeoNames | Topônimos | B | CC BY | gazetteer | API, dumps | atual | Global | Alta | Média | Baixo | P1 |
| GADM | Fronteiras admin. | A/B | **CC BY-NC** ⛔ | vetorial | dumps | moderno | Global | Alta | — | Médio | **R** (usar geoBoundaries) |
| USGS GNIS | Topônimos (EUA) | A | PD | gazetteer | dumps | atual | EUA | Alta | Baixa | Baixo | P2 |
| Copernicus DEM / SRTM | Elevação | A | Copernicus/PD | raster | tiles | atual | Global | Alta | Baixa | Baixo | P2 |
| **IBGE** | Brasil | A | **aberto** (Dec. 8.777) / microdados restritos | tabular/vetorial | API, dumps | moderno–hoje | Brasil | Alta | Média | Médio | **P0** |
| INEP/MEC | Brasil (educação) | A | aberto (c/ atrib.) | tabular | dumps | moderno–hoje | Brasil | Alta | Baixa | Baixo | P1 |
| IPEA / IPEADATA | Brasil | A/B | aberto | tabular | API, dumps | moderno–hoje | Brasil | Alta | Baixa | Médio | P2 |
| MapBiomas | Brasil (cobertura) | A/B | **CC BY-SA** ⚠ | raster/vetorial | dumps, GEE | 1985–hoje | Brasil | Média | Média | Médio | P2 (isolar) |
| IPHAN | Brasil (patrimônio) | A | Item | texto/imagem | portal | toda a história | Brasil | Baixa | Alta | Médio | P2 |
| Biblioteca Nacional / Hemeroteca | Brasil (acervo) | A | Item (muito PD) | texto/imagem | IIIF/portal | histórico | Brasil | Média | Alta | Médio | P2 |

### Tabela D — Curricular/jurídica (10), Mídia/acervos (11), Índices (12)

| Fonte | Área | Confiab. | Licença | Tipo de dado | Formato/API | Cob. temporal | Cob. geo | Automação | Curadoria | Risco edu. | Prior. KC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **BNCC** (MEC) | Curricular | A | **Fato/legal livre** | texto normativo | PDF | atual | Brasil | Média | Alta | Baixo | **P0** (conformidade) |
| LDB / LGPD / Planalto | Jurídica | A | **legal não-protegido** | texto legal | PDF/HTML | atual | Brasil | Média | Alta | Baixo | **P0** (conformidade) |
| WCAG (W3C) / e-MAG | Acessibilidade | A | licença W3C (c/ cond.) | padrão | HTML | atual | Global/Brasil | Média | Média | Baixo | P1 |
| Wikimedia Commons | Mídia/imagens | B | **por arquivo** (PD/CC0/BY/SA) | imagem/mídia | API, dumps | toda | Global | Alta | Alta (filtrar) | Médio | P1 (filtrado) |
| Met Open Access / Smithsonian | Acervo/imagens | A | **CC0** | imagem | API, dumps | histórico | Global | Alta | Média | Baixo | P2 |
| Library of Congress / Internet Archive | Acervo | A | Item (muito PD) | texto/imagem/mídia | API, IIIF | histórico | Global | Média | Alta | Médio | P2 |
| Europeana / DPLA | Acervo (agregador) | B | **por item** (rights statements) | metadado/imagem | API | histórico | Global/EUA | Alta | Alta (filtrar) | Médio | P2 (filtrado) |
| David Rumsey Map Collection | Mapas históricos | A | **CC BY-NC-SA** ⛔ | imagem/mapa | IIIF | histórico | Global | Média | Alta | Médio | **R** (PD via outro provedor) |
| Old Maps Online | Mapas (índice) | C | aponta a terceiros | índice/metadado | API | histórico | Global | Alta | Média | Baixo | I |
| **Wikidata** | Índice/ponte | C | **CC0** | linked data | **SPARQL**, dumps | toda | Global | Alta | Média | Médio | **I** |
| Wikipedia / DBpedia | Índice/ponte | C | CC BY-SA | texto/linked | API, dumps | toda | Global | Alta | Alta | **Alto** | **I** |
| VIAF | Índice (pessoas) | C | aberto | autoridade/linked | dumps | toda | Global | Alta | Baixa | Baixo | I |
| IA generativa (Claude etc.) | Auxiliar | C | n/a | linguagem | — | — | — | n/a | Alta | **Alto** | **I** (nunca fonte) |

---

## 3. Fontes prioritárias para a espinha dorsal inicial (P0)

Critério: o conjunto **mínimo, autoritativo e majoritariamente automatizável** capaz de sustentar a hipótese de espinha dorsal da D5 (150–300 nós / 1.500–3.000 eventos) **e** a capacidade central de simultaneidade da D4/A6 (cada evento com tempo + espaço + confiança). Organizadas pelo papel que cumprem.

**Régua do tempo (eixo temporal, do Big Bang ao presente)**
1. **Macrostrat** (CC BY, API) — entrega a escala de tempo internacional legível por máquina. Veículo aberto preferencial.
2. **ICS Chronostratigraphic Chart** — autoridade dos nomes/idades; ingerida **como fatos re-codificados**, com atribuição (não o gráfico NC).
3. **NASA** (PD) — âncoras cósmicas (formação do universo, Sistema Solar, Terra).

**Morfologia do espaço no tempo (o globo em qualquer idade)**
4. **Natural Earth** (PD) — base vetorial do mundo atual.
5. **geoBoundaries** (CC BY) — fronteiras administrativas abertas (no lugar do GADM).
6. **GPlates + EarthByte** (GPL + CC BY 3.0) — paleogeografia rotacionável por idade, **sempre rotulada como reconstrução**.

**Eventos científicos de tempo profundo**
7. **Paleobiology Database** (CC BY, API) — surgimento/extinção de táxons, extinções em massa.
8. **NOAA/NCEI Paleo** (PD) — estados climáticos profundos (p. ex., contexto do Grande Evento de Oxidação), como inferência rotulada.

**Eventos e lugares da história humana (a base da simultaneidade humana)**
9. **Pleiades** (CC BY) — lugares do mundo antigo.
10. **World Historical Gazetteer** (CC BY na estrutura; datasets filtrados) — lugares através do tempo e da língua; é também o conector natural entre eventos e espaço na era humana.

**Ponta contemporânea**
11. **Our World in Data** (CC BY) e **World Bank** (CC BY) — indicadores e fatos modernos para fechar a linha do tempo no presente.

**Camada Brasil (exigida pela conformidade e pela cena canônica)**
12. **IBGE** (aberto) — cartografia e estatística nacional; base da camada brasileira da simultaneidade ("Inconfidência Mineira em 1789").

**Conformidade (filtro, não conteúdo — mas P0 porque governa a saída)**
13. **BNCC / LDB / LGPD** (textos legais/normativos, uso livre).

**Índice transversal (não conta como nó, mas habilita a costura)**
- **Wikidata** (CC0, SPARQL) — **apenas** para reconciliar identificadores entre as fontes acima (o mesmo "Paris", o mesmo "Lavoisier"), nunca como origem de *claim*.

Observação sobre a hipótese da D5: esta lista P0 é compatível com 150–300 nós e 1.500–3.000 eventos **sem esgotar nenhuma fonte** — cada uma é profunda o bastante para muito mais. A validação numérica fina (A5) ocorre ao confrontar a seleção P0 com a granularidade real desejada na Etapa 2; **não** congelo o número aqui.

---

## 4. Fontes descartadas ou de uso restrito

Duas categorias distintas: **restritas por licença** (existem e são boas, mas o uso comercial exige cuidado/substituição) e **descartadas como autoridade** (permanecem úteis apenas como índice, pela regra da baseline).

### 4.1 Restritas por licença (⛔ comercial)

| Fonte | Restrição | Encaminhamento |
|---|---|---|
| **Seshat** | CC BY-**NC**-SA: proíbe uso comercial | Não ingerir a expressão. Onde um fato (datas, atributos de polities) for re-derivável de fontes A primárias, obtê-lo dessas fontes via curadoria. Tratar Seshat como *referência de leitura*, não como insumo. |
| **ACLED** | Exige **licença comercial** paga; EULA proíbe criar dataset/produto **substituto ou concorrente** | Excluir da ingestão sem licença. Para conflitos contemporâneos, usar fontes abertas (GDELT como sinal, fontes oficiais/ONU) ou negociar licença se virar requisito. |
| **GADM** | CC BY-**NC**: sem uso comercial sem permissão | **Substituir por geoBoundaries (CC BY)** + Natural Earth + OSM. |
| **Gráfico do ICS** | CC BY-**NC**-SA (a imagem) | Não redistribuir o gráfico. Re-codificar os **fatos** (nomes + idades) e renderizar visualização própria; atribuir Cohen et al./ICS. |
| **David Rumsey** | CC BY-**NC**-SA (os *scans*) | Para mapas originais em **domínio público**, obter de provedor PD-explícito (Library of Congress, Wikimedia Commons, Internet Archive, Old Maps Online → host). |
| **Deep Time Maps** | Proprietário/licenciado | Substituir por reconstruções EarthByte/GPlates renderizadas internamente. |
| **PALEOMAP / Scotese** | Termos a confirmar (possível restrição) | Tratar como restrito até confirmação; preferir EarthByte como rota aberta. |

### 4.2 Restrições "brandas" (utilizáveis, com disciplina)

- **OpenStreetMap (ODbL)** e **MapBiomas / ESA-Gaia / Wikipedia (CC BY-SA, IGO)** — **ShareAlike/copyleft**. Utilizáveis, mas o banco/derivado que incorpora esses dados herda obrigação de ShareAlike. **Mitigação:** mantê-los em **camadas isoladas**, sem deixar a obrigação contaminar o esquema proprietário do Knowledge Core (ver Risco L2).
- **GBIF, Wikimedia Commons, Europeana, DPLA, WHG (datasets)** — **licença heterogênea por item/dataset**. Utilizáveis com **filtro de licença na entrada** que rejeita o que for NC/desconhecido.

### 4.3 Descartadas como autoridade (mantidas só como índice — regra da baseline)

- **Wikidata, Wikipedia, DBpedia, VIAF** e **IA generativa**: **nunca** origem de *claim*. Papel exclusivo: localizar dados e reconciliar identificadores (Wikidata/VIAF), orientar a busca humana (Wikipedia), adaptar linguagem (IA, conforme A3/Q5). Esta não é uma rejeição de qualidade — é a salvaguarda R9 da baseline contra o atalho "Wikipedia + IA como autoridade".

---

## 5. Riscos de licença e confiabilidade

### 5.1 Riscos de licença

- **L1 — Contaminação por não-comercial (NC).** Seshat, GADM, gráfico do ICS, scans do David Rumsey, ACLED, Deep Time Maps. Risco: ingerir expressão NC e contaminar um produto comercial. **Mitigação:** princípio fato × expressão (Seção 0.1); substitutos abertos (geoBoundaries, EarthByte, provedores PD); **rastreio de licença por asset (D11)** como portão obrigatório de entrada.
- **L2 — Propagação de ShareAlike/copyleft.** ODbL (OSM) e CC BY-SA (MapBiomas, ESA/Gaia, Wikipedia). Risco: a obrigação de "compartilhar igual" se espalhar para o esquema do Knowledge Core. **Mitigação:** isolar dados SA em camadas/bancos separados; não fundir SA no núcleo proprietário; decidir cedo (Etapa 2) a fronteira entre "camada SA" e "núcleo".
- **L3 — Heterogeneidade por item/dataset.** GBIF, Commons, Europeana, DPLA, WHG. Risco: assumir que "a fonte é CC BY" quando o item específico é NC. **Mitigação:** licença como **metadado obrigatório por asset**; ingestão recusa item sem licença declarada ou desconhecida.
- **L4 — Profundidade da cadeia de atribuição.** Os modelos de rotação EarthByte sintetizam dezenas de estudos (cada linha cita sua origem); a OWID republica terceiros. Risco: atribuição incompleta. **Mitigação:** armazenar a **cadeia de proveniência completa**, não só o último elo.
- **L5 — Ambiguidade de obras do poder público (BR).** A Lei 9.610/98 omite disposição sobre obras da administração pública (revogados os arts. específicos), embora textos legais/normativos sejam expressamente não-protegidos (art. 8) e o Decreto 8.777/2016 estabeleça abertura com atribuição. **Mitigação:** tratar legislação/BNCC como livre; para *publicações* de órgãos, confirmar licença caso a caso.

### 5.2 Riscos de confiabilidade

- **C1 — Índice confundido com autoridade.** Risco de uma *claim* nascer no Wikidata/Wikipedia. **Mitigação:** invariante de arquitetura (Etapa 2) — toda *claim* rastreia a uma fonte A/B; índices só resolvem identidade/localização.
- **C2 — Inferência lida como fato (tempo profundo).** Paleogeografia, paleoclima e datas profundas são **modelos**, não observações. Risco direto ao diferencial de honestidade epistêmica. **Mitigação:** **tipagem de claim** (fato documentado / inferência científica / reconstrução modelada) com nota de incerteza — exatamente a cena canônica do Grande Evento de Oxidação.
- **C3 — Tópicos contemporâneos e contestados.** Colonização, escravidão, povos indígenas, evolução, Big Bang (R3 da baseline). **Mitigação:** apresentar interpretações historiográficas distintas quando existirem, fontes visíveis, e **política editorial escrita antes da Etapa 4**.
- **C4 — Longevidade e manutenção da fonte.** Projetos acadêmicos adormecem (Fossilworks; precedente ChronoZoom em R7). **Mitigação:** preferir fontes com lastro institucional; **versionar/"congelar" o snapshot ingerido**; desacoplar do consumo ao vivo.
- **C5 — Defasagem de "eventos correntes".** A ponta contemporânea envelhece. **Mitigação:** definir **cadência de atualização por fonte** (não nesta etapa — é insumo para a Etapa 2/operacional).
- **C6 — Sensibilidade pedagógica de fontes de conflito.** GDELT/ACLED carregam violência e ruído. **Mitigação:** se entrarem, curadoria humana e adequação por faixa etária antes de exposição ao aluno.

### 5.3 Confiança das verificações desta auditoria (honestidade epistêmica)

Licenças **verificadas diretamente** nesta etapa (alta confiança): Our World in Data (CC BY próprio; terceiros variam), World Bank (CC BY 4.0), **Seshat (CC BY-NC-SA)**, Paleobiology Database (CC BY 4.0), EarthByte/GPlates (CC BY 3.0 / GPL), **GADM (NC)**, **ACLED (licença comercial + anti-substituto)**, Pleiades (CC BY), WHG (estrutura CC BY; datasets variam), **gráfico do ICS (CC BY-NC-SA; fatos livres)**, **David Rumsey (CC BY-NC-SA)**, arcabouço de dados abertos do Brasil (Decreto 8.777 + IBGE).

Licenças assumidas de **conhecimento estabelecido**, a **confirmar por asset** antes da ingestão de produção: NASA Exoplanet Archive (termos exatos), ESA/Gaia (CC BY-SA IGO), Macrostrat (CC BY), GeoNames (CC BY), geoBoundaries (CC BY 4.0), PeriodO (CC0?), MapBiomas (CC BY-SA), Copernicus/ERA5, Berkeley Earth (CC BY), Open Tree of Life (CC0), Met/Smithsonian (CC0), e os *rights statements* item a item de Commons/Europeana/DPLA/LoC/Internet Archive. **Recomendação:** transformar esta lista em uma checklist de confirmação de licença para a curadoria, antes de qualquer ingestão.

---

## 6. Estratégia de uso das fontes na próxima etapa

Handoff para a **Etapa 2 (modelagem do Knowledge Core)**. Aqui só se define **como as fontes serão usadas** — proveniência, licença e curadoria. **Não** se modela esquema, **não** se desenha pipeline, **não** se escreve código; isso é da Etapa 2 em diante.

1. **Portão de ingestão por asset (D11 operacionalizada).** Nenhum dado entra sem dois metadados obrigatórios: **licença** (com flags NC/SA/Item) e **tipo de claim** (fato documentado / inferência científica / reconstrução modelada). O portão rejeita item sem licença declarada, NC sem caminho de "fato", ou *claim* sem fonte A/B.

2. **Construir P0 só a partir de autoridades A/B.** A espinha dorsal nasce das fontes da Seção 3. Índices (C) entram apenas como **camada de reconciliação de identificadores** — o mecanismo que costura "o mesmo lugar/pessoa/evento" entre fontes — nunca como origem de fato. Esta é a tradução técnica da regra "Wikidata é ponte, não autoridade".

3. **Padrão fato-não-expressão para fontes NC.** Para ICS, Seshat e mapas PD sob scan NC: ingerir o **fato re-codificado** (ou trocar de provedor para PD-explícito), com atribuição na cadeia de proveniência. A Etapa 2 deve prever o campo de **proveniência multi-elo** (L4).

4. **Padrão de isolamento de ShareAlike.** Definir, na Etapa 2, a fronteira entre **"camada SA"** (OSM/MapBiomas/ESA, com obrigação ShareAlike) e o **núcleo** proprietário, de modo que a obrigação copyleft não atravesse essa fronteira (L2).

5. **Sustentar a simultaneidade (D4/A6) desde o modelo.** A auditoria já mapeia *qual fonte alimenta cada eixo*: tempo (Macrostrat/ICS/NASA), espaço (Natural Earth/geoBoundaries/GPlates), evento científico (PBDB/NOAA-Paleo), evento humano (Pleiades/WHG), presente (OWID/World Bank), Brasil (IBGE). A Etapa 2 garante que **todo evento carregue tempo + lugar + confiança** — pré-condição de "o que acontecia no mundo neste momento?".

6. **Curadoria humana mínima + parcerias (Q3/D11), focada onde dói.** O esforço humano se concentra nos pontos altos da coluna "Curadoria" da tabela: tópicos controversos (C3), negociação/checagem de NC, filtragem de licença heterogênea (L3), e rotulagem de inferência (C2). Museus/universidades/especialistas entram como co-curadores justamente aí. O restante (PBDB, Macrostrat, Natural Earth, IBGE) é ingestão majoritariamente automatizável.

7. **Antifragilidade de fonte (R7/C4).** A Etapa 2 trabalha sobre **snapshots versionados** das fontes, não sobre dependência ao vivo, e prefere fontes com lastro institucional. Cadência de atualização (C5) é decisão operacional posterior.

**Pendências herdadas que esta auditoria torna acionáveis:**
- Checklist de **confirmação de licença por asset** (Seção 5.3) — pré-requisito da ingestão.
- **Política editorial de controvérsias** (R3) — a ser escrita antes da Etapa 4, mas as fontes de alto risco já estão sinalizadas (Risco edu. "Alto").
- **Validação numérica da espinha dorsal** (A5) — a confrontar na Etapa 2; aqui apenas confirmada como *plausível* sem congelamento.
- Decisão sobre **negociar licença comercial do ACLED** caso conflitos contemporâneos virem requisito — hoje, excluído.

---

## Anexo — Fontes consultadas na verificação de licenças (Etapa 1)

Our World in Data (FAQ/Guidelines de reuso); World Bank (Summary Terms of Use / Data Catalog, CC BY 4.0); Seshat Databank (páginas de download e datasets — CC BY-NC-SA); Paleobiology Database (Creative Commons / API paper / IPT — CC BY 4.0); EarthByte/GPlates (páginas de software e datasets — dados CC BY 3.0, software GPL); GADM (gadm.org/license — não-comercial); ACLED (EULA, Content Usage Terms, Attribution Policy, FAQs de acesso — licença comercial obrigatória); Pleiades / World Historical Gazetteer (páginas de uso e datasets — CC BY na estrutura, datasets variáveis); International Commission on Stratigraphy (registros do gráfico — CC BY-NC-SA; artigo Episodes — CC BY-NC); David Rumsey Map Collection (About / Copyright and Permissions — CC BY-NC-SA 3.0); arcabouço brasileiro de dados abertos (Decreto 8.777/2016 no Planalto; IBGE — Dados Abertos, INDA e Sala de Acesso a Dados Restritos; Portal Brasileiro de Dados Abertos).

*Demais licenças foram classificadas a partir de conhecimento estabelecido e estão marcadas para confirmação por asset na Seção 5.3.*

---

*Documento de entrega da Etapa 1, sob a baseline v1.0. Não modela dados, não propõe MVP, não contém código nem arquitetura técnica. Próxima etapa, quando solicitada: Etapa 2 — modelagem do Knowledge Core, consumindo as fontes P0 desta auditoria conforme a estratégia da Seção 6.*
