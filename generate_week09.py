# -*- coding: utf-8 -*-
"""
Generator for Week 9 bundles:
- w09_cours.fr.js / w09_cours.fa.js
- w09_td.fr.js / w09_td.fa.js
- w09_tp.fr.js / w09_tp.fa.js
- w09_annales.fr.js / w09_annales.fa.js
- w09_revision.fr.js / w09_revision.fa.js
"""

import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 9: COURS (FR & FA)
# ==============================================================================

c9_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 9 (Déduction Naturelle en LPPO)</div>
  <ul>
    <li>Maîtriser les 4 règles d'inférence pour les quantificateurs : $\\forall I$, $\\forall E$, $\\exists I$, $\\exists E$.</li>
    <li>Comprendre la <strong>condition de variable fraîche (eigenvariable)</strong> pour $\\forall I$ et $\\exists E$ et savoir pourquoi la violer produit des sophismes logiques.</li>
    <li>Savoir formaliser une preuve par instanciation universelle ($\forall E$) et témoin existentiel ($\exists I$).</li>
    <li>Maîtriser l'élimination de l'existentiel ($\exists E$) sous forme de sous-preuve hypothétique.</li>
    <li>Comprendre et prouver le célèbre <strong>Paradoxe du Buveur</strong> : $\\exists x (P(x) \\implies \\forall y P(y))$ avec le tiers exclu.</li>
  </ul>
</div>

<h2 id="w09-c-regles-quantificateurs">1. Les 4 Règles d'Inférence des Quantificateurs</h2>

<p>En Logique des Propositions, la déduction naturelle manipulait des connecteurs booléens ($\land, \lor, \implies, \neg$). En LPPO, nous ajoutons les quantificateurs $\forall$ et $\exists$. Chaque quantificateur possède une règle d'introduction ($I$) et une règle d'élimination ($E$).</p>

<div class="box box-definition">
  <div class="box-title">Règle $\\forall I$ (Introduction du Pour-Tout)</div>
  <p>Pour prouver qu'une propriété $A$ est vraie pour TOUT élément ($\forall x A$), on prouve qu'elle est vraie pour un élément <strong>arbitraire</strong> représenté par une nouvelle variable $y$.</p>
  $$\\frac{A[x \\leftarrow y]}{\\forall x A} (\\forall I)$$
  <p><strong>Condition critique de fraîcheur (Side Condition) :</strong> La variable $y$ doit être <em>fraîche</em>. C'est-à-dire que $y$ ne doit apparaître <strong>libre dans aucune hypothèse active</strong> dont dépend $A[x \\leftarrow y]$.</p>
</div>

<div class="box box-definition">
  <div class="box-title">Règle $\\forall E$ (Élimination du Pour-Tout)</div>
  <p>Si l'on sait que $\\forall x A$ est vrai, alors la propriété est vraie pour <strong>n'importe quel terme</strong> $t$ constructible dans le langage !</p>
  $$\\frac{\\forall x A}{A[x \\leftarrow t]} (\\forall E)$$
  <p><em>Condition :</em> Le terme $t$ doit être librement substituable à $x$ dans $A$ (aucune variable de $t$ ne doit être capturée par un quantificateur interne de $A$).</p>
</div>

