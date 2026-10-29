import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 2: COURS (FR & FA)
# ==============================================================================

cours_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 2</div>
  <ul>
    <li>Maîtriser la notion sémantique de valuation et de modèle d'une formule.</li>
    <li>Distinguer sans la moindre hésitation : formule satisfiable, valide (tautologie), et insatisfiable (antilogie).</li>
    <li>Comprendre et appliquer la notion de conséquence sémantique ($F \\models G$ et $\\Sigma \\models G$).</li>
    <li>Savoir réfuter une conséquence sémantique ou une équivalence en exhibant un <strong>contre-modèle</strong>.</li>
    <li>Démontrer des équivalences logiques par le calcul algébrique pur, <strong>sans table de vérité</strong>.</li>
    <li>Maîtriser les lois fondamentales de l'algèbre de Boole : absorption, distributivité, De Morgan, idempotence.</li>
  </ul>
</div>

<h2 id="w02-c-semantique">1. Sémantique : Valuations et Modèles</h2>
<p>
La syntaxe décrit la forme des formules ; la <strong>sémantique</strong> leur donne un sens en calculant leur valeur de vérité dans un monde donné.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 2.1 — Valuation et Valeur de Vérité ($[F]_v$)</div>
  <p>Une <strong>valuation</strong> est une application $v : \\mathcal{V} \\to \\{0, 1\\}$ qui associe à chaque variable propositionnelle une valeur de vérité.</p>
  <p>La valeur de vérité $[F]_v \\in \\{0, 1\\}$ d'une formule $F$ sous la valuation $v$ est définie récursivement par :</p>
  <ul>
    <li>$[p]_v = v(p)$ pour tout atome $p \\in \\mathcal{V}$ ;</li>
    <li>$[\\top]_v = 1$ et $[\\bot]_v = 0$ ;</li>
    <li>$[\\neg F]_v = 1 - [F]_v$ ;</li>
    <li>$[F_1 \\land F_2]_v = \\min([F_1]_v, [F_2]_v)$ (vaut 1 si et seulement si $[F_1]_v = 1$ et $[F_2]_v = 1$) ;</li>
    <li>$[F_1 \\lor F_2]_v = \\max([F_1]_v, [F_2]_v)$ (vaut 1 dès qu'au moins l'une des sous-formules vaut 1) ;</li>
    <li>$[F_1 \\Rightarrow F_2]_v = \\max(1 - [F_1]_v, [F_2]_v)$ (vaut 0 si $[F_1]_v=1$ et $[F_2]_v=0$, 1 sinon) ;</li>
    <li>$[F_1 \\Leftrightarrow F_2]_v = 1$ si $[F_1]_v = [F_2]_v$, et 0 sinon.</li>
  </ul>
  <p>Si $[F]_v = 1$, on dit que la valuation $v$ <strong>satisfait</strong> $F$, ou que $v$ est un <strong>modèle</strong> de $F$ (noté $v \\models F$).</p>
</div>

<h2 id="w02-c-taxonomie">2. Taxonomie Sémantique : Satisfiable, Valide, Insatisfiable</h2>

<div class="box box-definition">
  <div class="box-title">Définition 2.2 — Classification des Formules</div>
  <table class="truth-table">
    <thead><tr><th>Concept</th><th>Condition Mathématique</th><th>Intuition</th></tr></thead>
    <tbody>
      <tr><td><strong>Satisfiable</strong></td><td>$\\exists v, [F]_v = 1$</td><td>Possède <em>au moins un</em> modèle dans sa table de vérité.</td></tr>
      <tr><td><strong>Valide (Tautologie)</strong></td><td>$\\forall v, [F]_v = 1$ (noté $\\models F$)</td><td>Vraie dans <em>tous</em> les mondes possibles (toute valuation est un modèle).</td></tr>
      <tr><td><strong>Insatisfiable (Antilogie)</strong></td><td>$\\forall v, [F]_v = 0$</td><td>Ne possède <em>aucun</em> modèle (fausse partout).</td></tr>
      <tr><td><strong>Contingente</strong></td><td>Satisfiable mais non valide</td><td>Vraie sur certaines lignes de sa table, fausse sur d'autres.</td></tr>
    </tbody>
  </table>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — Satisfiable n'implique pas Valide !</div>
  <p><strong>Erreur fréquente :</strong> Trouver une valuation $v$ où $[F]_v = 1$ et en conclure que $F$ est une tautologie.</p>
  <p><strong>Règle de correction :</strong> Pour prouver qu'une formule est <em>satisfiable</em>, UN SEUL exemple (modèle) suffit. Mais pour prouver qu'une formule est <em>valide</em>, il faut prouver qu'elle vaut 1 pour TOUTES les valuations possibles. Un seul contre-exemple où $[F]_v = 0$ détruit la validité !</p>
</div>

<h2 id="w02-c-consequence">3. Conséquence Sémantique et Contre-modèles</h2>

<div class="box box-definition">
  <div class="box-title">Définition 2.3 — Conséquence Sémantique ($F \\models G$)</div>
  <p>Une formule $G$ est conséquence sémantique d'une formule $F$ (noté $F \\models G$) si et seulement si tout modèle de $F$ est un modèle de $G$ :</p>
  $$\\forall v, \\quad [F]_v = 1 \\implies [G]_v = 1$$
  <p>Pour un ensemble de prémisses $\\Sigma = \\{F_1, \\dots, F_k\\}$, $\\Sigma \\models G$ signifie que toute valuation satisfaisant simultanément chaque formule de $\\Sigma$ satisfait également $G$.</p>
  <p><strong>Théorème de déduction sémantique :</strong> $$F \\models G \\iff \\models (F \\Rightarrow G)$$</p>
</div>

<div class="box box-method">
  <div class="box-title">Méthode de résolution — Prouver ou Réfuter une conséquence sans table</div>
  <ul>
    <li><strong>Pour prouver $F \\models G$ :</strong> On suppose qu'une valuation $v$ rend $F$ vraie ($[F]_v = 1$). On analyse les contraintes que cela impose sur les variables, et on déduit rigoureusement que $[G]_v$ vaut nécessairement 1.</li>
    <li><strong>Pour réfuter $F \\models G$ :</strong> On exhibe un <strong>contre-modèle</strong> explicite : une valuation $v$ telle que $[F]_v = 1$ mais $[G]_v = 0$.</li>
  </ul>
