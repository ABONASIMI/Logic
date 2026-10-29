import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 3: COURS (FR & FA)
# ==============================================================================

cours_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 3</div>
  <ul>
    <li>Comprendre la notion de fonction booléenne et son dénombrement ($2^{2^n}$).</li>
    <li>Définir rigoureusement les littéraux, clauses disjonctives, termes, FNC et FND.</li>
    <li>Maîtriser l'algorithme canonique de passage de la table de vérité vers la FND (mintermes) et vers la FNC (maxtermes).</li>
    <li>Convertir une formule arbitraire en FNC ou FND par calcul algébrique pur sans table.</li>
    <li>Reconnaître instantanément la satisfiabilité triviale d'une FND et la validité triviale d'une FNC.</li>
    <li>Comprendre la complétude fonctionnelle d'un jeu de connecteurs et les connecteurs universels NAND et NOR.</li>
  </ul>
</div>

<h2 id="w03-c-fonctions">1. Fonctions Booléennes et Dénombrement</h2>
<div class="box box-definition">
  <div class="box-title">Définition 3.1 — Fonction Booléenne</div>
  <p>Une <strong>fonction booléenne</strong> à $n$ variables est une application :</p>
  $$f : \\{0, 1\\}^n \\longrightarrow \\{0, 1\\}$$
  <p>Puisque le domaine $\\{0, 1\\}^n$ contient exactement $2^n$ n-uplets (lignes de la table de vérité), et que pour chacun de ces n-uplets $f$ peut valoir 0 ou 1, il existe exactement :</p>
  $$2^{2^n} \\quad \\text{fonctions booléennes distinctes à } n \\text{ variables}.$$
</div>

<h2 id="w03-c-fnc-fnd">2. Formes Normales : FNC et FND</h2>
<div class="box box-definition">
  <div class="box-title">Définition 3.2 — Vocabulaire Normalisé</div>
  <ul>
    <li><strong>Littéral :</strong> Une variable propositionnelle $p$ (littéral positif) ou sa négation $\\neg p$ (littéral négatif).</li>
    <li><strong>Clause disjonctive (ou simplement Clause) :</strong> Une disjonction de littéraux : $(l_1 \\lor l_2 \\lor \\dots \\lor l_k)$.</li>
    <li><strong>Terme (ou Clause conjonctive) :</strong> Une conjonction de littéraux : $(l_1 \\land l_2 \\land \\dots \\land l_k)$.</li>
    <li><strong>Forme Normale Conjonctive (FNC / CNF) :</strong> Une conjonction de clauses : $$\\bigwedge_{i=1}^m \\left( \\bigvee_{j=1}^{k_i} l_{i,j} \\right)$$</li>
    <li><strong>Forme Normale Disjonctive (FND / DNF) :</strong> Une disjonction de termes : $$\\bigvee_{i=1}^m \\left( \\bigwedge_{j=1}^{k_i} l_{i,j} \\right)$$</li>
  </ul>
</div>

<h2 id="w03-c-conversion">3. Passage de la Table de Vérité aux Formes Normales</h2>
<div class="box box-method">
  <div class="box-title">Algorithme canonique à partir d'une table de vérité</div>
  <ul>
    <li><strong>Pour construire la FND :</strong> On repère chaque ligne de la table où la formule vaut <strong>1</strong>. Pour chaque telle ligne, on forme un <em>minterme</em> (conjonction où la variable apparaît positive si elle vaut 1, et négative si elle vaut 0). On prend la disjonction ($\lor$) de tous ces mintermes.</li>
    <li><strong>Pour construire la FNC :</strong> On repère chaque ligne où la formule vaut <strong>0</strong>. Pour chaque telle ligne, on forme un <em>maxterme</em> (disjonction où la variable apparaît négative si elle vaut 1, et positive si elle vaut 0). On prend la conjonction ($\land$) de tous ces maxtermes.</li>
  </ul>
</div>

