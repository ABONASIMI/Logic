import json, os

def make_bundle(lesson_id, lang, html_content, interactive_js=""):
    obj = {
        "id": lesson_id,
        "lang": lang,
        "html": html_content
    }
    js = f'Logic.reg("lesson:{lesson_id}:{lang}", {{\n  id: {json.dumps(lesson_id)},\n  lang: {json.dumps(lang)},\n  html: {json.dumps(html_content, ensure_ascii=False)},\n  initInteractive: function(container, lang) {{\n{interactive_js}\n  }}\n}});\n'
    out_path = f'Logic_Academy/data/lessons/{lesson_id}.{lang}.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'Generated {out_path}')

# ==============================================================================
# WEEK 1: COURS (FR & FA)
# ==============================================================================

cours_fr = """
<div class="box box-objectives">
  <div class="box-title">Objectifs d'apprentissage — Semaine 1</div>
  <ul>
    <li>Comprendre la notion fondamentale de proposition et de valeur de vérité ($\\{0, 1\\}$).</li>
    <li>Maîtriser la définition inductive de l'ensemble des formules propositionnelles $\\mathcal{F}$.</li>
    <li>Construire et analyser l'Arbre de Syntaxe Abstraite (AST) d'une formule et identifier son connecteur principal.</li>
    <li>Convertir une formule en notation préfixe (polonaise) sans parenthèses.</li>
    <li>Appliquer rigoureusement les règles de priorité et d'associativité pour lever les ambiguïtés.</li>
    <li>Construire des tables de vérité et analyser en profondeur la sémantique de l'implication matérielle.</li>
    <li>Distinguer sans erreur les formulations en langage naturel : <em>si</em>, <em>seulement si</em>, <em>il faut que</em>, <em>il suffit que</em>.</li>
  </ul>
</div>

<h2 id="w01-c-intro">1. Introduction : Qu'est-ce que la Logique Propositionnelle ?</h2>
<p>
La <strong>logique propositionnelle</strong> (aussi appelée calcul des propositions) est la branche fondamentale des mathématiques et de l'informatique théorique qui étudie la vérité ou la fausseté de déclarations composées à partir d'énoncés élémentaires appelés <em>propositions atomiques</em>.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 1.1 — Proposition et Valeur de Vérité</div>
  <p>Une <strong>proposition</strong> est une affirmation déclarative qui est soit <strong>vraie</strong> (notée $1$ ou $\\top$), soit <strong>fausse</strong> (notée $0$ ou $\\bot$), mais jamais les deux en même temps (principe du tiers exclu et de non-contradiction).</p>
  <p>Une proposition élémentaire qui ne peut être décomposée en énoncés plus simples est appelée une <strong>variable propositionnelle</strong> ou un <strong>atome</strong> (généralement notée $p, q, r, s, \\dots$).</p>
</div>

<div class="box box-intuition">
  <div class="box-title">Intuition & Raisonnement quotidien</div>
  <p>Considérons les énoncés suivants :</p>
  <ul>
    <li><em>« Paris est la capitale de la France »</em> : c'est une proposition vraie ($1$).</li>
    <li><em>« $2 + 2 = 5$ »</em> : c'est une proposition fausse ($0$).</li>
    <li><em>« Quelle heure est-il ? »</em> : ce n'est PAS une proposition car c'est une question, elle ne possède aucune valeur de vérité.</li>
  </ul>
</div>

<h2 id="w01-c-syntaxe">2. Syntaxe Formelle et Grammaire Inductive</h2>
<p>
En informatique, une chaîne de caractères n'est pas une formule logique valide par magie : elle doit respecter une grammaire rigoureuse.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 1.2 — Ensemble Inductif des Formules ($\\mathcal{F}$)</div>
  <p>Soit $\\mathcal{V}$ un ensemble dénombrable de variables propositionnelles. L'ensemble $\\mathcal{F}$ des formules de la logique propositionnelle est le plus petit ensemble satisfaisant les trois règles inductives :</p>
  <ol>
    <li><strong>Base :</strong> Tout atome $p \\in \\mathcal{V}$ est une formule ($p \\in \\mathcal{F}$). Les constantes $\\top$ (Vrai) et $\\bot$ (Faux) sont des formules.</li>
    <li><strong>Induction unaire :</strong> Si $F \\in \\mathcal{F}$, alors $(\\neg F) \\in \\mathcal{F}$ (négation de $F$).</li>
    <li><strong>Induction binaire :</strong> Si $F_1, F_2 \\in \\mathcal{F}$, alors $(F_1 \\land F_2) \\in \\mathcal{F}$ (conjonction), $(F_1 \\lor F_2) \\in \\mathcal{F}$ (disjonction), $(F_1 \\Rightarrow F_2) \\in \\mathcal{F}$ (implication), et $(F_1 \\Leftrightarrow F_2) \\in \\mathcal{F}$ (équivalence).</li>
  </ol>
</div>

<h2 id="w01-c-ast">3. Arbre de Syntaxe Abstraite (AST) et Connecteur Principal</h2>
<p>
L'écriture linéaire avec des parenthèses dissimule la structure hiérarchique réelle d'une formule. La véritable représentation mathématique et computationnelle d'une formule est son <strong>Arbre de Syntaxe Abstraite (AST)</strong>.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 1.3 — Connecteur Principal et AST</div>
  <ul>
    <li><strong>Connecteur principal :</strong> C'est le connecteur logique appliqué en dernier lieu lors de la construction inductive de la formule. Dans l'AST, c'est l'étiquette de la racine.</li>
    <li><strong>Feuilles :</strong> Ce sont les variables propositionnelles ou les constantes $\\top, \\bot$. Elles n'ont aucun sous-arbre enfant.</li>
    <li><strong>Nœuds internes :</strong> Ce sont les connecteurs logiques. Un connecteur unaire ($\\neg$) a 1 enfant ; un connecteur binaire ($\\land, \\lor, \\Rightarrow, \\Leftrightarrow$) a 2 enfants.</li>
  </ul>
</div>

<p>Exemple : Pour la formule $F_1 = \\neg(p \\land (q \\Rightarrow ((q \\lor r) \\land q)))$, le connecteur principal est la négation $\\neg$. L'arbre se ramifie ensuite sous la conjonction $\\land$.</p>

<div class="ast-container">
  <div class="ast-ascii">
            ¬  (racine = connecteur principal)
            │
            ∧
          /   \\
         p     ⇒
              / \\
             q   ∧
                / \\
               ∨   q
              / \\
             q   r
  </div>
</div>

<h2 id="w01-c-prefixe">4. Notation Préfixe (Notation Polonaise)</h2>
<p>
La notation préfixe consiste à écrire l'opérateur <strong>avant</strong> ses opérandes. Elle s'obtient par un <strong>parcours préfixe</strong> de l'AST :
$$\\text{Visiter la Racine} \\longrightarrow \\text{Sous-arbre Gauche} \\longrightarrow \\text{Sous-arbre Droit}$$
L'immense avantage de la notation préfixe est qu'elle est <strong>totalement non ambiguë sans aucune parenthèse</strong> !
</p>
<p>Pour l'arbre ci-dessus, le parcours préfixe donne :<br>
<code>¬ ∧ p ⇒ q ∧ ∨ q r q</code></p>

<h2 id="w01-c-priorite">5. Règles de Priorité et d'Associativité</h2>
<p>
Pour alléger l'écriture en évitant d'écrire des dizaines de parenthèses superflues, les logiciens ont établi des conventions universelles :
</p>
<table class="truth-table">
  <thead>
    <tr><th>Opérateur</th><th>Nom</th><th>Priorité</th><th>Associativité</th></tr>
  </thead>
  <tbody>
    <tr><td>$\\neg$</td><td>Négation</td><td>1 (la plus forte)</td><td>Unaire</td></tr>
    <tr><td>$\\land$</td><td>Conjonction (ET)</td><td>2</td><td>Associatif à gauche</td></tr>
    <tr><td>$\\lor$</td><td>Disjonction (OU)</td><td>3</td><td>Associatif à gauche</td></tr>
    <tr><td>$\\Rightarrow$</td><td>Implication</td><td>4</td><td><strong>Associatif à droite</strong> ($p \\Rightarrow q \\Rightarrow r \\equiv p \\Rightarrow (q \\Rightarrow r)$)</td></tr>
    <tr><td>$\\Leftrightarrow$</td><td>Équivalence</td><td>5 (la plus faible)</td><td>Non associatif</td></tr>
  </tbody>
</table>

<h2 id="w01-c-implication">6. Analyse Approfondie de l'Implication Matérielle</h2>
<p>
L'implication $p \\Rightarrow q$ est l'un des plus grands pièges pour les étudiants.
</p>

<div class="box box-definition">
  <div class="box-title">Définition 1.4 — Table de Vérité de l'Implication</div>
  <p>L'implication $p \\Rightarrow q$ est <strong>fausse</strong> dans un seul et unique cas : lorsque la prémisse $p$ est VRAIE ($1$) et la conclusion $q$ est FAUSSE ($0$). Dans tous les autres cas, elle est <strong>VRAIE</strong> ($1$).</p>
  <table class="truth-table" style="max-width:320px; margin:0.8rem auto;">
    <thead><tr><th>$p$</th><th>$q$</th><th>$p \\Rightarrow q$</th></tr></thead>
    <tbody>
      <tr><td>0</td><td>0</td><td class="truth-val-true">1</td></tr>
      <tr><td>0</td><td>1</td><td class="truth-val-true">1</td></tr>
      <tr><td>1</td><td>0</td><td class="truth-val-false">0</td></tr>
      <tr><td>1</td><td>1</td><td class="truth-val-true">1</td></tr>
    </tbody>
  </table>
  <p>Équivalence algébrique fondamentale : $$(p \\Rightarrow q) \\equiv (\\neg p \\lor q)$$</p>
</div>

<div class="box box-consigne">
  <div class="box-title">Comprendre la consigne — Les formulations du langage naturel</div>
  <p>Voici la correspondance exacte attendue aux examens de la Sorbonne :</p>
  <ul>
    <li><strong>« Si $p$, alors $q$ »</strong> $\\implies p \\Rightarrow q$</li>
    <li><strong>« $q$ si $p$ »</strong> $\\implies p \\Rightarrow q$</li>
    <li><strong>« $p$ seulement si $q$ »</strong> $\\implies p \\Rightarrow q$ (et SURTOUT PAS $q \\Rightarrow p$ !)</li>
    <li><strong>« Pour que $p$, il faut que $q$ »</strong> $\\implies p \\Rightarrow q$ ($q$ est une condition <em>nécessaire</em>)</li>
    <li><strong>« Pour que $q$, il suffit que $p$ »</strong> $\\implies p \\Rightarrow q$ ($p$ est une condition <em>suffisante</em>)</li>
  </ul>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — La fausse équivalence entre condition nécessaire et suffisante</div>
  <p><strong>Erreur fréquente :</strong> Traduire « Je ne sors que s'il fait beau » par $\\text{beau} \\Rightarrow \\text{sortir}$.</p>
  <p><strong>Explication de l'erreur :</strong> Si cette formule était vraie, cela voudrait dire que dès qu'il fait beau, vous êtes OBLIGÉ de sortir. Or la phrase signifie seulement : « Si je sors, alors il fait forcément beau » (il ne peut pas arriver que je sorte sous la pluie). La traduction exacte est donc : $\\text{sortir} \\Rightarrow \\text{beau}$.</p>
</div>
"""

