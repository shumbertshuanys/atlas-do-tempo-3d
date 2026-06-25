'use strict';
/* =====================================================================
   ATLAS DO TEMPO 3D — MODELO PURO (framework-free, testável em node)
   Fonte ÚNICA do contrato visual §8. Sem DOM, sem THREE.
     - vocabulário epistêmico/domínio (CT/DOMAINS) + helpers puros
     - STAGES (APRESENTAÇÃO, não corpus) + stageForScalar
     - fromStaticArray(ITEMS,CLAIMSETS,opts) -> SceneModel   (D-A3.7)
     - overlayFields(item,porta) -> OverlayModel              (§8, fonte única)
     - produtores puros overlay->markup/texto (os 3 renderizadores DESENHAM isto)
   A virada (D-A3.virada) acrescenta fromEnvelope devolvendo o MESMO SceneModel.
   Carregado pelo HTML via <script src> e por node via require (cauda UMD).
   ===================================================================== */

/* TIPO epistêmico → cor + ícone redundante (cor nunca sozinha; §8.2).
   Chaves HIFENIZADAS — iguais ao corpus (nota-descoberta §6.5). */
const CT = {
  'fato-documentado':      { c: '#6fd3ff', g: '▣', n: 'fato documentado' },
  'interpretação':         { c: '#c79bff', g: '◆', n: 'interpretação' },
  'inferência-científica': { c: '#7ee6a8', g: '△', n: 'inferência científica' },
  'proxy':                 { c: '#ffd166', g: '⊚', n: 'proxy' },
  'reconstrução-modelada': { c: '#ff9e6d', g: '◈', n: 'reconstrução modelada' },
  'estimativa':            { c: '#f4a3c6', g: '~', n: 'estimativa' },
  'hipótese':              { c: '#9bb4d6', g: '?', n: 'hipótese' },
  // o schema permite estes (ausentes da carga de 35) — mapeados p/ não cair no fail-loud:
  'medição direta':        { c: '#8fe3ff', g: '▤', n: 'medição direta' },
  'aproximação didática':  { c: '#bcd0ee', g: '≈', n: 'aproximação didática' },
};
/* FAIL-LOUD (R-V2): tipo fora do CT NÃO vira 'hipótese' em silêncio — vira um rótulo
   marcado unknown, vermelho, que mente é IMPOSSÍVEL (o teste falha se aparecer). */
const ctOf = t => CT[t] || { c: '#ff6b6b', g: '!', n: (t || '—') + ' · tipo desconhecido', unknown: true };

const DOMAINS = {
  historia: { nm: 'História', c: '#6fd3ff' }, geologia: { nm: 'Geologia', c: '#ff9e6d' },
  biologia: { nm: 'Biologia', c: '#7ee6a8' }, cosmos: { nm: 'Cosmos', c: '#c79bff' },
  quimica: { nm: 'Química', c: '#ffd166' }, fisica: { nm: 'Física', c: '#f4a3c6' },
  clima: { nm: 'Clima', c: '#79c8d4' },
};
const domOf = d => DOMAINS[d] || { nm: (d || '—') + ' · domínio não mapeado', c: '#9aa3ad', unmapped: true };

/* ESTÁGIOS no eixo do tempo (datum 3Z; T0=2000 CE; t01 normalizado) — APRESENTAÇÃO. */
const STAGES = [
  { id: 'bigbang', t01: 0.00, name: 'Big Bang & recombinação', disp: '~13,8 Ga', scalar: -13.8e9, regime: '1 · cósmico', cam: { r: 46, ph: 1.32, th: 0.0 }, kind: 'cosmic' },
  { id: 'galaxies', t01: 0.20, name: 'Formação de galáxias', disp: '~13 Ga', scalar: -13.0e9, regime: '1 · cósmico', cam: { r: 30, ph: 1.15, th: 0.7 }, kind: 'cosmic' },
  { id: 'sun', t01: 0.42, name: 'Sol & disco protoplanetário', disp: '~4,6 Ga', scalar: -4.6e9, regime: '1 · cósmico', cam: { r: 19, ph: 1.05, th: 1.6 }, kind: 'cosmic' },
  { id: 'earth', t01: 0.54, name: 'Acreção da Terra', disp: '~4,5 Ga', scalar: -4.5e9, regime: '2 · geológico', cam: { r: 6.2, ph: 1.35, th: 2.3 }, kind: 'earth' },
  { id: 'goe', t01: 0.70, name: 'Grande Oxigenação (GOE)', disp: '~2,4 Ga', scalar: -2.4e9, regime: '2 · geológico', cam: { r: 5.0, ph: 1.30, th: 3.5 }, kind: 'earth' },
  { id: 'kpg', t01: 0.90, name: 'Extinção K-Pg', disp: '~66 Ma', scalar: -66e6, regime: '2 · geológico', cam: { r: 4.4, ph: 1.42, th: 4.6 }, kind: 'earth' },
  { id: 's1789', t01: 1.00, name: '1789 — o presente histórico', disp: '1789 CE', scalar: -211, regime: '5 · histórico', cam: { r: 4.0, ph: 1.40, th: 5.4 }, kind: 'earth' },
];
const stageById = id => STAGES.find(s => s.id === id);
/* stageForScalar: liga o canonical_scalar de um item ao estágio de APRESENTAÇÃO
   (mais próximo em escala log — cobre cósmico×terrestre sem privilegiar nenhum). */
