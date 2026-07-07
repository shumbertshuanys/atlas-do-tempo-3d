# Kit de validação de demanda — professores reais (Chat 3)

> Instrumento de campo. **Não é documento conceitual, etapa, playbook nem handoff** —
> é material operacional de validação, pedido explícito do dono (não fere R7).
> A execução das conversas é do dono, no mundo real. Este kit só prepara e padroniza.
>
> **Objetivo único:** medir se existe demanda real de professor pela **função central**
> ("o que acontecia no mundo neste momento?") e decidir, com evidência, se as camadas
> educacionais congeladas (Etapas 6–9) devem ou **não** reabrir. Ver o critério de
> invalidação (§3) — ele é o mais importante e o mais fácil de trair.
>
> **Regra de ouro do projeto aplicada aqui:** na dúvida, **não reabre**. Elogio não é
> demanda. Um piloto marcado vale mais que dez "que legal".

---

## 1. Roteiro de demonstração — 10 minutos, no frame que já roda

O frame de produção (`frame/atlas-3d-frame-v1.html`) é o único artefato mostrável hoje.
A demo prova a **tese** (base universal + simultaneidade + honestidade epistêmica),
não o produto acabado. Nada de camada educacional aparece — porque não existe.

### 1.0 Pré-checagem técnica (5 min antes, na máquina do dono)

- `bash scripts/bootstrap.sh` verde; subir `python service/atlas_api.py` (bind
  `127.0.0.1:8765`, recusa sem `.env`).
- Abrir o frame; confirmar rodapé **"FONTE: API · pública"**. Se a API cair, o frame
  degrada sozinho ao espelho estático — degradação honesta, pode deixar acontecer.
- Rodar uma vez os cliques do roteiro. Ter o eixo do tempo já na cena cósmica.
- **Só se for usar o Caminho B (§1.2):** exportar `ATLAS_CURATORIAL_TOKEN` e
  `window.ATLAS_CURATORIAL_TOKEN` em localhost. Sem token/localhost o frame **recusa**
  a face curatorial e volta à pública (é o comportamento correto — não force).

### 1.1 O que a porta pública realmente mostra (não prometer além disto)

Verificado no código (`atlas-model.js` / envelope gateado). Na **porta pública** só
circula `corpus ∩ approved`:

| Cena | Aparece na porta pública (fato, com fonte) | **Não** aparece na pública (gated) |
|---|---|---|
| Cósmica (~13,8 Ga → 4,5 Ga) | Big Bang, CMB, formação de galáxias, Sistema Solar, acreção da Terra (5) | — |
| GOE (~2,4 Ga) | GOE, fotossíntese oxigênica, BIF (3) | atmosfera pré-GOE (`pending`) |
| K-Pg (~66 Ma) | Chicxulub, extinção K-Pg, anomalia de irídio (3) | vulcanismo Deccan (`pending`, hipótese) |
| **1789** | **Estados Gerais, Queda da Bastilha (só 2)** | Declaração de Direitos, tráfico atlântico, Inconfidência (`pending`); Lavoisier, Andes, arau-gigante (`seeded-demo`) |

**Consequência que dita o roteiro:** as cenas profundas são densas e carregam a demo.
A cena 1789 na porta pública é magra (2 pontos franceses) — porque o Brasil de 1789 e
os temas sensíveis estão, por construção, na fila de curadoria humana Tier 0. Isso não é
um bug a esconder: é o diferencial a mostrar (ver §1.2, Caminho B).

### 1.2 Decisão de operação da demo — dois caminhos (o dono escolhe)

O produto tem duas faces reais no frame. **Escolha uma antes da conversa. Nunca ligar
"demonstração (seeded)" com um professor** — são itens de fonte não validada, não
representam o produto e confundem o julgamento.

- **Caminho A — porta pública pura (gates OFF). Recomendado como padrão.**
  É a experiência real (o que um aluno veria). Funciona em qualquer máquina, inclusive
  vídeo com tela compartilhada. Custo: 1789 mostra só 2 itens franceses — então em 1789
  você usa a honestidade como fala (ver minuto 5:00). Zero risco de confundir selos.

- **Caminho B — face curatorial só com "em revisão" (pending) ligado. Local, com token.**
  Liga só o toggle *em revisão* (jamais *demonstração*). Aí Inconfidência, tráfico e
  Declaração **aparecem com selo "em revisão"** e o aviso "não circula como fato até
  aprovação". Use isto para o momento mais forte da demo: mostrar que o atlas **se recusa
  a entregar leitura historiográfica sensível sem curadoria**. Exige rodar na máquina do
  dono (localhost + token) — não serve para link enviado. Risco: explicar bem que
  "em revisão" ≠ "inventado"; o item é corpus real aguardando revisão humana.

