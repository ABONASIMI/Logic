/* Logic Academy - lightweight math typesetting (no external dependency).
 * New content uses  {{ ... }}  for inline math written in plain Unicode (¬ ∧ ∨ ⇒ ⇔ ∀ ∃ ⊨ ⊢ …) with
 *   x_1  x_{i+1}  (subscript),  x^2  x^{n}  (superscript),  \bar{...}  (overline = Boolean complement).
 * Legacy content may still contain $...$ / $$...$$ (a small TeX subset is converted).
 * Everything produced is wrapped in dir="ltr" so symbols/parentheses never get reordered inside Persian (RTL) text.
 */
(function () {
  'use strict';
  var Logic = (window.Logic = window.Logic || {});
  var M = (Logic.math = {});

  var TEX = {
    'Rightarrow': '⇒', 'Leftrightarrow': '⇔', 'implies': '⟹', 'iff': '⟺', 'land': '∧', 'wedge': '∧', 'lor': '∨', 'vee': '∨', 'neg': '¬', 'lnot': '¬',
    'forall': '∀', 'exists': '∃', 'models': '⊨', 'vdash': '⊢', 'top': '⊤', 'bot': '⊥', 'Box': '□', 'square': '□', 'emptyset': '∅', 'in': '∈', 'notin': '∉',
    'cup': '∪', 'cap': '∩', 'subset': '⊂', 'subseteq': '⊆', 'to': '→', 'rightarrow': '→', 'leftarrow': '←', 'longrightarrow': '⟶', 'mapsto': '↦',
    'equiv': '≡', 'neq': '≠', 'ne': '≠', 'leq': '≤', 'geq': '≥', 'cdot': '·', 'times': '×', 'dots': '…', 'ldots': '…', 'cdots': '⋯', 'quad': '\u2003', 'qquad': '\u2003\u2003',
    'doteq': '≐', 'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'sigma': 'σ', 'Sigma': 'Σ', 'theta': 'θ', 'lambda': 'λ', 'varphi': 'φ', 'phi': 'φ', 'psi': 'ψ', 'omega': 'ω', 'Gamma': 'Γ', 'Delta': 'Δ',
    'langle': '⟨', 'rangle': '⟩', 'lbrace': '{', 'rbrace': '}', '{': '{', '}': '}', ',': '\u2009', ';': '\u2004', ' ': ' ', 'sim': '∼', 'approx': '≈', 'prec': '≺', 'succ': '≻',
    'mathcal': '', 'text': '', 'mathrm': '', 'mathbb': '', 'implies ': '⟹', 'nvDash': '⊭', 'nvdash': '⊬', 'Vdash': '⊩', 'infty': '∞', 'sum': '∑', 'prod': '∏', 'pm': '±', 'circ': '∘', 'varnothing': '∅'
  };

  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  /** convert the body of a math span (our notation + small TeX subset) to HTML */
  M.toHTML = function (src) {
    var s = src;
    // TeX-isms
    s = s.replace(/\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, '($1)⁄($2)');
    s = s.replace(/\\(?:text|mathrm|mathcal|mathbb|mathit|textbf|operatorname)\s*\{([^{}]*)\}/g, '$1');
    s = s.replace(/\\(?:bar|overline)\s*\{([^{}]*)\}/g, '\u0001$1\u0002');
    s = s.replace(/\\(?:bar|overline)\s+([A-Za-z0-9])/g, '\u0001$1\u0002');
    s = s.replace(/\\([A-Za-z]+|[{},; ])/g, function (m, name) { return TEX[name] !== undefined ? TEX[name] : name; });
    var out = '', i = 0;
    while (i < s.length) {
      var c = s[i];
      if (c === '_' || c === '^') {
        var tag = c === '_' ? 'sub' : 'sup', body = '';
        i++;
        if (s[i] === '{') { var depth = 1, j = i + 1; while (j < s.length && depth) { if (s[j] === '{') depth++; else if (s[j] === '}') depth--; j++; } body = s.slice(i + 1, j - 1); i = j; }
        else { var m = /^[A-Za-z0-9+\-]/.exec(s.slice(i)); body = m ? m[0] : ''; i += body.length; }
        out += '<' + tag + '>' + esc(body) + '</' + tag + '>';
      } else if (c === '\u0001') { out += '<span class="ov">'; i++; }
      else if (c === '\u0002') { out += '</span>'; i++; }
      else if (c === '{' || c === '}') { i++; } // stray TeX braces
      else { out += esc(c); i++; }
    }
    return out;
  };

  function span(inner, display) { return '<span class="m' + (display ? ' m-block' : '') + '" dir="ltr">' + M.toHTML(inner) + '</span>'; }

  /** process an HTML string: {{...}} (new), $$...$$ and $...$ (legacy). <pre>/<code>/<script> are left untouched. */
  M.process = function (html) {
    var parts = html.split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>|<script[\s\S]*?<\/script>|<[^>]+>)/g);
    // tags are separate parts; text parts are processed, but math must be matched across text only
    var inCodeDepth = 0;
    return parts.map(function (p, idx) {
      if (idx % 2 === 1) return p; // tag or protected block
      return p
        .replace(/\{\{([\s\S]*?)\}\}/g, function (_, m) { return span(m.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')); })
        .replace(/\$\$([\s\S]+?)\$\$/g, function (_, m) { return span(m, true); })
        .replace(/\$([^$\n]+?)\$/g, function (_, m) { return span(m); });
    }).join('');
  };
})();