</div>

<h2 id="w02-c-algebre">4. Lois de l'Algèbre de Boole et Démonstrations Algébriques</h2>
<p>
Lorsqu'un énoncé stipule <em>« sans utiliser de table de vérité »</em>, la seule méthode autorisée est l'application pas à pas des équivalences algébriques.
</p>

<div class="box box-definition">
  <div class="box-title">Tableau des 12 Lois Fondamentales de l'Algèbre Booléenne</div>
  <table class="truth-table">
    <thead><tr><th>Nom de la Règle</th><th>Formulation Conjonctive</th><th>Formulation Disjonctive</th></tr></thead>
    <tbody>
      <tr><td>Idempotence</td><td>$A \\land A \\equiv A$</td><td>$A \\lor A \\equiv A$</td></tr>
      <tr><td>Commutativité</td><td>$A \\land B \\equiv B \\land A$</td><td>$A \\lor B \\equiv B \\lor A$</td></tr>
      <tr><td>Associativité</td><td>$(A \\land B) \\land C \\equiv A \\land (B \\land C)$</td><td>$(A \\lor B) \\lor C \\equiv A \\lor (B \\lor C)$</td></tr>
      <tr><td>Distributivité</td><td>$A \\land (B \\lor C) \\equiv (A \\land B) \\lor (A \\land C)$</td><td>$A \\lor (B \\land C) \\equiv (A \\lor B) \\land (A \\lor C)$</td></tr>
      <tr><td>Éléments neutres</td><td>$A \\land \\top \\equiv A$</td><td>$A \\lor \\bot \\equiv A$</td></tr>
      <tr><td>Éléments absorbants</td><td>$A \\land \\bot \\equiv \\bot$</td><td>$A \\lor \\top \\equiv \\top$</td></tr>
      <tr><td>Complémentation</td><td>$A \\land \\neg A \\equiv \\bot$ (Contradiction)</td><td>$A \\lor \\neg A \\equiv \\top$ (Tiers Exclu)</td></tr>
      <tr><td>Double négation</td><td>$\\neg \\neg A \\equiv A$</td><td>—</td></tr>
      <tr><td>Lois de De Morgan</td><td>$\\neg(A \\land B) \\equiv \\neg A \\lor \\neg B$</td><td>$\\neg(A \\lor B) \\equiv \\neg A \\land \\neg B$</td></tr>
      <tr><td><strong>Absorption</strong></td><td>$A \\land (A \\lor B) \\equiv A$</td><td><strong>$A \\lor (A \\land B) \\equiv A$</strong></td></tr>
      <tr><td>Élimination Implication</td><td>$A \\Rightarrow B \\equiv \\neg A \\lor B$</td><td>$\\neg(A \\Rightarrow B) \\equiv A \\land \\neg B$</td></tr>
      <tr><td>Élimination Équivalence</td><td>$A \\Leftrightarrow B \\equiv (A \\Rightarrow B) \\land (B \\Rightarrow A)$</td><td>$A \\Leftrightarrow B \\equiv (A \\land B) \\lor (\\neg A \\land \\neg B)$</td></tr>
    </tbody>
  </table>
