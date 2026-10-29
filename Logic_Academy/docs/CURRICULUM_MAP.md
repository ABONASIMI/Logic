# CURRICULUM MAP — LOGIC ACADEMY (UL2IN007 / LU2IN007)
Sorbonne Université — Faculté des Sciences et Ingénierie

Cette cartographie curriculaire structure l'apprentissage en **11 semaines cohérentes**. Elle résout la divergence historique entre les anciens numéros de cours magistraux et la maquette 2026–2027 (notamment l'avancement de DPLL/SAT au Thème 4 et le placement de la Déduction Naturelle aux Thèmes 5 et 6).

---

## Vue Synoptique du Cursus (Semaines 1 à 11)

| Semaine | Thème Pédagogique | Cours Magistral | Fiche TD (2026-27) | Fiche TP (2026-27) | Annales Cibles |
|---|---|---|---|---|---|
| **Semaine 1** | **Syntaxe propositionnelle, AST & Sémantique** | `cours1-moodle.pdf` (2026) | Thème 1 : Ex 1, 2, 3 | Thème 1.2.3 : Ex 1, 2 (Python AST) | Partiels & Examens (Q1) |
| **Semaine 2** | **Interprétations, Validité & Algèbre Booléenne** | `cours2-moodle.pdf` (2026) | Thème 2 : Ex 4, 5, 6, 7, 8 | Thème 1.2.3 : Ex 3, 4 (Valuation Python) | Partiels (Ex 1, 2) |
| **Semaine 3** | **Fonctions Booléennes & Formes Normales (CNF/DNF)** | `cours3-moodle.pdf` (2026) | Thème 3 : Ex 9, 10, 11, 12, 13 | Thème 1.2.3 : Ex 5 (Table de vérité Python) | Partiels (Ex 2, 3) |
| **Semaine 4** | **SAT, Algorithme DPLL & Solveur Glucose** | `cours6.pdf` (DPLL-SAT) | Thème 4 : Ex 14, 15, 16 | Thème 4 & 5 : Ex 6, 7, 8, 9, 10, 11, 12 | Partiels & Examens DPLL |
| **Semaine 5** | **Déduction Naturelle Propositionnelle (Intuitionniste)** | `cours4-moodle.pdf` (Connecteurs) | Thème 5 : Ex 17, 18 | Thème 6.7 : Ex 13 (Édukera Prop) | Partiels & Examens NatDed |
| **Semaine 6** | **Règles Dérivées, Logique Classique & Absurde** | `cours5-moodle.pdf` (Classique) | Thème 6 : Ex 19, 20, 21 | Thème 6.7 : Ex 13 (Édukera Tiers Exclu) | Partiels & Examens Classique |
| **Semaine 7** | **LPPO Syntaxe : Termes, Prédicats & Variables Liées** | `cours7-moodle.pdf` (LPPO Syntaxe) | Thème 7 : Ex 22, 23, 24, 25, 26 | Thème 8 : Ex 14, 15 (Termes Python) | Examens Terminaux LPPO |
| **Semaine 8** | **LPPO Sémantique : Modèles, Valuations & Substitutions** | `cours8-moodle.pdf` (LPPO Sémantique) | Thème 8 : Ex 27, 28, 29, 30, 31, 32 | Thème 8 : Ex 15 suite (Modèles finis) | Examens Terminaux LPPO |
| **Semaine 9** | **Déduction Naturelle LPPO (Quantificateurs)** | `cours9-moodle.pdf` (Quantificateurs) | Thème 9 : Ex 33, 34 | Thème 9 : Édukera Quantificateurs | Examens Terminaux NatDed |
| **Semaine 10** | **Résolution & Unification (Propositionnel & Premier Ordre)** | `Logique_cours 10_Prolog.pdf` (Partie 1) | Thème 10 : Ex 35, 36, 37, 38, 39 | Thème 10 : Ex 16, 17, 18 (Prolog intro) | Examens Terminaux Résolution |
| **Semaine 11** | **Programmation Logique (Prolog) & Formes Normales LPPO** | `Logique_cours 10` (P2) + `Cours11` | Thème 11 : Ex 40, 41 | Thème 11 : Ex 19, 20, 21 (Prolog listes) | Examens Terminaux Herbrand/Prolog |