cours_fa = """
<div class="box box-objectives">
  <div class="box-title">اهداف آموزشی و خروجی‌های یادگیری — هفته ۱</div>
  <ul>
    <li>درک مفهوم بنیادی گزاره منطقی و مقادیر درستی ($\\{0, 1\\}$).</li>
    <li>تسلط بر تعریف استقرایی و گرامری مجموعه فرمول‌های گزاره‌ای $\\mathcal{F}$.</li>
    <li>رسم و تحلیل درخت نحو انتزاعی (AST) و شناسایی بی‌درنگ رابط اصلی (Connecteur Principal).</li>
    <li>تبدیل فرمول به نشانه‌گذاری پیشوندی (لهستانی) بدون نیاز به پرانتز.</li>
    <li>به‌کارگیری دقیق اولویت عملگرها و خاصیت شرکت‌پذیری برای رفع ابهام.</li>
    <li>ساخت جدول‌های درستی و کالبدشکافی معنایی شرطی مادی ($p \\Rightarrow q$).</li>
    <li>تشخیص تفاوت‌های ظریف در زبان طبیعی: <em>اگر</em>، <em>تنها اگر</em>، <em>لازم است که</em>، <em>کافی است که</em>.</li>
  </ul>
</div>

<h2 id="w01-c-intro">۱. مقدمه: منطق گزاره‌ای چیست؟</h2>
<p>
<strong>منطق گزاره‌ای (Calcul des propositions)</strong> بنیادی‌ترین شاخه منطق ریاضی و علوم کامپیوتر نظری است که به بررسی ارزش صدق یا کذب جملات ترکیبی بر پایه جملات ساده به نام <em>اتم‌ها</em> یا گزاره‌های اولیه می‌پردازد.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۱.۱ — گزاره و مقدار درستی</div>
  <p>یک <strong>گزاره (Proposition)</strong> جمله‌ای اخباری است که یا <strong>درست</strong> است (با نماد $1$ یا $\\top$) یا <strong>نادرست</strong> (با نماد $0$ یا $\\bot$)، و نمی‌تواند هم‌زمان هر دو باشد (اصل امتناع تناقض و طرد شق ثالث).</p>
  <p>کوچک‌ترین جزء معنایی که خود قابل تجزیه به گزاره‌های ساده‌تر نباشد را <strong>متغیر گزاره‌ای</strong> یا <strong>اتم (Atome)</strong> می‌نامیم (معمولاً با حروف $p, q, r, s, \\dots$).</p>
</div>

<div class="box box-intuition">
  <div class="box-title">شهود و تفکر منطقی در زندگی روزمره</div>
  <p>جملات زیر را در نظر بگیرید:</p>
  <ul>
    <li><em>«پاریس پایتخت فرانسه است»</em>: این یک گزاره است و ارزش آن درست ($1$) می‌باشد.</li>
    <li><em>«$۲ + ۲ = ۵$»</em>: این یک گزاره است و ارزش آن نادرست ($0$) می‌باشد.</li>
    <li><em>«ساعت چند است؟»</em>: این گزاره نیست زیرا یک پرسش است و ارزش درستی یا نادرستی ندارد.</li>
  </ul>
</div>

<h2 id="w01-c-syntaxe">۲. نحو صوری و تعریف استقرایی فرمول‌ها</h2>
<p>
در علوم کامپیوتر، هر رشته متنی یک فرمول معتبر منطقی نیست؛ فرمول باید از قواعد سفت‌وسخت گرامر استقرایی پیروی کند.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۱.۲ — مجموعه استقرایی فرمول‌های گزاره‌ای ($\\mathcal{F}$)</div>
  <p>فرض کنید $\\mathcal{V}$ مجموعه شمارای متغیرهای گزاره‌ای باشد. مجموعه $\\mathcal{F}$ شامل تمام فرمول‌های خوش‌ساخت، کوچک‌ترین مجموعه‌ای است که سه شرط زیر را ارضا می‌کند:</p>
  <ol>
    <li><strong>پایه استقرا:</strong> هر اتم $p \\in \\mathcal{V}$ یک فرمول است ($p \\in \\mathcal{F}$). ثابت‌های $\\top$ و $\\bot$ نیز فرمول هستند.</li>
    <li><strong>گام استقرای تک‌تایی:</strong> اگر $F \\in \\mathcal{F}$ باشد، آنگاه $(\\neg F) \\in \\mathcal{F}$ (نقیض $F$).</li>
    <li><strong>گام استقرای دو‌تایی:</strong> اگر $F_1, F_2 \\in \\mathcal{F}$ باشند، آنگاه $(F_1 \\land F_2)$ (عطف)، $(F_1 \\lor F_2)$ (فصل)، $(F_1 \\Rightarrow F_2)$ (شرطی)، و $(F_1 \\Leftrightarrow F_2)$ (دو‌شرطی) همگی عضو $\\mathcal{F}$ هستند.</li>
  </ol>
</div>

<h2 id="w01-c-ast">۳. درخت نحو انتزاعی (AST) و رابط اصلی</h2>
<p>
نمایش خطی با پرانتزها ساختار درختی و اولویت‌های پردازشی را پنهان می‌کند. ساختار واقعی یک فرمول در حافظه رایانه، یک <strong>درخت نحو انتزاعی (AST)</strong> است.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۱.۳ — رابط اصلی (Connecteur Principal) و گره‌های AST</div>
  <ul>
    <li><strong>رابط اصلی:</strong> آخرین عملگری است که در فرآیند ساخت فرمول اعمال می‌شود. در درخت نحو، برچسب <strong>ریشه درخت</strong> است.</li>
    <li><strong>برگ‌ها (Feuilles):</strong> متغیرهای گزاره‌ای یا ثابت‌های $\\top, \\bot$ هستند که هیچ فرزندی ندارند.</li>
    <li><strong>گره‌های داخلی:</strong> رابط‌های منطقی هستند. رابط نقیض ($\\neg$) یک فرزند و رابط‌های دوتایی دو فرزند دارند.</li>
  </ul>
</div>

<p>به عنوان مثال برای فرمول $F_1 = \\neg(p \\land (q \\Rightarrow ((q \\lor r) \\land q)))$، رابط اصلی نقیض $\\neg$ در بالاترین سطح است:</p>

<div class="ast-container">
  <div class="ast-ascii">
            ¬  (ریشه = رابط اصلی)
            │
            ∧
          /   \\
         p     ⇒
              / \\
             q   ∧
                / \\
               ∨   q
              / \\
             q   r
  </div>
</div>

<h2 id="w01-c-prefixe">۴. نشانه‌گذاری پیشوندی (لهستانی)</h2>
<p>
در نشانه‌گذاری پیشوندی، ابتدا عملگر و سپس عملوندها نوشته می‌شوند. این ترتیب دقیقاً از <strong>پیمایش پیشوندی (Pre-order Traversal)</strong> درخت به دست می‌آید:
$$\\text{بازدید ریشه} \\longrightarrow \\text{زیردرخت چپ} \\longrightarrow \\text{زیردرخت راست}$$
مزیت خیره‌کننده نشانه‌گذاری پیشوندی این است که <strong>بدون هیچ‌گونه پرانتزی کاملاً بدون ابهام است</strong>!
</p>
<p>پیمایش پیشوندی درخت بالا عبارت است از:<br>
<code>¬ ∧ p ⇒ q ∧ ∨ q r q</code></p>

<h2 id="w01-c-priorite">۵. اولویت عملگرها و خاصیت شرکت‌پذیری</h2>
<p>برای پرهیز از پرانتزگذاری‌های مکرر و خسته‌کننده، اولویت‌های استاندارد زیر حاکم است:</p>
<table class="truth-table">
  <thead>
    <tr><th>عملگر</th><th>نام</th><th>اولویت</th><th>شرکت‌پذیری (Associativité)</th></tr>
  </thead>
  <tbody>
    <tr><td>$\\neg$</td><td>نقیض</td><td>۱ (بالاترین اولویت)</td><td>تک‌تایی</td></tr>
    <tr><td>$\\land$</td><td>عطف (AND)</td><td>۲</td><td>شرکت‌پذیر از چپ</td></tr>
    <tr><td>$\\lor$</td><td>فصل (OR)</td><td>۳</td><td>شرکت‌پذیر از چپ</td></tr>
    <tr><td>$\\Rightarrow$</td><td>شرطی (ایستلزام)</td><td>۴</td><td><strong>شرکت‌پذیر از راست</strong> ($p \\Rightarrow q \\Rightarrow r \\equiv p \\Rightarrow (q \\Rightarrow r)$)</td></tr>
    <tr><td>$\\Leftrightarrow$</td><td>دوشرطی</td><td>۵ (پایین‌ترین)</td><td>غیر شرکت‌پذیر</td></tr>
  </tbody>
</table>

<h2 id="w01-c-implication">۶. کالبدشکافی معنایی شرطی مادی ($p \\Rightarrow q$)</h2>
<p>
شرطی منطقی یکی از بزرگ‌ترین دام‌هایی است که دانشجویان در آن گرفتار می‌شوند.
</p>

<div class="box box-definition">
  <div class="box-title">تعریف ۱.۴ — جدول درستی شرطی مادی</div>
  <p>گزاره شرطی $p \\Rightarrow q$ <strong>تنها و تنها در یک حالت نادرست است</strong>: هنگامی که مقدم $p$ درست ($1$) باشد اما تالی $q$ نادرست ($0$) باشد. در تمام حالات دیگر، حتی اگر مقدم نادرست باشد، کل شرطی <strong>درست</strong> است!</p>
  <table class="truth-table" style="max-width:320px; margin:0.8rem auto;">
    <thead><tr><th>$p$</th><th>$q$</th><th>$p \\Rightarrow q$</th></tr></thead>
    <tbody>
      <tr><td>0</td><td>0</td><td class="truth-val-true">1</td></tr>
      <tr><td>0</td><td>1</td><td class="truth-val-true">1</td></tr>
      <tr><td>1</td><td>0</td><td class="truth-val-false">0</td></tr>
      <tr><td>1</td><td>1</td><td class="truth-val-true">1</td></tr>
    </tbody>
  </table>
  <p>هم‌ارزی جبری طلایی: $$(p \\Rightarrow q) \\equiv (\\neg p \\lor q)$$</p>
</div>

<div class="box box-consigne">
  <div class="box-title">فهمیدن خواست سؤال — ترجمه عبارات زبان طبیعی در آزمون‌های سوربن</div>
  <p>همواره در امتحانات سوربن به تطابق‌های دقیق زیر توجه کنید:</p>
  <ul>
    <li><strong>«اگر $p$ آنگاه $q$» (Si $p$, alors $q$)</strong> $\\implies p \\Rightarrow q$</li>
    <li><strong>«$q$ اگر $p$» ($q$ si $p$)</strong> $\\implies p \\Rightarrow q$</li>
    <li><strong>«$p$ فقط اگر $q$» ($p$ seulement si $q$)</strong> $\\implies p \\Rightarrow q$ (و به هیچ وجه $q \\Rightarrow p$ نیست!)</li>
    <li><strong>«برای اینکه $p$ رخ دهد، لازم است که $q$ باشد» (Pour que $p$, il faut que $q$)</strong> $\\implies p \\Rightarrow q$ ($q$ شرط لازم است)</li>
    <li><strong>«برای اینکه $q$ رخ دهد، کافی است که $p$ باشد» (Pour que $q$, il suffit que $p$)</strong> $\\implies p \\Rightarrow q$ ($p$ شرط کافی است)</li>
  </ul>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — اشتباه گرفتن شرط لازم با شرط کافی</div>
  <p><strong>اشتباه بسیار رایج:</strong> ترجمه عبارت «من فقط در صورتی قدم می‌زنم که هوا خوب باشد» به صورت $\\text{هوا خوب} \\Rightarrow \\text{قدم زدن}$.</p>
  <p><strong>تحلیل خطا:</strong> اگر این رابطه درست بود، یعنی هر زمان هوا خوب باشد شما مجبورید قدم بزنید! در حالی که جمله می‌گوید: اگر من را در حال قدم زدن دیدید، حتماً هوا خوب است (امکان ندارد زیر باران قدم بزنم). پس فرمول درست $\\text{قدم زدن} \\Rightarrow \\text{هوا خوب}$ است.</p>
</div>
"""