</div>
"""

cours_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۲</div>
  <ul>
    <li>تسلط عمیق بر مفهوم معنایی ارزش‌گذاری (Valuation) و مدل (Modèle) فرمول.</li>
    <li>تشخیص دقیق سه وضعیت منطقی: فرمول صدق‌پذیر (Satisfiable)، معتبر/تاتولوژی (Valide)، و ناپذیرفتنی (Insatisfiable).</li>
    <li>درک مفهوم پیامد معنایی ($F \\models G$ و $\\Sigma \\models G$) و ارتباط آن با استدلال معتبر.</li>
    <li>ابطال ادعاهای پیامد یا هم‌ارزی با ارائه <strong>مثال نقض (Contre-modèle)</strong> دقیق و عددی.</li>
    <li>اثبات هم‌ارزی‌های منطقی به روش جبری نمادین، <strong>اکیداً بدون استفاده از جدول درستی</strong>.</li>
    <li>تسلط بر قوانین ۱۲گانه جبر بولی: جذب (Absorption)، توزیع‌پذیری، دمورگان و حذف شرطی.</li>
  </ul>
</div>

<h2 id="w02-c-semantique">۱. معناشناسی: ارزش‌گذاری‌ها و مدل‌ها</h2>
<p>
نحو شکل ظاهری فرمول را تعیین می‌کند، اما <strong>معناشناسی (Sémantique)</strong> ارزش درستی فرمول را در یک دنیای فرضی مشخص می‌سازد.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۲.۱ — ارزش‌گذاری و محاسبه ارزش فرمول ($[F]_v$)</div>
  <p>یک <strong>ارزش‌گذاری (Valuation)</strong> تابعی است به صورت $v : \\mathcal{V} \\to \\{0, 1\\}$ که به هر متغیر گزاره‌ای یک ارزش درستی (۰ یا ۱) نسبت می‌دهد.</p>
  <p>ارزش درستی یک فرمول مرکب $[F]_v$ به صورت بازگشتی بر روی ساختار فرمول محاسبه می‌شود:</p>
  <ul>
    <li>برای اتم‌ها: $[p]_v = v(p)$؛</li>
    <li>برای ثابت‌ها: $[\\top]_v = 1$ و $[\\bot]_v = 0$؛</li>
    <li>برای نقیض: $[\\neg F]_v = 1 - [F]_v$؛</li>
    <li>برای عطف: $[F_1 \\land F_2]_v = \\min([F_1]_v, [F_2]_v)$؛</li>
    <li>برای فصل: $[F_1 \\lor F_2]_v = \\max([F_1]_v, [F_2]_v)$؛</li>
    <li>برای شرطی: $[F_1 \\Rightarrow F_2]_v = 1$ به جز حالتی که $[F_1]_v=1$ و $[F_2]_v=0$ باشد که در آن صورت مقدار 0 می‌گیرد؛</li>
    <li>برای دوشرطی: $[F_1 \\Leftrightarrow F_2]_v = 1$ اگر و تنها اگر $[F_1]_v = [F_2]_v$.</li>
  </ul>
  <p>اگر $[F]_v = 1$ باشد، می‌گوییم ارزش‌گذاری $v$ فرمول $F$ را ارضا می‌کند و به $v$ یک <strong>مدل (Modèle)</strong> برای $F$ می‌گویند (نماد: $v \\models F$).</p>
</div>

<h2 id="w02-c-taxonomie">۲. رده‌بندی معنایی: صدق‌پذیر، معتبر، ناپذیرفتنی</h2>

<div class="box box-definition">
  <div class="box-title">تعریف ۲.۲ — رده‌بندی وضعیت صدق فرمول‌ها</div>
  <table class="truth-table">
    <thead><tr><th>اصطلاح</th><th>شرط صوری ریاضی</th><th>شهود و مفهوم</th></tr></thead>
    <tbody>
      <tr><td><strong>صدق‌پذیر (Satisfiable)</strong></td><td>$\\exists v, [F]_v = 1$</td><td>حداقل یک سطر با مقدار ۱ در جدول درستی دارد (حداقل یک مدل دارد).</td></tr>
      <tr><td><strong>معتبر / تاتولوژی (Valide)</strong></td><td>$\\forall v, [F]_v = 1$ (نماد: $\\models F$)</td><td>در تمام سطرها مقدار ۱ دارد و در هر دنیای ممکنی درست است.</td></tr>
      <tr><td><strong>ناپذیرفتنی / تناقض (Insatisfiable)</strong></td><td>$\\forall v, [F]_v = 0$</td><td>هیچ مدلی ندارد و در تمام سطرها مقدار ۰ می‌گیرد.</td></tr>
      <tr><td><strong>مشروط / ممکن (Contingente)</strong></td><td>صدق‌پذیر ولی نامعتبر</td><td>در برخی سطرها ۱ و در برخی دیگر ۰ است.</td></tr>
    </tbody>
  </table>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — صدق‌پذیری دلیلی بر اعتبار نیست!</div>
  <p><strong>اشتباه پرتکرار:</strong> پیدا کردن یک ارزش‌گذاری که در آن $[F]_v = 1$ می‌شود و نتیجه‌گیری شتاب‌زده مبنی بر اینکه فرمول تاتولوژی است!</p>
  <p><strong>روش اصلاح:</strong> برای اثبات <em>صدق‌پذیری</em>، ارائه یک مثال منفرد (یک مدل) کافی است. اما برای اثبات <em>اعتبار</em>، باید فرمول برای تمام $2^n$ حالت ممکن درست باشد. پیدا کردن حتی یک حالت که در آن فرمول ۰ شود، اعتبار آن را باطل می‌کند.</p>
</div>

<h2 id="w02-c-consequence">۳. پیامد معنایی و روش مثال نقض</h2>

<div class="box box-definition">
  <div class="box-title">تعریف ۲.۳ — پیامد معنایی ($F \\models G$)</div>
  <p>گزاره $G$ پیامد معنایی $F$ است (نماد: $F \\models G$) اگر و فقط اگر هر مدلی برای $F$، مدلی برای $G$ نیز باشد:</p>
  $$\\forall v, \\quad [F]_v = 1 \\implies [G]_v = 1$$
  <p><strong>قضیه استنتاج معنایی:</strong> $$F \\models G \\iff \\models (F \\Rightarrow G)$$</p>
</div>

<div class="box box-method">
  <div class="box-title">روش گام به گام — اثبات یا رد پیامد معنایی بدون جدول</div>
  <ul>
    <li><strong>برای اثبات $F \\models G$:</strong> فرض می‌کنیم ارزش‌گذاری دلخواهی مانند $v$ داریم که $[F]_v = 1$ است. از این فرض محدودیت‌های مقادیر متغیرها را استخراج کرده و منطقاً اثبات می‌کنیم که $[G]_v$ هم الزاماً باید ۱ شود.</li>
    <li><strong>برای رد $F \\models G$:</strong> یک <strong>مثال نقض (Contre-modèle)</strong> صریح ارائه می‌دهیم: ارزش‌گذاری‌ای که در آن $[F]_v = 1$ اما $[G]_v = 0$ شود.</li>
  </ul>
</div>

<h2 id="w02-c-algebre">۴. قوانین ۱۲گانه جبر بولی و اثبات جبری</h2>
<p>
هنگامی که در سؤال نوشته شده است <em>«بدون رسم جدول درستی»</em>، تنها روش مجاز استفاده خط‌به‌خط از هم‌ارزی‌های جبری زیر است:
</p>

<div class="box box-definition">
  <div class="box-title">جدول قوانین بنیادین جبر بولی</div>
  <table class="truth-table">
    <thead><tr><th>نام قاعده</th><th>حالت عطفی</th><th>حالت فصلی</th></tr></thead>
    <tbody>
      <tr><td>قاعده جذب (Absorption)</td><td>$A \\land (A \\lor B) \\equiv A$</td><td><strong>$A \\lor (A \\land B) \\equiv A$</strong></td></tr>
      <tr><td>توزیع‌پذیری (Distributivité)</td><td>$A \\land (B \\lor C) \\equiv (A \\land B) \\lor (A \\land C)$</td><td>$A \\lor (B \\land C) \\equiv (A \\lor B) \\land (A \\lor C)$</td></tr>
      <tr><td>قوانین دمورگان</td><td>$\\neg(A \\land B) \\equiv \\neg A \\lor \\neg B$</td><td>$\\neg(A \\lor B) \\equiv \\neg A \\land \\neg B$</td></tr>
      <tr><td>حذف شرطی</td><td>$A \\Rightarrow B \\equiv \\neg A \\lor B$</td><td>$\\neg(A \\Rightarrow B) \\equiv A \\land \\neg B$</td></tr>
      <tr><td>طرد شق ثالث و تناقض</td><td>$A \\land \\neg A \\equiv \\bot$</td><td>$A \\lor \\neg A \\equiv \\top$</td></tr>
    </tbody>
  </table>
</div>
"""

make_bundle("w02_cours", "fr", cours_fr)
make_bundle("w02_cours", "fa", cours_fa)

