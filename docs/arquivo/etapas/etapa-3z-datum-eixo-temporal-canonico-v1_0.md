# Etapa 3Z — Datum e Eixo Temporal Canônico

**Projeto (nomes provisórios):** Atlas do Tempo 3D / Linha do Tempo Total
**Status:** Entrega da **Etapa 3Z** (resolução de pendência estrutural do domínio da Etapa 3) · sob a baseline v1.0 (Etapa 0), a auditoria da Etapa 1, o portão da Etapa 1.1, a modelagem do Knowledge Core (Etapa 2), a experiência da Etapa 3, a política editorial 3.1 e os aprendizados da Etapa 4 (4A–4H) · 12/06/2026
**Escopo desta etapa (e seus limites):** **decidir o datum e o eixo temporal canônico** do Knowledge Core — como armazenar, converter e exibir datas/idades num eixo único capaz de ligar tempo cósmico, geológico, biológico, arqueológico, histórico, contemporâneo e projetivo, resolvendo a pendência **1950 BP × J2000** registrada desde as Etapas 4B/4F/4G/4H. Conforme solicitado, **não** cria cenas, **não** povoa conteúdo, **não** escreve código, **não** propõe MVP, **não** define stack, **não** avança para UX final, **não** entra em currículo/professor/plano de aula, **não** reabre auditoria de fontes (1/1.1) e **não** reabre política editorial (3.1).

**O que herda e respeita.** A régua canônica Ga↔dia (Etapa 2), o `TimeRange`/`ChronologicalScale`/`UncertaintyProfile` (Etapa 2), os sete regimes de tempo da matriz da 4F (§4), a `ProvenanceMetadata` (Etapa 2) e a regra “não inventar precisão” (toda a Etapa 4).

-----

## Sumário

1. O problema do datum temporal (Tarefa 1)
1. O eixo canônico interno (Tarefa 2)
1. Preservação do datum original da fonte (Tarefa 3)
1. Regras por regime temporal (Tarefa 4)
1. Decisão 1950 BP × J2000 (Tarefa 5)
1. Exemplos obrigatórios (Tarefa 6)
1. Impacto na timeline (Tarefa 7)
1. Impacto nas cenas existentes (Tarefa 8)
1. Decisão final (Tarefa 9)
1. Próximos passos para a Etapa 5 (Tarefa 10)

-----

## 1. O problema do datum temporal (Tarefa 1)

Comunidades científicas diferentes medem o tempo a partir de **referências (data) diferentes**, em **unidades** diferentes, com **precisões** e **incertezas** diferentes. Um produto que vai do Big Bang ao futuro projetado precisa conciliá-las **sem** impor a linguagem de uma comunidade a todas as outras.

|Sistema                           |O que é                                               |Onde se usa                      |Armadilha                                                           |
|----------------------------------|------------------------------------------------------|---------------------------------|--------------------------------------------------------------------|
|**BP 1950**                       |“Before Present”, com “presente” **fixado em 1950 CE**|arqueologia, Quaternário, datação|“presente” **não é hoje**; datas futuras viram BP negativo (absurdo)|
|**J2000**                         |época de referência astronômica = 2000-01-01 12:00 TT |astronomia, efemérides           |sem sentido para o público em contexto histórico                    |
|**BCE/CE**                        |calendário (proléptico) gregoriano                    |história                         |problema do “ano zero”; ilegível em tempo profundo (13,8 bi BCE)    |
|**ISO 8601**                      |data/hora de calendário precisa (`1969-07-20`)        |tempo contemporâneo              |só serve onde há precisão de dia/hora                               |
|**Ma**                            |mega-annum (milhões de anos **atrás**)                |geologia                         |ilegível para datas históricas (1789 = 0,0000002 Ma)                |
|**Ga**                            |giga-annum (bilhões de anos **atrás**)                |geologia profunda, cosmologia    |idem, ainda mais grosso                                             |
|**radiocarbon BP** (não calibrado)|anos de radiocarbono “brutos”                         |datação ¹⁴C                      |**não são anos de calendário**; exigem calibração                   |
|**calibrated BP (cal BP)**        |BP calibrado para anos de calendário                  |arqueologia                      |depende da **curva de calibração** usada                            |
|**tempo projetivo/futuro**        |ano de cenário + modelo (2050, 2100)                  |clima, projeções                 |não é “fato”; depende do **modelo/cenário**                         |

