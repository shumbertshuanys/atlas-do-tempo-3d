# Encerramento de sessão — virada ao vivo + 3D real · ponte de continuidade

**Data:** jun/2026 · **Estado:** sessão encerrada com a virada **concluída e verde**, árvore limpa.
**Natureza:** nota de continuidade para o lado **claude.ai (planejamento)**. O registro autoritativo de execução é `registro-execucao-a3-virada-3d.md` (no repo); este doc é a camada fina que aponta para ele, lista os fios em aberto, diz o que sincronizar no projeto do claude.ai e traz o prompt de reinício.

> **Regra de ouro (relembrada):** o estado vive nos arquivos commitados, não na conversa. Uma sessão nova se re-hidrata do `CLAUDE.md` + `docs/passos/` + `registro-execucao`. O bootstrap (`down -v && bootstrap.sh`) reconstrói os quatro verdes do banco; os testes de frame são `node` à parte.

---

## 1. Estado no encerramento

A virada ao vivo + 3D real está **completa** — os 7 passos do §9 do plano (`passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md`), sob PRONTO = EVIDÊNCIA em cada degrau.

| Suíte | Resultado |
|---|---|
| Banco: `verify` · `test_a4` · `test_a3` · `test_a3_http` | 10/10 · 10/10 · 10/10 · 5/5 |
| Frame (node): `3D-T` · `ASSET-T` · `LIVE-T` | 5/5 · 3/3 · 4/4 |
| `git grep password=atlas` no código | limpo |
| `git status` | limpo (8 commits no master) |

- **Prova ponta-a-ponta:** o frame faz `GET /momento/publico` → `fromEnvelope` → renderiza **Chicxulub vindo do envelope**, não do array. A divergência frame↔corpus se extinguiu **por construção**.
- **Artefatos que provam a virada:** `3D-T1` (overlay §8 idêntico entre modos) · `LIVE-T1`+`LIVE-T2` (público nunca vaza não-fato; gating por host — 1789 = 2 itens, 0 ClaimSets) · `LIVE-T4` (cliente sem segredo curatorial).
- **Invariantes respeitadas:** miolo `db/ddl/`/`010` intocado; `011` **só adição** (`displayPoint`); seeded **não** virou corpus; as 3 sensíveis **não** religadas (host `pending`); §8 vivo em **todo** degrau.

## 2. Decisão arquitetural realizada nesta sessão

`frame/atlas-model.js` (puro, UMD-lite — **Opção 1** do bloqueio do passo 2): `SceneModel` único, `overlayFields` como **fonte única do §8**, `ctOf` **fail-loud**. Os 3 renderizadores + o painel passaram a **desenhar** os produtores — o §8 deixou de ser reconstruído em 4 lugares. Shaders/câmera **intactos** (a promessa cirúrgica foi mantida). O node importa **o mesmo arquivo** que o browser carrega → sem deriva entre o testado e o que roda.

## 3. Notas honestas de escopo (registradas no handoff §8 do repo)

- O frame ao vivo **não refaz fetch a cada quadro** durante o play: usa a última janela; refetch acontece em **scrub/gate**. Aceitável no MVP; registrado.
- `db/roles/020` mantém **senhas-dev de papel casadas pelo `.env`**. A externalização total via gerenciador de segredos é **E14** (Opção B).

## 4. Fios em aberto (parqueados para as próximas sessões — em ordem)

1. **Revisão humana das decisões de reconciliação (loop da regra do projeto).** O agente tomou sozinho três escolhas de reconciliação plano↔realidade — todas **corretas e registradas**, mas ainda **sem a leitura humana**: (a) a normalização de vocabulário virou **identidade** (a descoberta falsificou a tabela §5.2 — o corpus vivo é hifenizado, igual ao frame); (b) `displayPoint` aditivo em `011` (contingência do §6 nº 1, pois o envelope não expunha ponto); (c) refetch só em scrub/gate. **Ação:** ~10 min lendo `registro-execucao-a3-virada-3d.md` + o diff dos 8 commits, para fechar o loop retroativamente. *(Tarefa humana; não precisa de Claude.)* **Status: pendente.**
2. **PR × master.** Recomendação registrada: **seguir no master agora**, abrir `main` protegido + fluxo de PR **no momento em que o frame sair de localhost** (fronteira que a E14 gateia). Duas perguntas em aberto que decidem se a recomendação muda: `main` é branch separado/protegido ou só naming do mesmo tronco? Há (ou virá em breve) colaborador além de você? **Status: parqueado; default = master.**
3. **Cósmicos como corpus, com fonte.** Os teasers `rep:bigbang`/`rep:galaxies`/`rep:sun` **não estão no corpus** → a cena cósmica é procedural rotulada. Próxima frente: **modelá-los como itens de corpus com fonte** (nunca promover seeded). Pede uma passada de descoberta + planejamento. **Status: próxima frente natural.**
4. **Reintegrar as 3 ClaimSets sensíveis.** Bloqueadas no **host sair de `pending`** (fonte por asset). **Não acionável** até o host ser confirmado (Trilha C / fila de revisão). **Status: bloqueado externamente.**
5. **E14 — segredos Opção B + auth real da curatorial.** É o que gateia o frame sair de localhost (e a fronteira do PR/`main`). **Status: etapa futura.**

