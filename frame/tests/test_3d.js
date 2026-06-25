'use strict';
/* =====================================================================
   3D-T1..5 — DEGRADAÇÃO CRUZADA (Art.12 / §8.3)
   Prova que o §8 nasce num ÚNICO overlayFields e SOBREVIVE idêntico de
   3D a estático. Sobre as funções PURAS de frame/atlas-model.js (node).
   Fonte = array estático (a virada troca uma fonte; o contrato é o mesmo).
   ===================================================================== */
const M = require('../atlas-model.js');
const { deepEqual, stripTags, makeSuite } = require('./_harness.js');
const { test, report } = makeSuite('3D-T');

const NEGACIONISMO = /n[ãa]o houve impacto|impacto n[ãa]o ocorreu|negacion|terra plana|nunca existiu/i;

/* Surfaces "cheias" do §8: painel de detalhe (3D e 2D compartilham) e cartão
   estático (piso). Compacto: bandeira 3D e rótulo 2D (tipo+conf+equivalente). */
function fullSurfaces(ov, it) {
  return {
    detail: M.overlayDetailHTML(ov, it),     // 3D + 2D (painel compartilhado)
    static: M.overlayStaticCardHTML(ov, it), // estático (piso)
  };
}
function tokensOf(ov, it) {
  const t = [];
  t.push(ov.typeLabel.name);
  t.push(ov.confidence.word);
  t.push(M.formatYear(ov.uncertaintyBand.start));
  t.push(M.formatYear(ov.uncertaintyBand.end));
  (ov.seals || []).forEach(s => t.push(s));
  if (ov.attribution && ov.attribution.label) t.push(ov.attribution.label);
  if (ov.claimSetBoundary) {
    t.push(ov.claimSetBoundary.tema);
    ov.claimSetBoundary.sides.forEach(s => { t.push(s.stmt); t.push(s.weight.toFixed(2)); });
  }
  return t;
}
function present(html, token) { return stripTags(html).includes(stripTags(token)); }

const smK = M.fromStaticArray(M.ITEMS, M.CLAIMSETS, { stage: 'kpg', porta: 'curatorial' });
const sm89 = M.fromStaticArray(M.ITEMS, M.CLAIMSETS, { stage: 's1789', porta: 'curatorial' });
const chic = smK.items.find(i => i.itemId === 'evt:impacto-chicxulub');
const lavo = sm89.items.find(i => i.itemId === 'chem:lavoisier-traite-1789'); // seeded-demo

test('3D-T1', 'overlayFields é fonte única — overlay idêntico entre modos; campos §8 batem em detalhe e estático', () => {
  if (!chic) return { passou: false, detalhe: 'chicxulub ausente do SceneModel K-Pg' };
  // 1) overlayFields não depende de "mode": deep-equal entre invocações independentes
  const a = M.overlayFields(chic, smK.porta);
  const b = M.overlayFields(chic, smK.porta);
  const c = M.overlayFields(chic, smK.porta);
  if (!(deepEqual(a, b) && deepEqual(b, c)))
    return { passou: false, detalhe: 'overlayFields não-determinístico (depende de estado/mode global)' };
  // 2) anti-drift: todo token §8 do overlay aparece em AMBAS as surfaces cheias
  const surf = fullSurfaces(a, chic);
  const faltas = [];
  tokensOf(a, chic).forEach(tok => {
    if (!present(surf.detail, tok)) faltas.push('detalhe:«' + tok + '»');
    if (!present(surf.static, tok)) faltas.push('estático:«' + tok + '»');
  });
  // 3) selo seeded sobrevive aos dois (item seeded distinto)
  const sov = M.overlayFields(lavo, sm89.porta);
  const ssurf = fullSurfaces(sov, lavo);
  if (!(sov.seals || []).includes('seeded-demo')) faltas.push('overlay seeded sem selo');
  else { if (!present(ssurf.detail, 'seeded')) faltas.push('detalhe sem selo seeded');
         if (!present(ssurf.static, 'seeded')) faltas.push('estático sem selo seeded'); }
  return { passou: faltas.length === 0, detalhe: faltas.length ? ('campos perdidos: ' + faltas.join(', ')) : 'overlay determinístico; §8 idêntico em detalhe/estático + selo seeded preservado' };
});