<h2 id="w03-c-completude">4. Complétude Fonctionnelle des Jeux de Connecteurs</h2>
<div class="box box-definition">
  <div class="box-title">Définition 3.3 — Système Complet de Connecteurs</div>
  <p>Un ensemble de connecteurs $\\mathcal{C}$ est dit <strong>complet</strong> si toute fonction booléenne peut être représentée par une formule utilisant uniquement les connecteurs de $\\mathcal{C}$.</p>
  <ul>
    <li>$\\{\neg, \\land, \\lor\\}$ est complet (démontré par la construction de la FND pour toute table).</li>
    <li>$\\{\neg, \\land\\}$ est complet (car $A \\lor B \\equiv \\neg(\\neg A \\land \\neg B)$).</li>
    <li>$\\{\neg, \\lor\\}$ est complet (car $A \\land B \\equiv \\neg(\\neg A \\lor \\neg B)$).</li>
    <li>$\\{\neg, \\Rightarrow\\}$ est complet (car $\\neg A \\lor B \\equiv A \\Rightarrow B$).</li>
    <li><strong>$\\{\land, \\lor\\}$ est INCOMPLET :</strong> toute formule construite uniquement avec $\\land$ et $\\lor$ est <em>monotone croissante</em> ; elle ne peut jamais exprimer la négation $\\neg p$.</li>
    <li><strong>Connecteur universel NAND (barre de Sheffer $|$) :</strong> $\\{|\\}$ est complet à lui seul ! ($p | q \\equiv \\neg(p \\land q)$).</li>
    <li><strong>Connecteur universel NOR (flèche de Peirce $\\downarrow$) :</strong> $\\{\\downarrow\\}$ est complet à lui seul ! ($p \\downarrow q \\equiv \\neg(p \\lor q)$).</li>
  </ul>
</div>
"""

cours_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۳</div>
  <ul>
    <li>درک تابع بولی و فرمول شمارش تعداد آن‌ها ($2^{2^n}$).</li>
    <li>تعریف دقیق لیترال، بند فصلی (Clause)، ترم عطفی، فرم FNC و فرم FND.</li>
    <li>تسلط بر الگوریتم استاندارد استخراج FND (مین‌ترم‌ها) و FNC (مکس‌ترم‌ها) از روی جدول درستی.</li>
    <li>تبدیل مستقیم فرمول به فرم نرمال از طریق قوانین جبر بولی بدون رسم جدول.</li>
    <li>تشخیص سریع و خطی صدق‌پذیری در FND و اعتبار در FNC.</li>
    <li>مفهوم تمامیت مجموعه‌های رابط‌های منطقی و رابط‌های فراگیر نند (NAND) و نور (NOR).</li>
  </ul>
</div>

<h2 id="w03-c-fonctions">۱. توابع بولی و شمارش آن‌ها</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۳.۱ — تابع بولی</div>
  <p>یک <strong>تابع بولی</strong> با $n$ متغیر، نگاشتی است به صورت :</p>
  $$f : \\{0, 1\\}^n \\longrightarrow \\{0, 1\\}$$
  <p>چون دامنه دارای $2^n$ بردار ورودی است، تعداد کل توابع بولی ممکن دقیقاً برابر است با :</p>
  $$2^{2^n} \\quad \\text{تابع بولی متمایز با } n \\text{ متغیر}.$$
</div>

<h2 id="w03-c-fnc-fnd">۲. فرم‌های نرمال: FNC و FND</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۳.۲ — واژگان استاندارد فرم‌های نرمال</div>
  <ul>
    <li><strong>لیترال (Littéral):</strong> یک متغیر گزاره‌ای $p$ یا نقیض آن $\\neg p$.</li>
    <li><strong>بند فصلی (Clause):</strong> فصلی از چند لیترال : $(l_1 \\lor l_2 \\lor \\dots \\lor l_k)$.</li>
    <li><strong>ترم عطفی (Terme):</strong> عطفی از چند لیترال : $(l_1 \\land l_2 \\land \\dots \\land l_k)$.</li>
    <li><strong>فرم نرمال عطفی (FNC / CNF):</strong> عطف چند بند : $$\\bigwedge_{i=1}^m \\left( \\bigvee_{j=1}^{k_i} l_{i,j} \\right)$$</li>
    <li><strong>فرم نرمال فصلی (FND / DNF):</strong> فصل چند ترم : $$\\bigvee_{i=1}^m \\left( \\bigwedge_{j=1}^{k_i} l_{i,j} \\right)$$</li>
  </ul>
</div>

<h2 id="w03-c-conversion">۳. استخراج فرم‌های نرمال از جدول درستی</h2>
<div class="box box-method">
  <div class="box-title">الگوریتم ساخت فرم‌های نرمال از جدول درستی</div>
  <ul>
    <li><strong>برای ساخت FND :</strong> تمام سطرهایی را که خروجی فرمول در آن‌ها <strong>۱</strong> است پیدا کنید. برای هر سطر یک <em>مین‌ترم</em> بنویسید (عطف متغیرها به گونه‌ای که اگر مقدار ۱ دارند خودشان و اگر ۰ دارند نقیضشان باشد). سپس بین تمام مین‌ترم‌ها علامت فصل ($\lor$) بگذارید.</li>
    <li><strong>برای ساخت FNC :</strong> تمام سطرهایی را که خروجی فرمول در آن‌ها <strong>۰</strong> است پیدا کنید. برای هر سطر یک <em>مکس‌ترم</em> بنویسید (فصل متغیرها به گونه‌ای که اگر مقدار ۱ دارند نقیضشان و اگر ۰ دارند خودشان باشد). سپس بین تمام مکس‌ترم‌ها علامت عطف ($\land$) بگذارید.</li>
  </ul>
</div>

<h2 id="w03-c-completude">۴. تمامیت تابعی مجموعه‌های رابط‌های منطقی</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۳.۳ — مجموعه کامل رابط‌ها</div>
  <p>مجموعه‌ای از رابط‌ها را <strong>کامل</strong> می‌نامند هرگاه بتوان هر تابع بولی دلخواهی را تنها با استفاده از رابط‌های آن مجموعه بیان کرد.</p>
  <ul>
    <li>مجموعه $\\{\neg, \\land, \\lor\\}$ کامل است.</li>
    <li>مجموعه‌های دو عنصری $\\{\neg, \\land\\}$ و $\\{\neg, \\lor\\}$ و $\\{\neg, \\Rightarrow\\}$ همگی کاملند.</li>
    <li><strong>مجموعه $\\{\land, \\lor\\}$ ناقص است:</strong> زیرا هر فرمولی که تنها با AND و OR ساخته شود یکنواخت صعودی است و هرگز نمی‌تواند نقیض را تولید کند.</li>
    <li><strong>رابط تک‌عنصری نند (NAND / خط شفر $|$):</strong> به تنهایی یک مجموعه کامل است!</li>
    <li><strong>رابط تک‌عنصری نور (NOR / پیکان پیرس $\\downarrow$):</strong> به تنهایی یک مجموعه کامل است!</li>
  </ul>
</div>
"""

