#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de rascunhos da rodada de medição (v0) — o stand-in de 'rascunhar (IA)'
para o Chat 5. Num sistema pleno, retrieval+LLM produziria estes pacotes; aqui
eles são codificados numa tabela compacta e escritos como JSON em
ingestao/rascunhos/. São PROPOSTAS DA IA aguardando revisão humana (§6.1) — não
verdade. As fontes citadas são autoridades reais propostas (Art.5); o revisor
as abre e confere no checklist. Nenhum campo review_status/provenance_status é
escrito aqui (§3.1): eles nascem só na promoção humana.

Alvos (spec §10, "sugestão da rodada, sem virar curadoria"):
  T1 — efemérides consensuais fonte A, gregorianCE (≥10);
  T0 — fatia Brasil por tema sensível (PG5 'mediado', Leis 10.639/11.645) (3).
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(AQUI, "rascunhos")


def ano(y):
    """Escalar canônico 3Z para um ano gregoriano (T0 = 2000.0 CE)."""
    return float(y - 2000)


def pacote(pid, iid, item_type, domain, layer, title, y, disp, ctype, conf, evid,
           lat, lng, place, statement, src_title, tier, lic, locator, uri,
           pg5="público", tier_proposto="T1", precisao="dia", incerteza="data exata",
           is_global=False, anach=None):
    a = ano(y)
    geo = None
    if lat is not None:
        geo = {"lat": lat, "lng": lng, "place": place, "is_paleo": False,
               "is_reconstruction": False, "modern_correspondence": None}
    return {
        "pacote_id": pid,
        "item": {
            "id": iid, "item_type": item_type, "domain": domain, "layer": layer,
            "title": title, "canonical_start": a, "canonical_end": a, "canonical_scalar": a,
            "source_time_basis": "gregorianCE", "display_time": disp,
            "time_precision": precisao, "time_uncertainty": incerteza,
            "is_global": is_global, "anachronism_note": anach, "geo": geo,
        },
        "claims": [{"local_id": "c1", "statement": statement, "claim_type": ctype,
                    "confidence": conf, "evidence_level": evid, "uncertainty_profile": incerteza,
                    "bindings": [{"source_local_id": "s1", "locator": locator}]}],
        "sources": [{"local_id": "s1", "title": src_title, "authority_tier": tier,
                     "license": lic, "uri": uri, "is_aggregator": False}],
        "relations": [], "claim_set": None, "pg5": pg5, "tier_proposto": tier_proposto,
        "pessoa_viva_citada": False, "contem_dado_menor": False,
        "ms_maquina": 1500,  # custo de máquina informativo (não entra no número humano)
    }


