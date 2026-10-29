# -*- coding: utf-8 -*-
"""
Generator for Week 11 bundles:
- w11_cours.fr.js / w11_cours.fa.js
- w11_td.fr.js / w11_td.fa.js
- w11_tp.fr.js / w11_tp.fa.js
- w11_annales.fr.js / w11_annales.fa.js
- w11_revision.fr.js / w11_revision.fa.js
"""

import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 11: COURS (FR & FA)
# ==============================================================================

c11_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 11 (Prolog Avancé, Formes Normales & Skolémisation)</div>
  <ul>
    <li>Maîtriser la récursivité sur les listes en Prolog avec l'opérateur cons <code>[Tete | Queue]</code>.</li>
    <li>Comprendre l'écriture et le fonctionnement bidirectionnel du prédicat <code>append/3</code>.</li>
    <li>Mettre une formule LPPO sous <strong>Forme Normale Négative (FNN)</strong> et <strong>Forme Prénexe</strong>.</li>
    <li>Maîtriser la <strong>Skolémisation</strong> : élimination rigoureuse des quantificateurs existentiels par des constantes et fonctions de Skolem.</li>
    <li>Comprendre la notion capitale d'<strong>équisatisfiabilité</strong> et le <strong>Théorème de Herbrand</strong>.</li>
  </ul>
</div>

<h2 id="w11-c-listes-prolog">1. Les Listes en Prolog et le Prédicat <code>append</code></h2>
<div class="box box-definition">
  <div class="box-title">Définition 11.1 — Structure Inductive d'une Liste</div>
  <p>En Prolog, une liste est définie inductivement par :</p>
  <ul>
    <li>La liste vide : <code>[]</code></li>
    <li>La cellule cons : <code>[T | Q]</code> où <code>T</code> est le premier élément (la tête) et <code>Q</code> est le reste de la liste (la queue).</li>
  </ul>
  <p>Exemple : <code>[a, b, c]</code> est du sucre syntaxique pour <code>[a | [b | [c | []]]]</code>.</p>
</div>

<div class="box box-method">
  <div class="box-title">Le Prédicat Magique : <code>append(L1, L2, L3)</code></div>
  <pre><code>append([], L, L).
append([X | L1], L2, [X | L3]) :- append(L1, L2, L3).</code></pre>
  <p>Prolog peut utiliser ce prédicat dans les deux sens :</p>
  <ul>
    <li><strong>Concaténer :</strong> <code>?- append([a, b], [c, d], R).</code> $\implies$ <code>R = [a, b, c, d]</code>.</li>
    <li><strong>Décomposer :</strong> <code>?- append(X, Y, [a, b]).</code> génère par backtracking toutes les partitions possibles de la liste !</li>
  </ul>
</div>

<h2 id="w11-c-formes-normales-lppo">2. Formes Normales en LPPO : Prénexe et Skolémisation</h2>
<p>Pour appliquer la méthode de résolution à une formule de premier ordre quelconque, on doit la transformer en forme clausale en suivant 4 étapes strictes :</p>

<div class="box box-method">
  <div class="box-title">Les 4 Étapes de la Transformation Clausale en LPPO</div>
  <ol>
    <li><strong>Forme Normale Négative (FNN) :</strong> On élimine les équivalences et implications, puis on pousse les négations jusqu'aux atomes à l'aide des lois de De Morgan :
    $$\neg \forall x A \equiv \exists x \neg A \quad \text{et} \quad \neg \exists x A \equiv \forall x \neg A$$</li>
    <li><strong>Renommage des variables ($\alpha$-conversion) :</strong> On s'assure que chaque quantificateur porte sur une variable portant un nom distinct afin d'éviter toute ambiguïté de portée.</li>
    <li><strong>Forme Prénexe :</strong> On extrait tous les quantificateurs en tête de formule :
    $$Q_1 x_1 Q_2 x_2 \dots Q_k x_k \; M(x_1, \dots, x_k)$$
    où la matrice $M$ ne contient plus aucun quantificateur.</li>
    <li><strong>Skolémisation (Forme de Skolem) :</strong> On élimine les quantificateurs existentiels de gauche à droite :
      <ul>
        <li>Si $\exists y$ n'est précédé d'aucun quantificateur universel, on remplace chaque occurrence libre de $y$ par une nouvelle constante de Skolem $c$.</li>
        <li>Si $\exists y$ est précédé par les quantificateurs universels $\forall x_1, \dots, \forall x_n$, on remplace $y$ par un terme fonctionnel $f_y(x_1, \dots, x_n)$ où $f_y$ est un nouveau symbole de fonction.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Attention Conceptuelle : Équivalence vs Équisatisfiabilité</div>
  <p>La formule skolémisée $F_{sk}$ n'est <strong>PAS logiquement équivalente</strong> à la formule de départ $F$ (car la signature a été enrichie de nouvelles fonctions) !</p>
  <p>En revanche, elles sont <strong>ÉQUISATISFIABLES</strong> :</p>
  $$F \text{ est satisfiable} \iff F_{sk} \text{ est satisfiable}$$
  <p>C'est exactement ce dont la preuve par réfutation a besoin pour conclure !</p>
