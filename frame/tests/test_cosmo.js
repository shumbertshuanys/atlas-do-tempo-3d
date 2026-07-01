'use strict';
/* =====================================================================
   COSMO-T1..5 — Frente A: cósmicos como corpus COM fonte.
   Sobre o envelope REAL da porta pública (fixtures/env_publico_cosmico.json =
   saída de core.f_momento_publico, carga 47) + as funções PURAS do frame.
   Prova: a janela cósmica deixa de vir vazia onde há lastro; nenhum cósmico
   como fato seco; incerteza nos 3 degraus; anti-promoção (todo com fonte,
   nenhum seeded); item sem geometria (displayPoint NULL) sem regressão de
   marcador; zero ClaimSet cósmico de falsa equivalência.
   ===================================================================== */
const fs = require('fs'), path = require('path');
const M = require('../atlas-model.js');
const { stripTags, makeSuite } = require('./_harness.js');
const { test, report } = makeSuite('COSMO-T');

const fx = n => JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures', n), 'utf8'));
const envCosmico = fx('env_publico_cosmico.json');
const sm = M.fromEnvelope(envCosmico, { stage: 'bigbang' });
const present = (html, token) => stripTags(html).includes(stripTags(token));

test('COSMO-T1', 'a janela cósmica pública DEIXA de vir vazia: retorna os itens fonteados, todos público/isFact (§6 nº 1 do plano)', () => {
  if (sm.source !== 'api-public') return { passou: false, detalhe: 'source != api-public: ' + sm.source };
  if (sm.items.length < 1) return { passou: false, detalhe: 'cósmico veio vazio — sem lastro (regressão)' };
  const ruins = sm.items.filter(si => !(si.isFact === true && si.selo === 'público'));
  return { passou: ruins.length === 0,
    detalhe: ruins.length ? 'não-público vazou: ' + ruins.map(r => r.itemId + '(' + r.selo + ')').join(', ')
                          : sm.items.length + ' itens cósmicos públicos com lastro: ' + sm.items.map(i => i.itemId).join(', ') };
});

test('COSMO-T2', 'nenhum cósmico exibido como "fato-documentado"; tipo casa o CT (sem fail-loud) e a incerteza aparece nos 3 degraus (painel 3D/2D + estático)', () => {
  const faltas = [];
  sm.items.forEach(si => {
    if (si.epistemicType === 'fato-documentado') faltas.push(si.itemId + ':exibido como fato-documentado');
    const ov = M.overlayFields(si, sm.porta);
    // fail-loud: tipo fora do CT vira rótulo vermelho unknown (pegaria a regressão da grafia medição-direta)
    if (ov.typeLabel.unknown === true) faltas.push(si.itemId + ':tipo fora do CT (fail-loud) — «' + si.epistemicType + '»');
    // incerteza como FAIXA presente no painel (3D+2D) e no cartão estático
    const detail = M.overlayDetailHTML(ov, si);
    const card = M.overlayStaticCardHTML(ov, si);
    const y0 = M.formatYear(ov.uncertaintyBand.start), y1 = M.formatYear(ov.uncertaintyBand.end);
    [['painel', detail], ['estático', card]].forEach(([nm, out]) => {
      if (!present(out, y0) || !present(out, y1)) faltas.push(si.itemId + ':' + nm + ' sem faixa de incerteza');
    });
  });
  return { passou: faltas.length === 0,
    detalhe: faltas.length ? faltas.join(', ') : sm.items.length + ' cósmicos: nunca fato-documentado, tipo no CT, incerteza nos 3 degraus' };
});

test('COSMO-T3', 'anti-promoção: TODO cósmico tem attributionRef.provenanceRef ([N1]); NENHUM é seeded-demo', () => {
  const faltas = [];
  sm.items.forEach(si => {
    if (!(si.attributionRef && si.attributionRef.provenanceRef)) faltas.push(si.itemId + ':sem provenanceRef');
    if (si.selo === 'seeded-demo') faltas.push(si.itemId + ':seeded-demo (promoção proibida)');
  });
  return { passou: faltas.length === 0,
    detalhe: faltas.length ? faltas.join(', ') : sm.items.length + ' cósmicos com proveniência; nenhum promovido de seeded' };
});

test('COSMO-T4', 'item sem geometria terrestre: displayPoint NULL + geometryRegime=semLugarTerrestre; estágio cósmico esquemático (sem marcador terrestre, nunca foto)', () => {
  const faltas = [];
  sm.items.forEach(si => {
    if (si.displayPoint !== null && si.displayPoint !== undefined)
      faltas.push(si.itemId + ':displayPoint não-nulo (' + JSON.stringify(si.displayPoint) + ') — marcador terrestre espúrio');
    if (si.geometryRegime !== 'semLugarTerrestre')
      faltas.push(si.itemId + ':geometryRegime!=semLugarTerrestre (' + si.geometryRegime + ')');
  });
  // a cena do estágio cósmico é esquemática/reconstrução — NUNCA foto (R-V7)
  ['bigbang', 'galaxies', 'sun'].forEach(sid => {
    const lab = M.regimeLabel(sid);
    if (!lab || lab.schematic !== true || !/esquemátic|reconstru|representaç/i.test(lab.label)) faltas.push(sid + ':estágio não-esquemático');
    if (/\bfotografia\b|\bfoto\b|fotorrealis/i.test(lab && lab.label || '')) faltas.push(sid + ':cena reivindica foto');
  });
  return { passou: faltas.length === 0,
    detalhe: faltas.length ? faltas.join(', ') : 'displayPoint NULL tratado; estágios cósmicos esquemáticos, sem marcador terrestre nem foto' };
});

test('COSMO-T5', 'zero ClaimSet cósmico de falsa equivalência (etapa-3.1 §10.7: a expansão é claim único; criacionismo não é lado)', () => {
  const n = sm.claimSets.length;
  return { passou: n === 0,
    detalhe: n === 0 ? 'nenhum ClaimSet na janela cósmica (sem palco para falsa equivalência)'
                     : 'ClaimSet cósmico presente: ' + sm.claimSets.map(c => c.claimSetId).join(', ') };
});

report('COSMO-T (cósmicos como corpus com fonte)');
