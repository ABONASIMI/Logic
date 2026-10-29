// Engine tests: node tests/engine.test.js
const assert = require('assert');
const E = require('../js/logic-engine.js');
let n = 0;
function t(name, fn) { try { fn(); n++; console.log('  ok  ' + name); } catch (e) { console.error('FAIL  ' + name + '\n      ' + e.message); process.exitCode = 1; } }
const P = E.parse;

t('right associativity of ∧ (course slide 11)', () => assert.strictEqual(E.fullParen(P('p ∧ q ∧ r ∧ s')), 'p ∧ (q ∧ (r ∧ s))'));
t('right associativity of ⇒', () => assert.strictEqual(E.fullParen(P('A ⇒ B ⇒ C')), 'A ⇒ (B ⇒ C)'));
t('course example ¬A ∨ C ∨ B ∧ C ∨ D', () => assert.strictEqual(E.fullParen(P('¬A ∨ C ∨ B ∧ C ∨ D')), '¬A ∨ (C ∨ ((B ∧ C) ∨ D))'));
t('TD1 Ex1 F2 = ¬p ∧ q ⇒ q ∨ r ∧ q', () => {
  const f = P('¬p ∧ q ⇒ q ∨ r ∧ q');
  assert.strictEqual(E.fullParen(f), '(¬p ∧ q) ⇒ (q ∨ (r ∧ q))');
  assert.strictEqual(E.prefix(f), '⇒ ∧ ¬ p q ∨ q ∧ r q');
});
t('TD1 Ex1 F1 prefix', () => assert.strictEqual(E.prefix(P('¬(p ∧ (q ⇒ ((q ∨ r) ∧ q)))')), '¬ ∧ p ⇒ q ∧ ∨ q r q'));
t('TD1 Ex1 F4 = p ⇒ q ∧ ¬r ⇒ p ∨ q', () => assert.strictEqual(E.fullParen(P('p ⇒ q ∧ ¬r ⇒ p ∨ q')), 'p ⇒ ((q ∧ ¬r) ⇒ (p ∨ q))'));
t('course prefix example', () => assert.strictEqual(E.prefix(P('(p0 ∨ p1) ∧ (p2 ⇒ p3)')), '∧ ∨ p0 p1 ⇒ p2 p3'));
t('course infix example p0 ∨ p1 ∧ p2 ⇒ p3', () => assert.strictEqual(E.fullParen(P('p0 ∨ p1 ∧ p2 ⇒ p3')), '(p0 ∨ (p1 ∧ p2)) ⇒ p3'));
t('minimal printing round-trips', () => {
  ['p ∧ q ∧ r', '(p ∧ q) ∧ r', 'p ⇒ (q ⇒ r)', '(p ⇒ q) ⇒ r', '¬(p ∨ q) ∧ r', '(p ∨ q) ∧ r', 'p ∨ q ∧ r'].forEach(s => {
    const f = P(s); const g = P(E.minimal(f)); assert.ok(E.equal(f, g), s + ' -> ' + E.minimal(f));
  });
  assert.strictEqual(E.minimal(P('(p ∧ q) ∧ r')), '(p ∧ q) ∧ r');
  assert.strictEqual(E.minimal(P('p ∧ (q ∧ r)')), 'p ∧ q ∧ r');
});
t('implication truth table', () => {
  const tt = E.truthTable(P('p ⇒ q')); assert.deepStrictEqual(tt.rows.map(r => r.result), [true, true, false, true]);
});
t('course example (F1∨F2)⇒(F2∧F3) slide 19', () => {
  const tt = E.truthTable(P('(F1 ∨ F2) ⇒ (F2 ∧ F3)'));
  assert.deepStrictEqual(tt.rows.map(r => +r.result), [1, 1, 0, 1, 0, 0, 0, 1]);
});
t('TD1 Ex3 Q1 F=(p∧q)∧((q⇒p)∨¬(p∨q)) is true only at p=q=1', () => {
  const f = P('(p ∧ q) ∧ ((q ⇒ p) ∨ ¬(p ∨ q))'); const tt = E.truthTable(f);
  assert.deepStrictEqual(tt.rows.map(r => +r.result), [0, 0, 0, 1]);
  assert.strictEqual(E.classify(f), 'sat-not-valid');
  assert.ok(E.equivalent(f, P('p ∧ q')));
});
t('TD1 Ex3 Q2 (Anna/Julie): F1=J, F2=J⇒A', () => {
  const F3 = P('J ∨ (J ⇒ A)'), F4 = P('J ∧ (J ⇒ A)');
  assert.strictEqual(E.classify(F3), 'valid');
  assert.deepStrictEqual(E.models(F4, ['A', 'J']).map(I => E.assignmentString(I)), ['A=1, J=1']);
});
t('TD1 Ex3 Q3 (révisions): exactly 3 models; J=1 in all of them; A and X undetermined', () => {
  const H = P('(A ∨ X ∨ J) ∧ (¬A ⇒ ¬X) ∧ (A ⇒ J)');
  const ms = E.models(H, ['A', 'J', 'X']).map(I => E.assignmentString(I)).sort();
  assert.deepStrictEqual(ms, ['A=0, J=1, X=0', 'A=1, J=1, X=0', 'A=1, J=1, X=1']);
  assert.ok(E.entails([H], P('J')).holds);
  assert.ok(!E.entails([H], P('A')).holds); assert.ok(!E.entails([H], P('¬A')).holds);
  assert.ok(!E.entails([H], P('X')).holds); assert.ok(!E.entails([H], P('¬X')).holds);
  assert.ok(E.entails([H], P('X ⇒ A')).holds);
});
t('Ex8 ChatGPT: A∧B is NOT equivalent to ¬((A⇒¬B)∨(¬A⇒B))', () => {
  const F = P('A ∧ B'), G = P('¬((A ⇒ ¬B) ∨ (¬A ⇒ B))');
  assert.strictEqual(E.classify(G), 'unsat'); assert.ok(!E.equivalent(F, G));
});
t('entailment {p, p⇒q} ⊨ q and {p, p∨q} ⊭ q', () => {
  assert.ok(E.entails([P('p'), P('p ⇒ q')], P('q')).holds);
  const r = E.entails([P('p'), P('p ∨ q')], P('q')); assert.ok(!r.holds); assert.deepStrictEqual(r.counterModel, { p: true, q: false });
});
t('De Morgan equivalences', () => {
  assert.ok(E.equivalent(P('¬(p ∨ q)'), P('¬p ∧ ¬q'))); assert.ok(E.equivalent(P('¬(p ∧ q)'), P('¬p ∨ ¬q')));
  assert.ok(!E.equivalent(P('p ⇒ q'), P('q ⇒ p'))); assert.ok(E.equivalent(P('p ⇒ q'), P('¬q ⇒ ¬p')));
});
t('CNF / DNF are equivalent to the original on random formulas', () => {
  const atoms = ['p', 'q', 'r'];
  function rnd(d) {
    if (d === 0 || Math.random() < 0.2) return E.mk.V(atoms[Math.floor(Math.random() * 3)]);
    const k = Math.floor(Math.random() * 5);
    if (k === 0) return E.mk.Not(rnd(d - 1));
    const l = rnd(d - 1), r = rnd(d - 1);
    return [E.mk.And, E.mk.Or, E.mk.Imp, E.mk.Iff][k - 1](l, r);
  }
  for (let i = 0; i < 300; i++) {
    const f = rnd(4), vs = ['p', 'q', 'r'];
    const c = E.cnfFormula(f), d = E.dnfFormula(f), nn = E.nnf(f);
    E.interpretations(vs).forEach(I => { const v = E.evalF(f, I); assert.strictEqual(E.evalF(c, I), v); assert.strictEqual(E.evalF(d, I), v); assert.strictEqual(E.evalF(nn, I), v); });
    // printing round trip
    assert.ok(E.equal(f, P(E.minimal(f))), E.minimal(f));
    assert.ok(E.equal(f, P(E.fullParen(f))));
  }
});
t('boolean algebra view agrees with semantics', () => {
  const f = P('(¬p ∧ q) ⇒ (r ∨ p)'); const b = E.boolExpr(f);
  E.interpretations(['p', 'q', 'r']).forEach(I => assert.strictEqual(E.boolEval(b, I), +E.evalF(f, I)));
});
console.log(n + ' tests passed');
