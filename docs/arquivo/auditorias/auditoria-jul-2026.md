# Auditoria técnica — Atlas do Tempo 3D (julho/2026)

> Registro condensado da auditoria externa (claude.ai, Claude Fable 5, 02–03/jul/2026).
> Escopo: ideia, arquitetura, estrutura de dados, alimentação, LLM/RAG, MVP.
> Insumos: repositório público (clone, commit 3c37714) + 70 documentos de etapa/governança.
> Destino: `docs/arquivo/auditorias/`. Documento histórico — não normativo.

## Vereditos

1. **Ideia:** boa e diferenciada (atlas espaço-temporal com proveniência, incerteza,
   tipagem epistêmica e leitura de simultaneidade). O risco dominante não é técnico:
   é **demanda não validada** — nenhuma conversa com professor real até a data.
2. **Núcleo de dados: preservar intacto.** Verificado no código: invariantes como
   CHECK/FK reais (`n1_affirmative_needs_provenance`, `paleo_is_always_reconstruction`,
   `n2_derived_carries_no_provenance`, `claim.provenance_ref NOT NULL FK`); gating por
   construção (`v_publishable_public` = approved ∩ corpus ∩ fonte-por-asset); teste
   negativo genuíno (T1). Decisão de motor correta (Postgres+PostGIS+JSONB; vetorial
   fora). Carga: 40 itens, 3 ClaimSets, 7 relações — escala de demonstração.
3. **Aparato conceitual: congelar.** 64 arquivos / ~20,1 mil linhas de markdown
   governando ~754 linhas de SQL + ~1,6 mil de Python e 40 itens (~9:1). O processo
   estava consumindo o produto.
4. **Alimentação de dados:** o pipeline de 20 etapas humanas por item é correto como
   piso para conteúdo sensível e inviável como regra universal. Sem tierização +
   ingestão assistida, o projeto fica em escala de maquete permanentemente.

## Achados específicos do repositório

- Evidência versionada desatualizada: reports e README (35 itens / 8 seeded) ≠ código
  (40 / 0); README omite `test_a3`/`test_a3_http` do critério de sucesso.
- Histórico git = 1 commit-monstro, violando a regra da própria casa; trilha de
  evidência vive em prosa, não em commits.
- `seeded-demo` residual no frame HTML (banco limpo).
- Espelho `CLAUDE.md` no projeto claude.ai divergindo 465 linhas do repo.

## Comparação de modelos (A/B/C)

- **A — base pré-curada pura:** epistemicamente perfeita, economicamente morta
  (custo humano por item inviabiliza cobertura).
- **B — LLM/RAG dinâmico em tempo de uso:** descartado. Não garante proveniência,
  gating do sensível, não-falsa-equivalência nem licença; alucinação em produto
  escolar para menores é passivo jurídico.
- **C — híbrido (adotado):** runtime responde só do banco canônico gateado;
  LLM+recuperação atuam na INGESTÃO (rascunho de claims/tipagem/fontes → `pending`
  → revisão humana tierizada: Tier 0 pleno; Tier 1 rascunho de IA + amostragem).
  O banco responde ao aluno; a IA ajuda a construir o banco.

## Riscos (ordem)

1. Demanda não validada. 2. Escala de conteúdo vs. custo de curadoria.
3. Economia (nenhum número comercial existe). 4. Jurídico em escala (licença por
asset, LGPD de menores). 5. Processo virar produto (recorrência). 6. 3D como
sorvedouro de escopo — o 3D serve o conteúdo, nunca o contrário.

## Recomendações que viraram decisão

Congelar Etapas 0–15; regras R1–R8; instruções v2.1 no projeto claude.ai;
consolidação em 4 documentos vivos + `docs/arquivo/`; reconciliar evidência do
repo; laço de ingestão assistida com medição de itens/hora; fatia vertical Brasil
(1500 · 1789 · 1822 · 1888 · 1914 · 1945 + simultaneidade); validação com 5
professores antes de reabrir camadas educacionais.
Ver `docs/DECISOES.md`, entradas D-20260702-01 a D-20260703-05.