make_bundle("w03_cours", "fr", cours_fr)
make_bundle("w03_cours", "fa", cours_fa)

# ==============================================================================
# WEEK 3: TD (FR & FA) - Exercices 9 à 13 de main_td-etudiants.pdf
# ==============================================================================

td_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de TD 3 — Formes Normales & Fonctions Booléennes</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 7–8, Thème 3, Exercices 9 à 13). Étude complète de l'identification, de la satisfiabilité, du passage table/formes et de la mise sous forme normale algébrique.</p>
</div>

<div id="td-exo9-container"></div>
<div id="td-exo10-container"></div>
<div id="td-exo13-container"></div>
"""

td_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه تمرین‌های کلاسی TD 3 — فرم‌های نرمال و توابع بولی</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۷ و ۸، تم ۳، تمرین‌های ۹ تا ۱۳). حل تشریحی شناسایی FNC/FND، اعتبارسنجی سریع و تبدیل جبری بدون جدول.</p>
</div>

<div id="td-exo9-container"></div>
<div id="td-exo10-container"></div>
<div id="td-exo13-container"></div>
"""

td_interactive = """
  // Exercice 9
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo9-container'), {
    id: 'w03_td_ex9',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۹ — شناسایی فرم‌های نرمال FNC و FND' : 'Exercice 9 – Forme normale : identification',
    source: 'main_td-etudiants.pdf (p. 7)',
    theme: lang === 'fa' ? 'تم ۳' : 'Thème 3',
    statement: lang === 'fa' ?
      '<p>برای هر یک از فرمول‌های زیر مشخص کنید آیا زیر شکل FNC، FND، هر دو، یا هیچ‌کدام است ؟</p>' +
      '<ol>' +
      '<li>$F_1 = p$' +
      '<li>$F_2 = p \\lor \\neg q$' +
      '<li>$F_3 = (p \\land q) \\lor (r \\land (s \\lor t))$' +
      '<li>$F_4 = (p \\lor q) \\land (\\neg p \\lor r) \\land (q \\lor \\neg r)$' +
      '</ol>' :
      '<p>Pour chacune des formules suivantes, déterminer si elle est sous FNC, sous FND, sous les deux, ou sous aucune des deux formes :</p>' +
      '<ol>' +
      '<li>$F_1 = p$' +
      '<li>$F_2 = p \\lor \\neg q$' +
      '<li>$F_3 = (p \\land q) \\lor (r \\land (s \\lor t))$' +
      '<li>$F_4 = (p \\lor q) \\land (\\neg p \\lor r) \\land (q \\lor \\neg r)$' +
      '</ol>',
    consigne: lang === 'fa' ?
      'یک لیترال منفرد می‌تواند به عنوان بند تک‌عضوی (FNC با یک بند و یک لیترال) یا به عنوان ترم تک‌عضوی (FND با یک ترم و یک لیترال) در نظر گرفته شود.' :
      'Rappel de cours : un littéral isolé satisfait à la fois la définition d\\'une clause à 1 littéral (donc FNC) et d\\'un terme à 1 littéral (donc FND).',
    hint: lang === 'fa' ? 
      'دقت کنید که در FNC عملگر بیرونی حتماً باید عطف و عملگر درونی فصل باشد. برای FND برعکس است.' :
      'Vérifiez la profondeur syntaxique : en FNC, la racine est une conjonction de disjonctions de littéraux. En FND, c\\'est une disjonction de conjonctions de littéraux.',
    steps: lang === 'fa' ? [
      '<strong>فرمول F1 ($p$) :</strong> این یک لیترال منفرد است. هم یک بند تک‌عضوی است (FNC با ۱ بند) و هم یک ترم تک‌عضوی (FND با ۱ ترم). بنابراین تحت <strong>هر دو شکل</strong> است.',
      '<strong>فرمول F2 ($p \\lor \\neg q$) :</strong> این یک فصل از دو لیترال است. این یک بند disjonctive منفرد است (FNC با ۱ بند). از طرف دیگر فصلی از دو ترم تک‌لیترالی است (FND با دو ترم $p$ و $\\neg q$). بنابراین تحت <strong>هر دو شکل</strong> است!',
      '<strong>فرمول F3 :</strong> ترم دوم دارای عبارت درونی $(s \\lor t)$ در داخل عطف با $r$ است که این عمق ۳ سطحی در هیچ فرم نرمالی مجاز نیست. بنابراین تحت <strong>هیچ‌کدام</strong> نیست.',
      '<strong>فرمول F4 :</strong> عطف سه پرانتز فصلی از لیترال‌هاست. این فرم دقیقاً تعریف <strong>FNC</strong> است (و FND نیست زیرا در بالاترین سطح عطف است).'
    ] : [
      '<strong>Formule F1 ($p$) :</strong> Littéral unique. C\\'est une conjonction à 1 clause contenant 1 littéral (FNC), et une disjonction à 1 terme contenant 1 littéral (FND). Donc sous <strong>les deux formes</strong>.',
      '<strong>Formule F2 ($p \\lor \\neg q$) :</strong> Disjonction de deux littéraux. C\\'est une FNC (conjonction dégénérée à 1 clause) ET une FND (disjonction de deux termes de 1 littéral). Donc sous <strong>les deux formes</strong>.',
      '<strong>Formule F3 :</strong> Présence d\\'une imbrication $(s \\lor t)$ dans une conjonction sous une disjonction. Profondeur syntaxique invalide. <strong>Aucune des deux</strong>.',
      '<strong>Formule F4 :</strong> Conjonction stricte de trois clauses disjonctives. C\\'est une <strong>FNC pure</strong>.'
    ],
    justification: lang === 'fa' ?
      'تطابق مستقیم با تعاریف صوری اسلاید ۵ جزوه درس ۳.' :
      'Application rigoureuse de la définition inductive des formes normales normales conjonctives et disjonctives.',
    finalAnswer: lang === 'fa' ?
      '۱. $F_1$ : <strong>هر دو (FNC و FND)</strong>.<br>۲. $F_2$ : <strong>هر دو (FNC و FND)</strong>.<br>۳. $F_3$ : <strong>هیچ‌کدام</strong>.<br>۴. $F_4$ : <strong>فقط FNC</strong>.' :
      '1. $F_1$ : <strong>Les deux (FNC et FND)</strong>.<br>2. $F_2$ : <strong>Les deux (FNC et FND)</strong>.<br>3. $F_3$ : <strong>Aucune des deux</strong>.<br>4. $F_4$ : <strong>FNC uniquement</strong>.',
    verification: lang === 'fa' ?
      'بررسی اینکه هیچ عملگری جز عطف و فصل و نقیض وجود نداشته باشد و نقیض‌ها فقط مستقیماً چسبیده به متغیرها باشند.' :
      'Vérifiez qu\\'aucun connecteur $\\neg$ ne porte sur une expression composée, et que la hiérarchie ne dépasse pas deux niveaux d\\'opérateurs binaires.',
    trap: lang === 'fa' ?
      'دام مشهور: تصور اینکه $p \\lor \\neg q$ فقط FNC است یا فقط FND. در آزمون سوربن تأکید می‌شود که یک عبارت فصلی از لیترال‌ها همزمان FNC و FND محسوب می‌شود.' :
      'Le piège d\\'examen est d\\'oublier qu\\'une clause disjonctive est AUSSI une FND de termes unaires.'
  });

  // Exercice 13
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo13-container'), {
    id: 'w03_td_ex13',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱۳ — تبدیل جبری به فرم‌های نرمال بدون جدول' : 'Exercice 13 – Mise en forme normale algébrique sans table',
    source: 'main_td-etudiants.pdf (p. 8)',
    theme: lang === 'fa' ? 'تم ۳' : 'Thème 3',
    statement: lang === 'fa' ?
      '<p>بدون رسم جدول درستی، فرمول زیر را به شکل FNC و سپس FND تبدیل کنید :</p>' +
      '<p>$$F = (p \\Rightarrow q) \\Rightarrow (p \\land r)$$</p>' :
      '<p>Sans construire de table de vérité, mettre sous forme normale conjonctive (FNC) puis sous forme normale disjonctive (FND) la formule :</p>' +
      '<p>$$F = (p \\Rightarrow q) \\Rightarrow (p \\land r)$$</p>',
    consigne: lang === 'fa' ?
      'ابتدا تمام شرطی‌ها را با قانون $A \\Rightarrow B \\equiv \\neg A \\lor B$ حذف کنید. سپس نقیض‌ها را با دمورگان به پشت متغیرها ببرید و با توزیع‌پذیری به فرم نهایی برسید.' :
      'Étape 1 : Éliminer les implications. Étape 2 : Descendre les négations sur les atomes (De Morgan). Étape 3 : Distribuer pour obtenir FNC puis FND.',
    hint: lang === 'fa' ? 
      'برای شرطی اصلی: $\\neg(p \\Rightarrow q) \\lor (p \\land r)$. به یاد داشته باشید که $\\neg(p \\Rightarrow q) \\equiv p \\land \\neg q$.' :
      'Rappel fondamental : la négation d\\'une implication est une conjonction : $\\neg(A \\Rightarrow B) \\equiv A \\land \\neg B$.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (حذف شرطی اصلی) :</strong><br>' +
      '$F \\equiv \\neg(p \\Rightarrow q) \\lor (p \\land r)$.',
      '<strong>گام ۲ (نقیض شرطی داخلی) :</strong><br>' +
      'چون $p \\Rightarrow q \\equiv \\neg p \\lor q$، نقیض آن طبق دمورگان می‌شود :<br>' +
      '$\\neg(\\neg p \\lor q) \\equiv \\neg\\neg p \\land \\neg q \\equiv p \\land \\neg q$.<br>' +
      'بنابراین : $F \\equiv (p \\land \\neg q) \\lor (p \\land r)$.<br>' +
      'این عبارت هم‌اکنون یک <strong>FND کامل</strong> است!',
      '<strong>گام ۳ (تبدیل به FNC از طریق فاکتورگیری و توزیع‌پذیری) :</strong><br>' +
      'از $p$ فاکتور می‌گیریم (توزیع‌پذیری معکوس) :<br>' +
      '$F \\equiv p \\land (\\neg q \\lor r)$.<br>' +
      'این عبارت یک <strong>FNC کامل</strong> است (عطف دو بند $p$ و $\\neg q \\lor r$).'
    ] : [
      '<strong>Étape 1 (Élimination de l\\'implication externe) :</strong><br>' +
      '$F \\equiv \\neg(p \\Rightarrow q) \\lor (p \\land r)$.',
      '<strong>Étape 2 (Négation de l\\'implication interne) :</strong><br>' +
      'Comme $\\neg(A \\Rightarrow B) \\equiv A \\land \\neg B$, on obtient immédiatement :<br>' +
      '$F \\equiv (p \\land \\neg q) \\lor (p \\land r)$.<br>' +
      'Cette expression est déjà une <strong>FND valide</strong> (disjonction de 2 termes).',
      '<strong>Étape 3 (Mise sous FNC par factorisation) :</strong><br>' +
      'On factorise par $p$ grâce à la distributivité :<br>' +
      '$F \\equiv p \\land (\\neg q \\lor r)$.<br>' +
      'Cette formule est sous <strong>FNC valide</strong> (conjonction de la clause unitaire $p$ et de la clause $\\neg q \\lor r$).'
    ],
    justification: lang === 'fa' ?
      'تبدیل‌ها مستقیماً بر مبنای قوانین هم‌ارزی دمورگان و توزیع‌پذیری فصل بر عطف صورت گرفته است.' :
      'Transformations algébriques directes par les lois de De Morgan et la distributivité.',
    finalAnswer: lang === 'fa' ?
      '<strong>فرم FND :</strong> $$(p \\land \\neg q) \\lor (p \\land r)$$<br>' +
      '<strong>فرم FNC :</strong> $$p \\land (\\neg q \\lor r)$$' :
      '<strong>Forme Normale Disjonctive (FND) :</strong> $$(p \\land \\neg q) \\lor (p \\land r)$$<br>' +
      '<strong>Forme Normale Conjonctive (FNC) :</strong> $$p \\land (\\neg q \\lor r)$$',
    verification: lang === 'fa' ?
      'تست ارزش‌گذاری: اگر $p=0$ باشد، F=0 می‌شود. هم در FND و هم در FNC با $p=0$ نتیجه صفر است. اگر $p=1$ و $q=0$ باشد، نتیجه ۱ است که در هر دو فرم هم‌خوان است.' :
      'Test de cohérence : si $p=0$, alors $F \\equiv 0$. Les deux formes obtenues s\\'évaluent bien à 0 lorsque $p=0$.',
    trap: lang === 'fa' ?
      'توزیع اشتباه پرانتزها و از دست دادن یک لیتیرال در فرآیند تبدیل.' :
      'Attention à ne pas oublier de simplifier les parenthèses superflues lors de la distributivité.'
  });
"""