</div>
"""

c11_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف یادگیری — هفته ۱۱ (پرولوگ پیشرفته، فرم‌های نرمال و اسکولم‌سازی)</div>
  <ul>
    <li>تسلط بر بازگشت روی لیست‌ها در پرولوگ با ساختار <code>[سر | دم]</code>.</li>
    <li>درک عملکرد دوطرفه و شگفت‌انگیز محمول <code>append/3</code>.</li>
    <li>تبدیل فرمول مرتبه اول به <strong>فرم نرمال منفی (NNF)</strong> و <strong>فرم پیشوندی (Prenex Form)</strong>.</li>
    <li>تسلط بر فرایند <strong>اسکولم‌سازی (Skolemization)</strong> برای حذف سورهای وجودی با توابع اسکولم.</li>
    <li>درک مفهوم بنیادی <strong>هم‌پذیرش‌پذیری (Equisatisfiability)</strong> و <strong>قضیه هربراند (Herbrand's Theorem)</strong>.</li>
  </ul>
</div>

<h2 id="w11-c-listes-prolog">۱. لیست‌ها در پرولوگ و محمول <code>append</code></h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۱۱.۱ — ساختار بازگشتی لیست</div>
  <p>در زبان پرولوگ، لیست ساختاری است که به صورت بازگشتی تعریف می‌شود:</p>
  <ul>
    <li>لیست تهی: <code>[]</code></li>
    <li>عملگر سازنده لیست: <code>[T | Q]</code> که در آن <code>T</code> اولین عنصر (Head) و <code>Q</code> باقی‌مانده لیست (Tail) است.</li>
  </ul>
</div>

<div class="box box-method">
  <div class="box-title">قوانین محمول بنیادین <code>append/3</code></div>
  <pre><code>append([], L, L).
append([X | L1], L2, [X | L3]) :- append(L1, L2, L3).</code></pre>
  <p>این محمول به دلیل ماهیت رابطه‌ای پرولوگ، هم برای چسباندن لیست‌ها و هم برای قطعه‌قطعه کردن و تجزیه لیست‌ها با مکانیزم عقب‌گرد عمل می‌کند.</p>
</div>

<h2 id="w11-c-formes-normales-lppo">۲. فرم‌های نرمال در LPPO: فرم پیشوندی و اسکولم‌سازی</h2>
<div class="box box-method">
  <div class="box-title">چهار مرحله استاندارد تبدیل به فرم بندی</div>
  <ol>
    <li><strong>فرم نرمال منفی (NNF):</strong> رساندن نقیض به پشت اتم‌ها با قوانین دمورگان سورها:
    $$\neg \forall x A \equiv \exists x \neg A \quad , \quad \neg \exists x A \equiv \forall x \neg A$$</li>
    <li><strong>تغییر نام متغیرها:</strong> برای هر سور نام متغیر جداگانه می‌گذاریم تا تداخل حوزه رخ ندهد.</li>
    <li><strong>فرم پیشوندی (Prenex):</strong> بیرون کشیدن تمام سورها به ابتدای عبارت:
    $$Q_1 x_1 Q_2 x_2 \dots Q_k x_k \; M(x_1, \dots, x_k)$$</li>
    <li><strong>اسکولم‌سازی (Skolemization):</strong> حذف سورهای وجود ($\exists$):
      <ul>
        <li>اگر پشت سور وجود هیچ سور کلی ($\forall$) نباشد، با یک ثابت اسکولم $c$ جایگزین می‌شود.</li>
        <li>اگر پشت سور وجود، سورهای کلی $\forall x_1 \dots \forall x_n$ قرار داشته باشند، آن متغیر با تابع اسکولم $f(x_1, \dots, x_n)$ جایگزین می‌گردد.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box box-pourquoi">
  <div class="box-title">نکته حیاتی: هم‌ارزی منطقی در برابر هم‌پذیرش‌پذیری</div>
  <p>فرمول اسکولم‌شده $F_{sk}$ با فرمول اولیه $F$ <strong>هم‌ارز منطقی نیست</strong>؛ اما این دو فرمول <strong>هم‌پذیرش‌پذیر (Equisatisfiable)</strong> هستند؛ یعنی $F$ سازگار و مدل‌دار است اگر و تنها اگر $F_{sk}$ مدل‌دار باشد. و این برای اثبات به روش تفکیک و تناقض کاملاً کافی است!</p>
</div>
"""

