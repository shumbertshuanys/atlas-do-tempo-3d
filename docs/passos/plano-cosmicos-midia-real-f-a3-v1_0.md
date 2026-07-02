# Plano — F-A.3 (mídia cósmica real) · v1.0

**Versão:** v1.0 · **Data:** jul/2026 · **Natureza:** plano de execução (lado **planejamento**). **Não escreve código**, não migra dados de fato, não popula asset. Entrega o **desenho do passo** + os **forks para assinatura humana**. A modelagem só começa depois de você assinar as decisões abaixo — e **não** nesta sessão.

**Herda e respeita:** Frente A (5 cósmicos como corpus fonteado; convenção epistêmica hifenizada end-to-end) · B2 (reificação de `MediaAsset`: `nature_label`/`license_profile_ref`/`storage_partition`/arestas `representa`·`evidencia`/CHECK de isolamento) · Etapa 3.1 §7 e §10.7 (regime de mídia; **nenhuma "foto" do evento** cósmico) · Etapa 1.1 (portão de ingestão / licença por asset) · invariantes do miolo (ASSET-T/COSMO-T4/R-V7/Art.7: cena cósmica **sempre** esquemática) · o padrão aditivo provado na virada (`displayPoint` no `011`).

---

## 1. Objetivo

Estrear a **superfície de mídia real** no caminho vivo, anexando imagens **licenciadas e corretamente rotuladas** aos 5 itens cósmicos da Frente A — **no dossiê/popup**, nunca na cena. O estágio cósmico ganha imagem real **sem** virar foto do evento e **sem** rebaixar o piso epistêmico (o CMB continua medição; o Big Bang continua sem foto).

## 2. Escopo

**Dentro:**
- Até **5** `media_asset` (1 por item cósmico), cada um com `nature_label`, licença por asset, `attribution_text`, `textual_equivalent`, ligado ao item por aresta `representa` com `provenance_ref`.
- **Extensão aditiva** do envelope `011` (`f_item_envelope_core`) para carregar `media[]` por item — mesmo padrão do `displayPoint`, derivado do autoritativo, sem tocar o miolo.
- **Extensão aditiva** do modelo do frame (`overlayFields` ganha `media`) + **produtor** que desenha o asset **rotulado** no dossiê, com o `natureLabel` como texto persistente + equivalente textual (sr-only). Nunca seta a textura da cena.
- Suíte nova `MEDIA-T*` (node, framework-free) + guarda de regressão sobre ASSET-T/COSMO-T4.
- Passagem de cada asset pelo **portão de ingestão** (Etapa 1.1): confirmar licença, mapear `license_profile_ref`, rotear a `storage_partition='media-store'`.

**Fora (não nesta frente):**
- A cena procedural (shaders/`regimeLabel`) — **intocada**; nenhuma foto vira globo/órbita.
- Novo tipo epistêmico, novo ClaimSet, novo regime, extensão do eixo 3Z.
- Mídia para itens **não-cósmicos** (GOE/K-Pg/1789) — fica para depois.
- As 3 sensíveis (host `pending`) — seguem bloqueadas.
- Auth/segredos da porta curatorial — é a **E14**, a próxima frente.

## 3. Diagnóstico

- **O §8 não expõe mídia hoje.** No `atlas-model.js`, a cena cósmica é só procedural; nenhum item carrega asset. Logo, F-A.3 = **introduzir** a superfície de mídia, não trocar cena por foto. Distinção estrutural: **cena esquemática** (invariante ASSET-T) ≠ **asset no dossiê** (superfície nova, rotulada).
- **`media_asset` está reificado por B2** (§5.1/§5.2 ex.3): a natureza é **coluna** do asset (e pode ser reforçada por um claim-sobre-asset); a licença força a partição de armazenamento; a asset↔fato é **aresta**, não campo embutido.
- **Sub-checagem obrigatória (primeira coisa na execução):** confirmar em `db/ddl/001-esquema-reificado.sql` que **(a)** a tabela `media_asset` existe com `nature_label`/`license_profile_ref`/`storage_partition`/`attribution_text`/`textual_equivalent`; **(b)** as arestas `representa`/`evidencia` estão utilizáveis; **(c)** há **zero** linhas de asset até aqui. Não pude ler o DDL daqui (não montado nesta interface).
  - Se o design do B2 foi implementado no A3 (provável — "reconstruível do DDL"): F-A.3 é **dado + envelope + frame + testes**, **sem** mudança de schema.
  - Se a tabela estiver ausente: F-A.3 ganha uma sub-etapa de **adição de schema** antes de tudo (adição, não reescrita do miolo).