make_bundle("w03_td", "fr", td_fr, td_interactive)
make_bundle("w03_td", "fa", td_fa, td_interactive)

# ==============================================================================
# WEEK 3: TP (FR & FA) - Exercice 5 de main_tp-etudiants.pdf
# ==============================================================================

tp_fr = """
<div class="box box-objectives">
  <div class="box-title">Laboratoire TP 3 — Analyseur Syntaxique Récursif en Python</div>
  <p>Source officielle : <code>main_tp-etudiants.pdf</code> (p. 5–6, Thème 1.2.3, Exercice 5). Implémentation complète de l'analyseur de syntaxe prenant en compte le parenthésage arbitraire, l'équilibrage des parenthèses et la recherche du connecteur principal.</p>
</div>

<h2 id="w03-tp-parser">1. Analyseur Syntaxique Robuste (<code>decompose</code>)</h2>
<pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    # Recherche le premier connecteur à partir de 'index'
    connecteurs = ["IMPLIES", "AND", "OR", "NOT"]
    meilleur_pos = len(formule)
    meilleur_connec = None
    
    for c in connecteurs:
        pos = formule.find(c, index)
        if pos != -1 and pos < meilleur_pos:
            meilleur_pos = pos
            meilleur_connec = c
            
    if meilleur_connec is None:
        return ("", -1)
    return (meilleur_connec, meilleur_pos)

def decompose_simple(formule: str) -> tuple[str, list[str]]:
    formule = formule.strip()
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])
    for c in ["IMPLIES", "AND", "OR"]:
        parts = formule.split(f" {c} ", 1)
        if len(parts) == 2:
            return (c, [parts[0].strip(), parts[1].strip()])
    # C'est un atome ou une constante
    return (formule, [])

def decompose(formule: str) -> tuple[str, list[str]]:
    formule = formule.strip()
    
    # Vérification de l'équilibre des parenthèses
    if formule.count("(") != formule.count(")"):
        return None
        
    # Élimination des parenthèses superflues englobantes
    while formule.startswith("(") and formule.endswith(")"):
        # Vérifier si la parenthèse fermante correspond bien à la première ouvrante
        profondeur = 0
        englobante = True
        for i in range(len(formule) - 1):
            if formule[i] == "(":
                profondeur += 1
            elif formule[i] == ")":
                profondeur -= 1
            if profondeur == 0:
                englobante = False
                break
        if englobante:
            formule = formule[1:-1].strip()
        else:
            break
            
    # Recherche du connecteur principal à profondeur 0
    profondeur = 0
    for i, ch in enumerate(formule):
        if ch == "(":
            profondeur += 1
        elif ch == ")":
            profondeur -= 1
        elif profondeur == 0:
            for c in ["IMPLIES", "AND", "OR"]:
                if formule.startswith(f" {c} ", i):
                    gauche = formule[:i].strip()
                    droite = formule[i + len(c) + 2:].strip()
                    return (c, [gauche, droite])
                    
    if formule.startswith("NOT ") and profondeur == 0:
        return ("NOT", [formule[4:].strip()])
        
    return decompose_simple(formule)</code></pre>
"""

