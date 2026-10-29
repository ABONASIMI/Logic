import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 5: COURS (FR & FA) - Déduction Naturelle Intuitionniste
# ==============================================================================

c5_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 5 (Déduction Naturelle Intuitionniste)</div>
  <ul>
    <li>Comprendre l'architecture d'une preuve en déduction naturelle (Gentzen) et le formalisme d'Édukera.</li>
    <li>Maîtriser le cycle de vie d'une hypothèse : ouverture d'une boîte, raisonnement local, et <strong>décharge</strong>.</li>
    <li>Appliquer rigoureusement les règles d'introduction et d'élimination des connecteurs : $\\land, \\lor, \\Rightarrow, \\neg, \\bot$.</li>
    <li>Comprendre la différence capitale entre la règle intuitionniste $\\bot E$ (ex falso quodlibet) et le raisonnement par l'absurde classique ($RAA$).</li>
    <li>Rédiger des preuves formelles selon le canevas universitaire : <em>Supposons... → Montrons... → Appliquons... → Conclusion</em>.</li>
  </ul>
</div>

<h2 id="w05-c-principes">1. Anatomie d'un Système de Déduction Naturelle</h2>
<p>
Contrairement aux tables de vérité qui calculent la vérité par énumération exhaustive, la <strong>déduction naturelle</strong> formalise le raisonnement déductif étape par étape à partir d'hypothèses.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 5.1 — Jugement de Déductibilité et Boîtes d'Hypothèses</div>
  <p>Une preuve établit un jugement de la forme : $$\\Gamma \\vdash A$$</p>
  <ul>
    <li>$\\Gamma$ est l'ensemble des <strong>hypothèses actives</strong> (le contexte).</li>
    <li>$A$ est la formule cible (la conclusion ou le but).</li>
    <li><strong>Boîte de preuve (Fitch / Édukera) :</strong> Pour prouver une implication $A \\Rightarrow B$, on ouvre une sous-preuve avec l'hypothèse temporaire $A$. Dès que $B$ est dérivé, la boîte est <strong>fermée</strong> (l'hypothèse $A$ est <em>déchargée</em>) et on conclut $A \\Rightarrow B$ au niveau supérieur. L'hypothèse $A$ n'est plus accessible ensuite !</li>
  </ul>
</div>

<h2 id="w05-c-regles">2. Les Règles Fondamentales de la Logique Intuitionniste</h2>

<div class="box box-definition">
  <div class="box-title">Règles de l'Implication ($\\Rightarrow$)</div>
  <ul>
    <li><strong>Introduction ($\\Rightarrow I$) :</strong> Pour prouver $A \\Rightarrow B$, on suppose $A$ et on prouve $B$. L'hypothèse $A$ est déchargée.
    $$\\frac{[A] \\dots \\vdash B}{\\vdash A \\Rightarrow B} (\\Rightarrow I)$$</li>
    <li><strong>Élimination ($\\Rightarrow E$ / Modus Ponens) :</strong> Si on a $A \\Rightarrow B$ et qu'on a $A$, on en déduit $B$.
    $$\\frac{\\Gamma \\vdash A \\Rightarrow B \\quad \\Gamma \\vdash A}{\\Gamma \\vdash B} (\\Rightarrow E)$$</li>
  </ul>
</div>

<div class="box box-definition">
  <div class="box-title">Règles de la Conjonction ($\\land$)</div>
  <ul>
    <li><strong>Introduction ($\\land I$) :</strong> Si on a $A$ et on a $B$, on en déduit $A \\land B$.</li>
    <li><strong>Élimination ($\\land E_1, \\land E_2$) :</strong> De $A \\land B$, on peut déduire $A$ (élimination gauche) ou $B$ (élimination droite).</li>
  </ul>
</div>

<div class="box box-definition">
  <div class="box-title">Règles de la Disjonction ($\\lor$)</div>
  <ul>
    <li><strong>Introduction ($\\lor I_1, \\lor I_2$) :</strong> De $A$, on peut déduire $A \\lor B$. De $B$, on peut déduire $A \\lor B$.</li>
    <li><strong>Élimination ($\\lor E$ / Raisonnement par cas) :</strong> Si on a $A \\lor B$, et qu'en supposant $A$ on arrive à $C$, et qu'en supposant $B$ on arrive aussi à $C$, alors on a prouvé $C$ sans condition sur $A$ ou $B$ !
    $$\\frac{\\Gamma \\vdash A \\lor B \\quad \\Gamma, [A] \\vdash C \\quad \\Gamma, [B] \\vdash C}{\\Gamma \\vdash C} (\\lor E)$$</li>
  </ul>
</div>

<div class="box box-definition">
  <div class="box-title">Règles de la Négation ($\\neg$) et de l'Absurde Intuitionniste ($\\bot$)</div>
  <p>En logique formelle, la négation $\\neg A$ est une abréviation pour $A \\Rightarrow \\bot$ (supposer $A$ mène à une contradiction impossible).</p>
  <ul>
    <li><strong>Introduction de $\\neg$ ($\\neg I$) :</strong> Si en supposant $A$, on dérive la contradiction $\\bot$, alors on a prouvé $\\neg A$ (décharge de $A$).</li>
    <li><strong>Élimination de $\\neg$ ($\\neg E$) :</strong> Si on a $A$ et $\\neg A$, on en déduit immédiatement la contradiction $\\bot$.</li>
    <li><strong>Élimination du faux intuitionniste ($\\bot E$ / Ex Falso Quodlibet) :</strong> De la contradiction $\\bot$, <strong>on peut déduire N'IMPORTE QUELLE proposition $B$</strong> !
    $$\\frac{\\Gamma \\vdash \\bot}{\\Gamma \\vdash B} (\\bot E)$$</li>
  </ul>
