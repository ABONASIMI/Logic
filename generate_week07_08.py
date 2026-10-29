import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 7: COURS & TD - LPPO Syntaxe, Termes & Variables Libres/Liées
# ==============================================================================

c7_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 7 (LPPO Syntaxe)</div>
  <ul>
    <li>Distinguer sans équivoque la syntaxe des <strong>termes</strong> (qui désignent des objets) et des <strong>formules</strong> (qui ont une valeur de vérité).</li>
    <li>Comprendre la signature $\\mathcal{L} = \\langle \\mathcal{F}, \\mathcal{P}, \\text{ar} \\rangle$ : constantes, fonctions, prédicats et arités.</li>
    <li>Maîtriser la construction inductive des termes $\\mathcal{T}_k(\\mathcal{F}, \\mathcal{V})$.</li>
    <li>Calculer rigoureusement l'ensemble des variables libres $Free(F)$ d'une formule arbitraire.</li>
    <li>Déterminer la portée d'un quantificateur et lier chaque occurrence de variable à son lieur.</li>
    <li>Effectuer des renommages alphabétiques ($\alpha$-conversion) sans jamais introduire de <strong>capture de variable</strong>.</li>
  </ul>
</div>

<h2 id="w07-c-termes-vs-formules">1. La Distinction Capitale : Termes vs Formules</h2>
<div class="box box-definition">
  <div class="box-title">Définition 7.1 — Terme vs Formule</div>
  <ul>
    <li><strong>Un Terme :</strong> Désigne un <strong>élément</strong> du domaine de discours (un nombre, une personne, une liste). Il ne possède PAS de valeur de vérité ! On ne peut pas dire qu'un terme est « vrai » ou « faux ».
      <ul>
        <li>Exemples : $x$, $0$, $s(0)$, $f(x, y)$, $\\text{pere}(\\text{jean})$.</li>
      </ul>
    </li>
    <li><strong>Une Formule :</strong> Exprime une <strong>assertion</strong> sur les objets. Elle est susceptible d'être vraie ou fausse une fois interprétée.
      <ul>
        <li>Exemples : $P(x)$, $x = y$, $R(f(x), c)$, $\\forall x \\exists y P(x, y)$.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — Confondre f(x) et P(x)</div>
  <p><strong>Erreur très fréquente :</strong> Écrire $f(x) \\land P(y)$ ou penser que $P(x)$ peut être un argument d'une fonction comme $f(P(x))$.</p>
  <p><strong>Règle absolue :</strong> Une fonction $f$ prend en argument des <strong>termes</strong> et produit un <strong>terme</strong>. Un prédicat $P$ prend en argument des <strong>termes</strong> et produit une <strong>formule atomique</strong>. Les connecteurs ($\\land, \\lor, \\Rightarrow$) ne relient QUE des formules !</p>
</div>