**Por que nenhum deve ser a única linguagem visível:**

- **BP 1950** confunde o público (“presente” = 1950) e quebra no futuro.
- **J2000** é técnico e mudo para história.
- **BCE/CE** colapsa em tempo profundo e tem o problema do ano zero.
- **Ma/Ga** são inúteis para datas finas.
- **radiocarbon BP** sequer é calendário sem calibração.
- Cada um carrega **precisão e incerteza próprias** — exibir um número seco numa linguagem alheia ao regime **mente sobre a precisão**.

**Conclusão do problema:** é preciso **separar três coisas** que hoje se confundem — (a) **armazenamento interno** (um eixo único para ordenar/intersectar), (b) **datum de origem** (preservado, por honestidade), e (c) **exibição** (apropriada ao regime). Misturá-las é a raiz da pendência.

-----

## 2. O eixo canônico interno (Tarefa 2)

**Proposta: um eixo numérico contínuo único — `canonicalTimeScalar` — medido em anos (decimais) relativos a uma época canônica fixa `T0 = 2000.0 CE` (alinhada a J2000.0).** Negativo = passado; positivo = futuro. Este eixo serve **à máquina** (ordenar, intersectar, buscar, comparar); **não** é, por si, a linguagem de exibição.

**Por que `T0 = 2000.0` (≈ J2000):** (a) é o padrão astronômico moderno; (b) “anos antes de 2000” é intuitivo e quase igual a “anos atrás” para o usuário contemporâneo; (c) a diferença de 50 anos para o BP1950 **só importa no regime histórico/arqueológico de precisão anual** — e nesse regime o BP original é **preservado** (§3) e reconciliado explicitamente; em Ma/Ga, 50 anos é ruído abaixo de qualquer incerteza.

**Campos conceituais do `TimeRange` canônico:**

```txt
TimeRange = {
  canonicalTimeScalar,  # valor ordenável (geralmente o ponto médio), em anos rel. a T0=2000.0 CE; negativo=passado
  canonicalStart,       # limite inicial do intervalo no eixo canônico
  canonicalEnd,         # limite final do intervalo no eixo canônico
  sourceTimeBasis,      # datum nativo da fonte (BP1950 | calBP | radiocarbonBP | J2000 | gregorianCE | ISO8601 | Ma | Ga | scenarioYear)
  displayTime,          # string de exibição, apropriada ao regime (ex.: "~13,8 Ga"; "1789"; "20 jul 1969")
  timePrecision,        # granularidade: Ga|Ma|ka|século|década|ano|mês|dia|cenário
  timeUncertainty,      # ± / faixa / distribuição (nunca "número seco" quando há incerteza)
  temporalConfidence,   # confiança na datação (alta|média-alta|média|média-baixa|baixa)
  conversionMethod,     # como a fonte virou canônico (direto | Ma→anos | Ga→anos | BP1950→T0 | calibração¹⁴C | cenário)
  conversionNotes       # ressalvas (curva de calibração, modelo, datum, caveats)
}
```

**O eixo permite:**

- **ordenação / interseção / simultaneidade:** comparar `canonicalTimeScalar` (ou sobreposição de `[canonicalStart, canonicalEnd]`) entre itens de **qualquer** regime — é o que a função da Etapa 5 precisa.
- **busca por ano / idade geológica / intervalo:** a consulta converte o termo buscado (1789; 2,4 Ga; “14 ka”) para o eixo e intersecta.
- **ligação histórico↔profundo:** ambos são pontos/intervalos no **mesmo** escalar.
- **futuro/projetivo:** valores positivos, com `sourceTimeBasis = scenarioYear` e modelo em `conversionNotes`.
- **precisão e incerteza variáveis:** `timePrecision`/`timeUncertainty` por item; o intervalo `[start,end]` carrega a faixa.

