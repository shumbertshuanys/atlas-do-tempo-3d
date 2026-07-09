# ESTADO — Atlas do Tempo 3D

> Documento vivo (regra R2). Atualizar ao fim de toda sessão que mude o estado.
> Estado mutável mora AQUI — nunca em memória de conversa.
> Última atualização: 2026-07-09 · Chat 5 FECHADO (rodada 1 de medição do laço:
> revisão cronometrada + promoção pelo dono, re-verde com pinos novos, número
> medido em D-20260709-01; conversas de validação seguem em curso no mundo real)

## Fase

MVP enxuto pós re-centragem. Tese em prova: núcleo epistêmico + experiência 3D com
a função central "O que acontecia no mundo neste momento?". Camadas educacionais
(BNCC, planejamento, matching, saída pedagógica) CONGELADAS até demanda validada.

## Construído e verificado

- **Banco:** Postgres 16 + PostGIS 3.4 (docker-compose, volume `atlas-pgdata`).
  Esquema reificado em `db/ddl/001-esquema-reificado.sql` — invariantes como
  CHECK/FK reais ([N1] proveniência obrigatória; cache derivado sem proveniência;
  paleoposição ⇒ reconstrução).
- **Carga real (migration_report.json):** **54 itens** (46 corpus + **8 `seeded-demo`
  gateados** — nunca públicos, por construção) · **61 claims** · 3 ClaimSets
  (`kpg-causa`, `goe-ritmo`, `rev-francesa`) · 7 membros · 35 fontes ·
  **27 públicos** · **14 promovidos pelo laço** (11 T1 approved + 3 T0 pending) ·
  cenas: 1789 · GOE ~2,4 Ga · K-Pg ~66 Ma + faixa 1866–1927 (lote-medicao-01) +
  fatia Brasil sensível (1835/1888/1910, pending).
  *Nota histórica: a afirmação "zero seeded-demo no banco" era falsa — os 8
  seeded existem e são gateados; o invariante que importa (seeded nunca vaza ao
  público) está provado (T5/A4).*
- **Gating por construção:** `core.v_publishable_public` + funções gateadas
  (`f_simultaneidade_publica/_curatorial`) + envelope `MomentResult`
  (`f_momento_publico/_curatorial`), portão por GRANT (papéis
  `atlas_public`/`atlas_curatorial`).
- **API só-leitura** (`service/atlas_api.py`, 2 endpoints, recusa subir sem
  `.env`; 12-factor Opção A) e **frame 3D AO VIVO**: `atlas-3d-frame-v1.html`
  consome `/momento/publico` via `fromEnvelope` (papel `atlas_public`);
  comutador de fonte array⇄API; fallback honesto ao espelho estático se a API
  cair; face curatorial só localhost + token.
- **Frente A — cósmicos como corpus COM fonte: FEITA (jul/2026).** 5 âncoras
  (`evt:big-bang`, `state:cmb-recombinacao`, `proc:formacao-galaxias`,
  `evt:formacao-sistema-solar`, `proc:formacao-terra`) como corpus/approved/
  públicos, `sourceTimeBasis=Ga`, sem geometria, com fonte ([N1]); nenhum é
  `fato-documentado`; sem ClaimSet. O estágio cósmico deixou de vir vazio na
  porta pública. Detalhe: `docs/arquivo/passos/registro-execucao-cosmicos-frente-a.md`.
- **Laço de ingestão assistida — v0 IMPLEMENTADO (Chat 5, jul/2026).** CLI
  `ingestao/laco.py` (6 comandos: rascunhar · validar · triar · lote · revisar ·
  promover · medir) + módulos puros (vocab espelha o DDL · validação §4 · triagem
  §5 · manifesto append-only · medição · promoção git-primeiro). Suíte
  `ingestao/tests/test_laco.py` **14/14**, incl. os dois testes negativos (§10.4).
  Promoção materializa `ingestao/carga-promovida.jsonl`, consumido **aditivo e
  dormente** por `migrate.py` (zero mudança em `db/ddl/`/`db/read-layer/`).