tp_fa = """
<div class="box box-objectives">
  <div class="box-title">آزمایشگاه برنامه‌نویسی TP 3 — پارسر و تحلیل‌گر نحوی بازگشتی در پایتون</div>
  <p>منبع رسمی: جزوه <code>main_tp-etudiants.pdf</code> (صفحه ۵ و ۶، تم ۱.۲.۳، تمرین ۵). پیاده‌سازی کامل و قدرتمند تابع تجزیه نحوی <code>decompose</code> با بررسی تعادل پرانتزها، حذف پرانتزهای زائد بیرونی و تشخیص رابط اصلی در عمق صفر.</p>
</div>

<h2 id="w03-tp-parser">۱. کد کامل پارسر ساختاریافته (<code>decompose</code>)</h2>
<pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    # جستجوی اولین رابط منطقی از اندیس مشخص‌شده
    connecteurs = ["IMPLIES", "AND", "OR", "NOT"]
    meilleur_pos = len(formule)
    meilleur_connec = None
    
    for c in connecteurs:
        pos = formule.find(c, index)
        if pos != -1 and pos < meilleur_pos:
            meilleur_pos = pos
            meilleur_connec = c
            
    if meilleur_connec is None:
        return ("", -1)
    return (meilleur_connec, meilleur_pos)

def decompose_simple(formule: str) -> tuple[str, list[str]]:
    formule = formule.strip()
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])
    for c in ["IMPLIES", "AND", "OR"]:
        parts = formule.split(f" {c} ", 1)
        if len(parts) == 2:
            return (c, [parts[0].strip(), parts[1].strip()])
    # اتم یا ثابت است
    return (formule, [])

def decompose(formule: str) -> tuple[str, list[str]]:
    formule = formule.strip()
    
    # بررسی تطابق تعداد پرانتزهای باز و بسته
    if formule.count("(") != formule.count(")"):
        return None
        
    # حذف پرانتزهای احاطه‌کننده بیرونی
    while formule.startswith("(") and formule.endswith(")"):
        profondeur = 0
        englobante = True
        for i in range(len(formule) - 1):
            if formule[i] == "(":
                profondeur += 1
            elif formule[i] == ")":
                profondeur -= 1
            if profondeur == 0:
                englobante = False
                break
        if englobante:
            formule = formule[1:-1].strip()
        else:
            break
            
    # جستجوی رابط اصلی در عمق صفر (بیرون از هر پرانتز)
    profondeur = 0
    for i, ch in enumerate(formule):
        if ch == "(":
            profondeur += 1
        elif ch == ")":
            profondeur -= 1
        elif profondeur == 0:
            for c in ["IMPLIES", "AND", "OR"]:
                if formule.startswith(f" {c} ", i):
                    gauche = formule[:i].strip()
                    droite = formule[i + len(c) + 2:].strip()
                    return (c, [gauche, droite])
                    
    if formule.startswith("NOT ") and profondeur == 0:
        return ("NOT", [formule[4:].strip()])
        
    return decompose_simple(formule)</code></pre>
"""