make_bundle("w01_cours", "fr", cours_fr)
make_bundle("w01_cours", "fa", cours_fa)

# ==============================================================================
# WEEK 1: TD (FR & FA) - Exercices 1, 2, 3 de main_td-etudiants.pdf
# ==============================================================================

td_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de TD 1 — Solutions Officielles Intégrales & Justifications</div>
  <p>Source officielle : <code>main_td-etudiants.pdf</code> (p. 2–3, Thème 1). Cette séance traite des arbres de syntaxe abstraite, de la notation préfixe, du parenthésage selon les priorités, des subtilités de l'implication en langage naturel, et de la résolution rigoureuse d'énigmes logiques par tables de vérité.</p>
</div>

<div id="td-exo1-container"></div>
<div id="td-exo2-container"></div>
<div id="td-exo3-container"></div>
"""

td_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه تمرین‌های کلاسی TD 1 — حل تشریحی خط‌به‌خط و توجیه ریاضی</div>
  <p>منبع رسمی: جزوه <code>main_td-etudiants.pdf</code> (صفحه ۲ و ۳، تم ۱). این جلسه شامل رسم کامل درخت‌های نحو انتزاعی (AST)، نشانه‌گذاری پیشوندی، پرانتزگذاری صوری، تحلیل جملات شرطی زبان فرانسه و حل گام‌به‌گام معمای جزیره راستگویان و دروغگویان است.</p>
</div>

<div id="td-exo1-container"></div>
<div id="td-exo2-container"></div>
<div id="td-exo3-container"></div>
"""

