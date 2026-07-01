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

test('ASSET-T2', 'os cósmicos viraram corpus COM fonte (Frente A): fonteados, nunca seeded, nunca "fato-documentado" — e a cena cósmica segue esquemática (nunca foto)', () => {
  const cosmicos = ['evt:big-bang', 'state:cmb-recombinacao', 'proc:formacao-galaxias', 'evt:formacao-sistema-solar', 'proc:formacao-terra'];
  const sm = M.fromStaticArray(M.ITEMS, M.CLAIMSETS, { porta: 'curatorial' });
  const faltas = [];
  cosmicos.forEach(id => {
    const si = sm.items.find(i => i.itemId === id);
    if (!si) { faltas.push(id + ':ausente'); return; }
    // corpus com fonte — nunca seeded, nunca fato-documentado (ninguém testemunhou t=0)
    if (si.selo === 'seeded-demo') faltas.push(id + ':seeded (não pode)');
    if (si.epistemicType === 'fato-documentado') faltas.push(id + ':exibido como fato-documentado');
    const ov = M.overlayFields(si, 'curatorial');
    if (!ov.attribution || !ov.attribution.label) faltas.push(id + ':sem atribuição de fonte');
  });
  // a cena cósmica permanece ESQUEMÁTICA (nunca foto) — garantido no rótulo do estágio
  ['bigbang', 'galaxies', 'sun'].forEach(sid => {
    const lab = M.regimeLabel(sid);
    if (!lab || lab.schematic !== true || !/esquemátic|reconstru|representaç/i.test(lab.label)) faltas.push(sid + ':cena não-esquemática');
    if (/\bfotografia\b|\bfoto\b|fotorrealis/i.test(lab.label)) faltas.push(sid + ':cena reivindica foto');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : '5 cósmicos = corpus fonteado, nunca seeded/fato-documentado; cena cósmica esquemática' };
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
