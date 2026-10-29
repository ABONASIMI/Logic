#!/usr/bin/env python3
"""Authoring generator for TD Week 3 (Thème 3 : Fonctions Booléennes et Formes Normales).
Exhaustive step-by-step solutions for:
- Exercice 9: Q1 (Identifier les FND et FNC parmi 7 expressions booléennes)
- Exercice 10: Q1 (Fonction valide : FNC et FND avec >= 3 clauses/termes et minimums), Q2 (Fonction insatisfiable : FNC et FND avec >= 3 clauses/termes et minimums)
- Exercice 11: Q1 (Table de vérité de XOR, en déduire FND et FNC), Q2 (f(x,y)=1 ssi x=0 et y=0 : FND et FNC), Q3 (Déduire l'équivalence F |=| G)
- Exercice 12: Q1 (Table de vérité déduite d'une FND sans calcul), Q2 (Table de vérité déduite d'une FNC sans calcul)
- Exercice 13: Formule F = (A & (B | C)) | (~A & ~B) sans table de vérité : Q1 (Fonction associée f_F), Q2 (Mise en FND algébrique), Q3 (Mise en FNC algébrique par distributivité)
"""
import os

W03 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w03'
os.makedirs(W03, exist_ok=True)

fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TD Thème 3 : Fonctions Booléennes et Formes Normales (FND / FNC)</h1>
  <p class="lead">Corrections intégrales et détaillées pas à pas des 5 exercices officiels du polycopié de TD (Exercices 9 à 13) : identification syntaxique des formes normales, critères algébriques de validité et d'insatisfiabilité, synthèse canonique par mintermes et maxtermes, lecture directe de tables de vérité et mise en FND/FNC par calcul équationnel.</p>
</div>

<div class="toc-box">
  <h3>Sommaire des exercices du TD</h3>
  <ul>
    <li><a href="#td3_ex9">Exercice 9 – Identification syntaxique des FND et FNC</a></li>
    <li><a href="#td3_ex10">Exercice 10 – Formes normales de fonctions valides et insatisfiables</a></li>
    <li><a href="#td3_ex11">Exercice 11 – Synthèse canonique FND/FNC depuis une table de vérité et preuve d'équivalence</a></li>
    <li><a href="#td3_ex12">Exercice 12 – Lecture directe d'une table de vérité depuis une FND ou une FNC</a></li>
    <li><a href="#td3_ex13">Exercice 13 – Transformation algébrique en FND et FNC sans table de vérité</a></li>
  </ul>
</div>

<div class="box info">
  <h4>Rappel des notations du TD de la Sorbonne</h4>
  <p>Dans les exercices 9 à 13 du polycopié officiel, les fonctions booléennes sont notées avec les conventions algébriques :</p>
  <ul>
    <li>Variables booléennes : {{ x, y, z \in \{0, 1\} }}.</li>
    <li>Complément (négation) : {{ \overline{x} = 1 - x }} ; Produit (ET) : {{ x \cdot y }} ; Somme (OU) : {{ x + y }}.</li>
    <li>En notation booléenne, une <strong>FND</strong> est une <strong>somme de produits de littéraux</strong>, et une <strong>FNC</strong> est un <strong>produit de sommes de littéraux</strong>.</li>
  </ul>
</div>

<!-- EXERCICE 9 -->
<h2 id="td3_ex9">Exercice 9 – Identification syntaxique des FND et FNC</h2>