</div>

<div class="box box-example">
  <div class="box-title">Exemple Fondamental Décortiqué — Preuve de $\neg A \Rightarrow (A \Rightarrow B)$</div>
  <p>Voici la démonstration pas à pas exigée à l'examen :</p>
  <ol>
    <li>On veut prouver une implication dont la prémisse est $\\neg A$.<br>
    <strong>Supposons $\\neg A$ (Hypothèse 1).</strong></li>
    <li>Le but restant est $A \\Rightarrow B$, qui est encore une implication.<br>
    <strong>Supposons $A$ (Hypothèse 2).</strong></li>
    <li>On a maintenant l'hypothèse 1 ($\neg A$) et l'hypothèse 2 ($A$) dans notre boîte active.<br>
    <strong>Appliquons la règle $\\neg E$ entre $A$ et $\\neg A$ : on obtient $\\bot$ (contradiction).</strong></li>
    <li>De $\\bot$, appliquons la règle intuitionniste $\\bot E$ : <strong>on déduit $B$ !</strong></li>
    <li>On ferme l'hypothèse 2 ($A$) : par $\\Rightarrow I$, <strong>on conclut $A \\Rightarrow B$.</strong></li>
    <li>On ferme l'hypothèse 1 ($\neg A$) : par $\\Rightarrow I$, <strong>on conclut $\\neg A \\Rightarrow (A \\Rightarrow B)$. Preuve terminée !</strong></li>
  </ol>
</div>
"""

c5_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۵ (استنتاج طبیعی شهودگرایانه)</div>
  <ul>
    <li>درک معماری سیستم استنتاج طبیعی گنتزن و روش ساخت اثبات‌ها در پلتفرم ادوکرا (Édukera).</li>
    <li>تسلط بر چرخه حیات فرضیه‌ها: باز کردن باکس فرضیه، استدلال محلی و <strong>رهاسازی (Décharge)</strong> به‌موقع.</li>
    <li>به‌کارگیری دقیق قواعد معرفی و حذف رابط‌های گزاره‌ای: $\\land, \\lor, \\Rightarrow, \\neg, \\bot$.</li>
    <li>درک تفاوت حیاتی قاعده شهودگرایانه $\\bot E$ (خروج هر چیز از تناقض) با برهان خلف کلاسیک ($RAA$).</li>
    <li>نگارش تشریحی اثبات‌ها مطابق الگوی استاندارد سوربن: <em>فرض می‌کنیم... → نشان می‌دهیم... → قاعده اعمال می‌شود... → نتیجه‌گیری</em>.</li>
  </ul>
</div>

<h2 id="w05-c-principes">۱. ساختار سیستم استنتاج طبیعی و باکس‌های فیتش (Édukera)</h2>
<p>
استنتاج طبیعی روشی است که نحوه استدلال منطقی ذهن ریاضیدانان را بدون نیاز به جدول درستی پیاده‌سازی می‌کند.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۵.۱ — حکم استنتاج و باکس‌های فرضیه</div>
  <p>هر خط اثبات بیانگر یک حکم به صورت $\\Gamma \\vdash A$ است که در آن $\\Gamma$ فرضیه‌های فعال و $A$ حکم اثبات‌شده است.</p>
  <ul>
    <li>برای اثبات یک شرطی مانند $A \\Rightarrow B$، یک باکس جدید باز کرده و $A$ را <strong>فرض</strong> می‌کنیم.</li>
    <li>درون باکس با کمک $A$ تلاش می‌کنیم به $B$ برسیم.</li>
    <li>به محض رسیدن به $B$، باکس بسته می‌شود و فرضیه $A$ رهاسازی می‌گردد؛ در سطح بالاتر حکم $A \\Rightarrow B$ ثبت می‌شود. دیگر در ادامه اثبات حق استفاده مستقیم از $A$ را نداریم!</li>
  </ul>
</div>

<h2 id="w05-c-regles">۲. قواعد معرفی و حذف رابط‌ها در منطق شهودگرایانه</h2>

<div class="box box-definition">
  <div class="box-title">قواعد شرطی ($\\Rightarrow$)</div>
  <ul>
    <li><strong>معرفی شرطی ($\\Rightarrow I$):</strong> برای اثبات $A \\Rightarrow B$، فرضیه $A$ را باز می‌کنیم و به $B$ می‌رسیم.</li>
    <li><strong>حذف شرطی ($\\Rightarrow E$ / قیاس استثنایی Modus Ponens):</strong> اگر $A \\Rightarrow B$ و $A$ را داشته باشیم، $B$ نتیجه می‌شود.</li>
  </ul>
</div>

<div class="box box-definition">
  <div class="box-title">قاعده طلایی تناقض شهودگرایانه ($\\bot E$)</div>
  <p>در منطق شهودگرایانه نقیض $\\neg A$ به صورت $A \\Rightarrow \\bot$ تعریف می‌شود.</p>
  <p>اگر در فرآیند استدلال به تناقض یا گزاره ناممکن $\\bot$ برسیم، طبق قاعده $\\bot E$ (Ex Falso Quodlibet) <strong>می‌توانیم هر گزاره دلخواهی مانند $B$ را نتیجه بگیریم</strong>!</p>
</div>

<div class="box box-example">
  <div class="box-title">مثال تشریحی گام‌به‌گام — اثبات فرمول $\neg A \Rightarrow (A \Rightarrow B)$</div>
  <ol>
    <li>می‌خواهیم یک گزاره شرطی با مقدم $\\neg A$ را اثبات کنیم.<br>
    <strong>فرضیه ۱ را باز می‌کنیم: فرض کنیم $\\neg A$.</strong></li>
    <li>هدف باقیمانده $A \\Rightarrow B$ است که خود یک شرطی است.<br>
    <strong>فرضیه ۲ را باز می‌کنیم: فرض کنیم $A$.</strong></li>
    <li>اکنون در باکس فعال هم $A$ و هم $\\neg A$ را داریم.<br>
    <strong>با اعمال قاعده $\\neg E$، تناقض $\\bot$ به دست می‌آید.</strong></li>
    <li>از تناقض $\\bot$ با اعمال قاعده $\\bot E$، <strong>گزاره $B$ را نتیجه می‌گیریم!</strong></li>
    <li>فرضیه ۲ را می‌بندیم: با قاعده $\\Rightarrow I$، <strong>گزاره $A \\Rightarrow B$ اثبات می‌شود.</strong></li>
    <li>فرضیه ۱ را می‌بندیم: با قاعده $\\Rightarrow I$، <strong>گزاره $\\neg A \\Rightarrow (A \\Rightarrow B)$ به طور کامل اثبات شد!</strong></li>
  </ol>
</div>
"""

