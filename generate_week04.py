import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 4: COURS (FR & FA) - SAT, DPLL & Solveur Glucose
# ==============================================================================

cours_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 4</div>
  <ul>
    <li>Comprendre la formulation clausale du problème SAT et le rôle de la clause vide $\\Box$.</li>
    <li>Maîtriser la règle de <strong>propagation unitaire (UP)</strong> et savoir simplifier rigoureusement un ensemble de clauses.</li>
    <li>Appliquer la règle du <strong>littéral pur (PL)</strong> et comprendre sa justification sémantique.</li>
    <li>Exécuter l'algorithme <strong>DPLL</strong> en construisant son arbre de recherche complet avec retours sur trace (backtracking).</li>
    <li>Calculer rigoureusement l'<strong>heuristique $h_k$</strong> de sélection de variables et respecter l'ordre d'exploration (faux en premier).</li>
    <li>Modéliser des contraintes du monde réel (ex: garnitures de pizzas) en clauses propositionnelles au format <strong>DIMACS</strong>.</li>
  </ul>
</div>

<h2 id="w04-c-sat">1. Le Problème SAT et la Forme Clausale</h2>
<p>
Le problème <strong>SAT (Satisfiabilité Booléenne)</strong> consiste à déterminer s'il existe une valuation satisfaisant simultanément un ensemble de clauses. C'est le premier problème historiquement prouvé <strong>NP-complet</strong> (théorème de Cook-Levin, 1971).
</p>

<div class="box box-definition">
  <div class="box-title">Définition 4.1 — Théorie Clausale et Clause Vide</div>
  <p>Une formule en FNC est représentée comme un <strong>ensemble fini de clauses</strong> $\\Sigma = \\{C_1, C_2, \\dots, C_m\\}$, où chaque clause $C_i$ est un ensemble fini de littéraux :</p>
  $$C_i = \\{l_{i,1}, l_{i,2}, \\dots, l_{i,k}\\} \\quad \\text{représentant} \\quad l_{i,1} \\lor l_{i,2} \\lor \\dots \\lor l_{i,k}$$
  <ul>
    <li>Une clause est satisfaite par une valuation $v$ si <em>au moins un</em> de ses littéraux vaut 1 sous $v$.</li>
    <li>L'ensemble $\\Sigma$ est satisfait si <em>toutes</em> ses clauses sont satisfaites simultanément.</li>
    <li><strong>La clause vide $\\Box$ (notée $\\{\\}$) :</strong> C'est une disjonction sans aucun littéral. Par définition, elle est <strong>toujours fausse</strong> (neutre pour $\\lor$). Si un ensemble de clauses contient $\\Box$, il est immédiatement <strong>insatisfiable</strong>.</li>
    <li><strong>L'ensemble vide $\\emptyset$ :</strong> C'est une conjonction de zéro clause. Il est <strong>toujours vrai</strong> (neutre pour $\\land$). S'il ne reste plus aucune clause à satisfaire, la formule est <strong>satisfiable</strong> !</li>
  </ul>
</div>

<h2 id="w04-c-regles">2. Les Règles de Réduction Fondamentales de DPLL</h2>

<div class="box box-definition">
  <div class="box-title">Règle 1 — Règle de la Clause Unitaire & Propagation Unitaire (UP)</div>
  <p>Si $\\Sigma$ contient une clause unitaire $C = \\{l\\}$ (réduite à un seul littéral $l$) :</p>
  <p>Pour que $\\Sigma$ soit satisfiable, il est <strong>obligatoire</strong> que $l$ soit vrai (affectation $v(l) = 1$). On applique alors la simplification suivante à $\\Sigma$ :</p>
  <ol>
    <li>On supprime toutes les clauses contenant le littéral $l$ (car elles sont déjà satisfaites).</li>
    <li>On supprime le littéral complémentaire $\\neg l$ de toutes les autres clauses (car $\\neg l = 0$, donc il ne peut pas aider à satisfaire ces clauses).</li>
  </ol>
  <p>Cette simplification est répétée en cascade jusqu'à ce qu'il n'y ait plus aucune clause unitaire : c'est la <strong>propagation unitaire</strong>.</p>
</div>

<div class="box box-definition">
  <div class="box-title">Règle 2 — Règle du Littéral Pur (PL)</div>
  <p>Un littéral $l$ est dit <strong>pur</strong> dans $\\Sigma$ s'il apparaît dans au moins une clause, mais que son complément $\\neg l$ n'apparaît dans <em>aucune</em> clause de $\\Sigma$.</p>
  <p><strong>Justification sémantique :</strong> Poser $l = 1$ satisfait immédiatement toutes les clauses contenant $l$, sans risquer de falsifier aucune autre clause puisque $\\neg l$ n'existe nulle part ! On peut donc éliminer toutes les clauses contenant $l$.</p>
</div>

<h2 id="w04-c-dpll">3. L'Algorithme DPLL Classique</h2>
<div class="box box-algorithm">
  <div class="box-title">Algorithme DPLL(Σ)</div>
  <ol>
    <li><strong>Propagation unitaire :</strong> Tant que $\\Sigma$ contient une clause unitaire $\\{l\\}$, simplifier $\\Sigma$ par $l \\leftarrow 1$.</li>
    <li><strong>Test de terminaison immédiat :</strong>
      <ul>
        <li>Si $\\Box \\in \\Sigma$ (clause vide générée) : <strong>Conflit ! Renvoyer UNSAT</strong> (retour arrière).</li>
        <li>Si $\\Sigma = \\emptyset$ (toutes les clauses éliminées) : <strong>Succès ! Renvoyer SAT</strong> (modèle trouvé).</li>
      </ul>
    </li>
    <li><strong>Élimination des littéraux purs :</strong> Pour tout littéral pur $l$, affecter $l \\leftarrow 1$ et supprimer les clauses le contenant.</li>
    <li><strong>Branchement heuristique :</strong> Choisir une variable non encore affectée $p$ selon une heuristique (ex: $h_k$).
      <ul>
        <li>Explorer la première branche : $DPLL(\\Sigma \\cup \\{\\neg p\\})$ (branche <strong>Faux</strong> en premier).</li>
        <li>Si cette branche renvoie SAT, terminer avec succès.</li>
        <li>Sinon (retour arrière / backtracking), explorer la seconde branche : $DPLL(\\Sigma \\cup \\{p\\})$ (branche <strong>Vrai</strong>).</li>
      </ul>
    </li>
  </ol>
