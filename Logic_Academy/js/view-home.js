/* Logic Academy - Home View (Dashboard of the 11 Weeks) */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  function renderWeekCard(w) {
    var isFa = Logic.lang === 'fa';
    var isRead = Logic.store.isRead(w.id);
    var card = h('article.wcard',
      h('a.wcard-main', { href: '#/' + w.id },
        h('span.wnum', isFa ? ('هفته ' + w.num) : ('Semaine ' + w.num)),
        h('span.wtitle', Logic.pick(w.title)),
        h('span.wcounts', (isFa ? 'درس تئوری · ' : 'Cours · ') + 'TD ' + w.tdExos.length + (isFa ? ' تمرین · ' : ' exos · ') + 'TP ' + w.tpExos.length + (isFa ? ' تمرین' : ' exos'))
      ),
      h('p', { style: 'font-size:0.88rem; color:var(--muted); margin:0.3rem 0;' }, Logic.pick(w.desc)),
      h('div.wprog', Logic.progressBar(isRead ? 1 : 0, Logic.t('progress.label')), h('span.wpct', isRead ? '100 %' : '0 %')),
      h('div.wlinks',
        h('a', { href: '#/' + w.id + '/cours' }, isFa ? '📖 درس' : '📖 Cours'),
        h('a', { href: '#/' + w.id + '/td' }, isFa ? '✏️ تمرین TD' : '✏️ TD'),
        h('a', { href: '#/' + w.id + '/tp' }, isFa ? '💻 آزمایشگاه TP' : '💻 TP'),
        h('a', { href: '#/' + w.id + '/annales' }, isFa ? '🏛 آزمون‌ها' : '🏛 Annales'),
        h('a', { href: '#/' + w.id + '/revision' }, isFa ? '🎯 مرور' : '🎯 Révision')
      )
    );
    return card;
  }

  Logic.views.home = {
    render: function () {
      var isFa = Logic.lang === 'fa';
      var idx = Logic.data.index || {};
      var weeksList = Object.keys(idx.weeks || {}).map(function (k) { return idx.weeks[k]; });

      var node = h('div.page.home',
        h('section.hero',
          h('p.eyebrow', isFa ? 'دانشگاه سوربن — سال تحصیلی ۲۰۲۶–۲۰۲۷' : 'Sorbonne Université — Année 2026–2027'),
          h('h1', Logic.t('home.hero.title')),
          h('p.lede', Logic.t('home.hero.desc')),
          h('div.hero-actions',
            h('a.btn.primary', { href: '#/w01' }, Logic.t('home.start')),
            h('a.btn', { href: '#/annales' }, isFa ? '🏛 آرشیو کامل آزمون‌ها' : '🏛 Bibliothèque Annales'),
            h('a.btn', { href: '#/glossary' }, isFa ? '📖 واژه‌نامه تخصصی' : '📖 Glossaire Bilingue')
          )
        ),
        h('section.weeks',
          h('h2.sec-head', h('span', isFa ? 'برنامه جامع ۱۱ هفته‌ای (UL2IN007)' : 'Cursus Officiel des 11 Semaines (UL2IN007)')),
          h('div.wgrid', weeksList.map(renderWeekCard))
        ),
        h('section.tools-grid',
          h('a.tcard', { href: '#/annales' },
            h('strong', isFa ? '🏛 آرشیو ۳۱ دوره امتحانات سوربن' : '🏛 31 Épreuves d\'Annales'),
            h('span', isFa ? '۱۴۲ سؤال امتحانی از ۲۰۱۵ تا ۲۰۲۳ با حل تشریحی' : '142 exercices classés par thème avec solutions complètes')
          ),
          h('a.tcard', { href: '#/glossary' },
            h('strong', isFa ? '📖 واژه‌نامه تخصصی منطق' : '📖 Glossaire Mathématique Bilingue'),
            h('span', isFa ? 'اصطلاحات فرانسوی به فارسی با تعریف دقیق' : 'Définitions formelles et explications en persan')
          ),
          h('a.tcard', { href: '#/me' },
            h('strong', isFa ? '👤 فضای شخصی و پیشرفت من' : '👤 Mon Espace d\'Étude'),
            h('span', isFa ? 'پیگیری میزان تسلط، یادداشت‌ها و ذخیره‌سازی' : 'Suivi de maîtrise, notes personnelles et sauvegarde')
          )
        )
      );

      return { node: node, title: Logic.t('nav.home') };
    }
  };
})();

