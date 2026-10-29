#!/usr/bin/env python3
"""Authoring generator for TD Week 1 (Thème 1).
Full subquestion-by-subquestion solutions for:
- Exercice 1: Q1.1 (F1), Q1.2 (F2), Q2.1 (F3), Q2.2 (F4)
- Exercice 2: Q1 & Q2 across all 6 statements
- Exercice 3: Q1 (F truth table), Q2 (Anna & Julie crime riddle), Q3 (Anissa, Xavier, Jennifer revision riddle)
"""
import os

W01 = '/home/mnasimi/sorbonne/Logic_Academy/content/w01'
os.makedirs(W01, exist_ok=True)

# Build both FR and FA with identical structure, IDs, and widgets
fr = """
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TD Thème 1 : Syntaxe, Tables de Vérité et Énigmes Logiques</h1>
  <p class="lead">Corrections intégrales et ultra-détaillées des 3 exercices officiels du polycopié de TD (2026-2027), avec décomposition sous-question par sous-question, arbres de syntaxe, tables de vérité complètes et justifications universitaires.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du TD</h3>
  <ul>
    <li><a href="#ex1">Exercice 1 – Arbre de syntaxe abstraite et notation préfixe</a></li>
    <li><a href="#ex2">Exercice 2 – Implication et formalisation du langage naturel</a></li>
    <li><a href="#ex3">Exercice 3 – Tables de vérité et énigmes logiques</a></li>
  </ul>
</div>

<h2 id="ex1">Exercice 1 – Arbre de syntaxe abstraite et notation préfixe</h2>

<div class="box info">
  <h4>Contexte et compétences visées</h4>
  <p>Cet exercice évalue la maîtrise de la structure arborescente des formules (AST), la capacité à identifier le connecteur principal, la conversion en notation préfixe (notation polonaise), et l'application stricte des conventions de priorité de Sorbonne Université (priorité décroissante et associativité à droite).</p>
</div>

<!-- Question 1.1 -->
<div class="q-card" id="q1_1">
  <div class="q-header">
    <span class="q-num">Question 1.1</span>
    <span class="q-title">AST et notation préfixe de {{ F_1 = \neg(p \land (q \Rightarrow ((q \lor r) \land q))) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Pour la formule suivante où {{ p, q }} et {{ r }} sont des symboles de propositions :</p>
    <ul>
      <li>dessiner son arbre de syntaxe abstraite</li>
      <li>écrire la formule en notation préfixe</li>
    </ul>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_1 = \neg(p \land (q \Rightarrow ((q \lor r) \land q))) }}</p>
  </div>

  <div class="box tip">
    <h4>Stratégie et décomposition</h4>
    <p>La formule est entièrement parenthésée. Pour trouver la racine, on suit la règle d'induction :</p>
    <ol>
      <li>Le symbole le plus externe est {{ \neg }}. Il porte sur toute la sous-formule parenthésée. La racine de l'AST est donc {{ \neg }}.</li>
      <li>Son unique fils est la conjonction {{ \land }} entre {{ p }} et {{ (q \Rightarrow ((q \lor r) \land q)) }}.</li>
      <li>Le fils droit de {{ \land }} est une implication {{ \Rightarrow }} ayant pour fils gauche {{ q }} et pour fils droit une conjonction {{ \land }}.</li>
      <li>Cette seconde conjonction a pour fils gauche la disjonction {{ (q \lor r) }} et pour fils droit la feuille {{ q }}.</li>
    </ol>
  </div>

  <div class="w-ast" data-formula="~(p & (q => ((q | r) & q)))"></div>

  <details class="sol" open>
    <summary>Solution détaillée et notation préfixe</summary>
    <div class="box method">
      <h4>Parcours préfixe (Racine &rarr; Fils Gauche &rarr; Fils Droit)</h4>
      <p>Appliquons récursivement l'algorithme de parcours préfixe :</p>
      <ul>
        <li>Niveau 1 : <code>&not;</code> suivi du parcours de son sous-arbre.</li>
        <li>Niveau 2 : <code>&and;</code> suivi de la feuille <code>p</code> et du sous-arbre droit.</li>
        <li>Niveau 3 : <code>&rArr;</code> suivi de la feuille <code>q</code> et du sous-arbre droit.</li>
        <li>Niveau 4 : <code>&and;</code> suivi du sous-arbre gauche et de la feuille <code>q</code>.</li>
        <li>Niveau 5 : <code>&or;</code> suivi des feuilles <code>q</code> et <code>r</code>.</li>
      </ul>
      <p>En rassemblant l'ensemble sans aucune parenthèse, la notation préfixe exacte est :</p>
      <pre><code>¬ ∧ p ⇒ q ∧ ∨ q r q</code></pre>
      <p><strong>Vérification :</strong> Le nombre de symboles de connecteurs binaires (4) + connecteur unaire (1) = 5 connecteurs. Le nombre de feuilles est 5 (p, q, q, r, q). La formule préfixe possède bien 10 symboles.</p>
    </div>
  </details>
</div>

<!-- Question 1.2 -->
<div class="q-card" id="q1_2">
  <div class="q-header">
    <span class="q-num">Question 1.2</span>
    <span class="q-title">AST et notation préfixe de {{ F_2 = \neg p \land q \Rightarrow q \lor r \land q }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Pour la formule {{ F_2 = \neg p \land q \Rightarrow q \lor r \land q }} :</p>
    <ul>
      <li>dessiner son arbre de syntaxe abstraite</li>
      <li>écrire la formule en notation préfixe</li>
    </ul>
  </div>

  <div class="box warn">
    <h4>Rétablissement impératif des parenthèses d'après les priorités Sorbonne</h4>
    <p>La formule {{ F_2 }} comporte zéro parenthèse. Appliquons rigoureusement la règle {{ \neg > \land > \lor > \Rightarrow }} :</p>
    <ol>
      <li>{{ \neg }} est prioritaire : {{ (\neg p) }}.</li>
      <li>{{ \land }} est prioritaire sur {{ \lor }} et {{ \Rightarrow }} :
        <ul>
          <li>À gauche : {{ ((\neg p) \land q) }}.</li>
          <li>À droite : {{ (r \land q) }}.</li>
        </ul>
      </li>
      <li>{{ \lor }} est prioritaire sur {{ \Rightarrow }} : la partie droite devient {{ (q \lor (r \land q)) }}.</li>
      <li>Le connecteur de priorité la plus faible est l'implication centrale {{ \Rightarrow }}. C'est donc le <strong>connecteur principal (la racine)</strong> !</li>
    </ol>
    <p>Formule totalement parenthésée : {{ ((\neg p) \land q) \Rightarrow (q \lor (r \land q)) }}.</p>
  </div>

  <div class="w-ast" data-formula="(~p & q) => (q | (r & q))"></div>

  <details class="sol" open>
    <summary>Solution détaillée et notation préfixe</summary>
    <div class="box method">
      <h4>Notation préfixe de {{ F_2 }}</h4>
      <p>La racine est {{ \Rightarrow }} :</p>
      <ul>
        <li>Sous-arbre gauche : <code>&and; &not; p q</code></li>
        <li>Sous-arbre droit : <code>&or; q &and; r q</code></li>
      </ul>
      <p>Ce qui donne en notation préfixe :</p>
      <pre><code>⇒ ∧ ¬ p q ∨ q ∧ r q</code></pre>
    </div>
  </details>
</div>

<!-- Question 2.1 -->
<div class="q-card" id="q2_1">
  <div class="q-header">
    <span class="q-num">Question 2.1</span>
    <span class="q-title">Parenthésage de {{ F_3 = p \land q \land r \land s }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Parenthéser la formule suivante en respectant la priorité des opérateurs :</p>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_3 = p \land q \land r \land s }}</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée et justification Sorbonne</summary>
    <div class="box method">
      <h4>Règle d'associativité à droite (Sorbonne Cours 1, Slide 11)</h4>
      <p>Tous les opérateurs sont identiques ({{ \land }}), ils ont donc la même priorité. La convention du cours stipule impérativement :</p>
      <p><em>« Priorité égale : sous-formule de droite prioritaire. »</em></p>
      <p>Déroulement des regroupements pas à pas depuis la droite :</p>
      <ol>
        <li>Regroupement des deux atomes les plus à droite : {{ (r \land s) }}.</li>
        <li>Regroupement avec l'atome précédent : {{ (q \land (r \land s)) }}.</li>
        <li>Regroupement final avec {{ p }} : {{ (p \land (q \land (r \land s))) }}.</li>
      </ol>
      <p><strong>Réponse finale d'examen :</strong></p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">{{ (p \land (q \land (r \land s))) }}</p>
      <p><strong>Erreur fatale à éviter :</strong> Écrire <code>(((p &and; q) &and; r) &and; s)</code>. Même si la conjonction est sémantiquement associative en algèbre booléenne, <em>syntaxiquement</em> l'arbre obtenu serait faux selon la convention officielle du cours de la Sorbonne !</p>
    </div>
  </details>
</div>

<!-- Question 2.2 -->
<div class="q-card" id="q2_2">
  <div class="q-header">
    <span class="q-num">Question 2.2</span>
    <span class="q-title">Parenthésage de {{ F_4 = p \Rightarrow q \land \neg r \Rightarrow p \lor q }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Parenthéser la formule suivante en respectant la priorité des opérateurs :</p>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_4 = p \Rightarrow q \land \neg r \Rightarrow p \lor q }}</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas-à-pas</summary>
    <div class="box method">
      <h4>Application rigoureuse de la hiérarchie {{ \neg > \land > \lor > \Rightarrow }}</h4>
      <ol>
        <li><strong>Niveau 1 ({{ \neg }}) :</strong> Négation la plus forte sur {{ r }} : on obtient <code>(&not; r)</code>.</li>
        <li><strong>Niveau 2 ({{ \land }}) :</strong> Conjonction <code>q &and; (&not; r)</code> : on obtient <code>(q &and; (&not; r))</code>.</li>
        <li><strong>Niveau 3 ({{ \lor }}) :</strong> Disjonction <code>p &or; q</code> : on obtient <code>(p &or; q)</code>.</li>
        <li>Il reste deux implications : <code>p &rArr; (q &and; (&not; r)) &rArr; (p &or; q)</code>.</li>
        <li><strong>Niveau 4 (associativité à droite de {{ \Rightarrow }}) :</strong> En cas d'implications multiples en chaîne, la sous-formule de <em>droite</em> est prioritaire !
          <br/>On regroupe donc d'abord : <code>((q &and; (&not; r)) &rArr; (p &or; q))</code>.
          <br/>Puis l'implication globale depuis <code>p</code> :
        </li>
      </ol>
      <p><strong>Réponse finale d'examen :</strong></p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">{{ (p \Rightarrow ((q \land (\neg r)) \Rightarrow (p \lor q))) }}</p>
    </div>
  </details>
</div>

<h2 id="ex2">Exercice 2 – Implication et formalisation du langage naturel</h2>

<div class="box info">
  <h4>Contexte de l'exercice</h4>
  <p>Soient les propositions atomiques :</p>
  <ul>
    <li>{{ p_1 }} : « il fait beau »</li>
    <li>{{ p_2 }} : « je me promène »</li>
  </ul>
  <p>On étudie la situation concrète où <strong>il ne fait pas beau et je me promène</strong>, ce qui correspond à l'interprétation formelle :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ I(p_1) = 0 \quad \text{et} \quad I(p_2) = 1 }}</p>
</div>

<!-- Question 2.1 & 2.2 combinées pour clarté -->
<div class="q-card" id="q_imp">
  <div class="q-header">
    <span class="q-num">Questions 1 &amp; 2</span>
    <span class="q-title">Traduction formelle et évaluation des 6 énoncés</span>
  </div>

  <details class="sol" open>
    <summary>Analyse détaillée des 6 énoncés sous {{ I(p_1)=0, I(p_2)=1 }}</summary>
    <div class="box method">
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>N°</th>
            <th>Énoncé en français</th>
            <th>Formule logique</th>
            <th>Calcul {{ [F]^I }} sous {{ I(p_1)=0, I(p_2)=1 }}</th>
            <th>Statut</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1</strong></td>
            <td>« S'il fait beau, je me promène »</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">VÉRIFIÉ</span></td>
          </tr>
          <tr>
            <td><strong>2</strong></td>
            <td>« Pour que je me promène, il faut qu'il fasse beau »</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">NON VÉRIFIÉ</span></td>
          </tr>
          <tr>
            <td><strong>3</strong></td>
            <td>« Je ne me promène que s'il fait beau »</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">NON VÉRIFIÉ</span></td>
          </tr>
          <tr>
            <td><strong>4</strong></td>
            <td>« Je me promène dès qu'il fait beau »</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">VÉRIFIÉ</span></td>
          </tr>
          <tr>
            <td><strong>5</strong></td>
            <td>« Je me promène seulement s'il fait beau »</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">NON VÉRIFIÉ</span></td>
          </tr>
          <tr>
            <td><strong>6</strong></td>
            <td>« Pour que je me promène, il suffit qu'il fasse beau »</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">VÉRIFIÉ</span></td>
          </tr>
        </tbody>
      </table>

      <h4 style="margin-top:15px;">Synthèse théorique indispensable</h4>
      <ul>
        <li><strong>Condition suffisante (« il suffit », « si », « dès que ») :</strong> Le beau temps suffit à provoquer la promenade &rarr; {{ p_1 \Rightarrow p_2 }}. Comme {{ p_1 }} est faux ({{ 0 }}), l'implication est automatiquement <em>vraie</em> par le principe d'explosion ! Donc 1, 4 et 6 sont vérifiés.</li>
        <li><strong>Condition nécessaire (« il faut », « seulement si », « ne ... que si ») :</strong> Le beau temps est obligatoire pour se promener. Si je me promène, c'est qu'il fait beau &rarr; {{ p_2 \Rightarrow p_1 }}. Or je me promène ({{ p_2=1 }}) sans beau temps ({{ p_1=0 }}). L'implication {{ 1 \Rightarrow 0 }} est <em>fausse</em>. Donc 2, 3 et 5 sont non vérifiés.</li>
      </ul>
    </div>
  </details>
</div>

<h2 id="ex3">Exercice 3 – Tables de vérité et énigmes logiques</h2>

<!-- Question 3.1 -->
<div class="q-card" id="q3_1">
  <div class="q-header">
    <span class="q-num">Question 1</span>
    <span class="q-title">Table de vérité de {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit la formule {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }} où {{ p }} et {{ q }} sont des propositions. Calculer la table de vérité de {{ F }}.</p>
  </div>

  <div class="w-tt" data-formula="(p & q) & ((q => p) | ~(p | q))"></div>

  <details class="sol" open>
    <summary>Calcul détaillé ligne par ligne</summary>
    <div class="box method">
      <p>La formule possède {{ 2 }} variables, soit {{ 2^2 = 4 }} interprétations possibles :</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ p }}</th>
            <th>{{ q }}</th>
            <th>{{ p \land q }}</th>
            <th>{{ q \Rightarrow p }}</th>
            <th>{{ p \lor q }}</th>
            <th>{{ \neg(p \lor q) }}</th>
            <th>{{ (q \Rightarrow p) \lor \neg(p \lor q) }}</th>
            <th>{{ F }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>Conclusion sémantique :</strong> {{ F }} est vraie sous l'unique interprétation {{ I(p)=1, I(q)=1 }}. Elle est donc <strong>satisfiable</strong>, mais <strong>non valide</strong>.</p>
    </div>
  </details>
</div>

<!-- Question 3.2 -->
<div class="q-card" id="q3_2">
  <div class="q-header">
    <span class="q-num">Question 2</span>
    <span class="q-title">Énigme judiciaire : Anna et Julie</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Anna et Julie sont interrogées au sujet d'un crime et déclarent :</p>
    <ul>
      <li><strong>Anna :</strong> « Julie est coupable. »</li>
      <li><strong>Julie :</strong> « Si je suis coupable, alors Anna l'est aussi. »</li>
    </ul>
    <p>Propositions : {{ A }} : « Anna est coupable », {{ J }} : « Julie est coupable ».</p>
    <ol>
      <li>Donner la formule {{ F_1 }} (affirmation d'Anna) et {{ F_2 }} (affirmation de Julie).</li>
      <li>Soit {{ F_3 = F_1 \lor F_2 }} : (a) Calculer sa table de vérité, (b) Que peut-on en conclure ?</li>
      <li>Soit {{ F_4 = F_1 \land F_2 }} : (a) Calculer sa table de vérité, (b) Que peut-on en conclure ?</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Correction pas à pas et conclusions</summary>
    <div class="box method">
      <h4>1. Formalisation</h4>
      <ul>
        <li>Déclaration d'Anna : {{ F_1 = J }}</li>
        <li>Déclaration de Julie : {{ F_2 = J \Rightarrow A }}</li>
      </ul>

      <h4>2. Étude de {{ F_3 = F_1 \lor F_2 = J \lor (J \Rightarrow A) }}</h4>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ J }}</th>
            <th>{{ F_1 = J }}</th>
            <th>{{ F_2 = J \Rightarrow A }}</th>
            <th>{{ F_3 = F_1 \lor F_2 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>Conclusion pour {{ F_3 }} :</strong> La formule {{ F_3 }} est une <strong>tautologie (formule valide)</strong>. Elle vaut 1 dans toutes les interprétations. On peut donc en conclure avec certitude qu'<strong>au moins l'une des deux suspectes dit toujours la vérité</strong>, quelle que soit la culpabilité réelle d'Anna ou de Julie !</p>

      <h4>3. Étude de {{ F_4 = F_1 \land F_2 = J \land (J \Rightarrow A) }}</h4>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ J }}</th>
            <th>{{ F_1 = J }}</th>
            <th>{{ F_2 = J \Rightarrow A }}</th>
            <th>{{ F_4 = F_1 \land F_2 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>0</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>Conclusion pour {{ F_4 }} :</strong> {{ F_4 }} n'admet qu'un seul et unique modèle : {{ A=1, J=1 }}. Par conséquent, <strong>si toutes les deux disent la vérité, alors Anna et Julie sont toutes les deux coupables</strong>.</p>
    </div>
  </details>
</div>

<!-- Question 3.3 -->
<div class="q-card" id="q3_3">
  <div class="q-header">
    <span class="q-num">Question 3</span>
    <span class="q-title">Énigme de l'examen : Anissa, Xavier et Jennifer</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Anissa, Xavier et Jennifer ont un examen de logique à passer. On suppose que :</p>
    <ul>
      <li>{{ H_1 }} : L'un des trois au moins révisera pour l'examen.</li>
      <li>{{ H_2 }} : Si Anissa ne révise pas, alors Xavier non plus.</li>
      <li>{{ H_3 }} : Si Anissa révise, alors Jennifer aussi.</li>
    </ul>
    <p>Propositions : {{ A }} : « Anissa révise », {{ X }} : « Xavier révise », {{ J }} : « Jennifer révise ».</p>
    <ol>
      <li>Formaliser ces trois hypothèses.</li>
      <li>Peut-on dire qui révisera ? qui ne révisera pas ?</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Résolution sémantique rigoureuse</summary>
    <div class="box method">
      <h4>1. Formalisation mathématique</h4>
      <ul>
        <li>{{ H_1 : A \lor X \lor J }} (au moins l'un des trois)</li>
        <li>{{ H_2 : \neg A \Rightarrow \neg X }} (ce qui équivaut par contraposition à {{ X \Rightarrow A }})</li>
        <li>{{ H_3 : A \Rightarrow J }}</li>
      </ul>

      <h4>2. Recherche des modèles de la théorie {{ \mathcal{T} = \{H_1, H_2, H_3\} }}</h4>
      <p>Dressons la table de vérité des 3 hypothèses sur les {{ 2^3 = 8 }} interprétations possibles :</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ X }}</th>
            <th>{{ J }}</th>
            <th>{{ H_1 }}</th>
            <th>{{ H_2 : \neg A \Rightarrow \neg X }}</th>
            <th>{{ H_3 : A \Rightarrow J }}</th>
            <th>{{ H_1 \land H_2 \land H_3 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (Modèle I1)</strong></td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (Modèle I2)</strong></td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (Modèle I3)</strong></td></tr>
        </tbody>
      </table>

      <h4>3. Déductions logiques certaines</h4>
      <p>Il existe exactement 3 interprétations qui satisfont simultanément les trois hypothèses :</p>
      <ul>
        <li>{{ I_1 = \{A=0, X=0, J=1\} }}</li>
        <li>{{ I_2 = \{A=1, X=0, J=1\} }}</li>
        <li>{{ I_3 = \{A=1, X=1, J=1\} }}</li>
      </ul>
      <p><strong>Conclusion mathématique d'examen :</strong></p>
      <ul>
        <li>Dans les trois modèles, on a sans exception {{ J = 1 }}. <strong>On peut donc affirmer avec une certitude absolue que Jennifer révisera</strong> ({{ \mathcal{T} \models J }}).</li>
        <li>Pour Anissa : elle révise dans {{ I_2 }} et {{ I_3 }} ({{ A=1 }}), mais ne révise pas dans {{ I_1 }} ({{ A=0 }}). <strong>On ne peut donc pas déterminer si Anissa révisera ou non.</strong></li>
        <li>Pour Xavier : il révise dans {{ I_3 }} ({{ X=1 }}), mais ne révise pas dans {{ I_1 }} et {{ I_2 }} ({{ X=0 }}). <strong>On ne peut donc pas déterminer si Xavier révisera ou non.</strong></li>
        <li>On peut seulement ajouter : si Xavier révise, alors nécessairement Anissa révise aussi (modèle {{ I_3 }}).</li>
      </ul>
    </div>
  </details>
</div>
"""