</div>

<h2 id="w04-c-hk">4. L'Heuristique $h_k$ (Sorbonne)</h2>
<p>
Lorsqu'aucune clause unitaire ni littéral pur n'est disponible, le choix de la variable de branchement est crucial. À la Sorbonne, le cours utilise l'heuristique $h_k$ :
</p>

<div class="box box-definition">
  <div class="box-title">Définition 4.2 — Heuristique $h_k(p)$</div>
  <p>Pour $k \\ge 2$ (taille de clause) et $p$ une variable propositionnelle :</p>
  $$h_k(p) = \\text{nbocc}(k, \\Sigma, p) + \\text{nbocc}(k, \\Sigma, \\neg p)$$
  <p>où $\\text{nbocc}(k, \\Sigma, l)$ est le nombre d'occurrences du littéral $l$ dans les clauses de taille $k$.</p>
  <p><strong>Règle de sélection :</strong></p>
  <ol>
    <li>On sélectionne la variable qui maximise $h_2(p)$ (les clauses de taille 2 sont les plus faciles à transformer en clauses unitaires !).</li>
    <li>En cas d'égalité, on départage avec $h_3(p)$, puis $h_4(p)$, etc.</li>
    <li>Si l'égalité persiste, on départage par <strong>ordre alphabétique</strong> du nom de la variable.</li>
    <li><strong>Convention de branchement :</strong> On teste toujours la branche <strong>$p = 0$ (Faux) en premier</strong> !</li>
  </ol>
</div>

<h2 id="w04-c-dimacs">5. Format Standard DIMACS et Solveur Glucose</h2>
<p>
Les solveurs SAT industriels (comme <strong>Glucose</strong>) utilisent le format de fichier texte normalisé <strong>DIMACS</strong> :
</p>
<pre><code>c Fichier DIMACS exemple
p cnf 3 4
1 2 0
-1 3 0
-2 -3 0
1 -3 0</code></pre>
<ul>
  <li>Les lignes commençant par <code>c</code> sont des commentaires.</li>
  <li>La ligne d'en-tête est <code>p cnf n m</code> où $n$ est le nombre de variables et $m$ le nombre de clauses.</li>
  <li>Chaque clause est écrite sur une ligne, séparée par des espaces et <strong>terminée par un 0</strong>.</li>
  <li>La variable $x_i$ est codée par l'entier $i$ ; sa négation $\\neg x_i$ par l'entier négatif $-i$.</li>
