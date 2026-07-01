# Frente A — Registro de execução (cósmicos como corpus COM fonte)

**Versão:** v1.0 · **Data:** jul/2026 · **Natureza:** handoff de execução (9 pontos).
**Plano:** `plano-cosmicos-corpus-com-fonte-v1_0.md` · **Descoberta+tabela:** `nota-descoberta-cosmicos-frente-a.md`.

## 1. O que foi feito
O estágio cósmico deixou de vir **vazio** na porta pública: 5 âncoras (Abordagem 2) entraram no corpus
**com fonte e proveniência**, pelo pipeline já provado (`migrate.py` → `011` → serviço → `fromEnvelope`),
sem tocar o miolo (`db/ddl/`/`010`/`011`) e sem promover `seeded-demo`.

## 2. Escopo entregue (F-A.fork = Abordagem 2)
`evt:big-bang` · `state:cmb-recombinacao` · `proc:formacao-galaxias` · `evt:formacao-sistema-solar` ·
`proc:formacao-terra` (+ aresta-ponte `proc:formacao-terra` —`precede`→ `proc:goe`).

## 3. Tipagem epistêmica (assinada, jul/2026)
Todos **PÚBLICA/is_fact**, `sourceTimeBasis=Ga`, globais (sem geometria). **Nenhum** `fato-documentado`:
CMB = `medição-direta` (alta); demais = `inferência-científica` (galáxias **média** + faixa ampla; os
outros alta). **Sem ClaimSet** cósmico (`etapa-3.1 §10.7`: expansão = claim único; criacionismo não é lado).

## 4. Como fica o banco (adição, invariantes intactas)
Carga **35→40 itens · 42→47 claims · 5→6 relações · 17→21 fontes · 11→16 públicos · 23→28 curatorial**.
`seeded 8 · pending 12 · claimsets 3 · membros 7 · geometrias 14` **inalterados**. `soma_ok`, gating por
construção e [N1] intactos.

## 5. Frame reconciliado
- `CT` ganhou a chave hifenizada `medição-direta` (+ `aproximação-didática`), mantendo aliases com espaço
  — sem o fix, o CMB cairia no fail-loud vermelho (achado da descoberta §2).
- Espelho estático: 3 teasers `rep:*` **sem lastro** → 5 itens reais do corpus (fallback casa a porta viva).
- Fixture `env_publico_cosmico.json` regenerada da porta pública (5 itens, 0 ClaimSets).
- Render **intacto**: `displayPoint` NULL → órbita/global (nunca marcador terrestre); cena esquemática.

## 6. Evidência (PRONTO = EVIDÊNCIA)
- **Banco:** `verify 10/10 · test_a4 10/10 · test_a3 10/10 · test_a3_http 5/5` (volume novo).
- **Frame (node):** `3D-T 5/5 · ASSET-T 3/3 · LIVE-T 4/4 · COSMO-T 5/5`.
- **COSMO-T1** (não-vazio) · **T2** (nunca fato-documentado; tipo no CT sem fail-loud; incerteza nos 3
  degraus) · **T3** (todo com `provenanceRef`, nenhum seeded) · **T4** (`displayPoint` NULL +
  `semLugarTerrestre`; estágio esquemático, sem marcador/foto) · **T5** (zero ClaimSet cósmico).

## 7. Commits (por mudança lógica)
(a) descoberta+tabela assinada · (b) migração cósmica + inventário (`migrate.py`/`verify.py`/`test_a4.py`) ·
(c) reconciliação do frame (`atlas-model.js` + fixture) · (d) `COSMO-T*` + reajuste `ASSET-T2`/`LIVE-T3` ·
(e) `CLAUDE.md` + este handoff.

## 8. Decisões humanas registradas
D1 CMB=`medição-direta`+fix `CT` · D2 galáxias PÚBLICA/média · D3 itens 1/4/5 PÚBLICA/`inferência` alta ·
D4 sem ClaimSet (Hubble adiado) · D5 `fato-documentado` proibido para cósmico.

## 9. Próximo passo sugerido
Enriquecer (opcional): mídia real (JWST/Hubble PD, `natureLabel` correto — F-A.3 adiada) e/ou tensão de
Hubble como controvérsia estreita (host público+fonteado), se a `etapa-3.1` justificar.

---

## Rodapé — o que este passo NÃO faz
- **NÃO** promoveu `seeded-demo` a corpus (os 5 são novos, com fonte; os 8 seeded seguem intactos).
- **NÃO** reescreveu `db/ddl/`/`010`/`011` (adição só em `migrate.py`; `011` não foi tocado — o
  `displayPoint` NULL já existia). **NÃO** estendeu o eixo 3Z nem criou regime novo.
- **NÃO** religou as 3 sensíveis (host `pending`; seguem na fila da Trilha C).
- **NÃO** transformou o estágio cósmico em foto (cena procedural/esquemática, R-V7).
- **NÃO** deu palco a falsa equivalência (sem ClaimSet cósmico; núcleo = claim único com incerteza).
- **NÃO** fixou status epistêmico sem assinatura (tabela assinada antes de modelar).
