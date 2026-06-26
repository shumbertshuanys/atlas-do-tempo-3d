# Registro de execução — virada ao vivo + 3D real (D-A3.7/6/virada + Opção A)

**Versão:** v1.0 · **Data:** jun/2026 · **Natureza:** handoff de execução (9 pontos, Playbook §2)
**Antecede:** plano `passo-a3-plano-execucao-virada-ao-vivo-3d-v1_0.md` + descoberta `nota-descoberta-a3-virada-3d.md`
**Sessão:** escreveu código (frame) + 1 extensão aditiva de banco (`011`); seguiu PG1 em cada degrau.

## 1. Objetivo
Levar o frame de **espelho estático** a **experiência ligada à API pública ao vivo**, executando
D-A3.7 (modelo único + overlay §8), D-A3.6 (assets esquemáticos rotulados) e a **virada de fonte**
(array → `/momento/publico`), sem tocar o miolo provado e preservando §8 + gating por construção.

## 2. O que foi feito (na ordem do §9 do plano)
- **PG1 inicial:** `down -v && bootstrap.sh` fresh → **10/10 + 10/10 + 10/10 + 5/5**.
- **Descoberta (§6):** 5 achados; falsificou a tabela de normalização §5.2 do plano (corpus é
  **hifenizado = frame** → normalização é identidade); cósmicos **ausentes** do corpus; `confidence`
  = `alta/média/baixa`; envelope **não** expõe ponto (só `geometryRegime`). → `nota-descoberta-a3-virada-3d.md`.
- **D-A3.7:** `frame/atlas-model.js` (puro, UMD) — `fromStaticArray`/`overlayFields` + produtores
  overlay→markup; `ctOf` **fail-loud** (tipo fora do `CT` não vira `hipótese` em silêncio). O frame
  passou a **desenhar** os produtores nos 3 renderizadores + painel (§8 deixou de ser reconstruído
  em 4 lugares). Shaders/câmera/física intactos.
- **D-A3.6:** `regimeLabel` puro + badge `#regimecap` no 3D — cena procedural sempre
  esquemática/reconstrução, **nunca foto** (R-V7).
- **Virada:** `fromEnvelope` (mesmo `SceneModel`) + extensão aditiva `displayPoint` em `011`
  (centróide PostGIS); comutador de fonte array⇄API (default API → `/momento/publico`); gates
  re-mapeados a papel/endpoint (OFF→pública; ON→curatorial token/localhost); fallback honesto ao
  espelho local se a API cair.
- **Config Opção A (12-factor):** `.env`/`.env.example`, interpolação no `docker-compose`, serviço
  que **recusa subir** sem var; `password=atlas` removido do código.
- **CLAUDE.md** atualizado; este handoff.

## 3. Evidência falsificável (PRONTO = EVIDÊNCIA)
- **Frame (node, framework-free):** `3D-T1..5` 5/5 (overlay §8 idêntico entre modos; equivalente
  textual em todo degrau; fronteira ClaimSet idêntica com pesos assimétricos; reconstrução+anacronismo;
  piso estático não perde campo) · `ASSET-T1..3` 3/3 · `LIVE-T1..4` 4/4 (K-Pg só fato + kpg-causa;
  1789 só iluminismo+posse, 0 ClaimSets; sem órfãos + cósmico vazio; cliente sem segredo).
- **Integração ponta-a-ponta** (smoke descartável, fetch mockado): frame faz `GET /momento/publico`
  → `fromEnvelope` → `select` renderiza Chicxulub + ClaimSet + 0.82 vindos do **envelope**, não do array.
- **Banco:** `down -v && bootstrap.sh` fresh → **10/10 + 10/10 + 10/10 + 5/5** com o fluxo 12-factor.
- **Segredos:** `git grep password=atlas` limpo no código; serviço sem var → erro + exit 2.

## 4. Decisões tomadas
- Normalização epistêmica = **identidade** (corpus já hifenizado); mantido só o guarda fail-loud.
- Cósmicos **vazios na porta pública** (honesto) — teasers seguem só na face curatorial/estática como
  representação; virar corpus exige tarefa de modelagem **com fonte** (não promover seeded).
- `020` mantém senhas-dev de papel (casadas pelo `.env`); Opção B (gerenciador) → **E14**.

## 5. Invariantes preservadas
§8 idêntico nos 3 degraus (3D-T1); público nunca vaza não-fato (LIVE-T1) e gating por host (LIVE-T2);
tempo profundo sempre reconstrução/esquemático (3D-T4/ASSET-T); sem segredo no cliente (LIVE-T4); miolo
`db/ddl/`/`010` intocado; `011` só **adição** (`displayPoint`).

## 6. Arquivos tocados
`frame/atlas-model.js` (novo) · `frame/atlas-3d-frame-v1.html` · `frame/tests/` (novo: `_harness`,
`test_3d`, `test_assets`, `test_live`, `fixtures/`) · `db/read-layer/011-momento-envelope.sql` (+displayPoint)
· `service/atlas_api.py` · `db/migration/{migrate,verify,test_a4,test_a3,test_a3_http}.py` ·
`docker-compose.yml` · `scripts/bootstrap.sh` · `.env.example` · `.env` (gitignored) · `CLAUDE.md`.

## 7. Como reproduzir
`cp .env.example .env` → `docker compose down -v && bash scripts/bootstrap.sh` (10/10×3 + 5/5);
`for t in test_3d test_assets test_live; do node frame/tests/$t.js; done` (5/5 · 3/3 · 4/4).

## 8. Pendências / próximas frentes
Cósmicos como corpus **com fonte**; reintegrar as 3 sensíveis quando host sair de `pending` (Trilha C);
E14 (segredos Opção B + auth real da curatorial). Nota: durante o *play* o frame ao vivo não refaz
fetch a cada quadro (usa a última janela carregada) — refetch em scrub/gate; aceitável no MVP.

## Rodapé — o que este passo NÃO fez
NÃO reabriu B1/B2 nem reescreveu `db/ddl/`/`010`; NÃO promoveu seeded a corpus; NÃO religou as 3
sensíveis; NÃO embutiu segredo curatorial no cliente; NÃO desligou o §8 em nenhum degrau.