> **Nota de implementação conceitual (não-código):** o escalar vai de ~−1,38×10¹⁰ (Big Bang) a valores pequenos positivos (futuro). O ordenamento é trivial; a **exibição** nunca usa o escalar cru — usa `displayTime`.

-----

## 3. Preservação do datum original da fonte (Tarefa 3)

**Regra obrigatória (vinculante):** o sistema **pode** converter datas para o eixo canônico interno, mas **nunca** apaga o **datum original da fonte**. A conversão é **aditiva**, jamais destrutiva.

**Onde cada coisa vive:**

- **`TimeRange.sourceTimeBasis`** + o **valor original** (no datum nativo) ficam **sempre** no item. Ex.: `sourceTimeBasis = radiocarbonBP`, valor bruto `12.000 ¹⁴C BP`.
- **`TimeRange.canonicalStart/End/Scalar`** são a conversão para o eixo — **derivados**, marcados como tais.
- **`ProvenanceMetadata`** registra: o datum nativo da fonte, a **curva/método de calibração** (quando ¹⁴C), o **modelo de cenário** (quando projetivo), a **versão da escala** (ICS, para Ma/Ga) e quem/quando converteu (`DatasetSnapshot`).

**Exemplos de preservação:**

- **radiocarbono:** preserva `radiocarbonBP` **e** `calBP` (após calibração) **e** a curva usada; o canônico deriva do **cal BP**, nunca do ¹⁴C bruto.
- **dado astronômico:** preserva `J2000` (se a fonte for astronômica).
- **evento histórico:** preserva `gregorianCE`/`ISO8601` (BCE/CE).
- **idade geológica:** preserva `Ma`/`Ga` **e** a versão da escala ICS.
- **cenário climático:** preserva o **ano do cenário** (2050/2100) **e** o **modelo/RCP-SSP**.

> **Princípio de honestidade temporal:** se a fonte disse “12.000 ¹⁴C BP”, o produto deve poder mostrar isso — a conversão é uma **lente**, não uma sobrescrita. Apagar o datum original seria o equivalente temporal de apagar a proveniência de um claim (proibido desde a Etapa 1.1).

-----

## 4. Regras por regime temporal (Tarefa 4)

Para cada um dos sete regimes (matriz da 4F §4): formato de entrada, datum comum da fonte, conversão interna, formato de exibição, precisão típica, incerteza típica e risco de erro.

|Regime                    |Entrada             |Datum/fonte comum                              |Conversão interna                                           |Exibição                              |Precisão típica|Incerteza típica               |Risco de erro                                  |
|--------------------------|--------------------|-----------------------------------------------|------------------------------------------------------------|--------------------------------------|---------------|-------------------------------|-----------------------------------------------|
|**1. Cósmico**            |Ga                  |inferência astronômica (não J2000 para a idade)|`Ga → anos rel. T0`                                         |“~13,8 Ga”                            |Ga (faixa)     |± dezenas de Ma a centenas     |tratar como data exata                         |
|**2. Geológico profundo** |Ga/Ma               |ICS + datação radiométrica                     |`Ma/Ga → anos rel. T0` (50 anos = ruído)                    |“~2,4 Ga” / “~66 Ma”                  |Ga/Ma (faixa)  |± Ma                           |falsa precisão; ignorar versão ICS             |
|**3. Biológico/evolutivo**|Ma/ka               |PBDB + escala                                  |`Ma/ka → anos rel. T0`                                      |“~300 ka” / “~66 Ma”                  |Ma/ka (faixa)  |± significativa em origens     |datas de origem como cravadas                  |
|**4. Arqueológico**       |ka / cal BP / ¹⁴C BP|**cal BP** (radiocarbono calibrado)            |**calibrar ¹⁴C→cal BP**, depois `cal BP → T0` (**+50 anos**)|“~14.000 anos atrás” ou “~12.000 a.C.”|século/milênio |faixa de calibração            |usar ¹⁴C bruto; ignorar o offset de 50 anos    |
|**5. Histórico**          |BCE/CE / ISO        |gregoriano proléptico                          |`CE/BCE → anos rel. T0` (ano-zero astronômico)              |“1789”, “476 d.C.”, “44 a.C.”         |ano/dia        |lacunas documentais            |erro do ano zero; calendário juliano×gregoriano|
|**6. Contemporâneo**      |ISO 8601            |calendário + dados                             |`ISO → anos rel. T0` (direto)                               |“20 jul 1969”, “1969”                 |dia/ano        |baixa (datas), variável (dados)|confundir dado medido com estimativa           |
|**7. Projetivo/futuro**   |ano de cenário      |ano + **modelo** (RCP/SSP)                     |`ano → anos rel. T0` (positivo)                             |“2050 (cenário X)”                    |cenário        |faixa de cenários              |exibir projeção como fato                      |

