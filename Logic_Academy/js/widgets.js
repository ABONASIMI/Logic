/* Logic Academy - interactive widgets driven by LogicEngine (real computation, no canned output).
 * Declarative markup inside lesson HTML:
 *   <div class="w-lab"  data-formula="¬p ∧ q ⇒ q ∨ r ∧ q"></div>        full formula laboratory (parse, AST, prefix, truth table, classification)
 *   <div class="w-tt"   data-formula="p ⇒ q"></div>                       truth table (one column per sub-formula)
 *   <div class="w-ast"  data-formula="..."></div>                         syntax tree
 *   <div class="w-eval" data-formula="..." data-i="p=1,q=0"></div>        step-by-step evaluation  [F]^I  (editable valuation)
 *   <div class="w-entail" data-h="p; p ⇒ q" data-f="q"></div>             semantic consequence checker with counter-model
 *   <div class="w-equiv" data-a="..." data-b="..."></div>                 logical equivalence checker
 *   <div class="w-quiz" data-id="w01-quiz"><script type="application/json">{...}</script></div>
 */
(function () {
  'use strict';
  var Logic = (window.Logic = window.Logic || {});
  var E = window.LogicEngine;
  var W = (Logic.widgets = {});
  var SVGNS = 'http://www.w3.org/2000/svg';

  var T = {
    fr: {
      formula: 'Formule', analyse: 'Analyser', parseErr: 'Formule incorrecte : ', ascii: 'Saisie : ¬ ∧ ∨ ⇒ ⇔ ou ~ & | -> <->  (TRUE, FALSE autorisés)',
      full: 'Entièrement parenthésée (convention du cours : sous-formule de droite prioritaire)', minimal: 'Parenthésage minimal', prefix: 'Notation préfixe',
      main: 'Connecteur principal', size: 'Nombre de nœuds', height: 'Hauteur', atoms: 'Atomes', tree: 'Arbre de syntaxe abstraite', table: 'Table de vérité',
      boolexp: 'Expression booléenne [F]^I (algèbre de Boole du cours)', classif: 'Nature de la formule', valid: 'VALIDE (tautologie) : vraie pour toute interprétation',
      satnv: 'SATISFIABLE mais NON valide', unsat: 'INSATISFIABLE : fausse pour toute interprétation', models: 'modèle(s) sur', rows: 'interprétations',
      valuation: 'Interprétation I', evalTitle: 'Évaluation pas à pas (de bas en haut dans l\'arbre)', value: 'valeur', result: 'Résultat',
      hyp: 'Hypothèses H (séparées par « ; »)', concl: 'Conclusion F', check: 'Vérifier H ⊨ F', holds: 'H ⊨ F est VÉRIFIÉE : toute interprétation qui rend vraies toutes les hypothèses rend F vraie.',
      notHolds: 'H ⊨ F est FAUSSE. Contre-modèle (hypothèses vraies, conclusion fausse) : ', equivYes: 'Les deux formules sont logiquement équivalentes (mêmes valeurs sur chaque interprétation).',
      equivNo: 'Non équivalentes. Interprétation qui les distingue : ', checkEq: 'Vérifier l\'équivalence', quizCheck: 'Vérifier mes réponses', quizReset: 'Recommencer', correct: 'Correct', wrong: 'Incorrect',
      score: 'Score', answerAll: 'Répondez d\'abord à toutes les questions.', formulaA: 'Formule A', formulaB: 'Formule B', free: 'sans contrainte', best: 'Meilleur score enregistré'
    },
    fa: {
      formula: 'فرمول', analyse: 'تحلیل', parseErr: 'فرمول نادرست: ', ascii: 'ورودی: ¬ ∧ ∨ ⇒ ⇔ یا ~ & | -> <->  (TRUE و FALSE مجازند)',
      full: 'کاملاً پرانتزگذاری‌شده (قرارداد درس: زیرفرمول راست اولویت دارد)', minimal: 'کمینهٔ پرانتز', prefix: 'نمادگذاری پیشوندی',
      main: 'ترابند (رابط) اصلی', size: 'تعداد گره‌ها', height: 'ارتفاع', atoms: 'اتم‌ها', tree: 'درخت نحو انتزاعی (AST)', table: 'جدول ارزش',
      boolexp: 'عبارت بولی [F]^I (جبر بول درس)', classif: 'ماهیت فرمول', valid: 'معتبر (راست‌گو / توتولوژی): به‌ازای هر تعبیر درست است',
      satnv: 'ارضاپذیر اما نامعتبر', unsat: 'ارضاناپذیر: به‌ازای هر تعبیر نادرست است', models: 'مدل روی', rows: 'تعبیر',
      valuation: 'تعبیر I', evalTitle: 'ارزیابی گام‌به‌گام (از پایین درخت به بالا)', value: 'مقدار', result: 'نتیجه',
      hyp: 'فرض‌ها H (جداشده با «؛»)', concl: 'نتیجه F', check: 'بررسی H ⊨ F', holds: 'H ⊨ F برقرار است: هر تعبیری که همهٔ فرض‌ها را درست کند، F را هم درست می‌کند.',
      notHolds: 'H ⊨ F برقرار نیست. پادمدل (فرض‌ها درست، نتیجه نادرست): ', equivYes: 'دو فرمول هم‌ارز منطقی‌اند (روی هر تعبیر مقدار یکسان دارند).',
      equivNo: 'هم‌ارز نیستند. تعبیری که آن‌ها را از هم جدا می‌کند: ', checkEq: 'بررسی هم‌ارزی', quizCheck: 'بررسی پاسخ‌های من', quizReset: 'شروع دوباره', correct: 'درست', wrong: 'نادرست',
      score: 'امتیاز', answerAll: 'ابتدا به همهٔ پرسش‌ها پاسخ دهید.', formulaA: 'فرمول A', formulaB: 'فرمول B', free: 'بدون قید', best: 'بهترین امتیاز ثبت‌شده'
    }
  };
  function L() { return T[Logic.lang === 'fa' ? 'fa' : 'fr']; }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html !== undefined) e.innerHTML = html; return e; }
  function m(s) { return Logic.math.process('{{' + s + '}}'); }
  function mm(s) { return '<span class="m" dir="ltr">' + Logic.math.toHTML(s) + '</span>'; }
  function svgEl(tag, attrs) { var e = document.createElementNS(SVGNS, tag); Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); }); return e; }
  function bit(b) { return b ? '1' : '0'; }
  function fmtAtom(n) { return n.replace(/^([A-Za-z]+)([0-9]+)$/, '$1_$2'); }
  function fstr(f) { return E.minimal(f).replace(/\b([A-Za-z])([0-9]+)\b/g, '$1_$2'); }
  W.fstr = fstr;

  // ---------------------------------------------------------------- syntax tree (SVG)
  W.astSVG = function (f) {
    var X = 0, nodes = [], edges = [];
    function layout(g, depth) {
      var label, kids = [];
      if (g.t === 'var') label = g.n; else if (g.t === 'const') label = g.v ? '⊤' : '⊥';
      else if (g.t === 'not') { label = '¬'; kids = [g.a]; } else { label = E.SYM[g.t]; kids = [g.l, g.r]; }
      var n = { label: label, depth: depth, kids: [], leaf: kids.length === 0 };
      nodes.push(n);
      kids.forEach(function (k) { n.kids.push(layout(k, depth + 1)); });
      if (n.leaf) { n.x = X; X += 1; }
      else n.x = n.kids.length === 1 ? n.kids[0].x : (n.kids[0].x + n.kids[n.kids.length - 1].x) / 2;
      return n;
    }
    var root = layout(f, 0);
    var maxD = 0; nodes.forEach(function (n) { if (n.depth > maxD) maxD = n.depth; });
    var dx = 54, dy = 56, pad = 28;
    var width = Math.max(1, X) * dx + pad, height = (maxD + 1) * dy + 14;
    var svg = svgEl('svg', { width: width, height: height, viewBox: '0 0 ' + width + ' ' + height, 'class': 'ast-svg', role: 'img' });
    var gE = svgEl('g'), gN = svgEl('g');
    nodes.forEach(function (n) {
      n.px = pad / 2 + n.x * dx + dx / 2 - 0; n.py = n.depth * dy + 24;
    });
    nodes.forEach(function (n) {
      n.kids.forEach(function (k) { gE.appendChild(svgEl('line', { x1: n.px, y1: n.py, x2: k.px, y2: k.py, 'class': 'ast-edge' })); });
    });
    nodes.forEach(function (n) {
      var g = svgEl('g', { 'class': 'ast-node' + (n.leaf ? ' ast-leaf' : '') + (n === root ? ' ast-root' : '') });
      g.appendChild(svgEl('circle', { cx: n.px, cy: n.py, r: 15 }));
      var t = svgEl('text', { x: n.px, y: n.py + 5, 'text-anchor': 'middle' }); t.textContent = n.label; g.appendChild(t);
      gN.appendChild(g);
    });
    svg.appendChild(gE); svg.appendChild(gN);
    return svg;
  };

  // ---------------------------------------------------------------- truth table
  W.truthTableEl = function (f, opts) {
    opts = opts || {};
    var tt = E.truthTable(f), t = L();
    var tbl = el('table', 'truth-table tt-generated');
    var thead = el('thead'), trh = el('tr');
    tt.vars.forEach(function (v) { trh.appendChild(el('th', 'tt-var', mm(fmtAtom(v)))); });
    tt.cols.forEach(function (c, i) { trh.appendChild(el('th', i === tt.cols.length - 1 ? 'tt-final' : '', mm(fstr(c)))); });
    thead.appendChild(trh); tbl.appendChild(thead);
    var tb = el('tbody'), nTrue = 0;
    tt.rows.forEach(function (r) {
      var tr = el('tr');
      tt.vars.forEach(function (v) { tr.appendChild(el('td', 'tt-var', bit(r.I[v]))); });
      r.vals.forEach(function (b, i) { tr.appendChild(el('td', (b ? 'truth-val-true' : 'truth-val-false') + (i === r.vals.length - 1 ? ' tt-final' : ''), bit(b))); });
      if (r.result) nTrue++;
      tb.appendChild(tr);
    });
    tbl.appendChild(tb);
    var wrap = el('div', 'tt-wrap'); wrap.appendChild(tbl);
    var cls = E.classify(f);
    var sum = el('p', 'tt-summary tt-' + cls,
      '<strong>' + (cls === 'valid' ? t.valid : cls === 'unsat' ? t.unsat : t.satnv) + '</strong> — ' + nTrue + '/' + tt.rows.length + ' ' + t.models + ' ' + tt.vars.map(function (v) { return mm(fmtAtom(v)); }).join(', ') + '.');
    wrap.appendChild(sum);
    return wrap;
  };

  // ---------------------------------------------------------------- Boolean-algebra expression, optionally with values substituted
  function boolHTML(b, I, ctx) {
    ctx = ctx || 0;
    switch (b.k) {
      case 'var': return I ? bit(I[b.n]) : 'I(' + fmtAtom(b.n).replace(/_(\d+)/, '<sub>$1</sub>') + ')';
      case 'const': return String(b.v);
      case 'bar': return '<span class="ov">' + boolHTML(b.a, I, 2) + '</span>';
      case 'prod': { var s = boolHTML(b.l, I, 1) + '·' + boolHTML(b.r, I, 1); return ctx >= 1 && ctx !== 2 ? '(' + s + ')' : (ctx === 2 ? s : s); }
      case 'sum': { var t = boolHTML(b.l, I, 0) + ' + ' + boolHTML(b.r, I, 0); return ctx === 1 ? '(' + t + ')' : t; }
    }
  }
  W.boolHTML = boolHTML;

  function parseOrError(box, src) {
    try { return E.parse(src); } catch (e) { box.innerHTML = '<p class="w-err">' + L().parseErr + Logic.esc(e.message) + '</p>'; return null; }
  }
  function parseI(str) { var I = {}; (str || '').split(/[,;\s]+/).forEach(function (p) { var kv = p.split('='); if (kv.length === 2 && kv[0]) I[kv[0]] = kv[1].trim() === '1' || kv[1].trim().toLowerCase() === 'true'; }); return I; }

  // ---------------------------------------------------------------- widgets
  function initTT(node) {
    var f = parseOrError(node, node.getAttribute('data-formula')); if (!f) return;
    node.innerHTML = ''; node.classList.add('w-box');
    node.appendChild(el('div', 'w-title', '📊 ' + L().table + ' — ' + mm(fstr(f))));
    node.appendChild(W.truthTableEl(f));
  }
  function initAST(node) {
    var f = parseOrError(node, node.getAttribute('data-formula')); if (!f) return;
    node.innerHTML = ''; node.classList.add('w-box');
    node.appendChild(el('div', 'w-title', '🌳 ' + L().tree + ' — ' + mm(fstr(f))));
    var sc = el('div', 'ast-scroll'); sc.appendChild(W.astSVG(f)); node.appendChild(sc);
    node.appendChild(el('p', 'w-meta', L().prefix + ' : ' + mm(E.prefix(f))));
  }
  function evalBody(node, f, I) {
    var t = L(), vars = E.vars(f), out = el('div', 'w-evalout');
    out.appendChild(el('div', 'w-sub', '<strong>' + t.evalTitle + '</strong>'));
    var ol = el('ol', 'eval-steps');
    E.subformulas(f).forEach(function (g) {
      var v = E.evalF(g, I);
      ol.appendChild(el('li', null, mm(fstr(g)) + ' = <strong class="' + (v ? 'truth-val-true' : 'truth-val-false') + '">' + bit(v) + '</strong>'));
    });
    if (E.subformulas(f).length === 0) ol.appendChild(el('li', null, mm(fstr(f)) + ' = <strong>' + bit(E.evalF(f, I)) + '</strong>'));
    out.appendChild(ol);
    var b = E.boolExpr(f);
    out.appendChild(el('p', 'w-meta', mm('[' + fstr(f) + ']^I') + ' = <span class="m bool" dir="ltr">' + boolHTML(b, null) + '</span>'));
    out.appendChild(el('p', 'w-meta', '= <span class="m bool" dir="ltr">' + boolHTML(b, I) + '</span> = <strong>' + E.boolEval(b, I) + '</strong>'));
    return out;
  }
  function initEval(node) {
    var f = parseOrError(node, node.getAttribute('data-formula')); if (!f) return;
    var vars = E.vars(f), I = parseI(node.getAttribute('data-i')); vars.forEach(function (v) { if (!(v in I)) I[v] = false; });
    node.innerHTML = ''; node.classList.add('w-box');
    node.appendChild(el('div', 'w-title', '🧮 ' + mm('[' + fstr(f) + ']^I')));
    var ctl = el('div', 'w-controls', '<span>' + L().valuation + ' : </span>');
    var body = el('div');
    vars.forEach(function (v) {
      var lab = el('label', 'w-toggle');
      var cb = el('input'); cb.type = 'checkbox'; cb.checked = I[v];
      cb.addEventListener('change', function () { I[v] = cb.checked; body.innerHTML = ''; body.appendChild(evalBody(node, f, I)); lab.querySelector('.tv').textContent = bit(I[v]); });
      lab.appendChild(cb); lab.appendChild(el('span', 'm', ' I(' + v + ')=')); lab.appendChild(el('span', 'tv', bit(I[v])));
      ctl.appendChild(lab);
    });
    node.appendChild(ctl); node.appendChild(body); body.appendChild(evalBody(node, f, I));
  }
  function initLab(node) {
    var t = L(), start = node.getAttribute('data-formula') || '';
    node.innerHTML = ''; node.classList.add('w-box', 'w-lab-box');
    node.appendChild(el('div', 'w-title', '🔬 ' + t.formula));
    var row = el('div', 'w-controls');
    var inp = el('input', 'w-input'); inp.type = 'text'; inp.value = start; inp.setAttribute('dir', 'ltr'); inp.setAttribute('aria-label', t.formula); inp.spellcheck = false;
    var btn = el('button', 'btn-step btn-step-primary', t.analyse);
    row.appendChild(inp); row.appendChild(btn); node.appendChild(row);
    node.appendChild(el('p', 'w-meta', t.ascii));
    var out = el('div', 'w-labout'); node.appendChild(out);
    function run() {
      out.innerHTML = '';
      var f; try { f = E.parse(inp.value); } catch (e) { out.innerHTML = '<p class="w-err">' + t.parseErr + Logic.esc(e.message) + '</p>'; return; }
      var dl = el('dl', 'w-dl');
      function add(k, v) { dl.appendChild(el('dt', null, k)); dl.appendChild(el('dd', null, v)); }
      add(t.full, mm(E.fullParen(f).replace(/\b([A-Za-z])([0-9]+)\b/g, '$1_$2')));
      add(t.minimal, mm(fstr(f)));
      add(t.prefix, mm(E.prefix(f).replace(/\b([A-Za-z])([0-9]+)\b/g, '$1_$2')));
      add(t.main, f.t === 'var' || f.t === 'const' ? '—' : mm(E.SYM[f.t]));
      add(t.atoms, E.vars(f).map(function (v) { return mm(fmtAtom(v)); }).join(', ') || '—');
      add(t.size + ' / ' + t.height, E.size(f) + ' / ' + E.height(f));
      out.appendChild(dl);
      out.appendChild(el('div', 'w-sub', '<strong>🌳 ' + t.tree + '</strong>'));
      var sc = el('div', 'ast-scroll'); sc.appendChild(W.astSVG(f)); out.appendChild(sc);
      out.appendChild(el('div', 'w-sub', '<strong>📊 ' + t.table + '</strong>'));
      if (E.vars(f).length > 6) out.appendChild(el('p', 'w-err', '≤ 6 atomes'));
      else out.appendChild(W.truthTableEl(f));
      out.appendChild(el('p', 'w-meta', '<strong>' + t.boolexp + '</strong> : ' + mm('[F]^I') + ' = <span class="m bool" dir="ltr">' + boolHTML(E.boolExpr(f), null) + '</span>'));
    }
    btn.addEventListener('click', run); inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') run(); });
    run();
  }
  function initEntail(node) {
    var t = L();
    var hs = node.getAttribute('data-h') || '', fs = node.getAttribute('data-f') || '';
    node.innerHTML = ''; node.classList.add('w-box');
    node.appendChild(el('div', 'w-title', '⊨ ' + t.check));
    var r1 = el('div', 'w-controls'); var h = el('input', 'w-input'); h.value = hs; h.setAttribute('dir', 'ltr'); r1.appendChild(el('span', null, t.hyp + ' : ')); r1.appendChild(h);
    var r2 = el('div', 'w-controls'); var c = el('input', 'w-input'); c.value = fs; c.setAttribute('dir', 'ltr'); r2.appendChild(el('span', null, t.concl + ' : ')); r2.appendChild(c);
    var btn = el('button', 'btn-step btn-step-primary', t.check); var out = el('div', 'w-labout');
    node.appendChild(r1); node.appendChild(r2); node.appendChild(btn); node.appendChild(out);
    function run() {
      out.innerHTML = '';
      try {
        var H = h.value.split(/[;؛]/).map(function (s) { return s.trim(); }).filter(Boolean).map(E.parse), F = E.parse(c.value);
        var r = E.entails(H, F);
        out.appendChild(el('p', r.holds ? 'tt-valid' : 'tt-unsat', r.holds ? t.holds : t.notHolds + mm(E.assignmentString(r.counterModel))));
      } catch (e) { out.innerHTML = '<p class="w-err">' + t.parseErr + Logic.esc(e.message) + '</p>'; }
    }
    btn.addEventListener('click', run); run();
  }
  function initEquiv(node) {
    var t = L();
    node.innerHTML = ''; node.classList.add('w-box');
    var a = el('input', 'w-input'); a.value = node.getAttribute('data-a') || ''; a.setAttribute('dir', 'ltr');
    var b = el('input', 'w-input'); b.value = node.getAttribute('data-b') || ''; b.setAttribute('dir', 'ltr');
    var btn = el('button', 'btn-step btn-step-primary', t.checkEq); var out = el('div', 'w-labout');
    var r1 = el('div', 'w-controls'); r1.appendChild(el('span', null, t.formulaA + ' : ')); r1.appendChild(a);
    var r2 = el('div', 'w-controls'); r2.appendChild(el('span', null, t.formulaB + ' : ')); r2.appendChild(b);
    node.appendChild(el('div', 'w-title', '≡ ' + t.checkEq)); node.appendChild(r1); node.appendChild(r2); node.appendChild(btn); node.appendChild(out);
    function run() {
      out.innerHTML = '';
      try {
        var A = E.parse(a.value), B = E.parse(b.value), vs = E.vars(A).concat(E.vars(B)).filter(function (v, i, arr) { return arr.indexOf(v) === i; }).sort();
        var bad = null; E.interpretations(vs).forEach(function (I) { if (!bad && E.evalF(A, I) !== E.evalF(B, I)) bad = I; });
        out.appendChild(el('p', bad ? 'tt-unsat' : 'tt-valid', bad ? t.equivNo + mm(E.assignmentString(bad)) + ' → ' + mm('[A]=' + bit(E.evalF(A, bad)) + ', [B]=' + bit(E.evalF(B, bad))) : t.equivYes));
      } catch (e) { out.innerHTML = '<p class="w-err">' + t.parseErr + Logic.esc(e.message) + '</p>'; }
    }
    btn.addEventListener('click', run); run();
  }
  function initQuiz(node) {
    var t = L(), spec;
    try { spec = JSON.parse(node.querySelector('script').textContent); } catch (e) { node.innerHTML = '<p class="w-err">quiz JSON</p>'; return; }
    var id = node.getAttribute('data-id') || 'quiz', key = 'logic_quiz_' + id;
    node.innerHTML = ''; node.classList.add('w-box', 'w-quiz-box');
    var best = null; try { best = localStorage.getItem(key); } catch (e) { }
    node.appendChild(el('div', 'w-title', '🎯 Quiz' + (best !== null ? ' — ' + t.best + ' : ' + best + '/' + spec.questions.length : '')));
    var qs = [];
    spec.questions.forEach(function (q, qi) {
      var box = el('div', 'quiz-q'); box.appendChild(el('p', 'quiz-stmt', '<strong>' + (qi + 1) + '.</strong> ' + Logic.math.process(q.q)));
      var opts = el('div', 'quiz-opts');
      q.options.forEach(function (o, oi) {
        var lab = el('label', 'quiz-opt'); var inp = el('input'); inp.type = q.multi ? 'checkbox' : 'radio'; inp.name = id + '-' + qi; inp.value = oi;
        lab.appendChild(inp); lab.appendChild(el('span', null, ' ' + Logic.math.process(o))); opts.appendChild(lab);
      });
      box.appendChild(opts); var fb = el('div', 'quiz-fb'); box.appendChild(fb); node.appendChild(box); qs.push({ q: q, box: box, fb: fb });
    });
    var btn = el('button', 'btn-step btn-step-primary', t.quizCheck), rs = el('button', 'btn-step', t.quizReset), res = el('p', 'quiz-score');
    node.appendChild(btn); node.appendChild(rs); node.appendChild(res);
    btn.addEventListener('click', function () {
      var score = 0, all = true;
      qs.forEach(function (o) {
        var chosen = Array.prototype.map.call(o.box.querySelectorAll('input:checked'), function (i) { return +i.value; }).sort();
        if (!chosen.length) all = false;
      });
      if (!all) { res.textContent = t.answerAll; return; }
      qs.forEach(function (o) {
        var chosen = Array.prototype.map.call(o.box.querySelectorAll('input:checked'), function (i) { return +i.value; }).sort();
        var ans = [].concat(o.q.answer).sort(), ok = JSON.stringify(chosen) === JSON.stringify(ans);
        if (ok) score++;
        o.fb.className = 'quiz-fb ' + (ok ? 'quiz-ok' : 'quiz-ko');
        o.fb.innerHTML = '<strong>' + (ok ? '✓ ' + t.correct : '✗ ' + t.wrong) + '.</strong> ' + Logic.math.process(o.q.why || o.q.explain || '');
      });
      res.innerHTML = '<strong>' + t.score + ' : ' + score + ' / ' + qs.length + '</strong>';
      try { var prev = parseInt(localStorage.getItem(key), 10); if (isNaN(prev) || score > prev) localStorage.setItem(key, String(score)); } catch (e) { }
    });
    rs.addEventListener('click', function () {
      qs.forEach(function (o) { o.fb.innerHTML = ''; o.fb.className = 'quiz-fb'; Array.prototype.forEach.call(o.box.querySelectorAll('input'), function (i) { i.checked = false; }); }); res.textContent = '';
    });
  }

  var REG = { 'w-lab': initLab, 'w-tt': initTT, 'w-ast': initAST, 'w-eval': initEval, 'w-entail': initEntail, 'w-equiv': initEquiv, 'w-quiz': initQuiz };
  W.register = function (cls, fn) { REG[cls] = fn; };
  W.init = function (root) {
    Object.keys(REG).forEach(function (cls) {
      Array.prototype.forEach.call(root.querySelectorAll('.' + cls), function (n) {
        if (n.getAttribute('data-ready')) return;
        n.setAttribute('data-ready', '1');
        try { REG[cls](n); } catch (e) { n.innerHTML = '<p class="w-err">Widget error: ' + Logic.esc(String(e && e.message)) + '</p>'; console.error(e); }
      });
    });
  };
})();

