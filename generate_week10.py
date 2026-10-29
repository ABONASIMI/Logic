# -*- coding: utf-8 -*-
"""
Generator for Week 10 bundles:
- w10_cours.fr.js / w10_cours.fa.js
- w10_td.fr.js / w10_td.fa.js
- w10_tp.fr.js / w10_tp.fa.js
- w10_annales.fr.js / w10_annales.fa.js
- w10_revision.fr.js / w10_revision.fa.js
"""

import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 10: COURS (FR & FA)
# ==============================================================================

c10_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 10 (Résolution, Unification & Prolog)</div>
  <ul>
    <li>Comprendre le <strong>principe de résolution</strong> en logique des propositions et son utilisation par réfutation (recherche de la clause vide $\\Box$).</li>
    <li>Maîtriser l'<strong>algorithme d'unification de Robinson</strong> pour calculer le Plus Général Unificateur (mgu).</li>
    <li>Comprendre la vérification d'occurrence (<strong>occurs check</strong>) et le risque de boucle infinie en cas d'omission.</li>
    <li>Effectuer des résolutions en LPPO avec standardisation à part des variables.</li>
    <li>Découvrir la programmation logique en <strong>Prolog</strong>, les clauses de Horn et les arbres de résolution <strong>SLD</strong>.</li>
  </ul>
</div>

<h2 id="w10-c-resolution-prop">1. La Règle de Résolution Propositionnelle</h2>
<div class="box box-definition">
  <div class="box-title">Définition 10.1 — La Règle de Résolution</div>
  <p>Soient deux clauses $C_1 = A \lor p$ et $C_2 = B \lor \neg p$. Leur <strong>résolvante</strong> sur le littéral complémentaire $p$ est la clause :</p>
  $$\\text{Res}(C_1, C_2) = A \\lor B$$
  <p>Si $C_1 = p$ et $C_2 = \neg p$, la résolvante est la <strong>clause vide</strong>, notée $\\Box$, qui est par définition insatisfiable (équivalente à $\\bot$).</p>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — Éliminer deux littéraux simultanément</div>
  <p><strong>ATTENTION ERREUR CLASSIQUE :</strong> Si $C_1 = p \lor q$ et $C_2 = \neg p \lor \neg q$, la résolvante sur $p$ est $q \lor \neg q \equiv \\top$ (une tautologie sans intérêt). Il est <strong>STRICTEMENT INTERDIT</strong> d'éliminer à la fois $p$ et $q$ pour écrire $\\Box$ ! En effet, la valuation $v(p)=1, v(q)=0$ satisfait $C_1$ et $C_2$, donc l'ensemble n'est PAS contradictoire !</p>
</div>

<h2 id="w10-c-unification-robinson">2. L'Algorithme d'Unification de Robinson</h2>
<div class="box box-definition">
  <div class="box-title">Définition 10.2 — Unificateur et mgu</div>
  <p>Deux termes $t_1$ et $t_2$ sont unifiables s'il existe une substitution $\sigma$ telle que $t_1\sigma = t_2\sigma$. Le <strong>mgu</strong> (most general unifier) est l'unificateur le plus général dont tout autre unificateur est une instance.</p>
</div>

