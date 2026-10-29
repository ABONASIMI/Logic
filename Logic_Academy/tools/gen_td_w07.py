#!/usr/bin/env python3
"""Authoring generator for TD Week 7 (Thème 7 : Syntaxe de la LPPO).
Exhaustive step-by-step solutions for:
- Exercice 22: Q1, Q2 (Entiers naturels et Termes T_0(F))
- Exercice 23: Q1, Q2 (Termes avec variables T(X, F), nb_f(t), nb_g(t))
- Exercice 24: Q1, Q2, Q3, Q4 (Symboles d'une formule, arités, Free(F), clôture universelle, renommage)
- Exercice 25: Q1, Q2, Q3 (Construction de formule à trous, arbre syntaxique, clôture et renommage)
- Exercice 26: Q1, Q2, Q3 (Renommage avec une seule variable x et analyse de capture)
"""
import os

W07 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w07'
os.makedirs(W07, exist_ok=True)

fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TD Thème 7 : Syntaxe de la LPPO, Termes, Variables Libres et Renommage</h1>
  <p class="lead">Corrections intégrales et détaillées des Exercices 22 à 26 du polycopié officiel de TD (2026-2027) : définitions inductives de termes, induction structurelle, identification d'arités, calcul de {{ \text{Free}(F) }}, clôtures universelles et {{ \alpha }}-renommage sans capture.</p>
</div>

<div class="toc-box">
  <h3>Sommaire des exercices du TD</h3>
  <ul>
    <li><a href="#td7_ex22">Exercice 22 – Entiers naturels et Termes clos {{ \mathcal{T}_0(\mathcal{F}) }}</a></li>
    <li><a href="#td7_ex23">Exercice 23 – Termes avec variables et comptage inductif</a></li>
    <li><a href="#td7_ex24">Exercice 24 – Symboles d'une formule, {{ \text{Free}(F) }} et renommage</a></li>
    <li><a href="#td7_ex25">Exercice 25 – Construction de formules sous contraintes et arbre syntaxique</a></li>
    <li><a href="#td7_ex26">Exercice 26 – Renommage de variables et formules équivalentes</a></li>
  </ul>
</div>

<!-- EXERCICE 22 -->
<h2 id="td7_ex22">Exercice 22 – Entiers naturels et Termes clos {{ \mathcal{T}_0(\mathcal{F}) }}</h2>

<div class="box info">
  <h4>Cadre de l'exercice (Représentation de Peano des entiers naturels)</h4>
  <p>Soit {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_1 }} avec {{ \mathcal{F}_0 = \{a\} }} (la constante zéro) et {{ \mathcal{F}_1 = \{s\} }} (la fonction successeur unaire). Pour tout {{ n \in \mathbb{N} }}, on note {{ s^n(a) }} l'expression définie par récurrence sur {{ n }} par :</p>
  <p style="text-align:center;">{{ s^n(a) = \begin{cases} a & \text{si } n = 0 \\ s(s^k(a)) & \text{si } n = k + 1 \text{ avec } k \in \mathbb{N} \end{cases} }}</p>
</div>

<!-- Q22.1 -->
<div class="q-card" id="td7_q22_1">
  <div class="q-header">
    <span class="q-num">Exercice 22 – Question 1</span>
    <span class="q-title">Particularisation de la définition inductive de {{ \mathcal{T}_0(\mathcal{F}) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Particulariser la définition de l'ensemble de termes {{ \mathcal{T}_0(\mathcal{F}) }} (l'ensemble des termes sans variables construits sur {{ \mathcal{F} }}) pour l'ensemble {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_1 }} avec {{ \mathcal{F}_0 = \{a\} }} et {{ \mathcal{F}_1 = \{s\} }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Définition inductive particularisée à {{ \mathcal{F}_0 = \{a\} }} et {{ \mathcal{F}_1 = \{s\} }}</h4>
      <p>En appliquant la définition générale des termes clos {{ \mathcal{T}_0(\mathcal{F}) = \mathcal{T}(\emptyset, \mathcal{F}) }} au vocabulaire {{ \mathcal{F}_0 = \{a\} }} et {{ \mathcal{F}_1 = \{s\} }}, l'ensemble {{ \mathcal{T}_0(\mathcal{F}) }} est le <strong>plus petit ensemble</strong> d'expressions vérifiant les deux règles suivantes :</p>
      <ol>
        <li><strong>Cas de base (Constantes {{ \mathcal{F}_0 }}) :</strong> {{ a \in \mathcal{T}_0(\mathcal{F}) }}.</li>
        <li><strong>Étape inductive (Fonction unaire {{ s \in \mathcal{F}_1 }}) :</strong> Si {{ t \in \mathcal{T}_0(\mathcal{F}) }}, alors {{ s(t) \in \mathcal{T}_0(\mathcal{F}) }}.</li>
      </ol>
      <p><em>Remarque avec la hiérarchie {{ (\mathcal{T}_{0,k}(\mathcal{F}))_{k \in \mathbb{N}} }} du cours :</em> {{ \mathcal{T}_{0,0}(\mathcal{F}) = \{a\} }}, {{ \mathcal{T}_{0,k+1}(\mathcal{F}) = \mathcal{T}_{0,k}(\mathcal{F}) \cup \{s(t) \mid t \in \mathcal{T}_{0,k}(\mathcal{F})\} }}, et {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{k \in \mathbb{N}} \mathcal{T}_{0,k}(\mathcal{F}) }}.</p>
    </div>
  </details>
</div>