**Regras transversais:**

- **Radiocarbono nunca entra cru:** calibrar para cal BP **antes** de mapear ao canônico; preservar ambos (§3).
- **O offset de 50 anos (BP1950→T0=2000) só é aplicado nos regimes 4 e 5** (precisão ≤ século); nos regimes 1–3 é descartável (abaixo da incerteza).
- **Futuro é sempre rotulado** com cenário/modelo; jamais exibido como fato datado.

-----

## 5. Decisão 1950 BP × J2000 (Tarefa 5)

A recomendação preliminar do enunciado está **correta** e é **confirmada**, com **três refinamentos**:

**Confirmado:**

- **Não** usar BP1950 nem J2000 como **única linguagem visível**.
- Usar um **eixo canônico interno** (§2).
- **Preservar `sourceTimeBasis`** (§3).
- **Converter** conforme a necessidade.
- **Exibir** de acordo com o **regime** (§4).
- Usar **BP1950** quando a fonte for de fato BP/radiocarbono (e o público, arqueológico).
- Usar **J2000** quando a fonte for de fato astronômica.
- **Não** converter visualmente tudo para BP nem para J2000.

**Refinamentos (precisões adicionadas):**

1. **A época canônica interna é `T0 = 2000.0 CE`, alinhada a J2000.0** — escolhida como **âncora de armazenamento** (não de exibição). Isso resolve a tensão: J2000 deixa de competir com BP1950 pela tela e passa a ser apenas a **referência interna**; BP1950 vira um `sourceTimeBasis` preservado e convertido.
1. **A reconciliação dos 50 anos (BP1950 ↔ T0=2000) é regra explícita** e aplicada **somente** nos regimes 4–5 (precisão ≤ século). Documentada em `conversionMethod = BP1950→T0` / `conversionNotes`.
1. **Radiocarbono exige calibração** (¹⁴C BP → cal BP) **antes** da conversão canônica; o ¹⁴C bruto é preservado, nunca usado diretamente no eixo.

**Em uma frase:** *o sistema armazena tudo num eixo único ancorado em 2000.0 CE (≈J2000), preserva o datum nativo de cada fonte, e exibe cada item na linguagem do seu regime — BP só quando a fonte é BP, J2000 só internamente/astronômico, anos para história, Ma/Ga para tempo profundo.*

-----

## 6. Exemplos obrigatórios (Tarefa 6)

Aplicação da decisão aos oito exemplos. `canonical` = `canonicalTimeScalar` (anos rel. a T0=2000.0 CE; negativo=passado), com `[start,end]` quando faixa.

