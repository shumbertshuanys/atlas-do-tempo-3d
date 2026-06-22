# Backlog — Discovery curricular para priorização de domínios (fase de upgrade)

**Natureza:** item de backlog / registro de decisão diferida (anti-perda). **Não é passo do roteiro atual.** Complementa a *Decisão de re-centragem da tese / MVP enxuto* e o `estado-atual-e-roteiro`. Origem: conversa sobre coletar grades escolares de muitas escolas. Data: revisão atual.

**Status:** ⏸️ **Diferido** — fase de upgrade das camadas escolares (Etapas 6 e 8). Aprovado para registro, **não** para execução agora.

---

## 1. Ideia registrada (intenção)

Usar os currículos/grades reais das escolas como sinal para **identificar quais domínios as escolas efetivamente usam** e, a partir disso, **decidir quais dados gerais povoar primeiro** no sistema (prioridade de *seed* do Knowledge Core).

## 2. Refinamento (para não violar a espinha do projeto)

A pergunta "quais domínios as escolas usam" **já tem fonte primária normativa** — não depende de raspar escolas:

- A BNCC organiza a educação básica em **áreas do conhecimento e componentes curriculares**; os 27 referenciais curriculares estaduais contextualizam isso por UF. Essa é a fonte autoritativa da *estrutura* curricular.
- A grade de cada escola (PPP → plano anual → plano de aula) **deriva** dessas fontes; coletá-las em massa traz pouca informação nova sobre *quais domínios existem*.

Consequência:

- **Fonte primária dos domínios:** corpus normativo (BNCC + 27 referenciais + LDB). *A enumeração exata de áreas/componentes deve ser extraída da BNCC quando o passo for ativado — não fixada aqui, para não envelhecer.*
- **Amostra de escolas:** sinal **secundário** — informa **ênfase, sequência e recorte real em sala**, não a existência dos domínios. É pesquisa de campo (discovery); **não** entra no Knowledge Core.

## 3. Conexão com a tese e com o *seed* inicial

As **lentes de domínio** do sistema já estão definidas (re-centragem): História/sociedade, Geologia/tectônica, Química, Oceanos, Clima, Vida/biologia, Sistema Terra. Mapeamento conceitual escola ↔ sistema:

| Componente escolar (BNCC) | Lente(s) do sistema |
|---|---|
| História | História/sociedade (`Event` + `CivilizationState`) |
| Geografia | Geologia, Clima, Oceanos, Sistema Terra |
| Ciências (EF) / Biologia, Química, Física (EM) | Vida, Química, Geologia, Clima |
| Demais componentes | fora do corpus inicial; contexto/exploração futura |

Leitura: o *seed* inicial do KC deve priorizar os domínios de **maior aderência curricular** (História, Geografia, Ciências) **sem** estreitar a tese multidomínio. O discovery refina a **ordem e a ênfase** do povoamento, não o universo navegável.

## 4. Por que é fase de upgrade (e não agora)

A re-centragem para o MVP enxuto tirou as camadas escolares (Etapa 6 conformidade, 7 planejamento, 8 matching, 9 output) do escopo e as registrou como **roteiro de upgrade**. O roteiro vigente é fundação técnica + governança/publicação. Este item entra **junto/antes** do trabalho de indexação BNCC (Etapa 6) e do design do Matching (Etapa 8).

## 5. Forma proposta quando for ativado (esqueleto de mini-passo)

- **Objetivo:** priorizar o povoamento do KC e calibrar a indexação BNCC usando a estrutura curricular real.
- **Escopo:** (a) consolidar o corpus normativo; (b) amostra proposital pequena (≈10–20 PPP/matrizes/planos anuais), variando região e rede pública/privada.
- **Fontes:** BNCC (basenacionalcomum.mec.gov.br); 27 referenciais curriculares estaduais; LDB; pareceres/resoluções CNE; amostra de PPP/matrizes públicas.
- **Método:** extrair áreas/componentes e mapeá-los às lentes; medir ênfase/sequência na amostra; produzir uma **matriz de prioridade de *seed* por domínio**.
- **Riscos:** (R1) deixar a grade "originar" conteúdo — **proibido**: BNCC é indexação, não origem; (R2) licença incerta por documento — passa pelo portão de ingestão (Etapa 1.1); (R3) LGPD/menores — **nenhum PII**; só documentos institucionais; (R4) amostra enviesar a tese para o currículo — manter o multidomínio.
- **Entregável:** documento curto "Prioridade de *seed* por domínio" + lista de mapeamentos escola ↔ lente (apontando para o KC por ID estável, **nunca** copiando para o núcleo).

## 6. Invariantes a respeitar (herdados)

- O conhecimento **não nasce da grade**; a grade é camada de aplicação/indexação.
- BNCC = conformidade/indexação, **não** fonte de autoridade factual.
- Qualquer documento ingerido passa pela checagem de licença (Etapa 1.1).
- Nenhum dado pessoal de aluno; a amostra é de documentos institucionais públicos.

## 7. Gatilho de retomada

Retomar quando o projeto entrar na **fase de upgrade das camadas escolares** (após fundação técnica e governança), como insumo da Etapa 6 (indexação BNCC) e da Etapa 8 (Matching). Até lá: **não executar**.
