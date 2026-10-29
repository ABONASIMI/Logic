#!/usr/bin/env python3
"""Authoring generator for TD Week 2 (Thème 2).
Exhaustive step-by-step solutions for:
- Exercice 4: Q1 (F1, ~F1), Q2 (F3, F4)
- Exercice 5: (a), (b), (c), (d)
- Exercice 6: Q1 (F1 valide -> F1 & F2 =| F2), Q2 (F1 insat -> F1 | F2 =| F2)
- Exercice 7: Q1 ([F]^I simplification équationnelle), Q2 (Énigme révision par algèbre booléenne)
- Exercice 8: Q1 (ChatGPT 2025 réfuté par [F]^I, [G]^I), Q2 (ChatGPT 2026 : F vs G avec variable C)
"""
import os

W02 = '/home/mnasimi/sorbonne/Logic_Academy/content/w02'
os.makedirs(W02, exist_ok=True)

fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TD Thème 2 : Conséquence Sémantique et Calcul Équationnel</h1>
  <p class="lead">Corrections intégrales des 5 exercices officiels du polycopié de TD (2026-2027) : satisfiabilité et validité sans table de vérité, conséquences sémantiques formelles, algèbre de Boole et analyse critique des réponses d'IA.</p>
</div>

<div class="toc-box">
  <h3>Sommaire des exercices du TD</h3>
  <ul>
    <li><a href="#td2_ex4">Exercice 4 – Formules satisfiables et valides sans table de vérité</a></li>
    <li><a href="#td2_ex5">Exercice 5 – Conséquence sémantique formelle</a></li>
    <li><a href="#td2_ex6">Exercice 6 – Équivalence logique et propriétés d'absorption</a></li>
    <li><a href="#td2_ex7">Exercice 7 – Expressions booléennes et résolution équationnelle d'énigme</a></li>
    <li><a href="#td2_ex8">Exercice 8 – Analyse critique : faut-il toujours croire ChatGPT ?</a></li>
  </ul>
</div>

<div class="box warn">
  <h4>Consigne générale impérative du sujet de TD</h4>
  <p><em>« Pour répondre aux exercices de ce thème vous ne devez pas utiliser de table de vérité. »</em></p>
  <p>Toute réponse basée sur une table de vérité sera pénalisée de 0 point par les correcteurs de la Sorbonne. Toutes les justifications doivent reposer exclusivement sur l'exhibition de modèles/contre-modèles ou sur le calcul équationnel en algèbre de Boole.</p>
</div>

<!-- EXERCICE 4 -->
<h2 id="td2_ex4">Exercice 4 – Formules satisfiables et valides sans table de vérité</h2>