- **Piso epistêmico já fixado pela Frente A:** CMB = `medição-direta`; Big Bang/galáxias/sistema-solar/Terra = `inferência-científica`. A mídia **não pode contradizer** esse piso (ver a tabela do §4.2).

## 4. Decisões principais (forks abertos — **aguardam sua assinatura**)

### 4.1 Fork técnico — como a mídia chega ao frame

- **Abordagem A — o envelope estende (recomendada).** `f_item_envelope_core` ganha `media[]`, derivado do autoritativo, aditivo, exatamente como o `displayPoint`. Mantém o princípio "**§8 é a fonte única**": os 3 renderizadores desenham o mesmo contrato. Custo conhecido: reaplicar `011` recria as funções via `DROP … CASCADE` e **perde os grants de papel** → reaplicar `020` em seguida (o bootstrap já faz). A3-T3 checa **presença de chaves**: adicionar `media` exige atualizar A3-T3 para esperar a chave nova.
- **Abordagem B — endpoint/consulta de assets separada.** Uma segunda porta só para mídia, fora do envelope. Mais desacoplada, mas **cria uma segunda fonte de verdade** e fura o princípio da fonte única do §8 — o frame teria de casar duas leituras. **Não recomendada.**

> **Recomendação:** Abordagem A. É o padrão já provado na virada, mantém a fonte única e a degradação honesta nos 3 degraus.

### 4.2 Tabela epistêmica de mídia — **assinatura por item** (D-FA3.1…D-FA3.5)

O coração da frente. Para cada item cósmico: que mídia real existe e que `natureLabel` ela **obrigatoriamente** carrega. **Dois itens têm fork interno** (marcados). Nada é modelado antes de você assinar.

| Item | Mídia real disponível | `natureLabel` obrigatório | Cuidado / legenda |
|---|---|---|---|
| **`evt:big-bang`** (D-FA3.1) | Não há foto possível — só ilustração conceitual. | `representação-artística` (ou `reconstrução-científica` se for figura derivada de modelo) | §10.7: **"nenhuma 'foto' do evento"**. Legenda explícita: ilustração, não registro. |
| **`state:cmb-recombinacao`** (D-FA3.2) | Mapa all-sky do CMB (COBE / WMAP / Planck). | **`mapa`** (ou `gráfico`) — é **medição visualizada, NÃO foto** | O ponto epistêmico central: parece "foto do universo bebê", mas é **mapa de dados**. Casa com o tipo `medição-direta` do corpus. |
| **`proc:formacao-galaxias`** (D-FA3.3 — **FORK**) | **(i)** Deep field real (Hubble/JWST) de galáxias jovens → `fotografia`; **ou** **(ii)** ilustração da montagem hierárquica → `representação-artística`. | conforme sua escolha (i)/(ii) | Se (i): legenda de **look-back time** — vemos luz de bilhões de anos atrás; são galáxias reais, não o "início". |
| **`evt:formacao-sistema-solar`** (D-FA3.4 — **FORK**) | **(i)** Foto de disco protoplanetário **análogo** (ALMA / HL Tau) → `fotografia`; **ou** **(ii)** ilustração do **nosso** disco → `representação-artística`/`reconstrução-científica`. | conforme sua escolha (i)/(ii) | Se (i): legenda **"outro sistema, não o nosso Sol"** — análogo, não registro do nosso. |
| **`proc:formacao-terra`** (D-FA3.5) | Não há foto da acreção — só reconstrução. | `representação-artística` ou `reconstrução-científica` | Sem foto possível; legenda de reconstrução. |

