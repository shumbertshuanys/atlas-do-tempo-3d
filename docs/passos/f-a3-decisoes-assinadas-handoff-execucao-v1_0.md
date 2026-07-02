# F-A.3 (mídia cósmica real) — Decisões assinadas + handoff de execução · v1.0

**Versão:** v1.0 · **Data:** jul/2026 · **Natureza:** registro anti-perda (lado **planejamento**). Fecha o passo de planejamento da F-A.3 com **todos os forks assinados** e entrega o contrato para a **sessão de execução (Claude Code)**. **Não escreve código.**
**Complementa:** `docs/passos/plano-cosmicos-midia-real-f-a3-v1_0.md` (o plano de 9 pontos).

---

## 1. Decisões assinadas (travadas — não reabrir sem nova assinatura)

| # | Decisão | Valor assinado |
|---|---|---|
| §4.1 | Superfície técnica | **A** — o envelope `011` estende com `media[]` (padrão aditivo do `displayPoint`; fonte única do §8; reaplicar `020` após o `DROP … CASCADE` do `011`). |
| §4.3 | Cadência | **Os 5 de uma vez** (piloto completo do pipeline de mídia). |
| §4.4 | Reforço epistêmico | `nature_label` (coluna) em **todos**; **+ claim-sobre-asset** "esta imagem é `mapa`, não fotografia" **só no CMB** (padrão B2 §5.2 ex.3). |
| D-FA3.1 | `evt:big-bang` | **`representação-artística`** (ou `reconstrução-científica` se a figura escolhida for derivada de modelo — decide-se no asset, na ingestão). **Sem foto** (§10.7). |
| D-FA3.2 | `state:cmb-recombinacao` | **`mapa`** (medição visualizada — COBE/WMAP/Planck; casa com o tipo `medição-direta` do corpus). |
| D-FA3.3 | `proc:formacao-galaxias` | **`fotografia`** — deep field real (Hubble/JWST); **legenda de look-back time** ("galáxias reais; vemos luz de bilhões de anos atrás, não 'o início'"). |
| D-FA3.4 | `evt:formacao-sistema-solar` | **`fotografia`** — disco protoplanetário **análogo** (ALMA/HL Tau); **legenda "outro sistema, não o nosso Sol"**. |
| D-FA3.5 | `proc:formacao-terra` | **`representação-artística`** ou **`reconstrução-científica`**. **Sem foto**. |

**Distribuição emergente:** 2 `fotografia` (galáxias, disco análogo) · 1 `mapa` (CMB) · 2 reconstrução/arte (Big Bang, Terra). Foto onde há **objeto observável**; mapa onde é **medição**; arte onde **nada é observável**.

## 2. Guardrails que a execução DEVE preservar (invariantes, não preferências)

- **Cena esquemática intocada:** `regimeLabel`/shaders não mudam; o asset vive **só no dossiê**, nunca vira textura de globo/órbita (R-V7 / Art.7 / COSMO-T4).
- **Piso epistêmico:** nenhum asset rotulado `fotografia` onde não há objeto observável (Big Bang, Terra) nem sobre o **mapa** do CMB.
- **Licença por asset (portão Etapa 1.1):** confirmar licença → `license_profile_ref` → `storage_partition='media-store'` (PD/CC-BY; **nunca** isolado/blocked nesta frente). `attribution_text` (CC-BY: ESA/Hubble, ESO/ALMA) **viaja com o asset** ([R-B2.7]).
- **Anti-seeded:** assets **novos com fonte**; asset↔item é **aresta `representa` com `provenance_ref`**, nunca embutido ([D-B2.3]). Nenhum `seeded-demo` promovido.
- **Degradação honesta:** num degrau sem imagem (2D/estático), o produtor mostra `natureLabel` + equivalente textual **como texto** — o rótulo nunca some.
- **Miolo intocado:** `db/ddl/`/`010`/`011` só **estendem** (não reescrevem); nenhum tipo epistêmico, ClaimSet, regime ou eixo 3Z novo.

## 3. Entregáveis da execução (do §8 do plano)

