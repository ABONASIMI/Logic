#!/usr/bin/env python3
"""Generator for Week 5 (w05) of Logic Academy:
Déduction Naturelle Propositionnelle Intuitionniste (Thème 5).
Generates cours, td, tp, annales, revision in both FR and FA with strict parity.
"""
import os, json, re

W05 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w05'
os.makedirs(W05, exist_ok=True)

# ==============================================================================
# 1. COURS (FR & FA)
# ==============================================================================

cours_fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>Thème 5 : Déduction Naturelle Propositionnelle (Logique Intuitionniste)</h1>
  <p class="lead">Système de déduction formelle de Gentzen, emboîtement de boîtes de la Sorbonne, cycle de vie et décharge des hypothèses, règles d'introduction et d'élimination des connecteurs et stratégies de preuve constructives.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du cours</h3>
  <ul>
    <li><a href="#sec1">1. Des tables de vérité aux systèmes de déduction formelle (Gentzen, 1934)</a></li>
    <li><a href="#sec2">2. Emboîtement de boîtes, axiome et constantes logiques</a></li>
    <li><a href="#sec3">3. Règles d'Introduction (I) et d'Élimination (E) des connecteurs</a></li>
    <li><a href="#sec4">4. Stratégies de preuve : raisonnement descendant (but) vs ascendant (hypothèses)</a></li>
    <li><a href="#sec5">5. Pourquoi {{ I_\neg }} est intuitionniste alors que {{ \text{Abs} }} est classique ?</a></li>
    <li><a href="#sec6">6. Laboratoire interactif de vérification de séquents</a></li>
  </ul>
</div>

<h2 id="sec1">1. Des tables de vérité aux systèmes de déduction formelle (Gentzen, 1934)</h2>

<div class="box info">
  <h4>Pourquoi construire un système de preuve purement syntaxique ?</h4>
  <p>Dans les Thèmes 1 à 4, nous avons étudié la <strong>sémantique</strong> : une formule {{ F }} est valide ({{ \models F }}) si {{ [F]^I = 1 }} pour toute interprétation {{ I }}. Mais dès que l'on passera à la logique des prédicats du premier ordre (Thèmes 7 à 9), les domaines d'interprétation deviendront <strong>infinis</strong> (comme {{ \mathbb{N} }} ou {{ \mathbb{R} }}), rendant impossible l'énumération des modèles.</p>
  <p>Un <strong>système de déduction</strong> (introduit par Gerhard Gentzen en 1934 avec la <em>Déduction Naturelle</em>) caractérise les formules valides de manière purement <strong>syntaxique</strong>, à l'aide de règles de raisonnement élémentaires qui manipulent la structure des formules sans jamais calculer de valeurs booléennes {{ 0 }} ou {{ 1 }}.</p>
</div>

<div class="box def">
  <h4>Séquent (jugement de déductibilité) {{ \Gamma \vdash F }}</h4>
  <p>Une étape de preuve établit un <strong>jugement</strong> (ou <em>séquent</em>) noté :</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;">{{ h_1 : F_1, \, h_2 : F_2, \, \dots, \, h_n : F_n \vdash F }}</p>
  <ul>
    <li>La partie gauche {{ \Gamma = \{h_1 : F_1, \dots, h_n : F_n\} }} représente l'ensemble des <strong>hypothèses actives</strong> (le contexte courant).</li>
    <li>La formule {{ F }} à droite du symbole {{ \vdash }} (qui se lit <em>« prouve »</em> ou <em>« démontre »</em>) est le <strong>but</strong> (la conclusion à établir).</li>
    <li>Lorsque {{ \Gamma = \emptyset }}, on écrit {{ \vdash F }} : la formule {{ F }} est prouvable sans aucune hypothèse préalable, on dit que {{ F }} est un <strong>théorème</strong>.</li>
    <li><strong>Théorème de correction et complétude :</strong> Une formule est prouvable ({{ \Gamma \vdash F }}) dans le système de déduction classique si et seulement si elle est conséquence sémantique ({{ \Gamma \models F }}).</li>
  </ul>
</div>

<h2 id="sec2">2. Emboîtement de boîtes, axiome et constantes logiques</h2>

<div class="box method">
  <h4>Le formalisme des boîtes numérotées de la Sorbonne (Cours 4, Slides 7 à 11)</h4>
  <p>À Sorbonne Université, une preuve en déduction naturelle s'écrit sous forme d'un <strong>emboîtement de boîtes numérotées</strong> délimitées par des chevrons {{ \langle i \rangle \dots \langle i \rangle }} (équivalent exact des boîtes verticales de Fitch) :</p>
  <pre><code>⟨i⟩ supposons h1 : F1, h2 : F2, ..., hn : Fn
    montrons F par Nom_Règle
    ⟨i+1⟩ ... sous-preuve 1 ... ⟨i+1⟩
    ⟨i+2⟩ ... sous-preuve 2 ... ⟨i+2⟩
⟨i⟩</code></pre>
  <p><strong>Règle de portée (cycle de vie d'une hypothèse) :</strong></p>
  <ul>
    <li>Une hypothèse {{ h : A }} introduite en tête d'une boîte {{ \langle j \rangle }} est <strong>active et utilisable</strong> dans toute la boîte {{ \langle j \rangle }} ainsi que dans toutes ses sous-boîtes {{ \langle i \rangle }} emboîtées à l'intérieur de {{ \langle j \rangle }}.</li>
    <li>Dès que la boîte {{ \langle j \rangle }} se referme, l'hypothèse {{ h : A }} est <strong>déchargée</strong> (désactivée) : il est strictement interdit d'invoquer {{ h }} en dehors de {{ \langle j \rangle }} !</li>
  </ul>
</div>

<div class="box def">
  <h4>Règle d'Axiome ({{ \text{Ax} }}) et règles des constantes {{ \text{true} }} ({{ \top }}) et {{ \text{false} }} ({{ \bot }})</h4>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>Nom de la règle</th>
        <th>Schéma de Gentzen</th>
        <th>Écriture en boîtes Sorbonne</th>
        <th>Explication</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Axiome ({{ \text{Ax} }})</strong></td>
        <td>{{ \Gamma, h : A \vdash A }}</td>
        <td><code>⟨i⟩ supposons ..., h : A</code><br/><code>    montrons A par Ax avec h</code><br/><code>⟨i⟩</code></td>
        <td>Si le but {{ A }} figure déjà parmi les hypothèses actives (dans la boîte courante ou une boîte englobante), la preuve est immédiate.</td>
      </tr>
      <tr>
        <td><strong>Introduction de true ({{ I_\top }})</strong></td>
        <td>{{ \Gamma \vdash \text{true} }}</td>
        <td><code>⟨i⟩ montrons true par I⊤ ⟨i⟩</code></td>
        <td>La constante {{ \text{true} }} est toujours prouvable immédiatement. Elle n'a <strong>aucune règle d'élimination</strong> (on ne déduit rien d'utile de {{ h : \text{true} }}).</td>
      </tr>
      <tr>
        <td><strong>Élimination de false ({{ E_\bot }})</strong><br/><em>(Ex falso quodlibet)</em></td>
        <td>{{ \frac{\Gamma \vdash \text{false}}{\Gamma \vdash B} }}</td>
        <td><code>⟨i⟩ supposons ..., h : false</code><br/><code>    montrons B par E⊥ avec h</code><br/><code>⟨i⟩</code></td>
        <td><strong>Principe d'explosion intuitionniste :</strong> d'une contradiction {{ \text{false} }} ({{ \bot }}), on peut déduire <em>n'importe quelle formule {{ B }}</em> ! La constante {{ \text{false} }} n'a <strong>aucune règle d'introduction</strong>.</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec3">3. Règles d'Introduction (I) et d'Élimination (E) des connecteurs</h2>

<div class="box info">
  <h4>Philosophie générale : Introduction vs Élimination (Cours 4, Slide 12)</h4>
  <ul>
    <li><strong>Règles d'Introduction ({{ I }}) :</strong> Elles indiquent comment <em>construire une preuve</em> d'une formule dont le connecteur principal (la racine de l'arbre syntaxique) est {{ \Rightarrow, \land, \lor, \neg }} ou {{ \Leftrightarrow }}.</li>
    <li><strong>Règles d'Élimination ({{ E }}) :</strong> Elles indiquent comment <em>exploiter (décomposer) une hypothèse ou une formule déjà prouvée</em> dont le connecteur principal est {{ \Rightarrow, \land, \lor, \neg }} ou {{ \Leftrightarrow }}.</li>
  </ul>
</div>

<div class="box def">
  <h4>Catalogue officiel des règles de la Déduction Naturelle Intuitionniste (Sorbonne)</h4>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>Connecteur</th>
        <th>Règle d'Introduction ({{ I }})</th>
        <th>Règle d'Élimination ({{ E }}) et Règle Dérivée directe ({{ D }})</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Implication ({{ \Rightarrow }})</strong></td>
        <td><strong>{{ I_\Rightarrow }} ({{ \Rightarrow I }}) :</strong> Pour prouver {{ A \Rightarrow B }}, on ouvre une sous-boîte où l'on suppose {{ h : A }} et l'on montre {{ B }}.<br/>
        <code>⟨i⟩ montrons A ⇒ B par I⇒</code><br/>
        <code>  ⟨i+1⟩ supposons h : A, montrons B ... ⟨i+1⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\Rightarrow }} ({{ \Rightarrow E }} / Modus Ponens) :</strong> Pour prouver {{ B }}, on montre {{ A \Rightarrow B }} dans une sous-boîte et {{ A }} dans une autre.<br/>
        <em>Raccourci formulaire {{ D_\Rightarrow }} :</em> si {{ h_1 : A \Rightarrow B }} et {{ h_2 : A }} sont en hypothèses, on conclut {{ B }} directement par <code>D⇒ avec h1, h2</code>.</td>
      </tr>
      <tr>
        <td><strong>Conjonction ({{ \land }})</strong></td>
        <td><strong>{{ I_\land }} ({{ \land I }}) :</strong> Pour prouver {{ A \land B }}, on ouvre deux sous-boîtes : l'une montrant {{ A }}, l'autre montrant {{ B }}.<br/>
        <code>⟨i⟩ montrons A ∧ B par I∧</code><br/>
        <code>  ⟨i+1⟩ montrons A ... ⟨i+1⟩</code><br/>
        <code>  ⟨i+2⟩ montrons B ... ⟨i+2⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\land^g }} ({{ \land E_1 }}) et {{ E_\land^d }} ({{ \land E_2 }}) :</strong> À partir d'une preuve de {{ A \land B }}, {{ E_\land^g }} extrait la branche gauche {{ A }}, et {{ E_\land^d }} extrait la branche droite {{ B }}.<br/>
        <em>Raccourci formulaire {{ D_\land^g }} / {{ D_\land^d }} :</em> si {{ h : A \land B }} est en hypothèse, <code>D∧g avec h</code> donne {{ A }} et <code>D∧d avec h</code> donne {{ B }}.</td>
      </tr>
      <tr>
        <td><strong>Disjonction ({{ \lor }})</strong></td>
        <td><strong>{{ I_\lor^g }} ({{ \lor I_1 }}) et {{ I_\lor^d }} ({{ \lor I_2 }}) :</strong> Pour prouver {{ A \lor B }}, il suffit soit de prouver {{ A }} (par {{ I_\lor^g }}), soit de prouver {{ B }} (par {{ I_\lor^d }}).<br/>
        <em>Attention :</em> il faut choisir le côté ({{ g }} ou {{ d }}) qui est effectivement démontrable sous les hypothèses actives !</td>
        <td><strong>{{ E_\lor }} ({{ \lor E }} / Raisonnement par cas) :</strong> Pour prouver un but {{ C }} à l'aide d'une disjonction {{ A \lor B }}, il faut <strong>3 sous-boîtes</strong> :<br/>
        1. Prouver {{ A \lor B }}<br/>
        2. Supposer {{ h_A : A }} et montrer {{ C }}<br/>
        3. Supposer {{ h_B : B }} et montrer {{ C }}<br/>
        <em>Raccourci {{ D_\lor }} :</em> si {{ h : A \lor B }} est déjà en hypothèse, seules les sous-boîtes 2 et 3 sont requises (<code>D∨ avec h</code>).</td>
      </tr>
      <tr>
        <td><strong>Négation ({{ \neg }})</strong></td>
        <td><strong>{{ I_\neg }} ({{ \neg I }}) :</strong> Pour prouver une négation {{ \neg A }}, on ouvre une sous-boîte où l'on suppose {{ h : A }} et l'on montre {{ \text{false} }} ({{ \bot }}).<br/>
        <code>⟨i⟩ montrons ¬A par I¬</code><br/>
        <code>  ⟨i+1⟩ supposons h : A, montrons false ... ⟨i+1⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\neg }} ({{ \neg E }}) :</strong> Pour prouver {{ \text{false} }} ({{ \bot }}), on montre {{ \neg A }} dans une sous-boîte et {{ A }} dans une autre.<br/>
        <em>Raccourci formulaire {{ D_\bot^1 }} :</em> si l'on possède deux hypothèses contradictoires {{ h_1 : A }} et {{ h_2 : \neg A }}, on peut prouver <strong>n'importe quel but {{ B }}</strong> en une ligne par <code>D⊥1 avec h1, h2</code> (combine {{ E_\neg }} et {{ E_\bot }}).</td>
      </tr>
      <tr>
        <td><strong>Équivalence ({{ \Leftrightarrow }})</strong></td>
        <td><strong>{{ I_\Leftrightarrow }} ({{ \Leftrightarrow I }}) :</strong> Pour prouver {{ A \Leftrightarrow B }}, on montre {{ A \Rightarrow B }} dans une première sous-boîte et {{ B \Rightarrow A }} dans une seconde.</td>
        <td><strong>{{ E_\Leftrightarrow^g }} et {{ E_\Leftrightarrow^d }} :</strong> De {{ A \Leftrightarrow B }}, on extrait {{ A \Rightarrow B }} (gauche) ou {{ B \Rightarrow A }} (droite).</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec4">4. Stratégies de preuve : raisonnement descendant (but) vs ascendant (hypothèses)</h2>

