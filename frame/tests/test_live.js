'use strict';
/* =====================================================================
   LIVE-T1..4 — VIRADA AO VIVO (frame contra /momento/publico).
   Sobre fromEnvelope + envelopes REAIS capturados da função gateada
   (fixtures/*.json = saída de core.f_momento_publico/_curatorial, carga 42).
   Prova que o gating por construção SOBREVIVE ao adaptador e que o cliente
   público não embute segredo curatorial.
   ===================================================================== */
const fs = require('fs'), path = require('path');
const M = require('../atlas-model.js');
const { makeSuite } = require('./_harness.js');
const { test, report } = makeSuite('LIVE-T');

const fx = n => JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures', n), 'utf8'));
const envKpg = fx('env_publico_kpg.json');
const env1789 = fx('env_publico_1789.json');
const envCosmico = fx('env_publico_cosmico.json');

test('LIVE-T1', 'janela K-Pg pública: só itens públicos (isFact=true, selo=público, approved) + ClaimSet kpg-causa; nada pending/seeded', () => {
  const sm = M.fromEnvelope(envKpg, { stage: 'kpg' });
  if (sm.source !== 'api-public') return { passou: false, detalhe: 'source != api-public: ' + sm.source };
  const ruins = sm.items.filter(si => !(si.isFact === true && si.selo === 'público' && si.reviewStatus === 'approved'));
  if (ruins.length) return { passou: false, detalhe: 'itens não-públicos vazaram: ' + ruins.map(r => r.itemId + '(' + r.selo + '/' + r.reviewStatus + ')').join(', ') };
  const naoFato = sm.items.filter(si => si.selo === 'seeded-demo' || si.selo === 'em-revisão' || si.reviewStatus === 'pending');
  if (naoFato.length) return { passou: false, detalhe: 'não-fato exibido: ' + naoFato.map(r => r.itemId).join(', ') };
  const csIds = sm.claimSets.map(c => c.claimSetId);
  if (!csIds.includes('cset:kpg-causa')) return { passou: false, detalhe: 'cset:kpg-causa ausente (host público chicxulub deveria trazê-lo): ' + JSON.stringify(csIds) };
  return { passou: true, detalhe: sm.items.length + ' itens públicos, todos fato; ClaimSets=' + JSON.stringify(csIds) };
});

test('LIVE-T2', 'janela 1789 pública: só iluminismo + posse-washington e ZERO ClaimSets (prova negativa: rev-francesa não vaza)', () => {
  const sm = M.fromEnvelope(env1789, { stage: 's1789' });
  const ids = sm.items.map(si => si.itemId).sort();
  const esperado = ['concept:iluminismo', 'evt:posse-washington-1789'];
  const idsOk = ids.length === esperado.length && ids.every((v, i) => v === esperado[i]);
  if (!idsOk) return { passou: false, detalhe: 'itens públicos 1789 != esperado: ' + JSON.stringify(ids) };
  if (sm.claimSets.length !== 0) return { passou: false, detalhe: 'ClaimSet vazou na pública 1789: ' + JSON.stringify(sm.claimSets.map(c => c.claimSetId)) };
  return { passou: true, detalhe: '2 itens públicos, 0 ClaimSets (gating por host: rev-francesa não vaza)' };
});

test('LIVE-T3', 'nenhum item órfão: fromEnvelope só produz o que o envelope traz; ClaimSet só com host exibido; cósmico público AGORA tem lastro (Frente A)', () => {
  const falhas = [];
  [['kpg', envKpg], ['1789', env1789], ['cosmico', envCosmico]].forEach(([nm, env]) => {
    const sm = M.fromEnvelope(env, {});
    if (!sm.source.startsWith('api')) falhas.push(nm + ':source não-API');
    if (sm.items.length !== (env.items || []).length) falhas.push(nm + ':contagem diverge do envelope (' + sm.items.length + '!=' + (env.items || []).length + ')');
    const ids = new Set(sm.items.map(si => si.itemId));
    sm.claimSets.forEach(cs => { if (!ids.has(cs.host)) falhas.push(nm + ':ClaimSet ' + cs.claimSetId + ' sem host exibido (' + cs.host + ')'); });
  });
  // cósmico público DEIXOU de ser vazio: agora traz corpus fonteado (Frente A, §6 nº 1 do plano).
  // A divergência honesta virou lastro; nenhum item é exibido como não-fato.
  const smC = M.fromEnvelope(envCosmico, { stage: 'bigbang' });
  if (smC.items.length === 0) falhas.push('cósmico público veio vazio — deveria ter lastro após a Frente A');
  const naoFato = smC.items.filter(si => !(si.isFact === true && si.selo === 'público'));
  if (naoFato.length) falhas.push('cósmico com não-fato: ' + naoFato.map(r => r.itemId).join(', '));
  return { passou: falhas.length === 0, detalhe: falhas.length ? falhas.join(', ') : 'sem órfãos; ClaimSets gated por host; cósmico público com lastro (' + smC.items.length + ' itens, todos fato)' };
});

test('LIVE-T4', 'cliente público sem segredo: frame usa /momento/publico por padrão e NÃO embute token/credencial curatorial', () => {
  const html = fs.readFileSync(path.join(__dirname, '..', 'atlas-3d-frame-v1.html'), 'utf8');
  const falhas = [];
  if (!/\/momento\/publico/.test(html)) falhas.push('frame não consome /momento/publico');
  // segredo embutido no cliente é proibido (R-V6): token/senha literais
  if (/X-Atlas-Auth['"]?\s*[:,]\s*['"][A-Za-z0-9._-]{6,}['"]/.test(html)) falhas.push('header X-Atlas-Auth com token LITERAL embutido');
  if (/password\s*[:=]\s*['"][^'"]+['"]/.test(html)) falhas.push('senha literal no cliente');
  if (/(ATLAS_CURATORIAL_TOKEN|atlas_curatorial)\s*[:=]\s*['"][^'"]+['"]/.test(html)) falhas.push('credencial curatorial literal no cliente');
  return { passou: falhas.length === 0, detalhe: falhas.length ? falhas.join(', ') : 'cliente consome a porta pública; nenhum segredo curatorial embutido' };
});

report('LIVE-T (virada ao vivo)');