|#|Exemplo                         |sourceTimeBasis            |canonical (anos rel. T0)             |displayTime                |timePrecision          |timeUncertainty                   |conversionNotes                                                                        |
|-|--------------------------------|---------------------------|-------------------------------------|---------------------------|-----------------------|----------------------------------|---------------------------------------------------------------------------------------|
|1|**Big Bang**                    |inferência cosmológica (Ga)|≈ −1,38×10¹⁰                         |“~13,8 Ga”                 |Ga                     |±~2×10⁷ (0,02 Ga)                 |Ga→anos; offset de 50 anos descartável                                                 |
|2|**GOE**                         |Ga (NOAA Paleo)            |faixa ≈ [−2,4×10⁹, −2,0×10⁹]         |“~2,4 Ga”                  |Ga (faixa)             |bordas difusas (~10⁸)             |processo, não ponto; ICS                                                               |
|3|**K-Pg**                        |Ma (ICS, radiométrico)     |≈ −6,6×10⁷                           |“~66 Ma”                   |Ma (alta res. relativa)|±~10⁴–10⁵                         |limite K-Pg bem datado; offset descartável                                             |
|4|**Povoamento das Américas**     |cal BP (de ¹⁴C calibrado)  |faixa ≈ [−1,8×10⁴, −1,5×10⁴] (aprox.)|“~15.000–18.000 anos atrás”|milênio (faixa)        |faixa de calibração + debate      |**calibrar ¹⁴C→cal BP**; cal BP→T0 com **+50 anos**; ver `claimset:povoamento-americas`|
|5|**Revolução Francesa**          |gregorianCE                |−211                                 |“1789”                     |ano                    |— (data documentada)              |CE→T0 (1789−2000); ano-zero astronômico                                                |
|6|**Apollo 11**                   |ISO 8601                   |≈ −30,45                             |“20 jul 1969”              |dia                    |—                                 |ISO→T0 direto; `1969-07-20`                                                            |
|7|**Mudanças climáticas modernas**|ISO/ano (séries)           |faixa ≈ [−150, +25] (1850→hoje)      |“1850–presente”            |ano (séries)           |baixa (medição), cresce no recente|dados medidos; figuras recriadas                                                       |
|8|**Cenário climático futuro**    |scenarioYear + modelo      |+50 / +100                           |“2050 / 2100 (cenário)”    |cenário                |faixa de cenários (SSP/RCP)       |**projeção, não fato**; preservar modelo/cenário                                       |


> **Destaque (exemplo 4):** é o único onde o **offset de 50 anos importa** e onde a **calibração** é obrigatória — exatamente o regime que motivou a tensão BP1950×J2000. A decisão o trata explicitamente; nos exemplos 1–3 o mesmo offset é ruído.

-----

## 7. Impacto na timeline (Tarefa 7)

A decisão (eixo canônico único + exibição por regime) é o que **permite** uma timeline coerente do Big Bang ao futuro.

- **Zoom logarítmico:** o eixo canônico (anos rel. T0) suporta uma escala **log** para tempo profundo (de Ga a ka), porque é um escalar contínuo único — sem log, 13,8 Ga esmagaria toda a história humana num pixel.
- **Escala histórica linear:** ao aproximar dos últimos milênios, a timeline troca para escala **linear** em anos — a mesma `canonicalTimeScalar`, outra projeção visual.
- **Alternância Ma/Ga ↔ anos:** o `displayTime` por regime faz a régua **trocar de rótulo** automaticamente conforme o zoom (Ga→Ma→ka→séculos→anos→dias), sem mudar o dado subjacente.
- **Eventos pontuais:** plotados pelo `canonicalTimeScalar` (ponto); em tempo profundo, ainda assim com barra de incerteza.
- **Processos longos:** plotados por `[canonicalStart, canonicalEnd]` (barra), com bordas difusas quando incertas.
- **States:** faixas de fundo no intervalo canônico.
- **Cenas contemporâneas:** escala linear fina (dia/ano); séries de dados.
- **Cenas futuras:** região **positiva** do eixo, visualmente **rotulada como projeção** (hachura/cor distinta).
- **Comparação antes/depois:** dois cortes no mesmo eixo canônico (ex.: K-Pg −66 Ma × Paleoceno) — trivial porque é o mesmo escalar.
- **Função “O que acontecia no mundo neste momento?”:** é uma **interseção** no eixo canônico — dado um ponto/intervalo, retornam-se todos os itens cujos `[start,end]` o contêm. **É a decisão desta etapa que torna a função da Etapa 5 possível entre regimes.**

-----

## 8. Impacto nas cenas existentes (Tarefa 8)

Revisão **conceitual** (sem reescrever as cenas). Pergunta: o eixo canônico exige mudança no padrão `Scene` v1.1?

