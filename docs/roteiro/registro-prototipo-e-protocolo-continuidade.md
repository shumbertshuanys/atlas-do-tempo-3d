# Registro do protótipo e protocolo de continuidade

**Natureza:** documento-âncora para colocar no **conhecimento do projeto**. Garante que, ao dividir os próximos passos entre chats, nada se perca. Complementa o `estado-atual-e-roteiro.md` (o índice) e segue a cadência de handoff do corpus (Etapas 4Z, 5Z).

---

## 1. Registro do protótipo (em vez do código cru)

**Arquivos (vivem fora do conhecimento do projeto, como anexos/downloads):**
`atlas-prototipo-3d.html` (principal) · `atlas-mvp-incremento-1.html` · `atlas-1789-fatia-vertical.html`.

**O que o protótipo prova (a alma do produto):**
- **Esqueleto = tempo → lente de domínio → eventos do domínio.** A lente filtra *dentro* do instante; nunca troca de instante. **Lente vazia é informação** (ex.: história em 2,4 Ga = "não havia humanidade").
- **Todo instante é atravessado por todas as lentes.** 1789 responde em história/química/física/geologia/vida; GOE (2,4 Ga) em química/vida/clima/geologia; K-Pg (66 Ma) em geologia/vida/química/clima.
- **Cosmos navegável multiescala:** o palco 3D troca de estágio no eixo do tempo (cosmos/galáxias no tempo profundo ↔ Terra no regime histórico), com a troca em ~4,54 Ga (formação da Terra).
- **Espinha epistêmica em qualquer escala:** cada item tem `claimType` (fato documentado, interpretação, inferência científica, proxy, reconstrução modelada, estimativa, hipótese), fonte, e "como sabemos" — inclusive "como sabemos sem documentos" no tempo profundo (S-MIF, BIFs, irídio).
- **Gating operando numa vista única:** o que é sensível ou incerto aparece **mediado** ("em revisão"), nunca como fato. ClaimSets exibem leituras concorrentes com pesos e a regra de **não-falsa-equivalência** (ex.: `k-pg-causa` — impacto central, Deccan contribuinte).

**Status:** **rascunho fechado.** Roda no sandbox (three.js antigo), visual estilizado. **Não** será mais iterado aqui — sua evolução é a **produção no Claude Code** (passo A3).

**Ressalvas honestas (para não confundir com o corpus):**
- Os itens de química/física/geologia/vida de **1789** são **semeados** para demonstração — **não** estão no corpus (a 4D é só história). Conteúdo multidomínio real é tarefa de modelagem (pendências F1/F2).
- Os itens de **GOE e K-Pg** são **fiéis ao 4E/4G** (conteúdo do corpus), com o gating refletindo a revisão científica (núcleo publicável; incerto mediado).
- O globo das cenas profundas mostra **geografia esquemática**, não paleogeografia real — isso é trabalho de produção.

---

## 2. O que salvar no conhecimento do projeto

| Documento | Ação |
|---|---|
| `estado-atual-e-roteiro.md` | **Salvar** (índice/fio condutor) |
| `analise-pendencias-atuais.md` | **Salvar** (mapa de pendências) |
| este `registro-prototipo-e-protocolo-continuidade.md` | **Salvar** |
| `decisao-recentragem-tese-mvp-enxuto.md` | já está no projeto ✅ |
| `revisao-politicas-regras` (P1–P7) | manter à mão — **decisão pendente** de ratificação |
| Protótipos `.html` | **não** colocar no conhecimento — guardar como **arquivo** |

> Regra: o conhecimento do projeto guarda **decisões e contexto duráveis**, não código nem rascunhos.

---

## 3. Plano por chat (um passo por chat)

Cada chat trata **um** passo do roteiro, é **nomeado** por ele, **começa** lendo o `estado-atual-e-roteiro` e **termina** com um doc de handoff curto salvo no projeto.

| Chat | Passo (do roteiro) | Entrega esperada |
|---|---|---|
| **(este)** | A1 — Incremento 2 | ✅ GOE e K-Pg multidomínio no protótipo |
| **Próximo** | **B1 — Motor de banco** | comparativo (RDF* × property graph × relacional) + esquema mínimo do grafo + plano de migração dos dados do protótipo |
| depois | A3 — Produção 3D (Claude Code) | cosmos/galáxias/Terra bem representados; degradação 3D→2D |
| depois | B2 — Reificação | `Source`/`Claim`/`MediaAsset` como tipos de primeira classe |
| em paralelo | C1 — Ratificar P1/P2/P7 | governança fixada (Constituição + Playbook) |
| quando for ao público | C2/C3 | fila de revisão; fonte/licença; jurídico/LGPD |

---

## 4. Regras de continuidade (anti-perda)

- **Mesmo projeto, sempre.** Chats passados ficam pesquisáveis e o conhecimento é compartilhado. Não criar projeto novo.
- **Nomear o chat pelo passo.** Facilita reencontrar.
- **Abrir cada chat** com: "estamos no passo X do `estado-atual-e-roteiro`; contexto no projeto."
- **Fechar cada chat** com um handoff curto (o que foi decidido, o que ficou pendente, próximo passo) salvo no projeto — como os 4Z/5Z do corpus.
- **Arquivos executáveis não atravessam chats sozinhos** — reenviar quando precisar editar.