td_interactive = """
  // Exercice 1
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo1-container'), {
    id: 'w01_td_ex1',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۱ — درخت نحو انتزاعی و نشانه‌گذاری پیشوندی' : 'Exercice 1 – Arbre de syntaxe abstraite & notation préfixe',
    source: 'main_td-etudiants.pdf (p. 2)',
    theme: lang === 'fa' ? 'تم ۱' : 'Thème 1',
    statement: lang === 'fa' ? 
      '<p><strong>سؤال ۱ :</strong> برای هر یک از فرمول‌های زیر که در آن‌ها $p, q, r$ گزاره‌اند، درخت نحو انتزاعی را رسم کرده و فرمول را در نشانه‌گذاری پیشوندی بنویسید :</p>' +
      '<ol><li>$F_1 = \\neg(p \\land (q \\Rightarrow ((q \\lor r) \\land q)))$</li><li>$F_2 = \\neg p \\land q \\Rightarrow q \\lor r \\land q$</li></ol>' +
      '<p><strong>سؤال ۲ :</strong> فرمول‌های زیر را با رعایت اولویت عملگرها به طور کامل پرانتزگذاری کنید :</p>' +
      '<ol><li>$F_3 = p \\land q \\land r \\land s$</li><li>$F_4 = p \\Rightarrow q \\land \\neg r \\Rightarrow p \\lor q$</li></ol>' :
      '<p><strong>Question 1 :</strong> Pour chacune des formules suivantes où $p, q, r$ sont des symboles de propositions :</p>' +
      '<ul><li>dessiner son arbre de syntaxe abstraite</li><li>écrire la formule en notation préfixe.</li></ul>' +
      '<ol><li>$F_1 = \\neg(p \\land (q \\Rightarrow ((q \\lor r) \\land q)))$</li><li>$F_2 = \\neg p \\land q \\Rightarrow q \\lor r \\land q$</li></ol>' +
      '<p><strong>Question 2 :</strong> Parenthéser les formules suivantes en respectant la priorité des opérateurs :</p>' +
      '<ol><li>$F_3 = p \\land q \\land r \\land s$</li><li>$F_4 = p \\Rightarrow q \\land \\neg r \\Rightarrow p \\lor q$</li></ol>',
    consigne: lang === 'fa' ? 
      'وقتی از شما خواسته می‌شود درخت نحو را رسم کنید، باید رابط اصلی را در ریشه قرار دهید و پرانتزها را در درخت نکشید زیرا شاخه‌ها خود نشان‌دهنده اولویت‌اند. در نشانه‌گذاری پیشوندی هیچ پرانتزی نباید وجود داشته باشد.' :
      'Quand on vous demande l\\'AST, la racine doit impérativement être le connecteur principal. Ne dessinez jamais de parenthèses dans l\\'AST : la géométrie de l\\'arbre encode la priorité. Pour la notation préfixe, supprimez TOUTES les parenthèses.',
    hint: lang === 'fa' ? 
      'برای F2 اولویت‌ها عبارتند از: نقیض، سپس عطف، سپس فصل، و در آخر شرطی. برای شرکت‌پذیری شرطی‌ها به یاد داشته باشید که از سمت راست گروه‌بندی می‌شوند!' :
      'Pour F2, appliquez l\\'ordre de priorité décroissant : ¬ > ∧ > ∨ > ⇒. Attention : l\\'implication ⇒ est associative à droite !',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (فرمول F1) :</strong> رابط اصلی نقیض $\\neg$ است. داخل آن یک عطف $\\land$ بین $p$ و یک عبارت شرطی قرار دارد. با پیمایش پیشوندی (ریشه، چپ، راست) عبارت پیشوندی به دست می‌آید :<br><code>¬ ∧ p ⇒ q ∧ ∨ q r q</code>',
      '<strong>گام ۲ (فرمول F2) :</strong> با اعمال اولویت‌ها: ابتدا نقیض $\\neg p$، سپس عطف‌های $\\neg p \\land q$ و $r \\land q$، سپس فصل $q \\lor (r \\land q)$، و در نهایت رابط اصلی شرطی $\\Rightarrow$ است. فرمول پرانتزگذاری‌شده: $((\\neg p) \\land q) \\Rightarrow (q \\lor (r \\land q))$.<br>عبارت پیشوندی :<br><code>⇒ ∧ ¬ p q ∨ q ∧ r q</code>',
      '<strong>گام ۳ (فرمول F3) :</strong> عطف شرکت‌پذیر از چپ است، بنابراین :<br>$((p \\land q) \\land r) \\land s$',
      '<strong>گام ۴ (فرمول F4) :</strong> ابتدا نقیض $\\neg r$، سپس عطف $q \\land (\\neg r)$، سپس فصل $p \\lor q$. باقی‌مانده دو شرطی متوالی است : $p \\Rightarrow (q \\land \\neg r) \\Rightarrow (p \\lor q)$. چون شرطی شرکت‌پذیر از راست است، گروه‌بندی از راست انجام می‌شود :<br>$p \\Rightarrow ((q \\land (\\neg r)) \\Rightarrow (p \\lor q))$'
    ] : [
      '<strong>Étape 1 (Formule F1) :</strong> Le connecteur principal est $\\neg$. L\\'opérande interne est une conjonction dont le fils gauche est $p$ et le fils droit est l\\'implication. Le parcours préfixe donne :<br><code>¬ ∧ p ⇒ q ∧ ∨ q r q</code>',
      '<strong>Étape 2 (Formule F2) :</strong> On applique les priorités strictes (¬ > ∧ > ∨ > ⇒). On a donc $\\neg p$, puis $(\\neg p \\land q)$, puis $(r \\land q)$, puis $(q \\lor (r \\land q))$. Le connecteur principal est l\\'implication $\\Rightarrow$.<br>Préfixe : <code>⇒ ∧ ¬ p q ∨ q ∧ r q</code>',
      '<strong>Étape 3 (Formule F3) :</strong> La conjonction $\\land$ est associative à gauche. Le parenthésage complet est :<br>$((p \\land q) \\land r) \\land s$',
      '<strong>Étape 4 (Formule F4) :</strong> On applique les priorités : d\\'abord $\\neg r$, puis $q \\land \\neg r$, puis $p \\lor q$. Pour les deux implications, on applique l\\'associativité à droite :<br>$p \\Rightarrow ((q \\land (\\neg r)) \\Rightarrow (p \\lor q))$'
    ],
    justification: lang === 'fa' ?
      'توجیه صوری بر پایه تعاریف گرامری اسلایدهای ۱۲ تا ۱۸ جزوه درس ۱ است. شرکت‌پذیری از راست شرطی ناشی از تطابق کورس با سیستم‌های بازنویسی و اثبات گزاره‌ها است.' :
      'Conforme aux règles de grammaire formelle et d\\'associativité des diapositives 12 à 18 du Cours 1. L\\'associativité à droite de l\\'implication est une convention standard en logique mathématique et en théorie des types.',
    finalAnswer: lang === 'fa' ?
      '<strong>پاسخ نهایی :</strong><br>' +
      '۱. Préfixe F1 : <code>¬ ∧ p ⇒ q ∧ ∨ q r q</code><br>' +
      '۲. Préfixe F2 : <code>⇒ ∧ ¬ p q ∨ q ∧ r q</code><br>' +
      '۳. Parenthésage F3 : $((p \\land q) \\land r) \\land s$<br>' +
      '۴. Parenthésage F4 : $p \\Rightarrow ((q \\land \\neg r) \\Rightarrow (p \\lor q))$' :
      '<strong>Réponses définitives :</strong><br>' +
      '1. Préfixe F1 : <code>¬ ∧ p ⇒ q ∧ ∨ q r q</code><br>' +
      '2. Préfixe F2 : <code>⇒ ∧ ¬ p q ∨ q ∧ r q</code><br>' +
      '3. Parenthésage F3 : $((p \\land q) \\land r) \\land s$<br>' +
      '4. Parenthésage F4 : $p \\Rightarrow ((q \\land \\neg r) \\Rightarrow (p \\lor q))$',
    verification: lang === 'fa' ?
      'برای بررسی صحت نشانه‌گذاری پیشوندی، از یک الگوریتم پشته استفاده کنید: از راست به چپ بخوانید؛ اتم‌ها را در پشته بگذارید و با رسیدن به عملگر دوتایی دو مقدار را پاپ کرده و نتیجه را پوش کنید. در انتها باید دقیقاً یک عبارت در پشته باقی بماند.' :
      'Vérification par algorithme de pile : en lisant la notation préfixe de droite à gauche, on empile les atomes et dès qu\\'on rencontre un connecteur binaire, on dépile deux éléments. La pile doit contenir exactement un élément à la fin sans débordement.',
    trap: lang === 'fa' ?
      'بزرگ‌ترین دام در سؤال ۲.۲، پرانتزگذاری شرطی از چپ به راست مانند $((p \\Rightarrow (q \\land \\neg r)) \\Rightarrow (p \\lor q))$ است که نمره کامل آن کسر خواهد شد زیرا $\\Rightarrow$ در استاندارد سوربن اکیداً شرکت‌پذیر از راست است!' :
      'Le piège classique à l\\'examen est de parenthéser l\\'implication à gauche : $((p \\Rightarrow (q \\land \\neg r)) \\Rightarrow (p \\lor q))$ est FAUX ! L\\'implication est toujours associative à droite en logique.'
  });

  // Exercice 2
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo2-container'), {
    id: 'w01_td_ex2',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۲ — شرطی و زبان طبیعی' : 'Exercice 2 – Implication et langage naturel',
    source: 'main_td-etudiants.pdf (p. 2)',
    theme: lang === 'fa' ? 'تم ۱' : 'Thème 1',
    statement: lang === 'fa' ?
      '<p>فرض کنید $b$ گزاره «هوا خوب است» و $p$ گزاره «من قدم می‌زنم» باشد.</p>' +
      '<p><strong>سؤال ۱ :</strong> کدام‌یک از گزاره‌های زیر در حالتی که <em>هوا خوب نیست ($b=0$)</em> و <em>من قدم می‌زنم ($p=1$)</em> درست هستند ؟</p>' +
      '<ol>' +
      '<li>S’il fait beau, je me promène (اگر هوا خوب باشد، قدم می‌زنم)</li>' +
      '<li>Pour que je me promène, il faut qu’il fasse beau (برای اینکه قدم بزنم، لازم است هوا خوب باشد)</li>' +
      '<li>Je ne me promène que si il fait beau (من فقط در صورتی قدم می‌زنم که هوا خوب باشد)</li>' +
      '<li>Je me promène dès qu’il fait beau (به محض اینکه هوا خوب شود، قدم می‌زنم)</li>' +
      '<li>Je me promène seulement si il fait beau (من فقط اگر هوا خوب باشد قدم می‌زنم)</li>' +
      '<li>Pour que je me promène, il suffit qu’il fasse beau (برای اینکه قدم بزنم، کافی است هوا خوب باشد)</li>' +
      '</ol>' :
      '<p>Soient $b$ : « Il fait beau » et $p$ : « Je me promène ».</p>' +
      '<p><strong>Question 1 :</strong> Parmi les énoncés suivants, lesquels sont vérifiés s’il ne fait pas beau ($b=0$) et que je me promène ($p=1$) ?</p>' +
      '<ol>' +
      '<li>S’il fait beau, je me promène</li>' +
      '<li>Pour que je me promène, il faut qu’il fasse beau</li>' +
      '<li>Je ne me promène que si il fait beau</li>' +
      '<li>Je me promène dès qu’il fait beau</li>' +
      '<li>Je me promène seulement si il fait beau</li>' +
      '<li>Pour que je me promène, il suffit qu’il fasse beau</li>' +
      '</ol>',
    consigne: lang === 'fa' ? 
      'ابتدا هر جمله زبان فرانسه را به یک فرمول صوری بر حسب $b$ و $p$ ترجمه کنید. سپس ارزش فرمول را تحت ارزش‌گذاری $v(b)=0$ و $v(p)=1$ محاسبه نمایید.' :
      'Traduisez chaque phrase en une formule logique précise reliant $b$ et $p$. Ensuite, évaluez la valeur de vérité de chaque formule sous la valuation $v(b)=0$ et $v(p)=1$.',
    hint: lang === 'fa' ? 
      'به یاد داشته باشید که شرطی $X \\Rightarrow Y$ زمانی که $X=0$ باشد همواره درست ($1$) است. اما اگر $X=1$ و $Y=0$ باشد، نادرست ($0$) خواهد شد.' :
      'Rappel : $X \\Rightarrow Y$ est VRAI dès que $X=0$. Par contre, si $X=1$ et $Y=0$, l\\'implication est FAUSSE.',
    steps: lang === 'fa' ? [
      '<strong>تحلیل عبارت ۱ :</strong> «S\\'il fait beau, je me promène» $\\equiv b \\Rightarrow p$. چون $b=0$ است، مقدم شرطی نادرست است، پس طبق تعریف شرطی مادی، کل گزاره <strong>درست ($1$)</strong> است.',
      '<strong>تحلیل عبارت ۲ :</strong> «Pour que je me promène, il faut qu\\'il fasse beau». هوای خوب شرط <em>لازم</em> است، پس $\\equiv p \\Rightarrow b$. چون $p=1$ و $b=0$ است، مقدم درست و تالی نادرست است، پس گزاره <strong>نادرست ($0$)</strong> است.',
      '<strong>تحلیل عبارت ۳ :</strong> «Je ne me promène que si il fait beau» $\\equiv p \\Rightarrow b$. با $p=1, b=0$ ارزش آن <strong>نادرست ($0$)</strong> است.',
      '<strong>تحلیل عبارت ۴ :</strong> «Je me promène dès qu\\'il fait beau» $\\equiv b \\Rightarrow p$. با $b=0$ ارزش آن <strong>درست ($1$)</strong> است.',
      '<strong>تحلیل عبارت ۵ :</strong> «Je me promène seulement si il fait beau» $\\equiv p \\Rightarrow b$. با $p=1, b=0$ ارزش آن <strong>نادرست ($0$)</strong> است.',
      '<strong>تحلیل عبارت ۶ :</strong> «Pour que je me promène, il suffit qu\\'il fasse beau». هوای خوب شرط <em>کافی</em> است، پس $\\equiv b \\Rightarrow p$. با $b=0$ ارزش آن <strong>درست ($1$)</strong> است.'
    ] : [
      '<strong>Énoncé 1 :</strong> « S\\'il fait beau, je me promène » $\\equiv b \\Rightarrow p$. Comme $b=0$, la prémisse est fausse, donc l\\'implication est <strong>VRAIE (1)</strong>.',
      '<strong>Énoncé 2 :</strong> « Pour que je me promène, il faut qu\\'il fasse beau » : le beau temps est une condition <em>nécessaire</em> $\\equiv p \\Rightarrow b$. Comme $p=1$ et $b=0$, l\\'implication est <strong>FAUSSE (0)</strong>.',
      '<strong>Énoncé 3 :</strong> « Je ne me promène que si il fait beau » $\\equiv p \\Rightarrow b$. Avec $p=1, b=0$, l\\'énoncé est <strong>FAUX (0)</strong>.',
      '<strong>Énoncé 4 :</strong> « Je me promène dès qu\\'il fait beau » $\\equiv b \\Rightarrow p$. Comme $b=0$, l\\'énoncé est <strong>VRAI (1)</strong>.',
      '<strong>Énoncé 5 :</strong> « Je me promène seulement si il fait beau » $\\equiv p \\Rightarrow b$. Avec $p=1, b=0$, l\\'énoncé est <strong>FAUX (0)</strong>.',
      '<strong>Énoncé 6 :</strong> « Pour que je me promène, il suffit qu\\'il fasse beau » : le beau temps est une condition <em>suffisante</em> $\\equiv b \\Rightarrow p$. Comme $b=0$, l\\'énoncé est <strong>VRAI (1)</strong>.'
    ],
    justification: lang === 'fa' ?
      'تعریف ریاضی جدول درستی شرطی مادی: $[A \\Rightarrow B]_v = 0 \\iff [A]_v = 1 \\text{ et } [B]_v = 0$.' :
      'Définition formelle de l\\'implication matérielle : $[A \\Rightarrow B]_v = 0 \\iff [A]_v = 1 \\text{ et } [B]_v = 0$. Dès que $[A]_v = 0$, $[A \\Rightarrow B]_v = 1$.',
    finalAnswer: lang === 'fa' ?
      '<strong>گزاره‌های برقرار (درست) :</strong> جملات <strong>۱، ۴ و ۶</strong>.<br><strong>گزاره‌های نقض‌شده (نادرست) :</strong> جملات <strong>۲، ۳ و ۵</strong>.' :
      '<strong>Énoncés vérifiés (Vrais) :</strong> <strong>1, 4 et 6</strong>.<br><strong>Énoncés non vérifiés (Faux) :</strong> <strong>2, 3 et 5</strong>.',
    verification: lang === 'fa' ?
      'دقت کنید که جملات ۱، ۴ و ۶ همگی دارای فرم صوری $b \\Rightarrow p$ هستند، در حالی که جملات ۲، ۳ و ۵ دارای فرم صوری $p \\Rightarrow b$ می‌باشند.' :
      'Remarquez la partition parfaite : les phrases 1, 4 et 6 se formalisent toutes par $b \\Rightarrow p$, tandis que les phrases 2, 3 et 5 se formalisent par $p \\Rightarrow b$.',
    trap: lang === 'fa' ?
      'دام مشهور: تصور اینکه چون هوا خوب نیست ($b=0$)، نمی‌توان گفت «اگر هوا خوب باشد قدم می‌زنم». در منطق صوری برعکس است: وقتی شرط محقق نشده، قول ما به هیچ وجه نقض نشده است، پس گزاره برقرار است!' :
      'Le piège cognitif classique consiste à penser que si la prémisse est fausse, la phrase « n\\'a pas de sens ». En logique mathématique, une promesse dont la condition préalable n\\'est pas remplie n\\'est JAMAIS violée, elle est donc réputée vraie.'
  });

  // Exercice 3
  LogicTools.renderExerciseStepper(container.querySelector('#td-exo3-container'), {
    id: 'w01_td_ex3',
    lang: lang,
    title: lang === 'fa' ? 'تمرین ۳ — جدول درستی و معمای جزیره' : 'Exercice 3 – Tables de vérité et énigmes',
    source: 'main_td-etudiants.pdf (p. 3)',
    theme: lang === 'fa' ? 'تم ۱' : 'Thème 1',
    statement: lang === 'fa' ?
      '<p>در جزیره‌ای دورافتاده، هر فرد یا همیشه راست می‌گوید (Véridique) یا همیشه دروغ می‌گوید (Menteur). با دو بومی به نام‌های A و B ملاقات می‌کنیم.</p>' +
      '<p><strong>سؤال ۱ :</strong> فرد A می‌گوید : <em>«B است یک دروغگو»</em>. فرد B می‌گوید : <em>«A و من از یک نوع هستیم (هر دو راستگو یا هر دو دروغگو)»</em>. آیا می‌توان نوع هر یک از افراد A و B را مشخص کرد ؟</p>' +
      '<p><strong>سؤال ۲ :</strong> این مسئله را به کمک متغیرهای گزاره‌ای $a$ (A راستگو است) و $b$ (B راستگو است) مدل کرده و با جدول درستی حل کنید.</p>' :
      '<p>Sur une île, chaque habitant est soit un véridique (dit toujours la vérité), soit un menteur (ment toujours). On rencontre deux habitants A et B.</p>' +
      '<p><strong>Question 1 :</strong> A déclare : « B est un menteur ». B déclare : « A et moi sommes du même type ». Que sont A et B ?</p>' +
      '<p><strong>Question 2 :</strong> Modéliser l\\'énigme avec les variables $a$ (« A est véridique ») et $b$ (« B est véridique ») et résoudre avec une table de vérité.</p>',
    consigne: lang === 'fa' ?
      'اصل مدل‌سازی: ادعای یک فرد درست است اگر و فقط اگر خود آن فرد راستگو باشد. یعنی اگر فرد X ادعای P را بکند، فرمول هم‌ارزی $x \\Leftrightarrow P$ باید همواره برقرار باشد.' :
      'Principe fondamental de modélisation : une déclaration $P$ faite par un individu $X$ est équivalente à la véridicité de cet individu : $x \\Leftrightarrow P$. Le problème consiste à trouver l\\'unique valuation satisfaisant simultanément les déclarations de A et de B.',
    hint: lang === 'fa' ? 
      'سخنان A یعنی : $a \\Leftrightarrow \\neg b$. سخنان B یعنی : $b \\Leftrightarrow (a \\Leftrightarrow b)$. جدولی با ۴ سطر برای a و b رسم کنید.' :
      'Modélisation formelle : déclaration de A $\\implies a \\Leftrightarrow \\neg b$ ; déclaration de B $\\implies b \\Leftrightarrow (a \\Leftrightarrow b)$. Cherchez la seule ligne de la table où ces deux formules valent 1.',
    steps: lang === 'fa' ? [
      '<strong>گام ۱ (فرموله‌سازی) :</strong><br>ادعای A : $F_A = a \\Leftrightarrow \\neg b$<br>ادعای B : $F_B = b \\Leftrightarrow (a \\Leftrightarrow b)$<br>ما به دنبال مدلی برای $F = F_A \\land F_B$ هستیم.',
      '<strong>گام ۲ (ساخت جدول درستی) :</strong><br>' +
      'سطر ۱ ($a=0, b=0$) : $F_A = (0 \\Leftrightarrow 1) = 0$. ناممکن.<br>' +
      'سطر ۲ ($a=0, b=1$) : $F_A = (0 \\Leftrightarrow 0) = 1$. اما برای B : $(a \\Leftrightarrow b) = (0 \\Leftrightarrow 1) = 0$. پس $F_B = (1 \\Leftrightarrow 0) = 0$. ناممکن.<br>' +
      'سطر ۳ ($a=1, b=0$) : $F_A = (1 \\Leftrightarrow 1) = 1$. برای B : $(a \\Leftrightarrow b) = (1 \\Leftrightarrow 0) = 0$. پس $F_B = (0 \\Leftrightarrow 0) = 1$. هر دو درستند!<br>' +
      'سطر ۴ ($a=1, b=1$) : $F_A = (1 \\Leftrightarrow 0) = 0$. ناممکن.'
    ] : [
      '<strong>Étape 1 (Modélisation) :</strong><br>Déclaration de A : $F_A = (a \\Leftrightarrow \\neg b)$<br>Déclaration de B : $F_B = (b \\Leftrightarrow (a \\Leftrightarrow b))$<br>On cherche l\\'unique valuation rendant vraie la formule $F = F_A \\land F_B$.',
      '<strong>Étape 2 (Table de vérité) :</strong><br>' +
      'Ligne 1 ($a=0, b=0$) : $F_A = (0 \\Leftrightarrow 1) = 0$. Invalide.<br>' +
      'Ligne 2 ($a=0, b=1$) : $F_A = (0 \\Leftrightarrow 0) = 1$, mais $(a \\Leftrightarrow b) = 0$, d\\'où $F_B = (1 \\Leftrightarrow 0) = 0$. Invalide.<br>' +
      'Ligne 3 ($a=1, b=0$) : $F_A = (1 \\Leftrightarrow 1) = 1$, et $(a \\Leftrightarrow b) = 0$, d\\'où $F_B = (0 \\Leftrightarrow 0) = 1$. VALIDE !<br>' +
      'Ligne 4 ($a=1, b=1$) : $F_A = (1 \\Leftrightarrow 0) = 0$. Invalide.'
    ],
    justification: lang === 'fa' ?
      'تنها یک ارزش‌گذاری وجود دارد که هر دو رابطه هم‌ارزی را هم‌زمان ارضا کند: $v(a)=1$ و $v(b)=0$.' :
      'La conjonction $F_A \\land F_B$ admet un modèle unique : la valuation $v$ définie par $v(a)=1$ et $v(b)=0$.',
    finalAnswer: lang === 'fa' ?
      '<strong>پاسخ نهایی :</strong> فرد <strong>A راستگو (Véridique)</strong> است و فرد <strong>B دروغگو (Menteur)</strong> است.' :
      '<strong>Conclusion définitive :</strong> <strong>A est un véridique</strong> et <strong>B est un menteur</strong>.',
    verification: lang === 'fa' ?
      'بررسی سازگاری کلامی: A که راستگو است می‌گوید B دروغگوست (که واقعاً هست). B که دروغگوست می‌گوید هر دو هم‌نوعیم (در حالی که یکی راستگو و دیگری دروغگوست، پس B دروغ گفته و ماهیت دروغگویی‌اش ارضا شده است).' :
      'Vérification sémantique : A (véridique) dit que B est un menteur, ce qui est vrai. B (menteur) affirme qu\\'ils sont du même type, ce qui est faux (puisque l\\'un est véridique et l\\'autre menteur), donc B a bien menti.',
    trap: lang === 'fa' ?
      'دام رایج: فراموش کردن رابطه دو‌شرطی بین فرد و ادعایش. اگر فقط بنویسید $a \\Rightarrow \\neg b$، مدل‌سازی ناقص است زیرا فرض نکرده‌اید که اگر A دروغگو باشد سخنش باید برعکس شود.' :
      'Le piège est d\\'écrire une simple implication $a \\Rightarrow \\neg b$ au lieu d\\'une équivalence $a \\Leftrightarrow \\neg b$. Une implication ne contraindrait pas A s\\'il était menteur.'
  });
"""

