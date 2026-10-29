#!/usr/bin/env python3
import os

W01 = '/home/mnasimi/sorbonne/Logic_Academy/content/w01'
os.makedirs(W01, exist_ok=True)

# Generate cours.fr.html and cours.fa.html with strict parity
fr = """
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>Thème 1 : Syntaxe et Sémantique Propositionnelle</h1>
  <p class="lead">Fondements mathématiques du calcul des propositions : grammaire inductive, arbres de syntaxe abstraite, conventions d'évaluation de la Sorbonne et modélisation du raisonnement.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du cours</h3>
  <ul>
    <li><a href="#sec1">1. Introduction et motivations en informatique</a></li>
    <li><a href="#sec2">2. Syntaxe formelle et arbres syntaxiques (AST)</a></li>
    <li><a href="#sec3">3. Règles de priorité et parenthésage Sorbonne</a></li>
    <li><a href="#sec4">4. Sémantique et algèbre des valeurs de vérité</a></li>
    <li><a href="#sec5">5. Tables de vérité et classification des formules</a></li>
    <li><a href="#sec6">6. Modélisation rigoureuse du langage naturel et implication</a></li>
    <li><a href="#sec7">7. Laboratoire interactif</a></li>
  </ul>
</div>

<h2 id="sec1">1. Introduction et motivations en informatique</h2>

<div class="box info">
  <h4>Pourquoi la logique formelle est le cœur de l'informatique</h4>
  <p>En informatique fondamentale, un ordinateur ne manipule pas des idées vagues mais des états binaires stricts ({{ 0 }} et {{ 1 }}). La logique propositionnelle constitue le socle mathématique indispensable à :</p>
  <ul>
    <li><strong>La conception des circuits numériques :</strong> modélisation des portes logiques (ET, OU, NON) et simplification booléenne par tables de Karnaugh.</li>
    <li><strong>L'écriture de conditions logicielles :</strong> expressions conditionnelles <code>if (A &amp;&amp; !B || C)</code> dans les langages de programmation.</li>
    <li><strong>La vérification formelle de programmes :</strong> prouver mathématiquement qu'un algorithme critique (aéronautique, cryptographie) ne contient aucun bug.</li>
    <li><strong>L'intelligence artificielle et la résolution de contraintes :</strong> solveurs SAT/SMT utilisés quotidiennement pour résoudre des problèmes NP-complets industriels.</li>
  </ul>
</div>

<h2 id="sec2">2. Syntaxe formelle et arbres syntaxiques (AST)</h2>

<div class="box def">
  <h4>Définition inductive de l'ensemble des formules propositionnelles {{ \mathcal{F}_p(\mathcal{P}_0) }}</h4>
  <p>Soit {{ \mathcal{P}_0 = \{p, q, r, p_0, p_1, \dots\} }} un ensemble dénombrable de <strong>symboles de propositions</strong> (ou atomes). L'ensemble {{ \mathcal{F}_p(\mathcal{P}_0) }} des formules propositionnelles bien formées est défini inductivement par les trois règles suivantes (Sorbonne Cours 1, Slide 14) :</p>
  <ol>
    <li><strong>Base :</strong> Les constantes logiques {{ \text{true} }} (notée aussi {{ \top }}) et {{ \text{false} }} (notée aussi {{ \bot }}) appartiennent à {{ \mathcal{F}_p(\mathcal{P}_0) }}. Tout symbole de proposition {{ p \in \mathcal{P}_0 }} appartient à {{ \mathcal{F}_p(\mathcal{P}_0) }}.</li>
    <li><strong>Induction unaire :</strong> Si {{ F \in \mathcal{F}_p(\mathcal{P}_0) }}, alors {{ (\neg F) \in \mathcal{F}_p(\mathcal{P}_0) }} (négation).</li>
    <li><strong>Induction binaire :</strong> Si {{ F_1, F_2 \in \mathcal{F}_p(\mathcal{P}_0) }}, alors :
      <ul>
        <li>{{ (F_1 \land F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (conjonction : « ET »)</li>
        <li>{{ (F_1 \lor F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (disjonction : « OU »)</li>
        <li>{{ (F_1 \Rightarrow F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (implication : « IMPLIQUE »)</li>
        <li>{{ (F_1 \Leftrightarrow F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (équivalence : « ÉQUIVAUT »)</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box method">
  <h4>Arbre de Syntaxe Abstraite (AST — Abstract Syntax Tree)</h4>
  <p>Toute formule bien formée possède une représentation unique sous forme d'arbre ordonné :</p>
  <ul>
    <li>Les <strong>feuilles</strong> portent les symboles atomiques ({{ p, q, r }}) ou les constantes ({{ \top, \bot }}).</li>
    <li>Les <strong>nœuds internes</strong> portent les connecteurs logiques ({{ \neg, \land, \lor, \Rightarrow, \Leftrightarrow }}).</li>
    <li>La <strong>racine</strong> de l'arbre est le <em>connecteur principal</em> de la formule (l'opération effectuée en tout dernier lieu).</li>
  </ul>
  <p>Les parcours d'arbres permettent d'exprimer la formule sous différentes notations :</p>
  <ul>
    <li><strong>Parcours infixe :</strong> sous-arbre gauche, nœud racine, sous-arbre droit. C'est la notation standard avec parenthèses : <code>(p &and; q) &rArr; r</code>.</li>
    <li><strong>Parcours préfixe (notation polonaise de Łukasiewicz) :</strong> nœud racine, sous-arbre gauche, sous-arbre droit. Exemple : <code>&rArr; &and; p q r</code>. Cette notation a l'immense avantage d'être totalement <em>dénuée d'ambiguïté sans jamais nécessiter la moindre parenthèse</em> !</li>
  </ul>
</div>

<div class="w-ast" data-formula="~(p & (q => ((q | r) & q)))"></div>

<h2 id="sec3">3. Règles de priorité et parenthésage Sorbonne</h2>

<div class="box warn">
  <h4>Priorité décroissante des opérateurs et associativité à droite</h4>
  <p>Pour alléger l'écriture des formules et supprimer les parenthèses superflues, le cours de Logique de Sorbonne Université fixe deux conventions impératives (Cours 1, Slide 11) :</p>
  <ol>
    <li><strong>Ordre de priorité décroissante :</strong>
      <div style="text-align:center; font-weight:bold; margin: 10px 0; font-size:1.1em;">
        {{ \neg \quad > \quad \land \quad > \quad \lor \quad > \quad \Rightarrow \quad > \quad \Leftrightarrow }}
      </div>
      La négation {{ \neg }} lie plus fort que tout, suivie du ET {{ \land }}, puis du OU {{ \lor }}, puis de l'implication {{ \Rightarrow }}, et enfin de l'équivalence {{ \Leftrightarrow }}.
    </li>
    <li><strong>Convention d'associativité en cas de priorité égale :</strong>
      <em>La sous-formule de droite est toujours prioritaire !</em> (Associativité à droite).
      <br/>Exemples fondamentaux :
      <ul>
        <li>{{ A \land B \land C \equiv A \land (B \land C) }}</li>
        <li>{{ A \Rightarrow B \Rightarrow C \equiv A \Rightarrow (B \Rightarrow C) }}</li>
      </ul>
      <p><strong>ATTENTION PIÈGE D'EXAMEN :</strong> En arithmétique ou dans certains langages de programmation, l'évaluation se fait souvent de gauche à droite. À la Sorbonne en UL2IN007, <code>A &rArr; B &rArr; C</code> signifie impérativement <code>A &rArr; (B &rArr; C)</code> et JAMAIS <code>(A &rArr; B) &rArr; C</code> !</p>
    </li>
  </ol>
</div>

<h2 id="sec4">4. Sémantique et algèbre des valeurs de vérité</h2>

<div class="box def">
  <h4>Interprétation et fonction d'évaluation inductive {{ [F]^I }}</h4>
  <p>La syntaxe décrit des chaînes de caractères sans signification. La <strong>sémantique</strong> leur donne un sens de vérité en les reliant à l'ensemble booléen {{ \mathbb{B} = \{0, 1\} }}.</p>
  <ul>
    <li>Une <strong>interprétation</strong> (ou valuation) est une fonction {{ I : \mathcal{P}_0 \to \{0, 1\} }} qui associe à chaque symbole de proposition une valeur de vérité ({{ 0 }} pour Faux, {{ 1 }} pour Vrai).</li>
    <li>La valeur de vérité d'une formule composée {{ F }} sous l'interprétation {{ I }}, notée {{ [F]^I }}, est calculée par induction sur la structure de son AST :
      <ul>
        <li>{{ [\text{true}]^I = 1 }}, {{ [\text{false}]^I = 0 }}</li>
        <li>{{ [p]^I = I(p) }} pour tout symbole atomique {{ p }}</li>
        <li>{{ [\neg F]^I = 1 - [F]^I }}</li>
        <li>{{ [F_1 \land F_2]^I = \min([F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \lor F_2]^I = \max([F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \Rightarrow F_2]^I = \max(1 - [F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \Leftrightarrow F_2]^I = 1 }} si {{ [F_1]^I = [F_2]^I }}, et {{ 0 }} sinon.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="w-eval" data-formula="(p & q) => (p | r)"></div>

<h2 id="sec5">5. Tables de vérité et classification des formules</h2>

<div class="box method">
  <h4>Construction méthodique d'une table de vérité</h4>
  <p>Une formule comportant {{ n }} variables distinctes admet exactement {{ 2^n }} interprétations différentes. Pour construire une table irréprochable :</p>
  <ol>
    <li>Lister les variables propositionnelles par ordre alphabétique en tête des premières colonnes.</li>
    <li>Énumérer les lignes dans l'ordre binaire naturel (de {{ 00\dots0 }} à {{ 11\dots1 }}).</li>
    <li>Créer une colonne pour chaque sous-formule stricte, de la plus petite vers la plus grande, en respectant la décomposition de l'AST.</li>
    <li>La toute dernière colonne correspond au connecteur principal de la formule complète.</li>
  </ol>
</div>

<div class="w-tt" data-formula="(p & q) & ((q => p) | ~(p | q))"></div>

<div class="box tip">
  <h4>Classification sémantique tripartite des formules</h4>
  <ul>
    <li><strong>Formule satisfiable (ou consistante) :</strong> Il existe au moins une interprétation {{ I }} telle que {{ [F]^I = 1 }}. L'interprétation {{ I }} est appelée un <em>modèle</em> de {{ F }}.</li>
    <li><strong>Formule valide (ou tautologie, notée {{ \models F }}) :</strong> Pour <em>toute</em> interprétation {{ I }}, on a {{ [F]^I = 1 }}. La formule est vraie quelles que soient les circonstances.</li>
    <li><strong>Formule insatisfiable (ou antilogie / contradiction) :</strong> Pour <em>toute</em> interprétation {{ I }}, on a {{ [F]^I = 0 }}. La formule ne possède aucun modèle.</li>
  </ul>
</div>

<h2 id="sec6">6. Modélisation rigoureuse du langage naturel et implication</h2>

<div class="box warn">
  <h4>L'implication matérielle {{ A \Rightarrow B }} : vérité et paradoxes apparents</h4>
  <p>Par définition sémantique, {{ A \Rightarrow B }} équivaut strictement à {{ \neg A \lor B }}. Elle n'est fausse que dans un seul et unique cas : <strong>quand la prémisse {{ A }} est Vraie et que la conclusion {{ B }} est Fausse</strong>.</p>
  <p><em>Principe d'explosion (Ex falso quodlibet) :</em> Dès lors que {{ A }} est faux ({{ I(A)=0 }}), l'implication {{ A \Rightarrow B }} est <strong>automatiquement VRAIE</strong>, quelle que soit la valeur de vérité de {{ B }} !</p>
  <p><em>Exemple frappant :</em> L'affirmation « S'il pleut des vaches, alors la Lune est en fromage vert » est une implication formellement VRAIE en logique classique, car son hypothèse est fausse.</p>
</div>

<div class="box method">
  <h4>Dictionnaire de traduction : Langage naturel &harr; Logique propositionnelle</h4>
  <p>Ce tableau récapitule les tournures françaises classiques et leur formalisation exacte :</p>
  <table class="logic-table" style="width:100%; margin:12px 0;">
    <thead>
      <tr>
        <th>Énoncé en français</th>
        <th>Sens mathématique</th>
        <th>Traduction formelle</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>« Si A, alors B » / « B dès que A »</td>
        <td>A entraîne B</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>« A seulement si B » / « A uniquement si B »</td>
        <td>Si B n'est pas réalisé, A ne peut l'être ({{ \neg B \Rightarrow \neg A }})</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>« Pour que B, il faut que A » (condition nécessaire)</td>
        <td>A est obligatoire pour avoir B</td>
        <td>{{ B \Rightarrow A }}</td>
      </tr>
      <tr>
        <td>« Pour que B, il suffit que A » (condition suffisante)</td>
        <td>La présence de A garantit B</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>« A si et seulement si B » / « A équivaut à B »</td>
        <td>Condition nécessaire ET suffisante</td>
        <td>{{ A \Leftrightarrow B }}</td>
      </tr>
      <tr>
        <td>« Ni A ni B »</td>
        <td>Ni l'un ni l'autre n'est vrai</td>
        <td>{{ \neg A \land \neg B \equiv \neg(A \lor B) }}</td>
      </tr>
      <tr>
        <td>« Au moins l'un des deux (A ou B) »</td>
        <td>Disjonction inclusive</td>
        <td>{{ A \lor B }}</td>
      </tr>
      <tr>
        <td>« Au plus l'un des deux (A ou B) »</td>
        <td>Ils ne peuvent pas être vrais ensemble</td>
        <td>{{ \neg(A \land B) \equiv \neg A \lor \neg B }}</td>
      </tr>
      <tr>
        <td>« Exactement l'un des deux (OU exclusif) »</td>
        <td>L'un est vrai mais pas les deux</td>
        <td>{{ (A \lor B) \land \neg(A \land B) \equiv \neg(A \Leftrightarrow B) }}</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec7">7. Laboratoire interactif</h2>

<div class="box tip">
  <h4>Bac à sable de calcul propositionnel</h4>
  <p>Saisissez n'importe quelle formule pour visualiser son arbre de syntaxe, sa table de vérité, et analyser ses propriétés sémantiques en temps réel.</p>
</div>

<div class="w-lab" data-formula="(p => q) & (q => r) => (p => r)"></div>
"""