# ------------------------ Tier 1: efemérides consensuais fonte A -------------
T1 = [
    pacote("pkg-t1-14bis", "evt:voo-14bis-1906", "Event", "historia", "Ciência e técnica",
           "Voo público do 14-Bis (Santos Dumont)", 1906, "23 de outubro de 1906",
           "fato-documentado", "alta", "documental", 48.869, 2.249, "Campo de Bagatelle, Paris",
           "Em 23/10/1906 o 14-Bis de Santos Dumont fez voo público homologado em Bagatelle, Paris.",
           "Aéro-Club de France — atas de homologação (1906)", "A", "domínio público",
           "ata de 23/10/1906", "https://gallica.bnf.fr"),
    pacote("pkg-t1-cabo", "evt:cabo-transatlantico-1866", "Event", "historia", "Comunicações",
           "Cabo telegráfico transatlântico permanente", 1866, "27 de julho de 1866",
           "fato-documentado", "alta", "documental", 47.63, -53.10, "Heart's Content, Terra Nova",
           "Em 27/07/1866 entrou em operação o primeiro cabo telegráfico transatlântico permanente.",
           "Atlantic Telegraph Company — registros operacionais (1866)", "A", "domínio público",
           "registro de 27/07/1866", "https://archive.org"),
    pacote("pkg-t1-sobral", "evt:eclipse-sobral-1919", "Event", "fisica", "Astronomia",
           "Eclipse solar de Sobral (teste da relatividade geral)", 1919, "29 de maio de 1919",
           "medição-direta", "alta", "medição astronômica", -3.69, -40.35, "Sobral, Ceará",
           "A observação do eclipse de 29/05/1919 mediu a deflexão da luz estelar consistente com a RG.",
           "Dyson, Eddington & Davidson (1920), Phil. Trans. R. Soc. A 220", "A", "domínio público",
           "p. 291", "https://royalsocietypublishing.org"),
    pacote("pkg-t1-wright", "evt:primeiro-voo-wright-1903", "Event", "historia", "Ciência e técnica",
           "Primeiro voo motorizado dos irmãos Wright", 1903, "17 de dezembro de 1903",
           "fato-documentado", "alta", "documental", 36.02, -75.67, "Kitty Hawk, Carolina do Norte",
           "Em 17/12/1903 o Flyer dos Wright realizou o primeiro voo motorizado sustentado e controlado.",
           "Smithsonian National Air and Space Museum — acervo Wright", "A", "CC BY",
           "ficha do Wright Flyer", "https://airandspace.si.edu"),
    pacote("pkg-t1-lindbergh", "evt:travessia-lindbergh-1927", "Event", "historia", "Ciência e técnica",
           "Travessia aérea solo do Atlântico (Lindbergh)", 1927, "20–21 de maio de 1927",
           "fato-documentado", "alta", "documental", 49.01, 2.55, "Le Bourget, Paris (chegada)",
           "Em 20–21/05/1927 Charles Lindbergh cruzou o Atlântico sem escalas de Nova York a Paris.",
           "U.S. Library of Congress — registros da travessia (1927)", "A", "domínio público",
           "registro de chegada 21/05/1927", "https://loc.gov"),
    pacote("pkg-t1-raiox", "evt:descoberta-raios-x-1895", "Event", "fisica", "Física",
           "Descoberta dos raios X (Röntgen)", 1895, "8 de novembro de 1895",
           "fato-documentado", "alta", "documental", 49.79, 9.94, "Würzburg, Alemanha",
           "Em 08/11/1895 Wilhelm Röntgen registrou uma nova radiação penetrante, os raios X.",
           "Röntgen (1895), Sitzungsberichte der Würzburger Physik.-Medic. Gesellschaft", "A", "domínio público",
           "comunicação de 1895", "https://archive.org"),
    pacote("pkg-t1-marconi", "evt:radio-transatlantico-1901", "Event", "historia", "Comunicações",
           "Primeira transmissão de rádio transatlântica (Marconi)", 1901, "12 de dezembro de 1901",
           "fato-documentado", "média-alta", "documental", 47.57, -52.68, "Signal Hill, Terra Nova",
           "Em 12/12/1901 Marconi relatou a recepção do primeiro sinal de rádio transatlântico.",
           "Marconi — cadernos e correspondência (1901); acervo institucional", "A", "domínio público",
           "nota de 12/12/1901", "https://archive.org"),
    pacote("pkg-t1-suez", "evt:abertura-canal-suez-1869", "Event", "historia", "Infraestrutura",
           "Abertura do Canal de Suez", 1869, "17 de novembro de 1869",
           "fato-documentado", "alta", "documental", 30.58, 32.27, "Ismailia / Canal de Suez",
           "Em 17/11/1869 o Canal de Suez foi inaugurado, ligando o Mediterrâneo ao Mar Vermelho.",
           "Compagnie universelle du canal de Suez — atas de inauguração (1869)", "A", "domínio público",
           "ata de 17/11/1869", "https://gallica.bnf.fr"),
    pacote("pkg-t1-panama", "evt:abertura-canal-panama-1914", "Event", "historia", "Infraestrutura",
           "Abertura do Canal do Panamá", 1914, "15 de agosto de 1914",
           "fato-documentado", "alta", "documental", 9.08, -79.68, "Canal do Panamá",
           "Em 15/08/1914 o Canal do Panamá abriu à navegação com a travessia do SS Ancon.",
           "U.S. National Archives — Panama Canal records (1914)", "A", "domínio público",
           "registro da travessia do Ancon", "https://archives.gov"),
    pacote("pkg-t1-venus", "evt:transito-venus-1874", "Event", "fisica", "Astronomia",
           "Trânsito de Vênus de 1874", 1874, "9 de dezembro de 1874",
           "medição-direta", "alta", "medição astronômica", None, None, None,
           "O trânsito de Vênus de 09/12/1874 foi observado por expedições para medir a paralaxe solar.",
           "Relatórios das expedições ao trânsito de Vênus (1874–1877)", "A", "domínio público",
           "relatório da expedição 1874", "https://archive.org", is_global=True),
    pacote("pkg-t1-krakatoa", "evt:erupcao-krakatoa-1883", "Event", "geologia", "Vulcanismo",
           "Erupção do Krakatoa de 1883", 1883, "27 de agosto de 1883",
           "fato-documentado", "alta", "registro documental/instrumental", -6.10, 105.42, "Estreito de Sunda",
           "Em 27/08/1883 a erupção paroxística do Krakatoa foi registrada global e instrumentalmente.",
           "Royal Society (1888), The Eruption of Krakatoa and Subsequent Phenomena", "A", "domínio público",
           "p. 1 (relatório)", "https://archive.org"),
]