Leitura da tabela: dos 5, **no máximo 2** admitem uma `fotografia` genuína (galáxias reais; disco análogo), e **mesmo essas** exigem legenda que impeça a leitura ingênua. O CMB é o caso-armadilha (mapa que parece foto). Big Bang e Terra **não** admitem foto — coerente com §10.7.

### 4.3 Fork de cadência — quantos assets nesta fatia

- **Abordagem A — os 5 de uma vez (recomendada):** piloto completo do pipeline de mídia end-to-end; o estágio cósmico fica **inteiro** com mídia rotulada.
- **Abordagem B — fatiar:** só os epistemicamente mais limpos primeiro (ex.: CMB + galáxias), deixando Big Bang/Sol/Terra para uma segunda fatia. Mais conservador, mas deixa o estágio **parcialmente** sem mídia.

> **Recomendação:** Abordagem A — a superfície é pequena e os 5 rótulos já estão decididos/forkados acima; fatiar só adia sem reduzir risco.

### 4.4 Fork menor — reforço por claim-sobre-asset

- **Só a coluna `nature_label`** (mínimo; é a invariante que os testes travam), **ou** **coluna + claim-sobre-asset** ("esta imagem é `mapa`, não fotografia", padrão B2 §5.2 ex.3) — recomendado **ao menos para o CMB**, onde a confusão foto×mapa é mais provável.

> **Recomendação:** coluna para todos + claim-sobre-asset **no CMB** (cinturão e suspensório no caso-armadilha).

## 5. Modelo conceitual

- **Nós:** até 5 `media_asset`, cada um `{ nature_label, license_profile_ref, attribution_text, textual_equivalent, storage_partition='media-store', storage_uri }`.
- **Arestas:** cada asset —`representa`→ seu item, com `provenance_ref` (a fonte do asset). Opcional (§4.4): `claim` com `subject_ref` = asset, reforçando o `natureLabel`.
- **Envelope (Abordagem A):** `f_item_envelope_core` deriva `media[]` = para cada aresta `representa` que aponta ao item, `{ natureLabel, attribution, textualEquivalent, uri }`. Aditivo; nenhuma chave §8 existente muda.
- **Frame:** `overlayFields` ganha `media` (array, possivelmente vazio). Produtor novo `overlayMediaHTML(ov)` desenha cada asset como figura **rotulada** no dossiê. **Degradação honesta:** num degrau que não exibe imagem (2D/estático), o produtor mostra `natureLabel` + equivalente textual **como texto** — o rótulo nunca some ([R-B2.7]; "degradação não muda o piso").
- **Cena:** `regimeLabel` e shaders **intocados**. O asset vive no dossiê; **nunca** vira textura de globo/órbita (guarda MEDIA-T3 + COSMO-T4).

## 6. Fontes / insumos necessários

- **Imagens:** NASA (domínio público) · ESA/Hubble e ESO/ALMA (tipicamente CC BY 4.0 — **atribuição obrigatória**, viaja no `attribution_text`) · JWST (STScI/NASA, PD com crédito recomendado). **Cada asset** passa pelo **portão da Etapa 1.1**: confirmar licença → `license_profile_ref` → `storage_partition`. Para PD/CC-BY, a partição é `media-store` (**não** isolado, **não** bloqueado).
- **Corpus:** os 5 itens da Frente A (IDs e tipos epistêmicos já assinados) — a mídia **anexa**, não redefine.
- **Editorial:** Etapa 3.1 §7 (regime de mídia) e §10.7 (Big Bang sem foto) como régua dos `natureLabel`.