</ul>
"""

cours_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۴</div>
  <ul>
    <li>درک فرم بندی مسئله SAT و نقش حیاتی بند تهی $\\Box$ در اثبات تناقض.</li>
    <li>تسلط کامل بر قاعده <strong>انتشار تک‌عضوی (Unit Propagation)</strong> و ساده‌سازی دقیق بندها.</li>
    <li>به‌کارگیری قاعده <strong>لیترال خالص (Pure Literal)</strong> و توجیه معنایی آن.</li>
    <li>اجرای گام‌به‌گام الگوریتم <strong>DPLL</strong> و رسم درخت جستجو با بازگشت به عقب (Backtracking).</li>
    <li>محاسبه دقیق <strong>هیوریستیک $h_k$</strong> برای انتخاب متغیر انشعاب و رعایت شرط انشعاب ابتدا نادرست.</li>
    <li>مدل‌سازی قیود واقعی در قالب بندهای گزاره‌ای با فرمت استاندارد <strong>DIMACS</strong> و حل با حل‌کننده گلوکز.</li>
  </ul>
</div>

<h2 id="w04-c-sat">۱. مسئله SAT و نمایش فرم بندی</h2>
<p>
مسئله <strong>SAT (Satisfiabilité Booléenne)</strong> تعیین صدق‌پذیری مجموعه‌ای از بندها است. این مسئله نخستین مسئله تاریخ است که کامل‌بودن آن برای کلاس NP به اثبات رسید (قضیه کوک-لوین، ۱۹۷۱).
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۴.۱ — تئوری بندی و بند تهی</div>
  <p>یک فرمول FNC به شکل مجموعه‌ای از بندها نمایش داده می‌شود: $\\Sigma = \\{C_1, C_2, \\dots, C_m\\}$.</p>
  <ul>
    <li>یک بند زمانی ارضا می‌شود که <em>حداقل یکی</em> از لیترال‌های آن ارزش ۱ بگیرد.</li>
    <li>مجموعه $\\Sigma$ زمانی ارضا می‌شود که <em>تمامی</em> بندهای آن به طور هم‌زمان ارضا شوند.</li>
    <li><strong>بند تهی $\\Box$ (یا $\\{\\}$):</strong> بندی است که هیچ لیترالی ندارد. طبق تعریف فصلی، این بند <strong>همواره نادرست (تناقض)</strong> است. اگر در حین ساده‌سازی بند تهی تولید شود، آن شاخه بلافاصله <strong>ناپذیرفتنی (UNSAT)</strong> اعلام شده و پس‌گرد انجام می‌شود.</li>
    <li><strong>مجموعه تهی $\\emptyset$:</strong> مجموعه‌ای از صفر بند است. طبق تعریف عطفی، این مجموعه <strong>همواره درست</strong> است. اگر تمامی بندها حذف شوند، به معنای رسیدن به پاسخ <strong>SAT (صدق‌پذیر)</strong> است!</li>
  </ul>
</div>

<h2 id="w04-c-regles">۲. دو قاعده اساسی کاهش در الگوریتم DPLL</h2>

<div class="box box-definition">
  <div class="box-title">قاعده ۱ — قاعده بند تک‌عضوی و انتشار تک‌عضوی (UP)</div>
  <p>اگر در $\\Sigma$ بندی تک‌عضوی مانند $\\{l\\}$ وجود داشته باشد:</p>
  <p>برای اینکه فرمول درست شود، چاره‌ای جز قرار دادن $l = 1$ نیست. با این تخصیص، تغییرات زیر در $\\Sigma$ اعمال می‌شود:</p>
  <ol>
    <li>تمامی بندهایی که حاوی $l$ هستند به طور کامل حذف می‌شوند (چون قبلاً ارضا شده‌اند).</li>
    <li>لیترال معکوس $\\neg l$ از تمام بندهای دیگر حذف می‌شود (چون مقدار آن صفر شده و کمکی به ارضای آن بندها نمی‌کند).</li>
  </ol>
  <p>این فرآیند به صورت آبشاری تکرار می‌شود تا هیچ بند تک‌عضوی دیگری باقی نماند.</p>
</div>

<div class="box box-definition">
  <div class="box-title">قاعده ۲ — قاعده لیترال خالص (Pure Literal)</div>
  <p>یک لیترال $l$ را <strong>خالص</strong> می‌نامند هرگاه در کل مجموعه بندها ظاهر شده باشد اما نقیض آن $\\neg l$ در هیچ بندی وجود نداشته باشد.</p>
  <p><strong>توجیه معنایی:</strong> با قرار دادن $l = 1$، تمام بندهای حاوی آن ارضا می‌شوند، بدون اینکه هیچ خطر یا اثر منفی برای سایر بندها ایجاد شود (چون $\\neg l$ وجود ندارد). بنابراین تمامی بندهای حاوی $l$ حذف می‌شوند.</p>
</div>

<h2 id="w04-c-hk">۳. هیوریستیک انتخاب متغیر $h_k$ در دانشگاه سوربن</h2>
<p>
هنگامی که هیچ بند تک‌عضوی یا لیترال خالصی نباشد، باید روی یک متغیر انشعاب بزنیم. فرمول هیوریستیک سوربن عبارت است از:
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۴.۲ — فرمول هیوریستیک $h_k(p)$</div>
  <p>برای طول بند $k \\ge 2$ و متغیر $p$:</p>
  $$h_k(p) = \\text{nbocc}(k, \\Sigma, p) + \\text{nbocc}(k, \\Sigma, \\neg p)$$
  <p>که در آن $\\text{nbocc}$ تعداد دفعات تکرار لیترال در بندهای به طول $k$ است.</p>
  <p><strong>الگوریتم اولویت انتخاب:</strong></p>
  <ol>
    <li>متغیری را انتخاب می‌کنیم که $h_2(p)$ آن بیشترین باشد (بندهای دوتایی سریع‌تر به بند تک‌عضوی تبدیل می‌شوند).</li>
    <li>اگر مساوی شدند، با $h_3(p)$ و سپس $h_4(p)$ مقایسه می‌کنیم.</li>
    <li>اگر باز هم مساوی بودند، به <strong>ترتیب الفبایی</strong> نام متغیرها انتخاب می‌کنیم.</li>
    <li><strong>قرارداد انشعاب:</strong> همواره ابتدا شاخه <strong>$p = 0$ (نادرست)</strong> را بررسی می‌کنیم!</li>
  </ol>
</div>
"""

make_bundle("w04_cours", "fr", cours_fr)
make_bundle("w04_cours", "fa", cours_fa)

# ==============================================================================
# WEEK 4: TD (FR & FA) - Exercices 14, 15, 16 de main_td-etudiants.pdf
# ==============================================================================

td_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de TD 4 — Propagation Unitaire, DPLL & Modélisation Pizza</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 9–10, Thème 4, Exercices 14, 15 et 16). Exécution pas à pas avec affichage rigoureux de la théorie clausale $\\Sigma$ après chaque opération.</p>
</div>

<div id="td-exo14-container"></div>
<div id="td-exo15-container"></div>
<div id="td-exo16-container"></div>
"""

td_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه تمرین‌های کلاسی TD 4 — انتشار تک‌عضوی، الگوریتم DPLL و مدل‌سازی پیتزا</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۹ و ۱۰، تم ۴، تمرین‌های ۱۴، ۱۵ و ۱۶). حل خط‌به‌خط ردگیری مجموعه بندها پس از هر مرحله انتشار و انشعاب.</p>
</div>

<div id="td-exo14-container"></div>
<div id="td-exo15-container"></div>
<div id="td-exo16-container"></div>
"""

