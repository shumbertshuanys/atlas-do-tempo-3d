# Encerramento — Frente A (cósmicos como corpus COM fonte) · continuidade

**Versão:** v1.0
**Data:** jun/2026
**Natureza:** ponte de continuidade (lado de **planejamento**). Fecha a Frente A e prepara a próxima sessão. **Não inicia nova frente** — a escolha da próxima é do humano.
**Complementa:** `docs/passos/registro-execucao-cosmicos-frente-a.md` (log de execução) e `docs/passos/plano-cosmicos-corpus-com-fonte-v1_0.md` (o plano executado).

---

## 1. O que fechou — estado provado (não reabrir)

- **Frente A concluída e verde**, banco reconstruído do zero (volume limpo).
- **Carga:** 40 itens · 47 claims · 21 fontes.
- **Suítes:** `verify` 10/10 · `test_a4` 10/10 · `test_a3` 10/10 · `test_a3_http` 5/5 · frame (node) 3D-T 5/5 · ASSET-T 3/3 · LIVE-T 4/4 · **COSMO-T 5/5**.
- **5 âncoras** (Abordagem 2, tabela epistêmica **assinada**): `evt:big-bang` · `state:cmb-recombinacao` · `proc:formacao-galaxias` · `evt:formacao-sistema-solar` · `proc:formacao-terra` — todas em Ga, **sem geometria terrestre** (`displayPoint` NULL), com proveniência (N1). Aresta-ponte `formacao-terra → GOE`.
- **6 commits por mudança lógica**; working tree limpo.

## 2. Invariantes preservadas — a prova, não a promessa

| Invariante | Como se sustentou | Teste que trava |
|---|---|---|
| Nenhum cósmico é fato-documentado | CMB = `medição-direta`; demais `inferência-científica`; galáxias em confiança **média** com faixa ampla | COSMO-T2 |
| Público no tempo cósmico deixou de vir vazio | porta pública retorna os itens com lastro fonteado | COSMO-T1 |
| Zero ClaimSet cósmico (sem falsa equivalência) | `etapa-3.1 §10.7` dispensa; núcleo estabelecido = claim de alta confiança com incerteza | COSMO-T5 |
| Anti-seeded (prova negativa) | os 5 são **novos com fonte**; os 8 seeded **intactos**, nenhum promovido | COSMO-T3 |
| Estágio cósmico esquemático/procedural, nunca foto | `displayPoint` NULL → órbita, sem marcador terrestre | COSMO-T4 |
| Miolo intacto | `db/ddl/` · `010` · `011` **não tocados** — só adição | (re-verde das suítes existentes) |

## 3. Achado que virou fix cirúrgico (aprendizado a carregar)

- **O que era:** `claim_type` flui **cru** ao frame; `medição-direta` (hífen, convenção canônica do corpus, herdada da descoberta da virada) **não casava** a chave `medição direta` (espaço) do CT → erro.
- **Fix:** chave canônica **hifenizada** no CT + **alias de compat**. `COSMO-T2` trava a regressão.
- **Consequência:** a convenção hifenizada é agora **end-to-end** (corpus → envelope → CT do frame), alinhada ao guarda fail-loud do `ctOf` da virada. **Regra para o futuro:** ao adicionar tipo epistêmico novo, usar a forma **hifenizada canônica**.

## 4. Fila de frentes — próxima é escolha do humano (nenhuma iniciada)

- **E14 — segredos Opção B + auth real da curatorial.** A fronteira que gateia o frame **sair de localhost** (e, por tabela, PR/`main`). Prioridade no instante em que o alvo virar **exposição/usuários reais**.
- **Mídia cósmica real (F-A.3, estava adiada).** JWST/Hubble PD, `natureLabel` correto (foto × mapa/gráfico do CMB × reconstrução); estágio segue procedural. **Extensão natural** da Frente A — baixo risco, mesmo pipeline provado.
- **Tensão de Hubble como controvérsia estreita.** Só se a `etapa-3.1` justificar; seria ClaimSet com **pesos assimétricos**, gateando por host. (A Frente A registrou **zero** ClaimSet cósmico por ora.)
- **Backlog de discovery curricular** (`backlog-discovery-curricular-priorizacao-dominios`). Lado **pedagógico**, se quiser pender para aplicação em vez de corpus/infra.
- **Bloqueadas (não acionáveis):** as 3 sensíveis (`direitos-limites` · `inconfidencia` · `escravidao-central`) — host **pending** (Trilha C).

## 5. Sincronização / confirmar

- **Confirmar** que o `CLAUDE.md` reflete: **§4** carga 40 · 47 · 21 e COSMO-T 5/5; **§5** frente nº 1 (cósmicos) → **feita**. O §9 passo 6 previa isso; se o commit `docs` já cobriu, ok — só um check (PRONTO = EVIDÊNCIA vale para o estado, não só para o código).
- **Subir ao conhecimento do claude.ai** (para o próximo planejamento aqui já ver): este encerramento + `registro-execucao-cosmicos-frente-a.md`. Código de `db/` e testes **não** precisam sincronizar (mesma regra de antes).
- **Master local até a E14** (sem push obrigatório; sem colaborador).

---

## Prompt de retomada (próxima sessão de PLANEJAMENTO)

> Atlas do Tempo 3D — retomada após a **Frente A (cósmicos como corpus com fonte)** concluída e verde.
> Leia o estado sincronizado: `CLAUDE.md` (§4 carga 40·47·21, todos os verdes incl. **COSMO-T 5/5**; §5 frente 1 → feita), `docs/passos/registro-execucao-cosmicos-frente-a.md` e este encerramento (**§4 fila de frentes**).
> **Estado de partida (não reabrir):** Frente A completa; miolo intacto (só adição); convenção epistêmica **hifenizada end-to-end** (fix do CT + COSMO-T2); 6 commits; árvore limpa; as 3 sensíveis seguem bloqueadas (host pending).
> **Escolha a próxima frente a planejar:** E14 (segredos Opção B + auth curatorial) · mídia cósmica real (F-A.3) · tensão de Hubble (se a etapa-3.1 justificar) · discovery curricular · ou outra que eu indicar.
> **Disciplina:** PT-BR, um passo por vez, **PLANEJAMENTO — não escrever código**; ao propor duas abordagens, explicar ambas e me deixar escolher; **nunca** promover seeded a corpus; **não** religar as 3 sensíveis enquanto o host estiver pending; **segurar os portões humanos**.