make_bundle("w03_tp", "fr", tp_fr)
make_bundle("w03_tp", "fa", tp_fa)

# ==============================================================================
# WEEK 3: ANNALES & REVISION (FR & FA)
# ==============================================================================

annales_w3_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales d'Examens Ciblées — Semaine 3</div>
  <p>Exercices d'examens sur la complétude des jeux de connecteurs et les critères de validité des formes normales.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">Examen Partiel 2021–2022 — Exercice 2 (Complétude et NAND)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">Source : partiel_2021_2022_S2.pdf (p. 2)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">Semaine 3</span><span class="badge">Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>On note $|$ le connecteur binaire NAND (barre de Sheffer), défini par $p | q \\equiv \\neg(p \\land q)$.</p>
    <p>1. Exprimer la négation $\\neg p$ en utilisant uniquement le connecteur $|$.<br>
    2. Exprimer la conjonction $p \\land q$ en utilisant uniquement le connecteur $|$.<br>
    3. Exprimer la disjonction $p \\lor q$ en utilisant uniquement le connecteur $|$.<br>
    4. En déduire que le jeu de connecteurs $\\{|\\}$ est fonctionnellement complet.</p>
  </div>
  <div class="step-content">
    <strong>Correction officielle Sorbonne :</strong><br>
    1. <strong>Négation :</strong> Par idempotence de la conjonction ($p \\land p \\equiv p$), on a :<br>
    $$\\neg p \\equiv p \\mid p$$<br>
    2. <strong>Conjonction :</strong> On nie le NAND : $p \\land q \\equiv \\neg(p | q) \\equiv (p | q) | (p | q)$.<br>
    3. <strong>Disjonction :</strong> Par De Morgan, $p \\lor q \\equiv \\neg(\\neg p \\land \\neg q) \\equiv \\neg p | \\neg q \\equiv (p | p) | (q | q)$.<br>
    4. <strong>Complétude :</strong> Puisque $\\{\\neg, \\land\\}$ est un jeu complet de connecteurs et que chaque connecteur de ce jeu s'exprime avec $|$, le jeu $\\{|\\}$ est fonctionnellement complet.
  </div>