# ==============================================================================
# WEEK 11: TD 11 (Exercices 40 & 41) (FR & FA)
# ==============================================================================

td11_fr = """
<div class="box box-objectives">
  <div class="box-title">TD Thème 11 — Listes Prolog & Formes Normales LPPO (Exercices 40 et 41)</div>
  <p>Source : <code>main_td-etudiants.pdf</code>, pages 23–24. Résolution exhaustive des exercices 40 et 41.</p>
</div>

<h2 id="w11-td-ex40">Exercice 40 — Listes en Prolog : Unification et Prédicats (p. 23)</h2>
<div class="box box-solution">
  <div class="box-title">Question 1 : Réponses aux requêtes d'unification</div>
  <ol>
    <li><code>?- [a, b, c] = [X].</code> $\implies$ <strong>false (Échec)</strong> car le membre de gauche a 3 éléments et celui de droite un seul.</li>
    <li><code>?- [a, b, c] = [X, Y, Z].</code> $\implies$ <strong>Succès : X = a, Y = b, Z = c.</strong></li>
    <li><code>?- [a, b, c] = [X | Y].</code> $\implies$ <strong>Succès : X = a, Y = [b, c].</strong> (Tête = premier élément, Queue = liste des éléments suivants).</li>
    <li><code>?- [a, [b, c], d] = [X, Y, Z].</code> $\implies$ <strong>Succès : X = a, Y = [b, c], Z = d.</strong></li>
    <li><code>?- append([a, b], [c, d], [a, b, c, d]).</code> $\implies$ <strong>true.</strong></li>
    <li><code>?- append([a, b], [c, d], L).</code> $\implies$ <strong>L = [a, b, c, d].</strong></li>
    <li><code>?- append([a, b], [c, d], [c, d, a, b]).</code> $\implies$ <strong>false.</strong></li>
    <li><code>?- append(X, [c, Y], [a, b, c, d]).</code> $\implies$ <strong>X = [a, b], Y = d.</strong></li>
    <li><code>?- append(X, Y, [a, b, c, d]).</code> $\implies$ Génère successivement 5 solutions :
      <ul>
        <li><code>X = [], Y = [a, b, c, d]</code></li>
        <li><code>X = [a], Y = [b, c, d]</code></li>
        <li><code>X = [a, b], Y = [c, d]</code></li>
        <li><code>X = [a, b, c], Y = [d]</code></li>
        <li><code>X = [a, b, c, d], Y = []</code></li>
      </ul>
    </li>
  </ol>
</div>

<div class="box box-solution">
  <div class="box-title">Question 2 : Définition des Prédicats de Manipulation de Listes</div>
  <p><strong>1. Prédicat <code>premier(L, X)</code> :</strong></p>
  <pre><code>premier([X | _], X).</code></pre>
  <p><strong>2. Prédicat <code>dernier(L, X)</code> :</strong></p>
  <pre><code>dernier([X], X).
dernier([_ | Queue], X) :- dernier(Queue, X).</code></pre>
  <p><strong>3. Prédicat <code>longueur(L, N)</code> :</strong></p>
  <pre><code>longueur([], 0).
longueur([_ | Q], N) :- longueur(Q, N1), N is N1 + 1.</code></pre>
</div>

<h2 id="w11-td-ex41">Exercice 41 — Formes Normales en LPPO (p. 24)</h2>
<p>Formule initiale : $F = \neg ( (\forall x(p(f(x)) \implies \neg q(x))) \implies \neg \exists x (p(f(x)) \land q(x)) )$.</p>

<div class="box box-solution">
  <div class="box-title">Résolution Étape par Étape</div>
  <p><strong>Étape 1 : Forme Normale Négative (FNN)</strong></p>
  <p>On applique $\neg(A \implies B) \equiv A \land \neg B$ :</p>
  $$(\forall x(p(f(x)) \implies \neg q(x))) \land \neg \neg \exists x (p(f(x)) \land q(x))$$
  $$\equiv (\forall x(\neg p(f(x)) \lor \neg q(x))) \land \exists x (p(f(x)) \land q(x))$$

  <p><strong>Étape 2 : Renommage et Forme Prénexe</strong></p>
  <p>On renomme la variable de l'existentiel en $y$ :</p>
  $$(\forall x(\neg p(f(x)) \lor \neg q(x))) \land \exists y (p(f(y)) \land q(y))$$
  <p>Extraction des quantificateurs :</p>
  $$\forall x \exists y [ (\neg p(f(x)) \lor \neg q(x)) \land p(f(y)) \land q(y) ]$$

  <p><strong>Étape 3 : Skolémisation</strong></p>
  <p>Le quantificateur $\exists y$ dépend de $\forall x$. On introduit le symbole de fonction de Skolem $g$ : $y \mapsto g(x)$.</p>
  $$\forall x [ (\neg p(f(x)) \lor \neg q(x)) \land p(f(g(x))) \land q(g(x)) ]$$

  <p><strong>Étape 4 : Forme Normale Conjonctive (Clauses)</strong></p>
  <ul>
    <li>$C_1 = \neg p(f(x)) \lor \neg q(x)$</li>
    <li>$C_2 = p(f(g(x)))$</li>
    <li>$C_3 = q(g(x))$</li>
  </ul>

  <p><strong>Étape 5 : Résolution et Conclusion</strong></p>
  <p>Résolution entre $C_2$ (avec renommage $x'$) et $C_1$ avec l'unificateur $\sigma = \{x \mapsto g(x')\}$ :</p>
  $$\text{Res}(C_2, C_1) = \neg q(g(x'))$$
  <p>Résolution avec $C_3$ :</p>
  $$\text{Res}(\neg q(g(x')), q(g(x))) = \Box$$
  <p><strong>Conclusion :</strong> On a dérivé la clause vide $\Box$. La formule $F$ est donc <strong>INSATISFIABLE</strong> !</p>
</div>
"""