> Regra fixa dos dois caminhos: **não-fato nunca é mostrado *como* fato**; os selos
> ("público", "em revisão", "seeded") persistem em todos os modos (Constituição, Art. 6).

### 1.3 Roteiro minuto a minuto

**0:00–0:30 — Enquadramento honesto (desarma a gentileza).**
"Vou te mostrar um protótipo de atlas do tempo. Não é produto pronto: não tem plano de
aula, não tem alinhamento à BNCC, não foi usado com alunos. Quero sua reação crua, de
professor — inclusive as críticas." (Sem isto, o professor tende a elogiar por educação e
o sinal se contamina.)

**0:30–2:30 — A tese em movimento (deixe ver, não explique arquitetura).**
Abra na cena cósmica e arraste a linha do tempo do Big Bang até 1789. Ponto a passar:
é **um eixo contínuo** de bilhões de anos até uma data histórica; cada item tem **tipo
epistêmico** com cor + ícone. Não fale de banco, FK, gating. Deixe a continuidade falar.

**2:30–5:00 — A função central + honestidade epistêmica (o diferencial).**
Pare numa cena densa (K-Pg é a mais forte). Clique num item e abra o dossiê: mostre
**claim + tipo + fonte + faixa de incerteza**. Frase: "repare que ele não afirma como
fato o que é inferência, e mostra de onde veio." Depois abra o **ClaimSet `kpg-causa`**:
Chicxulub (peso 0,82) × vulcanismo Deccan (0,30). Frase: "controvérsia legítima aparece
como leituras com **peso desigual**, não como 'dois lados iguais' — e que houve extinção
não está em disputa." Esse é o coração do que diferencia o produto.

**5:00–7:30 — O momento histórico (1789).**
Vá à cena 1789. Mostre Estados Gerais + Bastilha (fato documentado, fonte A).
- *Caminho A:* "no mesmo instante, o atlas te dá o eixo do mundo; itens de outros
  domínios entram aqui à medida que passam por curadoria. Hoje, na porta pública, são
  esses dois — o Brasil de 1789 está no acervo, mas em revisão."
- *Caminho B:* ligue *em revisão*, clique em **Inconfidência** e **tráfico atlântico**;
  mostre o selo e o aviso. Frase: "o Brasil de 1789 está aqui — Inconfidência, tráfico,
  escravidão — mas o atlas se recusa a te entregar isso como fato pronto sem revisão
  humana. Isso é de propósito."
Faça já aqui, informalmente, a ponte para a entrevista: "isso — o mundo inteiro num
instante — te seria útil? como?" (não force resposta positiva).

**7:30–9:00 — Incerteza como recurso pedagógico.**
Mostre uma reconstrução rotulada (ex.: atmosfera pré-GOE / paleoposição) com o selo
"reconstrução modelada / incerteza" persistindo. Frase: "para ensinar que ciência tem
incerteza, ele nunca finge precisão." Pergunte se isso ressoa com o que ele enfrenta
(aluno que acha que "ciência = verdade pronta").

**9:00–10:00 — Fechar abrindo a entrevista.**
"Isso é o que existe hoje. O que você imagina fazendo com isso numa aula — ou por que
não usaria? E o que faltaria pra você usar de verdade?" → emenda no Bloco 2 do guia.

### 1.4 O que **NÃO** prometer nem dizer (lista de contenção)

- Não dizer que tem **plano de aula** ou **alinhamento à BNCC** — congelado, não existe.
- Não dizer que **gera atividades, trilhas ou avaliações** — não existe.
- Não dizer que **cobre o currículo** — são 3 cenas + eixo cósmico; é demonstração.
- Não dizer que **já está em escola / testado com alunos** — não está.
- Não ligar **"demonstração (seeded)"** — fonte não validada; não é o produto.
- Não prometer **prazo, preço ou acesso**. Se perguntarem, isso é **sinal** (anote — §3).
- Não induzir ("você ia amar isso, né?"). Pergunta aberta sempre.

---

## 2. Guia de entrevista semiestruturada (~10 perguntas)