function stageForScalar(scalar) {
  const ls = x => Math.log10(Math.abs(x) + 1);
  let best = STAGES[0], bd = Infinity;
  for (const s of STAGES) { const d = Math.abs(ls(scalar) - ls(s.scalar)); if (d < bd) { bd = d; best = s; } }
  return best;
}
/* regimeLabel (D-A3.6): rótulo de cena ESQUEMÁTICA por estágio. Todo asset é
   procedural (shaders/fbm) → SEMPRE reconstrução/representação, NUNCA fotografia
   (R-V7; §8.2; Art.7). O 3D exibe isto de forma persistente; degrada com a cena. */
function regimeLabel(stageId) {
  const s = stageById(stageId);
  if (!s) return null;
  let label;
  if (s.kind === 'cosmic') label = 'representação esquemática do regime cósmico — reconstrução de consenso.';
  else if (s.id === 's1789') label = 'globo esquemático (procedural) — representação cartográfica.';
  else label = 'globo esquemático · paleogeografia reconstruída.';
  return { regime: s.regime, schematic: true, label };
}

/* ---------- helpers de tempo/confiança (puros) ---------- */
function formatYear(sc) {
  const a = Math.abs(sc);
  if (a >= 1e9) return (sc / 1e9).toFixed(2).replace('.', ',') + ' Ga';
  if (a >= 1e6) return (sc / 1e6).toFixed(1).replace('.', ',') + ' Ma';
  const ce = Math.round(2000 + sc);
  return ce > 0 ? ce + ' CE' : (1 - ce) + ' BCE';
}
function fmtScalar(s) {
  if (s <= -1e9) return (s / 1e9).toFixed(2).replace('.', ',') + 'e9 anos';
  if (s <= -1e6) return (s / 1e6).toFixed(1).replace('.', ',') + 'e6 anos';
  return Math.round(s) + ' anos rel. T0';
}
const shortConf = c => ({ alta: 'conf. alta', 'média': 'conf. média', baixa: 'conf. baixa' }[c] || c);
const confPips = c => ({ alta: 3, 'média': 2, baixa: 1 }[c] || 2);

const SEMPRE_ROTULAR = new Set(['reconstrução-modelada', 'hipótese', 'estimativa', 'proxy', 'inferência-científica']);
function uncertaintyDisplayPolicy(epistemicType, porta) {
  if (porta === 'curatorial') return 'aparatoCompleto';
  return SEMPRE_ROTULAR.has(epistemicType) ? 'sempreRotular' : 'rótuloCompacto';
}

const TYPE_BY_PREFIX = { evt: 'Event', concept: 'Concept', proc: 'Process', state: 'State', entity: 'Entity', life: 'Species', geo: 'State', chem: 'State', phys: 'State', rep: 'Representation' };
const typeFromId = id => TYPE_BY_PREFIX[String(id).split(':')[0]] || null;

/* =====================================================================
   SceneItem a partir do array estático (chaves do frame → alvo normalizado)
   ===================================================================== */
