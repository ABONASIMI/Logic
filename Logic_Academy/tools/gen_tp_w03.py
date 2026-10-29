#!/usr/bin/env python3
"""Authoring generator for TP Week 3 (Thème 3 : Décomposition Syntaxique de Formules et Arbres de Syntaxe).
Exhaustive tutorial and Python implementations for:
- Exercice 5 Question 1: decompose_simple(formule: str) -> (str, list[str])
- Exercice 5 Question 3: trouve_prochain_connec(formule: str, index: int) -> (str, int)
- Exercice 5 Question 2: decompose(formule: str) -> (str, list[str]) (4 étapes officielles : équilibre des parenthèses, suppression des parenthèses externes, détection du niveau 0, découpage binaire/unaire)
- Application directe Thème 3: évaluation récursive et reconnaissance syntaxique automatique de FND / FNC grâce à decompose
"""
import os

W03 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w03'
os.makedirs(W03, exist_ok=True)

fr = r'''
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TP Thème 3 : Décomposition Syntaxique de Formules et Formes Normales</h1>
  <p class="lead">Travaux Pratiques officiels (Exercice 5 du polycopié de TP) : construction pas à pas d'un analyseur syntaxique (parseur) de formules propositionnelles en Python (<code>decompose_simple</code>, <code>trouve_prochain_connec</code>, <code>decompose</code> avec suivi de profondeur de parenthésage) et application à la vérification syntaxique des formes normales FND/FNC.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du TP</h3>
  <ul>
    <li><a href="#tp3_intro">1. Objectif et représentation d'une formule sous forme d'arbre</a></li>
    <li><a href="#tp3_ex5_q1">2. Exercice 5 – Question 1 : Décomposition élémentaire sans parenthèses (<code>decompose_simple</code>)</a></li>
    <li><a href="#tp3_ex5_q3">3. Exercice 5 – Question 3 : Recherche du prochain connecteur (<code>trouve_prochain_connec</code>)</a></li>
    <li><a href="#tp3_ex5_q2">4. Exercice 5 – Question 2 : Décomposition générale avec suivi de profondeur (<code>decompose</code>)</a></li>
    <li><a href="#tp3_app_fn">5. Application au Thème 3 : Reconnaissance automatique de FND et FNC en Python</a></li>
  </ul>
</div>

<!-- SECTION 1 : INTRO -->
<h2 id="tp3_intro">1. Objectif et représentation d'une formule sous forme d'arbre</h2>

<div class="box info">
  <h4>Pourquoi décomposer une formule propositionnelle ?</h4>
  <p>Dans les exercices précédents du TP, l'évaluation d'une formule reposait sur une traduction directe vers <code>eval()</code> de Python. Or, pour manipuler la <strong>structure syntaxique</strong> d'une formule (par exemple pour vérifier si elle est en <strong>FNC</strong> ou en <strong>FND</strong>, ou pour lui appliquer les lois de De Morgan et de distributivité), un programme doit être capable d'identifier le <strong>connecteur principal</strong> (la racine de l'arbre syntaxique) et ses <strong>sous-formules immédiates</strong>.</p>
  <p>L'objectif de l'<strong>Exercice 5</strong> est d'écrire une fonction <code>decompose(formule: str)</code> qui renvoie un couple <code>(racine, sous_formules)</code> :</p>
  <ul>
    <li>Si la formule est atomique (ex. <code>"p"</code>), elle renvoie <code>('p', [])</code>.</li>
    <li>Si la formule est unaire (ex. <code>"NOT (p AND q)"</code>), elle renvoie <code>('NOT', ['(p AND q)'])</code>.</li>
    <li>Si la formule est binaire (ex. <code>"(p OR q) AND (NOT r)"</code>), elle renvoie <code>('AND', ['(p OR q)', '(NOT r)'])</code>.</li>
  </ul>
</div>

<!-- SECTION 2 : EX 5 Q1 -->
<h2 id="tp3_ex5_q1">2. Exercice 5 – Question 1 : Décomposition élémentaire (<code>decompose_simple</code>)</h2>

<div class="q-card" id="tp3_q5_1">
  <div class="q-header">
    <span class="q-num">Exercice 5 – Question 1</span>
    <span class="q-title">Fonction <code>decompose_simple(formule: str) -> tuple[str, list[str]]</code></span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel du polycopié de TP</h4>
    <p>On commence par le cas des formules sans parenthèses qui contiennent au plus un connecteur. Écrivez la fonction <code>decompose_simple(formule: str) -> (str, list[str])</code> :</p>
    <ul>
      <li><code>decompose_simple("p")</code> renvoie <code>('p', [])</code></li>
      <li><code>decompose_simple("NOT p")</code> renvoie <code>('NOT', ['p'])</code></li>
      <li><code>decompose_simple("p IMPLIES q")</code> renvoie <code>('IMPLIES', ['p', 'q'])</code></li>
      <li><code>decompose_simple("p OR q")</code> renvoie <code>('OR', ['p', 'q'])</code></li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Analyse et implémentation Python complète</summary>
    <div class="box method">
      <h4>Méthode de résolution</h4>
      <p>Puisque la formule ne contient aucune parenthèse et possède <strong>au plus un connecteur</strong>, il n'y a que trois cas possibles après nettoyage des espaces aux extrémités avec <code>.strip()</code> :</p>
      <ol>
        <li>La chaîne commence par <code>"NOT "</code> : le connecteur principal est <code>'NOT'</code> et l'unique sous-formule est la sous-chaîne située après <code>"NOT "</code> (à partir de l'indice {{ 4 }}).</li>
        <li>La chaîne contient l'un des connecteurs binaires entouré d'espaces (<code>" IMPLIES "</code>, <code>" AND "</code>, <code>" OR "</code>) : on découpe la chaîne en deux avec <code>.split(mot_cle, 1)</code>.</li>
        <li>Sinon, la chaîne ne contient aucun connecteur : c'est une variable propositionnelle (atome) ou une constante (<code>"True"</code> / <code>"False"</code>), et la liste des sous-formules est vide <code>[]</code>.</li>
      </ol>
      <pre><code>def decompose_simple(formule: str) -> tuple[str, list[str]]:
    """
    Décompose une formule sans parenthèses contenant au plus un connecteur.
    Renvoie un couple (connecteur_ou_atome, liste_des_sous_formules).
    """
    formule = formule.strip()

    # Cas 1 : Négation unaire en tête
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])

    # Cas 2 : Connecteur binaire (IMPLIES, AND, OR)
    for connec in ["IMPLIES", "AND", "OR"]:
        sep = " " + connec + " "
        if sep in formule:
            gauche, droite = formule.split(sep, 1)
            return (connec, [gauche.strip(), droite.strip()])

    # Cas 3 : Formule atomique (ou constante True/False)
    return (formule, [])


# Tests unitaires de vérification
assert decompose_simple("p") == ('p', [])
assert decompose_simple("NOT p") == ('NOT', ['p'])
assert decompose_simple("p IMPLIES q") == ('IMPLIES', ['p', 'q'])
assert decompose_simple("p OR q") == ('OR', ['p', 'q'])</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 3 : EX 5 Q3 -->
<h2 id="tp3_ex5_q3">3. Exercice 5 – Question 3 : Recherche du prochain connecteur (<code>trouve_prochain_connec</code>)</h2>

<div class="q-card" id="tp3_q5_3">
  <div class="q-header">
    <span class="q-num">Exercice 5 – Question 3</span>
    <span class="q-title">Fonction auxiliaire <code>trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]</code></span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel du polycopié de TP</h4>
    <p>Pour vous aider à écrire la fonction de la question 2, vous pouvez écrire la fonction suivante :<br/>
    <code>trouve_prochain_connec(formule: str, index: int) -> (str, int)</code> qui renvoie le nom et la position du premier connecteur dans la <code>formule</code> dont la position est supérieure ou égale à <code>index</code>.</p>
    <ul>
      <li><code>trouve_prochain_connec("NOT b", 0)</code> renvoie <code>('NOT', 0)</code></li>
      <li><code>trouve_prochain_connec("b IMPLIES (q OR r)", 0)</code> renvoie <code>('IMPLIES', 2)</code></li>
      <li><code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> renvoie <code>('AND', 8)</code></li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Explication du piège d'indice et code Python</summary>
    <div class="box method">
      <h4>Pourquoi <code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> renvoie-t-il <code>('AND', 8)</code> ?</h4>
      <p>Analysons les positions (indices {{ 0, 1, 2, \dots }}) dans la chaîne <code>"(NOT b) AND (q OR r)"</code> :</p>
      <ul>
        <li>Indice {{ 0 }} : <code>'('</code></li>
        <li>Indice {{ 1 }} : <code>'N'</code> (début de <code>"NOT"</code>, qui commence donc à la position {{ 1 }}).</li>
        <li>Indice {{ 2 }} : <code>'O'</code>. Comme on cherche à partir de <code>index = 2</code>, le mot <code>"NOT"</code> (qui commençait à l'indice {{ 1 }}) est déjà dépassé !</li>
        <li>Indice {{ 8 }} : <code>'A'</code> (début de <code>"AND"</code>). C'est bien le premier connecteur dont la position de départ est {{ \geq 2 }}.</li>
      </ul>
      <p>La méthode <code>formule.find(connec, index)</code> de Python cherche exactement la première occurrence de la sous-chaîne <code>connec</code> à partir de la position <code>index</code> (et renvoie <code>-1</code> si elle n'apparaît pas) :</p>
      <pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    """
    Renvoie un couple (nom_connecteur, position) correspondant au premier
    connecteur apparaissant dans formule à une position >= index.
    Si aucun connecteur n'est trouvé, renvoie ('', -1).
    """
    connecteurs = ["IMPLIES", "AND", "OR", "NOT"]
    meilleur_connec = ""
    meilleure_pos = -1

    for c in connecteurs:
        pos = formule.find(c, index)
        if pos != -1:
            if meilleure_pos == -1 or pos < meilleure_pos:
                meilleure_pos = pos
                meilleur_connec = c

    return (meilleur_connec, meilleure_pos)


# Tests officiels de l'énoncé
assert trouve_prochain_connec("NOT b", 0) == ('NOT', 0)
assert trouve_prochain_connec("b IMPLIES (q OR r)", 0) == ('IMPLIES', 2)
assert trouve_prochain_connec("(NOT b) AND (q OR r)", 2) == ('AND', 8)</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 4 : EX 5 Q2 -->
<h2 id="tp3_ex5_q2">4. Exercice 5 – Question 2 : Décomposition générale (<code>decompose</code>)</h2>

<div class="q-card" id="tp3_q5_2">
  <div class="q-header">
    <span class="q-num">Exercice 5 – Question 2</span>
    <span class="q-title">Fonction générale <code>decompose(formule: str) -> tuple[str, list[str]] | None</code></span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel du polycopié de TP (les 4 étapes)</h4>
    <p>On passe maintenant au cas général : <code>decompose(formule: str) -> (str, list[str])</code>. On suppose que la formule est bien formée sauf éventuellement pour les parenthèses. Ainsi, on procède de la manière suivante :</p>
    <ol>
      <li>On vérifie l'équilibre des parenthèses (autant de parenthèses ouvrantes que de parenthèses fermantes). Si la formule est mal parenthésée, on affiche un message d'erreur et la fonction renvoie <code>None</code>. S'il n'y a pas de parenthèses, on fait appel à <code>decompose_simple</code>.</li>
      <li>Si la formule commence par une parenthèse ouvrante et se termine par la parenthèse fermante correspondante, on peut les supprimer.</li>
      <li>On parcourt la formule en maintenant le compte des parenthèses ouvertes et non encore fermées. Le connecteur principal sera le premier connecteur rencontré lorsque ce compte est à zéro. On stocke l'indice où le compte passe à zéro pour la première fois.</li>
      <li>On utilise cet indice pour trouver le connecteur principal, puis on extrait la ou les sous-formules correspondantes.</li>
    </ol>
    <p>Exemples officiels :</p>
    <ul>
      <li><code>decompose("(NOT b) AND (q OR r)")</code> renvoie <code>('AND', ['(NOT b)', '(q OR r)'])</code></li>
      <li><code>decompose("((NOT b) AND (q OR r))")</code> renvoie <code>('AND', ['(NOT b)', '(q OR r)'])</code></li>
      <li><code>decompose("(p OR q")</code> affiche <code>Formule mal parenthésée: (p OR q</code> et renvoie <code>None</code></li>
      <li><code>decompose("NOT (p OR q)")</code> renvoie <code>('NOT', ['(p OR q)'])</code></li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Analyse détaillée du compteur de profondeur et implémentation</summary>
    <div class="box method">
      <h4>Attention au piège classique de l'étape 2 : <code>"(NOT b) AND (q OR r)"</code> vs <code>"((NOT b) AND (q OR r))"</code></h4>
      <p>Les deux formules commencent par <code>'('</code> et se terminent par <code>')'</code> ! Mais dans <code>"(NOT b) AND (q OR r)"</code>, la parenthèse ouvrante de l'indice {{ 0 }} se referme dès l'indice {{ 6 }} (après <code>b</code>) : il ne faut surtout <strong>pas</strong> supprimer le premier et le dernier caractère, sinon on obtiendrait <code>"NOT b) AND (q OR r"</code> qui est invalide !</p>
      <p>Pour savoir si la parenthèse finale à l'indice {{ L - 1 }} correspond bien à la parenthèse initiale de l'indice {{ 0 }}, on suit le compteur de profondeur {{ \text{cpt} }} (qui vaut {{ +1 }} sur <code>'('</code> et {{ -1 }} sur <code>')'</code>) :</p>
      <ul>
        <li>Si {{ \text{cpt} }} retombe à {{ 0 }} à un indice {{ i < L - 1 }}, alors le premier bloc parenthésé est terminé avant la fin de la chaîne : les parenthèses externes ne sont <strong>pas</strong> englobantes, et {{ i }} est justement l'indice où le compte passe à zéro pour la première fois (étape 3) !</li>
        <li>Si {{ \text{cpt} }} ne retombe à {{ 0 }} qu'au tout dernier caractère {{ i = L - 1 }}, alors la paire externe englobe toute la formule : on la retire (<code>formule = formule[1:-1].strip()</code>) et on recommence !</li>
      </ul>

      <h4>Trace pas à pas sur <code>"(NOT b) AND (q OR r)"</code></h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>Indice {{ i }}</th>
            <th>{{ 0 }}</th>
            <th>{{ 1..5 }}</th>
            <th>{{ 6 }}</th>
            <th>{{ 7 }}</th>
            <th>{{ 8..10 }}</th>
            <th>{{ 11 }}</th>
            <th>{{ 12 }}</th>
            <th>{{ 13..18 }}</th>
            <th>{{ 19 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Caractère</strong></td>
            <td><code>(</code></td>
            <td><code>NOT b</code></td>
            <td><code>)</code></td>
            <td><code> </code></td>
            <td><code>AND</code></td>
            <td><code> </code></td>
            <td><code>(</code></td>
            <td><code>q OR r</code></td>
            <td><code>)</code></td>
          </tr>
          <tr>
            <td><strong>Profondeur {{ \text{cpt} }}</strong></td>
            <td>{{ 1 }}</td>
            <td>{{ 1 }}</td>
            <td><strong>{{ 0 }}</strong></td>
            <td>{{ 0 }}</td>
            <td>{{ 0 }}</td>
            <td>{{ 0 }}</td>
            <td>{{ 1 }}</td>
            <td>{{ 1 }}</td>
            <td>{{ 0 }}</td>
          </tr>
        </tbody>
      </table>
      <p>Le compte {{ \text{cpt} }} repasse à {{ 0 }} pour la première fois à l'indice {{ i = 6 }} (qui est {{ \neq 19 }}). On appelle alors <code>trouve_prochain_connec(formule, 6)</code> qui renvoie <code>('AND', 8)</code>. La sous-formule gauche est <code>formule[:8].strip() == '(NOT b)'</code> et la sous-formule droite est <code>formule[8+3:].strip() == '(q OR r)'</code>.</p>

      <h4>Implémentation complète conforme aux 4 étapes du TP</h4>
      <pre><code>def decompose(formule: str):
    """
    Décompose une formule propositionnelle générale en (connecteur_principal, sous_formules).
    Vérifie l'équilibre des parenthèses et renvoie None si la formule est mal parenthésée.
    """
    formule = formule.strip()

    # Étape 1 : Vérification de l'équilibre des parenthèses
    cpt = 0
    for ch in formule:
        if ch == '(':
            cpt += 1
        elif ch == ')':
            cpt -= 1
        if cpt < 0:
            # Une parenthèse fermante apparaît avant sa parenthèse ouvrante
            print(f"Formule mal parenthésée: {formule}")
            return None

    if cpt != 0:
        print(f"Formule mal parenthésée: {formule}")
        return None

    # S'il n'y a aucune parenthèse, on appelle decompose_simple
    if '(' not in formule:
        return decompose_simple(formule)

    # Étapes 2 & 3 : Suppression des parenthèses externes englobantes
    # et recherche du premier indice où le compte de parenthèses est à 0
    while True:
        if '(' not in formule:
            return decompose_simple(formule)

        cpt = 0
        premier_zero = -1
        for i, ch in enumerate(formule):
            if ch == '(':
                cpt += 1
            elif ch == ')':
                cpt -= 1
            if cpt == 0 and premier_zero == -1:
                premier_zero = i

        # Si la formule commence par '(' et que la parenthèse correspondante
        # est le tout dernier caractère de la chaîne, on les supprime (Étape 2)
        if formule[0] == '(' and premier_zero == len(formule) - 1:
            formule = formule[1:-1].strip()
        else:
            break

    # Étape 4 : Extraction du connecteur principal à partir de premier_zero
    connec, pos = trouve_prochain_connec(formule, premier_zero)

    if connec == "NOT" and pos == 0:
        # Le connecteur principal est un NOT unaire en tête : ex. "NOT (p OR q)"
        return ("NOT", [formule[3:].strip()])
    elif connec != "":
        # Connecteur binaire au niveau 0 : ex. "(NOT b) AND (q OR r)" ou "b IMPLIES (q OR r)"
        gauche = formule[:pos].strip()
        droite = formule[pos + len(connec):].strip()
        return (connec, [gauche, droite])

    return decompose_simple(formule)


# Tests officiels du polycopié
assert decompose("(NOT b) AND (q OR r)") == ('AND', ['(NOT b)', '(q OR r)'])
assert decompose("((NOT b) AND (q OR r))") == ('AND', ['(NOT b)', '(q OR r)'])
assert decompose("(p OR q") is None
assert decompose("NOT (p OR q)") == ('NOT', ['(p OR q)'])
assert decompose("b IMPLIES (q OR r)") == ('IMPLIES', ['b', '(q OR r)'])</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 5 : APPLICATION AUX FORMES NORMALES -->
<h2 id="tp3_app_fn">5. Application au Thème 3 : Reconnaissance automatique de FND et FNC en Python</h2>

<div class="q-card" id="tp3_q5_fn">
  <div class="q-header">
    <span class="q-num">Application Thème 3</span>
    <span class="q-title">Vérifier par récursion sur <code>decompose</code> si une formule est un littéral, une clause, un terme, une FNC ou une FND</span>
  </div>
  <div class="box def">
    <h4>Lien direct entre le TP (Exercice 5) et le TD (Exercice 9)</h4>
    <p>Grâce à <code>decompose(formule)</code>, nous pouvons programmer directement en Python la définition inductive des formes normales vue en cours et dans l'Exercice 9 du TD :</p>
    <ul>
      <li><code>est_litteral(f)</code> : vrai ssi <code>f</code> est un atome ou <code>NOT atome</code>.</li>
      <li><code>est_clause(f)</code> : vrai ssi <code>f</code> est un littéral ou une disjonction (<code>OR</code>) de clauses.</li>
      <li><code>est_terme(f)</code> : vrai ssi <code>f</code> est un littéral ou une conjonction (<code>AND</code>) de termes.</li>
      <li><code>est_fnc(f)</code> : vrai ssi <code>f</code> est une clause ou une conjonction (<code>AND</code>) de FNC.</li>
      <li><code>est_fnd(f)</code> : vrai ssi <code>f</code> est un terme ou une disjonction (<code>OR</code>) de FND.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Code Python complet du vérificateur de FNC / FND</summary>
    <div class="box method">
      <pre><code>def est_atome(formule: str) -> bool:
    """Vérifie si la formule est réduite à une variable propositionnelle."""
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return len(sous_f) == 0 and racine not in ("True", "False", "")


def est_litteral(formule: str) -> bool:
    """Un littéral est un atome p ou la négation d'un atome (NOT p)."""
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    if len(sous_f) == 0:
        return est_atome(formule)
    if racine == "NOT" and len(sous_f) == 1:
        return est_atome(sous_f[0])
    return False


def est_clause(formule: str) -> bool:
    """Une clause est un littéral ou un OR de clauses (somme de littéraux)."""
    if est_litteral(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "OR" and all(est_clause(sf) for sf in sous_f)


def est_terme(formule: str) -> bool:
    """Un terme est un littéral ou un AND de termes (produit de littéraux)."""
    if est_litteral(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "AND" and all(est_terme(sf) for sf in sous_f)


def est_fnc(formule: str) -> bool:
    """Une FNC est une clause ou un AND de FNC (produit de sommes de littéraux)."""
    if est_clause(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "AND" and all(est_fnc(sf) for sf in sous_f)


def est_fnd(formule: str) -> bool:
    """Une FND est un terme ou un OR de FND (somme de produits de littéraux)."""
    if est_terme(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "OR" and all(est_fnd(sf) for sf in sous_f)


# Vérification sur les expressions de l'Exercice 9 du TD :
# 1. x.y + y.~z -> FND uniquement
assert est_fnd("(x AND y) OR (y AND (NOT z))") is True
assert est_fnc("(x AND y) OR (y AND (NOT z))") is False

# 2. (x + y + z).(y + ~z) -> FNC uniquement
assert est_fnd("((x OR y) OR z) AND (y OR (NOT z))") is False
assert est_fnc("((x OR y) OR z) AND (y OR (NOT z))") is True

# 5. x.y.z -> à la fois FND et FNC !
assert est_fnd("(x AND y) AND z") is True
assert est_fnc("(x AND y) AND z") is True</code></pre>
    </div>
  </details>
</div>
'''