- **Rodada 1 de medição — FECHADA (2026-07-09, D-20260709-01).** O dono revisou
  cronometrado os 14 pacotes, aprovou `lote-medicao-01` e promoveu: 11 T1 →
  `approved`/públicos; 3 T0 (`mediado`) → `pending` + fila viva. **Número-decisor:
  T1 = 0,02 min/item (TETO — amostra 100%, sem amortização); T0 = 0,26 min/item
  média (custo PARCIAL — papéis P14 não executados). Taxa de defeito: 0/14.**
  Rótulos normativos em D-20260709-01 (o JSON de medição não os carrega).

## Evidência (verificada em 2026-07-09)

Banco reconstruído do git: `DROP SCHEMA core/derived/iso CASCADE` + `bootstrap.sh`
(o `down -v` do volume é ato do humano — negado ao agente pelo harness; conteúdo
equivalente, pois o banco é 100% derivado do git, R1).

| Suíte | Resultado |
|---|---|
| `verify.py` (T1–T10) | ✅ 10/10 |
| `test_a4.py` (A4-T1..T10; total público no eixo = 27) | ✅ 10/10 |
| `test_a3.py` (A3-T1..T10) | ✅ 10/10 |
| `test_a3_http.py` (A3-HTTP-1..5) | ✅ 5/5 |
| Frame (node): 3D-T · ASSET-T · LIVE-T · COSMO-T | ✅ 5/5 · 3/3 · 4/4 · 5/5 |
| `ingestao/tests/test_laco.py` (LACO-T1..T12, +2 sub) — Chat 5 | ✅ 14/14 |

Reports versionados em `db/reports/` regenerados desta execução (R6).

**Seeded no frame (verificação Chat 2):** o espelho estático em
`frame/atlas-model.js` embarca **4** itens `seeded-demo` (`chem:lavoisier-traite-1789`,
`phys:terra-orbita-1789`, `geo:andes-1789`, `life:grande-auk-1789`) — **subconjunto
dos 8 do banco**, mesmos IDs e selos, visíveis apenas com o gate curatorial ON.
No HTML do frame o restante é só UI do gate/selos. **Não há conteúdo seeded
órfão no frame**; nada foi removido, porque remover criaria divergência
frame↔corpus (o banco mantém os 8). Decidir o destino dos 8 seeded (modelar
com fonte ou remover da carga) é tarefa de modelagem futura, do dono.

## Dívidas conhecidas (ordem de ataque)

1. **Fila de sensíveis** pendente de revisão humana (Tier 0):
   `docs/fila-revisao-claimsets-sensiveis.md` — 3 ClaimSets (`direitos-limites`,
   `inconfidencia`, `escravidao-central`) aguardam host sair de `pending`, **+ 3
   itens T0 da rodada 1 do laço** (`pkg-t0-males`, `pkg-t0-chibata`,
   `pkg-t0-lei-aurea`, PG5 `mediado`) aguardando designação dos papéis P14
   (D-20260708-01). → antes de qualquer publicação desses temas.
2. **E14 — segredos Opção B:** gerenciador com rotação/auditoria/RIPD + auth
   real da porta curatorial (hoje token só localhost).
3. **Demanda: em validação (kit do Chat 3 entregue; conversas em execução).**
   Kit em `docs/validacao/` — roteiro de demo na porta pública, guia de
   entrevista, critérios de sinal/invalidação PRÉ-REGISTRADOS (D-20260707-01),
   perfil dos 5, fichas. Segue o maior risco do produto até o veredito, que
   entra como nova entrada no DECISOES com as 5 fichas como evidência (PG1).
   Camadas educacionais continuam congeladas até lá.
4. **8 itens `seeded-demo` na carga** (gateados, nunca públicos): modelar com
   fonte real ou remover — decisão de modelagem do dono (ver verificação acima).

