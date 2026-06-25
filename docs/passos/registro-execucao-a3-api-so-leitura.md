# Registro de execução — API só-leitura (D-A3.3/4/5) · Handoff

**Versão:** v1.0 · **Data:** jun/2026
**Antecede:** virada ao vivo (frame → API) + 3D (D-A3.6..8)
**Sucede:** plano de execução `passo-a3-plano-execucao-api-so-leitura-v1_0.md` (forma β ratificada)
**Natureza:** registro do que foi **escrito e provado** nesta sessão de execução, formato 9 pontos.

---

## 1. Objetivo (o que esta sessão entregou)

A **API mínima só-leitura** que expõe "O que acontecia no mundo?" como envelope `MomentResult`
completo (forma β): funções-envelope no banco + serviço fino + portão por grant. Cada campo derivado
do autoritativo; cada garantia com um teste que poderia ter falhado (PG1).

## 2. Escopo executado

- `db/read-layer/011-momento-envelope.sql` (**adição**): TYPE `core.t_momento` + `f_momento_publico`/
  `_curatorial` + helper `f_item_envelope_core`. Reusa `f_simultaneidade_*`/`f_item_*` do A4.
- `db/migration/test_a3.py` (A3-T1..T10) + `db/reports/test_a3_report.json`.
- `db/roles/020-papeis-leitura.sql` (papéis `atlas_public`/`atlas_curatorial`; portão por grant).
- `service/atlas_api.py` (serviço fino só-leitura, 2 endpoints) + `db/migration/test_a3_http.py`
  (A3-HTTP-1..5) + `db/reports/test_a3_http_report.json`.
- `scripts/bootstrap.sh` aplica 011 + 020 e roda as 4 suítes; `CLAUDE.md` atualizado; nota de
  descoberta `nota-descoberta-a3-api-envelope.md`.

## 3. Diagnóstico confirmado na execução

- O envelope **nasce no banco** (Etapa 11 §6.3 [NORMATIVO]): leitura factual nunca é "texto pelado".
- O gating é **propriedade da fonte** (porta pública reusa `f_simultaneidade_publica` → só
  `v_publishable_public`) e do **grant** (papel público sem EXECUTE na curatorial), não `if` de runtime.
- **Descoberta corrigiu o contrato** (regra §6 do plano): ver ponto 5.

## 4. Decisões aplicadas

| ID | Como ficou |
|---|---|
| D-A3.3 | Envelope `core.t_momento` (forma β, `RETURNS` 1 linha); cada item carrega §8 via `f_item_envelope_core` + merge dos campos por porta. |
| D-A3.4 | Serviço stdlib (`http.server`), 2 endpoints GET; serializa `to_jsonb(envelope)`; escrita → 405; sem credencial de escrita. |
| D-A3.5 | `SECURITY DEFINER` + `REVOKE EXECUTE FROM PUBLIC` (011) + grants por papel (020). `atlas_public` só na pública; `atlas_curatorial` nas duas. |

## 5. Divergência da carga (descoberta) e ajuste do contrato

- **Plano assumia "1789→`rev-francesa`" como exemplo público.** Carga real: o host de `rev-francesa`
  (`evt:estados-gerais-1789`) tem `per_asset_source_confirmed=false` → **não** está em
  `v_publishable_public`. Idem `goe-ritmo` (`proc:goe`). **Só `kpg-causa`** (host `chicxulub`) é público.
- **Ajuste (sem afrouxar invariante):** A3-T8 testa a **invariante** — todo ClaimSet público tem host
  em `items[]` — com **exemplo positivo `kpg-causa` (K-Pg)** e **prova negativa em 1789** (rev-francesa
  não vaza). A invariante §5.5 ficou **mais** exercitada, não menos.
- **Membros de ClaimSet** têm um único `weight` (não a tripla `evidence/scholarly/display`). A3-T9 não
  fabrica três pesos: testa **assimetria de peso + fronteira `resolution` presente** (honestidade
  epistêmica). Detalhe em `nota-descoberta-a3-api-envelope.md`.

## 6. Evidência (PG1) — os 4 artefatos verdes em volume novo

`docker compose down -v && bash scripts/bootstrap.sh`:

- `verify.py` **10/10** · `test_a4.py` **10/10** · `test_a3.py` **10/10** · `test_a3_http.py` **5/5**.

Os três artefatos que **provam a API** (do prompt de execução):

- **A3-T2** — público nunca devolve não-fato (isFact=true, selo='público', approved em toda janela).
- **A3-HTTP-1** — `atlas_public` chamando `f_momento_curatorial` → *permission denied* (portão por grant).
- **A3-T3** — todo item carrega as chaves §8 não-nulas (incl. `attributionRef.provenanceRef`, [N1]).

## 7. Riscos remanescentes

- **R-A3.7** coberto por A3-HTTP-1 (fica vermelho se alguém der EXECUTE da curatorial ao público).
- **Senhas dos papéis (`020`) — DECISÃO DE PRODUÇÃO PENDENTE (registrada, não tomada).** As credenciais
  `atlas_public`/`atlas_curatorial` (e o DSN dev homônimo `atlas/atlas/atlas`) são de **desenvolvimento**;
  produção deve injetá-las por **ambiente**, não versionar. **Decidir antes de a virada sair de localhost**
  (push de repo já conta como compartilhado). *Recomendação:* **12-factor mínimo** (`.env` no gitignore,
  `.env.example` com placeholders, `docker-compose` interpolando `${VAR}`); o **gerenciador de segredos**
  com rotação/auditoria pertence à **Etapa 14** (operação/DPIA), não ao MVP. A virada do **público** usa
  `atlas_public`; o **curatorial** pode ficar em localhost/rede interna até a E14 definir a auth. *Evidência
  falsificável para o passo de config:* `git grep` não acha `password=atlas` fora de `.env.example`/docs, e
  o serviço **recusa subir** sem a variável setada (erra alto, não silenciosamente).
- **`navigationSuggestions`/`generatedSceneCandidate`** ficaram rasos/vazios no A3 (previsto §5.3).

## 8. Entregáveis (no repo)

`011-momento-envelope.sql` · `020-papeis-leitura.sql` · `service/atlas_api.py` · `test_a3.py` ·
`test_a3_http.py` · relatórios em `db/reports/` · `bootstrap.sh` (8 passos) · `CLAUDE.md` · esta nota +
`nota-descoberta-a3-api-envelope.md`. Commits por mudança lógica: (a) envelope SQL, (b) test_a3+wiring,
(c) serviço+papéis+HTTP, (d) docs.

## 9. Próximo passo

**Virada ao vivo:** o frame consome `service/atlas_api.py` (`/momento/publico`) em vez dos arrays
estáticos — a divergência frame↔corpus se extingue por construção. **3D real (D-A3.6..8)** em paralelo
contra o array via `SceneModel`; a virada troca **uma fonte só**.

---

## Rodapé — o que esta sessão NÃO fez

- **NÃO** reescreveu `db/ddl/`/`db/read-layer/010` (miolo provado) — só **adição** (011/020/serviço/testes).
- **NÃO** virou o frame ao vivo nem iniciou o 3D (D-A3.6..8).
- **NÃO** religou as 3 sensíveis (`direitos-limites`/`inconfidencia`/`escravidao-central`) — host
  `pending`, seguem na fila (Trilha C).
- **NÃO** promoveu `seeded-demo` a corpus/fato; **NÃO** criou caminho de escrita na API nem deu ao
  serviço credencial de escrita.