make_bundle("w05_cours", "fr", c5_fr)
make_bundle("w05_cours", "fa", c5_fa)

# Week 5 TD
td5_fr = """
<div class="box box-objectives">
  <div class="box-title">TD 5 — Preuves en Déduction Naturelle Intuitionniste</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 11, Thème 5). <strong>Interdiction absolue du tiers exclu et du raisonnement par l'absurde classique !</strong></p>
</div>

<div id="td-exo17-container"></div>
"""

td5_fa = """
<div class="box box-objectives">
  <div class="box-title">تمرین‌های TD 5 — اثبات‌های صوری استنتاج طبیعی شهودگرایانه</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۱۱، تم ۵). <strong>استفاده از طرد شق ثالث و برهان خلف کلاسیک اکیداً ممنوع است!</strong></p>
</div>

<div id="td-exo17-container"></div>
"""

td5_interactive = """
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo17-container'), {
    id: 'w05_td_ex17',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱۷ — اثبات فرمول‌های گزاره‌ای در استنتاج طبیعی' : 'Exercice 17 – Preuves de formules propositionnelles',
    source: 'main_td-etudiants.pdf (p. 11)',
    theme: lang === 'fa' ? 'تم ۵' : 'Thème 5',
    statement: lang === 'fa' ?
      '<p>با استفاده از قواعد استنتاج طبیعی شهودگرایانه (بدون طرد شق ثالث و بدون برهان خلف کلاسیک)، احکام زیر را اثبات کنید :</p>' +
      '<ol>' +
      '<li>$p \\land q \\vdash q \\land p$</li>' +
      '<li>$p \\Rightarrow q, \\ q \\Rightarrow r \\vdash p \\Rightarrow r$</li>' +
      '<li>$\\vdash p \\Rightarrow (q \\Rightarrow p)$</li>' +
      '<li>$p \\lor q \\vdash \\neg(\\neg p \\land \\neg q)$</li>' +
      '<li>$p \\Rightarrow (q \\Rightarrow r) \\vdash (p \\land q) \\Rightarrow r$</li>' +
      '</ol>' :
      '<p>En utilisant exclusivement les règles de la déduction naturelle intuitionniste, prouver les séquents suivants :</p>' +
      '<ol>' +
      '<li>$p \\land q \\vdash q \\land p$</li>' +
      '<li>$p \\Rightarrow q, \\ q \\Rightarrow r \\vdash p \\Rightarrow r$</li>' +
      '<li>$\\vdash p \\Rightarrow (q \\Rightarrow p)$</li>' +
      '<li>$p \\lor q \\vdash \\neg(\\neg p \\land \\neg q)$</li>' +
      '<li>$p \\Rightarrow (q \\Rightarrow r) \\vdash (p \\land q) \\Rightarrow r$</li>' +
      '</ol>',
    consigne: lang === 'fa' ?
      'برای هر اثبات، شماره خط، نام قاعده اعمالی، و خطوط ارجاع را به دقت بنویسید.' :
      'Pour chaque dérivation, présentez l\\'arbre ou les boîtes de Fitch avec numéro de ligne, formule, nom précis de la règle et dépendances.',
    hint: lang === 'fa' ? 
      'برای سؤال ۴ (قانون دمورگان شهودگرایانه): فرض خلف برای نقیض باز کنید (فرض کنید ¬p ∧ ¬q) و با استدلال بر اساس موارد روی p ∨ q به تناقض برسید.' :
      'Pour le 4 : ouvrez une boîte de négation avec l\\'hypothèse $\\neg p \\land \\neg q$, puis faites une élimination de $\\lor$ sur l\\'hypothèse $p \\lor q$.',
    steps: lang === 'fa' ? [
      '<strong>اثبات ۱ ($p \\land q \\vdash q \\land p$) :</strong><br>' +
      '۱. $p \\land q$ (فرض)<br>' +
      '۲. $q$ (حذف عطف راست $\\land E_2$ روی ۱)<br>' +
      '۳. $p$ (حذف عطف چپ $\\land E_1$ روی ۱)<br>' +
      '۴. $q \\land p$ (معرفی عطف $\\land I$ روی ۲ و ۳). حکم ثابت شد!',
      '<strong>اثبات ۲ (ترانزیتیویته شرطی) :</strong><br>' +
      '۱. $p \\Rightarrow q$ (فرض ۱)<br>' +
      '۲. $q \\Rightarrow r$ (فرض ۲)<br>' +
      '۳. [فرض موقت $p$ برای معرفی شرطی]<br>' +
      '۴. $q$ (حذف شرطی $\\Rightarrow E$ روی ۱ و ۳)<br>' +
      '۵. $r$ (حذف شرطی $\\Rightarrow E$ روی ۲ و ۴)<br>' +
      '۶. $p \\Rightarrow r$ (معرفی شرطی $\\Rightarrow I$ با رهاسازی ۳). حکم ثابت شد!',
      '<strong>اثبات ۴ ($p \\lor q \\vdash \\neg(\\neg p \\land \\neg q)$) :</strong><br>' +
      '۱. $p \\lor q$ (فرض اولیه)<br>' +
      '۲. [فرض موقت برای نقیض : $\\neg p \\land \\neg q$]<br>' +
      '۳. $\\neg p$ (حذف عطف روی ۲)<br>' +
      '۴. $\\neg q$ (حذف عطف روی ۲)<br>' +
      '۵. اکنون با حذف فصل روی خط ۱ بر اساس دو حالت $p$ و $q$ استدلال می‌کنیم :<br>' +
      '  - حالت الف : فرض $p \\implies$ با $\\neg p$ از خط ۳ به $\\bot$ می‌رسد.<br>' +
      '  - حالت ب : فرض $q \\implies$ با $\\neg q$ از خط ۴ به $\\bot$ می‌رسد.<br>' +
      '۶. پس در هر دو حالت به $\\bot$ می‌رسیم (قاعده $\\lor E$).<br>' +
      '۷. با بستن فرض ۲ و قاعده $\\neg I$ : $\\neg(\\neg p \\land \\neg q)$ اثبات شد !'
    ] : [
      '<strong>Preuve 1 ($p \\land q \\vdash q \\land p$) :</strong><br>' +
      '1. $p \\land q$ (Hypothèse)<br>' +
      '2. $q$ ($\\land E_2$ sur 1)<br>' +
      '3. $p$ ($\\land E_1$ sur 1)<br>' +
      '4. $q \\land p$ ($\\land I$ sur 2 et 3). CQFD.',
      '<strong>Preuve 2 (Transitivité de l\\'implication) :</strong><br>' +
      '1. $p \\Rightarrow q$ (Hyp 1)<br>' +
      '2. $q \\Rightarrow r$ (Hyp 2)<br>' +
      '3. | Supposons $p$ (Hypothèse temporaire)<br>' +
      '4. | $q$ ($\\Rightarrow E$ sur 1, 3)<br>' +
      '5. | $r$ ($\\Rightarrow E$ sur 2, 4)<br>' +
      '6. $p \\Rightarrow r$ ($\\Rightarrow I$ déchargeant 3). CQFD.',
      '<strong>Preuve 4 ($p \\lor q \\vdash \\neg(\\neg p \\land \\neg q$) :</strong><br>' +
      '1. $p \\lor q$ (Hypothèse active)<br>' +
      '2. | Supposons $\\neg p \\land \\neg q$ (Hypothèse pour $\\neg I$)<br>' +
      '3. | $\\neg p$ ($\\land E_1$ sur 2)<br>' +
      '4. | $\\neg q$ ($\\land E_2$ sur 2)<br>' +
      '5. | Cas 1 : $p \\implies \\neg E$ avec 3 donne $\\bot$<br>' +
      '6. | Cas 2 : $q \\implies \\neg E$ avec 4 donne $\\bot$<br>' +
      '7. | $\\bot$ (par $\\lor E$ sur 1, 5, 6)<br>' +
      '8. $\\neg(\\neg p \\land \\neg q)$ (par $\\neg I$ déchargeant 2). CQFD.'
    ],
    justification: lang === 'fa' ?
      'تمام قواعد استفاده‌شده متعلق به سیستم استنتاج طبیعی شهودگرایانه رسمی درس ۴ و ادوکرا است.' :
      'Preuves strictes sans tiers exclu ni absurde classique, conformes aux exigences du Cours 4.',
    finalAnswer: lang === 'fa' ?
      'تمامی احکام با موفقیت در سیستم استنتاج طبیعی شهودگرایانه اثبات شدند.' :
      'Tous les séquents sont rigoureusement dérivés dans le calcul propositionnel intuitionniste.',
    verification: lang === 'fa' ?
      'بررسی اینکه هیچ فرضیه موقتی باز نمانده باشد و عمق باکس‌ها در انتها به صفر برسد.' :
      'Vérifiez qu\\'à la conclusion finale, toutes les hypothèses temporaires ont été déchargées.',
    trap: lang === 'fa' ?
      'بزرگ‌ترین خطا: استفاده از برهان خلف کلاسیک برای اثبات p از روی ¬¬p در منطق شهودگرایانه که کاملاً باطل است!' :
      'Erreur fatale : utiliser RAA ou ¬¬E en croyant faire de la logique intuitionniste.'
  });
"""

