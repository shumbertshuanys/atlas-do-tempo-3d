# Passo A3 — Produção 3D · HANDOFF FINAL

> Encerramento do Passo A3 do **Atlas do Tempo 3D** (Trilha A). Formato de handoff
> do Playbook §2 (9 pontos + rodapé "o que NÃO faz"). Ambas as faces concluídas e
> verificadas. Idioma: PT-BR.

---

## 1. Objetivo

Dar a primeira inflexão do projeto para **implementação real**, em duas faces
simultâneas: (a) uma **fundação de dados** em PostgreSQL+PostGIS que carrega os
invariantes constitucionais *na estrutura* (não na boa vontade do código de
aplicação) e migra o protótipo reconciliando corpus × demonstração; e (b) um
**frame 3D de produção** em three.js que torna o eixo do tempo o piloto da
experiência e preserva o piso epistêmico em toda degradação visual.

## 2. Escopo

**Dentro:** DDL reificado (B2) aplicado; IsolatedLicenseStore físico; migração
Fases 1–6 do protótipo; verificação falsificável dos invariantes; frame 3D com
shaders procedurais, câmera dirigida pelo tempo, rótulos epistêmicos, gating e
degradação 3D→2D→estático.

**Fora (herdado, não reaberto):** o motor de banco (B1) e o modelo de reificação
(B2) — herdados como dados. Não se promoveu nenhum item *seeded-demo* a *corpus*.
Não se construiu cosmos AAA finalizado nem pipeline de ingestão em escala (isso é
Trilha B / etapas posteriores).

## 3. Diagnóstico

O protótipo (`atlas-prototipo-3d.html`) misturava, num mesmo plano, itens com
proveniência real (história 1789, GOE, K-Pg) e itens **multidomínio semeados** de
1789 (química/física/geologia/biologia) cujo propósito era *demonstrar a
simultaneidade*, sem fonte validada. Migrar isso ingenuamente fabricaria
autoridade. O diagnóstico central: **a proveniência precisa ser um eixo de
primeira classe na carga**, e os invariantes precisam ser testáveis — não
afirmados. No 3D, o risco simétrico era um "tema escuro bonito" que tratasse
incerteza como decoração; o piso epistêmico tinha de sobreviver inclusive quando
o WebGL é desligado.

## 4. Decisões principais

- **D-A3.1 — Reconciliação de proveniência.** `provenance_status` deriva
  *exclusivamente* de `seeded:true`. Os 8 itens semeados recebem proveniência
  declarada como "demonstração — fonte não validada contra o corpus" (B1 §6 não
  inventa fontes). 27 itens são `corpus`.
- **D-A3.2 — Mapa para o gate Art.6.** Rótulo do protótipo → `review_status`:
  `publicável`→`approved`; `mediado`→`pending`. Neste corpus, **0** em
  `legal-review` (nada toca pessoa viva/regime sensível).
- **D-A3.3 — Assets procedurais.** Sem assets externos; cosmos/galáxia/Terra/
  geologia por **shaders GLSL** (ruído simplex/fbm): plasma do Big Bang que esfria
  na recombinação, nebulosas de emissão, galáxia espiral em braços log, Sol com
  granulação, disco protoplanetário, e **Terra que morfa de fundida→moderna** com
  bandas de ferro (GOE), cicatriz/véu de impacto (K-Pg) e atmosfera fresnel.
- **D-A3.4 — Câmera dirigida pelo tempo.** O eixo `canonicalTimeScalar` (datum 3Z)
  é normalizado em estágios-âncora; o slider pilota a câmera com keyframes e blend
  triangular (Art.1: o tempo é o esqueleto).
- **D-A3.5 — Lente-sobre-instante.** Instante = posição no eixo; lente = filtro de
  domínio. **Lente vazia é informação** ("nada conhecido aqui por estas lentes" é
  exibido, não escondido).
- **D-A3.6 — Rótulo epistêmico onipresente.** Todo item carrega tipo (cor **+
  ícone**, redundância não-cromática) + confiança + **incerteza-como-faixa** (nunca
  um ponto) + atribuição. ClaimSet com pesos assimétricos e nota de
  não-equivalência; negacionismo nunca é "lado"; paleoposição → AnachronismNotice.
- **D-A3.7 — Gating no render.** Só `approved`+`corpus` renderiza como **fato**;
  `seeded-demo` recebe selo "demonstração"; `pending` recebe selo "em revisão". O
  portão filtra a exibição, não os dados.
- **D-A3.8 — Degradação 3D→2D→estático.** Três renderizadores do **mesmo modelo de
  exibição** (fonte única de verdade): WebGL → Canvas2D (mapa equirretangular
  rotulado) → HTML/CSS (lista). O contrato §8 sobrevive aos três; **fallback
  automático** para 2D se faltar WebGL.

## 5. Modelo conceitual

```
                      entity_node  (backbone reificado; 6 entity_kind)
                            │
   ┌──────────┬────────────┼───────────┬─────────────┬───────────┐
 item    relationship    claim     claim_set      source     media_asset
   │       (is_affirm.)  (subj_ref) (membros/peso) (tier A/B)  (partição
   │        +prov_ref?    +prov_ref  +no_equiv.)               por licença)
   │         └─[N1]────────┘                                    └─Art.11→iso
 knowledge_item ── geometry_version (paleo⇒reconstrução; CHECK)
   (datum 3Z completo · review_status · provenance_status)
                            │
        VIEWS de exibição (Art.6 / §9):
        v_displayable_curatorial  ⊇  v_publishable_public
        (approved+admitido)          (approved ∩ corpus ∩ fonte-confirmada)

   Cliente 3D: eixo do tempo → estágios → câmera; visibleItems() = janela
   temporal ∩ lente ∩ gate; um modelo, três renderizadores (3D/2D/estático).
```