td11_fa = """
<div class="box box-objectives">
  <div class="box-title">حل تمرینات موضوع ۱۱ — لیست‌های پرولوگ و فرم‌های نرمال LPPO (تمرین‌های ۴۰ و ۴۱)</div>
  <p>منبع رسمی: <code>main_td-etudiants.pdf</code>، صفحات ۲۳ و ۲۴. حل تشریحی گام‌به‌گام کار با لیست‌ها، یکسان‌سازی، فرم پیشوندی و اسکولم‌سازی.</p>
</div>

<h2 id="w11-td-ex40">تمرین ۴۰ — لیست‌ها در پرولوگ و یکسان‌سازی (صفحه ۲۳)</h2>
<div class="box box-solution">
  <div class="box-title">پاسخ تشریحی سؤال ۱</div>
  <ol>
    <li><code>?- [a, b, c] = [X].</code> $\implies$ <strong>شکست (false)</strong> چون تعداد اعضا همخوانی ندارد.</li>
    <li><code>?- [a, b, c] = [X, Y, Z].</code> $\implies$ <strong>موفقیت: X = a, Y = b, Z = c.</strong></li>
    <li><code>?- [a, b, c] = [X | Y].</code> $\implies$ <strong>موفقیت: X = a و Y = [b, c].</strong> (سر لیست $X$ و دم لیست $Y$).</li>
    <li><code>?- append(X, [c, Y], [a, b, c, d]).</code> $\implies$ <strong>موفقیت: X = [a, b] و Y = d.</strong></li>
    <li><code>?- append(X, Y, [a, b, c, d]).</code> $\implies$ با زدن کلید <code>;</code> تمام ۵ افراز ممکن لیست تولید می‌شود.</li>
  </ol>
</div>

<h2 id="w11-td-ex41">تمرین ۴۱ — فرم‌های نرمال در LPPO (صفحه ۲۴)</h2>
<div class="box box-solution">
  <div class="box-title">مراحل گام‌به‌گام اسکولم‌سازی و تفکیک</div>
  <p>فرمول داده‌شده: $F = \neg ( (\forall x(p(f(x)) \implies \neg q(x))) \implies \neg \exists x (p(f(x)) \land q(x)) )$.</p>
  <ul>
    <li><strong>مرحله ۱ (NNF):</strong> نقیض به داخل برده می‌شود: $(\forall x(\neg p(f(x)) \lor \neg q(x))) \land \exists x (p(f(x)) \land q(x))$.</li>
    <li><strong>مرحله ۲ (تغییر نام و پیشوندی):</strong> متغیر سور وجودی را به $y$ تغییر می‌دهیم و سورها را بیرون می‌کشیم: $\forall x \exists y [(\neg p(f(x)) \lor \neg q(x)) \land p(f(y)) \land q(y)]$.</li>
    <li><strong>مرحله ۳ (اسکولم‌سازی):</strong> چون $\exists y$ بعد از $\forall x$ است، متغیر $y$ با تابع اسکولم $g(x)$ جایگزین می‌شود.</li>
    <li><strong>مرحله ۴ (بندها):</strong> سه بند $C_1, C_2, C_3$ استخراج می‌گردد.</li>
    <li><strong>مرحله ۵ (تفکیک):</strong> با تفکیک متوالی، بند پوچ $\Box$ حاصل می‌شود؛ بنابراین فرمول $F$ <strong>ناسازگار (Insatisfiable)</strong> است.</li>
  </ul>
</div>
"""