function buildSceneItemFromStatic(it) {
  const selo = it.prov === 'seeded-demo' ? 'seeded-demo' : (it.rev === 'pending' ? 'em-revisão' : 'público');
  const reconstructionFlag = !!(it.recon || it.caveat);
  return {
    itemId: it.id, title: it.title, itemType: typeFromId(it.id), domain: it.dom,
    epistemicType: it.ct, confidenceLevel: it.conf, evidenceLevel: null,
    selo, isFact: it.prov === 'corpus' && it.rev === 'approved', reviewStatus: it.rev,
    uncertaintyRange: it.u.slice(),
    uncertaintyDisplayPolicy: null, // preenchido por porta em fromStaticArray
    geometryRegime: it.global ? 'semLugarTerrestre' : (it.recon ? 'paleoPositions' : 'modernGeometry'),
    reconstructionFlag,
    displayPoint: (it.lat != null && it.lng != null) ? { lat: it.lat, lng: it.lng } : null,
    attributionRef: { label: it.src, provenanceRef: null, sourceTier: it.tier || null },
    claimSetRef: it.claimset || null,
    presentationStage: it.stage,
    displayTime: (stageById(it.stage) || {}).disp || null,
    isGlobal: !!it.global, place: it.place || null,
    anachronismNote: reconstructionFlag
      ? (it.caveat ? 'a posição mostrada representa a janela de evidência conhecida, não a paleoposição exata.'
                   : 'a paleogeografia da época difere da geografia de hoje.')
      : null,
    claim: it.claim || null, repr: !!it.repr,
    claimSet: null, // resolvido em fromStaticArray
  };
}

function normalizeClaimSet(ref, cs) {
  if (!cs) return null;
  return {
    claimSetId: ref, host: cs.host, tema: cs.tema,
    sides: (cs.sides || []).map(([stmt, weight]) => ({ stmt, weight })),
    noeq: cs.noeq,
  };
}

/* fromStaticArray — devolve o SceneModel. opts: {stage|stages, porta} */
function fromStaticArray(items, claimsets, opts) {
  opts = opts || {};
  const porta = opts.porta || 'publico';
  const stageSet = opts.stages ? new Set(opts.stages) : (opts.stage ? new Set([opts.stage]) : null);
  let scene = items.map(buildSceneItemFromStatic);
  scene.forEach(si => {
    si.uncertaintyDisplayPolicy = uncertaintyDisplayPolicy(si.epistemicType, porta);
    si.claimSet = si.claimSetRef ? normalizeClaimSet(si.claimSetRef, claimsets[si.claimSetRef]) : null;
  });
  if (stageSet) scene = scene.filter(si => stageSet.has(si.presentationStage));
  // ClaimSets exibíveis: host entre os itens da cena (gating por host — paridade com o envelope)
  const ids = new Set(scene.map(si => si.itemId));
  const claimSets = Object.keys(claimsets)
    .map(ref => normalizeClaimSet(ref, claimsets[ref]))
    .filter(cs => cs && ids.has(cs.host));
  return {
    source: 'static-array', porta,
    stage: opts.stage || null,
    items: scene, claimSets,
  };
}

/* =====================================================================
   overlayFields — §8 NASCE AQUI. Os 3 renderizadores DESENHAM o resultado.
   Não depende de "mode": é função pura de (item, porta).
   ===================================================================== */
function overlayTextualEquivalent(item) {
  const k = ctOf(item.epistemicType);
  const when = item.displayTime || (formatYear(item.uncertaintyRange[0]) + ' a ' + formatYear(item.uncertaintyRange[1]));
  const place = item.isGlobal ? 'global (sem ponto único)' : (item.place || '—');
  return `${k.n} · ${item.title} · ${when} · ${place} · ${shortConf(item.confidenceLevel)}`;
}
function overlayFields(item, porta) {
  const k = ctOf(item.epistemicType);
  const seals = [];
  if (item.selo === 'seeded-demo') seals.push('seeded-demo');
  else if (item.reviewStatus === 'pending' || item.selo === 'em-revisão') seals.push('em-revisão');
  return {
    typeLabel: { glyph: k.g, name: k.n, color: k.c, unknown: !!k.unknown },
    confidence: { pips: confPips(item.confidenceLevel), word: item.confidenceLevel },
    uncertaintyBand: { start: item.uncertaintyRange[0], end: item.uncertaintyRange[1], asRange: true },
    seals,
    attribution: { label: item.attributionRef.label, tier: item.attributionRef.sourceTier, provenanceRef: item.attributionRef.provenanceRef },
    anachronismNotice: item.reconstructionFlag ? (item.anachronismNote || 'reconstrução sobre a base atual.') : null,
    claimSetBoundary: item.claimSet ? { tema: item.claimSet.tema, sides: item.claimSet.sides, noeq: item.claimSet.noeq } : null,
    textualEquivalent: overlayTextualEquivalent(item),
    repr: !!item.repr,
    displayTime: item.displayTime || null,
  };
}

