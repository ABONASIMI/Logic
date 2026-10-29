/* Logic Academy - Lesson & Week Viewer (Textbook Reader Surface) */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  Logic.views.lesson = {
    render: function (rt) {
      var wid = rt.week || 'w01';
      var tab = rt.section || 'cours'; // cours | td | tp | annales | revision
      var wMeta = Logic.weekMeta(wid);
      var isFa = Logic.lang === 'fa';

      var node = h('div.reader-page');
      var reader = h('div.reader');

      // 1. Sidebar Navigation
      var side = h('aside.side');
      var sideTitle = h('div.side-title',
        h('a', { href: '#/' + wid }, isFa ? ('هفته ' + wMeta.num + ' : ' + Logic.pick(wMeta.title)) : ('Semaine ' + wMeta.num + ' : ' + Logic.pick(wMeta.title)))
      );
      side.appendChild(sideTitle);

      var kindTabs = h('div.kind-tabs');
      var sections = [
        { id: 'cours', label: isFa ? '📖 درس' : '📖 Cours' },
        { id: 'td', label: isFa ? '✏️ تمرین TD' : '✏️ TD' },
        { id: 'tp', label: isFa ? '💻 آزمایشگاه TP' : '💻 TP' },
        { id: 'annales', label: isFa ? '🏛 آزمون‌ها' : '🏛 Annales' },
        { id: 'revision', label: isFa ? '🎯 مرور' : '🎯 Révision' }
      ];

      sections.forEach(function (sec) {
        var a = h('a', {
          href: '#/' + wid + '/' + sec.id,
          'aria-current': (tab === sec.id) ? 'true' : 'false'
        }, sec.label);
        kindTabs.appendChild(a);
      });
      side.appendChild(kindTabs);

      // TOC list
      var tocNav = h('nav.toc');
      var tocTitle = h('div.side-title', isFa ? 'فهرست بخش‌های این صفحه' : 'Dans cette section');
      tocNav.appendChild(tocTitle);
      var tocList = h('ul.toc-list');
      tocNav.appendChild(tocList);
      side.appendChild(tocNav);
      reader.appendChild(side);

      // 2. Main Paper Surface
      var paper = h('article.paper', { lang: Logic.lang, dir: Logic.DIR[Logic.lang] });
      
      var lessonHead = h('header.lesson-head');
      var eyebrow = h('p.eyebrow',
        h('a', { href: '#/' }, isFa ? 'خانه' : 'Accueil'),
        ' › ',
        h('a', { href: '#/' + wid }, isFa ? ('هفته ' + wMeta.num) : ('Semaine ' + wMeta.num)),
        ' › ',
        isFa ? ('بخش ' + tab.toUpperCase()) : ('Section ' + tab.toUpperCase())
      );
      lessonHead.appendChild(eyebrow);

      var h1 = h('h1', Logic.pick(wMeta.title) + ' — ' + (
        tab === 'cours' ? (isFa ? 'درس تئوری' : 'Cours Magistral') :
        tab === 'td' ? (isFa ? 'تمرین‌های هدایت‌شده TD' : 'Travaux Dirigés (TD)') :
        tab === 'tp' ? (isFa ? 'کارهای عملی و برنامه‌نویسی TP' : 'Travaux Pratiques (TP)') :
        tab === 'annales' ? (isFa ? 'نمونه سؤالات آزمون‌های سوربن' : 'Questions d\'Annales Ciblées') :
        (isFa ? 'مرور جامع و آزمون آمادگی' : 'Fiche de Révision & Bilan')
      ));
      lessonHead.appendChild(h1);

      var metaBar = h('div', { style: 'font-size:0.84rem; color:var(--muted); margin:0.6rem 0;' },
        '📄 ' + (isFa ? 'منبع رسمی سوربن: ' : 'Source officielle : ') + wMeta.coursSource
      );
      lessonHead.appendChild(metaBar);
      paper.appendChild(lessonHead);

      // Container for dynamic lesson content
      var contentArea = h('div.prose');
      contentArea.innerHTML = '<p class="loading">' + Logic.t('app.loading') + '</p>';
      paper.appendChild(contentArea);

      // Footer controls of lesson: Mark as read + Notes
      var footControls = h('div', { style: 'margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid var(--rule); display:flex; flex-direction:column; gap:1.2rem;' });
      var readBtn = h('button.btn-step', {
        onclick: function () {
          var curr = Logic.store.isRead(wid + '/' + tab);
          Logic.store.setRead(wid + '/' + tab, !curr);
          Logic.toast(isFa ? (!curr ? 'به عنوان خوانده‌شده علامت‌گذاری شد ✓' : 'وضعیت به ناخوانده تغییر یافت') : (!curr ? 'Marqué comme maîtrisé ✓' : 'Statut réinitialisé'), 'ok');
          readBtn.textContent = Logic.store.isRead(wid + '/' + tab) ? (isFa ? '✓ مطالعه‌شده (لغو)' : '✓ Maîtrisé (annuler)') : (isFa ? 'نشانه‌گذاری به عنوان مطالعه‌شده' : 'Marquer comme maîtrisé');
        }
      }, Logic.store.isRead(wid + '/' + tab) ? (isFa ? '✓ مطالعه‌شده (لغو)' : '✓ Maîtrisé (annuler)') : (isFa ? 'نشانه‌گذاری به عنوان مطالعه‌شده' : 'Marquer comme maîtrisé'));
      footControls.appendChild(readBtn);

      // Personal Notes Box
      var notesWrap = h('div');
      var notesLabel = h('strong', { style: 'display:block; margin-bottom:0.4rem; font-size:0.9rem;' }, isFa ? '📝 یادداشت‌های شخصی من برای این بخش:' : '📝 Mes notes personnelles sur cette section :');
      var noteArea = h('textarea', {
        style: 'width:100%; min-height:80px; padding:10px; border-radius:6px; border:1px solid var(--rule); background:var(--code-bg); color:var(--text); font-family:var(--font-ui);',
        placeholder: isFa ? 'یادداشت‌های خود را اینجا وارد کنید (به صورت محلی در مرورگر ذخیره می‌شود)...' : 'Saisissez vos remarques ou points à revoir ici...'
      });
      noteArea.value = Logic.store.getNote(wid + '/' + tab);
      noteArea.oninput = function () {
        Logic.store.setNote(wid + '/' + tab, noteArea.value);
      };
      notesWrap.appendChild(notesLabel);
      notesWrap.appendChild(noteArea);
      footControls.appendChild(notesWrap);

      // Pager (prev week / next week)
      var pager = h('div', { style: 'display:flex; justify-content:space-between; margin-top:1rem;' });
      var currNum = wMeta.num;
      if (currNum > 1) {
        var prevWid = 'w' + (currNum - 1 < 10 ? '0' + (currNum - 1) : (currNum - 1));
        pager.appendChild(h('a.btn-step', { href: '#/' + prevWid + '/' + tab }, isFa ? ('→ هفته ' + (currNum - 1)) : ('← Semaine ' + (currNum - 1))));
      } else {
        pager.appendChild(h('span'));
      }
      if (currNum < 11) {
        var nextWid = 'w' + (currNum + 1 < 10 ? '0' + (currNum + 1) : (currNum + 1));
        pager.appendChild(h('a.btn-step.btn-step-primary', { href: '#/' + nextWid + '/' + tab }, isFa ? ('هفته ' + (currNum + 1) + ' ←') : ('Semaine ' + (currNum + 1) + ' →')));
      }
      footControls.appendChild(pager);

      paper.appendChild(footControls);
      reader.appendChild(paper);
      node.appendChild(reader);

      // Asynchronously load the lesson content for this week and tab
      var lessonKey = wid + '_' + tab;
      Logic.loadLesson(lessonKey, Logic.lang).then(function (lessonData) {
        contentArea.innerHTML = '';
        if (lessonData && lessonData.html) {
          // Honest status banner for unfinished material (never pretend a stub is a full lesson)
          var st = lessonData.status || (Logic.data.status && Logic.data.status[lessonKey]) || 'stub';
          if (st !== 'complete') {
            var msg = isFa
              ? (st === 'partial' ? '⚠️ این بخش ناقص است: فقط بخشی از پرسش‌های رسمی با حل کامل پوشش داده شده‌اند. وضعیت دقیق در FINAL_COVERAGE_REPORT.md آمده است.'
                : '⚠️ این بخش هنوز تکمیل نشده است (خلاصه/پیش‌نویس). به آن برای یادگیری کامل تکیه نکنید. وضعیت دقیق در FINAL_COVERAGE_REPORT.md.')
              : (st === 'partial' ? '⚠️ Section PARTIELLE : seule une partie des questions officielles est corrigée en détail. Voir FINAL_COVERAGE_REPORT.md pour le statut exact.'
                : '⚠️ Section NON TERMINÉE (résumé / brouillon) : ne pas la considérer comme un cours ou une correction complète. Voir FINAL_COVERAGE_REPORT.md.');
            contentArea.appendChild(h('div.status-banner.status-' + st, msg));
          }
          var holder = h('div.lesson-body');
          holder.innerHTML = Logic.math.process(lessonData.html);
          contentArea.appendChild(holder);
          // Build TOC from headings (JS scrolling: the URL hash is reserved for the router)
          var headings = holder.querySelectorAll('h2, h3');
          tocList.innerHTML = '';
          headings.forEach(function (hd, idx) {
            if (!hd.id) hd.id = 'sec-' + idx;
            var a = h('a', { href: Logic.href('/' + wid + '/' + tab, { at: hd.id }) }, hd.textContent);
            a.addEventListener('click', function (ev) {
              ev.preventDefault();
              hd.scrollIntoView({ behavior: 'smooth', block: 'start' });
              Logic.go('/' + wid + '/' + tab, { at: hd.id }, true);
            });
            tocList.appendChild(h('li', { class: hd.tagName.toLowerCase() === 'h3' ? 'toc-l3' : '' }, a));
          });
          // Interactive widgets (real computation) + legacy per-lesson initialiser
          try { Logic.widgets.init(holder); } catch (e) { console.error(e); }
          if (lessonData.initInteractive) {
            try { lessonData.initInteractive(holder, Logic.lang); } catch (e) { console.error(e); }
          }
          if (Logic.restoreScroll) Logic.restoreScroll(rt.query && rt.query.get ? rt.query.get('at') : null);
        } else {
          contentArea.innerHTML = '<p>' + (isFa ? 'محتوای این بخش در حال آماده‌سازی است.' : 'Contenu en cours de finalisation.') + '</p>';
        }
      }).catch(function (err) {
        contentArea.innerHTML = '<p class="empty">' + Logic.t('app.error') + '</p>';
        console.error(err);
      });

      return { node: node, title: Logic.pick(wMeta.title) };
    }
  };
})();