fa = """
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>تمرین‌های عملی فصل ۱: نحو، جدول‌های درستی و معماهای منطقی</h1>
  <p class="lead">حل کامل، دقیق و خط‌به‌خط هر ۳ تمرین رسمی جزوه TD دانشگاه سوربن (سال تحصیلی ۲۰۲۶-۲۰۲۷)، همراه با تفکیک تمام زیرمسئله‌ها، رسم درخت‌های نحو انتزاعی، جدول‌های درستی کامل و تحلیل استدلال‌ها.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب تمرین‌ها</h3>
  <ul>
    <li><a href="#ex1">تمرین ۱ – درخت نحو انتزاعی و نمادگذاری پیشوندی</a></li>
    <li><a href="#ex2">تمرین ۲ – استلزام و مدل‌سازی صوری زبان طبیعی</a></li>
    <li><a href="#ex3">تمرین ۳ – جدول‌های درستی و معماهای منطقی</a></li>
  </ul>
</div>

<h2 id="ex1">Exercice 1 – Arbre de syntaxe abstraite et notation préfixe</h2>

<div class="box info">
  <h4>زمینه مسئله و مهارت‌های مورد سنجش</h4>
  <p>این تمرین تسلط بر ساختار درختی فرمول‌ها (AST)، تشخیص عملگر اصلی در فرمول‌های پیچیده، تبدیل به نمادگذاری پیشوندی (لهستانی لوکاسیویچ) و اجرای دقیق قواعد اولویت دانشگاه سوربن (کاهش اولویت و شرکت‌پذیری از راست) را مورد ارزیابی قرار می‌دهد.</p>
</div>

<!-- Question 1.1 -->
<div class="q-card" id="q1_1">
  <div class="q-header">
    <span class="q-num">زیرمسئله ۱.۱</span>
    <span class="q-title">درخت نحو انتزاعی و نمادگذاری پیشوندی {{ F_1 = \neg(p \land (q \Rightarrow ((q \lor r) \land q))) }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>برای فرمول زیر که در آن {{ p, q }} و {{ r }} نمادهای گزاره‌ای هستند:</p>
    <ul>
      <li>درخت نحو انتزاعی (AST) آن را رسم کنید.</li>
      <li>فرمول را در نمادگذاری پیشوندی بنویسید.</li>
    </ul>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_1 = \neg(p \land (q \Rightarrow ((q \lor r) \land q))) }}</p>
  </div>

  <div class="box tip">
    <h4>راهبرد و گام‌های تجزیه</h4>
    <p>فرمول کاملاً پرانتزگذاری شده است. برای یافتن ریشه، قواعد استقرایی را از بیرون به درون دنبال می‌کنیم:</p>
    <ol>
      <li>بیرونی‌ترین عملگر نقیض {{ \neg }} است که بر کل پرانتز اثر می‌کند؛ بنابراین ریشه درخت {{ \neg }} است.</li>
      <li>تنها فرزند آن عطف {{ \land }} میان اتم {{ p }} و زیرفرمول {{ (q \Rightarrow ((q \lor r) \land q)) }} است.</li>
      <li>فرزند راست {{ \land }}، عملگر شرطی {{ \Rightarrow }} با فرزند چپ {{ q }} و فرزند راست عطف دوتایی {{ \land }} است.</li>
      <li>این عطف اخیر دارای فرزند چپ فصل {{ (q \lor r) }} و فرزند راست برگ اتمی {{ q }} است.</li>
    </ol>
  </div>

  <div class="w-ast" data-formula="~(p & (q => ((q | r) & q)))"></div>

  <details class="sol" open>
    <summary>پاسخ تشریحی و نمادگذاری پیشوندی</summary>
    <div class="box method">
      <h4>پیمایش پیشوندی (ریشه &larr; زیردرخت چپ &larr; زیردرخت راست)</h4>
      <p>الگوریتم پیمایش پیشوندی را به روش بازگشتی پیاده می‌کنیم:</p>
      <ul>
        <li>سطح ۱: عملگر <code>&not;</code> به همراه پیمایش زیردرخت آن.</li>
        <li>سطح ۲: عملگر <code>&and;</code> به همراه برگ <code>p</code> و سپس زیردرخت راست.</li>
        <li>سطح ۳: عملگر <code>&rArr;</code> به همراه برگ <code>q</code> و زیردرخت راست.</li>
        <li>سطح ۴: عملگر <code>&and;</code> به همراه زیردرخت چپ و برگ <code>q</code>.</li>
        <li>سطح ۵: عملگر <code>&or;</code> به همراه برگ‌های <code>q</code> و <code>r</code>.</li>
      </ul>
      <p>با کنار هم قرار دادن تمام نمادها بدون نیاز به حتی یک پرانتز، فرمول پیشوندی نهایی برابر است با:</p>
      <pre><code>¬ ∧ p ⇒ q ∧ ∨ q r q</code></pre>
      <p><strong>بررسی درستی:</strong> ۴ عملگر دوتایی + ۱ عملگر یکتایی = ۵ عملگر. تعداد برگ‌ها ۵ تاست (p, q, q, r, q). رشته پیشوندی حاصل دقیقاً دارای ۱۰ نماد معتبر است.</p>
    </div>
  </details>
</div>

<!-- Question 1.2 -->
<div class="q-card" id="q1_2">
  <div class="q-header">
    <span class="q-num">زیرمسئله ۱.۲</span>
    <span class="q-title">درخت نحو انتزاعی و نمادگذاری پیشوندی {{ F_2 = \neg p \land q \Rightarrow q \lor r \land q }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>برای فرمول {{ F_2 = \neg p \land q \Rightarrow q \lor r \land q }} :</p>
    <ul>
      <li>درخت نحو انتزاعی آن را رسم کنید.</li>
      <li>فرمول را در نمادگذاری پیشوندی بنویسید.</li>
    </ul>
  </div>

  <div class="box warn">
    <h4>بازسازی پرانتزهای ناپیدا طبق قواعد رسمی سوربن</h4>
    <p>فرمول {{ F_2 }} فاقد پرانتز است. قاعده اولویت {{ \neg > \land > \lor > \Rightarrow }} را اعمال می‌کنیم:</p>
    <ol>
      <li>نقیض {{ \neg }} بالاترین اولویت را دارد: {{ (\neg p) }}.</li>
      <li>عطف {{ \land }} بر فصل {{ \lor }} و استلزام {{ \Rightarrow }} اولویت دارد:
        <ul>
          <li>در سمت چپ: {{ ((\neg p) \land q) }}.</li>
          <li>در سمت راست: {{ (r \land q) }}.</li>
        </ul>
      </li>
      <li>فصل {{ \lor }} بر استلزام {{ \Rightarrow }} اولویت دارد: سمت راست تبدیل می‌شود به {{ (q \lor (r \land q)) }}.</li>
      <li>ضعیف‌ترین عملگر، استلزام میانی {{ \Rightarrow }} است که بنابراین <strong>عملگر اصلی و ریشه نهایی درخت</strong> خواهد بود!</li>
    </ol>
    <p>شکل کاملاً پرانتزگذاری‌شده: {{ ((\neg p) \land q) \Rightarrow (q \lor (r \land q)) }}.</p>
  </div>

  <div class="w-ast" data-formula="(~p & q) => (q | (r & q))"></div>

  <details class="sol" open>
    <summary>پاسخ تشریحی و نمادگذاری پیشوندی</summary>
    <div class="box method">
      <h4>نمادگذاری پیشوندی فرمول {{ F_2 }}</h4>
      <p>ریشه درخت {{ \Rightarrow }} است:</p>
      <ul>
        <li>زیردرخت چپ: <code>&and; &not; p q</code></li>
        <li>زیردرخت راست: <code>&or; q &and; r q</code></li>
      </ul>
      <p>نتیجه نهایی در نمادگذاری پیشوندی:</p>
      <pre><code>⇒ ∧ ¬ p q ∨ q ∧ r q</code></pre>
    </div>
  </details>
</div>

<!-- Question 2.1 -->
<div class="q-card" id="q2_1">
  <div class="q-header">
    <span class="q-num">زیرمسئله ۲.۱</span>
    <span class="q-title">پرانتزگذاری دقیق فرمول {{ F_3 = p \land q \land r \land s }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرمول زیر را با رعایت دقیق اولویت عملگرها پرانتزگذاری کنید:</p>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_3 = p \land q \land r \land s }}</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی و توجیه طبق ضوابط دانشگاه سوربن</summary>
    <div class="box method">
      <h4>قاعده شرکت‌پذیری از راست (اسلاید ۱۱ درس ۱)</h4>
      <p>همه عملگرها یکسان ({{ \land }}) هستند و بنابراین اولویت برابری دارند. قاعده رسمی درس سوربن صراحتاً اعلام می‌کند:</p>
      <p><em>«در صورت اولویت برابر: زیرفرمول سمت راست همیشه اولویت دارد.»</em></p>
      <p>مراحل پرانتزگذاری گام‌به‌گام از راست به چپ:</p>
      <ol>
        <li>دسته‌بندی دو اتم انتهایی راست: {{ (r \land s) }}.</li>
        <li>دسته‌بندی با اتم ماقبل: {{ (q \land (r \land s)) }}.</li>
        <li>دسته‌بندی نهایی با اتم نخست {{ p }}: {{ (p \land (q \land (r \land s))) }}.</li>
      </ol>
      <p><strong>پاسخ نهایی مورد قبول در برگه امتحان:</strong></p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">{{ (p \land (q \land (r \land s))) }}</p>
      <p><strong>اشتباه رایج و مرگبار در آزمون:</strong> نوشتن <code>(((p &and; q) &and; r) &and; s)</code>. هرچند از نظر معنایی عطف در جبر بولی شرکت‌پذیر است، اما از دیدگاه <em>نحوی</em> در درس سوربن، درخت متناظر با پرانتزگذاری از چپ کاملاً غلط محسوب می‌شود!</p>
    </div>
  </details>
</div>

<!-- Question 2.2 -->
<div class="q-card" id="q2_2">
  <div class="q-header">
    <span class="q-num">زیرمسئله ۲.۲</span>
    <span class="q-title">پرانتزگذاری دقیق فرمول {{ F_4 = p \Rightarrow q \land \neg r \Rightarrow p \lor q }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرمول زیر را با رعایت دقیق اولویت عملگرها پرانتزگذاری کنید:</p>
    <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_4 = p \Rightarrow q \land \neg r \Rightarrow p \lor q }}</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>اعمال دقیق سلسله‌مراتب {{ \neg > \land > \lor > \Rightarrow }}</h4>
      <ol>
        <li><strong>گام ۱ ({{ \neg }}):</strong> نقیض بر اتم {{ r }} اثر دارد: <code>(&not; r)</code>.</li>
        <li><strong>گام ۲ ({{ \land }}):</strong> عطف <code>q &and; (&not; r)</code> اتصال می‌یابد: <code>(q &and; (&not; r))</code>.</li>
        <li><strong>گام ۳ ({{ \lor }}):</strong> فصل <code>p &or; q</code> پرانتز می‌گیرد: <code>(p &or; q)</code>.</li>
        <li>دو عملگر شرطی باقی می‌ماند: <code>p &rArr; (q &and; (&not; r)) &rArr; (p &or; q)</code>.</li>
        <li><strong>گام ۴ (شرکت‌پذیری از راست عملگر {{ \Rightarrow }}):</strong> برای زنجیره شرطی، زیرفرمول سمت <em>راست</em> در اولویت قرار دارد!
          <br/>ابتدا بخش راست پرانتز می‌گیرد: <code>((q &and; (&not; r)) &rArr; (p &or; q))</code>.
          <br/>سپس کل عبارت با گزاره <code>p</code> شرطی می‌شود:
        </li>
      </ol>
      <p><strong>پاسخ نهایی تشریحی برای آزمون:</strong></p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">{{ (p \Rightarrow ((q \land (\neg r)) \Rightarrow (p \lor q))) }}</p>
    </div>
  </details>
</div>

<h2 id="ex2">Exercice 2 – Implication et formalisation du langage naturel</h2>

<div class="box info">
  <h4>مقدمه و داده‌های مسئله</h4>
  <p>گزاره‌های اتمی زیر را در نظر بگیرید:</p>
  <ul>
    <li>{{ p_1 }}: «هوا خوب است»</li>
    <li>{{ p_2 }}: «من پیاده‌روی می‌کنم»</li>
  </ul>
  <p>وضعیت واقعی مورد بررسی این است که <strong>هوا خوب نیست ولی من پیاده‌روی می‌کنم</strong>، که نشان‌دهنده تعبیر صوری زیر است:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ I(p_1) = 0 \quad \text{et} \quad I(p_2) = 1 }}</p>
</div>

<!-- Question 2.1 & 2.2 combinées pour clarté -->
<div class="q-card" id="q_imp">
  <div class="q-header">
    <span class="q-num">سوالات ۱ و ۲</span>
    <span class="q-title">ترجمه صوری و ارزیابی درستی هر ۶ عبارت</span>
  </div>

  <details class="sol" open>
    <summary>تحلیل جامع هر ۶ عبارت زبانی تحت تعبیر {{ I(p_1)=0, I(p_2)=1 }}</summary>
    <div class="box method">
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>شماره</th>
            <th>عبارت در زبان طبیعی</th>
            <th>فرمول منطقی صوری</th>
            <th>محاسبه {{ [F]^I }} تحت {{ I(p_1)=0, I(p_2)=1 }}</th>
            <th>وضعیت درستی</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>۱</strong></td>
            <td>«اگر هوا خوب باشد، پیاده‌روی می‌کنم»</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">صادق است (درست)</span></td>
          </tr>
          <tr>
            <td><strong>۲</strong></td>
            <td>«برای پیاده‌روی من، لازم است که هوا خوب باشد»</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">کاذب است (نادرست)</span></td>
          </tr>
          <tr>
            <td><strong>۳</strong></td>
            <td>«من پیاده‌روی نمی‌کنم مگر آن‌که هوا خوب باشد»</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">کاذب است (نادرست)</span></td>
          </tr>
          <tr>
            <td><strong>۴</strong></td>
            <td>«به محض این‌که هوا خوب شود، پیاده‌روی می‌کنم»</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">صادق است (درست)</span></td>
          </tr>
          <tr>
            <td><strong>۵</strong></td>
            <td>«من پیاده‌روی می‌کنم تنها در صورتی که هوا خوب باشد»</td>
            <td>{{ p_2 \Rightarrow p_1 }}</td>
            <td>{{ 1 \Rightarrow 0 = 0 }}</td>
            <td><span class="badge" style="background:#e74c3c; color:#fff;">کاذب است (نادرست)</span></td>
          </tr>
          <tr>
            <td><strong>۶</strong></td>
            <td>«برای پیاده‌روی من، کافی است که هوا خوب باشد»</td>
            <td>{{ p_1 \Rightarrow p_2 }}</td>
            <td>{{ 0 \Rightarrow 1 = 1 }}</td>
            <td><span class="badge" style="background:#2ecc71; color:#fff;">صادق است (درست)</span></td>
          </tr>
        </tbody>
      </table>

      <h4 style="margin-top:15px;">جمع‌بندی نظری فوق‌العاده مهم برای امتحانات</h4>
      <ul>
        <li><strong>شرط کافی («کافی است»، «اگر»، «به محض»):</strong> خوب بودن هوا برای پیاده‌روی کفایت می‌کند &larr; {{ p_1 \Rightarrow p_2 }}. از آنجا که {{ p_1 }} نادرست است ({{ 0 }})، گزاره شرطی طبق اصل انفجار به طور خودکار <em>درست</em> است! بنابراین گزاره‌های ۱، ۴ و ۶ صادق‌اند.</li>
        <li><strong>شرط لازم («لازم است»، «تنها اگر»، «مگر این‌که»):</strong> خوب بودن هوا پیش‌نیاز اجباری پیاده‌روی است &larr; {{ p_2 \Rightarrow p_1 }}. اما من پیاده‌روی می‌کنم ({{ p_2=1 }}) در حالی که هوا خوب نیست ({{ p_1=0 }}). ارزش {{ 1 \Rightarrow 0 }} برابر با <em>نادرست</em> است؛ بنابراین جملات ۲، ۳ و ۵ کاذب هستند.</li>
      </ul>
    </div>
  </details>
</div>

<h2 id="ex3">Exercice 3 – Tables de vérité et énigmes logiques</h2>

<!-- Question 3.1 -->
<div class="q-card" id="q3_1">
  <div class="q-header">
    <span class="q-num">سوال ۱</span>
    <span class="q-title">جدول درستی فرمول {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>برای فرمول {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }} که در آن {{ p }} و {{ q }} گزاره هستند، جدول درستی کامل {{ F }} را محاسبه کنید.</p>
  </div>

  <div class="w-tt" data-formula="(p & q) & ((q => p) | ~(p | q))"></div>

  <details class="sol" open>
    <summary>محاسبه سطر به سطر با تمامی ستون‌های میانی</summary>
    <div class="box method">
      <p>فرمول دارای {{ 2 }} متغیر است، بنابراین شامل {{ 2^2 = 4 }} سطر تعبیر ممکن است:</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ p }}</th>
            <th>{{ q }}</th>
            <th>{{ p \land q }}</th>
            <th>{{ q \Rightarrow p }}</th>
            <th>{{ p \lor q }}</th>
            <th>{{ \neg(p \lor q) }}</th>
            <th>{{ (q \Rightarrow p) \lor \neg(p \lor q) }}</th>
            <th>{{ F }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>نتیجه‌گیری معنایی:</strong> فرمول {{ F }} تنها و تنها در تعبیر {{ I(p)=1, I(q)=1 }} درست است. بنابراین این فرمول <strong>صدق‌پذیر (Satisfiable)</strong> است، اما <strong>معتبر (توتولوژی) نیست</strong>.</p>
    </div>
  </details>
</div>

<!-- Question 3.2 -->
<div class="q-card" id="q3_2">
  <div class="q-header">
    <span class="q-num">سوال ۲</span>
    <span class="q-title">معمای بازجویی جنایی: آنا و ژولی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>آنا و ژولی درباره یک پرونده قتل مورد بازجویی قرار گرفته و این ادعاها را مطرح می‌کنند:</p>
    <ul>
      <li><strong>آنا:</strong> «ژولی گناهکار است.»</li>
      <li><strong>ژولی:</strong> «اگر من گناهکار باشم، آنگاه آنا هم گناهکار است.»</li>
    </ul>
    <p>گزاره‌ها: {{ A }}: «آنا گناهکار است»، {{ J }}: «ژولی گناهکار است».</p>
    <ol>
      <li>فرمول {{ F_1 }} (ادعای آنا) و {{ F_2 }} (ادعای ژولی) را بنویسید.</li>
      <li>فرض کنید {{ F_3 = F_1 \lor F_2 }} باشد: (الف) جدول درستی آن را حساب کنید، (ب) چه نتیجه‌ای می‌گیرید؟</li>
      <li>فرض کنید {{ F_4 = F_1 \land F_2 }} باشد: (الف) جدول درستی آن را حساب کنید، (ب) چه نتیجه‌ای می‌گیرید؟</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>پاسخ گام‌به‌گام و تحلیل‌های رسمی</summary>
    <div class="box method">
      <h4>۱. فرمول‌بندی صوری</h4>
      <ul>
        <li>ادعای آنا: {{ F_1 = J }}</li>
        <li>ادعای ژولی: {{ F_2 = J \Rightarrow A }}</li>
      </ul>

      <h4>۲. بررسی فصل ادعاها: {{ F_3 = F_1 \lor F_2 = J \lor (J \Rightarrow A) }}</h4>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ J }}</th>
            <th>{{ F_1 = J }}</th>
            <th>{{ F_2 = J \Rightarrow A }}</th>
            <th>{{ F_3 = F_1 \lor F_2 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>0</td><td><strong>1</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td><strong>1</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>نتیجه‌گیری برای {{ F_3 }} :</strong> فرمول {{ F_3 }} یک <strong>توتولوژی (فرمول همواره معتبر)</strong> است، زیرا در تمامی سطرها مقدار ۱ دارد. بنابراین نتیجه می‌گیریم که با اطمینان مطلق <strong>حداقل یکی از این دو نفر همیشه راست می‌گوید</strong>، فارغ از این‌که حقیقت جنایت چه باشد!</p>

      <h4>۳. بررسی عطف ادعاها: {{ F_4 = F_1 \land F_2 = J \land (J \Rightarrow A) }}</h4>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ J }}</th>
            <th>{{ F_1 = J }}</th>
            <th>{{ F_2 = J \Rightarrow A }}</th>
            <th>{{ F_4 = F_1 \land F_2 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>0</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td><strong>0</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td><strong>1</strong></td></tr>
        </tbody>
      </table>
      <p><strong>نتیجه‌گیری برای {{ F_4 }} :</strong> فرمول {{ F_4 }} تنها و تنها یک مدل دارد: {{ A=1, J=1 }}. در نتیجه، <strong>اگر هر دو نفر راست بگویند، الزاماً آنا و ژولی هر دو گناهکار هستند</strong>.</p>
    </div>
  </details>
</div>

<!-- Question 3.3 -->
<div class="q-card" id="q3_3">
  <div class="q-header">
    <span class="q-num">سوال ۳</span>
    <span class="q-title">معمای امتحان منطق: انیسا، خاویر و جنیفر</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>انیسا، خاویر و جنیفر قرار است در امتحان منطق شرکت کنند. می‌دانیم که:</p>
    <ul>
      <li>{{ H_1 }} : حداقل یکی از این سه نفر برای امتحان درس می‌خواند.</li>
      <li>{{ H_2 }} : اگر انیسا درس نخواند، آنگاه خاویر هم درس نخواهد خواند.</li>
      <li>{{ H_3 }} : اگر انیسا درس بخواند، آنگاه جنیفر هم درس خواهد خواند.</li>
    </ul>
    <p>گزاره‌ها: {{ A }}: «انیسا درس می‌خواند»، {{ X }}: «خاویر درس می‌خواند»، {{ J }}: «جنیفر درس می‌خواند».</p>
    <ol>
      <li>این سه فرض را فرمول‌بندی کنید.</li>
      <li>آیا می‌توان مشخص کرد چه کسی قطعاً درس می‌خواند و چه کسی درس نمی‌خواند؟</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>حل دقیق معناشناسی و تحلیل کامل مدل‌ها</summary>
    <div class="box method">
      <h4>۱. فرمول‌بندی ریاضی صوری</h4>
      <ul>
        <li>{{ H_1 : A \lor X \lor J }} (حداقل یکی از سه نفر)</li>
        <li>{{ H_2 : \neg A \Rightarrow \neg X }} (که با عکس نقیض دقیقاً معادل است با {{ X \Rightarrow A }})</li>
        <li>{{ H_3 : A \Rightarrow J }}</li>
      </ul>

      <h4>۲. جستجوی مدل‌های نظریه {{ \mathcal{T} = \{H_1, H_2, H_3\} }}</h4>
      <p>جدول درستی هر سه فرض را در تمام {{ 2^3 = 8 }} تعبیر ممکن تشکیل می‌دهیم:</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ A }}</th>
            <th>{{ X }}</th>
            <th>{{ J }}</th>
            <th>{{ H_1 }}</th>
            <th>{{ H_2 : \neg A \Rightarrow \neg X }}</th>
            <th>{{ H_3 : A \Rightarrow J }}</th>
            <th>{{ H_1 \land H_2 \land H_3 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (مدل I1)</strong></td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (مدل I2)</strong></td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">1 (مدل I3)</strong></td></tr>
        </tbody>
      </table>

      <h4>۳. استنتاج‌های قطعی منطقی</h4>
      <p>دقیقاً ۳ تعبیر وجود دارند که هر سه فرض را به طور هم‌زمان ارضا می‌کنند:</p>
      <ul>
        <li>{{ I_1 = \{A=0, X=0, J=1\} }}</li>
        <li>{{ I_2 = \{A=1, X=0, J=1\} }}</li>
        <li>{{ I_3 = \{A=1, X=1, J=1\} }}</li>
      </ul>
      <p><strong>نتیجه‌گیری دانشگاهی نهایی:</strong></p>
      <ul>
        <li>در هر ۳ مدل بدون استثنا مقدار {{ J = 1 }} است. <strong>بنابراین با قطعیت ۱۰۰٪ می‌توان گفت که جنیفر قطعاً درس خواهد خواند</strong> ({{ \mathcal{T} \models J }}).</li>
        <li>درباره انیسا: در دو مدل {{ I_2 }} و {{ I_3 }} مقدارش ۱ است ({{ A=1 }})، اما در مدل {{ I_1 }} درس نمی‌خواند ({{ A=0 }}). <strong>بنابراین بدون اطلاعات بیشتر، نمی‌توان با قطعیت گفت که انیسا درس می‌خواند یا خیر.</strong></li>
        <li>درباره خاویر: در مدل {{ I_3 }} مقدارش ۱ است ({{ X=1 }})، ولی در دو مدل {{ I_1 }} و {{ I_2 }} درس نمی‌خواند ({{ X=0 }}). <strong>بنابراین بدون اطلاعات بیشتر، نمی‌توان با قطعیت گفت که خاویر درس می‌خواند یا خیر.</strong></li>
        <li>تنها می‌توان افزود: اگر خاویر درس بخواند، الزاماً انیسا نیز درس می‌خواند (مطابق مدل {{ I_3 }}).</li>
      </ul>
    </div>
  </details>
</div>
"""

open(os.path.join(W01, 'td.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W01, 'td.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("td.fr.html and td.fa.html written.")
