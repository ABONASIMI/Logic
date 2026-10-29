/* Logic Academy - propositional logic engine (parser, evaluation, truth tables, normal forms, entailment).
 * Works in the browser (window.LogicEngine) and in Node (module.exports) so that every solution can be machine-checked.
 * Conventions follow the Sorbonne course (UL2IN007, Cours 1):
 *   priority (strongest first): ¬  ∧  ∨  ⇒  ⇔ ; equal priority: the RIGHT sub-formula has priority,
 *   i.e. every binary connective is right-associative:  A∧B∧C = A∧(B∧C),  A⇒B⇒C = A⇒(B⇒C).
 */
(function (root) {
  'use strict';
  var E = {};

  // ------------------------------------------------------------------ tokenizer
  var OPS = [
    ['<->', 'iff'], ['<=>', 'iff'], ['⇔', 'iff'], ['↔', 'iff'], ['IFF', 'iff'],
    ['=>', 'imp'], ['->', 'imp'], ['⇒', 'imp'], ['→', 'imp'], ['IMPLIES', 'imp'],
    ['∧', 'and'], ['/\\', 'and'], ['&&', 'and'], ['&', 'and'], ['AND', 'and'],
    ['∨', 'or'], ['\\/', 'or'], ['||', 'or'], ['|', 'or'], ['OR', 'or'],
    ['¬', 'not'], ['~', 'not'], ['!', 'not'], ['NOT', 'not']
  ];
  function tokenize(s) {
    var toks = [], i = 0;
    while (i < s.length) {
      var c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if (c === '(' || c === ')') { toks.push({ k: c }); i++; continue; }
      var found = false;
      for (var j = 0; j < OPS.length; j++) {
        var op = OPS[j][0];
        if (s.substr(i, op.length) === op) {
          if (/^[A-Z]+$/.test(op) && /[A-Za-z0-9_]/.test(s[i + op.length] || '')) continue; // keyword must end
          toks.push({ k: OPS[j][1] }); i += op.length; found = true; break;
        }
      }
      if (found) continue;
      if (c === '⊤') { toks.push({ k: 'const', v: true }); i++; continue; }
      if (c === '⊥') { toks.push({ k: 'const', v: false }); i++; continue; }
      var m = /^[A-Za-z_][A-Za-z0-9_']*/.exec(s.slice(i));
      if (m) {
        var w = m[0];
        if (w === 'TRUE' || w === 'true' || w === 'True') toks.push({ k: 'const', v: true });
        else if (w === 'FALSE' || w === 'false' || w === 'False') toks.push({ k: 'const', v: false });
        else toks.push({ k: 'var', v: w });
        i += w.length; continue;
      }
      var d = /^[0-9]+/.exec(s.slice(i));
      if (d) { toks.push({ k: 'var', v: d[0] }); i += d[0].length; continue; }
      throw new Error('Caractère inattendu : « ' + c + ' »');
    }
    return toks;
  }

  // ------------------------------------------------------------------ parser (precedence climbing, right associative)
  E.parse = function (src) {
    var toks = tokenize(src), pos = 0;
    function peek() { return toks[pos]; }
    function eat(k) { var t = toks[pos]; if (!t || (k && t.k !== k)) throw new Error('Syntaxe : attendu ' + (k || 'symbole') + (t ? ' mais trouvé ' + t.k : ' mais fin de formule')); pos++; return t; }
    function binary(level) {
      var kinds = ['iff', 'imp', 'or', 'and'];
      if (level === kinds.length) return unary();
      var k = kinds[level];
      var l = binary(level + 1);
      if (peek() && peek().k === k) { eat(k); var r = binary(level); return { t: k, l: l, r: r }; }
      return l;
    }
    function unary() {
      var t = peek();
      if (!t) throw new Error('Syntaxe : formule incomplète');
      if (t.k === 'not') { eat(); return { t: 'not', a: unary() }; }
      if (t.k === '(') { eat(); var f = binary(0); eat(')'); return f; }
      if (t.k === 'var') { eat(); return { t: 'var', n: t.v }; }
      if (t.k === 'const') { eat(); return { t: 'const', v: t.v }; }
      throw new Error('Syntaxe : symbole inattendu ' + t.k);
    }
    var f = binary(0);
    if (pos < toks.length) throw new Error('Syntaxe : symbole inattendu après la fin de la formule');
    return f;
  };

  // ------------------------------------------------------------------ printing
  var SYM = { not: '¬', and: '∧', or: '∨', imp: '⇒', iff: '⇔' };
  var LEVEL = { iff: 1, imp: 2, or: 3, and: 4, not: 5, var: 6, const: 6 };
  E.SYM = SYM;
  function isBin(f) { return f.t === 'and' || f.t === 'or' || f.t === 'imp' || f.t === 'iff'; }
  E.isBin = isBin;

  /** fully parenthesised string */
  E.full = function (f, top) {
    switch (f.t) {
      case 'var': return f.n;
      case 'const': return f.v ? 'true' : 'false';
      case 'not': return '¬' + E.full(f.a);
      default: var s = E.full(f.l) + ' ' + SYM[f.t] + ' ' + E.full(f.r); return top === false ? '(' + s + ')' : (top === undefined ? s : s);
    }
  };
  E.fullParen = function (f) { // every binary sub-formula parenthesised except the outermost
    function go(g, outer) {
      if (g.t === 'var') return g.n;
      if (g.t === 'const') return g.v ? 'true' : 'false';
      if (g.t === 'not') return '¬' + go(g.a, false);
      var s = go(g.l, false) + ' ' + SYM[g.t] + ' ' + go(g.r, false);
      return outer ? s : '(' + s + ')';
    }
    return go(f, true);
  };
  /** minimal parenthesisation under the course convention (right associativity) */
  E.minimal = function (f) {
    function go(g) {
      if (g.t === 'var') return g.n;
      if (g.t === 'const') return g.v ? 'true' : 'false';
      if (g.t === 'not') return '¬' + (isBin(g.a) ? '(' + go(g.a) + ')' : go(g.a));
      var lp = LEVEL[g.t];
      var ls = go(g.l), rs = go(g.r);
      if (LEVEL[g.l.t] <= lp && isBin(g.l)) ls = '(' + ls + ')';
      if (LEVEL[g.r.t] < lp && isBin(g.r)) rs = '(' + rs + ')';
      return ls + ' ' + SYM[g.t] + ' ' + rs;
    }
    return go(f);
  };
  E.prefix = function (f) {
    switch (f.t) {
      case 'var': return f.n;
      case 'const': return f.v ? 'true' : 'false';
      case 'not': return '¬ ' + E.prefix(f.a);
      default: return SYM[f.t] + ' ' + E.prefix(f.l) + ' ' + E.prefix(f.r);
    }
  };
  E.equal = function (a, b) { return E.fullParen(a) === E.fullParen(b) && a.t === b.t; };

  // ------------------------------------------------------------------ structure
  E.vars = function (f) {
    var seen = {}, out = [];
    (function go(g) {
      if (g.t === 'var') { if (!seen[g.n]) { seen[g.n] = 1; out.push(g.n); } }
      else if (g.t === 'not') go(g.a);
      else if (isBin(g)) { go(g.l); go(g.r); }
    })(f);
    return out.sort();
  };
  E.size = function (f) { return f.t === 'var' || f.t === 'const' ? 1 : f.t === 'not' ? 1 + E.size(f.a) : 1 + E.size(f.l) + E.size(f.r); };
  E.height = function (f) { return f.t === 'var' || f.t === 'const' ? 0 : f.t === 'not' ? 1 + E.height(f.a) : 1 + Math.max(E.height(f.l), E.height(f.r)); };
  E.subformulas = function (f) { // distinct non-atomic subformulas in post-order (as in a truth table)
    var seen = {}, out = [];
    (function go(g) {
      if (g.t === 'var' || g.t === 'const') return;
      if (g.t === 'not') go(g.a); else { go(g.l); go(g.r); }
      var key = E.fullParen(g) + '|' + g.t;
      var s = E.minimal(g);
      if (!seen[s]) { seen[s] = 1; out.push(g); }
    })(f);
    return out;
  };

  // ------------------------------------------------------------------ semantics
  E.evalF = function (f, I) {
    switch (f.t) {
      case 'var': if (!(f.n in I)) throw new Error('Variable sans valeur : ' + f.n); return !!I[f.n];
      case 'const': return f.v;
      case 'not': return !E.evalF(f.a, I);
      case 'and': return E.evalF(f.l, I) && E.evalF(f.r, I);
      case 'or': return E.evalF(f.l, I) || E.evalF(f.r, I);
      case 'imp': return !E.evalF(f.l, I) || E.evalF(f.r, I);
      case 'iff': return E.evalF(f.l, I) === E.evalF(f.r, I);
    }
  };
  E.interpretations = function (vars) { // binary-increasing order, first variable = most significant bit; first row = all 0
    var n = vars.length, out = [];
    for (var i = 0; i < (1 << n); i++) {
      var I = {};
      for (var j = 0; j < n; j++) I[vars[j]] = ((i >> (n - 1 - j)) & 1) === 1;
      out.push(I);
    }
    return out;
  };
  E.truthTable = function (f, extraVars) {
    var vars = E.vars(f);
    if (extraVars) extraVars.forEach(function (v) { if (vars.indexOf(v) < 0) vars.push(v); });
    vars.sort();
    var cols = E.subformulas(f);
    if (cols.length === 0 || E.minimal(cols[cols.length - 1]) !== E.minimal(f)) cols.push(f);
    var rows = E.interpretations(vars).map(function (I) {
      return { I: I, vals: cols.map(function (c) { return E.evalF(c, I); }), result: E.evalF(f, I) };
    });
    return { vars: vars, cols: cols, rows: rows };
  };
  E.models = function (f, vars) { vars = vars || E.vars(f); return E.interpretations(vars).filter(function (I) { return E.evalF(f, I); }); };
  E.isValid = function (f) { return E.interpretations(E.vars(f)).every(function (I) { return E.evalF(f, I); }); };
  E.isSatisfiable = function (f) { return E.interpretations(E.vars(f)).some(function (I) { return E.evalF(f, I); }); };
  E.classify = function (f) { var v = E.isValid(f), s = E.isSatisfiable(f); return v ? 'valid' : (s ? 'sat-not-valid' : 'unsat'); };
  function allVars(fs) { var s = {}; fs.forEach(function (f) { E.vars(f).forEach(function (v) { s[v] = 1; }); }); return Object.keys(s).sort(); }
  /** H ⊨ F ; returns {holds, counterModel} */
  E.entails = function (H, F) {
    var vs = allVars(H.concat([F])), all = E.interpretations(vs);
    for (var i = 0; i < all.length; i++) {
      var I = all[i];
      if (H.every(function (h) { return E.evalF(h, I); }) && !E.evalF(F, I)) return { holds: false, counterModel: I };
    }
    return { holds: true };
  };
  E.equivalent = function (A, B) { return E.entails([A], B).holds && E.entails([B], A).holds; };

  // ------------------------------------------------------------------ boolean-algebra view  [F]^I  (course notation: + , · , overline)
  /** returns a tree of the boolean expression: {k:'var'|'const'|'bar'|'sum'|'prod', ...} */
  E.boolExpr = function (f) {
    switch (f.t) {
      case 'var': return { k: 'var', n: f.n };
      case 'const': return { k: 'const', v: f.v ? 1 : 0 };
      case 'not': return { k: 'bar', a: E.boolExpr(f.a) };
      case 'and': return { k: 'prod', l: E.boolExpr(f.l), r: E.boolExpr(f.r) };
      case 'or': return { k: 'sum', l: E.boolExpr(f.l), r: E.boolExpr(f.r) };
      case 'imp': return { k: 'sum', l: { k: 'bar', a: E.boolExpr(f.l) }, r: E.boolExpr(f.r) };
      case 'iff': return { k: 'sum', l: { k: 'prod', l: { k: 'bar', a: E.boolExpr(f.l) }, r: { k: 'bar', a: E.boolExpr(f.r) } }, r: { k: 'prod', l: E.boolExpr(f.l), r: E.boolExpr(f.r) } };
    }
  };
  E.boolToString = function (b, ctx) { // text with combining overline for complemented atoms, overline-bracket otherwise
    ctx = ctx || 0; // 0 top, 1 inside product, 2 inside bar
    switch (b.k) {
      case 'var': return 'I(' + b.n + ')';
      case 'const': return String(b.v);
      case 'bar':
        if (b.a.k === 'var') return 'Ī(' + b.a.n + ')'.replace('Ī', 'I\u0305');
        if (b.a.k === 'const') return '\u203E' + b.a.v;
        return '‾(' + E.boolToString(b.a, 0) + ')';
      case 'prod': { var s = E.boolToString(b.l, 1) + '·' + E.boolToString(b.r, 1); return ctx >= 1 ? '(' + s + ')' : s; }
      case 'sum': { var t = E.boolToString(b.l, 0) + ' + ' + E.boolToString(b.r, 0); return ctx >= 1 ? '(' + t + ')' : t; }
    }
  };
  /** evaluates a boolean expression tree under I (booleans as 0/1) */
  E.boolEval = function (b, I) {
    switch (b.k) {
      case 'var': return I[b.n] ? 1 : 0;
      case 'const': return b.v;
      case 'bar': return 1 - E.boolEval(b.a, I);
      case 'prod': return E.boolEval(b.l, I) * E.boolEval(b.r, I);
      case 'sum': return Math.max(E.boolEval(b.l, I), E.boolEval(b.r, I));
    }
  };

  // ------------------------------------------------------------------ normal forms
  var V = function (n) { return { t: 'var', n: n }; };
  var Not = function (a) { return { t: 'not', a: a }; };
  var And = function (l, r) { return { t: 'and', l: l, r: r }; };
  var Or = function (l, r) { return { t: 'or', l: l, r: r }; };
  E.mk = { V: V, Not: Not, And: And, Or: Or, Imp: function (l, r) { return { t: 'imp', l: l, r: r }; }, Iff: function (l, r) { return { t: 'iff', l: l, r: r }; } };
  /** eliminate ⇔ and ⇒ */
  E.elimImp = function (f) {
    switch (f.t) {
      case 'var': case 'const': return f;
      case 'not': return Not(E.elimImp(f.a));
      case 'and': return And(E.elimImp(f.l), E.elimImp(f.r));
      case 'or': return Or(E.elimImp(f.l), E.elimImp(f.r));
      case 'imp': return Or(Not(E.elimImp(f.l)), E.elimImp(f.r));
      case 'iff': var a = E.elimImp(f.l), b = E.elimImp(f.r); return And(Or(Not(a), b), Or(Not(b), a));
    }
  };
  /** negation normal form (negations only on atoms) */
  E.nnf = function (f, neg) {
    f = (neg === undefined) ? E.elimImp(f) : f;
    neg = !!neg;
    switch (f.t) {
      case 'var': return neg ? Not(f) : f;
      case 'const': return { t: 'const', v: neg ? !f.v : f.v };
      case 'not': return E.nnf(f.a, !neg);
      case 'and': return neg ? Or(E.nnf(f.l, true), E.nnf(f.r, true)) : And(E.nnf(f.l, false), E.nnf(f.r, false));
      case 'or': return neg ? And(E.nnf(f.l, true), E.nnf(f.r, true)) : Or(E.nnf(f.l, false), E.nnf(f.r, false));
    }
  };
  function distribOr(a, b) { // a,b in CNF
    if (a.t === 'and') return And(distribOr(a.l, b), distribOr(a.r, b));
    if (b.t === 'and') return And(distribOr(a, b.l), distribOr(a, b.r));
    return Or(a, b);
  }
  E.cnfFormula = function (f) {
    var n = E.nnf(f);
    (function check(g) { })(n);
    function go(g) { if (g.t === 'and') return And(go(g.l), go(g.r)); if (g.t === 'or') return distribOr(go(g.l), go(g.r)); return g; }
    return go(n);
  };
  function distribAnd(a, b) { // a,b in DNF
    if (a.t === 'or') return Or(distribAnd(a.l, b), distribAnd(a.r, b));
    if (b.t === 'or') return Or(distribAnd(a, b.l), distribAnd(a, b.r));
    return And(a, b);
  }
  E.dnfFormula = function (f) {
    var n = E.nnf(f);
    function go(g) { if (g.t === 'or') return Or(go(g.l), go(g.r)); if (g.t === 'and') return distribAnd(go(g.l), go(g.r)); return g; }
    return go(n);
  };
  /** literal = {n, pos}; clause = array of literals (sorted, deduplicated); returns null for a tautological clause */
  function litKey(l) { return (l.pos ? '' : '¬') + l.n; }
  E.clausesOfCNF = function (f) {
    var out = [];
    (function conj(g) { if (g.t === 'and') { conj(g.l); conj(g.r); } else out.push(g); })(f);
    var res = [];
    out.forEach(function (c) {
      var lits = [];
      (function dis(g) {
        if (g.t === 'or') { dis(g.l); dis(g.r); }
        else if (g.t === 'var') lits.push({ n: g.n, pos: true });
        else if (g.t === 'not' && g.a.t === 'var') lits.push({ n: g.a.n, pos: false });
        else if (g.t === 'const') lits.push({ c: g.v });
        else throw new Error('Pas en FNC');
      })(c);
      var m = {}, uniq = [], taut = false;
      lits.forEach(function (l) {
        if (l.c !== undefined) { if (l.c) taut = true; return; }
        var k = litKey(l); if (!m[k]) { m[k] = 1; uniq.push(l); }
      });
      uniq.forEach(function (l) { if (m[litKey({ n: l.n, pos: !l.pos })]) taut = true; });
      if (taut) return;
      uniq.sort(function (a, b) { return a.n < b.n ? -1 : a.n > b.n ? 1 : (a.pos === b.pos ? 0 : (a.pos ? -1 : 1)); });
      res.push(uniq);
    });
    return res;
  };
  E.clauseToString = function (c) { return c.length === 0 ? '□' : c.map(litKey).join(' ∨ '); };
  E.litKey = litKey;

  // ------------------------------------------------------------------ misc helpers used by the UI
  E.toHTMLSub = function (s) { return s.replace(/([A-Za-z])([0-9]+)/g, '$1<sub>$2</sub>'); };
  E.assignmentString = function (I) { return Object.keys(I).sort().map(function (k) { return k + '=' + (I[k] ? 1 : 0); }).join(', '); };

  if (typeof module !== 'undefined' && module.exports) module.exports = E;
  else root.LogicEngine = E;
})(typeof window !== 'undefined' ? window : this);