## 5. O que sincronizar no projeto do claude.ai

> O repo é a **fonte de verdade**; o conhecimento do claude.ai é um **espelho de conveniência** para as sessões de planejamento. Sincronizar mantém o planejamento de amanhã preciso.

**Obrigatório (para o planejamento de amanhã ler o estado certo):**
- **ATUALIZAR `CLAUDE.md`** — o estado-mestre (§4 com a virada concluída; §5 com as próximas frentes). Se só um arquivo for sincronizado, é este.
- **ADICIONAR `registro-execucao-a3-virada-3d.md`** — o registro de execução desta sessão.
- **ADICIONAR `passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md`** — o plano (mantém a trilha de `passo-*` completa).
- **ADICIONAR este `encerramento-sessao-a3-virada-3d-continuidade.md`** — a ponte de continuidade.

**Opcional (mantém o espelho de artefatos coerente; segue a convenção atual de ter o HTML no conhecimento):**
- **ATUALIZAR `atlas-3d-frame-v1.html`** — mudou bastante e agora **depende** de `atlas-model.js`.
- **ADICIONAR `frame/atlas-model.js`** — novo; é o núcleo puro do HTML. Se atualizar o HTML, adicione este junto, senão o espelho fica um meio quebrado.

**Não precisa sincronizar:** código de `db/` (SQL), `service/` (Python), `frame/tests/` (JS) e `.env*`. Hoje não estão no conhecimento do claude.ai e o planejamento **não depende** deles — vivem no repo, e o `CLAUDE.md` + o registro descrevem a estrutura.

## 6. Prompt de reinício (amanhã)

> Para retomar **o planejamento aqui no claude.ai**. Se um plano fechar, a execução vai para o Claude Code (padrão de duas fases).

```
Atlas do Tempo 3D — retomada após a virada ao vivo + 3D real (concluída e verde).
Antes de tudo, leia o estado sincronizado no conhecimento do projeto:
  - CLAUDE.md (pós-virada: §4 com a virada concluída e provada; §5 com as próximas frentes)
  - registro-execucao-a3-virada-3d.md (o que foi feito + as notas honestas de escopo)
  - passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md (o plano que foi executado)
  - encerramento-sessao-a3-virada-3d-continuidade.md (esta ponte: fios em aberto §4)

Estado de partida (não reabrir): virada completa; 8 commits no master; árvore limpa;
verdes — banco 10/10·10/10·10/10·5/5, frame (node) 3D-T 5/5·ASSET-T 3/3·LIVE-T 4/4;
git grep password=atlas limpo. atlas-model.js (puro) é a fonte única do §8.

Retome os fios em aberto, nesta ordem:
  1. A revisão humana das decisões de reconciliação (normalização=identidade, displayPoint em 011,
     refetch só em scrub/gate) foi feita? Se sim, confirme e siga. Se não, é tarefa humana de ~10 min
     (ler o registro + diff) — me lembre disso antes de planejar nova frente.
  2. PR × master: main é branch separado/protegido ou só naming do mesmo tronco? Há (ou virá) colaborador?
     Responda as duas e decidimos (default registrado = seguir no master até a E14).
  3. Escolher a próxima frente a planejar. Candidata natural: COSMICOS COMO CORPUS COM FONTE
     (modelar rep:bigbang/galaxies/sun como itens de corpus, com fonte — nunca promover seeded;
     passada de descoberta + planejamento). Alternativas: começar a planejar a E14 (segredos Opção B +
     auth real da curatorial), ou outra frente que eu indicar. As 3 sensíveis seguem bloqueadas
     no host pending — não acionáveis ainda.

Disciplina: trabalhe em português do Brasil, um passo por vez; isto é PLANEJAMENTO — não escreva código;
ao propor duas abordagens, explique ambas e me deixe escolher; nunca promova seeded a corpus;
não religue as 3 sensíveis enquanto o host estiver pending.
```

---

### Rodapé — o que este encerramento NÃO faz
Não duplica o detalhe do `registro-execucao-a3-virada-3d.md` (esse é o autoritativo). Não reabre a virada nem as decisões D-A3.6/7/8. Não promove seeded a corpus nem religa as 3 sensíveis. Não decide PR×master nem a próxima frente — registra-os como fios em aberto para você decidir na retomada.
