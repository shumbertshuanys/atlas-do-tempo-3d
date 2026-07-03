# Decisão — Re-centragem da tese e escopo do MVP enxuto

**Natureza:** registro de decisão. Re-centra a tese do produto (amplia o enquadramento da **Etapa 0**) e generaliza a função central (amplia a **Etapa 5**). **Preserva integralmente a arquitetura.** Data: revisão atual.

---

## 1. A tese re-centrada

O produto é um **atlas tridimensional do espaço-tempo do conhecimento**: clique em qualquer lugar, em qualquer época, em qualquer domínio, e veja o que se sabe ali — com proveniência e incerteza.

Capacidade geral, em uma linha:

> **ponto no espaço + ponto no tempo + domínio → o que se sabe ali** (evento, estado, processo ou feição), com fonte e nível de confiança.

"O que acontecia no mundo neste momento?" deixa de ser *a* função e passa a ser **uma lente** — a de eventos/história. É um exemplo de uso (a pergunta de um professor de história), não a definição do sistema.

---

## 2. Generalização do objeto e da função

- **Objeto central:** de *evento* para **ponto navegável**. Às vezes a resposta é um acontecimento (história); às vezes é o estado de um lugar (a química de um oceano, a formação de uma montanha), sem nenhum "evento".
- **Função central:** de "o que acontecia no mundo" (histórico) para **"o que se sabe neste ponto do espaço-tempo"** — domínio-neutra, com o domínio como **lente selecionável**.

---

## 3. Domínios como lentes de primeira classe

Não "um exemplo de uso", e sim camadas de primeira classe — cada uma já tem tipo no Knowledge Core (Etapa 4F):

| Lente | Pergunta que responde | Tipo no Knowledge Core |
|---|---|---|
| História / sociedade | o que ocorria aqui? | `Event` + `CivilizationState` |
| Geologia / tectônica | como esta terra se formou? | `PaleogeographicState` (+ processo geológico) |
| Química | qual a composição (ar/mar) nesta época? | `GeochemicalState` |
| Oceanos | qual o estado do oceano? | `OceanographicState` |
| Clima | qual o clima então? | `ClimateState` |
| Vida / biologia | que vida havia aqui? | `BiomeState` (+ `Species`) |
| Sistema Terra | integra as lentes acima | `EarthSystemState` |

---

## 4. O que muda e o que não muda

**Não muda (arquitetura):** o Knowledge Core (já tem os tipos acima), a espinha epistêmica (claim-first, fonte, incerteza, `ClaimSet`, invariante de exibição), a direção única de dependência, a experiência 3D, o eixo temporal canônico (Big Bang → presente → projetivo) e as cenas já construídas.

**Muda (enquadramento, não arquitetura):** a função central vira domínio-neutra; os "contextos" viram lentes de primeira classe. É **re-enquadramento, não reconstrução**.

**Prova de que sempre foi multidomínio:** das três cenas-gabarito já feitas, **duas não são históricas** — GOE (2,4 Ga, química da atmosfera, Etapa 4E) e K-Pg (66 Ma, geologia e vida, Etapa 4G).

---

## 5. Escopo do MVP enxuto — a alma

**Dentro:**
- o atlas navegável;
- multiescala (tempo profundo → história → presente);
- multidomínio (lente de domínio selecionável);
- a espinha epistêmica intacta (o gating mantém o sensível/`pending` mediado ou oculto — isto *é* a alma, não recurso de usuário);
- **uma vista única — exploração livre**.

**Fora (upgrades futuros — encaixam por cima sem tocar o núcleo):**
- contas / autenticação;
- versão estudante e versão professor;
- Teacher Planning Layer (Etapa 7);
- Content Matching Engine (Etapa 8);
- Pedagogical Output Layer (Etapa 9);
- mapeamento BNCC / grade por série (Etapa 6 como indexação);
- LMS.

**Justificativa:** a arquitetura foi desenhada para isto (dependência única). As camadas de escola são **consumidoras aditivas** que apontam para o núcleo; não precisam existir para o atlas existir. Os documentos das Etapas 6–9 viram o **roteiro de upgrade**, não lixo.

---

## 6. Plano de construção — cadência evidence-first (não documento-por-etapa)

Aplica as propostas de governança **P1** (pronto = evidência executável), **P2** (fatias como instrumento padrão) e **P3** (operar na fatia).

- **Incremento 1 — o frame.** Eixo de tempo de Ga até hoje com bandas de regime; seletor de lente de domínio; globo/mapa esquemático; dossiê epistêmico (reusado e ampliado da fatia de 1789); troca de cena. **1789 totalmente clicável**; GOE e K-Pg **posicionados** no eixo (mostrando o alcance multiescala), ainda não dossiados. *Entrega:* protótipo navegável rodando.
- **Incremento 2 — o multidomínio.** GOE (química/atmosfera) e K-Pg (geologia/vida) instanciados **fiéis** ao 4E/4G, com suas lentes. *Entrega:* a tese multidomínio provada — mesmo planeta, mesmo eixo, lentes diferentes, do tempo profundo à história.

Ambos terminam em **artefato que abre e se clica**, não em documento.

---

## 7. Relação com as pendências

**Nenhuma pendência bloqueia** os dois incrementos (protótipo descartável; o mapa esquemático cobre a geometria pendente; confirmação de fonte-por-asset, fundação escolar e jurídico ficam para o salto ao público). A decisão de **motor de banco** (RDF* × property graph × relacional) fica para **depois** do protótipo, decidida com os padrões reais de consulta como evidência; os dados do protótipo já são um **graph-seed claim-first** que migra para o motor escolhido.

---

## 8. O que esta decisão supersede / preserva

- **Supersede:** o enquadramento da função central como simultaneidade histórica (Etapa 5) e o recorte mais largo de MVP da Etapa 12 (múltiplas vistas / camadas de usuário no primeiro corte).
- **Preserva:** todo o resto — a arquitetura, a espinha epistêmica e o backlog como roteiro de upgrade.
