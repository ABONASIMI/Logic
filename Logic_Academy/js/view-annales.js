/* Logic Academy - Annales Library View (31 Exam Papers / 142 Questions) */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  Logic.views.annales = {
    render: function (rt) {
      var isFa = Logic.lang === 'fa';
      var annalesData = Logic.data.annales || [];

      var node = h('div.page.annales');

      var header = h('header.page-head',
        h('p.eyebrow', h('a', { href: '#/' }, isFa ? 'صفحه اصلی' : 'Accueil'), ' › ', isFa ? 'کتابخانه آزمون‌ها' : 'Annales'),
        h('h1', isFa ? '🏛 آرشیو جامع امتحانات سوربن (۳۱ دوره — ۱۴۲ سؤال)' : '🏛 Bibliothèque Complète des Annales (31 Épreuves — 142 Questions)'),
        h('p.lede', isFa ? 
          'مجموعه کامل آزمون‌های میان‌ترم (Partiel)، پایان‌ترم (Session 1) و شهریور (Session 2) از سال ۲۰۱۵ تا ۲۰۲۳ با حل تشریحی، نکات کلیدی و تطابق با ۱۱ هفته آموزشی.' :
          'Collection exhaustive des examens partiels et terminaux de Sorbonne Université (2015 à 2023). Toutes les questions sont classées par thème avec solutions détaillées et méthodes d\'examen.'
        )
      );
      node.appendChild(header);

      // Filters & Search Box
      var filterBar = h('div', { style: 'background:var(--paper); padding:1.2rem; border-radius:8px; border:1px solid var(--rule); margin-bottom:1.5rem; display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem;' });
      
      var searchInput = h('input', {
        type: 'text',
        placeholder: isFa ? '🔍 جستجوی مفهوم (مثلاً: DPLL، Buveur، Unification)...' : '🔍 Rechercher un concept (ex: DPLL, Buveur, Unification)...',
        style: 'padding:8px 12px; border-radius:5px; border:1px solid var(--rule-strong); background:var(--code-bg); color:var(--text); font-family:var(--font-ui); width:100%;'
      });
      filterBar.appendChild(searchInput);

      var selYear = h('select', { style: 'padding:8px; border-radius:5px; border:1px solid var(--rule-strong); background:var(--code-bg); color:var(--text);' });
      selYear.appendChild(h('option', { value: '' }, isFa ? 'همه سال‌های تحصیلی (۲۰۱۵-۲۰۲۳)' : 'Toutes les années (2015-2023)'));
      ['2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019', '2017-2018', '2016-2017', '2015-2016'].forEach(function (y) {
        selYear.appendChild(h('option', { value: y }, y));
      });
      filterBar.appendChild(selYear);

      var selKind = h('select', { style: 'padding:8px; border-radius:5px; border:1px solid var(--rule-strong); background:var(--code-bg); color:var(--text);' });
      selKind.appendChild(h('option', { value: '' }, isFa ? 'همه انواع آزمون‌ها' : 'Tous les types d\'épreuves'));
      selKind.appendChild(h('option', { value: 'Partiel' }, isFa ? 'آزمون‌های میان‌ترم (Partiel)' : 'Examens Partiels'));
      selKind.appendChild(h('option', { value: 'Session 1' }, isFa ? 'امتحانات نهایی (Session 1)' : 'Examens Terminaux (Session 1)'));
      selKind.appendChild(h('option', { value: 'Session 2' }, isFa ? 'امتحانات جبرانی (Session 2)' : 'Examens Rattrapage (Session 2)'));
      filterBar.appendChild(selKind);

      var selWeek = h('select', { style: 'padding:8px; border-radius:5px; border:1px solid var(--rule-strong); background:var(--code-bg); color:var(--text);' });
      selWeek.appendChild(h('option', { value: '' }, isFa ? 'همه هفته‌های آموزشی' : 'Toutes les semaines'));
      for (var w = 1; w <= 11; w++) {
        selWeek.appendChild(h('option', { value: String(w) }, isFa ? ('هفته ' + w) : ('Semaine ' + w)));
      }
      filterBar.appendChild(selWeek);

      node.appendChild(filterBar);

      // Results container
      var resultsContainer = h('div.annales-results');
      node.appendChild(resultsContainer);

      function updateResults() {
        resultsContainer.innerHTML = '';
        var q = Logic.norm(searchInput.value || '');
        var yr = selYear.value;
        var kd = selKind.value;
        var wk = selWeek.value ? parseInt(selWeek.value, 10) : null;

        var count = 0;

        annalesData.forEach(function (paper) {
          if (yr && paper.year !== yr) return;
          if (kd && paper.kind.indexOf(kd) < 0) return;

          paper.exercises.forEach(function (ex) {
            if (wk && ex.weeks.indexOf(wk) < 0) return;
            if (q) {
              var hay = Logic.norm(paper.file + ' ' + ex.raw_title + ' ' + ex.topics.join(' ') + ' ' + ex.snippet);
              if (hay.indexOf(q) < 0) return;
            }

            count++;
            var annaleKey = paper.file + '#ex' + ex.num;
            var isDone = Logic.store.isAnnaleDone(annaleKey);

            var card = h('div.exo-card',
              h('div.exo-header',
                h('div',
                  h('h3.exo-title', (isFa ? 'تمرین شماره ' : 'Exercice ') + ex.num + ' — ' + (ex.raw_title || (isFa ? 'سؤال آزمون' : 'Question d\'examen'))),
                  h('span', { style: 'font-size:0.8rem; color:var(--muted);' }, '📄 ' + paper.file + ' (p. ' + ex.page + ') · ' + paper.year + ' (' + paper.kind + ' ' + paper.track + ')')
                ),
                h('div.exo-meta-badges',
                  ex.weeks.map(function(w){
                    return h('span.badge.badge-accent', isFa ? ('هفته ' + w) : ('Semaine ' + w));
                  }),
                  ex.topics.map(function(t){
                    return h('span.badge', t);
                  })
                )
              ),
              h('div.exo-statement',
                h('p', { style: 'font-family:var(--font-mono); font-size:0.92rem; background:var(--code-bg); padding:10px; border-radius:5px;' }, ex.snippet + '...')
              ),
              h('div.stepper-actions',
                h('a.btn-step', { href: '#/w0' + (ex.weeks[0] < 10 ? '0' + ex.weeks[0] : ex.weeks[0]) + '/annales' },
                  isFa ? '🔗 مطالعه درس و حل تشریحی در هفته ' + ex.weeks[0] : '🔗 Voir la solution dans la Semaine ' + ex.weeks[0]
                ),
                h('button.btn-step' + (isDone ? ' btn-step-primary' : ''), {
                  onclick: function (e) {
                    var nState = !Logic.store.isAnnaleDone(annaleKey);
                    Logic.store.setAnnaleDone(annaleKey, nState);
                    Logic.toast(isFa ? (nState ? 'آزمون به عنوان حل‌شده ثبت شد' : 'وضعیت لغو شد') : (nState ? 'Exercice marqué comme résolu' : 'Statut réinitialisé'), 'ok');
                    updateResults();
                  }
                }, isDone ? (isFa ? '✓ تسلط کامل (حل‌شده)' : '✓ Résolu (annuler)') : (isFa ? 'نشانه‌گذاری به عنوان حل‌شده' : 'Marquer comme résolu'))
              )
            );

            resultsContainer.appendChild(card);
          });
        });

        if (count === 0) {
          resultsContainer.appendChild(h('p.empty', isFa ? 'هیچ تمرینی با این مشخصات یافت نشد.' : 'Aucun exercice ne correspond aux filtres sélectionnés.'));
        }
      }

      searchInput.oninput = updateResults;
      selYear.onchange = updateResults;
      selKind.onchange = updateResults;
      selWeek.onchange = updateResults;

      updateResults();

      return { node: node, title: isFa ? 'آرشیو آزمون‌ها' : 'Bibliothèque Annales' };
    }
  };
})();

