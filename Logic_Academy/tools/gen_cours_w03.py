#!/usr/bin/env python3
"""Authoring generator for Week 3 Cours (Thème 3).
Covers:
- Fonctions booléennes (2^{2^n}), décomposition de Shannon, bijection avec les classes d'équivalence
- Littéraux, clauses, termes, FNC (CNF) et FND (DNF)
- Passage de la table de vérité vers FND (mintermes) et FNC (maxtermes)
- Mise sous forme normale par calcul algébrique sans table de vérité
- Critères linéaires de validité d'une FNC et de satisfiabilité d'une FND
- Complétude fonctionnelle ({¬,∧}, {¬,∨}, {¬,⇒}, NAND |, NOR ↓, incomplétude de {∧,∨})
"""
import os

W03 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w03'
os.makedirs(W03, exist_ok=True)

fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>Thème 3 : Fonctions Booléennes, Formes Normales (FNC/FND) &amp; Complétude</h1>
  <p class="lead">Représentation fonctionnelle des formules propositionnelles, dénombrement {{ 2^{2^n} }}, formes normales conjonctive (FNC) et disjonctive (FND), algorithmes de normalisation et complétude fonctionnelle des connecteurs.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du cours</h3>
  <ul>
    <li><a href="#sec1">1. Fonctions booléennes, dénombrement {{ 2^{2^n} }} et théorème de représentation</a></li>
    <li><a href="#sec2">2. Littéraux, clauses, termes et formes normales (FNC et FND)</a></li>
    <li><a href="#sec3">3. Construction canonique de la FND et de la FNC par table de vérité</a></li>
    <li><a href="#sec4">4. Mise en forme normale par transformations algébriques sans table</a></li>
    <li><a href="#sec5">5. Critères linéaires de décision (validité FNC, satisfiabilité FND)</a></li>
    <li><a href="#sec6">6. Complétude fonctionnelle et connecteurs universels (NAND, NOR)</a></li>
  </ul>
</div>

<h2 id="sec1">1. Fonctions booléennes, dénombrement {{ 2^{2^n} }} et théorème de représentation</h2>

