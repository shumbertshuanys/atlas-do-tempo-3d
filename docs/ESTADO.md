# ESTADO — Atlas do Tempo 3D

> Documento vivo (regra R2). Atualizar ao fim de toda sessão que mude o estado.
> Estado mutável mora AQUI — nunca em memória de conversa.
> Última atualização: 2026-07-03 · Chat 1 (governança, claude.ai)

## Fase

MVP enxuto pós re-centragem. Tese em prova: núcleo epistêmico + experiência 3D com
a função central "O que acontecia no mundo neste momento?". Camadas educacionais
(BNCC, planejamento, matching, saída pedagógica) CONGELADAS até demanda validada.

## Construído e verificado

- **Banco:** Postgres 16 + PostGIS 3.4 (docker-compose). Esquema reificado em
  `db/ddl/001-esquema-reificado.sql` — 13 tabelas; invariantes como CHECK/FK reais:
  [N1] aresta afirmativa exige `provenance_ref`; [N2] cache derivado nunca carrega
  proveniência; paleoposição ⇒ reconstrução; `claim.provenance_ref` NOT NULL + FK.
- **Gating por construção:** `core.v_publishable_public`
  (approved ∩ corpus ∩ fonte-por-asset confirmada) + funções gateadas de
  simultaneidade (`f_simultaneidade_publica/_curatorial`) + envelope `MomentResult`.
- **Carga:** 40 itens · 3 ClaimSets (`kpg-causa`, `goe-ritmo`, `rev-francesa`) ·
  7 relações · 3 cenas: 1789 · GOE ~2,4 Ga · K-Pg ~66 Ma. Zero `seeded-demo` no banco.
- **Testes:** `verify.py` (T1–T10), `test_a3`, `test_a3_http`, `test_a4` — verdes na
  última execução local (reports versionados estão DESATUALIZADOS; ver dívida 1).
- **API só-leitura** (`service/atlas_api.py`, papéis por grant) e **frame 3D**
  (`frame/`, modelo puro `atlas-model.js` com testes próprios).

## Dívidas conhecidas (ordem de ataque)

1. **Evidência versionada desatualizada:** `db/reports/*.json` e `README.md` dizem
   35 itens / 8 seeded-demo; o `migrate.py` atual carrega 40 / 0. Reconciliar e
   commitar juntos (R6). → Chat 2
2. **Histórico git = 1 commit-monstro** ("Snapshot..."). Adotar R5/R6 daqui em
   diante; não reescrever o passado. → Chat 2
3. **`seeded-demo` residual no frame HTML** (banco limpo; frame não): modelar de
   verdade ou remover do frame que embarca. → Chat 2
4. **CLAUDE.md** ainda reflete o playbook revogado e diverge do espelho no projeto
   claude.ai: gravar R1–R8, enxugar, ressincronizar espelho (R8). → Chat 2
5. **Fila de claimsets sensíveis** pendente de revisão humana (Tier 0):
   `docs/fila-revisao-claimsets-sensiveis.md`. → antes de qualquer publicação
6. **Demanda: zero conversas com professores até hoje.** Maior risco do produto
   inteiro. → Chat 3 (pode correr em paralelo aos chats 4–5)

## Prioridades

(a) validar demanda com 5 professores reais (História/Geografia, pública e privada);
(b) laço de ingestão assistida por IA com revisão tierizada — medir itens/hora
    de revisão humana (o número decide a economia do produto);
(c) fatia vertical Brasil profunda e bonita no frame 3D
    (eixo 1500 · 1789 · 1822 · 1888 · 1914 · 1945 + simultaneidade mundial).

## Próxima missão

**Chat 2 — Higiene de evidência do repo** (Claude Code): reconciliar
código↔reports↔README; gravar R1–R8 no CLAUDE.md revogando o playbook; resolver
`seeded-demo` do frame. Pronto = 4 suítes verdes commitadas junto com o código.

## Plano de chats

| # | Missão | Onde | Status |
|---|--------|------|--------|
| 1 | Governança e limpeza (instruções v2.1, vivos, arquivamento) | claude.ai → Claude Code | EM CURSO |
| 2 | Higiene de evidência do repo | Claude Code | PRÓXIMO |
| 3 | Roteiro de validação com professores | claude.ai (execução: mundo real) | — |
| 4 | Espec do laço de ingestão assistida (Tier 0/1) | claude.ai | — |
| 5 | Implementação do laço v0 + medição itens/hora | Claude Code | — |
| 6 | Fatia vertical Brasil (curadoria + fontes A) | claude.ai | — |
| 7 | Ingestão da fatia + frame + aula-piloto | Claude Code | — |