td_interactive = """
  // Exercice 14
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo14-container'), {
    id: 'w04_td_ex14',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱۴ — انتشار تک‌عضوی (Unit Propagation)' : 'Exercice 14 – Propagation unitaire',
    source: 'main_td-etudiants.pdf (p. 9)',
    theme: lang === 'fa' ? 'تم ۴' : 'Thème 4',
    statement: lang === 'fa' ?
      '<p>مجموعه بندهای زیر را در نظر بگیرید :</p>' +
      '$$C_1 = a \\lor b, \\quad C_2 = \\neg a \\lor b \\lor c, \\quad C_3 = b \\lor \\neg c \\lor d, \\quad C_4 = \\neg b \\lor \\neg e, \\quad C_5 = e \\lor d, \\quad C_6 = \\neg d$$' +
      '<p><strong>سؤال ۱ :</strong> انتشار تک‌عضوی را بر روی $F = C_1 \\land C_2 \\land C_3 \\land C_4 \\land C_5 \\land C_6$ اعمال کنید. چه چیزی به دست می‌آید ؟ چه نتیجه‌ای می‌گیرید ؟</p>' +
      '<p><strong>سؤال ۲ :</strong> فرض کنید $D_3 = \\neg b \\lor \\neg c \\lor d$. انتشار تک‌عضوی را روی $F_2$ که با جایگزینی $C_3$ با $D_3$ ساخته شده اعمال کنید. چه نتیجه‌ای می‌گیرید ؟</p>' :
      '<p>On considère l\\'ensemble de clauses suivant :</p>' +
      '$$C_1 = a \\lor b, \\quad C_2 = \\neg a \\lor b \\lor c, \\quad C_3 = b \\lor \\neg c \\lor d, \\quad C_4 = \\neg b \\lor \\neg e, \\quad C_5 = e \\lor d, \\quad C_6 = \\neg d$$' +
      '<p><strong>Question 1 :</strong> Appliquer la propagation unitaire à $F = C_1 \\land \\dots \\land C_6$. Qu\\'obtient-on ? Que peut-on en déduire ?</p>' +
      '<p><strong>Question 2 :</strong> On pose $D_3 = \\neg b \\lor \\neg c \\lor d$. Appliquer la propagation unitaire à $F_2$ (en remplaçant $C_3$ par $D_3$). Que peut-on en déduire ?</p>',
    consigne: lang === 'fa' ?
      'تنها بند تک‌عضوی اولیه C6 = ¬d است. مقدار d را صفر کنید، بندها را ساده کنید و اگر بند تک‌عضوی جدیدی تولید شد ادامه دهید.' :
      'Repérez la clause unitaire $C_6 = \\neg d$. Affectez $d \\leftarrow 0$ et propagez. Affichez l\\'ensemble résiduel à chaque étape.',
    hint: lang === 'fa' ? 
      'وقتی d=0 شد، در بند C5 داریم e یا d، پس e تک‌عضوی می‌شود!' :
      'En propageant $\\neg d$, la clause $C_5 = e \\lor d$ devient la clause unitaire $\\{e\\}$.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (انتشار ¬d) :</strong><br>' +
      'بند تک‌عضوی $C_6 = \\{\\neg d\\} \\implies d \\leftarrow 0$.<br>' +
      'حذف $C_6$. در $C_3$ و $C_5$ لیترال $d$ حذف می‌شود.<br>' +
      'مجموعه بندها به روز می‌شود :<br>' +
      '$C_1 = a \\lor b, \\quad C_2 = \\neg a \\lor b \\lor c, \\quad C_3^{(1)} = b \\lor \\neg c, \\quad C_4 = \\neg b \\lor \\neg e, \\quad C_5^{(1)} = \\{e\\}$.',
      '<strong>گام ۲ (انتشار e) :</strong><br>' +
      'بند تک‌عضوی $C_5^{(1)} = \\{e\\} \\implies e \\leftarrow 1$.<br>' +
      'حذف $C_5^{(1)}$. در $C_4$ لیترال $\\neg e$ (که مقدارش صفر شده) حذف می‌شود.<br>' +
      'بند $C_4$ تبدیل به بند تک‌عضوی جدید می‌شود : $C_4^{(1)} = \\{\\neg b\\}$.',
      '<strong>گام ۳ (انتشار ¬b) :</strong><br>' +
      'بند تک‌عضوی $C_4^{(1)} = \\{\\neg b\\} \\implies b \\leftarrow 0$.<br>' +
      'حذف $C_4^{(1)}$. در سایر بندها لیترال $b$ حذف می‌شود :<br>' +
      '$C_1$ تبدیل می‌شود به : $\\{a\\}$ (تک‌عضوی جدید !)<br>' +
      '$C_2$ تبدیل می‌شود به : $\\{\\neg a \\lor c\\}$<br>' +
      '$C_3^{(1)}$ تبدیل می‌شود به : $\\{\\neg c\\}$ (تک‌عضوی جدید !)',
      '<strong>گام ۴ (انتشار a و ¬c) :</strong><br>' +
      'از $C_1^{(1)}$ داریم $a \\leftarrow 1$. در $C_2$ لیترال $\\neg a$ حذف شده و $C_2$ تبدیل به $\\{c\\}$ می‌شود.<br>' +
      'اما همزمان از $C_3^{(1)}$ داشتیم $c \\leftarrow 0$ (یعنی $\\{\\neg c\\}$).<br>' +
      'انتشار $c \\leftarrow 0$ بر روی بند $\\{c\\}$ منجر به ایجاد <strong>بند تهی $\\Box$</strong> می‌شود !'
    ] : [
      '<strong>Étape 1 (Propagation de $\\neg d$) :</strong><br>' +
      'Clause unitaire $C_6 = \\{\\neg d\\} \\implies d \\leftarrow 0$.<br>' +
      'On supprime $C_6$ et on retire $d$ de $C_3$ et $C_5$.<br>' +
      '$\\Sigma_1 = \\{a \\lor b, \\neg a \\lor b \\lor c, b \\lor \\neg c, \\neg b \\lor \\neg e, \\{e\\}\\}$.',
      '<strong>Étape 2 (Propagation de $e$) :</strong><br>' +
      'Clause unitaire $\\{e\\} \\implies e \\leftarrow 1$.<br>' +
      'On supprime la clause et on retire $\\neg e$ de $C_4$.<br>' +
      '$\\Sigma_2 = \\{a \\lor b, \\neg a \\lor b \\lor c, b \\lor \\neg c, \\{\\neg b\\}\\}$.',
      '<strong>Étape 3 (Propagation de $\\neg b$) :</strong><br>' +
      'Clause unitaire $\\{\\neg b\\} \\implies b \\leftarrow 0$.<br>' +
      'On retire $b$ des clauses restantes :<br>' +
      '$\\Sigma_3 = \\{\\{a\\}, \\neg a \\lor c, \\{\\neg c\\}\\}$.',
      '<strong>Étape 4 (Propagation de $a$ et contradiction) :</strong><br>' +
      'Clause unitaire $\\{a\\} \\implies a \\leftarrow 1$. La clause $\\neg a \\lor c$ devient $\\{c\\}$.<br>' +
      'On a maintenant simultanément les clauses unitaires $\\{c\\}$ et $\\{\\neg c\\}$.<br>' +
      'La propagation de $\\neg c$ dans $\\{c\\}$ produit la <strong>clause vide $\\Box$</strong>.'
    ],
    justification: lang === 'fa' ?
      'تولید بند تهی به صورت صوری و ریاضی ثابت می‌کند که این مجموعه بندها ناپذیرفتنی (Insatisfiable) است.' :
      'La dérivation de la clause vide $\\Box$ par propagation unitaire pure prouve formellement que l\\'ensemble de clauses est insatisfiable.',
    finalAnswer: lang === 'fa' ?
      '<strong>سؤال ۱ :</strong> انتشار تک‌عضوی به بند تهی $\\Box$ ختم می‌شود. نتیجه می‌گیریم فرمول $F$ <strong>ناپذیرفتنی (Insatisfiable)</strong> است.<br>' +
      '<strong>سؤال ۲ :</strong> برای $F_2$ با تغییر $C_3$ به $D_3 = \\neg b \\lor \\neg c \\lor d$، بند $D_3$ پس از $b=0$ ارضا می‌شود و بند متناقضی ایجاد نمی‌شود. یک مدل کامل به دست می‌آید : $a=1, b=0, c=1, d=0, e=1$. بنابراین $F_2$ <strong>صدق‌پذیر (SAT)</strong> است.' :
      '<strong>Question 1 :</strong> On obtient la clause vide $\\Box$. On en déduit que la théorie $F$ est <strong>insatisfiable (UNSAT)</strong>.<br>' +
      '<strong>Question 2 :</strong> Pour $F_2$, après propagation de $d=0, e=1, b=0$, la clause $D_3$ est satisfaite par $\\neg b$. On propage $a=1$, ce qui donne $c=1$. Modèle obtenu : $a=1, b=0, c=1, d=0, e=1$. La théorie $F_2$ est <strong>satisfiable (SAT)</strong>.',
    verification: lang === 'fa' ?
      'بررسی درستی مدل سوال ۲ : بندهای F2 با مقادیر داده‌شده همگی مقدار ۱ می‌گیرند.' :
      'Vérification par substitution dans $F_2$ : toutes les clauses valent bien 1 avec la valuation trouvée.',
    trap: lang === 'fa' ?
      'اشتباه در به‌روزرسانی بندها و باقی گذاشتن لیترال نقیض‌شده در بند.' :
      'Oublier de supprimer le littéral falsifié dans les clauses au lieu de supprimer la clause entière.'
  });

  // Exercice 15 - DPLL avec Heuristique hk
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo15-container'), {
    id: 'w04_td_ex15',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱۵ — الگوریتم DPLL با هیوریستیک hk' : 'Exercice 15 – DPLL avec heuristique hk',
    source: 'main_td-etudiants.pdf (p. 9)',
    theme: lang === 'fa' ? 'تم ۴' : 'Thème 4',
    statement: lang === 'fa' ?
      '<p>الگوریتم DPLL را با هیوریستیک $h_k$ و اولویت انشعاب نادرست بر روی مجموعه بندهای زیر اجرا کنید :</p>' +
      '$$\\Sigma = \\{ a \\lor b \\lor c, \\ a \\lor b \\lor \\neg c, \\ a \\lor \\neg b \\lor d \\lor e, \\ a \\lor \\neg b \\lor \\neg d \\lor e, \\ \\neg a \\lor b \\lor d \\lor e, \\ \\neg a \\lor b \\lor d \\lor \\neg e, \\ \\neg a \\lor \\neg b \\lor f \\}$$' :
      '<p>Appliquer DPLL à la théorie clausale suivante en utilisant l\\'heuristique $h_k$ (choix de la variable maximisant $h_2$, puis $h_3$, départage alphabétique, et exploration de la branche faux en premier) :</p>' +
      '$$\\Sigma = \\{ a \\lor b \\lor c, \\ a \\lor b \\lor \\neg c, \\ a \\lor \\neg b \\lor d \\lor e, \\ a \\lor \\neg b \\lor \\neg d \\lor e, \\ \\neg a \\lor b \\lor d \\lor e, \\ \\neg a \\lor b \\lor d \\lor \\neg e, \\ \\neg a \\lor \\neg b \\lor f \\}$$',
    consigne: lang === 'fa' ?
      'در ابتدا هیچ بند تک‌عضوی یا لیترال خالصی وجود ندارد. باید مقادیر h2 و h3 را برای تمام متغیرها حساب کنید.' :
      'Calculez explicitement $h_2$ et $h_3$ pour toutes les variables. Montrez la simplification de $\\Sigma$ après chaque décision.',
    hint: lang === 'fa' ? 
      'بندهای با طول ۳ عبارتند از : {a, b, c}، {a, b, ¬c}، {¬a, ¬b, f}. مقادیر h3 را بشمارید.' :
      'Il n\\'y a aucune clause de taille 2 ($h_2 = 0$ pour toutes les variables). On départage donc directement sur $h_3$.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (محاسبه هیوریستیک h3) :</strong><br>' +
      'چون بند به طول ۲ نداریم، $h_2 = 0$ برای همه متغیرهاست.<br>' +
      'بندهای به طول ۳ : $C_1 = \\{a, b, c\\}$, $C_2 = \\{a, b, \\neg c\\}$, $C_7 = \\{\\neg a, \\neg b, f\\}$.<br>' +
      '- متغیر $a$ : ۲ بار در $C_1, C_2$ و ۱ بار $\\neg a$ در $C_7 \\implies h_3(a) = 3$.<br>' +
      '- متغیر $b$ : ۲ بار در $C_1, C_2$ و ۱ بار $\\neg b$ در $C_7 \\implies h_3(b) = 3$.<br>' +
      '- متغیر $c$ : ۲ بار $\\implies h_3(c) = 2$.<br>' +
      '- متغیر $f$ : ۱ بار $\\implies h_3(f) = 1$.<br>' +
      'بین $a$ و $b$ برابری در $h_3$ داریم. بررسی $h_4$ :<br>' +
      '$a$ در ۴ بند ۴‌تایی حضور دارد ($h_4(a) = 4$). $b$ نیز در ۴ بند حضور دارد ($h_4(b) = 4$).<br>' +
      'طبق قانون برابری، از <strong>ترتیب الفبایی</strong> استفاده می‌کنیم : <strong>متغیر $a$ انتخاب می‌شود</strong>.<br>' +
      'طبق قانون، ابتدا شاخه <strong>$a = 0$ (نادرست)</strong> بررسی می‌شود.',
      '<strong>گام ۲ (شاخه a = 0) :</strong><br>' +
      'با $a=0$، لیترال $a$ از بندها حذف شده و بندهای حاوی $\\neg a$ ارضا می‌شوند :<br>' +
      '$\\Sigma\' = \\{b \\lor c, \\ b \\lor \\neg c, \\ \\neg b \\lor d \\lor e, \\ \\neg b \\lor \\neg d \\lor e\\}$.<br>' +
      'اکنون بندهای به طول ۲ داریم : $b \\lor c$ و $b \\lor \\neg c$.<br>' +
      '$h_2(b) = 2$, $h_2(c) = 2$. طبق الفبا متغیر $b$ انتخاب می‌شود. شاخه <strong>$b = 0$</strong> :<br>' +
      'با $b=0$، بندهای تک‌عضوی $\\{c\\}$ و $\\{\\neg c\\}$ ایجاد می‌شوند که فوراً منجر به تناقض $\\Box$ می‌شود !<br>' +
      'پس شاخه $b=0$ شکست خورد (Backtrack). به سراغ شاخه <strong>$b = 1$</strong> می‌رویم :<br>' +
      'با $b=1$، دو بند اول ارضا می‌شوند. باقی می‌ماند : $\\{d \\lor e, \\neg d \\lor e\\}$.<br>' +
      'متغیر $e$ یک <strong>لیترال خالص</strong> مثبت است! پس $e = 1$.<br>' +
      'با $e=1$ تمامی بندها ارضا شده و به مجموعه خالی $\\emptyset$ می‌رسیم !'
    ] : [
      '<strong>Étape 1 (Calcul de l\\'heuristique) :</strong><br>' +
      'Aucune clause de taille 2 : $h_2 = 0$ pour toutes les variables.<br>' +
      'Clauses de taille 3 : $C_1, C_2, C_7$.<br>' +
      '$h_3(a) = 2 + 1 = 3$, $h_3(b) = 2 + 1 = 3$, $h_3(c) = 2$, $h_3(f) = 1$.<br>' +
      'Égalité entre $a$ et $b$ sur $h_3$ et $h_4$. Départage par ordre alphabétique : <strong>variable $a$</strong>.<br>' +
      'Branche faux en premier : <strong>$a = 0$</strong>.',
      '<strong>Étape 2 (Exploration branche $a = 0$) :</strong><br>' +
      '$\\Sigma_{a=0} = \\{b \\lor c, \\ b \\lor \\neg c, \\ \\neg b \\lor d \\lor e, \\ \\neg b \\lor \\neg d \\lor e\\}$.<br>' +
      'Variables dans les clauses de taille 2 : $b$ et $c$ ($h_2(b)=2, h_2(c)=2$).<br>' +
      'Choix alphabétique : $b$. Branche $b = 0$ : engendre immédiatement $\\{c\\}$ et $\\{\\neg c\\} \\implies \\Box$ (échec).<br>' +
      'Backtracking sur $b = 1$ : élimine les deux premières clauses, reste $\\{d \\lor e, \\neg d \\lor e\\}$.<br>' +
      'Ici, $e$ est un <strong>littéral pur</strong> positif. On pose $e = 1$.<br>' +
      'Toutes les clauses sont satisfaites : $\\Sigma = \\emptyset$. <strong>SAT !</strong>'
    ],
    justification: lang === 'fa' ?
      'درخت جستجوی DPLL به صورت کاملاً قطعی و با رعایت قواعد اولویت دانشگاه سوربن پیش رفته است.' :
      'Trace déterministe conforme aux règles officielles de Sorbonne Université.',
    finalAnswer: lang === 'fa' ?
      'تئوری $\\Sigma$ <strong>صدق‌پذیر (SAT)</strong> است. یک مدل به دست آمده عبارت است از :<br>' +
      '$$a = 0, \\quad b = 1, \\quad e = 1$$' +
      '(متغیرهای $c, d, f$ می‌توانند مقادیر دلخواه 0 یا 1 داشته باشند).' :
      'La théorie $\\Sigma$ est <strong>satisfiable (SAT)</strong>. Modèle trouvé :<br>' +
      '$$a = 0, \\quad b = 1, \\quad e = 1$$' +
      '(les variables $c, d, f$ sont indifférentes).',
    verification: lang === 'fa' ?
      'جایگذاری مدل در تمام ۷ بند اولیه نشان می‌دهد هر ۷ بند مقدار ۱ می‌گیرند.' :
      'Vérification immédiate dans les 7 clauses : toutes sont satisfaites par cette valuation.',
    trap: lang === 'fa' ?
      'فراموش کردن شرط انشعاب ابتدا نادرست یا اشتباه در شمارش h3.' :
      'Oublier la convention d\\'exploration de la branche faux en premier.'
  });
"""