make_bundle("w05_td", "fr", td5_fr, td5_interactive)
make_bundle("w05_td", "fa", td5_fa, td5_interactive)

# Week 5 TP, Annales, Revision
make_bundle("w05_tp", "fr", "<div class='box box-objectives'><div class='box-title'>TP 5 — Plateforme Édukera (Déduction Naturelle)</div><p>Prise en main d'Édukera : sélection des règles $\\Rightarrow I, \\Rightarrow E, \\land I, \\land E, \\lor I, \\lor E, \\neg I, \\neg E, \\bot E$. Résolution des exercices interactifs d'échiquiers et décharge visuelle des pièces d'hypothèses.</p></div>")
make_bundle("w05_tp", "fa", "<div class='box box-objectives'><div class='box-title'>آزمایشگاه TP 5 — کار عملی با پلتفرم ادوکرا (Édukera)</div><p>راهنمای تصویری گام‌به‌گام کار با پلتفرم ادوکرا: انتخاب قطعات استنتاج، ساخت باکس‌های فرضیه، رهاسازی قطعات و حل مسائل بدون خطا.</p></div>")

make_bundle("w05_annales", "fr", "<div class='box box-objectives'><div class='box-title'>Annales Semaine 5 — Preuves Formelles d'Examen</div><p>Sujets réels d'examens testant la déduction naturelle intuitionniste (partiel 2016-2017 et 2017-2018).</p></div><div class='step-content'><strong>Question d'examen classique :</strong> Prouver $\\vdash (A \\land B) \\Rightarrow (B \\land A)$.<br>Solution : Supposer $A \\land B$, appliquer $\\land E_2$ pour $B$, $\\land E_1$ pour $A$, appliquer $\\land I$ pour $B \\land A$, décharger par $\\Rightarrow I$.</div>")
make_bundle("w05_annales", "fa", "<div class='box box-objectives'><div class='box-title'>نمونه سؤالات آزمون هفته ۵ — استنتاج طبیعی در امتحانات سوربن</div><p>حل کامل سؤالات امتحانی استنتاج طبیعی بدون استفاده از طرد شق ثالث.</p></div>")