</div>
"""

annales_w3_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات آزمون‌های نهایی سوربن — هفته ۳</div>
  <p>سؤالات آزمون دانشگاه در زمینه اثبات تمامیت عملگر نند (NAND / Sheffer) و بازنویسی عملگرها.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">امتحان میان‌ترم ۲۰۲۱–۲۰۲۲ — تمرین ۲ (تمامیت شفر و NAND)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">منبع رسمی: partiel_2021_2022_S2.pdf (صفحه ۲)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">هفته ۳</span><span class="badge">امتحان Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>عملگر دوتایی خط شفر یا NAND را با نماد $|$ نشان می‌دهیم که طبق تعریف $p | q \\equiv \\neg(p \\land q)$ است.</p>
    <p>۱. نقیض $\\neg p$ را تنها با استفاده از $|$ بنویسید.<br>
    ۲. عطف $p \\land q$ را تنها با استفاده از $|$ بیان کنید.<br>
    ۳. فصل $p \\lor q$ را تنها با استفاده از $|$ بیان کنید.<br>
    ۴. نتیجه بگیرید که مجموعه تک‌عضوی $\\{|\\}$ یک سیستم کامل تابعی است.</p>
  </div>
  <div class="step-content">
    <strong>پاسخ تشریحی دانشگاه سوربن :</strong><br>
    ۱. <strong>نقیض :</strong> طبق ویژگی یکسان‌توانی ($p \\land p \\equiv p$)، داریم :<br>
    $$\\neg p \\equiv p \\mid p$$<br>
    ۲. <strong>عطف :</strong> با نفی کردن نند : $p \\land q \\equiv \\neg(p | q) \\equiv (p | q) | (p | q)$.<br>
    ۳. <strong>فصل :</strong> با قانون دمورگان : $p \\lor q \\equiv \\neg(\\neg p \\land \\neg q) \\equiv \\neg p | \\neg q \\equiv (p | p) | (q | q)$.<br>
    ۴. <strong>اثبات تمامیت :</strong> چون می‌دانیم مجموعه $\\{\\neg, \\land\\}$ کامل است و نشان دادیم هر دو عملگر نقیض و عطف تنها با رابط $|$ قابل ساخت هستند، پس مجموعه تک‌عضوی $\\{|\\}$ به تنهایی کامل است.
  </div>
</div>
"""