# ==============================================================================
# WEEK 2: TD (FR & FA) - Exercices 4 à 8 de main_td-etudiants.pdf
# ==============================================================================

td_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de TD 2 — Solutions Officielles Intégrales & Justifications</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 4–6, Thème 2, Exercices 4 à 8). <strong>Consigne impérative : Pour répondre aux exercices de ce thème, vous ne devez PAS utiliser de table de vérité.</strong></p>
</div>

<div id="td-exo4-container"></div>
<div id="td-exo5-container"></div>
<div id="td-exo6-container"></div>
<div id="td-exo7-container"></div>
<div id="td-exo8-container"></div>
"""

td_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه تمرین‌های کلاسی TD 2 — حل تشریحی و گام به گام بدون جدول درستی</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۴ تا ۶، تم ۲، تمرین‌های ۴ تا ۸). <strong>دستور اکید سؤالات: برای پاسخ به سؤالات این تم نباید از جدول درستی استفاده کنید!</strong></p>
</div>

<div id="td-exo4-container"></div>
<div id="td-exo5-container"></div>
<div id="td-exo6-container"></div>
<div id="td-exo7-container"></div>
<div id="td-exo8-container"></div>
"""

td_interactive = """
  // Exercice 4
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo4-container'), {
    id: 'w02_td_ex4',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۴ — فرمول‌های صدق‌پذیر و معتبر بدون جدول' : 'Exercice 4 – Formules satisfiables, valides sans table',
    source: 'main_td-etudiants.pdf (p. 4)',
    theme: lang === 'fa' ? 'تم ۲' : 'Thème 2',
    statement: lang === 'fa' ?
      '<p>بدون استفاده از جدول درستی، تعیین کنید که آیا فرمول‌های زیر صدق‌پذیرند؟ معتبرند؟</p>' +
      '<ol>' +
      '<li>$F_1 = (p \\Rightarrow q) \\lor (q \\Rightarrow p)$</li>' +
      '<li>$F_2 = (p \\Rightarrow q) \\land (p \\land \\neg q)$</li>' +
      '<li>$F_3 = (p \\land q) \\Rightarrow (p \\lor r)$</li>' +
      '</ol>' :
      '<p>Sans utiliser de table de vérité, déterminer si les formules suivantes sont satisfiables, valides ou insatisfiables :</p>' +
      '<ol>' +
      '<li>$F_1 = (p \\Rightarrow q) \\lor (q \\Rightarrow p)$</li>' +
      '<li>$F_2 = (p \\Rightarrow q) \\land (p \\land \\neg q)$</li>' +
      '<li>$F_3 = (p \\land q) \\Rightarrow (p \\lor r)$</li>' +
      '</ol>',
    consigne: lang === 'fa' ?
      'برای اثبات صدق‌پذیری، یک مدل مشخص با مقادیر متغیرها ارائه دهید. برای اثبات اعتبار، یا از تبدیل‌های جبری هم‌ارز به T استفاده کنید یا نشان دهید فرض خلاف (صفر شدن فرمول) به تناقض می‌رسد.' :
      'Pour prouver la satisfiabilité, exhibez une valuation modèle explicite. Pour prouver la validité sans table, appliquez les équivalences vers T ou raisonnez par l\\'absurde en supposant que la formule vaut 0.',
    hint: lang === 'fa' ? 
      'برای F1 از فرمول حذف شرطی استفاده کنید : $p \\Rightarrow q \\equiv \\neg p \\lor q$.' :
      'Pour F1, transformez les implications : $p \\Rightarrow q \\equiv \\neg p \\lor q$ et $q \\Rightarrow p \\equiv \\neg q \\lor p$. Regroupez ensuite avec le tiers exclu.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (تحلیل فرمول F1) :</strong><br>' +
      'تبدیل شرطی‌ها به فصل : $F_1 \\equiv (\\neg p \\lor q) \\lor (\\neg q \\lor p)$.<br>' +
      'جابجایی و شرکت‌پذیری : $F_1 \\equiv (p \\lor \\neg p) \\lor (q \\lor \\neg q)$.<br>' +
      'با قانون طرد شق ثالث : $p \\lor \\neg p \\equiv \\top$.<br>' +
      'بنابراین $F_1 \\equiv \\top \\lor \\top \\equiv \\top$.<br>' +
      'فرمول $F_1$ <strong>معتبر (تاتولوژی)</strong> است (و بنابراین حتماً صدق‌پذیر نیز هست).',
      '<strong>گام ۲ (تحلیل فرمول F2) :</strong><br>' +
      'تبدیل شرطی : $p \\Rightarrow q \\equiv \\neg p \\lor q$.<br>' +
      'بنابراین : $F_2 \\equiv (\\neg p \\lor q) \\land p \\land \\neg q$.<br>' +
      'پخش عطف بر روی فصل : $F_2 \\equiv (\\neg p \\land p \\land \\neg q) \\lor (q \\land p \\land \\neg q)$.<br>' +
      'اما $\\neg p \\land p \\equiv \\bot$ و $q \\land \\neg q \\equiv \\bot$.<br>' +
      'در نتیجه $F_2 \\equiv \\bot \\lor \\bot \\equiv \\bot$.<br>' +
      'فرمول $F_2$ <strong>ناپذیرفتنی (Insatisfiable)</strong> و مسلماً نامعتبر است.',
      '<strong>گام ۳ (تحلیل فرمول F3) :</strong><br>' +
      'تبدیل شرطی : $F_3 \\equiv \\neg(p \\land q) \\lor (p \\lor r)$.<br>' +
      'با قانون دمورگان : $\\neg(p \\land q) \\equiv \\neg p \\lor \\neg q$.<br>' +
      'بنابراین : $F_3 \\equiv (\\neg p \\lor p) \\lor \\neg q \\lor r \\equiv \\top \\lor \\neg q \\lor r \\equiv \\top$.<br>' +
      'فرمول $F_3$ <strong>معتبر (تاتولوژی)</strong> و صدق‌پذیر است.'
    ] : [
      '<strong>Étape 1 (Formule F1) :</strong><br>' +
      'On applique l\\'élimination de l\\'implication : $F_1 \\equiv (\\neg p \\lor q) \\lor (\\neg q \\lor p)$.<br>' +
      'Par associativité et commutativité : $F_1 \\equiv (p \\lor \\neg p) \\lor (q \\lor \\neg q)$.<br>' +
      'Or $p \\lor \\neg p \\equiv \\top$ (tiers exclu), d\\'où $F_1 \\equiv \\top \\lor \\top \\equiv \\top$.<br>' +
      'La formule $F_1$ est <strong>valide</strong> (et donc satisfiable).',
      '<strong>Étape 2 (Formule F2) :</strong><br>' +
      'On a $p \\Rightarrow q \\equiv \\neg(p \\land \\neg q)$.<br>' +
      'En posant $A = (p \\land \\neg q)$, la formule s\\'écrit : $F_2 \\equiv \\neg A \\land A \\equiv \\bot$.<br>' +
      'La formule $F_2$ est une contradiction : elle est <strong>insatisfiable</strong> et non valide.',
      '<strong>Étape 3 (Formule F3) :</strong><br>' +
      'Par élimination de l\\'implication : $F_3 \\equiv \\neg(p \\land q) \\lor (p \\lor r)$.<br>' +
      'Par De Morgan : $F_3 \\equiv (\\neg p \\lor \\neg q) \\lor (p \\lor r) \\equiv (\\neg p \\lor p) \\lor \\neg q \\lor r$.<br>' +
      'Comme $\\neg p \\lor p \\equiv \\top$, on a $F_3 \\equiv \\top \\lor \\neg q \\lor r \\equiv \\top$.<br>' +
      'La formule $F_3$ est <strong>valide</strong>.'
    ],
    justification: lang === 'fa' ?
      'محاسبات صرفاً بر اساس قوانین جبر بولی (دمورگان، طرد شق ثالث، و توزیع‌پذیری) انجام گرفته است.' :
      'Calculs effectués exclusivement par équivalences algébriques reconnues (De Morgan, tiers exclu, distributivité).',
    finalAnswer: lang === 'fa' ?
      '۱. $F_1$ : <strong>معتبر</strong> و صدق‌پذیر.<br>۲. $F_2$ : <strong>ناپذیرفتنی</strong> (تناقض).<br>۳. $F_3$ : <strong>معتبر</strong> و صدق‌پذیر.' :
      '1. $F_1$ : <strong>Valide</strong> et satisfiable.<br>2. $F_2$ : <strong>Insatisfiable</strong>.<br>3. $F_3$ : <strong>Valide</strong> et satisfiable.',
    verification: lang === 'fa' ?
      'برای F1 فرض کنید مقداری صفر شود: برای صفر شدن فصل باید هر دو شرطی صفر شوند، یعنی هم (p=1 و q=0) و هم (q=1 و p=0) که تناقض است.' :
      'Raisonnement sémantique de contrôle : $F_1$ ne pourrait valoir 0 que si ses deux disjonctes valaient 0 simultanément, ce qui exigerait $(p=1, q=0)$ ET $(q=1, p=0)$, ce qui est impossible.',
    trap: lang === 'fa' ?
      'استفاده از جدول درستی در این تمرین تخلف از دستور صریح سؤال است و نمره آن صفر خواهد شد!' :
      'Toute tentative de réponse par tableau de vérité viole la consigne explicite et entraîne 0 point.'
  });

  // Exercice 8 - ChatGPT
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo8-container'), {
    id: 'w02_td_ex8',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۸ — آیا همیشه باید حرف ChatGPT را باور کرد؟' : 'Exercice 8 – Faut-il toujours croire ChatGPT ?',
    source: 'main_td-etudiants.pdf (p. 5)',
    theme: lang === 'fa' ? 'تم ۲' : 'Thème 2',
    statement: lang === 'fa' ?
      '<p>یک دانشجو از چت‌جی‌پی‌تی خواست تا فرمول زیر را ساده کند :</p>' +
      '<p>$$F = (x \\land y) \\lor (z \\land y)$$</p>' +
      '<p>چت‌جی‌پی‌تی ادعا کرد که این فرمول با عبارت زیر هم‌ارز است :</p>' +
      '<p>$$G = (x \\lor y) \\land (z \\lor y)$$</p>' +
      '<p><strong>سؤال ۱ :</strong> آیا ادعای چت‌جی‌پی‌تی درست است ؟ پاسخ خود را با یک مثال نقض (ارزش‌گذاری برای x, y, z) توجیه کنید.<br>' +
      '<strong>سؤال ۲ :</strong> فرمول $F$ را به شکل صحیح و به کمک قوانین جبر بولی ساده کنید.</p>' :
      '<p>Un étudiant a demandé à ChatGPT de simplifier la formule : $$F = (x \\land y) \\lor (z \\land y)$$</p>' +
      '<p>ChatGPT a répondu que cette formule était équivalente à : $$G = (x \\lor y) \\land (z \\lor y)$$</p>' +
      '<p><strong>Question 1 :</strong> L\\'affirmation de ChatGPT est-elle correcte ? Justifier par un contre-exemple (valuation pour $x, y, z$).<br>' +
      '<strong>Question 2 :</strong> Simplifier correctement la formule $F$ en utilisant les lois de l\\'algèbre de Boole.</p>',
    consigne: lang === 'fa' ?
      'برای رد ادعای هم‌ارزی، باید مقادیر دقیقی برای x و y و z بدهید که در آن ارزش F و G متفاوت شود.' :
      'Pour réfuter une équivalence $F \\equiv G$, vous devez fournir une valuation explicite $v$ telle que $[F]_v \\neq [G]_v$.',
    hint: lang === 'fa' ? 
      'مقدار $y=0$ را تست کنید تا ببینید F و G چه مقادیری می‌گیرند.' :
      'Testez la valuation $y=0$, avec $x=1$ et $z=1$.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (یافتن مثال نقض) :</strong><br>' +
      'ارزش‌گذاری $v$ را در نظر بگیرید : $v(x)=1$, $v(y)=0$, $v(z)=1$.<br>' +
      'محاسبه $F$ : $[F]_v = (1 \\land 0) \\lor (1 \\land 0) = 0 \\lor 0 = 0$.<br>' +
      'محاسبه $G$ : $[G]_v = (1 \\lor 0) \\land (1 \\lor 0) = 1 \\land 1 = 1$.<br>' +
      'چون $[F]_v \\neq [G]_v$ است، هم‌ارزی کاملاً <strong>غلط</strong> است!',
      '<strong>گام ۲ (ساده‌سازی صحیح به روش فاکتورگیری/توزیع‌پذیری) :</strong><br>' +
      'در فرمول $F = (x \\land y) \\lor (z \\land y)$، مؤلفه $y$ مشترک است.<br>' +
      'طبق خاصیت توزیع‌پذیری عطف نسبت به فصل :<br>' +
      '$$F \\equiv (x \\lor z) \\land y$$'
    ] : [
      '<strong>Étape 1 (Contre-exemple explicite) :</strong><br>' +
      'Considérons la valuation $v$ définie par : $v(x)=1, v(y)=0, v(z)=1$.<br>' +
      'Évaluation de $F$ : $[F]_v = (1 \\land 0) \\lor (1 \\land 0) = 0 \\lor 0 = 0$.<br>' +
      'Évaluation de $G$ : $[G]_v = (1 \\lor 0) \\land (1 \\lor 0) = 1 \\land 1 = 1$.<br>' +
      'Comme $[F]_v \\neq [G]_v$, la formule $F$ n\\'est PAS équivalente à $G$. ChatGPT s\\'est trompé.',
      '<strong>Étape 2 (Simplification correcte) :</strong><br>' +
      'On applique la distributivité de $\\land$ par rapport à $\\lor$ en factorisant par $y$ :<br>' +
      '$$F = (x \\land y) \\lor (z \\land y) \\equiv (x \\lor z) \\land y$$'
    ],
    justification: lang === 'fa' ?
      'قانون توزیع‌پذیری: $(A \\lor B) \\land C \\equiv (A \\land C) \\lor (B \\land C)$. هوش مصنوعی عملگرهای عطف و فصل را در پرانتزها اشتباهاً معکوس کرده بود.' :
      'Loi de distributivité : $(A \\lor B) \\land C \\equiv (A \\land C) \\lor (B \\land C)$. ChatGPT a confondu les connecteurs internes et externes.',
    finalAnswer: lang === 'fa' ?
      '۱. ادعای چت‌جی‌پی‌تی نادرست است. مثال نقض : $x=1, y=0, z=1$ که در آن $F=0$ ولی $G=1$ می‌شود.<br>' +
      '۲. شکل ساده‌شده صحیح : $$(x \\lor z) \\land y$$' :
      '1. Non, ChatGPT a tort. Contre-exemple : $x=1, y=0, z=1 \\implies [F]_v = 0$ alors que $[G]_v = 1$.<br>' +
      '2. Formule correctement simplifiée : $$(x \\lor z) \\land y$$',
    verification: lang === 'fa' ?
      'بررسی جبری: $(x \\lor z) \\land y \\equiv (x \\land y) \\lor (z \\land y)$ که دقیقاً فرمول اولیه F است.' :
      'En redéveloppant $(x \\lor z) \\land y$, on retrouve exactement $(x \\land y) \\lor (z \\land y)$.',
    trap: lang === 'fa' ?
      'دام رایج: نوشتن $(x+y)\\cdot(z+y)$ بدون توجه به معنای نمادها در جبر بولی که منجر به ایجاد عبارت کاملاً متفاوتی می‌شود.' :
      'Le piège est de manipuler les symboles booléens comme en arithmétique ordinaire en inversant les rôles de l\\'addition et de la multiplication.'
  });
"""