<!-- Q4.1 -->
<div class="q-card" id="td2_q4_1">
  <div class="q-header">
    <span class="q-num">Question 1</span>
    <span class="q-title">Étude de {{ F_1 = (p \land \neg q) \lor (\neg p \land q) }} et {{ \neg F_1 }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>On considère la formule {{ F_1 = (p \land \neg q) \lor (\neg p \land q) }}. Les formules {{ F_1 }} et {{ \neg F_1 }} sont-elles satisfiables ? Sont-elles valides ?</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée sans table de vérité</summary>
    <div class="box method">
      <h4>1. Étude de la formule {{ F_1 }}</h4>
      <ul>
        <li><strong>Satisfiabilité de {{ F_1 }} :</strong>
          <br/>Considérons l'interprétation {{ I_1 }} définie par {{ I_1(p) = 1 }} et {{ I_1(q) = 0 }}.
          <br/>Calculons {{ [F_1]^{I_1} }} :
          <div style="margin:6px 0;">
            {{ [F_1]^{I_1} = (I_1(p) \cdot \overline{I_1(q)}) + (\overline{I_1(p)} \cdot I_1(q)) = (1 \cdot 1) + (0 \cdot 0) = 1 + 0 = 1 }}
          </div>
          Puisqu'il existe au moins une interprétation {{ I_1 }} telle que {{ [F_1]^{I_1} = 1 }}, <strong>la formule {{ F_1 }} est satisfiable</strong>.
        </li>
        <li><strong>Validité de {{ F_1 }} :</strong>
          <br/>Pour prouver qu'une formule n'est pas valide, il suffit d'exhiber un contre-modèle.
          <br/>Considérons l'interprétation {{ I_0 }} définie par {{ I_0(p) = 0 }} et {{ I_0(q) = 0 }}.
          <div style="margin:6px 0;">
            {{ [F_1]^{I_0} = (0 \cdot 1) + (1 \cdot 0) = 0 + 0 = 0 }}
          </div>
          Puisqu'il existe une interprétation {{ I_0 }} telle que {{ [F_1]^{I_0} = 0 }}, <strong>la formule {{ F_1 }} n'est pas valide</strong>.
        </li>
      </ul>

      <h4>2. Étude de la formule {{ \neg F_1 }}</h4>
      <ul>
        <li><strong>Satisfiabilité de {{ \neg F_1 }} :</strong>
          <br/>Sous l'interprétation {{ I_0 }} ci-dessus, on a :
          <div style="margin:6px 0;">
            {{ [\neg F_1]^{I_0} = 1 - [F_1]^{I_0} = 1 - 0 = 1 }}
          </div>
          Donc {{ I_0 }} est un modèle de {{ \neg F_1 }}. <strong>La formule {{ \neg F_1 }} est satisfiable</strong>.
        </li>
        <li><strong>Validité de {{ \neg F_1 }} :</strong>
          <br/>Sous l'interprétation {{ I_1 }} ci-dessus, on a :
          <div style="margin:6px 0;">
            {{ [\neg F_1]^{I_1} = 1 - [F_1]^{I_1} = 1 - 1 = 0 }}
          </div>
          Donc {{ I_1 }} est un contre-modèle de {{ \neg F_1 }}. <strong>La formule {{ \neg F_1 }} n'est pas valide</strong>.
        </li>
      </ul>
      <p><strong>Synthèse d'examen :</strong> {{ F_1 }} et {{ \neg F_1 }} sont toutes deux <strong>satisfiables mais non valides</strong> (formules contingentes).</p>
    </div>
  </details>
</div>

<!-- Q4.2 -->
<div class="q-card" id="td2_q4_2">
  <div class="q-header">
    <span class="q-num">Question 2</span>
    <span class="q-title">Étude de {{ F_3 = F_1 \lor F_2 }} et {{ F_4 = F_1 \land F_2 }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit {{ F_2 = (p \land q) \lor (\neg p \land \neg q) }}. Les formules suivantes sont-elles satisfiables ? Sont-elles valides ?</p>
    <ul>
      <li>{{ F_3 = F_1 \lor F_2 }}</li>
      <li>{{ F_4 = F_1 \land F_2 }}</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Calcul algébrique rigoureux</summary>
    <div class="box method">
      <h4>1. Étude de {{ F_3 = F_1 \lor F_2 }}</h4>
      <p>Traduisons en expression booléenne sous une interprétation quelconque {{ I }} en posant {{ x = I(p) }} et {{ y = I(q) }} :</p>
      <div style="line-height:2em; font-size:1.05em;">
        {{ [F_3]^I = [F_1]^I + [F_2]^I }}<br/>
        {{ = (x \cdot \overline{y} + \overline{x} \cdot y) + (x \cdot y + \overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot \overline{y} + x \cdot y) + (\overline{x} \cdot y + \overline{x} \cdot \overline{y}) }} \quad <em>(Commutativité et associativité)</em><br/>
        {{ = x \cdot (\overline{y} + y) + \overline{x} \cdot (y + \overline{y}) }} \quad <em>(Distributivité)</em><br/>
        {{ = x \cdot 1 + \overline{x} \cdot 1 }} \quad <em>(Complémentarité)</em><br/>
        {{ = x + \overline{x} = 1 }} \quad <em>(Complémentarité finale)</em>
      </div>
      <p>Puisque {{ [F_3]^I = 1 }} pour <em>toute</em> interprétation {{ I }}, <strong>{{ F_3 }} est valide</strong> (et donc trivialement satisfiable).</p>

      <h4>2. Étude de {{ F_4 = F_1 \land F_2 }}</h4>
      <p>Calculons {{ [F_4]^I = [F_1]^I \cdot [F_2]^I }} sous une interprétation quelconque {{ I }} :</p>
      <div style="line-height:2em; font-size:1.05em;">
        {{ [F_4]^I = (x \cdot \overline{y} + \overline{x} \cdot y) \cdot (x \cdot y + \overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot \overline{y}) \cdot (x \cdot y) + (x \cdot \overline{y}) \cdot (\overline{x} \cdot \overline{y}) + (\overline{x} \cdot y) \cdot (x \cdot y) + (\overline{x} \cdot y) \cdot (\overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot x) \cdot (\overline{y} \cdot y) + (x \cdot \overline{x}) \cdot (\overline{y} \cdot \overline{y}) + (\overline{x} \cdot x) \cdot (y \cdot y) + (\overline{x} \cdot \overline{x}) \cdot (y \cdot \overline{y}) }}<br/>
        {{ = x \cdot 0 + 0 \cdot \overline{y} + 0 \cdot y + \overline{x} \cdot 0 = 0 + 0 + 0 + 0 = 0 }}
      </div>
      <p>Puisque {{ [F_4]^I = 0 }} pour toute interprétation {{ I }}, <strong>{{ F_4 }} est insatisfiable</strong> (et donc non valide).</p>
    </div>
  </details>
</div>

<!-- EXERCICE 5 -->
<h2 id="td2_ex5">Exercice 5 – Conséquence sémantique formelle</h2>

<div class="q-card" id="td2_ex5_all">
  <div class="q-header">
    <span class="q-num">Exercice 5</span>
    <span class="q-title">Analyse théorique de conséquence avec formule insatisfiable {{ F }} et contingente {{ G }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit {{ F }} une formule insatisfiable et {{ G }} une formule ni valide, ni non satisfiable (c'est-à-dire contingente : satisfiable et non valide). Répondre et justifier :</p>
    <ul>
      <li>(a) A-t-on {{ F \models G }} ?</li>
      <li>(b) A-t-on {{ G \models F }} ?</li>
      <li>(c) A-t-on {{ \neg F \models G }} ?</li>
      <li>(d) A-t-on {{ G \models \neg F }} ?</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Justifications mathématiques rigoureuses</summary>
    <div class="box method">
      <h4>(a) A-t-on {{ F \models G }} ? &rarr; OUI</h4>
      <p><strong>Justification :</strong> Par définition, {{ F \models G }} signifie que pour toute interprétation {{ I }}, si {{ [F]^I = 1 }}, alors {{ [G]^I = 1 }}.</p>
      <p>Or, la formule {{ F }} est insatisfiable, ce qui signifie qu'il <em>n'existe aucune</em> interprétation {{ I }} telle que {{ [F]^I = 1 }}. L'implication est donc universellement vraie par vacuité (principe du faux qui implique tout : <em>ex falso quodlibet</em>). On a donc bien {{ F \models G }}.</p>

      <h4>(b) A-t-on {{ G \models F }} ? &rarr; NON</h4>
      <p><strong>Justification par contre-modèle :</strong> Par hypothèse, {{ G }} est satisfiable, il existe donc au moins une interprétation {{ I_1 }} telle que {{ [G]^{I_1} = 1 }}.</p>
      <p>Cependant, comme {{ F }} est insatisfiable, on a obligatoirement {{ [F]^{I_1} = 0 }}. L'interprétation {{ I_1 }} vérifie donc l'hypothèse ({{ [G]^{I_1} = 1 }}) mais ne vérifie pas la conclusion ({{ [F]^{I_1} = 0 }}). {{ I_1 }} est un <strong>contre-modèle explicite</strong>. Donc {{ G \not\models F }}.</p>

      <h4>(c) A-t-on {{ \neg F \models G }} ? &rarr; NON</h4>
      <p><strong>Justification par contre-modèle :</strong> Puisque {{ F }} est insatisfiable, sa négation {{ \neg F }} est <strong>valide</strong> (pour toute interprétation {{ I }}, {{ [\neg F]^I = 1 - 0 = 1 }}).</p>
      <p>D'autre part, comme {{ G }} n'est pas valide, il existe au moins une interprétation {{ I_0 }} telle que {{ [G]^{I_0} = 0 }}. Pour cette interprétation {{ I_0 }}, on a {{ [\neg F]^{I_0} = 1 }} et {{ [G]^{I_0} = 0 }}. L'interprétation {{ I_0 }} constitue un contre-modèle. Donc {{ \neg F \not\models G }}.</p>

      <h4>(d) A-t-on {{ G \models \neg F }} ? &rarr; OUI</h4>
      <p><strong>Justification :</strong> Comme établi au point (c), la formule {{ \neg F }} est <strong>valide</strong>, ce qui implique que pour <em>toute</em> interprétation {{ I }}, {{ [\neg F]^I = 1 }}.</p>
      <p>Dès lors, pour toute interprétation {{ I }} satisfaisant {{ G }} ({{ [G]^I = 1 }}), on a immédiatement {{ [\neg F]^I = 1 }}. Par conséquent, {{ G \models \neg F }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 6 -->
<h2 id="td2_ex6">Exercice 6 – Équivalence logique et propriétés d'absorption</h2>

<div class="q-card" id="td2_ex6_all">
  <div class="q-header">
    <span class="q-num">Exercice 6</span>
    <span class="q-title">Preuves formelles d'équivalences avec formules valides et insatisfiables</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soient {{ F_1 }} et {{ F_2 }} deux formules de la logique propositionnelle.</p>
    <ol>
      <li>Montrer que si {{ F_1 }} est valide, alors {{ F_1 \land F_2 \equiv F_2 }}.</li>
      <li>Montrer que si {{ F_1 }} est insatisfiable, alors {{ F_1 \lor F_2 \equiv F_2 }}.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Démonstrations algébriques formelles</summary>
    <div class="box method">
      <h4>1. Preuve : si {{ F_1 }} est valide, alors {{ F_1 \land F_2 \equiv F_2 }}</h4>
      <p>Soit {{ I }} une interprétation quelconque. Par hypothèse, {{ F_1 }} est valide, donc {{ [F_1]^I = 1 }}.</p>
      <p>Calculons la valeur de vérité de {{ F_1 \land F_2 }} sous {{ I }} :</p>
      <div style="margin:6px 0;">
        {{ [F_1 \land F_2]^I = [F_1]^I \cdot [F_2]^I = 1 \cdot [F_2]^I = [F_2]^I }} \quad <em>(1 est élément neutre de la conjonction)</em>
      </div>
      <p>Puisque cette égalité {{ [F_1 \land F_2]^I = [F_2]^I }} est vérifiée pour <strong>toute interprétation {{ I }}</strong>, on conclut par définition de l'équivalence logique que :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_1 \land F_2 \equiv F_2 }}</p>

      <h4>2. Preuve : si {{ F_1 }} est insatisfiable, alors {{ F_1 \lor F_2 \equiv F_2 }}</h4>
      <p>Soit {{ I }} une interprétation quelconque. Par hypothèse, {{ F_1 }} est insatisfiable, donc {{ [F_1]^I = 0 }}.</p>
      <p>Calculons la valeur de vérité de {{ F_1 \lor F_2 }} sous {{ I }} :</p>
      <div style="margin:6px 0;">
        {{ [F_1 \lor F_2]^I = [F_1]^I + [F_2]^I = 0 + [F_2]^I = [F_2]^I }} \quad <em>(0 est élément neutre de la disjonction)</em>
      </div>
      <p>Puisque cette égalité {{ [F_1 \lor F_2]^I = [F_2]^I }} est vérifiée pour <strong>toute interprétation {{ I }}</strong>, on conclut par définition de l'équivalence logique que :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_1 \lor F_2 \equiv F_2 }}</p>
    </div>
  </details>
</div>

<!-- EXERCICE 7 -->
<h2 id="td2_ex7">Exercice 7 – Expressions booléennes et résolution équationnelle d'énigme</h2>

<div class="q-card" id="td2_q7_1">
  <div class="q-header">
    <span class="q-num">Question 1</span>
    <span class="q-title">Simplification équationnelle de {{ [F]^I }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Soit la formule {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }} où {{ p }} et {{ q }} sont des propositions. Calculer et simplifier l'expression booléenne {{ [F]^I }} en fonction de {{ I(p) }} et {{ I(q) }} en indiquant l'équivalence utilisée à chaque étape.</p>
  </div>

  <details class="sol" open>
    <summary>Calcul pas à pas avec justifications des règles</summary>
    <div class="box method">
      <p>Posons pour alléger l'écriture {{ x = I(p) }} et {{ y = I(q) }}. Développons l'expression {{ [F]^I }} :</p>
      <div style="line-height:2.2em; font-size:1.05em;">
        {{ [F]^I = [p \land q]^I \cdot [(q \Rightarrow p) \lor \neg(p \lor q)]^I }}<br/>
        {{ = (x \cdot y) \cdot ( [q \Rightarrow p]^I + [\neg(p \lor q)]^I ) }}<br/>
        {{ = (x \cdot y) \cdot ( (\overline{y} + x) + \overline{x + y} ) }} \quad <em>(Traduction sémantique de l'implication et de la négation)</em><br/>
        {{ \equiv (x \cdot y) \cdot ( (\overline{y} + x) + (\overline{x} \cdot \overline{y}) ) }} \quad <em>(Loi de De Morgan sur {{ \overline{x + y} }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + (\overline{y} + \overline{x} \cdot \overline{y}) ) }} \quad <em>(Commutativité et associativité de +)</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} \cdot (1 + \overline{x}) ) }} \quad <em>(Factorisation par {{ \overline{y} }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} \cdot 1 ) }} \quad <em>(Élément absorbant : {{ 1 + \overline{x} = 1 }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} ) }} \quad <em>(Élément neutre de {{ \cdot }})</em><br/>
        {{ \equiv (x \cdot y) \cdot x + (x \cdot y) \cdot \overline{y} }} \quad <em>(Distributivité de {{ \cdot }} sur {{ + }})</em><br/>
        {{ \equiv (x \cdot x) \cdot y + x \cdot (y \cdot \overline{y}) }} \quad <em>(Associativité et commutativité)</em><br/>
        {{ \equiv x \cdot y + x \cdot 0 }} \quad <em>(Idempotence {{ x \cdot x = x }} et complémentarité {{ y \cdot \overline{y} = 0 }})</em><br/>
        {{ \equiv x \cdot y + 0 }} \quad <em>(Élément absorbant : {{ x \cdot 0 = 0 }})</em><br/>
        {{ \equiv x \cdot y }} \quad <em>(Élément neutre : {{ a + 0 = a }})</em>
      </div>
      <p><strong>Conclusion finale :</strong> {{ [F]^I = I(p) \cdot I(q) }}. La formule {{ F }} se réduit algébriquement à la simple conjonction {{ p \land q }}.</p>
    </div>
  </details>