make_bundle("w01_td", "fr", td_fr, td_interactive)
make_bundle("w01_td", "fa", td_fa, td_interactive)

# ==============================================================================
# WEEK 1: TP (FR & FA) - Exercices 1 & 2 de main_tp-etudiants.pdf
# ==============================================================================

tp_fr = """
<div class="box box-objectives">
  <div class="box-title">Laboratoire TP 1 — Interprétation Récursive & AST en Python</div>
  <p>Source officielle : <code>main_tp-etudiants.pdf</code> (p. 2–3, Thème 1.2.3, Exercices 1 et 2). Ce TP implémente le cœur algorithmique d'un interpréteur de logique propositionnelle en Python : décomposition structurelle, extraction des atomes, et évaluation récursive de formules booléennes.</p>
</div>

<h2 id="w01-tp-spec">1. Spécification Formelle et Représentation</h2>
<p>Les formules sont données sous forme de chaînes de caractères (<code>str</code>) respectant la grammaire :</p>
<ul>
  <li>Constantes : <code>"TRUE"</code> et <code>"FALSE"</code>.</li>
  <li>Atomes : chaînes minuscules (ex : <code>"p"</code>, <code>"bonjour"</code>).</li>
  <li>Connecteur unaire : <code>"NOT F"</code>.</li>
  <li>Connecteurs binaires : <code>"F1 AND F2"</code>, <code>"F1 OR F2"</code>, <code>"F1 IMPLIES F2"</code>.</li>
</ul>

<h2 id="w01-tp-exo1">2. Exercice 1 — Évaluation de formules closes (<code>eval_TF</code>)</h2>
<p>
La fonction <code>decompose(formule: str) -> tuple[str, list[str]]</code> prend une formule et renvoie son connecteur principal et la liste de ses sous-formules :
</p>
<ul>
  <li><code>decompose("TRUE")</code> $\\to$ <code>('TRUE', [])</code></li>
  <li><code>decompose("NOT FALSE")</code> $\\to$ <code>('NOT', ['FALSE'])</code></li>
  <li><code>decompose("(TRUE AND FALSE) OR TRUE")</code> $\\to$ <code>('OR', ['(TRUE AND FALSE)', 'TRUE'])</code></li>
</ul>

<div class="box box-algorithm">
  <div class="box-title">Algorithme d'évaluation récursive (eval_TF)</div>
  <pre><code>def eval_TF(formule: str) -> bool:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # Cas de base : les feuilles
    if connec == "TRUE":
        return True
    if connec == "FALSE":
        return False
        
    # Cas récursif unaire : NOT
    if connec == "NOT":
        return not eval_TF(sous_formules[0])
        
    # Cas récursif binaire : AND, OR, IMPLIES
    if connec == "AND":
        return eval_TF(sous_formules[0]) and eval_TF(sous_formules[1])
    if connec == "OR":
        return eval_TF(sous_formules[0]) or eval_TF(sous_formules[1])
    if connec == "IMPLIES":
        # p => q équivaut à (not p) or q
        val_gauche = eval_TF(sous_formules[0])
        val_droite = eval_TF(sous_formules[1])
        return (not val_gauche) or val_droite
        
    raise ValueError(f"Connecteur inconnu : {connec}")</code></pre>
</div>

<h2 id="w01-tp-exo2">3. Exercice 2 — Extraction d'atomes (<code>genere_fa</code>)</h2>
<p>
Pour évaluer une formule contenant des variables (comme <code>"p AND q"</code>), il faut d'abord isoler l'ensemble de ses atomes pour construire une valuation.
</p>

<div class="box box-algorithm">
  <div class="box-title">Algorithme d'extraction (genere_fa)</div>
  <pre><code>def genere_fa(formule: str) -> set[str]:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # Cas d'une feuille
    if len(sous_formules) == 0:
        if connec in ("TRUE", "FALSE"):
            return set()
        return {connec}
        
    # Cas récursif : union des atomes de tous les sous-arbres
    atomes = set()
    for sf in sous_formules:
        atomes = atomes.union(genere_fa(sf))
    return atomes</code></pre>
</div>

<div class="box box-pourquoi">
  <div class="box-title">Pourquoi je me trompe ? — Feuilles vs Variables</div>
  <p><strong>Difficulté rencontrée :</strong> Confondre feuille de l'arbre et variable propositionnelle.</p>
  <p><strong>Explication :</strong> Les constantes <code>"TRUE"</code> et <code>"FALSE"</code> étiquettent des feuilles (car <code>sous_formules == []</code>), mais ce ne sont PAS des variables propositionnelles ! Il ne faut donc jamais les inclure dans le set retourné par <code>genere_fa</code>.</p>
</div>
"""