1. **Sub-checagem do DDL:** confirmar em `db/ddl/001-esquema-reificado.sql` que `media_asset` existe (`nature_label`/`license_profile_ref`/`storage_partition`/`attribution_text`/`textual_equivalent`) e as arestas `representa`/`evidencia` estão utilizáveis. Se ausente → adição de schema (aditiva) antes.
2. **Migração** (`migrate.py`, adição): 5 `media_asset` + 5 arestas `representa` (+`provenance_ref`) + fontes dos assets + **1 claim-sobre-asset** (CMB). Item count **inalterado (40)** — assets são nós, não itens.
3. **Extensão do `011`:** `media[]` no envelope, derivado do autoritativo; reaplicar `020` (grants).
4. **Extensão do frame:** `overlayFields.media` + `overlayMediaHTML` (com fallback textual); cena intocada.
5. **Atualizações de guarda:** `A3-T3` passa a esperar a chave `media`; **`verify.py` T10** atualiza o inventário (novos nós/arestas/fontes/claim) **mantendo `soma_ok` e as demais asserções intactas** (o guardrail protege a invariante, não o inventário — como na Frente A). Fixture de porta pública regenerada.
6. **Suíte nova `MEDIA-T1…5`:**
   - **T1** todo asset tem `nature_label` não-nulo (sem mídia sem rótulo).
   - **T2** `fotografia` **proibido** em Big Bang, Terra e no CMB (CMB = `mapa`/`gráfico`).
   - **T3** cena esquemática: `regimeLabel` inalterado; asset **não** vira textura (ASSET-T/COSMO-T4 verdes).
   - **T4** licença por asset presente; `storage_partition='media-store'`; sem caminho de leitura ao store isolado.
   - **T5** anti-seeded: assets novos, aresta `representa` com proveniência, nenhum embutido/seeded.

## 4. Evidência exigida (PRONTO = EVIDÊNCIA) — a execução só encerra com:

`verify` · `test_a4` · `test_a3` · `test_a3_http` **re-verdes** + `3D-T` · `ASSET-T` · `LIVE-T` · `COSMO-T` **re-verdes** + **`MEDIA-T` 5/5** fechando, em **volume novo** (`docker compose down -v && bash scripts/bootstrap.sh`). Handoff de execução (9 pontos + rodapé) em `docs/passos/`.

## 5. O que a F-A.3 NÃO faz

Não toca a cena procedural · não rotula como foto o que não é observável (Big Bang/Terra/CMB) · não promove seeded · não reescreve o miolo · não cria ClaimSet/tipo/regime/eixo · não religa as 3 sensíveis (host `pending`) · não entra em auth/segredos (**é a E14, a próxima frente**).

---

## Prompt de retomada (sessão de EXECUÇÃO — Claude Code)

> Atlas do Tempo 3D — executar a **F-A.3 (mídia cósmica real)**, com **todos os forks assinados**. Leia `CLAUDE.md`, `docs/passos/plano-cosmicos-midia-real-f-a3-v1_0.md` e este registro (`f-a3-decisoes-assinadas-handoff-execucao-v1_0.md`, **§1 decisões · §2 guardrails · §3 entregáveis · §4 evidência**).
> **Decisões travadas:** técnica=A (envelope estende `media[]`) · cadência=5 de uma vez · CMB reforçado com claim-sobre-asset · Big Bang=`representação-artística` · CMB=`mapa` · galáxias=`fotografia` (deep field, legenda look-back) · sistema solar=`fotografia` (disco análogo, legenda "não o nosso Sol") · Terra=`representação-artística`.
> **Primeiro:** a sub-checagem do DDL (§3.1). Depois, um passo por vez, os entregáveis do §3, **segurando o portão de licença da Etapa 1.1 por asset**.
> **Não** toque a cena esquemática (ASSET-T/COSMO-T4/R-V7/Art.7) · **não** promova seeded · **não** reescreva o miolo · **não** religue as 3 sensíveis (host pending) · **não** entre na E14. Encerre só com a evidência do §4 (re-verde de tudo + `MEDIA-T` 5/5 em volume novo) e o handoff em `docs/passos/`.