**Resposta geral: NÃO há mudança estrutural no `Scene` v1.1.** O eixo canônico vive **dentro** do `TimeRange` de cada item (campos `canonical*`/`sourceTimeBasis`), que o `Scene` já referencia via `timeRange`/`timePrecision`. As cenas **herdam** o eixo sem alteração de esquema; ganham apenas **precisão interna** de ordenação/interseção.

|Cena                                           |Precisa alterar Scene v1.1?|Impacto (apenas indicado)                                                                                                                                    |
|-----------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**1789** (`scene:world-1789-french-revolution`)|**Não**                    |`sourceTimeBasis = gregorianCE`; `displayTime="1789"` (já era). Eventos de dia (Bastilha `1789-07-14`) ganham `canonical` preciso. Nenhum campo novo na cena.|
|**2,4 Ga / GOE** (`scene:earth-2-4ga-...`)     |**Não**                    |`sourceTimeBasis = Ga`; faixa `[−2,4e9,−2,0e9]`; offset de 50 anos descartado. `displayTime` “~2,4 Ga” inalterado.                                           |
|**66 Ma / K-Pg** (`scene:earth-66ma-...`)      |**Não**                    |`sourceTimeBasis = Ma`; impacto como ponto `≈−6,6e7`; extinção como faixa. `paleoPosition` (4H) e datum são **ortogonais** — um é espaço, outro é tempo.     |


> **Observação:** a decisão **valida retroativamente** o que as cenas já faziam (tratar “2,4 Ga”/“66 Ma” como aproximações de faixa, e datas históricas como anos). Formaliza o que estava implícito. Único acréscimo operacional: ao **confirmar fontes por asset** (pendência aberta), preencher `sourceTimeBasis`/`conversionMethod` de cada `TimeRange` — trabalho de curadoria, não de remodelagem.

-----

## 9. Decisão final (Tarefa 9)

**Datum interno escolhido.** Eixo único `canonicalTimeScalar` = **anos (decimais) relativos à época canônica `T0 = 2000.0 CE`, alinhada a J2000.0**; negativo = passado, positivo = futuro. Intervalos via `[canonicalStart, canonicalEnd]`. É a **âncora de armazenamento e ordenação**, não a linguagem de exibição.

**Preservação do datum original.** Obrigatória e aditiva: cada `TimeRange` guarda `sourceTimeBasis` + valor nativo; `ProvenanceMetadata` guarda método/curva/modelo/versão de escala. O canônico é **derivado** e marcado como tal. **Nunca** se apaga o datum da fonte.

**Regra de exibição.** Por **regime** (§4): Ga/Ma em tempo profundo; “anos atrás”/“a.C.” no arqueológico; ano/data no histórico/contemporâneo; “ano (cenário/modelo)” no futuro. **BP** só quando a fonte é BP/¹⁴C; **J2000** apenas interno/astronômico. Nunca converter a **tela** inteira para BP ou J2000.

**Regra de conversão.** `conversionMethod` registra a transformação (Ma/Ga→anos; CE/BCE→T0; ISO→T0; **¹⁴C→cal BP→T0**; cenário→T0). O **offset de 50 anos** (BP1950→T0=2000) aplica-se **apenas** aos regimes arqueológico/histórico (precisão ≤ século); é ruído em Ma/Ga. Radiocarbono **sempre** calibrado antes do eixo.

**Exceções.**

- **Tempo profundo (Ga/Ma):** offset de 50 anos descartado (abaixo da incerteza).
- **Astronomia de efemérides:** pode manter J2000 nativo (é o caso onde J2000 é a fonte real).
- **Futuro:** sempre rotulado como projeção; nunca “fato datado”.
- **Datas pré-gregorianas:** usar gregoriano **proléptico** + nota; cuidar do ano-zero astronômico e de juliano×gregoriano.

**Riscos.**

- **Falsa precisão** ao converter faixas profundas em números cravados — mitigado por `timePrecision`/`timeUncertainty` obrigatórios.
- **Radiocarbono não calibrado** entrando cru — mitigado pela regra de calibração obrigatória.
- **Offset de 50 anos** aplicado no regime errado — mitigado pela regra “só ≤ século”.
- **Exibir projeção como fato** — mitigado pelo rótulo de cenário/modelo.