tp_fa = """
<div class="box box-objectives">
  <div class="box-title">آزمایشگاه برنامه‌نویسی TP 1 — ارزیابی بازگشتی و ساخت AST در پایتون</div>
  <p>منبع رسمی: جزوه <code>main_tp-etudiants.pdf</code> (صفحه ۲ و ۳، تم ۱.۲.۳، تمرین‌های ۱ و ۲). در این کارگاه، موتور مفسر منطق گزاره‌ای در زبان پایتون طراحی می‌شود: تجزیه ساختاری رشته‌ها، استخراج اتم‌ها و محاسبه بازگشتی ارزش درستی فرمول‌ها.</p>
</div>

<h2 id="w01-tp-spec">۱. مشخصات صوری و نمایش داده‌ها</h2>
<p>فرمول‌ها به صورت رشته‌های متنی (<code>str</code>) مطابق گرامر زیر تعریف می‌شوند:</p>
<ul>
  <li>ثابت‌ها: <code>"TRUE"</code> و <code>"FALSE"</code>.</li>
  <li>اتم‌ها: متغیرهای با حروف کوچک (مانند: <code>"p"</code>, <code>"bonjour"</code>).</li>
  <li>رابط تک‌تایی: <code>"NOT F"</code>.</li>
  <li>رابط‌های دوتایی: <code>"F1 AND F2"</code>, <code>"F1 OR F2"</code>, <code>"F1 IMPLIES F2"</code>.</li>
</ul>

<h2 id="w01-tp-exo1">۲. تمرین ۱ — ارزیابی فرمول‌های بدون متغیر (<code>eval_TF</code>)</h2>
<p>
تابع <code>decompose(formule: str) -> tuple[str, list[str]]</code> رابط اصلی و لیست زیرفرمول‌ها را برمی‌گرداند:
</p>
<ul>
  <li><code>decompose("TRUE")</code> $\\to$ <code>('TRUE', [])</code></li>
  <li><code>decompose("NOT FALSE")</code> $\\to$ <code>('NOT', ['FALSE'])</code></li>
  <li><code>decompose("(TRUE AND FALSE) OR TRUE")</code> $\\to$ <code>('OR', ['(TRUE AND FALSE)', 'TRUE'])</code></li>
</ul>

<div class="box box-algorithm">
  <div class="box-title">الگوریتم بازگشتی ارزیابی (eval_TF)</div>
  <pre><code>def eval_TF(formule: str) -> bool:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # حالت پایه: برگ‌های درخت
    if connec == "TRUE":
        return True
    if connec == "FALSE":
        return False
        
    # حالت بازگشتی تک‌تایی: نقیض
    if connec == "NOT":
        return not eval_TF(sous_formules[0])
        
    # حالت بازگشتی دوتایی: عطف، فصل، شرطی
    if connec == "AND":
        return eval_TF(sous_formules[0]) and eval_TF(sous_formules[1])
    if connec == "OR":
        return eval_TF(sous_formules[0]) or eval_TF(sous_formules[1])
    if connec == "IMPLIES":
        # هم‌ارزی جبری: p => q معادل است با (not p) or q
        val_gauche = eval_TF(sous_formules[0])
        val_droite = eval_TF(sous_formules[1])
        return (not val_gauche) or val_droite
        
    raise ValueError(f"رابط ناشناخته: {connec}")</code></pre>
</div>

<h2 id="w01-tp-exo2">۳. تمرین ۲ — استخراج اتم‌ها (<code>genere_fa</code>)</h2>
<p>
برای ارزیابی فرمول‌های حاوی متغیر، باید ابتدا اتم‌های آن استخراج شوند تا یک دیکشنری ارزش‌گذاری ساخته شود.
</p>

<div class="box box-algorithm">
  <div class="box-title">الگوریتم استخراج اتم‌ها (genere_fa)</div>
  <pre><code>def genere_fa(formule: str) -> set[str]:
    formule = formule.strip()
    connec, sous_formules = decompose(formule)
    
    # حالت برگ بودن گره
    if len(sous_formules) == 0:
        if connec in ("TRUE", "FALSE"):
            return set()
        return {connec}
        
    # حالت بازگشتی: اجتماع اتم‌های تمامی زیردرخت‌ها
    atomes = set()
    for sf in sous_formules:
        atomes = atomes.union(genere_fa(sf))
    return atomes</code></pre>
</div>

<div class="box box-pourquoi">
  <div class="box-title">چرا اشتباه می‌کنم؟ — تفاوت برگ و متغیر گزاره‌ای</div>
  <p><strong>ریشه سردرگمی:</strong> یکی دانستن مفهوم «برگ در درخت نحو» با «متغیر گزاره‌ای».</p>
  <p><strong>توضیح رفع ابهام:</strong> ثابت‌های <code>"TRUE"</code> و <code>"FALSE"</code> نیز در برگ قرار می‌گیرند زیرا فرزندی ندارند (<code>sous_formules == []</code>)، اما آن‌ها ثابت منطقی‌اند نه متغیر گزاره‌ای! بنابراین هرگز نباید در خروجی مجموعه اتم‌های <code>genere_fa</code> قرار گیرند.</p>
</div>
"""