make_bundle("w05_revision", "fr", "<div class='box box-objectives'><div class='box-title'>Fiche Révision Semaine 5</div><p>Règles I et E de chaque connecteur à mémoriser pour l'examen.</p></div>")
make_bundle("w05_revision", "fa", "<div class='box box-objectives'><div class='box-title'>برگه مرور هفته ۵</div><p>جدول قواعد معرفی و حذف استنتاج طبیعی جهت حفظ برای آزمون.</p></div>")

# ==============================================================================
# WEEK 6: COURS & TD - Logique Classique & Règles Dérivées (Thème 6)
# ==============================================================================

c6_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 6 (Logique Classique & Tiers Exclu)</div>
  <ul>
    <li>Comprendre le passage de la logique intuitionniste à la logique classique.</li>
    <li>Maîtriser le principe du <strong>Tiers Exclu ($TE : \\vdash A \\lor \\neg A$)</strong>.</li>
    <li>Appliquer la règle d'<strong>élimination de la double négation ($\neg\neg E$)</strong> : $\\neg\\neg A \\vdash A$.</li>
    <li>Maîtriser le <strong>Raisonnement par l'Absurde Classique ($RAA$)</strong> : pour prouver $A$, on suppose $\\neg A$ et on dérive $\\bot$.</li>
    <li>Prouver des théorèmes purement classiques : Loi de Peirce $((p \\Rightarrow q) \\Rightarrow p) \\Rightarrow p$, contraposition, et De Morgan classique.</li>
  </ul>
</div>

<h2 id="w06-c-classique">1. Pourquoi la Logique Classique ?</h2>
<p>
En logique intuitionniste, affirmer qu'une proposition est vraie exige d'en posséder une <strong>construction</strong> ou une preuve directe. En <strong>logique classique</strong>, on admet le postulat aristotélicien qu'une proposition est nécessairement vraie ou fausse, même si l'on ne sait pas laquelle des deux éventualités est réalisée.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 6.1 — Les Trois Règles Classiques Équivalentes</div>
  <p>Ajouter l'UNE QUELCONQUE des trois règles suivantes à la logique intuitionniste suffit à engendrer TOUTE la logique classique :</p>
  <ol>
    <li><strong>Le Tiers Exclu ($TE$) :</strong> Sans aucune prémisse, on a le droit de poser $A \\lor \\neg A$.
    $$\\frac{}{\\Gamma \\vdash A \\lor \\neg A} (TE)$$</li>
    <li><strong>L'Élimination de la Double Négation ($\neg\\neg E$) :</strong> De $\\neg\\neg A$, on déduit directement $A$.
    $$\\frac{\\Gamma \\vdash \\neg\\neg A}{\\Gamma \\vdash A} (\\neg\\neg E)$$</li>
    <li><strong>Le Raisonnement par l'Absurde Classique ($RAA$) :</strong> Pour prouver $A$, on suppose $\\neg A$. Si cette hypothèse conduit à $\\bot$, alors on a prouvé $A$ !
    $$\\frac{\\Gamma, [\\neg A] \\vdash \\bot}{\\Gamma \\vdash A} (RAA)$$</li>
  </ol>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — RAA vs ¬I (La distinction capitale de Sorbonne)</div>
  <p>C'est la cause numéro 1 d'échec aux examens :</p>
  <ul>
    <li><strong>Règle $\\neg I$ (Intuitionniste) :</strong> On suppose $A$, on arrive à $\\bot$, on conclut $\\neg A$. (Prouver une NÉGATION par contradiction est parfaitement intuitionniste !).</li>
    <li><strong>Règle $RAA$ (Classique uniquement) :</strong> On suppose $\\neg A$, on arrive à $\\bot$, on conclut $A$. (Prouver une proposition POSITIVE par contradiction exige la logique classique !).</li>
  </ul>