/* =====================================================================
   PRODUTORES PUROS — overlay -> markup/texto. ÚNICA fonte por degrau.
   (sem DOM: devolvem strings; o renderizador só posiciona.)
   ===================================================================== */
function escapeHtml(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

function pipsHTML(n) {
  return [0, 1, 2].map(i => `<span class="pip ${i < n ? 'on' : ''}"></span>`).join('');
}
function ubandHTML(ov) {
  return `<div class="uband"><div class="bar"><div class="span" style="left:8%;right:8%"></div></div>
    <div class="lbl"><span>${escapeHtml(formatYear(ov.uncertaintyBand.start))}</span><span>${escapeHtml(formatYear(ov.uncertaintyBand.end))}</span></div></div>`;
}
function claimSetHTML(cs) {
  if (!cs) return '';
  const max = Math.max(...cs.sides.map(s => s.weight));
  const sides = cs.sides.map(s => `<div class="side"><div class="top">
      <div class="wbar"><div class="wfill" style="width:${Math.round(s.weight / max * 100)}%"></div></div>
      <div class="wnum">${s.weight.toFixed(2)}</div></div><div class="stmt">${escapeHtml(s.stmt)}</div></div>`).join('');
  return `<div class="cset"><div class="cset-h"><span class="lab">ClaimSet</span> ${escapeHtml(cs.tema)}</div>
    ${sides}<div class="noeq"><span>⚖︎</span><span><b>Sem equivalência forçada.</b> ${escapeHtml(cs.noeq)}</span></div></div>`;
}
function noticesHTML(ov) {
  let h = '';
  if (ov.anachronismNotice) h += `<div class="notice anachro"><span class="ic">⟳</span>
    <span><b>Aviso de anacronismo.</b> A posição mostrada é uma <b>reconstrução</b> sobre a base atual; ${escapeHtml(ov.anachronismNotice)}</span></div>`;
  if (ov.seals.includes('seeded-demo')) h += `<div class="notice seedn"><span class="ic">◑</span>
    <span><b>Item de demonstração (seeded-demo).</b> Fonte ainda não validada contra o corpus; <b>excluído do cluster público</b>. Não é promovido a fato sem revisão.</span></div>`;
  if (ov.seals.includes('em-revisão')) h += `<div class="notice pendn"><span class="ic">◔</span>
    <span><b>Em revisão (pending).</b> Exibido com rótulo; não circula no portão público até aprovação. Nunca aparece <i>como</i> fato consolidado.</span></div>`;
  if (ov.repr) h += `<div class="notice pendn"><span class="ic">◇</span>
    <span><b>Representação de cena.</b> Ilustra um regime — não é um ponto-evento georreferenciado nem reivindica objetos individuais.</span></div>`;
  return h;
}
/* PAINEL DE DETALHE — 3D + 2D (compartilham). §8 por inteiro. */
function overlayDetailHTML(ov, item) {
  const k = ov.typeLabel;
  const place = item.isGlobal ? 'global (sem ponto único)' : (item.place || '—');
  const tierCls = item.attributionRef.sourceTier === 'A' ? '' : (item.attributionRef.sourceTier === 'B' ? 'b' : 'demo');
  const tierTxt = item.attributionRef.sourceTier ? ('fonte tier ' + item.attributionRef.sourceTier) : 'sem tier (demonstração)';
  const evid = item.evidenceLevel ? `<div class="meta-k">evidência</div><div class="meta-v">${escapeHtml(item.evidenceLevel)}</div>` : '';
  return `${item.claim ? `<div class="det-claim">${escapeHtml(item.claim)}</div>` : ''}
    <div class="meta-grid">
      <div class="meta-k">tipo</div><div class="meta-v"><span class="typechip" style="background:${k.color}22;color:${k.color}"><span class="g">${k.glyph}</span>${escapeHtml(k.name)}</span></div>
      <div class="meta-k">confiança</div><div class="meta-v"><span class="conf">${pipsHTML(ov.confidence.pips)}</span> &nbsp;<b>${escapeHtml(ov.confidence.word)}</b></div>
      <div class="meta-k">incerteza</div><div class="meta-v">${ubandHTML(ov)}</div>
      <div class="meta-k">domínio</div><div class="meta-v"><b>${escapeHtml(domOf(item.domain).nm)}</b></div>
      <div class="meta-k">lugar</div><div class="meta-v">${escapeHtml(place)}</div>
      <div class="meta-k">proveniência</div><div class="meta-v">${item.selo === 'seeded-demo' ? '<b style="color:var(--seed)">seeded-demo</b>' : (item.isFact ? '<b>corpus</b>' : '<b>' + escapeHtml(item.selo) + '</b>')} · ${escapeHtml(item.reviewStatus)}</div>
      ${evid}
    </div>
    <div class="src">fonte: ${escapeHtml(ov.attribution.label)}<span class="tier ${tierCls}">${tierTxt}</span></div>
    ${noticesHTML(ov)}${claimSetHTML(ov.claimSetBoundary)}
    <div class="txteq" style="margin-top:11px;font-size:10.5px;color:var(--txt-faint)">equivalente textual: ${escapeHtml(ov.textualEquivalent)}</div>`;
}
/* CARTÃO ESTÁTICO — piso de acesso. O equivalente textual É o conteúdo. */
function overlayStaticCardHTML(ov, item) {
  const k = ov.typeLabel;
  const seal = ov.seals.includes('seeded-demo')
    ? `<span class="badge seed" style="font-family:var(--mono);font-size:9px;padding:1px 6px;border-radius:4px;background:rgba(255,179,71,.16);color:#ffb347">seeded-demo</span>`
    : (ov.seals.includes('em-revisão')
      ? `<span class="badge pend" style="font-family:var(--mono);font-size:9px;padding:1px 6px;border-radius:4px;background:rgba(155,180,214,.16);color:#9bb4d6">em revisão</span>` : '');
  const place = item.isGlobal ? 'global (sem ponto único)' : (item.place || '—');
  const csLine = ov.claimSetBoundary
    ? `<div class="row"><span class="k">claimset</span><span>${escapeHtml(ov.claimSetBoundary.tema)} — ${ov.claimSetBoundary.sides.map(s => escapeHtml(s.stmt) + ' (' + s.weight.toFixed(2) + ')').join(' · ')} — pesos assimétricos; ${escapeHtml(ov.claimSetBoundary.noeq)}</span></div>`
    : '';
  const evid = item.evidenceLevel ? `<div class="row"><span class="k">evidência</span><span>${escapeHtml(item.evidenceLevel)}</span></div>` : '';
  const anachro = ov.anachronismNotice ? ` · reconstrução (anacronismo): ${escapeHtml(ov.anachronismNotice)}` : '';
  return `<div class="scard" style="border-left-color:${domOf(item.domain).c}">
    <div class="sc-top">
      <span class="typechip" style="background:${k.color}22;color:${k.color}"><span class="g">${k.glyph}</span>${escapeHtml(k.name)}</span>
      ${seal}<span class="sc-when">${escapeHtml(formatYear(ov.uncertaintyBand.start))} — ${escapeHtml(formatYear(ov.uncertaintyBand.end))}</span>
    </div>
    <div class="sc-title">${escapeHtml(item.title)}</div>
    ${item.claim ? `<div class="sc-claim">${escapeHtml(item.claim)}</div>` : ''}
    <div class="sc-meta">
      <div class="row"><span class="k">confiança</span><span>${pipsStaticHTML(ov.confidence.pips)} ${escapeHtml(ov.confidence.word)}</span></div>
      <div class="row"><span class="k">incerteza</span><span>faixa ${escapeHtml(formatYear(ov.uncertaintyBand.start))} a ${escapeHtml(formatYear(ov.uncertaintyBand.end))} (nunca um ponto)</span></div>
      <div class="row"><span class="k">domínio</span><span>${escapeHtml(domOf(item.domain).nm)}</span></div>
      <div class="row"><span class="k">lugar</span><span>${escapeHtml(place)}${anachro}</span></div>
      <div class="row"><span class="k">proveniência</span><span>${escapeHtml(item.selo)} · ${escapeHtml(item.reviewStatus)}</span></div>
      <div class="row"><span class="k">fonte</span><span>${escapeHtml(ov.attribution.label)}${item.attributionRef.sourceTier ? ' · tier ' + escapeHtml(item.attributionRef.sourceTier) : ''}</span></div>
      ${evid}
      ${csLine}
      <div class="row"><span class="k">equivalente</span><span>${escapeHtml(ov.textualEquivalent)}</span></div>
    </div></div>`;
}
function pipsStaticHTML(n) {
  return [0, 1, 2].map(i => `<span style="display:inline-block;width:11px;height:4px;border-radius:2px;margin-right:2px;background:${i < n ? '#37e0d8' : 'rgba(120,150,200,.2)'}"></span>`).join('');
}
/* BANDEIRA 3D — compacto: glifo + título + conf; + equivalente textual acessível (texto, não atributo). */
function overlay3DFlagHTML(ov, item) {
  const k = ov.typeLabel;
  return `<span style="color:${k.color}">${k.glyph}</span> ${escapeHtml(item.title)} <span class="mini">· ${escapeHtml(shortConf(ov.confidence.word))}</span><span class="sr-only" style="position:absolute;left:-9999px">${escapeHtml(ov.textualEquivalent)}</span>`;
}
/* RÓTULO 2D — texto do canvas (glifo + título). */
function overlay2DLabelText(ov, item) {
  return ov.typeLabel.glyph + ' ' + item.title;
}

/* =====================================================================
   DADOS estáticos (subconjunto curado consistente com o banco) — fonte do
   array enquanto a virada não troca para fromEnvelope. Verbatim do frame.
   ===================================================================== */
const ITEMS = [
  { id: 'rep:bigbang', stage: 'bigbang', dom: 'cosmos', title: 'Recombinação & fundo cósmico', claim: 'Representação do desacoplamento da radiação ~380 mil anos após o início da expansão. Cena ilustrativa do regime cósmico — não um ponto-evento georreferenciado.', ct: 'reconstrução-modelada', conf: 'média', u: [-13.81e9, -13.78e9], prov: 'corpus', rev: 'approved', global: true, src: 'Cosmologia de consenso (representação)', tier: 'B', repr: true },
  { id: 'rep:galaxies', stage: 'galaxies', dom: 'cosmos', title: 'Primeiras galáxias', claim: 'Representação da montagem hierárquica de galáxias no universo jovem. Teaser do regime cósmico; o atlas ainda não reivindica objetos individuais aqui.', ct: 'reconstrução-modelada', conf: 'média', u: [-13.4e9, -12.6e9], prov: 'corpus', rev: 'approved', global: true, src: 'Astrofísica de consenso (representação)', tier: 'B', repr: true },
  { id: 'rep:sun', stage: 'sun', dom: 'cosmos', title: 'Sol e disco protoplanetário', claim: 'Representação da formação do Sol e do disco que origina os planetas. O disco é ilustrativo; a Terra ainda não é um corpo de dados próprio nesta cena.', ct: 'reconstrução-modelada', conf: 'alta', u: [-4.62e9, -4.55e9], prov: 'corpus', rev: 'approved', global: true, src: 'Ciência planetária de consenso (representação)', tier: 'B', repr: true },

  { id: 'proc:goe', stage: 'goe', dom: 'geologia', title: 'Grande Evento de Oxigenação', claim: 'Acúmulo de O₂ livre na atmosfera a partir de ~2,4 Ga, transformando a química de superfície da Terra.', ct: 'inferência-científica', conf: 'alta', u: [-2.5e9, -2.2e9], prov: 'corpus', rev: 'approved', lat: -26, lng: 28, place: 'Cráton do Kaapvaal (registro)', recon: true, src: 'PBDB, geociências', tier: 'A', claimset: 'goe-ritmo' },
  { id: 'proc:fotossintese-oxigenica', stage: 'goe', dom: 'biologia', title: 'Fotossíntese oxigênica', claim: 'Cianobactérias passam a liberar O₂ como subproduto da fotossíntese — a fonte do oxigênio do GOE.', ct: 'inferência-científica', conf: 'alta', u: [-2.7e9, -2.4e9], prov: 'corpus', rev: 'approved', global: true, src: 'PBDB, geomicrobiologia', tier: 'A' },
  { id: 'proc:deposicao-bif', stage: 'goe', dom: 'geologia', title: 'Formações ferríferas bandadas (BIF)', claim: 'Bandas de óxido de ferro precipitam quando o O₂ encontra ferro dissolvido nos oceanos — um proxy do oxigênio crescente.', ct: 'proxy', conf: 'alta', u: [-2.6e9, -2.3e9], prov: 'corpus', rev: 'approved', lat: -22, lng: 119, place: 'Hamersley (registro)', recon: true, src: 'Registro litológico, geociências', tier: 'A' },
  { id: 'state:atmosfera-primitiva', stage: 'goe', dom: 'quimica', title: 'Atmosfera pré-GOE (anóxica)', claim: 'Antes do GOE a atmosfera era essencialmente sem O₂ livre; a transição é modelada a partir de proxies isotópicos.', ct: 'reconstrução-modelada', conf: 'média', u: [-2.5e9, -2.3e9], prov: 'corpus', rev: 'pending', global: true, src: 'Modelos geoquímicos', tier: 'B' },

  { id: 'evt:impacto-chicxulub', stage: 'kpg', dom: 'geologia', title: 'Impacto de Chicxulub', claim: 'Um asteroide de ~10 km atinge a região de Yucatán há ~66 Ma, marcando o limite K-Pg.', ct: 'inferência-científica', conf: 'alta', u: [-66.05e6, -65.95e6], prov: 'corpus', rev: 'approved', lat: 21.4, lng: -89.5, place: 'Cratera de Chicxulub (janela de evidência atual)', recon: true, src: 'USGS, PBDB, geociências', tier: 'A', caveat: true, claimset: 'kpg-causa' },
  { id: 'proc:extincao-kpg', stage: 'kpg', dom: 'biologia', title: 'Extinção em massa K-Pg', claim: 'Cerca de 75% das espécies desaparecem, incluindo os dinossauros não-avianos.', ct: 'inferência-científica', conf: 'alta', u: [-66.0e6, -65.8e6], prov: 'corpus', rev: 'approved', global: true, src: 'PBDB, paleontologia', tier: 'A' },
  { id: 'concept:anomalia-iridio', stage: 'kpg', dom: 'quimica', title: 'Anomalia de irídio', claim: 'Camada global rica em irídio no limite K-Pg — assinatura geoquímica compatível com fonte extraterrestre.', ct: 'proxy', conf: 'alta', u: [-66.0e6, -65.9e6], prov: 'corpus', rev: 'approved', global: true, src: 'Alvarez et al. e replicações, geoquímica', tier: 'A' },
  { id: 'proc:vulcanismo-deccan-traps', stage: 'kpg', dom: 'geologia', title: 'Vulcanismo dos Deccan Traps', claim: 'Erupções maciças na Índia coincidem com o limite K-Pg; seu peso causal está em debate científico ativo.', ct: 'hipótese', conf: 'média', u: [-66.4e6, -65.5e6], prov: 'corpus', rev: 'pending', lat: 18.5, lng: 73.8, place: 'Planalto do Decão (registro)', recon: true, src: 'USGS, geociências', tier: 'A' },

  { id: 'evt:estados-gerais-1789', stage: 's1789', dom: 'historia', title: 'Convocação dos Estados Gerais', claim: 'Em maio de 1789 reúnem-se os Estados Gerais em Versalhes — abertura institucional da Revolução Francesa.', ct: 'fato-documentado', conf: 'alta', u: [-211.1, -210.9], prov: 'corpus', rev: 'approved', lat: 48.80, lng: 2.12, place: 'Versalhes', src: 'Arquivos históricos (A)', tier: 'A', claimset: 'rev-francesa' },
  { id: 'evt:queda-bastilha-1789', stage: 's1789', dom: 'historia', title: 'Queda da Bastilha', claim: '14 de julho de 1789: a tomada da Bastilha torna-se símbolo da Revolução.', ct: 'fato-documentado', conf: 'alta', u: [-210.6, -210.4], prov: 'corpus', rev: 'approved', lat: 48.853, lng: 2.369, place: 'Paris', src: 'Arquivos históricos (A)', tier: 'A' },
  { id: 'evt:declaracao-direitos-1789', stage: 's1789', dom: 'historia', title: 'Declaração dos Direitos do Homem', claim: 'Agosto de 1789: a Assembleia proclama direitos universais — cuja extensão real era limitada à época.', ct: 'fato-documentado', conf: 'alta', u: [-210.5, -210.3], prov: 'corpus', rev: 'pending', lat: 48.86, lng: 2.34, place: 'Paris', src: 'Arquivos históricos (A)', tier: 'A' },
  { id: 'proc:trafico-atlantico', stage: 's1789', dom: 'historia', title: 'Tráfico atlântico de escravizados', claim: 'Em 1789 o tráfico transatlântico está em alta intensidade — pano de fundo material do período, e não nota de rodapé.', ct: 'fato-documentado', conf: 'alta', u: [-212, -209], prov: 'corpus', rev: 'pending', lat: 6.0, lng: -1.5, place: 'Costa da África Ocidental', src: 'Bases historiográficas (A)', tier: 'A' },
  { id: 'evt:inconfidencia-mineira', stage: 's1789', dom: 'historia', title: 'Inconfidência Mineira', claim: '1789, Minas Gerais: movimento de elite colonial contra a Coroa portuguesa; suas leituras divergem.', ct: 'interpretação', conf: 'média', u: [-211.2, -210.8], prov: 'corpus', rev: 'pending', lat: -21.13, lng: -43.42, place: 'Vila Rica (Ouro Preto)', src: 'Historiografia brasileira (A/B)', tier: 'B' },

  { id: 'chem:lavoisier-traite-1789', stage: 's1789', dom: 'quimica', title: 'Tratado de Lavoisier (1789)', claim: 'Publicação do "Traité élémentaire de chimie" — marco da química moderna. Item de demonstração.', ct: 'fato-documentado', conf: 'alta', u: [-211.1, -210.9], prov: 'seeded-demo', rev: 'approved', lat: 48.85, lng: 2.35, place: 'Paris', src: '(demonstração — fonte não validada)', tier: null },
  { id: 'phys:terra-orbita-1789', stage: 's1789', dom: 'fisica', title: 'Mecânica celeste (estado em 1789)', claim: 'A Terra orbita o Sol conforme a mecânica newtoniana — estado do conhecimento físico no instante. Item de demonstração.', ct: 'interpretação', conf: 'alta', u: [-212, -209], prov: 'seeded-demo', rev: 'approved', global: true, src: '(demonstração — fonte não validada)', tier: null },
  { id: 'geo:andes-1789', stage: 's1789', dom: 'geologia', title: 'Cordilheira dos Andes (em 1789)', claim: 'Os Andes já existem como orogênese ativa — escala geológica vista por um instante histórico. Item de demonstração.', ct: 'estimativa', conf: 'média', u: [-213, -208], prov: 'seeded-demo', rev: 'approved', lat: -32, lng: -70, place: 'Andes centrais', recon: false, src: '(demonstração — fonte não validada)', tier: null },
  { id: 'life:grande-auk-1789', stage: 's1789', dom: 'biologia', title: 'Arau-gigante ainda vivo (1789)', claim: 'Em 1789 o arau-gigante (Pinguinus impennis) ainda não estava extinto. Item de demonstração.', ct: 'estimativa', conf: 'média', u: [-213, -208], prov: 'seeded-demo', rev: 'approved', lat: 63, lng: -23, place: 'Atlântico Norte', src: '(demonstração — fonte não validada)', tier: null },
];

const CLAIMSETS = {
  'kpg-causa': { tema: 'Causa dominante da extinção K-Pg', host: 'evt:impacto-chicxulub', sides: [['Impacto de Chicxulub como gatilho dominante', 0.82], ['Vulcanismo dos Deccan como agravante/co-fator', 0.30]], noeq: 'O peso é exibível e assimétrico. Não há simetria visual entre lados de peso desigual; "houve impacto" não é um lado em disputa.' },
  'goe-ritmo': { tema: 'Ritmo da oxigenação (abrupto × gradual)', host: 'proc:goe', sides: [['Transição com pulsos/sobressaltos ("whiffs" e oscilações)', 0.62], ['Subida essencialmente monotônica', 0.38]], noeq: 'Debate sobre o RITMO, não sobre a ocorrência. Que o O₂ subiu não está em disputa.' },
  'rev-francesa': { tema: 'Causas da Revolução Francesa', host: 'evt:estados-gerais-1789', sides: [['Crise fiscal e estrutura social do Antigo Regime', 0.70], ['Circulação de ideias iluministas', 0.55], ['Conjuntura econômica imediata (colheitas, preço do pão)', 0.50]], noeq: 'Causas plurais com pesos próximos — pluralidade não é equivalência forçada nem "dois lados".' },
};

/* =====================================================================
   CAUDA UMD — node (require) e browser (window.AtlasModel)
   ===================================================================== */
const API = {
  CT, DOMAINS, ctOf, domOf, STAGES, stageById, stageForScalar, regimeLabel,
  formatYear, fmtScalar, shortConf, confPips, uncertaintyDisplayPolicy, typeFromId,
  buildSceneItemFromStatic, normalizeClaimSet, fromStaticArray,
  overlayFields, overlayTextualEquivalent,
  overlayDetailHTML, overlayStaticCardHTML, overlay3DFlagHTML, overlay2DLabelText,
  escapeHtml,
  ITEMS, CLAIMSETS,
};
if (typeof module !== 'undefined' && module.exports) module.exports = API;
if (typeof window !== 'undefined') window.AtlasModel = API;