make_bundle("w01_tp", "fr", tp_fr)
make_bundle("w01_tp", "fa", tp_fa)

# ==============================================================================
# WEEK 1: ANNALES (FR & FA)
# ==============================================================================

annales_w1_fr = """
<div class="box box-objectives">
  <div class="box-title">Annales d'Examens Ciblées — Semaine 1</div>
  <p>Sélection de questions réelles tirées des 31 sujets d'examens de la Sorbonne portant sur la syntaxe propositionnelle, les arbres de décomposition et la sémantique de l'implication.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">Examen Partiel 2017–2018 — Exercice 1 (Syntaxe et parenthésage)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">Source : partiel_2017_2018.pdf (p. 1)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">Semaine 1</span><span class="badge">Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>On considère la formule non parenthésée : $$F = p \\Rightarrow q \\lor \\neg r \\land p \\Rightarrow q$$</p>
    <p>1. Donner l'ordre de priorité décroissant des connecteurs utilisés dans cette formule.<br>
    2. Parenthéser complètement la formule $F$ en respectant scrupuleusement ces priorités et l'associativité.<br>
    3. Quel est le connecteur principal de $F$ ? Dessiner son arbre de syntaxe abstraite.</p>
  </div>
  <div class="step-content">
    <strong>Correction complète rédigée Sorbonne :</strong><br>
    1. <strong>Priorités :</strong> $\\neg$ (priorité 1) $>$ $\\land$ (priorité 2) $>$ $\\lor$ (priorité 3) $>$ $\\Rightarrow$ (priorité 4).<br>
    2. <strong>Parenthésage :</strong><br>
    - Négation : $(\\neg r)$<br>
    - Conjonction : $((\\neg r) \\land p)$<br>
    - Disjonction : $(q \\lor ((\\neg r) \\land p))$<br>
    - Double implication (associativité à droite) :<br>
    $$p \\Rightarrow ((q \\lor ((\\neg r) \\land p)) \\Rightarrow q)$$<br>
    3. <strong>Connecteur principal :</strong> La première implication $\\Rightarrow$ (celle de gauche).
  </div>
</div>
"""