make_bundle("w02_td", "fr", td_fr, td_interactive)
make_bundle("w02_td", "fa", td_fa, td_interactive)

# ==============================================================================
# WEEK 2: TP (FR & FA) - Exercices 3 & 4 de main_tp-etudiants.pdf
# ==============================================================================

tp_fr = """
<div class="box box-objectives">
  <div class="box-title">Laboratoire TP 2 — Valuations, Décideurs Sémantiques & Conséquence en Python</div>
  <p>Source officielle : <code>main_tp-etudiants.pdf</code> (p. 3–5, Thème 1.2.3, Exercices 3 et 4). Ce TP développe les algorithmes de décision sémantique : évaluation sous valuation, génération des $2^n$ mondes possibles, recherche des modèles, et test de conséquence sémantique.</p>
</div>

<h2 id="w02-tp-eval">1. Évaluation sous une valuation donnée (<code>eval_formule</code>)</h2>
<pre><code>def eval_formule(formule: str, valuation: dict[str, bool]) -> bool:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # Feuille : constante ou atome
    if len(sous_formules) == 0:
        if connec == "TRUE":
            return True
        if connec == "FALSE":
            return False
        # C'est un atome : on consulte la valuation
        return valuation[connec]
        
    if connec == "NOT":
        return not eval_formule(sous_formules[0], valuation)
    if connec == "AND":
        return eval_formule(sous_formules[0], valuation) and eval_formule(sous_formules[1], valuation)
    if connec == "OR":
        return eval_formule(sous_formules[0], valuation) or eval_formule(sous_formules[1], valuation)
    if connec == "IMPLIES":
        vg = eval_formule(sous_formules[0], valuation)
        vd = eval_formule(sous_formules[1], valuation)
        return (not vg) or vd
        
    raise ValueError(f"Connecteur inconnu : {connec}")</code></pre>

<h2 id="w02-tp-decideurs">2. Décideurs Sémantiques (<code>is_satisfiable</code>, <code>is_valid</code>, <code>consequence_sem</code>)</h2>
<pre><code>def genere_interpretations(fa: set[str]) -> list[dict[str, bool]]:
    liste_atomes = sorted(list(fa))
    n = len(liste_atomes)
    res = []
    for i in range(1 << n):
        val = {}
        for j in range(n):
            val[liste_atomes[j]] = bool((i >> (n - 1 - j)) & 1)
        res.append(val)
    return res

def is_satisfiable(formule: str) -> bool:
    fa = genere_fa(formule)
    for val in genere_interpretations(fa):
        if eval_formule(formule, val):
            return True # Au moins un modèle trouvé
    return False

def is_valid(formule: str) -> bool:
    fa = genere_fa(formule)
    for val in genere_interpretations(fa):
        if not eval_formule(formule, val):
            return False # Contre-exemple trouvé
    return True

def consequence_sem(f1: str, f2: str) -> bool:
    # F1 |= F2 ssi pour toute valuation où F1 est vraie, F2 est vraie
    fa = genere_fa(f1).union(genere_fa(f2))
    for val in genere_interpretations(fa):
        if eval_formule(f1, val) and not eval_formule(f2, val):
            return False # Contre-modèle trouvé
    return True</code></pre>
"""