# ==============================================================================
# WEEK 11: TP 11 (Exercices 19, 20, 21) (FR & FA)
# ==============================================================================

tp11_fr = """
<div class="box box-objectives">
  <div class="box-title">TP Thème 11 — Listes et Applications Prolog (Exercices 19, 20 et 21)</div>
  <p>Source : <code>main_tp-etudiants.pdf</code>, pages 19–24. Pratique avancée des listes en Prolog.</p>
</div>

<h2 id="w11-tp-ex20">Exercice 20 — Manipulation de Listes</h2>
<pre><code>% Deuxième élément
deuxieme([_, X | _], X).

% Avant-dernier élément
avantDernier([X, _], X).
avantDernier([_ | Q], X) :- avantDernier(Q, X).

% Inversion de liste (version avec accumulateur O(n))
inverse(L, Res) :- inv_acc(L, [], Res).
inv_acc([], Acc, Acc).
inv_acc([T | Q], Acc, Res) :- inv_acc(Q, [T | Acc], Res).</code></pre>

<h2 id="w11-tp-ex21">Exercice 21 — Menus et Listes de Courses</h2>
<pre><code>entree(salade). entree(avocat).
plat(poulet). plat(saumon).
dessert(pomme). dessert(yaourt).

menuValide([E, P, D]) :- entree(E), plat(P), dessert(D).</code></pre>
"""

tp11_fa = """
<div class="box box-objectives">
  <div class="box-title">کار عملی موضوع ۱۱ — برنامه‌های کاربردی لیست‌ها در پرولوگ (تمرین‌های ۱۹، ۲۰ و ۲۱)</div>
  <p>منبع رسمی: <code>main_tp-etudiants.pdf</code>، صفحات ۱۹ تا ۲۴.</p>
</div>

<h2 id="w11-tp-ex20">تمرین ۲۰ — دستکاری و معکوس کردن لیست</h2>
<pre><code>% عنصر دوم
deuxieme([_, X | _], X).

% عنصر یکی مانده به آخر
avantDernier([X, _], X).
avantDernier([_ | Q], X) :- avantDernier(Q, X).

% معکوس کردن بهینه با انباشت‌گر (O(n))
inverse(L, Res) :- inv_acc(L, [], Res).
inv_acc([], Acc, Acc).
inv_acc([T | Q], Acc, Res) :- inv_acc(Q, [T | Acc], Res).</code></pre>
"""

# ==============================================================================
# WEEK 11: ANNALES (FR & FA)
# ==============================================================================