# ------------------------ Tier 0: fatia Brasil por tema sensível -------------
# PG5 'mediado' por TEMA (Leis 10.639/2003 e 11.645/2008), mesmo sendo fato
# documentado — bom teste da triagem por tema (§10). Pessoas históricas
# (falecidas): sem bloqueio de pessoa viva. Na promoção → 'pending' (sem papel
# competente designado, D-20260708) e entram na fila viva.
T0 = [
    pacote("pkg-t0-lei-aurea", "evt:lei-aurea-1888", "Event", "historia", "Brasil",
           "Lei Áurea (abolição da escravidão)", 1888, "13 de maio de 1888",
           "fato-documentado", "alta", "documental", -22.90, -43.18, "Rio de Janeiro",
           "A Lei nº 3.353 de 13/05/1888 declarou extinta a escravidão no Brasil.",
           "Coleção das Leis do Império do Brasil — Lei nº 3.353/1888", "A", "domínio público",
           "Lei nº 3.353, art. 1º", "https://www2.camara.leg.br",
           pg5="mediado", tier_proposto="T0",
           anach="Tema regido pelas Leis 10.639/2003 e 11.645/2008; abolição não encerra o racismo estrutural."),
    pacote("pkg-t0-chibata", "evt:revolta-da-chibata-1910", "Event", "historia", "Brasil",
           "Revolta da Chibata", 1910, "22–27 de novembro de 1910",
           "fato-documentado", "alta", "documental", -22.90, -43.15, "Baía de Guanabara, Rio de Janeiro",
           "Em novembro de 1910 marinheiros liderados por João Cândido se revoltaram contra os castigos físicos.",
           "Arquivo Nacional — documentação da Revolta da Chibata", "B", "domínio público",
           "fundo Marinha, 1910", "https://arquivonacional.gov.br",
           pg5="mediado", tier_proposto="T0", precisao="dia", incerteza="intervalo de dias",
           anach="Tema de história afro-brasileira (Lei 10.639/2003)."),
    pacote("pkg-t0-males", "evt:levante-dos-males-1835", "Event", "historia", "Brasil",
           "Levante dos Malês", 1835, "24–25 de janeiro de 1835",
           "fato-documentado", "alta", "documental", -12.97, -38.51, "Salvador, Bahia",
           "Em 24–25/01/1835 africanos muçulmanos escravizados e libertos se levantaram em Salvador.",
           "Documentação judicial e historiografia do Levante dos Malês", "B", "domínio público",
           "autos do processo, 1835", "https://arquivonacional.gov.br",
           pg5="mediado", tier_proposto="T0", precisao="dia", incerteza="intervalo de dias",
           anach="História afro-brasileira e das religiões de matriz africana (Leis 10.639/2003 e 11.645/2008)."),
]


def main():
    os.makedirs(DEST, exist_ok=True)
    n = 0
    for pkg in T1 + T0:
        caminho = os.path.join(DEST, pkg["pacote_id"] + ".json")
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(pkg, f, ensure_ascii=False, indent=2)
        n += 1
        print("escrito:", os.path.relpath(caminho, AQUI))
    print(f"\n{n} rascunhos escritos ({len(T1)} T1 + {len(T0)} T0).")


if __name__ == "__main__":
    main()