tp_fa = """
<div class="box box-objectives">
  <div class="box-title">آزمایشگاه برنامه‌نویسی TP 2 — ارزش‌گذاری‌ها، تصمیم‌گیرهای معنایی و پیامد در پایتون</div>
  <p>منبع رسمی: جزوه <code>main_tp-etudiants.pdf</code> (صفحه ۳ تا ۵، تم ۱.۲.۳، تمرین‌های ۳ و ۴). در این بخش توابع کلیدی تصمیم‌گیری معنایی پیاده‌سازی می‌شوند: ارزیابی تحت دیکشنری مقادیر، تولید $2^n$ حالت، استخراج مدل‌ها و آزمون خودکار پیامد معنایی.</p>
</div>

<h2 id="w02-tp-eval">۱. ارزیابی فرمول تحت یک ارزش‌گذاری مشخص (<code>eval_formule</code>)</h2>
<pre><code>def eval_formule(formule: str, valuation: dict[str, bool]) -> bool:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # حالت برگ: ثابت یا متغیر گزاره‌ای
    if len(sous_formules) == 0:
        if connec == "TRUE":
            return True
        if connec == "FALSE":
            return False
        # متغیر گزاره‌ای است و مقدار آن را از دیکشنری می‌خوانیم
        return valuation[connec]
        
    if connec == "NOT":
        return not eval_formule(sous_formules[0], valuation)
    if connec == "AND":
        return eval_formule(sous_formules[0], valuation) and eval_formule(sous_formules[1], valuation)
    if connec == "OR":
        return eval_formule(sous_formules[0], valuation) or eval_formule(sous_formules[1], valuation)
    if connec == "IMPLIES":
        vg = eval_formule(sous_formules[0], valuation)
        vd = eval_formule(sous_formules[1], valuation)
        return (not vg) or vd
        
    raise ValueError(f"رابط ناشناخته: {connec}")</code></pre>

<h2 id="w02-tp-decideurs">۲. توابع تصمیم‌گیر معنایی (<code>is_satisfiable</code>, <code>is_valid</code>, <code>consequence_sem</code>)</h2>
<pre><code>def genere_interpretations(fa: set[str]) -> list[dict[str, bool]]:
    liste_atomes = sorted(list(fa))
    n = len(liste_atomes)
    res = []
    # تولید ۲ به توان n حالت ممکن
    for i in range(1 << n):
        val = {}
        for j in range(n):
            val[liste_atomes[j]] = bool((i >> (n - 1 - j)) & 1)
        res.append(val)
    return res

def is_satisfiable(formule: str) -> bool:
    fa = genere_fa(formule)
    for val in genere_interpretations(fa):
        if eval_formule(formule, val):
            return True # حداقل یک مدل پیدا شد
    return False

def is_valid(formule: str) -> bool:
    fa = genere_fa(formule)
    for val in genere_interpretations(fa):
        if not eval_formule(formule, val):
            return False # مثال نقض پیدا شد
    return True

def consequence_sem(f1: str, f2: str) -> bool:
    # F1 |= F2 اگر و تنها اگر در هر مدلی از F1، مقدار F2 نیز درست باشد
    fa = genere_fa(f1).union(genere_fa(f2))
    for val in genere_interpretations(fa):
        if eval_formule(f1, val) and not eval_formule(f2, val):
            return False # مثال نقض پیدا شد
    return True</code></pre>
"""

