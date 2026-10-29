#!/usr/bin/env python3
"""Authoring generator for Week 2 Cours (Thème 2).
Covers:
- Algèbre de Boole (B, ., +, -)
- Traduction [F]^I et raisonnement équationnel pas à pas
- Validité, satisfiabilité sans tables de vérité
- Conséquence sémantique H |= F et contre-modèles
- Équivalence logique F1 =| F2
"""
import os

W02 = '/home/mnasimi/sorbonne/Logic_Academy/content/w02'
os.makedirs(W02, exist_ok=True)

fr = """
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>Thème 2 : Expressions Booléennes et Conséquence Sémantique</h1>
  <p class="lead">Le calcul propositionnel sans tables de vérité : algèbre de Boole, raisonnement équationnel formel, satisfiabilité, validité et conséquence sémantique {{ \mathcal{H} \models F }}.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du cours</h3>
  <ul>
    <li><a href="#sec1">1. Au-delà des tables de vérité : l'explosion combinatoire</a></li>
    <li><a href="#sec2">2. L'Algèbre de Boole minimale {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }}</a></li>
    <li><a href="#sec3">3. Traduction inductive et raisonnement équationnel sur {{ [F]^I }}</a></li>
    <li><a href="#sec4">4. Validité, satisfiabilité et insatisfiabilité sans table de vérité</a></li>
    <li><a href="#sec5">5. Conséquence sémantique formelle ({{ \mathcal{H} \models F }}) et contre-modèles</a></li>
    <li><a href="#sec6">6. Équivalence logique et théorème de déduction sémantique</a></li>
    <li><a href="#sec7">7. Laboratoire de déduction et équivalence</a></li>
  </ul>
</div>

<h2 id="sec1">1. Au-delà des tables de vérité : l'explosion combinatoire</h2>

<div class="box info">
  <h4>Pourquoi abandonner les tables de vérité ?</h4>
  <p>Une formule comportant {{ n }} variables atomiques nécessite une table de vérité de {{ 2^n }} lignes. En pratique industrielle (vérification de microprocesseurs, solveurs de contraintes industriels), les formules manipulent des milliers de variables. Pour {{ n = 30 }}, {{ 2^{30} \approx 10^9 }} lignes ! Aucun ordinateur ne peut énumérer une telle table.</p>
  <p>Le cours de Logique de Sorbonne Université introduit donc <strong>l'approche algébrique et déductive</strong> : manipuler symboliquement la valeur de vérité {{ [F]^I }} par le calcul booléen équationnel pour établir des propriétés universelles valables pour <em>toutes</em> les interprétations d'un seul coup.</p>
</div>

<h2 id="sec2">2. L'Algèbre de Boole minimale {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }}</h2>

<div class="box def">
  <h4>Structure de l'algèbre de Boole de la Sorbonne (Cours 2, Slide 4)</h4>
  <p>L'algèbre minimale est le quadruplet {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }} où {{ \mathbb{B} = \{0, 1\} }} avec deux éléments distincts ({{ 0 \neq 1 }}). Les opérations vérifient les axiomes et propriétés fondamentales pour tous {{ a, b, c \in \mathbb{B} }} :</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>Propriété</th>
        <th>Opération Conjonctive ({{ \cdot }})</th>
        <th>Opération Disjonctive ({{ + }})</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Commutativité</strong></td>
        <td>{{ a \cdot b = b \cdot a }}</td>
        <td>{{ a + b = b + a }}</td>
      </tr>
      <tr>
        <td><strong>Associativité</strong></td>
        <td>{{ a \cdot (b \cdot c) = (a \cdot b) \cdot c }}</td>
        <td>{{ a + (b + c) = (a + b) + c }}</td>
      </tr>
      <tr>
        <td><strong>Distributivité croisée</strong></td>
        <td>{{ a \cdot (b + c) = (a \cdot b) + (a \cdot c) }}</td>
        <td>{{ a + (b \cdot c) = (a + b) \cdot (a + c) }} <em>(Piège !)</em></td>
      </tr>
      <tr>
        <td><strong>Élément neutre</strong></td>
        <td>{{ a \cdot 1 = a }}</td>
        <td>{{ a + 0 = a }}</td>
      </tr>
      <tr>
        <td><strong>Élément absorbant</strong></td>
        <td>{{ a \cdot 0 = 0 }}</td>
        <td>{{ a + 1 = 1 }}</td>
      </tr>
      <tr>
        <td><strong>Idempotence</strong></td>
        <td>{{ a \cdot a = a }}</td>
        <td>{{ a + a = a }}</td>
      </tr>
      <tr>
        <td><strong>Complémentarité</strong></td>
        <td>{{ a \cdot \overline{a} = 0 }}</td>
        <td>{{ a + \overline{a} = 1 }}</td>
      </tr>
      <tr>
        <td><strong>Involution</strong></td>
        <td colspan="2" style="text-align:center;">{{ \overline{\overline{a}} = a }}</td>
      </tr>
      <tr>
        <td><strong>Lois de De Morgan</strong></td>
        <td>{{ \overline{a \cdot b} = \overline{a} + \overline{b} }}</td>
        <td>{{ \overline{a + b} = \overline{a} \cdot \overline{b} }}</td>
      </tr>
      <tr>
        <td><strong>Absorption</strong></td>
        <td>{{ a \cdot (a + b) = a }}</td>
        <td>{{ a + (a \cdot b) = a }}</td>
      </tr>
      <tr>
        <td><strong>Règle de simplification</strong></td>
        <td>{{ a \cdot (\overline{a} + b) = a \cdot b }}</td>
        <td>{{ a + \overline{a} \cdot b = a + b }}</td>
      </tr>
    </tbody>
  </table>
  <p><strong>ATTENTION PIÈGE D'EXAMEN :</strong> En algèbre classique sur les réels, l'addition n'est jamais distributive sur la multiplication. En algèbre de Boole, <em>l'addition booléenne est distributive sur la multiplication</em> : {{ a + (b \cdot c) = (a + b) \cdot (a + c) }} !</p>
</div>

<h2 id="sec3">3. Traduction inductive et raisonnement équationnel sur {{ [F]^I }}</h2>

<div class="box method">
  <h4>Traduction inductive d'une formule vers son expression booléenne</h4>
  <p>Soit {{ I }} une interprétation fixée. On traduit la formule {{ F }} de manière purement mécanique depuis sa syntaxe vers l'algèbre de Boole :</p>
  <ul>
    <li>{{ [\text{true}]^I = 1 }} \quad et \quad {{ [\text{false}]^I = 0 }}</li>
    <li>{{ [p]^I = I(p) }} pour toute variable atomique {{ p }}</li>
    <li>{{ [\neg F]^I = \overline{[F]^I} }}</li>
    <li>{{ [F_1 \land F_2]^I = [F_1]^I \cdot [F_2]^I }}</li>
    <li>{{ [F_1 \lor F_2]^I = [F_1]^I + [F_2]^I }}</li>
    <li>{{ [F_1 \Rightarrow F_2]^I = \overline{[F_1]^I} + [F_2]^I }}</li>
    <li>{{ [F_1 \Leftrightarrow F_2]^I = [F_1]^I \cdot [F_2]^I + \overline{[F_1]^I} \cdot \overline{[F_2]^I} }}</li>
  </ul>
</div>

<div class="box tip">
  <h4>Exemple de raisonnement équationnel du cours (Cours 2, Slide 12)</h4>
  <p>Soit la formule de Peirce : {{ F = (F_1 \Rightarrow F_2) \Rightarrow F_1 }}. Calculons son interprétation {{ [F]^I }} :</p>
  <div style="font-size:1.05em; line-height:2em;">
    {{ [F]^I = \overline{[F_1 \Rightarrow F_2]^I} + [F_1]^I }} \quad <em>(Définition de l'implication)</em><br/>
    {{ \equiv \overline{\overline{[F_1]^I} + [F_2]^I} + [F_1]^I }} \quad <em>(Définition de l'implication interne)</em><br/>
    {{ \equiv (\overline{\overline{[F_1]^I}} \cdot \overline{[F_2]^I}) + [F_1]^I }} \quad <em>(Loi de De Morgan)</em><br/>
    {{ \equiv ([F_1]^I \cdot \overline{[F_2]^I}) + [F_1]^I }} \quad <em>(Involution)</em><br/>
    {{ \equiv [F_1]^I }} \quad <em>(Loi d'absorption : {{ x + x \cdot y = x }})</em>
  </div>
  <p>On a ainsi prouvé en 4 lignes algébriques que pour toute interprétation {{ I }}, {{ [F]^I = [F_1]^I }}, ce qui aurait nécessité une table immense si {{ F_1 }} et {{ F_2 }} étaient composées de nombreuses variables !</p>
</div>

<h2 id="sec4">4. Validité, satisfiabilité et insatisfiabilité sans table de vérité</h2>

<div class="box def">
  <h4>Définitions mathématiques exactes et méthodes de preuve</h4>
  <ul>
    <li><strong>Formule satisfiable :</strong> {{ \exists I, [F]^I = 1 }}.
      <br/><em>Méthode sans table :</em> Il suffit d'<strong>exhiber explicitement une interprétation</strong> {{ I_0 }} et de calculer {{ [F]^{I_0} = 1 }}.
    </li>
    <li><strong>Formule valide (tautologie, {{ \models F }}) :</strong> {{ \forall I, [F]^I = 1 }}.
      <br/><em>Méthode sans table :</em> Soit par calcul équationnel direct en montrant que {{ [F]^I \equiv 1 }} quelle que soit l'interprétation {{ I }}, soit par l'absurde en supposant {{ [F]^I = 0 }} et en aboutissant à une contradiction.
    </li>
    <li><strong>Formule insatisfiable (antilogie) :</strong> {{ \forall I, [F]^I = 0 }}.
      <br/><em>Méthode sans table :</em> Montrer que {{ [F]^I \equiv 0 }} pour tout {{ I }}.
    </li>
    <li><strong>Formule non valide :</strong> Il suffit d'<strong>exhiber un contre-modèle</strong>, c'est-à-dire une interprétation {{ I_c }} telle que {{ [F]^{I_c} = 0 }}.
    </li>
  </ul>
</div>

<div class="w-eval" data-formula="(p => q) => (~q => ~p)"></div>

<h2 id="sec5">5. Conséquence sémantique formelle ({{ \mathcal{H} \models F }}) et contre-modèles</h2>

<div class="box def">
  <h4>Définition de la conséquence sémantique (Cours 2, Slide 18)</h4>
  <p>Soit {{ \mathcal{H} = \{H_1, H_2, \dots, H_k\} }} un ensemble fini d'hypothèses et {{ F }} une formule conclusion. On dit que {{ F }} est <strong>conséquence sémantique</strong> de {{ \mathcal{H} }}, noté {{ \mathcal{H} \models F }}, si et seulement si :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">
    Pour toute interprétation {{ I }}, si {{ [H_1 \land H_2 \land \dots \land H_k]^I = 1 }}, alors {{ [F]^I = 1 }}.
  </p>
  <p>Autrement dit : <em>Tout modèle de l'ensemble d'hypothèses {{ \mathcal{H} }} est obligatoirement un modèle de la conclusion {{ F }}.</em></p>
</div>

<div class="box method">
  <h4>Comment prouver ou réfuter {{ \mathcal{H} \models F }} sans table de vérité ?</h4>
  <ol>
    <li><strong>Pour prouver que {{ \mathcal{H} \models F }} est VRAIE :</strong>
      <br/>Soit {{ I }} une interprétation quelconque telle que {{ [H_1]^I = 1, \dots, [H_k]^I = 1 }}. Par déductions logiques nécessaires à partir de ces égalités, montrons que nécessairement {{ [F]^I = 1 }}.
    </li>
    <li><strong>Pour prouver que {{ \mathcal{H} \models F }} est FAUSSE (Réfutation) :</strong>
      <br/>Il suffit de <strong>construire un contre-modèle explicite</strong> {{ I_{cm} }} tel que :
      <div style="text-align:center; font-weight:bold; margin:6px 0;">
        {{ [H_1]^{I_{cm}} = 1, \quad \dots, \quad [H_k]^{I_{cm}} = 1 \quad \text{et} \quad [F]^{I_{cm}} = 0 }}
      </div>
      Ce contre-modèle suffit à anéantir l'implication universelle.
    </li>
  </ol>
</div>

<div class="w-entail" data-hyp="p; p => q" data-concl="q"></div>

<h2 id="sec6">6. Équivalence logique et théorème de déduction sémantique</h2>

<div class="box tip">
  <h4>Théorème de Déduction Sémantique</h4>
  <p>Pour tout ensemble de formules {{ \mathcal{H} }} et toutes formules {{ A }} et {{ B }} :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">
    {{ \mathcal{H} \cup \{A\} \models B \quad \iff \quad \mathcal{H} \models (A \Rightarrow B) }}
  </p>
  <p>En particulier, avec {{ \mathcal{H} = \emptyset }} :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">
    {{ A \models B \quad \iff \quad \models (A \Rightarrow B) }}
  </p>
  <p>Ce théorème magistral établit le pont fondamental entre la relation métamathématique de déduction ({{ \models }}) et le connecteur syntaxique d'implication ({{ \Rightarrow }}).</p>
</div>

<div class="box def">
  <h4>Équivalence logique {{ F_1 \equiv F_2 }} (notée {{ F_1 |\equiv| F_2 }} dans le cours)</h4>
  <p>Deux formules sont logiquement équivalentes ssi elles ont la même valeur sous toute interprétation :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;">
    {{ F_1 \equiv F_2 \quad \iff \quad \forall I, [F_1]^I = [F_2]^I \quad \iff \quad (F_1 \models F_2 \text{ et } F_2 \models F_1) }}
  </p>
</div>

<div class="w-equiv" data-fa="~(p & q)" data-fb="~p | ~q"></div>

<h2 id="sec7">7. Laboratoire de déduction et équivalence</h2>

<div class="box tip">
  <h4>Bac à sable de calcul sémantique</h4>
  <p>Vérifiez interactivement des conséquences sémantiques arbitraires, trouvez des contre-modèles et comparez deux formules pour tester leur équivalence sans table de vérité.</p>
</div>

<div class="w-lab" data-formula="(p & (p => q)) => q"></div>
"""

