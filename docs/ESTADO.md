# ESTADO — Atlas do Tempo 3D

> Documento vivo (regra R2). Atualizar ao fim de toda sessão que mude o estado.
> Estado mutável mora AQUI — nunca em memória de conversa.
> Última atualização: 2026-07-07 · Chat 3 (kit de validação entregue, claude.ai;
> execução das 5 conversas em curso no mundo real)

## Fase

MVP enxuto pós re-centragem. Tese em prova: núcleo epistêmico + experiência 3D com
a função central "O que acontecia no mundo neste momento?". Camadas educacionais
(BNCC, planejamento, matching, saída pedagógica) CONGELADAS até demanda validada.

## Construído e verificado

- **Banco:** Postgres 16 + PostGIS 3.4 (docker-compose, volume `atlas-pgdata`).
  Esquema reificado em `db/ddl/001-esquema-reificado.sql` — invariantes como
  CHECK/FK reais ([N1] proveniência obrigatória; cache derivado sem proveniência;
  paleoposição ⇒ reconstrução).
- **Carga real (migration_report.json):** **40 itens** (32 corpus + **8 `seeded-demo`
  gateados** — nunca públicos, por construção) · **47 claims** · 3 ClaimSets
  (`kpg-causa`, `goe-ritmo`, `rev-francesa`) · 7 membros · 21 fontes ·
  **16 públicos** · 3 cenas: 1789 · GOE ~2,4 Ga · K-Pg ~66 Ma.
  *Correção sobre a versão anterior deste documento: a afirmação "zero
  seeded-demo no banco" era falsa — os 8 seeded existem e são gateados; o
  invariante que importa (seeded nunca vaza ao público) está provado (T5/A4).*
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

## Evidência (verificada em 2026-07-03, volume novo: `down -v` + bootstrap)

| Suíte | Resultado |
|---|---|
| `verify.py` (T1–T10) | ✅ 10/10 |
| `test_a4.py` (A4-T1..T10; total público no eixo = 16) | ✅ 10/10 |
| `test_a3.py` (A3-T1..T10) | ✅ 10/10 |
| `test_a3_http.py` (A3-HTTP-1..5) | ✅ 5/5 |
| Frame (node): 3D-T · ASSET-T · LIVE-T · COSMO-T | ✅ 5/5 · 3/3 · 4/4 · 5/5 |

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

1. **Fila de claimsets sensíveis** pendente de revisão humana (Tier 0):
   `docs/fila-revisao-claimsets-sensiveis.md` — 3 ClaimSets (`direitos-limites`,
   `inconfidencia`, `escravidao-central`) aguardam host sair de `pending`.
   → antes de qualquer publicação; não religar ao vivo antes disso.
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
(b) laço de ingestão assistida por IA com revisão tierizada — medir itens/hora
    de revisão humana (o número decide a economia do produto);
(c) fatia vertical Brasil profunda e bonita no frame 3D
    (eixo 1500 · 1789 · 1822 · 1888 · 1914 · 1945 + simultaneidade mundial).

## Próxima missão

**Chat 4 — Spec do laço de ingestão assistida (Tier 0/1)** (claude.ai;
decisão/desenho, sem código). Especificar o laço em que IA rascunha (fontes
candidatas, claims tipados, correspondência moderna) e humano revisa — Tier 0
pleno, Tier 1 amostragem — sempre entrando como `pending` (D-20260703-03).
Produto: spec enxuto pronto para commit que destrave o Chat 5 (implementação
v0 + **medição de itens/hora**, o número que decide a economia do produto).
Guardrails: R7 (spec não vira tomo); IA nunca escreve claim/source/reviewStatus.
Em paralelo, fora do chat: as 5 conversas do kit (dono, mundo real).

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
| 4 | Espec do laço de ingestão assistida (Tier 0/1) | claude.ai | PRÓXIMO |
| 5 | Implementação do laço v0 + medição itens/hora | Claude Code | — |
| 6 | Fatia vertical Brasil (curadoria + fontes A) | claude.ai | — |
| 7 | Ingestão da fatia + frame + aula-piloto | Claude Code | — |