<div class="box method">
  <h4>Méthode infaillible pour construire une preuve sans jamais bloquer</h4>
  <ol>
    <li><strong>Étape 1 — Décomposer le but par les règles d'Introduction (analyse descendante) :</strong>
      <ul>
        <li>Si le but est {{ A \Rightarrow B }} : appliquez <strong>toujours immédiatement</strong> {{ I_\Rightarrow }} (<code>supposons h : A, montrons B</code>). Répétez tant que le but est une implication !</li>
        <li>Si le but est {{ A \land B }} : appliquez <strong>toujours immédiatement</strong> {{ I_\land }} pour séparer la preuve en deux sous-objectifs indépendants {{ A }} et {{ B }}.</li>
        <li>Si le but est {{ \neg A }} : appliquez <strong>toujours immédiatement</strong> {{ I_\neg }} (<code>supposons h : A, montrons false</code>).</li>
        <li>Si le but est {{ A \lor B }} : <em>prudence !</em> N'appliquez {{ I_\lor^g }} ou {{ I_\lor^d }} que si les hypothèses actuelles permettent déjà d'établir {{ A }} ou d'établir {{ B }}. Si ce n'est pas le cas, regardez d'abord vos hypothèses !</li>
      </ul>
    </li>
    <li><strong>Étape 2 — Exploiter les hypothèses par les règles d'Élimination (analyse ascendante) :</strong>
      <ul>
        <li>Si vous avez une hypothèse conjonctive {{ h : A \land B }} : vous disposez à la fois de {{ A }} ({{ E_\land^g }}) et de {{ B }} ({{ E_\land^d }}).</li>
        <li>Si vous avez une hypothèse disjonctive {{ h : A \lor B }} : utilisez <strong>systématiquement</strong> le raisonnement par cas {{ E_\lor }} (ou {{ D_\lor }}) pour découper votre preuve en deux branches : Cas 1 ({{ h_A : A }}) et Cas 2 ({{ h_B : B }}).</li>
        <li>Si vous avez {{ h_1 : A \Rightarrow B }} et {{ h_2 : A }} : déduisez {{ B }} par Modus Ponens ({{ E_\Rightarrow }} / {{ D_\Rightarrow }}).</li>
        <li>Si vous apercevez {{ A }} et {{ \neg A }} dans vos hypothèses actives : vous avez gagné ! Appliquez {{ E_\neg }} pour obtenir {{ \text{false} }}, puis {{ E_\bot }} (ou directement {{ D_\bot^1 }}) pour conclure n'importe quel but {{ C }}.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box tip">
  <h4>Exemple complet du cours (Cours 4, Slide 26) : Preuve de {{ \neg(A \lor B) \Rightarrow (\neg A \land \neg B) }}</h4>
  <p>Observons comment la structure de la formule guide mécaniquement chaque ligne de la preuve :</p>
  <pre><code>⟨1⟩ montrons ¬(A ∨ B) ⇒ (¬A ∧ ¬B) par I⇒
  ⟨2⟩ supposons h1 : ¬(A ∨ B), montrons ¬A ∧ ¬B par I∧
    ⟨3⟩ montrons ¬A par I¬
      ⟨4⟩ supposons h2 : A, montrons false par E¬
        ⟨5⟩ montrons ¬(A ∨ B) par Ax avec h1 ⟨5⟩
        ⟨6⟩ montrons A ∨ B par I∨g
          ⟨7⟩ montrons A par Ax avec h2 ⟨7⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
    ⟨8⟩ montrons ¬B par I¬
      ⟨9⟩ supposons h3 : B, montrons false par E¬
        ⟨10⟩ montrons ¬(A ∨ B) par Ax avec h1 ⟨10⟩
        ⟨11⟩ montrons A ∨ B par I∨d
          ⟨12⟩ montrons B par Ax avec h3 ⟨12⟩
        ⟨11⟩
      ⟨9⟩
    ⟨8⟩
  ⟨2⟩
