/* Logic Academy - Bilingual Glossary View (Français & فارسی) */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  Logic.views.glossary = {
    render: function () {
      var isFa = Logic.lang === 'fa';
      var glossaryData = Logic.data.glossary || [];

      var node = h('div.page.glossary');

      var header = h('header.page-head',
        h('p.eyebrow', h('a', { href: '#/' }, isFa ? 'صفحه اصلی' : 'Accueil'), ' › ', isFa ? 'واژه‌نامه' : 'Glossaire'),
        h('h1', isFa ? '📖 واژه‌نامه تخصصی منطق ریاضی و کامپیوتری' : '📖 Glossaire Bilingue de Logique Universitaire'),
        h('p.lede', isFa ?
          'تعاریف دقیق ریاضی به همراه ترجمه، مفهوم شهودی و علت پیدایش هر اصطلاح در علوم کامپیوتر به زبان‌های فرانسه و فارسی.' :
          'Définitions formelles, intuitions et explications conceptuelles en français et persan pour maîtriser le vocabulaire universitaire de la Sorbonne.'
        )
      );
      node.appendChild(header);

      var searchBar = h('div', { style: 'margin-bottom:1.5rem;' },
        h('input', {
          type: 'text',
          placeholder: isFa ? '🔍 جستجوی اصطلاح (مثلاً: Atome، FNC، Modèle، Unification)...' : '🔍 Rechercher un terme (ex: Atome, FNC, Modèle, Unification)...',
          style: 'width:100%; padding:10px 14px; border-radius:6px; border:1px solid var(--rule-strong); background:var(--code-bg); color:var(--text); font-family:var(--font-ui); font-size:1rem;'
        })
      );
      node.appendChild(searchBar);

      var grid = h('div', { style: 'display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 450px), 1fr)); gap:1.2rem;' });
      node.appendChild(grid);

      function renderItems(q) {
        grid.innerHTML = '';
        var normQ = Logic.norm(q || '');

        glossaryData.forEach(function (item) {
          if (normQ) {
            var hay = Logic.norm(item.fr + ' ' + item.fa + ' ' + item.def_fr + ' ' + item.def_fa);
            if (hay.indexOf(normQ) < 0) return;
          }

          var card = h('article.wcard', { style: 'gap:0.5rem;' },
            h('div', { style: 'display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--rule); padding-bottom:0.4rem;' },
              h('strong', { style: 'color:var(--accent); font-size:1.05rem;' }, item.fr),
              h('span', { style: 'font-family:var(--font-fa); font-weight:700; color:var(--text); font-size:1rem;' }, item.fa)
            ),
            h('p', { style: 'font-size:0.92rem; margin:0.4rem 0;' }, item.def_fr),
            h('p', { style: 'font-family:var(--font-fa); font-size:0.95rem; line-height:1.7; color:var(--text); background:var(--code-bg); padding:8px; border-radius:4px; margin:0.4rem 0;' }, item.def_fa),
            h('div', { style: 'font-size:0.82rem; color:var(--muted);' },
              h('em', isFa ? '💡 چرا این مفهوم ایجاد شد؟ ' : '💡 Pourquoi cette notion ? '),
              isFa ? item.why_fa : item.why_fr
            )
          );
          grid.appendChild(card);
        });

        if (!grid.children.length) {
          grid.appendChild(h('p.empty', isFa ? 'هیچ اصطلاحی با این واژه یافت نشد.' : 'Aucun terme ne correspond à cette recherche.'));
        }
      }

      searchBar.querySelector('input').oninput = function (e) {
        renderItems(e.target.value);
      };

      renderItems('');

      return { node: node, title: isFa ? 'واژه‌نامه تخصصی' : 'Glossaire Bilingue' };
    }
  };
})();