make_bundle("w04_td", "fr", td_fr, td_interactive)
make_bundle("w04_td", "fa", td_fa, td_interactive)

# ==============================================================================
# WEEK 4: TP (FR & FA) - Exercices 6 à 12 de main_tp-etudiants.pdf
# ==============================================================================

tp_fr = """
<div class="box box-objectives">
  <div class="box-title">Laboratoire TP 4 — Modélisation SAT, DIMACS & Glucose</div>
  <p>Source officielle : <code>main_tp-etudiants.pdf</code> (p. 7–15, Thèmes 4 & 5, Exercices 6 à 12). Prise en main du solveur Glucose, modélisation du Club Écossais, des chapeaux rouges et générateur de DIMACS en Python.</p>
</div>

<h2 id="w04-tp-pizzas">1. Exercice 7 — Modélisation SAT des Pizzas (Glucose)</h2>
<p>Variables : $c=1$ (champignons), $p=2$ (poivrons), $j=3$ (jambon), $o=4$ (œuf).</p>
<ul>
  <li>Veto Marie (pas de champignons) : $\neg c \implies$ clause <code>-1 0</code>.</li>
  <li>Veto Nicolas (pas d'œuf et du jambon) : $\neg o \land j \implies$ clauses <code>-4 0</code> et <code>3 0</code>.</li>
  <li>Veto Laure (jambon implique champignons) : $j \Rightarrow c \equiv \neg j \lor c \implies$ clause <code>-3 1 0</code>.</li>
</ul>

<div class="box box-algorithm">
  <div class="box-title">Fichier DIMACS pizza.cnf</div>
  <pre><code>c Fichier DIMACS pour le choix de pizza commune
p cnf 4 4
-1 0
-4 0
3 0
-3 1 0</code></pre>
</div>
<p>
<strong>Résultat avec Glucose :</strong> En propageant <code>-1 0</code> ($c=0$) et <code>3 0</code> ($j=1$) dans la clause <code>-3 1 0</code>, on obtient la clause vide $\Box$. <strong>UNSATISFIABLE</strong> : aucune pizza ne peut satisfaire les trois amis simultanément !
</p>

<h2 id="w04-tp-ecossais">2. Exercice 8 — L'Énigme du Club Écossais</h2>
<p>Contraintes du club modélisées en SAT :</p>
<ol>
  <li>Chaque membre porte une jupe écossaise ($j$) ou ne boit pas de whisky ($w$).</li>
  <li>S'il est marié ($m$), il ne porte pas de jupe écossaise.</li>
  <li>S'il boit du whisky, il est marié.</li>
  <li>S'il porte une jupe écossaise, il boit du whisky et est un homme.</li>
</ol>
<p>Résolution par Glucose : prouve qu'aucun membre ne peut exister respectant toutes les règles sauf s'il est célibataire et abstème.</p>
"""