---

## Détail Semaine par Semaine

### SEMAINE 1 — Syntaxe de la Logique Propositionnelle, AST & Tables de Vérité
- **Cours Associé :** `cours1-moodle.pdf` (Édition 2026–2027, 23 pages).
  - *Notions fondamentales :* Définition inductive de l'ensemble des formules $\mathcal{F}$, connecteurs ($\neg, \land, \lor, \Rightarrow, \Leftrightarrow$), arbre de syntaxe abstraite (AST), connecteur principal, notation préfixe (polonaise), associativité et priorités opératoires, sémantique des connecteurs, table de vérité, analyse sémantique de l'implication matérielle ("si... alors", "seulement si", "il suffit", "il faut").
- **TD Thème 1 (p. 2-3 de `main_td-etudiants.pdf`) :**
  - **Exercice 1 :** Arbre de syntaxe abstraite et notation préfixe.
    - Q1 : Décomposition et AST de $F_1 = \neg(p \land (q \Rightarrow ((q \lor r) \land q)))$ et $F_2 = \neg p \land q \Rightarrow q \lor r \land q$.
    - Q2 : Parenthésage complet respectant les priorités pour $F_3 = p \land q \land r \land s$ et $F_4 = p \Rightarrow q \land \neg r \Rightarrow p \lor q$.
  - **Exercice 2 :** Implication et langage naturel.
    - Q1 : Analyse des conditions "S'il fait beau...", "Il faut qu'il fasse beau...", "Seulement si...", "Il suffit...".
    - Q2 : Détermination de la valeur de vérité des propositions conditionnelles.
  - **Exercice 3 :** Tables de vérité et énigmes logiques.
    - Énigme de l'île des menteurs et des véridiques (habitants A et B). Modélisation propositionnelle et résolution par table de vérité.
- **TP Thème 1.2.3 — Partie 1 (p. 2-3 de `main_tp-etudiants.pdf`) :**
  - **Exercice 1 :** Décomposition en sous-formules et AST.
    - Implémentation récursive de `eval_TF(formule: str) -> bool` pour les formules closes composées de `TRUE` et `FALSE`.
  - **Exercice 2 :** Découverte des formules atomiques.
    - Spécification de `decompose(formule: str) -> tuple[str, list[str]]`.
    - Implémentation de `genere_fa(formule: str) -> set[str]` pour extraire l'ensemble des variables propositionnelles.