<div class="q-card" id="td3_q9_1">
  <div class="q-header">
    <span class="q-num">Exercice 9 – Question 1</span>
    <span class="q-title">Reconnaître les expressions en FND, en FNC, les deux ou aucune</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Dans les expressions booléennes ci-dessous, {{ x, y }} et {{ z }} sont des variables booléennes. Identifier parmi ces expressions celles qui sont en forme normale disjonctive (FND) et celles qui sont en forme normale conjonctive (FNC).</p>
    <ol>
      <li>{{ x \cdot y + y \cdot \overline{z} }}</li>
      <li>{{ (x + y + z) \cdot (y + \overline{z}) }}</li>
      <li>{{ x \cdot (y + y \cdot \overline{z}) }}</li>
      <li>{{ (x + y) + (z \cdot (y + \overline{z})) }}</li>
      <li>{{ x \cdot y \cdot z }}</li>
      <li>{{ x + y + \overline{z} }}</li>
      <li>{{ x }}</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Analyse syntaxique détaillée des 7 expressions</summary>
    <div class="box method">
      <h4>Méthode d'analyse</h4>
      <p>La propriété « être en FND » ou « être en FNC » est purement <strong>syntaxique</strong> (elle dépend de la forme de l'arbre de l'expression et non de sa valeur sémantique). On inspecte l'opérateur principal à la racine, puis les sous-expressions de niveau 1 et 2 :</p>
      <ul>
        <li><strong>Expression 1 : {{ x \cdot y + y \cdot \overline{z} }}</strong>
          <br/>C'est une somme ({{ + }}) de deux termes {{ (x \cdot y) }} et {{ (y \cdot \overline{z}) }}, chacun étant un produit ({{ \cdot }}) de littéraux ({{ x, y, \overline{z} }}).
          <br/>Conclusion : <strong>FND uniquement</strong> (ce n'est pas une FNC car l'opérateur principal est {{ + }} appliqué à des produits contenant plusieurs littéraux).
        </li>
        <li><strong>Expression 2 : {{ (x + y + z) \cdot (y + \overline{z}) }}</strong>
          <br/>C'est un produit ({{ \cdot }}) de deux clauses {{ (x + y + z) }} et {{ (y + \overline{z}) }}, chacune étant une somme ({{ + }}) de littéraux.
          <br/>Conclusion : <strong>FNC uniquement</strong> (ce n'est pas une FND car l'opérateur principal est {{ \cdot }} appliqué à des sommes de plusieurs littéraux).
        </li>
        <li><strong>Expression 3 : {{ x \cdot (y + y \cdot \overline{z}) }}</strong>
          <br/>L'opérateur principal est un produit ({{ \cdot }}), mais le second facteur {{ (y + y \cdot \overline{z}) }} n'est pas une somme de littéraux : il contient lui-même un produit {{ y \cdot \overline{z} }} sous une somme (3 niveaux d'alternance {{ \cdot \to + \to \cdot }}).
          <br/>Conclusion : <strong>Ni FND, ni FNC</strong>.
        </li>
        <li><strong>Expression 4 : {{ (x + y) + (z \cdot (y + \overline{z})) }}</strong>
          <br/>L'opérateur principal est une somme ({{ + }}), mais le sous-terme {{ z \cdot (y + \overline{z}) }} est un produit dont le second facteur {{ (y + \overline{z}) }} est une somme et non un littéral (alternance {{ + \to \cdot \to + }}).
          <br/>Conclusion : <strong>Ni FND, ni FNC</strong>.
        </li>
        <li><strong>Expression 5 : {{ x \cdot y \cdot z }}</strong>
          <br/>– Vu comme une somme d'<strong>un seul produit</strong> {{ (x \cdot y \cdot z) }} de trois littéraux : c'est une <strong>FND</strong>.
          <br/>– Vu comme un produit de <strong>trois clauses unitaires</strong> {{ (x) \cdot (y) \cdot (z) }} (chacune étant une somme d'un seul littéral) : c'est aussi une <strong>FNC</strong> !
          <br/>Conclusion : <strong>À la fois FND et FNC</strong>.
        </li>
        <li><strong>Expression 6 : {{ x + y + \overline{z} }}</strong>
          <br/>– Vu comme un produit d'<strong>une seule clause</strong> {{ (x + y + \overline{z}) }} de trois littéraux : c'est une <strong>FNC</strong>.
          <br/>– Vu comme une somme de <strong>trois termes unitaires</strong> {{ (x) + (y) + (\overline{z}) }} (chacun étant un produit d'un seul littéral) : c'est aussi une <strong>FND</strong> !
          <br/>Conclusion : <strong>À la fois FND et FNC</strong>.
        </li>
        <li><strong>Expression 7 : {{ x }}</strong>
          <br/>Un littéral isolé {{ x }} est simultanément un terme d'un seul littéral (somme d'un seul produit d'un seul littéral) et une clause d'un seul littéral (produit d'une seule somme d'un seul littéral).
          <br/>Conclusion : <strong>À la fois FND et FNC</strong>.
        </li>
      </ul>

      <h4>Tableau récapitulatif</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>N°</th>
            <th>Expression</th>
            <th>FND ?</th>
            <th>FNC ?</th>
            <th>Justification</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ x \cdot y + y \cdot \overline{z} }}</td><td><strong>OUI</strong></td><td>NON</td><td>Somme de 2 produits de littéraux</td></tr>
          <tr><td>2</td><td>{{ (x + y + z) \cdot (y + \overline{z}) }}</td><td>NON</td><td><strong>OUI</strong></td><td>Produit de 2 sommes de littéraux</td></tr>
          <tr><td>3</td><td>{{ x \cdot (y + y \cdot \overline{z}) }}</td><td>NON</td><td>NON</td><td>Produit contenant un produit imbriqué sous une somme</td></tr>
          <tr><td>4</td><td>{{ (x + y) + (z \cdot (y + \overline{z})) }}</td><td>NON</td><td>NON</td><td>Somme contenant une somme imbriquée sous un produit</td></tr>
          <tr><td>5</td><td>{{ x \cdot y \cdot z }}</td><td><strong>OUI</strong></td><td><strong>OUI</strong></td><td>1 produit de 3 littéraux = produit de 3 clauses unitaires</td></tr>
          <tr><td>6</td><td>{{ x + y + \overline{z} }}</td><td><strong>OUI</strong></td><td><strong>OUI</strong></td><td>Somme de 3 termes unitaires = 1 clause de 3 littéraux</td></tr>
          <tr><td>7</td><td>{{ x }}</td><td><strong>OUI</strong></td><td><strong>OUI</strong></td><td>Littéral isolé (cas dégénéré commun aux deux formes)</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 10 -->
<h2 id="td3_ex10">Exercice 10 – Formes normales de fonctions valides et insatisfiables</h2>

<div class="q-card" id="td3_q10_1">
  <div class="q-header">
    <span class="q-num">Exercice 10 – Question 1</span>
    <span class="q-title">Fonction booléenne valide {{ f(x, y, z) = 1 }} : construction de FNC et FND</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit {{ f(x, y, z) }} une fonction booléenne valide, i.e. prenant la valeur {{ 1 }} quels que soient {{ x, y }} et {{ z }}.</p>
    <ul>
      <li>Donner une forme normale conjonctive (FNC) de {{ f }} contenant au moins 3 sommes différentes. Combien de sommes sont nécessaires au minimum ?</li>
      <li>Donner une forme normale disjonctive (FND) de {{ f }} contenant au moins 3 produits différents. Combien de produits sont nécessaires au minimum ?</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 1</summary>
    <div class="box method">
      <h4>1. Forme Normale Conjonctive (FNC) d'une fonction valide {{ f(x, y, z) \equiv 1 }}</h4>
      <p><strong>Rappel théorique :</strong> Un produit de sommes {{ C_1 \cdot C_2 \cdots C_m }} vaut {{ 1 }} pour tout {{ (x, y, z) \in \{0, 1\}^3 }} si et seulement si <strong>chacune des sommes {{ C_j }} vaut {{ 1 }}</strong> partout, c'est-à-dire si chaque somme {{ C_j }} contient au moins une variable et son complément ({{ u + \overline{u} = 1 }}).</p>
      <ul>
        <li><strong>Exemple de FNC avec au moins 3 sommes différentes :</strong>
          <div style="margin:6px 0;">
            {{ f(x, y, z) = (x + \overline{x} + y) \cdot (y + \overline{y} + z) \cdot (x + z + \overline{z}) }}
          </div>
          Chacune des 3 clauses contient une paire complémentaire ({{ x + \overline{x} = 1 }}, {{ y + \overline{y} = 1 }}, {{ z + \overline{z} = 1 }}), donc {{ f(x, y, z) = 1 \cdot 1 \cdot 1 = 1 }} pour tout {{ (x, y, z) }}.
        </li>
        <li><strong>Nombre minimum de sommes nécessaires en FNC :</strong>
          <br/>Il suffit d'<strong>une seule somme ({{ 1 }} clause)</strong> ! Par exemple :
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x + \overline{x} }} \quad (\text{ou } {{ x + \overline{x} + y + z }})
          </div>
          En effet, une somme unique de littéraux {{ x + \overline{x} }} est bien un produit d'une seule somme, donc une FNC valide.
        </li>
      </ul>

      <h4>2. Forme Normale Disjonctive (FND) d'une fonction valide {{ f(x, y, z) \equiv 1 }}</h4>
      <p><strong>Analyse :</strong> Une somme de produits {{ T_1 + T_2 + \dots + T_k }} vaut {{ 1 }} partout si les termes {{ T_i }} couvrent l'intégralité de l'espace des {{ 2^3 = 8 }} triplets {{ (x, y, z) \in \{0, 1\}^3 }}.</p>
      <ul>
        <li><strong>Exemple de FND avec au moins 3 produits différents :</strong>
          <br/>Partitionnons l'espace selon les valeurs de {{ x }} et {{ y }} :
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x \cdot y + x \cdot \overline{y} + \overline{x} }}
          </div>
          Vérification algébrique : {{ x \cdot y + x \cdot \overline{y} + \overline{x} = x \cdot (y + \overline{y}) + \overline{x} = x \cdot 1 + \overline{x} = x + \overline{x} = 1 }}.
          <br/>(On peut aussi donner la FND canonique complète à 8 mintermes, ou à 4 termes : {{ x \cdot y + x \cdot \overline{y} + \overline{x} \cdot y + \overline{x} \cdot \overline{y} }}).
        </li>
        <li><strong>Nombre minimum de produits nécessaires en FND :</strong>
          <br/>Il faut au minimum <strong>{{ 2 }} produits</strong> ! Par exemple :
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x + \overline{x} }}
          </div>
          (où {{ x }} et {{ \overline{x} }} sont deux produits d'un seul littéral chacun).
          <br/><em>Pourquoi {{ 1 }} seul produit est-il impossible ?</em> Un produit unique de littéraux {{ \ell_1 \cdot \ell_2 \cdots \ell_r }} (avec {{ r \geq 1 }}) s'annule dès que l'on choisit l'interprétation qui met {{ \ell_1 = 0 }} (par exemple si {{ \ell_1 = x }}, il vaut {{ 0 }} pour {{ x = 0 }} ; et si le produit contient {{ x \cdot \overline{x} }}, il vaut toujours {{ 0 }}). Un seul terme ne peut donc jamais couvrir tout l'espace {{ \{0, 1\}^3 }}. Il faut au minimum {{ 2 }} produits.
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q10_2">
  <div class="q-header">
    <span class="q-num">Exercice 10 – Question 2</span>
    <span class="q-title">Fonction booléenne insatisfiable {{ g(x, y, z) = 0 }} : construction de FNC et FND</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit {{ g(x, y, z) }} une fonction booléenne insatisfiable, i.e. prenant la valeur {{ 0 }} quels que soient {{ x, y }} et {{ z }}.</p>
    <ul>
      <li>Donner une forme normale conjonctive (FNC) de {{ g }} contenant au moins 3 sommes différentes. Combien de sommes sont nécessaires au minimum ?</li>
      <li>Donner une forme normale disjonctive (FND) de {{ g }} contenant au moins 3 produits différents. Combien de produits sont nécessaires au minimum ?</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 2 (par dualité avec la Question 1)</summary>
    <div class="box method">
      <h4>1. Forme Normale Conjonctive (FNC) d'une fonction insatisfiable {{ g(x, y, z) \equiv 0 }}</h4>
      <p><strong>Analyse :</strong> Un produit de sommes {{ C_1 \cdot C_2 \cdots C_m }} vaut {{ 0 }} partout si et seulement si, pour tout triplet {{ (x, y, z) \in \{0, 1\}^3 }}, au moins l'une des clauses {{ C_j }} s'annule.</p>
      <ul>
        <li><strong>Exemple de FNC avec au moins 3 sommes différentes :</strong>
          <div style="margin:6px 0;">
            {{ g(x, y, z) = (x + y) \cdot (x + \overline{y}) \cdot \overline{x} }}
          </div>
          Vérification algébrique : {{ (x + y) \cdot (x + \overline{y}) \cdot \overline{x} = (x + y \cdot \overline{y}) \cdot \overline{x} = (x + 0) \cdot \overline{x} = x \cdot \overline{x} = 0 }}.
          <br/>(Autre exemple encore plus simple : {{ x \cdot \overline{x} \cdot (y + z) }}, qui est le produit des 3 clauses différentes {{ (x) }}, {{ (\overline{x}) }} et {{ (y + z) }}).
        </li>
        <li><strong>Nombre minimum de sommes nécessaires en FNC :</strong>
          <br/>Il faut au minimum <strong>{{ 2 }} sommes</strong> ! Par exemple :
          <div style="margin:6px 0;">
            {{ g(x, y, z) = (x) \cdot (\overline{x}) }}
          </div>
          (produit de deux clauses unitaires).
          <br/><em>Pourquoi {{ 1 }} seule somme est-elle impossible ?</em> Une clause unique non vide {{ \ell_1 + \ell_2 + \dots + \ell_r }} (avec {{ r \geq 1 }}) vaut {{ 1 }} dès que l'on affecte la valeur {{ 1 }} au premier littéral {{ \ell_1 }} (et si elle contient {{ x + \overline{x} }}, elle vaut toujours {{ 1 }}). Une seule somme ne peut donc jamais être constamment nulle.
        </li>
      </ul>

      <h4>2. Forme Normale Disjonctive (FND) d'une fonction insatisfiable {{ g(x, y, z) \equiv 0 }}</h4>
      <p><strong>Rappel théorique :</strong> Une somme de produits {{ T_1 + T_2 + \dots + T_k }} vaut {{ 0 }} partout si et seulement si <strong>chacun des produits {{ T_i }} vaut {{ 0 }}</strong> partout, c'est-à-dire si chaque produit {{ T_i }} contient une variable et son complément ({{ u \cdot \overline{u} = 0 }}).</p>
      <ul>
        <li><strong>Exemple de FND avec au moins 3 produits différents :</strong>
          <div style="margin:6px 0;">
            {{ g(x, y, z) = x \cdot \overline{x} \cdot y + y \cdot \overline{y} \cdot z + x \cdot z \cdot \overline{z} }}
          </div>
          Chacun des 3 termes contient une paire contradictoire ({{ x \cdot \overline{x} = 0 }}, {{ y \cdot \overline{y} = 0 }}, {{ z \cdot \overline{z} = 0 }}), d'où {{ g(x, y, z) = 0 + 0 + 0 = 0 }}.
        </li>
        <li><strong>Nombre minimum de produits nécessaires en FND :</strong>
          <br/>Il suffit d'<strong>un seul produit ({{ 1 }} terme)</strong> ! Par exemple :
          <div style="margin:6px 0;">
            {{ g(x, y, z) = x \cdot \overline{x} }}
          </div>
          Ce terme unique est bien une FND (somme d'un seul produit de deux littéraux) et vaut {{ 0 }} pour toute interprétation.
        </li>
      </ul>

      <h4>Tableau de synthèse (symétrie duale Question 1 / Question 2)</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>Nature de la fonction</th>
            <th>Minimum de clauses en FNC</th>
            <th>Minimum de termes en FND</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Valide ({{ \equiv 1 }})</strong></td>
            <td><strong>1 somme</strong> : {{ x + \overline{x} }}</td>
            <td><strong>2 produits</strong> : {{ x + \overline{x} }}</td>
          </tr>
          <tr>
            <td><strong>Insatisfiable ({{ \equiv 0 }})</strong></td>
            <td><strong>2 sommes</strong> : {{ x \cdot \overline{x} }}</td>
            <td><strong>1 produit</strong> : {{ x \cdot \overline{x} }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 11 -->
<h2 id="td3_ex11">Exercice 11 – Synthèse canonique FND/FNC et preuve d'équivalence</h2>

<div class="q-card" id="td3_q11_1">
  <div class="q-header">
    <span class="q-num">Exercice 11 – Question 1</span>
    <span class="q-title">Fonction booléenne du OU exclusif (XOR) : table de vérité, FND et FNC</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Rappeler la table de vérité de la fonction booléenne correspondant au « ou exclusif » et en déduire une expression booléenne en FND et une expression booléenne en FNC de cette fonction.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 1</summary>
    <div class="box method">
      <h4>1. Table de vérité de {{ \text{xor}(x, y) }}</h4>
      <p>La fonction {{ \text{xor}(x, y) }} vaut {{ 1 }} si et seulement si exactement l'un des deux arguments {{ x }} ou {{ y }} vaut {{ 1 }} ({{ x \neq y }}) :</p>
      <table class="tt-table">
        <thead>
          <tr>
            <th>Ligne</th>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ \text{xor}(x, y) }}</th>
            <th>Minterme (si {{ = 1 }})</th>
            <th>Maxterme (si {{ = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td><td>—</td><td>{{ x + y }}</td></tr>
          <tr><td>2</td><td>0</td><td>1</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot y }}</td><td>—</td></tr>
          <tr><td>3</td><td>1</td><td>0</td><td><strong>1</strong></td><td>{{ x \cdot \overline{y} }}</td><td>—</td></tr>
          <tr><td>4</td><td>1</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + \overline{y} }}</td></tr>
        </tbody>
      </table>

      <h4>2. Déduction de la FND canonique (lignes où {{ \text{xor}(x, y) = 1 }})</h4>
      <p>La fonction vaut {{ 1 }} sur les lignes 2 ({{ x = 0, y = 1 \mapsto \overline{x} \cdot y }}) et 3 ({{ x = 1, y = 0 \mapsto x \cdot \overline{y} }}). On additionne ces deux mintermes :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FND}(\text{xor})(x, y) = \overline{x} \cdot y + x \cdot \overline{y} }}
      </p>

      <h4>3. Déduction de la FNC canonique (lignes où {{ \text{xor}(x, y) = 0 }})</h4>
      <p>La fonction vaut {{ 0 }} sur les lignes 1 ({{ x = 0, y = 0 }}, maxterme {{ x + y }}) et 4 ({{ x = 1, y = 1 }}, maxterme {{ \overline{x} + \overline{y} }}). On multiplie ces deux maxtermes :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FNC}(\text{xor})(x, y) = (x + y) \cdot (\overline{x} + \overline{y}) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q11_2">
  <div class="q-header">
    <span class="q-num">Exercice 11 – Question 2</span>
    <span class="q-title">Fonction {{ f(x, y) }} valant {{ 1 }} uniquement en {{ (0, 0) }} : FND et FNC</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Donner l'expression booléenne de la fonction {{ f(x, y) }} qui vaut {{ 1 }} si et seulement si {{ x }} et {{ y }} valent {{ 0 }}. Donner sa forme normale disjonctive (FND) et sa forme normale conjonctive (FNC).</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 2</summary>
    <div class="box method">
      <h4>1. Table de vérité de {{ f(x, y) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>Ligne</th>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ f(x, y) }}</th>
            <th>Minterme ({{ f = 1 }})</th>
            <th>Maxterme ({{ f = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot \overline{y} }}</td><td>—</td></tr>
          <tr><td>2</td><td>0</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ x + \overline{y} }}</td></tr>
          <tr><td>3</td><td>1</td><td>0</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + y }}</td></tr>
          <tr><td>4</td><td>1</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + \overline{y} }}</td></tr>
        </tbody>
      </table>

      <h4>2. Forme Normale Disjonctive (FND)</h4>
      <p>Il y a une seule ligne où {{ f(x, y) = 1 }} : la ligne {{ (0, 0) }}, dont le minterme est {{ \overline{x} \cdot \overline{y} }}.</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FND}(f)(x, y) = \overline{x} \cdot \overline{y} }}
      </p>
      <p><em>Remarque :</em> {{ \overline{x} \cdot \overline{y} }} est aussi une FNC (produit de deux clauses unitaires {{ (\overline{x}) \cdot (\overline{y}) }}), mais calculons également la FNC canonique par les maxtermes pour répondre à la Question 3 !</p>

      <h4>3. Forme Normale Conjonctive canonique (FNC par maxtermes)</h4>
      <p>Il y a trois lignes où {{ f(x, y) = 0 }} : {{ (0, 1) }}, {{ (1, 0) }} et {{ (1, 1) }}. Le produit des trois maxtermes correspondants donne la FNC canonique :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FNC}(f)(x, y) = (\overline{x} + y) \cdot (x + \overline{y}) \cdot (\overline{x} + \overline{y}) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q11_3">
  <div class="q-header">
    <span class="q-num">Exercice 11 – Question 3</span>
    <span class="q-title">Déduire l'équivalence logique {{ F |\equiv| G }} sans nouveau calcul</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Déduire de la question précédente que les formules {{ F = \neg A \land \neg B }} et {{ G = (\neg A \lor B) \land ((A \lor \neg B) \land (\neg A \lor \neg B)) }} sont équivalentes.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 3</summary>
    <div class="box method">
      <p>Traduisons les deux formules propositionnelles {{ F }} et {{ G }} en leurs fonctions booléennes associées {{ f_F(x, y) }} et {{ f_G(x, y) }} (en posant {{ x = I(A) }} et {{ y = I(B) }}) :</p>
      <ul>
        <li>Pour {{ F = \neg A \land \neg B }} :
          <div style="margin:6px 0;">
            {{ f_F(x, y) = \overline{x} \cdot \overline{y} }}
          </div>
          On reconnaît exactement la <strong>FND canonique</strong> de la fonction {{ f(x, y) }} de la Question 2.
        </li>
        <li>Pour {{ G = (\neg A \lor B) \land ((A \lor \neg B) \land (\neg A \lor \neg B)) }} :
          <div style="margin:6px 0;">
            {{ f_G(x, y) = (\overline{x} + y) \cdot (x + \overline{y}) \cdot (\overline{x} + \overline{y}) }}
          </div>
          On reconnaît exactement la <strong>FNC canonique</strong> (par les maxtermes) de cette même fonction {{ f(x, y) }} de la Question 2 !
        </li>
      </ul>
      <p>Puisque {{ f_F }} et {{ f_G }} représentent toutes deux la même fonction booléenne {{ f(x, y) }} (qui vaut {{ 1 }} ssi {{ x = 0 }} et {{ y = 0 }}), on a pour toute interprétation {{ I }} :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ [F]^I = f_F(I(A), I(B)) = f(I(A), I(B)) = f_G(I(A), I(B)) = [G]^I }}
      </p>
      <p>Par définition de l'équivalence sémantique, les formules {{ F }} et {{ G }} sont donc logiquement équivalentes : <strong>{{ F |\equiv| G }}</strong>.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 12 -->