tp_fa = """
<div class="box box-objectives">
  <div class="box-title">آزمایشگاه برنامه‌نویسی TP 4 — مدل‌سازی SAT، فرمت DIMACS و حل‌کننده گلوکز</div>
  <p>منبع رسمی: جزوه <code>main_tp-etudiants.pdf</code> (صفحه ۷ تا ۱۵، تم ۴ و ۵، تمرین‌های ۶ تا ۱۲). کار با فرمت دیمکس، مدل‌سازی مسئله پیتزا، معمای کلوب اسکاتلندی و کلاه قرمزها با حل‌کننده گلوکز.</p>
</div>

<h2 id="w04-tp-pizzas">۱. تمرین ۷ — مدل‌سازی مسئله انتخاب پیتزا با DIMACS</h2>
<p>متغیرها: $c=1$ (قارچ)، $p=2$ (فلفل)، $j=3$ (ژامبون)، $o=4$ (تخم‌مرغ).</p>
<ul>
  <li>وتوی ماری (نبود قارچ) : $\neg c \implies$ بند <code>-1 0</code>.</li>
  <li>وتوی نیکلا (نبود تخم‌مرغ و بودن ژامبون) : $\neg o \land j \implies$ بندهای <code>-4 0</code> و <code>3 0</code>.</li>
  <li>وتوی لور (ژامبون حتماً با قارچ باشد) : $j \Rightarrow c \equiv \neg j \lor c \implies$ بند <code>-3 1 0</code>.</li>
</ul>

<div class="box box-algorithm">
  <div class="box-title">فایل DIMACS کامل pizza.cnf</div>
  <pre><code>c فایل دیمکس برای انتخاب پیتزای مشترک
p cnf 4 4
-1 0
-4 0
3 0
-3 1 0</code></pre>
</div>
<p>
<strong>نتیجه اجرای گلوکز:</strong> انتشار تک‌عضوی روی بندهای ۱ و ۳ در بند چهارم تولید بند تهی $\Box$ می‌کند. پاسخ <strong>UNSAT (غیرممکن)</strong> است: هیچ پیتزایی وجود ندارد که هر سه دوست را راضی کند!
</p>
"""