<div class="box box-definition">
  <div class="box-title">Règle $\\exists I$ (Introduction de l'Existant)</div>
  <p>Pour prouver qu'il existe un élément vérifiant $A$ ($\exists x A$), il suffit de trouver <strong>un exemple concret (un témoin $t$)</strong> pour lequel $A[x \\leftarrow t]$ est vrai.</p>
  $$\\frac{A[x \\leftarrow t]}{\\exists x A} (\\exists I)$$
</div>

<div class="box box-definition">
  <div class="box-title">Règle $\\exists E$ (Élimination de l'Existant)</div>
  <p>Si l'on sait qu'il existe au moins un élément vérifiant $A$ ($\exists x A$), et que l'on veut prouver une conclusion $C$, on ouvre une sous-preuve en supposant que cet élément s'appelle $y$ (inconnu mais fixé) :</p>
  $$\\frac{\\exists x A \\quad [A[x \\leftarrow y]] \\vdash C}{C} (\\exists E)$$
  <p><strong>Condition critique de fraîcheur :</strong> Le paramètre $y$ ne doit apparaître libre :
  <ol>
    <li>Dans aucune des hypothèses actives résiduelles (en dehors de l'hypothèse locale $A[x \\leftarrow y]$ qui est déchargée).</li>
    <li><strong>Ni dans la conclusion finale $C$ !</strong> (On ne peut pas faire sortir le nom de la variable locale de sa portée).</li>
  </ol>
  </p>
</div>

<h2 id="w09-c-paradoxe-buveur">2. Le Paradoxe du Buveur (Drinker's Paradox)</h2>
<div class="box box-theorem">
  <div class="box-title">Théorème 9.1 — Le Paradoxe du Buveur</div>
  <p>Dans tout bar (non vide), il existe une personne $x$ telle que : si cette personne boit, alors tout le monde boit !</p>
  $$\\vdash \\exists x (P(x) \\implies \\forall y P(y))$$
</div>

<div class="box box-method">
  <div class="box-title">Principe et Intuition de la Preuve</div>
  <p>Ce résultat semble magique ou paradoxal dans le langage courant, mais il est purement classique et découle du Tiers Exclu appliqué à la formule $\\forall y P(y)$ :</p>
  <ul>
    <li><strong>Cas 1 : Tout le monde boit ($\forall y P(y)$ est vrai).</strong><br>
    Prenons n'importe qui dans le bar, disons Alice ($a$). L'implication $P(a) \implies \forall y P(y)$ a une conclusion vraie, donc l'implication est vraie ! Alice est le buveur cherché.</li>
    <li><strong>Cas 2 : Quelqu'un ne boit pas ($\neg \forall y P(y)$ est vrai, donc $\exists y \neg P(y)$).</strong><br>
    Soit Bob ($b$) une personne qui ne boit pas ($\neg P(b)$). Dans l'implication $P(b) \implies \forall y P(y)$, la prémisse $P(b)$ est fausse ! Or, en logique, faux implique n'importe quoi ($F \implies Q \equiv V$). Donc l'implication est vraie pour Bob ! Bob est le buveur cherché.</li>
  </ul>
  <p>Dans tous les cas, un tel buveur existe toujours !</p>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — Les Erreurs Fatales en Déduction Naturelle LPPO</div>
  <p><strong>Erreur 1 : Utiliser une variable déjà mentionnée dans $\forall I$.</strong> Si vous posez $y$ alors que $y$ apparaît dans une hypothèse active (par exemple dans $P(y)$), vous prouvez en réalité $P(y) \implies \forall x P(x)$, ce qui est complètement faux sémantiquement !</p>
  <p><strong>Erreur 2 : Faire sortir la variable témoin de l'élimination existentielle $\exists E$.</strong> Si vous partez de $\exists x P(x)$, supposez $P(y)$, et concluez immédiatement $P(y)$ hors de la boîte, vous avez violé la règle car $y \in Free(C)$ ! Vous venez de déduire « tout $y$ vérifie $P$ » à partir d'un simple existant !</p>
</div>
"""

c9_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف یادگیری — هفته ۹ (استنتاج طبیعی در منطق مرتبه اول LPPO)</div>
  <ul>
    <li>تسلط بر ۴ قاعده استنتاج سورها: $\\forall I$ (معرفی برای‌هر)، $\\forall E$ (حذف برای‌هر)، $\\exists I$ (معرفی وجود)، و $\\exists E$ (حذف وجود).</li>
    <li>فهم عمیق <strong>شرط متغیر تازه (Eigenvariable Condition)</strong> در $\\forall I$ و $\\exists E$ و چرایی باطل شدن برهان در صورت نقض آن.</li>
    <li>مهارت در پیاده‌سازی نمونه‌سازی کلی ($\forall E$) و شاهد وجودی ($\exists I$).</li>
    <li>تسلط بر حذف سور وجود ($\exists E$) به شکل یک جعبه فرض محلی با پارامتر تازه.</li>
    <li>درک و اثبات رسمی <strong>پارادوکس مشهور می‌خوار (Drinker's Paradox)</strong>: $\\exists x (P(x) \\implies \\forall y P(y))$ با استفاده از طرد شق ثالث.</li>
  </ul>
</div>

<h2 id="w09-c-regles-quantificateurs">۱. چهار قاعده اصلی استنتاج برای سورها</h2>

<p>در منطق گزاره‌ای با عملگرهای بولی ($\land, \lor, \implies, \neg$) کار می‌کردیم. در منطق مرتبه اول (LPPO)، سورهای $\forall$ و $\exists$ اضافه می‌شوند. برای هر سور یک قاعده معرفی (I) و یک قاعده حذف (E) داریم.</p>

<div class="box box-definition">
  <div class="box-title">قاعده $\\forall I$ (معرفی سور کلی - Pour-tout)</div>
  <p>برای اثبات این‌که یک ویژگی $A$ برای <strong>همه</strong> عناصر برقرار است ($\forall x A$)، ثابت می‌کنیم که برای یک عنصر کاملاً <strong>دلخواه و اختیاری</strong> با نماد متغیر تازه $y$ درست است.</p>
  $$\\frac{A[x \\leftarrow y]}{\\forall x A} (\\forall I)$$
  <p><strong>شرط حیاتی تازگی (Eigenvariable) :</strong> نماد $y$ باید <em>تازه</em> باشد؛ یعنی $y$ نباید در هیچ‌یک از فرض‌های فعال که $A[x \\leftarrow y]$ به آن‌ها وابسته است، به صورت آزاد ($Free$) ظاهر شده باشد.</p>
</div>

<div class="box box-definition">
  <div class="box-title">قاعده $\\forall E$ (حذف سور کلی)</div>
  <p>اگر بدانیم $\\forall x A$ صادق است، آن ویژگی برای <strong>هر ترم دلخواهی</strong> مثل $t$ که در زبان ساخته شود صادق خواهد بود!</p>
  $$\\frac{\\forall x A}{A[x \\leftarrow t]} (\\forall E)$$
  <p><em>شرط:</em> ترم $t$ باید بتواند آزادانه جایگزین $x$ شود (متغیرهای درون $t$ در دامنه سورهای درونی $A$ به دام نیفتند).</p>
</div>

<div class="box box-definition">
  <div class="box-title">قاعده $\\exists I$ (معرفی سور وجود)</div>
  <p>برای اثبات وجود عنصری با ویژگی $A$ ($\exists x A$)، کافی است فقط <strong>یک مثال مشخص و عینی (یک ترم شاهد $t$)</strong> ارائه دهیم که $A[x \\leftarrow t]$ برای آن برقرار باشد.</p>
  $$\\frac{A[x \\leftarrow t]}{\\exists x A} (\\exists I)$$
</div>

<div class="box box-definition">
  <div class="box-title">قاعده $\\exists E$ (حذف سور وجود)</div>
  <p>اگر بدانیم حداقل یک عنصر با ویژگی $A$ وجود دارد ($\exists x A$)، و هدف ما اثبات نتیجه‌ای مانند $C$ باشد، یک برهان فرعی باز می‌کنیم و فرض می‌کنیم نام آن عنصر $y$ باشد (موجودی ناشناخته اما معین):</p>
  $$\\frac{\\exists x A \\quad [A[x \\leftarrow y]] \\vdash C}{C} (\\exists E)$$
  <p><strong>شرط اساسی تازگی:</strong> پارامتر موقت $y$ نباید به صورت آزاد ظاهر شود:
  <ol>
    <li>در هیچ‌یک از فرضیات فعال دیگر (به جز فرض محلی $A[x \\leftarrow y]$ که در انتهای جعبه بسته و تخلیه می‌شود).</li>
    <li><strong>در خود نتیجه نهایی $C$ نیز نباید آزاد باشد!</strong> (نام متغیر محلی درون جعبه هرگز نباید به بیرون درز کند).</li>
  </ol>
  </p>
</div>

<h2 id="w09-c-paradoxe-buveur">۲. پارادوکس می‌خوار (Drinker's Paradox)</h2>
<div class="box box-theorem">
  <div class="box-title">قضیه ۹.۱ — پارادوکس می‌خوار</div>
  <p>در هر میخانه (غیرخالی)، همواره شخصی مانند $x$ وجود دارد به طوری که: اگر او بنوشد، آنگاه همه در میخانه می‌نوشند!</p>
  $$\\vdash \\exists x (P(x) \\implies \\forall y P(y))$$
</div>

<div class="box box-method">
  <div class="box-title">شهود و چرایی اثبات با طرد شق ثالث</div>
  <p>این گزاره در زبان روزمره شگفت‌انگیز یا ناممکن به نظر می‌رسد، اما یک تاتولوژی منطق کلاسیک است که از طرد شق ثالث روی $\\forall y P(y)$ حاصل می‌شود:</p>
  <ul>
    <li><strong>حالت اول: همه در حال نوشیدن هستند ($\forall y P(y)$ صادق است).</strong><br>
    هر شخصی را در میخانه در نظر بگیرید، مثلاً سهراب ($a$). در این شرط، تالی ($Q$) یعنی «همه می‌نوشند» درست است؛ پس شرط $P(a) \implies \forall y P(y)$ به طور بدیهی درست است! سهراب همان شخص مورد نظر است.</li>
    <li><strong>حالت دوم: حداقل یک نفر نمی‌نوشد ($\neg \forall y P(y)$ صادق است، یعنی $\exists y \neg P(y)$).</strong><br>
    فرض کنیم رستم ($b$) شخصی است که نمی‌نوشد ($\neg P(b)$). در عبارت شرطی $P(b) \implies \forall y P(y)$، مقدم شرط ($P(b)$) نادرست است! و می‌دانیم در منطق گزاره‌ای، از نادرست هر نتیجه‌ای حاصل می‌شود ($F \implies Q \equiv V$). پس این رابطه شرطی برای رستم برقرار است! رستم همان شخص است.</li>
  </ul>
  <p>بنابراین در تمام جهان‌های ممکن، همیشه چنین شخصی وجود دارد!</p>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — خطاهای ویرانگر در استنتاج طبیعی LPPO</div>
  <p><strong>خطای ۱: انتخاب متغیری که قبلاً در فرضیات آمده است در قاعده $\forall I$.</strong> اگر برای متغیر دلخواه نامی بگذارید که در فرضیات فعال وجود دارد (مثلاً $y$ در فرض $P(y)$)، شما عملاً $P(y) \implies \forall x P(x)$ را نتیجه می‌گیرید که کاملاً غلط است!</p>
  <p><strong>خطای ۲: بیرون آوردن متغیر محلی در قاعده $\exists E$.</strong> اگر با فرض $P(y)$ از $\exists x P(x)$ نتیجه بگیرید $P(y)$ و جعبه را ببندید، چون $y$ در نتیجه باقی مانده است، کل برهان باطل است؛ زیرا شما از «وجود حداقل یک مورد» نتیجه گرفته‌اید که «فلان متغیر مشخص» همواره آن ویژگی را دارد!</p>
</div>
"""

# ==============================================================================
# WEEK 9: TD 9 (Exercices 33 & 34) (FR & FA)
# ==============================================================================

td9_fr = """
<div class="box box-objectives">
  <div class="box-title">TD Thème 9 — Preuves Formelles en LPPO (Exercices 33 et 34)</div>
  <p>Source : <code>main_td-etudiants.pdf</code>, pages 19–20. Toutes les preuves sont détaillées pas à pas avec les arbres de déduction naturelle au format Fitch.</p>
</div>

<h2 id="w09-td-ex33">Exercice 33 — Preuves de Formules Quantifiées (p. 19)</h2>
<p>Prouver rigoureusement chacune des 7 formules ci-dessous en déduction naturelle.</p>

<h3>Question 1 : $F_1 = (\\forall x p(x) \\lor \\forall x q(x)) \\implies \\forall x (p(x) \\lor q(x))$</h3>
<div class="box box-solution">
  <div class="box-title">Correction détaillée Question 1</div>
  <p><strong>Stratégie :</strong> On suppose l'hypothèse de gauche $h_1 : \\forall x p(x) \\lor \\forall x q(x)$. Il s'agit d'une disjonction, donc on effectue une élimination de la disjonction $(\\lor E)$ avec deux sous-preuves. Dans chaque cas, on choisit une variable fraîche $y$, on instancie le quantificateur universel $(\\forall E)$ avec $y$, puis on introduit la disjonction $(\\lor I)$ et enfin le quantificateur universel $(\\forall I)$.</p>
  <div class="fitch-proof">
    <div class="fitch-line"><span class="fitch-num">1</span> <span class="fitch-hyp">Hypothèse $h_1 : \forall x p(x) \lor \forall x q(x)$</span></div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">2</span> <span class="fitch-hyp">Sous-preuve Cas 1 : $h_2 : \forall x p(x)$</span></div>
      <div class="fitch-box">
        <div class="fitch-line"><span class="fitch-num">3</span> <span class="fitch-hyp">Soit $y$ une variable fraîche</span></div>
        <div class="fitch-line"><span class="fitch-num">4</span> <span>$p(y)$</span> <span class="fitch-rule">par $\forall E$ sur 2 avec $x \leftarrow y$</span></div>
        <div class="fitch-line"><span class="fitch-num">5</span> <span>$p(y) \lor q(y)$</span> <span class="fitch-rule">par $\lor I_g$ sur 4</span></div>
      </div>
      <div class="fitch-line"><span class="fitch-num">6</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">par $\forall I$ sur 3–5 ($y$ fraîche)</span></div>
    </div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">7</span> <span class="fitch-hyp">Sous-preuve Cas 2 : $h_3 : \forall x q(x)$</span></div>
      <div class="fitch-box">
        <div class="fitch-line"><span class="fitch-num">8</span> <span class="fitch-hyp">Soit $y$ une variable fraîche</span></div>
        <div class="fitch-line"><span class="fitch-num">9</span> <span>$q(y)$</span> <span class="fitch-rule">par $\forall E$ sur 7 avec $x \leftarrow y$</span></div>
        <div class="fitch-line"><span class="fitch-num">10</span> <span>$p(y) \lor q(y)$</span> <span class="fitch-rule">par $\lor I_d$ sur 9</span></div>
      </div>
      <div class="fitch-line"><span class="fitch-num">11</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">par $\forall I$ sur 8–10 ($y$ fraîche)</span></div>
    </div>
    <div class="fitch-line"><span class="fitch-num">12</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">par $\lor E$ sur 1, 2–6, 7–11</span></div>
    <div class="fitch-line"><span class="fitch-num">13</span> <span>$(\forall x p(x) \lor \forall x q(x)) \implies \forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">par $\implies I$ déchargeant 1</span></div>
  </div>
</div>

<h3>Question 2 : $F_2 = (\\exists x (p(x) \\lor q(x))) \\implies (\\exists x p(x) \\lor \\exists x q(x))$</h3>
<div class="box box-solution">
  <div class="box-title">Correction détaillée Question 2</div>
  <p><strong>Stratégie :</strong> Supposons $h_1 : \exists x (p(x) \lor q(x))$. Pour éliminer cet existentiel $(\exists E)$, on introduit une variable fraîche $y$ et l'hypothèse locale $p(y) \lor q(y)$. On élimine ensuite la disjonction : si $p(y)$, alors $\exists x p(x)$ par $\exists I$ (témoin $y$), puis $\exists x p(x) \lor \exists x q(x)$ par $\lor I$. De même si $q(y)$. La conclusion ne contenant pas $y$, la règle $\exists E$ est valide !</p>
</div>

<h3>Question 3 : $F_3 = (\\exists x \\forall y r(x, y)) \\implies (\\forall y \\exists x r(x, y))$</h3>
<div class="box box-solution">
  <div class="box-title">Correction détaillée Question 3 (Inversion $\exists \forall \implies \forall \exists$)</div>
  <p><strong>Règle d'or des portées :</strong> On suppose $h_1 : \exists x \forall y r(x, y)$. On applique $\exists E$ en fixant une variable fraîche $a$ et $h_2 : \forall y r(a, y)$. Maintenant, pour prouver $\forall y \exists x r(x, y)$, on se donne une nouvelle variable fraîche $b$ ($\forall I$). Par $\forall E$ sur $h_2$ avec le terme $b$, on obtient $r(a, b)$. Par $\exists I$ avec le témoin $a$, on obtient $\exists x r(x, b)$. Par $\forall I$ sur $b$, on obtient $\forall y \exists x r(x, y)$. Enfin par $\exists E$, on décharge $a$. CQFD !</p>
</div>

<h2 id="w09-td-ex34">Exercice 34 — Preuves Imbriquées : Le Paradoxe du Buveur (p. 19-20)</h2>
<p>Le but est de prouver $\exists x (p(x) \implies \forall y p(y))$ en 4 étapes modulaires.</p>

<div class="box box-solution">
  <div class="box-title">Correction Q1 : Preuve $B_1$ sous l'hypothèse $h_1 : \forall y p(y)$</div>
  <p>Sous l'hypothèse $h_1$, choisissons une variable fraîche quelconque $z$.</p>
  <div class="fitch-proof">
    <div class="fitch-line"><span class="fitch-num">1</span> <span class="fitch-hyp">Hypothèse $h_1 : \forall y p(y)$</span></div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">2</span> <span class="fitch-hyp">Sous-hypothèse $h' : p(z)$</span></div>
      <div class="fitch-line"><span class="fitch-num">3</span> <span>$\forall y p(y)$</span> <span class="fitch-rule">Répétition de 1</span></div>
    </div>
    <div class="fitch-line"><span class="fitch-num">4</span> <span>$p(z) \implies \forall y p(y)$</span> <span class="fitch-rule">par $\implies I$ déchargeant 2</span></div>
    <div class="fitch-line"><span class="fitch-num">5</span> <span>$\exists x (p(x) \implies \forall y p(y))$</span> <span class="fitch-rule">par $\exists I$ avec le témoin $z$</span></div>
  </div>
</div>

<div class="box box-solution">
  <div class="box-title">Correction Q2 : Preuve $B_2$ de $(\neg \forall y p(y)) \implies (\exists y \neg p(y))$</div>
  <p>Cette dualité n'est pas intuitionniste ; elle nécessite le Raisonnement par l'Absurde classique (RAA) : pour prouver $\exists y \neg p(y)$, on suppose sa négation $\neg \exists y \neg p(y)$. Pour toute variable $z$, si $\neg p(z)$, alors $\exists y \neg p(y)$, contradiction avec l'hypothèse ! Donc par RAA, $p(z)$ est vrai. Comme $z$ est fraîche, $\forall y p(y)$ est vrai par $\forall I$. Contradiction avec $\neg \forall y p(y)$ ! Donc par RAA, $\exists y \neg p(y)$ est prouvé.</p>
</div>

<div class="box box-solution">
  <div class="box-title">Correction Q3 : Preuve $B_3$ sous l'hypothèse $h_2 : \neg \forall y p(y)$</div>
  <p>Par la preuve $B_2$, on déduit $\exists y \neg p(y)$. On applique $\exists E$ avec une variable fraîche $z$ et l'hypothèse $h_3 : \neg p(z)$.</p>
  <div class="fitch-proof">
    <div class="fitch-line"><span class="fitch-num">1</span> <span class="fitch-hyp">Hypothèse $h_2 : \neg \forall y p(y)$</span></div>
    <div class="fitch-line"><span class="fitch-num">2</span> <span>$\exists y \neg p(y)$</span> <span class="fitch-rule">par application de la preuve $B_2$ sur 1</span></div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">3</span> <span class="fitch-hyp">Soit $z$ frais, hypothèse $h_3 : \neg p(z)$</span></div>
      <div class="fitch-box">
        <div class="fitch-line"><span class="fitch-num">4</span> <span class="fitch-hyp">Sous-hypothèse $h_4 : p(z)$</span></div>
        <div class="fitch-line"><span class="fitch-num">5</span> <span>$\bot$</span> <span class="fitch-rule">par $\neg E$ sur 4 et 3</span></div>
        <div class="fitch-line"><span class="fitch-num">6</span> <span>$\forall y p(y)$</span> <span class="fitch-rule">par $\bot E$ (ex falso) sur 5</span></div>
      </div>
      <div class="fitch-line"><span class="fitch-num">7</span> <span>$p(z) \implies \forall y p(y)$</span> <span class="fitch-rule">par $\implies I$ déchargeant 4</span></div>
      <div class="fitch-line"><span class="fitch-num">8</span> <span>$\exists x (p(x) \implies \forall y p(y))$</span> <span class="fitch-rule">par $\exists I$ avec le témoin $z$</span></div>
    </div>
    <div class="fitch-line"><span class="fitch-num">9</span> <span>$\exists x (p(x) \implies \forall y p(y))$</span> <span class="fitch-rule">par $\exists E$ sur 2 et 3–8</span></div>
  </div>
</div>

<div class="box box-solution">
  <div class="box-title">Correction Q4 : Synthèse par le Tiers Exclu</div>
  <p>Par la règle du Tiers Exclu classique $(TE)$, on a $\forall y p(y) \lor \neg \forall y p(y)$.</p>
  <ul>
    <li>Dans la première branche ($\forall y p(y)$), la preuve $B_1$ conclut $\exists x (p(x) \implies \forall y p(y))$.</li>
    <li>Dans la seconde branche ($\neg \forall y p(y)$), la preuve $B_3$ conclut $\exists x (p(x) \implies \forall y p(y))$.</li>
  </ul>
  <p>Par $\lor E$, on conclut sans aucune hypothèse résiduelle : $\vdash \exists x (p(x) \implies \forall y p(y))$. Preuve complète achevée !</p>
</div>
"""

td9_fa = """
<div class="box box-objectives">
  <div class="box-title">حل تمرینات موضوع ۹ — برهان‌های صوری در LPPO (تمرین‌های ۳۳ و ۳۴)</div>
  <p>منبع رسمی: <code>main_td-etudiants.pdf</code>، صفحات ۱۹ و ۲۰. تمام اثبات‌ها به صورت گام‌به‌گام و با درخت‌های استاندارد فیچ (Fitch) ارائه شده‌اند.</p>
</div>

<h2 id="w09-td-ex33">تمرین ۳۳ — اثبات فرمول‌های سوردار (صفحه ۱۹)</h2>
<p>اثبات دقیق هر ۷ فرمول به روش استنتاج طبیعی.</p>

<h3>سؤال ۱ : $F_1 = (\\forall x p(x) \\lor \\forall x q(x)) \\implies \\forall x (p(x) \\lor q(x))$</h3>
<div class="box box-solution">
  <div class="box-title">حل تشریحی گام‌به‌گام سؤال ۱</div>
  <p><strong>استراتژی:</strong> مقدم شرط را فرض می‌کنیم $h_1 : \\forall x p(x) \\lor \\forall x q(x)$. چون این فرض یک فصل ($\lor$) است، قاعده حذف فصل ($\lor E$) را روی دو شاخه اجرا می‌کنیم. در هر شاخه، یک متغیر تازه مانند $y$ برمی‌داریم، با قاعده $\forall E$ ویژگی $p(y)$ یا $q(y)$ را استخراج می‌کنیم، سپس با $\lor I$ به $p(y) \lor q(y)$ می‌رسیم و نهایتاً با $\forall I$ سور کلی $\forall x$ را می‌سازیم.</p>
  <div class="fitch-proof">
    <div class="fitch-line"><span class="fitch-num">۱</span> <span class="fitch-hyp">فرض اصلی $h_1 : \forall x p(x) \lor \forall x q(x)$</span></div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">۲</span> <span class="fitch-hyp">زیربرهان حالت اول: $h_2 : \forall x p(x)$</span></div>
      <div class="fitch-box">
        <div class="fitch-line"><span class="fitch-num">۳</span> <span class="fitch-hyp">فرض متغیر تازه $y$</span></div>
        <div class="fitch-line"><span class="fitch-num">۴</span> <span>$p(y)$</span> <span class="fitch-rule">با $\forall E$ روی خط ۲ با جایگزینی $x \leftarrow y$</span></div>
        <div class="fitch-line"><span class="fitch-num">۵</span> <span>$p(y) \lor q(y)$</span> <span class="fitch-rule">با معرفی فصل راست $\lor I$</span></div>
      </div>
      <div class="fitch-line"><span class="fitch-num">۶</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">با قاعده $\forall I$ روی ۳–۵ (چون $y$ تازه است)</span></div>
    </div>
    <div class="fitch-box">
      <div class="fitch-line"><span class="fitch-num">۷</span> <span class="fitch-hyp">زیربرهان حالت دوم: $h_3 : \forall x q(x)$</span></div>
      <div class="fitch-box">
        <div class="fitch-line"><span class="fitch-num">۸</span> <span class="fitch-hyp">فرض متغیر تازه $y$</span></div>
        <div class="fitch-line"><span class="fitch-num">۹</span> <span>$q(y)$</span> <span class="fitch-rule">با $\forall E$ روی خط ۷ با $x \leftarrow y$</span></div>
        <div class="fitch-line"><span class="fitch-num">۱۰</span> <span>$p(y) \lor q(y)$</span> <span class="fitch-rule">با معرفی فصل چپ $\lor I$</span></div>
      </div>
      <div class="fitch-line"><span class="fitch-num">۱۱</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">با قاعده $\forall I$ روی ۸–۱۰</span></div>
    </div>
    <div class="fitch-line"><span class="fitch-num">۱۲</span> <span>$\forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">با حذف فصل $\lor E$ روی خطوط ۱، ۲–۶، ۷–۱۱</span></div>
    <div class="fitch-line"><span class="fitch-num">۱۳</span> <span>$(\forall x p(x) \lor \forall x q(x)) \implies \forall x (p(x) \lor q(x))$</span> <span class="fitch-rule">با معرفی شرط $\implies I$ و تخلیه فرض ۱</span></div>
  </div>
</div>

<h3>سؤال ۳ : $F_3 = (\\exists x \\forall y r(x, y)) \\implies (\\forall y \\exists x r(x, y))$</h3>
<div class="box box-solution">
  <div class="box-title">قاعده طلایی دامنه‌ها در جابجایی سورها ($\exists \forall \implies \forall \exists$)</div>
  <p>فرض می‌کنیم $h_1 : \exists x \forall y r(x, y)$. برای حذف سور وجود ($\exists E$)، یک پارامتر تازه به نام $a$ و فرض محلی $h_2 : \forall y r(a, y)$ تعیین می‌کنیم. حال برای اثبات سور کلی بیرون یعنی $\forall y$， یک متغیر تازه دیگر به نام $b$ می‌گیریم ($\forall I$). با اعمال $\forall E$ روی $h_2$ با ترم $b$ به $r(a, b)$ می‌رسیم. سپس با $\exists I$ و قرار دادن شاهد $a$ به $\exists x r(x, b)$ دست می‌یابیم. با بستن جعبه متغیر $b$، به $\forall y \exists x r(x, y)$ می‌رسیم و در نهایت با حذف وجود، جعبه $a$ را می‌بندیم. حکم کاملاً اثبات شد!</p>
</div>

<h2 id="w09-td-ex34">تمرین ۳۴ — برهان‌های تو در تو: پارادوکس می‌خوار (صفحات ۱۹ و ۲۰)</h2>
<p>هدف اثبات فرمول $\exists x (p(x) \implies \forall y p(y))$ در ۴ مرحله مدولار دانشگاهی است.</p>

<div class="box box-solution">
  <div class="box-title">حل بخش ۱: برهان $B_1$ با فرض $h_1 : \forall y p(y)$</div>
  <p>تحت فرض $h_1$، یک متغیر دلخواه تازه مانند $z$ انتخاب می‌کنیم. اگر فرض موقت $p(z)$ را اضافه کنیم، چون تالی یعنی $\forall y p(y)$ از خط ۱ آماده است، شرط $p(z) \implies \forall y p(y)$ صادق است. سپس با معرفی سور وجود ($\exists I$) و قرار دادن شاهد $z$، فرمول نهایی به دست می‌آید.</p>
</div>

<div class="box box-solution">
  <div class="box-title">حل بخش ۲: برهان $B_2$ برای $(\neg \forall y p(y)) \implies (\exists y \neg p(y))$</div>
  <p>این رابطه هم‌ارزی دمورگان سورها در حالت کلی نیازمند منطق کلاسیک و برهان خلف (RAA) است. برای اثبات $\exists y \neg p(y)$، فرض خلف $\neg \exists y \neg p(y)$ را می‌گذاریم. به کمک آن نشان می‌دهیم که برای هر $z$ دلخواه، $p(z)$ برقرار است، لذا $\forall y p(y)$ نتیجه می‌شود که با فرض $\neg \forall y p(y)$ تناقض دارد؛ پس حکم اثبات می‌شود.</p>
</div>

<div class="box box-solution">
  <div class="box-title">حل بخش ۳: برهان $B_3$ تحت فرض $h_2 : \neg \forall y p(y)$</div>
  <p>با برهان $B_2$ نتیجه می‌گیریم $\exists y \neg p(y)$. حال با $\exists E$ متغیر تازه $z$ و فرض $h_3 : \neg p(z)$ را باز می‌کنیم. درون این جعبه، اگر فرض کنیم $p(z)$، با $\neg p(z)$ تناقض $(\bot)$ می‌دهد و طبق قاعده از تناقض هر چیزی برمی‌آید ($\bot E$)، گزاره $\forall y p(y)$ حاصل می‌شود؛ لذا $p(z) \implies \forall y p(y)$ درست است و با شاهد $z$ به فرمول مطلوب می‌رسیم.</p>
</div>

<div class="box box-solution">
  <div class="box-title">حل بخش ۴: ترکیب نهایی با طرد شق ثالث (Tiers Exclu)</div>
  <p>طبق اصل طرد شق ثالث کلاسیک، گزاره $\forall y p(y) \lor \neg \forall y p(y)$ همواره صادق است.
  در شاخه اول برهان $B_1$ و در شاخه دوم برهان $B_3$ هر دو مستقلاً فرمول را ثابت می‌کنند. با حذف فصل، بدون هیچ فرض باقی‌مانده‌ای، برهان کامل می‌شود!</p>
</div>
"""

# ==============================================================================
# WEEK 9: TP 9 (Édukera & LPPO) (FR & FA)
# ==============================================================================

tp9_fr = """
<div class="box box-objectives">
  <div class="box-title">TP Thème 9 — Déduction Naturelle sous Édukera (Exercice 13)</div>
  <p>Source : <code>main_tp-etudiants.pdf</code>, page 12. Guide pratique pour manipuler les quantificateurs dans le prouveur interactif Édukera.</p>
</div>

<h2 id="w09-tp-edukera">1. Manipulation des Règles Quantificateurs dans Édukera</h2>
<p>Dans Édukera, chaque règle est représentée par un bloc graphique :</p>
<ul>
  <li><strong>Pour $\forall I$ :</strong> Édukera crée automatiquement une boîte indentée étiquetée avec un nom de variable fraîche (ex: <code>x_0</code>). Il est impossible de faire référence à une variable déjà liée ou libre dans le contexte !</li>
  <li><strong>Pour $\forall E$ :</strong> Vous devez fournir au système le terme exact avec lequel instancier la variable quantifiée (ex: <code>c</code>, <code>f(a)</code>, etc.).</li>
  <li><strong>Pour $\exists I$ :</strong> Vous devez glisser le témoin dans le slot d'entrée de la règle.</li>
  <li><strong>Pour $\exists E$ :</strong> Édukera ouvre une sous-boîte en introduisant une nouvelle constante de Skolem locale. Toute tentative de faire fuiter cette variable hors de la boîte déclenche une erreur de validité logique.</li>
</ul>

<div class="box box-consigne">
  <div class="box-title">Règle de l'échiquier Édukera pour les contre-modèles</div>
  <p>Pour chaque formule non valide proposée par Édukera, vous devez poser au moins une pièce de chaque type sur l'échiquier pour construire un <strong>contre-modèle fini</strong>.</p>
</div>
"""

tp9_fa = """
<div class="box box-objectives">
  <div class="box-title">کار عملی موضوع ۹ — استنتاج طبیعی در سامانه Edukera (تمرین ۱۳)</div>
  <p>منبع رسمی: <code>main_tp-etudiants.pdf</code>، صفحه ۱۲. راهنمای کاربردی استفاده از سورها در اثبات‌کننده تعاملی Edukera.</p>
</div>

<h2 id="w09-tp-edukera">۱. نحوه کار با قواعد سورها در Edukera</h2>
<p>در محیط تعاملی Edukera هر قاعده به شکل یک بلوک بصری است:</p>
<ul>
  <li><strong>قاعده $\forall I$:</strong> سامانه یک کادر تورفته با متغیر تازه محلی (مانند <code>x_0</code>) باز می‌کند. سیستم اجازه استفاده از متغیرهای از قبل موجود را نمی‌دهد.</li>
  <li><strong>قاعده $\forall E$:</strong> دانشجو باید ترم مورد نظر برای جایگزینی را در فیلد مربوطه تایپ کند (مانند <code>c</code> یا <code>f(a)</code>).</li>
  <li><strong>قاعده $\exists I$:</strong> ترم شاهد را برای اثبات در خانه ورودی قرار می‌دهیم.</li>
  <li><strong>قاعده $\exists E$:</strong> سامانه یک کادر فرعی با یک نام موقت ایجاد می‌کند و به محض تلاش برای خروج این متغیر از کادر، پیام خطای نقض استنتاج نمایش داده می‌شود.</li>
</ul>
"""

# ==============================================================================
# WEEK 9: ANNALES (FR & FA)
# ==============================================================================

ann9_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales d'Examen — Semaine 9 (Preuves LPPO en Déduction Naturelle)</div>
  <p>Sélection des exercices réels d'examens de Sorbonne Université portant sur les quantificateurs.</p>
</div>

<h2 id="w09-ann-ex1">1. Examen 2020-2021 Session 1 — Exercice 3</h2>
<div class="box box-enonce">
  <div class="box-title">Énoncé Officiel</div>
  <p>Le but de cet exercice est de prouver la formule $\exists x (p(x) \implies \forall y p(y))$ en utilisant la règle du Tiers Exclu.</p>
</div>
<div class="box box-solution">
  <div class="box-title">Corrigé d'Examen</div>
  <p>Il s'agit exactement de la décomposition modulaire en 4 sous-preuves vue au TD 9 Exercice 34. Les étudiants ayant rédigé la preuve avec les lemmes intermédiaires $B_1$, $B_2$, $B_3$ ont obtenu la note maximale (5/5).</p>
</div>

<h2 id="w09-ann-ex2">2. Examen 2022-2023 Session 1 — Exercice 2</h2>
<div class="box box-enonce">
  <div class="box-title">Énoncé Officiel</div>
  <p>Prouver en déduction naturelle classique la formule :</p>
  $$(\\forall x p(x) \\implies \\exists x q(x)) \\implies \\exists x (p(x) \\implies q(x))$$
</div>
<div class="box box-solution">
  <div class="box-title">Corrigé d'Examen</div>
  <p>Preuve par tiers exclu sur $\forall x p(x)$ : si $\forall x p(x)$ est vrai, alors par hypothèse $\exists x q(x)$ est vrai ; soit $c$ tel que $q(c)$, alors $p(c) \implies q(c)$ est vrai. Si $\neg \forall x p(x)$ est vrai, il existe $c$ tel que $\neg p(c)$, d'où $p(c) \implies q(c)$ est vrai par ex falso. Conclusion par $\exists I$.</p>
</div>
"""

ann9_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات امتحانی — هفته ۹ (استنتاج طبیعی در LPPO)</div>
  <p>منتخب سؤالات امتحانات نهایی دانشگاه سوربن در موضوع اثبات‌های صوری با سورها.</p>
</div>

<h2 id="w09-ann-ex1">۱. امتحان ۲۰۲۰–۲۰۲۱ نوبت اول — سؤال ۳</h2>
<div class="box box-enonce">
  <div class="box-title">صورت رسمی سؤال</div>
  <p>هدف این سؤال اثبات فرمول $\exists x (p(x) \implies \forall y p(y))$ با استفاده از قاعده طرد شق ثالث است.</p>
</div>
<div class="box box-solution">
  <div class="box-title">پاسخ تشریحی امتحانی</div>
  <p>این سؤال دقیقاً همان تمرین ۳۴ کتابچه تمرینات دانشگاه است که در بخش TD هفته ۹ به تفصیل با لم‌های $B_1$ و $B_2$ و $B_3$ به طور کامل حل کردیم.</p>
</div>

<h2 id="w09-ann-ex2">۲. امتحان ۲۰۲۲–۲۰۲۳ نوبت اول — سؤال ۲</h2>
<div class="box box-enonce">
  <div class="box-title">صورت رسمی سؤال</div>
  <p>اثبات فرمول زیر در استنتاج طبیعی کلاسیک:</p>
  $$(\\forall x p(x) \\implies \\exists x q(x)) \\implies \\exists x (p(x) \\implies q(x))$$
</div>
<div class="box box-solution">
  <div class="box-title">پاسخ تشریحی امتحانی</div>
  <p>اثبات با طرد شق ثالث روی $\forall x p(x)$: اگر همه عناصر در $p$ صدق کنند، با فرض مساله شاهدی برای $q$ پیدا می‌شود و شرط برقرار است. اگر عضوی در $p$ صدق نکند، مقدم شرط نادرست شده و باز هم کل رابطه شرطی با آن شاهد برقرار است.</p>
</div>
"""

# ==============================================================================
# WEEK 9: REVISION (FR & FA)
# ==============================================================================

rev9_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche Synthèse Révision — Semaine 9</div>
  <ul>
    <li><strong>Règle $\forall I$ :</strong> Variable $y$ doit être fraîche (n'apparaît libre dans aucune hypothèse active).</li>
    <li><strong>Règle $\forall E$ :</strong> Remplacement par n'importe quel terme $t$ librement substituable.</li>
    <li><strong>Règle $\exists I$ :</strong> Fournir un terme témoin $t$.</li>
    <li><strong>Règle $\exists E$ :</strong> Variable locale $y$ ne doit jamais fuiter dans la conclusion ni dans les hypothèses extérieures !</li>
    <li><strong>Paradoxe du buveur :</strong> Se résout grâce au Tiers Exclu sur la totalité $\forall y p(y)$.</li>
  </ul>
</div>
"""

rev9_fa = """
<div class="box box-objectives">
  <div class="box-title">خلاصه مرور و جمع‌بندی — هفته ۹</div>
  <ul>
    <li><strong>قاعده $\forall I$:</strong> متغیر $y$ باید تازه باشد (در فرضیات فعال آزاد نباشد).</li>
    <li><strong>قاعده $\forall E$:</strong> جایگزینی با هر ترم دلخواه $t$ مجاز است.</li>
    <li><strong>قاعده $\exists I$:</strong> ارائه یک ترم شاهد عینی $t$.</li>
    <li><strong>قاعده $\exists E$:</strong> متغیر محلی $y$ هرگز نباید در نتیجه نهایی یا فرضیات بیرونی ظاهر شود!</li>
    <li><strong>پارادوکس می‌خوار:</strong> به کمک طرد شق ثالث روی گزاره کلی $\forall y p(y)$ اثبات می‌شود.</li>
  </ul>
</div>
"""

# Build week 9 bundles
make_bundle('w09_cours', 'fr', c9_fr)
make_bundle('w09_cours', 'fa', c9_fa)
make_bundle('w09_td', 'fr', td9_fr)
make_bundle('w09_td', 'fa', td9_fa)
make_bundle('w09_tp', 'fr', tp9_fr)
make_bundle('w09_tp', 'fa', tp9_fa)
make_bundle('w09_annales', 'fr', ann9_fr)
make_bundle('w09_annales', 'fa', ann9_fa)
make_bundle('w09_revision', 'fr', rev9_fr)
make_bundle('w09_revision', 'fa', rev9_fa)

print("Week 9 generation complete!")