make_bundle("w03_annales", "fr", annales_w3_fr)
make_bundle("w03_annales", "fa", annales_w3_fa)

revision_w3_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Révision Express — Semaine 3</div>
  <p>Critères décidables linéaires pour les formes normales.</p>
</div>

<h2 id="w03-rev-criteres">Critères de décision immédiate</h2>
<ul>
  <li><strong>Validité d'une FNC :</strong> Une FNC est une tautologie si et seulement si <em>chacune</em> de ses clauses contient au moins une variable et sa négation ($p \\lor \\neg p$).</li>
  <li><strong>Satisfiabilité d'une FND :</strong> Une FND est satisfiable si et seulement si <em>au moins un</em> de ses termes ne contient aucun couple contradictoire ($p \\land \\neg p$).</li>
</ul>
"""

revision_w3_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه جمع‌بندی سریع — هفته ۳</div>
  <p>معیارهای سریع و خطی برای تصمیم‌گیری وضعیت فرم‌های نرمال.</p>
</div>

<h2 id="w03-rev-criteres">معیارهای تصمیم‌گیری چشمی</h2>
<ul>
  <li><strong>اعتبار فرم FNC :</strong> یک FNC معتبر (تاتولوژی) است اگر و تنها اگر در <em>تک‌تک بندهای آن</em> حداقل یک جفت لیترال متناقض ($p \\lor \\neg p$) وجود داشته باشد.</li>
  <li><strong>صدق‌پذیری فرم FND :</strong> یک FND صدق‌پذیر است اگر و تنها اگر <em>حداقل یکی از ترم‌های آن</em> تناقض نداشته باشد (فاقد $p \\land \\neg p$ باشد).</li>
</ul>
"""

make_bundle("w03_revision", "fr", revision_w3_fr)
make_bundle("w03_revision", "fa", revision_w3_fa)

print("Week 3 generation complete!")