fa = """
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>فصل ۲: عبارات بولی و استلزام معنایی</h1>
  <p class="lead">محاسبات منطق گزاره‌ای بدون نیاز به جدول درستی: جبر بولی، استدلال معادلاتی صوری، صدق‌پذیری، اعتبار و استلزام معنایی {{ \mathcal{H} \models F }}.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب درس</h3>
  <ul>
    <li><a href="#sec1">۱. فراتر از جدول‌های درستی: مسئله انفجار ترکیبیاتی</a></li>
    <li><a href="#sec2">۲. جبر بولی کمینه {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }}</a></li>
    <li><a href="#sec3">۳. ترجمه استقرایی و استدلال معادلاتی روی {{ [F]^I }}</a></li>
    <li><a href="#sec4">۴. اعتبار، صدق‌پذیری و ناسازگاری بدون جدول درستی</a></li>
    <li><a href="#sec5">۵. استلزام معنایی صوری ({{ \mathcal{H} \models F }}) و پادمدل‌ها</a></li>
    <li><a href="#sec6">۶. هم‌ارزی منطقی و قضیه استنتاج معنایی</a></li>
    <li><a href="#sec7">۷. آزمایشگاه تعاملی استنتاج و هم‌ارزی</a></li>
  </ul>
</div>

<h2 id="sec1">1. Au-delà des tables de vérité : l'explosion combinatoire</h2>

<div class="box info">
  <h4>چرا باید جدول‌های درستی را کنار بگذاریم؟</h4>
  <p>یک فرمول با {{ n }} متغیر مستقل به جدول درستی با {{ 2^n }} سطر نیاز دارد. در مسائل صنعتی واقعی (تأیید درستی پردازنده‌ها، حل‌کننده‌های صنعتی قیود)، فرمول‌ها با هزاران متغیر سر و کار دارند. حتی برای ۳۰ متغیر ({{ n = 30 }})، جدول بیش از یک میلیارد سطر ({{ 2^{30} \approx 10^9 }}) خواهد داشت! هیچ کامپیوتر مدرنی قادر به پیمایش چنین جدولی نیست.</p>
  <p>به همین دلیل، درس منطق دانشگاه سوربن <strong>روش جبری و استنتاجی</strong> را آموزش می‌دهد: دستکاری نمادین ارزش حقیقت {{ [F]^I }} با قوانین جبر بولی، تا خواص کلی برای <em>تمامی</em> تعبیرها به طور هم‌زمان و یک‌جا اثبات گردند.</p>
</div>

<h2 id="sec2">2. L'Algèbre de Boole minimale {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }}</h2>

<div class="box def">
  <h4>ساختار جبر بولی دانشگاه سوربن (اسلاید ۴ درس ۲)</h4>
  <p>جبر بولی کمینه به صورت چهارگانه {{ (\mathbb{B}, \cdot, +, \overline{\phantom{x}}) }} تعریف می‌شود که در آن {{ \mathbb{B} = \{0, 1\} }} مجموعه‌ای دارای دو عنصر متمایز است ({{ 0 \neq 1 }}). برای تمام مقادیر {{ a, b, c \in \mathbb{B} }} خواص بنیادی زیر برقرار است:</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>خاصیت جبری</th>
        <th>عملگر عطفی ضرب ({{ \cdot }})</th>
        <th>عملگر فصلی جمع ({{ + }})</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>جابجایی</strong></td>
        <td>{{ a \cdot b = b \cdot a }}</td>
        <td>{{ a + b = b + a }}</td>
      </tr>
      <tr>
        <td><strong>شرکت‌پذیری</strong></td>
        <td>{{ a \cdot (b \cdot c) = (a \cdot b) \cdot c }}</td>
        <td>{{ a + (b + c) = (a + b) + c }}</td>
      </tr>
      <tr>
        <td><strong>توزیع‌پذیری متقابل</strong></td>
        <td>{{ a \cdot (b + c) = (a \cdot b) + (a \cdot c) }}</td>
        <td>{{ a + (b \cdot c) = (a + b) \cdot (a + c) }} <em>(تله مهم!)</em></td>
      </tr>
      <tr>
        <td><strong>عنصر همانی (خنثی)</strong></td>
        <td>{{ a \cdot 1 = a }}</td>
        <td>{{ a + 0 = a }}</td>
      </tr>
      <tr>
        <td><strong>عنصر جاذب (پوچ‌ساز)</strong></td>
        <td>{{ a \cdot 0 = 0 }}</td>
        <td>{{ a + 1 = 1 }}</td>
      </tr>
      <tr>
        <td><strong>بت‌خواری (خاصیت ایندمپوتنت)</strong></td>
        <td>{{ a \cdot a = a }}</td>
        <td>{{ a + a = a }}</td>
      </tr>
      <tr>
        <td><strong>متمم‌داری</strong></td>
        <td>{{ a \cdot \overline{a} = 0 }}</td>
        <td>{{ a + \overline{a} = 1 }}</td>
      </tr>
      <tr>
        <td><strong>نفی مضاعف</strong></td>
        <td colspan="2" style="text-align:center;" dir="ltr">{{ \overline{\overline{a}} = a }}</td>
      </tr>
      <tr>
        <td><strong>قوانین دمرگان</strong></td>
        <td>{{ \overline{a \cdot b} = \overline{a} + \overline{b} }}</td>
        <td>{{ \overline{a + b} = \overline{a} \cdot \overline{b} }}</td>
      </tr>
      <tr>
        <td><strong>جذب</strong></td>
        <td>{{ a \cdot (a + b) = a }}</td>
        <td>{{ a + (a \cdot b) = a }}</td>
      </tr>
      <tr>
        <td><strong>قاعده ساده‌سازی</strong></td>
        <td>{{ a \cdot (\overline{a} + b) = a \cdot b }}</td>
        <td>{{ a + \overline{a} \cdot b = a + b }}</td>
      </tr>
    </tbody>
  </table>
  <p><strong>تله امتحانی بسیار حساس:</strong> در حساب معمولی اعداد حقیقی، جمع هرگز بر روی ضرب توزیع نمی‌شود. اما در جبر بولی، <em>جمع بولی بر روی ضرب توزیع‌پذیر است</em>: {{ a + (b \cdot c) = (a + b) \cdot (a + c) }} !</p>
</div>

<h2 id="sec3">3. Traduction inductive et raisonnement équationnel sur {{ [F]^I }}</h2>

<div class="box method">
  <h4>ترجمه استقرایی فرمول منطقی به عبارت جبر بولی</h4>
  <p>فرض کنید تعبیر {{ I }} داده شده باشد. تبدیل فرمول {{ F }} به عبارت بولی به صورت کاملاً مکانیکی انجام می‌شود:</p>
  <ul>
    <li>{{ [\text{true}]^I = 1 }} \quad و \quad {{ [\text{false}]^I = 0 }}</li>
    <li>برای هر نماد اتمی {{ p }} داریم: {{ [p]^I = I(p) }}</li>
    <li>{{ [\neg F]^I = \overline{[F]^I} }}</li>
    <li>{{ [F_1 \land F_2]^I = [F_1]^I \cdot [F_2]^I }}</li>
    <li>{{ [F_1 \lor F_2]^I = [F_1]^I + [F_2]^I }}</li>
    <li>{{ [F_1 \Rightarrow F_2]^I = \overline{[F_1]^I} + [F_2]^I }}</li>
    <li>{{ [F_1 \Leftrightarrow F_2]^I = [F_1]^I \cdot [F_2]^I + \overline{[F_1]^I} \cdot \overline{[F_2]^I} }}</li>
  </ul>
</div>

<div class="box tip">
  <h4>نمونه استدلال معادلاتی رسمی درس سوربن (اسلاید ۱۲)</h4>
  <p>فرمول مشهور پِیرس را در نظر بگیرید: {{ F = (F_1 \Rightarrow F_2) \Rightarrow F_1 }}. ارزش تعبیر {{ [F]^I }} را ساده می‌کنیم:</p>
  <div style="font-size:1.05em; line-height:2em;" dir="ltr">
    {{ [F]^I = \overline{[F_1 \Rightarrow F_2]^I} + [F_1]^I }} \quad <em>(تعریف شرطی بیرونی)</em><br/>
    {{ \equiv \overline{\overline{[F_1]^I} + [F_2]^I} + [F_1]^I }} \quad <em>(تعریف شرطی درونی)</em><br/>
    {{ \equiv (\overline{\overline{[F_1]^I}} \cdot \overline{[F_2]^I}) + [F_1]^I }} \quad <em>(قانون دمرگان)</em><br/>
    {{ \equiv ([F_1]^I \cdot \overline{[F_2]^I}) + [F_1]^I }} \quad <em>(نفی مضاعف)</em><br/>
    {{ \equiv [F_1]^I }} \quad <em>(قانون جذب : {{ x + x \cdot y = x }})</em>
  </div>
  <p>بدین ترتیب در ۴ خط استدلال جبری محض اثبات شد که تحت هر تعبیر ممکن {{ I }}، همواره {{ [F]^I = [F_1]^I }} است؛ اگر {{ F_1 }} و {{ F_2 }} دارای متغیرهای متعدد بودند، اثبات با جدول به هزاران سطر نیاز داشت!</p>
</div>

<h2 id="sec4">4. Validité, satisfiabilité et insatisfiabilité sans table de vérité</h2>

<div class="box def">
  <h4>تعاریف دقیق ریاضی و روش‌های اثبات برگه امتحانی</h4>
  <ul>
    <li><strong>فرمول صدق‌پذیر (Satisfiable):</strong> {{ \exists I, [F]^I = 1 }}.
      <br/><em>روش بدون جدول:</em> کافی است <strong>یک تعبیر مشخص</strong> {{ I_0 }} ارائه داده و نشان دهید {{ [F]^{I_0} = 1 }}.
    </li>
    <li><strong>فرمول معتبر (Tautology / Valid - نماد {{ \models F }}):</strong> {{ \forall I, [F]^I = 1 }}.
      <br/><em>روش بدون جدول:</em> با استدلال معادلاتی نشان دهید {{ [F]^I \equiv 1 }} تحت هر تعبیر دلخواه {{ I }}، یا با برهان خلف با فرض {{ [F]^I = 0 }} به تناقض برسید.
    </li>
    <li><strong>فرمول ناسازگار یا تناقض (Unsatisfiable):</strong> {{ \forall I, [F]^I = 0 }}.
      <br/><em>روش بدون جدول:</em> اثبات جبری این‌که {{ [F]^I \equiv 0 }} برای هر {{ I }}.
    </li>
    <li><strong>فرمول غیرمعتبر (رد اعتبار):</strong> کافی است <strong>یک پادمدل (Counter-model)</strong> ارائه دهید، یعنی تعبیری {{ I_c }} که در آن {{ [F]^{I_c} = 0 }} باشد.
    </li>
  </ul>
</div>

<div class="w-eval" data-formula="(p => q) => (~q => ~p)"></div>

<h2 id="sec5">5. Conséquence sémantique formelle ({{ \mathcal{H} \models F }}) et contre-modèles</h2>

<div class="box def">
  <h4>تعریف دقیق استلزام معنایی (اسلاید ۱۸ درس ۲)</h4>
  <p>فرض کنید {{ \mathcal{H} = \{H_1, H_2, \dots, H_k\} }} مجموعه‌ای متناهی از فرضیات و {{ F }} فرمول نتیجه باشد. می‌گوییم {{ F }} یک <strong>نتیجه معنایی</strong> از {{ \mathcal{H} }} است (با نماد {{ \mathcal{H} \models F }}) اگر و فقط اگر:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">
    تحت هر تعبیر {{ I }}، اگر {{ [H_1 \land H_2 \land \dots \land H_k]^I = 1 }} باشد، آنگاه {{ [F]^I = 1 }} است.
  </p>
  <p>به بیان ساده‌تر: <em>هر مدلی که تمام فرضیات {{ \mathcal{H} }} را برآورده کند، الزاماً مدلی برای نتیجه {{ F }} نیز هست.</em></p>
</div>

<div class="box method">
  <h4>چگونه {{ \mathcal{H} \models F }} را بدون جدول درستی اثبات یا رد کنیم؟</h4>
  <ol>
    <li><strong>برای اثبات درستی استلزام {{ \mathcal{H} \models F }} :</strong>
      <br/>یک تعبیر دلخواه {{ I }} در نظر می‌گیریم که در آن {{ [H_1]^I = 1, \dots, [H_k]^I = 1 }} باشد. با زنجیره‌ای از استنتاج‌های صوری اجتناب‌ناپذیر نشان می‌دهیم که اجباراً {{ [F]^I = 1 }} خواهد بود.
    </li>
    <li><strong>برای رد استلزام (اثبات نادرستی {{ \mathcal{H} \models F }}) :</strong>
      <br/>کافی است <strong>یک پادمدل صریح</strong> {{ I_{cm} }} معرفی کنیم به طوری که:
      <div style="text-align:center; font-weight:bold; margin:6px 0;" dir="ltr">
        {{ [H_1]^{I_{cm}} = 1, \quad \dots, \quad [H_k]^{I_{cm}} = 1 \quad \text{et} \quad [F]^{I_{cm}} = 0 }}
      </div>
      وجود تنها یک پادمدل، ادعای استلزام کلی را باطل می‌کند.
    </li>
  </ol>
</div>

<div class="w-entail" data-hyp="p; p => q" data-concl="q"></div>

<h2 id="sec6">6. Équivalence logique et théorème de déduction sémantique</h2>

<div class="box tip">
  <h4>قضیه بنیادین استنتاج معنایی (Deduction Theorem)</h4>
  <p>برای هر مجموعه فرضیات {{ \mathcal{H} }} و هر دو فرمول دلخواه {{ A }} و {{ B }} داریم:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">
    {{ \mathcal{H} \cup \{A\} \models B \quad \iff \quad \mathcal{H} \models (A \Rightarrow B) }}
  </p>
  <p>به ویژه هنگامی که مجموعه فرضیات تهی باشد ({{ \mathcal{H} = \emptyset }}):</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">
    {{ A \models B \quad \iff \quad \models (A \Rightarrow B) }}
  </p>
  <p>این قضیه شکوهمند پیوند ناگسستنی میان استنتاج فرامنطقی ({{ \models }}) و عملگر شرطی درون‌منطقی ({{ \Rightarrow }}) را برقرار می‌سازد.</p>
</div>

<div class="box def">
  <h4>هم‌ارزی منطقی {{ F_1 \equiv F_2 }} (با نماد {{ F_1 |\equiv| F_2 }} در جزوه سوربن)</h4>
  <p>دو فرمول را هم‌ارز منطقی می‌نامند اگر و تنها اگر تحت تمامی تعبیرها ارزش یکسانی تولید کنند:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">
    {{ F_1 \equiv F_2 \quad \iff \quad \forall I, [F_1]^I = [F_2]^I \quad \iff \quad (F_1 \models F_2 \text{ et } F_2 \models F_1) }}
  </p>
</div>

<div class="w-equiv" data-fa="~(p & q)" data-fb="~p | ~q"></div>

<h2 id="sec7">7. Laboratoire de déduction et équivalence</h2>

<div class="box tip">
  <h4>میزکار تعاملی تحلیل‌های معنایی</h4>
  <p>استلزام‌های معنایی دلخواه را بیازمایید، پادمدل‌های نقض‌کننده را کشف کنید و هم‌ارزی دو فرمول را بدون نیاز به کشیدن جدول‌های طولانی بررسی نمایید.</p>
</div>

<div class="w-lab" data-formula="(p & (p => q)) => q"></div>
"""

open(os.path.join(W02, 'cours.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W02, 'cours.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("cours.fr.html and cours.fa.html written.")