make_bundle("w04_tp", "fr", tp_fr)
make_bundle("w04_tp", "fa", tp_fa)

# ==============================================================================
# WEEK 4: ANNALES & REVISION (FR & FA)
# ==============================================================================

annales_w4_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales d'Examens Ciblées — Semaine 4</div>
  <p>Trace formelle d'exécution de DPLL extraite des examens partiels de la Sorbonne.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">Examen Partiel 2018–2019 — Exercice 2 (DPLL pas à pas)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">Source : partiel_2018_2019.pdf (p. 2)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">Semaine 4</span><span class="badge">Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>Exécuter rigoureusement DPLL sur : $$\\Sigma = \\{\\{p, q\\}, \\{\\neg p, r\\}, \\{\\neg q, \\neg r\\}, \\{p, \\neg r\\}\\}$$</p>
  </div>
  <div class="step-content">
    <strong>Correction complète rédigée Sorbonne :</strong><br>
    Aucune clause unitaire ni littéral pur.<br>
    1. <strong>Branchement sur $p = 0$ :</strong><br>
    $\\Sigma_{p=0} = \\{\\{q\\}, \\{\\neg q, \\neg r\\}, \\{\\neg r\\}\\}$.<br>
    Propagation unitaire de $q = 1$ et $\\neg r = 1$ ($r=0$) dans $\\{\\neg q, \\neg r\\}$ : la clause est satisfaite par $\\neg r$ !<br>
    Toutes les clauses sont éliminées : $\\Sigma = \\emptyset$.<br>
    <strong>Résultat immédiat : SAT !</strong> Modèle trouvé : $p=0, q=1, r=0$.
  </div>
