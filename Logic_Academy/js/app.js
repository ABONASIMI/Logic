/* Logic Academy - Application Shell, Router, Topbar & Offline Handler */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;
  var els = {};

  function parseHash() {
    var hash = (location.hash || '#/').slice(1) || '/';
    var q = '';
    var i = hash.indexOf('?');
    if (i >= 0) { q = hash.slice(i + 1); hash = hash.slice(0, i); }
    var parts = hash.split('/').filter(Boolean).map(function (p) {
      try { return decodeURIComponent(p); } catch (e) { return p; }
    });
    return { parts: parts, query: new URLSearchParams(q), raw: hash };
  }
  Logic.parseHash = parseHash;

  Logic.href = function (path, query) {
    var qs = '';
    if (query) {
      var p = new URLSearchParams();
      Object.keys(query).forEach(function (k) {
        if (query[k] !== undefined && query[k] !== null && query[k] !== '') p.set(k, query[k]);
      });
      qs = p.toString();
    }
    return '#' + path + (qs ? '?' + qs : '');
  };

  Logic.go = function (path, query, replace) {
    var hash = Logic.href(path, query);
    if (replace) history.replaceState(null, '', hash);
    else location.hash = hash;
  };

  function routeFor(r) {
    var p = r.parts;
    if (!p.length) return { name: 'home', key: 'home' };
    var a = p[0];
    if (a === 'annales') return { name: 'annales', key: 'annales' };
    if (a === 'glossary') return { name: 'glossary', key: 'glossary' };
    if (a === 'me') return { name: 'me', key: 'me' };

    // Week route: w01, w02, ..., w11
    if (/^w\d{2}$/.test(a)) {
      return {
        name: 'lesson',
        key: a + (p[1] ? '/' + p[1] : '/cours'),
        week: a,
        section: p[1] || 'cours'
      };
    }

    return { name: 'home', key: 'home' };
  }

  function renderTopbar() {
    var top = els.top;
    if (!top) return;
    Logic.clear(top);
    var isFa = Logic.lang === 'fa';

    var inner = h('div.top-inner',
      h('div.top-brand',
        h('a.brand-link', { href: '#/' },
          h('span.brand-title', isFa ? 'آکادمی منطق سوربن' : 'Logic Academy'),
          h('span.brand-sub', 'UL2IN007')
        )
      ),
      h('nav.top-nav',
        h('a.nav-link', { href: '#/' }, Logic.t('nav.home')),
        h('a.nav-link', { href: '#/annales' }, Logic.t('nav.annales')),
        h('a.nav-link', { href: '#/glossary' }, Logic.t('nav.glossary')),
        h('a.nav-link', { href: '#/me' }, Logic.t('nav.me'))
      ),
      h('div.top-actions',
        // Language switcher
        h('button.btn-step', {
          title: Logic.t('lang.switch'),
          onclick: function () {
            var newLang = Logic.lang === 'fr' ? 'fa' : 'fr';
            Logic.captureScroll();           // remember the heading currently at the top of the viewport
            Logic.store.setLang(newLang);
            applyLanguage(newLang);
            route(true);                     // re-render in the other language WITHOUT jumping to the top
          }
        }, isFa ? '🇫🇷 Français' : '🇦🇫 / 🇮🇷 فارسی'),
        // Theme switcher
        h('button.btn-step', {
          title: Logic.store.getTheme() === 'dark' ? Logic.t('theme.light') : Logic.t('theme.dark'),
          onclick: function () {
            var th = Logic.store.getTheme() === 'dark' ? 'light' : 'dark';
            Logic.store.setTheme(th);
            applyTheme(th);
          }
        }, Logic.store.getTheme() === 'dark' ? '☀️' : '🌙')
      )
    );
    top.appendChild(inner);
  }

  function renderFooter() {
    var foot = els.foot;
    if (!foot) return;
    Logic.clear(foot);
    var isFa = Logic.lang === 'fa';

    var inner = h('div.foot-inner',
      h('p', isFa ?
        'آکادمی جامع منطق ریاضی و کامپیوتری — دانشگاه سوربن (Faculté des Sciences et Ingénierie).' :
        'Logic Academy — Sorbonne Université — Licence 2 d\'Informatique (UL2IN007 / LU2IN007).'
      ),
      h('p', { style: 'font-size:0.82rem; color:var(--muted);' }, isFa ?
        'آموزش عمیق دوزبانه (فرانسوی و فارسی/دری). کاملاً آفلاین و مستقل از اینترنت.' :
        'Manuel interactif bilingue (Français & فارسی). Fonctionne intégralement hors ligne.'
      )
    );
    foot.appendChild(inner);
  }

  function applyLanguage(l) {
    Logic.lang = l;
    document.documentElement.lang = l;
    document.documentElement.dir = Logic.DIR[l] || 'ltr';
    renderTopbar();
    renderFooter();
  }

  function applyTheme(th) {
    document.documentElement.setAttribute('data-theme', th);
  }

  // ---- reading-position preservation (language switch keeps page, section AND scroll position)
  var pending = null;
  Logic.captureScroll = function () {
    var best = null, bestTop = -1e9;
    Logic.$$('.lesson-body [id], .lesson-body .anchor').forEach(function (n) {
      var top = n.getBoundingClientRect().top;
      if (top <= 90 && top > bestTop) { best = n; bestTop = top; }
    });
    pending = best ? { id: best.id, top: bestTop } : { id: null, y: window.scrollY };
  };
  Logic.restoreScroll = function (atId) {
    var p = pending; pending = null;
    if (p && p.id) {
      var n = document.getElementById(p.id);
      if (n) { window.scrollBy(0, n.getBoundingClientRect().top - p.top); return; }
    }
    if (p && p.y !== undefined) { window.scrollTo(0, p.y); return; }
    if (atId) { var t = document.getElementById(atId); if (t) { t.scrollIntoView({ block: 'start' }); } }
  };

  function route(keepScroll) {
    var r = parseHash();
    var target = routeFor(r);
    target.query = r.query;
    var view = Logic.views[target.name] || Logic.views.home;

    var res = view.render(target);
    var app = els.app;
    Logic.clear(app);
    app.appendChild(res.node);
    document.title = (res.title ? res.title + ' – ' : '') + Logic.t('app.title');
    if (keepScroll !== true && !(r.query && r.query.get('at'))) window.scrollTo(0, 0);
  }

  window.addEventListener('DOMContentLoaded', function () {
    els.top = document.getElementById('logic-top');
    els.app = document.getElementById('app');
    els.foot = document.getElementById('logic-foot');

    applyTheme(Logic.store.getTheme());
    applyLanguage(Logic.store.getLang());

    var lastRouteKey = '';
    window.addEventListener('hashchange', function () {
      // in-page anchor updates (?at=…) must not re-render the lesson
      var r = parseHash(), k = routeFor(r).key;
      if (k === lastRouteKey && r.query.get('at')) { lastRouteKey = k; return; }
      lastRouteKey = k; route();
    });
    lastRouteKey = routeFor(parseHash()).key;
    route();

    // Register service worker if available
    if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
      navigator.serviceWorker.register('./sw.js').catch(function(){});
    }
  });
})();

