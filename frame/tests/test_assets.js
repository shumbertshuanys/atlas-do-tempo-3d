'use strict';
/* =====================================================================
   ASSET-T1..3 — D-A3.6: assets procedurais ESQUEMÁTICOS ROTULADOS.
   O fotorrealismo anacrônico no tempo profundo é proibido (R-V7; §8.2; Art.7).
   Os shaders já são procedurais/self-contained; aqui prova-se o RÓTULO:
   toda cena se declara reconstrução/representação — nunca fotografia.
   ===================================================================== */
const M = require('../atlas-model.js');
const { makeSuite } = require('./_harness.js');
const { test, report } = makeSuite('ASSET-T');

const RECON = /esquemátic|reconstru|representaç/i;
const FOTO_POSITIVA = /\bfotografia\b|\bfoto\b|imagem de sat[ée]lite|fotorrealis/i;

test('ASSET-T1', 'todo estágio tem rótulo esquemático (schematic=true) com palavra de reconstrução; nenhum se diz fotografia', () => {
  const faltas = [];
  M.STAGES.forEach(s => {
    const lab = M.regimeLabel(s.id);
    if (!lab) { faltas.push(s.id + ':sem rótulo'); return; }
    if (lab.schematic !== true) faltas.push(s.id + ':schematic!=true');
    if (!RECON.test(lab.label)) faltas.push(s.id + ':rótulo sem reconstrução/esquemático');
    if (FOTO_POSITIVA.test(lab.label)) faltas.push(s.id + ':rótulo reivindica fotografia');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : M.STAGES.length + ' estágios rotulados como esquemáticos/reconstrução, nenhum como foto' };
});

test('ASSET-T2', 'os 3 teasers cósmicos são reconstrução-modelada + representação (repr) — nunca foto-fato', () => {
  const cosmicos = ['rep:bigbang', 'rep:galaxies', 'rep:sun'];
  const sm = M.fromStaticArray(M.ITEMS, M.CLAIMSETS, { porta: 'curatorial' });
  const faltas = [];
  cosmicos.forEach(id => {
    const si = sm.items.find(i => i.itemId === id);
    if (!si) { faltas.push(id + ':ausente'); return; }
    if (si.epistemicType !== 'reconstrução-modelada') faltas.push(id + ':tipo!=reconstrução-modelada (' + si.epistemicType + ')');
    const ov = M.overlayFields(si, 'curatorial');
    if (ov.repr !== true) faltas.push(id + ':sem flag de representação');
    // a bandeira/painel exibem a natureza de representação (não some)
    if (!/Representação de cena/.test(M.overlayDetailHTML(ov, si))) faltas.push(id + ':painel sem aviso de representação');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : '3 cósmicos = reconstrução-modelada + representação rotulada' };
});

test('ASSET-T3', 'regimeLabel ecoa o regime do estágio (cósmico/geológico/histórico) — rótulo coerente com o tempo', () => {
  const faltas = [];
  M.STAGES.forEach(s => {
    const lab = M.regimeLabel(s.id);
    if (!lab.regime || lab.regime !== s.regime) faltas.push(s.id + ':regime divergente (' + (lab && lab.regime) + ' != ' + s.regime + ')');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : 'rótulo de regime coerente em todos os estágios' };
});

report('ASSET-T (assets procedurais rotulados)');