## 6. Fontes / insumos

Protótipo `atlas-prototipo-3d.html` (35 itens, 10 ClaimSets, 6 cenas) como insumo
único da carga. Esquema herdado de B1/B2; datum de 3Z; contrato visual de §8/PG6;
portões de Art.6/§9. Fontes de domínio citadas *nos itens* (USGS, PBDB, geociências,
arquivos históricos) entram como `source` com `authority_tier`; itens semeados
entram **sem** tier, com proveniência de demonstração.

## 7. Riscos

- **R-A3.1 — Geometria de tempo profundo é esquemática.** Pontos modernos rotulados
  como reconstrução; paleopolígonos validados (GPlates/EarthByte) são dívida de
  **fidelidade**, não de correção. *Mitigação:* `is_reconstruction=true` forçado por
  CHECK + AnachronismNotice no cliente.
- **R-A3.2 — 8 itens seeded-demo sem fonte.** Risco de vazarem ao público como fato.
  *Mitigação:* excluídos de `v_publishable_public` por construção (provado em T5);
  selo "demonstração" no cliente.
- **R-A3.3 — Frame 3D é "incremento 1", não cosmos final.** A Terra aparece/some por
  corte (o shader não tem `uOpacity`); rótulos do hemisfério traseiro podem
  transparecer; estágios cósmicos são representações, não catálogos de objetos.
  *Mitigação:* honestidade explícita na UI (selo "representação de cena") e neste
  handoff; refino fica para iteração seguinte.
- **R-A3.4 — 11 itens com fonte-por-asset pendente.** Bloqueados no portão público
  até confirmação (§9.2). *Mitigação:* `per_asset_source_confirmed=false` registrado;
  divergência roteada a F2.

## 8. Entregáveis

| arquivo | o que é | estado |
|---|---|---|
| `out/atlas-3d-frame-v1.html` | **frame 3D de produção** (single-file, three.js+GLSL, 3 renderizadores) | ✅ validado |
| `out/ddl-esquema-reificado-bundle.sql` | bundle do esquema (00→05): tabelas, CHECK, triggers, papéis, views | ✅ aplicado |
| `out/verification_report.json` | **10/10** provas falsificáveis dos invariantes | ✅ verde |
| `out/registro-divergencias.md` | 22 divergências (11 fonte-pendente, 8 seeded, 3 geometria) | ✅ |
| `out/migration_report.json` | contadores + divergências da carga | ✅ |
| `out/registro-progresso-a3.md` | registro de progresso detalhado (Faces 1 e 2) | ✅ |
| `migration/{extract.js,migrate.py,verify.py}` | pipeline de migração + verificação | ✅ |

**Verificação (PG1/Art.15 — pronto = artefato falsificável):** 10/10 testes verdes.
[N1] rejeita aresta afirmativa sem proveniência (negativo) e confirma 3 com
proveniência (positivo); Art.6 não vaza pending/legal/rejected (estático) e exclui
um `legal-review` sintético da view embora ele exista na base (dinâmico); §9 exclui
`seeded-demo` do público; Art.11 nega `kc_service` no schema `iso` e rejeita asset
ShareAlike fora do isolated-store; [N2] confirma que `derived_cache` não é nó e não
carrega proveniência; Art.12/§8 rejeita paleoposição não-reconstrução; contagens
batem (35 = 27 corpus + 8 seeded; 39 claims = 35 de item + 4 membros).

## 9. Próximos passos

1. **Trilha B (dados em escala):** sair do protótipo para ingestão real — povoar
   `entity_node`/`knowledge_item` a partir de fontes de autoridade (USGS, PBDB,
   ICS, arquivos), com o gate operando desde o primeiro registro.
2. **Resolver divergências por fase:** F2 confirma fonte-por-asset dos 11 pendentes;
   F1/F2 decide o destino dos 8 seeded (modelar contra corpus ou manter rebaixado);
   F3 substitui pontos de tempo profundo por paleopolígonos validados.
3. **Refino do frame (incremento 2):** `uOpacity` na Terra para transição suave;
   occlusão de rótulos do hemisfério traseiro; LOD de partículas; e ligar o cliente
   às **views reais** do banco (hoje o cliente usa um espelho curado dos mesmos
   dados) por uma camada de leitura sobre `v_displayable_curatorial`.
4. **Função "O que acontecia no mundo?" (Etapa 5):** já há base — `f_simultaneidade`
   no banco e o eixo-instante no cliente; falta unir os dois numa consulta pública
   gateada.

---

### Rodapé — o que o Passo A3 **não** faz

- **Não** reabre o motor de banco (B1) nem a reificação (B2): ambos herdados.
- **Não** promove nenhum item *seeded-demo* a *corpus*, nem inventa fontes para eles.
- **Não** publica nada `pending`/`legal-review`/`rejected` como fato ao público; o
  gating opera por construção (provado, não prometido).
- **Não** entrega um cosmos AAA finalizado: é o **primeiro incremento de produção** do
  frame; as representações cósmicas são ilustrativas e a geometria de tempo profundo
  é esquemática/rotulada.
- **Não** liga (ainda) o cliente 3D às views do banco em tempo real: o frame usa um
  espelho curado dos mesmos dados, consistente com a carga, à espera da camada de
  leitura (próximo passo 3).
- **Não** substitui currículo, BNCC ou o planejamento do professor: continua sendo a
  base universal sobre a qual as camadas pedagógicas se aplicam depois.