<h2 id="td3_ex12">Exercice 12 – Lecture directe d'une table de vérité depuis une FND ou une FNC</h2>

<div class="q-card" id="td3_q12_1">
  <div class="q-header">
    <span class="q-num">Exercice 12 – Question 1</span>
    <span class="q-title">Déduire la table de vérité de {{ f(x, y, z) = x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>On considère la fonction booléenne {{ f(x, y, z) = x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z }}. En déduire sa table de vérité.</p>
  </div>

  <details class="sol" open>
    <summary>Méthode de lecture directe sans évaluer ligne par ligne</summary>
    <div class="box method">
      <h4>Principe de lecture directe d'une FND</h4>
      <p>La fonction {{ f }} est donnée en <strong>FND</strong> (somme de 3 produits). Une somme vaut {{ 1 }} dès qu'au moins l'un de ses produits vaut {{ 1 }}. Au lieu de calculer l'expression sur les 8 lignes, on identifie directement les triplets {{ (x, y, z) }} qui rendent chaque produit égal à {{ 1 }} :</p>
      <ul>
        <li><strong>Terme {{ T_1 = x \cdot y }} :</strong> vaut {{ 1 }} ssi {{ x = 1 }} et {{ y = 1 }} (quel que soit {{ z \in \{0, 1\} }}).
          <br/>Cela donne les 2 triplets : <strong>{{ (1, 1, 0) }}</strong> et <strong>{{ (1, 1, 1) }}</strong>.
        </li>
        <li><strong>Terme {{ T_2 = \overline{y} \cdot \overline{z} }} :</strong> vaut {{ 1 }} ssi {{ y = 0 }} et {{ z = 0 }} (quel que soit {{ x \in \{0, 1\} }}).
          <br/>Cela donne les 2 triplets : <strong>{{ (0, 0, 0) }}</strong> et <strong>{{ (1, 0, 0) }}</strong>.
        </li>
        <li><strong>Terme {{ T_3 = \overline{x} \cdot y \cdot z }} :</strong> vaut {{ 1 }} ssi {{ x = 0, y = 1 }} et {{ z = 1 }}.
          <br/>Cela donne le triplet : <strong>{{ (0, 1, 1) }}</strong>.
        </li>
      </ul>
      <p>Sur ces 5 triplets, {{ f(x, y, z) = 1 }} ; sur les 3 triplets restants {{ (0, 0, 1), (0, 1, 0), (1, 0, 1) }}, {{ f(x, y, z) = 0 }}.</p>

      <h4>Table de vérité complète de {{ f(x, y, z) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ z }}</th>
            <th>{{ f(x, y, z) }}</th>
            <th>Terme justificatif</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{y} \cdot \overline{z} = 1 }}</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td><td>Aucun terme à 1</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td><strong>0</strong></td><td>Aucun terme à 1</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot y \cdot z = 1 }}</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{y} \cdot \overline{z} = 1 }}</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td><strong>0</strong></td><td>Aucun terme à 1</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td><td>{{ x \cdot y = 1 }}</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td><td>{{ x \cdot y = 1 }}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q12_2">
  <div class="q-header">
    <span class="q-num">Exercice 12 – Question 2</span>
    <span class="q-title">Déduire la table de vérité de {{ g(x, y, z) = (x + y) \cdot (\overline{y} + \overline{z}) \cdot (\overline{x} + y + z) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>On considère la fonction booléenne {{ g(x, y, z) = (x + y) \cdot (\overline{y} + \overline{z}) \cdot (\overline{x} + y + z) }}. En déduire sa table de vérité.</p>
  </div>

  <details class="sol" open>
    <summary>Méthode de lecture directe par les zéros des clauses</summary>
    <div class="box method">
      <h4>Principe de lecture directe d'une FNC</h4>
      <p>La fonction {{ g }} est donnée en <strong>FNC</strong> (produit de 3 clauses). Un produit vaut {{ 0 }} dès qu'au moins l'une de ses sommes vaut {{ 0 }}. On identifie donc directement les triplets {{ (x, y, z) }} qui <strong>annulent chaque clause</strong> :</p>
      <ul>
        <li><strong>Clause {{ C_1 = x + y }} :</strong> vaut {{ 0 }} ssi {{ x = 0 }} et {{ y = 0 }} (quel que soit {{ z \in \{0, 1\} }}).
          <br/>Elle annule {{ g }} sur les 2 triplets : <strong>{{ (0, 0, 0) }}</strong> et <strong>{{ (0, 0, 1) }}</strong>.
        </li>
        <li><strong>Clause {{ C_2 = \overline{y} + \overline{z} }} :</strong> vaut {{ 0 }} ssi {{ \overline{y} = 0 }} et {{ \overline{z} = 0 }}, c'est-à-dire {{ y = 1 }} et {{ z = 1 }} (quel que soit {{ x \in \{0, 1\} }}).
          <br/>Elle annule {{ g }} sur les 2 triplets : <strong>{{ (0, 1, 1) }}</strong> et <strong>{{ (1, 1, 1) }}</strong>.
        </li>
        <li><strong>Clause {{ C_3 = \overline{x} + y + z }} :</strong> vaut {{ 0 }} ssi {{ \overline{x} = 0, y = 0 }} et {{ z = 0 }}, c'est-à-dire {{ x = 1, y = 0, z = 0 }}.
          <br/>Elle annule {{ g }} sur le triplet : <strong>{{ (1, 0, 0) }}</strong>.
        </li>
      </ul>
      <p>Sur ces 5 triplets, {{ g(x, y, z) = 0 }} ; sur les 3 triplets restants {{ (0, 1, 0), (1, 0, 1), (1, 1, 0) }}, aucune clause ne s'annule donc {{ g(x, y, z) = 1 }}.</p>
      <p><em>Observation remarquable :</em> En comparant avec la Question 1, on constate que {{ g(x, y, z) = \overline{f(x, y, z)} }} ! En effet, par la loi de De Morgan appliquée à {{ f }}, {{ \overline{f} = \overline{x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z} = (\overline{x} + \overline{y}) \cdot (y + z) \cdot (x + \overline{y} + \overline{z}) }}, ou ici les zéros de {{ g }} sont exactement les uns de {{ f }} !</p>

      <h4>Table de vérité complète de {{ g(x, y, z) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ z }}</th>
            <th>{{ g(x, y, z) }}</th>
            <th>Clause annulée (si {{ g = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td><strong>0</strong></td><td>{{ x + y = 0 }}</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td><td>{{ x + y = 0 }}</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td><strong>1</strong></td><td>Toutes les clauses valent 1</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td><strong>0</strong></td><td>{{ \overline{y} + \overline{z} = 0 }}</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td><td>{{ \overline{x} + y + z = 0 }}</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td><strong>1</strong></td><td>Toutes les clauses valent 1</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td><td>Toutes les clauses valent 1</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td><strong>0</strong></td><td>{{ \overline{y} + \overline{z} = 0 }}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 13 -->
<h2 id="td3_ex13">Exercice 13 – Transformation algébrique en FND et FNC sans table de vérité</h2>

<div class="q-card" id="td3_q13_1">
  <div class="q-header">
    <span class="q-num">Exercice 13 – Question 1</span>
    <span class="q-title">Fonction booléenne associée à {{ F = (A \land (B \lor C)) \lor (\neg A \land \neg B) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>On considère la formule {{ F = (A \land (B \lor C)) \lor (\neg A \land \neg B) }}. Pour répondre à cet exercice, vous ne devez pas utiliser de table de vérité.</p>
    <p><strong>Question 1 :</strong> Donner l'expression de la fonction booléenne associée à {{ F }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 1</summary>
    <div class="box method">
      <p>Associons aux variables propositionnelles {{ A, B, C }} les variables booléennes {{ x, y, z \in \{0, 1\} }} (où {{ x = I(A), y = I(B), z = I(C) }}). Par traduction inductive directe des connecteurs logiques ({{ \land \mapsto \cdot }}, {{ \lor \mapsto + }}, {{ \neg \mapsto \overline{\phantom{x}} }}), la fonction booléenne {{ f_F(x, y, z) }} associée à {{ F }} est :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">
        {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }}
      </p>
      <p><em>Remarque :</em> Cette expression n'est ni en FND (à cause du facteur {{ x \cdot (y + z) }}), ni en FNC (car l'opérateur principal est une somme {{ + }}).</p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q13_2">
  <div class="q-header">
    <span class="q-num">Exercice 13 – Question 2</span>
    <span class="q-title">Mise sous Forme Normale Disjonctive (FND) par calcul algébrique</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p><strong>Question 2 :</strong> Mettre cette fonction sous forme normale disjonctive.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 2</summary>
    <div class="box method">
      <p>Pour obtenir une FND (somme de produits de littéraux), il suffit de distribuer le produit {{ \cdot }} sur la somme {{ + }} dans le premier sous-terme {{ x \cdot (y + z) }} :</p>
      <div style="line-height:2.2em; font-size:1.05em;">
        {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }}<br/>
        {{ = x \cdot y + x \cdot z + \overline{x} \cdot \overline{y} }} \quad <em>(Distributivité de {{ \cdot }} sur {{ + }})</em>
      </div>
      <p>L'expression obtenue est une somme de 3 produits de littéraux ({{ x \cdot y }}, {{ x \cdot z }} et {{ \overline{x} \cdot \overline{y} }}) : elle est donc en <strong>Forme Normale Disjonctive (FND)</strong>.</p>
      <p>En revenant à la syntaxe propositionnelle, la formule en FND équivalente à {{ F }} est :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ F_{\text{FND}} = (A \land B) \lor (A \land C) \lor (\neg A \land \neg B) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q13_3">
  <div class="q-header">
    <span class="q-num">Exercice 13 – Question 3</span>
    <span class="q-title">Mise sous Forme Normale Conjonctive (FNC) par distributivité de {{ + }} sur {{ \cdot }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p><strong>Question 3 :</strong> Mettre cette fonction sous forme normale conjonctive.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée de la Question 3</summary>
    <div class="box method">
      <p>Partons de l'expression initiale {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }} (qui est plus factorisée que la FND, ce qui évite des développements inutiles !) et appliquons la distributivité de la somme {{ + }} sur le produit {{ \cdot }} :</p>
      <div style="line-height:2.3em; font-size:1.05em;">
        {{ f_F(x, y, z) = \underbrace{x \cdot (y + z)}_{U} + (\overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot (y + z) + \overline{x}) \cdot (x \cdot (y + z) + \overline{y}) }} \quad <em>(Distributivité de {{ + }} sur {{ \cdot }} : {{ U + \overline{x} \cdot \overline{y} = (U + \overline{x}) \cdot (U + \overline{y}) }})</em><br/>
        {{ = (\overline{x} + x \cdot (y + z)) \cdot (\overline{y} + x \cdot (y + z)) }} \quad <em>(Commutativité de {{ + }})</em><br/>
        {{ = (\overline{x} + x) \cdot (\overline{x} + y + z) \cdot (\overline{y} + x) \cdot (\overline{y} + y + z) }} \quad <em>(Distributivité de {{ + }} sur {{ \cdot }} dans chaque facteur)</em><br/>
        {{ = 1 \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot (1 + z) }} \quad <em>(Complémentarité : {{ \overline{x} + x = 1 }} et {{ \overline{y} + y = 1 }})</em><br/>
        {{ = 1 \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot 1 }} \quad <em>(Élément absorbant : {{ 1 + z = 1 }})</em><br/>
        {{ = (\overline{x} + y + z) \cdot (x + \overline{y}) }} \quad <em>(Élément neutre {{ 1 }} pour le produit {{ \cdot }})</em>
      </div>
      <p><em>Remarque :</em> Même si l'on ne simplifiait pas les clauses tautologiques {{ (x + \overline{x}) }} et {{ (y + \overline{y} + z) }}, le produit des 4 clauses {{ (x + \overline{x}) \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot (y + \overline{y} + z) }} est déjà syntaxiquement en FNC ! La forme simplifiée minimale est :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">
        {{ \text{FNC}(f_F)(x, y, z) = (\overline{x} + y + z) \cdot (x + \overline{y}) }}
      </p>
      <p>En revenant à la syntaxe propositionnelle, la formule en FNC équivalente à {{ F }} est :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ F_{\text{FNC}} = (\neg A \lor B \lor C) \land (A \lor \neg B) }}
      </p>
    </div>
  </details>
</div>
"""

fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>تمرین‌های هفته ۳ (TD 3): توابع بولی و فرم‌های نرمال (FND / FNC)</h1>
  <p class="lead">پاسخ‌نامه تشریحی و گام‌به‌گام ۵ تمرین رسمی جزوه TD سوربن (تمرین‌های ۹ تا ۱۳): تشخیص نحوی فرم‌های نرمال، معیارهای جبری اعتبار و ناسازگاری، سنتز کانونی با مین‌ترم‌ها و ماکس‌ترم‌ها، استخراج مستقیم جدول درستی و تبدیل جبری به FND/FNC بدون جدول درستی.</p>
</div>

<div class="toc-box">
  <h3>فهرست تمرین‌های TD</h3>
  <ul>
    <li><a href="#td3_ex9">تمرین ۹ – تشخیص نحوی فرم‌های نرمال FND و FNC</a></li>
    <li><a href="#td3_ex10">تمرین ۱۰ – فرم‌های نرمال توابع معتبر (توتولوژی) و ناسازگار (تناقض)</a></li>
    <li><a href="#td3_ex11">تمرین ۱۱ – سنتز کانونی FND/FNC از روی جدول درستی و اثبات هم‌ارزی</a></li>
    <li><a href="#td3_ex12">تمرین ۱۲ – استخراج مستقیم جدول درستی از روی FND یا FNC</a></li>
    <li><a href="#td3_ex13">تمرین ۱۳ – تبدیل جبری به FND و FNC بدون استفاده از جدول درستی</a></li>
  </ul>
</div>

<div class="box info">
  <h4>یادآوری نمادگذاری جزوه TD دانشگاه سوربن</h4>
  <p>در تمرین‌های ۹ تا ۱۳ جزوه رسمی، توابع بولی با قراردادهای جبری زیر نوشته می‌شوند:</p>
  <ul>
    <li>متغیرهای بولی: {{ x, y, z \in \{0, 1\} }}.</li>
    <li>متمم (نقیض): {{ \overline{x} = 1 - x }} ؛ حاصل‌ضرب (عطف): {{ x \cdot y }} ؛ حاصل‌جمع (فصل): {{ x + y }}.</li>
    <li>در نمادگذاری بولی، یک <strong>FND</strong> <strong>مجموعی از حاصل‌ضرب‌های لیترال‌ها</strong> و یک <strong>FNC</strong> <strong>حاصل‌ضربی از مجموع‌های لیترال‌ها</strong> است.</li>
  </ul>
</div>

<!-- EXERCICE 9 -->
<h2 id="td3_ex9">تمرین ۹ – تشخیص نحوی فرم‌های نرمال FND و FNC</h2>

<div class="q-card" id="td3_q9_1">
  <div class="q-header">
    <span class="q-num">تمرین ۹ – پرسش ۱</span>
    <span class="q-title">تشخیص عبارت‌های در فرم FND، در فرم FNC، هر دو یا هیچ‌کدام</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>در عبارت‌های بولی زیر، {{ x, y }} و {{ z }} متغیرهای بولی هستند. مشخص کنید کدام‌یک از این عبارت‌ها در فرم نرمال فصلی (FND) و کدام‌یک در فرم نرمال عطفی (FNC) قرار دارند.</p>
    <ol>
      <li>{{ x \cdot y + y \cdot \overline{z} }}</li>
      <li>{{ (x + y + z) \cdot (y + \overline{z}) }}</li>
      <li>{{ x \cdot (y + y \cdot \overline{z}) }}</li>
      <li>{{ (x + y) + (z \cdot (y + \overline{z})) }}</li>
      <li>{{ x \cdot y \cdot z }}</li>
      <li>{{ x + y + \overline{z} }}</li>
      <li>{{ x }}</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>تحلیل نحوی دقیق هر ۷ عبارت</summary>
    <div class="box method">
      <h4>روش تحلیل</h4>
      <p>ویژگی «در فرم FND بودن» یا «در فرم FNC بودن» کاملاً <strong>نحوی (Syntactic)</strong> است (به شکل درخت عبارت بستگی دارد، نه به مقدار معنایی آن). عملگر اصلی در ریشه و سپس زیرعبارت‌های سطح ۱ و ۲ را بررسی می‌کنیم:</p>
      <ul>
        <li><strong>عبارت ۱: {{ x \cdot y + y \cdot \overline{z} }}</strong>
          <br/>این عبارت یک مجموع ({{ + }}) از دو جمله {{ (x \cdot y) }} و {{ (y \cdot \overline{z}) }} است که هر یک حاصل‌ضربی ({{ \cdot }}) از لیترال‌ها ({{ x, y, \overline{z} }}) می‌باشند.
          <br/>نتیجه: <strong>فقط FND</strong> (فرم FNC نیست زیرا عملگر اصلی {{ + }} است که روی حاصل‌ضرب‌های چندلیترالی عمل می‌کند).
        </li>
        <li><strong>عبارت ۲: {{ (x + y + z) \cdot (y + \overline{z}) }}</strong>
          <br/>این عبارت یک حاصل‌ضرب ({{ \cdot }}) از دو بند {{ (x + y + z) }} و {{ (y + \overline{z}) }} است که هر یک مجموعی ({{ + }}) از لیترال‌ها هستند.
          <br/>نتیجه: <strong>فقط FNC</strong> (فرم FND نیست زیرا عملگر اصلی {{ \cdot }} است که روی مجموع‌های چندلیترالی عمل می‌کند).
        </li>
        <li><strong>عبارت ۳: {{ x \cdot (y + y \cdot \overline{z}) }}</strong>
          <br/>عملگر اصلی حاصل‌ضرب ({{ \cdot }}) است، اما عامل دوم یعنی {{ (y + y \cdot \overline{z}) }} مجموعی ساده از لیترال‌ها نیست بلکه خودش شامل یک حاصل‌ضرب {{ y \cdot \overline{z} }} در زیرِ جمع است (۳ سطح تناوب {{ \cdot \to + \to \cdot }}).
          <br/>نتیجه: <strong>نه FND و نه FNC</strong>.
        </li>
        <li><strong>عبارت ۴: {{ (x + y) + (z \cdot (y + \overline{z})) }}</strong>
          <br/>عملگر اصلی جمع ({{ + }}) است، اما زیرجمله {{ z \cdot (y + \overline{z}) }} حاصل‌ضربی است که عامل دوم آن یعنی {{ (y + \overline{z}) }} یک جمع است نه یک لیترال (تناوب {{ + \to \cdot \to + }}).
          <br/>نتیجه: <strong>نه FND و نه FNC</strong>.
        </li>
        <li><strong>عبارت ۵: {{ x \cdot y \cdot z }}</strong>
          <br/>– اگر آن را مجموعی متشکل از <strong>یک حاصل‌ضرب واحد</strong> {{ (x \cdot y \cdot z) }} از سه لیترال ببینیم: یک <strong>FND</strong> است.
          <br/>– اگر آن را حاصل‌ضربی از <strong>سه بند یک‌لیترالی (واحد)</strong> {{ (x) \cdot (y) \cdot (z) }} ببینیم: یک <strong>FNC</strong> نیز هست!
          <br/>نتیجه: <strong>هم FND و هم FNC</strong>.
        </li>
        <li><strong>عبارت ۶: {{ x + y + \overline{z} }}</strong>
          <br/>– اگر آن را حاصل‌ضربی متشکل از <strong>یک بند واحد</strong> {{ (x + y + \overline{z}) }} از سه لیترال ببینیم: یک <strong>FNC</strong> است.
          <br/>– اگر آن را مجموعی از <strong>سه جمله یک‌لیترالی</strong> {{ (x) + (y) + (\overline{z}) }} ببینیم: یک <strong>FND</strong> نیز هست!
          <br/>نتیجه: <strong>هم FND و هم FNC</strong>.
        </li>
        <li><strong>عبارت ۷: {{ x }}</strong>
          <br/>یک لیترال منفرد {{ x }} هم‌زمان یک جمله تک‌لیترالی (مجموعِ یک حاصل‌ضربِ یک‌لیترالی) و یک بند تک‌لیترالی (حاصل‌ضربِ یک مجموعِ یک‌لیترالی) است.
          <br/>نتیجه: <strong>هم FND و هم FNC</strong>.
        </li>
      </ul>

      <h4>جدول جمع‌بندی</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>شماره</th>
            <th>عبارت بولی</th>
            <th>آیا FND است؟</th>
            <th>آیا FNC است؟</th>
            <th>توجیه نحوی</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ x \cdot y + y \cdot \overline{z} }}</td><td><strong>بله</strong></td><td>خیر</td><td>مجموع ۲ حاصل‌ضرب از لیترال‌ها</td></tr>
          <tr><td>2</td><td>{{ (x + y + z) \cdot (y + \overline{z}) }}</td><td>خیر</td><td><strong>بله</strong></td><td>حاصل‌ضرب ۲ مجموع از لیترال‌ها</td></tr>
          <tr><td>3</td><td>{{ x \cdot (y + y \cdot \overline{z}) }}</td><td>خیر</td><td>خیر</td><td>حاصل‌ضرب دارای ضرب تودرتو در زیر جمع</td></tr>
          <tr><td>4</td><td>{{ (x + y) + (z \cdot (y + \overline{z})) }}</td><td>خیر</td><td>خیر</td><td>مجموع دارای جمع تودرتو در زیر ضرب</td></tr>
          <tr><td>5</td><td>{{ x \cdot y \cdot z }}</td><td><strong>بله</strong></td><td><strong>بله</strong></td><td>۱ حاصل‌ضرب ۳ لیترالی = حاصل‌ضرب ۳ بند واحد</td></tr>
          <tr><td>6</td><td>{{ x + y + \overline{z} }}</td><td><strong>بله</strong></td><td><strong>بله</strong></td><td>مجموع ۳ جمله واحد = ۱ بند ۳ لیترالی</td></tr>
          <tr><td>7</td><td>{{ x }}</td><td><strong>بله</strong></td><td><strong>بله</strong></td><td>لیترال منفرد (حالت حدی مشترک هر دو فرم)</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 10 -->
<h2 id="td3_ex10">تمرین ۱۰ – فرم‌های نرمال توابع معتبر (توتولوژی) و ناسازگار (تناقض)</h2>

<div class="q-card" id="td3_q10_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۰ – پرسش ۱</span>
    <span class="q-title">تابع بولی معتبر {{ f(x, y, z) = 1 }}: ساخت FNC و FND</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>فرض کنید {{ f(x, y, z) }} یک تابع بولی معتبر باشد، یعنی به ازای هر مقادیر {{ x, y }} و {{ z }} مقدار {{ 1 }} بگیرد.</p>
    <ul>
      <li>یک فرم نرمال عطفی (FNC) برای {{ f }} بنویسید که شامل حداقل ۳ مجموع متفاوت باشد. حداقل چند مجموع لازم است؟</li>
      <li>یک فرم نرمال فصلی (FND) برای {{ f }} بنویسید که شامل حداقل ۳ حاصل‌ضرب متفاوت باشد. حداقل چند حاصل‌ضرب لازم است؟</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۱</summary>
    <div class="box method">
      <h4>۱. فرم نرمال عطفی (FNC) یک تابع معتبر {{ f(x, y, z) \equiv 1 }}</h4>
      <p><strong>یادآوری نظری:</strong> حاصل‌ضرب چند مجموع {{ C_1 \cdot C_2 \cdots C_m }} به ازای هر {{ (x, y, z) \in \{0, 1\}^3 }} برابر {{ 1 }} است اگر و تنها اگر <strong>تک‌تک مجموع‌های {{ C_j }} همواره برابر {{ 1 }} باشند</strong>؛ یعنی هر مجموع {{ C_j }} حداقل شامل یک متغیر و متمم آن ({{ u + \overline{u} = 1 }}) باشد.</p>
      <ul>
        <li><strong>مثال از FNC با حداقل ۳ مجموع متفاوت:</strong>
          <div style="margin:6px 0;">
            {{ f(x, y, z) = (x + \overline{x} + y) \cdot (y + \overline{y} + z) \cdot (x + z + \overline{z}) }}
          </div>
          هر یک از ۳ بند بالا شامل یک جفت مکمل است ({{ x + \overline{x} = 1 }}، {{ y + \overline{y} = 1 }}، {{ z + \overline{z} = 1 }})، لذا {{ f(x, y, z) = 1 \cdot 1 \cdot 1 = 1 }} به ازای هر {{ (x, y, z) }}.
        </li>
        <li><strong>حداقل تعداد مجموع‌های لازم در FNC:</strong>
          <br/>تنها <strong>یک مجموع ({{ 1 }} بند)</strong> کافی است! برای نمونه:
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x + \overline{x} }} \quad (\text{or } {{ x + \overline{x} + y + z }})
          </div>
          زیرا یک مجموع واحد از لیترال‌ها یعنی {{ x + \overline{x} }} حاصل‌ضربی متشکل از یک بند است و یک FNC معتبر محسوب می‌شود.
        </li>
      </ul>

      <h4>۲. فرم نرمال فصلی (FND) یک تابع معتبر {{ f(x, y, z) \equiv 1 }}</h4>
      <p><strong>تحلیل:</strong> مجموع چند حاصل‌ضرب {{ T_1 + T_2 + \dots + T_k }} همواره برابر {{ 1 }} است اگر جمله‌های {{ T_i }} تمام فضای {{ 2^3 = 8 }} سه‌تایی {{ (x, y, z) \in \{0, 1\}^3 }} را پوشش دهند.</p>
      <ul>
        <li><strong>مثال از FND با حداقل ۳ حاصل‌ضرب متفاوت:</strong>
          <br/>فضا را بر حسب مقادیر {{ x }} و {{ y }} افراز می‌کنیم:
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x \cdot y + x \cdot \overline{y} + \overline{x} }}
          </div>
          بررسی جبری: {{ x \cdot y + x \cdot \overline{y} + \overline{x} = x \cdot (y + \overline{y}) + \overline{x} = x \cdot 1 + \overline{x} = x + \overline{x} = 1 }}.
          <br/>(همچنین می‌توان FND کانونی کامل با ۸ مین‌ترم یا با ۴ جمله {{ x \cdot y + x \cdot \overline{y} + \overline{x} \cdot y + \overline{x} \cdot \overline{y} }} را نوشت).
        </li>
        <li><strong>حداقل تعداد حاصل‌ضرب‌های لازم در FND:</strong>
          <br/>حداقل <strong>{{ 2 }} حاصل‌ضرب</strong> لازم است! برای نمونه:
          <div style="margin:6px 0;">
            {{ f(x, y, z) = x + \overline{x} }}
          </div>
          (که در آن {{ x }} و {{ \overline{x} }} دو حاصل‌ضربِ تک‌لیترالی هستند).
          <br/><em>چرا {{ 1 }} حاصل‌ضرب تنها غیرممکن است؟</em> یک حاصل‌ضرب منفرد از لیترال‌ها {{ \ell_1 \cdot \ell_2 \cdots \ell_r }} (با {{ r \geq 1 }}) به محض انتخاب تعبیری که {{ \ell_1 = 0 }} قرار دهد صفر می‌شود (مثلاً اگر {{ \ell_1 = x }} باشد، به ازای {{ x = 0 }} صفر می‌شود؛ و اگر شامل {{ x \cdot \overline{x} }} باشد، همیشه {{ 0 }} است). پس یک جمله تنها هرگز نمی‌تواند تمام فضای {{ \{0, 1\}^3 }} را پوشش دهد و حداقل {{ 2 }} حاصل‌ضرب لازم است.
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q10_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۰ – پرسش ۲</span>
    <span class="q-title">تابع بولی ناسازگار {{ g(x, y, z) = 0 }}: ساخت FNC و FND</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>فرض کنید {{ g(x, y, z) }} یک تابع بولی ناسازگار باشد، یعنی به ازای هر مقادیر {{ x, y }} و {{ z }} مقدار {{ 0 }} بگیرد.</p>
    <ul>
      <li>یک فرم نرمال عطفی (FNC) برای {{ g }} بنویسید که شامل حداقل ۳ مجموع متفاوت باشد. حداقل چند مجموع لازم است؟</li>
      <li>یک فرم نرمال فصلی (FND) برای {{ g }} بنویسید که شامل حداقل ۳ حاصل‌ضرب متفاوت باشد. حداقل چند حاصل‌ضرب لازم است؟</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۲ (به کمک دوگانگی با پرسش ۱)</summary>
    <div class="box method">
      <h4>۱. فرم نرمال عطفی (FNC) یک تابع ناسازگار {{ g(x, y, z) \equiv 0 }}</h4>
      <p><strong>تحلیل:</strong> حاصل‌ضرب چند مجموع {{ C_1 \cdot C_2 \cdots C_m }} همواره برابر {{ 0 }} است اگر و تنها اگر به ازای هر سه‌تایی {{ (x, y, z) \in \{0, 1\}^3 }}، حداقل یکی از بندهای {{ C_j }} صفر شود.</p>
      <ul>
        <li><strong>مثال از FNC با حداقل ۳ مجموع متفاوت:</strong>
          <div style="margin:6px 0;">
            {{ g(x, y, z) = (x + y) \cdot (x + \overline{y}) \cdot \overline{x} }}
          </div>
          بررسی جبری: {{ (x + y) \cdot (x + \overline{y}) \cdot \overline{x} = (x + y \cdot \overline{y}) \cdot \overline{x} = (x + 0) \cdot \overline{x} = x \cdot \overline{x} = 0 }}.
          <br/>(مثال ساده‌تر دیگر: {{ x \cdot \overline{x} \cdot (y + z) }} که حاصل‌ضرب ۳ بند متفاوت {{ (x) }}، {{ (\overline{x}) }} و {{ (y + z) }} است).
        </li>
        <li><strong>حداقل تعداد مجموع‌های لازم در FNC:</strong>
          <br/>حداقل <strong>{{ 2 }} مجموع</strong> لازم است! برای نمونه:
          <div style="margin:6px 0;">
            {{ g(x, y, z) = (x) \cdot (\overline{x}) }}
          </div>
          (حاصل‌ضرب دو بند یک‌لیترالی).
          <br/><em>چرا {{ 1 }} مجموع تنها غیرممکن است؟</em> یک بند منفرد ناتهی {{ \ell_1 + \ell_2 + \dots + \ell_r }} (با {{ r \geq 1 }}) به محض آن‌که به لیترال اول {{ \ell_1 }} مقدار {{ 1 }} بدهیم برابر {{ 1 }} می‌شود (و اگر شامل {{ x + \overline{x} }} باشد همیشه {{ 1 }} است). پس یک مجموع تنها هرگز نمی‌تواند همواره صفر باشد.
        </li>
      </ul>

      <h4>۲. فرم نرمال فصلی (FND) یک تابع ناسازگار {{ g(x, y, z) \equiv 0 }}</h4>
      <p><strong>یادآوری نظری:</strong> مجموع چند حاصل‌ضرب {{ T_1 + T_2 + \dots + T_k }} همواره برابر {{ 0 }} است اگر و تنها اگر <strong>تک‌تک حاصل‌ضرب‌های {{ T_i }} همواره برابر {{ 0 }} باشند</strong>؛ یعنی هر حاصل‌ضرب {{ T_i }} شامل یک متغیر و متمم آن ({{ u \cdot \overline{u} = 0 }}) باشد.</p>
      <ul>
        <li><strong>مثال از FND با حداقل ۳ حاصل‌ضرب متفاوت:</strong>
          <div style="margin:6px 0;">
            {{ g(x, y, z) = x \cdot \overline{x} \cdot y + y \cdot \overline{y} \cdot z + x \cdot z \cdot \overline{z} }}
          </div>
          هر یک از ۳ جمله بالا شامل یک جفت متناقض است ({{ x \cdot \overline{x} = 0 }}، {{ y \cdot \overline{y} = 0 }}، {{ z \cdot \overline{z} = 0 }})، بنابراین {{ g(x, y, z) = 0 + 0 + 0 = 0 }}.
        </li>
        <li><strong>حداقل تعداد حاصل‌ضرب‌های لازم در FND:</strong>
          <br/>تنها <strong>یک حاصل‌ضرب ({{ 1 }} جمله)</strong> کافی است! برای نمونه:
          <div style="margin:6px 0;">
            {{ g(x, y, z) = x \cdot \overline{x} }}
          </div>
          این جمله واحد یک FND (مجموعِ یک حاصل‌ضرب دو لیترالی) است و به ازای هر تعبیری مقدار {{ 0 }} دارد.
        </li>
      </ul>

      <h4>جدول جمع‌بندی (تقارن دوگانه پرسش ۱ و پرسش ۲)</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>ماهیت تابع بولی</th>
            <th>حداقل تعداد بند در FNC</th>
            <th>حداقل تعداد جمله در FND</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>معتبر ({{ \equiv 1 }})</strong></td>
            <td><strong>۱ مجموع</strong>: {{ x + \overline{x} }}</td>
            <td><strong>۲ حاصل‌ضرب</strong>: {{ x + \overline{x} }}</td>
          </tr>
          <tr>
            <td><strong>ناسازگار ({{ \equiv 0 }})</strong></td>
            <td><strong>۲ مجموع</strong>: {{ x \cdot \overline{x} }}</td>
            <td><strong>۱ حاصل‌ضرب</strong>: {{ x \cdot \overline{x} }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 11 -->
<h2 id="td3_ex11">تمرین ۱۱ – سنتز کانونی FND/FNC و اثبات هم‌ارزی</h2>

<div class="q-card" id="td3_q11_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۱ – پرسش ۱</span>
    <span class="q-title">تابع بولی یای انحصاری (XOR): جدول درستی، FND و FNC</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>جدول درستی تابع بولی متناظر با «یای انحصاری» (XOR) را یادآوری کرده و از روی آن یک عبارت بولی در فرم FND و یک عبارت بولی در فرم FNC برای این تابع استنتاج کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۱</summary>
    <div class="box method">
      <h4>۱. جدول درستی {{ \text{xor}(x, y) }}</h4>
      <p>تابع {{ \text{xor}(x, y) }} برابر {{ 1 }} است اگر و تنها اگر دقیقاً یکی از دو آرگومان {{ x }} یا {{ y }} برابر {{ 1 }} باشد ({{ x \neq y }}):</p>
      <table class="tt-table">
        <thead>
          <tr>
            <th>سطر</th>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ \text{xor}(x, y) }}</th>
            <th>مین‌ترم (اگر {{ = 1 }})</th>
            <th>ماکس‌ترم (اگر {{ = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td><td>—</td><td>{{ x + y }}</td></tr>
          <tr><td>2</td><td>0</td><td>1</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot y }}</td><td>—</td></tr>
          <tr><td>3</td><td>1</td><td>0</td><td><strong>1</strong></td><td>{{ x \cdot \overline{y} }}</td><td>—</td></tr>
          <tr><td>4</td><td>1</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + \overline{y} }}</td></tr>
        </tbody>
      </table>

      <h4>۲. استنتاج FND کانونی (سطرهایی که {{ \text{xor}(x, y) = 1 }})</h4>
      <p>تابع در سطرهای ۲ ({{ x = 0, y = 1 \mapsto \overline{x} \cdot y }}) و ۳ ({{ x = 1, y = 0 \mapsto x \cdot \overline{y} }}) مقدار {{ 1 }} می‌گیرد. با جمع کردن این دو مین‌ترم داریم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FND}(\text{xor})(x, y) = \overline{x} \cdot y + x \cdot \overline{y} }}
      </p>

      <h4>۳. استنتاج FNC کانونی (سطرهایی که {{ \text{xor}(x, y) = 0 }})</h4>
      <p>تابع در سطرهای ۱ ({{ x = 0, y = 0 }}، ماکس‌ترم {{ x + y }}) و ۴ ({{ x = 1, y = 1 }}، ماکس‌ترم {{ \overline{x} + \overline{y} }}) مقدار {{ 0 }} می‌گیرد. با ضرب کردن این دو ماکس‌ترم داریم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FNC}(\text{xor})(x, y) = (x + y) \cdot (\overline{x} + \overline{y}) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q11_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۱ – پرسش ۲</span>
    <span class="q-title">تابع {{ f(x, y) }} که فقط در {{ (0, 0) }} مقدار {{ 1 }} دارد: FND و FNC</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>عبارت بولی تابع {{ f(x, y) }} را که اگر و تنها اگر {{ x }} و {{ y }} هر دو {{ 0 }} باشند مقدار {{ 1 }} می‌گیرد، بنویسید. فرم نرمال فصلی (FND) و فرم نرمال عطفی (FNC) آن را به دست آورید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۲</summary>
    <div class="box method">
      <h4>۱. جدول درستی {{ f(x, y) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>سطر</th>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ f(x, y) }}</th>
            <th>مین‌ترم ({{ f = 1 }})</th>
            <th>ماکس‌ترم ({{ f = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot \overline{y} }}</td><td>—</td></tr>
          <tr><td>2</td><td>0</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ x + \overline{y} }}</td></tr>
          <tr><td>3</td><td>1</td><td>0</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + y }}</td></tr>
          <tr><td>4</td><td>1</td><td>1</td><td><strong>0</strong></td><td>—</td><td>{{ \overline{x} + \overline{y} }}</td></tr>
        </tbody>
      </table>

      <h4>۲. فرم نرمال فصلی (FND)</h4>
      <p>تنها یک سطر وجود دارد که در آن {{ f(x, y) = 1 }} است: سطر {{ (0, 0) }} که مین‌ترم آن {{ \overline{x} \cdot \overline{y} }} می‌باشد.</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FND}(f)(x, y) = \overline{x} \cdot \overline{y} }}
      </p>
      <p><em>نکته:</em> عبارت {{ \overline{x} \cdot \overline{y} }} خود یک FNC نیز هست (حاصل‌ضرب دو بند واحد {{ (\overline{x}) \cdot (\overline{y}) }})، اما برای پاسخ به پرسش ۳، فرم FNC کانونی را از طریق ماکس‌ترم‌ها نیز می‌نویسیم!</p>

      <h4>۳. فرم نرمال عطفی کانونی (FNC از طریق ماکس‌ترم‌ها)</h4>
      <p>سه سطر وجود دارد که در آن‌ها {{ f(x, y) = 0 }} است: {{ (0, 1) }}، {{ (1, 0) }} و {{ (1, 1) }}. حاصل‌ضرب سه ماکس‌ترم متناظر، FNC کانونی را به دست می‌دهد:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ \text{FNC}(f)(x, y) = (\overline{x} + y) \cdot (x + \overline{y}) \cdot (\overline{x} + \overline{y}) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q11_3">
  <div class="q-header">
    <span class="q-num">تمرین ۱۱ – پرسش ۳</span>
    <span class="q-title">استنتاج هم‌ارزی منطقی {{ F |\equiv| G }} بدون محاسبه جدید</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>از پرسش قبل نتیجه بگیرید که فرمول‌های {{ F = \neg A \land \neg B }} و {{ G = (\neg A \lor B) \land ((A \lor \neg B) \land (\neg A \lor \neg B)) }} با یکدیگر هم‌ارزند.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۳</summary>
    <div class="box method">
      <p>دو فرمول گزاره‌ای {{ F }} و {{ G }} را به توابع بولی متناظرشان {{ f_F(x, y) }} و {{ f_G(x, y) }} ترجمه می‌کنیم (با قرار دادن {{ x = I(A) }} و {{ y = I(B) }}):</p>
      <ul>
        <li>برای فرمول {{ F = \neg A \land \neg B }}:
          <div style="margin:6px 0;">
            {{ f_F(x, y) = \overline{x} \cdot \overline{y} }}
          </div>
          که دقیقاً همان <strong>FND کانونی</strong> تابع {{ f(x, y) }} در پرسش ۲ است.
        </li>
        <li>برای فرمول {{ G = (\neg A \lor B) \land ((A \lor \neg B) \land (\neg A \lor \neg B)) }}:
          <div style="margin:6px 0;">
            {{ f_G(x, y) = (\overline{x} + y) \cdot (x + \overline{y}) \cdot (\overline{x} + \overline{y}) }}
          </div>
          که دقیقاً همان <strong>FNC کانونی</strong> (بر حسب ماکس‌ترم‌ها) برای همان تابع {{ f(x, y) }} در پرسش ۲ است!
        </li>
      </ul>
      <p>از آن‌جا که {{ f_F }} و {{ f_G }} هر دو نمایش‌دهنده تابع بولی یکسان {{ f(x, y) }} هستند (که مقدار {{ 1 }} می‌دهد اگر و تنها اگر {{ x = 0 }} و {{ y = 0 }})، به ازای هر تعبیر {{ I }} داریم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ [F]^I = f_F(I(A), I(B)) = f(I(A), I(B)) = f_G(I(A), I(B)) = [G]^I }}
      </p>
      <p>طبق تعریف هم‌ارزی معنایی، فرمول‌های {{ F }} و {{ G }} منطقاً هم‌ارز هستند: <strong>{{ F |\equiv| G }}</strong>.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 12 -->
<h2 id="td3_ex12">تمرین ۱۲ – استخراج مستقیم جدول درستی از روی FND یا FNC</h2>

<div class="q-card" id="td3_q12_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۲ – پرسش ۱</span>
    <span class="q-title">استنتاج جدول درستی {{ f(x, y, z) = x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>تابع بولی {{ f(x, y, z) = x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z }} را در نظر بگیرید. جدول درستی آن را استنتاج کنید.</p>
  </div>

  <details class="sol" open>
    <summary>روش استخراج مستقیم بدون محاسبه سطر به سطر</summary>
    <div class="box method">
      <h4>اصل خوانش مستقیم از روی FND</h4>
      <p>تابع {{ f }} در فرم <strong>FND</strong> (مجموع ۳ حاصل‌ضرب) داده شده است. یک مجموع به محض این‌که حداقل یکی از حاصل‌ضرب‌هایش برابر {{ 1 }} شود، مقدار {{ 1 }} می‌گیرد. به جای محاسبه عبارت در هر ۸ سطر، مستقیماً سه‌تایی‌های {{ (x, y, z) }} را که هر حاصل‌ضرب را برابر {{ 1 }} می‌کنند مشخص می‌کنیم:</p>
      <ul>
        <li><strong>جمله {{ T_1 = x \cdot y }}:</strong> برابر {{ 1 }} است اگر و تنها اگر {{ x = 1 }} و {{ y = 1 }} (به ازای هر {{ z \in \{0, 1\} }}).
          <br/>این جمله ۲ سه‌تایی را می‌دهد: <strong>{{ (1, 1, 0) }}</strong> و <strong>{{ (1, 1, 1) }}</strong>.
        </li>
        <li><strong>جمله {{ T_2 = \overline{y} \cdot \overline{z} }}:</strong> برابر {{ 1 }} است اگر و تنها اگر {{ y = 0 }} و {{ z = 0 }} (به ازای هر {{ x \in \{0, 1\} }}).
          <br/>این جمله ۲ سه‌تایی را می‌دهد: <strong>{{ (0, 0, 0) }}</strong> و <strong>{{ (1, 0, 0) }}</strong>.
        </li>
        <li><strong>جمله {{ T_3 = \overline{x} \cdot y \cdot z }}:</strong> برابر {{ 1 }} است اگر و تنها اگر {{ x = 0, y = 1 }} و {{ z = 1 }}.
          <br/>این جمله سه‌تایی <strong>{{ (0, 1, 1) }}</strong> را می‌دهد.
        </li>
      </ul>
      <p>در این ۵ سه‌تایی، {{ f(x, y, z) = 1 }} است؛ و در ۳ سه‌تایی باقی‌مانده یعنی {{ (0, 0, 1), (0, 1, 0), (1, 0, 1) }}، مقدار {{ f(x, y, z) = 0 }} است.</p>

      <h4>جدول درستی کامل {{ f(x, y, z) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ z }}</th>
            <th>{{ f(x, y, z) }}</th>
            <th>جمله توجیه‌کننده</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{y} \cdot \overline{z} = 1 }}</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td><td>هیچ جمله‌ای ۱ نیست</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td><strong>0</strong></td><td>هیچ جمله‌ای ۱ نیست</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td><strong>1</strong></td><td>{{ \overline{x} \cdot y \cdot z = 1 }}</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>1</strong></td><td>{{ \overline{y} \cdot \overline{z} = 1 }}</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td><strong>0</strong></td><td>هیچ جمله‌ای ۱ نیست</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td><td>{{ x \cdot y = 1 }}</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td><td>{{ x \cdot y = 1 }}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q12_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۲ – پرسش ۲</span>
    <span class="q-title">استنتاج جدول درستی {{ g(x, y, z) = (x + y) \cdot (\overline{y} + \overline{z}) \cdot (\overline{x} + y + z) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>تابع بولی {{ g(x, y, z) = (x + y) \cdot (\overline{y} + \overline{z}) \cdot (\overline{x} + y + z) }} را در نظر بگیرید. جدول درستی آن را استنتاج کنید.</p>
  </div>

  <details class="sol" open>
    <summary>روش استخراج مستقیم از طریق صفرهای بندها</summary>
    <div class="box method">
      <h4>اصل خوانش مستقیم از روی FNC</h4>
      <p>تابع {{ g }} در فرم <strong>FNC</strong> (حاصل‌ضرب ۳ بند) داده شده است. یک حاصل‌ضرب به محض این‌که حداقل یکی از مجموع‌هایش برابر {{ 0 }} شود، مقدار {{ 0 }} می‌گیرد. بنابراین مستقیماً سه‌تایی‌های {{ (x, y, z) }} را که <strong>هر بند را صفر می‌کنند</strong> مشخص می‌سازیم:</p>
      <ul>
        <li><strong>بند {{ C_1 = x + y }}:</strong> برابر {{ 0 }} است اگر و تنها اگر {{ x = 0 }} و {{ y = 0 }} (به ازای هر {{ z \in \{0, 1\} }}).
          <br/>این بند، {{ g }} را در ۲ سه‌تایی صفر می‌کند: <strong>{{ (0, 0, 0) }}</strong> و <strong>{{ (0, 0, 1) }}</strong>.
        </li>
        <li><strong>بند {{ C_2 = \overline{y} + \overline{z} }}:</strong> برابر {{ 0 }} است اگر و تنها اگر {{ \overline{y} = 0 }} و {{ \overline{z} = 0 }}، یعنی {{ y = 1 }} و {{ z = 1 }} (به ازای هر {{ x \in \{0, 1\} }}).
          <br/>این بند، {{ g }} را در ۲ سه‌تایی صفر می‌کند: <strong>{{ (0, 1, 1) }}</strong> و <strong>{{ (1, 1, 1) }}</strong>.
        </li>
        <li><strong>بند {{ C_3 = \overline{x} + y + z }}:</strong> برابر {{ 0 }} است اگر و تنها اگر {{ \overline{x} = 0, y = 0 }} و {{ z = 0 }}، یعنی {{ x = 1, y = 0, z = 0 }}.
          <br/>این بند، {{ g }} را در سه‌تایی <strong>{{ (1, 0, 0) }}</strong> صفر می‌کند.
        </li>
      </ul>
      <p>در این ۵ سه‌تایی، {{ g(x, y, z) = 0 }} است؛ و در ۳ سه‌تایی باقی‌مانده یعنی {{ (0, 1, 0), (1, 0, 1), (1, 1, 0) }} هیچ بندی صفر نمی‌شود، پس {{ g(x, y, z) = 1 }} است.</p>
      <p><em>مشاهده جالب:</em> با مقایسه با پرسش ۱ می‌بینیم که {{ g(x, y, z) = \overline{f(x, y, z)} }} است! در واقع طبق قانون دمورگان روی {{ f }} داریم {{ \overline{f} = \overline{x \cdot y + \overline{y} \cdot \overline{z} + \overline{x} \cdot y \cdot z} = (\overline{x} + \overline{y}) \cdot (y + z) \cdot (x + \overline{y} + \overline{z}) }}، و صفرهای {{ g }} دقیقاً همان یک‌های {{ f }} هستند!</p>

      <h4>جدول درستی کامل {{ g(x, y, z) }}</h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>{{ x }}</th>
            <th>{{ y }}</th>
            <th>{{ z }}</th>
            <th>{{ g(x, y, z) }}</th>
            <th>بند صفرشده (اگر {{ g = 0 }})</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td><strong>0</strong></td><td>{{ x + y = 0 }}</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td><td>{{ x + y = 0 }}</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td><strong>1</strong></td><td>تمام بندها برابر ۱ هستند</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td><strong>0</strong></td><td>{{ \overline{y} + \overline{z} = 0 }}</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td><td>{{ \overline{x} + y + z = 0 }}</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td><strong>1</strong></td><td>تمام بندها برابر ۱ هستند</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td><td>تمام بندها برابر ۱ هستند</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td><strong>0</strong></td><td>{{ \overline{y} + \overline{z} = 0 }}</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 13 -->
<h2 id="td3_ex13">تمرین ۱۳ – تبدیل جبری به FND و FNC بدون استفاده از جدول درستی</h2>

<div class="q-card" id="td3_q13_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۳ – پرسش ۱</span>
    <span class="q-title">تابع بولی متناظر با فرمول {{ F = (A \land (B \lor C)) \lor (\neg A \land \neg B) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>فرمول {{ F = (A \land (B \lor C)) \lor (\neg A \land \neg B) }} را در نظر بگیرید. برای پاسخ به این تمرین نباید از جدول درستی استفاده کنید.</p>
    <p><strong>پرسش ۱:</strong> عبارت تابع بولی متناظر با {{ F }} را بنویسید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۱</summary>
    <div class="box method">
      <p>به متغیرهای گزاره‌ای {{ A, B, C }} متغیرهای بولی {{ x, y, z \in \{0, 1\} }} را نسبت می‌دهیم (که در آن {{ x = I(A), y = I(B), z = I(C) }}). با ترجمه استقرایی مستقیم رابط‌های منطقی ({{ \land \mapsto \cdot }}، {{ \lor \mapsto + }}، {{ \neg \mapsto \overline{\phantom{x}} }})، تابع بولی {{ f_F(x, y, z) }} متناظر با {{ F }} عبارت است از:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">
        {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }}
      </p>
      <p><em>نکته:</em> این عبارت نه در فرم FND است (به دلیل عامل {{ x \cdot (y + z) }}) و نه در فرم FNC (زیرا عملگر اصلی جمع {{ + }} است).</p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q13_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۳ – پرسش ۲</span>
    <span class="q-title">تبدیل به فرم نرمال فصلی (FND) با محاسبه جبری</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p><strong>پرسش ۲:</strong> این تابع را به فرم نرمال فصلی (FND) ببرید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۲</summary>
    <div class="box method">
      <p>برای رسیدن به FND (مجموعی از حاصل‌ضرب‌های لیترال‌ها)، کافی است ضرب {{ \cdot }} را بر روی جمع {{ + }} در زیرجمله اول یعنی {{ x \cdot (y + z) }} توزیع کنیم:</p>
      <div style="line-height:2.2em; font-size:1.05em;">
        {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }}<br/>
        {{ = x \cdot y + x \cdot z + \overline{x} \cdot \overline{y} }} \quad <em>(توزیع‌پذیری {{ \cdot }} بر روی {{ + }})</em>
      </div>
      <p>عبارت به دست آمده مجموع ۳ حاصل‌ضرب از لیترال‌هاست ({{ x \cdot y }}، {{ x \cdot z }} و {{ \overline{x} \cdot \overline{y} }}): بنابراین در <strong>فرم نرمال فصلی (FND)</strong> قرار دارد.</p>
      <p>با بازگشت به نمادگذاری گزاره‌ای، فرمول در فرم FND هم‌ارز با {{ F }} عبارت است از:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ F_{\text{FND}} = (A \land B) \lor (A \land C) \lor (\neg A \land \neg B) }}
      </p>
    </div>
  </details>
</div>

<div class="q-card" id="td3_q13_3">
  <div class="q-header">
    <span class="q-num">تمرین ۱۳ – پرسش ۳</span>
    <span class="q-title">تبدیل به فرم نرمال عطفی (FNC) با توزیع‌پذیری {{ + }} بر روی {{ \cdot }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p><strong>پرسش ۳:</strong> این تابع را به فرم نرمال عطفی (FNC) ببرید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی پرسش ۳</summary>
    <div class="box method">
      <p>از عبارت اولیه {{ f_F(x, y, z) = x \cdot (y + z) + \overline{x} \cdot \overline{y} }} شروع می‌کنیم (که نسبت به FND فاکتورگیری‌شده‌تر است و از گسترش‌های غیرضروری جلوگیری می‌کند!) و قانون توزیع‌پذیری جمع {{ + }} بر روی ضرب {{ \cdot }} را به کار می‌بریم:</p>
      <div style="line-height:2.3em; font-size:1.05em;">
        {{ f_F(x, y, z) = \underbrace{x \cdot (y + z)}_{U} + (\overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot (y + z) + \overline{x}) \cdot (x \cdot (y + z) + \overline{y}) }} \quad <em>(توزیع‌پذیری {{ + }} بر روی {{ \cdot }}: {{ U + \overline{x} \cdot \overline{y} = (U + \overline{x}) \cdot (U + \overline{y}) }})</em><br/>
        {{ = (\overline{x} + x \cdot (y + z)) \cdot (\overline{y} + x \cdot (y + z)) }} \quad <em>(جابه‌جایی {{ + }})</em><br/>
        {{ = (\overline{x} + x) \cdot (\overline{x} + y + z) \cdot (\overline{y} + x) \cdot (\overline{y} + y + z) }} \quad <em>(توزیع‌پذیری {{ + }} بر روی {{ \cdot }} در هر عامل)</em><br/>
        {{ = 1 \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot (1 + z) }} \quad <em>(متمم: {{ \overline{x} + x = 1 }} و {{ \overline{y} + y = 1 }})</em><br/>
        {{ = 1 \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot 1 }} \quad <em>(عنصر جاذب: {{ 1 + z = 1 }})</em><br/>
        {{ = (\overline{x} + y + z) \cdot (x + \overline{y}) }} \quad <em>(عنصر خنثی {{ 1 }} برای ضرب {{ \cdot }})</em>
      </div>
      <p><em>نکته:</em> حتی اگر بندهای توتولوژی {{ (x + \overline{x}) }} و {{ (y + \overline{y} + z) }} را ساده نکنیم، حاصل‌ضرب ۴ بند {{ (x + \overline{x}) \cdot (\overline{x} + y + z) \cdot (x + \overline{y}) \cdot (y + \overline{y} + z) }} از نظر نحوی در فرم FNC قرار دارد! فرم ساده‌شده کمینه عبارت است از:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">
        {{ \text{FNC}(f_F)(x, y, z) = (\overline{x} + y + z) \cdot (x + \overline{y}) }}
      </p>
      <p>با بازگشت به نمادگذاری گزاره‌ای، فرمول در فرم FNC هم‌ارز با {{ F }} عبارت است از:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">
        {{ F_{\text{FNC}} = (\neg A \lor B \lor C) \land (A \lor \neg B) }}
      </p>
    </div>
  </details>
</div>
"""

with open(os.path.join(W03, 'td.fr.html'), 'w', encoding='utf-8') as f:
    f.write(fr.strip() + '\n')

with open(os.path.join(W03, 'td.fa.html'), 'w', encoding='utf-8') as f:
    f.write(fa.strip() + '\n')

print("Generated td.fr.html and td.fa.html in w03 successfully.")