test('3D-T2', 'textualEquivalent não-vazio e presente em todos os degraus (3D/2D/estático)', () => {
  const faltas = [];
  smK.items.forEach(it => {
    const ov = M.overlayFields(it, smK.porta);
    const te = ov.textualEquivalent;
    if (!te || !te.trim()) { faltas.push(it.itemId + ':vazio'); return; }
    const flag = M.overlay3DFlagHTML(ov, it);   // 3D (compacto, com descrição acessível)
    const lab2d = M.overlay2DLabelText(ov, it); // 2D (rótulo do canvas)
    const card = M.overlayStaticCardHTML(ov, it); // estático
    const detail = M.overlayDetailHTML(ov, it);
    [['3D-flag', flag], ['2D-label', lab2d], ['estático', card], ['detalhe', detail]].forEach(([nm, out]) => {
      if (!out || !stripTags(out).trim()) faltas.push(it.itemId + ':' + nm + ' vazio');
    });
    // o equivalente textual em si tem de aparecer em 3D (acessível), estático e detalhe
    if (!present(flag, te)) faltas.push(it.itemId + ':3D sem equivalente');
    if (!present(card, te)) faltas.push(it.itemId + ':estático sem equivalente');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : smK.items.length + ' itens com equivalente textual em todos os degraus' };
});

test('3D-T3', 'fronteira do ClaimSet idêntica nos 3 degraus; pesos assimétricos; nenhum lado negacionista', () => {
  if (!chic) return { passou: false, detalhe: 'host ausente' };
  const ov = M.overlayFields(chic, smK.porta);
  const cs = ov.claimSetBoundary;
  if (!cs) return { passou: false, detalhe: 'chicxulub deveria hospedar cset:kpg-causa' };
  if (cs.sides.length < 2) return { passou: false, detalhe: 'ClaimSet com <2 lados' };
  const ws = cs.sides.map(s => s.weight);
  if (Math.max(...ws) === Math.min(...ws)) return { passou: false, detalhe: 'pesos achatados (falsa equivalência)' };
  const neg = cs.sides.find(s => NEGACIONISMO.test(s.stmt));
  if (neg) return { passou: false, detalhe: 'lado negacionista exibido: ' + neg.stmt };
  const surf = fullSurfaces(ov, chic);
  const faltas = [];
  [cs.tema, cs.noeq, ...cs.sides.map(s => s.stmt), ...cs.sides.map(s => s.weight.toFixed(2))].forEach(tok => {
    if (!present(surf.detail, tok)) faltas.push('detalhe:«' + tok + '»');
    if (!present(surf.static, tok)) faltas.push('estático:«' + tok + '»');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : 'fronteira (tema+' + cs.sides.length + ' lados+pesos+noeq) idêntica em detalhe/estático' };
});

test('3D-T4', 'item de tempo profundo: reconstructionFlag + AnachronismNotice nos 3 degraus; nenhum como foto/fato', () => {
  const deep = smK.items.filter(i => i.reconstructionFlag);
  if (!deep.length) return { passou: false, detalhe: 'nenhum item com reconstructionFlag no K-Pg (esperado ≥1: chicxulub)' };
  const faltas = [];
  deep.forEach(it => {
    const ov = M.overlayFields(it, smK.porta);
    if (!ov.anachronismNotice) { faltas.push(it.itemId + ':sem AnachronismNotice'); return; }
    const surf = fullSurfaces(ov, it);
    if (!present(surf.detail, 'reconstrução')) faltas.push(it.itemId + ':detalhe sem "reconstrução"');
    if (!present(surf.static, 'reconstrução')) faltas.push(it.itemId + ':estático sem "reconstrução"');
    if (!present(surf.detail, ov.anachronismNotice)) faltas.push(it.itemId + ':detalhe sem nota');
    if (!present(surf.static, ov.anachronismNotice)) faltas.push(it.itemId + ':estático sem nota');
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : deep.length + ' itens de reconstrução com aviso em detalhe/estático' };
});

test('3D-T5', 'sem-WebGL: 2D→estático preserva TODOS os campos do OverlayModel (piso não perde nada)', () => {
  // O piso estático deve conter tudo que o painel (3D/2D) contém: nenhuma perda na queda.
  const faltas = [];
  smK.items.forEach(it => {
    const ov = M.overlayFields(it, smK.porta);
    const detail = M.overlayDetailHTML(ov, it);
    const card = M.overlayStaticCardHTML(ov, it);
    tokensOf(ov, it).forEach(tok => {
      if (present(detail, tok) && !present(card, tok)) faltas.push(it.itemId + ':perdeu «' + tok + '» no piso');
    });
  });
  return { passou: faltas.length === 0, detalhe: faltas.length ? faltas.join(', ') : 'piso estático preserva todo campo §8 presente no painel (' + smK.items.length + ' itens)' };
});

report('3D-T (degradação cruzada)');