⟨1⟩</code></pre>
  <p>En notation tabulaire de Fitch (ligne par ligne avec justifications), cette même dérivation s'écrit :</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr><th>Ligne</th><th>Contexte actif</th><th>Formule dérivée</th><th>Règle et justification</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>{{ h_1 }}</td><td>{{ \neg(A \lor B) }}</td><td>Hypothèse (ouverture de la boîte pour {{ I_\Rightarrow }})</td></tr>
      <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A }}</td><td>Hypothèse (ouverture de la sous-boîte pour {{ I_\neg }})</td></tr>
      <tr><td>3</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor B }}</td><td>{{ I_\lor^g }} sur la ligne 2</td></tr>
      <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 1 et 3</td></tr>
      <tr><td>5</td><td>{{ h_1 }}</td><td>{{ \neg A }}</td><td>{{ I_\neg }} (lignes 2 à 4, décharge de {{ h_2 }})</td></tr>
      <tr><td>6</td><td>{{ h_1, h_3 }}</td><td>{{ B }}</td><td>Hypothèse (ouverture de la sous-boîte pour {{ I_\neg }})</td></tr>
      <tr><td>7</td><td>{{ h_1, h_3 }}</td><td>{{ A \lor B }}</td><td>{{ I_\lor^d }} sur la ligne 6</td></tr>
      <tr><td>8</td><td>{{ h_1, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 1 et 7</td></tr>
      <tr><td>9</td><td>{{ h_1 }}</td><td>{{ \neg B }}</td><td>{{ I_\neg }} (lignes 6 à 8, décharge de {{ h_3 }})</td></tr>
      <tr><td>10</td><td>{{ h_1 }}</td><td>{{ \neg A \land \neg B }}</td><td>{{ I_\land }} sur les lignes 5 et 9</td></tr>
      <tr><td>11</td><td>{{ \emptyset }}</td><td>{{ \neg(A \lor B) \Rightarrow (\neg A \land \neg B) }}</td><td>{{ I_\Rightarrow }} (lignes 1 à 10, décharge de {{ h_1 }})</td></tr>
    </tbody>
  </table>
</div>

<h2 id="sec5">5. Pourquoi {{ I_\neg }} est intuitionniste alors que {{ \text{Abs} }} est classique ?</h2>

<div class="box warn">
  <h4>La distinction fondamentale du cours (Cours 4 Slide 22 &amp; Cours 5 Slide 3)</h4>
  <p>Beaucoup d'étudiants confondent l'introduction de la négation ({{ I_\neg }}) et le raisonnement par l'absurde classique ({{ \text{Abs} }} / {{ \text{RAA} }}). Voici la différence exacte :</p>
  <ul>
    <li><strong>Introduction de la négation {{ I_\neg }} (100% Intuitionniste) :</strong>
      <br/>Pour prouver une <strong>formule négative {{ \neg A }}</strong>, on suppose {{ A }} et on dérive {{ \text{false} }}. Pourquoi est-ce constructif ? Parce qu'en logique intuitionniste, {{ \neg A }} est par définition un synonyme de l'implication {{ A \Rightarrow \text{false} }} (« toute preuve de {{ A }} engendre une contradiction »). Donc {{ I_\neg }} n'est rien d'autre qu'un cas particulier de {{ I_\Rightarrow }} !
    </li>
    <li><strong>Raisonnement par l'absurde {{ \text{Abs} }} / {{ \text{RAA} }} (Uniquement Classique — Thème 6) :</strong>
      <br/>Pour prouver une <strong>formule affirmative {{ A }}</strong>, on suppose {{ \neg A }} et on dérive {{ \text{false} }}. En logique intuitionniste, supposer {{ \neg A }} et aboutir à {{ \text{false} }} permet seulement de conclure {{ \neg\neg A }} (par {{ I_\neg }}), mais <strong>jamais {{ A }}</strong> !
    </li>
  </ul>
  <p><strong>Conséquence célèbre :</strong> En logique intuitionniste, on sait prouver {{ A \Rightarrow \neg\neg A }}, mais on ne peut <strong>pas</strong> prouver {{ \neg\neg A \Rightarrow A }} ni le Tiers Exclu {{ A \lor \neg A }}. Vérifions la preuve intuitionniste de {{ A \Rightarrow \neg\neg A }} (Cours 5, Slide 3) :</p>
  <pre><code>⟨1⟩ montrons A ⇒ ¬¬A par I⇒
  ⟨2⟩ supposons h1 : A, montrons ¬¬A par I¬
    ⟨3⟩ supposons h2 : ¬A, montrons false par E¬
      ⟨4⟩ montrons ¬A par Ax avec h2 ⟨4⟩
      ⟨5⟩ montrons A par Ax avec h1 ⟨5⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
</div>

<h2 id="sec6">6. Laboratoire interactif de vérification de séquents</h2>

<div class="box tip">
  <h4>Vérifiez vos séquents avant d'en rédiger la preuve formelle</h4>
  <p>Utilisez le vérificateur ci-dessous pour tester si vos hypothèses entraînent bien la conclusion visée, et inspectez l'arbre syntaxique de la formule pour identifier le connecteur principal qui dicte la première règle d'introduction.</p>
</div>

<div class="w-entail" data-h="A => ~C; C => B; A | ~B" data-f="~C"></div>

<div class="w-lab" data-formula="(A => B) => ((B => C) => (A => C))"></div>
"""

cours_fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>فصل ۵: استنتاج طبیعی گزاره‌ای (منطق شهودگرایانه)</h1>
  <p class="lead">سیستم استنتاج صوری گنتزن، ساختار باکس‌های تودرتوی سوربن، چرخه حیات و رهاسازی فرضیات، قواعد معرفی و حذف عملگرهای منطقی و راهبردهای اثبات سازنده.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب درس</h3>
  <ul>
    <li><a href="#sec1">۱. گذار از جدول‌های درستی به سیستم‌های استنتاج صوری (گنتزن، ۱۹۳۴)</a></li>
    <li><a href="#sec2">۲. باکس‌های تودرتو، قاعده اصل موضوعی (Ax) و ثوابت منطقی</a></li>
    <li><a href="#sec3">۳. قواعد معرفی (I) و حذف (E) عملگرهای منطقی</a></li>
    <li><a href="#sec4">۴. راهبردهای اثبات: استدلال از بالا به پایین (هدف‌محور) و پایین به بالا (فرضیه‌محور)</a></li>
    <li><a href="#sec5">۵. چرا قاعده {{ I_\neg }} شهودگرایانه است اما برهان خلف {{ \text{Abs} }} کلاسیک است؟</a></li>
    <li><a href="#sec6">۶. آزمایشگاه تعاملی بررسی درستی احکام استنتاجی</a></li>
  </ul>
</div>

<h2 id="sec1">1. Des tables de vérité aux systèmes de déduction formelle (Gentzen, 1934)</h2>

<div class="box info">
  <h4>چرا به یک سیستم اثبات کاملاً نحوی (Syntactic) نیاز داریم؟</h4>
  <p>در فصل‌های ۱ تا ۴، <strong>معناشناسی (Semantics)</strong> را مطالعه کردیم: فرمول {{ F }} معتبر است ({{ \models F }}) اگر به ازای هر تعبیر {{ I }} داشته باشیم {{ [F]^I = 1 }}. اما هنگامی که وارد منطق محمولات مرتبه اول شویم (فصل‌های ۷ تا ۹)، دامنه‌های تعبیر <strong>نامتناهی</strong> خواهند شد (مانند {{ \mathbb{N} }} یا {{ \mathbb{R} }}) و شمارش مدل‌ها غیرممکن می‌گردد.</p>
  <p>یک <strong>سیستم استنتاج</strong> (که توسط گرهارد گنتزن در سال ۱۹۳۴ با نام <em>استنتاج طبیعی</em> معرفی شد) فرمول‌های معتبر را به روشی کاملاً <strong>نحوی و نمادین</strong> توصیف می‌کند؛ یعنی با قواعد استدلال پایه‌ای که تنها ساختار ظاهری فرمول‌ها را بدون محاسبه مقادیر بولی {{ 0 }} یا {{ 1 }} دستکاری می‌کنند.</p>
</div>

<div class="box def">
  <h4>حکم استنتاج‌پذیری (سِکوئنت / Séquence) {{ \Gamma \vdash F }}</h4>
  <p>هر گام از یک اثبات صوری، یک <strong>حکم استنتاجی</strong> را به شکل زیر برقرار می‌سازد:</p>
  <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">{{ h_1 : F_1, \, h_2 : F_2, \, \dots, \, h_n : F_n \vdash F }}</p>
  <ul>
    <li>بخش چپ یعنی {{ \Gamma = \{h_1 : F_1, \dots, h_n : F_n\} }} مجموعه <strong>فرضیات فعال</strong> (بافتار جاری اثبات) را نشان می‌دهد.</li>
    <li>فرمول {{ F }} در سمت راست نماد {{ \vdash }} (که خوانده می‌شود <em>«اثبات می‌کند»</em>) همان <strong>هدف</strong> یا نتیجه مورد نظر است.</li>
    <li>هنگامی که {{ \Gamma = \emptyset }} باشد، می‌نویسیم {{ \vdash F }} : فرمول {{ F }} بدون هیچ فرض اولیه‌ای اثبات‌پذیر است و به آن یک <strong>قضیه (Théorème)</strong> می‌گوییم.</li>
    <li><strong>قضیه سازگاری (Correction) و تمامیت (Complétude):</strong> یک فرمول در سیستم استنتاج طبیعی کلاسیک اثبات‌پذیر است ({{ \Gamma \vdash F }}) اگر و تنها اگر نتیجه معنایی فرضیات باشد ({{ \Gamma \models F }}).</li>
  </ul>
</div>

<h2 id="sec2">2. Emboîtement de boîtes, axiome et constantes logiques</h2>

<div class="box method">
  <h4>فرمالیسم باکس‌های شماره‌گذاری‌شده دانشگاه سوربن (درس ۴، اسلایدهای ۷ تا ۱۱)</h4>
  <p>در دانشگاه سوربن، اثبات‌های استنتاج طبیعی به صورت <strong>باکس‌های تودرتوی شماره‌گذاری‌شده</strong> با علامت‌های {{ \langle i \rangle \dots \langle i \rangle }} نوشته می‌شوند (که معادل دقیق باکس‌های عمودی فیتش هستند):</p>
  <pre><code>⟨i⟩ supposons h1 : F1, h2 : F2, ..., hn : Fn
    montrons F par Nom_Règle
    ⟨i+1⟩ ... sous-preuve 1 ... ⟨i+1⟩
    ⟨i+2⟩ ... sous-preuve 2 ... ⟨i+2⟩
⟨i⟩</code></pre>
  <p><strong>قانون دامنه دید (چرخه حیات یک فرضیه):</strong></p>
  <ul>
    <li>هر فرضیه {{ h : A }} که در ابتدای باکس {{ \langle j \rangle }} معرفی شود، در سراسر باکس {{ \langle j \rangle }} و تمامی زیرباکس‌های {{ \langle i \rangle }} که درون {{ \langle j \rangle }} قرار دارند <strong>فعال و قابل استفاده</strong> است.</li>
    <li>به محض بسته شدن باکس {{ \langle j \rangle }}، فرضیه {{ h : A }} <strong>رهاسازی (Déchargée)</strong> و غیرفعال می‌شود: استناد به {{ h }} در بیرون از باکس {{ \langle j \rangle }} خطای علمی فاحش است!</li>
  </ul>
</div>

<div class="box def">
  <h4>قاعده اصل موضوعی ({{ \text{Ax} }}) و قواعد ثوابت {{ \text{true} }} ({{ \top }}) و {{ \text{false} }} ({{ \bot }})</h4>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>نام قاعده</th>
        <th>طرحواره گنتزن</th>
        <th>نگارش باکسی سوربن</th>
        <th>توضیح کاربرد</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>اصل موضوع ({{ \text{Ax} }})</strong></td>
        <td>{{ \Gamma, h : A \vdash A }}</td>
        <td><code>⟨i⟩ supposons ..., h : A</code><br/><code>    montrons A par Ax avec h</code><br/><code>⟨i⟩</code></td>
        <td>اگر هدف {{ A }} عیناً در میان فرضیات فعال (در باکس فعلی یا باکس‌های پدر) موجود باشد، اثبات بلافاصله کامل است.</td>
      </tr>
      <tr>
        <td><strong>معرفی درستی ({{ I_\top }})</strong></td>
        <td>{{ \Gamma \vdash \text{true} }}</td>
        <td><code>⟨i⟩ montrons true par I⊤ ⟨i⟩</code></td>
        <td>ثابت {{ \text{true} }} همواره بدون نیاز به فرض اثبات‌پذیر است. این ثابت <strong>هیچ قاعده حذفی ندارد</strong> (از فرض {{ h : \text{true} }} چیزی استخراج نمی‌شود).</td>
      </tr>
      <tr>
        <td><strong>حذف نادرستی ({{ E_\bot }})</strong><br/><em>(Ex falso quodlibet)</em></td>
        <td>{{ \frac{\Gamma \vdash \text{false}}{\Gamma \vdash B} }}</td>
        <td><code>⟨i⟩ supposons ..., h : false</code><br/><code>    montrons B par E⊥ avec h</code><br/><code>⟨i⟩</code></td>
        <td><strong>اصل انفجار شهودگرایانه:</strong> از تناقض {{ \text{false} }} ({{ \bot }}) می‌توان <em>هر فرمول دلخواه {{ B }}</em> را استنتاج کرد! ثابت {{ \text{false} }} <strong>هیچ قاعده معرفی ندارد</strong>.</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec3">3. Règles d'Introduction (I) et d'Élimination (E) des connecteurs</h2>

<div class="box info">
  <h4>فلسفه کلی قواعد: معرفی در برابر حذف (درس ۴، اسلاید ۱۲)</h4>
  <ul>
    <li><strong>قواعد معرفی ({{ I }} - Introduction):</strong> نشان می‌دهند چگونه یک فرمول که عملگر اصلی آن (ریشه درخت نحوی) {{ \Rightarrow, \land, \lor, \neg }} یا {{ \Leftrightarrow }} است را <em>اثبات و تولید کنیم</em>.</li>
    <li><strong>قواعد حذف ({{ E }} - Élimination):</strong> نشان می‌دهند چگونه از یک فرضیه یا فرمول اثبات‌شده که عملگر اصلی آن {{ \Rightarrow, \land, \lor, \neg }} یا {{ \Leftrightarrow }} است <em>بهره‌برداری و استنتاج کنیم</em>.</li>
  </ul>
</div>

<div class="box def">
  <h4>جدول کامل قواعد استنتاج طبیعی شهودگرایانه (استاندارد سوربن)</h4>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>عملگر منطقی</th>
        <th>قاعده معرفی ({{ I }})</th>
        <th>قاعده حذف ({{ E }}) و قاعده مشتق مستقیم فرمول‌نامه ({{ D }})</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>شرطی ({{ \Rightarrow }})</strong></td>
        <td><strong>{{ I_\Rightarrow }} ({{ \Rightarrow I }}) :</strong> برای اثبات {{ A \Rightarrow B }}، یک زیرباکس باز کرده، در آن {{ h : A }} را فرض می‌کنیم و {{ B }} را نشان می‌دهیم.<br/>
        <code>⟨i⟩ montrons A ⇒ B par I⇒</code><br/>
        <code>  ⟨i+1⟩ supposons h : A, montrons B ... ⟨i+1⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\Rightarrow }} ({{ \Rightarrow E }} / قیاس استثنایی) :</strong> برای اثبات {{ B }}، در یک زیرباکس {{ A \Rightarrow B }} و در زیرباکس دیگر {{ A }} را اثبات می‌کنیم.<br/>
        <em>میانبر فرمول‌نامه {{ D_\Rightarrow }} :</em> اگر {{ h_1 : A \Rightarrow B }} و {{ h_2 : A }} در فرضیات باشند، مستقیماً با <code>D⇒ avec h1, h2</code> نتیجه {{ B }} حاصل می‌شود.</td>
      </tr>
      <tr>
        <td><strong>عطف ({{ \land }})</strong></td>
        <td><strong>{{ I_\land }} ({{ \land I }}) :</strong> برای اثبات {{ A \land B }}، دو زیرباکس مجزا باز می‌کنیم: یکی برای اثبات {{ A }} و دیگری برای اثبات {{ B }}.<br/>
        <code>⟨i⟩ montrons A ∧ B par I∧</code><br/>
        <code>  ⟨i+1⟩ montrons A ... ⟨i+1⟩</code><br/>
        <code>  ⟨i+2⟩ montrons B ... ⟨i+2⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\land^g }} ({{ \land E_1 }}) و {{ E_\land^d }} ({{ \land E_2 }}) :</strong> از اثبات {{ A \land B }}، قاعده {{ E_\land^g }} مؤلفه چپ یعنی {{ A }} و قاعده {{ E_\land^d }} مؤلفه راست یعنی {{ B }} را استخراج می‌کند.<br/>
        <em>میانبر فرمول‌نامه {{ D_\land^g }} / {{ D_\land^d }} :</em> اگر {{ h : A \land B }} فرض باشد، <code>D∧g avec h</code> فرمول {{ A }} و <code>D∧d avec h</code> فرمول {{ B }} را می‌دهد.</td>
      </tr>
      <tr>
        <td><strong>فصل ({{ \lor }})</strong></td>
        <td><strong>{{ I_\lor^g }} ({{ \lor I_1 }}) و {{ I_\lor^d }} ({{ \lor I_2 }}) :</strong> برای اثبات {{ A \lor B }}، کافی است یا {{ A }} را اثبات کنیم (با {{ I_\lor^g }}) و یا {{ B }} را اثبات کنیم (با {{ I_\lor^d }}).<br/>
        <em>نکته مهم:</em> باید سمتی ({{ g }} چپ یا {{ d }} راست) را انتخاب کنید که با فرضیات فعلی قابل اثبات باشد!</td>
        <td><strong>{{ E_\lor }} ({{ \lor E }} / استدلال بر اساس حالات) :</strong> برای اثبات هدف {{ C }} با استفاده از فصل {{ A \lor B }}، به <strong>۳ زیرباکس</strong> نیاز است:<br/>
        ۱. اثبات {{ A \lor B }}<br/>
        ۲. فرض {{ h_A : A }} و اثبات {{ C }}<br/>
        ۳. فرض {{ h_B : B }} و اثبات {{ C }}<br/>
        <em>میانبر {{ D_\lor }} :</em> اگر {{ h : A \lor B }} در فرضیات باشد، فقط زیرباکس‌های ۲ و ۳ لازم است (<code>D∨ avec h</code>).</td>
      </tr>
      <tr>
        <td><strong>نقیض ({{ \neg }})</strong></td>
        <td><strong>{{ I_\neg }} ({{ \neg I }}) :</strong> برای اثبات یک نقیض {{ \neg A }}، زیرباکسی باز کرده، {{ h : A }} را فرض می‌کنیم و به {{ \text{false} }} ({{ \bot }}) می‌رسیم.<br/>
        <code>⟨i⟩ montrons ¬A par I¬</code><br/>
        <code>  ⟨i+1⟩ supposons h : A, montrons false ... ⟨i+1⟩</code><br/>
        <code>⟨i⟩</code></td>
        <td><strong>{{ E_\neg }} ({{ \neg E }}) :</strong> برای اثبات {{ \text{false} }} ({{ \bot }})، در یک زیرباکس {{ \neg A }} و در دیگری {{ A }} را اثبات می‌کنیم.<br/>
        <em>میانبر فرمول‌نامه {{ D_\bot^1 }} :</em> اگر دو فرض متناقض {{ h_1 : A }} و {{ h_2 : \neg A }} داشته باشیم، می‌توانیم <strong>هر هدف دلخواه {{ B }}</strong> را یک‌خطی با <code>D⊥1 avec h1, h2</code> نتیجه بگیریم (ترکیب {{ E_\neg }} و {{ E_\bot }}).</td>
      </tr>
      <tr>
        <td><strong>هم‌ارزی ({{ \Leftrightarrow }})</strong></td>
        <td><strong>{{ I_\Leftrightarrow }} ({{ \Leftrightarrow I }}) :</strong> برای اثبات {{ A \Leftrightarrow B }}، در زیرباکس اول {{ A \Rightarrow B }} و در زیرباکس دوم {{ B \Rightarrow A }} را ثابت می‌کنیم.</td>
        <td><strong>{{ E_\Leftrightarrow^g }} و {{ E_\Leftrightarrow^d }} :</strong> از {{ A \Leftrightarrow B }}، شرطی {{ A \Rightarrow B }} (چپ) یا {{ B \Rightarrow A }} (راست) استخراج می‌شود.</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec4">4. Stratégies de preuve : raisonnement descendant (but) vs ascendant (hypothèses)</h2>

<div class="box method">
  <h4>روش گام‌به‌گام و تضمینی برای نوشتن هر اثبات بدون گیر کردن</h4>
  <ol>
    <li><strong>گام ۱ — خرد کردن هدف با قواعد معرفی (تحلیل از بالا به پایین / Goal-Directed) :</strong>
      <ul>
        <li>اگر هدف {{ A \Rightarrow B }} است: <strong>همیشه بلافاصله</strong> قاعده {{ I_\Rightarrow }} را اعمال کنید (<code>supposons h : A, montrons B</code>). این کار را تا زمانی که هدف شرطی است تکرار کنید!</li>
        <li>اگر هدف {{ A \land B }} است: <strong>همیشه بلافاصله</strong> قاعده {{ I_\land }} را به کار ببرید تا اثبات به دو زیرهدف مستقل {{ A }} و {{ B }} تقسیم شود.</li>
        <li>اگر هدف {{ \neg A }} است: <strong>همیشه بلافاصله</strong> قاعده {{ I_\neg }} را اعمال کنید (<code>supposons h : A, montrons false</code>).</li>
        <li>اگر هدف {{ A \lor B }} است: <em>احتیاط کنید!</em> تنها زمانی {{ I_\lor^g }} یا {{ I_\lor^d }} را بزنید که فرضیات فعلی مستقیماً یکی از دو شاخه {{ A }} یا {{ B }} را نتیجه دهند. در غیر این صورت، ابتدا سراغ فرضیات بروید!</li>
      </ul>
    </li>
    <li><strong>گام ۲ — بهره‌برداری از فرضیات با قواعد حذف (تحلیل از پایین به بالا / Hypothesis-Driven) :</strong>
      <ul>
        <li>اگر فرض عطفی {{ h : A \land B }} دارید: هم به {{ A }} (با {{ E_\land^g }}) و هم به {{ B }} (با {{ E_\land^d }}) دسترسی دارید.</li>
        <li>اگر فرض فصلی {{ h : A \lor B }} دارید: <strong>تقریباً همیشه</strong> باید از قاعده استدلال بر اساس حالات {{ E_\lor }} (یا {{ D_\lor }}) استفاده کنید و اثبات را به دو شاخه حالت ۱ ({{ h_A : A }}) و حالت ۲ ({{ h_B : B }}) بشکنید.</li>
        <li>اگر {{ h_1 : A \Rightarrow B }} و {{ h_2 : A }} را دارید: با قیاس استثنایی ({{ E_\Rightarrow }} / {{ D_\Rightarrow }}) فرمول {{ B }} را استخراج کنید.</li>
        <li>اگر {{ A }} و {{ \neg A }} را هم‌زمان در فرضیات فعال دیدید: کار تمام است! با {{ E_\neg }} به {{ \text{false} }} برسید و با {{ E_\bot }} (یا مستقیماً {{ D_\bot^1 }}) هر هدف دلخواه {{ C }} را نتیجه بگیرید.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box tip">
  <h4>مثال کامل درس (درس ۴، اسلاید ۲۶) : اثبات {{ \neg(A \lor B) \Rightarrow (\neg A \land \neg B) }}</h4>
  <p>ببینید چگونه ساختار نحوی فرمول به صورت کاملاً مکانیکی تمام خطوط اثبات را هدایت می‌کند:</p>
  <pre><code>⟨1⟩ montrons ¬(A ∨ B) ⇒ (¬A ∧ ¬B) par I⇒
  ⟨2⟩ supposons h1 : ¬(A ∨ B), montrons ¬A ∧ ¬B par I∧
    ⟨3⟩ montrons ¬A par I¬
      ⟨4⟩ supposons h2 : A, montrons false par E¬
        ⟨5⟩ montrons ¬(A ∨ B) par Ax avec h1 ⟨5⟩
        ⟨6⟩ montrons A ∨ B par I∨g
          ⟨7⟩ montrons A par Ax avec h2 ⟨7⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
    ⟨8⟩ montrons ¬B par I¬
      ⟨9⟩ supposons h3 : B, montrons false par E¬
        ⟨10⟩ montrons ¬(A ∨ B) par Ax avec h1 ⟨10⟩
        ⟨11⟩ montrons A ∨ B par I∨d
          ⟨12⟩ montrons B par Ax avec h3 ⟨12⟩
        ⟨11⟩
      ⟨9⟩
    ⟨8⟩
  ⟨2⟩
⟨1⟩</code></pre>
  <p>همین اثبات در قالب جدولی خط‌به‌خط فیتش (Fitch) به صورت زیر نوشته می‌شود:</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول استنتاج‌شده</th><th>قاعده و توجیه</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>{{ h_1 }}</td><td>{{ \neg(A \lor B) }}</td><td>فرض (باز کردن باکس برای {{ I_\Rightarrow }})</td></tr>
      <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A }}</td><td>فرض (باز کردن زیرباکس برای {{ I_\neg }})</td></tr>
      <tr><td>3</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor B }}</td><td>قاعده {{ I_\lor^g }} روی سطر ۲</td></tr>
      <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۱ و ۳</td></tr>
      <tr><td>5</td><td>{{ h_1 }}</td><td>{{ \neg A }}</td><td>قاعده {{ I_\neg }} (سطرهای ۲ تا ۴، رهاسازی {{ h_2 }})</td></tr>
      <tr><td>6</td><td>{{ h_1, h_3 }}</td><td>{{ B }}</td><td>فرض (باز کردن زیرباکس برای {{ I_\neg }})</td></tr>
      <tr><td>7</td><td>{{ h_1, h_3 }}</td><td>{{ A \lor B }}</td><td>قاعده {{ I_\lor^d }} روی سطر ۶</td></tr>
      <tr><td>8</td><td>{{ h_1, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۱ و ۷</td></tr>
      <tr><td>9</td><td>{{ h_1 }}</td><td>{{ \neg B }}</td><td>قاعده {{ I_\neg }} (سطرهای ۶ تا ۸، رهاسازی {{ h_3 }})</td></tr>
      <tr><td>10</td><td>{{ h_1 }}</td><td>{{ \neg A \land \neg B }}</td><td>قاعده {{ I_\land }} روی سطرهای ۵ و ۹</td></tr>
      <tr><td>11</td><td>{{ \emptyset }}</td><td>{{ \neg(A \lor B) \Rightarrow (\neg A \land \neg B) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۱۰، رهاسازی {{ h_1 }})</td></tr>
    </tbody>
  </table>
</div>

<h2 id="sec5">5. Pourquoi {{ I_\neg }} est intuitionniste alors que {{ \text{Abs} }} est classique ?</h2>

<div class="box warn">
  <h4>تمایز حیاتی درس (اسلاید ۲۲ درس ۴ و اسلاید ۳ درس ۵)</h4>
  <p>بسیاری از دانشجویان قاعده معرفی نقیض ({{ I_\neg }}) را با برهان خلف کلاسیک ({{ \text{Abs} }} / {{ \text{RAA} }}) اشتباه می‌گیرند. تفاوت دقیق آن‌ها چنین است:</p>
  <ul>
    <li><strong>معرفی نقیض {{ I_\neg }} (کاملاً شهودگرایانه):</strong>
      <br/>برای اثبات یک <strong>فرمول منفی {{ \neg A }}</strong>، فرض می‌کنیم {{ A }} برقرار است و به تناقض {{ \text{false} }} می‌رسیم. چرا این کار سازنده و شهودگرایانه است؟ زیرا در منطق شهودگرایانه، {{ \neg A }} دقیقاً مخفف شرطی {{ A \Rightarrow \text{false} }} است («هر اثباتی از {{ A }} به تناقض می‌انجامد»). بنابراین {{ I_\neg }} صرفاً حالت خاصی از {{ I_\Rightarrow }} است!
    </li>
    <li><strong>برهان خلف {{ \text{Abs} }} / {{ \text{RAA} }} (منحصراً کلاسیک — فصل ۶):</strong>
      <br/>برای اثبات یک <strong>فرمول مثبت {{ A }}</strong>، فرض می‌کنیم {{ \neg A }} و به تناقض {{ \text{false} }} می‌رسیم. در منطق شهودگرایانه، فرض کردن {{ \neg A }} و رسیدن به {{ \text{false} }} فقط {{ \neg\neg A }} را ثابت می‌کند (با {{ I_\neg }})، اما <strong>هرگز {{ A }} را نتیجه نمی‌دهد</strong>!
    </li>
  </ul>
  <p><strong>نتیجه مشهور:</strong> در منطق شهودگرایانه می‌توانیم {{ A \Rightarrow \neg\neg A }} را اثبات کنیم، اما <strong>نمی‌توانیم</strong> {{ \neg\neg A \Rightarrow A }} یا اصل طرد شق ثالث {{ A \lor \neg A }} را اثبات نماییم. اثبات شهودگرایانه {{ A \Rightarrow \neg\neg A }} (درس ۵، اسلاید ۳) به قرار زیر است:</p>
  <pre><code>⟨1⟩ montrons A ⇒ ¬¬A par I⇒
  ⟨2⟩ supposons h1 : A, montrons ¬¬A par I¬
    ⟨3⟩ supposons h2 : ¬A, montrons false par E¬
      ⟨4⟩ montrons ¬A par Ax avec h2 ⟨4⟩
      ⟨5⟩ montrons A par Ax avec h1 ⟨5⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
</div>

<h2 id="sec6">6. Laboratoire interactif de vérification de séquents</h2>

<div class="box tip">
  <h4>پیش از نگارش اثبات صوری، درستی حکم را بیازمایید</h4>
  <p>از ابزار تعاملی زیر برای بررسی درستی استلزام فرضیات به نتیجه استفاده کنید و درخت نحوی فرمول را ببینید تا عملگر اصلی تعیین‌کننده نخستین قاعده معرفی مشخص شود.</p>
</div>

<div class="w-entail" data-h="A => ~C; C => B; A | ~B" data-f="~C"></div>

<div class="w-lab" data-formula="(A => B) => ((B => C) => (A => C))"></div>
"""

open(os.path.join(W05, 'cours.fr.html'), 'w', encoding='utf-8').write(cours_fr.strip())
open(os.path.join(W05, 'cours.fa.html'), 'w', encoding='utf-8').write(cours_fa.strip())
print("w05 cours written.")


# ==============================================================================
# 2. TD (FR & FA) - Exercices 17 (Q1..Q6) et 18 (Q1, Q2)
# ==============================================================================

td_fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TD Thème 5 : Preuves en Déduction Naturelle Intuitionniste</h1>
  <p class="lead">Corrections intégrales des Exercices 17 (Questions 1 à 6) et 18 (Énigme d'Anissa, Boris et Chloé) du polycopié officiel de TD 2026-2027, rédigées en boîtes numérotées de la Sorbonne et en tables de Fitch ligne par ligne.</p>
</div>

<div class="toc-box">
  <h3>Sommaire des exercices du TD</h3>
  <ul>
    <li><a href="#td5_ex17">Exercice 17 – Preuves formelles de 6 théorèmes intuitionnistes</a></li>
    <li><a href="#td5_ex18">Exercice 18 – Énigme logique : la fête d'Anissa, Boris et Chloé</a></li>
  </ul>
</div>

<div class="box warn">
  <h4>Consigne officielle du Thème 5</h4>
  <p><em>« Vous devez répondre aux questions de ce thème en utilisant exclusivement les règles de base de la déduction naturelle intuitionniste (sans Tiers Exclu {{ \text{TE} }} ni raisonnement par l'absurde classique {{ \text{Abs} }}). »</em></p>
</div>

<!-- EXERCICE 17 -->
<h2 id="td5_ex17">Exercice 17 – Preuves formelles de 6 théorèmes intuitionnistes</h2>

<!-- Q17.1 -->
<div class="q-card" id="td5_q17_1">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 1</span>
    <span class="q-title">Preuve de {{ F_1 = (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la formule de transitivité de l'implication :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_1 = (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Boîtes Sorbonne &amp; Table de Fitch)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>La formule {{ F_1 }} est une cascade de trois implications imbriquées. On applique donc trois fois de suite la règle d'introduction {{ I_\Rightarrow }} pour empiler les trois hypothèses {{ h_1 : A \Rightarrow B }}, {{ h_2 : B \Rightarrow C }} et {{ h_3 : A }}. Le but restant est {{ C }}, que l'on obtient par deux éliminations {{ E_\Rightarrow }} (Modus Ponens) successives.</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ ((B ⇒ C) ⇒ (A ⇒ C)) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons (B ⇒ C) ⇒ (A ⇒ C) par I⇒
    ⟨3⟩ supposons h2 : B ⇒ C, montrons A ⇒ C par I⇒
      ⟨4⟩ supposons h3 : A, montrons C par E⇒
        ⟨5⟩ montrons B ⇒ C par Ax avec h2 ⟨5⟩
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ B \Rightarrow C }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>{{ E_\Rightarrow }} sur les lignes 1 et 3</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ C }}</td><td>{{ E_\Rightarrow }} sur les lignes 2 et 4</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ A \Rightarrow C }}</td><td>{{ I_\Rightarrow }} (lignes 3–5, décharge de {{ h_3 }})</td></tr>
          <tr><td>7</td><td>{{ h_1 }}</td><td>{{ (B \Rightarrow C) \Rightarrow (A \Rightarrow C) }}</td><td>{{ I_\Rightarrow }} (lignes 2–6, décharge de {{ h_2 }})</td></tr>
          <tr><td>8</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</td><td>{{ I_\Rightarrow }} (lignes 1–7, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.2 -->
<div class="q-card" id="td5_q17_2">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 2</span>
    <span class="q-title">Preuve de {{ F_2 = (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la formule :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_2 = (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Boîtes Sorbonne &amp; Table de Fitch)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>Après deux introductions {{ I_\Rightarrow }} qui posent {{ h_1 : ((A \land B) \Rightarrow C) \land (A \Rightarrow B) }} et {{ h_2 : A }}, on extrait de {{ h_1 }} les deux implications par {{ E_\land^g }} et {{ E_\land^d }}. Avec {{ A }} et {{ A \Rightarrow B }}, on obtient {{ B }} par {{ E_\Rightarrow }}, puis on assemble {{ A \land B }} par {{ I_\land }} avant d'appliquer {{ E_\Rightarrow }} sur {{ (A \land B) \Rightarrow C }}.</p>
      <pre><code>⟨1⟩ montrons (((A ∧ B) ⇒ C) ∧ (A ⇒ B)) ⇒ (A ⇒ C) par I⇒
  ⟨2⟩ supposons h1 : ((A ∧ B) ⇒ C) ∧ (A ⇒ B), montrons A ⇒ C par I⇒
    ⟨3⟩ supposons h2 : A, montrons C par E⇒
      ⟨4⟩ montrons (A ∧ B) ⇒ C par E∧g
        ⟨5⟩ montrons ((A ∧ B) ⇒ C) ∧ (A ⇒ B) par Ax avec h1 ⟨5⟩
      ⟨4⟩
      ⟨6⟩ montrons A ∧ B par I∧
        ⟨7⟩ montrons A par Ax avec h2 ⟨7⟩
        ⟨8⟩ montrons B par E⇒
          ⟨9⟩ montrons A ⇒ B par E∧d
            ⟨10⟩ montrons ((A ∧ B) ⇒ C) ∧ (A ⇒ B) par Ax avec h1 ⟨10⟩
          ⟨9⟩
          ⟨11⟩ montrons A par Ax avec h2 ⟨11⟩
        ⟨8⟩
      ⟨6⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ ((A \land B) \Rightarrow C) \land (A \Rightarrow B) }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2 }}</td><td>{{ (A \land B) \Rightarrow C }}</td><td>{{ E_\land^g }} sur la ligne 1</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ A \Rightarrow B }}</td><td>{{ E_\land^d }} sur la ligne 1</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2 }}</td><td>{{ B }}</td><td>{{ E_\Rightarrow }} sur les lignes 4 et 2</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ A \land B }}</td><td>{{ I_\land }} sur les lignes 2 et 5</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2 }}</td><td>{{ C }}</td><td>{{ E_\Rightarrow }} sur les lignes 3 et 6</td></tr>
          <tr><td>8</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow C }}</td><td>{{ I_\Rightarrow }} (lignes 2–7, décharge de {{ h_2 }})</td></tr>
          <tr><td>9</td><td>{{ \emptyset }}</td><td>{{ (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</td><td>{{ I_\Rightarrow }} (lignes 1–8, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.3 -->
<div class="q-card" id="td5_q17_3">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 3</span>
    <span class="q-title">Preuve de {{ F_3 = (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la formule de monotonie de la disjonction :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_3 = (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Boîtes Sorbonne &amp; Table de Fitch)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>Après avoir posé {{ h_1 : A \Rightarrow B }} et {{ h_2 : A \lor C }} par {{ I_\Rightarrow }}, le but est {{ B \lor C }}. Attention au piège : on ne peut pas appliquer directement {{ I_\lor^g }} ni {{ I_\lor^d }} car on ne sait pas encore si l'on est dans le cas {{ A }} ou dans le cas {{ C }} ! Il faut d'abord éliminer la disjonction {{ h_2 : A \lor C }} par {{ E_\lor }} : dans le cas {{ A }}, on déduit {{ B }} puis {{ B \lor C }} (par {{ I_\lor^g }}) ; dans le cas {{ C }}, on déduit directement {{ B \lor C }} (par {{ I_\lor^d }}).</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ ((A ∨ C) ⇒ (B ∨ C)) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons (A ∨ C) ⇒ (B ∨ C) par I⇒
    ⟨3⟩ supposons h2 : A ∨ C, montrons B ∨ C par E∨
      ⟨4⟩ montrons A ∨ C par Ax avec h2 ⟨4⟩
      ⟨5⟩ supposons h3 : A, montrons B ∨ C par I∨g
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨5⟩
      ⟨9⟩ supposons h4 : C, montrons B ∨ C par I∨d
        ⟨10⟩ montrons C par Ax avec h4 ⟨10⟩
      ⟨9⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor C }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>Hypothèse Cas 1 (pour {{ E_\lor }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>{{ E_\Rightarrow }} sur les lignes 1 et 3</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B \lor C }}</td><td>{{ I_\lor^g }} sur la ligne 4</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ C }}</td><td>Hypothèse Cas 2 (pour {{ E_\lor }})</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ B \lor C }}</td><td>{{ I_\lor^d }} sur la ligne 6</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2 }}</td><td>{{ B \lor C }}</td><td>{{ E_\lor }} sur la ligne 2, Cas 1 (3–5) et Cas 2 (6–7)</td></tr>
          <tr><td>9</td><td>{{ h_1 }}</td><td>{{ (A \lor C) \Rightarrow (B \lor C) }}</td><td>{{ I_\Rightarrow }} (lignes 2–8, décharge de {{ h_2 }})</td></tr>
          <tr><td>10</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</td><td>{{ I_\Rightarrow }} (lignes 1–9, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.4 -->
<div class="q-card" id="td5_q17_4">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 4</span>
    <span class="q-title">Preuve de {{ F_4 = (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la formule :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_4 = (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Double élimination de disjonction imbriquée)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>Après deux introductions {{ I_\Rightarrow }}, nous avons deux hypothèses disjonctives : {{ h_1 : A \lor (B \Rightarrow C) }} et {{ h_2 : A \lor B }}. On élimine d'abord {{ h_1 }} par {{ E_\lor }} :</p>
      <ul>
        <li><strong>Branche 1 ({{ h_3 : A }}) :</strong> on obtient immédiatement {{ A \lor C }} par {{ I_\lor^g }}.</li>
        <li><strong>Branche 2 ({{ h_4 : B \Rightarrow C }}) :</strong> on élimine la seconde disjonction {{ h_2 : A \lor B }} par {{ E_\lor }} ! Dans le sous-cas {{ h_5 : A }}, on conclut {{ A \lor C }} par {{ I_\lor^g }}. Dans le sous-cas {{ h_6 : B }}, on applique {{ E_\Rightarrow }} avec {{ h_4 }} pour obtenir {{ C }}, puis {{ A \lor C }} par {{ I_\lor^d }}.</li>
      </ul>
      <pre><code>⟨1⟩ montrons (A ∨ (B ⇒ C)) ⇒ ((A ∨ B) ⇒ (A ∨ C)) par I⇒
  ⟨2⟩ supposons h1 : A ∨ (B ⇒ C), montrons (A ∨ B) ⇒ (A ∨ C) par I⇒
    ⟨3⟩ supposons h2 : A ∨ B, montrons A ∨ C par E∨
      ⟨4⟩ montrons A ∨ (B ⇒ C) par Ax avec h1 ⟨4⟩
      ⟨5⟩ supposons h3 : A, montrons A ∨ C par I∨g
        ⟨6⟩ montrons A par Ax avec h3 ⟨6⟩
      ⟨5⟩
      ⟨7⟩ supposons h4 : B ⇒ C, montrons A ∨ C par E∨
        ⟨8⟩ montrons A ∨ B par Ax avec h2 ⟨8⟩
        ⟨9⟩ supposons h5 : A, montrons A ∨ C par I∨g
          ⟨10⟩ montrons A par Ax avec h5 ⟨10⟩
        ⟨9⟩
        ⟨11⟩ supposons h6 : B, montrons A ∨ C par I∨d
          ⟨12⟩ montrons C par E⇒
            ⟨13⟩ montrons B ⇒ C par Ax avec h4 ⟨13⟩
            ⟨14⟩ montrons B par Ax avec h6 ⟨14⟩
          ⟨12⟩
        ⟨11⟩
      ⟨7⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \lor (B \Rightarrow C) }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>Hypothèse Cas 1 de {{ h_1 }}</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A \lor C }}</td><td>{{ I_\lor^g }} sur la ligne 3</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ B \Rightarrow C }}</td><td>Hypothèse Cas 2 de {{ h_1 }}</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_4, h_5 }}</td><td>{{ A }}</td><td>Hypothèse Sous-cas 2a de {{ h_2 }}</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4, h_5 }}</td><td>{{ A \lor C }}</td><td>{{ I_\lor^g }} sur la ligne 6</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ B }}</td><td>Hypothèse Sous-cas 2b de {{ h_2 }}</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ C }}</td><td>{{ E_\Rightarrow }} sur les lignes 5 et 8</td></tr>
          <tr><td>10</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ A \lor C }}</td><td>{{ I_\lor^d }} sur la ligne 9</td></tr>
          <tr><td>11</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ A \lor C }}</td><td>{{ E_\lor }} sur la ligne 2, sous-cas (6–7) et (8–10)</td></tr>
          <tr><td>12</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor C }}</td><td>{{ E_\lor }} sur la ligne 1, cas (3–4) et (5–11)</td></tr>
          <tr><td>13</td><td>{{ h_1 }}</td><td>{{ (A \lor B) \Rightarrow (A \lor C) }}</td><td>{{ I_\Rightarrow }} (lignes 2–12, décharge de {{ h_2 }})</td></tr>
          <tr><td>14</td><td>{{ \emptyset }}</td><td>{{ (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</td><td>{{ I_\Rightarrow }} (lignes 1–13, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.5 -->
<div class="q-card" id="td5_q17_5">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 5</span>
    <span class="q-title">Preuve de {{ F_5 = (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la loi de contraposition directe :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_5 = (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Boîtes Sorbonne &amp; Table de Fitch)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>La contraposition directe {{ (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }} est <strong>parfaitement intuitionniste</strong> car sa conclusion finale {{ \neg A }} est une négation ! On introduit {{ h_1 : A \Rightarrow B }} et {{ h_2 : \neg B }} par {{ I_\Rightarrow }}, puis {{ h_3 : A }} par {{ I_\neg }} pour chercher {{ \text{false} }}. De {{ A }} et {{ A \Rightarrow B }} on tire {{ B }}, qui contredit {{ \neg B }} par {{ E_\neg }}.</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ (¬B ⇒ ¬A) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons ¬B ⇒ ¬A par I⇒
    ⟨3⟩ supposons h2 : ¬B, montrons ¬A par I¬
      ⟨4⟩ supposons h3 : A, montrons false par E¬
        ⟨5⟩ montrons ¬B par Ax avec h2 ⟨5⟩
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ \neg B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>Hypothèse (pour {{ I_\neg }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>{{ E_\Rightarrow }} sur les lignes 1 et 3</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 2 et 4</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ \neg A }}</td><td>{{ I_\neg }} (lignes 3–5, décharge de {{ h_3 }})</td></tr>
          <tr><td>7</td><td>{{ h_1 }}</td><td>{{ \neg B \Rightarrow \neg A }}</td><td>{{ I_\Rightarrow }} (lignes 2–6, décharge de {{ h_2 }})</td></tr>
          <tr><td>8</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</td><td>{{ I_\Rightarrow }} (lignes 1–7, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.6 -->
<div class="q-card" id="td5_q17_6">
  <div class="q-header">
    <span class="q-num">Exercice 17 – Question 6</span>
    <span class="q-title">Preuve de {{ F_6 = (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Prouver en déduction naturelle intuitionniste la formule :</p>
    <p style="text-align:center; font-weight:bold;">{{ F_6 = (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</p>
  </div>

  <details class="sol" open>
    <summary>Preuve complète (Boîtes Sorbonne &amp; Table de Fitch)</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>On suppose {{ h_1 : A \land B }} (par {{ I_\Rightarrow }}), puis comme le but est une négation {{ \neg(\neg A \lor \neg B) }}, on applique {{ I_\neg }} en supposant {{ h_2 : \neg A \lor \neg B }} et en cherchant à prouver {{ \text{false} }}. On élimine alors la disjonction {{ h_2 }} par {{ E_\lor }} : dans la branche {{ h_3 : \neg A }}, on contredit {{ A }} (extrait de {{ h_1 }} par {{ E_\land^g }}) ; dans la branche {{ h_4 : \neg B }}, on contredit {{ B }} (extrait de {{ h_1 }} par {{ E_\land^d }}).</p>
      <pre><code>⟨1⟩ montrons (A ∧ B) ⇒ ¬(¬A ∨ ¬B) par I⇒
  ⟨2⟩ supposons h1 : A ∧ B, montrons ¬(¬A ∨ ¬B) par I¬
    ⟨3⟩ supposons h2 : ¬A ∨ ¬B, montrons false par E∨
      ⟨4⟩ montrons ¬A ∨ ¬B par Ax avec h2 ⟨4⟩
      ⟨5⟩ supposons h3 : ¬A, montrons false par E¬
        ⟨6⟩ montrons ¬A par Ax avec h3 ⟨6⟩
        ⟨7⟩ montrons A par E∧g
          ⟨8⟩ montrons A ∧ B par Ax avec h1 ⟨8⟩
        ⟨7⟩
      ⟨5⟩
      ⟨9⟩ supposons h4 : ¬B, montrons false par E¬
        ⟨10⟩ montrons ¬B par Ax avec h4 ⟨10⟩
        ⟨11⟩ montrons B par E∧d
          ⟨12⟩ montrons A ∧ B par Ax avec h1 ⟨12⟩
        ⟨11⟩
      ⟨9⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \land B }}</td><td>Hypothèse (pour {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1 }}</td><td>{{ A }}</td><td>{{ E_\land^g }} sur la ligne 1</td></tr>
          <tr><td>3</td><td>{{ h_1 }}</td><td>{{ B }}</td><td>{{ E_\land^d }} sur la ligne 1</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ \neg A \lor \neg B }}</td><td>Hypothèse (pour {{ I_\neg }})</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \neg A }}</td><td>Hypothèse Cas 1 (pour {{ E_\lor }})</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 5 et 2</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ \neg B }}</td><td>Hypothèse Cas 2 (pour {{ E_\lor }})</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 7 et 3</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\lor }} sur la ligne 4, Cas 1 (5–6) et Cas 2 (7–8)</td></tr>
          <tr><td>10</td><td>{{ h_1 }}</td><td>{{ \neg(\neg A \lor \neg B) }}</td><td>{{ I_\neg }} (lignes 4–9, décharge de {{ h_2 }})</td></tr>
          <tr><td>11</td><td>{{ \emptyset }}</td><td>{{ (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</td><td>{{ I_\Rightarrow }} (lignes 1–10, décharge de {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 18 -->
<h2 id="td5_ex18">Exercice 18 – Énigme logique : la fête d'Anissa, Boris et Chloé</h2>

<div class="q-card" id="td5_q18_1">
  <div class="q-header">
    <span class="q-num">Exercice 18 – Question 1</span>
    <span class="q-title">Formalisation propositionnelle des trois affirmations</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Anissa, Boris et Chloé sont invités à une fête. Soient les affirmations suivantes :</p>
    <ul>
      <li>{{ h_1 }} : Si Anissa vient, alors Chloé ne vient pas.</li>
      <li>{{ h_2 }} : Si Chloé vient, alors Boris vient.</li>
      <li>{{ h_3 }} : Anissa vient ou Boris ne vient pas.</li>
    </ul>
    <p>En utilisant les propositions atomiques {{ A }} (« Anissa vient »), {{ B }} (« Boris vient ») et {{ C }} (« Chloé vient »), formaliser chacune des affirmations par une formule propositionnelle.</p>
  </div>

  <details class="sol" open>
    <summary>Formalisation exacte</summary>
    <div class="box method">
      <ul>
        <li><strong>Hypothèse {{ h_1 }} :</strong> « Si Anissa vient, alors Chloé ne vient pas » se traduit par :
          <p style="text-align:center; font-weight:bold;">{{ h_1 : A \Rightarrow \neg C }}</p>
        </li>
        <li><strong>Hypothèse {{ h_2 }} :</strong> « Si Chloé vient, alors Boris vient » se traduit par :
          <p style="text-align:center; font-weight:bold;">{{ h_2 : C \Rightarrow B }}</p>
        </li>
        <li><strong>Hypothèse {{ h_3 }} :</strong> « Anissa vient ou Boris ne vient pas » se traduit par :
          <p style="text-align:center; font-weight:bold;">{{ h_3 : A \lor \neg B }}</p>
        </li>
        <li><strong>Conclusion à établir :</strong> « Chloé ne vient pas à la fête » se traduit par :
          <p style="text-align:center; font-weight:bold;">{{ \neg C }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="td5_q18_2">
  <div class="q-header">
    <span class="q-num">Exercice 18 – Question 2</span>
    <span class="q-title">Preuve en déduction naturelle de {{ \{h_1, h_2, h_3\} \vdash \neg C }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Montrer par les règles de la déduction naturelle que si les trois affirmations {{ h_1, h_2, h_3 }} sont vérifiées, alors on peut déduire que Chloé ne vient pas à la fête ({{ \neg C }}).</p>
  </div>

  <details class="sol" open>
    <summary>Preuve formelle complète en logique intuitionniste</summary>
    <div class="box method">
      <h4>Analyse stratégique</h4>
      <p>Nous cherchons à démontrer le séquent {{ h_1 : A \Rightarrow \neg C, \, h_2 : C \Rightarrow B, \, h_3 : A \lor \neg B \vdash \neg C }}. Le but {{ \neg C }} étant une négation, on commence par la règle intuitionniste {{ I_\neg }} en supposant {{ h_4 : C }} et en cherchant à établir {{ \text{false} }}.</p>
      <p>Pour obtenir {{ \text{false} }}, on procède par élimination de la disjonction {{ E_\lor }} sur l'hypothèse {{ h_3 : A \lor \neg B }} :</p>
      <ul>
        <li><strong>Cas 1 ({{ h_5 : A }}) :</strong> Avec {{ h_1 : A \Rightarrow \neg C }} et {{ h_5 : A }}, on obtient {{ \neg C }} par {{ E_\Rightarrow }}, ce qui contredit {{ h_4 : C }} par {{ E_\neg }} !</li>
        <li><strong>Cas 2 ({{ h_6 : \neg B }}) :</strong> Avec {{ h_2 : C \Rightarrow B }} et {{ h_4 : C }}, on obtient {{ B }} par {{ E_\Rightarrow }}, ce qui contredit {{ h_6 : \neg B }} par {{ E_\neg }} !</li>
      </ul>
      <pre><code>⟨1⟩ supposons h1 : A ⇒ ¬C, h2 : C ⇒ B, h3 : A ∨ ¬B
    montrons ¬C par I¬
  ⟨2⟩ supposons h4 : C, montrons false par E∨
    ⟨3⟩ montrons A ∨ ¬B par Ax avec h3 ⟨3⟩
    ⟨4⟩ supposons h5 : A, montrons false par E¬
      ⟨5⟩ montrons ¬C par E⇒
        ⟨6⟩ montrons A ⇒ ¬C par Ax avec h1 ⟨6⟩
        ⟨7⟩ montrons A par Ax avec h5 ⟨7⟩
      ⟨5⟩
      ⟨8⟩ montrons C par Ax avec h4 ⟨8⟩
    ⟨4⟩
    ⟨9⟩ supposons h6 : ¬B, montrons false par E¬
      ⟨10⟩ montrons ¬B par Ax avec h6 ⟨10⟩
      ⟨11⟩ montrons B par E⇒
        ⟨12⟩ montrons C ⇒ B par Ax avec h2 ⟨12⟩
        ⟨13⟩ montrons C par Ax avec h4 ⟨13⟩
      ⟨11⟩
    ⟨9⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>Ligne</th><th>Hypothèses actives</th><th>Formule</th><th>Justification</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow \neg C }}</td><td>Hypothèse de l'énigme</td></tr>
          <tr><td>2</td><td>{{ h_2 }}</td><td>{{ C \Rightarrow B }}</td><td>Hypothèse de l'énigme</td></tr>
          <tr><td>3</td><td>{{ h_3 }}</td><td>{{ A \lor \neg B }}</td><td>Hypothèse de l'énigme</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ C }}</td><td>Hypothèse (ouverture de sous-boîte pour {{ I_\neg }})</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ B }}</td><td>{{ E_\Rightarrow }} sur les lignes 2 et 4</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ A }}</td><td>Hypothèse Cas 1 (pour {{ E_\lor }} sur la ligne 3)</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ \neg C }}</td><td>{{ E_\Rightarrow }} sur les lignes 1 et 6</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 7 et 4</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2, h_3, h_4, h_6 }}</td><td>{{ \neg B }}</td><td>Hypothèse Cas 2 (pour {{ E_\lor }} sur la ligne 3)</td></tr>
          <tr><td>10</td><td>{{ h_1, h_2, h_3, h_4, h_6 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\neg }} sur les lignes 9 et 5</td></tr>
          <tr><td>11</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>{{ E_\lor }} sur la ligne 3, Cas 1 (6–8) et Cas 2 (9–10)</td></tr>
          <tr><td>12</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \neg C }}</td><td>{{ I_\neg }} (lignes 4–11, décharge de {{ h_4 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>
"""

td_fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>تمرین‌های فصل ۵: اثبات در استنتاج طبیعی شهودگرایانه</h1>
  <p class="lead">حل تشریحی کامل تمرین‌های ۱۷ (سوالات ۱ تا ۶) و ۱۸ (معمای مهمانی آنیسا، بوریس و کلوئه) از جزوه رسمی TD سال تحصیلی ۲۰۲۶-۲۰۲۷، به دو روش باکس‌های شماره‌گذاری‌شده سوربن و جدول خط‌به‌خط فیتش.</p>
</div>

<div class="toc-box">
  <h3>فهرست تمرین‌های این بخش</h3>
  <ul>
    <li><a href="#td5_ex17">تمرین ۱۷ – اثبات صوری ۶ قضیه در منطق شهودگرایانه</a></li>
    <li><a href="#td5_ex18">تمرین ۱۸ – معمای منطقی: مهمانی آنیسا، بوریس و کلوئه</a></li>
  </ul>
</div>

<div class="box warn">
  <h4>دستورالعمل رسمی فصل ۵ در برگه TD</h4>
  <p><em>«برای پاسخ به سوالات این فصل باید منحصراً از قواعد پایه استنتاج طبیعی شهودگرایانه استفاده کنید (بدون اصل طرد شق ثالث {{ \text{TE} }} و بدون برهان خلف کلاسیک {{ \text{Abs} }}).»</em></p>
</div>

<!-- EXERCICE 17 -->
<h2 id="td5_ex17">Exercice 17 – Preuves formelles de 6 théorèmes intuitionnistes</h2>

<!-- Q17.1 -->
<div class="q-card" id="td5_q17_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۱</span>
    <span class="q-title">اثبات فرمول {{ F_1 = (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>فرمول تعدی شرطی زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_1 = (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (باکس‌های سوربن و جدول فیتش)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>فرمول {{ F_1 }} از سه شرطی تودرتو تشکیل شده است. بنابراین سه بار متوالی قاعده معرفی شرطی {{ I_\Rightarrow }} را اعمال می‌کنیم تا سه فرض {{ h_1 : A \Rightarrow B }}، {{ h_2 : B \Rightarrow C }} و {{ h_3 : A }} باز شوند. هدف باقی‌مانده {{ C }} است که با دو بار اعمال قاعده حذف شرطی {{ E_\Rightarrow }} (قیاس استثنایی) به دست می‌آید.</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ ((B ⇒ C) ⇒ (A ⇒ C)) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons (B ⇒ C) ⇒ (A ⇒ C) par I⇒
    ⟨3⟩ supposons h2 : B ⇒ C, montrons A ⇒ C par I⇒
      ⟨4⟩ supposons h3 : A, montrons C par E⇒
        ⟨5⟩ montrons B ⇒ C par Ax avec h2 ⟨5⟩
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ B \Rightarrow C }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۱ و ۳</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ C }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۲ و ۴</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ A \Rightarrow C }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۳ تا ۵، رهاسازی {{ h_3 }})</td></tr>
          <tr><td>7</td><td>{{ h_1 }}</td><td>{{ (B \Rightarrow C) \Rightarrow (A \Rightarrow C) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۲ تا ۶، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>8</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow ((B \Rightarrow C) \Rightarrow (A \Rightarrow C)) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۷، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.2 -->
<div class="q-card" id="td5_q17_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۲</span>
    <span class="q-title">اثبات فرمول {{ F_2 = (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>فرمول زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_2 = (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (باکس‌های سوربن و جدول فیتش)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>پس از دو بار اعمال {{ I_\Rightarrow }} که فرضیات {{ h_1 : ((A \land B) \Rightarrow C) \land (A \Rightarrow B) }} و {{ h_2 : A }} را باز می‌کنند، از فرض عطفی {{ h_1 }} دو شرطی را با {{ E_\land^g }} و {{ E_\land^d }} بیرون می‌کشیم. از {{ A }} و {{ A \Rightarrow B }} گزاره {{ B }} را با {{ E_\Rightarrow }} می‌گیریم، سپس {{ A \land B }} را با {{ I_\land }} ساخته و با {{ E_\Rightarrow }} به {{ C }} می‌رسیم.</p>
      <pre><code>⟨1⟩ montrons (((A ∧ B) ⇒ C) ∧ (A ⇒ B)) ⇒ (A ⇒ C) par I⇒
  ⟨2⟩ supposons h1 : ((A ∧ B) ⇒ C) ∧ (A ⇒ B), montrons A ⇒ C par I⇒
    ⟨3⟩ supposons h2 : A, montrons C par E⇒
      ⟨4⟩ montrons (A ∧ B) ⇒ C par E∧g
        ⟨5⟩ montrons ((A ∧ B) ⇒ C) ∧ (A ⇒ B) par Ax avec h1 ⟨5⟩
      ⟨4⟩
      ⟨6⟩ montrons A ∧ B par I∧
        ⟨7⟩ montrons A par Ax avec h2 ⟨7⟩
        ⟨8⟩ montrons B par E⇒
          ⟨9⟩ montrons A ⇒ B par E∧d
            ⟨10⟩ montrons ((A ∧ B) ⇒ C) ∧ (A ⇒ B) par Ax avec h1 ⟨10⟩
          ⟨9⟩
          ⟨11⟩ montrons A par Ax avec h2 ⟨11⟩
        ⟨8⟩
      ⟨6⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ ((A \land B) \Rightarrow C) \land (A \Rightarrow B) }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2 }}</td><td>{{ (A \land B) \Rightarrow C }}</td><td>قاعده {{ E_\land^g }} روی سطر ۱</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ A \Rightarrow B }}</td><td>قاعده {{ E_\land^d }} روی سطر ۱</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2 }}</td><td>{{ B }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۴ و ۲</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ A \land B }}</td><td>قاعده {{ I_\land }} روی سطرهای ۲ و ۵</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2 }}</td><td>{{ C }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۳ و ۶</td></tr>
          <tr><td>8</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow C }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۲ تا ۷، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>9</td><td>{{ \emptyset }}</td><td>{{ (((A \land B) \Rightarrow C) \land (A \Rightarrow B)) \Rightarrow (A \Rightarrow C) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۸، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.3 -->
<div class="q-card" id="td5_q17_3">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۳</span>
    <span class="q-title">اثبات فرمول {{ F_3 = (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>فرمول یکنوایی فصل زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_3 = (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (باکس‌های سوربن و جدول فیتش)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>پس از فرض کردن {{ h_1 : A \Rightarrow B }} و {{ h_2 : A \lor C }} با {{ I_\Rightarrow }}، هدف {{ B \lor C }} است. مراقب تله باشید: اینجا نمی‌توان مستقیماً {{ I_\lor^g }} یا {{ I_\lor^d }} زد چون هنوز نمی‌دانیم کدام شاخه برقرار است! ابتدا باید فصل {{ h_2 : A \lor C }} را با {{ E_\lor }} حذف کنیم: در حالت {{ A }} به {{ B }} و سپس با {{ I_\lor^g }} به {{ B \lor C }} می‌رسیم؛ در حالت {{ C }} مستقیماً با {{ I_\lor^d }} به {{ B \lor C }} می‌رسیم.</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ ((A ∨ C) ⇒ (B ∨ C)) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons (A ∨ C) ⇒ (B ∨ C) par I⇒
    ⟨3⟩ supposons h2 : A ∨ C, montrons B ∨ C par E∨
      ⟨4⟩ montrons A ∨ C par Ax avec h2 ⟨4⟩
      ⟨5⟩ supposons h3 : A, montrons B ∨ C par I∨g
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨5⟩
      ⟨9⟩ supposons h4 : C, montrons B ∨ C par I∨d
        ⟨10⟩ montrons C par Ax avec h4 ⟨10⟩
      ⟨9⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor C }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>فرض حالت اول (برای {{ E_\lor }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۱ و ۳</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B \lor C }}</td><td>قاعده {{ I_\lor^g }} روی سطر ۴</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ C }}</td><td>فرض حالت دوم (برای {{ E_\lor }})</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ B \lor C }}</td><td>قاعده {{ I_\lor^d }} روی سطر ۶</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2 }}</td><td>{{ B \lor C }}</td><td>قاعده {{ E_\lor }} روی سطر ۲، حالت اول (۳–۵) و حالت دوم (۶–۷)</td></tr>
          <tr><td>9</td><td>{{ h_1 }}</td><td>{{ (A \lor C) \Rightarrow (B \lor C) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۲ تا ۸، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>10</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow ((A \lor C) \Rightarrow (B \lor C)) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۹، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.4 -->
<div class="q-card" id="td5_q17_4">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۴</span>
    <span class="q-title">اثبات فرمول {{ F_4 = (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>فرمول زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_4 = (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (دو استدلال بر اساس حالات تودرتو)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>پس از دو بار اعمال {{ I_\Rightarrow }}، دو فرض فصلی در اختیار داریم: {{ h_1 : A \lor (B \Rightarrow C) }} و {{ h_2 : A \lor B }}. ابتدا روی {{ h_1 }} قاعده {{ E_\lor }} را می‌زنیم:</p>
      <ul>
        <li><strong>شاخه اول ({{ h_3 : A }}) :</strong> بلافاصله با {{ I_\lor^g }} نتیجه {{ A \lor C }} حاصل می‌شود.</li>
        <li><strong>شاخه دوم ({{ h_4 : B \Rightarrow C }}) :</strong> اکنون فصل دوم یعنی {{ h_2 : A \lor B }} را با {{ E_\lor }} می‌شکنیم! در زیرحالت {{ h_5 : A }} با {{ I_\lor^g }} به {{ A \lor C }} می‌رسیم. در زیرحالت {{ h_6 : B }}، با {{ E_\Rightarrow }} و {{ h_4 }} به {{ C }} و سپس با {{ I_\lor^d }} به {{ A \lor C }} می‌رسیم.</li>
      </ul>
      <pre><code>⟨1⟩ montrons (A ∨ (B ⇒ C)) ⇒ ((A ∨ B) ⇒ (A ∨ C)) par I⇒
  ⟨2⟩ supposons h1 : A ∨ (B ⇒ C), montrons (A ∨ B) ⇒ (A ∨ C) par I⇒
    ⟨3⟩ supposons h2 : A ∨ B, montrons A ∨ C par E∨
      ⟨4⟩ montrons A ∨ (B ⇒ C) par Ax avec h1 ⟨4⟩
      ⟨5⟩ supposons h3 : A, montrons A ∨ C par I∨g
        ⟨6⟩ montrons A par Ax avec h3 ⟨6⟩
      ⟨5⟩
      ⟨7⟩ supposons h4 : B ⇒ C, montrons A ∨ C par E∨
        ⟨8⟩ montrons A ∨ B par Ax avec h2 ⟨8⟩
        ⟨9⟩ supposons h5 : A, montrons A ∨ C par I∨g
          ⟨10⟩ montrons A par Ax avec h5 ⟨10⟩
        ⟨9⟩
        ⟨11⟩ supposons h6 : B, montrons A ∨ C par I∨d
          ⟨12⟩ montrons C par E⇒
            ⟨13⟩ montrons B ⇒ C par Ax avec h4 ⟨13⟩
            ⟨14⟩ montrons B par Ax avec h6 ⟨14⟩
          ⟨12⟩
        ⟨11⟩
      ⟨7⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \lor (B \Rightarrow C) }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>فرض حالت اولِ {{ h_1 }}</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A \lor C }}</td><td>قاعده {{ I_\lor^g }} روی سطر ۳</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ B \Rightarrow C }}</td><td>فرض حالت دومِ {{ h_1 }}</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_4, h_5 }}</td><td>{{ A }}</td><td>فرض زیرحالت ۲-الف برای {{ h_2 }}</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4, h_5 }}</td><td>{{ A \lor C }}</td><td>قاعده {{ I_\lor^g }} روی سطر ۶</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ B }}</td><td>فرض زیرحالت ۲-ب برای {{ h_2 }}</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ C }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۵ و ۸</td></tr>
          <tr><td>10</td><td>{{ h_1, h_2, h_4, h_6 }}</td><td>{{ A \lor C }}</td><td>قاعده {{ I_\lor^d }} روی سطر ۹</td></tr>
          <tr><td>11</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ A \lor C }}</td><td>قاعده {{ E_\lor }} روی سطر ۲، زیرحالت‌های (۶–۷) و (۸–۱۰)</td></tr>
          <tr><td>12</td><td>{{ h_1, h_2 }}</td><td>{{ A \lor C }}</td><td>قاعده {{ E_\lor }} روی سطر ۱، حالت‌های (۳–۴) و (۵–۱۱)</td></tr>
          <tr><td>13</td><td>{{ h_1 }}</td><td>{{ (A \lor B) \Rightarrow (A \lor C) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۲ تا ۱۲، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>14</td><td>{{ \emptyset }}</td><td>{{ (A \lor (B \Rightarrow C)) \Rightarrow ((A \lor B) \Rightarrow (A \lor C)) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۱۳، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.5 -->
<div class="q-card" id="td5_q17_5">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۵</span>
    <span class="q-title">اثبات فرمول {{ F_5 = (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>قانون عکس نقیض مستقیم زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_5 = (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (باکس‌های سوربن و جدول فیتش)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>قانون عکس نقیض مستقیم {{ (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }} <strong>کاملاً شهودگرایانه است</strong> زیرا نتیجه نهایی آن یعنی {{ \neg A }} یک نقیض است! پس از معرفی {{ h_1 : A \Rightarrow B }} و {{ h_2 : \neg B }} با {{ I_\Rightarrow }}، با قاعده {{ I_\neg }} فرض {{ h_3 : A }} را باز کرده و به دنبال {{ \text{false} }} می‌گردیم. از {{ A }} و {{ A \Rightarrow B }} به {{ B }} می‌رسیم که با {{ \neg B }} توسط {{ E_\neg }} تناقض می‌دهد.</p>
      <pre><code>⟨1⟩ montrons (A ⇒ B) ⇒ (¬B ⇒ ¬A) par I⇒
  ⟨2⟩ supposons h1 : A ⇒ B, montrons ¬B ⇒ ¬A par I⇒
    ⟨3⟩ supposons h2 : ¬B, montrons ¬A par I¬
      ⟨4⟩ supposons h3 : A, montrons false par E¬
        ⟨5⟩ montrons ¬B par Ax avec h2 ⟨5⟩
        ⟨6⟩ montrons B par E⇒
          ⟨7⟩ montrons A ⇒ B par Ax avec h1 ⟨7⟩
          ⟨8⟩ montrons A par Ax avec h3 ⟨8⟩
        ⟨6⟩
      ⟨4⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1, h_2 }}</td><td>{{ \neg B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>3</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ A }}</td><td>فرض (برای {{ I_\neg }})</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ B }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۱ و ۳</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۲ و ۴</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2 }}</td><td>{{ \neg A }}</td><td>قاعده {{ I_\neg }} (سطرهای ۳ تا ۵، رهاسازی {{ h_3 }})</td></tr>
          <tr><td>7</td><td>{{ h_1 }}</td><td>{{ \neg B \Rightarrow \neg A }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۲ تا ۶، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>8</td><td>{{ \emptyset }}</td><td>{{ (A \Rightarrow B) \Rightarrow (\neg B \Rightarrow \neg A) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۷، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- Q17.6 -->
<div class="q-card" id="td5_q17_6">
  <div class="q-header">
    <span class="q-num">تمرین ۱۷ – سوال ۶</span>
    <span class="q-title">اثبات فرمول {{ F_6 = (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>فرمول زیر را در استنتاج طبیعی شهودگرایانه اثبات کنید:</p>
    <p style="text-align:center; font-weight:bold;" dir="ltr">{{ F_6 = (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</p>
  </div>

  <details class="sol" open>
    <summary>اثبات کامل (باکس‌های سوربن و جدول فیتش)</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>ابتدا {{ h_1 : A \land B }} را با {{ I_\Rightarrow }} فرض می‌کنیم. سپس چون هدف یک نقیض {{ \neg(\neg A \lor \neg B) }} است، با قاعده {{ I_\neg }} فرض {{ h_2 : \neg A \lor \neg B }} را باز کرده و به دنبال اثبات {{ \text{false} }} می‌رویم. اکنون فصل {{ h_2 }} را با {{ E_\lor }} حذف می‌کنیم: در شاخه {{ h_3 : \neg A }}، با {{ A }} (حاصل از {{ E_\land^g }} روی {{ h_1 }}) به تناقض می‌رسیم؛ در شاخه {{ h_4 : \neg B }}، با {{ B }} (حاصل از {{ E_\land^d }} روی {{ h_1 }}) به تناقض می‌رسیم.</p>
      <pre><code>⟨1⟩ montrons (A ∧ B) ⇒ ¬(¬A ∨ ¬B) par I⇒
  ⟨2⟩ supposons h1 : A ∧ B, montrons ¬(¬A ∨ ¬B) par I¬
    ⟨3⟩ supposons h2 : ¬A ∨ ¬B, montrons false par E∨
      ⟨4⟩ montrons ¬A ∨ ¬B par Ax avec h2 ⟨4⟩
      ⟨5⟩ supposons h3 : ¬A, montrons false par E¬
        ⟨6⟩ montrons ¬A par Ax avec h3 ⟨6⟩
        ⟨7⟩ montrons A par E∧g
          ⟨8⟩ montrons A ∧ B par Ax avec h1 ⟨8⟩
        ⟨7⟩
      ⟨5⟩
      ⟨9⟩ supposons h4 : ¬B, montrons false par E¬
        ⟨10⟩ montrons ¬B par Ax avec h4 ⟨10⟩
        ⟨11⟩ montrons B par E∧d
          ⟨12⟩ montrons A ∧ B par Ax avec h1 ⟨12⟩
        ⟨11⟩
      ⟨9⟩
    ⟨3⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \land B }}</td><td>فرض (برای {{ I_\Rightarrow }})</td></tr>
          <tr><td>2</td><td>{{ h_1 }}</td><td>{{ A }}</td><td>قاعده {{ E_\land^g }} روی سطر ۱</td></tr>
          <tr><td>3</td><td>{{ h_1 }}</td><td>{{ B }}</td><td>قاعده {{ E_\land^d }} روی سطر ۱</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2 }}</td><td>{{ \neg A \lor \neg B }}</td><td>فرض (برای {{ I_\neg }})</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \neg A }}</td><td>فرض حالت اول (برای {{ E_\lor }})</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۵ و ۲</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ \neg B }}</td><td>فرض حالت دوم (برای {{ E_\lor }})</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_4 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۷ و ۳</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\lor }} روی سطر ۴، حالت اول (۵–۶) و حالت دوم (۷–۸)</td></tr>
          <tr><td>10</td><td>{{ h_1 }}</td><td>{{ \neg(\neg A \lor \neg B) }}</td><td>قاعده {{ I_\neg }} (سطرهای ۴ تا ۹، رهاسازی {{ h_2 }})</td></tr>
          <tr><td>11</td><td>{{ \emptyset }}</td><td>{{ (A \land B) \Rightarrow \neg(\neg A \lor \neg B) }}</td><td>قاعده {{ I_\Rightarrow }} (سطرهای ۱ تا ۱۰، رهاسازی {{ h_1 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>

<!-- EXERCICE 18 -->
<h2 id="td5_ex18">Exercice 18 – Énigme logique : la fête d'Anissa, Boris et Chloé</h2>

<div class="q-card" id="td5_q18_1">
  <div class="q-header">
    <span class="q-num">تمرین ۱۸ – سوال ۱</span>
    <span class="q-title">صوری‌سازی گزاره‌ای سه ادعای معما</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>آنیسا، بوریس و کلوئه به یک مهمانی دعوت شده‌اند. گزاره‌های زیر مفروض هستند:</p>
    <ul>
      <li>{{ h_1 }} : اگر آنیسا بیاید، آنگاه کلوئه نمی‌آید.</li>
      <li>{{ h_2 }} : اگر کلوئه بیاید، آنگاه بوریس می‌آید.</li>
      <li>{{ h_3 }} : آنیسا می‌آید یا بوریس نمی‌آید.</li>
    </ul>
    <p>با استفاده از متغیرهای اتمی {{ A }} («آنیسا می‌آید»)، {{ B }} («بوریس می‌آید») و {{ C }} («کلوئه می‌آید»)، هر یک از ادعاها را با یک فرمول منطق گزاره‌ای صوری‌سازی کنید.</p>
  </div>

  <details class="sol" open>
    <summary>صوری‌سازی دقیق</summary>
    <div class="box method">
      <ul>
        <li><strong>فرض {{ h_1 }} :</strong> «اگر آنیسا بیاید، آنگاه کلوئه نمی‌آید» ترجمه می‌شود به:
          <p style="text-align:center; font-weight:bold;" dir="ltr">{{ h_1 : A \Rightarrow \neg C }}</p>
        </li>
        <li><strong>فرض {{ h_2 }} :</strong> «اگر کلوئه بیاید، آنگاه بوریس می‌آید» ترجمه می‌شود به:
          <p style="text-align:center; font-weight:bold;" dir="ltr">{{ h_2 : C \Rightarrow B }}</p>
        </li>
        <li><strong>فرض {{ h_3 }} :</strong> «آنیسا می‌آید یا بوریس نمی‌آید» ترجمه می‌شود به:
          <p style="text-align:center; font-weight:bold;" dir="ltr">{{ h_3 : A \lor \neg B }}</p>
        </li>
        <li><strong>نتیجه مورد نظر:</strong> «کلوئه به مهمانی نمی‌آید» ترجمه می‌شود به:
          <p style="text-align:center; font-weight:bold;" dir="ltr">{{ \neg C }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="td5_q18_2">
  <div class="q-header">
    <span class="q-num">تمرین ۱۸ – سوال ۲</span>
    <span class="q-title">اثبات در استنتاج طبیعی برای حکم {{ \{h_1, h_2, h_3\} \vdash \neg C }}</span>
  </div>
  <div class="box def">
    <h4>صورت رسمی مسئله</h4>
    <p>با استفاده از قواعد استنتاج طبیعی نشان دهید اگر هر سه گزاره {{ h_1, h_2, h_3 }} برقرار باشند، می‌توان نتیجه گرفت که کلوئه به مهمانی نمی‌آید ({{ \neg C }}).</p>
  </div>

  <details class="sol" open>
    <summary>اثبات صوری کامل در منطق شهودگرایانه</summary>
    <div class="box method">
      <h4>تحلیل راهبردی اثبات</h4>
      <p>می‌خواهیم سِکوئنت {{ h_1 : A \Rightarrow \neg C, \, h_2 : C \Rightarrow B, \, h_3 : A \lor \neg B \vdash \neg C }} را اثبات کنیم. از آنجا که هدف {{ \neg C }} یک نقیض است، با قاعده شهودگرایانه {{ I_\neg }} فرض {{ h_4 : C }} را باز کرده و به دنبال اثبات تناقض {{ \text{false} }} می‌رویم.</p>
      <p>برای رسیدن به {{ \text{false} }}، قاعده حذف فصل {{ E_\lor }} را روی فرض {{ h_3 : A \lor \neg B }} اعمال می‌کنیم:</p>
      <ul>
        <li><strong>حالت اول ({{ h_5 : A }}) :</strong> از {{ h_1 : A \Rightarrow \neg C }} و {{ h_5 : A }} با {{ E_\Rightarrow }} به {{ \neg C }} می‌رسیم، که با {{ h_4 : C }} توسط {{ E_\neg }} تناقض می‌دهد!</li>
        <li><strong>حالت دوم ({{ h_6 : \neg B }}) :</strong> از {{ h_2 : C \Rightarrow B }} و {{ h_4 : C }} با {{ E_\Rightarrow }} به {{ B }} می‌رسیم، که با {{ h_6 : \neg B }} توسط {{ E_\neg }} تناقض می‌دهد!</li>
      </ul>
      <pre><code>⟨1⟩ supposons h1 : A ⇒ ¬C, h2 : C ⇒ B, h3 : A ∨ ¬B
    montrons ¬C par I¬
  ⟨2⟩ supposons h4 : C, montrons false par E∨
    ⟨3⟩ montrons A ∨ ¬B par Ax avec h3 ⟨3⟩
    ⟨4⟩ supposons h5 : A, montrons false par E¬
      ⟨5⟩ montrons ¬C par E⇒
        ⟨6⟩ montrons A ⇒ ¬C par Ax avec h1 ⟨6⟩
        ⟨7⟩ montrons A par Ax avec h5 ⟨7⟩
      ⟨5⟩
      ⟨8⟩ montrons C par Ax avec h4 ⟨8⟩
    ⟨4⟩
    ⟨9⟩ supposons h6 : ¬B, montrons false par E¬
      ⟨10⟩ montrons ¬B par Ax avec h6 ⟨10⟩
      ⟨11⟩ montrons B par E⇒
        ⟨12⟩ montrons C ⇒ B par Ax avec h2 ⟨12⟩
        ⟨13⟩ montrons C par Ax avec h4 ⟨13⟩
      ⟨11⟩
    ⟨9⟩
  ⟨2⟩
⟨1⟩</code></pre>
      <table class="logic-table" style="width:100%; margin:10px 0;">
        <thead>
          <tr><th>سطر</th><th>فرضیات فعال</th><th>فرمول</th><th>توجیه و قاعده</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>{{ h_1 }}</td><td>{{ A \Rightarrow \neg C }}</td><td>فرض مسئله</td></tr>
          <tr><td>2</td><td>{{ h_2 }}</td><td>{{ C \Rightarrow B }}</td><td>فرض مسئله</td></tr>
          <tr><td>3</td><td>{{ h_3 }}</td><td>{{ A \lor \neg B }}</td><td>فرض مسئله</td></tr>
          <tr><td>4</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ C }}</td><td>فرض (باز کردن زیرباکس برای {{ I_\neg }})</td></tr>
          <tr><td>5</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ B }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۲ و ۴</td></tr>
          <tr><td>6</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ A }}</td><td>فرض حالت اول (برای {{ E_\lor }} روی سطر ۳)</td></tr>
          <tr><td>7</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ \neg C }}</td><td>قاعده {{ E_\Rightarrow }} روی سطرهای ۱ و ۶</td></tr>
          <tr><td>8</td><td>{{ h_1, h_2, h_3, h_4, h_5 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۷ و ۴</td></tr>
          <tr><td>9</td><td>{{ h_1, h_2, h_3, h_4, h_6 }}</td><td>{{ \neg B }}</td><td>فرض حالت دوم (برای {{ E_\lor }} روی سطر ۳)</td></tr>
          <tr><td>10</td><td>{{ h_1, h_2, h_3, h_4, h_6 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\neg }} روی سطرهای ۹ و ۵</td></tr>
          <tr><td>11</td><td>{{ h_1, h_2, h_3, h_4 }}</td><td>{{ \text{false} }} ({{ \bot }})</td><td>قاعده {{ E_\lor }} روی سطر ۳، حالت اول (۶–۸) و حالت دوم (۹–۱۰)</td></tr>
          <tr><td>12</td><td>{{ h_1, h_2, h_3 }}</td><td>{{ \neg C }}</td><td>قاعده {{ I_\neg }} (سطرهای ۴ تا ۱۱، رهاسازی {{ h_4 }})</td></tr>
        </tbody>
      </table>
    </div>
  </details>
</div>
"""

open(os.path.join(W05, 'td.fr.html'), 'w', encoding='utf-8').write(td_fr.strip())
open(os.path.join(W05, 'td.fa.html'), 'w', encoding='utf-8').write(td_fa.strip())
print("w05 td written.")