</div>

<div class="q-card" id="td2_q7_2">
  <div class="q-header">
    <span class="q-num">Question 2</span>
    <span class="q-title">Résolution équationnelle de l'énigme d'Anissa, Xavier et Jennifer</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>On reprend l'énigme du Thème 1 : {{ H_1 }} : l'un au moins révise ; {{ H_2 }} : si Anissa ne révise pas, Xavier non plus ; {{ H_3 }} : si Anissa révise, Jennifer aussi.</p>
    <p>En notant {{ A }}, {{ X }} et {{ J }} les propositions booléennes correspondantes, formaliser puis déterminer par un <strong>raisonnement équationnel</strong> qui révisera et qui ne révisera pas.</p>
  </div>

  <details class="sol" open>
    <summary>Résolution équationnelle complète</summary>
    <div class="box method">
      <h4>1. Formalisation algébrique</h4>
      <p>Dans toute interprétation {{ I }} satisfaisant les trois hypothèses simultanément, le produit de leurs valeurs de vérité vaut 1 :</p>
      <div style="margin:8px 0; font-size:1.1em;">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = 1 }}
      </div>
      <p>Exprimons chaque terme en posant {{ a = I(A), x = I(X), j = I(J) }} :</p>
      <ul>
        <li>{{ [H_1]^I = a + x + j }}</li>
        <li>{{ [H_2]^I = [\neg A \Rightarrow \neg X]^I = \overline{\overline{a}} + \overline{x} = a + \overline{x} }}</li>
        <li>{{ [H_3]^I = [A \Rightarrow J]^I = \overline{a} + j }}</li>
      </ul>

      <h4>2. Calcul algébrique du produit</h4>
      <p>Calculons d'abord {{ [H_2]^I \cdot [H_3]^I }} :</p>
      <div style="line-height:2em;">
        {{ (a + \overline{x}) \cdot (\overline{a} + j) = a \cdot \overline{a} + a \cdot j + \overline{x} \cdot \overline{a} + \overline{x} \cdot j }}<br/>
        {{ = 0 + a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j = a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j }}
      </div>
      <p>Multiplions maintenant par {{ [H_1]^I = a + x + j }} :</p>
      <div style="line-height:2em;">
        {{ (a + x + j) \cdot (a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j) }}<br/>
        {{ = a \cdot (a \cdot j) + a \cdot (\overline{a} \cdot \overline{x}) + a \cdot (\overline{x} \cdot j) + x \cdot (a \cdot j) + x \cdot (\overline{a} \cdot \overline{x}) + x \cdot (\overline{x} \cdot j) + j \cdot (a \cdot j) + j \cdot (\overline{a} \cdot \overline{x}) + j \cdot (\overline{x} \cdot j) }}
      </div>
      <p>Simplifions chaque monôme :</p>
      <ul>
        <li>{{ a \cdot a \cdot j = a \cdot j }}</li>
        <li>{{ a \cdot \overline{a} \cdot \overline{x} = 0 }}</li>
        <li>{{ a \cdot \overline{x} \cdot j }}</li>
        <li>{{ x \cdot a \cdot j = a \cdot x \cdot j }}</li>
        <li>{{ x \cdot \overline{a} \cdot \overline{x} = 0 }}</li>
        <li>{{ x \cdot \overline{x} \cdot j = 0 }}</li>
        <li>{{ j \cdot a \cdot j = a \cdot j }}</li>
        <li>{{ j \cdot \overline{a} \cdot \overline{x} = \overline{a} \cdot \overline{x} \cdot j }}</li>
        <li>{{ j \cdot \overline{x} \cdot j = \overline{x} \cdot j }}</li>
      </ul>
      <p>La somme globale devient :</p>
      <div style="margin:8px 0; font-size:1.05em;">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = a \cdot j + a \cdot \overline{x} \cdot j + a \cdot x \cdot j + \overline{a} \cdot \overline{x} \cdot j + \overline{x} \cdot j }}
      </div>
      <p>Factorisons par {{ j }} (qui apparaît dans <strong>chaque</strong> terme restant !) :</p>
      <div style="margin:8px 0; font-size:1.1em; font-weight:bold;">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = j \cdot ( a + a \cdot \overline{x} + a \cdot x + \overline{a} \cdot \overline{x} + \overline{x} ) }}
      </div>
      <p>Par absorption, {{ a + a \cdot \overline{x} + a \cdot x = a }} et {{ \overline{x} + \overline{a} \cdot \overline{x} = \overline{x} }}, donc l'expression se simplifie en :</p>
      <div style="margin:8px 0; font-size:1.15em; font-weight:bold; text-align:center;">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = j \cdot (a + \overline{x}) }}
      </div>

      <h4>3. Conclusion formelle</h4>
      <p>Pour que cette expression soit égale à 1, il est <strong>strictement nécessaire que {{ j = 1 }}</strong> (car si {{ j = 0 }}, le produit vaut 0 quel que soit le reste). En revanche, le facteur {{ (a + \overline{x}) }} peut être égal à 1 soit avec {{ a = 1 }}, soit avec {{ x = 0 }}.</p>
      <p><strong>Conclusion d'examen :</strong></p>
      <ul>
        <li><strong>Jennifer révisera avec certitude</strong> ({{ I(J) = 1 }}).</li>
        <li>On ne peut rien affirmer avec certitude sur la révision d'Anissa ou de Xavier.</li>
      </ul>
    </div>
  </details>
</div>

<!-- EXERCICE 8 -->
<h2 id="td2_ex8">Exercice 8 – Analyse critique : faut-il toujours croire ChatGPT ?</h2>