**Decisões pendentes (registradas, não resolvidas aqui):**

- Escolha fina da **curva de calibração** ¹⁴C padrão (ex.: família IntCal) — decisão de curadoria/ingestão, por asset.
- Tratamento de **calendários não-ocidentais** (lunar islâmico, etc.) como `sourceTimeBasis` adicionais — futura, quando surgirem fontes que o exijam.
- **Fuso/hora** em eventos contemporâneos de precisão sub-diária — quando necessário.

-----

## 10. Próximos passos para a Etapa 5 (Tarefa 10)

A Etapa 3Z fecha a pendência do datum: existe agora **um eixo único** que liga cósmico→profundo→histórico→contemporâneo→futuro, **preserva** o datum de origem e **exibe** por regime. Isso é precondição direta da função da Etapa 5.

**O que a Etapa 5 deve consumir desta decisão (exatamente):**

1. **O eixo `canonicalTimeScalar` (T0 = 2000.0 CE ≈ J2000) como base da interseção temporal** — a função “O que acontecia no mundo neste momento?” é uma **interseção de intervalos `[canonicalStart, canonicalEnd]`** neste eixo; é assim que ela opera **entre regimes** (1789 e 2,4 Ga no mesmo eixo).
1. **A regra de exibição por regime** (§4) — a Etapa 5 deve devolver resultados com `displayTime` apropriado ao regime de cada item, não no escalar cru.
1. **A preservação de `sourceTimeBasis`** (§3) — a função deve poder mostrar “como a fonte mediu o tempo” (honestidade temporal), não só a conversão.
1. **`timePrecision`/`timeUncertainty`** — a interseção deve respeitar **incerteza** (um item com faixa difusa “aparece” no momento consultado com a ressalva de incerteza, não como presença cravada).
1. **O tratamento do futuro/projetivo** — a Etapa 5 deve saber distinguir um resultado **factual** de um **projetivo (cenário/modelo)** ao responder a consultas no lado positivo do eixo.

**Pendências que seguem para outras etapas (não para a 5):** curva de calibração ¹⁴C padrão; calendários não-ocidentais; reificação de `Source`/`MediaAsset`; confirmação asset-level (que passará a preencher `sourceTimeBasis`/`conversionMethod`).

-----

## Encerramento

- **Pendência do datum: resolvida.** Eixo canônico único ancorado em **T0 = 2000.0 CE (≈ J2000)**, com datum de origem **preservado** e exibição **por regime**.
- **1950 BP × J2000: decidido.** Nenhum dos dois é a linguagem visível; J2000 é a âncora **interna**, BP1950 é um `sourceTimeBasis` **preservado e convertido** (com offset de 50 anos só onde a precisão exige).
- **Impacto nas cenas:** **nenhuma alteração estrutural** no `Scene` v1.1 — a decisão formaliza o que as três cenas-gabarito já faziam.
- **Pronto para a Etapa 5.** A função “O que acontecia no mundo neste momento?” tem agora o eixo único de que precisava para intersectar regimes diferentes.

-----

*Documento de entrega da Etapa 3Z, sob todas as etapas anteriores (0, 1, 1.1, 2, 3, 3.1, 4A–4H, 4Z). Resolve a pendência estrutural do datum temporal: define o eixo canônico interno (`canonicalTimeScalar`, T0 = 2000.0 CE ≈ J2000), a preservação obrigatória do `sourceTimeBasis`, as regras por regime temporal, a decisão formal 1950 BP × J2000, os oito exemplos, o impacto na timeline e nas cenas existentes (sem alteração estrutural do `Scene` v1.1) e o que a Etapa 5 deve consumir. Não cria cenas, não povoa conteúdo, não escreve código, não propõe MVP, não define stack, não avança para UX final, não entra em currículo/professor/plano de aula, não reabre auditoria de fontes nem política editorial. Pendência do datum encerrada; Etapa 5 — Função “O que acontecia no mundo neste momento?” — desbloqueada.*