make_bundle("w02_tp", "fr", tp_fr)
make_bundle("w02_tp", "fa", tp_fa)

# ==============================================================================
# WEEK 2: ANNALES & REVISION (FR & FA)
# ==============================================================================

annales_w2_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales d'Examens Ciblées — Semaine 2</div>
  <p>Problèmes réels d'examens portant sur la conséquence sémantique, la recherche de contre-modèles et la preuve sans table de vérité.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">Examen Partiel 2020–2021 — Exercice 2 (Conséquence sémantique)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">Source : partiel_2020_2021_L2.pdf (p. 2)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">Semaine 2</span><span class="badge">Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>Soient les formules $F = (p \\Rightarrow q) \\land (q \\Rightarrow r)$ et $G = p \\Rightarrow r$.</p>
    <p>1. A-t-on $F \\models G$ ? Justifier rigoureusement sans table de vérité.<br>
    2. A-t-on $G \\models F$ ? Justifier rigoureusement.</p>
  </div>
  <div class="step-content">
    <strong>Correction complète rédigée Sorbonne :</strong><br>
    1. <strong>Étude de $F \\models G$ :</strong> Soit $v$ une valuation satisfaisant $F$. Alors $[p \\Rightarrow q]_v = 1$ et $[q \\Rightarrow r]_v = 1$. Supposons que $[p]_v = 1$. Par Modus Ponens sémantique sur la première prémisse, on a nécessairement $[q]_v = 1$. Puis, sur la seconde prémisse, avec $[q]_v = 1$, on a nécessairement $[r]_v = 1$. Ainsi, dès que $[p]_v = 1$, on a $[r]_v = 1$, ce qui prouve que $[p \\Rightarrow r]_v = 1$. Donc <strong>$F \\models G$ est VRAI</strong> (transitivité de l'implication).<br><br>
    2. <strong>Étude de $G \\models F$ :</strong> Cette relation est <strong>FAUSSE</strong>. Réfutation par contre-modèle explicite : choisissons $v(p)=0, v(q)=1, v(r)=0$.<br>
    - $[G]_v = [0 \\Rightarrow 0]_v = 1$.<br>
    - $[F]_v = [0 \\Rightarrow 1]_v \\land [1 \\Rightarrow 0]_v = 1 \\land 0 = 0$.<br>
    La valuation $v$ est bien un modèle de $G$ mais n'est pas un modèle de $F$.
  </div>
</div>
"""

annales_w2_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات آزمون‌های نهایی سوربن — هفته ۲</div>
  <p>سؤالات آزمون‌های واقعی در خصوص پیامد معنایی، ترانزیتیویته شرطی‌ها و ارائه مثال نقض دقیق عددی.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">امتحان میان‌ترم ۲۰۲۰–۲۰۲۱ — تمرین ۲ (پیامد معنایی و برهان)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">منبع رسمی: partiel_2020_2021_L2.pdf (صفحه ۲)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">هفته ۲</span><span class="badge">امتحان Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>دو فرمول زیر را در نظر بگیرید: $F = (p \\Rightarrow q) \\land (q \\Rightarrow r)$ و $G = p \\Rightarrow r$.</p>
    <p>۱. آیا رابطه $F \\models G$ برقرار است ؟ پاسخ را بدون رسم جدول درستی به دقت توجیه کنید.<br>
    ۲. آیا رابطه عکس $G \\models F$ برقرار است ؟ پاسخ را اثبات یا رد کنید.</p>
  </div>
  <div class="step-content">
    <strong>پاسخ تشریحی مطابق کلید تصحیح سوربن :</strong><br>
    ۱. <strong>بررسی $F \\models G$ :</strong> فرض کنید ارزش‌گذاری $v$ مدلی برای $F$ باشد، یعنی $[p \\Rightarrow q]_v = 1$ و $[q \\Rightarrow r]_v = 1$. اگر $[p]_v = 1$ باشد، از شرطی اول الزاماً نتیجه می‌شود $[q]_v = 1$. سپس از شرطی دوم با توجه به ۱ بودن $q$، الزاماً نتیجه می‌شود $[r]_v = 1$. بنابراین تحت ارزش‌گذاری $v$ هرگاه $p=1$ باشد $r=1$ خواهد بود، یعنی $[p \\Rightarrow r]_v = 1$. پس رابطه <strong>$F \\models G$ کاملاً برقرار است</strong>.<br><br>
    ۲. <strong>بررسی $G \\models F$ :</strong> این رابطه <strong>نادرست</strong> است. برای رد آن مثال نقض صریح ارائه می‌دهیم :<br>
    ارزش‌گذاری $v(p)=0$ و $v(q)=1$ و $v(r)=0$ را در نظر بگیرید :<br>
    - مقدار $G$ : $[0 \\Rightarrow 0] = 1$ (درست است).<br>
    - مقدار $F$ : $[0 \\Rightarrow 1] \\land [1 \\Rightarrow 0] = 1 \\land 0 = 0$ (نادرست است).<br>
    این ارزش‌گذاری نشان می‌دهد مدلی برای $G$ وجود دارد که $F$ را ارضا نمی‌کند.
  </div>
</div>
"""

make_bundle("w02_annales", "fr", annales_w2_fr)
make_bundle("w02_annales", "fa", annales_w2_fa)

revision_w2_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Révision Express — Semaine 2</div>
  <p>Synthèse des définitions, pièges et méthodes à maîtriser pour le Thème 2.</p>
</div>

<h2 id="w02-rev-bilan">1. Tableau Comparatif Crucial</h2>
<table class="truth-table">
  <thead><tr><th>Propriété</th><th>Comment le prouver ?</th><th>Comment le réfuter ?</th></tr></thead>
  <tbody>
    <tr><td>$F$ est valide</td><td>Démontrer que pour tout $v$, $[F]_v = 1$ (ou $F \\equiv \\top$).</td><td>Donner <strong>un contre-modèle</strong> où $[F]_v = 0$.</td></tr>
    <tr><td>$F$ est satisfiable</td><td>Donner <strong>un modèle</strong> où $[F]_v = 1$.</td><td>Démontrer que pour tout $v$, $[F]_v = 0$ ($F \\equiv \\bot$).</td></tr>
    <tr><td>$F \\models G$</td><td>Montrer que $[F]_v = 1 \\implies [G]_v = 1$.</td><td>Donner <strong>un contre-modèle</strong> : $[F]_v = 1$ et $[G]_v = 0$.</td></tr>
    <tr><td>$F \\equiv G$</td><td>Démontrer algébriquement $F \\equiv G$.</td><td>Donner une valuation $v$ où $[F]_v \\neq [G]_v$.</td></tr>
  </tbody>
</table>
"""

revision_w2_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه مرور سریع — هفته ۲</div>
  <p>جدول مقایسه‌ای و جمع‌بندی روش‌های اثبات و ابطال در تم ۲.</p>
</div>

<h2 id="w02-rev-bilan">۱. جدول مقایسه‌ای طلایی اثبات و ابطال</h2>
<table class="truth-table">
  <thead><tr><th>خاصیت</th><th>چگونه اثبات کنیم؟</th><th>چگونه رد کنیم؟</th></tr></thead>
  <tbody>
    <tr><td>$F$ معتبر است</td><td>اثبات اینکه تحت هر $v$ مقدار ۱ دارد (یا $F \\equiv \\top$).</td><td>ارائه <strong>یک مثال نقض</strong> که در آن $[F]_v = 0$ شود.</td></tr>
    <tr><td>$F$ صدق‌پذیر است</td><td>ارائه <strong>تنها یک مدل</strong> که در آن $[F]_v = 1$ شود.</td><td>اثبات اینکه در تمام حالات $[F]_v = 0$ است ($F \\equiv \\bot$).</td></tr>
    <tr><td>$F \\models G$</td><td>اثبات اینکه هرگاه $[F]_v=1$ شود الزاماً $[G]_v=1$ است.</td><td>ارائه <strong>یک مثال نقض</strong> که در آن $[F]_v=1$ ولی $[G]_v=0$ باشد.</td></tr>
    <tr><td>$F \\equiv G$</td><td>اثبات هم‌ارزی جبری خط‌به‌خط.</td><td>ارائه یک ارزش‌گذاری که در آن $[F]_v \\neq [G]_v$ شود.</td></tr>
  </tbody>
</table>
"""

make_bundle("w02_revision", "fr", revision_w2_fr)
make_bundle("w02_revision", "fa", revision_w2_fa)

print("Week 2 generation complete!")