- **Annales Liées :**
  - `partiel_2015_2016.pdf` Ex 1 (Syntaxe et arbres).
  - `partiel_2017_2018.pdf` Ex 1 (Parenthésage et tables).
  - `examen1_2016_2017.pdf` Ex 1 (Définition inductive d'une formule).

---

### SEMAINE 2 — Interprétations, Validité, Conséquence Sémantique & Algèbre Booléenne
- **Cours Associé :** `cours2-moodle.pdf` (Édition 2026–2027, 23 pages).
  - *Notions fondamentales :* Valuation $v : \mathcal{V} \to \{0, 1\}$, valeur de vérité $[F]_v$, modèle d'une formule, formule satisfiable, formule valide (tautologie), formule insatisfiable (antilogie / contradiction), conséquence sémantique $F \models G$ et ensemble de formules $\Sigma \models G$, équivalence logique $F \equiv G$, lois fondamentales de l'algèbre de Boole (idempotence, associativité, commutativité, distributivité, De Morgan, absorption, tiers exclu, contradiction, élimination de l'implication).
- **TD Thème 2 (p. 4-6 de `main_td-etudiants.pdf`) :**
  - *Contrainte impérative : Ne pas utiliser de table de vérité !*
  - **Exercice 4 :** Formules satisfiables et valides par raisonnement sémantique.
  - **Exercice 5 :** Conséquence sémantique : prouver $F \models G$ ou trouver un contre-modèle.
  - **Exercice 6 :** Équivalence logique : démonstrations algébriques.
  - **Exercice 7 :** Simplification d'expressions booléennes (absorption, distributivité).
  - **Exercice 8 :** "Faut-il toujours croire ChatGPT ?" : analyse critique d'une simplification proposée par une IA, détection de fallacies, contre-modèle explicite.
- **TP Thème 1.2.3 — Partie 2 (p. 3-5 de `main_tp-etudiants.pdf`) :**
  - **Exercice 2 (suite) :** Évaluation récursive d'une formule selon une valuation donnée `eval_formule(formule, valuation)`.
  - **Exercice 3 :** Génération de toutes les interprétations possibles `genere_interpretations(fa)` ($2^n$ valuations).
  - **Exercice 4 :** Fonctions sémantiques : `is_satisfiable(formule)`, `is_valid(formule)`, `models(formule)`, et `consequence_sem(formule1, formule2)`.
- **Annales Liées :**
  - `partiel_2019_2020_L2.pdf` Ex 1 (Satisfiabilité et validité sans table).
  - `partiel_2020_2021_L2.pdf` Ex 2 (Conséquence sémantique et contre-exemples).
  - `examen1_2020_2021.pdf` Ex 4 (Modèle et conséquence sémantique).

---

### SEMAINE 3 — Fonctions Booléennes, Formes Normales (FNC / FND) & Complétude
- **Cours Associé :** `cours3-moodle.pdf` (Édition 2026–2027, 24 pages).
  - *Notions fondamentales :* Fonction booléenne $f : \{0, 1\}^n \to \{0, 1\}$, littéral (positif $p$, négatif $\neg p$), clause disjonctive, clause conjonctive (terme), Forme Normale Conjonctive (FNC / CNF), Forme Normale Disjonctive (FND / DNF), algorithme de passage table de vérité $\to$ FND (somme de mintermes), passage table $\to$ FNC (produit de maxtermes), mise sous forme normale par équivalences algébriques, satisfiabilité triviale d'une FND, validité triviale d'une FNC, complétude fonctionnelle d'un ensemble de connecteurs (systèmes complets $\{\neg, \land\}$, $\{\neg, \lor\}$, connecteurs universels NAND / NOR).
- **TD Thème 3 (p. 7-8 de `main_td-etudiants.pdf`) :**
  - **Exercice 9 :** Identification rigoureuse des formes normales (FNC, FND, les deux, aucune).
  - **Exercice 10 :** Critères syntaxiques de validité d'une FNC et d'insatisfiabilité d'une FND.
  - **Exercice 11 :** Fonctions booléennes et cardinalité ($2^{2^n}$).
  - **Exercice 12 :** Reconstruction de la table de vérité à partir d'une FNC ou FND.
  - **Exercice 13 :** Mise sous forme normale (FNC et FND) par manipulation algébrique sans table de vérité.
- **TP Thème 1.2.3 — Partie 3 (p. 5-6 de `main_tp-etudiants.pdf`) :**
  - **Exercice 3 (suite) :** Construction de la table de vérité complète sous forme de tableau 2D.
  - **Exercice 5 :** Analyseur syntaxique complet : implémentation de `trouve_prochain_connec` et `decompose` prenant en compte le parenthésage arbitraire.
- **Annales Liées :**
  - `partiel_2021_2022_S2.pdf` Ex 1 & 2 (FNC, FND et complétude).
  - `partiel_2022_2023_S2.pdf` Ex 1 (Formes normales et simplification).
  - `examen1_2021_2022_L2.pdf` Ex 1 (Fonctions booléennes et FNC).

---

### SEMAINE 4 — Le Problème SAT, l'Algorithme DPLL & le Solveur Glucose
- **Cours Associé :** `cours6.pdf` (Cours DPLL-SAT, 96 pages).
  - *Notions fondamentales :* Le problème SAT, complexité NP-complète (théorème de Cook-Levin), clause vide $\Box$ (contradiction / faux), clause unitaire, règle de propagation unitaire (UP), règle du littéral pur (PL), règle de décision et branchement binaire, retour sur trace (backtracking), algorithme DPLL classique (Davis-Putnam-Logemann-Loveland), heuristiques de choix de variables ($h_k$, MOM, VSIDS), formats de modélisation (DIMACS CNF).
- **TD Thème 4 (p. 9-10 de `main_td-etudiants.pdf`) :**
  - **Exercice 14 :** Propagation unitaire pas à pas sur des ensembles de clauses.
  - **Exercice 15 :** Exécution complète de l'algorithme DPLL avec arbre de recherche, application de la règle du littéral pur et de l'heuristique $h_k$, avec ordre de branchement conventionnel (faux d'abord si spécifié).
  - **Exercice 16 :** Modélisation SAT : choix d'une garniture de pizza sous contraintes diététiques et gustatives.
- **TP Thème 4 & 5 (p. 7-15 de `main_tp-etudiants.pdf`) :**
  - **Exercice 6 :** Prise en main du solveur Glucose et syntaxe des fichiers `.cnf` DIMACS (`p cnf n m`).
  - **Exercice 7 :** Résolution du problème des pizzas avec Glucose.
  - **Exercice 8 :** Modélisation de l'énigme du Club Écossais en clauses DIMACS.
  - **Exercice 9 :** Énigme des chapeaux rouges.
  - **Exercices 10, 11, 12 :** Modélisation informatique et logique d'un problème de coloration de graphe / placement, et script Python de génération automatique de DIMACS.
- **Annales Liées :**
  - `partiel_2018_2019.pdf` Ex 2 (Trace DPLL pas à pas).
  - `partiel_2020_2021_L3.pdf` Ex 2 (DPLL et propagation unitaire).
  - `examen1_2022_2023_L3.pdf` Ex 2 (Modélisation SAT et solveur).

---

### SEMAINE 5 — Déduction Naturelle Propositionnelle (Logique Intuitionniste)
- **Cours Associé :** `cours4-moodle.pdf` (Règles de déduction : connecteurs, 26 pages).
  - *Notions fondamentales :* Système de déduction naturelle de Gentzen, notion de jugement de déductibilité $\Gamma \vdash A$, hypothèses actives vs déchargées, boîtes de sous-preuve, règles d'introduction ($I$) et d'élimination ($E$) pour chaque connecteur : $\land I, \land E_1, \land E_2, \lor I_1, \lor I_2, \lor E, \Rightarrow I, \Rightarrow E$ (Modus Ponens), $\neg I, \neg E, \bot E$ (règle de l'absurde intuitionniste / *ex falso quodlibet*).
- **TD Thème 5 (p. 11 de `main_td-etudiants.pdf`) :**
  - *Contrainte formelle : Utilisation stricte de la déduction naturelle intuitionniste (interdiction du tiers exclu, de la double négation classique et du raisonnement par l'absurde classique).*
  - **Exercice 17 :** Preuves formelles complètes :
    - $p \land q \vdash q \land p$
    - $p \Rightarrow q, q \Rightarrow r \vdash p \Rightarrow r$
    - $\vdash p \Rightarrow (q \Rightarrow p)$
    - $p \lor q \vdash \neg(\neg p \land \neg q)$
    - $p \Rightarrow (q \Rightarrow r) \vdash (p \land q) \Rightarrow r$
  - **Exercice 18 :** Résolution d'énigme logique par preuve formelle en déduction naturelle.
- **TP Thème 6.7 (p. 16-18 de `main_tp-etudiants.pdf`) :**
  - **Exercice 13 :** Début du module Édukera : manipulation interactive des pièces de puzzle de preuve, ouverture et fermeture correcte des contextes d'hypothèses.
- **Annales Liées :**
  - `partiel_2016_2017.pdf` Ex 3 (Preuves propositionnelles en déduction naturelle).
  - `partiel_2017_2018.pdf` Ex 3 (Déduction naturelle intuitionniste).
  - `examen1_2018_2019.pdf` Ex 3 (Preuves formelles et arbres de dérivation).

---

### SEMAINE 6 — Règles Dérivées, Logique Classique & Raisonnement par l'Absurde
- **Cours Associé :** `cours5-moodle.pdf` (Règles dérivées - logiques classiques et intuitionnistes, 11 pages).
  - *Notions fondamentales :* Différence philosophique et mathématique entre logique intuitionniste et logique classique, principe du Tiers Exclu ($TE : \vdash A \lor \neg A$), règle d'élimination de la double négation ($\neg\neg E : \neg\neg A \vdash A$), Raisonnement par l'Absurde Classique ($RAA$), règles dérivées (Modus Tollens, contraposition $\neg q \Rightarrow \neg p \vdash p \Rightarrow q$, loi de Peirce $((p \Rightarrow q) \Rightarrow p) \vdash p$).
- **TD Thème 6 (p. 12 de `main_td-etudiants.pdf`) :**
  - **Exercice 19 :** Comparaison logique intuitionniste vs logique classique : prouver pourquoi certaines formules exigent $TE$ ou $RAA$.
  - **Exercice 20 :** Preuves de théorèmes classiques :
    - $\vdash \neg\neg p \Rightarrow p$ (avec $TE$)
    - $\vdash (p \Rightarrow q) \lor (q \Rightarrow p)$
    - $\vdash ((p \Rightarrow q) \Rightarrow p) \Rightarrow p$ (Loi de Peirce)
    - $\neg(p \land q) \vdash \neg p \lor \neg q$ (De Morgan classique)
  - **Exercice 21 :** Énigme résolue par raisonnement classique.
- **TP Thème 6.7 (suite) :**
  - **Exercice 13 (suite) :** Édukera : preuves avancées nécessitant l'utilisation du tiers exclu et des règles dérivées classiques.
- **Annales Liées :**
  - `partiel_2019_2020_MonoMajeure.pdf` Ex 3 (Preuve avec tiers exclu).
  - `examen1_2021_2022_L3.pdf` Ex 3 (Déduction naturelle classique vs intuitionniste).
  - `examen2_2020_2021.pdf` Ex 3 (Double négation et Peirce).

---

### SEMAINE 7 — Logique des Prédicats du Premier Ordre (LPPO) : Syntaxe & Variables
- **Cours Associé :** `cours7-moodle.pdf` (LPPO : syntaxe - sémantique, 23 pages).
  - *Notions fondamentales :* Signature $\mathcal{L} = \langle \mathcal{F}, \mathcal{P}, \text{ar} \rangle$, ensemble des variables $\mathcal{V}$, constantes ($\text{ar}=0$), symboles de fonctions, ensemble inductif des termes $\mathcal{T}(\mathcal{F}, \mathcal{V})$, sous-ensembles $\mathcal{T}_0, \mathcal{T}_1, \dots, \mathcal{T}_k$, symboles de prédicats, formules atomiques $P(t_1, \dots, t_n)$, quantificateurs universel ($\forall$) et existentiel ($\exists$), portée d'un quantificateur, occurrences de variables, variables libres ($Free(F)$), variables liées ($Bound(F)$), formules closes (énoncés / *sentences*), clôture universelle ($\tilde{\forall}F$), renommage alphabétique ($\alpha$-conversion), interdiction de capture de variables.
- **TD Thème 7 (p. 13-15 de `main_td-etudiants.pdf`) :**
  - **Exercice 22 :** Entiers naturels et termes (représentation de Peano avec constante $0$ et fonction successeur $s$).
  - **Exercice 23 :** Construction et reconnaissance de termes avec variables.
  - **Exercice 24 :** Identification des symboles d'une formule (fonctions vs prédicats, arités).
  - **Exercice 25 :** Construction rigoureuse de formules du premier ordre.
  - **Exercice 26 :** Renommage de variables liées et formules équivalentes (détection des captures illicites).
- **TP Thème 8 — Partie 1 (p. 17-22 de `main_tp-etudiants.pdf`) :**
  - **Exercice 14 :** Modélisation en Python de l'ensemble des termes $\mathcal{T}(\mathcal{F}, \mathcal{V})$ : définition inductive des ensembles $\mathcal{T}_k$.
  - **Exercice 15 :** Représentation des formules en LPPO, calcul algorithmique des variables libres d'une formule en Python.
- **Annales Liées :**
  - `examen1_2015_2016.pdf` Ex 6 (Ensemble des termes et induction).
  - `examen1_2017_2018.pdf` Ex 1 (Variables libres et renommage).
  - `examen1_2020_2021.pdf` Ex 1 & 2 (Termes, clôture et variables liées).

---

### SEMAINE 8 — LPPO Sémantique : Structures, Interprétations, Modèles & Substitutions
- **Cours Associé :** `cours8-moodle.pdf` (Interprétation : variables et quantificateurs, 26 pages).
  - *Notions fondamentales :* Structure / Interprétation $\mathcal{M} = \langle D, \mathcal{I} \rangle$, domaine de discours $D \neq \emptyset$, interprétation des constantes $c^\mathcal{M} \in D$, des fonctions $f^\mathcal{M} : D^n \to D$, et des prédicats $P^\mathcal{M} \subseteq D^n$, valuation des variables $v : \mathcal{V} \to D$, évaluation d'un terme $[t]^\mathcal{M}_v$, interprétation d'une formule $[F]^\mathcal{M}_v \in \{0, 1\}$, sémantique de Tarski pour $\forall x F$ et $\exists x F$, modèle $\mathcal{M} \models F$, validité logique $\models F$, satisfiabilité au premier ordre, substitution sans capture $F[x \leftarrow t]$ et condition d'admissibilité (terme libre pour une variable).
- **TD Thème 8 (p. 16-18 de `main_td-etudiants.pdf`) :**
  - **Exercice 27 :** Calcul de substitutions $F[x \leftarrow t]$, détection des substitutions interdites créant des captures.
  - **Exercice 28 :** Interprétation de prédicats et de fonctions sur des domaines arithmétiques ($\mathbb{N}, \mathbb{Z}, \mathbb{R}$).
  - **Exercice 29 :** Évaluation de formules sous différentes valuations.
  - **Exercice 30 :** Quantification de formules atomiques sur des univers finis.
  - **Exercice 31 :** Construction explicite de modèles et de contre-modèles sur des domaines finis.
  - **Exercice 32 :** Interprétation globale de formules complexes du premier ordre.
- **TP Thème 8 — Partie 2 :**
  - **Exercice 15 (suite) :** Évaluation numérique d'une formule du premier ordre sur un domaine fini en Python.
- **Annales Liées :**
  - `examen1_2016_2017.pdf` Ex 3 (Interprétation sur des graphes et relations).
  - `examen1_2019_2020.pdf` Ex 2 (Modèles sur un échiquier $6 \times 6$).
  - `examen1_2022_2023_L2.pdf` Ex 3 (Contre-modèles finis pour invalider une formule).

---

### SEMAINE 9 — Déduction Naturelle au Premier Ordre (Quantificateurs)
- **Cours Associé :** `cours9-moodle.pdf` (Règles de déduction : quantificateurs, 18 pages).
  - *Notions fondamentales :* Règles pour le quantificateur universel :
    - Introduction : $\forall I : \frac{\Gamma \vdash F[x \leftarrow y]}{\Gamma \vdash \forall x F}$ avec condition d'eigenvariable ($y$ fraîche, n'apparaît pas libre dans $\Gamma$ ni dans $\forall x F$).
    - Élimination : $\forall E : \frac{\Gamma \vdash \forall x F}{\Gamma \vdash F[x \leftarrow t]}$ ($t$ libre pour $x$).
  - Règles pour le quantificateur existentiel :
    - Introduction : $\exists I : \frac{\Gamma \vdash F[x \leftarrow t]}{\Gamma \vdash \exists x F}$ (témoin $t$).
    - Élimination : $\exists E : \frac{\Gamma \vdash \exists x F \quad \Gamma, F[x \leftarrow y] \vdash C}{\Gamma \vdash C}$ (condition d'isolation de l'hypothèse avec variable fraîche $y$).
- **TD Thème 9 (p. 19-20 de `main_td-etudiants.pdf`) :**
  - **Exercice 33 :** Preuves de théorèmes quantifiés :
    - $\forall x (p(x) \land q(x)) \vdash (\forall x p(x)) \land (\forall x q(x))$
    - $(\exists x p(x)) \lor (\exists x q(x)) \vdash \exists x (p(x) \lor q(x))$
    - $\forall x p(x) \vdash \exists x p(x)$
    - $(\forall x (p(x) \Rightarrow q(x))) \land (\forall x p(x)) \vdash \forall x q(x)$
  - **Exercice 34 :** Preuves imbriquées et paradoxe du buveur :
    - Démonstration complète de la formule $\exists x (p(x) \Rightarrow \forall y p(y))$ en utilisant la règle du Tiers Exclu appliqué à $\forall y p(y)$.
- **TP Thème 9 (p. 23 de `main_tp-etudiants.pdf`) :**
  - Module Édukera LPPO : preuves formelles interactives avec instanciation de variables et gestion des témoins existentiels.
- **Annales Liées :**
  - `examen1_2015_2016.pdf` Ex 4 & 5 (Preuves quantifiées et analyse d'erreurs d'eigenvariable).
  - `examen1_2018_2019.pdf` Ex 4 (Preuve formelle avec $\forall$ et $\exists$).
  - `examen1_2021_2022_L3.pdf` Ex 5 (Preuve du paradoxe du buveur).

---

### SEMAINE 10 — Règle de Résolution & Algorithme d'Unification
- **Cours Associé :** `Logique_cours 10_Prolog.pdf` (Partie 1 : Résolution et Unification, p. 1-35).
  - *Notions fondamentales :* Forme clausale au premier ordre, littéraux complémentaires, règle de résolution propositionnelle, complétude par réfutation (recherche de la clause vide $\Box$), problème de l'unification syntaxique, substitution $\sigma$, unificateur, plus général unificateur (MGU / $\text{mgu}$), algorithme d'unification de Robinson, test d'occurrence (*occurs-check*), standardisation séparée des variables (*standardizing apart*), règle de résolution au premier ordre :
    $$\frac{C_1 \lor P(t_1, \dots, t_n) \quad C_2 \lor \neg P(u_1, \dots, u_n)}{(C_1 \lor C_2)\sigma} \quad \text{où } \sigma = \text{mgu}(P(\vec{t}), P(\vec{u}))$$
  - Arbres de résolution, ordre de sélection des clauses, format Prolog des clauses définies (clauses de Horn).
- **TD Thème 10 (p. 21-22 de `main_td-etudiants.pdf`) :**
  - **Exercice 35 :** Règle de résolution propositionnelle, factorisation et simplification.
  - **Exercice 36 :** Preuve par réfutation dans le cas propositionnel : modélisation d'un système de diagnostic médical.
  - **Exercice 37 :** Application de l'algorithme d'unification sur des paires d'atomes complexes, détection des échecs avec *occurs-check*.
  - **Exercice 38 :** Preuve par résolution au premier ordre avec unificateurs explicites menant à la clause vide $\Box$.
  - **Exercice 39 :** Construction de l'arbre de résolution au format Prolog.
- **TP Thème 10 (p. 24-26 de `main_tp-etudiants.pdf`) :**
  - **Exercice 16 :** Premières requêtes Prolog (faits, prédicats, variables anonymes `_`).
  - **Exercice 17 :** Modélisation d'un arbre généalogique et relations de parenté (`pere`, `mere`, `frere`, `ancetre`).
  - **Exercice 18 :** Modélisation de graphes orientés et recherche de chemins finis et acycliques en Prolog.
- **Annales Liées :**
  - `examen1_2017_2018.pdf` Ex 2 (Unification, MGU et résolution).
  - `examen1_2020_2021.pdf` Ex 5 (Preuve par résolution au premier ordre).
  - `examen2_2021_2022-2.pdf` Ex 4 (Algorithme d'unification pas à pas).

---

### SEMAINE 11 — Programmation Logique Avancée (Prolog), Théorème de Herbrand & Formes Normales LPPO
- **Cours Associés :** `Logique_6ECTS_Cours11.pdf` (Herbrand et Formes normales, 38 p) et `Logique_cours 10_Prolog.pdf` (Partie 2 : Prolog et SLD, p. 36-66).
  - *Notions fondamentales :*
    - **Prolog avancé :** Résolution SLD (Sélection Linéaire sur clauses Définies), arbre SLD, stratégie de recherche (profondeur d'abord, retour arrière / backtracking), manipulation de listes `[Tete|Reste]`, récursion sur les listes.
    - **Formes normales LPPO :** Forme Normale Négative (FNN), Forme Prénexe (mise en tête de tous les quantificateurs $\mathcal{Q}_1 x_1 \dots \mathcal{Q}_n x_n \, M$), règles d'extrusion des quantificateurs, Skolémisation (élimination des $\exists$ via des constantes ou des fonctions de Skolem dépendant des $\forall$ englobants), équi-satisfiabilité ($F \approx_{\text{sat}} F^*$), forme clausale LPPO.
    - **Théorème de Herbrand :** Univers de Herbrand $H_\mathcal{L}$, base de Herbrand $B_\mathcal{L}$, structures de Herbrand, réduction de la satisfiabilité au premier ordre à la satisfiabilité propositionnelle sur les instances terrestres (*ground instances*).
- **TD Thème 11 (p. 23-24 de `main_td-etudiants.pdf`) :**
  - **Exercice 40 :** Listes en Prolog : unification de listes, implémentation et trace de prédicats (`element`, `concatene`, `inverse`).
  - **Exercice 41 :** Formes normales en LPPO : mise sous forme prénexe par renommage préalable, Skolémisation pas à pas en justifiant l'arité de chaque fonction de Skolem, et obtention de la forme clausale.
- **TP Thème 11 (p. 27-28 de `main_tp-etudiants.pdf`) :**
  - **Exercice 19 :** Tests d'unification en Prolog : observation du comportement du moteur vis-à-vis de l'occurs-check.
  - **Exercice 20 :** Manipulation avancée de listes (appartenance, concaténation, longueur, inversion récursive).
  - **Exercice 21 :** Listes de courses et menus : modélisation de règles de combinaison culinaire et résolution de requêtes.
- **Annales Liées :**
  - `examen1_2016_2017.pdf` Ex 5 (Univers de Herbrand et formes prénexes).
  - `examen1_2019_2020.pdf` Ex 5 (Skolémisation et forme clausale).
  - `examen2_2018_2019.pdf` Ex 5 (Arbre SLD et requêtes Prolog).