fa = """
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>فصل ۱: نحو و معناشناسی منطق گزاره‌ای</h1>
  <p class="lead">مبانی ریاضیاتی حساب گزاره‌ها: دستور زبان استقرایی، درخت‌های نحو انتزاعی (AST)، قواعد اولویت دانشگاه سوربن و مدل‌سازی منطقی استدلال‌ها.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب درس</h3>
  <ul>
    <li><a href="#sec1">۱. مقدمه و چرایی منطق در علوم کامپیوتر</a></li>
    <li><a href="#sec2">۲. نحو صوری و درخت‌های نحو انتزاعی (AST)</a></li>
    <li><a href="#sec3">۳. قواعد اولویت عملگرها و پرانتزگذاری در سوربن</a></li>
    <li><a href="#sec4">۴. معناشناسی و جبر ارزش‌های درستی</a></li>
    <li><a href="#sec5">۵. جدول‌های درستی و رده‌بندی صوری فرمول‌ها</a></li>
    <li><a href="#sec6">۶. مدل‌سازی دقیق زبان طبیعی و عملگر شرطی</a></li>
    <li><a href="#sec7">۷. آزمایشگاه تعاملی محاسبات منطقی</a></li>
  </ul>
</div>

<h2 id="sec1">1. Introduction et motivations en informatique</h2>

<div class="box info">
  <h4>چرا منطق صوری قلب تپنده علوم کامپیوتر است؟</h4>
  <p>در مبانی علوم کامپیوتر، ماشین با مفاهیم مبهم کار نمی‌کند بلکه با وضعیت‌های قطعی دوتایی ({{ 0 }} و {{ 1 }}) سر و کار دارد. منطق گزاره‌ای زیربنای ریاضی ضروری برای حوزه‌های زیر است:</p>
  <ul>
    <li><strong>طراحی مدارهای دیجیتال:</strong> مدل‌سازی گیت‌های منطقی (AND, OR, NOT) و ساده‌سازی توابع بولی با جدول‌های کارنو.</li>
    <li><strong>نوشتن عبارات شرطی در برنامه‌نویسی:</strong> عبارت‌های کنترلی نظیر <code>if (A &amp;&amp; !B || C)</code> در تمام زبان‌های نرم‌افزاری.</li>
    <li><strong>اثبات درستی برنامه‌ها (Formal Verification):</strong> اثبات ریاضی این‌که سامانه‌های حیاتی (هوانوردی، رمزنگاری) فاقد هرگونه باگ هستند.</li>
    <li><strong>هوش مصنوعی و حل مسائل قیود:</strong> حل‌کننده‌های مدرن SAT/SMT که روزانه مسائل عظیم در ابعاد صنعتی را حل می‌کنند.</li>
  </ul>
</div>

<h2 id="sec2">2. Syntaxe formelle et arbres syntaxiques (AST)</h2>

<div class="box def">
  <h4>تعریف استقرایی مجموعه فرمول‌های گزاره‌ای {{ \mathcal{F}_p(\mathcal{P}_0) }}</h4>
  <p>فرض کنید {{ \mathcal{P}_0 = \{p, q, r, p_0, p_1, \dots\} }} یک مجموعه شمارا از <strong>نمادهای گزاره‌ای</strong> (اتم‌ها) باشد. مجموعه {{ \mathcal{F}_p(\mathcal{P}_0) }} شامل تمامی فرمول‌های خوش‌ساخت گزاره‌ای به روش استقرایی با سه قاعده زیر تعریف می‌شود (اسلاید ۱۴ درس سوربن):</p>
  <ol>
    <li><strong>پایه استقرا:</strong> ثابت‌های درستی {{ \text{true} }} (با نماد {{ \top }}) و نادرستی {{ \text{false} }} (با نماد {{ \bot }}) عضو {{ \mathcal{F}_p(\mathcal{P}_0) }} هستند. هر نماد گزاره‌ای {{ p \in \mathcal{P}_0 }} نیز عضو {{ \mathcal{F}_p(\mathcal{P}_0) }} است.</li>
    <li><strong>گام استقرای تک‌تایی:</strong> اگر {{ F \in \mathcal{F}_p(\mathcal{P}_0) }} باشد، آنگاه نقیض آن {{ (\neg F) \in \mathcal{F}_p(\mathcal{P}_0) }} است.</li>
    <li><strong>گام استقرای دوتایی:</strong> اگر {{ F_1, F_2 \in \mathcal{F}_p(\mathcal{P}_0) }} باشند، آنگاه:
      <ul>
        <li>{{ (F_1 \land F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (عطف منطقی: «و»)</li>
        <li>{{ (F_1 \lor F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (فصل منطقی: «یا»)</li>
        <li>{{ (F_1 \Rightarrow F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (شرطی / استلزام: «نتیجه می‌دهد»)</li>
        <li>{{ (F_1 \Leftrightarrow F_2) \in \mathcal{F}_p(\mathcal{P}_0) }} (دوشرطی: «هم‌ارز است با»)</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box method">
  <h4>درخت نحو انتزاعی (AST — Abstract Syntax Tree)</h4>
  <p>هر فرمول خوش‌ساخت دارای یک نمایش یکتا به صورت درخت مرتب است:</p>
  <ul>
    <li><strong>برگ‌ها</strong> دربرگیرنده نمادهای گزاره‌ای اتمی ({{ p, q, r }}) یا مقادیر ثابت ({{ \top, \bot }}) هستند.</li>
    <li><strong>گره‌های درونی</strong> رابط‌های منطقی ({{ \neg, \land, \lor, \Rightarrow, \Leftrightarrow }}) را نشان می‌دهند.</li>
    <li><strong>ریشه درخت</strong> نشان‌دهنده <em>رابط اصلی</em> فرمول است (عملیاتی که در آخرین گام ارزیابی می‌شود).</li>
  </ul>
  <p>پیمایش‌های درختی امکان نمایش فرمول در قالب‌های مختلف را فراهم می‌کنند:</p>
  <ul>
    <li><strong>پیمایش میان‌ترتیب (Infix):</strong> زیردرخت چپ، گره ریشه، زیردرخت راست. همان فرمول‌نویسی معمول همراه با پرانتز است: <code>(p &and; q) &rArr; r</code>.</li>
    <li><strong>پیمایش پیش‌ترتیب (Prefix - نمادگذاری پولندی لوکاسیویچ):</strong> گره ریشه، زیردرخت چپ، زیردرخت راست. مانند: <code>&rArr; &and; p q r</code>. این فرمت این مزیت شگفت‌انگیز را دارد که بدون نیاز به هیچ پرانتزی، کاملاً <em>فاقد هرگونه ابهام</em> است!</li>
  </ul>
</div>

<div class="w-ast" data-formula="~(p & (q => ((q | r) & q)))"></div>

<h2 id="sec3">3. Règles de priorité et parenthésage Sorbonne</h2>

<div class="box warn">
  <h4>اولویت کاهشی عملگرها و شرکت‌پذیری از راست در دانشگاه سوربن</h4>
  <p>برای خلاصه‌سازی فرمول‌ها و حذف پرانتزهای دست‌وپاگیر، کورس منطق دانشگاه سوربن دو قاعده سخت‌گیرانه وضع کرده است (اسلاید ۱۱ درس):</p>
  <ol>
    <li><strong>ترتیب اولویت عملگرها از قوی به ضعیف:</strong>
      <div style="text-align:center; font-weight:bold; margin: 10px 0; font-size:1.1em;" dir="ltr">
        {{ \neg \quad > \quad \land \quad > \quad \lor \quad > \quad \Rightarrow \quad > \quad \Leftrightarrow }}
      </div>
      نقیض {{ \neg }} قوی‌ترین اتصال را دارد، سپس عطف {{ \land }}، سپس فصل {{ \lor }}، سپس استلزام {{ \Rightarrow }}، و در نهایت دوشرطی {{ \Leftrightarrow }}.
    </li>
    <li><strong>قاعده شرکت‌پذیری در صورت اولویت برابر:</strong>
      <em>زیرفرمول سمت راست همیشه اولویت دارد!</em> (شرکت‌پذیری از راست).
      <br/>مثال‌های اساسی:
      <ul>
        <li>{{ A \land B \land C \equiv A \land (B \land C) }}</li>
        <li>{{ A \Rightarrow B \Rightarrow C \equiv A \Rightarrow (B \Rightarrow C) }}</li>
      </ul>
      <p><strong>هشدار مهم و تله امتحانی:</strong> در حساب معمولی یا برخی زبان‌ها ارزیابی از چپ به راست است. اما در آزمون‌های سوربن، عبارت <code>A &rArr; B &rArr; C</code> اجباراً به معنای <code>A &rArr; (B &rArr; C)</code> است و هرگز به معنای <code>(A &rArr; B) &rArr; C</code> نخواهد بود!</p>
    </li>
  </ol>
</div>

<h2 id="sec4">4. Sémantique et algèbre des valeurs de vérité</h2>

<div class="box def">
  <h4>تعبیر (ارزیابی) و تابع معنایی استقرایی {{ [F]^I }}</h4>
  <p>نحو صرفاً رشته‌هایی از حروف بدون معنا تولید می‌کند. <strong>معناشناسی</strong> با متصل کردن فرمول‌ها به مجموعه بولی {{ \mathbb{B} = \{0, 1\} }} به آن‌ها مفهوم حقیقت می‌بخشد.</p>
  <ul>
    <li>یک <strong>تعبیر</strong> (یا ارزیابی / مدل) تابعی است به شکل {{ I : \mathcal{P}_0 \to \{0, 1\} }} که به هر نماد اتمی، یک مقدار درستی ({{ 0 }} برای نادرست و {{ 1 }} برای درست) نسبت می‌دهد.</li>
    <li>ارزش درستی یک فرمول ترکیبی {{ F }} تحت تعبیر {{ I }} که با {{ [F]^I }} نشان داده می‌شود، به روش استقرایی روی ساختار درخت نحو ارزیابی می‌گردد:
      <ul>
        <li>{{ [\text{true}]^I = 1 }} و {{ [\text{false}]^I = 0 }}</li>
        <li>برای هر نماد اتمی {{ p }} داریم: {{ [p]^I = I(p) }}</li>
        <li>{{ [\neg F]^I = 1 - [F]^I }}</li>
        <li>{{ [F_1 \land F_2]^I = \min([F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \lor F_2]^I = \max([F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \Rightarrow F_2]^I = \max(1 - [F_1]^I, [F_2]^I) }}</li>
        <li>{{ [F_1 \Leftrightarrow F_2]^I = 1 }} اگر و تنها اگر {{ [F_1]^I = [F_2]^I }} باشد، وگرنه برابر {{ 0 }} است.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="w-eval" data-formula="(p & q) => (p | r)"></div>

<h2 id="sec5">5. Tables de vérité et classification des formules</h2>

<div class="box method">
  <h4>روش گام‌به‌گام ساخت جدول درستی دانشگاهی</h4>
  <p>فرمول با {{ n }} متغیر مستقل دقیقاً دارای {{ 2^n }} سطر تعبیر مختلف است. برای ساخت جدولی استاندارد و نمره‌آور:</p>
  <ol>
    <li>متغیرهای گزاره‌ای را به ترتیب الفبا در ستون‌های نخست قرار دهید.</li>
    <li>سطرها را بر اساس ترتیب طبیعی دودویی پر کنید (از {{ 00\dots0 }} تا {{ 11\dots1 }}).</li>
    <li>برای هر زیرفرمول سره بر اساس ساختار درخت AST، از کوچک‌ترین به بزرگ‌ترین ستون‌های میانی تشکیل دهید.</li>
    <li>آخرین ستون، نتیجه رابط اصلی فرمول نهایی را به نمایش می‌گذارد.</li>
  </ol>
</div>

<div class="w-tt" data-formula="(p & q) & ((q => p) | ~(p | q))"></div>

<div class="box tip">
  <h4>دسته‌بندی سه‌گانه معنایی فرمول‌ها</h4>
  <ul>
    <li><strong>فرمول صدق‌پذیر (Satisfiable):</strong> حداقل یک تعبیر {{ I }} وجود دارد به گونه‌ای که {{ [F]^I = 1 }} باشد. تعبیر {{ I }} را یک <em>مدل</em> برای {{ F }} می‌نامند.</li>
    <li><strong>فرمول معتبر یا توتولوژی (Tautology / Valid - نماد {{ \models F }}):</strong> تحت <em>تمامی</em> تعبیرهای ممکن {{ I }}، همواره {{ [F]^I = 1 }} است. فرمولی که تحت هر شرایطی در جهان حقیقت دارد.</li>
    <li><strong>فرمول ناسازگار یا تناقض (Contradiction / Unsatisfiable):</strong> تحت <em>هر</em> تعبیر دلخواه {{ I }}، مقدار {{ [F]^I = 0 }} است و هیچ مدلی ندارد.</li>
  </ul>
</div>

<h2 id="sec6">6. Modélisation rigoureuse du langage naturel et implication</h2>

<div class="box warn">
  <h4>شرطی مادی {{ A \Rightarrow B }} : حقیقت و تناقض‌های ظاهری آن</h4>
  <p>از نظر معنایی، {{ A \Rightarrow B }} دقیقاً هم‌ارز با {{ \neg A \lor B }} است. این فرمول تنها در یک حالت نادرست می‌شود: <strong>مقدم {{ A }} درست باشد ولی نتیجه {{ B }} نادرست باشد</strong>.</p>
  <p><em>اصل انفجار (Ex falso quodlibet):</em> هرگاه فرض مقدم {{ A }} نادرست باشد ({{ I(A)=0 }})، کل گزاره شرطی {{ A \Rightarrow B }} <strong>به طور خودکار درست</strong> خواهد بود، فارغ از این‌که گزاره دوم {{ B }} چه باشد!</p>
  <p><em>مثال مشهور:</em> عبارت «اگر گاوها پرواز کنند، ماه از پنیر سبز ساخته شده است» در منطق کلاسیک گزاره‌ای کاملاً «درست» محسوب می‌شود زیرا فرض اولیه آن باطل است.</p>
</div>

<div class="box method">
  <h4>فرهنگ واژگان تبدیل عبارات زبان به فرمول‌های منطقی</h4>
  <p>جدول زیر الگوهای زبانی معمول و ترجمه دقیق آن‌ها را نشان می‌دهد:</p>
  <table class="logic-table" style="width:100%; margin:12px 0;">
    <thead>
      <tr>
        <th>عبارت در زبان روزمره</th>
        <th>مفهوم ریاضی</th>
        <th>فرمول منطقی صوری</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>«اگر A آنگاه B» / «به محض وقوع A، گزاره B رخ می‌دهد»</td>
        <td>A نتیجه می‌دهد B</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>«A فقط اگر B» (تنها در صورتی که B باشد، A می‌تواند باشد)</td>
        <td>اگر B نباشد، A هم نیست ({{ \neg B \Rightarrow \neg A }})</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>«برای B، لازم است که A باشد» (شرط لازم / nécessaire)</td>
        <td>A برای داشتن B اجباری است</td>
        <td>{{ B \Rightarrow A }}</td>
      </tr>
      <tr>
        <td>«برای B، کافی است که A باشد» (شرط کافی / suffisant)</td>
        <td>وجود A تضمین‌کننده وقوع B است</td>
        <td>{{ A \Rightarrow B }}</td>
      </tr>
      <tr>
        <td>«A اگر و فقط اگر B» / «A هم‌ارز با B»</td>
        <td>شرط لازم و کافی دوطرفه</td>
        <td>{{ A \Leftrightarrow B }}</td>
      </tr>
      <tr>
        <td>«نه A و نه B» (هیچ‌کدام)</td>
        <td>نفی هر دو حالت</td>
        <td>{{ \neg A \land \neg B \equiv \neg(A \lor B) }}</td>
      </tr>
      <tr>
        <td>«حداقل یکی از دو گزاره (A یا B)»</td>
        <td>فصل منطقی شمول‌پذیر</td>
        <td>{{ A \lor B }}</td>
      </tr>
      <tr>
        <td>«حداکثر یکی از دو گزاره (A یا B)»</td>
        <td>نمی‌توانند هم‌زمان درست باشند</td>
        <td>{{ \neg(A \land B) \equiv \neg A \lor \neg B }}</td>
      </tr>
      <tr>
        <td>«دقیقاً یکی از دو گزاره (یا منحصراً این، یا آن)»</td>
        <td>یا مانعة‌الجمع (XOR)</td>
        <td>{{ (A \lor B) \land \neg(A \land B) \equiv \neg(A \Leftrightarrow B) }}</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec7">7. Laboratoire interactif</h2>

<div class="box tip">
  <h4>میزکار تعاملی محاسبات گزاره‌ای</h4>
  <p>فرمول دلخواه خود را وارد کنید تا هم‌زمان درخت نحو، جدول درستی کامل و تحلیل خواص معنایی آن محاسبه و رسم شود.</p>
</div>

<div class="w-lab" data-formula="(p => q) & (q => r) => (p => r)"></div>
"""

open(os.path.join(W01, 'cours.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W01, 'cours.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("cours.fr.html and cours.fa.html written.")