<div class="box def">
  <h4>Fonction booléenne d'arité {{ n }} associée à une formule (Cours 3, Slides 3–6)</h4>
  <p>Soit {{ F \in \mathcal{F}_p(\mathcal{P}_0) }} une formule propositionnelle dont les variables atomiques sont {{ p_1, \dots, p_n }}. Une <strong>fonction booléenne d'arité {{ n }}</strong> est une application :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">
    {{ f_F : \mathbb{B}^n \longrightarrow \mathbb{B} \quad \text{où} \quad \mathbb{B} = \{0, 1\} }}
  </p>
  <p>Elle représente la formule {{ F }} si et seulement si, pour toute interprétation {{ I }}, on a :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;">
    {{ f_F(I(p_1), \dots, I(p_n)) = [F]^I }}
  </p>
  <p><strong>Théorème de dénombrement :</strong> Le domaine de départ {{ \mathbb{B}^n }} comporte exactement {{ 2^n }} {{ n }}-uplets distincts (qui correspondent aux {{ 2^n }} lignes d'une table de vérité). Pour chacune de ces {{ 2^n }} lignes, l'image par {{ f }} peut prendre {{ 2 }} valeurs ({{ 0 }} ou {{ 1 }}). Il existe donc exactement :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.2em;">
    {{ 2^{2^n} \quad \text{fonctions booléennes distinctes d'arité } n }}
  </p>
</div>

<div class="box info">
  <h4>Les {{ 2^{2^1} = 4 }} fonctions d'arité {{ n = 1 }} et le Lemme de Shannon (Cours 3, Slides 6–9)</h4>
  <p>Pour {{ n = 1 }}, il existe exactement {{ 4 }} fonctions booléennes {{ f_1, f_2, f_3, f_4 : \mathbb{B} \to \mathbb{B} }} :</p>
  <table class="logic-table" style="width:100%; margin:10px 0; text-align:center;">
    <thead>
      <tr>
        <th>{{ x }}</th>
        <th>{{ f_1(x) = 0 }}</th>
        <th>{{ f_2(x) = 1 }}</th>
        <th>{{ f_3(x) = x }}</th>
        <th>{{ f_4(x) = \overline{x} }}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{ 0 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
      </tr>
      <tr>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
      </tr>
    </tbody>
  </table>
  <p><strong>Lemme de décomposition de Shannon (Slide 7) :</strong> Toute fonction booléenne {{ f : \mathbb{B}^n \to \mathbb{B} }} d'arité {{ n \geq 1 }} se décompose suivant sa première variable {{ x_1 }} sous la forme :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;">
    {{ f(x_1, x_2, \dots, x_n) = x_1 \cdot f(1, x_2, \dots, x_n) + \overline{x_1} \cdot f(0, x_2, \dots, x_n) }}
  </p>
  <p>Par récurrence sur l'arité {{ n }}, cela démontre que <strong>toute fonction booléenne peut être définie par une expression booléenne</strong>, et réciproquement toute expression booléenne représente une formule logique. L'ensemble des fonctions booléennes est en bijection avec l'ensemble quotient {{ \mathcal{F}_p(\mathcal{P}_0) / |\equiv| }} des classes d'équivalence de formules (Slide 22).</p>
</div>

<h2 id="sec2">2. Littéraux, clauses, termes et formes normales (FNC et FND)</h2>

<div class="box def">
  <h4>Définitions syntaxiques des formes normales (Cours 3, Slides 12 &amp; 19)</h4>
  <p>On distingue rigoureusement le vocabulaire des <em>expressions booléennes</em> (dans {{ \mathbb{B} }}, avec {{ \cdot, +, \overline{\phantom{x}} }}) et celui des <em>formules logiques</em> (dans {{ \mathcal{F}_p }}, avec {{ \land, \lor, \neg }}) :</p>
  <ul>
    <li><strong>Littéral :</strong>
      <ul>
        <li>En expression booléenne : une variable booléenne {{ x }} (littéral positif) ou son complémentaire {{ \overline{x} }} (littéral négatif).</li>
        <li>En formule logique : un symbole propositionnel {{ p }} ou sa négation {{ \neg p }}.</li>
      </ul>
    </li>
    <li><strong>Forme Normale Conjonctive (FNC / CNF) :</strong>
      <ul>
        <li>En expression booléenne : un <strong>produit de sommes de littéraux</strong>, par exemple {{ (x_1 + \overline{x_2}) \cdot (x_1 + x_3 + \overline{x_4}) \cdot \overline{x_1} }}.</li>
        <li>En formule logique : une <strong>conjonction de disjonctions de littéraux</strong> (appelées <em>clauses</em>), soit {{ \bigwedge_i \left(\bigvee_j l_{i,j}\right) }}, par exemple {{ (p \lor \neg q) \land (p \lor r \lor \neg z) \land \neg p }}.</li>
      </ul>
    </li>
    <li><strong>Forme Normale Disjonctive (FND / DNF) :</strong>
      <ul>
        <li>En expression booléenne : une <strong>somme de produits de littéraux</strong>, par exemple {{ (x_1 \cdot \overline{x_2}) + (x_1 \cdot x_3 \cdot \overline{x_4}) + \overline{x_1} }}.</li>
        <li>En formule logique : une <strong>disjonction de conjonctions de littéraux</strong> (appelées <em>termes</em> ou monômes), soit {{ \bigvee_i \left(\bigwedge_j l_{i,j}\right) }}, par exemple {{ (p \land \neg q) \lor (p \land r \land \neg z) \lor \neg p }}.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="box warn">
  <h4>Cas particuliers dégénérés : simultanément en FNC et en FND ! (Cours 3, Slides 12 &amp; 19)</h4>
  <p>C'est la question piège classique du TD (Exercice 9) et des partiels de la Sorbonne :</p>
  <ul>
    <li><strong>Un littéral isolé</strong> (comme {{ x }} ou {{ \overline{x} }}) est <strong>à la fois en FNC et en FND</strong> (produit d'une seule somme réduite à 1 littéral, et somme d'un seul produit réduit à 1 littéral).</li>
    <li><strong>Une somme élémentaire de littéraux</strong> (comme {{ x + y + \overline{z} }} ou {{ p \lor q \lor r }}) est <strong>à la fois en FNC et en FND</strong> :
      <ul>
        <li>C'est une <strong>FNC</strong> composée d'un produit portant sur un unique facteur {{ (x + y + \overline{z}) }}.</li>
        <li>C'est une <strong>FND</strong> composée de la somme de 3 produits élémentaires {{ x }}, {{ y }} et {{ \overline{z} }} (chacun de taille 1).</li>
      </ul>
    </li>
    <li><strong>Un produit élémentaire de littéraux</strong> (comme {{ x \cdot \overline{y} \cdot z }} ou {{ p \land \neg q \land r }}) est également <strong>à la fois en FNC et en FND</strong> :
      <ul>
        <li>C'est une <strong>FND</strong> composée d'une somme portant sur un unique produit {{ (x \cdot \overline{y} \cdot z) }}.</li>
        <li>C'est une <strong>FNC</strong> composée du produit de 3 sommes élémentaires {{ (x) \cdot (\overline{y}) \cdot (z) }} (chacune réduite à 1 littéral).</li>
      </ul>
    </li>
  </ul>
</div>

<h2 id="sec3">3. Construction canonique de la FND et de la FNC par table de vérité</h2>

<div class="box method">
  <h4>Algorithme canonique des mintermes (FND) et des maxtermes (FNC) (Cours 3, Slides 15–18)</h4>
  <p>Soit {{ f(x_1, \dots, x_n) }} une fonction booléenne et {{ \mathcal{D}_f = \{(b_1, \dots, b_n) \in \mathbb{B}^n \mid f(b_1, \dots, b_n) = 1\} }} l'ensemble des lignes où la table de vérité vaut {{ 1 }} :</p>
  <ol>
    <li><strong>Construction de la FND canonique (sur les lignes où {{ f = 1 }}) :</strong>
      <p>Pour chaque {{ n }}-uplet {{ (b_1, \dots, b_n) \in \mathcal{D}_f }}, on forme le produit (<em>minterme</em>) {{ x'_1 \cdot x'_2 \cdots x'_n }} avec :</p>
      <p style="text-align:center; font-weight:bold;">
        {{ x'_i = x_i \text{ si } b_i = 1, \quad \text{et} \quad x'_i = \overline{x_i} \text{ si } b_i = 0 }}
      </p>
      <p>La FND est la somme de tous ces mintermes : {{ f(x_1, \dots, x_n) = \sum_{(b_1, \dots, b_n) \in \mathcal{D}_f} x'_1 \cdots x'_n }}.</p>
    </li>
    <li><strong>Construction de la FNC canonique (sur les lignes où {{ f = 0 }}) :</strong>
      <p>Pour chaque {{ n }}-uplet {{ (b_1, \dots, b_n) \notin \mathcal{D}_f }} (c'est-à-dire où {{ f(b_1, \dots, b_n) = 0 }}), on forme la somme (<em>maxterme</em>) {{ x''_1 + x''_2 + \dots + x''_n }} en inversant la polarité :</p>
      <p style="text-align:center; font-weight:bold;">
        {{ x''_i = x_i \text{ si } b_i = 0, \quad \text{et} \quad x''_i = \overline{x_i} \text{ si } b_i = 1 }}
      </p>
      <p>La FNC est le produit de tous ces maxtermes : {{ f(x_1, \dots, x_n) = \prod_{(b_1, \dots, b_n) \notin \mathcal{D}_f} (x''_1 + \dots + x''_n) }}.</p>
      <p><em>Justification :</em> {{ f }} est la négation de la FND de {{ \overline{f} }}. Par les lois de De Morgan, nier chaque minterme {{ x'_1 \cdots x'_n }} où {{ f = 0 }} produit exactement la clause {{ \overline{x'_1} + \dots + \overline{x'_n} }} !</p>
    </li>
  </ol>
</div>

<div class="box tip">
  <h4>Exemple complet du cours : {{ F = \neg(p \lor (\neg q \land r)) \lor q }} (Slides 16–18 &amp; 21)</h4>
  <p>En posant {{ f(x, y, z) = \overline{x + \overline{y} \cdot z} + y }}, la table de vérité donne :</p>
  <ul>
    <li>{{ \mathcal{D}_f = \{(0,0,0), (0,1,0), (0,1,1), (1,1,0), (1,1,1)\} }} (5 lignes à {{ 1 }}) :
      <br/><strong>FND canonique :</strong> {{ \overline{x} \cdot \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot \overline{z} + \overline{x} \cdot y \cdot z + x \cdot y \cdot \overline{z} + x \cdot y \cdot z }}.
    </li>
    <li>{{ \overline{\mathcal{D}_f} = \{(0,0,1), (1,0,0), (1,0,1)\} }} (3 lignes à {{ 0 }}) :
      <br/><strong>FNC canonique :</strong> {{ (x + y + \overline{z}) \cdot (\overline{x} + y + z) \cdot (\overline{x} + y + \overline{z}) }}.
    </li>
  </ul>
</div>

<div class="w-tt" data-formula="~(p | (~q & r)) | q"></div>

<h2 id="sec4">4. Mise en forme normale par transformations algébriques sans table</h2>

<div class="box method">
  <h4>Procédure mécanique en 3 étapes (Cours 3, Slide 14)</h4>
  <p>Une même formule admet plusieurs FNC et FND équivalentes (les formes canoniques issues de la table sont souvent très longues). Pour obtenir une FNC ou une FND compacte <strong>sans table de vérité</strong> :</p>
  <ol>
    <li><strong>Traduction / Élimination de {{ \Rightarrow }} et {{ \Leftrightarrow }} :</strong> remplacer {{ A \Rightarrow B }} par {{ \overline{a} + b }} (ou {{ \neg A \lor B }}) et {{ A \Leftrightarrow B }} par {{ a \cdot b + \overline{a} \cdot \overline{b} }}.</li>
    <li><strong>Descente des négations aux feuilles (Forme Normale Négative) :</strong> appliquer les lois de De Morgan ({{ \overline{x + y} = \overline{x} \cdot \overline{y} }} et {{ \overline{x \cdot y} = \overline{x} + \overline{y} }}) et l'involution ({{ \overline{\overline{x}} = x }}) jusqu'à ce que la barre de complémentation ne porte plus que sur des variables atomiques.</li>
    <li><strong>Application de la distributivité et simplifications :</strong>
      <ul>
        <li>Pour obtenir une <strong>FND</strong> : distribuer le produit {{ \cdot }} sur la somme {{ + }} via {{ x \cdot (y + z) = x \cdot y + x \cdot z }}.</li>
        <li>Pour obtenir une <strong>FNC</strong> : distribuer la somme {{ + }} sur le produit {{ \cdot }} via {{ x + (y \cdot z) = (x + y) \cdot (x + z) }}.</li>
      </ul>
    </li>
  </ol>
  <p><strong>Exemple du cours (Slide 14) :</strong> Mettons {{ e = \overline{x + \overline{y} \cdot z} + y }} en FND puis en FNC :</p>
  <div style="line-height:2em;">
    {{ e = (\overline{x} \cdot \overline{\overline{y} \cdot z}) + y = \overline{x} \cdot (\overline{\overline{y}} + \overline{z}) + y = \overline{x} \cdot (y + \overline{z}) + y }}<br/>
    {{ \equiv \overline{x} \cdot y + \overline{x} \cdot \overline{z} + y }} \quad <strong>(FND obtenue par distributivité de {{ \cdot }} sur {{ + }})</strong><br/>
    {{ \equiv (y + \overline{x}) \cdot (y + \overline{z}) }} \quad <strong>(FNC obtenue en distribuant {{ + y }} sur {{ \overline{x} \cdot (y + \overline{z}) }} puis {{ y + y = y }})</strong>
  </div>
</div>

<div class="w-equiv" data-a="(A & B) | (B => (B & A))" data-b="A | ~B"></div>

<h2 id="sec5">5. Critères linéaires de décision (validité FNC, satisfiabilité FND)</h2>

<div class="box tip">
  <h4>Pourquoi normaliser ? Décision immédiate de la validité et de la satisfiabilité</h4>
  <p>Une fois une expression mise sous forme normale, certaines propriétés sémantiques deviennent lisibles instantanément (en temps linéaire) :</p>
  <ul>
    <li><strong>Critère de validité d'une FNC ({{ f \equiv 1 }}) :</strong>
      <br/>Un produit de sommes {{ C_1 \cdot C_2 \cdots C_m }} vaut {{ 1 }} pour toute interprétation si et seulement si <strong>chaque somme (clause) {{ C_i }} vaut identiquement {{ 1 }}</strong>.
      <br/>Or une clause disjonctive est valide si et seulement si elle contient au moins une variable et son complémentaire ({{ x + \overline{x} = 1 }}).
      <br/><em>Théorème :</em> <strong>Une FNC est valide ssi chacune de ses clauses contient au moins un couple de littéraux complémentaires ({{ p \lor \neg p }}).</strong>
    </li>
    <li><strong>Critère de satisfiabilité d'une FND ({{ f \not\equiv 0 }}) :</strong>
      <br/>Une somme de produits {{ P_1 + P_2 + \dots + P_m }} est satisfiable si et seulement si <strong>au moins un produit (terme) {{ P_i }} est satisfiable</strong> (et inversement, la FND est insatisfiable ssi <em>chaque</em> produit {{ P_i }} vaut {{ 0 }}).
      <br/>Or un produit de littéraux est insatisfiable ssi il contient une contradiction ({{ x \cdot \overline{x} = 0 }}).
      <br/><em>Théorème :</em> <strong>Une FND est satisfiable ssi au moins l'un de ses produits ne contient aucun couple de littéraux complémentaires ({{ p \land \neg p }}).</strong>
    </li>
  </ul>
</div>

<h2 id="sec6">6. Complétude fonctionnelle et connecteurs universels (NAND, NOR)</h2>

<div class="box def">
  <h4>Systèmes fonctionnellement complets de connecteurs</h4>
  <p>Un ensemble de connecteurs logiques {{ \mathcal{C} }} est dit <strong>fonctionnellement complet</strong> si toute fonction booléenne {{ f : \mathbb{B}^n \to \mathbb{B} }} peut être représentée par une formule construite uniquement avec les connecteurs de {{ \mathcal{C} }}.</p>
  <ul>
    <li><strong>{{ \{\neg, \land, \lor\} }} est complet :</strong> démontré par l'existence de la FND (et de la FNC) pour toute fonction booléenne.</li>
    <li><strong>{{ \{\neg, \land\} }} est complet :</strong> car {{ A \lor B \equiv \neg(\neg A \land \neg B) }} par la loi de De Morgan.</li>
    <li><strong>{{ \{\neg, \lor\} }} est complet :</strong> car {{ A \land B \equiv \neg(\neg A \lor \neg B) }} par la loi de De Morgan.</li>
    <li><strong>{{ \{\neg, \Rightarrow\} }} est complet :</strong> car {{ A \lor B \equiv (\neg A) \Rightarrow B }}, ce qui ramène au système complet {{ \{\neg, \lor\} }}.</li>
    <li><strong>{{ \{\land, \lor\} }} est INCOMPLET :</strong> toute formule construite uniquement avec {{ \land }} et {{ \lor }} sans négation prend la valeur {{ 1 }} lorsque toutes ses variables valent {{ 1 }} (et {{ 0 }} lorsqu'elles valent {{ 0 }}). Il est donc mathématiquement impossible d'exprimer le complémentaire {{ \neg p }} !</li>
  </ul>
</div>

<div class="box info">
  <h4>Les deux connecteurs universels : NAND ({{ \mid }}) et NOR ({{ \downarrow }})</h4>
  <p>En électronique numérique, il est fondamental de fabriquer des circuits avec un seul type de porte logique :</p>
  <ol>
    <li><strong>L'opérateur NAND (barre de Sheffer {{ p \mid q \equiv \neg(p \land q) }}) :</strong>
      <br/>Le singleton {{ \{\mid\} }} est fonctionnellement complet à lui seul :
      <ul>
        <li>Négation : {{ \neg p \equiv p \mid p }}</li>
        <li>Conjonction : {{ p \land q \equiv \neg(p \mid q) \equiv (p \mid q) \mid (p \mid q) }}</li>
        <li>Disjonction : {{ p \lor q \equiv \neg p \mid \neg q \equiv (p \mid p) \mid (q \mid q) }}</li>
      </ul>
    </li>
    <li><strong>L'opérateur NOR (flèche de Peirce {{ p \downarrow q \equiv \neg(p \lor q) }}) :</strong>
      <br/>Le singleton {{ \{\downarrow\} }} est également fonctionnellement complet à lui seul :
      <ul>
        <li>Négation : {{ \neg p \equiv p \downarrow p }}</li>
        <li>Disjonction : {{ p \lor q \equiv \neg(p \downarrow q) \equiv (p \downarrow q) \downarrow (p \downarrow q) }}</li>
        <li>Conjonction : {{ p \land q \equiv \neg p \downarrow \neg q \equiv (p \downarrow p) \downarrow (q \downarrow q) }}</li>
      </ul>
    </li>
  </ol>
</div>

<div class="w-lab" data-formula="(A & (B | C)) | (~A & ~B)"></div>
"""

fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>فصل ۳: توابع بولی، فرم‌های نرمال (FNC/FND) و تمامیت تابعی</h1>
  <p class="lead">نمایش تابعی فرمول‌های گزاره‌ای، شمارش {{ 2^{2^n} }} تابع متمایز، فرم‌های نرمال عطفی (FNC) و فصلی (FND)، الگوریتم‌های استانداردسازی و تمامیت مجموعه‌های رابط‌های منطقی.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب درس</h3>
  <ul>
    <li><a href="#sec1">۱. توابع بولی، شمارش {{ 2^{2^n} }} و قضیه نمایش</a></li>
    <li><a href="#sec2">۲. لیترال‌ها، بندها، ترم‌ها و فرم‌های نرمال (FNC و FND)</a></li>
    <li><a href="#sec3">۳. استخراج استاندارد FND و FNC از روی جدول درستی</a></li>
    <li><a href="#sec4">۴. تبدیل به فرم نرمال با محاسبات جبری بدون جدول درستی</a></li>
    <li><a href="#sec5">۵. معیارهای تصمیم‌گیری خطی (اعتبار FNC و صدق‌پذیری FND)</a></li>
    <li><a href="#sec6">۶. تمامیت تابعی و عملگرهای جهان‌شمول (NAND و NOR)</a></li>
  </ul>
</div>

<h2 id="sec1">1. Fonctions booléennes, dénombrement {{ 2^{2^n} }} et théorème de représentation</h2>

<div class="box def">
  <h4>تابع بولی از مرتبه (آریته) {{ n }} متناظر با یک فرمول (اسلایدهای ۳ تا ۶ درس ۳)</h4>
  <p>فرض کنید {{ F \in \mathcal{F}_p(\mathcal{P}_0) }} یک فرمول گزاره‌ای شامل متغیرهای اتمی {{ p_1, \dots, p_n }} باشد. یک <strong>تابع بولی از مرتبه {{ n }}</strong> نگاشتی است به صورت:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">
    {{ f_F : \mathbb{B}^n \longrightarrow \mathbb{B} \quad \text{où} \quad \mathbb{B} = \{0, 1\} }}
  </p>
  <p>این تابع نمایش‌دهنده فرمول {{ F }} است اگر و تنها اگر تحت هر تعبیر دلخواه {{ I }} داشته باشیم:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">
    {{ f_F(I(p_1), \dots, I(p_n)) = [F]^I }}
  </p>
  <p><strong>قضیه شمارش توابع بولی:</strong> دامنه ورودی {{ \mathbb{B}^n }} دقیقاً دارای {{ 2^n }} چندتایی متمایز است (که متناظر با {{ 2^n }} سطر جدول درستی هستند). برای هر یک از این {{ 2^n }} سطر، خروجی تابع {{ f }} می‌تواند یکی از {{ 2 }} مقدار ({{ 0 }} یا {{ 1 }}) را اختیار کند. بنابراین در مجموع دقیقاً:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.2em;" dir="ltr">
    {{ 2^{2^n} \quad \text{fonctions booléennes distinctes d'arité } n }}
  </p>
</div>

<div class="box info">
  <h4>{{ 2^{2^1} = 4 }} تابع بولی یک‌متغیره ({{ n = 1 }}) و لم تجزیه شانون (اسلایدهای ۶ تا ۹)</h4>
  <p>به ازای {{ n = 1 }}، دقیقاً {{ 4 }} تابع بولی متمایز {{ f_1, f_2, f_3, f_4 : \mathbb{B} \to \mathbb{B} }} وجود دارد:</p>
  <table class="logic-table" style="width:100%; margin:10px 0; text-align:center;" dir="ltr">
    <thead>
      <tr>
        <th>{{ x }}</th>
        <th>{{ f_1(x) = 0 }}</th>
        <th>{{ f_2(x) = 1 }}</th>
        <th>{{ f_3(x) = x }}</th>
        <th>{{ f_4(x) = \overline{x} }}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{ 0 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
      </tr>
      <tr>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 1 }}</td>
        <td>{{ 0 }}</td>
      </tr>
    </tbody>
  </table>
  <p><strong>لم تجزیه شانون (اسلاید ۷):</strong> هر تابع بولی {{ f : \mathbb{B}^n \to \mathbb{B} }} با مرتبه {{ n \geq 1 }} بر حسب متغیر نخست خود {{ x_1 }} به صورت زیر بسط داده می‌شود:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">
    {{ f(x_1, x_2, \dots, x_n) = x_1 \cdot f(1, x_2, \dots, x_n) + \overline{x_1} \cdot f(0, x_2, \dots, x_n) }}
  </p>
  <p>با استقرای ریاضی روی {{ n }} ثابت می‌شود که <strong>هر تابع بولی را می‌توان با یک عبارت بولی تعریف کرد</strong> و برعکس هر عبارت بولی نمایشگر یک فرمول منطقی است. مجموعه توابع بولی در تناظر یک‌به‌یک (Bijection) با مجموعه خارج‌قسمتی کلاس‌های هم‌ارزی فرمول‌ها {{ \mathcal{F}_p(\mathcal{P}_0) / |\equiv| }} قرار دارد (اسلاید ۲۲).</p>
</div>

<h2 id="sec2">2. Littéraux, clauses, termes et formes normales (FNC et FND)</h2>

<div class="box def">
  <h4>تعاریف نحوی فرم‌های نرمال (اسلایدهای ۱۲ و ۱۹ درس ۳)</h4>
  <p>در درس سوربن میان نمادگذاری <em>عبارات بولی</em> (در {{ \mathbb{B} }} با عملگرهای {{ \cdot, +, \overline{\phantom{x}} }}) و <em>فرمول‌های منطقی</em> (در {{ \mathcal{F}_p }} با عملگرهای {{ \land, \lor, \neg }}) تفکیک دقیقی قائل می‌شویم:</p>
  <ul>
    <li><strong>لیترال (Littéral):</strong>
      <ul>
        <li>در عبارت بولی: یک متغیر بولی {{ x }} (لیترال مثبت) یا متمم آن {{ \overline{x} }} (لیترال منفی).</li>
        <li>در فرمول منطقی: یک نماد گزاره‌ای {{ p }} یا نقیض آن {{ \neg p }}.</li>
      </ul>
    </li>
    <li><strong>فرم نرمال عطفی (FNC / CNF):</strong>
      <ul>
        <li>در عبارت بولی: <strong>ضربی از جمع‌های لیترال‌ها</strong>، مانند {{ (x_1 + \overline{x_2}) \cdot (x_1 + x_3 + \overline{x_4}) \cdot \overline{x_1} }}.</li>
        <li>در فرمول منطقی: <strong>عطفی از فصل‌های لیترال‌ها</strong> (که به هر فصل یک <em>بند / Clause</em> می‌گویند)، یعنی {{ \bigwedge_i \left(\bigvee_j l_{i,j}\right) }}، مانند {{ (p \lor \neg q) \land (p \lor r \lor \neg z) \land \neg p }}.</li>
      </ul>
    </li>
    <li><strong>فرم نرمال فصلی (FND / DNF):</strong>
      <ul>
        <li>در عبارت بولی: <strong>جمعی از ضرب‌های لیترال‌ها</strong>، مانند {{ (x_1 \cdot \overline{x_2}) + (x_1 \cdot x_3 \cdot \overline{x_4}) + \overline{x_1} }}.</li>
        <li>در فرمول منطقی: <strong>فصلی از عطف‌های لیترال‌ها</strong> (که به هر عطف یک <em>ترم / Terme</em> می‌گویند)، یعنی {{ \bigvee_i \left(\bigwedge_j l_{i,j}\right) }}، مانند {{ (p \land \neg q) \lor (p \land r \land \neg z) \lor \neg p }}.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="box warn">
  <h4>حالات خاص و مرزی: هم‌زمان در فرم FNC و FND! (اسلایدهای ۱۲ و ۱۹)</h4>
  <p>این نکته یکی از پرتکرارترین سوالات تله در تمرین ۹ جزوه TD و آزمون‌های میان‌ترم سوربن است:</p>
  <ul>
    <li><strong>یک لیترال منفرد</strong> (مانند {{ x }} یا {{ \overline{x} }}) <strong>هم‌زمان در فرم FNC و FND</strong> قرار دارد (ضربی از یک جمع تک‌لیترالی، و جمعی از یک ضرب تک‌لیترالی).</li>
    <li><strong>یک جمع ساده از لیترال‌ها</strong> (مانند {{ x + y + \overline{z} }} یا {{ p \lor q \lor r }}) <strong>هم‌زمان در فرم FNC و FND</strong> است:
      <ul>
        <li>یک <strong>FNC</strong> است زیرا ضربی شامل تنها یک عامل فصلی {{ (x + y + \overline{z}) }} می‌باشد.</li>
        <li>یک <strong>FND</strong> است زیرا جمعی از ۳ تک‌جمله‌ای {{ x }}، {{ y }} و {{ \overline{z} }} (هر کدام به طول ۱) محسوب می‌شود.</li>
      </ul>
    </li>
    <li><strong>یک ضرب ساده از لیترال‌ها</strong> (مانند {{ x \cdot \overline{y} \cdot z }} یا {{ p \land \neg q \land r }}) نیز <strong>هم‌زمان در فرم FNC و FND</strong> است:
      <ul>
        <li>یک <strong>FND</strong> است زیرا جمعی شامل تنها یک عبارت ضربی {{ (x \cdot \overline{y} \cdot z) }} است.</li>
        <li>یک <strong>FNC</strong> است زیرا ضربی از ۳ پرانتز جمع تک‌عضوی {{ (x) \cdot (\overline{y}) \cdot (z) }} می‌باشد.</li>
      </ul>
    </li>
  </ul>
</div>

<h2 id="sec3">3. Construction canonique de la FND et de la FNC par table de vérité</h2>

<div class="box method">
  <h4>الگوریتم استاندارد مین‌ترم‌ها (FND) و مکس‌ترم‌ها (FNC) از جدول درستی (اسلایدهای ۱۵ تا ۱۸)</h4>
  <p>فرض کنید {{ f(x_1, \dots, x_n) }} یک تابع بولی و {{ \mathcal{D}_f = \{(b_1, \dots, b_n) \in \mathbb{B}^n \mid f(b_1, \dots, b_n) = 1\} }} مجموعه سطرهایی باشد که در آن‌ها خروجی جدول درستی برابر {{ 1 }} است:</p>
  <ol>
    <li><strong>ساخت FND استاندارد (بر اساس سطرهای دارای خروجی {{ f = 1 }}) :</strong>
      <p>به ازای هر چندتایی {{ (b_1, \dots, b_n) \in \mathcal{D}_f }}، عبارت ضربی (<em>مین‌ترم</em>) {{ x'_1 \cdot x'_2 \cdots x'_n }} را تشکیل می‌دهیم به طوری که:</p>
      <p style="text-align:center; font-weight:bold;" dir="ltr">
        {{ x'_i = x_i \text{ si } b_i = 1, \quad \text{et} \quad x'_i = \overline{x_i} \text{ si } b_i = 0 }}
      </p>
      <p>فرم FND حاصل‌جمع تمام این مین‌ترم‌هاست: {{ f(x_1, \dots, x_n) = \sum_{(b_1, \dots, b_n) \in \mathcal{D}_f} x'_1 \cdots x'_n }}.</p>
    </li>
    <li><strong>ساخت FNC استاندارد (بر اساس سطرهای دارای خروجی {{ f = 0 }}) :</strong>
      <p>به ازای هر چندتایی {{ (b_1, \dots, b_n) \notin \mathcal{D}_f }} (یعنی سطرهایی که در آن‌ها {{ f(b_1, \dots, b_n) = 0 }} است)، عبارت جمعی (<em>مکس‌ترم</em>) {{ x''_1 + x''_2 + \dots + x''_n }} را با قطبیت معکوس می‌نویسیم:</p>
      <p style="text-align:center; font-weight:bold;" dir="ltr">
        {{ x''_i = x_i \text{ si } b_i = 0, \quad \text{et} \quad x''_i = \overline{x_i} \text{ si } b_i = 1 }}
      </p>
      <p>فرم FNC حاصل‌ضرب تمام این مکس‌ترم‌هاست: {{ f(x_1, \dots, x_n) = \prod_{(b_1, \dots, b_n) \notin \mathcal{D}_f} (x''_1 + \dots + x''_n) }}.</p>
      <p><em>توجیه ریاضی:</em> تابع {{ f }} متمم FND تابع {{ \overline{f} }} است. طبق قوانین دمرگان، متمم گرفتن از هر مین‌ترم {{ x'_1 \cdots x'_n }} متناظر با سطرهای صفر، دقیقاً بند فصلی {{ \overline{x'_1} + \dots + \overline{x'_n} }} را تولید می‌کند!</p>
    </li>
  </ol>
</div>

<div class="box tip">
  <h4>مثال کامل اسلایدهای درس: {{ F = \neg(p \lor (\neg q \land r)) \lor q }} (اسلایدهای ۱۶ تا ۱۸ و ۲۱)</h4>
  <p>با قرار دادن {{ f(x, y, z) = \overline{x + \overline{y} \cdot z} + y }}، جدول درستی به ما می‌دهد:</p>
  <ul>
    <li>{{ \mathcal{D}_f = \{(0,0,0), (0,1,0), (0,1,1), (1,1,0), (1,1,1)\} }} (۵ سطر با مقدار {{ 1 }}) :
      <br/><strong>فرم FND استاندارد:</strong> <span dir="ltr">{{ \overline{x} \cdot \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot \overline{z} + \overline{x} \cdot y \cdot z + x \cdot y \cdot \overline{z} + x \cdot y \cdot z }}</span>.
    </li>
    <li>{{ \overline{\mathcal{D}_f} = \{(0,0,1), (1,0,0), (1,0,1)\} }} (۳ سطر با مقدار {{ 0 }}) :
      <br/><strong>فرم FNC استاندارد:</strong> <span dir="ltr">{{ (x + y + \overline{z}) \cdot (\overline{x} + y + z) \cdot (\overline{x} + y + \overline{z}) }}</span>.
    </li>
  </ul>
</div>

<div class="w-tt" data-formula="~(p | (~q & r)) | q"></div>

<h2 id="sec4">4. Mise en forme normale par transformations algébriques sans table</h2>

<div class="box method">
  <h4>روش مکانیکی ۳ مرحله‌ای بدون جدول درستی (اسلاید ۱۴ درس ۳)</h4>
  <p>یک فرمول واحد می‌تواند چندین FNC و FND هم‌ارز داشته باشد (فرم‌های استاندارد جدول اغلب بسیار طولانی هستند). برای یافتن FNC یا FND فشرده <strong>بدون رسم جدول درستی</strong>:</p>
  <ol>
    <li><strong>حذف شرطی {{ \Rightarrow }} و دوگان {{ \Leftrightarrow }} :</strong> جایگزینی {{ A \Rightarrow B }} با {{ \overline{a} + b }} (یا {{ \neg A \lor B }}) و {{ A \Leftrightarrow B }} با {{ a \cdot b + \overline{a} \cdot \overline{b} }}.</li>
    <li><strong>انتقال نقیض‌ها به روی متغیرها (فرم نرمال منفی) :</strong> اعمال قوانین دمرگان ({{ \overline{x + y} = \overline{x} \cdot \overline{y} }} و {{ \overline{x \cdot y} = \overline{x} + \overline{y} }}) و نفی مضاعف ({{ \overline{\overline{x}} = x }}) تا جایی که علامت متمم تنها بر روی متغیرهای اتمی قرار گیرد.</li>
    <li><strong>اعمال قانون توزیع‌پذیری و ساده‌سازی :</strong>
      <ul>
        <li>برای رسیدن به <strong>FND</strong> : توزیع ضرب {{ \cdot }} بر روی جمع {{ + }} با قاعده {{ x \cdot (y + z) = x \cdot y + x \cdot z }}.</li>
        <li>برای رسیدن به <strong>FNC</strong> : توزیع جمع {{ + }} بر روی ضرب {{ \cdot }} با قاعده {{ x + (y \cdot z) = (x + y) \cdot (x + z) }}.</li>
      </ul>
    </li>
  </ol>
  <p><strong>مثال اسلاید ۱۴ درس :</strong> تبدیل عبارت {{ e = \overline{x + \overline{y} \cdot z} + y }} به FND و سپس FNC:</p>
  <div style="line-height:2em;" dir="ltr">
    {{ e = (\overline{x} \cdot \overline{\overline{y} \cdot z}) + y = \overline{x} \cdot (\overline{\overline{y}} + \overline{z}) + y = \overline{x} \cdot (y + \overline{z}) + y }}<br/>
    {{ \equiv \overline{x} \cdot y + \overline{x} \cdot \overline{z} + y }} \quad <strong>(FND حاصل از توزیع {{ \cdot }} روی {{ + }})</strong><br/>
    {{ \equiv (y + \overline{x}) \cdot (y + \overline{z}) }} \quad <strong>(FNC حاصل از توزیع {{ + y }} روی {{ \overline{x} \cdot (y + \overline{z}) }} و سپس {{ y + y = y }})</strong>
  </div>
</div>

<div class="w-equiv" data-a="(A & B) | (B => (B & A))" data-b="A | ~B"></div>

<h2 id="sec5">5. Critères linéaires de décision (validité FNC, satisfiabilité FND)</h2>

<div class="box tip">
  <h4>چرا فرم‌های نرمال مهم هستند؟ تشخیص فوری اعتبار و صدق‌پذیری</h4>
  <p>هنگامی که یک عبارت در فرم نرمال قرار می‌گیرد، بررسی خواص معنایی آن در زمان خطی و با یک نگاه انجام‌پذیر است:</p>
  <ul>
    <li><strong>معیار اعتبار فرم نرمال عطفی FNC ({{ f \equiv 1 }}) :</strong>
      <br/>حاصل‌ضرب چند پرانتز جمع {{ C_1 \cdot C_2 \cdots C_m }} تحت هر تعبیری برابر {{ 1 }} است اگر و تنها اگر <strong>تک‌تک بندهای فصلی {{ C_i }} همواره برابر {{ 1 }} باشند</strong>.
      <br/>از طرفی، یک جمع از لیترال‌ها زمانی همواره برابر ۱ است که حداقل شامل یک متغیر و متمم آن باشد ({{ x + \overline{x} = 1 }}).
      <br/><em>قضیه امتحانی:</em> <strong>یک FNC معتبر (توتولوژی) است اگر و تنها اگر در هر یک از بندهای آن حداقل یک جفت لیترال متمم ({{ p \lor \neg p }}) حضور داشته باشد.</strong>
    </li>
    <li><strong>معیار صدق‌پذیری فرم نرمال فصلی FND ({{ f \not\equiv 0 }}) :</strong>
      <br/>حاصل‌جمع چند عبارت ضربی {{ P_1 + P_2 + \dots + P_m }} صدق‌پذیر است اگر و تنها اگر <strong>حداقل یکی از ضرب‌ها (ترم‌ها) {{ P_i }} صدق‌پذیر باشد</strong> (و برعکس، یک FND ناسازگار است اگر و تنها اگر <em>تک‌تک</em> ضرب‌های {{ P_i }} برابر {{ 0 }} باشند).
      <br/>یک ضرب از لیترال‌ها زمانی ناسازگار (همواره صفر) است که شامل یک متغیر و متمم آن باشد ({{ x \cdot \overline{x} = 0 }}).
      <br/><em>قضیه امتحانی:</em> <strong>یک FND صدق‌پذیر است اگر و تنها اگر حداقل یکی از ترم‌های ضربی آن فاقد جفت لیترال متناقض ({{ p \land \neg p }}) باشد.</strong>
    </li>
  </ul>
</div>

<h2 id="sec6">6. Complétude fonctionnelle et connecteurs universels (NAND, NOR)</h2>

<div class="box def">
  <h4>مجموعه‌های کامل تابعی از رابط‌های منطقی</h4>
  <p>مجموعه‌ای از عملگرهای منطقی {{ \mathcal{C} }} را <strong>کامل تابعی (Fonctionnellement complet)</strong> می‌نامند هرگاه بتوان هر تابع بولی دلخواه {{ f : \mathbb{B}^n \to \mathbb{B} }} را تنها با استفاده از رابط‌های موجود در {{ \mathcal{C} }} فرمول‌بندی کرد.</p>
  <ul>
    <li><strong>{{ \{\neg, \land, \lor\} }} کامل است:</strong> به واسطه وجود FND (و FNC) برای هر تابع بولی دلخواه اثبات شد.</li>
    <li><strong>{{ \{\neg, \land\} }} کامل است:</strong> زیرا طبق قانون دمرگان داریم {{ A \lor B \equiv \neg(\neg A \land \neg B) }}.</li>
    <li><strong>{{ \{\neg, \lor\} }} کامل است:</strong> زیرا طبق قانون دمرگان داریم {{ A \land B \equiv \neg(\neg A \lor \neg B) }}.</li>
    <li><strong>{{ \{\neg, \Rightarrow\} }} کامل است:</strong> زیرا {{ A \lor B \equiv (\neg A) \Rightarrow B }} که مسئله را به مجموعه کامل {{ \{\neg, \lor\} }} تحویل می‌دهد.</li>
    <li><strong>{{ \{\land, \lor\} }} ناقص است:</strong> هر فرمولی که تنها با {{ \land }} و {{ \lor }} بدون نقیض ساخته شود، به ازای ورودی همه {{ 1 }} همواره خروجی {{ 1 }} می‌دهد (و به ازای همه {{ 0 }} خروجی {{ 0 }} می‌دهد). بنابراین هرگز نمی‌تواند عملگر نقیض {{ \neg p }} را شبیه‌سازی کند!</li>
  </ul>
</div>

<div class="box info">
  <h4>دو عملگر جهان‌شمول در مدارهای منطقی: NAND ({{ \mid }}) و NOR ({{ \downarrow }})</h4>
  <p>در مهندسی سخت‌افزار و طراحی تراشه‌ها، ساخت تمام مدارها با یک نوع گیت منطقی واحد اهمیت حیاتی دارد:</p>
  <ol>
    <li><strong>عملگر NAND (خط شفر {{ p \mid q \equiv \neg(p \land q) }}) :</strong>
      <br/>مجموعه تک‌عضوی {{ \{\mid\} }} به تنهایی کامل تابعی است:
      <ul>
        <li>نقیض: <span dir="ltr">{{ \neg p \equiv p \mid p }}</span></li>
        <li>عطف: <span dir="ltr">{{ p \land q \equiv \neg(p \mid q) \equiv (p \mid q) \mid (p \mid q) }}</span></li>
        <li>فصل: <span dir="ltr">{{ p \lor q \equiv \neg p \mid \neg q \equiv (p \mid p) \mid (q \mid q) }}</span></li>
      </ul>
    </li>
    <li><strong>عملگر NOR (پیکان پیرس {{ p \downarrow q \equiv \neg(p \lor q) }}) :</strong>
      <br/>مجموعه تک‌عضوی {{ \{\downarrow\} }} نیز به تنهایی کامل تابعی است:
      <ul>
        <li>نقیض: <span dir="ltr">{{ \neg p \equiv p \downarrow p }}</span></li>
        <li>فصل: <span dir="ltr">{{ p \lor q \equiv \neg(p \downarrow q) \equiv (p \downarrow q) \downarrow (p \downarrow q) }}</span></li>
        <li>عطف: <span dir="ltr">{{ p \land q \equiv \neg p \downarrow \neg q \equiv (p \downarrow p) \downarrow (q \downarrow q) }}</span></li>
      </ul>
    </li>
  </ol>
</div>

<div class="w-lab" data-formula="(A & (B | C)) | (~A & ~B)"></div>
"""

open(os.path.join(W03, 'cours.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W03, 'cours.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("w03 cours.fr.html and cours.fa.html written.")
