#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas do Tempo 3D — Passo A4, Fatia 1: migração do protótipo para o esquema
reificado (reconstrução fiel das Fases 1–6 do B1 §6 sobre o esquema do A3).

Insumo único da carga: o protótipo atlas-prototipo-3d.html (35 itens), aqui
extraído fielmente. Regras de reconciliação (D-A3.1/D-A3.2):
  - provenance_status: 'seeded-demo' se seeded:true, senão 'corpus' (não inventa fonte).
  - review_status: pub='publicável'->'approved'; pub='mediado'->'pending'.
  - per_asset_source_confirmed: NOT srcPend  (§9.2 F2).
Eixo canônico (3Z): canonical_start/end/scalar em anos rel. a T0=2000.0 CE.

Não promove seeded a corpus. Não inventa fontes para seeded. [N1] vale na carga.
"""
import json, os, sys, psycopg2

# saída em UTF-8 mesmo em consoles legados (ex.: cp1252 no Windows) — o relatório
# contém '∩'/'⊂'. Não muda o conteúdo, só o encoding do stdout.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DSN = "host=localhost dbname=atlas user=atlas password=%s" % os.environ["ATLAS_DB_PASSWORD"]

# diretório de saída relativo ao próprio script (db/migration -> raiz/out),
# independente do diretório de trabalho e do SO.
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "out")

# --------------------------------------------------------------------------
# 35 itens extraídos do protótipo. Campos canônicos (cs,ce,scalar,stb,disp,prec,unc)
# derivados das strings de data do protótipo segundo o datum 3Z (T0=2000.0 CE).
# (start,end) = intervalo no eixo; a interseção de simultaneidade usa OVERLAP.
# --------------------------------------------------------------------------
GA, MA = 1e9, 1e6
ITENS = [
 # ===== Cena 1789 (gregorianCE; 1789 -> -211) =====
 # história (corpus)
 dict(id="evt:estados-gerais-1789",t="Event",dom="historia",lay="Política",ti="Abertura dos Estados Gerais",
   ct="fato-documentado",cf="alta",ev="documental",src="Historiografia e arquivos (A/B)",tier="A",
   pub="publicável",srcPend=True,lat=48.80,lng=2.12,place="Versalhes",
   cs=-210.68,ce=-210.64,sc=-210.66,stb="gregorianCE",disp="5 de maio de 1789",prec="dia",unc="data exata",
   cset="rev-francesa"),
 dict(id="evt:queda-bastilha-1789",t="Event",dom="historia",lay="Política",ti="Queda da Bastilha",
   ct="fato-documentado",cf="alta",ev="documental",src="Historiografia e arquivos (A/B)",tier="A",
   pub="publicável",srcPend=True,lat=48.86,lng=2.35,place="Paris",
   cs=-210.49,ce=-210.45,sc=-210.47,stb="gregorianCE",disp="14 de julho de 1789",prec="dia",unc="data exata"),
 dict(id="evt:posse-washington-1789",t="Event",dom="historia",lay="Política",ti="Posse de Washington",
   ct="fato-documentado",cf="alta",ev="documental",src="Arquivos e historiografia dos EUA (A/B)",tier="A",
   pub="publicável",srcPend=False,lat=40.71,lng=-74.01,place="Nova York",
   cs=-210.69,ce=-210.65,sc=-210.67,stb="gregorianCE",disp="30 de abril de 1789",prec="dia",unc="data exata",
   anach="A capital em 1789 era Nova York; Washington, D.C. ainda não era a capital."),
 dict(id="concept:iluminismo",t="Concept",dom="historia",lay="Cultura",ti="Iluminismo",
   ct="interpretação",cf="média",ev="documental",src="Historiografia (A/B)",tier="B",
   pub="publicável",srcPend=False,lat=50.0,lng=8.0,place="Europa (difuso)",
   cs=-400.0,ce=-200.0,sc=-300.0,stb="gregorianCE",disp="séc. XVII–XVIII",prec="século",unc="período longo"),
 dict(id="evt:declaracao-direitos-1789",t="Event",dom="historia",lay="Política",ti="Declaração dos Direitos do Homem",
   ct="fato-documentado",cf="alta",ev="documental",src="Texto histórico; historiografia (A/B)",tier="A",
   pub="mediado",srcPend=False,lat=48.864,lng=2.349,place="Paris",
   cs=-210.37,ce=-210.33,sc=-210.35,stb="gregorianCE",disp="26 de agosto de 1789",prec="dia",unc="data exata",
   cset="direitos-limites"),
 dict(id="evt:inconfidencia-mineira",t="Event",dom="historia",lay="Brasil",ti="Inconfidência Mineira",
   ct="interpretação",cf="média",ev="documental",src="Arquivo Nacional, BN, IBGE (A/B)",tier="B",
   pub="mediado",srcPend=False,lat=-20.38,lng=-43.50,place="Capitania de Minas Gerais",
   cs=-211.0,ce=-210.0,sc=-210.5,stb="gregorianCE",disp="1789",prec="ano",unc="ano",
   cset="inconfidencia"),
 dict(id="proc:trafico-atlantico",t="Process",dom="historia",lay="África",ti="Tráfico atlântico",
   ct="fato-documentado",cf="alta",ev="documental",src="Bases do tráfico e historiografia (A/B)",tier="A",
   pub="mediado",srcPend=False,lat=8.0,lng=-25.0,place="mundo atlântico",
   cs=-260.0,ce=-150.0,sc=-211.0,stb="gregorianCE",disp="ativo em 1789",prec="período",unc="processo de longa duração",
   cset="escravidao-central"),
 dict(id="state:china-qing-1789",t="State",dom="historia",lay="Civilizações",ti="China Qing em 1789",
   ct="interpretação",cf="alta",ev="documental",src="Historiografia (A/B)",tier="A",
   pub="mediado",srcPend=False,lat=39.90,lng=116.40,place="China Qing",
   cs=-211.0,ce=-210.0,sc=-210.5,stb="gregorianCE",disp="1789",prec="ano",unc="ano"),
 dict(id="entity:povos-indigenas-brasil",t="Entity",dom="historia",lay="Povos indígenas",ti="Povos indígenas nas Américas",
   ct="interpretação",cf="alta",ev="documental + tradição/registro oral",src="Etno-historiografia, IPHAN, fontes indígenas (A/B)",tier="A",
   pub="mediado",srcPend=False,lat=-10.0,lng=-52.0,place="Américas",
   cs=-211.0,ce=-210.0,sc=-210.5,stb="gregorianCE",disp="1789",prec="ano",unc="ano",
   anach="Não apagar territórios indígenas sob fronteiras coloniais."),
 # química/física/geologia/vida — SEMEADOS para demonstração (multidomínio em 1789)
 dict(id="chem:lavoisier-traite-1789",t="Event",dom="quimica",lay="Ciência",ti="Tratado de química de Lavoisier",
   ct="fato-documentado",cf="alta",ev="documental",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,lat=48.85,lng=2.34,place="Paris",
   cs=-211.0,ce=-210.0,sc=-210.5,stb="gregorianCE",disp="1789",prec="ano",unc="ano"),
 dict(id="chem:atmosfera-1789",t="State",dom="quimica",lay="Química",ti="Composição da atmosfera",
   ct="fato-documentado",cf="alta",ev="medição / consenso",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,glob=True,place="planetário (toda a Terra)",
   cs=-260.0,ce=-150.0,sc=-211.0,stb="gregorianCE",disp="1789",prec="período",unc="estado estável em escala de séculos"),
 dict(id="chem:co2-1789",t="State",dom="quimica",lay="Química",ti="CO₂ atmosférico pré-industrial",
   ct="estimativa",cf="alta",ev="inferência indireta (testemunhos de gelo)",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=True,seeded=True,glob=True,place="planetário",
   cs=-260.0,ce=-150.0,sc=-211.0,stb="gregorianCE",disp="1789",prec="período",unc="proxy de gelo (não medido em 1789)"),
 dict(id="phys:terra-orbita-1789",t="State",dom="fisica",lay="Física",ti="A Terra em sua órbita",
   ct="interpretação",cf="alta",ev="mecânica orbital",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,glob=True,place="planetário / Sistema Solar",
   cs=-260.0,ce=-150.0,sc=-211.0,stb="gregorianCE",disp="1789",prec="período",unc="estado estável em milênios"),
 dict(id="geo:andes-1789",t="State",dom="geologia",lay="Geologia",ti="Cordilheira dos Andes",
   ct="estimativa",cf="média",ev="registro geológico",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,lat=-20.0,lng=-67.0,place="América do Sul",
   cs=-2.5e7,ce=0.0,sc=-210.5,stb="gregorianCE",disp="1789 (soerguida ao longo de dezenas de Ma)",prec="período",unc="orogênese de dezenas de Ma"),
 dict(id="geo:alpes-1789",t="State",dom="geologia",lay="Geologia",ti="Os Alpes",
   ct="estimativa",cf="média",ev="registro geológico",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,lat=46.5,lng=8.5,place="Europa",
   cs=-3.5e7,ce=0.0,sc=-210.5,stb="gregorianCE",disp="1789",prec="período",unc="orogênese alpina"),
 dict(id="life:grande-auk-1789",t="Species",dom="biologia",lay="Vida",ti="Arau-gigante (grande auk)",
   ct="estimativa",cf="média",ev="registro zoológico/histórico",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,lat=58.0,lng=-20.0,place="Atlântico Norte",
   cs=-1.0e4,ce=-156.0,sc=-210.5,stb="gregorianCE",disp="1789 (extinto em 1844)",prec="período",unc="vivo até 1844"),
 dict(id="life:biosfera-1789",t="State",dom="biologia",lay="Vida",ti="A biosfera de 1789",
   ct="interpretação",cf="média",ev="ecologia histórica",src="(demonstração — fonte não validada)",tier=None,
   pub="publicável",srcPend=False,seeded=True,glob=True,place="planetário",
   cs=-260.0,ce=-150.0,sc=-211.0,stb="gregorianCE",disp="1789",prec="período",unc="composição reconstruída"),

 # ===== Cena GOE (~2,4 Ga; sourceTimeBasis=Ga) — corpus =====
 dict(id="proc:goe",t="Process",dom="geologia",lay="Atmosfera",ti="Grande Evento de Oxidação",
   ct="inferência-científica",cf="alta",ev="proxies geoquímicos",src="NOAA Paleo, USGS, geociências (A/B)",tier="A",
   pub="publicável",srcPend=True,glob=True,place="planetário",
   cs=-2.5*GA,ce=-2.0*GA,sc=-2.4*GA,stb="Ga",disp="~2,4 Ga",prec="Ga",unc="faixa ~2,5–2,0 Ga",
   cset="goe-ritmo"),
 dict(id="proc:fotossintese-oxigenica",t="Process",dom="biologia",lay="Vida",ti="Fotossíntese oxigênica",
   ct="inferência-científica",cf="alta",ev="biomarcadores, estromatólitos",src="PBDB, geociências (A/B)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="planetário",
   cs=-2.7*GA,ce=-2.4*GA,sc=-2.5*GA,stb="Ga",disp="~2,4 Ga (e antes)",prec="Ga",unc="faixa ampla"),
 dict(id="entity:cianobacterias",t="Entity",dom="biologia",lay="Vida",ti="Cianobactérias",
   ct="inferência-científica",cf="alta",ev="registro microfóssil/estromatólitos",src="PBDB (A)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="oceanos rasos",
   cs=-2.6*GA,ce=-2.3*GA,sc=-2.45*GA,stb="Ga",disp="~2,4 Ga",prec="Ga",unc="faixa"),
 dict(id="proc:deposicao-bif",t="Process",dom="geologia",lay="Geologia",ti="Formações ferríferas bandadas (BIFs)",
   ct="proxy",cf="alta",ev="estratigrafia (BIFs)",src="USGS, Macrostrat (A/B)",tier="A",
   pub="publicável",srcPend=True,glob=True,place="bacias oceânicas (registro: Hamersley, Transvaal)",
   cs=-2.5*GA,ce=-2.4*GA,sc=-2.45*GA,stb="Ga",disp="~2,5–2,4 Ga",prec="Ga",unc="faixa"),
 dict(id="state:atmosfera-primitiva",t="State",dom="quimica",lay="Atmosfera",ti="Atmosfera anóxica (pré-GOE)",
   ct="inferência-científica",cf="alta",ev="S-MIF, minerais detríticos",src="geociências (A/B)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="planetário",
   cs=-2.7*GA,ce=-2.4*GA,sc=-2.5*GA,stb="Ga",disp="antes de ~2,4 Ga",prec="Ga",unc="faixa"),
 dict(id="state:oceanos-ferruginosos",t="State",dom="quimica",lay="Oceanos",ti="Oceanos ferruginosos",
   ct="reconstrução-modelada",cf="média",ev="especiação de ferro (proxy)",src="geoquímica (A/B)",tier="B",
   pub="mediado",srcPend=True,glob=True,place="planetário (reconstrução)",
   cs=-2.6*GA,ce=-2.3*GA,sc=-2.45*GA,stb="Ga",disp="~2,4 Ga",prec="Ga",unc="reconstrução modelada"),
 dict(id="state:clima-goe",t="State",dom="clima",lay="Clima",ti="Glaciações huronianas",
   ct="hipótese",cf="média",ev="diamictitos",src="geociências (A/B)",tier="B",
   pub="mediado",srcPend=True,glob=True,place="planetário",
   cs=-2.4*GA,ce=-2.2*GA,sc=-2.3*GA,stb="Ga",disp="~2,4–2,2 Ga",prec="Ga",unc="relação causal em debate",
   cset="goe-glaciacoes"),
 dict(id="state:paleogeografia-2-4ga",t="State",dom="geologia",lay="Paleogeografia",ti="Paleogeografia de ~2,4 Ga",
   ct="reconstrução-modelada",cf="baixa",ev="paleomagnetismo (escasso)",src="GPlates/EarthByte (A, CC BY)",tier="A",
   pub="mediado",srcPend=True,glob=True,place="planetário (muito incerto)",
   cs=-2.5*GA,ce=-2.3*GA,sc=-2.4*GA,stb="Ga",disp="~2,4 Ga",prec="Ga",unc="reconstrução de baixa confiança",
   anach="Não projetar continentes modernos nem supercontinentes de outras épocas sobre 2,4 Ga."),

 # ===== Cena K-Pg (~66 Ma; sourceTimeBasis=Ma) — corpus =====
 dict(id="evt:impacto-chicxulub",t="Event",dom="geologia",lay="Astronomia/Geologia",ti="Impacto de Chicxulub",
   ct="inferência-científica",cf="alta",ev="cratera, anomalia de irídio, esférulas, camada-limite",src="USGS, PBDB, geociências (A/B)",tier="A",
   pub="publicável",srcPend=False,lat=21.3,lng=-89.5,place="região de Chicxulub (posição em reconstrução)",caveat=True,
   cs=-66.05*MA,ce=-65.95*MA,sc=-66.0*MA,stb="Ma",disp="~66 Ma",prec="Ma",unc="ponto-evento (faixa estreita)",
   cset="kpg-causa",anach="'México' não existe em 66 Ma; marcador em posição reconstruída/aproximada."),
 dict(id="proc:extincao-kpg",t="Process",dom="biologia",lay="Vida/extinções",ti="Extinção em massa K-Pg",
   ct="inferência-científica",cf="alta",ev="registro fóssil (camada-limite)",src="PBDB (A)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="planetário",
   cs=-66.0*MA,ce=-65.7*MA,sc=-65.9*MA,stb="Ma",disp="~66 Ma",prec="Ma",unc="faixa"),
 dict(id="entity:dinossauros-nao-avianos",t="Entity",dom="biologia",lay="Vida",ti="Dinossauros não-avianos",
   ct="inferência-científica",cf="alta",ev="registro fóssil",src="PBDB (A)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="continentes",
   cs=-70.0*MA,ce=-66.0*MA,sc=-67.0*MA,stb="Ma",disp="até ~66 Ma",prec="Ma",unc="faixa"),
 dict(id="entity:aves",t="Entity",dom="biologia",lay="Vida",ti="Aves — dinossauros que sobreviveram",
   ct="inferência-científica",cf="alta",ev="filogenia, registro fóssil",src="PBDB, geociências (A/B)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="continentes",
   cs=-66.0*MA,ce=-64.0*MA,sc=-65.5*MA,stb="Ma",disp="~66 Ma em diante",prec="Ma",unc="linhagem sobrevivente"),
 dict(id="concept:anomalia-iridio",t="Concept",dom="quimica",lay="Geoquímica",ti="Anomalia de irídio",
   ct="proxy",cf="alta",ev="geoquímica (irídio)",src="USGS, geociências (A/B)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="camada-limite global",
   cs=-66.05*MA,ce=-65.95*MA,sc=-66.0*MA,stb="Ma",disp="~66 Ma",prec="Ma",unc="faixa estreita"),
 dict(id="proc:vulcanismo-deccan-traps",t="Process",dom="geologia",lay="Tectônica/vulcanismo",ti="Vulcanismo do Deccan",
   ct="inferência-científica",cf="média",ev="registro vulcânico/datação",src="USGS, geociências (A/B)",tier="A",
   pub="mediado",srcPend=False,glob=True,place="placa indiana (em outra latitude na época)",
   cs=-66.4*MA,ce=-65.5*MA,sc=-66.0*MA,stb="Ma",disp="~66 Ma (em curso)",prec="Ma",unc="peso causal em debate",
   cset="kpg-causa"),
 dict(id="state:clima-pos-impacto-kpg",t="State",dom="clima",lay="Clima",ti="Inverno de impacto",
   ct="inferência-científica",cf="média",ev="modelagem + proxies",src="geociências (A/B)",tier="B",
   pub="mediado",srcPend=True,glob=True,place="planetário",
   cs=-66.0*MA,ce=-65.8*MA,sc=-65.9*MA,stb="Ma",disp="após ~66 Ma",prec="Ma",unc="intensidade/duração em faixa"),
 dict(id="state:oceanos-pos-impacto-kpg",t="State",dom="quimica",lay="Oceanos",ti="Acidificação oceânica pós-impacto",
   ct="hipótese",cf="média",ev="geoquímica marinha (proxy)",src="geociências (A/B)",tier="B",
   pub="mediado",srcPend=True,glob=True,place="oceanos",
   cs=-66.0*MA,ce=-65.5*MA,sc=-65.8*MA,stb="Ma",disp="após ~66 Ma",prec="Ma",unc="mecanismo/magnitude em revisão",
   cset="kpg-acidificacao-oceanica"),
 dict(id="state:paleogeografia-66ma",t="State",dom="geologia",lay="Paleogeografia",ti="Paleogeografia de ~66 Ma",
   ct="reconstrução-modelada",cf="média",ev="paleomagnetismo, GPlates",src="GPlates/EarthByte (A, CC BY)",tier="A",
   pub="mediado",srcPend=True,glob=True,place="planetário (reconstrução)",
   cs=-67.0*MA,ce=-65.0*MA,sc=-66.0*MA,stb="Ma",disp="~66 Ma",prec="Ma",unc="reconstrução modelada",
   anach="Sem países; placa indiana longe da posição atual; evidência atual ≠ paleoposição."),
 dict(id="proc:recuperacao-ecologica-pos-kpg",t="Process",dom="biologia",lay="Vida",ti="Recuperação e ascensão dos mamíferos",
   ct="inferência-científica",cf="alta",ev="registro fóssil",src="PBDB (A)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="planetário",
   cs=-66.0*MA,ce=-60.0*MA,sc=-63.0*MA,stb="Ma",disp="após ~66 Ma",prec="Ma",unc="tempo de recuperação incerto"),

 # ===== Cena CÓSMICA (tempo profundo; sourceTimeBasis=Ga) — corpus COM fonte (Frente A) =====
 # Tipagem epistêmica ASSINADA (humano, jul/2026): docs/passos/nota-descoberta-cosmicos-frente-a.md §8.
 # Todos GLOBAIS, sem geometria terrestre → displayPoint NULL, geometryRegime 'semLugarTerrestre'.
 # NENHUM 'fato-documentado' (ninguém testemunhou t=0); incerteza SEMPRE presente. Sem ClaimSet
 # (etapa-3.1 §10.7: a expansão é claim único; criacionismo não é claim concorrente).
 dict(id="evt:big-bang",t="Event",dom="cosmos",lay="Cosmos",ti="Big Bang — início da expansão",
   ct="inferência-científica",cf="alta",ev="CMB (Planck), nucleossíntese primordial, expansão (Hubble-Lemaître)",
   src="NASA/ESA — Planck 2018; cosmologia de precisão (PD)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="universo observável (sem ponto)",
   cs=-13.807*GA,ce=-13.767*GA,sc=-13.787*GA,stb="Ga",disp="~13,8 Ga (13,787 ± 0,020)",prec="Ga",
   unc="±0,020 Ga (Planck 2018); a singularidade t=0 é extrapolação do modelo"),
 dict(id="state:cmb-recombinacao",t="State",dom="cosmos",lay="Cosmos",ti="Fundo cósmico de micro-ondas (recombinação)",
   ct="medição-direta",cf="alta",ev="espectro de corpo negro do CMB (COBE/Planck)",
   src="NASA/ESA — Planck 2018; cosmologia de precisão (PD)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="céu inteiro (radiação de fundo)",
   cs=-13.80*GA,ce=-13.77*GA,sc=-13.787*GA,stb="Ga",disp="~13,8 Ga (≈ 380 mil anos após o início)",prec="Ga",
   unc="recombinação ~380 ka após o início; o CMB é observado diretamente"),
 dict(id="proc:formacao-galaxias",t="Process",dom="cosmos",lay="Cosmos",ti="Formação das primeiras estrelas e galáxias",
   ct="inferência-científica",cf="média",ev="levantamentos profundos (JWST/Hubble), função de massa estelar",
   src="NASA/ESA — JWST e levantamentos profundos; astrofísica revisada (PD)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="universo jovem (sem ponto)",
   cs=-13.5*GA,ce=-13.0*GA,sc=-13.2*GA,stb="Ga",disp="~13,5–13 Ga",prec="Ga",
   unc="faixa ~13,5–13 Ga; timing/processo em evolução rápida com o JWST"),
 dict(id="evt:formacao-sistema-solar",t="Event",dom="cosmos",lay="Cosmos",ti="Formação do Sol e do Sistema Solar",
   ct="inferência-científica",cf="alta",ev="datação radiométrica de CAIs em meteoritos",
   src="NASA — datação radiométrica de CAIs; ciência planetária revisada (PD)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="disco protoplanetário (sem ponto terrestre)",
   cs=-4.60*GA,ce=-4.55*GA,sc=-4.567*GA,stb="Ga",disp="~4,57 Ga",prec="Ga",
   unc="4,567 Ga (datação de CAIs — a idade mais antiga do Sistema Solar)"),
 dict(id="proc:formacao-terra",t="Process",dom="geologia",lay="Geologia",ti="Acreção da Terra",
   ct="inferência-científica",cf="alta",ev="datação radiométrica (zircões de Jack Hills, meteoritos)",
   src="USGS — geocronologia (zircões/meteoritos); geociências revisadas (PD)",tier="A",
   pub="publicável",srcPend=False,glob=True,place="proto-Terra (planetário)",
   cs=-4.57*GA,ce=-4.50*GA,sc=-4.54*GA,stb="Ga",disp="~4,54 Ga",prec="Ga",
   unc="~4,54 Ga; acreção ao longo de ~10–100 Ma"),
]

# ClaimSets carregados como worked examples (claim-sobre-claims) — 3 conjuntos, 7 membros.
# rev-francesa adicionado em D-A3.1 (host approved); direitos-limites/inconfidencia/
# escravidao-central NÃO entram: hosts pending → fila de revisão (Trilha C, Playbook §5).
CLAIMSETS = {
 "kpg-causa": dict(host="evt:impacto-chicxulub", tema="Causa dominante da extinção K-Pg",
   resolution="Peso assimétrico exibível; não há simetria visual entre lados de peso desigual; 'houve impacto' não é um lado em disputa.",
   members=[("Impacto de Chicxulub como gatilho dominante",0.82,"central"),
            ("Vulcanismo dos Deccan como agravante/co-fator",0.30,"contribuinte")]),
 "goe-ritmo": dict(host="proc:goe", tema="Ritmo da oxigenação (abrupto × gradual)",
   resolution="Debate sobre o RITMO, não sobre a ocorrência. Que o O₂ subiu não está em disputa.",
   members=[("Transição com pulsos/sobressaltos (whiffs e oscilações)",0.62,"a"),
            ("Subida essencialmente monotônica",0.38,"b")]),
 "rev-francesa": dict(host="evt:estados-gerais-1789", tema="Causas da Revolução Francesa",
   resolution="Causas plurais com pesos próximos — pluralidade não é equivalência forçada nem 'dois lados'.",
   members=[("Crise fiscal e estrutura social do Antigo Regime",0.70,"estrutural"),
            ("Circulação de ideias iluministas",0.55,"ideias"),
            ("Conjuntura econômica imediata (colheitas, preço do pão)",0.50,"conjuntural")]),
}

# Arestas afirmativas (todas com proveniência — [N1] vale na carga; n1_rejected=0).
RELS = [
 ("rel:chicxulub-causou-extincao","evt:impacto-chicxulub","proc:extincao-kpg","causou"),
 ("rel:goe-causou-bif","proc:goe","proc:deposicao-bif","causou"),
 ("rel:fotossintese-causou-goe","proc:fotossintese-oxigenica","proc:goe","causou"),
 ("rel:estados-influenciou-bastilha","evt:estados-gerais-1789","evt:queda-bastilha-1789","influenciou"),
 ("rel:chicxulub-causou-inverno","evt:impacto-chicxulub","state:clima-pos-impacto-kpg","causou"),
 # ponte cósmico→tempo profundo terrestre (Frente A): a acreção da Terra precede o GOE.
 ("rel:formacao-terra-precede-goe","proc:formacao-terra","proc:goe","precede"),
]

def main():
    cx = psycopg2.connect(DSN); cx.autocommit = False; cu = cx.cursor()
    # idempotência: limpar
    for t in ["core.claim_set_member","core.claim_set","core.relationship","core.claim",
              "core.geometry_version","core.media_asset","core.knowledge_item",
              "core.provenance_metadata","core.source","core.license_profile",
              "derived.derived_cache","iso.media_asset_isolated","core.entity_node"]:
        cu.execute(f"DELETE FROM {t};")

    def node(uri, kind):
        cu.execute("INSERT INTO core.entity_node(uri,entity_kind) VALUES(%s,%s) ON CONFLICT DO NOTHING;",(uri,kind))

    # perfis de licença (governam expressão/asset, nunca o fato — Art.11)
    cu.execute("INSERT INTO core.license_profile(id,label,share_alike,license_risk_level) VALUES "
               "('lic:ccby','CC BY 4.0',false,1),('lic:odbl','ODbL (ShareAlike)',true,2),"
               "('lic:nc','CC BY-NC (NC-como-expressão)',false,4);")

    # fontes + proveniência (uma por item; dedup por string de fonte)
    src_ids = {}
    def source_for(item):
        s = item["src"]; key = s
        if key in src_ids: return src_ids[key]
        sid = "src:%03d" % (len(src_ids)+1)
        node(sid,"source")
        cu.execute("INSERT INTO core.source(id,title,source_type,authority_tier,license) VALUES(%s,%s,%s,%s,%s);",
                   (sid, s, ("demonstração" if item.get("seeded") else "domínio"), item["tier"], "CC BY"))
        src_ids[key] = sid
        return sid

    # itens
    n_geom = 0
    for it in ITENS:
        prov = "seeded-demo" if it.get("seeded") else "corpus"          # D-A3.1
        rev  = "approved" if it["pub"]=="publicável" else "pending"      # D-A3.2
        conf_asset = (not it.get("srcPend", False))                     # §9.2 F2
        node(it["id"],"item")
        cu.execute("""INSERT INTO core.knowledge_item
          (id,item_type,domain,layer,title,canonical_start,canonical_end,canonical_scalar,
           source_time_basis,display_time,time_precision,time_uncertainty,
           review_status,provenance_status,per_asset_source_confirmed,is_global,anachronism_note)
          VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
          (it["id"],it["t"],it["dom"],it["lay"],it["ti"],it["cs"],it["ce"],it["sc"],
           it["stb"],it["disp"],it["prec"],it["unc"],
           rev,prov,conf_asset,bool(it.get("glob",False)),it.get("anach")))

        # claim do item (1 por item) — proveniência OBRIGATÓRIA [N1]
        sid = source_for(it)
        pid = "prov:"+it["id"]
        cu.execute("INSERT INTO core.provenance_metadata(id,source_id,method,scale_version,created_by) VALUES(%s,%s,%s,%s,%s);",
                   (pid,sid,"curadoria A3","3Z","migrate.py"))
        cid = "claim:"+it["id"]
        node(cid,"claim")
        cu.execute("""INSERT INTO core.claim(id,subject_ref,statement,claim_type,evidence_level,confidence,review_status,provenance_ref)
                      VALUES(%s,%s,%s,%s,%s,%s,%s,%s);""",
                   (cid,it["id"],it["ti"],it["ct"],it["ev"],it["cf"],rev,pid))

        # geometria (ponto) para itens com lat/lng; paleo => reconstrução (Art.12/§8)
        if "lat" in it and "lng" in it:
            is_paleo = bool(it.get("caveat"))          # chicxulub: posição reconstruída
            is_recon = is_paleo
            cu.execute("""INSERT INTO core.geometry_version(id,item_ref,geom,is_paleo,is_reconstruction,scale_version)
                          VALUES(%s,%s, ST_SetSRID(ST_MakePoint(%s,%s),4326), %s,%s,%s);""",
                       ("geom:"+it["id"],it["id"],it["lng"],it["lat"],is_paleo,is_recon,"3Z"))
            n_geom += 1

    # claim_sets (claim-sobre-claims) + membros (7 claims-membro novos)
    for csid, cs in CLAIMSETS.items():
        node("cset:"+csid,"claim_set")
        cu.execute("INSERT INTO core.claim_set(id,subject_ref,tema,resolution) VALUES(%s,%s,%s,%s);",
                   ("cset:"+csid, cs["host"], cs["tema"], cs["resolution"]))
        hsrc = src_ids.get(next(i["src"] for i in ITENS if i["id"]==cs["host"]))
        hpid = "prov:"+cs["host"]
        for k,(stmt,w,stance) in enumerate(cs["members"]):
            mcid = "claim:%s:m%d" % (csid,k)
            node(mcid,"claim")
            cu.execute("""INSERT INTO core.claim(id,subject_ref,statement,claim_type,confidence,review_status,provenance_ref)
                          VALUES(%s,%s,%s,%s,%s,%s,%s);""",
                       (mcid, "cset:"+csid, stmt, "interpretação", "média", "approved", hpid))
            cu.execute("INSERT INTO core.claim_set_member(claim_set_id,claim_id,weight,stance) VALUES(%s,%s,%s,%s);",
                       ("cset:"+csid, mcid, w, stance))

    # arestas afirmativas (todas com proveniência)
    for rid,src,dst,rtype in RELS:
        node(rid,"relationship")
        pid = "prov:"+src  # herda proveniência do nó-origem
        cu.execute("""INSERT INTO core.relationship(id,src_ref,dst_ref,relation_type,is_affirmative,provenance_ref,review_status)
                      VALUES(%s,%s,%s,%s,true,%s,'approved');""",(rid,src,dst,rtype,pid))

    # um asset de demonstração em cada partição (exercita o modelo de licença)
    node("asset:paleo-2-4ga","media_asset")
    cu.execute("""INSERT INTO core.media_asset(id,nature_label,license_profile_ref,storage_partition,attribution_text)
                  VALUES('asset:paleo-2-4ga','reconstrução-científica','lic:ccby','media-store','GPlates/EarthByte, CC BY');""")
    cu.execute("""INSERT INTO iso.media_asset_isolated(id,nature_label,license_label,share_alike,attribution_text)
                  VALUES('iso:osm-base','mapa','ODbL',true,'© OpenStreetMap contributors, ODbL');""")

    cx.commit()

    # relatório de carga
    def one(q):
        cu.execute(q); return cu.fetchone()[0]
    rep = {
      "itens": one("SELECT count(*) FROM core.knowledge_item"),
      "corpus": one("SELECT count(*) FROM core.knowledge_item WHERE provenance_status='corpus'"),
      "seeded_demo": one("SELECT count(*) FROM core.knowledge_item WHERE provenance_status='seeded-demo'"),
      "approved": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='approved'"),
      "pending": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='pending'"),
      "legal_review": one("SELECT count(*) FROM core.knowledge_item WHERE review_status='legal-review'"),
      "claims_de_item": one("SELECT count(*) FROM core.claim c JOIN core.knowledge_item i ON c.subject_ref=i.id"),
      "claims_membros": one("SELECT count(*) FROM core.claim_set_member"),
      "claims_total": one("SELECT count(*) FROM core.claim"),
      "claimsets": one("SELECT count(*) FROM core.claim_set"),
      "relacoes": one("SELECT count(*) FROM core.relationship"),
      "arestas_afirmativas": one("SELECT count(*) FROM core.relationship WHERE is_affirmative"),
      "n1_rejected": 0,
      "geometrias": one("SELECT count(*) FROM core.geometry_version"),
      "fontes": one("SELECT count(*) FROM core.source"),
      "fontes_por_asset_pendentes": one("SELECT count(*) FROM core.knowledge_item WHERE per_asset_source_confirmed=false"),
      "exibivel_curatorial": one("SELECT count(*) FROM core.v_displayable_curatorial"),
      "publicavel_publico": one("SELECT count(*) FROM core.v_publishable_public"),
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "migration_report.json"),"w",encoding="utf-8") as f:
        json.dump(rep,f,ensure_ascii=False,indent=2)
    print(json.dumps(rep,ensure_ascii=False,indent=2))
    cu.close(); cx.close()

if __name__ == "__main__":
    main()