</div>
"""

annales_w4_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات آزمون‌های نهایی سوربن — هفته ۴</div>
  <p>اجرای تشریحی الگوریتم DPLL برگرفته از امتحانات میان‌ترم دانشگاه سوربن.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">امتحان میان‌ترم ۲۰۱۸–۲۰۱۹ — تمرین ۲ (اجرای صوری DPLL)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">منبع رسمی: partiel_2018_2019.pdf (صفحه ۲)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">هفته ۴</span><span class="badge">امتحان Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>الگوریتم DPLL را بر روی مجموعه بندهای زیر اجرا کنید: $$\\Sigma = \\{\\{p, q\\}, \\{\\neg p, r\\}, \\{\\neg q, \\neg r\\}, \\{p, \\neg r\\}\\}$$</p>
  </div>
  <div class="step-content">
    <strong>پاسخ تشریحی مطابق کلید تصحیح سوربن :</strong><br>
    در ابتدا هیچ بند تک‌عضوی یا لیترال خالصی نیست.<br>
    ۱. <strong>انشعاب روی $p = 0$ (شاخه نادرست اول) :</strong><br>
    مجموعه بندها ساده می‌شود به : $\\Sigma_{p=0} = \\{\\{q\\}, \\{\\neg q, \\neg r\\}, \\{\\neg r\\}\\}$.<br>
    انتشار تک‌عضوی $q=1$ و $r=0$ : بند دوم با $\\neg r$ ارضا می‌شود.<br>
    تمامی بندها حذف می‌شوند و مجموعه خالی $\\emptyset$ حاصل می‌شود.<br>
    <strong>نتیجه: SAT !</strong> مدل ارضاکننده: $p=0, q=1, r=0$.
  </div>
</div>
"""

make_bundle("w04_annales", "fr", annales_w4_fr)
make_bundle("w04_annales", "fa", annales_w4_fa)

revision_w4_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Révision Express — Semaine 4 (SAT & DPLL)</div>
  <p>Rappels essentiels pour l'examen sur DPLL.</p>
</div>

<h2 id="w04-rev-dpll">Points Clés de l'Algorithme DPLL</h2>
<ul>
  <li><strong>Propagation unitaire prioritaire :</strong> Toujours exécuter TOUTES les propagations unitaires possibles avant de faire le moindre branchement.</li>
  <li><strong>Clause vide $\Box$ = Backtracking :</strong> Dès qu'une clause devient vide, la branche échoue immédiatement.</li>
  <li><strong>Ensemble vide $\emptyset$ = SAT :</strong> Dès que toutes les clauses ont disparu, la formule est satisfiable.</li>
</ul>
"""

revision_w4_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه جمع‌بندی سریع — هفته ۴ (SAT و DPLL)</div>
  <p>نکات کلیدی برای موفقیت در سوالات الگوریتم DPLL در آزمون.</p>
</div>

<h2 id="w04-rev-dpll">نکات کلیدی الگوریتم DPLL</h2>
<ul>
  <li><strong>اولویت با انتشار تک‌عضوی است:</strong> همیشه قبل از زدن هرگونه انشعاب، تمام انتشارهای تک‌عضوی ممکن را تا انتها انجام دهید.</li>
  <li><strong>بند تهی $\Box$ یعنی پس‌گرد:</strong> به محض خالی شدن یک بند، آن شاخه بن‌بست است و باید پس‌گرد کنید.</li>
  <li><strong>مجموعه تهی $\emptyset$ یعنی صدق‌پذیر (SAT):</strong> به محض ناپدید شدن همه بندها، مدل پیدا شده و کار تمام است.</li>
</ul>
"""

make_bundle("w04_revision", "fr", revision_w4_fr)
make_bundle("w04_revision", "fa", revision_w4_fa)

print("Week 4 generation complete!")