fa = r'''
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>کارگاه عملی هفته ۳ (TP 3): تجزیه نحوی فرمول‌ها و فرم‌های نرمال</h1>
  <p class="lead">کارگاه عملی رسمی (تمرین ۵ جزوه TP سوربن): ساخت گام‌به‌گام یک تجزیه‌گر نحوی (Parser) برای فرمول‌های گزاره‌ای در پایتون (توابع <code>decompose_simple</code>، <code>trouve_prochain_connec</code> و <code>decompose</code> با ردیابی عمق پرانتزها) و کاربرد آن در تشخیص خودکار فرم‌های نرمال FND/FNC.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب کارگاه</h3>
  <ul>
    <li><a href="#tp3_intro">۱. هدف و نمایش درختی یک فرمول منطقی</a></li>
    <li><a href="#tp3_ex5_q1">۲. تمرین ۵ – پرسش ۱: تجزیه مقدماتی بدون پرانتز (<code>decompose_simple</code>)</a></li>
    <li><a href="#tp3_ex5_q3">۳. تمرین ۵ – پرسش ۳: یافتن رابط منطقی بعدی (<code>trouve_prochain_connec</code>)</a></li>
    <li><a href="#tp3_ex5_q2">۴. تمرین ۵ – پرسش ۲: تجزیه عمومی با ردیابی عمق پرانتز (<code>decompose</code>)</a></li>
    <li><a href="#tp3_app_fn">۵. کاربرد در مبحث هفته ۳: تشخیص خودکار FND و FNC در پایتون</a></li>
  </ul>
</div>

<!-- SECTION 1 : INTRO -->
<h2 id="tp3_intro">۱. هدف و نمایش درختی یک فرمول منطقی</h2>

<div class="box info">
  <h4>چرا یک فرمول گزاره‌ای را تجزیه (Decompose) می‌کنیم؟</h4>
  <p>در تمرین‌های پیشین کارگاه، ارزیابی فرمول بر پایه ترجمه مستقیم به تابع <code>eval()</code> پایتون قرار داشت. اما برای دستکاری <strong>ساختار نحوی</strong> یک فرمول (مثلاً بررسی این‌که آیا فرمول در فرم <strong>FNC</strong> یا <strong>FND</strong> قرار دارد، یا اعمال قوانین دمورگان و توزیع‌پذیری)، برنامه باید بتواند <strong>رابط اصلی</strong> (ریشه درخت نحوی) و <strong>زیرفرمول‌های مستقیم</strong> آن را تشخیص دهد.</p>
  <p>هدف <strong>تمرین ۵</strong> نوشتن تابع <code>decompose(formule: str)</code> است که یک زوج <code>(racine, sous_formules)</code> برمی‌گرداند:</p>
  <ul>
    <li>اگر فرمول اتمی باشد (مانند <code>"p"</code>)، خروجی <code>('p', [])</code> است.</li>
    <li>اگر فرمول یک‌موضعی باشد (مانند <code>"NOT (p AND q)"</code>)، خروجی <code>('NOT', ['(p AND q)'])</code> است.</li>
    <li>اگر فرمول دوموضعی باشد (مانند <code>"(p OR q) AND (NOT r)"</code>)، خروجی <code>('AND', ['(p OR q)', '(NOT r)'])</code> است.</li>
  </ul>
</div>

<!-- SECTION 2 : EX 5 Q1 -->
<h2 id="tp3_ex5_q1">۲. تمرین ۵ – پرسش ۱: تجزیه مقدماتی (<code>decompose_simple</code>)</h2>

<div class="q-card" id="tp3_q5_1">
  <div class="q-header">
    <span class="q-num">تمرین ۵ – پرسش ۱</span>
    <span class="q-title">تابع <code>decompose_simple(formule: str) -> tuple[str, list[str]]</code></span>
  </div>
  <div class="box def">
    <h4>صورت رسمی سؤال در جزوه TP</h4>
    <p>ابتدا از حالت فرمول‌های بدون پرانتز که حداکثر شامل یک رابط منطقی هستند شروع می‌کنیم. تابع <code>decompose_simple(formule: str) -> (str, list[str])</code> را بنویسید:</p>
    <ul>
      <li><code>decompose_simple("p")</code> مقدار <code>('p', [])</code> برمی‌گرداند</li>
      <li><code>decompose_simple("NOT p")</code> مقدار <code>('NOT', ['p'])</code> برمی‌گرداند</li>
      <li><code>decompose_simple("p IMPLIES q")</code> مقدار <code>('IMPLIES', ['p', 'q'])</code> برمی‌گرداند</li>
      <li><code>decompose_simple("p OR q")</code> مقدار <code>('OR', ['p', 'q'])</code> برمی‌گرداند</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>تحلیل و پیاده‌سازی کامل پایتون</summary>
    <div class="box method">
      <h4>روش حل</h4>
      <p>از آن‌جا که فرمول هیچ پرانتزی ندارد و <strong>حداکثر دارای یک رابط</strong> است، پس از حذف فاصله‌های اضافی دو طرف رشته با <code>.strip()</code>، تنها سه حالت ممکن وجود دارد:</p>
      <ol>
        <li>رشته با <code>"NOT "</code> آغاز شود: رابط اصلی <code>'NOT'</code> است و تنها زیرفرمول، زیررشته بعد از <code>"NOT "</code> (از اندیس {{ 4 }} به بعد) است.</li>
        <li>رشته شامل یکی از رابط‌های دوتایی محصور در فاصله (<code>" IMPLIES "</code>، <code>" AND "</code>، <code>" OR "</code>) باشد: رشته را با <code>.split(mot_cle, 1)</code> به دو بخش تقسیم می‌کنیم.</li>
        <li>در غیر این صورت، رشته هیچ رابطی ندارد: یک متغیر گزاره‌ای (اتم) یا ثابت (<code>"True"</code> / <code>"False"</code>) است و لیست زیرفرمول‌ها تهی <code>[]</code> خواهد بود.</li>
      </ol>
      <pre><code>def decompose_simple(formule: str) -> tuple[str, list[str]]:
    """
    Décompose une formule sans parenthèses contenant au plus un connecteur.
    Renvoie un couple (connecteur_ou_atome, liste_des_sous_formules).
    """
    formule = formule.strip()

    # Cas 1 : Négation unaire en tête
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])

    # Cas 2 : Connecteur binaire (IMPLIES, AND, OR)
    for connec in ["IMPLIES", "AND", "OR"]:
        sep = " " + connec + " "
        if sep in formule:
            gauche, droite = formule.split(sep, 1)
            return (connec, [gauche.strip(), droite.strip()])

    # Cas 3 : Formule atomique (ou constante True/False)
    return (formule, [])


# Tests unitaires de vérification
assert decompose_simple("p") == ('p', [])
assert decompose_simple("NOT p") == ('NOT', ['p'])
assert decompose_simple("p IMPLIES q") == ('IMPLIES', ['p', 'q'])
assert decompose_simple("p OR q") == ('OR', ['p', 'q'])</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 3 : EX 5 Q3 -->
<h2 id="tp3_ex5_q3">۳. تمرین ۵ – پرسش ۳: یافتن رابط منطقی بعدی (<code>trouve_prochain_connec</code>)</h2>

<div class="q-card" id="tp3_q5_3">
  <div class="q-header">
    <span class="q-num">تمرین ۵ – پرسش ۳</span>
    <span class="q-title">تابع کمکی <code>trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]</code></span>
  </div>
  <div class="box def">
    <h4>صورت رسمی سؤال در جزوه TP</h4>
    <p>برای کمک به نوشتن تابع پرسش ۲، می‌توانید ابتدا تابع زیر را بنویسید:<br/>
    <code>trouve_prochain_connec(formule: str, index: int) -> (str, int)</code> که نام و موقعیت اولین رابط منطقی در <code>formule</code> را که موقعیت شروع آن بزرگ‌تر یا مساوی <code>index</code> است برمی‌گرداند.</p>
    <ul>
      <li><code>trouve_prochain_connec("NOT b", 0)</code> مقدار <code>('NOT', 0)</code> برمی‌گرداند</li>
      <li><code>trouve_prochain_connec("b IMPLIES (q OR r)", 0)</code> مقدار <code>('IMPLIES', 2)</code> برمی‌گرداند</li>
      <li><code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> مقدار <code>('AND', 8)</code> برمی‌گرداند</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>توضیح نکته ظریف اندیس‌گذاری و کد پایتون</summary>
    <div class="box method">
      <h4>چرا <code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> خروجی <code>('AND', 8)</code> می‌دهد؟</h4>
      <p>موقعیت کاراکترها (اندیس‌های {{ 0, 1, 2, \dots }}) را در رشته <code>"(NOT b) AND (q OR r)"</code> بررسی می‌کنیم:</p>
      <ul>
        <li>اندیس {{ 0 }}: کاراکتر <code>'('</code></li>
        <li>اندیس {{ 1 }}: کاراکتر <code>'N'</code> (شروع کلمه <code>"NOT"</code> که از موقعیت {{ 1 }} آغاز می‌شود).</li>
        <li>اندیس {{ 2 }}: کاراکتر <code>'O'</code>. از آن‌جا که جستجو را از <code>index = 2</code> آغاز می‌کنیم، کلمه <code>"NOT"</code> (که در اندیس {{ 1 }} شروع شده بود) رد شده است!</li>
        <li>اندیس {{ 8 }}: کاراکتر <code>'A'</code> (شروع کلمه <code>"AND"</code>). این اولین رابطی است که موقعیت شروع آن {{ \geq 2 }} است.</li>
      </ul>
      <p>متد <code>formule.find(connec, index)</code> در پایتون دقیقاً اولین رخداد زیررشته <code>connec</code> را از موقعیت <code>index</code> به بعد جستجو می‌کند (و در صورت عدم وجود، <code>-1</code> برمی‌گرداند):</p>
      <pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    """
    Renvoie un couple (nom_connecteur, position) correspondant au premier
    connecteur apparaissant dans formule à une position >= index.
    Si aucun connecteur n'est trouvé, renvoie ('', -1).
    """
    connecteurs = ["IMPLIES", "AND", "OR", "NOT"]
    meilleur_connec = ""
    meilleure_pos = -1

    for c in connecteurs:
        pos = formule.find(c, index)
        if pos != -1:
            if meilleure_pos == -1 or pos < meilleure_pos:
                meilleure_pos = pos
                meilleur_connec = c

    return (meilleur_connec, meilleure_pos)


# Tests officiels de l'énoncé
assert trouve_prochain_connec("NOT b", 0) == ('NOT', 0)
assert trouve_prochain_connec("b IMPLIES (q OR r)", 0) == ('IMPLIES', 2)
assert trouve_prochain_connec("(NOT b) AND (q OR r)", 2) == ('AND', 8)</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 4 : EX 5 Q2 -->
<h2 id="tp3_ex5_q2">۴. تمرین ۵ – پرسش ۲: تجزیه عمومی (<code>decompose</code>)</h2>

<div class="q-card" id="tp3_q5_2">
  <div class="q-header">
    <span class="q-num">تمرین ۵ – پرسش ۲</span>
    <span class="q-title">تابع عمومی <code>decompose(formule: str) -> tuple[str, list[str]] | None</code></span>
  </div>
  <div class="box def">
    <h4>صورت رسمی سؤال در جزوه TP (۴ گام الگوریتم)</h4>
    <p>اکنون به سراغ حالت کلی می‌رویم: <code>decompose(formule: str) -> (str, list[str])</code>. فرض می‌کنیم فرمول به‌جز احتمالاً از نظر پرانتزگذاری، خوش‌ساخت است. بنابراین به ترتیب زیر عمل می‌کنیم:</p>
    <ol>
      <li>توازن پرانتزها را بررسی می‌کنیم (تعداد پرانتزهای باز برابر با پرانتزهای بسته باشد). اگر فرمول بدپرانتزگذاری شده باشد، پیام خطایی چاپ کرده و تابع <code>None</code> برمی‌گرداند. اگر هیچ پرانتزی وجود نداشته باشد، تابع <code>decompose_simple</code> را فراخوانی می‌کنیم.</li>
      <li>اگر فرمول با یک پرانتز باز شروع شود و با پرانتز بسته متناظر با همان پرانتز پایان یابد، می‌توان آن‌ها را حذف کرد.</li>
      <li>فرمول را پیمایش کرده و شمارنده پرانتزهای بازِ هنوز بسته‌نشده را نگه می‌داریم. رابط اصلی، اولین رابطی خواهد بود که هنگام صفر بودن این شمارنده با آن روبه‌رو می‌شویم. اندیسی را که شمارنده برای اولین بار در آن به صفر می‌رسد ذخیره می‌کنیم.</li>
      <li>از این اندیس برای یافتن رابط اصلی استفاده کرده و سپس زیرفرمول یا زیرفرمول‌های متناظر را استخراج می‌کنیم.</li>
    </ol>
    <p>مثال‌های رسمی جزوه:</p>
    <ul>
      <li><code>decompose("(NOT b) AND (q OR r)")</code> مقدار <code>('AND', ['(NOT b)', '(q OR r)'])</code> برمی‌گرداند</li>
      <li><code>decompose("((NOT b) AND (q OR r))")</code> مقدار <code>('AND', ['(NOT b)', '(q OR r)'])</code> برمی‌گرداند</li>
      <li><code>decompose("(p OR q")</code> پیام <code>Formule mal parenthésée: (p OR q</code> را چاپ کرده و <code>None</code> برمی‌گرداند</li>
      <li><code>decompose("NOT (p OR q)")</code> مقدار <code>('NOT', ['(p OR q)'])</code> برمی‌گرداند</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>تحلیل دقیق شمارنده عمق پرانتزها و پیاده‌سازی</summary>
    <div class="box method">
      <h4>توجه به دام کلاسیک گام ۲: مقایسه <code>"(NOT b) AND (q OR r)"</code> با <code>"((NOT b) AND (q OR r))"</code></h4>
      <p>هر دو فرمول با <code>'('</code> شروع شده و با <code>')'</code> تمام می‌شوند! اما در <code>"(NOT b) AND (q OR r)"</code>، پرانتز بازِ اندیس {{ 0 }} در همان اندیس {{ 6 }} (بعد از <code>b</code>) بسته می‌شود؛ بنابراین مطلقاً <strong>نباید</strong> کاراکتر اول و آخر را حذف کرد، زیرا در آن صورت رشته نامعتبر <code>"NOT b) AND (q OR r"</code> تولید می‌شود!</p>
      <p>برای تشخیص این‌که آیا پرانتز پایانی در اندیس {{ L - 1 }} واقعاً جفتِ پرانتز ابتدایی در اندیس {{ 0 }} است یا نه، شمارنده عمق {{ \text{cpt} }} را دنبال می‌کنیم (که روی <code>'('</code> یک واحد اضافه {{ +1 }} و روی <code>')'</code> یک واحد کم {{ -1 }} می‌شود):</p>
      <ul>
        <li>اگر {{ \text{cpt} }} در اندیسی مانند {{ i < L - 1 }} به {{ 0 }} بازگردد، یعنی اولین بلوک پرانتزدار پیش از پایان رشته بسته شده است: در این حالت پرانتزهای بیرونی دربرگیرنده کل فرمول <strong>نیستند</strong>، و {{ i }} دقیقاً همان اندیسی است که شمارنده برای نخستین بار به صفر رسیده است (گام ۳)!</li>
        <li>اگر {{ \text{cpt} }} تنها در آخرین کاراکتر یعنی {{ i = L - 1 }} به {{ 0 }} برسد، آنگاه جفت پرانتز بیرونی کل فرمول را در بر گرفته است: آن را حذف می‌کنیم (<code>formule = formule[1:-1].strip()</code>) و فرآیند را تکرار می‌کنیم!</li>
      </ul>

      <h4>ردیابی گام‌به‌گام روی <code>"(NOT b) AND (q OR r)"</code></h4>
      <table class="tt-table">
        <thead>
          <tr>
            <th>اندیس {{ i }}</th>
            <th>{{ 0 }}</th>
            <th>{{ 1..5 }}</th>
            <th>{{ 6 }}</th>
            <th>{{ 7 }}</th>
            <th>{{ 8..10 }}</th>
            <th>{{ 11 }}</th>
            <th>{{ 12 }}</th>
            <th>{{ 13..18 }}</th>
            <th>{{ 19 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>کاراکتر</strong></td>
            <td><code>(</code></td>
            <td><code>NOT b</code></td>
            <td><code>)</code></td>
            <td><code> </code></td>
            <td><code>AND</code></td>
            <td><code> </code></td>
            <td><code>(</code></td>
            <td><code>q OR r</code></td>
            <td><code>)</code></td>
          </tr>
          <tr>
            <td><strong>عمق {{ \text{cpt} }}</strong></td>
            <td>{{ 1 }}</td>
            <td>{{ 1 }}</td>
            <td><strong>{{ 0 }}</strong></td>
            <td>{{ 0 }}</td>
            <td>{{ 0 }}</td>
            <td>{{ 0 }}</td>
            <td>{{ 1 }}</td>
            <td>{{ 1 }}</td>
            <td>{{ 0 }}</td>
          </tr>
        </tbody>
      </table>
      <p>شمارنده {{ \text{cpt} }} برای اولین بار در اندیس {{ i = 6 }} (که {{ \neq 19 }} است) به {{ 0 }} می‌رسد. سپس <code>trouve_prochain_connec(formule, 6)</code> را صدا می‌زنیم که <code>('AND', 8)</code> برمی‌گرداند. زیرفرمول چپ برابر <code>formule[:8].strip() == '(NOT b)'</code> و زیرفرمول راست برابر <code>formule[8+3:].strip() == '(q OR r)'</code> خواهد بود.</p>

      <h4>پیاده‌سازی کامل مطابق با ۴ گام جزوه TP</h4>
      <pre><code>def decompose(formule: str):
    """
    Décompose une formule propositionnelle générale en (connecteur_principal, sous_formules).
    Vérifie l'équilibre des parenthèses et renvoie None si la formule est mal parenthésée.
    """
    formule = formule.strip()

    # Étape 1 : Vérification de l'équilibre des parenthèses
    cpt = 0
    for ch in formule:
        if ch == '(':
            cpt += 1
        elif ch == ')':
            cpt -= 1
        if cpt < 0:
            # Une parenthèse fermante apparaît avant sa parenthèse ouvrante
            print(f"Formule mal parenthésée: {formule}")
            return None

    if cpt != 0:
        print(f"Formule mal parenthésée: {formule}")
        return None

    # S'il n'y a aucune parenthèse, on appelle decompose_simple
    if '(' not in formule:
        return decompose_simple(formule)

    # Étapes 2 & 3 : Suppression des parenthèses externes englobantes
    # et recherche du premier indice où le compte de parenthèses est à 0
    while True:
        if '(' not in formule:
            return decompose_simple(formule)

        cpt = 0
        premier_zero = -1
        for i, ch in enumerate(formule):
            if ch == '(':
                cpt += 1
            elif ch == ')':
                cpt -= 1
            if cpt == 0 and premier_zero == -1:
                premier_zero = i

        # Si la formule commence par '(' et que la parenthèse correspondante
        # est le tout dernier caractère de la chaîne, on les supprime (Étape 2)
        if formule[0] == '(' and premier_zero == len(formule) - 1:
            formule = formule[1:-1].strip()
        else:
            break

    # Étape 4 : Extraction du connecteur principal à partir de premier_zero
    connec, pos = trouve_prochain_connec(formule, premier_zero)

    if connec == "NOT" and pos == 0:
        # Le connecteur principal est un NOT unaire en tête : ex. "NOT (p OR q)"
        return ("NOT", [formule[3:].strip()])
    elif connec != "":
        # Connecteur binaire au niveau 0 : ex. "(NOT b) AND (q OR r)" ou "b IMPLIES (q OR r)"
        gauche = formule[:pos].strip()
        droite = formule[pos + len(connec):].strip()
        return (connec, [gauche, droite])

    return decompose_simple(formule)


# Tests officiels du polycopié
assert decompose("(NOT b) AND (q OR r)") == ('AND', ['(NOT b)', '(q OR r)'])
assert decompose("((NOT b) AND (q OR r))") == ('AND', ['(NOT b)', '(q OR r)'])
assert decompose("(p OR q") is None
assert decompose("NOT (p OR q)") == ('NOT', ['(p OR q)'])
assert decompose("b IMPLIES (q OR r)") == ('IMPLIES', ['b', '(q OR r)'])</code></pre>
    </div>
  </details>
</div>

<!-- SECTION 5 : APPLICATION AUX FORMES NORMALES -->
<h2 id="tp3_app_fn">۵. کاربرد در مبحث هفته ۳: تشخیص خودکار FND و FNC در پایتون</h2>

<div class="q-card" id="tp3_q5_fn">
  <div class="q-header">
    <span class="q-num">کاربرد در مبحث هفته ۳</span>
    <span class="q-title">بررسی بازگشتی با <code>decompose</code> برای تشخیص لیترال، بند، جمله، FNC و FND</span>
  </div>
  <div class="box def">
    <h4>ارتباط مستقیم میان کارگاه (تمرین ۵) و تمرین‌های تئوری (تمرین ۹ TD)</h4>
    <p>به لطف تابع <code>decompose(formule)</code>، می‌توانیم تعریف استقرایی فرم‌های نرمال را که در درس و تمرین ۹ جزوه TD دیدیم مستقیماً در پایتون کدنویسی کنیم:</p>
    <ul>
      <li><code>est_litteral(f)</code>: درست است اگر و تنها اگر <code>f</code> یک اتم یا <code>NOT atome</code> باشد.</li>
      <li><code>est_clause(f)</code>: درست است اگر و تنها اگر <code>f</code> یک لیترال یا فصلی (<code>OR</code>) از بندها باشد.</li>
      <li><code>est_terme(f)</code>: درست است اگر و تنها اگر <code>f</code> یک لیترال یا عطفی (<code>AND</code>) از جمله‌ها باشد.</li>
      <li><code>est_fnc(f)</code>: درست است اگر و تنها اگر <code>f</code> یک بند یا عطفی (<code>AND</code>) از فرم‌های FNC باشد.</li>
      <li><code>est_fnd(f)</code>: درست است اگر و تنها اگر <code>f</code> یک جمله یا فصلی (<code>OR</code>) از فرم‌های FND باشد.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>کد کامل پایتون برای تشخیص‌دهنده FNC / FND</summary>
    <div class="box method">
      <pre><code>def est_atome(formule: str) -> bool:
    """Vérifie si la formule est réduite à une variable propositionnelle."""
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return len(sous_f) == 0 and racine not in ("True", "False", "")


def est_litteral(formule: str) -> bool:
    """Un littéral est un atome p ou la négation d'un atome (NOT p)."""
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    if len(sous_f) == 0:
        return est_atome(formule)
    if racine == "NOT" and len(sous_f) == 1:
        return est_atome(sous_f[0])
    return False


def est_clause(formule: str) -> bool:
    """Une clause est un littéral ou un OR de clauses (somme de littéraux)."""
    if est_litteral(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "OR" and all(est_clause(sf) for sf in sous_f)


def est_terme(formule: str) -> bool:
    """Un terme est un littéral ou un AND de termes (produit de littéraux)."""
    if est_litteral(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "AND" and all(est_terme(sf) for sf in sous_f)


def est_fnc(formule: str) -> bool:
    """Une FNC est une clause ou un AND de FNC (produit de sommes de littéraux)."""
    if est_clause(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "AND" and all(est_fnc(sf) for sf in sous_f)


def est_fnd(formule: str) -> bool:
    """Une FND est un terme ou un OR de FND (somme de produits de littéraux)."""
    if est_terme(formule):
        return True
    res = decompose(formule)
    if res is None:
        return False
    racine, sous_f = res
    return racine == "OR" and all(est_fnd(sf) for sf in sous_f)


# Vérification sur les expressions de l'Exercice 9 du TD :
# 1. x.y + y.~z -> FND uniquement
assert est_fnd("(x AND y) OR (y AND (NOT z))") is True
assert est_fnc("(x AND y) OR (y AND (NOT z))") is False

# 2. (x + y + z).(y + ~z) -> FNC uniquement
assert est_fnd("((x OR y) OR z) AND (y OR (NOT z))") is False
assert est_fnc("((x OR y) OR z) AND (y OR (NOT z))") is True

# 5. x.y.z -> à la fois FND et FNC !
assert est_fnd("(x AND y) AND z") is True
assert est_fnc("(x AND y) AND z") is True</code></pre>
    </div>
  </details>
</div>
'''

with open(os.path.join(W03, 'tp.fr.html'), 'w', encoding='utf-8') as f:
    f.write(fr.strip() + '\n')

with open(os.path.join(W03, 'tp.fa.html'), 'w', encoding='utf-8') as f:
    f.write(fa.strip() + '\n')

print("Generated tp.fr.html and tp.fa.html in w03 successfully.")