<div class="q-card" id="td2_q8_1">
  <div class="q-header">
    <span class="q-num">Question 1</span>
    <span class="q-title">Réfutation de la réponse de ChatGPT de juin 2025</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>À la question « Donne-moi une formule logiquement équivalente à {{ A \land B }} mais plus complexe », ChatGPT a répondu en juin 2025 que la formule {{ G = \neg((A \Rightarrow \neg B) \lor (\neg A \Rightarrow B)) }} était équivalente à {{ F = A \land B }}.</p>
    <ol>
      <li>En calculant {{ [F]^I }} et {{ [G]^I }}, montrer que la réponse de ChatGPT est fausse.</li>
      <li>Identifier l'erreur dans le raisonnement donné par ChatGPT.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Réfutation algébrique et analyse de l'erreur</summary>
    <div class="box method">
      <h4>1. Calcul algébrique de {{ [F]^I }} et {{ [G]^I }}</h4>
      <p>Posons {{ a = I(A) }} et {{ b = I(B) }}. On a évidemment {{ [F]^I = a \cdot b }}.</p>
      <p>Calculons {{ [G]^I }} :</p>
      <div style="line-height:2em; font-size:1.05em;">
        {{ [G]^I = \overline{ [A \Rightarrow \neg B]^I + [\neg A \Rightarrow B]^I } }}<br/>
        {{ = \overline{ (\overline{a} + \overline{b}) + (\overline{\overline{a}} + b) } }}<br/>
        {{ = \overline{ \overline{a} + \overline{b} + a + b } }}<br/>
        {{ = \overline{ (a + \overline{a}) + (b + \overline{b}) } }} \quad <em>(Commutativité et associativité)</em><br/>
        {{ = \overline{ 1 + 1 } = \overline{1} = 0 }}
      </div>
      <p>On constate que pour <strong>toute</strong> interprétation {{ I }}, {{ [G]^I = 0 }}. La formule {{ G }} est donc <strong>insatisfiable (une contradiction absolue)</strong> !</p>
      <p>Considérons maintenant l'interprétation {{ I_1 }} telle que {{ I_1(A) = 1 }} et {{ I_1(B) = 1 }} :</p>
      <ul>
        <li>{{ [F]^{I_1} = 1 \cdot 1 = 1 }}</li>
        <li>{{ [G]^{I_1} = 0 }}</li>
      </ul>
      <p>Puisque {{ [F]^{I_1} \neq [G]^{I_1} }}, les formules {{ F }} et {{ G }} ne sont <strong>pas logiquement équivalentes</strong>. La réponse fournie par ChatGPT est donc mathématiquement fausse.</p>

      <h4>2. Identification de l'erreur commise par ChatGPT</h4>
      <p>ChatGPT a écrit : <em>« cette négation force que ni l'un ni l'autre ne soit vrai, ce qui au final impose A &and; B »</em>.</p>
      <p>L'erreur fatale réside dans le fait que la sous-formule disjonctive {{ (A \Rightarrow \neg B) \lor (\neg A \Rightarrow B) }} est une <strong>tautologie (toujours vraie)</strong>. En effet, quelle que soit la valeur de vérité de {{ A }} et de {{ B }}, il est impossible que les deux implications soient fausses en même temps. En niant une tautologie, on obtient une formule <strong>insatisfiable</strong> (identiquement fausse), et non pas {{ A \land B }} !</p>
    </div>
  </details>
</div>

<div class="q-card" id="td2_q8_2">
  <div class="q-header">
    <span class="q-num">Question 2</span>
    <span class="q-title">Analyse des deux formules avec variable auxiliaire proposées en juillet 2026</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>En juillet 2026, ChatGPT propose deux nouvelles formules :</p>
    <ul>
      <li>{{ F = (A \lor C) \land (B \lor \neg C) \land (A \lor \neg C) }}</li>
      <li>{{ G = (A \lor C) \land (A \lor \neg C) \land (B \lor C) \land (B \lor \neg C) }}</li>
    </ul>
    <p>Montrer que l'une des formules est équivalente à {{ A \land B }} mais pas l'autre.</p>
  </div>

  <details class="sol" open>
    <summary>Démonstration algébrique comparative</summary>
    <div class="box method">
      <h4>1. Étude de la formule {{ G }}</h4>
      <p>Regroupons les conjonctions de {{ G }} deux à deux :</p>
      <ul>
        <li>Premier groupe : {{ (A \lor C) \land (A \lor \neg C) }}
          <br/>Par distributivité de {{ \lor }} sur {{ \land }} :
          {{ (A \lor C) \land (A \lor \neg C) \equiv A \lor (C \land \neg C) \equiv A \lor 0 \equiv A }}.
        </li>
        <li>Second groupe : {{ (B \lor C) \land (B \lor \neg C) }}
          <br/>De même :
          {{ (B \lor C) \land (B \lor \neg C) \equiv B \lor (C \land \neg C) \equiv B \lor 0 \equiv B }}.
        </li>
      </ul>
      <p>En recombinant les deux groupes :</p>
      <div style="margin:6px 0; font-size:1.1em; font-weight:bold;">
        {{ G \equiv A \land B }}
      </div>
      <p>La formule {{ G }} est donc <strong>parfaitement équivalente à {{ A \land B }}</strong>.</p>

      <h4>2. Étude de la formule {{ F }}</h4>
      <p>Simplifions l'expression de {{ F }} en regroupant le premier et le troisième terme :</p>
      <div style="margin:6px 0;">
        {{ (A \lor C) \land (A \lor \neg C) \equiv A \lor (C \land \neg C) \equiv A }}
      </div>
      <p>La formule {{ F }} se simplifie donc en :</p>
      <div style="margin:6px 0; font-size:1.1em; font-weight:bold;">
        {{ F \equiv A \land (B \lor \neg C) }}
      </div>
      <p>Est-elle équivalente à {{ A \land B }} ? <strong>NON !</strong> Réfutons-le par un contre-modèle explicite :</p>
      <p>Considérons l'interprétation {{ I_c }} définie par :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ I_c(A) = 1, \quad I_c(B) = 0, \quad I_c(C) = 0 }}</p>
      <ul>
        <li>Évaluation de {{ A \land B }} : {{ [A \land B]^{I_c} = 1 \cdot 0 = 0 }}.</li>
        <li>Évaluation de {{ F }} : {{ [F]^{I_c} = [A]^{I_c} \cdot ([B]^{I_c} + \overline{[C]^{I_c}}) = 1 \cdot (0 + 1) = 1 \cdot 1 = 1 }}.</li>
      </ul>
      <p>Puisque {{ [F]^{I_c} = 1 \neq [A \land B]^{I_c} = 0 }}, l'interprétation {{ I_c }} prouve de manière irréfutable que <strong>{{ F }} n'est pas équivalente à {{ A \land B }}</strong>.</p>
    </div>
  </details>