## 7. Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| R-FA3.1 | **"Foto do evento"** — rotular como `fotografia` algo que não é (Big Bang, Terra, ou o mapa do CMB) | Tabela §4.2 assinada; **MEDIA-T2** trava `fotografia` proibido nesses itens; CMB = `mapa`/`gráfico` |
| R-FA3.2 | **Cena virar foto** — asset usado como textura do estágio | Asset só no dossiê; `regimeLabel`/shaders intocados; **MEDIA-T3** + COSMO-T4 verdes |
| R-FA3.3 | **Licença/atribuição perdida** em export/offline | `attribution_text`+`nature_label` viajam com o asset ([R-B2.7]); **MEDIA-T4** exige presença |
| R-FA3.4 | **Isolamento furado** — asset SA/ODbL/NC contaminando o núcleo | Só PD/CC-BY nesta frente; CHECK de `storage_partition` ([D-B2.4]); sem caminho de leitura ao store isolado |
| R-FA3.5 | **Seeded promovido** — asset sem fonte entrando como corpus | Assets **novos com licença**; aresta `representa` com `provenance_ref`, não embutido; **MEDIA-T5** (anti-seeded) |
| R-FA3.6 | **Chave nova quebra A3-T3** (presença de chaves) | Atualizar A3-T3 para esperar `media`; nenhuma chave existente muda; regressão verde |
| R-FA3.7 | **Legenda ingênua** — foto real (galáxias/disco) lida como "o início" ou "o nosso Sol" | Legenda de look-back time / "análogo, não o nosso" embutida no `textual_equivalent` |

## 8. Entregáveis

1. **Sub-checagem do DDL** (§3) resolvida: schema confirma `media_asset` ou ganha adição.
2. **Migração de até 5 assets** (`migrate.py`, adição) com licença por asset, aresta `representa` + `provenance_ref`, partição `media-store`.
3. **Extensão aditiva do `011`** (`media[]` no envelope) + reaplicação do `020` (grants).
4. **Extensão aditiva do frame** (`overlayFields.media` + `overlayMediaHTML`, com fallback textual) — cena intocada.
5. **Suíte `MEDIA-T1…5`** + guarda de regressão; fixture de porta pública regenerada.
6. **Evidência (PRONTO = EVIDÊNCIA):** re-verde de `verify` · `test_a4` · `test_a3` · `test_a3_http` + `3D-T` · `ASSET-T` · `LIVE-T` · `COSMO-T`, mais `MEDIA-T` fechando; carga atualizada só em `+N assets` (itens/claims/fontes conforme a fatia).
7. **Handoff de execução** (9 pontos + rodapé) em `docs/passos/`.

## 9. Próximos passos

1. **Você assina** os forks: §4.1 (técnico), §4.2 (D-FA3.1…5, incl. os dois forks internos), §4.3 (cadência), §4.4 (reforço no CMB).
2. Com as assinaturas, uma **sessão de modelagem** (não esta) executa os entregáveis do §8, um passo por vez.
3. **Depois da F-A.3:** E14 (segredos Opção B + auth curatorial), conforme sua ordem.

---

## Rodapé — o que este passo NÃO faz

- **NÃO** escreve código, não migra dados, não popula asset — é planejamento; a execução vem depois da sua assinatura.
- **NÃO** toca a cena procedural: nenhuma foto vira globo/órbita/textura (R-V7/Art.7; COSMO-T4).
- **NÃO** rotula como `fotografia` o que não é foto — Big Bang e Terra são reconstrução; o CMB é `mapa`/`gráfico` (§10.7).
- **NÃO** promove `seeded-demo` a corpus; assets são novos, licenciados, com proveniência por aresta.
- **NÃO** reescreve o miolo (`db/ddl`/`010`/`011`): envelope e frame só **estendem** (padrão `displayPoint`).
- **NÃO** cria ClaimSet, tipo epistêmico ou regime novo; **NÃO** estende o eixo 3Z.
- **NÃO** religa as 3 sensíveis (host `pending`); **NÃO** entra em auth/segredos (é a E14).
- **NÃO** fixa `natureLabel` sem assinatura — a tabela §4.2 é proposta, não decisão tomada.
