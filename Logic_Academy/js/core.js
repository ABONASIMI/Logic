/* Logic Academy - core: namespace, data loader, bilingual i18n (FR/FA), DOM helpers, normalization. */
(function () {
  'use strict';
  var Logic = (window.Logic = window.Logic || {});
  Logic.data = {};
  Logic.views = {};
  var waiters = {};
  var inflight = {};

  /** Data bundles call Logic.reg(key, value) when loaded */
  Logic.reg = function (key, value) {
    Logic.data[key] = value;
    var w = waiters[key];
    if (w) { delete waiters[key]; w.forEach(function (f) { f(value); }); }
  };

  Logic.version = function () { return (Logic.data.build && Logic.data.build.version) || '1.0'; };

  /** Load a bundle dynamically */
  Logic.load = function (key, url) {
    if (Logic.data[key] !== undefined) return Promise.resolve(Logic.data[key]);
    if (inflight[key]) return inflight[key];
    var p = new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.async = true;
      s.src = url + '?v=' + Logic.version();
      s.onload = function () {
        if (Logic.data[key] !== undefined) resolve(Logic.data[key]);
        else reject(new Error('bundle ' + key + ' did not register'));
      };
      s.onerror = function () { delete inflight[key]; reject(new Error('cannot load ' + url)); };
      document.head.appendChild(s);
    });
    inflight[key] = p;
    p.catch(function () { delete inflight[key]; });
    return p;
  };

  Logic.loadLesson = function (id, lang) { return Logic.load('lesson:' + id + ':' + lang, 'data/lessons/' + id + '.' + lang + '.js'); };
  Logic.loadGlossary = function () { return Logic.load('glossary', 'data/glossary.js'); };
  Logic.loadAnnales = function () { return Logic.load('annales', 'data/annales.js'); };

  // ---------------------------------------------------------------------------------------------- Languages (French & Persian only)
  Logic.LANGS = ['fr', 'fa'];
  Logic.LANG_LABEL = { fr: 'Français', fa: 'فارسی' };
  Logic.LANG_SHORT = { fr: 'FR', fa: 'فا' };
  Logic.DIR = { fr: 'ltr', fa: 'rtl' };
  Logic.lang = 'fr';

  Logic.t = function (key, vars) {
    var ui = Logic.data.ui || {};
    var s = (ui[Logic.lang] && ui[Logic.lang][key]);
    if (s === undefined) s = ui.fr && ui.fr[key];
    if (s === undefined) s = key;
    if (vars) s = s.replace(/\{(\w+)\}/g, function (_, k) { return vars[k] !== undefined ? vars[k] : ''; });
    return s;
  };

  Logic.tn = function (key, n, vars) {
    vars = vars || {};
    vars.n = n;
    var k = n === 1 || n === 0 ? key + '.one' : key + '.other';
    return Logic.t(k, vars);
  };

  Logic.pick = function (obj, lang) {
    if (!obj) return '';
    lang = lang || Logic.lang;
    return obj[lang] || obj.fr || '';
  };

  // ---------------------------------------------------------------------------------------------- DOM Helpers
  Logic.h = function (spec, attrs) {
    var m = /^([a-z0-9]+)((?:[.#][\w-]+)*)$/i.exec(spec);
    var el = document.createElement(m ? m[1] : spec);
    if (m && m[2]) {
      m[2].replace(/([.#])([\w-]+)/g, function (_, k, v) { if (k === '.') el.classList.add(v); else el.id = v; return ''; });
    }
    var i = 1;
    if (attrs && typeof attrs === 'object' && !(attrs instanceof Node) && !Array.isArray(attrs)) {
      i = 2;
      Object.keys(attrs).forEach(function (k) {
        var v = attrs[k];
        if (v === null || v === undefined || v === false) return;
        if (k.slice(0, 2) === 'on' && typeof v === 'function') el.addEventListener(k.slice(2), v);
        else if (k === 'html') el.innerHTML = v;
        else if (k === 'text') el.textContent = v;
        else if (k === 'class') v.split(/\s+/).forEach(function (c) { if (c) el.classList.add(c); });
        else if (k === 'value') el.value = v;
        else if (k === 'checked' || k === 'selected' || k === 'disabled' || k === 'open') { if (v) el.setAttribute(k, ''); }
        else el.setAttribute(k, v === true ? '' : v);
      });
    }
    for (; i < arguments.length; i++) Logic.append(el, arguments[i]);
    return el;
  };

  Logic.append = function (el, c) {
    if (c === null || c === undefined || c === false) return;
    if (Array.isArray(c)) c.forEach(function (x) { Logic.append(el, x); });
    else if (c instanceof Node) el.appendChild(c);
    else el.appendChild(document.createTextNode(String(c)));
  };

  Logic.esc = function (s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); };
  Logic.clear = function (el) { while (el.firstChild) el.removeChild(el.firstChild); return el; };
  Logic.$ = function (sel, root) { return (root || document).querySelector(sel); };
  Logic.$$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  // ---------------------------------------------------------------------------------------------- Persian/French Normalisation
  var CH = {
    'ي': 'ی', 'ى': 'ی', 'ك': 'ک', 'ۀ': 'ه', 'ة': 'ه',
    'ـ': '', '‌': '', '‍': '', '‎': '', '‏': '', '­': '',
    '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9',
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9',
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', '’': "'", ' ': ' '
  };
  Logic.normChar = function (c) {
    if (CH[c] !== undefined) return CH[c];
    var d = c.normalize('NFD');
    if (d.length > 1) d = d.replace(/[̀-ًͯ-ٰٟۖ-ۭ]/g, '');
    else if (/[ً-ٰٟۖ-ۭ]/.test(d)) d = '';
    return d.toLowerCase();
  };
  Logic.norm = function (s) {
    var out = '';
    for (var i = 0; i < s.length; i++) out += Logic.normChar(s[i]);
    return out;
  };

  // Week meta accessor
  Logic.weekMeta = function (wid) {
    var idx = Logic.data.index;
    return idx && idx.weeks && idx.weeks[wid];
  };

  Logic.lessonMeta = function (id) {
    var idx = Logic.data.index;
    return idx && idx.lessons && idx.lessons[id];
  };
})();

