'use strict';
/* Harness mínimo, framework-free, no estilo dos relatórios verdes do projeto
   (db/migration/*.py emitem JSON {passaram, falharam, testes:[...]}).
   Sem dependências externas; roda em node puro. */

function deepEqual(a, b) {
  if (a === b) return true;
  if (typeof a !== typeof b) return false;
  if (a && b && typeof a === 'object') {
    if (Array.isArray(a) !== Array.isArray(b)) return false;
    const ka = Object.keys(a), kb = Object.keys(b);
    if (ka.length !== kb.length) return false;
    return ka.every(k => deepEqual(a[k], b[k]));
  }
  return false;
}

/* Extrai texto puro de markup HTML (remove tags + DECODIFICA entidades, como o
   textContent de um browser) — para checar que um campo §8 SOBREVIVE num
   renderizador sem depender da estrutura exata das tags nem do escaping. */
function stripTags(html) {
  return String(html)
    .replace(/<[^>]*>/g, ' ')
    .replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ').trim();
}

function makeSuite(prefix) {
  const tests = [];
  function test(id, descricao, fn) {
    let passou = false, detalhe = '';
    try {
      const r = fn();
      if (r && typeof r === 'object' && 'passou' in r) { passou = r.passou; detalhe = r.detalhe || ''; }
      else { passou = r !== false; detalhe = (r && r.detalhe) || ''; }
    } catch (e) {
      passou = false; detalhe = 'EXCEÇÃO: ' + (e && e.message ? e.message : String(e));
    }
    tests.push({ id, descricao, passou, detalhe });
  }
  function report(titulo) {
    const passaram = tests.filter(t => t.passou).length;
    const falharam = tests.length - passaram;
    const out = { suite: titulo, passaram, falharam, testes: tests };
    console.log(JSON.stringify(out, null, 2));
    if (falharam > 0) process.exitCode = 1;
    return out;
  }
  return { test, report };
}

/* assert helpers que devolvem {passou, detalhe} para uso dentro de test() */
function assert(cond, okMsg, failMsg) {
  return { passou: !!cond, detalhe: cond ? (okMsg || 'ok') : (failMsg || 'falhou') };
}

module.exports = { deepEqual, stripTags, makeSuite, assert };
