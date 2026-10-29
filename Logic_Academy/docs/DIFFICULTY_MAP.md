# DIFFICULTY MAP & COGNITIVE REMEDIATION
## UL2IN007 / LU2IN007 Logique — Sorbonne Université
### Analyse Approfondie des Obstacles Conceptuels & Stratégies Pédagogiques

Ce document analyse les 15 difficultés majeures documentées lors de l'apprentissage de la Logique (sessions 2025–2026), identifie la cause profonde de chaque blocage, explicite les prérequis conceptuels manquants, et définit les remédiations interactives et les rubriques d'autocorrection *"Pourquoi je me trompe ?" / "چرا اشتباه میکنم؟"*.

---

## Sommaire des Difficultés Documentées

1. [Symboles et Sémantique de l'Implication Propositionnelle](#1-symboles-et-sémantique-de-limplication-propositionnelle)
2. [Syntaxe, Arbres de Syntaxe Abstraite (AST) et Décomposition Récursive](#2-syntaxe-arbres-de-syntaxe-abstraite-ast-et-décomposition-récursive)
3. [Interprétation Récursive en Python (TP 1.2.3)](#3-interprétation-récursive-en-python-tp-123)
4. [Algèbre Booléenne vs Logique Propositionnelle & Simplifications](#4-algèbre-booléenne-vs-logique-propositionnelle--simplifications)
5. [Satisfiabilité, Validité, Conséquence Sémantique et Équivalence](#5-satisfiabilité-validité-conséquence-sémantique-et-équivalence)
6. [Formes Normales Conjonctives (FNC) et Disjonctives (FND)](#6-formes-normales-conjonctives-fnc-et-disjonctives-fnd)
7. [Déduction Naturelle Propositionnelle & Preuves Édukera](#7-déduction-naturelle-propositionnelle--preuves-édukera)
8. [Résolution SAT, Algorithme DPLL & Solveur Glucose](#8-résolution-sat-algorithme-dpll--solveur-glucose)
9. [LPPO Syntaxe : Termes, Prédicats et Arités](#9-lppo-syntaxe--termes-prédicats-et-arités)
10. [Variables Libres, Variables Liées, Portée et Renommage](#10-variables-libres-variables-liées-portée-et-renommage)
11. [Sémantique de la LPPO, Modèles Finis et Substitutions Admissibles](#11-sémantique-de-la-lppo-modèles-finis-et-substitutions-admissibles)
12. [Preuves avec Quantificateurs en Déduction Naturelle (Édukera)](#12-preuves-avec-quantificateurs-en-déduction-naturelle-édukera)
13. [Règle de Résolution & Algorithme d'Unification (Robinson)](#13-règle-de-résolution--algorithme-dunification-robinson)
14. [Prolog, Arbres SLD et Manipulation de Listes](#14-prolog-arbres-sld-et-manipulation-de-listes)
15. [Théorème de Herbrand, Formes Prénexes et Skolémisation](#15-théorème-de-herbrand-formes-prénexes-et-skolémisation)

---

## 1. Symboles et Sémantique de l'Implication Propositionnelle

### Origine de la Difficulté
Confusion fréquente entre l'implication causale du langage naturel ("si $P$ alors $Q$" suggérant un lien de cause à effet temporel) et l'implication matérielle de la logique formelle. Difficulté à saisir pourquoi une implication $p \Rightarrow q$ est décrétée **vraie** dès que sa prémisse $p$ est fausse (*ex falso quodlibet*).
De plus, confusion linguistique entre condition nécessaire et condition suffisante :
- "Pour que je me promène, il faut qu'il fasse beau" $\implies \text{promène} \Rightarrow \text{beau}$.
- "Pour que je me promène, il suffit qu'il fasse beau" $\implies \text{beau} \Rightarrow \text{promène}$.

### Prérequis à Enseigner de Zéro
- Définition d'un connecteur comme une fonction de vérité booléenne $\{0, 1\}^2 \to \{0, 1\}$.
- Équivalence sémantique fondamentale : $(p \Rightarrow q) \equiv (\neg p \lor q)$.
- Contrat d'honnêteté : une promesse "Si tu as 20/20, je t'offre un cadeau" n'est brisée que si l'élève a 20/20 et ne reçoit aucun cadeau. S'il n'a pas 20/20, la promesse n'est jamais violée.

### Outil Interactif Dédié
- **Sélecteur interactif d'implication :** Curseurs pour activer $p \in \{0, 1\}$ et $q \in \{0, 1\}$ avec affichage dynamique de la promesse tenue/violée et traduction instantanée en français et persan.

### Rubrique "Pourquoi je me trompe ?"
- **Erreur type :** Traduire "Je ne me promène que s'il fait beau" par $\text{beau} \Rightarrow \text{promène}$.
- **Diagnostic :** Inversion de la prémisse et de la conclusion. "Que si" exprime une condition *nécessaire*, non suffisante.
- **Règle de détection :** Poser le contre-exemple : "S'il fait beau mais qu'il y a une tempête de grêle, suis-je obligé de me promener ?" Non ! Donc le beau temps ne suffit pas.

---

## 2. Syntaxe, Arbres de Syntaxe Abstraite (AST) et Décomposition Récursive

### Origine de la Difficulté
Incapacité à identifier le connecteur principal d'une formule complexe non entièrement parenthésée ou dotée de parenthèses imbriquées (ex: $\neg(p \land (q \Rightarrow ((q \lor r) \land q)))$). Confusion entre atome, sous-formule immédiate et étiquette de feuille.

### Prérequis à Enseigner de Zéro
- Grammaire formelle de la logique : $\mathcal{F} ::= p \mid \neg F \mid (F_1 \land F_2) \mid (F_1 \lor F_2) \mid (F_1 \Rightarrow F_2) \mid (F_1 \Leftrightarrow F_2)$.
- Règles d'associativité et de priorité décroissante : $\neg > \land > \lor > \Rightarrow > \Leftrightarrow$ (associativité à droite pour $\Rightarrow$).
- Définition topologique de l'AST : la racine est le dernier opérateur appliqué ; les feuilles sont les atomes.
- Notation préfixe (polonaise) : parcours préfixe de l'AST (Racine, Gauche, Droite).

### Outil Interactif Dédié
- **Visualiseur AST & Surligneur Syntaxique :** Au survol d'un sous-arbre, la portion de chaîne correspondante s'illumine. Visualisation pas à pas du parcours préfixe.

---

## 3. Interprétation Récursive en Python (TP 1.2.3)

### Origine de la Difficulté
Blocage lors de l'implémentation de `decompose(formule)` et `eval_formule(formule, valuation)`. Confusion sur la raison pour laquelle un atome renvoie `('p', [])` sans sous-arbres, et pourquoi `TRUE` et `FALSE` sont des feuilles sans être des variables propositionnelles ordinaires. Difficulté à concevoir l'empilement des appels récursifs dans la call-stack.

### Prérequis à Enseigner de Zéro
- Induction structurelle sur les arbres en informatique.
- Cas de base vs cas récursif :
  - Si l'AST a 0 enfant : c'est une feuille (atome ou constante booléenne).
  - Si l'AST a 1 enfant (connecteur unaire `NOT`) : un appel récursif.
  - Si l'AST a 2 enfants (connecteur binaire `AND`, `OR`, `IMPLIES`) : deux appels récursifs combinés par l'opération booléenne.

### Outil Interactif Dédié
- **Simulateur Récursif de Call-Stack :** Visualisation étape par étape des frames de pile lors de l'évaluation de `eval_formule("(NOT p) AND (q OR r)", {"p": False, "q": True, "r": False})`.

---

## 4. Algèbre Booléenne vs Logique Propositionnelle & Simplifications

### Origine de la Difficulté
Malaise face à l'alternance d'écriture entre logique ($\neg, \land, \lor$) et algèbre de Boole $(\bar{x}, \cdot, +)$. Application fautive de lois de distributivité inexistantes ou oubli des règles d'absorption ($B \lor (A \land B) \equiv B$).

### Prérequis à Enseigner de Zéro
- Isomorphisme strict entre l'algèbre des propositions et l'algèbre de Boole à deux éléments $\langle \{0, 1\}, \lor, \land, \neg, 0, 1 \rangle$.
- Table complète des 12 lois algébriques fondamentales.
- Démonstrations algébriques pas à pas avec citation impérative de la règle à chaque étape :
  $$B \lor (A \land B) \equiv (B \land \top) \lor (B \land A) \equiv B \land (\top \lor A) \equiv B \land \top \equiv B$$

---

## 5. Satisfiabilité, Validité, Conséquence Sémantique et Équivalence

### Origine de la Difficulté
Confusion conceptuelle grave :
- Croire qu'une formule satisfiable est valide.
- Déclarer deux formules équivalentes parce qu'elles coïncident sur une seule ligne d'une table de vérité.
- Ne pas savoir comment réfuter une conséquence sémantique $F \models G$ par un contre-modèle.

### Prérequis à Enseigner de Zéro
- **Formule satisfiable :** $\exists v, [F]_v = 1$.
- **Formule valide (tautologie) :** $\forall v, [F]_v = 1$.
- **Formule insatisfiable :** $\forall v, [F]_v = 0$.
- **Conséquence sémantique $F \models G$ :** Pour toute valuation $v$, si $[F]_v = 1$ alors $[G]_v = 1$ (équivaut à : la formule $F \Rightarrow G$ est valide).
- **Contre-modèle :** Une valuation spécifique $v$ où $[F]_v = 1$ et $[G]_v = 0$.

---

## 6. Formes Normales Conjonctives (FNC) et Disjonctives (FND)

### Origine de la Difficulté
Difficulté à distinguer syntaxiquement FNC et FND. Erreurs lors de la double distributivité conduisant à des formules syntaxiquement invalides comme $(x + y) \cdot (z + y)$ sans justification.

### Prérequis à Enseigner de Zéro
- **Littéral :** Variable ou négation de variable ($p$ ou $\neg p$).
- **Clause :** Disjonction de littéraux $(l_1 \lor \dots \lor l_k)$.
- **Terme (dual) :** Conjonction de littéraux $(l_1 \land \dots \land l_k)$.
- **FNC :** Conjonction de clauses $\bigwedge_i \bigvee_j l_{i,j}$.
- **FND :** Disjonction de termes $\bigvee_i \bigwedge_j l_{i,j}$.
- Règle de vérification obligatoire : tester la formule obtenue avec des valuations cibles ($x=1, y=0, z=0$) pour confirmer la préservation sémantique.

---

## 7. Déduction Naturelle Propositionnelle & Preuves Édukera

### Origine de la Difficulté
C'est le point de blocage historique majeur :
- Quand et comment ouvrir une hypothèse ?
- Quand une hypothèse est-elle déchargée (fermée) ?
- Pourquoi a-t-on le droit de déduire $B$ après avoir prouvé une contradiction $\bot$ ?
- Pourquoi le raisonnement par l'absurde classique ($RAA$) est-il interdit en logique intuitionniste ?

### Prérequis à Enseigner de Zéro
- Anatomie d'un jugement : $\Gamma \vdash A$ (sous les hypothèses actives $\Gamma$, la formule $A$ est prouvée).
- Visualisation en boîtes de Fitch :
  - Pour prouver $A \Rightarrow B$, on ouvre une boîte avec l'hypothèse $A$, on dérive $B$, puis on ferme la boîte et on conclut $A \Rightarrow B$ au niveau supérieur via la règle $\Rightarrow I$. L'hypothèse $A$ n'est plus accessible !
  - Distinction formelle :
    - $\bot E$ (intuitionniste) : De $\bot$, on déduit n'importe quelle proposition $B$.
    - $\neg I$ (intuitionniste) : Si supposer $A$ mène à $\bot$, on a prouvé $\neg A$.
    - $RAA$ (classique uniquement) : Si supposer $\neg A$ mène à $\bot$, on conclut $A$.

---

## 8. Résolution SAT, Algorithme DPLL & Solveur Glucose

### Origine de la Difficulté
Perception de DPLL comme une boîte noire plutôt que comme un algorithme précis de parcours d'arbre avec simplification d'états clausaux.

### Prérequis à Enseigner de Zéro
- Format clausale : ensemble de clauses $\Sigma = \{C_1, \dots, C_m\}$.
- Règle unitaire : si $\{l\} \in \Sigma$, affecter $l \leftarrow 1$, supprimer toutes les clauses contenant $l$, et retirer $\neg l$ des autres clauses.
- Heuristique $h_k$ : calcul rigoureux du nombre d'occurrences pour briser les symétries.
- Trace formelle d'exécution : afficher l'ensemble de clauses résiduel $\Sigma$ après chaque affectation.

---

## 9. LPPO Syntaxe : Termes, Prédicats et Arités

### Origine de la Difficulté
Confusion entre terme et formule. Croire que $f(x)$ est une proposition ou que $P(x)$ est un terme.

### Prérequis à Enseigner de Zéro
- **Terme :** Désigne un **objet** du domaine de discours (constante $c$, variable $x$, ou fonction $f(t_1, \dots, t_n)$). Un terme ne possède PAS de valeur de vérité !
- **Formule :** Énonce une **affirmation** vraie ou fausse (prédicat $P(t_1, \dots, t_n)$, égalité $t_1 = t_2$, ou formule connectée/quantifiée).
- Définition inductive des termes : $\mathcal{T}_0$ (constantes et variables), $\mathcal{T}_{k+1} = \mathcal{T}_k \cup \{f(t_1, \dots, t_n) \mid t_i \in \mathcal{T}_k\}$.

---

## 10. Variables Libres, Variables Liées, Portée et Renommage

### Origine de la Difficulté
Erreurs dans le calcul de $Free(F)$ et lors du renommage ($\alpha$-conversion), provoquant des captures accidentelles de variables libres.

### Prérequis à Enseigner de Zéro
- Portée (*scope*) d'un quantificateur : le sous-arbre immédiat associé à $\forall x$ ou $\exists x$.
- Règle récursive de calcul de $Free(F)$ :
  - $Free(P(t_1, \dots, t_n)) = \text{Var}(t_1) \cup \dots \cup \text{Var}(t_n)$.
  - $Free(\neg F) = Free(F)$.
  - $Free(F_1 \land F_2) = Free(F_1) \cup Free(F_2)$.
  - $Free(\forall x F) = Free(F) \setminus \{x\}$.
- Règle de renommage sûr : on ne peut renommer une variable liée $x$ en $y$ que si $y$ n'apparaît pas libre dans la portée de $x$.

---

## 11. Sémantique de la LPPO, Modèles Finis et Substitutions Admissibles

### Origine de la Difficulté
Incompréhension de ce qu'est une structure $\mathcal{M} = \langle D, \mathcal{I} \rangle$ et comment évaluer des formules quantifiées sur des univers finis. Erreurs de substitution où un terme $t$ contient une variable capturée par un quantificateur de $F$.

### Prérequis à Enseigner de Zéro
- Définition d'un domaine $D$ (non vide).
- Interprétation des symboles : chaque fonction devient une vraie opération mathématique $f^\mathcal{M} : D^n \to D$ ; chaque prédicat devient une relation $P^\mathcal{M} \subseteq D^n$.
- Évaluation finie : si $D = \{a, b\}$, alors $\forall x P(x) \equiv P(a) \land P(b)$ et $\exists x P(x) \equiv P(a) \lor P(b)$.
- Condition d'admissibilité de la substitution : un terme $t$ est librement substituable à $x$ dans $F$ si aucune variable de $t$ ne devient liée après remplacement.

---

## 12. Preuves avec Quantificateurs en Déduction Naturelle (Édukera)

### Origine de la Difficulté
Hésitation critique sur les règles $\forall I$ et $\exists E$ : quelle variable introduire ? Quelle condition d'eigenvariable vérifier ?

### Prérequis à Enseigner de Zéro
- **Règle $\forall I$ :** Pour prouver $\forall x F$, on prouve $F[x \leftarrow y]$ où $y$ est une variable fraîche arbitraire qui n'apparaît dans aucune hypothèse active.
- **Règle $\forall E$ :** De $\forall x F$, on peut déduire $F[x \leftarrow t]$ pour **n'importe quel** terme $t$ admissible.
- **Règle $\exists I$ :** Pour prouver $\exists x F$, il suffit d'exhiber un terme témoin $t$ tel que $F[x \leftarrow t]$ soit vrai.
- **Règle $\exists E$ :** Pour utiliser $\exists x F$ pour prouver un but $C$, on ouvre une sous-preuve avec l'hypothèse $F[x \leftarrow y]$ avec $y$ fraîche, on dérive $C$, et si $y$ ne figure pas dans $C$ ni dans les hypothèses restantes, on conclut $C$.

---

## 13. Règle de Résolution & Algorithme d'Unification (Robinson)

### Origine de la Difficulté
Difficulté à calculer le plus général unificateur (MGU), oubli de l'occurs-check ($x$ unifié avec un terme contenant $x$), et confusion entre satisfiabilité et preuve par réfutation.

### Prérequis à Enseigner de Zéro
- Deux littéraux sont complémentaires s'ils ont le même prédicat, l'un positif, l'autre négatif, et que leurs arguments sont unifiables.
- Algorithme de Robinson : système d'équations de termes, décomposition, élimination des variables, échec si $x = f(\dots x \dots)$ (*occurs check*).
- Réfutation : Pour prouver $\Sigma \models F$, on met $\Sigma \cup \{\neg F\}$ sous forme clausale et on applique la résolution jusqu'à dériver la clause vide $\Box$.

---

## 14. Prolog, Arbres SLD et Manipulation de Listes

### Origine de la Difficulté
Compréhension du moteur de Prolog : ordre d'évaluation des buts (de gauche à droite), choix des règles (de haut en bas), retour en arrière (backtracking), et structure récursive des listes `[Tete | Reste]`.

### Prérequis à Enseigner de Zéro
- Définition d'une clause de Horn : au plus un littéral positif.
  - Fait : `p(a).` $\equiv p(a) \leftarrow \top$.
  - Règle : `p(X) :- q(X), r(X).` $\equiv p(X) \leftarrow q(X) \land r(X)$.
  - But : `?- p(X).` $\equiv \leftarrow p(X)$ (requête de réfutation).
- Arbre SLD : branche de succès (substitution réponse trouvée), branche d'échec (aucun unificateur possible $\implies$ retour arrière).

---

## 15. Théorème de Herbrand, Formes Prénexes et Skolémisation

### Origine de la Difficulté
Confusion capitale entre **équivalence logique** ($\equiv$) et **équi-satisfiabilité** ($\approx_{\text{sat}}$). Erreur sur l'arité des fonctions de Skolem (croire qu'une constante de Skolem suffit quand un existentiel est sous la portée d'un universel).

### Prérequis à Enseigner de Zéro
- **Forme prénexe :** Tous les quantificateurs en tête. Requiert de renommer d'abord les variables pour éviter toute collision lors de l'extrusion.
- **Skolémisation :**
  - Si $\exists y$ n'est dominé par aucun quantificateur universel : $y$ est remplacé par une constante de Skolem fraîche $c$.
  - Si $\exists y$ est dominé par $\forall x_1, \dots, \forall x_k$ : $y$ est remplacé par un terme fonctionnel $f(x_1, \dots, x_k)$ où $f$ est un nouveau symbole fonctionnel d'arité $k$.
- **Théorème fondamental :** La formule skolémisée $F^*$ **n'est pas équivalente** à $F$ (sa signature est enrichie), mais elle est **équi-satisfiable** : $F$ a un modèle si et seulement si $F^*$ a un modèle.