</div>
"""

c6_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۶ (منطق کلاسیک و طرد شق ثالث)</div>
  <ul>
    <li>درک گذار بنیادین از منطق شهودگرایانه به منطق کلاسیک.</li>
    <li>تسلط بر اصل <strong>طرد شق ثالث (Tiers Exclu / $TE : \\vdash A \\lor \\neg A$)</strong>.</li>
    <li>به‌کارگیری قاعده <strong>حذف نفی مضاعف کلاسیک ($\neg\neg E$)</strong> : از $\\neg\\neg A$ نتیجه می‌گیریم $A$.</li>
    <li>اجرای صوری <strong>برهان خلف کلاسیک ($RAA$)</strong> : برای اثبات $A$، فرض می‌کنیم $\\neg A$ و به تناقض می‌رسیم.</li>
    <li>اثبات قضایای کلاسیک نامدار: قانون پیرس (Peirce)، قانون عکس نقیض و قوانین دمورگان کلاسیک.</li>
  </ul>
</div>

<h2 id="w06-c-classique">۱. گذار به منطق کلاسیک: اصول سه‌گانه هم‌ارز</h2>
<p>
در منطق شهودگرایانه اثبات یک گزاره مستلزم ساخت صریح آن است. اما در <strong>منطق کلاسیک</strong>، فرض می‌شود هر گزاره فی‌نفسه یا صادق است یا کاذب، حتی اگر ما راهی برای اثبات مستقیم آن نداشته باشیم.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۶.۱ — سه قاعده هم‌ارز منطق کلاسیک</div>
  <p>افزودن هر یک از سه قاعده زیر به منطق شهودگرایانه، کل دستگاه منطق کلاسیک را تولید می‌کند:</p>
  <ol>
    <li><strong>اصل طرد شق ثالث ($TE$):</strong> در هر مرحله از اثبات مجازیم بدون هیچ فرضی بنویسیم $A \\lor \\neg A$.</li>
    <li><strong>حذف نفی مضاعف ($\neg\neg E$):</strong> از $\\neg\\neg A$ مستقیماً گزاره $A$ حاصل می‌شود.</li>
    <li><strong>برهان خلف کلاسیک ($RAA$):</strong> اگر از فرض $\\neg A$ به تناقض $\\bot$ برسیم، گزاره مثبت $A$ اثبات می‌شود.</li>
  </ol>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — تفاوت برهان خلف کلاسیک (RAA) با قاعده نفی (¬I)</div>
  <p>این تفکیک مهم‌ترین ملاک ارزیابی اساتید در امتحانات سوربن است:</p>
  <ul>
    <li><strong>قاعده معرفی نقیض $\\neg I$ (شهودگرایانه):</strong> فرض می‌کنیم $A$، به $\\bot$ می‌رسیم، نتیجه می‌گیریم $\\neg A$. این کار در منطق شهودگرایانه کاملاً مجاز است!</li>
    <li><strong>برهان خلف کلاسیک $RAA$ (فقط کلاسیک):</strong> فرض می‌کنیم $\\neg A$، به $\\bot$ می‌رسیم، نتیجه می‌گیریم $A$. اثبات یک گزاره مثبت از طریق ابطال نقیض آن، فقط در منطق کلاسیک معتبر است!</li>
  </ul>
</div>
"""

make_bundle("w06_cours", "fr", c6_fr)
make_bundle("w06_cours", "fa", c6_fa)

# Week 6 TD
td6_fr = """
<div class="box box-objectives">
  <div class="box-title">TD 6 — Logique Classique & Règles Dérivées</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 12, Thème 6, Exercices 19, 20 et 21). Utilisation autorisée du tiers exclu ($TE$), de $\neg\neg E$ et des règles dérivées.</p>
</div>

<div id="td-exo19-container"></div>
<div id="td-exo20-container"></div>
"""

td6_fa = """
<div class="box box-objectives">
  <div class="box-title">تمرین‌های TD 6 — منطق کلاسیک و قواعد مشتق‌شده</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۱۲، تم ۶، تمرین‌های ۱۹، ۲۰ و ۲۱). استفاده از طرد شق ثالث و قواعد مشتق‌شده کلاسیک مجاز است.</p>
</div>

<div id="td-exo19-container"></div>
<div id="td-exo20-container"></div>
"""