**Método (estilo "Mom Test"):** pergunte sobre a **vida e o comportamento atual**, não
sobre a ideia; **abertas primeiro**, produto por último; nunca faça pitch dentro da
pergunta; busque **fatos passados**, não previsões ("na sua última aula sobre X, o que
você fez?" vale mais que "você usaria?"). Anote o que ele diz, não o que você quer ouvir.

A ordem importa: **Bloco 1 antes da demo** (para a dor não vir contaminada pelo produto);
demo; **Bloco 2 depois**. 30–40 min no total.

### Bloco 1 — antes de mostrar qualquer coisa (rotina + dor real)

1. Me conta a última aula que você preparou sobre um tema de história/geografia mundial —
   do começo ao fim, o que você fez? *(comportamento concreto, não opinião)*
2. Onde você busca material quando prepara uma aula dessas? *(fontes reais — livro, mapa,
   vídeo, atlas, IA?)*
3. Nessa preparação, o que mais te consome tempo ou te irrita? *(dor, sem sugerir solução)*
4. Quando você quer que os alunos entendam que coisas aconteciam **ao mesmo tempo** em
   lugares diferentes — tipo o que havia no Brasil quando caiu a Bastilha — como você faz
   isso hoje? *(a dor específica que o produto ataca, perguntada sem citar o produto)*
5. Já tentou alguma ferramenta digital pra isso? Qual, e por que parou — ou continuou?
   *(histórico de comportamento e concorrência real)*

### Bloco 2 — depois da demo (reação + uso + disposição)

6. Sem filtro: o que passou pela sua cabeça vendo isso? *(reação crua e aberta)*
7. Tem algo aqui que resolveria um problema **seu**, real? Se sim, qual exatamente?
   *(precisa reconectar à dor do Bloco 1; se ele não conectar sozinho, é sinal fraco)*
8. Se você tivesse isso amanhã, em que momento de qual aula usaria — ou não usaria?
   *(uso concreto imaginado; aceitar "não usaria" como resposta legítima)*
9. O que precisaria existir para você levar isto a uma turma de verdade? *(aqui as camadas
   congeladas podem emergir como demanda **puxada** — anote QUAL camada, ver ficha §5)*
10. Como é, na sua escola, a decisão de adotar uma ferramenta assim — quem decide, tem
    verba, você pagaria do próprio bolso ou a escola paga? *(disposição a adotar/pagar
    ancorada no processo real, sem ancorar um valor — o projeto não tem número comercial)*

**Fechamento (não é pergunta-produto, é medida de sinal):** "Posso te procurar quando
tiver mais? Conhece alguém que deveria ver isso?" → mede indicação espontânea.

### Condução (colar na cabeça antes da conversa)

- Silêncio é bom — deixe o professor preencher. Não resgate a pausa.
- "Por quê?" até três vezes; a terceira costuma revelar a dor de verdade.
- Se ele criticar o produto, **não defenda** — anote a crítica; ela é o ouro.
- Distinga **elogio** ("que legal!") de **compromisso** ("me manda quando abrir",
  "topo testar dia 12"). Só o segundo conta como sinal (§3).

---

## 3. Critérios objetivos de sinal + invalidação honesta

Pré-registrados **antes** das conversas (anti-Goodhart; coerente com PG1 = evidência).
Contam **comportamento com custo**, não simpatia.

### 3.1 Sinais FORTES (compromisso do professor)
- Pediu acesso / quer usar de novo — espontâneo.
- Topou **aula-piloto** com data e turma concretas.
- **Indicou colega específico** (deu nome/contato).
- Ofereceu tempo futuro (reunião, testar com alunos).
- Perguntou **preço / como assinar** por conta própria.
- Conectou a demo a uma **dor real e específica dele** (não genérica).

### 3.2 Sinais FRACOS (não contam como validação)
- Elogio genérico ("bonito", "inovador", "que legal").
- "Faz sentido", "tem mercado" — sem compromisso próprio.
- Entusiasmo condicionado a features inexistentes, sem topar testar o que existe.
- Educado, mas nenhum próximo passo aceito.

### 3.3 Dois vereditos independentes (não confundir)
1. **Tese / função central** (o atlas + simultaneidade + honestidade epistêmica): ressoa?
2. **Camadas educacionais congeladas** (Etapas 6–9): há demanda específica por alguma?

A tese pode ressoar **sem** que nenhuma camada se justifique ainda. Nesse caso o sinal
valida seguir na **fatia vertical Brasil + laço de ingestão** — **não** reabrir Etapas 6–9.

### 3.4 Regra de decisão sobre as camadas (limiar proposto — a ratificar)

Sobre 5 conversas. Os números abaixo são **proposta do papel de estrategista**, não
verdade revelada — ratifique ou ajuste antes de ir a campo.

- **Reabrir camadas educacionais (verde parcial):** ≥ **3 de 5** professores com ≥ 1
  sinal forte cada **E** ≥ **2** deles apontando a **mesma** camada congelada em "o que
  falta" (ex.: dois dizem "preciso do plano alinhado à BNCC"). **Convergência** pesa mais
  que entusiasmo disperso — sem alvo comum não há o que construir.
- **Continuar investigando (amarelo):** 1–2 sinais fortes, ou fortes sem convergência de
  camada → mais 5 conversas antes de decidir. Não reabre ainda.
- **NÃO reabrir — invalidação honesta:** basta **qualquer** um destes nas 5 conversas →
  camadas ficam congeladas:
  - 0–1 sinal forte no total; ou
  - nenhuma dor real conectada à função central (não reconhecem o problema); ou
  - "o que falta" aponta direções dispersas e incompatíveis (cada um quer algo diferente);
    ou
  - já resolvem bem com ferramenta existente e não veem por que trocar; ou
  - interesse existe só em features congeladas, mas ninguém topa testar nem pagar.

**Em caso ambíguo, o default é NÃO reabrir.** A auditoria já marcou "demanda não validada"
como o **risco nº 1** do produto inteiro — enganar-se aqui, para o lado otimista, é o erro
mais caro. Registre o resultado honesto mesmo que decepcione.

---

## 4. Perfil-alvo dos 5 professores + mensagem de abordagem

### 4.1 Os 5 slots (diversificar para não enviesar a amostra)

História/Geografia, fundamental II e/ou médio, rede pública **e** privada:

1. **História · pública · médio** — perfil base; currículo mundial denso, muita
   simultaneidade.
2. **História · privada · fundamental II** — perfil "recurso"; escola com verba e
   tecnologia (testa disposição institucional a pagar).
3. **Geografia · pública · fund. II ou médio** — testa se a tese serve além de história
   (geografia usa espaço×tempo diretamente).
4. **História ou Geografia · pública periférica / interior** — infra baixa; testa a
   degradação a offline/projetor. Se não serve pra ele, isso é um **limite de mercado** a
   conhecer.
5. **Coordenador pedagógico OU professor-referência** — early adopter; enxerga o ângulo
   de adoção institucional e costuma indicar/dar acesso.

**Critérios de seleção:** dá aula ativamente (não só gestão); pega temas
mundiais/simultaneidade; mix de perfis tecnológicos (não só entusiastas de tech, senão
viés); **evitar amigos que serão gentis**; priorizar quem **reclama** de preparar aula
(dor viva).

**Onde achar:** rede pessoal de 2º grau, grupos de professores de História/Geografia
(WhatsApp/Telegram), escolas locais, LinkedIn, indicação. Meta: 5 conversas de 30–40 min.
Vídeo com tela compartilhada serve para o Caminho A; **presencial na máquina do dono** é
melhor se for usar o Caminho B (curatorial local).

### 4.2 Mensagem de abordagem (curta, honesta, não-vendedora)

Peça **ajuda e opinião crítica**, não "apresente um produto". Deixe claro que é cedo.

**Variante WhatsApp (curta):**
> Oi, [nome]! Tudo bem? Tô desenvolvendo um protótipo de atlas do tempo pra ensino de
> história/geografia e queria muito 30 min da tua experiência de sala pra reagir a ele —
> de forma crítica, sem papas na língua. Não tô vendendo nada, é fase de teste mesmo, e
> tua opinião honesta vale mais que elogio. Topa? Pode ser por vídeo ou presencial.

**Variante e-mail / LinkedIn (um pouco mais formal):**
> Assunto: 30 min da sua experiência de sala — protótipo de atlas do tempo
>
> Olá, [nome]. Sou [dono] e estou desenvolvendo um protótipo de atlas temporal para o
> ensino de história e geografia — uma linha do tempo com globo 3D e a função "o que
> acontecia no mundo neste momento". Está em fase inicial de validação: **não estou
> vendendo nada**. Queria 30–40 min para te mostrar e ouvir sua reação crítica de quem dá
> aula de verdade — o que faria sentido, o que não faria, o que faltaria. Sua opinião
> honesta (inclusive negativa) é exatamente o que preciso. Teria disponibilidade nas
> próximas duas semanas, por vídeo ou presencial?

---

*Entregáveis 1–4 do kit. O entregável 5 (ficha de registro por professor + entradas de
DECISOES) está em `ficha-professor-template.md`. Como operar está em `README.md`.*