*Dívidas da versão anterior, fechadas: evidência versionada (reconciliada no
Chat 2, commit `teste(evidencia)`); CLAUDE.md desatualizado (R1–R8 gravadas no
Chat 2); "histórico git = 1 commit-monstro" REVOGADA como falso positivo de
clone raso — ver `docs/DECISOES.md` D-20260703-10.*

## Prioridades

(a) validar demanda com 5 professores reais — **em curso** (kit entregue;
    execução do dono, no mundo real; veredito → DECISOES);
(b) laço de ingestão assistida por IA com revisão tierizada — **v0 rodou ponta
    a ponta e a rodada 1 está medida** (D-20260709-01: T1 = TETO 0,02 min/item;
    T0 = parcial). Próximos gatilhos, cada um por entrada no DECISOES: regime de
    amostragem do próximo lote T1 (50%) e designação dos papéis P14;
(c) fatia vertical Brasil profunda e bonita no frame 3D
    (eixo 1500 · 1789 · 1822 · 1888 · 1914 · 1945 + simultaneidade mundial).

## Próxima missão

**Rodada 1 do laço FECHADA (2026-07-09, D-20260709-01)** — revisão cronometrada,
promoção, fila viva, re-verde com pinos novos e número medido. Nada do Chat 5
está pendente.

**Proposta de próxima missão — Chat 6: fatia vertical Brasil profunda (prioridade c).**
Curadoria com fontes A do eixo 1500 · 1789 · 1822 · 1888 · 1914 · 1945 +
simultaneidade mundial, agora **usando o laço medido** (rascunhar → validar →
triar → lote → revisão do dono → promover). Pré-decisões do dono que destravam
mais valor, cada uma como entrada no DECISOES (não fazer sem entrada):
(i) **designar papéis P14** — sem isso a fatia Brasil sensível (Malês, Chibata,
Lei Áurea, já `pending`) não publica; (ii) **regime de amostragem do próximo
lote T1** (spec §11: 50% na calibração). Em paralelo, fora do chat: as 5
conversas do kit de validação (veredito → DECISOES). **Pendências de higiene:**
R8 (sincronizar espelhos claude.ai) não executável por aqui.

Frente técnica seguinte já **planejada e assinada** (execução pendente):
**F-A.3 — mídia cósmica real** — plano em
`docs/arquivo/passos/plano-cosmicos-midia-real-f-a3-v1_0.md`, decisões assinadas
em `docs/arquivo/passos/f-a3-decisoes-assinadas-handoff-execucao-v1_0.md`
(começa pela sub-checagem read-only do DDL: `media_asset` reificada?
`nature_label`/`license_profile_ref`/`storage_partition` + aresta `representa`?).
Guardrails: cena sempre esquemática (asset só no dossiê, nunca textura);
licença por asset; anti-seeded; suíte nova `MEDIA-T1..5` + re-verde de tudo.

## Plano de chats

| # | Missão | Onde | Status |
|---|--------|------|--------|
| 1 | Governança e limpeza (instruções v2.1, vivos, arquivamento) | claude.ai → Claude Code | ✅ FEITO (2026-07-03) |
| 2 | Higiene de evidência do repo | Claude Code | ✅ FEITO (2026-07-03) |
| 3 | Roteiro de validação com professores | claude.ai (execução: mundo real) | ✅ KIT ENTREGUE (2026-07-07) · conversas em curso |
| 4 | Espec do laço de ingestão assistida (Tier 0/1) | claude.ai | ✅ FEITO (2026-07-07) |
| 5 | Implementação do laço v0 + medição itens/hora | Claude Code | ✅ FEITO (2026-07-09) — rodada 1 medida, D-20260709-01 |
| 6 | Fatia vertical Brasil (curadoria + fontes A) | claude.ai | — |
| 7 | Ingestão da fatia + frame + aula-piloto | Claude Code | — |