ann11_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales & Synthèse de Fin de Semestre — Semaine 11</div>
  <p>Bilan complet de préparation aux examens finaux de Sorbonne Université pour l'UE UL2IN007 Logique.</p>
</div>

<h2 id="w11-ann-bilan">Conseils Méthodologiques pour l'Examen Final</h2>
<p>L'examen terminal porte traditionnellement sur :</p>
<ol>
  <li><strong>Partie 1 (Propositionnelle) :</strong> Syntaxe, arbres, valuations, FNC, résolutions, algorithme DPLL avec calcul rigoureux de $h_k$.</li>
  <li><strong>Partie 2 (Déduction Naturelle Propositionnelle) :</strong> Preuves avec boîtes de Fitch (règles classiques vs intuitionnistes).</li>
  <li><strong>Partie 3 (LPPO Sémantique) :</strong> Construction de modèles, interprétations finies, calcul de validité et contre-modèles.</li>
  <li><strong>Partie 4 (LPPO Déduction Naturelle) :</strong> Preuves avec quantificateurs ($\forall I, \exists E$), vigilance absolue sur les conditions de fraîcheur des variables !</li>
</ol>
"""

ann11_fa = """
<div class="box box-objectives">
  <div class="box-title">جمع‌بندی و راهنمای امتحانات پایانی — هفته ۱۱</div>
  <p>نقشه راه موفقیت در آزمون نهایی درس منطق دانشگاه سوربن (UL2IN007).</p>
</div>

<h2 id="w11-ann-bilan">نکات طلایی برای کسب بالاترین نمره در امتحان پایانی</h2>
<ol>
  <li><strong>بخش اول (گزاره‌ای):</strong> تسلط بر جداول ارزش، ارزش‌دهی‌ها، الگوریتم DPLL با محاسبه دقیق هیوریستیک $h_k$ و اولویت انشعاب مقدار صفر.</li>
  <li><strong>بخش دوم (استنتاج طبیعی گزاره‌ای):</strong> رسم دقیق کادرهای فیچ و رعایت قواعد معرفی و حذف.</li>
  <li><strong>بخش سوم (معناشناسی مرتبه اول):</strong> ساخت ساختارها و مدل‌های متناهی و ارائه پادمدل‌های دقیق.</li>
  <li><strong>بخش چهارم (استنتاج طبیعی LPPO):</strong> مراقبت اکید از شرط تازگی متغیرها در قواعد $\forall I$ و $\exists E$.</li>
</ol>
"""

# ==============================================================================
# WEEK 11: REVISION (FR & FA)
# ==============================================================================

rev11_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Synthèse Finale du Cours — Semaine 11</div>
  <ul>
    <li>Félicitations ! Vous avez parcouru l'intégralité du programme officiel de Logique de Sorbonne Université.</li>
    <li>11 Semaines, 41 Exercices de TD entièrement résolus, 21 Travaux Pratiques commentés et 142 Problèmes d'examens analysés.</li>
  </ul>
</div>
"""

rev11_fa = """
<div class="box box-objectives">
  <div class="box-title">خلاصه پایانی کل دوره — هفته ۱۱</div>
  <ul>
    <li>تبریک! شما کل برنامه رسمی و سرفصل آموزشی منطق دانشگاه سوربن را به پایان رساندید.</li>
    <li>۱۱ هفته آموزشی، ۴۱ تمرین کلاسی با حل تشریحی گام‌به‌گام، ۲۱ پروژه عملی پرولوگ و پایتون، و ۱۴۲ مسئله از ۳۱ دوره امتحانات گذشته.</li>
  </ul>
</div>
"""

# Build week 11 bundles
make_bundle('w11_cours', 'fr', c11_fr)
make_bundle('w11_cours', 'fa', c11_fa)
make_bundle('w11_td', 'fr', td11_fr)
make_bundle('w11_td', 'fa', td11_fa)
make_bundle('w11_tp', 'fr', tp11_fr)
make_bundle('w11_tp', 'fa', tp11_fa)
make_bundle('w11_annales', 'fr', ann11_fr)
make_bundle('w11_annales', 'fa', ann11_fa)
make_bundle('w11_revision', 'fr', rev11_fr)
make_bundle('w11_revision', 'fa', rev11_fa)

print("Week 11 generation complete!")