<div class="box box-method">
  <div class="box-title">Algorithme de Robinson par transformation d'équations</div>
  <p>On part d'un système d'équations $\{s_1 \doteq t_1, \dots, s_k \doteq t_k\}$ et on applique les règles jusqu'à convergence ou échec :</p>
  <ul>
    <li><strong>Effacement (Delete) :</strong> $\{t \doteq t\} \cup S \implies S$.</li>
    <li><strong>Décomposition :</strong> $\{f(u_1, \dots, u_n) \doteq f(v_1, \dots, v_n)\} \cup S \implies \{u_1 \doteq v_1, \dots, u_n \doteq v_n\} \cup S$.</li>
    <li><strong>Clash (Échec de symbole) :</strong> $\{f(\dots) \doteq g(\dots)\} \cup S \implies$ <strong>ÉCHEC</strong> (symboles différents).</li>
    <li><strong>Orientation :</strong> $\{t \doteq x\} \cup S \implies \{x \doteq t\} \cup S$ (si $t$ n'est pas une variable).</li>
    <li><strong>Élimination de variable :</strong> $\{x \doteq t\} \cup S$ :
      <ul>
        <li>Si $x \in Free(t)$ et $x \neq t$ : <strong>ÉCHEC (Occurs Check)</strong>. Exemple : $x \doteq f(x)$ n'a pas de solution finie !</li>
        <li>Sinon, on remplace $x$ par $t$ dans toutes les autres équations de $S$, et on conserve $x \mapsto t$ dans la substitution finale.</li>
      </ul>
    </li>
  </ul>
</div>

<h2 id="w10-c-prolog-intro">3. Programmation Logique & Prolog (Clauses de Horn)</h2>
<div class="box box-definition">
  <div class="box-title">Définition 10.3 — Clauses de Horn et Syntaxe Prolog</div>
  <p>Une <strong>clause de Horn</strong> contient au plus un littéral positif :</p>
  <ul>
    <li><strong>Fait :</strong> $P(t) \leftarrow$ (aucun littéral négatif). En Prolog : <code>p(t).</code></li>
    <li><strong>Règle :</strong> $P(t) \leftarrow Q_1 \land \dots \land Q_n \equiv P(t) \lor \neg Q_1 \lor \dots \lor \neg Q_n$. En Prolog : <code>p(t) :- q1, ..., qn.</code></li>
    <li><strong>Requête (But) :</strong> $\leftarrow Q_1 \land \dots \land Q_n \equiv \neg Q_1 \lor \dots \lor \neg Q_n$. En Prolog : <code>?- q1, ..., qn.</code></li>
  </ul>
  <p>L'interpréteur Prolog utilise la <strong>résolution SLD</strong> avec stratégie de recherche en profondeur d'abord (Depth-First Search) et retour sur trace (Backtracking).</p>
</div>
"""

c10_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف یادگیری — هفته ۱۰ (روش تفکیک، یکسان‌سازی رابینسون و پرولوگ)</div>
  <ul>
    <li>درک <strong>قاعده تفکیک (Resolution Principle)</strong> در منطق گزاره‌ای و اثبات با نقیض برای رسیدن به بند پوچ ($\Box$).</li>
    <li>تسلط بر <strong>الگوریتم یکسان‌سازی رابینسون (Robinson's MGU)</strong> با تبدیل گام‌به‌گام سیستم معادلات.</li>
    <li>فهم عمیق بررسی رخداد (<strong>Occurs Check</strong>) و علت بروز حلقه‌های بی‌نهایت در صورت غفلت از آن.</li>
    <li>اجرای تفکیک در منطق مرتبه اول LPPO همراه با تغییر نام متغیرهای هر بند (Standardizing apart).</li>
    <li>آشنایی با برنامه‌نویسی منطقی با <strong>Prolog</strong>، بندهای هورن (Horn Clauses) و درخت‌های تفکیک <strong>SLD</strong>.</li>
  </ul>
</div>

<h2 id="w10-c-resolution-prop">۱. قاعده تفکیک در منطق گزاره‌ای</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۱۰.۱ — قاعده تفکیک (Resolution)</div>
  <p>فرض کنیم دو بند $C_1 = A \lor p$ و $C_2 = B \lor \neg p$ داشته باشیم. <strong>تفکیک‌یافته (Resolvent)</strong> این دو روی لیترال مکمل $p$ برابر است با:</p>
  $$\\text{Res}(C_1, C_2) = A \\lor B$$
  <p>اگر $C_1 = p$ و $C_2 = \neg p$ باشد، تفکیک‌یافته یک <strong>بند پوچ یا خالی</strong> است که با $\\Box$ نمایش داده می‌شود و ذاتاً ناسازگار (معادل $\\bot$) است.</p>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — حذف همزمان دو حرف مکمل!</div>
  <p><strong>هشدار مهم:</strong> اگر $C_1 = p \lor q$ و $C_2 = \neg p \lor \neg q$ باشد، تفکیک روی $p$ عبارت $q \lor \neg q \equiv \\top$ را می‌دهد. <strong>اکیداً مجاز نیستید</strong> هر دو متغیر $p$ و $q$ را هم‌زمان حذف کنید و بنویسید $\\Box$! زیرا ارزش‌دهی $v(p)=1, v(q)=0$ هر دو بند را صادق می‌کند، پس این دو بند به هیچ وجه ناسازگار نیستند!</p>
</div>

<h2 id="w10-c-unification-robinson">۲. الگوریتم یکسان‌سازی رابینسون (MGU)</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۱۰.۲ — جایگزینی یکسان‌ساز و MGU</div>
  <p>دو ترم $t_1$ و $t_2$ یکسان‌پذیرند اگر جانشانی $\sigma$ وجود داشته باشد به طوری که $t_1\sigma = t_2\sigma$. فراگیرترین یکسان‌ساز (mgu) جانشانی پایه‌ای است که هر جانشانی یکسان‌ساز دیگر، نمونه‌ای از آن باشد.</p>
</div>

<div class="box box-method">
  <div class="box-title">قواعد سیستم معادلات الگوریتم رابینسون</div>
  <ul>
    <li><strong>حذف اتحاد (Delete):</strong> معادله تکراری $\{t \doteq t\}$ بدون اثر حذف می‌شود.</li>
    <li><strong>تجزیه (Decomposition):</strong> $\{f(u_1, \dots, u_n) \doteq f(v_1, \dots, v_n)\} \implies \{u_1 \doteq v_1, \dots, u_n \doteq v_n\}$.</li>
    <li><strong>تضاد نماد (Clash):</strong> $\{f(\dots) \doteq g(\dots)\} \implies$ <strong>شکست قطعی</strong>.</li>
    <li><strong>جهت‌دهی (Orient):</strong> تبدیل $\{t \doteq x\}$ به $\{x \doteq t\}$ در حالتی که $t$ متغیر نباشد.</li>
    <li><strong>بررسی رخداد (Occurs Check):</strong> در $\{x \doteq t\}$، اگر متغیر $x$ درون $t$ آمده باشد و $x \neq t$، بلافاصله <strong>شکست</strong> رخ می‌دهد! مثلاً معادله $x \doteq f(x)$ هیچ جواب محدودی ندارد. در غیر این صورت، در تمام معادلات دیگر به جای $x$ عبارت $t$ را قرار می‌دهیم.</li>
  </ul>
</div>

<h2 id="w10-c-prolog-intro">۳. برنامه‌نویسی منطقی پرولوگ و بندهای هورن</h2>
<div class="box box-definition">
  <div class="box-title">تعریف ۱۰.۳ — بندهای هورن در پرولوگ</div>
  <p>یک <strong>بند هورن (Horn Clause)</strong> حداکثر شامل یک لیترال مثبت است:</p>
  <ul>
    <li><strong>واقعیت (Fact):</strong> $P(t) \leftarrow$ (بدون لیترال منفی). در پرولوگ: <code>p(t).</code></li>
    <li><strong>قاعده (Rule):</strong> $P(t) \leftarrow Q_1 \land \dots \land Q_n$. در پرولوگ: <code>p(t) :- q1, ..., qn.</code></li>
    <li><strong>پرسش یا هدف (Query/Goal):</strong> $\leftarrow Q_1 \land \dots \land Q_n$. در پرولوگ: <code>?- q1, ..., qn.</code></li>
  </ul>
</div>
"""

# ==============================================================================
# WEEK 10: TD 10 (Exercices 35, 36, 37, 38, 39) (FR & FA)
# ==============================================================================

td10_fr = """
<div class="box box-objectives">
  <div class="box-title">TD Thème 10 — Résolution, Unification & Prolog (Exercices 35 à 39)</div>
  <p>Source : <code>main_td-etudiants.pdf</code>, pages 21–23. Résolution pas à pas de tous les exercices du Thème 10.</p>
</div>

<h2 id="w10-td-ex35">Exercice 35 — Règle de Résolution Propositionnelle (p. 21)</h2>
<div class="box box-solution">
  <div class="box-title">Calcul des Résolvantes</div>
  <ol>
    <li>$C_1 = p \lor r$ et $C_2 = \neg p \lor \neg s \lor t$ sur le pivot $p$ :<br>
    $$\text{Res}(C_1, C_2) = r \lor \neg s \lor t$$</li>
    <li>$C_1 = p \lor q \lor r$ et $C_2 = p \lor \neg q \lor s \lor \neg t$ sur le pivot $q$ :<br>
    $$\text{Res}(C_1, C_2) = p \lor r \lor s \lor \neg t$$</li>
    <li>$C_1 = p \lor q$ et $C_2 = \neg p \lor \neg q \lor s$ :<br>
    Sur le pivot $p$ : $\text{Res} = q \lor \neg q \lor s \equiv \top$ (tautologie triviale).<br>
    Sur le pivot $q$ : $\text{Res} = p \lor \neg p \lor s \equiv \top$.</li>
    <li>$C_1 = p \lor q \lor \neg r$ et $C_2 = p \lor q \lor r$ sur $r$ :<br>
    $$\text{Res}(C_1, C_2) = p \lor q$$</li>
    <li>$C_1 = p$ et $C_2 = \neg p \lor r \lor s$ sur $p$ :<br>
    $$\text{Res}(C_1, C_2) = r \lor s$$</li>
    <li>$C_1 = p$ et $C_2 = \neg p$ sur $p$ :<br>
    $$\text{Res}(C_1, C_2) = \Box \quad \text{(la clause vide, contradiction prouvée !)}$$</li>
  </ol>
</div>

<h2 id="w10-td-ex36">Exercice 36 — Diagnostic Médical par Résolution (p. 21)</h2>
<div class="box box-solution">
  <div class="box-title">Mise en Clauses & Preuve par Réfutation</div>
  <p><strong>Variables :</strong> $G$ (grippe), $T$ (tamiflu), $F$ (fièvre), $K$ (toux), $S$ (sup38).</p>
  <p><strong>Clauses de la base de connaissances :</strong></p>
  <ul>
    <li>$F \iff S \implies (\neg F \lor S)$ et $(\neg S \lor F)$.</li>
    <li>$G \implies T \implies (\neg G \lor T)$.</li>
    <li>$(F \land K) \implies G \implies (\neg F \lor \neg K \lor G)$.</li>
    <li>Faits : $K$ et $S$.</li>
  </ul>
  <p><strong>But à prouver :</strong> Le patient doit prendre du tamiflu ($T$). Pour réfuter, on ajoute la négation du but : $\neg T$.</p>
  <p><strong>Dérivation par résolution :</strong></p>
  <ol>
    <li>$\text{Res}(S, \neg S \lor F) \implies F$.</li>
    <li>$\text{Res}(F, \neg F \lor \neg K \lor G) \implies \neg K \lor G$.</li>
    <li>$\text{Res}(K, \neg K \lor G) \implies G$.</li>
    <li>$\text{Res}(G, \neg G \lor T) \implies T$.</li>
    <li>$\text{Res}(T, \neg T) \implies \Box$.</li>
  </ol>
  <p>La clause vide $\Box$ est obtenue. Par conséquent, la négation du but est insatisfiable avec la base, ce qui démontre rigoureusement que le patient doit prendre du tamiflu !</p>
</div>

<h2 id="w10-td-ex37">Exercice 37 — Résolution LPPO et Unification (p. 21-22)</h2>
<div class="box box-solution">
  <div class="box-title">Calcul des Résolvantes avec MGU de Robinson</div>
  <ol>
    <li>$C_1 = p(x, y, z) \lor \neg q(x, y) \lor \neg q(y, z)$ et $C_2 = \neg p(a, u, b)$ :<br>
    Unification de $p(x, y, z)$ et $p(a, u, b)$ : $\sigma = \{x \mapsto a, y \mapsto u, z \mapsto b\}$.<br>
    <strong>Résolvante :</strong> $(\neg q(x, y) \lor \neg q(y, z))\sigma = \neg q(a, u) \lor \neg q(u, b)$.</li>
    <li>$C_3 = q(x, y) \lor r(y, f(y))$ et $C_4 = \neg q(x', x') \lor s(x') \lor t(g(x'))$ (après renommage de $C_4$) :<br>
    Unification de $q(x, y)$ et $q(x', x')$ : $x \doteq x', y \doteq x' \implies \sigma = \{x \mapsto x', y \mapsto x'\}$.<br>
    <strong>Résolvante :</strong> $r(x', f(x')) \lor s(x') \lor t(g(x'))$.</li>
  </ol>
</div>

<h2 id="w10-td-ex39">Exercice 39 — Arbre de Résolution SLD Prolog (p. 22)</h2>
<div class="box box-solution">
  <div class="box-title">Arbre SLD pour la requête <code>?- p(a, Y, Z).</code></div>
  <p>Base de règles :</p>
  <pre><code>(1) p(X,Y,Z) :- q(X,Y), q(Y,Z).
(2) p(X,Y,X) :- q(b,X), q(Y,a).
(3) q(a,b).  (4) q(b,a).  (5) q(b,c).  (6) q(a,c).</code></pre>
  <p><strong>Déroulement SLD :</strong></p>
  <ul>
    <li>Branche 1 (règle 1 avec $X \mapsto a$) : But résiduel <code>?- q(a, Y), q(Y, Z).</code>
      <ul>
        <li>Avec fait (3) $q(a,b)$, $Y=b$. Nouveau sous-but : <code>?- q(b, Z).</code>
          <ul>
            <li>Avec fait (4) $q(b,a)$ : $Z=a \implies$ <strong>Succès : Y=b, Z=a.</strong></li>
            <li>Avec fait (5) $q(b,c)$ : $Z=c \implies$ <strong>Succès : Y=b, Z=c.</strong></li>
          </ul>
        </li>
        <li>Avec fait (6) $q(a,c)$, $Y=c$. Nouveau sous-but : <code>?- q(c, Z).</code>
          <ul>
            <li>Aucun fait ne commence par $c$ $\implies$ <strong>Échec (Backtracking).</strong></li>
          </ul>
        </li>
      </ul>
    </li>
    <li>Branche 2 (règle 2 avec $X \mapsto a$) : Unifie $p(a, Y, a)$ avec $Z=a$. But résiduel : <code>?- q(b, a), q(Y, a).</code>
      <ul>
        <li><code>q(b,a)</code> est immédiatement résolu par le fait (4). Reste <code>?- q(Y, a).</code>
          <ul>
            <li>Résolu par le fait (4) avec $Y=b \implies$ <strong>Succès : Y=b, Z=a.</strong></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</div>
"""

td10_fa = """
<div class="box box-objectives">
  <div class="box-title">حل تمرینات موضوع ۱۰ — تفکیک، یکسان‌سازی و پرولوگ (تمرین‌های ۳۵ تا ۳۹)</div>
  <p>منبع رسمی: <code>main_td-etudiants.pdf</code>، صفحات ۲۱ تا ۲۳. تحلیل کامل گام‌به‌گام تفکیک گزاره‌ای، الگوریتم رابینسون و درخت‌های SLD.</p>
</div>

<h2 id="w10-td-ex35">تمرین ۳۵ — قاعده تفکیک گزاره‌ای (صفحه ۲۱)</h2>
<div class="box box-solution">
  <div class="box-title">محاسبه تفکیک‌یافته‌ها (Resolvents)</div>
  <ol>
    <li>$C_1 = p \lor r$ و $C_2 = \neg p \lor \neg s \lor t$ با متغیر محوری $p$:<br>
    $$\text{Res}(C_1, C_2) = r \lor \neg s \lor t$$</li>
    <li>$C_1 = p \lor q \lor r$ و $C_2 = p \lor \neg q \lor s \lor \neg t$ روی $q$:<br>
    $$\text{Res}(C_1, C_2) = p \lor r \lor s \lor \neg t$$</li>
    <li>$C_1 = p \lor q$ و $C_2 = \neg p \lor \neg q \lor s$:<br>
    اگر روی $p$ تفکیک کنیم: $q \lor \neg q \lor s \equiv \top$ (همیشه‌درست و بی‌اثر). حذف همزمان هر دو اکیداً غلط است!</li>
    <li>$C_1 = p \lor q \lor \neg r$ و $C_2 = p \lor q \lor r$ روی $r$:<br>
    $$\text{Res}(C_1, C_2) = p \lor q$$</li>
    <li>$C_1 = p$ و $C_2 = \neg p$ روی $p$:<br>
    $$\text{Res}(C_1, C_2) = \Box \quad \text{(بند پوچ؛ اثبات ناسازگاری و تناقض!)}$$</li>
  </ol>
</div>

<h2 id="w10-td-ex36">تمرین ۳۶ — تشخیص پزشکی با روش تفکیک (صفحه ۲۱)</h2>
<div class="box box-solution">
  <div class="box-title">تبدیل به بندها و اثبات به روش تناقض</div>
  <p>هدف اثبات لزوم مصرف تامیفلو ($T$) توسط بیمار است. نقیض هدف یعنی $\neg T$ را به پایگاه دانش اضافه می‌کنیم و تفکیک متوالی انجام می‌دهیم تا به بند پوچ $\Box$ برسیم:</p>
  <ul>
    <li>تفکیک $S$ با $\neg S \lor F$ منجر به تب ($F$) می‌شود.</li>
    <li>تفکیک $F$ و سرفه ($K$) با قاعده ابتلا به آنفولانزا منجر به $G$ (گریپ) می‌شود.</li>
    <li>تفکیک $G$ با $\neg G \lor T$ نتیجه می‌دهد بیمار باید داروی تامیفلو ($T$) مصرف کند.</li>
    <li>در نهایت تفکیک $T$ با نقیض هدف ($\neg T$) بند پوچ $\Box$ را تولید می‌کند که اثبات را کامل می‌سازد!</li>
  </ul>
</div>

<h2 id="w10-td-ex39">تمرین ۳۹ — درخت تفکیک SLD در پرولوگ (صفحه ۲۲)</h2>
<div class="box box-solution">
  <div class="box-title">تحلیل درخت اجرای پرولوگ برای پرسش <code>?- p(a, Y, Z).</code></div>
  <p>پرولوگ از اولین قاعده شروع می‌کند و زیرهدف‌های <code>q(a, Y)</code> و <code>q(Y, Z)</code> را بررسی می‌کند. با حقیقت <code>q(a,b)</code> مقدار $Y=b$ یکسان می‌شود و برای زیرهدف دوم مقادیر $Z=a$ و $Z=c$ حاصل می‌گردد. با حقیقت <code>q(a,c)</code> چون هیچ واقعیتی با حرف $c$ آغاز نمی‌شود، جستجو با شکست (Fail) مواجه شده و عقب‌گرد (Backtracking) صورت می‌گیرد.</p>
</div>
"""

# ==============================================================================
# WEEK 10: TP 10 (Exercices 16, 17, 18) (FR & FA)
# ==============================================================================

tp10_fr = """
<div class="box box-objectives">
  <div class="box-title">TP Thème 10 — Découverte de SWI-Prolog (Exercices 16, 17 et 18)</div>
  <p>Source : <code>main_tp-etudiants.pdf</code>, pages 15–18. Prise en main pratique du langage Prolog.</p>
</div>

<h2 id="w10-tp-ex16">Exercice 16 — Premières requêtes Prolog</h2>
<p>On crée un fichier <code>exercice0.pl</code> contenant les faits :</p>
<pre><code>toto(a, b).
toto(c, b).</code></pre>
<p>Dans l'interpréteur :</p>
<ul>
  <li>Chargement : <code>?- [exercice0].</code></li>
  <li>Requête avec variable majuscule : <code>?- toto(X, b).</code><br>
  Prolog répond d'abord <code>X = a</code>. En appuyant sur <code>;</code> (point-virgule), Prolog cherche par backtracking la solution suivante : <code>X = c</code>.</li>
</ul>

<h2 id="w10-tp-ex17">Exercice 17 — Arbre Généalogique des Simpson</h2>
<pre><code>% Définition des règles familiales
parent(X, Y) :- pere(X, Y).
parent(X, Y) :- mere(X, Y).

grandPere(X, Y) :- pere(X, Z), parent(Z, Y).
frere(X, Y) :- parent(Z, X), parent(Z, Y), homme(X), X \\= Y.</code></pre>

<h2 id="w10-tp-ex18">Exercice 18 — Parcours de Graphe Orienté Sans Cycle</h2>
<pre><code>arc(a, b). arc(a, c). arc(b, d). arc(c, d). arc(d, e).

% Nœuds immédiatement intermédiaires
entre(X, S, D) :- arc(S, X), arc(X, D).

% Accessibilité transitive
accessible(X, Y) :- arc(X, Y).
accessible(X, Y) :- arc(X, Z), accessible(Z, Y).</code></pre>
"""

tp10_fa = """
<div class="box box-objectives">
  <div class="box-title">کار عملی موضوع ۱۰ — شروع کار با SWI-Prolog (تمرین‌های ۱۶، ۱۷ و ۱۸)</div>
  <p>منبع رسمی: <code>main_tp-etudiants.pdf</code>، صفحات ۱۵ تا ۱۸. پیاده‌سازی کاربردی حقایق، قوانین و بازگشت در پرولوگ.</p>
</div>

<h2 id="w10-tp-ex16">تمرین ۱۶ — نخستین پرسش‌ها در پرولوگ</h2>
<p>پرولوگ تمایز کلیدی قائل است: شناسه‌هایی که با حروف کوچک آغاز می‌شوند ثابت (Constant) هستند و شناسه‌های با حروف بزرگ متغیر (Variable) به شمار می‌آیند. با زدن کلید <code>;</code> پس از هر پاسخ، موتور استنتاج پرولوگ با مکانیزم عقب‌گرد (Backtracking) به دنبال شاخه‌های دیگر درخت SLD می‌رود.</p>

<h2 id="w10-tp-ex17">تمرین ۱۷ — روابط خانوادگی سیمپسون‌ها</h2>
<pre><code>parent(X, Y) :- pere(X, Y).
parent(X, Y) :- mere(X, Y).

grandPere(X, Y) :- pere(X, Z), parent(Z, Y).
frere(X, Y) :- parent(Z, X), parent(Z, Y), homme(X), X \\= Y.</code></pre>

<h2 id="w10-tp-ex18">تمرین ۱۸ — پیمایش گراف جهت‌دار بدون دور</h2>
<pre><code>arc(a, b). arc(a, c). arc(b, d). arc(c, d). arc(d, e).

entre(X, S, D) :- arc(S, X), arc(X, D).

accessible(X, Y) :- arc(X, Y).
accessible(X, Y) :- arc(X, Z), accessible(Z, Y).</code></pre>
"""

# ==============================================================================
# WEEK 10: ANNALES (FR & FA)
# ==============================================================================

ann10_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales & Sujets Types — Semaine 10 (Résolution & Unification)</div>
  <p>Les examens écrits finaux de Sorbonne Université se concentrent sur les thèmes 1 à 9, tandis que la résolution et Prolog sont évalués en contrôle continu (TME noté et devoirs surveillés). Voici les exercices types d'évaluation.</p>
</div>

<h2 id="w10-ann-ex1">Exercice Type 1 — Unification de Robinson avec Occurs Check</h2>
<div class="box box-enonce">
  <div class="box-title">Énoncé</div>
  <p>Appliquer l'algorithme de Robinson pour trouver le mgu du système :</p>
  $$\\{ f(x, g(y)) \\doteq f(h(z), x), \\quad y \\doteq a \\}$$
</div>
<div class="box box-solution">
  <div class="box-title">Correction</div>
  <p>1. Décomposition sur $f$ : $x \doteq h(z)$ et $g(y) \doteq x$.</p>
  <p>2. Remplacement de $x$ par $h(z)$ : $g(y) \doteq h(z)$.</p>
  <p>3. Clash entre les symboles de fonction $g$ et $h$ : <strong>ÉCHEC d'unification !</strong></p>
</div>
"""

ann10_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات امتحانی — هفته ۱۰ (تفکیک و یکسان‌سازی)</div>
  <p>موضوعات تفکیک و پرولوگ در دانشگاه سوربن بیشتر در آزمون‌های کنترل مستمر و جلسات عملی کامپیوتر ارزیابی می‌شوند. در ادامه مسائل استاندارد امتحانی آورده شده است.</p>
</div>

<h2 id="w10-ann-ex1">مسأله نمونه ۱ — یکسان‌سازی رابینسون همراه با Occurs Check</h2>
<div class="box box-enonce">
  <div class="box-title">صورت مسأله</div>
  <p>محاسبه MGU به روش رابینسون برای سیستم معادلات زیر:</p>
  $$\\{ f(x, g(y)) \\doteq f(h(z), x), \\quad y \\doteq a \\}$$
</div>
<div class="box box-solution">
  <div class="box-title">پاسخ تشریحی</div>
  <p>پس از تجزیه تابع $f$ به معادلات $x \doteq h(z)$ و $g(y) \doteq x$، با جایگذاری $x$ به معادله $g(y) \doteq h(z)$ می‌رسیم. به دلیل تناقض در نماد تابع سربرگ ($g$ در برابر $h$)، الگوریتم فوراً با شکست مواجه می‌شود و هیچ یکسان‌سازی وجود ندارد.</p>
</div>
"""

# ==============================================================================
# WEEK 10: REVISION (FR & FA)
# ==============================================================================

rev10_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Révision — Semaine 10</div>
  <ul>
    <li><strong>Règle de résolution :</strong> Éliminer un seul littéral complémentaire à la fois !</li>
    <li><strong>Occurs Check :</strong> $x \doteq f(x)$ est impossible en logique formelle standard.</li>
    <li><strong>Prolog :</strong> Évalue les buts de gauche à droite et explore les règles de haut en bas avec retour arrière (DFS/backtracking).</li>
  </ul>
</div>
"""

rev10_fa = """
<div class="box box-objectives">
  <div class="box-title">خلاصه مرور و جمع‌بندی — هفته ۱۰</div>
  <ul>
    <li><strong>قاعده تفکیک:</strong> در هر گام فقط یک جفت لیترال مکمل حذف می‌شود؛ هرگز دو متغیر را همزمان حذف نکنید!</li>
    <li><strong>بررسی رخداد (Occurs Check):</strong> قرار دادن یک متغیر برابر با تابعی شامل همان متغیر ($x \doteq f(x)$) غیرمجاز است.</li>
    <li><strong>پرولوگ:</strong> اهداف را از چپ به راست و قوانین را از بالا به پایین با جستجوی عمق‌اول و عقب‌گرد بررسی می‌کند.</li>
  </ul>
</div>
"""

# Build week 10 bundles
make_bundle('w10_cours', 'fr', c10_fr)
make_bundle('w10_cours', 'fa', c10_fa)
make_bundle('w10_td', 'fr', td10_fr)
make_bundle('w10_td', 'fa', td10_fa)
make_bundle('w10_tp', 'fr', tp10_fr)
make_bundle('w10_tp', 'fa', tp10_fa)
make_bundle('w10_annales', 'fr', ann10_fr)
make_bundle('w10_annales', 'fa', ann10_fa)
make_bundle('w10_revision', 'fr', rev10_fr)
make_bundle('w10_revision', 'fa', rev10_fa)

print("Week 10 generation complete!")