</div>
"""

fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>تمرین‌های عملی فصل ۲: استلزام معنایی و محاسبات معادلاتی</h1>
  <p class="lead">حل تشریحی کامل هر ۵ تمرین رسمی جزوه TD دانشگاه سوربن (سال تحصیلی ۲۰۲۶-۲۰۲۷): صدق‌پذیری و اعتبار بدون جدول درستی، استلزام معنایی صوری، جبر بولی و تحلیل علمی خطاهای هوش مصنوعی.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب تمرین‌ها</h3>
  <ul>
    <li><a href="#td2_ex4">تمرین ۴ – فرمول‌های صدق‌پذیر و معتبر بدون جدول درستی</a></li>
    <li><a href="#td2_ex5">تمرین ۵ – استلزام معنایی صوری</a></li>
    <li><a href="#td2_ex6">تمرین ۶ – هم‌ارزی منطقی و قوانین جذب</a></li>
    <li><a href="#td2_ex7">تمرین ۷ – عبارات بولی و حل معادلاتی معماها</a></li>
    <li><a href="#td2_ex8">تمرین ۸ – تحلیل نقادانه: آیا همواره باید پاسخ‌های ChatGPT را پذیرفت؟</a></li>
  </ul>
</div>

<div class="box warn">
  <h4>دستورالعمل صریح و اجباری اساتید در صورت مسئله TD</h4>
  <p><em>«برای پاسخ دادن به تمرین‌های این بخش، حق استفاده از جدول درستی را ندارید.»</em></p>
  <p>هرگونه پاسخی که با جدول درستی نوشته شود در تصحیح آزمون‌های سوربن نمره صفر خواهد گرفت. تمامی استدلال‌ها باید منحصراً بر پایه ارائه مدل/پادمدل یا محاسبات معادلاتی در جبر بولی باشند.</p>
</div>

<!-- EXERCICE 4 -->
<h2 id="td2_ex4">Exercice 4 – Formules satisfiables et valides sans table de vérité</h2>

<!-- Q4.1 -->
<div class="q-card" id="td2_q4_1">
  <div class="q-header">
    <span class="q-num">سوال ۱</span>
    <span class="q-title">بررسی فرمول‌های {{ F_1 = (p \land \neg q) \lor (\neg p \land q) }} و {{ \neg F_1 }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرمول {{ F_1 = (p \land \neg q) \lor (\neg p \land q) }} را در نظر بگیرید. آیا فرمول‌های {{ F_1 }} و {{ \neg F_1 }} صدق‌پذیر هستند؟ آیا معتبر (توتولوژی) هستند؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی بدون استفاده از جدول درستی</summary>
    <div class="box method">
      <h4>۱. بررسی ویژگی‌های فرمول {{ F_1 }}</h4>
      <ul>
        <li><strong>صدق‌پذیری {{ F_1 }} :</strong>
          <br/>تعبیر {{ I_1 }} را با مقادیر {{ I_1(p) = 1 }} و {{ I_1(q) = 0 }} در نظر می‌گیریم.
          <br/>مقدار {{ [F_1]^{I_1} }} را محاسبه می‌کنیم:
          <div style="margin:6px 0;" dir="ltr">
            {{ [F_1]^{I_1} = (I_1(p) \cdot \overline{I_1(q)}) + (\overline{I_1(p)} \cdot I_1(q)) = (1 \cdot 1) + (0 \cdot 0) = 1 + 0 = 1 }}
          </div>
          از آنجا که حداقل یک تعبیر {{ I_1 }} وجود دارد به طوری که {{ [F_1]^{I_1} = 1 }} باشد، <strong>فرمول {{ F_1 }} صدق‌پذیر (Satisfiable) است</strong>.
        </li>
        <li><strong>اعتبار (توتولوژی بودن) {{ F_1 }} :</strong>
          <br/>برای رد اعتبار یک فرمول، کافی است یک پادمدل صریح ارائه دهیم.
          <br/>تعبیر {{ I_0 }} را با مقادیر {{ I_0(p) = 0 }} و {{ I_0(q) = 0 }} در نظر می‌گیریم:
          <div style="margin:6px 0;" dir="ltr">
            {{ [F_1]^{I_0} = (0 \cdot 1) + (1 \cdot 0) = 0 + 0 = 0 }}
          </div>
          از آنجا که یک تعبیر {{ I_0 }} وجود دارد به طوری که {{ [F_1]^{I_0} = 0 }} باشد، <strong>فرمول {{ F_1 }} معتبر نیست</strong>.
        </li>
      </ul>

      <h4>۲. بررسی ویژگی‌های فرمول {{ \neg F_1 }}</h4>
      <ul>
        <li><strong>صدق‌پذیری {{ \neg F_1 }} :</strong>
          <br/>تحت تعبیر {{ I_0 }} بالا داریم:
          <div style="margin:6px 0;" dir="ltr">
            {{ [\neg F_1]^{I_0} = 1 - [F_1]^{I_0} = 1 - 0 = 1 }}
          </div>
          بنابراین {{ I_0 }} یک مدل برای {{ \neg F_1 }} است. <strong>فرمول {{ \neg F_1 }} صدق‌پذیر است</strong>.
        </li>
        <li><strong>اعتبار {{ \neg F_1 }} :</strong>
          <br/>تحت تعبیر {{ I_1 }} بالا داریم:
          <div style="margin:6px 0;" dir="ltr">
            {{ [\neg F_1]^{I_1} = 1 - [F_1]^{I_1} = 1 - 1 = 0 }}
          </div>
          بنابراین {{ I_1 }} یک پادمدل برای {{ \neg F_1 }} است. <strong>فرمول {{ \neg F_1 }} معتبر نیست</strong>.
        </li>
      </ul>
      <p><strong>جمع‌بندی امتحانی:</strong> هر دو فرمول {{ F_1 }} و {{ \neg F_1 }} <strong>صدق‌پذیر اما غیرمعتبر</strong> هستند (گزاره‌های محتمل / ممکن الوقوع).</p>
    </div>
  </details>
</div>

<!-- Q4.2 -->
<div class="q-card" id="td2_q4_2">
  <div class="q-header">
    <span class="q-num">سوال ۲</span>
    <span class="q-title">بررسی فرمول‌های {{ F_3 = F_1 \lor F_2 }} و {{ F_4 = F_1 \land F_2 }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرض کنید {{ F_2 = (p \land q) \lor (\neg p \land \neg q) }} باشد. آیا فرمول‌های زیر صدق‌پذیر هستند؟ آیا معتبر هستند؟</p>
    <ul>
      <li>{{ F_3 = F_1 \lor F_2 }}</li>
      <li>{{ F_4 = F_1 \land F_2 }}</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>محاسبات دقیق جبر بولی</summary>
    <div class="box method">
      <h4>۱. بررسی فرمول {{ F_3 = F_1 \lor F_2 }}</h4>
      <p>تحت یک تعبیر دلخواه {{ I }}، با قرار دادن {{ x = I(p) }} و {{ y = I(q) }} عبارت را ساده می‌کنیم:</p>
      <div style="line-height:2em; font-size:1.05em;" dir="ltr">
        {{ [F_3]^I = [F_1]^I + [F_2]^I }}<br/>
        {{ = (x \cdot \overline{y} + \overline{x} \cdot y) + (x \cdot y + \overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot \overline{y} + x \cdot y) + (\overline{x} \cdot y + \overline{x} \cdot \overline{y}) }} \quad <em>(خاصیت جابجایی و شرکت‌پذیری)</em><br/>
        {{ = x \cdot (\overline{y} + y) + \overline{x} \cdot (y + \overline{y}) }} \quad <em>(خاصیت توزیع‌پذیری)</em><br/>
        {{ = x \cdot 1 + \overline{x} \cdot 1 }} \quad <em>(قانون متمم)</em><br/>
        {{ = x + \overline{x} = 1 }} \quad <em>(متمم نهایی)</em>
      </div>
      <p>از آنجا که مقدار {{ [F_3]^I = 1 }} برای هر تعبیر ممکن {{ I }} برقرار است، <strong>فرمول {{ F_3 }} معتبر (توتولوژی) است</strong> (و بالطبع صدق‌پذیر نیز هست).</p>

      <h4>۲. بررسی فرمول {{ F_4 = F_1 \land F_2 }}</h4>
      <p>ارزش {{ [F_4]^I = [F_1]^I \cdot [F_2]^I }} را تحت تعبیر اختیاری {{ I }} حساب می‌کنیم:</p>
      <div style="line-height:2em; font-size:1.05em;" dir="ltr">
        {{ [F_4]^I = (x \cdot \overline{y} + \overline{x} \cdot y) \cdot (x \cdot y + \overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot \overline{y}) \cdot (x \cdot y) + (x \cdot \overline{y}) \cdot (\overline{x} \cdot \overline{y}) + (\overline{x} \cdot y) \cdot (x \cdot y) + (\overline{x} \cdot y) \cdot (\overline{x} \cdot \overline{y}) }}<br/>
        {{ = (x \cdot x) \cdot (\overline{y} \cdot y) + (x \cdot \overline{x}) \cdot (\overline{y} \cdot \overline{y}) + (\overline{x} \cdot x) \cdot (y \cdot y) + (\overline{x} \cdot \overline{x}) \cdot (y \cdot \overline{y}) }}<br/>
        {{ = x \cdot 0 + 0 \cdot \overline{y} + 0 \cdot y + \overline{x} \cdot 0 = 0 + 0 + 0 + 0 = 0 }}
      </div>
      <p>از آنجا که مقدار {{ [F_4]^I = 0 }} برای هر تعبیر ممکن {{ I }} برقرار است، <strong>فرمول {{ F_4 }} ناسازگار (تناقض) است</strong> (و در نتیجه معتبر نیست).</p>
    </div>
  </details>
</div>

<!-- EXERCICE 5 -->
<h2 id="td2_ex5">Exercice 5 – Conséquence sémantique formelle</h2>

<div class="q-card" id="td2_ex5_all">
  <div class="q-header">
    <span class="q-num">تمرین ۵</span>
    <span class="q-title">تحلیل نظری استلزام با فرمول ناسازگار {{ F }} و محتمل {{ G }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرض کنید {{ F }} یک فرمول ناسازگار (تناقض) و {{ G }} یک فرمول نه معتبر و نه ناسازگار (یعنی گزاره محتمل) باشد. مشخص کنید و توجیه نمایید:</p>
    <ul>
      <li>(الف) آیا رابطه {{ F \models G }} برقرار است؟</li>
      <li>(ب) آیا رابطه {{ G \models F }} برقرار است؟</li>
      <li>(ج) آیا رابطه {{ \neg F \models G }} برقرار است؟</li>
      <li>(د) آیا رابطه {{ G \models \neg F }} برقرار است؟</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی همراه با برهان‌های ریاضی</summary>
    <div class="box method">
      <h4>(الف) آیا {{ F \models G }} برقرار است؟ &larr; بله</h4>
      <p><strong>توجیه صوری:</strong> بنا بر تعریف، {{ F \models G }} بدان معناست که به ازای هر تعبیر دلخواه {{ I }}، اگر {{ [F]^I = 1 }} باشد، آنگاه {{ [G]^I = 1 }} است.</p>
      <p>اما فرمول {{ F }} ناسازگار است، یعنی <em>هیچ تعبیری</em> {{ I }} وجود ندارد که در آن {{ [F]^I = 1 }} شود. بنابراین این گزاره شرطی به صورت انتزاعی به دلیل انتفای مقدم همواره درست است (اصل انفجار منطقی: از باطل هر نتیجه‌ای حاصل می‌شود). بنابراین {{ F \models G }} برقرار است.</p>

      <h4>(ب) آیا {{ G \models F }} برقرار است؟ &larr; خیر</h4>
      <p><strong>توجیه با پادمدل:</strong> بنا بر فرض مسئله، {{ G }} صدق‌پذیر است، پس حداقل یک تعبیر {{ I_1 }} وجود دارد که در آن {{ [G]^{I_1} = 1 }} باشد.</p>
      <p>اما چون {{ F }} ناسازگار است، در این تعبیر الزاماً {{ [F]^{I_1} = 0 }} خواهد بود. تعبیر {{ I_1 }} فرض را برآورده می‌کند ({{ [G]^{I_1} = 1 }}) ولی نتیجه را نقض می‌نماید ({{ [F]^{I_1} = 0 }}). تعبیر {{ I_1 }} یک <strong>پادمدل صریح</strong> است؛ بنابراین {{ G 
ot\models F }}.</p>

      <h4>(ج) آیا {{ \neg F \models G }} برقرار است؟ &larr; خیر</h4>
      <p><strong>توجیه با پادمدل:</strong> از آنجا که {{ F }} ناسازگار است، نقیض آن {{ \neg F }} <strong>معتبر (توتولوژی)</strong> است (برای هر {{ I }}، {{ [\neg F]^I = 1 - 0 = 1 }}).</p>
      <p>از طرفی چون {{ G }} معتبر نیست، حداقل یک تعبیر {{ I_0 }} وجود دارد که در آن {{ [G]^{I_0} = 0 }} باشد. برای این تعبیر {{ I_0 }}، داریم {{ [\neg F]^{I_0} = 1 }} و {{ [G]^{I_0} = 0 }}. تعبیر {{ I_0 }} یک پادمدل است و رابطه {{ \neg F \not\models G }} نقض می‌شود.</p>

      <h4>(د) آیا {{ G \models \neg F }} برقرار است؟ &larr; بله</h4>
      <p><strong>توجیه صوری:</strong> همان‌طور که در بخش (ج) اثبات شد، فرمول {{ \neg F }} یک فرمول <strong>معتبر</strong> است، یعنی تحت <em>تمام</em> تعبیرهای ممکن {{ I }}، همواره {{ [\neg F]^I = 1 }} است.</p>
      <p>بنابراین تحت هر تعبیری {{ I }} که {{ G }} صادق باشد ({{ [G]^I = 1 }})، مقدار {{ [\neg F]^I = 1 }} حاصل می‌شود. در نتیجه {{ G \models \neg F }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 6 -->
<h2 id="td2_ex6">Exercice 6 – Équivalence logique et propriétés d'absorption</h2>

<div class="q-card" id="td2_ex6_all">
  <div class="q-header">
    <span class="q-num">تمرین ۶</span>
    <span class="q-title">اثبات‌های صوری هم‌ارزی با فرمول‌های معتبر و ناسازگار</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرض کنید {{ F_1 }} و {{ F_2 }} دو فرمول دلخواه در منطق گزاره‌ای باشند.</p>
    <ol>
      <li>نشان دهید اگر {{ F_1 }} معتبر باشد، آنگاه {{ F_1 \land F_2 \equiv F_2 }} است.</li>
      <li>نشان دهید اگر {{ F_1 }} ناسازگار باشد، آنگاه {{ F_1 \lor F_2 \equiv F_2 }} است.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>برهان‌های جبری صوری برگه امتحان</summary>
    <div class="box method">
      <h4>۱. اثبات: اگر {{ F_1 }} معتبر باشد، آنگاه {{ F_1 \land F_2 \equiv F_2 }}</h4>
      <p>تعبیر دلخواه {{ I }} را در نظر می‌گیریم. بنا بر فرض، فرمول {{ F_1 }} معتبر است، پس {{ [F_1]^I = 1 }}.</p>
      <p>ارزش درستی عطف {{ F_1 \land F_2 }} را تحت {{ I }} محاسبه می‌کنیم:</p>
      <div style="margin:6px 0;" dir="ltr">
        {{ [F_1 \land F_2]^I = [F_1]^I \cdot [F_2]^I = 1 \cdot [F_2]^I = [F_2]^I }} \quad <em>(عدد ۱ عنصر همانی عمل ضرب است)</em>
      </div>
      <p>از آنجا که تساوی {{ [F_1 \land F_2]^I = [F_2]^I }} برای <strong>هر تعبیر اختیاری {{ I }}</strong> برقرار است، بنا بر تعریف هم‌ارزی نتیجه می‌گیریم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_1 \land F_2 \equiv F_2 }}</p>

      <h4>۲. اثبات: اگر {{ F_1 }} ناسازگار باشد، آنگاه {{ F_1 \lor F_2 \equiv F_2 }}</h4>
      <p>تعبیر دلخواه {{ I }} را در نظر می‌گیریم. بنا بر فرض، فرمول {{ F_1 }} ناسازگار است، پس {{ [F_1]^I = 0 }}.</p>
      <p>ارزش درستی فصل {{ F_1 \lor F_2 }} را تحت {{ I }} محاسبه می‌کنیم:</p>
      <div style="margin:6px 0;" dir="ltr">
        {{ [F_1 \lor F_2]^I = [F_1]^I + [F_2]^I = 0 + [F_2]^I = [F_2]^I }} \quad <em>(عدد ۰ عنصر همانی عمل جمع است)</em>
      </div>
      <p>از آنجا که تساوی {{ [F_1 \lor F_2]^I = [F_2]^I }} برای <strong>هر تعبیر اختیاری {{ I }}</strong> برقرار است، بنا بر تعریف هم‌ارزی نتیجه می‌گیریم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_1 \lor F_2 \equiv F_2 }}</p>
    </div>
  </details>
</div>

<!-- EXERCICE 7 -->
<h2 id="td2_ex7">Exercice 7 – Expressions booléennes et résolution équationnelle d'énigme</h2>

<div class="q-card" id="td2_q7_1">
  <div class="q-header">
    <span class="q-num">سوال ۱</span>
    <span class="q-title">ساده‌سازی جبری عبارت {{ [F]^I }}</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرمول {{ F = (p \land q) \land ((q \Rightarrow p) \lor \neg(p \lor q)) }} که در آن {{ p }} و {{ q }} گزاره هستند را در نظر بگیرید. عبارت بولی {{ [F]^I }} را بر حسب {{ I(p) }} و {{ I(q) }} محاسبه کرده و با ذکر نام قاعده جبری در هر گام ساده کنید.</p>
  </div>

  <details class="sol" open>
    <summary>محاسبه گام‌به‌گام با نام قواعد</summary>
    <div class="box method">
      <p>برای اختصار می‌نویسیم {{ x = I(p) }} و {{ y = I(q) }}. عبارت {{ [F]^I }} را باز می‌کنیم:</p>
      <div style="line-height:2.2em; font-size:1.05em;" dir="ltr">
        {{ [F]^I = [p \land q]^I \cdot [(q \Rightarrow p) \lor \neg(p \lor q)]^I }}<br/>
        {{ = (x \cdot y) \cdot ( [q \Rightarrow p]^I + [\neg(p \lor q)]^I ) }}<br/>
        {{ = (x \cdot y) \cdot ( (\overline{y} + x) + \overline{x + y} ) }} \quad <em>(تعریف شرطی و نقیض)</em><br/>
        {{ \equiv (x \cdot y) \cdot ( (\overline{y} + x) + (\overline{x} \cdot \overline{y}) ) }} \quad <em>(قانون دمرگان روی {{ \overline{x + y} }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + (\overline{y} + \overline{x} \cdot \overline{y}) ) }} \quad <em>(جابجایی و شرکت‌پذیری)</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} \cdot (1 + \overline{x}) ) }} \quad <em>(فاکتورگیری از {{ \overline{y} }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} \cdot 1 ) }} \quad <em>(عنصر جاذب : {{ 1 + \overline{x} = 1 }})</em><br/>
        {{ \equiv (x \cdot y) \cdot ( x + \overline{y} ) }} \quad <em>(عنصر همانی ضرب {{ \cdot }})</em><br/>
        {{ \equiv (x \cdot y) \cdot x + (x \cdot y) \cdot \overline{y} }} \quad <em>(توزیع‌پذیری {{ \cdot }} روی {{ + }})</em><br/>
        {{ \equiv (x \cdot x) \cdot y + x \cdot (y \cdot \overline{y}) }} \quad <em>(شرکت‌پذیری و جابجایی)</em><br/>
        {{ \equiv x \cdot y + x \cdot 0 }} \quad <em>(بت‌خواری {{ x \cdot x = x }} و متمم {{ y \cdot \overline{y} = 0 }})</em><br/>
        {{ \equiv x \cdot y + 0 }} \quad <em>(پوچ‌سازی : {{ x \cdot 0 = 0 }})</em><br/>
        {{ \equiv x \cdot y }} \quad <em>(عنصر همانی جمع : {{ a + 0 = a }})</em>
      </div>
      <p><strong>نتیجه نهایی:</strong> {{ [F]^I = I(p) \cdot I(q) }}. فرمول {{ F }} از دیدگاه جبری کاملاً با عطف ساده {{ p \land q }} هم‌ارز است.</p>
    </div>
  </details>
</div>

<div class="q-card" id="td2_q7_2">
  <div class="q-header">
    <span class="q-num">سوال ۲</span>
    <span class="q-title">حل معادلاتی معمای انیسا، خاویر و جنیفر</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>معمای هفته گذشته را با استدلال معادلاتی بررسی می‌کنیم: {{ H_1 }}: حداقل یکی درس می‌خواند؛ {{ H_2 }}: اگر انیسا نخواند، خاویر هم نمی‌خواند؛ {{ H_3 }}: اگر انیسا بخواند، جنیفر هم می‌خواند.</p>
    <p>با تعریف گزاره‌های {{ A }}، {{ X }} و {{ J }}، با <strong>استدلال معادلاتی</strong> نشان دهید چه کسی قطعاً درس می‌خواند.</p>
  </div>

  <details class="sol" open>
    <summary>اثبات جبری کامل</summary>
    <div class="box method">
      <h4>۱. فرمول‌بندی جبری مسئله</h4>
      <p>در هر تعبیر دلخواه {{ I }} که هر سه فرض را برآورده کند، حاصل‌ضرب مقادیر آن‌ها برابر ۱ است:</p>
      <div style="margin:8px 0; font-size:1.1em;" dir="ltr">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = 1 }}
      </div>
      <p>با تعریف متغیرهای {{ a = I(A), x = I(X), j = I(J) }} داریم:</p>
      <ul>
        <li>{{ [H_1]^I = a + x + j }}</li>
        <li>{{ [H_2]^I = [\neg A \Rightarrow \neg X]^I = \overline{\overline{a}} + \overline{x} = a + \overline{x} }}</li>
        <li>{{ [H_3]^I = [A \Rightarrow J]^I = \overline{a} + j }}</li>
      </ul>

      <h4>۲. محاسبات جبری ضرب عبارات</h4>
      <p>ابتدا عبارت {{ [H_2]^I \cdot [H_3]^I }} را محاسبه می‌کنیم:</p>
      <div style="line-height:2em;" dir="ltr">
        {{ (a + \overline{x}) \cdot (\overline{a} + j) = a \cdot \overline{a} + a \cdot j + \overline{x} \cdot \overline{a} + \overline{x} \cdot j }}<br/>
        {{ = 0 + a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j = a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j }}
      </div>
      <p>سپس در عبارت {{ [H_1]^I = a + x + j }} ضرب می‌کنیم:</p>
      <div style="line-height:2em;" dir="ltr">
        {{ (a + x + j) \cdot (a \cdot j + \overline{a} \cdot \overline{x} + \overline{x} \cdot j) }}<br/>
        {{ = a \cdot (a \cdot j) + a \cdot (\overline{a} \cdot \overline{x}) + a \cdot (\overline{x} \cdot j) + x \cdot (a \cdot j) + x \cdot (\overline{a} \cdot \overline{x}) + x \cdot (\overline{x} \cdot j) + j \cdot (a \cdot j) + j \cdot (\overline{a} \cdot \overline{x}) + j \cdot (\overline{x} \cdot j) }}
      </div>
      <p>ساده‌سازی تک‌تک جملات حاصل‌ضرب:</p>
      <ul>
        <li>{{ a \cdot a \cdot j = a \cdot j }}</li>
        <li>{{ a \cdot \overline{a} \cdot \overline{x} = 0 }}</li>
        <li>{{ a \cdot \overline{x} \cdot j }}</li>
        <li>{{ x \cdot a \cdot j = a \cdot x \cdot j }}</li>
        <li>{{ x \cdot \overline{a} \cdot \overline{x} = 0 }}</li>
        <li>{{ x \cdot \overline{x} \cdot j = 0 }}</li>
        <li>{{ j \cdot a \cdot j = a \cdot j }}</li>
        <li>{{ j \cdot \overline{a} \cdot \overline{x} = \overline{a} \cdot \overline{x} \cdot j }}</li>
        <li>{{ j \cdot \overline{x} \cdot j = \overline{x} \cdot j }}</li>
      </ul>
      <p>عبارت حاصل برابر است با:</p>
      <div style="margin:8px 0; font-size:1.05em;" dir="ltr">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = a \cdot j + a \cdot \overline{x} \cdot j + a \cdot x \cdot j + \overline{a} \cdot \overline{x} \cdot j + \overline{x} \cdot j }}
      </div>
      <p>از متغیر {{ j }} (که در <strong>تمامی</strong> جملات باقی‌مانده تکرار شده است) فاکتور می‌گیریم:</p>
      <div style="margin:8px 0; font-size:1.1em; font-weight:bold;" dir="ltr">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = j \cdot ( a + a \cdot \overline{x} + a \cdot x + \overline{a} \cdot \overline{x} + \overline{x} ) }}
      </div>
      <p>طبق قانون جذب، چون {{ a + a \cdot \overline{x} + a \cdot x = a }} و {{ \overline{x} + \overline{a} \cdot \overline{x} = \overline{x} }}، جملات ساده شده و حاصل نهایی به دست می‌آید:</p>
      <div style="margin:8px 0; font-size:1.15em; font-weight:bold; text-align:center;" dir="ltr">
        {{ [H_1]^I \cdot [H_2]^I \cdot [H_3]^I = j \cdot (a + \overline{x}) }}
      </div>

      <h4>۳. نتیجه‌گیری صوری نهایی</h4>
      <p>برای این‌که حاصل‌ضرب فوق برابر با ۱ شود، <strong>اجباراً باید {{ j = 1 }} باشد</strong> (زیرا اگر {{ j = 0 }} باشد حاصل‌ضرب در هر صورت صفر خواهد بود). در مقابل، جمله دوم {{ (a + \overline{x}) }} هم با {{ a = 1 }} و هم با {{ x = 0 }} می‌تواند یک شود.</p>
      <p><strong>پاسخ نهایی برگه آزمون:</strong></p>
      <ul>
        <li><strong>جنیفر با قطعیت ۱۰۰٪ درس خواهد خواند</strong> ({{ I(J) = 1 }}).</li>
        <li>درباره انیسا و خاویر هیچ حکم قطعی و یقینی بدون مفروضات اضافی نمی‌توان داد.</li>
      </ul>
    </div>
  </details>
</div>

<!-- EXERCICE 8 -->
<h2 id="td2_ex8">Exercice 8 – Analyse critique : faut-il toujours croire ChatGPT ?</h2>

<div class="q-card" id="td2_q8_1">
  <div class="q-header">
    <span class="q-num">سوال ۱</span>
    <span class="q-title">رد ادعای چت‌جی‌پی‌تی در ژوئن ۲۰۲۵</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>در پاسخ به درخواست «فرمول معادل {{ A \land B }} ولی پیچیده‌تر»، ChatGPT فرمول {{ G = \neg((A \Rightarrow \neg B) \lor (\neg A \Rightarrow B)) }} را معادل {{ F = A \land B }} اعلام کرده است.</p>
    <ol>
      <li>با محاسبه {{ [F]^I }} و {{ [G]^I }} نشان دهید این پاسخ نادرست است.</li>
      <li>خطای بنیادین استدلال ChatGPT را مشخص کنید.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>رد جبری ادعا و ریشه‌یابی خطا</summary>
    <div class="box method">
      <h4>۱. محاسبه جبری {{ [F]^I }} و {{ [G]^I }}</h4>
      <p>با تعریف {{ a = I(A) }} و {{ b = I(B) }}، ارزش {{ [F]^I = a \cdot b }} است.</p>
      <p>ارزش {{ [G]^I }} را ساده می‌کنیم:</p>
      <div style="line-height:2em; font-size:1.05em;" dir="ltr">
        {{ [G]^I = \overline{ [A \Rightarrow \neg B]^I + [\neg A \Rightarrow B]^I } }}<br/>
        {{ = \overline{ (\overline{a} + \overline{b}) + (\overline{\overline{a}} + b) } }}<br/>
        {{ = \overline{ \overline{a} + \overline{b} + a + b } }}<br/>
        {{ = \overline{ (a + \overline{a}) + (b + \overline{b}) } }} \quad <em>(خاصیت جابجایی و شرکت‌پذیری)</em><br/>
        {{ = \overline{ 1 + 1 } = \overline{1} = 0 }}
      </div>
      <p>مشاهده می‌کنیم که تحت <strong>هر</strong> تعبیر دلخواه {{ I }}، همواره {{ [G]^I = 0 }} است. یعنی فرمول {{ G }} یک <strong>تناقض مطلق (ناسازگار)</strong> است!</p>
      <p>اکنون تعبیر {{ I_1 }} با مقادیر {{ I_1(A) = 1 }} و {{ I_1(B) = 1 }} را در نظر بگیرید:</p>
      <ul>
        <li>{{ [F]^{I_1} = 1 \cdot 1 = 1 }}</li>
        <li>{{ [G]^{I_1} = 0 }}</li>
      </ul>
      <p>چون در این تعبیر {{ [F]^{I_1} \neq [G]^{I_1} }} است، دو فرمول {{ F }} و {{ G }} به هیچ وجه <strong>هم‌ارز نیستند</strong> و پاسخ هوش مصنوعی مردود است.</p>

      <h4>۲. منشأ خطای استدلال هوش مصنوعی</h4>
      <p>هوش مصنوعی ادعا کرده بود نفی این عبارت دو گزاره را مجبور به درستی هم‌زمان می‌کند. اما در حقیقت عبارت فصلی {{ (A \Rightarrow \neg B) \lor (\neg A \Rightarrow B) }} یک <strong>توتولوژی محض</strong> بوده که فارغ از ارزش حقیقت گزاره‌های {{ A }} و {{ B }} در تمام جهان‌ها درست است. نقیض یک توتولوژی، فرمول <strong>همواره نادرست (ناسازگار)</strong> است، نه عطف {{ A \land B }} !</p>
    </div>
  </details>
</div>

<div class="q-card" id="td2_q8_2">
  <div class="q-header">
    <span class="q-num">سوال ۲</span>
    <span class="q-title">بررسی دو فرمول با متغیر کمکی ارائه‌شده در ژوئیه ۲۰۲۶</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>در ژوئیه ۲۰۲۶، چت‌جی‌پی‌تی این دو فرمول را پیشنهاد می‌کند:</p>
    <ul>
      <li>{{ F = (A \lor C) \land (B \lor \neg C) \land (A \lor \neg C) }}</li>
      <li>{{ G = (A \lor C) \land (A \lor \neg C) \land (B \lor C) \land (B \lor \neg C) }}</li>
    </ul>
    <p>نشان دهید یکی از این دو فرمول دقیقاً هم‌ارز {{ A \land B }} است ولی دیگری هم‌ارز نیست.</p>
  </div>

  <details class="sol" open>
    <summary>برهان تطبیقی جبری</summary>
    <div class="box method">
      <h4>۱. بررسی فرمول {{ G }}</h4>
      <p>جملات عطفی فرمول {{ G }} را دوبه‌دو دسته‌بندی می‌کنیم:</p>
      <ul>
        <li>دسته اول: {{ (A \lor C) \land (A \lor \neg C) }}
          <br/>با توزیع‌پذیری {{ \lor }} بر روی {{ \land }} داریم:
          {{ (A \lor C) \land (A \lor \neg C) \equiv A \lor (C \land \neg C) \equiv A \lor 0 \equiv A }}.
        </li>
        <li>دسته دوم: {{ (B \lor C) \land (B \lor \neg C) }}
          <br/>به همین ترتیب:
          {{ (B \lor C) \land (B \lor \neg C) \equiv B \lor (C \land \neg C) \equiv B \lor 0 \equiv B }}.
        </li>
      </ul>
      <p>با ترکیب دوباره دو دسته به دست می‌آید:</p>
      <div style="margin:6px 0; font-size:1.1em; font-weight:bold;" dir="ltr">
        {{ G \equiv A \land B }}
      </div>
      <p>بنابراین فرمول {{ G }} <strong>دقیقاً هم‌ارز منطقی {{ A \land B }} است</strong>.</p>

      <h4>۲. بررسی فرمول {{ F }}</h4>
      <p>با ترکیب عبارت اول و سوم فرمول {{ F }} داریم:</p>
      <div style="margin:6px 0;" dir="ltr">
        {{ (A \lor C) \land (A \lor \neg C) \equiv A \lor (C \land \neg C) \equiv A }}
      </div>
      <p>بنابراین فرمول {{ F }} به عبارت زیر خلاصه می‌شود:</p>
      <div style="margin:6px 0; font-size:1.1em; font-weight:bold;" dir="ltr">
        {{ F \equiv A \land (B \lor \neg C) }}
      </div>
      <p>آیا این عبارت با {{ A \land B }} هم‌ارز است؟ <strong>خیر!</strong> با یک پادمدل صریح آن را رد می‌کنیم:</p>
      <p>تعبیر {{ I_c }} را به صورت زیر برمی‌گزینیم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ I_c(A) = 1, \quad I_c(B) = 0, \quad I_c(C) = 0 }}</p>
      <ul>
        <li>ارزش {{ A \land B }} : {{ [A \land B]^{I_c} = 1 \cdot 0 = 0 }}.</li>
        <li>ارزش {{ F }} : {{ [F]^{I_c} = [A]^{I_c} \cdot ([B]^{I_c} + \overline{[C]^{I_c}}) = 1 \cdot (0 + 1) = 1 \cdot 1 = 1 }}.</li>
      </ul>
      <p>از آنجا که {{ [F]^{I_c} = 1 \neq [A \land B]^{I_c} = 0 }}، تعبیر {{ I_c }} یک پادمدل صریح است که ثابت می‌کند <strong>فرمول {{ F }} با {{ A \land B }} هم‌ارز نیست</strong>.</p>
    </div>
  </details>
</div>
"""

open(os.path.join(W02, 'td.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W02, 'td.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("td.fr.html and td.fa.html written.")
