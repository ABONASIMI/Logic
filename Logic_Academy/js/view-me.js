/* Logic Academy - Personal Space & Progress Tracker View */
(function () {
  'use strict';
  var Logic = window.Logic;
  var h = Logic.h;

  Logic.views.me = {
    render: function () {
      var isFa = Logic.lang === 'fa';
      var st = Logic.store.get();
      var stats = Logic.store.getProgressStats();

      var node = h('div.page.me');

      var header = h('header.page-head',
        h('p.eyebrow', h('a', { href: '#/' }, isFa ? 'صفحه اصلی' : 'Accueil'), ' › ', isFa ? 'فضای من' : 'Mon Espace'),
        h('h1', isFa ? '👤 داشبورد یادگیری و پیگیری تسلط' : '👤 Tableau de Bord & Progression'),
        h('p.lede', isFa ?
          'پیگیری کمی و کیفی میزان پیشرفت در دروس تئوری، تمرین‌های TD، کارهای عملی TP و امتحانات گذشته سوربن.' :
          'Suivez votre avancement dans les 11 semaines du cours, visualisez vos acquis, vos notes personnelles et vos points à réviser.'
        )
      );
      node.appendChild(header);

      // KPI Grid
      var kpiGrid = h('div', { style: 'display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:1rem; margin-bottom:2rem;' },
        kpiCard(isFa ? 'بخش‌های مطالعه‌شده' : 'Sections maîtrisées', stats.readCount + ' / 55', '📖'),
        kpiCard(isFa ? 'تمرین‌های حل‌شده' : 'Questions résolues', stats.tasksCount, '✏️'),
        kpiCard(isFa ? 'سؤالات آزمون مسلط‌شده' : 'Annales réussies', stats.annalesCount + ' / 142', '🏛'),
        kpiCard(isFa ? 'یادداشت‌های ثبت‌شده' : 'Notes rédigées', stats.notesCount, '📝')
      );
      node.appendChild(kpiGrid);

      // Difficult Topics Focus
      var weakSec = h('section',
        h('h2.sec-head', h('span', isFa ? '⚠️ مباحث کلیدی و اولویت‌های آزمون (نیاز به توجه ویژه)' : '⚠️ Sujets Prioritaires & Points d\'Attention')),
        h('div', { style: 'display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem;' },
          weakCard(
            isFa ? 'استنتاج طبیعی در ادوکرا (Edukera)' : 'Déduction Naturelle & Édukera',
            isFa ? 'مدیریت فرضیه‌ها، بستن به موقع باکس‌ها، و تفاوت استنتاج شهودگرایانه با کلاسیک.' : 'Ouverture et décharge des hypothèses, système intuitionniste vs tiers exclu.',
            '#/w05/cours'
          ),
          weakCard(
            isFa ? 'الگوریتم DPLL و انتشار تک‌عضوی' : 'Algorithme DPLL & Propagation Unitaire',
            isFa ? 'ردگیری دقیق شاخه‌ها، اعمال هیوریستیک hk و حذف بندهای راضی‌شده.' : 'Trace formelle de l\'arbre, heuristique hk et règles du littéral pur.',
            '#/w04/cours'
          ),
          weakCard(
            isFa ? 'متغیرهای آزاد و مقید در مرتبه اول (LPPO)' : 'Variables Libres/Liées & Substitutions LPPO',
            isFa ? 'محاسبه Free(F)، بازنام‌گذاری ایمن، و جلوگیری از تله‌اندازی متغیرها.' : 'Calcul rigoureux de Free(F), renommage alphabétique et évitement de capture.',
            '#/w07/cours'
          ),
          weakCard(
            isFa ? 'یکسان‌سازی رابینسون و تحلیل (Resolution)' : 'Unification de Robinson & Résolution',
            isFa ? 'تست وقوع (Occurs-check)، محاسبه MGU و استخراج بند تهی.' : 'Algorithme d\'unification pas à pas, occurs-check et preuve par réfutation.',
            '#/w10/cours'
          )
        )
      );
      node.appendChild(weakSec);

      // Data Backup and Reset Section
      var backupSec = h('section', { style: 'margin-top:2.5rem; background:var(--paper); padding:1.4rem; border-radius:8px; border:1px solid var(--rule);' },
        h('h3', { style: 'margin-top:0;' }, isFa ? '💾 پشتیبان‌گیری و انتقال داده‌ها' : '💾 Sauvegarde & Gestion des Données'),
        h('p', { style: 'font-size:0.9rem; color:var(--muted);' }, isFa ?
          'تمام پیشرفت شما به صورت محلی در حافظه مرورگر ذخیره می‌شود. می‌توانید آن را به صورت یک فایل JSON دانلود کنید تا روی دستگاه دیگری ادامه دهید.' :
          'Toutes vos données sont stockées localement dans votre navigateur. Vous pouvez exporter votre progression dans un fichier JSON.'
        ),
        h('div', { style: 'display:flex; gap:0.8rem; flex-wrap:wrap; margin-top:1rem;' },
          h('button.btn-step.btn-step-primary', {
            onclick: function () {
              var blob = new Blob([Logic.store.exportJSON()], { type: 'application/json' });
              var url = URL.createObjectURL(blob);
              var a = document.createElement('a');
              a.href = url;
              a.download = 'logic-academy-progress.json';
              a.click();
              URL.revokeObjectURL(url);
              Logic.toast(isFa ? 'فایل پشتیبان ذخیره شد ✓' : 'Sauvegarde exportée avec succès ✓', 'ok');
            }
          }, isFa ? '📥 دانلود فایل پشتیبان (Export)' : '📥 Exporter mes données (JSON)'),
          h('button.btn-step', {
            onclick: function () {
              var input = document.createElement('input');
              input.type = 'file';
              input.accept = '.json';
              input.onchange = function (e) {
                var file = e.target.files[0];
                if (!file) return;
                var reader = new FileReader();
                reader.onload = function (ev) {
                  var ok = Logic.store.importJSON(ev.target.result);
                  if (ok) {
                    Logic.toast(isFa ? 'پیشرفت با موفقیت بازیابی شد ✓' : 'Données importées avec succès ✓', 'ok');
                    Logic.go('me');
                  } else {
                    Logic.toast(isFa ? 'فایل نامعتبر است' : 'Fichier de sauvegarde invalide', 'bad');
                  }
                };
                reader.readAsText(file);
              };
              input.click();
            }
          }, isFa ? '📤 بارگذاری فایل پشتیبان (Import)' : '📤 Importer une sauvegarde'),
          h('button.btn-step', {
            style: 'color:var(--bad); border-color:var(--bad);',
            onclick: function () {
              if (confirm(isFa ? 'آیا مطمئن هستید که می‌خواهید تمام پیشرفت خود را بازنشانی کنید؟' : 'Êtes-vous sûr de vouloir réinitialiser toute votre progression ?')) {
                Logic.store.reset();
                Logic.toast(isFa ? 'پیشرفت بازنشانی شد' : 'Progression réinitialisée', 'ok');
                Logic.go('me');
              }
            }
          }, isFa ? '🗑 بازنشانی کامل پیشرفت' : '🗑 Tout réinitialiser')
        )
      );
      node.appendChild(backupSec);

      return { node: node, title: isFa ? 'فضای من' : 'Mon Espace' };
    }
  };

  function kpiCard(title, val, icon) {
    return h('div', { style: 'background:var(--paper); border:1px solid var(--rule); border-radius:8px; padding:1.1rem; display:flex; align-items:center; gap:0.9rem;' },
      h('span', { style: 'font-size:1.8rem;' }, icon),
      h('div',
        h('span', { style: 'display:block; font-size:0.78rem; text-transform:uppercase; color:var(--muted); font-weight:600;' }, title),
        h('strong', { style: 'font-size:1.35rem; color:var(--accent);' }, String(val))
      )
    );
  }

  function weakCard(title, desc, link) {
    var isFa = Logic.lang === 'fa';
    return h('div', { style: 'background:var(--paper); border:1px solid var(--rule); border-radius:8px; padding:1rem; display:flex; flex-direction:column; justify-content:space-between;' },
      h('div',
        h('strong', { style: 'color:var(--accent); font-size:1.02rem; display:block; margin-bottom:0.4rem;' }, title),
        h('p', { style: 'font-size:0.86rem; color:var(--muted); margin:0 0 0.8rem 0; line-height:1.5;' }, desc)
      ),
      h('a.btn-step', { href: link }, isFa ? 'مرور این مبحث ←' : 'Revoir ce concept →')
    );
  }
})();