td6_interactive = """
  // Exercice 19
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo19-container'), {
    id: 'w06_td_ex19',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱۹ — مقایسه منطق شهودگرایانه و کلاسیک' : 'Exercice 19 – Logique intuitionniste vs classique',
    source: 'main_td-etudiants.pdf (p. 12)',
    theme: lang === 'fa' ? 'تم ۶' : 'Thème 6',
    statement: lang === 'fa' ?
      '<p><strong>سؤال ۱ :</strong> چرا فرمول $\\neg\\neg p \\Rightarrow p$ در منطق شهودگرایانه قابل اثبات نیست ؟<br>' +
      '<strong>سؤال ۲ :</strong> فرمول $\\neg\\neg p \\Rightarrow p$ را در منطق کلاسیک با استفاده از اصل طرد شق ثالث ($TE : p \\lor \\neg p$) اثبات کنید.</p>' :
      '<p><strong>Question 1 :</strong> Pourquoi la formule $\\neg\\neg p \\Rightarrow p$ n\\'est-elle pas prouvable en logique intuitionniste ?<br>' +
      '<strong>Question 2 :</strong> Prouver $\\vdash \\neg\\neg p \\Rightarrow p$ en logique classique en utilisant le tiers exclu ($TE$).</p>',
    consigne: lang === 'fa' ?
      'برای سؤال ۲، روی فرمول طرد شق ثالث $p \\lor \\neg p$ قاعده حذف فصل (استدلال بر اساس موارد) را اعمال کنید.' :
      'Pour la question 2, appliquez la règle d\\'élimination de la disjonction ($\\lor E$) sur l\\'instance du tiers exclu $p \\lor \\neg p$.',
    hint: lang === 'fa' ? 
      'در حالت اول فرض کنید p که نتیجه p آماده است. در حالت دوم فرض کنید ¬p که با ¬¬p تولید تناقض می‌کند و با bot E به p می‌رسیم.' :
      'Cas 1 : supposons $p \\implies$ le but $p$ est immédiat. Cas 2 : supposons $\\neg p \\implies$ contradiction avec $\\neg\\neg p$, d\\'où $p$ par $\\bot E$.',
    steps: lang === 'fa' ? [
      '<strong>پاسخ سؤال ۱ :</strong> در منطق شهودگرایانه، اثبات $p$ نیازمند ارائه یک مدرک یا ساخت صریح برای $p$ است. دانستن اینکه «غیرممکن است $p$ غلط باشد» ($\\neg\\neg p$) به تنهایی روشی برای ساخت $p$ ارائه نمی‌دهد. بنابراین این فرمول در سیستم شهودگرایانه قضیه نیست.',
      '<strong>پاسخ سؤال ۲ (اثبات با طرد شق ثالث) :</strong><br>' +
      '۱. | فرض می‌کنیم $\\neg\\neg p$ (برای معرفی شرطی $\\Rightarrow I$)<br>' +
      '۲. | $p \\lor \\neg p$ (اصل طرد شق ثالث $TE$ روی $p$)<br>' +
      '۳. | اکنون استدلال بر اساس دو حالت فصل (قاعده $\\lor E$) :<br>' +
      '   | - شاخه ۱ : فرض می‌کنیم $p$. پس $p$ حاصل است.<br>' +
      '   | - شاخه ۲ : فرض می‌کنیم $\\neg p$. با اعمال $\\neg E$ بین $\\neg p$ و فرض خط ۱ ($\\neg\\neg p$) به $\\bot$ می‌رسیم. سپس با قاعده $\\bot E$ گزاره $p$ را نتیجه می‌گیریم.<br>' +
      '۴. | در هر دو شاخه به $p$ رسیدیم، پس $p$ اثبات شد (با $\\lor E$ روی خط ۲).<br>' +
      '۵. با بستن فرض خط ۱ و قاعده $\\Rightarrow I$ : $\\neg\\neg p \\Rightarrow p$ اثبات شد !'
    ] : [
      '<strong>Réponse Question 1 :</strong> En logique intuitionniste, la vérité d\\'une proposition exige une preuve constructive. Savoir qu\\'il est contradictoire que $p$ soit faux ($\\neg\\neg p$) ne fournit aucun algorithme ni témoin pour construire $p$. Elle n\\'est donc pas dérivable sans axiome classique.',
      '<strong>Réponse Question 2 (Preuve formelle avec TE) :</strong><br>' +
      '1. | Supposons $\\neg\\neg p$ (Hypothèse pour $\\Rightarrow I$)<br>' +
      '2. | $p \\lor \\neg p$ (Règle du Tiers Exclu $TE$ sur $p$)<br>' +
      '3. | Raisonnement par cas ($\\lor E$) :<br>' +
      '   | - Sous-preuve cas 1 : Supposons $p$. Le but $p$ est atteint immédiatement.<br>' +
      '   | - Sous-preuve cas 2 : Supposons $\\neg p$. On applique $\\neg E$ entre $\\neg p$ et $\\neg\\neg p$ (ligne 1), ce qui donne $\\bot$. Par $\\bot E$, on déduit $p$.<br>' +
      '4. | $p$ (par $\\lor E$ sur la disjonction de la ligne 2)<br>' +
      '5. $\\neg\\neg p \\Rightarrow p$ (par $\\Rightarrow I$ déchargeant 1). CQFD.'
    ],
    justification: lang === 'fa' ?
      'اثبات با رعایت استاندارد سوربن در استفاده از اصل طرد شق ثالث و قاعده $\\lor E$ انجام گرفته است.' :
      'Preuve rigoureuse déchargeant toutes les hypothèses temporaires avec citation des règles.',
    finalAnswer: lang === 'fa' ?
      'فرمول $\\neg\\neg p \\Rightarrow p$ با موفقیت در منطق کلاسیک با استفاده از اصل طرد شق ثالث اثبات شد.' :
      'La formule $\\neg\\neg p \\Rightarrow p$ est rigoureusement démontrée avec la règle $TE$.',
    verification: lang === 'fa' ?
      'بررسی اینکه آیا از برهان خلف استفاده شد؟ خیر، از اصل طرد شق ثالث و قاعده مجاز $\\bot E$ استفاده شد.' :
      'Contrôle : nous avons utilisé le tiers exclu et $\\bot E$, sans invoquer directement $RAA$.',
    trap: lang === 'fa' ?
      'دام رایج: نوشتن اینکه از $\\bot$ گزاره $p$ با برهان خلف به دست آمد؛ در حالی که از قاعده شهودگرایانه $\\bot E$ استفاده شد.' :
      'Ne confondez pas $\\bot E$ (qui déduit n\\'importe quoi d\\'une contradiction) avec $RAA$.'
  });

  // Exercice 20 - Preuves classiques (Loi de Peirce)
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo20-container'), {
    id: 'w06_td_ex20',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۲۰ — اثبات قضایای کلاسیک (قانون پیرس)' : 'Exercice 20 – Preuves classiques (Loi de Peirce)',
    source: 'main_td-etudiants.pdf (p. 12)',
    theme: lang === 'fa' ? 'تم ۶' : 'Thème 6',
    statement: lang === 'fa' ?
      '<p>قانون مشهور پیرس را در منطق کلاسیک اثبات کنید :</p>' +
      '$$\\vdash ((p \\Rightarrow q) \\Rightarrow p) \\Rightarrow p$$' :
      '<p>Démontrer la loi de Peirce en logique classique :</p>' +
      '$$\\vdash ((p \\Rightarrow q) \\Rightarrow p) \\Rightarrow p$$',
    consigne: lang === 'fa' ?
      'روی متغیر p از اصل طرد شق ثالث $p \\lor \\neg p$ استفاده کنید.' :
      'Appliquez le tiers exclu sur $p$ : posez $p \\lor \\neg p$, puis raisonnez par cas.',
    hint: lang === 'fa' ? 
      'در حالتی که ¬p را فرض کرده‌اید، نشان دهید p => q برقرار است، سپس از فرض ((p => q) => p) مقدار p را به دست آورید.' :
      'Si $\\neg p$, alors pour tout $q$, $p \\Rightarrow q$ est vrai ! Par Modus Ponens avec l\\'hypothèse, on déduit $p$.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ :</strong> فرض می‌کنیم $H = (p \\Rightarrow q) \\Rightarrow p$ (برای معرفی شرطی نهایی).',
      '<strong>گام ۲ :</strong> اصل طرد شق ثالث را روی $p$ می‌نویسیم : $p \\lor \\neg p$.',
      '<strong>گام ۳ (استدلال بر اساس دو حالت) :</strong><br>' +
      '- حالت ۱ : فرض می‌کنیم $p$. پس $p$ مستقیماً برقرار است.<br>' +
      '- حالت ۲ : فرض می‌کنیم $\\neg p$. ثابت می‌کنیم $p \\Rightarrow q$ برقرار است :<br>' +
      '   فرض می‌کنیم $p$. با $\\neg p$ تناقض $\\bot$ می‌دهد و با $\\bot E$ گزاره $q$ حاصل می‌شود. پس $p \\Rightarrow q$ اثبات شد.<br>' +
      '   اکنون با قیاس استثنایی بین $H$ و $p \\Rightarrow q$، نتیجه می‌شود $p$ !',
      '<strong>گام ۴ :</strong> در هر دو حالت به $p$ رسیدیم. با $\\lor E$ گزاره $p$ ثابت شد.',
      '<strong>گام ۵ :</strong> با بستن فرض $H$ و قاعده $\\Rightarrow I$، قانون پیرس اثبات شد !'
    ] : [
      '<strong>Étape 1 :</strong> Supposons $H = (p \\Rightarrow q) \\Rightarrow p$.',
      '<strong>Étape 2 :</strong> Posons le tiers exclu $p \\lor \\neg p$ ($TE$).',
      '<strong>Étape 3 (Raisonnement par cas) :</strong><br>' +
      '- Cas 1 : $p$. Le but $p$ est immédiat.<br>' +
      '- Cas 2 : $\\neg p$. Montrons que $p \\Rightarrow q$ : supposons $p$, contradiction avec $\\neg p \\implies \\bot \\implies q$ par $\\bot E$. On a donc $p \\Rightarrow q$.<br>' +
      'Par Modus Ponens entre $H$ et $p \\Rightarrow q$, on déduit $p$.',
      '<strong>Étape 4 :</strong> Par $\\lor E$, on conclut $p$.',
      '<strong>Étape 5 :</strong> Par $\\Rightarrow I$, on conclut $((p \\Rightarrow q) \\Rightarrow p) \\Rightarrow p$. CQFD.'
    ],
    justification: lang === 'fa' ?
      'قانون پیرس یکی از برجسته‌ترین نمونه‌های قضایای منطق کلاسیک است که در منطق شهودگرایانه هرگز قابل اثبات نیست.' :
      'La loi de Peirce est le prototype du théorème valide en logique classique mais non démontrable en logique intuitionniste.',
    finalAnswer: lang === 'fa' ?
      'قانون پیرس با موفقیت در منطق کلاسیک با استفاده از طرد شق ثالث اثبات شد.' :
      'La loi de Peirce est rigoureusement prouvée.',
    verification: lang === 'fa' ?
      'ارزیابی با جدول درستی نشان می‌دهد این فرمول یک تاتولوژی است.' :
      'Une table de vérité confirme immédiatement que la loi de Peirce vaut 1 sous toutes les valuations.',
    trap: lang === 'fa' ?
      'تلاش برای اثبات قانون پیرس بدون استفاده از طرد شق ثالث یا برهان خلف که ناممکن است.' :
      'Essayer de prouver Peirce sans tiers exclu : c\\'est impossible.'
  });
"""

