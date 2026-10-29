/* Logic Academy - common UI components & helpers */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  Logic.dot = function (state, label) {
    return h('span.dot', { 'data-state': state, role: 'img', 'aria-label': label || Logic.t('state.' + state) });
  };

  Logic.progressBar = function (frac, label) {
    var f = Math.max(0, Math.min(1, frac || 0));
    return h('span.pbar', {
      role: 'progressbar',
      'aria-valuemin': '0',
      'aria-valuemax': '100',
      'aria-valuenow': String(Math.round(f * 100)),
      'aria-label': label || ''
    }, h('span', { style: 'width:' + (f * 100).toFixed(1) + '%' }));
  };

  Logic.toast = function (msg, kind) {
    var toasts = document.getElementById('logic-toasts');
    if (!toasts) return;
    var t = h('div.toast' + (kind ? '.' + kind : ''), { role: 'status' }, msg);
    toasts.appendChild(t);
    setTimeout(function () {
      t.classList.add('fade');
      setTimeout(function () { if (t.parentNode) t.parentNode.removeChild(t); }, 300);
    }, 2800);
  };

  Logic.sectionHead = function (text, extra) {
    return h('h2.sec-head', h('span', text), extra || null);
  };
})();