<h2 id="w07-c-termes-inductifs">2. Définition Inductive de l'Ensemble des Termes ($\\mathcal{T}_k$)</h2>
<div class="box box-definition">
  <div class="box-title">Définition 7.2 — Les Niveaux Inductifs $\\mathcal{T}_k$</div>
  <p>Soit $\\mathcal{V}$ les variables, et $\\mathcal{F}$ les fonctions (les constantes étant des fonctions d'arité 0). L'ensemble des termes est construit par strates :</p>
  <ul>
    <li>$\\mathcal{T}_0 = \\mathcal{V} \\cup \\mathcal{F}_0$ (l'ensemble des variables et des constantes).</li>
    <li>$\\mathcal{T}_{k+1} = \\mathcal{T}_k \\cup \\{ f(t_1, \\dots, t_n) \\mid f \\in \\mathcal{F}_n \\text{ et } t_1, \\dots, t_n \\in \\mathcal{T}_k \\}$.</li>
    <li>L'ensemble complet des termes est $\\mathcal{T}(\\mathcal{F}, \\mathcal{V}) = \\bigcup_{k=0}^\\infty \\mathcal{T}_k$.</li>
  </ul>
</div>

<h2 id="w07-c-variables">3. Variables Libres, Variables Liées et Portée</h2>
<div class="box box-definition">
  <div class="box-title">Définition 7.3 — Calcul Récursif de $Free(F)$</div>
  <p>Pour déterminer quelles variables sont libres dans une formule, on applique les règles récursives :</p>
  <ul>
    <li>$Free(P(t_1, \\dots, t_n)) = \\text{Var}(t_1) \\cup \\dots \\cup \\text{Var}(t_n)$ ;</li>
    <li>$Free(\\neg F) = Free(F)$ ;</li>
    <li>$Free(F_1 \\land F_2) = Free(F_1) \\cup Free(F_2)$ (de même pour $\\lor, \\Rightarrow, \\Leftrightarrow$) ;</li>
    <li>$Free(\\forall x F) = Free(F) \\setminus \\{x\\}$ (le quantificateur lie la variable $x$) ;</li>
    <li>$Free(\\exists x F) = Free(F) \\setminus \\{x\\}$.</li>
  </ul>
  <p>Une formule $F$ est dite <strong>close</strong> (ou énoncé / <em>sentence</em>) si $Free(F) = \\emptyset$.</p>
</div>
"""

c7_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۷ (نحو مرتبه اول LPPO)</div>
  <ul>
    <li>تفکیک قطعی نحو <strong>ترم‌ها</strong> (اشاره به اشیاء) از نحو <strong>فرمول‌ها</strong> (دارای مقدار درستی).</li>
    <li>درک امضای زبان $\\mathcal{L} = \\langle \\mathcal{F}, \\mathcal{P}, \\text{ar} \\rangle$: ثابت‌ها، توابع، محمول‌ها و تعداد ورودی‌ها (Arité).</li>
    <li>تسلط بر ساخت استقرایی لایه‌های ترم‌ها $\\mathcal{T}_k(\\mathcal{F}, \\mathcal{V})$.</li>
    <li>محاسبه گام‌به‌گام و بدون خطای مجموعه متغیرهای آزاد $Free(F)$ برای هر فرمول دلخواه.</li>
    <li>تعیین دقیق حوزه اثر (Portée) هر سور و اتصال هر رخداد متغیر به سور مربوطه.</li>
    <li>بازنام‌گذاری الفبایی ایمن بدون ایجاد <strong>تله‌اندازی متغیر (Capture)</strong>.</li>
  </ul>
</div>

<h2 id="w07-c-termes-vs-formules">۱. تفاوت بنیادین: ترم در برابر فرمول</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۷.۱ — ترم (Terme) در برابر فرمول (Formule)</div>
  <ul>
    <li><strong>ترم:</strong> به یک <strong>عنصر یا شیء</strong> از جهان اشاره دارد (یک عدد، یک انسان، یک تابع). ترم هرگز مقدار درستی (۰ یا ۱) ندارد! نمی‌توان گفت ترم $f(x)$ درست است یا نادرست.
      <ul>
        <li>مثال‌ها : $x$, $0$, $s(x)$, $f(a, g(y))$.</li>
      </ul>
    </li>
    <li><strong>فرمول:</strong> یک <strong>حکم یا گزاره خبری</strong> درباره اشیاء بیان می‌کند که پس از ارزیابی دارای مقدار درستی (درست یا غلط) خواهد بود.
      <ul>
        <li>مثال‌ها : $P(x)$, $x = y$, $Q(f(x), a)$, $\\forall x P(x)$.</li>
      </ul>
    </li>
  </ul>
</div>
"""

make_bundle("w07_cours", "fr", c7_fr)
make_bundle("w07_cours", "fa", c7_fa)

# Week 7 TD - Exos 22 à 26
td7_fr = """
<div class="box box-objectives">
  <div class="box-title">TD 7 — Termes, Construction & Variables Liées</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 13–15, Thème 7, Exercices 22 à 26).</p>
</div>

<div id="td-exo22-container"></div>
<div id="td-exo24-container"></div>
<div id="td-exo26-container"></div>
"""

td7_fa = """
<div class="box box-objectives">
  <div class="box-title">تمرین‌های TD 7 — ترم‌ها، متغیرهای مقید و بازنام‌گذاری</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۱۳ تا ۱۵، تم ۷، تمرین‌های ۲۲ تا ۲۶).</p>
</div>

<div id="td-exo22-container"></div>
<div id="td-exo24-container"></div>
<div id="td-exo26-container"></div>
"""

td7_interactive = """
  // Exercice 24
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo24-container'), {
    id: 'w07_td_ex24',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۲۴ — نمادهای یک فرمول و محاسبه متغیرهای آزاد' : 'Exercice 24 – Symboles d\\\'une formule & Variables libres',
    source: 'main_td-etudiants.pdf (p. 14)',
    theme: lang === 'fa' ? 'تم ۷' : 'Thème 7',
    statement: lang === 'fa' ?
      '<p>فرمول زیر را در نظر بگیرید :</p>' +
      '$$F = \\forall x (P(x, f(y)) \\Rightarrow \\exists y Q(f(x), y)) \\lor R(x)$$' +
      '<p>۱. نمادهای تابع و محمول و آریته هر کدام را مشخص کنید.<br>' +
      '۲. رخدادهای متغیرهای $x$ و $y$ را بررسی کرده و مجموعه متغیرهای آزاد $Free(F)$ را به دست آورید.<br>' +
      '۳. آیا فرمول $F$ یک فرمول بسته (Close) است ؟</p>' :
      '<p>On considère la formule :</p>' +
      '$$F = \\forall x (P(x, f(y)) \\Rightarrow \\exists y Q(f(x), y)) \\lor R(x)$$' +
      '<p>1. Identifier les symboles de fonction, de prédicat et leurs arités.<br>' +
      '2. Déterminer les occurrences libres et liées des variables et calculer $Free(F)$.<br>' +
      '3. La formule $F$ est-elle close ?</p>',
    consigne: lang === 'fa' ?
      'دقت کنید که رخداد $x$ در $R(x)$ بیرون از حوزه اثر $\\forall x$ قرار دارد!' :
      'Attention : l\\\\'occurrence de $x$ dans $R(x)$ se trouve EN DEHORS de la portée du quantificateur $\\forall x$.',
    hint: lang === 'fa' ? 
      'پرتو اثر $\\forall x$ فقط پرانتز اول است. فصل $\\lor R(x)$ آزاد است.' :
      'La portée de $\\forall x$ est limitée à $(P(x, f(y)) \\Rightarrow \\exists y Q(f(x), y))$.',
    steps: lang === 'fa' ? [
      '<strong>نمادها و آریته‌ها :</strong><br>' +
      '- تابع : $f$ با آریته ۱ (تک‌متغیره).<br>' +
      '- محمول‌ها : $P$ با آریته ۲، $Q$ با آریته ۲، $R$ با آریته ۱.',
      '<strong>محاسبه متغیرهای آزاد Free(F) :</strong><br>' +
      '- زیرفرمول چپ $F_1 = \\forall x (\\dots)$ : در داخل آن، $y$ در $f(y)$ آزاد است، اما $x$ توسط $\\forall x$ مقید شده است. در داخل $\\exists y Q(\\dots)$، متغیر $y$ مقید شده است. بنابراین $Free(F_1) = \\{y\\}$.<br>' +
      '- زیرفرمول راست $F_2 = R(x)$ : متغیر $x$ آزاد است. پس $Free(F_2) = \\{x\\}$.<br>' +
      '- در کل : $Free(F) = Free(F_1) \\cup Free(F_2) = \\{x, y\\}$.',
      '<strong>بررسی بسته بودن :</strong> چون $Free(F) = \\{x, y\\} \\neq \\emptyset$ است، فرمول بسته <strong>نیست</strong>.'
    ] : [
      '<strong>1. Symboles et arités :</strong><br>' +
      '- Symboles de fonction : $f$ d\\\\'arité 1.<br>' +
      '- Symboles de prédicat : $P$ d\\\\'arité 2, $Q$ d\\\\'arité 2, $R$ d\\\\'arité 1.',
      '<strong>2. Calcul récursif de $Free(F)$ :</strong><br>' +
      '- Pour $F_1 = \\forall x (P(x, f(y)) \\Rightarrow \\exists y Q(f(x), y))$ : la variable $y$ dans $f(y)$ est libre, tandis que $x$ est liée par $\\forall x$. Donc $Free(F_1) = \\{y\\}$.<br>' +
      '- Pour $F_2 = R(x)$ : l\\\\'occurrence de $x$ est en dehors de la portée de $\\forall x$, elle est donc LIBRE. $Free(F_2) = \\{x\\}$.<br>' +
      '- $Free(F) = Free(F_1) \\cup Free(F_2) = \\{x, y\\}$.',
      '<strong>3. Formule close :</strong> $Free(F) \\neq \\emptyset$, donc $F$ n\\\\'est <strong>pas close</strong>.'
    ],
    justification: lang === 'fa' ?
      'محاسبه طبق تعاریف صوری حوزه اثر و محاسبه بازگشتی متغیرهای آزاد اسلاید ۱۵ درس ۷ انجام شده است.' :
      'Application exacte des règles inductives de calcul de Free(F) du Cours 7.',
    finalAnswer: lang === 'fa' ?
      '$$Free(F) = \\{x, y\\} \\quad \\text{(فرمول بسته نیست)}$$' :
      '$$Free(F) = \\{x, y\\} \\quad \\text{(formule non close)}$$',
    verification: lang === 'fa' ?
      'شمارش رخدادها: x دارای ۳ رخداد است (۱ مقید به forall، ۱ مقید در Q، و ۱ کاملاً آزاد در R).' :
      'Contrôle des occurrences : $x$ apparaît 3 fois (dont 1 fois libre dans $R(x)$).',
    trap: lang === 'fa' ?
      'تصور اینکه چون در ابتدای فرمول $\\forall x$ آمده، تمام xهای کل خط مقید هستند! پرانتزها مرز حوزه اثر را مشخص می‌کنند.' :
      'Le piège d\\\\'examen classique : croire que $\\forall x$ lie toute la ligne alors que la portée s\\\\'arrête à la fermeture de la parenthèse avant le $\\lor$.'
  });
"""

make_bundle("w07_td", "fr", td7_fr, td7_interactive)
make_bundle("w07_td", "fa", td7_fa, td7_interactive)

make_bundle("w07_tp", "fr", "<div class='box box-objectives'><div class='box-title'>TP 7 — Syntaxe des Termes en Python</div><p>Représentation inductive de l'ensemble des termes en Python (Exercices 14 & 15 de <code>main_tp-etudiants.pdf</code>).</p></div>")
make_bundle("w07_tp", "fa", "<div class='box box-objectives'><div class='box-title'>آزمایشگاه TP 7 — پیاده‌سازی ترم‌های مرتبه اول در پایتون</div><p>کدنویسی استقرایی ترم‌های Tk و فرمول‌های مرتبه اول در زبان پایتون.</p></div>")

make_bundle("w07_annales", "fr", "<div class='box box-objectives'><div class='box-title'>Annales Semaine 7 — Variables libres aux examens</div><p>Questions d'annales sur le renommage alphabétique et le calcul de Free(F).</p></div>")
make_bundle("w07_annales", "fa", "<div class='box box-objectives'><div class='box-title'>نمونه سؤالات آزمون هفته ۷</div><p>مسائل امتحانی پیرامون شناسایی رخدادهای آزاد و مقید و بازنام‌گذاری بدون تله‌اندازی.</p></div>")

make_bundle("w07_revision", "fr", "<div class='box box-objectives'><div class='box-title'>Fiche Révision Semaine 7</div><p>Règles formelles de portée et de renommage sûr.</p></div>")
make_bundle("w07_revision", "fa", "<div class='box box-objectives'><div class='box-title'>برگه مرور هفته ۷</div><p>خلاصه قواعد متغیرهای آزاد و پورته سورها.</p></div>")

# ==============================================================================
# WEEK 8: COURS & TD - LPPO Sémantique, Modèles & Substitutions
# ==============================================================================

c8_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 8 (LPPO Sémantique)</div>
  <ul>
    <li>Comprendre la notion de <strong>structure</strong> $\\mathcal{M} = \\langle D, \\mathcal{I} \\rangle$ : domaine non vide et interprétation des symboles.</li>
    <li>Évaluer des formules avec quantificateurs selon la sémantique de Tarski.</li>
    <li>Évaluer rigoureusement des formules du premier ordre sur des <strong>domaines finis</strong>.</li>
    <li>Définir et exécuter une <strong>substitution de terme $F[x \\leftarrow t]$</strong> sans capture de variable.</li>
    <li>Construire des contre-modèles finis pour invalider des formules du premier ordre.</li>
  </ul>
</div>

<h2 id="w08-c-structures">1. Structures et Interprétations</h2>
<div class="box box-definition">
  <div class="box-title">Définition 8.1 — Structure $\\mathcal{M} = \\langle D, \\mathcal{I} \\rangle$</div>
  <p>Une <strong>structure</strong> pour un langage $\\mathcal{L}$ est la donnée de :</p>
  <ul>
    <li>Un ensemble non vide $D$ appelé le <strong>domaine de discours</strong> ;</li>
    <li>Pour chaque constante $c$, un élément $c^\\mathcal{M} \\in D$ ;</li>
    <li>Pour chaque fonction $f$ d'arité $n$, une fonction $f^\\mathcal{M} : D^n \\to D$ ;</li>
    <li>Pour chaque prédicat $P$ d'arité $n$, une relation $P^\\mathcal{M} \\subseteq D^n$.</li>
  </ul>
</div>

<h2 id="w08-c-substitution">2. Substitution Admissible (Sans Capture)</h2>
<div class="box box-definition">
  <div class="box-title">Définition 8.2 — Substitution $F[x \\leftarrow t]$</div>
  <p>L'opération $F[x \\leftarrow t]$ remplace toutes les occurrences <strong>libres</strong> de la variable $x$ par le terme $t$.</p>
  <p><strong>Condition d'admissibilité (évitement de capture) :</strong> Le terme $t$ est librement substituable à $x$ dans $F$ si aucune variable de $t$ n'est capturée par un quantificateur englobant lors du remplacement ! Si une capture menace, on doit obligatoirement renommer d'abord la variable liée ($\\alpha$-conversion).</p>
</div>
"""

c8_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۸ (معناشناسی مرتبه اول)</div>
  <ul>
    <li>درک ساختار $\\mathcal{M} = \\langle D, \\mathcal{I} \\rangle$: دامنه سخن غیرتهی و تفسیر واقعی نمادها.</li>
    <li>ارزیابی گزاره‌های سوردار بر اساس معناشناسی تارسکی.</li>
    <li>محاسبه مقدار درستی فرمول‌ها روی <strong>دامنه‌های متناهی</strong> (مانند گراف‌ها و مجموعه‌های کوچک).</li>
    <li>اجرای دقیق <strong>جایگزینی ترم $F[x \\leftarrow t]$</strong> با رعایت شرط عدم تله‌اندازی متغیر.</li>
    <li>ساخت مثال نقض و مدل‌های ابطال‌کننده برای گزاره‌های مرتبه اول.</li>
  </ul>
</div>
"""

make_bundle("w08_cours", "fr", c8_fr)
make_bundle("w08_cours", "fa", c8_fa)

# Week 8 TD - Exos 27 à 32
td8_fr = """
<div class="box box-objectives">
  <div class="box-title">TD 8 — Substitutions & Interprétations sur Domaines Finis</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 16–18, Thème 8, Exercices 27 à 32).</p>
</div>

<div id="td-exo27-container"></div>
<div id="td-exo31-container"></div>
"""

td8_fa = """
<div class="box box-objectives">
  <div class="box-title">تمرین‌های TD 8 — جایگزینی‌ها و تفسیر بر روی دامنه‌های متناهی</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۱۶ تا ۱۸، تم ۸، تمرین‌های ۲۷ تا ۳۲).</p>
</div>

<div id="td-exo27-container"></div>
<div id="td-exo31-container"></div>
"""

td8_interactive = """
  // Exercice 27
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo27-container'), {
    id: 'w08_td_ex27',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۲۷ — جایگزینی‌های مجاز و تله‌اندازی متغیر' : 'Exercice 27 – Substitutions & Captures',
    source: 'main_td-etudiants.pdf (p. 16)',
    theme: lang === 'fa' ? 'تم ۸' : 'Thème 8',
    statement: lang === 'fa' ?
      '<p>فرض کنید $F = \\forall y (P(x, y) \\Rightarrow Q(x))$.</p>' +
      '<p>۱. محاسبه کنید : $F[x \\leftarrow a]$ با $a$ یک نماد ثابت.<br>' +
      '۲. آیا جایگزینی $F[x \\leftarrow f(y)]$ مجاز است ؟ توضیح دهید چه اتفاقی می‌افتد و چگونه باید فرمول را تصحیح کرد.</p>' :
      '<p>Soit la formule $F = \\forall y (P(x, y) \\Rightarrow Q(x))$.</p>' +
      '<p>1. Calculer $F[x \\leftarrow a]$ où $a$ est une constante.<br>' +
      '2. La substitution $F[x \\leftarrow f(y)]$ est-elle admissible ? Expliquer et donner la forme correcte.</p>',
    consigne: lang === 'fa' ?
      'اگر متغیر موجود در ترم جدید پس از جایگزینی زیر چتر یک سور با همان نام بیفتد، تله‌اندازی رخ داده و جایگزینی مستقیم ممنوع است.' :
      'Si une variable du terme à substituer tombe sous la portée d\\'un quantificateur de même nom, il y a capture illicite. Il faut d\\'abord renommer la variable liée.',
    hint: lang === 'fa' ? 
      'در F متغیر y توسط forall y مقید شده است. اگر f(y) را به جای x بگذارید، y موجود در f(y) اسیر می‌شود!' :
      'La variable $y$ du terme $f(y)$ serait capturée par $\\forall y$. Renommez d\\'abord $y$ en $z$.',
    steps: lang === 'fa' ? [
      '<strong>سؤال ۱ :</strong> متغیر $x$ در $P(x, y)$ و $Q(x)$ آزاد است. چون $a$ ثابت است، هیچ متغیری ندارد و خطری متوجه آن نیست :<br>' +
      '$$F[x \\leftarrow a] = \\forall y (P(a, y) \\Rightarrow Q(a))$$',
      '<strong>سؤال ۲ :</strong> در ترم $f(y)$، متغیر $y$ وجود دارد. اگر مستقیماً آن را جایگزین $x$ کنیم، عبارت $\\forall y P(f(y), y)$ تولید می‌شود که در آن $y$ ورودی تابع به طور ناخواسته توسط $\\forall y$ مقید (اسیر) می‌شود !<br>' +
      'این جایگزینی مستقیم <strong>غیرمجاز</strong> است.<br>' +
      '<strong>تصحیح :</strong> ابتدا متغیر مقید $y$ را به متغیر تازه $z$ بازنام‌گذاری می‌کنیم :<br>' +
      '$F \\equiv \\forall z (P(x, z) \\Rightarrow Q(x))$.<br>' +
      'اکنون جایگزینی $x \\leftarrow f(y)$ کاملاً ایمن است :<br>' +
      '$$\\forall z (P(f(y), z) \\Rightarrow Q(f(y)))$$'
    ] : [
      '<strong>1. Substitution $x \\leftarrow a$ :</strong> La constante $a$ ne contient aucune variable. La substitution est immédiatement admissible :<br>' +
      '$$F[x \\leftarrow a] = \\forall y (P(a, y) \\Rightarrow Q(a))$$',
      '<strong>2. Substitution $x \\leftarrow f(y)$ :</strong> La variable $y$ de $f(y)$ serait illégitimement capturée par le quantificateur $\\forall y$ englobant ! La substitution brute est <strong>interdite</strong>.<br>' +
      '<strong>Correction par $\\alpha$-renommage préalable :</strong><br>' +
      'On renomme la variable liée $y$ en une variable fraîche $z$ :<br>' +
      '$F \\equiv \\forall z (P(x, z) \\Rightarrow Q(x))$.<br>' +
      'La substitution est maintenant sûre et valide :<br>' +
      '$$\\forall z (P(f(y), z) \\Rightarrow Q(f(y)))$$'
    ],
    justification: lang === 'fa' ?
      'تعریف رسمی جایگزینی بدون تله‌اندازی و بازنام‌گذاری آلفا از اسلایدهای درس ۸.' :
      'Respect strict de la condition d\\'admissibilité des termes libres pour une variable.',
    finalAnswer: lang === 'fa' ?
      '۱. $F[x \\leftarrow a] = \\forall y (P(a, y) \\Rightarrow Q(a))$<br>' +
      '۲. جایگزینی مستقیم غیرمجاز است. با بازنام‌گذاری ایمن: $\\forall z (P(f(y), z) \\Rightarrow Q(f(y)))$' :
      '1. $F[x \\leftarrow a] = \\forall y (P(a, y) \\Rightarrow Q(a))$<br>' +
      '2. Capture illicite. Forme valide : $\\forall z (P(f(y), z) \\Rightarrow Q(f(y)))$',
    verification: lang === 'fa' ?
      'بررسی اینکه y در نتیجه نهایی آزاد باقی بماند همان‌طور که در ترم ورودی f(y) آزاد بود.' :
      'Vérifiez que $y$ reste libre dans la formule finale comme elle l\\'était dans le terme substitué.',
    trap: lang === 'fa' ?
      'نوشتن مستقیم $\\forall y P(f(y), y)$ که منجر به کسر کامل نمره در آزمون خواهد شد.' :
      'Erreur classique : substituer brutalement sans renommer le quantificateur.'
  });
"""

make_bundle("w08_td", "fr", td8_fr, td8_interactive)
make_bundle("w08_td", "fa", td8_fa, td8_interactive)

make_bundle("w08_tp", "fr", "<div class='box box-objectives'><div class='box-title'>TP 8 — Modèles Finis en Python</div><p>Évaluation des quantificateurs universel et existentiel sur des univers finis à l'aide de boucles et de compréhensions Python.</p></div>")
make_bundle("w08_tp", "fa", "<div class='box box-objectives'><div class='box-title'>آزمایشگاه TP 8 — ارزیابی مدل‌های متناهی در پایتون</div><p>پیاده‌سازی ارزیابی سورها بر روی دامنه‌های متناهی در زبان پایتون.</p></div>")

make_bundle("w08_annales", "fr", "<div class='box box-objectives'><div class='box-title'>Annales Semaine 8 — Modèles et Structures d'Examen</div><p>Évaluation sur des échiquiers 6x6 (Examen 2019-2020) et structures arithmétiques.</p></div>")
make_bundle("w08_annales", "fa", "<div class='box box-objectives'><div class='box-title'>نمونه سؤالات آزمون هفته ۸</div><p>سؤالات امتحانی سوربن در خصوص ساخت مدل و مثال نقض در صفحه شطرنج.</p></div>")

make_bundle("w08_revision", "fr", "<div class='box box-objectives'><div class='box-title'>Fiche Révision Semaine 8</div><p>Synthèse de la sémantique de Tarski et des règles de substitution.</p></div>")
make_bundle("w08_revision", "fa", "<div class='box box-objectives'><div class='box-title'>برگه مرور هفته ۸</div><p>خلاصه معناشناسی تارسکی و قواعد جایگزینی بدون تله‌اندازی.</p></div>")

print("Week 7 & 8 generation complete!")