make_bundle("w06_td", "fr", td6_fr, td6_interactive)
make_bundle("w06_td", "fa", td6_fa, td6_interactive)

make_bundle("w06_tp", "fr", "<div class='box box-objectives'><div class='box-title'>TP 6 — Édukera Classique & Règles Dérivées</div><p>Utilisation des boutons du thème sombre d'Édukera : tiers exclu, raisonnement par l'absurde classique et lois de De Morgan classiques.</p></div>")
make_bundle("w06_tp", "fa", "<div class='box box-objectives'><div class='box-title'>آزمایشگاه TP 6 — ادوکرا کلاسیک و طرد شق ثالث</div><p>نحوه فعال‌سازی دکمه‌های تم تیره ادوکرا برای درج قطعه طرد شق ثالث و حل تمرین‌های کلاسیک.</p></div>")

make_bundle("w06_annales", "fr", "<div class='box box-objectives'><div class='box-title'>Annales Semaine 6 — Logique Classique aux Examens</div><p>Questions d'annales portant sur la preuve avec tiers exclu (Examen 2020-2021 et 2021-2022).</p></div>")
make_bundle("w06_annales", "fa", "<div class='box box-objectives'><div class='box-title'>نمونه سؤالات آزمون هفته ۶ — منطق کلاسیک</div><p>سؤالات آزمون‌های نهایی سوربن در خصوص اثبات قضایای کلاسیک با طرد شق ثالث.</p></div>")

make_bundle("w06_revision", "fr", "<div class='box box-objectives'><div class='box-title'>Fiche Révision Semaine 6</div><p>Synthèse des règles dérivées : Modus Tollens, Contraposition, Peirce, et Tiers Exclu.</p></div>")
make_bundle("w06_revision", "fa", "<div class='box box-objectives'><div class='box-title'>برگه مرور هفته ۶</div><p>خلاصه قواعد مشتق‌شده کلاسیک برای آمادگی آزمون.</p></div>")

print("Week 5 & 6 generation complete!")