annales_w1_fa = """
<div class="box box-objectives">
  <div class="box-title">نمونه سؤالات آزمون‌های نهایی سوربن — هفته ۱</div>
  <p>سؤالات واقعی برگرفته از ۳۱ دوره امتحانات گذشته دانشگاه سوربن در زمینه نحو، اولویت عملگرها، درخت‌های AST و شرطی مادی با حل تشریحی.</p>
</div>

<div class="exo-card">
  <div class="exo-header">
    <div>
      <h3 class="exo-title">امتحان میان‌ترم ۲۰۱۷–۲۰۱۸ — تمرین ۱ (نحو و پرانتزگذاری صوری)</h3>
      <span style="font-size:0.8rem; color:var(--muted);">منبع رسمی: partiel_2017_2018.pdf (صفحه ۱)</span>
    </div>
    <div class="exo-meta-badges"><span class="badge badge-accent">هفته ۱</span><span class="badge">امتحان Partiel</span></div>
  </div>
  <div class="exo-statement">
    <p>فرمول بدون پرانتز زیر را در نظر بگیرید: $$F = p \\Rightarrow q \\lor \\neg r \\land p \\Rightarrow q$$</p>
    <p>۱. ترتیب نزولی اولویت رابط‌های به کار رفته در فرمول را بنویسید.<br>
    ۲. فرمول $F$ را با رعایت دقیق اولویت‌ها و خاصیت شرکت‌پذیری کاملاً پرانتزگذاری کنید.<br>
    ۳. رابط اصلی فرمول کدام است؟ درخت نحو انتزاعی آن را رسم کنید.</p>
  </div>
  <div class="step-content">
    <strong>پاسخ تشریحی مطابق برگه تصحیح سوربن :</strong><br>
    ۱. <strong>اولویت‌ها:</strong> نقیض $\\neg$ (اولویت ۱) $>$ عطف $\\land$ (اولویت ۲) $>$ فصل $\\lor$ (اولویت ۳) $>$ شرطی $\\Rightarrow$ (اولویت ۴).<br>
    ۲. <strong>پرانتزگذاری گام‌به‌گام:</strong><br>
    - ابتدا نقیض: $(\\neg r)$<br>
    - سپس عطف: $((\\neg r) \\land p)$<br>
    - سپس فصل: $(q \\lor ((\\neg r) \\land p))$<br>
    - دو شرطی متوالی (شرکت‌پذیر از راست):<br>
    $$p \\Rightarrow ((q \\lor ((\\neg r) \\land p)) \\Rightarrow q)$$<br>
    ۳. <strong>رابط اصلی:</strong> اولین نماد $\\Rightarrow$ از سمت چپ (ریشه درخت).
  </div>
</div>
"""

make_bundle("w01_annales", "fr", annales_w1_fr)
make_bundle("w01_annales", "fa", annales_w1_fa)

# ==============================================================================
# WEEK 1: REVISION (FR & FA)
# ==============================================================================

revision_w1_fr = """
<div class="box box-objectives">
  <div class="box-title">Fiche de Synthèse Express — Semaine 1</div>
  <p>Tout ce qu'il faut maîtriser par cœur pour réussir les épreuves de TD et d'examen sur le Thème 1.</p>
</div>

<h2 id="w01-rev-regles">1. Les 5 Règles d'Or de la Semaine 1</h2>
<ol>
  <li><strong>L'implication n'est fausse qu'une fois :</strong> $p \\Rightarrow q$ est FAUX $\\iff p=1$ et $q=0$. Si $p=0$, elle est VRAIE sans regarder $q$.</li>
  <li><strong>Associativité à droite de $\\Rightarrow$ :</strong> $p \\Rightarrow q \\Rightarrow r$ signifie TOUJOURS $p \\Rightarrow (q \\Rightarrow r)$.</li>
  <li><strong>Ordre des priorités :</strong> $\\neg > \\land > \\lor > \\Rightarrow > \\Leftrightarrow$.</li>
  <li><strong>Le connecteur principal est la racine de l'AST :</strong> c'est la dernière opération exécutée.</li>
  <li><strong>« Seulement si » introduit la conclusion :</strong> « $p$ seulement si $q$ » se traduit par $p \\Rightarrow q$ (condition nécessaire).</li>
</ol>

<h2 id="w01-rev-quiz">2. Quiz d'Auto-évaluation</h2>
<div class="box box-question">
  <div class="box-title">Question 1 : Valeur de vérité sous prémisse fausse</div>
  <p>Soit $v$ une valuation telle que $v(p)=0$ et $v(q)=0$. Quelle est la valeur de vérité de $(p \\Rightarrow q) \\Rightarrow p$ ?</p>
  <details>
    <summary><strong>Afficher la réponse justifiée</strong></summary>
    <p>1. Calcul de l'implication interne : $p \\Rightarrow q$. Comme $v(p)=0$, elle vaut $1$.<br>
    2. Calcul de l'implication externe : $1 \\Rightarrow p$. Comme $v(p)=0$, on a $1 \\Rightarrow 0 = 0$.<br>
    <strong>Réponse :</strong> La formule s'évalue à <strong>FAUX (0)</strong>.</p>
  </details>
</div>

<div class="box box-question">
  <div class="box-title">Question 2 : Préfixe d'une négation</div>
  <p>Quelle est la notation préfixe de $\\neg(p \\lor q)$ ?</p>
  <details>
    <summary><strong>Afficher la réponse justifiée</strong></summary>
    <p>La racine est $\\neg$, qui a un seul sous-arbre $\\lor p q$. Le parcours préfixe donne donc :<br>
    <code>¬ ∨ p q</code>.</p>
  </details>
</div>
"""

revision_w1_fa = """
<div class="box box-objectives">
  <div class="box-title">برگه جمع‌بندی سریع — هفته ۱</div>
  <p>مفاهیم کلیدی، قوانین طلایی و خلاصه روش‌های حل مسئله تم ۱ برای آمادگی امتحانات سوربن.</p>
</div>

<h2 id="w01-rev-regles">۱. پنج قانون طلایی هفته ۱</h2>
<ol>
  <li><strong>شرطی فقط یک جا نادرست است:</strong> $p \\Rightarrow q$ تنها وقتی غلط است که $p=1$ و $q=0$ باشد. اگر $p=0$ باشد، بدون توجه به $q$ کل شرطی درست است.</li>
  <li><strong>شرکت‌پذیری شرطی از راست است:</strong> عبارت $p \\Rightarrow q \\Rightarrow r$ همواره به صورت $p \\Rightarrow (q \\Rightarrow r)$ پرانتزگذاری می‌شود.</li>
  <li><strong>اولویت عملگرها:</strong> $\\neg > \\land > \\lor > \\Rightarrow > \\Leftrightarrow$.</li>
  <li><strong>رابط اصلی ریشه درخت AST است:</strong> این آخرین عملیاتی است که در محاسبه فرمول اعمال می‌گردد.</li>
  <li><strong>«تنها اگر» تالی را معرفی می‌کند:</strong> عبارت «$p$ تنها اگر $q$» به صورت $p \\Rightarrow q$ ترجمه می‌شود (شرط لازم).</li>
</ol>

<h2 id="w01-rev-quiz">۲. آزمونک خودسنجی</h2>
<div class="box box-question">
  <div class="box-title">سؤال ۱ : محاسبه مقدار درستی با مقدم نادرست</div>
  <p>فرض کنید ارزش‌گذاری $v$ داشته باشیم با $v(p)=0$ و $v(q)=0$. ارزش فرمول $(p \\Rightarrow q) \\Rightarrow p$ چقدر است ؟</p>
  <details>
    <summary><strong>مشاهده پاسخ تشریحی</strong></summary>
    <p>۱. محاسبه شرطی داخلی : چون $p=0$ است، $p \\Rightarrow q$ برابر $1$ می‌شود.<br>
    ۲. محاسبه شرطی بیرونی : داریم $1 \\Rightarrow p$. چون $p=0$ است، عبارت $1 \\Rightarrow 0$ برابر با $0$ خواهد شد.<br>
    <strong>پاسخ:</strong> ارزش نهایی فرمول <strong>نادرست (0)</strong> است.</p>
  </details>
</div>

<div class="box box-question">
  <div class="box-title">سؤال ۲ : نشانه‌گذاری پیشوندی نقیض</div>
  <p>نشانه‌گذاری پیشوندی فرمول $\\neg(p \\lor q)$ چیست ؟</p>
  <details>
    <summary><strong>مشاهده پاسخ تشریحی</strong></summary>
    <p>ریشه $\\neg$ است که فرزند آن $\\lor p q$ می‌باشد. بنابراین عبارت پیشوندی برابر است با :<br>
    <code>¬ ∨ p q</code>.</p>
  </details>
</div>
"""

make_bundle("w01_revision", "fr", revision_w1_fr)
make_bundle("w01_revision", "fa", revision_w1_fa)

print("Week 1 generation complete!")