<!-- Q22.2 -->
<div class="q-card" id="td7_q22_2">
  <div class="q-header">
    <span class="q-num">Exercice 22 – Question 2</span>
    <span class="q-title">Preuve par double inclusion : {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Montrer que {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée par double inclusion (Récurrence + Induction structurelle)</summary>
    <div class="box method">
      <p>Notons {{ E = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} = \{s^n(a) \mid n \in \mathbb{N}\} }}. Démontrons l'égalité {{ \mathcal{T}_0(\mathcal{F}) = E }} par double inclusion :</p>

      <h4>1. Première inclusion : {{ E \subseteq \mathcal{T}_0(\mathcal{F}) }} (par récurrence sur {{ n \in \mathbb{N} }})</h4>
      <p>Montrons par récurrence sur {{ n \in \mathbb{N} }} la propriété {{ \mathcal{P}(n) : \text{« } s^n(a) \in \mathcal{T}_0(\mathcal{F}) \text{ »} }}.</p>
      <ul>
        <li><strong>Initialisation ({{ n = 0 }}) :</strong> Par définition, {{ s^0(a) = a }}. Or, par le cas de base de la définition de {{ \mathcal{T}_0(\mathcal{F}) }} (Question 1), {{ a \in \mathcal{T}_0(\mathcal{F}) }}. Donc {{ \mathcal{P}(0) }} est vraie.</li>
        <li><strong>Hérédité :</strong> Soit {{ k \in \mathbb{N} }} fixé. Supposons {{ \mathcal{P}(k) }} vraie, c'est-à-dire {{ s^k(a) \in \mathcal{T}_0(\mathcal{F}) }}.
          <br/>Par définition de {{ s^{k+1}(a) }}, on a {{ s^{k+1}(a) = s(s^k(a)) }}.
          <br/>Comme {{ s^k(a) \in \mathcal{T}_0(\mathcal{F}) }} par hypothèse de récurrence, la règle inductive de la Question 1 implique immédiatement {{ s(s^k(a)) \in \mathcal{T}_0(\mathcal{F}) }}, soit {{ s^{k+1}(a) \in \mathcal{T}_0(\mathcal{F}) }}. Donc {{ \mathcal{P}(k+1) }} est vraie.</li>
      </ul>
      <p>Par le principe de récurrence, pour tout {{ n \in \mathbb{N} }}, {{ s^n(a) \in \mathcal{T}_0(\mathcal{F}) }}, d'où {{ \bigcup_{n \in \mathbb{N}} \{s^n(a)\} \subseteq \mathcal{T}_0(\mathcal{F}) }}.</p>

      <h4>2. Seconde inclusion : {{ \mathcal{T}_0(\mathcal{F}) \subseteq E }} (par induction structurelle sur {{ t \in \mathcal{T}_0(\mathcal{F}) }})</h4>
      <p>Montrons par induction structurelle sur {{ t \in \mathcal{T}_0(\mathcal{F}) }} que tout terme {{ t \in \mathcal{T}_0(\mathcal{F}) }} appartient à {{ E }} (c'est-à-dire qu'il existe {{ n \in \mathbb{N} }} tel que {{ t = s^n(a) }}) :</p>
      <ul>
        <li><strong>Cas de base ({{ t = a }}) :</strong> Pour {{ n = 0 \in \mathbb{N} }}, on a {{ a = s^0(a) \in E }}.</li>
        <li><strong>Étape inductive ({{ t = s(t') }} avec {{ t' \in \mathcal{T}_0(\mathcal{F}) }}) :</strong> Supposons par hypothèse d'induction que {{ t' \in E }}. Il existe alors {{ k \in \mathbb{N} }} tel que {{ t' = s^k(a) }}.
          <br/>On en déduit que {{ t = s(t') = s(s^k(a)) = s^{k+1}(a) }}. Comme {{ k + 1 \in \mathbb{N} }}, on a bien {{ t \in E }}.</li>
      </ul>
      <p>Par le principe d'induction structurelle (puisque {{ \mathcal{T}_0(\mathcal{F}) }} est le plus petit ensemble clos par ces deux règles), on conclut que {{ \mathcal{T}_0(\mathcal{F}) \subseteq E }}. Ainsi, {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 23 -->
<h2 id="td7_ex23">Exercice 23 – Termes avec variables et comptage inductif</h2>

<!-- Q23.1 -->
<div class="q-card" id="td7_q23_1">
  <div class="q-header">
    <span class="q-num">Exercice 23 – Question 1</span>
    <span class="q-title">Particularisation de {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} pour {{ \mathcal{X} = \{x\} }} et {{ \mathcal{F}_1 = \{f, g\} }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Particulariser la définition de l'ensemble de termes {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} pour {{ \mathcal{X} = \{x\} }} et {{ \mathcal{F} = \mathcal{F}_1 = \{f, g\} }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Définition inductive particularisée</h4>
      <p>Ici, {{ \mathcal{X} = \{x\} }}, {{ \mathcal{F}_0 = \emptyset }} (aucune constante) et {{ \mathcal{F}_1 = \{f, g\} }} (deux fonctions unaires). L'ensemble {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} est le <strong>plus petit ensemble</strong> vérifiant :</p>
      <ol>
        <li><strong>Cas de base (Variable {{ \mathcal{X} }}) :</strong> {{ x \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}.</li>
        <li><strong>Étape inductive (Fonctions unaires {{ \mathcal{F}_1 }}) :</strong> Si {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}, alors {{ f(t) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} et {{ g(t) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}.</li>
      </ol>
      <p><em>Exemples de termes de cet ensemble :</em> {{ x }}, {{ f(x) }}, {{ g(x) }}, {{ f(g(f(x))) }}, etc.</p>
    </div>
  </details>
</div>

<!-- Q23.2 -->
<div class="q-card" id="td7_q23_2">
  <div class="q-header">
    <span class="q-num">Exercice 23 – Question 2</span>
    <span class="q-title">Définition inductive de {{ \text{nb}_f(t) }} et {{ \text{nb}_g(t) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Donner une définition inductive du nombre {{ \text{nb}_f(t) }} de symboles {{ f }} et du nombre {{ \text{nb}_g(t) }} de symboles {{ g }} apparaissant dans un terme {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Définitions par induction structurelle sur {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</h4>
      <p>Comme tout terme {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} s'écrit de manière unique sous l'une des trois formes {{ x }}, {{ f(t') }} ou {{ g(t') }} avec {{ t' \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}, on définit {{ \text{nb}_f : \mathcal{T}(\mathcal{X}, \mathcal{F}) \to \mathbb{N} }} et {{ \text{nb}_g : \mathcal{T}(\mathcal{X}, \mathcal{F}) \to \mathbb{N} }} par :</p>
      <div style="margin:10px 0; text-align:center;">
        {{ \text{nb}_f(t) = \begin{cases} 0 & \text{si } t = x \\ 1 + \text{nb}_f(t') & \text{si } t = f(t') \\ \text{nb}_f(t') & \text{si } t = g(t') \end{cases} \qquad \text{et} \qquad \text{nb}_g(t) = \begin{cases} 0 & \text{si } t = x \\ \text{nb}_g(t') & \text{si } t = f(t') \\ 1 + \text{nb}_g(t') & \text{si } t = g(t') \end{cases} }}
      </div>
      <p><em>Exemple de vérification :</em> Pour {{ t = f(g(f(x))) }}, on obtient {{ \text{nb}_f(t) = 1 + \text{nb}_f(g(f(x))) = 1 + \text{nb}_f(f(x)) = 1 + 1 + \text{nb}_f(x) = 2 }}, et {{ \text{nb}_g(t) = \text{nb}_g(g(f(x))) = 1 + \text{nb}_g(f(x)) = 1 + \text{nb}_g(x) = 1 }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 24 -->
<h2 id="td7_ex24">Exercice 24 – Symboles d'une formule, {{ \text{Free}(F) }} et renommage</h2>

<div class="box info">
  <h4>Formule étudiée dans l'Exercice 24</h4>
  <p>On considère la formule {{ F \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} où {{ \mathcal{X} = \{x, x_1, x_2, x_3, z\} }} définie par :</p>
  <p style="text-align:center;">{{ F = \big(\forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z)))\big) }}</p>
</div>

<!-- Q24.1 & Q24.2 -->
<div class="q-card" id="td7_q24_1_2">
  <div class="q-header">
    <span class="q-num">Exercice 24 – Questions 1 &amp; 2</span>
    <span class="q-title">Identification des symboles de fonction et de prédicat et de leurs arités</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <ol>
      <li>Quels sont les symboles de fonction apparaissant dans {{ F }} ? Préciser leur arité.</li>
      <li>Quels sont les symboles de prédicat apparaissant dans {{ F }} ? Préciser leur arité.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>1. Symboles de fonction et arités (Question 1)</h4>
      <p>Inspectons les arguments passés à l'intérieur des atomes {{ s_1(s_2(x, x)) }}, {{ s_1(s_2(x, z)) }} et {{ s_3(s_4(x)) }} :</p>
      <ul>
        <li><strong>{{ s_2 }} est un symbole de fonction d'arité 2 ({{ s_2 \in \mathcal{F}_2 }}) :</strong> il apparaît en position d'argument de {{ s_1 }} et prend deux termes ({{ x, x }} ou {{ x, z }}) entre ses parenthèses.</li>
        <li><strong>{{ s_4 }} est un symbole de fonction d'arité 1 ({{ s_4 \in \mathcal{F}_1 }}) :</strong> il apparaît en position d'argument de {{ s_3 }} et prend un seul terme ({{ x }}) entre ses parenthèses.</li>
      </ul>
      <p>Il n'y a aucune constante ({{ \mathcal{F}_0 = \emptyset }}), car {{ x }} et {{ z }} appartiennent à {{ \mathcal{X} }}.</p>

      <h4>2. Symboles de prédicat et arités (Question 2)</h4>
      <p>Inspectons les symboles placés directement sous les connecteurs {{ \land }} et les quantificateurs {{ \forall x, \exists x }} :</p>
      <ul>
        <li><strong>{{ s_1 }} est un symbole de prédicat d'arité 1 ({{ s_1 \in \mathcal{P}_1 }}) :</strong> dans {{ s_1(s_2(x, x)) }} et {{ s_1(s_2(x, z)) }}, {{ s_1 }} est directement relié par {{ \land }} ou quantifié par {{ \exists x }}, et reçoit un unique terme {{ s_2(\dots) }} en argument.</li>
        <li><strong>{{ s_3 }} est un symbole de prédicat d'arité 1 ({{ s_3 \in \mathcal{P}_1 }}) :</strong> dans {{ s_3(s_4(x)) }}, {{ s_3 }} est directement relié par {{ \land }} et reçoit un unique terme {{ s_4(x) }} en argument.</li>
      </ul>
    </div>
  </details>
</div>

<!-- Q24.3 -->
<div class="q-card" id="td7_q24_3">
  <div class="q-header">
    <span class="q-num">Exercice 24 – Question 3</span>
    <span class="q-title">Ensemble des variables libres {{ \text{Free}(F) }} et clôture universelle</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Déterminer l'ensemble {{ \text{Free}(F) }} des variables libres de {{ F }} et donner une clôture universelle de {{ F }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>1. Calcul détaillé de {{ \text{Free}(F) }}</h4>
      <p>Posons {{ F = G_1 \land G_2 }} avec :</p>
      <ul>
        <li>{{ G_1 = \forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z))) }} :
          <br/>{{ \text{Free}(G_1) = \big(\text{Free}(s_1(s_2(x, x))) \cup \text{Free}(\exists x \, s_1(s_2(x, z)))\big) \setminus \{x\} = \big(\{x\} \cup (\{x, z\} \setminus \{x\})\big) \setminus \{x\} = \{x, z\} \setminus \{x\} = \{z\} }}.
          <br/>Dans {{ G_1 }}, toutes les occurrences de {{ x }} sont liées, mais l'occurrence de {{ z }} est <strong>libre</strong>.</li>
        <li>{{ G_2 = s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z))) }} :
          <br/>{{ \text{Free}(G_2) = \text{Free}(s_3(s_4(x))) \cup \text{Free}(\exists x \, s_1(s_2(x, z))) = \{x\} \cup (\{x, z\} \setminus \{x\}) = \{x\} \cup \{z\} = \{x, z\} }}.
          <br/>En effet, dans {{ s_3(s_4(x)) }}, l'occurrence de {{ x }} n'est dans la portée d'aucun quantificateur (le {{ \forall x }} de {{ G_1 }} a refermé sa portée avant le {{ \land }} principal !). Elle est donc <strong>libre</strong>.</li>
      </ul>
      <p>Par union, on obtient :</p>
      <p style="text-align:center;">{{ \text{Free}(F) = \text{Free}(G_1) \cup \text{Free}(G_2) = \{z\} \cup \{x, z\} = \{x, z\} }}</p>

      <h4>2. Clôture universelle de {{ F }}</h4>
      <p>Pour fermer universellement {{ F }}, on quantifie universellement toutes les variables de {{ \text{Free}(F) = \{x, z\} }} en tête de la formule :</p>
      <p style="text-align:center;">{{ \tilde{\forall} F = \forall x \forall z \, \Big( \big(\forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z)))\big) \Big) }}</p>
      <p><em>(Note : {{ \forall z \forall x \, F }} est également une clôture universelle correcte.)</em></p>
    </div>
  </details>
</div>

<!-- Q24.4 -->
<div class="q-card" id="td7_q24_4">
  <div class="q-header">
    <span class="q-num">Exercice 24 – Question 4</span>
    <span class="q-title">Renommage sans capture des variables liées de {{ F }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Renommer certaines variables de {{ F }} afin d'obtenir une formule logiquement équivalente dans laquelle les quantificateurs portent sur des variables différentes.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Analyse des portées et renommage avec {{ x_1, x_2, x_3 \in \mathcal{X} }}</h4>
      <p>Attention aux deux pièges classiques :</p>
      <ol>
        <li>Dans {{ \forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z))) }}, le second quantificateur {{ \exists x }} est <em>imbriqué</em> dans la portée du {{ \forall x }}, mais il masque (redéfinit) {{ x }} dans sa propre sous-formule {{ s_1(s_2(x, z)) }}. Ainsi, le premier {{ \forall x }} ne lie que {{ s_1(s_2(x, x)) }}, tandis que le {{ \exists x }} interne lie le {{ x }} de {{ s_1(s_2(x, z)) }}.</li>
        <li>L'occurrence de {{ x }} dans {{ s_3(s_4(x)) }} et les deux occurrences de {{ z }} sont <strong>libres</strong> : on n'a <strong>pas le droit de renommer une variable libre</strong> (sinon on change le sens de la formule !).</li>
      </ol>
      <p>En utilisant les variables fraîches {{ x_1, x_2, x_3 \in \mathcal{X} }} pour les trois quantificateurs, on obtient la formule logiquement équivalente :</p>
      <p style="text-align:center;">{{ F_{\text{ren}} = \big(\forall x_1 \, (s_1(s_2(x_1, x_1)) \land \exists x_2 \, s_1(s_2(x_2, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x_3 \, s_1(s_2(x_3, z)))\big) }}</p>
    </div>
  </details>
</div>

<!-- EXERCICE 25 -->
<h2 id="td7_ex25">Exercice 25 – Construction de formules sous contraintes et arbre syntaxique</h2>

<div class="box info">
  <h4>Énoncé et contraintes de l'Exercice 25</h4>
  <p>Soient {{ \mathcal{X} = \{x, y, z\} }}, {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_2 }} avec {{ \mathcal{F}_0 = \{k\} }} et {{ \mathcal{F}_2 = \{f\} }}, et {{ \mathcal{P} = \mathcal{P}_1 \cup \mathcal{P}_2 }} avec {{ \mathcal{P}_1 = \{p\} }} et {{ \mathcal{P}_2 = \{q\} }}. On considère le squelette de formule suivant :</p>
  <p style="text-align:center;">{{ F = (\forall y \, \Box(\Box, \Box(\Box, \Box))) \Rightarrow ((\Box \Box \exists \Box \, \Box(\Box(\Box, \Box))) \lor \Box(\Box, \Box)) }}</p>
  <p>Chaque case {{ \Box }} doit contenir un unique symbole (variable, fonction, prédicat ou quantificateur) de sorte que :</p>
  <ul>
    <li>{{ x }} admette uniquement <strong>2 occurrences libres</strong> et <strong>1 occurrence liée par {{ \forall }}</strong> dans {{ F }} ;</li>
    <li>{{ y }} admette uniquement <strong>1 occurrence liée par {{ \forall }}</strong> et <strong>1 occurrence liée par {{ \exists }}</strong> dans {{ F }} ;</li>
    <li>{{ z }} admette uniquement <strong>1 occurrence libre</strong> dans {{ F }}.</li>
  </ul>
</div>

<!-- Q25.1 -->
<div class="q-card" id="td7_q25_1">
  <div class="q-header">
    <span class="q-num">Exercice 25 – Question 1</span>
    <span class="q-title">Remplissage raisonné des cases de {{ F }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Remplir les cases de {{ F }} en respectant les contraintes sur {{ \mathcal{X}, \mathcal{F}, \mathcal{P} }} et sur les occurrences libres et liées de {{ x, y, z }}.</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Déduction unique de la structure syntaxique</h4>
      <ol>
        <li><strong>Identification des prédicats et des fonctions par l'arité des parenthèses :</strong>
          <ul>
            <li>Dans {{ \forall y \, \Box(\Box, \Box(\Box, \Box)) }} : le symbole de tête a 2 arguments et est sous {{ \forall y }}, c'est donc le prédicat binaire {{ q \in \mathcal{P}_2 }}. Son second argument {{ \Box(\Box, \Box) }} est un terme d'arité 2, donc construit avec la fonction binaire {{ f \in \mathcal{F}_2 }}. On a donc {{ \forall y \, q(\Box, f(\Box, \Box)) }}.</li>
            <li>Dans {{ \Box \Box \exists \Box \, \Box(\Box(\Box, \Box)) }} : les deux premières cases devant {{ \exists \Box }} doivent former un quantificateur universel sur {{ x }} (puisque {{ x }} doit avoir 1 occurrence liée par {{ \forall }} et qu'aucun {{ \forall x }} n'est encore écrit !), donc {{ \forall x \exists y }}. Le corps {{ \Box(\Box(\Box, \Box)) }} a un symbole de tête d'arité 1 (le prédicat unaire {{ p \in \mathcal{P}_1 }}) appliqué à un terme d'arité 2 (la fonction {{ f \in \mathcal{F}_2 }}), soit {{ \forall x \exists y \, p(f(\Box, \Box)) }}.</li>
            <li>Dans {{ \lor \, \Box(\Box, \Box) }} : le symbole de tête est sous {{ \lor }} et d'arité 2, c'est donc le prédicat binaire {{ q \in \mathcal{P}_2 }}, soit {{ q(\Box, \Box) }}.</li>
          </ul>
        </li>
        <li><strong>Placement des variables {{ x, y, z }} et de la constante {{ k }} :</strong>
          <ul>
            <li>Sous {{ \forall x \exists y \, p(f(\Box, \Box)) }}, {{ x }} doit être liée par {{ \forall x }} et {{ y }} par {{ \exists y }}, ce qui donne {{ \forall x \exists y \, p(f(x, y)) }}.</li>
            <li>Dans la branche droite {{ q(\Box, \Box) }} (hors de tout quantificateur), on doit placer la 2e occurrence libre de {{ x }} et l'unique occurrence libre de {{ z }}, par exemple {{ q(x, z) }}.</li>
            <li>Dans la branche gauche {{ \forall y \, q(\Box, f(\Box, \Box)) }}, il reste à placer la 1re occurrence libre de {{ x }}, l'unique occurrence de {{ y }} liée par {{ \forall y }}, et la constante {{ k \in \mathcal{F}_0 }} (car toutes les occurrences permises de {{ x, y, z }} sont épuisées !), par exemple {{ \forall y \, q(x, f(y, k)) }}.</li>
          </ul>
        </li>
      </ol>
      <p><strong>Formule complète obtenue :</strong></p>
      <p style="text-align:center;">{{ F = \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x \exists y \, p(f(x, y))) \lor q(x, z)\big) }}</p>
    </div>
  </details>
</div>

<!-- Q25.2 & Q25.3 -->
<div class="q-card" id="td7_q25_2_3">
  <div class="q-header">
    <span class="q-num">Exercice 25 – Questions 2 &amp; 3</span>
    <span class="q-title">Arbre syntaxique, occurrences libres, clôture universelle {{ F' }} et renommage {{ F'' }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <ol start="2">
      <li>Dessiner l'arbre de syntaxe de {{ F }} et encadrer les occurrences libres de variable.</li>
      <li>Proposer une clôture universelle {{ F' }} de {{ F }} puis renommer certains symboles de variable de {{ F' }} pour obtenir une formule {{ F'' }} logiquement équivalente dans laquelle tous les quantificateurs portent sur des variables différentes.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>1. Arbre syntaxique de {{ F }} et occurrences libres encadrées (Question 2)</h4>
      <p>Dans l'arbre ci-dessous, les trois feuilles correspondant à des occurrences libres sont encadrées par <code>[x]</code> et <code>[z]</code> :</p>
      <pre><code>                        (⇒)
                       /   \
                    (∀y)   (∨)
                     |     /  \
                    (q)  (∀x) (q)
                    / \    |   / \
                  [x] (f)(∃y)[x] [z]
                      / \  |
                     y  k (p)
                           |
                          (f)
                          / \
                         x   y</code></pre>
      <p>On vérifie que {{ \text{Free}(F) = \{x, z\} }}.</p>

      <h4>2. Clôture universelle {{ F' }} et forme renommée {{ F'' }} (Question 3)</h4>
      <ul>
        <li><strong>Clôture universelle {{ F' }} :</strong> En préfixant {{ F }} par {{ \forall x \forall z }}, on lie les occurrences libres de {{ x }} et {{ z }} :
          <div style="margin:6px 0; text-align:center;">{{ F' = \forall x \forall z \, \Big( \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x \exists y \, p(f(x, y))) \lor q(x, z)\big) \Big) }}</div>
        </li>
        <li><strong>Renommage sans capture {{ F'' }} :</strong> Dans {{ F' }}, il y a 5 quantificateurs ({{ \forall x }}, {{ \forall z }}, {{ \forall y }}, puis {{ \forall x }}, {{ \exists y }}). Renommons le second {{ \forall x }} en {{ \forall x_1 }} et le {{ \exists y }} en {{ \exists y_1 }} :
          <div style="margin:6px 0; text-align:center;">{{ F'' = \forall x \forall z \, \Big( \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x_1 \exists y_1 \, p(f(x_1, y_1))) \lor q(x, z)\big) \Big) }}</div>
          Tous les 5 quantificateurs ({{ \forall x, \forall z, \forall y, \forall x_1, \exists y_1 }}) portent désormais sur des variables deux à deux distinctes !
        </li>
      </ul>
    </div>
  </details>
</div>

<!-- EXERCICE 26 -->
<h2 id="td7_ex26">Exercice 26 – Renommage de variables et formules équivalentes</h2>

<div class="box info">
  <h4>Problème posé dans l'Exercice 26</h4>
  <p>Pour chacune des formules {{ F_1, F_2, F_3 }} suivantes, peut-on renommer certaines variables de {{ F_i }} pour obtenir une formule {{ F'_i }} logiquement équivalente telle que la <strong>seule variable apparaissant dans {{ F'_i }} soit {{ x }}</strong> ?</p>
</div>

<!-- Q26.1 -->
<div class="q-card" id="td7_q26_1">
  <div class="q-header">
    <span class="q-num">Exercice 26 – Question 1</span>
    <span class="q-title">Étude de {{ F_1 = \exists y \, (p(y) \land \forall x \, p(x)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Peut-on renommer certaines variables de {{ F_1 = \exists y \, (p(y) \land \forall x \, p(x)) }} pour obtenir {{ F'_1 \equiv F_1 }} n'utilisant que la variable {{ x }} ?</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Réponse : OUI</h4>
      <p>Dans la sous-formule {{ G = p(y) \land \forall x \, p(x) }} située sous {{ \exists y }}, vérifions les conditions de renommage de la variable liée {{ y }} en {{ x }} :</p>
      <ul>
        <li>{{ x \notin \text{Free}(G) }}, car la seule occurrence de {{ x }} dans {{ G }} est déjà liée par {{ \forall x }} ({{ \text{Free}(G) = \{y\} }}) ;</li>
        <li>L'unique occurrence de {{ y }} dans {{ G }} est dans {{ p(y) }}, qui se trouve <strong>en dehors</strong> de la portée du quantificateur interne {{ \forall x }}. Elle ne sera donc pas capturée par {{ \forall x }} !</li>
      </ul>
      <p>On peut donc légitimement renommer {{ \exists y }} en {{ \exists x }} pour obtenir la formule équivalente :</p>
      <p style="text-align:center;">{{ F'_1 = \exists x \, (p(x) \land \forall x \, p(x)) }}</p>
      <p>Dans {{ F'_1 }}, le premier {{ p(x) }} est lié au {{ \exists x }} externe et le second {{ p(x) }} est lié au {{ \forall x }} interne, exactement comme dans {{ F_1 }}.</p>
    </div>
  </details>
</div>

<!-- Q26.2 -->
<div class="q-card" id="td7_q26_2">
  <div class="q-header">
    <span class="q-num">Exercice 26 – Question 2</span>
    <span class="q-title">Étude de {{ F_2 = (\exists y \, p(y)) \Rightarrow (p(x) \lor (\forall z \, p(z))) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Peut-on renommer certaines variables de {{ F_2 = (\exists y \, p(y)) \Rightarrow (p(x) \lor (\forall z \, p(z))) }} pour obtenir {{ F'_2 \equiv F_2 }} n'utilisant que la variable {{ x }} ?</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Réponse : OUI</h4>
      <p>Les portées des quantificateurs {{ \exists y }} (qui est {{ p(y) }}) et {{ \forall z }} (qui est {{ p(z) }}) sont totalement disjointes entre elles et disjointes de l'occurrence libre {{ p(x) }} :</p>
      <ul>
        <li>Dans {{ \exists y \, p(y) }}, {{ x \notin \text{Free}(p(y)) }}, donc {{ \exists y \, p(y) \equiv \exists x \, p(x) }}.</li>
        <li>Dans {{ \forall z \, p(z) }}, {{ x \notin \text{Free}(p(z)) }}, donc {{ \forall z \, p(z) \equiv \forall x \, p(x) }}.</li>
        <li>L'occurrence libre de {{ x }} dans {{ p(x) }} est en dehors des portées de ces deux quantificateurs et reste libre.</li>
      </ul>
      <p>On obtient donc la formule logiquement équivalente n'utilisant que {{ x }} :</p>
      <p style="text-align:center;">{{ F'_2 = (\exists x \, p(x)) \Rightarrow (p(x) \lor (\forall x \, p(x))) }}</p>
    </div>
  </details>
</div>

<!-- Q26.3 -->
<div class="q-card" id="td7_q26_3">
  <div class="q-header">
    <span class="q-num">Exercice 26 – Question 3</span>
    <span class="q-title">Étude de {{ F_3 = (\forall x \exists y \, (p(y) \Rightarrow p(x))) \lor (\forall z \, p(z) \land p(y)) }}</span>
  </div>
  <div class="box def">
    <h4>Énoncé original</h4>
    <p>Peut-on renommer certaines variables de {{ F_3 = (\forall x \exists y \, (p(y) \Rightarrow p(x))) \lor (\forall z \, p(z) \land p(y)) }} pour obtenir {{ F'_3 \equiv F_3 }} n'utilisant que la variable {{ x }} ?</p>
  </div>

  <details class="sol" open>
    <summary>Solution détaillée pas à pas</summary>
    <div class="box method">
      <h4>Réponse : NON (Impossibilité absolue pour deux raisons indépendantes)</h4>
      <ol>
        <li><strong>Capture de variable dans les quantificateurs imbriqués {{ \forall x \exists y \, (p(y) \Rightarrow p(x)) }} :</strong>
          <br/>Dans la sous-formule {{ \exists y \, (p(y) \Rightarrow p(x)) }}, la variable {{ x }} possède une occurrence <strong>libre</strong> ({{ x \in \text{Free}(p(y) \Rightarrow p(x)) }}), qui est liée au {{ \forall x }} englobant. Si l'on renomme {{ \exists y }} en {{ \exists x }}, on obtient {{ \forall x \exists x \, (p(x) \Rightarrow p(x)) }} : l'occurrence de {{ x }} dans le conséquent est alors <strong>capturée</strong> par le {{ \exists x }} interne (et la sous-formule devient trivialement vraie au lieu d'exprimer une relation entre deux individus {{ x }} et {{ y }} indépendants). Il faut obligatoirement au moins deux noms de variables distincts pour exprimer {{ \forall x \exists y \, (p(y) \Rightarrow p(x)) }}.</li>
        <li><strong>Présence d'une occurrence libre de {{ y }} :</strong>
          <br/>De plus, dans {{ (\forall z \, p(z) \land p(y)) }}, l'occurrence de {{ y }} dans {{ p(y) }} est <strong>libre</strong> ({{ y \in \text{Free}(F_3) }}). Or l'{{ \alpha }}-renommage ne s'applique qu'aux variables liées : renommer une variable libre {{ y }} en {{ x }} change la sémantique de la formule (pour une valuation {{ v }} telle que {{ v(x) \neq v(y) }}).</li>
      </ol>
    </div>
  </details>
</div>
"""

fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>حل تمرین (TD) فصل ۷: نحو LPPO، ترم‌ها، متغیرهای آزاد و تغییرنام</h1>
  <p class="lead">پاسخ‌نامه تشریحی و گام‌به‌گام تمرین‌های ۲۲ تا ۲۶ جزوه رسمی TD (سال ۲۰۲۶-۲۰۲۷): تعاریف استقرایی ترم‌ها، استقرای ساختاری، تشخیص ظرفیت نمادها، محاسبه {{ \text{Free}(F) }}، بستار کلی و {{ \alpha }}-تغییرنام بدون اسارت.</p>
</div>

<div class="toc-box">
  <h3>فهرست تمرین‌های فصل ۷</h3>
  <ul>
    <li><a href="#td7_ex22">تمرین ۲۲ – اعداد طبیعی و ترم‌های بسته {{ \mathcal{T}_0(\mathcal{F}) }}</a></li>
    <li><a href="#td7_ex23">تمرین ۲۳ – ترم‌های متغیردار و شمارش استقرایی</a></li>
    <li><a href="#td7_ex24">تمرین ۲۴ – نمادهای یک فرمول، {{ \text{Free}(F) }} و تغییرنام</a></li>
    <li><a href="#td7_ex25">تمرین ۲۵ – ساخت فرمول با قیود نحوی و درخت نحوی</a></li>
    <li><a href="#td7_ex26">تمرین ۲۶ – تغییرنام متغیرها و فرمول‌های هم‌ارز</a></li>
  </ul>
</div>

<!-- EXERCICE 22 -->
<h2 id="td7_ex22">Exercice 22 – Entiers naturels et Termes clos {{ \mathcal{T}_0(\mathcal{F}) }}</h2>

<div class="box info">
  <h4>چارچوب تمرین (نمایش پئانو برای اعداد طبیعی)</h4>
  <p>فرض کنید {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_1 }} که در آن {{ \mathcal{F}_0 = \{a\} }} (ثابت صفر) و {{ \mathcal{F}_1 = \{s\} }} (تابع یک‌تایی تالی) است. برای هر {{ n \in \mathbb{N} }}، عبارت {{ s^n(a) }} به صورت بازگشتی روی {{ n }} چنین تعریف می‌شود:</p>
  <p style="text-align:center;">{{ s^n(a) = \begin{cases} a & \text{si } n = 0 \\ s(s^k(a)) & \text{si } n = k + 1 \text{ avec } k \in \mathbb{N} \end{cases} }}</p>
</div>

<!-- Q22.1 -->
<div class="q-card" id="td7_q22_1">
  <div class="q-header">
    <span class="q-num">تمرین ۲۲ – سؤال ۱</span>
    <span class="q-title">شخصی‌سازی تعریف استقرایی {{ \mathcal{T}_0(\mathcal{F}) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>تعریف مجموعه ترم‌های بسته {{ \mathcal{T}_0(\mathcal{F}) }} (مجموعه ترم‌های بدون متغیر ساخته‌شده روی {{ \mathcal{F} }}) را برای {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_1 }} با {{ \mathcal{F}_0 = \{a\} }} و {{ \mathcal{F}_1 = \{s\} }} شخصی‌سازی کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>تعریف استقرایی ویژه {{ \mathcal{F}_0 = \{a\} }} و {{ \mathcal{F}_1 = \{s\} }}</h4>
      <p>با اعمال تعریف کلی ترم‌های بسته {{ \mathcal{T}_0(\mathcal{F}) = \mathcal{T}(\emptyset, \mathcal{F}) }} بر الفبای {{ \mathcal{F}_0 = \{a\} }} و {{ \mathcal{F}_1 = \{s\} }}، مجموعه {{ \mathcal{T}_0(\mathcal{F}) }} <strong>کوچک‌ترین مجموعه</strong> از عباراتی است که در دو قاعده زیر صدق می‌کند:</p>
      <ol>
        <li><strong>حالت پایه (ثابت‌ها {{ \mathcal{F}_0 }}) :</strong> {{ a \in \mathcal{T}_0(\mathcal{F}) }}.</li>
        <li><strong>گام استقرایی (تابع یک‌تایی {{ s \in \mathcal{F}_1 }}) :</strong> اگر {{ t \in \mathcal{T}_0(\mathcal{F}) }} باشد، آنگاه {{ s(t) \in \mathcal{T}_0(\mathcal{F}) }} است.</li>
      </ol>
      <p><em>نکته با سلسله‌مراتب {{ (\mathcal{T}_{0,k}(\mathcal{F}))_{k \in \mathbb{N}} }} درس :</em> داریم {{ \mathcal{T}_{0,0}(\mathcal{F}) = \{a\} }}، {{ \mathcal{T}_{0,k+1}(\mathcal{F}) = \mathcal{T}_{0,k}(\mathcal{F}) \cup \{s(t) \mid t \in \mathcal{T}_{0,k}(\mathcal{F})\} }} و {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{k \in \mathbb{N}} \mathcal{T}_{0,k}(\mathcal{F}) }}.</p>
    </div>
  </details>
</div>

<!-- Q22.2 -->
<div class="q-card" id="td7_q22_2">
  <div class="q-header">
    <span class="q-num">تمرین ۲۲ – سؤال ۲</span>
    <span class="q-title">اثبات با زیرمجموعه‌بودن دوطرفه: {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>نشان دهید که {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی با شمول دوطرفه (استقرای ریاضی + استقرای ساختاری)</summary>
    <div class="box method">
      <p>مجموعه سمت راست را {{ E = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} = \{s^n(a) \mid n \in \mathbb{N}\} }} می‌نامیم. تساوی {{ \mathcal{T}_0(\mathcal{F}) = E }} را با اثبات دو رابطه زیرمجموعه‌بودن نشان می‌دهیم:</p>

      <h4>۱. شمول اول: {{ E \subseteq \mathcal{T}_0(\mathcal{F}) }} (با استقرای ریاضی روی {{ n \in \mathbb{N} }})</h4>
      <p>با استقرای ریاضی روی {{ n \in \mathbb{N} }} حکم {{ \mathcal{P}(n) : \text{« } s^n(a) \in \mathcal{T}_0(\mathcal{F}) \text{ »} }} را ثابت می‌کنیم.</p>
      <ul>
        <li><strong>پایه استقرا ({{ n = 0 }}) :</strong> طبق تعریف، {{ s^0(a) = a }}. از طرفی طبق قاعده پایه در تعریف {{ \mathcal{T}_0(\mathcal{F}) }} (سؤال ۱)، داریم {{ a \in \mathcal{T}_0(\mathcal{F}) }}. پس {{ \mathcal{P}(0) }} برقرار است.</li>
        <li><strong>گام استقرا :</strong> فرض کنیم برای {{ k \in \mathbb{N} }} حکم {{ \mathcal{P}(k) }} درست باشد، یعنی {{ s^k(a) \in \mathcal{T}_0(\mathcal{F}) }}.
          <br/>طبق تعریف بازگشتی {{ s^{k+1}(a) }} داریم {{ s^{k+1}(a) = s(s^k(a)) }}.
          <br/>چون طبق فرض استقرا {{ s^k(a) \in \mathcal{T}_0(\mathcal{F}) }} است، قاعده استقرایی سؤال ۱ نتیجه می‌دهد که {{ s(s^k(a)) \in \mathcal{T}_0(\mathcal{F}) }}، یعنی {{ s^{k+1}(a) \in \mathcal{T}_0(\mathcal{F}) }}. پس {{ \mathcal{P}(k+1) }} نیز برقرار است.</li>
      </ul>
      <p>بنابراین برای هر {{ n \in \mathbb{N} }} داریم {{ s^n(a) \in \mathcal{T}_0(\mathcal{F}) }}، و در نتیجه {{ \bigcup_{n \in \mathbb{N}} \{s^n(a)\} \subseteq \mathcal{T}_0(\mathcal{F}) }}.</p>

      <h4>۲. شمول دوم: {{ \mathcal{T}_0(\mathcal{F}) \subseteq E }} (با استقرای ساختاری روی {{ t \in \mathcal{T}_0(\mathcal{F}) }})</h4>
      <p>با استقرای ساختاری روی ترم {{ t \in \mathcal{T}_0(\mathcal{F}) }} ثابت می‌کنیم که هر {{ t \in \mathcal{T}_0(\mathcal{F}) }} متعلق به {{ E }} است (یعنی {{ n \in \mathbb{N} }} وجود دارد که {{ t = s^n(a) }}) :</p>
      <ul>
        <li><strong>حالت پایه ({{ t = a }}) :</strong> به ازای {{ n = 0 \in \mathbb{N} }} داریم {{ a = s^0(a) \in E }}.</li>
        <li><strong>گام استقرای ساختاری ({{ t = s(t') }} با {{ t' \in \mathcal{T}_0(\mathcal{F}) }}) :</strong> طبق فرض استقرای ساختاری فرض کنید {{ t' \in E }} باشد. پس {{ k \in \mathbb{N} }} وجود دارد که {{ t' = s^k(a) }}.
          <br/>در نتیجه {{ t = s(t') = s(s^k(a)) = s^{k+1}(a) }}. از آنجا که {{ k + 1 \in \mathbb{N} }} است، داریم {{ t \in E }}.</li>
      </ul>
      <p>بنا بر اصل استقرای ساختاری، {{ \mathcal{T}_0(\mathcal{F}) \subseteq E }}. از ترکیب دو شمول نتیجه می‌گیریم که {{ \mathcal{T}_0(\mathcal{F}) = \bigcup_{n \in \mathbb{N}} \{s^n(a)\} }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 23 -->
<h2 id="td7_ex23">Exercice 23 – Termes avec variables et comptage inductif</h2>

<!-- Q23.1 -->
<div class="q-card" id="td7_q23_1">
  <div class="q-header">
    <span class="q-num">تمرین ۲۳ – سؤال ۱</span>
    <span class="q-title">شخصی‌سازی {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} برای {{ \mathcal{X} = \{x\} }} و {{ \mathcal{F}_1 = \{f, g\} }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>تعریف مجموعه ترم‌های {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} را برای {{ \mathcal{X} = \{x\} }} و {{ \mathcal{F} = \mathcal{F}_1 = \{f, g\} }} شخصی‌سازی کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>تعریف استقرایی شخصی‌سازی‌شده</h4>
      <p>در اینجا {{ \mathcal{X} = \{x\} }}، {{ \mathcal{F}_0 = \emptyset }} (بدون ثابت) و {{ \mathcal{F}_1 = \{f, g\} }} (دو نماد تابعی یک‌تایی) است. مجموعه {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} <strong>کوچک‌ترین مجموعه‌ای</strong> است که در دو شرط زیر صدق کند:</p>
      <ol>
        <li><strong>حالت پایه (متغیر {{ \mathcal{X} }}) :</strong> {{ x \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}.</li>
        <li><strong>گام استقرایی (توابع یک‌تایی {{ \mathcal{F}_1 }}) :</strong> اگر {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} باشد، آنگاه {{ f(t) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} و {{ g(t) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} است.</li>
      </ol>
      <p><em>نمونه‌هایی از ترم‌های این مجموعه :</em> {{ x }}، {{ f(x) }}، {{ g(x) }}، {{ f(g(f(x))) }} و غیره.</p>
    </div>
  </details>
</div>

<!-- Q23.2 -->
<div class="q-card" id="td7_q23_2">
  <div class="q-header">
    <span class="q-num">تمرین ۲۳ – سؤال ۲</span>
    <span class="q-title">تعریف استقرایی {{ \text{nb}_f(t) }} و {{ \text{nb}_g(t) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>تعریفی استقرایی برای تعداد {{ \text{nb}_f(t) }} از نمادهای {{ f }} و تعداد {{ \text{nb}_g(t) }} از نمادهای {{ g }} که در ترم {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} ظاهر می‌شوند ارائه دهید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>تعاریف بازگشتی به روش استقرای ساختاری روی {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</h4>
      <p>چون هر ترم {{ t \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} به طور یکتا به یکی از سه شکل {{ x }}، {{ f(t') }} یا {{ g(t') }} با {{ t' \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} نوشته می‌شود، توابع {{ \text{nb}_f : \mathcal{T}(\mathcal{X}, \mathcal{F}) \to \mathbb{N} }} و {{ \text{nb}_g : \mathcal{T}(\mathcal{X}, \mathcal{F}) \to \mathbb{N} }} را چنین تعریف می‌کنیم:</p>
      <div style="margin:10px 0; text-align:center;">
        {{ \text{nb}_f(t) = \begin{cases} 0 & \text{si } t = x \\ 1 + \text{nb}_f(t') & \text{si } t = f(t') \\ \text{nb}_f(t') & \text{si } t = g(t') \end{cases} \qquad \text{et} \qquad \text{nb}_g(t) = \begin{cases} 0 & \text{si } t = x \\ \text{nb}_g(t') & \text{si } t = f(t') \\ 1 + \text{nb}_g(t') & \text{si } t = g(t') \end{cases} }}
      </div>
      <p><em>بررسی با مثال :</em> برای {{ t = f(g(f(x))) }} داریم {{ \text{nb}_f(t) = 1 + \text{nb}_f(g(f(x))) = 1 + \text{nb}_f(f(x)) = 1 + 1 + \text{nb}_f(x) = 2 }} و {{ \text{nb}_g(t) = \text{nb}_g(g(f(x))) = 1 + \text{nb}_g(f(x)) = 1 + \text{nb}_g(x) = 1 }}.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 24 -->
<h2 id="td7_ex24">Exercice 24 – Symboles d'une formule, {{ \text{Free}(F) }} et renommage</h2>

<div class="box info">
  <h4>فرمول مورد بررسی در تمرین ۲۴</h4>
  <p>فرمول {{ F \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} را با مجموعه متغیرهای {{ \mathcal{X} = \{x, x_1, x_2, x_3, z\} }} به صورت زیر در نظر می‌گیریم:</p>
  <p style="text-align:center;">{{ F = \big(\forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z)))\big) }}</p>
</div>

<!-- Q24.1 & Q24.2 -->
<div class="q-card" id="td7_q24_1_2">
  <div class="q-header">
    <span class="q-num">تمرین ۲۴ – سؤالات ۱ و ۲</span>
    <span class="q-title">تشخیص نمادهای تابعی و محمولی و ظرفیت (Arité) آن‌ها</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <ol>
      <li>نمادهای تابعی ظاهرشده در {{ F }} کدام‌اند؟ ظرفیت (arité) هر یک را مشخص کنید.</li>
      <li>نمادهای محمولی ظاهرشده در {{ F }} کدام‌اند؟ ظرفیت هر یک را مشخص کنید.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>۱. نمادهای تابعی و ظرفیت آن‌ها (سؤال ۱)</h4>
      <p>با بررسی آرگومان‌های درونی در اتم‌های {{ s_1(s_2(x, x)) }}، {{ s_1(s_2(x, z)) }} و {{ s_3(s_4(x)) }} می‌بینیم:</p>
      <ul>
        <li><strong>{{ s_2 }} یک نماد تابعی با ظرفیت ۲ است ({{ s_2 \in \mathcal{F}_2 }}) :</strong> زیرا در جایگاه آرگومانِ {{ s_1 }} نشسته و دو ترم ({{ x, x }} یا {{ x, z }}) درون پرانتز خود می‌گیرد.</li>
        <li><strong>{{ s_4 }} یک نماد تابعی با ظرفیت ۱ است ({{ s_4 \in \mathcal{F}_1 }}) :</strong> زیرا در جایگاه آرگومانِ {{ s_3 }} قرار گرفته و تنها یک ترم ({{ x }}) درون پرانتز خود دارد.</li>
      </ul>
      <p>هیچ نماد ثابتی وجود ندارد ({{ \mathcal{F}_0 = \emptyset }})، چرا که {{ x }} و {{ z }} عضو مجموعه متغیرها {{ \mathcal{X} }} هستند.</p>

      <h4>۲. نمادهای محمولی و ظرفیت آن‌ها (سؤال ۲)</h4>
      <p>با بررسی نمادهایی که مستقیماً زیر عملگرهای {{ \land }} و سورهای {{ \forall x, \exists x }} قرار گرفته‌اند:</p>
      <ul>
        <li><strong>{{ s_1 }} یک نماد محمول با ظرفیت ۱ است ({{ s_1 \in \mathcal{P}_1 }}) :</strong> در {{ s_1(s_2(x, x)) }} و {{ s_1(s_2(x, z)) }}، نماد {{ s_1 }} مستقیماً با {{ \land }} ترکیب شده یا زیر سور {{ \exists x }} قرار دارد و یک ترم واحد {{ s_2(\dots) }} را به عنوان آرگومان می‌پذیرد.</li>
        <li><strong>{{ s_3 }} یک نماد محمول با ظرفیت ۱ است ({{ s_3 \in \mathcal{P}_1 }}) :</strong> در {{ s_3(s_4(x)) }}، نماد {{ s_3 }} مستقیماً زیر عملگر {{ \land }} قرار داشته و یک ترم واحد {{ s_4(x) }} را به عنوان آرگومان می‌گیرد.</li>
      </ul>
    </div>
  </details>
</div>

<!-- Q24.3 -->
<div class="q-card" id="td7_q24_3">
  <div class="q-header">
    <span class="q-num">تمرین ۲۴ – سؤال ۳</span>
    <span class="q-title">مجموعه متغیرهای آزاد {{ \text{Free}(F) }} و بستار کلی</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>مجموعه {{ \text{Free}(F) }} شامل متغیرهای آزاد {{ F }} را تعیین کرده و یک بستار کلی (clôture universelle) برای {{ F }} بنویسید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>۱. محاسبه دقیق {{ \text{Free}(F) }}</h4>
      <p>فرمول را به صورت {{ F = G_1 \land G_2 }} تفکیک می‌کنیم:</p>
      <ul>
        <li>{{ G_1 = \forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z))) }} :
          <br/>{{ \text{Free}(G_1) = \big(\text{Free}(s_1(s_2(x, x))) \cup \text{Free}(\exists x \, s_1(s_2(x, z)))\big) \setminus \{x\} = \big(\{x\} \cup (\{x, z\} \setminus \{x\})\big) \setminus \{x\} = \{x, z\} \setminus \{x\} = \{z\} }}.
          <br/>در {{ G_1 }} تمام رخدادهای {{ x }} مقید هستند، اما رخداد {{ z }} <strong>آزاد</strong> است.</li>
        <li>{{ G_2 = s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z))) }} :
          <br/>{{ \text{Free}(G_2) = \text{Free}(s_3(s_4(x))) \cup \text{Free}(\exists x \, s_1(s_2(x, z))) = \{x\} \cup (\{x, z\} \setminus \{x\}) = \{x\} \cup \{z\} = \{x, z\} }}.
          <br/>در واقع، در {{ s_3(s_4(x)) }} رخداد متغیر {{ x }} در دامنه هیچ سوری نیست (دامنه {{ \forall x }} مربوط به {{ G_1 }} پیش از {{ \land }} اصلی بسته شده است!). پس این رخداد {{ x }} <strong>آزاد</strong> است.</li>
      </ul>
      <p>از اجتماع دو بخش داریم:</p>
      <p style="text-align:center;">{{ \text{Free}(F) = \text{Free}(G_1) \cup \text{Free}(G_2) = \{z\} \cup \{x, z\} = \{x, z\} }}</p>

      <h4>۲. بستار کلی فرمول {{ F }}</h4>
      <p>برای بستن کلی {{ F }}، تمام متغیرهای آزاد عضو {{ \text{Free}(F) = \{x, z\} }} را در ابتدای فرمول با سور کلی مقید می‌کنیم:</p>
      <p style="text-align:center;">{{ \tilde{\forall} F = \forall x \forall z \, \Big( \big(\forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x \, s_1(s_2(x, z)))\big) \Big) }}</p>
      <p><em>(تذکر: نوشتن {{ \forall z \forall x \, F }} نیز کاملاً صحیح است.)</em></p>
    </div>
  </details>
</div>

<!-- Q24.4 -->
<div class="q-card" id="td7_q24_4">
  <div class="q-header">
    <span class="q-num">تمرین ۲۴ – سؤال ۴</span>
    <span class="q-title">تغییرنام بدون اسارت متغیرهای مقید در {{ F }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>برخی از متغیرهای {{ F }} را چنان تغییر نام دهید که فرمولی منطقاً هم‌ارز حاصل شود که در آن سورها روی متغیرهای متفاوتی عمل کنند.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>تحلیل دامنه‌ها و تغییرنام با متغیرهای تازه {{ x_1, x_2, x_3 \in \mathcal{X} }}</h4>
      <p>به دو نکته کلیدی دقت کنید:</p>
      <ol>
        <li>در {{ \forall x \, (s_1(s_2(x, x)) \land \exists x \, s_1(s_2(x, z))) }}، سور دوم {{ \exists x }} درون دامنه {{ \forall x }} قرار دارد اما متغیر {{ x }} را در زیرفرمول خودش {{ s_1(s_2(x, z)) }} بازتعریف (سایه‌اندازی) می‌کند. بنابراین {{ \forall x }} اول فقط {{ s_1(s_2(x, x)) }} را مقید می‌سازد و {{ \exists x }} داخلی متغیر {{ x }} در {{ s_1(s_2(x, z)) }} را مقید می‌کند.</li>
        <li>رخداد {{ x }} در {{ s_3(s_4(x)) }} و هر دو رخداد {{ z }} <strong>آزاد</strong> هستند: <strong>هرگز مجاز به تغییر نام متغیرهای آزاد نیستیم</strong> (زیرا معنای فرمول عوض می‌شود!).</li>
      </ol>
      <p>با استفاده از متغیرهای تازه {{ x_1, x_2, x_3 \in \mathcal{X} }} برای سه سور موجود، به فرمول هم‌ارز زیر می‌رسیم:</p>
      <p style="text-align:center;">{{ F_{\text{ren}} = \big(\forall x_1 \, (s_1(s_2(x_1, x_1)) \land \exists x_2 \, s_1(s_2(x_2, z)))\big) \land \big(s_3(s_4(x)) \land (\exists x_3 \, s_1(s_2(x_3, z)))\big) }}</p>
    </div>
  </details>
</div>

<!-- EXERCICE 25 -->
<h2 id="td7_ex25">Exercice 25 – Construction de formules sous contraintes et arbre syntaxique</h2>

<div class="box info">
  <h4>صورت و قیود تمرین ۲۵</h4>
  <p>فرض کنید {{ \mathcal{X} = \{x, y, z\} }}، {{ \mathcal{F} = \mathcal{F}_0 \cup \mathcal{F}_2 }} با {{ \mathcal{F}_0 = \{k\} }} و {{ \mathcal{F}_2 = \{f\} }}، و {{ \mathcal{P} = \mathcal{P}_1 \cup \mathcal{P}_2 }} با {{ \mathcal{P}_1 = \{p\} }} و {{ \mathcal{P}_2 = \{q\} }}. اسکلت فرمول زیر داده شده است:</p>
  <p style="text-align:center;">{{ F = (\forall y \, \Box(\Box, \Box(\Box, \Box))) \Rightarrow ((\Box \Box \exists \Box \, \Box(\Box(\Box, \Box))) \lor \Box(\Box, \Box)) }}</p>
  <p>هر خانه {{ \Box }} باید با یک نماد یکتا پر شود به گونه‌ای که:</p>
  <ul>
    <li>متغیر {{ x }} دقیقاً دارای <strong>۲ رخداد آزاد</strong> و <strong>۱ رخداد مقید به {{ \forall }}</strong> در {{ F }} باشد؛</li>
    <li>متغیر {{ y }} دقیقاً دارای <strong>۱ رخداد مقید به {{ \forall }}</strong> و <strong>۱ رخداد مقید به {{ \exists }}</strong> در {{ F }} باشد؛</li>
    <li>متغیر {{ z }} دقیقاً دارای <strong>۱ رخداد آزاد</strong> در {{ F }} باشد.</li>
  </ul>
</div>

<!-- Q25.1 -->
<div class="q-card" id="td7_q25_1">
  <div class="q-header">
    <span class="q-num">تمرین ۲۵ – سؤال ۱</span>
    <span class="q-title">پر کردن استدلالی خانه‌های خالی فرمول {{ F }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>خانه‌های خالی فرمول {{ F }} را با رعایت کامل قیود روی {{ \mathcal{X}, \mathcal{F}, \mathcal{P} }} و تعداد رخدادهای آزاد و مقید {{ x, y, z }} پر کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>استنتاج یکتای ساختار نحوی</h4>
      <ol>
        <li><strong>تشخیص محمول‌ها و توابع از روی تعداد آرگومان‌های پرانتزها :</strong>
          <ul>
            <li>در {{ \forall y \, \Box(\Box, \Box(\Box, \Box)) }} : نماد سرشاخه ۲ آرگومان دارد و زیر {{ \forall y }} نشسته است، پس الزاماً محمول دوتایی {{ q \in \mathcal{P}_2 }} است. آرگومان دوم آن {{ \Box(\Box, \Box) }} یک ترم ۲ آرگومانی است، پس با تابع دوتایی {{ f \in \mathcal{F}_2 }} ساخته شده است: {{ \forall y \, q(\Box, f(\Box, \Box)) }}.</li>
            <li>در {{ \Box \Box \exists \Box \, \Box(\Box(\Box, \Box)) }} : دو خانه اول پیش از {{ \exists \Box }} باید یک سور کلی روی {{ x }} بسازند (چون {{ x }} باید ۱ رخداد مقید به {{ \forall }} داشته باشد)، یعنی {{ \forall x \exists y }}. بدنه {{ \Box(\Box(\Box, \Box)) }} شامل محمول یک‌تایی {{ p \in \mathcal{P}_1 }} است که روی ترم دوتایی {{ f \in \mathcal{F}_2 }} اثر می‌کند: {{ \forall x \exists y \, p(f(\Box, \Box)) }}.</li>
            <li>در {{ \lor \, \Box(\Box, \Box) }} : نماد سرشاخه زیر {{ \lor }} بوده و ۲ آرگومان دارد، پس محمول دوتایی {{ q \in \mathcal{P}_2 }} است: {{ q(\Box, \Box) }}.</li>
          </ul>
        </li>
        <li><strong>جای‌گذاری متغیرهای {{ x, y, z }} و ثابت {{ k }} :</strong>
          <ul>
            <li>زیر {{ \forall x \exists y \, p(f(\Box, \Box)) }}، متغیر {{ x }} باید مقید به {{ \forall x }} و {{ y }} مقید به {{ \exists y }} شود، که {{ \forall x \exists y \, p(f(x, y)) }} را می‌دهد.</li>
            <li>در شاخه راست {{ q(\Box, \Box) }} (بیرون از هر سوری)، رخداد آزاد دوم {{ x }} و تنها رخداد آزاد {{ z }} را قرار می‌دهیم: {{ q(x, z) }}.</li>
            <li>در شاخه چپ {{ \forall y \, q(\Box, f(\Box, \Box)) }}، رخداد آزاد اول {{ x }}، رخداد مقید {{ y }} (زیر {{ \forall y }}) و ثابت {{ k \in \mathcal{F}_0 }} (زیرا سهمیه رخدادهای {{ x, y, z }} تمام شده است!) را قرار می‌دهیم: {{ \forall y \, q(x, f(y, k)) }}.</li>
          </ul>
        </li>
      </ol>
      <p><strong>فرمول کامل به‌دست‌آمده :</strong></p>
      <p style="text-align:center;">{{ F = \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x \exists y \, p(f(x, y))) \lor q(x, z)\big) }}</p>
    </div>
  </details>
</div>

<!-- Q25.2 & Q25.3 -->
<div class="q-card" id="td7_q25_2_3">
  <div class="q-header">
    <span class="q-num">تمرین ۲۵ – سؤالات ۲ و ۳</span>
    <span class="q-title">درخت نحوی، رخدادهای آزاد، بستار کلی {{ F' }} و تغییرنام {{ F'' }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <ol start="2">
      <li>درخت نحوی فرمول {{ F }} را رسم کرده و دور رخدادهای آزاد متغیرها کادر بکشید.</li>
      <li>یک بستار کلی {{ F' }} برای {{ F }} پیشنهاد دهید و سپس برخی نمادهای متغیر در {{ F' }} را چنان تغییر نام دهید که فرمول هم‌ارز {{ F'' }} حاصل شود که در آن تمام سورها روی متغیرهای متفاوتی عمل کنند.</li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>۱. درخت نحوی {{ F }} و کادر دور رخدادهای آزاد (سؤال ۲)</h4>
      <p>در درخت زیر، سه برگ متناظر با رخدادهای آزاد درون کادر <code>[x]</code> و <code>[z]</code> قرار گرفته‌اند:</p>
      <pre><code>                        (⇒)
                       /   \
                    (∀y)   (∨)
                     |     /  \
                    (q)  (∀x) (q)
                    / \    |   / \
                  [x] (f)(∃y)[x] [z]
                      / \  |
                     y  k (p)
                           |
                          (f)
                          / \
                         x   y</code></pre>
      <p>مشاهده می‌شود که {{ \text{Free}(F) = \{x, z\} }}.</p>

      <h4>۲. بستار کلی {{ F' }} و فرم تغییرنام‌یافته {{ F'' }} (سؤال ۳)</h4>
      <ul>
        <li><strong>بستار کلی {{ F' }} :</strong> با افزودن {{ \forall x \forall z }} به ابتدای {{ F }}، رخدادهای آزاد {{ x }} و {{ z }} مقید می‌شوند:
          <div style="margin:6px 0; text-align:center;">{{ F' = \forall x \forall z \, \Big( \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x \exists y \, p(f(x, y))) \lor q(x, z)\big) \Big) }}</div>
        </li>
        <li><strong>تغییرنام بدون اسارت {{ F'' }} :</strong> در {{ F' }} پنج سور داریم ({{ \forall x }}، {{ \forall z }}، {{ \forall y }} و سپس {{ \forall x }}، {{ \exists y }}). کافی است {{ \forall x }} دوم را به {{ \forall x_1 }} و {{ \exists y }} را به {{ \exists y_1 }} تغییر نام دهیم:
          <div style="margin:6px 0; text-align:center;">{{ F'' = \forall x \forall z \, \Big( \big(\forall y \, q(x, f(y, k))\big) \Rightarrow \big((\forall x_1 \exists y_1 \, p(f(x_1, y_1))) \lor q(x, z)\big) \Big) }}</div>
          اکنون هر ۵ سور ({{ \forall x, \forall z, \forall y, \forall x_1, \exists y_1 }}) روی متغیرهایی دوبه‌دو متمایز عمل می‌کنند!
        </li>
      </ul>
    </div>
  </details>
</div>

<!-- EXERCICE 26 -->
<h2 id="td7_ex26">Exercice 26 – Renommage de variables et formules équivalentes</h2>

<div class="box info">
  <h4>مسئله مطرح‌شده در تمرین ۲۶</h4>
  <p>برای هر یک از فرمول‌های {{ F_1, F_2, F_3 }} زیر، آیا می‌توان برخی متغیرهای {{ F_i }} را چنان تغییر نام داد که به فرمول منطقاً هم‌ارز {{ F'_i }} برسیم که <strong>تنها متغیر ظاهرشده در {{ F'_i }} متغیر {{ x }} باشد</strong>؟</p>
</div>

<!-- Q26.1 -->
<div class="q-card" id="td7_q26_1">
  <div class="q-header">
    <span class="q-num">تمرین ۲۶ – سؤال ۱</span>
    <span class="q-title">بررسی فرمول {{ F_1 = \exists y \, (p(y) \land \forall x \, p(x)) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>آیا می‌توان متغیرهای {{ F_1 = \exists y \, (p(y) \land \forall x \, p(x)) }} را چنان تغییر نام داد که فرمول هم‌ارز {{ F'_1 \equiv F_1 }} فقط از متغیر {{ x }} استفاده کند؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>پاسخ: بله (OUI)</h4>
      <p>در زیرفرمول {{ G = p(y) \land \forall x \, p(x) }} واقع در دامنه {{ \exists y }}، شرایط تغییر نام متغیر مقید {{ y }} به {{ x }} را بررسی می‌کنیم:</p>
      <ul>
        <li>{{ x \notin \text{Free}(G) }}، زیرا تنها رخداد {{ x }} در {{ G }} قبلاً توسط {{ \forall x }} مقید شده است ({{ \text{Free}(G) = \{y\} }}) ؛</li>
        <li>تنها رخداد {{ y }} در {{ G }} درون {{ p(y) }} است که <strong>بیرون</strong> از دامنه سور داخلی {{ \forall x }} قرار دارد؛ بنابراین توسط {{ \forall x }} به اسارت درنمی‌آید!</li>
      </ul>
      <p>پس می‌توان به طور مجاز {{ \exists y }} را به {{ \exists x }} تغییر نام داد و به فرمول هم‌ارز زیر رسید:</p>
      <p style="text-align:center;">{{ F'_1 = \exists x \, (p(x) \land \forall x \, p(x)) }}</p>
      <p>در {{ F'_1 }}، اولین {{ p(x) }} به {{ \exists x }} بیرونی و دومین {{ p(x) }} به {{ \forall x }} درونی مقید است، دقیقاً همانند {{ F_1 }}.</p>
    </div>
  </details>
</div>

<!-- Q26.2 -->
<div class="q-card" id="td7_q26_2">
  <div class="q-header">
    <span class="q-num">تمرین ۲۶ – سؤال ۲</span>
    <span class="q-title">بررسی فرمول {{ F_2 = (\exists y \, p(y)) \Rightarrow (p(x) \lor (\forall z \, p(z))) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>آیا می‌توان متغیرهای {{ F_2 = (\exists y \, p(y)) \Rightarrow (p(x) \lor (\forall z \, p(z))) }} را چنان تغییر نام داد که فرمول هم‌ارز {{ F'_2 \equiv F_2 }} فقط از متغیر {{ x }} استفاده کند؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>پاسخ: بله (OUI)</h4>
      <p>دامنه‌های سورهای {{ \exists y }} (یعنی {{ p(y) }}) و {{ \forall z }} (یعنی {{ p(z) }}) کاملاً از یکدیگر و از رخداد آزاد {{ p(x) }} مجزا هستند:</p>
      <ul>
        <li>در {{ \exists y \, p(y) }} داریم {{ x \notin \text{Free}(p(y)) }}، پس {{ \exists y \, p(y) \equiv \exists x \, p(x) }}.</li>
        <li>در {{ \forall z \, p(z) }} داریم {{ x \notin \text{Free}(p(z)) }}، پس {{ \forall z \, p(z) \equiv \forall x \, p(x) }}.</li>
        <li>رخداد آزاد {{ x }} در {{ p(x) }} بیرون از دامنه هر دو سور است و همچنان آزاد باقی می‌ماند.</li>
      </ul>
      <p>بنابراین فرمول هم‌ارز که تنها از متغیر {{ x }} بهره می‌برد عبارت است از:</p>
      <p style="text-align:center;">{{ F'_2 = (\exists x \, p(x)) \Rightarrow (p(x) \lor (\forall x \, p(x))) }}</p>
    </div>
  </details>
</div>

<!-- Q26.3 -->
<div class="q-card" id="td7_q26_3">
  <div class="q-header">
    <span class="q-num">تمرین ۲۶ – سؤال ۳</span>
    <span class="q-title">بررسی فرمول {{ F_3 = (\forall x \exists y \, (p(y) \Rightarrow p(x))) \lor (\forall z \, p(z) \land p(y)) }}</span>
  </div>
  <div class="box def">
    <h4>صورت اصلی سؤال</h4>
    <p>آیا می‌توان متغیرهای {{ F_3 = (\forall x \exists y \, (p(y) \Rightarrow p(x))) \lor (\forall z \, p(z) \land p(y)) }} را چنان تغییر نام داد که فرمول هم‌ارز {{ F'_3 \equiv F_3 }} فقط از متغیر {{ x }} استفاده کند؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ تشریحی گام‌به‌گام</summary>
    <div class="box method">
      <h4>پاسخ: خیر (NON — غیرممکن به دو دلیل مستقل)</h4>
      <ol>
        <li><strong>اسارت متغیر در سورهای تودرتو {{ \forall x \exists y \, (p(y) \Rightarrow p(x)) }} :</strong>
          <br/>در زیرفرمول {{ \exists y \, (p(y) \Rightarrow p(x)) }}، متغیر {{ x }} دارای رخداد <strong>آزاد</strong> است ({{ x \in \text{Free}(p(y) \Rightarrow p(x)) }}) که به سور بیرونی {{ \forall x }} مقید شده است. اگر {{ \exists y }} را به {{ \exists x }} تغییر نام دهیم، به {{ \forall x \exists x \, (p(x) \Rightarrow p(x)) }} می‌رسیم که در آن رخداد {{ x }} در تالی توسط {{ \exists x }} داخلی <strong>اسیر</strong> می‌شود (و زیرفرمول به یک گزاره بدیهی تبدیل می‌شود). برای بیان {{ \forall x \exists y \, (p(y) \Rightarrow p(x)) }} حداقل به دو نام متغیر متمایز نیاز داریم.</li>
        <li><strong>وجود رخداد آزاد از متغیر {{ y }} :</strong>
          <br/>علاوه بر این، در {{ (\forall z \, p(z) \land p(y)) }}، رخداد {{ y }} در {{ p(y) }} <strong>آزاد</strong> است ({{ y \in \text{Free}(F_3) }}). تغییرنام مجاز تنها روی متغیرهای مقید تعریف شده است و تغییر نام متغیر آزاد {{ y }} به {{ x }} معنای فرمول را تغییر می‌دهد.</li>
      </ol>
    </div>
  </details>
</div>
"""

open(os.path.join(W07, 'td.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W07, 'td.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("td.fr.html and td.fa.html written for w07.")
