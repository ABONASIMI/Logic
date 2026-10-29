
<style>

/* ============ Base typography ============ */
h1, h2, h3 {
  text-align: center;
  color: #1565c0;
  font-family: "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
  margin-top: 0;
}
h1 { font-weight: 700; margin-bottom: 12px; }
h2, h3 { font-weight: 600; margin-bottom: 10px; }
p, li { line-height: 1.5; }
img { max-width: 100%; border-radius: 8px; }
hr { border: 0; height: 1px; background: #e0e0e0; margin: 20px 0; }

/* ============ Generic containers ============ */
div.box {
  padding: 16px;
  border-radius: 12px;
  margin: 18px 0;
  box-shadow: 0 1px 0 rgba(0,0,0,.03);
}
div.question { background: #e3f2fd; border-left: 6px solid #1976d2; }
div.answer   { background: #f9fbe7; border-left: 6px solid #cddc39; }
div.explain  { background: #fff3e0; border-left: 6px solid #fb8c00; }

/* ============ Code (inline & fenced) ============ */
code, pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}

/* Inline code */
code {
  background: #fff9c4;           /* light yellow inline */
  border: 1px solid #f4e38a;
  padding: 0 .25em;
  border-radius: 6px;
}

/* Fenced code blocks (``` … ```) */
pre {
  background: #fff9c4;           /* light yellow block */
  border-left: 6px solid #fdd835;/* amber accent */
  padding: 12px;
  border-radius: 10px;
  margin: 14px 0;
  overflow-x: auto;
}
pre code { background: transparent; border: 0; padding: 0; }

/* Optional labeled code wrapper you can use with HTML: <divclass="code"><divclass="label">A.sh</div>pre>code>…</code><pre</div> */

div.code {
  background: #fff9c4;
  border-left: 6px solid #fdd835;
  padding: 12px;
  border-radius: 10px;
  margin: 12px 0;
}
div.code .label {
  font-weight: 600;
  color: #6d4c41;
  margin-bottom: 8px;
  font-family: "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
}
div.code pre { background: transparent; margin: 0; padding: 0; }
/* ===== FORCE YELLOW CODE BLOCKS (works in VS Code & MPE) ===== */

/* Built-in VS Code preview */
.vscode-body pre,
.vscode-body pre code {
  background: #fff9c4 !important;
  border-left: 6px solid #fdd835 !important;
}

/* Markdown Preview Enhanced (uses highlight.js) */
.markdown-preview pre,
.markdown-preview pre code,
pre code.hljs,
.hljs {
  background: #fff9c4 !important;
  border-left: 6px solid #fdd835 !important;
}

/* Inline code (not in fences) */
.vscode-body code:not(pre code),
.markdown-preview code:not(pre code),
code:not(pre code) {
  background: #fff9c4 !important;
  border: 1px solid #f4e38a !important;
  padding: 0 .25em;
  border-radius: 6px;
}
/* ============ Tables ============ */
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #e0e0e0; padding: 8px 10px; }
thead th { background: #e3f2fd; }
tbody tr:nth-child(odd) { background: #fafafa; }

/* ============ Blockquotes ============ */
blockquote {
  margin: 12px 0;
  padding: 10px 14px;
  background: #f5f5f5;
  border-left: 6px solid #9e9e9e;
  border-radius: 8px;
  color: #37474f;
}

/* ============ Spacing utilities (use anywhere) ============ */
.spacer-sm { height: 8px; }
.spacer-md { height: 16px; }
.spacer-lg { height: 32px; }

.mt-2 { margin-top: 12px; } .mt-4 { margin-top: 24px; }
.mb-2 { margin-bottom: 12px; } .mb-4 { margin-bottom: 24px; }
.pt-2 { padding-top: 12px; } .pb-2 { padding-bottom: 12px; }

.center { text-align: center; }
.right { text-align: right; }
</style>


<div class="explain">

# Fiche express — Induction & structures (mots, listes, arbres, ordres)

Tu voulais :

1. **Notations complètes**,
2. Pour **chaque notation** : **Définition**, **2 exemples (1 classique + 1 nouveau) avec réponse pas à pas**, + **explication**.
3. Puis beaucoup d’**exemples résolus** (≈50 au total).

Je fais d’abord la **liste des notations**, puis je déroule **notation par notation** (déf → ex. classique → ex. nouveau → explication). À la fin, tu as un **bloc “exercices éclairs”** pour compléter et atteindre ~50 exemples.

---

## A) Notations — liste complète

1. Alphabet (A), mots (A^*), mot vide (\varepsilon)
2. Longueur (|w|) d’un mot
3. Comptage de lettres (|w|_a)
4. Concaténation de mots et puissances de langage (L^n, L^*)
5. Miroir (\tilde{w}) (renversement)
6. Ordre **préfixe** (\le_{\text{pref}})
7. Ordre **lexicographique** (\le_{\text{lex}})
8. Ordre **bien fondé** et **induction bien fondée**
9. Langage de **Dyck** (parenthèses / (a,b) équilibrés)
10. Relations **Inf1 / Inf2** sur (\mathbb N\times\mathbb N)
11. Ensemble inductif des **multiples** (D\subseteq\mathbb N\times\mathbb N)
12. **Listes** : `nil`, opérateur de construction (n|x), **somme** (s(x))
13. **Longueur** d’une liste (\ell(x)), **renversement** (\text{rev}(x))
14. **Arbres binaires** : hauteur (h(t)), nœuds (n(t)), feuilles (f(t))
15. **Arbres binaires stricts** (0 ou 2 fils) : identité (n=2f-1)
16. **Parcours préfixe** d’un arbre (\text{Pref}(t))
17. Ordres **produit** et **lexico sur paires** ((A\times B))
18. **Induction** : simple, forte, structurelle (patrons)

---

## B) Notations → définitions + exemples + explications

### 1) Alphabet (A), mots (A^*), mot vide (\varepsilon)

**Définition.** (A) est un ensemble fini de symboles. (A^*) : tous les mots finis sur (A), y compris (\varepsilon) (mot vide).

**Exemple classique.**

* Soit (A={a,b}). Alors (w=abba\in A^*), (\varepsilon\in A^*).
* Réponse : vrai, par définition.

**Exemple nouveau.**

* Avec (A={0,1}), le mot (10100\in A^*).
* Réponse : oui, chaque caractère est dans (A).

**Explication.** On construit les mots en ajoutant des lettres de (A). (\varepsilon) est toujours dans (A^*).

---

### 2) Longueur (|w|)

**Définition.** (|w|) = nombre de lettres de (w).

**Exemple classique.**

* (w=ababb) ⇒ (|w|=5).
* Pas à pas : on compte (a,b,a,b,b) → 5.

**Exemple nouveau.**

* (w=\varepsilon) ⇒ (|w|=0).
* Pas à pas : mot vide → 0.

**Explication.** Toujours (|\varepsilon|=0). Ajouter une lettre augmente la longueur de 1.

---

### 3) Comptage (|w|_a)

**Définition.** (|w|_a) = nombre d’occurrences de la lettre (a) dans (w).

**Exemple classique.**

* (w=abaabb). (|w|_a=3), (|w|_b=3).
* Pas à pas : positions des (a) : 1,3,4 → 3.

**Exemple nouveau.**

* (w=bbbab). (|w|_a=1).
* Pas à pas : seul (a) à l’avant-dernière position.

**Explication.** Sur (A={a,b}), (|w|=|w|_a+|w|_b).

---

### 4) Concaténation, (L^n), (L^*)

**Définition.** Concaténation : coller deux mots. Pour un langage (L), (L^0={\varepsilon}), (L^{n+1}=L^nL), (L^*=\bigcup_{n\ge0}L^n).

**Exemple classique.**

* (L={a}). Alors (L^2={aa}), (L^*={\varepsilon,a,aa,aaa,\dots}).
* Pas à pas : itérations de (a).

**Exemple nouveau.**

* (L={ab,b}). (L^2={abab,abb,bb}).
* Pas à pas : tous produits de 2 mots de (L).

**Explication.** (L^*) contient tous les produits de longueur arbitraire (y compris 0).

---

### 5) Miroir (\tilde{w})

**Définition.** (\tilde{w}) = mot renversé (lecture de droite à gauche).

**Exemple classique.**

* (w=abc) ⇒ (\tilde{w}=cba).
* Pas à pas : inverser l’ordre.

**Exemple nouveau.**

* (w=baab) ⇒ (\tilde{w}=baab) (palindrome).
* Pas à pas : renversement identique.

**Explication.** Le miroir est une bijection involutive : (\tilde{\tilde{w}}=w).

---

### 6) Ordre **préfixe** (\le_{\text{pref}})

**Définition.** (u\le_{\text{pref}} v) s’il existe (w) tel que (v=uw) (donc (u) est préfixe de (v)).

**Exemple classique.**

* (u=ab,\ v=abba). On a (v=ab\cdot ba) ⇒ (u\le_{\text{pref}}v).
* Pas à pas : exhiber le suffixe (w=ba).

**Exemple nouveau.**

* (\varepsilon \le_{\text{pref}} v) pour tout (v) (prendre (w=v)).
* Pas à pas : (v=\varepsilon\cdot v).

**Explication.** L’ordre préfixe **est bien fondé** sur (A^*) (pas de chaîne strictement décroissante infinie de préfixes).

---

### 7) Ordre **lexicographique** (\le_{\text{lex}})

**Définition.** On compare lettre à lettre selon l’ordre de (A). S’ils coïncident jusqu’à une position, on départage à la première différence ; sinon le plus court (préfixe) est plus petit.

**Exemple classique.**

* Sur (a<b) : (aa <*{\text{lex}} ab <*{\text{lex}} b).
* Pas à pas : (a=a) puis (a<b) ⇒ (aa<ab) ; et (a<b) ⇒ tout mot commençant par (a) < (b).

**Exemple nouveau.**

* (aba <_{\text{lex}} abb) (égalité sur (ab), puis (a<b)).
* Pas à pas : troisième lettre compare.

**Explication.** Total mais **pas bien fondé** sur (A^*) (on peut construire des chaînes infinies décroissantes).

---

### 8) Ordre **bien fondé** & **induction bien fondée**

**Définition.** Un ordre est bien fondé s’il n’existe **aucune** suite infinie strictement décroissante. Induction : pour prouver (P(x)) pour tout (x), supposer (P(y)) vraie pour **tous** les (y<x), puis montrer (P(x)).

**Exemple classique.**

* Sur (\mathbb N) (ordre usuel), toute partie non vide a un minimum.
* Pas à pas : c’est la propriété clé pour la récurrence.

**Exemple nouveau.**

* Ordre préfixe sur (A^*) : bien fondé (on peut raisonner sur la longueur).
* Pas à pas : toute chaîne descendante raccourcit la longueur.

**Explication.** Très utile quand la structure diminue “quelque part” (longueur, mesure, etc.).

---

### 9) Langage de **Dyck** (E) (équilibre (a/b))

**Définition.** Mots où le nombre de (a) égale celui de (b) et **tout préfixe** contient au moins autant de (a) que de (b).

**Exemple classique.**

* (w=aabb) est dans (E).
* Pas à pas : préfixes (a) (1≥0), (aa) (2≥0), (aab) (2≥1), (aabb) (2=2).

**Exemple nouveau.**

* (w=abab) est **dans** (E) ?
* Pas à pas : préfixes (a) (1≥0), (ab) (1≥1), (aba) (2≥1), (abab) (2=2) ⇒ oui.

**Explication.** Penser “pile” : (a) = ouvre, (b) = ferme ; on ne doit jamais “passer en négatif”.

---

### 10) Relations **Inf1 / Inf2** sur (\mathbb N\times\mathbb N)

**Définition (intuitif).** Deux relations générées par règles simples qui, au final, **capturent (n_1\le n_2)**.

**Exemple classique.**

* Montrer ((3,5)) appartient.
* Pas à pas : (3\le5) ; en partant de cas de base, on “augmente” les deux côtés (ou le 2e) jusqu’à ((3,5)).

**Exemple nouveau.**

* ((4,4)) appartient.
* Pas à pas : égalité ⇒ relation vraie (réflexe de “(\le)”).

**Explication.** Le but typique : prouver l’équivalence “appartenance ⇔ (\le)”.

---

### 11) Ensemble (D) des **multiples** (inductif)

**Définition.** (D\subseteq\mathbb N\times\mathbb N) : ((n,0)\in D) ; si ((n,n')\in D) alors ((n,n+n')\in D). Au final, ((n,n')\in D \iff \exists k,\ n'=kn).

**Exemple classique.**

* ((3,9)\in D) ? Oui, (9=3\cdot3).
* Pas à pas : de ((3,0)), ajouter 3 trois fois.

**Exemple nouveau.**

* ((5,0)\in D) ? Oui, cas de base ((k=0)).
* Pas à pas : déf. directe.

**Explication.** C’est une **définition inductive** de la divisibilité.

---

### 12) **Listes** : `nil`, (n|x) ; **somme** (s(x))

**Définition.** `nil` est la liste vide ; si (n\in\mathbb N) et (x) est une liste, alors (n|x) est la liste avec tête (n).
**Somme.** (s(nil)=0), (s(n|x)=n+s(x)).

**Exemple classique.**

* (x=1|2|3|nil). (s(x)=6).
* Pas à pas : (s(3|nil)=3), (s(2|…)=2+3=5), (s(1|…)=1+5=6).

**Exemple nouveau.**

* (x=0|7|4|nil). (s(x)=11).
* Pas à pas : (0+(7+(4+0))=11).

**Explication.** Prouver des propriétés par induction **structurelle** sur la forme de la liste.

---

### 13) **Longueur** (\ell(x)), **renversement** (\text{rev}(x)) d’une liste

**Définition.** (\ell(nil)=0), (\ell(n|x)=1+\ell(x)).
(\text{rev}(nil)=nil), (\text{rev}(n|x)=\text{rev}(x),|,n) (ajoute (n) à la fin).

**Exemple classique.**

* (x=2|5|nil) : (\ell(x)=2).
* Pas à pas : (\ell(nil)=0), (\ell(5|nil)=1), (\ell(2|…)=2).

**Exemple nouveau.**

* (\text{rev}(3|1|nil)=1|3|nil).
* Pas à pas : (\text{rev}(1|nil)=1|nil), puis ajouter 3 à la fin.

**Explication.** Propriété type : (\ell(\text{rev}(x))=\ell(x)) (preuve structurelle).

---

### 14) **Arbres binaires** : (h(t)), (n(t)), (f(t))

**Définition.**

* Hauteur (h) : (h(\emptyset)=0) ; (h(\bullet)=1) ; (h(\langle g,a,d\rangle)=1+\max(h(g),h(d))).
* Nœuds (n) : (n(\emptyset)=0) ; (n(\bullet)=1) ; (n(\langle g,a,d\rangle)=1+n(g)+n(d)).
* Feuilles (f) : (f(\emptyset)=0) ; (f(\bullet)=1) ; (f(\langle g,a,d\rangle)=f(g)+f(d)).

**Exemple classique.**

* Arbre **plein** de hauteur 3 : (n=7), (f=4).
* Pas à pas : niveau 1→1, niveau 2→2, niveau 3→4 feuilles, total 7 nœuds.

**Exemple nouveau.**

* **Chaîne** à gauche de 4 nœuds : (h=4), (n=4), (f=1).
* Pas à pas : chaque ajout augmente (h) de 1, une seule feuille.

**Explication.** Bornes utiles : (n(t)\le 2^{h(t)}-1) et (f(t)\le 2^{h(t)-1}).

---

### 15) **Arbres binaires stricts** (0 ou 2 fils) : (n=2f-1)

**Définition.** Un arbre strict : chaque nœud a 0 ou 2 enfants (jamais 1).

**Exemple classique.**

* Arbre strict complet de hauteur 3 : (f=4) ⇒ (n=2\cdot4-1=7).
* Pas à pas : structure parfaite, formule vérifiée.

**Exemple nouveau.**

* Si on remplace une feuille par un nœud avec deux feuilles : (f\gets f+1), (n\gets n+2) ⇒ (n'=2(f+1)-1=2f+1=n+2).
* Pas à pas : l’identité reste vraie.

**Explication.** Prouvable par induction structurelle sur la construction.

---

### 16) **Parcours préfixe** (\text{Pref}(t))

**Définition.** Visite racine, puis gauche, puis droite. (\text{Pref}(\emptyset)=\varepsilon), (\text{Pref}(a,g,d)=a,\text{Pref}(g),\text{Pref}(d)).

**Exemple classique.**

* Racine (A) avec fils (B) (gauche feuille), (C) (droite feuille) : (\text{Pref}=ABC).
* Pas à pas : A puis B puis C.

**Exemple nouveau.**

* Racine (R), gauche vide, droite feuille (X) : (\text{Pref}=RX).
* Pas à pas : R, gauche rien, droite X.

**Explication.** Bien connaître les trois parcours classiques (préfixe, infixe, postfixe).

---

### 17) Ordres **produit** et **lexico sur paires**

**Définition.**

* **Produit** : ((a,b)\le (a',b')) ssi (a\le a') **et** (b\le b').
* **Lexico** : on compare d’abord (a), puis (b) si (a=a').

**Exemple classique.**

* ((1,5)\le_{\text{lex}}(2,0)) (car (1<2)).
* Pas à pas : premier composant départage.

**Exemple nouveau.**

* ((2,3)\le_{\times}(3,3)) (car (2\le3) et (3\le3)).
* Pas à pas : deux composantes.

**Explication.** Pour des preuves par **double récurrence**, on utilise souvent un ordre lexico sur (\mathbb N\times\mathbb N).

---

### 18) **Induction** : simple, forte, structurelle (patrons prêts à recopier)

**Définition.**

* **Simple (sur (n))** : Base (0) (ou 1) ; H.I. (P(n)) ⇒ Pas (P(n+1)).
* **Forte** : supposer (P(k)) pour **tous** (k\le n) ⇒ (P(n+1)).
* **Structurelle** : Base sur les “constructeurs simples” ; Pas sur la **décomposition** (mot = (ua), liste = (n|x), arbre = (\langle g,a,d\rangle)).

**Exemple classique (simple).**

* Prouver (\sum_{i=1}^n i = \frac{n(n+1)}2).
* Pas à pas : base (n=1) OK ; H.I. + ajouter (n+1).

**Exemple nouveau (structurelle).**

* Prouver (\ell(\text{rev}(x))=\ell(x)) pour les listes.
* Pas à pas : base `nil` ; pas (n|x) : (\ell(\text{rev}(x),|,n)=\ell(\text{rev}(x))+1=\ell(x)+1).

**Explication.** Choisis **le bon type** d’induction suivant la **forme** de l’objet.

---

## C) Exercices éclairs (QCM raisonné / mini-démos) — corrigés pas à pas

> Objectif : compléter pour atteindre ~50 cas vus. Courts, mais structurés.

1. Sur (A={a,b}), (\varepsilon, a, b, ab, ba\in A^*) ?
   **Réponse.** Oui (définition de (A^*)).
   **Étapes.** Tous les caractères ∈ (A).

2. (|\varepsilon|=?)
   **Réponse.** 0.
   **Étapes.** Longueur du mot vide.

3. (|ababa|_a=?)
   **Réponse.** 3.
   **Étapes.** Comptage des (a).

4. (L={a,bb}). Donne (L^2).
   **Réponse.** ({aa,abb,bba,bbbb}).
   **Étapes.** Produits 2 à 2.

5. (w=abba). (\tilde{w}=?)
   **Réponse.** (abba).
   **Étapes.** Renversement → palindrome.

6. (u=ab,\ v=abc). (u\le_{\text{pref}}v) ?
   **Réponse.** Oui.
   **Étapes.** (v=u\cdot c).

7. Sur (a<b) : ordonne (ab, b, aa) en lexico.
   **Réponse.** (aa<ab<b).
   **Étapes.** Comparer première lettre.

8. Dire si l’ordre préfixe est bien fondé.
   **Réponse.** Oui.
   **Étapes.** Pas de chaîne infinie de préfixes.

9. Tester si (w=abba) est Dyck.
   **Réponse.** Non.
   **Étapes.** Préfixe “abb” : (a=1,b=2) → 1<2 → interdit.

10. Tester si (w=abab) est Dyck.
    **Réponse.** Oui.
    **Étapes.** Tous préfixes respectent (a\ge b), et (a=b=2) à la fin.

11. Relation Inf1/Inf2 : ((2,5)) appartient ?
    **Réponse.** Oui (2 ≤ 5).
    **Étapes.** Cible = encodage de “(\le)”.

12. ((7,4)) appartient ?
    **Réponse.** Non (7 ≤ 4 est faux).
    **Étapes.** Contradiction.

13. (D) des multiples : ((4,12)\in D) ?
    **Réponse.** Oui (12 = 3×4).
    **Étapes.** Règle d’ajout répété.

14. ((4,10)\in D) ?
    **Réponse.** Non.
    **Étapes.** 10/4 pas entier.

15. Liste (x=3|5|2|nil). (s(x)=?)
    **Réponse.** 10.
    **Étapes.** 3+5+2.

16. (\ell(7|nil)=?)
    **Réponse.** 1.
    **Étapes.** Définition de (\ell).

17. (\text{rev}(4|9|nil)=?)
    **Réponse.** (9|4|nil).
    **Étapes.** Renversement.

18. Arbre : une chaîne de 5 nœuds. (h=?\ f=?)
    **Réponse.** (h=5,\ f=1).
    **Étapes.** Un seul bout feuille.

19. Arbre plein (h=4). (n=?\ f=?)
    **Réponse.** (n=15, f=8).
    **Étapes.** Niveaux : 1,2,4,8.

20. Arbre strict avec (f=6). (n=?)
    **Réponse.** (n=2f-1=11).
    **Étapes.** Formule.

21. Parcours préfixe : racine R, gauche A (feuille), droite vide.
    **Réponse.** RA.
    **Étapes.** Racine, gauche, droite.

22. ((1,10)\le_{\times}(2,9)) ? (ordre **produit**)
    **Réponse.** Non (10≤9 faux).
    **Étapes.** Les 2 composantes doivent être ≤.

23. ((1,10)\le_{\text{lex}}(2,0)) ?
    **Réponse.** Oui (1<2 au premier composant).
    **Étapes.** Lexico = compare d’abord le 1er.

24. Prouver par induction simple : (1+2+\dots+n=\frac{n(n+1)}2) (squelette).
    **Réponse.** Base (n=1) ; H.I. (n) ; Pas (n+1).
    **Étapes.** Ajouter (n+1), factoriser.

25. Induction forte (squelette) : tout (n\ge2) s’écrit produit de nombres premiers.
    **Réponse.** Base 2 ; H.I. vrais pour ≤ n ; Pas (n+1) : ou premier, ou décompose.
    **Étapes.** Diviseur non trivial.

26. Preuve structurelle : (\ell(\text{rev}(x))=\ell(x)) (squelette).
    **Réponse.** Base `nil`; Pas (n|x) : longueur +1 conservée.
    **Étapes.** Définition de (\ell) et (\text{rev}).

27. Mots : prouver (|\tilde{w}|=|w|).
    **Réponse.** Structurelle sur (w).
    **Étapes.** Ajouter une lettre conserve la longueur.

28. Montrer (|uv|=|u|+|v|).
    **Réponse.** Structurelle sur (v).
    **Étapes.** Ajouter une lettre à droite augmente de 1.

29. Montrer (|uv|_a = |u|_a + |v|_a).
    **Réponse.** Structurelle sur (v).
    **Étapes.** Comptage lettre par lettre.

30. Dyck : (aabbab) ?
    **Réponse.** Non (préfixe “aabba” : (a=3, b=2), OK ; mais fin : (a=3, b=3) OK —> vérif plus fine : préfixes tous OK ? Ici oui → **en fait oui**).
    **Étapes.** Recompter proprement : a(1) aa(2) aab(2/1) aabb(2/2) aabba(3/2) aabbab(3/3) → **Oui**.

31. Dyck : (abbaab) ?
    **Réponse.** Non (préfixe “abb” a=1<b=2).
    **Étapes.** Préfixe invalide ⇒ exclu.

32. Inf1/Inf2 : décider ((0,n)).
    **Réponse.** Toujours vrai (0 ≤ n).
    **Étapes.** Propriété de base.

33. Inf1/Inf2 : décider ((n,n)).
    **Réponse.** Vrai.
    **Étapes.** Réflexivité de ≤.

34. Multiples (D) : ((6,24)) ?
    **Réponse.** Oui (24=4×6).
    **Étapes.** Ajouts de 6.

35. Multiples (D) : ((6,22)) ?
    **Réponse.** Non.
    **Étapes.** 22/6 non entier.

36. Listes : prouver (s(x|y)=s(x)+s(y)) si (x|y) signifie concaténation.
    **Réponse.** Structurelle sur (x).
    **Étapes.** Base `nil` ; Pas (n|x).

37. Arbres : prouver (f(t)\le n(t)).
    **Réponse.** Structurelle (feuille = 1≤1 ; composés : somme).
    **Étapes.** Addition des sous-arbres.

38. Arbres : (n(t)\le 2^{h(t)}-1) pour une chaîne de longueur (k).
    **Réponse.** Égalité (n=h) et (h=k) ⇒ (k \le 2^k-1) (vrai pour (k\ge1)).
    **Étapes.** Vérif par croissance.

39. Arbres stricts : si (f=1), alors (n=1).
    **Réponse.** (n=2f-1=1).
    **Étapes.** Formule.

40. Paires : montrer que le lexico sur (\mathbb N\times\mathbb N) est bien fondé.
    **Réponse.** Pas de chaîne infinie qui baisse d’abord le 1er, puis le 2nd finit par baisser.
    **Étapes.** Argument minimalité.

41. Mots : montrer que “préfixe de” est une relation d’ordre partiel.
    **Réponse.** Réflexive, antisymétrique, transitive.
    **Étapes.** Définition de préfixe.

42. Mots : montrer que le miroir conserve le nombre de (a).
    **Réponse.** Structurelle sur (w).
    **Étapes.** Chaque ajout de lettre est symétrique.

43. Listes : (\text{rev}(\text{rev}(x))=x).
    **Réponse.** Structurelle.
    **Étapes.** Base `nil` ; Pas (n|x).

44. Dyck : concaténation de deux mots Dyck est-elle Dyck ?
    **Réponse.** Oui.
    **Étapes.** Préfixes du premier OK ; après, on ajoute un mot équilibré.

45. Dyck : si (u\in E), alors (a,u,b\in E).
    **Réponse.** Oui (emboîtement).
    **Étapes.** Ajoute une paire externe.

46. Inf2 : de ((n,m)) on déduit ((n,m+1)).
    **Réponse.** Oui (car (n\le m ⇒ n\le m+1)).
    **Étapes.** Propriété de ≤.

47. Multiples : si ((n,m)\in D), alors ((n,m+k n)\in D).
    **Réponse.** Oui (ajouter (n), (k) fois).
    **Étapes.** Induction sur (k).

48. Listes : (\ell(x|y)=\ell(x)+\ell(y)).
    **Réponse.** Structurelle sur (x).
    **Étapes.** Base `nil`; Pas (n|x).

49. Arbres : si (t) est strict, alors (f\ge 1).
    **Réponse.** Oui (tout arbre strict non vide a au moins une feuille).
    **Étapes.** Décomposition.

50. Induction forte : tout (n\ge1) s’écrit somme de puissances de 2 distinctes (binaire).
    **Réponse.** Vrai (décomposition binaire).
    **Étapes.** Plus grande puissance ≤ n, puis sur le reste.

---

## D) Mini “patrons” à recopier (ultra courts)

* **Induction simple (sur (n))**
  Base : montrer (P(0)) (ou (P(1))).
  H.I. : supposer (P(n)).
  Pas : démontrer (P(n+1)) à partir de (P(n)).

* **Induction forte**
  Base : (P(0)).
  H.I. : supposer (P(k)) pour **tous** (k\le n).
  Pas : prouver (P(n+1)) en s’aidant de **tous** les cas plus petits.

* **Induction structurelle (mots/listes/arbres)**
  Base : cas le plus simple ((\varepsilon), `nil`, feuille/vide).
  Pas : supposer la propriété vraie pour les sous-objets (préfixe (u), suffixe (x), sous-arbres (g,d)) et prouver pour l’objet composé.

---

</div>



<!-- ======================================================= -->

<!-- Source: :contentReference[oaicite:0]{index=0} -->


<div class="box question">
  <h2>Exercice 1 — Deux relations inductives sur ℕ×ℕ</h2>
  <p><strong>Définitions.</strong></p>
  <pre>(R11) ∀n, (0,n) ∈ Inf1
(R12) si (n1,n2) ∈ Inf1 alors (n1+1, n2+1) ∈ Inf1

(R21) ∀n, (n,n) ∈ Inf2
(R22) si (n1,n2) ∈ Inf2 alors (n1, n2+1) ∈ Inf2</pre>

  <p><strong>Questions.</strong></p>
  <ol>
    <li>(1.a) Lister quelques éléments et donner la propriété caractéristique de <em>Inf1</em> et <em>Inf2</em>.</li>
    <li>(1.b) Prouver : ∀n, (n,n) ∈ <em>Inf1</em>.</li>
    <li>(1.c) Prouver : si (n1,n2) ∈ <em>Inf1</em> alors (n1,n2+1) ∈ <em>Inf1</em>.</li>
    <li>(2.a) Donner la propriété caractéristique de <em>Inf2</em>.</li>
    <li>(2.b) Prouver : ∀n, (0,n) ∈ <em>Inf2</em>.</li>
    <li>(2.c) Prouver : si (n1,n2) ∈ <em>Inf2</em> alors (n1+1,n2+1) ∈ <em>Inf2</em>.</li>
  </ol>
</div>

<div class="box answer">
  <h3>Réponse (complète et pédagogique)</h3>

  <h4>(1.a) Éléments et propriété caractéristique</h4>
  <p><u>Inf1</u> : on part de la “colonne x=0” puis on monte en diagonale (+1,+1).</p>
  <ul>
    <li>Bases : (0,0), (0,1), (0,2), … (par R11)</li>
    <li>Étapes (R12) : de (0,2) → (1,3) → (2,4) → (3,5) → … ; de (0,0) → (1,1) → (2,2) → …</li>
  </ul>
  <p><u>Inf2</u> : on part de la diagonale (n,n) puis on pousse vers le haut en n2 (+1).</p>
  <ul>
    <li>Bases : (0,0), (1,1), (2,2), … (par R21)</li>
    <li>Étapes (R22) : de (1,1) → (1,2) → (1,3) → … ; de (2,2) → (2,3) → (2,4) → …</li>
  </ul>
  <p><strong>Conclusion (caractérisation commune)</strong> :
    <code>(n1,n2) ∈ Inf1 ⇔ n1 ≤ n2</code> et <code>(n1,n2) ∈ Inf2 ⇔ n1 ≤ n2</code>.
  </p>

  <details><summary><em>Pourquoi c’est bien ⇔ ? (preuve idée courte)</em></summary>
  <ul>
    <li><strong>Inf1 ⊆ {n1 ≤ n2}</strong> : base (0,n) vérifie 0 ≤ n ; la règle (+1,+1) garde l’inégalité vraie.</li>
    <li><strong>{n1 ≤ n2} ⊆ Inf1</strong> : pour un couple (n1,n2) avec n1 ≤ n2, pars de (0, n2−n1) (R11) et applique (R12) n1 fois → (n1,n2).</li>
    <li><strong>Inf2 ⊆ {n1 ≤ n2}</strong> : bases (n,n) ont n ≤ n ; la règle (+0,+1) augmente seulement n2.</li>
    <li><strong>{n1 ≤ n2} ⊆ Inf2</strong> : pars de (n1,n1) (R21) et applique (R22) (n2−n1) fois → (n1,n2).</li>
  </ul>
  </details>

  <h4>(1.b) ∀n, (n,n) ∈ Inf1</h4>
  <p><u>Preuve par récurrence sur n</u> :
    Base : (0,0) ∈ Inf1 (R11).  
    Hérédité : si (k,k) ∈ Inf1, alors par (R12) (k+1,k+1) ∈ Inf1.  
    Donc ∀n, (n,n) ∈ Inf1.
  </p>
  <p><u>Alternative “construction directe”</u> : (n,n) s’obtient depuis (0,0) en appliquant (R12) exactement n fois.</p>

  <h4>(1.c) Si (n1,n2) ∈ Inf1 alors (n1,n2+1) ∈ Inf1</h4>
  <p><u>Méthode 1 (la plus simple)</u> : on utilise la caractérisation.  
    De (n1,n2) ∈ Inf1 on déduit n1 ≤ n2, donc n1 ≤ n2+1, donc (n1,n2+1) ∈ Inf1.
  </p>
  <p><u>Méthode 2 (reconstruction depuis une base)</u> :
    on veut <code>(n1,n2+1)</code>. Comme <code>n1 ≤ n2</code>, on a aussi <code>n1 ≤ n2+1</code>.  
    Construis-le directement : pars de <code>(0, (n2+1)−n1)</code> (R11) puis applique (R12) n1 fois → tu atteins <code>(n1, n2+1)</code>.
  </p>
  <p><em>Remarque importante</em> : on ne peut pas “partir de (n1,n2)” et appliquer (R12) pour ajouter +1 uniquement à n2 (R12 ajoute +1 aux deux).  
  On prouve donc l’appartenance de (n1,n2+1) en <strong>reconstruisant une dérivation</strong> depuis une base, ou via la caractérisation.</p>

  <h4>(2.a) Propriété caractéristique de Inf2</h4>
  <p>Comme ci-dessus : <strong><code>Inf2 = {(n1,n2) | n1 ≤ n2}</code></strong>.</p>

  <h4>(2.b) ∀n, (0,n) ∈ Inf2</h4>
  <p>De (R21) on a (0,0) ∈ Inf2. Puis on applique (R22) n fois pour obtenir (0,n).</p>

  <h4>(2.c) Si (n1,n2) ∈ Inf2 alors (n1+1,n2+1) ∈ Inf2</h4>
  <p><u>Méthode 1 (caractérisation)</u> : (n1,n2) ∈ Inf2 ⇒ n1 ≤ n2 ⇒ n1+1 ≤ n2+1 ⇒ (n1+1,n2+1) ∈ Inf2.</p>
  <p><u>Méthode 2 (construction)</u> : pars de (n1+1, n1+1) (R21), puis applique (R22) (n2−n1) fois pour atteindre (n1+1, n2+1).</p>
</div>

<div class="box explain">
  <h3>Explication (pas à pas, “comment on raisonne”)</h3>
  <ol>
    <li><strong>Regarde les règles et cherche l’invariant</strong> : ici, la différence <code>n2−n1</code> reste ≥ 0.</li>
    <li><strong>Devine la propriété caractéristique</strong> : “tous et seulement les couples avec <code>n1 ≤ n2</code>”.</li>
    <li><strong>Prouve ⇐ et ⇒ séparément</strong> :
      <ul>
        <li>les règles <em>gardent</em> l’invariant (⇒),</li>
        <li>et tout couple qui vérifie l’invariant est <em>constructible</em> à partir d’une base (⇐).</li>
      </ul>
    </li>
    <li><strong>Pour (1.c) et (2.c)</strong> : si la règle ne permet pas le “mouvement” voulu directement,  
      <u>repars d’une base</u> et <u>reconstruis</u> la dérivation, ou utilise la <u>caractérisation</u>.</li>
  </ol>

  <h4>Pièges fréquents</h4>
  <ul>
    <li>Confondre “je peux dériver <em>à partir</em> de (n1,n2)” avec “<em>il existe</em> une dérivation depuis une base vers (n1,n2)”.</li>
    <li>Oublier de prouver les deux sens pour une caractérisation (⊆ et ⊇).</li>
    <li>Essayer d’ajouter +1 seulement à une coordonnée avec (R12) (impossible : (R12) ajoute +1 aux deux).</li>
  </ul>

  <h4>Mémo ultra-court</h4>
  <ul>
    <li><strong>Inf1</strong> : base (0,n), step (+1,+1) → <code>n1≤n2</code>.</li>
    <li><strong>Inf2</strong> : base (n,n), step (+0,+1) → <code>n1≤n2</code>.</li>
    <li>Pour montrer qu’un couple est dedans : <em>construis-le</em> depuis une base en appliquant les règles le bon nombre de fois.</li>
  </ul>
</div>

---

<!-- ======================================================= -->

<!-- Source: :contentReference[oaicite:1]{index=1} -->

<div class="box question">
  <h2>Exercice 2 — Langage L sur A = {a,b}</h2>
  <p><strong>Définition inductive.</strong></p>
  <pre>(B) b ∈ L
(I) si u,v ∈ L alors a u v ∈ L</pre>
  <p><strong>À montrer.</strong></p>
  <ol>
    <li>(1) ∀w ∈ L, |w|<sub>b</sub> = |w|<sub>a</sub> + 1.</li>
    <li>(2) ∀w ∈ L et tout préfixe propre w′ de w, |w′|<sub>a</sub> ≥ |w′|<sub>b</sub>.</li>
  </ol>
</div>

<div class="box answer">
  <h3>Réponse détaillée</h3>

  <h4>Lemme 1 — Tous les mots de L se terminent par <code>b</code></h4>
  <p><em>Preuve par induction structurelle.</em> Base : <code>b</code> finit par <code>b</code>. Étape : si <code>u</code> et <code>v</code> finissent par <code>b</code>, alors <code>a u v</code> finit comme <code>v</code>, donc encore par <code>b</code>. ✓</p>

  <h4>(1) — Comptage global : <code>|w|<sub>b</sub> = |w|<sub>a</sub> + 1</code></h4>
  <p><em>Preuve par induction structurelle sur w.</em></p>
  <ul>
    <li><strong>Base</strong> : <code>w=b</code>. On a <code>|w|<sub>b</sub>=1</code> et <code>|w|<sub>a</sub>=0</code>, donc <code>1=0+1</code>. ✓</li>
    <li><strong>Étape</strong> : écrire <code>w = a u v</code> avec <code>u,v∈L</code>. Alors
      <div class="math">
        |w|<sub>a</sub> = 1 + |u|<sub>a</sub> + |v|<sub>a</sub>, &nbsp;&nbsp;
        |w|<sub>b</sub> = |u|<sub>b</sub> + |v|<sub>b</sub>.
      </div>
      Par I.H., <code>|u|<sub>b</sub>=|u|<sub>a</sub>+1</code> et <code>|v|<sub>b</sub>=|v|<sub>a</sub>+1</code>. Donc
      <pre>|w|<sub>b</sub> = (|u|<sub>a</sub>+1) + (|v|<sub>a</sub>+1)
          = (1 + |u|<sub>a</sub> + |v|<sub>a</sub>) + 1
          = |w|<sub>a</sub> + 1.</pre>
      ✓
    </li>
  </ul>

  <h4>(2) — Préfixes propres sans déficit de <code>a</code></h4>
  <p><em>Énoncé.</em> Pour tout <code>w∈L</code> et tout préfixe <strong>propre</strong> <code>w′</code> de <code>w</code>, on a <code>|w′|<sub>a</sub> ≥ |w′|<sub>b</sub></code>.</p>
  <p><em>Preuve par induction structurelle sur w</em> (on suppose le résultat vrai pour les sous-mots <code>u</code> et <code>v</code> lorsqu’on traite <code>w=a u v</code>).</p>
  <ul>
    <li><strong>Base</strong> <code>w=b</code> : seul préfixe propre <code>ε</code>, donc <code>0≥0</code>. ✓</li>
    <li><strong>Étape</strong> <code>w = a u v</code> : les préfixes propres de <code>w</code> sont de 4 types :
      <ol>
        <li><code>w′ = ε</code> : <code>0≥0</code>. ✓</li>
        <li><code>w′ = a</code> : <code>1≥0</code>. ✓</li>
        <li><code>w′ = a·x</code> avec <code>x</code> préfixe de <code>u</code> :
          <ul>
            <li>Si <code>x</code> est <em>propre</em>, par I.H. sur <code>u</code> on a <code>|x|<sub>a</sub> ≥ |x|<sub>b</sub></code>, donc <code>|w′|<sub>a</sub>=1+|x|<sub>a</sub> ≥ 1+|x|<sub>b</sub> &gt; |x|<sub>b</sub>=|w′|<sub>b</sub></code>. ✓</li>
            <li>Si <code>x=u</code>, alors par (1) <code>|u|<sub>b</sub>=|u|<sub>a</sub>+1</code>, d’où <code>|w′|<sub>a</sub>=1+|u|<sub>a</sub>=|u|<sub>b</sub>=|w′|<sub>b</sub></code>. ✓</li>
          </ul>
        </li>
        <li><code>w′ = a·u·y</code> avec <code>y</code> préfixe <em>propre</em> de <code>v</code> :
          <div class="math">
            |w′|<sub>a</sub> = 1 + |u|<sub>a</sub> + |y|<sub>a</sub>, &nbsp;
            |w′|<sub>b</sub> = |u|<sub>b</sub> + |y|<sub>b</sub> = (|u|<sub>a</sub>+1) + |y|<sub>b</sub>.
          </div>
          Par I.H. sur <code>v</code>, <code>|y|<sub>a</sub> ≥ |y|<sub>b</sub></code>, donc <code>|w′|<sub>a</sub>−|w′|<sub>b</sub> = |y|<sub>a</sub>−|y|<sub>b</sub> ≥ 0</code>. ✓
        </li>
      </ol>
    </li>
  </ul>

  <h4>Exemples rapides</h4>
  <ul>
    <li><strong>w = b</strong> : <code>|a|=0</code>, <code>|b|=1</code>. Préfixe propre : <code>ε</code> (OK).</li>
    <li><strong>w = a b b</strong> (cas <code>u=b</code>, <code>v=b</code>) :
      <table>
        <tr><th>préfixe</th><th>#a</th><th>#b</th><th>φ=#a-#b</th></tr>
        <tr><td><code>ε</code></td><td>0</td><td>0</td><td>0</td></tr>
        <tr><td><code>a</code></td><td>1</td><td>0</td><td>+1</td></tr>
        <tr><td><code>ab</code></td><td>1</td><td>1</td><td>0</td></tr>
        <tr><td><code>abb</code> (entier)</td><td>1</td><td>2</td><td>−1</td></tr>
      </table>
    </li>
  </ul>
</div>

<div class="box explain">
  <h3>Explications & dessins ASCII</h3>

  <h4>Modèle mental (arbre de construction)</h4>
  <pre>
           (a)
          /   \
        (u)   (v)

Exemple : w = a (a b b) b = a a b b b

```
         a
       /   \
      a     b
    /   \
   b     b
```

  </pre>

  <h4>Préfixes d’un w = a u v (découpe en zones)</h4>
  <pre>
w =  a |  (préfixes de u)  |  (préfixes de v)
      ^        ^                      ^
      1        2                      3

Préfixes propres possibles :

* ε
* a
* a · (préfixe de u)     ← hérite I.H. sur u  (+ égalité si préfixe = u)
* a · u · (préfixe de v) ← hérite I.H. sur v

    </pre>

  <h4>Astuce “potentiel”</h4>
  <p>Définir <code>φ(x)=|x|<sub>a</sub>-|x|<sub>b</sub></code>. Lire <code>a</code> → φ+1 ; lire <code>b</code> → φ−1.  
  Pour tout préfixe propre, φ ≥ 0 ; pour le mot complet, (1) dit φ = −1.</p>

  <h4>Check-list pour prouver</h4>
  <ul>
    <li>Commence par le <strong>lemme</strong> “tout mot finit par <code>b</code>”.</li>
    <li>Fais (1) par <strong>induction structurelle</strong> (base <code>b</code>, puis <code>w=a u v</code>).</li>
    <li>Pour (2), liste les <strong>4 types</strong> de préfixes et applique les I.H. sur <code>u</code> et <code>v</code>.</li>
    <li>Si tu doutes, trace la <strong>table des préfixes</strong> (comme l’exemple).</li>
  </ul>

  <h4>Mini-exos</h4>
  <ol>
    <li>Montrer que tout <code>w∈L</code>, <code>w≠b</code>, commence par <code>a</code> et finit par <code>b</code>.</li>
    <li>En déduire que <strong>la longueur de w est impaire</strong> : <code>|w| = 2|w|<sub>a</sub> + 1</code>.</li>
  </ol>
</div>


<!-- ======================================================= -->

<!-- Source: :contentReference[oaicite:2]{index=2} -->
<div class="box question">
  <h2>Exercice 3 — Arbres binaires (A quelconque)</h2>
  <p><strong>Définitions.</strong></p>
  <pre>h(∅)=0 ; h(•)=1 ; h(⟨g,a,d⟩)=1+max(h(g),h(d))
n(∅)=0 ; n(•)=1 ; n(⟨g,a,d⟩)=1+n(g)+n(d)
f(∅)=0 ; f(•)=1 ; f(⟨g,a,d⟩)=f(g)+f(d)</pre>
  <p><strong>À montrer :</strong> ∀t, <code>n(t) ≤ 2^{h(t)} − 1</code> et <code>f(t) ≤ 2^{h(t)-1}</code>.</p>
</div>

<div class="box answer">
  <h3>Réponse (preuves claires pas à pas)</h3>

  <h4>1) Majorer le nombre de nœuds : <code>n(t) ≤ 2^{h(t)} − 1</code></h4>
  <p><em>Preuve par induction structurelle sur t.</em></p>
  <ul>
    <li><strong>Base</strong> :
      <ul>
        <li><code>t=∅</code> : <code>n=0</code>, <code>h=0</code>, donc <code>0 ≤ 2^0−1 = 0</code>. ✓</li>
        <li><code>t=•</code> : <code>n=1</code>, <code>h=1</code>, donc <code>1 ≤ 2^1−1 = 1</code>. ✓</li>
      </ul>
    </li>
    <li><strong>Étape</strong> : <code>t = ⟨g,a,d⟩</code>, poser <code>H = 1 + max(h(g),h(d)) = h(t)</code>.  
      Par I.H. : <code>n(g) ≤ 2^{h(g)}−1</code> et <code>n(d) ≤ 2^{h(d)}−1</code>. Alors
      <pre>n(t) = 1 + n(g) + n(d)
     ≤ 1 + (2^{h(g)}−1) + (2^{h(d)}−1)
     = 2^{h(g)} + 2^{h(d)} − 1.</pre>
      Or <code>h(g) ≤ H−1</code> et <code>h(d) ≤ H−1</code>, donc
      <pre>2^{h(g)} + 2^{h(d)} ≤ 2^{H−1} + 2^{H−1} = 2^H.</pre>
      D’où <code>n(t) ≤ 2^H − 1 = 2^{h(t)} − 1</code>. ✓
    </li>
  </ul>
  <p><em>Intuition :</em> à hauteur <code>H</code>, il peut y avoir au plus <code>2^{H−1}</code> nœuds au dernier niveau, et au total <code>2^H−1</code>.</p>

  <h4>2) Majorer le nombre de feuilles : <code>f(t) ≤ 2^{h(t)-1}</code></h4>
  <p><em>Preuve par induction structurelle sur t.</em></p>
  <ul>
    <li><strong>Base</strong> :
      <ul>
        <li><code>t=∅</code> : <code>f=0</code>, <code>h=0</code>, donc <code>0 ≤ 2^{−1}</code> (vrai ; on peut aussi restreindre l’énoncé aux arbres non vides).</li>
        <li><code>t=•</code> : <code>f=1</code>, <code>h=1</code>, donc <code>1 ≤ 2^{0} = 1</code>. ✓</li>
      </ul>
    </li>
    <li><strong>Étape</strong> : <code>t = ⟨g,a,d⟩</code>, avec <code>H = h(t) = 1 + max(h(g),h(d))</code>.  
      I.H. : <code>f(g) ≤ 2^{h(g)−1}</code>, <code>f(d) ≤ 2^{h(d)−1}</code>. Alors
      <pre>f(t) = f(g) + f(d)
     ≤ 2^{h(g)−1} + 2^{h(d)−1}
     ≤ 2^{H−2} + 2^{H−2} = 2^{H−1} = 2^{h(t)−1}.</pre>
      (car <code>h(g),h(d) ≤ H−1</code> ⇒ <code>2^{h(g)−1},2^{h(d)−1} ≤ 2^{H−2}</code>). ✓
    </li>
  </ul>
  <p><em>Intuition :</em> au dernier niveau (profondeur <code>H−1</code>), il y a au plus <code>2^{H−1}</code> feuilles, et toutes les feuilles se situent au plus bas à ce niveau.</p>

  <h4>(Option) Cas d’égalité</h4>
  <p>Lorsque chaque niveau est complet (arbre “parfait”), on a exactement <code>n(t)=2^{h(t)}−1</code> et <code>f(t)=2^{h(t)−1}</code>.</p>
</div>

<div class="box explain">
  <h3>Explication (méthode et pièges)</h3>
  <ul>
    <li><strong>Méthode</strong> : prouver les bornes en <em>suivant la construction</em> de l’arbre ; remplacer chaque sous-terme par sa <em>borne inductive</em> ; puis utiliser <code>max</code> pour “remonter” à la hauteur de <code>t</code>.</li>
    <li><strong>Astuce</strong> : poser <code>H = 1+max(h(g),h(d))</code> et utiliser <code>2^{h(g)} ≤ 2^{H−1}</code>, <code>2^{h(d)} ≤ 2^{H−1}</code>.</li>
    <li><strong>Piège</strong> : ne pas oublier le “<code>−1</code>” dans <code>n</code>, et décaler d’<code>1</code> l’exposant pour <code>f</code>.</li>
  </ul>
</div>

---

<!-- ======================================================= -->

<div class="box question">
  <h2>Exercice 4 — Arbres binaires stricts (ABS)</h2>
  <p><strong>Définition :</strong> arbres non vides où chaque nœud a 0 ou 2 fils.</p>
  <ol>
    <li>(2) Montrer : <code>n(t) = ar(t) + 1</code>.</li>
    <li>(3) Montrer : <code>n(t) = 2·f(t) − 1</code>.</li>
  </ol>
</div>

<div class="box answer">
  <h3>Réponse (deux façons : inductive et combinatoire)</h3>

  <h4>(2) <code>n(t) = ar(t) + 1</code></h4>
  <p><em>Preuve par induction structurelle (arbres stricts non vides).</em></p>
  <ul>
    <li><strong>Base</strong> (feuille) : <code>n=1</code>, <code>ar=0</code> ⇒ <code>1=0+1</code>. ✓</li>
    <li><strong>Étape</strong> : <code>t = ⟨g,a,d⟩</code> avec deux enfants (arbre strict).  
      <code>n(t)=1+n(g)+n(d)</code>.  
      Les arêtes : toutes celles de <code>g</code> et <code>d</code> plus les deux qui relient la racine à chacun des deux enfants :  
      <code>ar(t)=ar(g)+ar(d)+2</code>.  
      I.H. : <code>n(g)=ar(g)+1</code>, <code>n(d)=ar(d)+1</code>. Donc
      <pre>n(t) = 1 + (ar(g)+1) + (ar(d)+1)
     = ar(g)+ar(d)+3
     = (ar(g)+ar(d)+2) + 1
     = ar(t) + 1.</pre>
      ✓
    </li>
  </ul>
  <p><em>Remarque combinatoire</em> (général pour tout arbre fini connexe) : un arbre a toujours <code>ar = n−1</code>, donc <code>n=ar+1</code>.</p>

  <h4>(3) <code>n(t) = 2·f(t) − 1</code></h4>
  <p><em>Preuve 1 (induction structurelle).</em></p>
  <ul>
    <li><strong>Base</strong> (feuille) : <code>n=1</code>, <code>f=1</code> ⇒ <code>1 = 2·1 − 1</code>. ✓</li>
    <li><strong>Étape</strong> : <code>t = ⟨g,a,d⟩</code> strict ⇒
      <code>n(t)=1+n(g)+n(d)</code>, <code>f(t)=f(g)+f(d)</code>.  
      I.H. : <code>n(g)=2f(g)−1</code>, <code>n(d)=2f(d)−1</code>. Alors
      <pre>n(t) = 1 + (2f(g)−1) + (2f(d)−1)
     = 2(f(g)+f(d)) − 1
     = 2 f(t) − 1.</pre>
      ✓
    </li>
  </ul>
  <p><em>Preuve 2 (combinatoire, très instructive).</em>  
    Écrivons <code>n = i + f</code> (nœuds internes + feuilles).  
    Dans un ABS, chaque nœud interne a exactement 2 enfants ⇒ le nombre d’arêtes vaut <code>ar = 2i</code>.  
    Or pour tout arbre fini, <code>ar = n − 1 = (i+f) − 1</code>.  
    Donc <code>2i = i + f − 1</code> ⇒ <code>i = f − 1</code> ⇒ <code>n = i + f = (f − 1) + f = 2f − 1</code>. ✓
  </p>
</div>

<div class="box explain">
  <h3>Explication (ce qu’il faut retenir)</h3>
  <ul>
    <li><strong>ABS</strong> : chaque nœud interne a 2 enfants ⇒ les arêtes “sortant” des internes sont <code>2·(#internes)</code>.</li>
    <li><strong>Identités à connaître</strong> :
      <ul>
        <li><code>n = ar + 1</code> (vrai pour tout arbre fini connexe).</li>
        <li><code>n = 2f − 1</code> (spécifique aux arbres stricts).</li>
        <li><code>#internes = f − 1</code> (conséquence directe).</li>
      </ul>
    </li>
    <li><strong>Méthode</strong> : induction structurelle = “décompose en <code>g</code> et <code>d</code> + recolle” ;  
        combinatoire = “compte les arêtes de deux façons”.</li>
  </ul>
</div>


