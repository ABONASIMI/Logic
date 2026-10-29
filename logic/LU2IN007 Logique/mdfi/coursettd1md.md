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

/* Optional labeled code wrapper you can use with HTML:
  <div class="code"><div class="label">A.sh</div><pre><code>…</code><pre></div> */

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


<div class="box explain">

<h3>Ch. 1 — Ensembles, relations, fonctions (résumé pédagogique, pages 1 → 20)</h3>
<small>Version claire et complète, en français simple. Signes utilisés : ∈, ∉, ⊆, ⊂, =, ≠, ∪, ∩, \, △ (différence symétrique), ×, Ā, |E|, Id<sub>E</sub>, R⁻¹, R∘S, Rⁿ, R⁺, R*.</small>

<!-- =========================
   1) ENSEMBLES : NOTIONS DE BASE
========================= -->

<h4>1) Ensembles : notions de base</h4>
<b>Idée.</b> Un ensemble regroupe des objets (éléments) bien définis.  
• Appartenance : x ∈ E ; non-appartenance : x ∉ E.  
• Ensemble vide : ∅.  Singleton : {e}.  Cardinal d’un ensemble fini : |E|.  
• Deux ensembles sont égaux s’ils ont exactement les mêmes éléments (peu importe l’ordre ou les répétitions).

<b>Exemples.</b>

1. 2 ∈ {1,2,3}, 4 ∉ {1,2,3}.
2. {2} est un élément de {{1,3},{2},{5}}, mais {2} n’est pas un élément de {1,2,5} (là ce sont des nombres, pas des ensembles).
3. |∅|=0, |{1,1,2}|=2 (les doublons ne comptent pas).

<b>Deux écritures utiles.</b>
• <i>Par extension</i> : E = {0,1,2,3}.
• <i>Par compréhension</i> : E = {x ∈ ℕ | x ≤ 3} (“x naturel tel que x ≤ 3”).

<hr>

<!-- =========================
   2) INCLUSION & ÉGALITÉ
========================= -->

<h4>2) Inclusion (⊆) et égalité (=)</h4>
• A ⊆ B : chaque élément de A est aussi dans B (A “contenu” dans B).  
• A ⊂ B : A ⊆ B et A ≠ B (inclusion stricte).  
• A = B ⇔ (A ⊆ B et B ⊆ A).

<b>Propriétés de ⊆.</b> Réflexive (A⊆A), transitive (A⊆B, B⊆C ⇒ A⊆C), antisymétrique (A⊆B & B⊆A ⇒ A=B). C’est un <i>ordre partiel</i> : deux ensembles ne sont pas toujours comparables.

<b>Exemples.</b>

1. ∅ ⊆ E (toujours vrai).
2. {1,2} ⊆ {1,2,3}.
3. {1,2} et {1,4,5} ne sont pas comparables (ni l’un ni l’autre ne contient l’autre).

<hr>

<!-- =========================
   3) OPÉRATIONS : ∪, ∩, \, COMPLÉMENT, △
========================= -->

<h4>3) Opérations ensemblistes</h4>
• Union : A ∪ B = {x | x∈A ou x∈B}.  
• Intersection : A ∩ B = {x | x∈A et x∈B}.  
• Différence : A \ B = {x∈A | x∉B}.  
• Complément (dans un univers E fixé) : Ā = {x∈E | x∉A}.  
• Différence symétrique : A △ B = (A \ B) ∪ (B \ A) (“dans l’un OU l’autre, mais pas les deux”).

<b>Mots clés.</b> A et B sont <i>disjoints</i> si A ∩ B = ∅.

<b>Exemples.</b>

1. {1,2,3} ∪ {2,3,4} = {1,2,3,4}.
2. {1,2,3} ∩ {2,4} = {2}.
3. Si E={1,2,3,4,5} et A={1,4}, alors Ā={2,3,5}.
4. {1,2,3} △ {3,4} = {1,2,4}.

<b>Comptage (ensembles finis).</b> |A ∪ B| = |A| + |B| − |A ∩ B|.
(Version 3 ensembles, à connaître : |A∪B∪C| = |A|+|B|+|C| − |A∩B| − |A∩C| − |B∩C| + |A∩B∩C|.)

<hr>

<!-- =========================
   4) PRODUIT CARTÉSIEN
========================= -->

<h4>4) Produit cartésien (×)</h4>
• A × B = { (a,b) | a∈A et b∈B }.  Pour n ensembles : E₁×…×Eₙ = ensembles de n-uplets.  
• Cardinal (fini) : |E₁×…×Eₙ| = |E₁|⋯|Eₙ|.

<b>Exemples.</b>

1. {1,2}×{a,b} = {(1,a),(1,b),(2,a),(2,b)}.
2. A×∅ = ∅×A = ∅ (impossible de former un couple).
3. Si |A|=3, |B|=2, |C|=5 ⇒ |A×B×C| = 3·2·5 = 30.

<hr>

<!-- =========================
   5) LOIS CLASSIQUES (IDENTITÉS)
========================= -->

<h4>5) Lois classiques (toujours utiles)</h4>
<b>Associativité.</b> A∪(B∪C)=(A∪B)∪C ; A∩(B∩C)=(A∩B)∩C.  
<b>Commutativité.</b> A∪B=B∪A ; A∩B=B∩A.  
<b>Distributivité.</b> A∩(B∪C)=(A∩B)∪(A∩C) ; A∪(B∩C)=(A∪B)∩(A∪C).  
<b>Idempotence.</b> A∪A=A ; A∩A=A.  
<b>Absorption.</b> A∪(A∩B)=A ; A∩(A∪B)=A.  
<b>De Morgan.</b> (A∪B)̄=Ā∩B̄ ; (A∩B)̄=Ā∪B̄.  
<b>Vide.</b> A∪∅=A ; A∩∅=∅ ; A\∅=A ; ∅\A=∅.

<b>Exemples rapides.</b>
• Avec A={1,2}, B={2,3}, C={2} : A∩(B∪C)=A∩{2,3}={2}=(A∩B)∪(A∩C).
• Dans E={1,2,3}, A={1}, B={2} : (A∪B)̄={3}=Ā∩B̄.

<hr>

<!-- =========================
   6) ENSEMBLE DES PARTIES (PUISSANCE)
========================= -->

<h4>6) Ensemble des parties P(E)</h4>
• P(E) = {A | A ⊆ E} : l’ensemble de tous les sous-ensembles de E.  
• Toujours ∅ ∈ P(E) et E ∈ P(E).  
• Cardinal : si |E|=n alors |P(E)|=2ⁿ.

<b>Exemple.</b> P({1,2,3}) = {∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}.

<b>Construction récursive.</b> Si E={e}∪F (avec e∉F), alors
P(E) = P(F) ∪ { {e}∪A | A∈P(F) }.

<hr>

<!-- =========================
   7) PARTITIONS
========================= -->

<h4>7) Partitions</h4>
• Une <b>partition</b> de E est une famille de sous-ensembles non vides, deux à deux disjoints, dont l’union est E.  
• Intuition : on “découpe” E en blocs sans chevauchement.

<b>Exemples.</b>

1. E={a,b,c} : {{a},{b,c}} est une partition.
2. E={1,2,3,4,5,6} : {{1,3,5},{2,4,6}} (impairs vs pairs).
3. {{a,b},{b,c}} n’est pas une partition de {a,b,c} (chevauchement en b).

<hr>

<!-- =========================
   8) RELATIONS : DÉFINITION & EXEMPLES
========================= -->

<h4>8) Relations (binaire, unaire, n-aire)</h4>
• Relation <b>binaire</b> R de E vers F : sous-ensemble de E×F. Si E=F : relation “sur E”.  
• Identité sur E : Id<sub>E</sub> = { (x,x) | x∈E }.  
• Relation <b>unaire</b> : simplement une partie de E (un prédicat “oui/non”).  
• Relation <b>n-aire</b> : sous-ensemble de E₁×…×Eₙ.

<b>Exemples (sur ℕ).</b>

1. ≤ = { (m,n) | m ≤ n }.
2. <  = { (m,n) | m < n } = ≤ \ Id<sub>ℕ</sub>.
3. “est parent de” sur un ensemble de personnes P ⊆ P×P.

<hr>

<!-- =========================
   9) OPÉRATIONS SUR LES RELATIONS
========================= -->

<h4>9) Opérations sur les relations</h4>
Comme une relation est un ensemble, on peut prendre union, intersection, différence, complément (dans un univers produit fixé), et inclusion.

<b>Inverse.</b> Pour R⊆E×F, l’inverse R⁻¹⊆F×E : (y,x)∈R⁻¹ ⇔ (x,y)∈R.
Ex. : “>” est l’inverse de “<”.

<b>Composition (produit).</b> Si R⊆E×F et S⊆F×G, alors
S∘R = { (x,z)∈E×G | ∃y∈F, (x,y)∈R et (y,z)∈S }.
Propriétés : associative ; <i>pas</i> commutative ; Id est neutre (R∘Id = Id∘R = R) ; ∅ est absorbant.

<b>Pouvoirs d’une relation (sur E).</b> R⁰=Id<sub>E</sub>, R¹=R, R²=R∘R, …, Rⁿ=R∘…∘R (n fois).

<hr>

<!-- =========================
   10) FERMETURES R⁺ ET R*
========================= -->

<h4>10) Fermetures (transitive R⁺, réflexo-transitive R*)</h4>
<b>Idée.</b> On “complète” la relation en ajoutant le minimum de couples pour obtenir la propriété voulue.

• <b>Transitive</b> : R⁺ = R ∪ R² ∪ R³ ∪ … (toutes les “chaînes” de longueur ≥ 1).
• <b>Réflexo-transitive</b> : R* = Id ∪ R ∪ R² ∪ … (ajoute aussi les boucles (x,x)).

<b>Interprétation graphe.</b> Si les nœuds sont les éléments et les arcs les couples (x,y)∈R :
• R⁺ relie x à y s’il existe un chemin de longueur ≥1.
• R* ajoute les boucles (chemin de longueur 0).

<b>Exemple clé (successeur S={(n,n+1)} sur ℕ).</b>
• S⁺ = “<” (on peut aller de n à m si n<m par des pas +1 répétés).
• S* = “≤” (on autorise aussi 0 pas : n→n).

<hr>

<!-- =========================
   11) PROPRIÉTÉS DES RELATIONS
========================= -->

<h4>11) Propriétés des relations (à tester)</h4>
• <b>Réflexive</b> : ∀x, (x,x)∈R.  • <b>Antiréflexive</b> (ou irréflexive) : ∀x, (x,x)∉R.  
• <b>Symétrique</b> : (x,y)∈R ⇒ (y,x)∈R.  • <b>Antisymétrique</b> : (x,y)∈R & (y,x)∈R ⇒ x=y.  
• <b>Transitive</b> : (x,y)∈R & (y,z)∈R ⇒ (x,z)∈R.  
• <b>Totale</b> (connexe au sens ordre) : ∀x≠y, (x,y)∈R ou (y,x)∈R.

<b>Exemples classiques.</b>

1. “≤” sur ℕ : réflexive, antisymétrique, transitive, totale.
2. “<” sur ℕ : transitive, antiréflexive, mais pas symétrique.
3. “a ≡ b (mod n)” : réflexive, symétrique, transitive (c’est une <i>équivalence</i>).
4. S={(n,n+1)} n’est pas transitive (2→3 et 3→4, mais pas 2→4).

<hr>

<!-- =========================
   12) ÉQUIVALENCES, CLASSES & QUOTIENT
========================= -->

<h4>12) Relations d’équivalence & quotient</h4>
• <b>Équivalence</b> : réflexive + symétrique + transitive.  
• Chaque élément e engendre une <b>classe</b> [e] = {x | e R x}.  
• L’ensemble des classes E/R forme une <b>partition</b> de E.

<b>Exemples.</b>

1. Mod 2 : deux classes (pairs / impairs).
2. Mod 3 : trois classes ([0], [1], [2]).
3. “même longueur de mot” sur A* : classes “longueur paire” et “longueur impaire”.

<hr>

<!-- =========================
   13) ORDRES (PARTIELS / TOTAUX)
========================= -->

<h4>13) Ordres (partiels et totaux)</h4>
• <b>Ordre</b> : réflexive + antisymétrique + transitive.  
• <b>Ordre partiel</b> : certains éléments peuvent être incomparables.  
• <b>Ordre total</b> : toute paire est comparable (x≤y ou y≤x).

<b>Exemples.</b>

1. “⊆” sur P(E) : ordre partiel (ex. {1} et {2} incomparables dans P({1,2})).
2. “≤” sur ℕ : ordre total.
3. “divise” (|) sur ℕ{0} : ordre partiel (2 et 3 sont incomparables).

<hr>

<!-- =========================
   14) FONCTIONS & APPLICATIONS
========================= -->

<h4>14) Fonctions et applications</h4>
• Une relation f⊆E×F est une <b>fonction</b> si chaque x∈E possède <i>au plus</i> une image (déterminisme).  
• Une <b>application</b> (fonction totale) est définie pour <i>tout</i> x∈E (exactement une image).  
• <b>Partielle</b> : si f n’est pas définie pour certains x.

<b>Vocabulaire.</b> y = f(x) ; image directe f(A) = {f(x) | x∈A} ; pré-image f⁻¹(B) = {x∈E | f(x)∈B}.
• f⁻¹(U∪V) = f⁻¹(U) ∪ f⁻¹(V) ; f⁻¹(U∩V) = f⁻¹(U) ∩ f⁻¹(V).
• f(A∪B) = f(A) ∪ f(B) (toujours) ; en revanche f(A∩B) ⊆ f(A)∩f(B) (égalité non garantie).

<b>Exemples essentiels.</b>

1. S:ℕ→ℕ, S(n)=n+1 est une application.
2. P:ℕ→ℕ, P(n)=n−1 n’est pas totale (P(0) non défini) ; mais P’:(ℕ{0})→ℕ, P’(n)=n−1 est totale.
3. “≤” n’est pas une fonction (un x a trop d’images).

<hr>

<!-- =========================
   15) INJECTIVE / SURJECTIVE / BIJECTIVE
========================= -->

<h4>15) Injective, surjective, bijective</h4>
• <b>Injective</b> : f(x₁)=f(x₂) ⇒ x₁=x₂ (deux entrées différentes n’ont pas la même image).  
• <b>Surjective</b> : ∀y∈F, ∃x∈E tel que f(x)=y (tout y est atteint).  
• <b>Bijective</b> : injective + surjective ; alors f admet une réciproque f⁻¹: F→E, et f∘f⁻¹=Id<sub>F</sub>, f⁻¹∘f=Id<sub>E</sub>.

<b>Exemples.</b>

1. S:ℕ→ℕ, n↦n+1 : injective, non surjective (0 n’a pas de antécédent).
2. S’:ℤ→ℤ, n↦n+1 : bijection (inverse : n↦n−1).
3. sq:ℤ→ℤ, n↦n² : ni injective (2 et −2), ni surjective (pas d’image négative).

<hr>

<!-- =========================
   16) PETITS EXEMPLES GUIDÉS (PAGES 1–20)
========================= -->

<h4>16) Exemples guidés (construits comme dans un TD)</h4>
<b>(A) Calculs d’ensembles.</b>  
• E={1,2,3,4,5}, A={1,3,5}, B={2,3,4}.  
A∪B={1,2,3,4,5}, A∩B={3}, A\B={1,5}, B\A={2,4}, Ā={2,4} (dans E).  
• C={1,2,4}, D={2,4,6}.  
C △ D = {1,6} ; C∩(D∪{1}) = {1,2,4} ; C\(D∩{2,4}) = {1}.

<b>(B) Produit cartésien.</b>
• X={0,1}, Y={a,b,c}. |X×Y| = 2·3 = 6 ; X×Y = {(0,a),(0,b),(0,c),(1,a),(1,b),(1,c)}.

<b>(C) Relations.</b>
• R sur {1,2,3} définie par R={(1,2),(2,3)}.
R²={(1,3)} ; R³=∅ ; donc R⁺={(1,2),(2,3),(1,3)} ; R* = Id ∪ R⁺.
• Inverse : R⁻¹={(2,1),(3,2)} ; R∘R⁻¹ = {(1,1),(2,2)} ; R⁻¹∘R = {(2,2),(3,3)} (pas commutatif).

<b>(D) Fonctions.</b>
• f:ℤ→ℤ, f(x)=2x+1 : injective (2x+1=2y+1 ⇒ x=y) et surjective (tout y a x=(y−1)/2∈ℤ). Donc bijection ; f⁻¹(y)=(y−1)/2.
• g:ℕ→ℕ, g(n)=⌊n/2⌋ : surjective (k a comme antécédents 2k et 2k+1), pas injective.

<hr>

<h4>17) Pièges fréquents (et comment les éviter)</h4>
• Confondre “∈” (appartenance) et “⊆” (inclusion). Ex. {2} ⊆ {1,2}, mais {2} ∉ {1,2}.  
• Oublier l’univers pour le complément : Ā dépend de E.  
• Appeler “fonction” une relation non déterministe (un x avec deux images).  
• Croire que la composition R∘S est commutative (en général non).  
• Penser qu’une classe d’équivalence est un seul élément : c’est un <i>sous-ensemble</i> entier (le “bloc” de la partition).

<hr>

<h4>18) Mini-checklist (révisions rapides)</h4>
1) <b>Ensembles</b> : ∈/∉, ⊆/⊂, ∪, ∩, \, △, compléments ; |A∪B| ; |P(E)|=2ⁿ.  
2) <b>Relations</b> : Id, inverse, composition, puissances Rⁿ, fermetures R⁺/R*. Tester réflexive/symétrique/antisymétrique/transitive/totale.  
3) <b>Fonctions</b> : déterminisme, total/partiel ; image/pré-image ; injective/surjective/bijective ; réciproque si bijective.

<hr>

<h4>19) Exercices d’entraînement (énoncés très courts, réponses immédiates)</h4>
1) Prouvez A∩(B∪C)=(A∩B)∪(A∩C). <i>(Indice : double inclusion.)</i> <br>
2) Développez (A∪B)̄ via De Morgan.<br>  
3) Donnez un exemple d’ensembles incomparables pour ⊆.<br>  
4) Donnez E, A tels que Ā soit non vide (précisez E).  <br>
5) Listez {0,1}×{a,b,c}.  <br>
6) Calculez |A×B×C| avec |A|=2, |B|=5, |C|=0. <br>  
7) Donnez une partition de {1,2,3,4} en 3 blocs.   <br> 
8) Sur {1,2,3}, donnez une relation R non réflexive et non  symétrique.   <br> 
9) Donnez un R tel que R∘R ≠ R.   <br> 
10) Construisez R⁺ pour R={(1,2),(2,3)}.   <br> 
11) Testez si “<” est symétrique et/ou transitive.   <br> 
12) Décrivez les classes modulo 4.   <br> 
13) Montrez que “⊆” sur P({1,2,3}) n’est pas total.  <br>   
14) Donnez un exemple de relation totale non symétrique.   <br> 
15) f:ℕ→ℕ, n↦n+2 : injective ? surjective ?   <br> 
16) f:ℤ→ℤ, n↦−n : bijective ? donnez f⁻¹.   <br> 
17) Donnez un exemple où f(A∩B) ⊊ f(A)∩f(B).   <br> 
18) Montrez f⁻¹(U∪V)=f⁻¹(U)∪f⁻¹(V).   <br> 
19) Donnez une fonction partielle ℕ⇀ℕ.   <br> 
20) Sur ℕ, montrez que S(n)=n+1 n’a pas d’inverse (comme fonction ℕ→ℕ).  <br> 

<hr>

<h4>20) Dernier conseil</h4>
Travaillez toujours “au symbole près” : écrivez les définitions mot-à-mot (⊆, R∘S, R⁺, R*…), faites des petits dessins mentaux de “qui contient qui” et vérifiez chaque propriété sur 2–3 exemples concrets. C’est la meilleure façon d’être rapide et sûr le jour du contrôle.


<hr>

<h4>21) Relations : propriétés fines & schémas usuels</h4>
<b>Antiréflexive (irréflexive)</b> : ∀x, (x,x) ∉ R. Exemple : « &lt; » sur ℕ est irréflexive.<br>
<b>Asymétrique</b> : ∀x≠y, (x,y)∈R ⇒ (y,x)∉R. Toute relation asymétrique est irréflexive. Exemple : « &lt; » est asymétrique.<br>
<b>Connexité (totale) sur un ensemble E</b> : ∀x≠y, (x,y)∈R ou (y,x)∈R. Exemple : « ≤ » sur ℕ est totale.<br>
<b>Trichotomie (pour un ordre strict)</b> : ∀x≠y, exactement une des trois est vraie : x&lt;y ou y&lt;x ou x=y (mais pas deux).<br><br>

<b>Schémas fréquents</b><br>
• R = « ≤ », R\Id = « < » ; R symétrique ⇒ R∩(R\Id) = ∅ ; R antisymétrique ⇒ (xRy et yRx) ⇒ x=y.<br>
• « ≡ mod n » est équivalence (réflexive, symétrique, transitive). Ses classes sont les restes 0,…,n−1.<br><br>

<b>Mini-exemples</b><br>

1. Sur E={a,b,c}, R={(a,b),(b,c)} n’est ni réflexive ni symétrique ni transitive. R⁺ ajoute (a,c).<br>
2. Sur ℕ, « divise » (|) : réflexive (n|n), antisymétrique, transitive ; pas totale (2∤3 et 3∤2).<br>

<hr>

<h4>22) Hasse (diagrammes d’ordre partiel)</h4>
Un <b>diagramme de Hasse</b> représente un ordre partiel sans flèches ni boucles, en retirant les arêtes « déductibles » par transitivité. On place x sous y si x≤y et on relie seulement les <b>recouvrements</b> (x&lt;y sans élément strictement entre).<br><br>

<b>Exemples</b><br>
• (P({1,2,3}), ⊆) : base en bas (∅), sommet en haut ({1,2,3}); chaque élément s’ajoute un par un.<br>
• Divisibilité sur {1,2,3,6} : 1 en bas, 2 et 3 au milieu, 6 en haut ; arêtes 1–2, 1–3, 2–6, 3–6.<br>

<hr>

<h4>23) Bornes, maximum, minimum, sup, inf</h4>
<b>Borne supérieure de A (sup A)</b> : plus petite des bornes supérieures (si elle existe).<br>
<b>Borne inférieure (inf A)</b> : plus grande des bornes inférieures (si elle existe).<br>
<b>Maximum</b> : un élément m∈A tel que ∀a∈A, a≤m. S’il existe, max A = sup A et m∈A.<br>
<b>Minimum</b> : dual. Si min A existe, min A = inf A et m∈A.<br><br>

<b>Exemples</b><br>
• Dans ℕ, tout ensemble non vide a un min (bien-ordonné).<br>
• Dans ℚ, l’ensemble {x∈ℚ | x²<2} n’a pas de max mais a sup = √2 (qui n’est pas rationnel).<br>

<hr>

<h4>24) Ordres lexicographiques</h4>
Sur A×B, on définit (a₁,b₁) ≤<sub>lex</sub> (a₂,b₂) si <b>soit</b> a₁&lt;a₂ <b>soit</b> (a₁=a₂ et b₁≤b₂).<br>
Prolongement naturel à A×B×C… ; très utile pour « trier » des tuples et obtenir des ordres totaux à partir d’ordres totaux.<br><br>

<b>Exemple</b><br>
Sur ℕ×ℕ, (0,100) ≤<sub>lex</sub> (1,0) car 0<1, même si 100>0. Par contre (1,2) ≤<sub>lex</sub> (1,5) car 1=1 et 2≤5.<br>

<hr>

<h4>25) Fonctions : images et pré-images (règles complètes)</h4>
<b>Image directe</b> : f(A) = { f(x) | x∈A }.<br>
<b>Pré-image</b> : f⁻¹(B) = { x | f(x)∈B } (définie pour toute fonction, même non bijective).<br><br>

<b>Règles sûres (toujours vraies)</b><br>
• f(A∪B) = f(A) ∪ f(B).<br>
• f(A∩B) ⊆ f(A) ∩ f(B) (égalité <i>fausse</i> en général).<br>
• f⁻¹(B∪C) = f⁻¹(B) ∪ f⁻¹(C).<br>
• f⁻¹(B∩C) = f⁻¹(B) ∩ f⁻¹(C).<br>
• f⁻¹(B̄) = (f⁻¹(B))̄ (complément pris dans le domaine).<br><br>

<b>Exemples</b><br>

1. f constante : f(A)=f(B) ⇒ f(A∩B) peut être ≠ f(A)∩f(B) si A∩B=∅.<br>
2. f(x)=x² sur ℤ : f({−2,2})={4} ; f⁻¹({4})={−2,2}.<br>

<hr>

<h4>26) Restrictions, co-restrictions, extension</h4>
<b>Restriction</b> : si f:E→F et A⊆E, la restriction f|<sub>A</sub>: A→F garde la même formule, mais un plus petit domaine.<br>
<b>Co-restriction</b> : si Im(f)⊆B⊆F, on peut voir f comme f:E→B.<br>
<b>Extension</b> : compléter la définition de f sur un domaine plus grand (en respectant la cohérence).<br><br>

<b>Utilité</b><br>
• Rendre une fonction « surjective » sur son image en remplaçant F par Im(f).<br>
• Rendre P(n)=n−1 totale en restreignant le domaine à ℕ{0}.<br>

<hr>

<h4>27) Injectivité, surjectivité, bijectivité — équivalences utiles</h4>
<b>Injective</b> ⇔ ∀y, la fibre f⁻¹({y}) contient au plus un élément.<br>
<b>Surjective</b> ⇔ Im(f)=F ⇔ ∀y∈F, f⁻¹({y}) ≠ ∅.<br>
<b>Bijective</b> ⇔ ∀y∈F, |f⁻¹({y})| = 1 (exactement un antécédent).<br><br>

<b>Inverses à gauche/droite</b><br>
• f injective ⇔ ∃g (à gauche) telle que g∘f = Id<sub>E</sub> (g « annule » f après).<br>
• f surjective ⇔ ∃h (à droite) telle que f∘h = Id<sub>F</sub> (h « remonte » sur f).<br>
• f bijective ⇔ ∃f⁻¹ unique telle que f∘f⁻¹=Id<sub>F</sub> et f⁻¹∘f=Id<sub>E</sub>.<br>

<hr>

<h4>28) Composition de fonctions</h4>
Si f:E→F et g:F→G, alors (g∘f):E→G, (g∘f)(x)=g(f(x)).<br>
<b>Associativité</b> : h∘(g∘f)=(h∘g)∘f. <b>Pas commutative</b> en général.<br><br>

<b>Préservation des propriétés</b><br>
• Si f et g sont injectives, g∘f est injective.<br>
• Si f et g sont surjectives, g∘f est surjective.<br>
• Si f et g sont bijectives, g∘f est bijective (et (g∘f)⁻¹ = f⁻¹ ∘ g⁻¹).<br>

<hr>

<h4>29) Permutations (bijections de E vers E)</h4>
Une <b>permutation</b> est une bijection σ:E→E. L’ensemble des permutations de E, muni de la composition, forme un <b>groupe</b> (neutre = Id, inverses = réciproques).<br><br>

<b>Exemples</b><br>
• Sur {1,2,3}, la transposition (1 2) échange 1↔2 et laisse 3 fixe. Sa propre inverse est elle-même.<br>
• Les permutations se représentent en 2 lignes ou en <i>cycles</i> (1 3 2) signifie 1↦3, 3↦2, 2↦1.<br>

<hr>

<h4>30) Dénombrabilité (compter l’infini)</h4>
Un ensemble E est <b>dénombrable</b> s’il existe une bijection E↔ℕ (on peut « lister » ses éléments).<br><br>
<b>Exemples dénombrables</b><br>
• ℕ, ℤ, les pairs {2n}, les impairs {2n+1}.<br>
• ℕ×ℕ (parcours en diagonales).<br>
• Les rationnels ℚ (on peut les lister en balayant les paires (p,q) et en simplifiant).<br><br>

<b>Non dénombrable</b><br>
• ℝ n’est pas dénombrable (argument diagonal).<br>
• P(E) a toujours une « taille » strictement plus grande que E : pas de bijection E→P(E).<br>

<hr>

<h4>31) Mots sur un alphabet, monoïdes libres</h4>
<b>Alphabet A</b> : ensemble fini de symboles (ex. A={a,b}).<br>
<b>Mot</b> : suite finie de symboles de A. Longueur |w|. Mot vide ε (|ε|=0).<br>
<b>Concaténation</b> : u·v (souvent notée uv). Associative ; ε est neutre (εu=uε=u).<br>
<b>A*</b> : ensemble de tous les mots sur A (incluant ε). (A*, concaténation, ε) est un <b>monoïde</b>.<br><br>

<b>Notions</b><br>
• Préfixe, suffixe, facteur (sous-mot). Ex : « pro » est préfixe de « proton » ; « ton » est suffixe ; « rot » est facteur.<br>
• Langage L ⊆ A* ; opérations : union, concaténation, étoile de Kleene L* = {ε} ∪ L ∪ LL ∪ LLL ∪ …<br>

<hr>

<h4>32) Équivalences ↔ partitions (aller-retour complet)</h4>
Toute <b>équivalence</b> R sur E induit une <b>partition</b> de E (les classes).<br>
Toute <b>partition</b> de E définit une <b>équivalence</b> en disant « x R y ⇔ x et y sont dans le même bloc ». Les deux constructions sont inverses l’une de l’autre.<br><br>

<b>Exemple</b><br>
Sur ℤ, « a ≡ b (mod 3) » donne les 3 classes [0], [1], [2]. Réciproquement, ces 3 blocs définissent l’équivalence modulo 3.<br>

<hr>

<h4>33) Ordres : chaînes, antichaînes, Zorn (intuition)</h4>
<b>Chaîne</b> : sous-ensemble totalement ordonné. <b>Antichaîne</b> : aucun deux éléments comparables.<br>
<b>Idée de Zorn (sans preuve)</b> : sous des hypothèses de chaînes majorées, il existe un élément maximal. (Outil théorique, utile plus tard.)<br>

<hr>

<h4>34) Exercices avancés (avec indications et réponses courtes)</h4>
<b>E1.</b> Sur E={1,2,3,4}, R={(1,2),(2,3),(3,4)}. Calculez R², R³, R⁺, R*.<br>
<i>Indication</i> : R² relie 1→3, 2→4 ; R³ relie 1→4 ; R⁴=∅. Donc R⁺=R∪R²∪R³ ; R*=Id∪R⁺.<br>
<b>Réponse</b> : R²={(1,3),(2,4)}, R³={(1,4)}, R⁺={(1,2),(2,3),(3,4),(1,3),(2,4),(1,4)}, R*=Id∪R⁺.<br><br>

<b>E2.</b> f:ℤ→ℤ, f(x)=3x−2. Injective ? Surjective ? Inverse ?<br> <i>Réponse</i> : injective (3x−2=3y−2 ⇒ x=y), surjective (pour y, prendre x=(y+2)/3 ∈ ℤ ⇔ y≡1 (mod 3) ? Non : sur ℤ, (y+2)/3 ∈ ℤ ⇔ y≡1 (mod 3). Donc <b>pas</b> surjective sur ℤ. Surjective si on co-restreint le codomaine à 3ℤ−2. Inverse sur cette image : f⁻¹(y)=(y+2)/3.<br><br>

<b>E3.</b> Montrer : f(A∩B) ⊆ f(A)∩f(B) et donner un contre-exemple où l’égalité échoue.<br> <i>Réponse</i> : vrai pour l’inclusion. Contre-exemple : f constante ⇒ f(A)=f(B), mais A∩B peut être ∅, donc f(A∩B)=∅ ≠ f(A)∩f(B).<br><br>

<b>E4.</b> Donner une relation asymétrique qui n’est pas totale sur E={1,2,3}.<br> <i>Réponse</i> : R={(1,2)}. Asymétrique (2,1) absent ; pas totale (1 et 3 non comparés, 2 et 3 non comparés).<br><br>

<b>E5.</b> Sur P({1,2,3}), montrer que « ⊆ » est un ordre partiel mais non total.<br> <i>Réponse</i> : réflexif, antisymétrique, transitif ; non total : {1} et {2} incomparables.<br><br>

<b>E6.</b> ℕ×ℕ est-il dénombrable ?<br> <i>Réponse</i> : oui, par énumération diagonale (ou encodage via un entier unique).<br><br>

<b>E7.</b> Décrire les classes modulo 4.<br> <i>Réponse</i> : [0]={…−8,−4,0,4,8,…}, [1]={…−7,−3,1,5,…}, [2]={…−6,−2,2,6,…}, [3]={…−5,−1,3,7,…}.<br><br>

<b>E8.</b> Prouvez : (A△B)△C = A△(B△C).<br> <i>Indication</i> : utiliser la définition par « XOR ensembliste » et les tables de vérité (associativité du XOR).<br> <i>Réponse</i> : vrai (associativité).<br><br>

<b>E9.</b> Donner un ordre lexicographique sur {0,1}×{a,b,c} et trier : (1,b), (0,c), (1,a), (0,a).<br> <i>Réponse</i> : 1) (0,a) 2) (0,c) 3) (1,a) 4) (1,b).<br><br>

<b>E10.</b> Soit f:ℕ→ℕ, f(n)=n+1 et g:ℕ→ℕ, g(n)=2n. Étudier g∘f et f∘g (formules + injectivité/surjectivité).<br> <i>Réponse</i> : g∘f(n)=2(n+1)=2n+2 (injective, non surjective : 1 n’est image d’aucun n). f∘g(n)=2n+1 (injective, non surjective : 0 n’a pas d’antécédent).<br>

<hr>

<h4>35) Astuces de révision (format « check »)</h4>
• Pour une <b>relation</b>, testez R(x,x) (réflexive/irréflexive), comparez paires inversées (symétrie/antisymétrie), et composez deux pas (transitivité).<br>
• Pour une <b>fonction</b>, commencez par « déterminisme » (un x, au plus une image) puis « totale ? » (chaque x a une image). Ensuite Im(f), pré-image, injective/surjective ; si bijection, écrivez f⁻¹.<br>
• Pour les <b>ensembles</b>, posez toujours l’univers E avant de parler de complément ; utilisez les formules de cardinal et la différence symétrique pour vérifier vos calculs.<br>

<hr>

<h4>36) Mini-banque supplémentaire (drills très courts)</h4>
1) Vrai/Faux : une relation asymétrique peut être réflexive. <b>Faux</b> (asymétrie ⇒ irréflexive).<br>
2) Donner un exemple de fonction non injective mais surjective ℕ→ℕ. <i>Impossible</i> (sur ℕ vers ℕ, la surjectivité impose l’injectivité si f est croissante ; mais on peut construire des surjections non injectives si on accepte des “planchers”, p.ex. g(n)=⌊n/2⌋ est sur ℕ→ℕ surjective <i>et</i> non injective).<br>
3) Montrer : f⁻¹(B\C) = f⁻¹(B) \ f⁻¹(C). <b>Vrai</b> (dépliage de définitions).<br>
4) Prouvez : si f et g sont bijectives, alors (g∘f)⁻¹ = f⁻¹∘g⁻¹. <b>Vrai</b> par calcul direct.<br>
5) Sur E fini, si f:E→E est injective, elle est surjective (et réciproquement).<br>

<hr>

<h3>Conclusion</h3>
Vous avez maintenant la « deuxième moitié » du chapitre : ordres (Hasse, bornes, lexicographique), fonctions fines (images/pré-images, restrictions, inverses), dénombrabilité, mots/monoïdes — plus une batterie d’exemples et d’exercices. <br><br>
Besoin d’un <b>pack d’exercices</b> format TD avec corrections ligne par ligne ? Dites-moi le volume (10, 20 ou 30) et le niveau (basique → très dur), je vous le prépare dans le même style avec &lt;br&gt; pour l’aération.

</div>


<div class="box explain">

<h3>Conclusion générale — « Ensembles, relations, fonctions » (pages 0 → ici)</h3>
<small>Résumé final + boîte à outils + exercices supplémentaires corrigés. Écriture claire, espacée, prête à copier-coller. J’ajoute des &lt;br&gt; quand utile.</small>

<hr>

<h4>1) Ce qu’il faut retenir (vision d’ensemble)</h4>
<b>Ensembles.</b> L’appartenance (∈/∉) et l’inclusion (⊆) sont la base. Savoir manipuler ∪, ∩, \, complément Ā (dans un univers E), différence symétrique △, produit cartésien ×. Le cardinal des ensembles finis se calcule avec les formules classiques (ex. |A∪B| = |A|+|B|−|A∩B|). P(E) contient tous les sous-ensembles de E, avec |P(E)| = 2ⁿ si |E|=n. <br><br>

<b>Partitions.</b> Découper E en blocs non vides, deux à deux disjoints, dont la réunion est E. C’est le miroir des relations d’équivalence : chaque équivalence ⇄ une partition (les classes). <br><br>

<b>Relations.</b> Une relation binaire R est un sous-ensemble de E×F (souvent E=F). Opérations : inverse R⁻¹, composition S∘R, puissances Rⁿ, fermetures R⁺ (transitive) et R* (réflexo-transitive). Propriétés à tester : réflexive / irréflexive, symétrique / antisymétrique, transitive, totale (connexe). <br><br>

<b>Équivalences & ordres.</b> Équivalence = réflexive + symétrique + transitive → classes d’équivalence → quotient E/R. Ordre = réflexive + antisymétrique + transitive ; partiel (pas forcément comparable) ou total (toute paire comparable). Diagramme de Hasse pour les ordres partiels. Notions de minimum/maximum, borne inf/sup. Ordre lexicographique sur des produits. <br><br>

<b>Fonctions.</b> Une fonction est une relation déterministe (au plus une image par x). Application = fonction totale (définie pour tout x du domaine). Image f(A), pré-image f⁻¹(B), règles sûres sur ∪/∩ et complément. Caractères : injective, surjective, bijective. Si bijection, réciproque f⁻¹ et stabilité par composition. <br><br>

<b>Infini & structures.</b> Dénombrabilité (ℕ, ℤ, ℚ, ℕ×ℕ) vs non dénombrable (ℝ, P(E)). Mots sur un alphabet A, concaténation, monoïde (A*, ·, ε). <br><br>

<b>Idées clés.</b> (i) Écrire les définitions « mot à mot » pour prouver ; (ii) raisonner par <i>double inclusion</i> pour les égalités d’ensembles ; (iii) « déplier » les quantificateurs pour tester une propriété de relation ; (iv) pour les fonctions : déterminisme → total/partiel → image/pré-image → inject/surject/biject → inverse. <br>

<hr>

<h4>2) Boîte à outils (formules & réflexes)</h4>
• |A∪B| = |A| + |B| − |A∩B| <br>
• |A∪B∪C| = |A|+|B|+|C| − |A∩B| − |A∩C| − |B∩C| + |A∩B∩C| <br>
• P(E) : si |E|=n alors |P(E)|=2ⁿ <br>
• De Morgan : (A∪B)̄ = Ā ∩ B̄ ; (A∩B)̄ = Ā ∪ B̄ <br>
• Différence symétrique : A △ B = (A\B) ∪ (B\A) <br>
• Produit cartésien (fini) : |E₁×…×Eₙ| = |E₁|…|Eₙ| <br>
• Composition de relations : (S∘R)(x,z) ⇔ ∃y, (x,y)∈R ∧ (y,z)∈S <br>
• Fermetures : R⁺ = ⋃<sub>k≥1</sub> Rᵏ ; R* = Id ∪ R⁺ <br>
• Fonctions : f(A∪B)=f(A)∪f(B) ; f(A∩B)⊆f(A)∩f(B) ; f⁻¹(B∪C)=f⁻¹(B)∪f⁻¹(C) ; f⁻¹(B∩C)=f⁻¹(B)∩f⁻¹(C) ; f⁻¹(B̄)=(f⁻¹(B))̄ <br>
• Bijections : (g∘f)⁻¹ = f⁻¹ ∘ g⁻¹ <br>

<hr>

<h4>3) Pièges à éviter</h4>
• Confondre « ∈ » et « ⊆ ». Exemple : {2} ⊆ {1,2} mais {2} ∉ {1,2}. <br>
• Oublier de fixer l’univers pour le complément Ā. <br>
• Appeler « fonction » une relation qui donne 2 images au même x (non déterministe). <br>
• Croire que la composition est commutative (en général, non). <br>
• Penser que « f(A∩B) = f(A)∩f(B) » (seulement ⊆ en général). <br>

<hr>

<h4>4) Stratégie de résolution (recette express)</h4>
<b>Égalité d’ensembles :</b> prouver A⊆B puis B⊆A. <br>
<b>Propriété d’une relation :</b> traduire la définition (xRx ? yRx ?) et tester avec un témoin y. <br>
<b>Fonction :</b> (1) déterminisme ; (2) total ? ; (3) image/pré-image ; (4) inject / surject ; (5) biject ? inverse ? <br>
<b>Comptage :</b> identifier les recouvrements (∩) avant de sommer. <br>

<hr>

<h3>Exercices supplémentaires — corrigés (nouvelle série)</h3>
<small>Énoncé → Solution courte. J’espace chaque item avec &lt;br&gt;.</small>

<b>Ex1.</b> Dans E, montrer : A(B∪C) = (A\B) ∩ (A\C). <br> <i>Sol.</i> x∈A(B∪C) ⇔ x∈A et x∉B∪C ⇔ (x∈A ∧ x∉B ∧ x∉C) ⇔ x∈(A\B)∩(A\C). <br><br>

<b>Ex2.</b> Prouvez : (A△B)△C = A△(B△C). <br> <i>Sol.</i> Interpréter △ comme XOR ensembliste ; or XOR est associatif → égalité. <br><br>

<b>Ex3.</b> Soit A={1,2,3,4}, B={3,4,5}, C={2,4,6}. Calculez A∪B, A∩B, A△B, (A\B)∪(B\A), A∩(B∪C). <br> <i>Sol.</i> A∪B={1,2,3,4,5}; A∩B={3,4}; A△B={1,2,5}; (A\B)∪(B\A)={1,2,5}; A∩(B∪C)={2,3,4}. <br><br>

<b>Ex4.</b> L’ensemble des sous-ensembles de {a,b,c,d} ayant exactement 2 éléments a un cardinal ? <br> <i>Sol.</i> C(4,2)=6 (toutes les paires). <br><br>

<b>Ex5.</b> Décrire une partition de {1,2,3,4,5,6} basée sur la parité et le signe « >3 ». <br> <i>Sol.</i> Quatre blocs : {1,3,5}, {2}, {4,6}, { } pour 2≤? Mieux : séparer en (impairs ≤3) {1,3}, (impairs >3) {5}, (pairs ≤3) {2}, (pairs >3) {4,6}. <br><br>

<b>Ex6.</b> Sur E={1,2,3}, R={(1,2),(2,3)}. Donnez R², R³, R⁺, R*. <br> <i>Sol.</i> R²={(1,3)} ; R³=∅ ; R⁺={(1,2),(2,3),(1,3)} ; R* = Id ∪ R⁺. <br><br>

<b>Ex7.</b> Tester si R est réflexive, symétrique, transitive : R={(1,1),(2,2),(1,2)} sur {1,2}. <br> <i>Sol.</i> Réflexive : oui (les boucles y sont). Symétrique : non (2,1) manque. Transitive : oui (pas de (2,1), donc pas de chaîne qui casse). <br><br>

<b>Ex8.</b> Construire une relation asymétrique non totale sur {a,b,c}. <br> <i>Sol.</i> R={(a,b)} : asymétrique (b,a) absent), non totale (a et c incomparables, b et c aussi). <br><br>

<b>Ex9.</b> Ordre de divisibilité sur {1,2,3,6}: donner les éléments minimaux et maximaux. <br> <i>Sol.</i> Minimaux : {1}. Maximaux : {6}. <br><br>

<b>Ex10.</b> Ordre lexicographique sur {0,1}×{a,b}: triez (1,a),(0,b),(0,a),(1,b). <br> <i>Sol.</i> (0,a) < (0,b) < (1,a) < (1,b). <br><br>

<b>Ex11.</b> f:ℤ→ℤ, f(x)=2x+1. Injective ? Surjective ? f⁻¹ ? <br> <i>Sol.</i> Injective : oui. Sur ℤ, pas surjective (les images sont toutes impaires). Sur Im(f)={…,-3,-1,1,3,…}, f⁻¹(y)=(y−1)/2. <br><br>

<b>Ex12.</b> g:ℕ→ℕ, g(n)=⌊n/2⌋. Injective ? Surjective ? <br> <i>Sol.</i> Non injective (2k et 2k+1 ont même image k). Surjective (tout k a des antécédents 2k, 2k+1). <br><br>

<b>Ex13.</b> Montrer f(A∩B) ⊆ f(A)∩f(B). Donner un contre-exemple pour l’égalité. <br> <i>Sol.</i> Inclusion : direct par définition. Contre-exemple : f constante → f(A)=f(B) mais si A∩B=∅, alors f(A∩B)=∅ ≠ {c}. <br><br>

<b>Ex14.</b> Prouvez f⁻¹(U∪V)=f⁻¹(U)∪f⁻¹(V) et f⁻¹(U∩V)=f⁻¹(U)∩f⁻¹(V). <br> <i>Sol.</i> Dépliage des définitions (équivalences logiques). <br><br>

<b>Ex15.</b> Si f et g sont bijectives, montrer que (g∘f) est bijective et donner (g∘f)⁻¹. <br> <i>Sol.</i> Composition de bijections = bijection ; (g∘f)⁻¹ = f⁻¹ ∘ g⁻¹. <br><br>

<b>Ex16.</b> Dénombrabilité : esquisser une énumération de ℕ×ℕ. <br> <i>Sol.</i> Parcours en diagonales : (0,0),(0,1),(1,0),(0,2),(1,1),(2,0),… <br><br>

<b>Ex17.</b> Montrer qu’il n’existe pas de bijection E → P(E). <br> <i>Sol.</i> Par « ensemble diagonal » B={x∈E | x∉f(x)} : contradiction si B=f(b). <br><br>

<b>Ex18.</b> Alphabet A={a,b}. Donnez A* jusqu’aux mots de longueur 2, et L* si L={a}. <br> <i>Sol.</i> A* (≤2) = {ε, a, b, aa, ab, ba, bb}. L* = {ε, a, aa, aaa, …}. <br><br>

<b>Ex19.</b> Sur P({1,2,3}), « ⊆ » est-il total ? Donner deux éléments incomparables. <br> <i>Sol.</i> Non. {1} et {2} sont incomparables (ni {1}⊆{2} ni l’inverse). <br><br>

<b>Ex20.</b> Soit R relation sur E avec R⊆S. Prouver R⁺ ⊆ S⁺ et R* ⊆ S*. <br> <i>Sol.</i> Par induction sur les puissances : Rᵏ ⊆ Sᵏ pour tout k ⇒ unions inchangées. <br>

<hr>

<h4>Mot de fin</h4>
Vous avez la carte complète : <b>ensembles</b> → <b>relations</b> (équivalences, ordres, fermetures) → <b>fonctions</b> (images, pré-images, inject/surject/biject, inverses) → <b>infini et mots</b>. <br>
En examen, partez toujours des <b>définitions</b>, utilisez la <b>double inclusion</b> pour les égalités, et suivez la <b>checklist</b> pour relations/fonctions. C’est systématique, fiable, et ça fait gagner des points.

</div>


<h3>TD1 — Exercice 1 : Ensembles (produit, parties, partitions)</h3>

<div class="box question">
<b>Question 1.</b> Calculer le produit cartésien <code>S<sub>1</sub> × S<sub>1</sub></code> pour <code>S<sub>1</sub> = {0, 1, 2}</code>.
</div>

<div class="box answer">
<b>Réponse.</b><br>
<code>S<sub>1</sub> × S<sub>1</sub> = { (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) }</code>.
</div>

<div class="box explain">
<b>Explications.</b><br>
• Le produit cartésien <code>A×B</code> est l’ensemble de tous les couples <code>(a,b)</code> avec <code>a∈A</code> et <code>b∈B</code>.<br>
• Si <code>|S<sub>1</sub>|=3</code>, alors <code>|S<sub>1</sub>×S<sub>1</sub>| = 3×3 = 9</code> couples.<br>
• Astuce : liste d’abord les couples qui commencent par 0, puis ceux qui commencent par 1, puis par 2.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Question 2a.</b> Calculer l’ensemble des parties <code>℘(S)</code> pour <code>S = S<sub>1</sub> = {0,1,2}</code>.
</div>

<div class="box answer">
<b>Réponse.</b><br>
<code>℘({0,1,2}) = { ∅, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2} }</code>.
</div>

<div class="box explain">
<b>Explications.</b><br>
• <code>℘(S)</code> (power set) = l’ensemble de <u>tous</u> les sous-ensembles de <code>S</code>.<br>
• Si <code>|S| = n</code>, alors <code>|℘(S)| = 2<sup>n</sup></code>. Ici <code>n=3</code> ⇒ 8 sous-ensembles.<br>
• Méthode : énumérer les sous-ensembles de taille 0, puis de taille 1, 2, et 3.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Question 2b.</b> Calculer <code>℘(S)</code> pour <code>S = S<sub>2</sub> = { 1, {1,4} }</code>.
</div>

<div class="box answer">
<b>Réponse.</b><br>
<code>℘(S<sub>2</sub>) = { ∅, {1}, {{1,4}}, { 1, {1,4} } }</code>.
</div>

<div class="box explain">
<b>Explications.</b><br>
• Attention : <code>1</code> et <code>{1,4}</code> sont deux <u>éléments</u> distincts de <code>S<sub>2</sub></code> (le second est un ensemble).<br>
• Comme <code>|S<sub>2</sub>|=2</code>, il y a <code>2<sup>2</sup>=4</code> sous-ensembles : vide, les 2 singletons, et l’ensemble total.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Question 2c.</b> Soit <code>S<sub>3</sub> = ℘({1})</code>. Calculer <code>℘(S<sub>3</sub>)</code>.
</div>

<div class="box answer">
<b>Réponse.</b><br>
On a d’abord <code>℘({1}) = { ∅, {1} }</code>. Donc<br>
<code>℘(S<sub>3</sub>) = ℘( { ∅, {1} } ) = { ∅, { ∅ }, { {1} }, { ∅, {1} } }</code>.
</div>

<div class="box explain">
<b>Explications.</b><br>
• Étape 1 : calculer <code>S<sub>3</sub></code> = toutes les parties de <code>{1}</code> ⇒ <code>{ ∅, {1} }</code> (2 éléments).<br>
• Étape 2 : prendre l’ensemble des parties de <code>S<sub>3</sub></code> ⇒ <code>2<sup>2</sup>=4</code> sous-ensembles, en veillant aux accolades imbriquées.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Question 3.</b> Donner <u>toutes</u> les partitions de l’ensemble <code>{1,2,3}</code>.
</div>

<div class="box answer">
<b>Réponse (les 5 partitions).</b><br>
1) <code>{{1,2,3}}</code><br>
2) <code>{{1},{2,3}}</code><br>
3) <code>{{2},{1,3}}</code><br>
4) <code>{{3},{1,2}}</code><br>
5) <code>{{1},{2},{3}}</code>
</div>

<div class="box explain">
<b>Explications.</b><br>
• Une partition = blocs <u>non vides</u>, <u>deux à deux disjoints</u>, dont l’union est tout l’ensemble.<br>
• Pour 3 éléments, le nombre de partitions est le nombre de Bell <code>B<sub>3</sub>=5</code> (cas : 1 bloc ; 1 singleton + 1 doublet (×3 façons) ; 3 singletons).<br>
• Vérification : aucun chevauchement, aucun oubli, et la réunion vaut <code>{1,2,3}</code>.
</div>



<h3>TD1 — Exercice 2 : Raisonnement sur les ensembles</h3>
<small>Énoncés d’après le TD1 LU2IN005. </small>

<div class="box question">
<b>Q1.</b> Soient <code>A,B</code> des parties de <code>E</code>. Montrer : <code>A ∩ (A ∩ B) = A ∩ B</code>.
</div>

<div class="box answer">
<b>Réponse.</b> Vrai par <u>associativité</u> et <u>idempotence</u> de <code>∩</code> :<br>
<code>A ∩ (A ∩ B) = (A ∩ A) ∩ B = A ∩ B</code>.
</div>

<div class="box explain">
<b>Preuve élément par élément.</b> « ⊆ » : si <code>x ∈ A ∩ (A ∩ B)</code>, alors <code>x ∈ A</code> et <code>x ∈ A ∩ B</code>, donc <code>x ∈ A</code> et <code>x ∈ B</code> ⇒ <code>x ∈ A ∩ B</code>.<br>
« ⊇ » : si <code>x ∈ A ∩ B</code>, alors <code>x ∈ A</code> et <code>x ∈ B</code>, donc <code>x ∈ A ∩ B</code> et encore <code>x ∈ A</code> ⇒ <code>x ∈ A ∩ (A ∩ B)</code>.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q2.</b> Soient <code>A,B,C</code> des parties de <code>E</code>. Montrer que si <code>A ∩ B = A ∩ C</code>, alors<br>
<code>A ∩ (B \ C) = ∅</code> et <code>A ∩ (C \ B) = ∅</code>.
</div>

<div class="box answer">
<b>Réponse.</b> Si <code>x ∈ A ∩ (B \ C)</code>, alors <code>x ∈ A</code>, <code>x ∈ B</code> et <code>x ∉ C</code>. Or <code>A ∩ B = A ∩ C</code> impose : «<code>x ∈ A</code> et <code>x ∈ B</code>» ⇔ «<code>x ∈ A</code> et <code>x ∈ C</code>», contradiction. Donc <code>A ∩ (B \ C)=∅</code>. Le même argument donne <code>A ∩ (C \ B)=∅</code>.
</div>

<div class="box explain">
<b>Idée.</b> L’égalité « couplée à A » force B et C à coïncider sur A : aucune partie de B\C (resp. C\B) ne peut rencontrer A.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q3.</b> En déduire l’équivalence :<br>
<code>A ∩ B = A ∩ C</code> ⇔ <code>A ∩ (B △ C) = ∅</code> &nbsp;(<i>où</i> <code>B △ C = (B\C) ∪ (C\B)</code>).
</div>

<div class="box answer">
<b>Réponse.</b> « ⇒ » : par Q2, <code>A ∩ (B\C)=∅</code> et <code>A ∩ (C\B)=∅</code>, donc leur union <code>A ∩ (B△C)=∅</code>.<br>
« ⇐ » : si <code>A ∩ (B△C)=∅</code>, alors <code>A ∩ (B\C)=∅</code> et <code>A ∩ (C\B)=∅</code>. Ainsi<br>
<code>A ∩ B = A ∩ ((B∩C) ∪ (B\C)) = (A∩B∩C) ∪ ∅ = A ∩ (B∩C)</code>,<br>
et symétriquement <code>A ∩ C = A ∩ (B∩C)</code>. Donc <code>A ∩ B = A ∩ C</code>.
</div>

<div class="box explain">
<b>Lecture.</b> « Égalité sur A » ⇔ « B et C ne diffèrent pas à l’intérieur de A ».
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q4.</b> Soient <code>A,B,C</code> des parties de <code>E</code>. Montrer que si <code>A ∪ B ⊆ A ∪ C</code> et <code>A ∩ B ⊆ A ∩ C</code>, alors <code>B ⊆ C</code>. <br>Dans quel cas a-t-on <code>B = C</code> ?
</div>

<div class="box answer">
<b>Réponse.</b> Soit <code>b ∈ B</code>. Deux cas :<br>
• Si <code>b ∈ A</code>, alors <code>b ∈ A ∩ B ⊆ A ∩ C</code> ⇒ <code>b ∈ C</code>.<br>
• Si <code>b ∉ A</code>, alors <code>b ∈ A ∪ B ⊆ A ∪ C</code>. Comme <code>b ∉ A</code>, il faut <code>b ∈ C</code>.<br>
Donc <code>B ⊆ C</code>. Pour l’égalité, il faut aussi l’inclusion réciproque (mêmes hypothèses en échangeant <code>B</code> et <code>C</code>) :<br>
<b>Condition nécessaire et suffisante :</b> <code>A ∪ B = A ∪ C</code> <u>et</u> <code>A ∩ B = A ∩ C</code>.
</div>

<div class="box explain">
<b>Truc.</b> Décomposer « <code>b ∈ B</code> » en « dans A » / « hors de A ». Les deux hypothèses couvrent exactement ces cas.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q5.</b> Montrer : <code>A × (B ∩ C) = (A × B) ∩ (A × C)</code>.
</div>

<div class="box answer">
<b>Réponse.</b> « ⊆ » : si <code>(a,b) ∈ A×(B∩C)</code>, alors <code>a∈A</code>, <code>b∈B∩C</code> ⇒ <code>(a,b)∈A×B</code> et <code>(a,b)∈A×C</code> ⇒ dans l’intersection.<br>
« ⊇ » : si <code>(a,b) ∈ (A×B) ∩ (A×C)</code>, alors <code>a∈A</code>, <code>b∈B</code> et <code>b∈C</code> ⇒ <code>b∈B∩C</code> ⇒ <code>(a,b)∈A×(B∩C)</code>.
</div>

<div class="box explain">
<b>Idée.</b> Un couple est dans l’intersection des produits ⇔ sa seconde composante est dans les deux ensembles.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q6.</b> A-t-on <code>℘(A ∩ B) = ℘(A) ∩ ℘(B)</code> ? Et <code>℘(A ∪ B) = ℘(A) ∪ ℘(B)</code> ?
</div>

<div class="box answer">
<b>Réponse.</b><br>
• <code>℘(A ∩ B) = ℘(A) ∩ ℘(B)</code> : <b>vrai</b>, car <code>X ⊆ A∩B</code> ⇔ (<code>X ⊆ A</code> et <code>X ⊆ B</code>).<br>
• <code>℘(A ∪ B) = ℘(A) ∪ ℘(B)</code> : <b>faux</b> en général. Contre-exemple : <code>A={1}</code>, <code>B={2}</code>. Alors <code>{1,2} ∈ ℘(A∪B)</code> mais <code>{1,2} ∉ ℘(A) ∪ ℘(B)</code>.
</div>

<div class="box explain">
<b>Lecture.</b> Être « partie de l’intersection » équivaut à « être partie de A et de B ». En revanche, une partie de <code>A∪B</code> peut mélanger des éléments de A et de B : elle n’est alors ni partie de A ni de B.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q7.</b> Soit <code>E ⊆ F</code> et <code>x ∈ F \ E</code>. Montrer :<br>
<code>℘(E ∪ {x}) = ℘(E) ∪ { {x} ∪ A &nbsp;|&nbsp; A ∈ ℘(E) }</code>.
</div>

<div class="box answer">
<b>Réponse.</b> Toute partie <code>X ⊆ E ∪ {x}</code> est de deux types :<br>
• soit <code>x ∉ X</code> ⇒ <code>X ⊆ E</code> ⇒ <code>X ∈ ℘(E)</code> ;<br>
• soit <code>x ∈ X</code> ⇒ <code>X = {x} ∪ A</code> avec <code>A = X \{x} ⊆ E</code> ⇒ <code>X ∈ { {x} ∪ A | A∈℘(E) }</code>.<br>
Réciproquement, toute partie listée à droite est évidemment incluse dans <code>E ∪ {x}</code>. Donc égalité.
</div>

<div class="box explain">
<b>Remarque (cardinal).</b> Si <code>|E|=n</code> (fini), alors le membre de droite contient <code>2^n</code> parties sans <code>x</code> + <code>2^n</code> parties avec <code>x</code>, total <code>2^{n+1}=|℘(E∪{x})|</code>.
</div>



<h3>TD1 — Exercice 2 : Raisonnement sur les ensembles (version détaillée pas à pas)</h3>

<div class="box question">
<b>Q1.</b> Soient <code>A,B</code> des parties de <code>E</code>. Montrer : <code>A ∩ (A ∩ B) = A ∩ B</code>.
</div>

<div class="box answer">
<b>Preuve pas à pas (double inclusion).</b><br>
1) <u>Inclusion</u> <code>A ∩ (A ∩ B) ⊆ A ∩ B</code> :<br>
&nbsp;&nbsp;Soit <code>x ∈ A ∩ (A ∩ B)</code>. Alors <code>x ∈ A</code> et <code>x ∈ A ∩ B</code>, donc <code>x ∈ B</code> aussi.<br>
&nbsp;&nbsp;Ainsi <code>x ∈ A</code> et <code>x ∈ B</code> ⇒ <code>x ∈ A ∩ B</code>.<br><br>
1) <u>Inclusion</u> <code>A ∩ B ⊆ A ∩ (A ∩ B)</code> :<br>
&nbsp;&nbsp;Soit <code>x ∈ A ∩ B</code>. Alors <code>x ∈ A</code> et <code>x ∈ B</code> ⇒ <code>x ∈ A ∩ B</code> et (bien sûr) <code>x ∈ A</code>.<br>
&nbsp;&nbsp;Donc <code>x ∈ A ∩ (A ∩ B)</code>.<br><br>
Les deux inclusions donnent l’égalité : <code>A ∩ (A ∩ B) = A ∩ B</code> (idempotence de <code>∩</code>).
</div>

<div class="box explain">
<b>Idée-clé.</b> On « répète » A inutilement : l’intersection avec A deux fois ne change rien.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q2.</b> Soient <code>A,B,C</code> des parties de <code>E</code>. Montrer que si <code>A ∩ B = A ∩ C</code>, alors <code>A ∩ (B \ C) = ∅</code> et <code>A ∩ (C \ B) = ∅</code>.
</div>

<div class="box answer">
<b>Preuve par contradiction (pour le premier).</b><br>
Supposons <code>∃x</code> tel que <code>x ∈ A ∩ (B \ C)</code> ; alors <code>x ∈ A</code>, <code>x ∈ B</code> et <code>x ∉ C</code>.<br>
Or <code>A ∩ B = A ∩ C</code> ⇒ « <code>x ∈ A</code> et <code>x ∈ B</code> » équivaut à « <code>x ∈ A</code> et <code>x ∈ C</code> », contradiction avec <code>x ∉ C</code>.<br>
Donc <code>A ∩ (B \ C)=∅</code>.<br><br>
<b>Par symétrie</b>, on obtient <code>A ∩ (C \ B)=∅</code>.
</div>

<div class="box explain">
<b>Lecture.</b> Sur A, B et C « coïncident » ; donc aucune différence (B\C ou C\B) ne peut rencontrer A.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q3.</b> En déduire l’équivalence : <code>A ∩ B = A ∩ C</code> ⇔ <code>A ∩ (B △ C) = ∅</code>, où <code>B △ C = (B\C) ∪ (C\B)</code>.
</div>

<div class="box answer">
<b>Sens « ⇒ ».</b> Si <code>A ∩ B = A ∩ C</code>, Q2 donne <code>A ∩ (B\C)=∅</code> et <code>A ∩ (C\B)=∅</code>. Donc<br>
<code>A ∩ (B △ C) = A ∩ ((B\C) ∪ (C\B)) = (A∩(B\C)) ∪ (A∩(C\B)) = ∅ ∪ ∅ = ∅</code>.<br><br>
<b>Sens « ⇐ ».</b> Si <code>A ∩ (B △ C) = ∅</code>, alors <code>A ∩ (B\C)=∅</code> et <code>A ∩ (C\B)=∅</code>.<br>
Écrivons alors :<br>
<code>A ∩ B = A ∩ ((B∩C) ∪ (B\C)) = (A∩B∩C) ∪ (A∩(B\C)) = A∩B∩C</code> ;<br>
<code>A ∩ C = A ∩ ((B∩C) ∪ (C\B)) = (A∩B∩C) ∪ (A∩(C\B)) = A∩B∩C</code>.<br>
Ainsi <code>A ∩ B = A ∩ C</code>.
</div>

<div class="box explain">
<b>Interprétation.</b> « Égalité sur A » ⇔ « B et C ne diffèrent pas à l’intérieur de A ».
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q4.</b> Soient <code>A,B,C</code> des parties de <code>E</code>. Si <code>A ∪ B ⊆ A ∪ C</code> et <code>A ∩ B ⊆ A ∩ C</code>, montrer <code>B ⊆ C</code>. Quand a-t-on <code>B = C</code> ?
</div>

<div class="box answer">
<b>Preuve (raisonnement par cas).</b><br>
Soit <code>b ∈ B</code>.<br>
• Si <code>b ∈ A</code>, alors <code>b ∈ A ∩ B ⊆ A ∩ C</code> ⇒ <code>b ∈ C</code>.<br>
• Si <code>b ∉ A</code>, comme <code>b ∈ B</code> on a <code>b ∈ A ∪ B ⊆ A ∪ C</code>. Or <code>b ∉ A</code>, donc nécessairement <code>b ∈ C</code>.<br>
Dans tous les cas, <code>b ∈ C</code>, donc <code>B ⊆ C</code>.<br><br>
<b>Pour l’égalité</b> : il faut l’inclusion réciproque, obtenue en échangeant <code>B</code> et <code>C</code>. Ainsi<br>
<u>Condition équivalente à</u> <code>B=C</code> : <code>A ∪ B = A ∪ C</code> et <code>A ∩ B = A ∩ C</code>.
</div>

<div class="box explain">
<b>Astuce.</b> Décomposer « dans A » / « hors de A ». Les deux hypothèses couvrent exactement ces cas.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q5.</b> Montrer : <code>A × (B ∩ C) = (A × B) ∩ (A × C)</code>.
</div>

<div class="box answer">
<b>Preuve élément par élément.</b><br>
• « ⊆ » : si <code>(a,b) ∈ A×(B∩C)</code>, alors <code>a∈A</code> et <code>b∈B∩C</code> ⇒ <code>(a,b)∈A×B</code> et <code>(a,b)∈A×C</code> ⇒ dans l’intersection.<br>
• « ⊇ » : si <code>(a,b) ∈ (A×B) ∩ (A×C)</code>, alors <code>a∈A</code>, <code>b∈B</code> et <code>b∈C</code> ⇒ <code>b∈B∩C</code> ⇒ <code>(a,b)∈A×(B∩C)</code>.<br>
Égalité obtenue par double inclusion.
</div>

<div class="box explain">
<b>Idée.</b> Un couple est dans les deux produits ⇔ sa 2<sup>e</sup> composante est dans les deux ensembles.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q6.</b> A-t-on <code>℘(A ∩ B) = ℘(A) ∩ ℘(B)</code> ? Et <code>℘(A ∪ B) = ℘(A) ∪ ℘(B)</code> ?
</div>

<div class="box answer">
<b>Première égalité.</b> <code>℘(A ∩ B) = ℘(A) ∩ ℘(B)</code> est <b>vraie</b> :<br>
&nbsp;&nbsp;Soit <code>X</code>. Alors <code>X ∈ ℘(A ∩ B)</code> ⇔ <code>X ⊆ A ∩ B</code> ⇔ (<code>X ⊆ A</code> et <code>X ⊆ B</code>) ⇔ (<code>X ∈ ℘(A)</code> et <code>X ∈ ℘(B)</code>) ⇔ <code>X ∈ ℘(A) ∩ ℘(B)</code>.<br><br>
<b>Deuxième égalité.</b> <code>℘(A ∪ B) = ℘(A) ∪ ℘(B)</code> est <b>fausse</b> en général :<br>
&nbsp;&nbsp;Exemple : <code>A={1}</code>, <code>B={2}</code>. Alors <code>{1,2} ⊆ A∪B</code> donc <code>{1,2} ∈ ℘(A∪B)</code> ;<br>
&nbsp;&nbsp;mais <code>{1,2} ⊄ A</code> et <code>{1,2} ⊄ B</code>, donc <code>{1,2} ∉ ℘(A) ∪ ℘(B)</code>.
</div>

<div class="box explain">
<b>Lecture.</b> Être « partie de l’intersection » ⇔ être « simultanément partie de A et de B ». En revanche, une partie de <code>A∪B</code> peut mélanger des éléments de A et de B et n’être partie d’aucun des deux pris séparément.
</div>

<hr class="spacer-md">

<div class="box question">
<b>Q7.</b> Soit <code>E ⊆ F</code> et <code>x ∈ F \ E</code>. Montrer :<br>
<code>℘(E ∪ {x}) = ℘(E) ∪ { {x} ∪ A &nbsp;|&nbsp; A ∈ ℘(E) }</code>.
</div>

<div class="box answer">
<b>Preuve par classification des parties de</b> <code>E∪{x}</code>.<br>
Soit <code>X ⊆ E ∪ {x}</code>.<br>
• Si <code>x ∉ X</code>, alors <code>X ⊆ E</code> ⇒ <code>X ∈ ℘(E)</code> (1<sup>er</sup> morceau du membre droit).<br>
• Si <code>x ∈ X</code>, alors on peut écrire <code>X = {x} ∪ A</code> avec <code>A = X \{x} ⊆ E</code> ⇒ <code>A ∈ ℘(E)</code> et <code>X ∈ { {x} ∪ A | A ∈ ℘(E) }</code> (2<sup>e</sup> morceau).<br><br>
Réciproquement, toute partie du membre droit est manifestement incluse dans <code>E ∪ {x}</code>. D’où l’égalité souhaitée.
</div>

<div class="box explain">
<b>Conséquence (cardinal fini).</b> Si <code>|E| = n</code>, alors <code>|℘(E)| = 2<sup>n</sup></code> et <code>|℘(E ∪ {x})| = 2<sup>n+1</sup></code> :<br>
• on compte <code>2<sup>n</sup></code> parties sans <code>x</code> (celles de <code>E</code>) ;<br>
• et <code>2<sup>n</sup></code> parties avec <code>x</code> (chacune de la forme <code>{x} ∪ A</code>, <code>A ∈ ℘(E)</code>).<br>
Total : <code>2<sup>n</sup> + 2<sup>n</sup> = 2·2<sup>n</sup> = 2<sup>n+1</sup></code>.
</div>



<h3>TD1 — Exercice 3 : Ensembles et Relations</h3>
<small>Énoncé exact — TD1 « Ensembles, Relations, Fonctions ».</small>

<div class="box question">
<b>Exercice 3 [Ensembles et Relations]</b><br>
On considère la relation (ternaire) <code>S</code> définie sur <code>D = {0, 1, 2, 3, 4}</code> par <code>S(a, b, c)</code> ssi <code>c = a+ b</code>. Décrire <code>S</code> sous la forme d’un sous-ensemble de <code>D3</code>.
</div>

<div class="box answer">
<b>Réponse.</b><br>
On veut <code>(a,b,c) ∈ D<sup>3</sup></code> tel que <code>c = a + b</code> et <code>c ∈ D</code> (donc <code>a+b ≤ 4</code>). L’ensemble est :
<pre><code>S = {
  (0,0,0), (0,1,1), (0,2,2), (0,3,3), (0,4,4),
  (1,0,1), (1,1,2), (1,2,3), (1,3,4),
  (2,0,2), (2,1,3), (2,2,4),
  (3,0,3), (3,1,4),
  (4,0,4)
}
</code></pre>
</div>

<div class="box explain">
<b>Explications (pas à pas).</b><br>
• On parcourt <code>a ∈ {0,..,4}</code>. Pour chaque <code>a</code>, on prend les <code>b</code> tels que <code>a+b ≤ 4</code> (ainsi <code>c=a+b</code> reste dans <code>D</code>).<br>
• Par exemple : pour <code>a=2</code>, <code>b ∈ {0,1,2}</code> donnent <code>(2,0,2)</code>, <code>(2,1,3)</code>, <code>(2,2,4)</code>. Pour <code>a=4</code>, seul <code>b=0</code> convient, donc <code>(4,0,4)</code>.<br>
• Notation : dans l’énoncé, <code>D3</code> désigne le produit cartésien <code>D × D × D = D<sup>3</sup></code>.
</div>



<h3>TD1 — Exercice 5 : Produit/composition et inverse de relations</h3>

<div class="box question">
<b>Énoncé exact</b> — <i>Produit/composition et inverse de relations</i> <br><br>
1. Soient <code>A = {1, 2, 3, 4}</code>, <code>B = {1, 3, 5}</code> et <code>R ⊆ A×B</code> la relation définie par <code>(a, b) ∈ R</code> ssi <code>a &lt; b</code>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;(a) Écrire la relation <code>R</code> comme un ensemble de paires ordonnées.<br>
&nbsp;&nbsp;&nbsp;&nbsp;(b) Calculer les relations <code>R<sup>−1</sup>.R</code> et <code>R.R<sup>−1</sup></code>.<br><br>
1. Montrer que pour deux relations quelconques <code>R ⊆ X × Y</code> et <code>S ⊆ Y × Z</code>, on a l’égalité
<code>(R.S)<sup>−1</sup> = S<sup>−1</sup>.R<sup>−1</sup></code>.<br><br>
1. On considère la relation <code>R ⊆ ℕ × ℕ</code> définie par <code>(x, y) ∈ R</code> ssi <code>y = 2x</code>. Quels sont les éléments de <code>R<sup>+</sup></code> ?
</div>

<hr class="spacer-md">

<!-- Q1(a) -->

<div class="box question">
<b>Q1(a).</b> Écrire <code>R</code> comme un ensemble de paires ordonnées.
</div>

<div class="box answer">
On dresse toutes les paires <code>(a,b)</code> avec <code>a ∈ A</code>, <code>b ∈ B</code> et <code>a &lt; b</code> :<br>
<code>R = { (1,3), (1,5), (2,3), (2,5), (3,5), (4,5) }</code>.
</div>

<div class="box explain">
<b>Méthode.</b> Pour chaque <code>a</code>, garder les <code>b</code> de <code>B</code> strictement plus grands :<br>
• <code>a=1</code> → <code>b=3,5</code> ; <code>a=2</code> → <code>b=3,5</code> ; <code>a=3</code> → <code>b=5</code> ; <code>a=4</code> → <code>b=5</code>.
</div>

<hr class="spacer-md">

<!-- Q1(b) -->

<div class="box question">
<b>Q1(b).</b> Calculer <code>R<sup>−1</sup>.R</code> et <code>R.R<sup>−1</sup></code>.
</div>

<div class="box answer">
<b>Inverse.</b> <code>R<sup>−1</sup> = { (3,1), (5,1), (3,2), (5,2), (5,3), (5,4) }</code> (on inverse chaque paire de <code>R</code>).<br><br>

<b>Composition</b> (on lit « point » comme la composition usuelle) :<br>
• <u>Sur <code>A×A</code></u>, <code>R<sup>−1</sup>.R</code> : il existe <code>b ∈ B</code> tel que <code>a < b</code> et <code>c < b</code>. En prenant <code>b=5</code>, la condition est vraie pour <i>tous</i> <code>a,c ∈ A</code>. Donc<br> <code>R<sup>−1</sup>.R = A × A</code> (relation totale sur <code>A</code>).<br><br>
• <u>Sur <code>B×B</code></u>, <code>R.R<sup>−1</sup></code> : il existe <code>a ∈ A</code> tel que <code>a < b</code> et <code>a < d</code>. Cela équivaut à <code>min(b,d) > 1</code>. Avec <code>B={1,3,5}</code>, on obtient<br> <code>R.R<sup>−1</sup> = { (3,3), (3,5), (5,3), (5,5) }</code>.

</div>

<div class="box explain">
<b>Détails.</b><br>
• <code>R<sup>−1</sup>.R</code> : pour tout <code>(a,c)</code>, choisir <code>b=5</code> (qui est dans <code>B</code>) donne <code>a&lt;5</code> et <code>c&lt;5</code>, donc <code>(a,c)</code> appartient ; ainsi tous les <code>16</code> couples de <code>A×A</code> sont présents.<br>
• <code>R.R<sup>−1</sup></code> : la condition « il existe <code>a</code> &lt; <code>b</code> et &lt; <code>d</code> » exclut tout couple où l’une des composantes vaut <code>1</code> (car rien n’est &lt;1 dans <code>A</code>).
</div>

<hr class="spacer-md">

<!-- Q2 -->

<div class="box question">
<b>Q2.</b> Montrer que <code>(R.S)<sup>−1</sup> = S<sup>−1</sup>.R<sup>−1</sup></code>.
</div>

<div class="box answer">
<b>Preuve élément par élément.</b><br>
Soient <code>x ∈ X</code>, <code>z ∈ Z</code>. On a :<br>
<code>(x,z) ∈ (R.S)</code> ⇔ <code>∃y ∈ Y</code> tel que <code>(x,y) ∈ R</code> et <code>(y,z) ∈ S</code>.<br>
Donc <code>(z,x) ∈ (R.S)<sup>−1</sup></code> ⇔ <code>∃y ∈ Y</code> tel que <code>(z,y) ∈ S<sup>−1</sup></code> et <code>(y,x) ∈ R<sup>−1</sup></code><br>
⇔ <code>(z,x) ∈ S<sup>−1</sup>.R<sup>−1</sup></code>. D’où l’égalité des deux relations.
</div>

<div class="box explain">
<b>Idée.</b> « Inverser » une composition revient à inverser l’ordre des facteurs et à prendre l’inverse de chacun.
</div>

<hr class="spacer-md">

<!-- Q3 -->

<div class="box question">
<b>Q3.</b> Pour <code>R = { (x,y) ∈ ℕ×ℕ | y = 2x }</code>, déterminer <code>R<sup>+</sup></code>.
</div>

<div class="box answer">
<b>Réponse.</b> Pour tout <code>k ≥ 1</code>, la puissance <code>R<sup>k</sup></code> est<br>
<code>R<sup>k</sup> = { (x,y) ∈ ℕ×ℕ | y = 2<sup>k</sup> x }</code>.<br>
Ainsi la fermeture transitive <b>sans</b> identité est<br>
<code>R<sup>+</sup> = ⋃<sub>k≥1</sub> R<sup>k</sup> = { (x,y) ∈ ℕ×ℕ | ∃k ≥ 1, y = 2<sup>k</sup> x }.</code>
</div>

<div class="box explain">
<b>Justification par récurrence.</b><br>
• <u>Initialisation</u> : <code>R = R<sup>1</sup></code> correspond à <code>y = 2x</code> (<code>2<sup>1</sup></code>).<br>
• <u>Hérédité</u> : si <code>R<sup>k</sup> = { (x,y) | y = 2<sup>k</sup> x }</code>, alors <code>R<sup>k+1</sup> = R<sup>k</sup>.R</code> donne <code>y = 2·(2<sup>k</sup>x) = 2<sup>k+1</sup>x</code>.<br>
Donc <code>R<sup>+</sup></code> est bien l’ensemble de tous les doublements itérés au moins une fois.
</div>



### TD1 — Exercice 6 : Composition et implications ensemblistes des propriétés des relations

<small>Énoncé exact — « Soit <code>R</code> une relation sur <code>E</code>. Montrer que … » (7 points ci-dessous). </small>

<div class="box question">
<b>1)</b> <code>R</code> est réflexive ⇔ <code>Id<sub>E</sub> ⊆ R</code>
</div>
<div class="box answer">
<b>(⇒)</b> Réflexive ⇒ pour tout <code>x∈E</code>, <code>(x,x)∈R</code>. Or <code>Id<sub>E</sub>={ (x,x) | x∈E }</code>, donc <code>Id<sub>E</sub>⊆R</code>.<br>
<b>(⇐)</b> Si <code>Id<sub>E</sub>⊆R</code>, alors pour tout <code>x</code>, <code>(x,x)∈Id<sub>E</sub>⊆R</code> : <code>R</code> est réflexive.
</div>
<div class="box explain">
Idée : « réflexive » signifie « toutes les boucles <code>(x,x)</code> sont dans <code>R</code> ». C’est exactement <code>Id<sub>E</sub> ⊆ R</code>.
</div>

<div class="box question">
<b>2)</b> <code>R</code> est symétrique ⇔ <code>R = R<sup>−1</sup></code>
</div>
<div class="box answer">
<b>(⇒)</b> Si <code>R</code> est symétrique et <code>(x,y)∈R</code>, alors <code>(y,x)∈R</code>, donc <code>(x,y)∈R<sup>−1</sup></code>. Ainsi <code>R⊆R<sup>−1</sup></code>. Par le même raisonnement à l’envers, <code>R<sup>−1</sup>⊆R</code>. Donc <code>R=R<sup>−1</sup></code>.<br>
<b>(⇐)</b> Si <code>R=R<sup>−1</sup></code> et <code>(x,y)∈R</code>, alors <code>(x,y)∈R<sup>−1</sup></code> donc <code>(y,x)∈R</code> : symétrie.
</div>
<div class="box explain">
« Être égal à son inverse » est la version ensembliste de « si <code>xRy</code> alors <code>yRx</code> ».
</div>

<div class="box question">
<b>3)</b> <code>R</code> est antisymétrique ⇔ <code>R ∩ R<sup>−1</sup> ⊆ Id<sub>E</sub></code>
</div>
<div class="box answer">
<b>(⇒)</b> Antisymétrie : si <code>(x,y)∈R</code> et <code>(y,x)∈R</code> alors <code>x=y</code>. Donc tout élément de <code>R∩R<sup>−1</sup></code> est de la forme <code>(x,x)</code> : inclus dans <code>Id<sub>E</sub></code>. <br>
<b>(⇐)</b> Si <code>R∩R<sup>−1</sup>⊆Id<sub>E</sub></code> et <code>(x,y),(y,x)∈R</code>, alors <code>(x,y)∈R∩R<sup>−1</sup></code>, donc <code>(x,y)=(x,x)</code> ⇒ <code>x=y</code> : antisymétrie.
</div>
<div class="box explain">
Le croisement <code>R∩R<sup>−1</sup></code> capture toutes les « arêtes bidirectionnelles » ; l’antisymétrie impose qu’elles soient des boucles.
</div>

<div class="box question">
<b>4)</b> <code>R</code> est transitive ⇔ <code>R.R ⊆ R</code>
</div>
<div class="box answer">
<b>(⇒)</b> Transitivité : <code>(x,y)∈R</code> et <code>(y,z)∈R</code> ⇒ <code>(x,z)∈R</code>. Par définition de la composition, <code>(x,z)∈R.R</code> implique alors <code>(x,z)∈R</code>. Donc <code>R.R⊆R</code>.<br>
<b>(⇐)</b> Si <code>R.R⊆R</code>, toute chaîne <code>(x,y),(y,z)∈R</code> donne <code>(x,z)∈R.R⊆R</code> : transitivité.
</div>
<div class="box explain">
Lire <code>R.R</code> comme « un pas de <code>R</code> puis encore un pas de <code>R</code> ». La condition dit : « deux pas restent dans <code>R</code> ».
</div>

<div class="box question">
<b>5)</b> Si <code>R</code> est réflexive, alors <code>R ⊆ R.R</code> et <code>R.R</code> est réflexive
</div>
<div class="box answer">
• <u>Inclusion</u> <code>R ⊆ R.R</code> : pour <code>(x,y)∈R</code>, comme <code>(y,y)∈R</code> (réflexivité), on a <code>(x,y)∈R.R</code> (témoins : <code>y</code>).<br>
• <u>Réflexivité de</u> <code>R.R</code> : pour tout <code>x</code>, comme <code>(x,x)∈R</code>, on peut composer <code>(x,x)</code> avec lui-même et obtenir <code>(x,x)∈R.R</code>.
</div>
<div class="box explain">
Astuce : la réflexivité fournit toujours un « point de collage » <code>y</code> pour réaliser la composition.
</div>

<div class="box question">
<b>6)</b> Si <code>R</code> est symétrique, alors <code>R<sup>−1</sup>.R = R.R<sup>−1</sup></code>
</div>
<div class="box answer">
Si <code>R</code> est symétrique, <code>R = R<sup>−1</sup></code>. Alors <code>R<sup>−1</sup>.R = R.R</code> et <code>R.R<sup>−1</sup> = R.R</code>, donc les deux sont égales.
</div>
<div class="box explain">
On remplace simplement <code>R<sup>−1</sup></code> par <code>R</code> de part et d’autre.
</div>

<div class="box question">
<b>7)</b> Si <code>R</code> est transitive, alors <code>R.R</code> est transitive
</div>
<div class="box answer">
On veut <code>(R.R).(R.R) ⊆ R.R</code>. Par associativité : <code>(R.R).(R.R) = R.(R.R).R</code>. Or <code>R</code> transitive ⇒ <code>R.R ⊆ R</code>, donc<br>
<code>R.(R.R).R ⊆ R.R.R</code> puis encore <code>R.R ⊆ R</code> donne <code>R.R.R ⊆ R.R</code>. Ainsi <code>R.R</code> est transitive.
</div>
<div class="box explain">
Chaîne de trois pas : « (2 pas) ⊆ 1 pas » appliqué deux fois ramène « 4 pas » dans « 2 pas ».
</div>


### TD1 — Exercice 7 : Relation d’équivalence sur les couples d’entiers

<small>Énoncé exact — « On considère l’ensemble ℕ × (ℕ \ {0}) … (a, b)R(c, d) ssi ad = bc. Démontrer que R est une relation d’équivalence. » </small>

<div class="box question">
<b>Exercice 7 — Relation d’équivalence sur les couples d’entiers</b><br>
On considère l’ensemble <code>ℕ × (ℕ \ {0})</code>, c’est-à-dire l’ensemble des couples d’entiers naturels dont le deuxième élément est non nul. Soit <code>R</code> définie sur cet ensemble par :<br>
<code>(a, b) R (c, d)</code> ssi <code>a d = b c</code>.<br>
Démontrer que <code>R</code> est une relation d’équivalence.
</div>

<div class="box answer">
<b>But.</b> Montrer successivement que <code>R</code> est <u>réflexive</u>, <u>symétrique</u> et <u>transitive</u>.
<hr class="spacer-sm">

<b>1) Réflexivité.</b> Pour tout <code>(a,b)</code> avec <code>b ≠ 0</code>, on a<br>
    <code>a·b = b·a</code> (commutativité du produit).<br>
Donc <code>(a,b) R (a,b)</code>. <i>R est réflexive.</i>

<hr class="spacer-sm">

<b>2) Symétrie.</b> Supposons <code>(a,b) R (c,d)</code>. Par définition, <code>a d = b c</code>. Par commutativité, cela équivaut à <code>c b = d a</code>, donc <code>(c,d) R (a,b)</code>. <i>R est symétrique.</i>

<hr class="spacer-sm">

<b>3) Transitivité (détaillée, pas à pas).</b><br>
Hypothèses : <code>(a,b) R (c,d)</code> et <code>(c,d) R (e,f)</code> avec <code>b,d,f ≠ 0</code>.<br>
Cela signifie :

<pre><code>(i)   a d = b c
(ii)  c f = d e
</code></pre>

Objectif : montrer <code>(a,b) R (e,f)</code>, c.-à-d. <code>a f = b e</code>.<br><br>
Étapes :

<ol>
  <li>Multipliez (i) par <code>f</code> (autorisé car <code>f ≠ 0</code>) : <code>a d f = b c f</code>.</li>
  <li>Dans le membre droit, remplacez <code>c f</code> par <code>d e</code> grâce à (ii) : <code>b c f = b (d e) = b d e</code>.</li>
  <li>On obtient donc <code>a d f = b d e</code>.</li>
  <li>Comme <code>d ≠ 0</code>, on peut simplifier par <code>d</code> (dans ℕ) : <code>a f = b e</code>.</li>
</ol>
Conclusion : <code>(a,b) R (e,f)</code>. <i>R est transitive.</i>

<hr class="spacer-sm">

<b>Conclusion.</b> <code>R</code> est réflexive, symétrique et transitive : c’est bien une <u>relation d’équivalence</u> sur <code>ℕ × (ℕ \ {0})</code>.

</div>

<div class="box explain">
<b>Intuition & exemples.</b><br>
• La condition <code>a d = b c</code> est exactement l’égalité des « fractions » <code>a/b</code> et <code>c/d</code> (avec dénominateurs non nuls).<br>
• Exemples :<br>
&nbsp;&nbsp;— <code>(1,2) R (2,4)</code> car <code>1·4 = 2·2 = 4</code> (donc <code>1/2 = 2/4</code>).<br>
&nbsp;&nbsp;— <code>(0,3) R (0,7)</code> car <code>0·7 = 3·0 = 0</code> : toutes les paires <code>(0,b)</code> sont équivalentes entre elles.<br>
• Les classes d’équivalence correspondent aux rationnels (positifs et 0) représentés par les couples <code>(a,b)</code> avec <code>b ≠ 0</code>.  
</div>




### TD1 — Exercice 8 : Partition engendrée par une relation d’équivalence

<small>Énoncé exact — « Soit <code>R</code> une relation d’équivalence dans <code>A</code> et soit <code>[a]</code> la classe d’équivalence de <code>a ∈ A</code>. Montrer que : (1) pour chaque <code>a ∈ A</code>, <code>a ∈ [a]</code> ; (2) <code>[a] = [b]</code> ssi <code>(a,b) ∈ R</code> ; (3) si <code>[a] ≠ [b]</code> alors <code>[a]</code> et <code>[b]</code> sont disjointes ; (4) l’ensemble des classes d’équivalence forme une partition de <code>A</code>. » </small>

<div class="box question">
<b>But.</b> Établir pas à pas les quatre propriétés ci-dessus à partir des axiomes d’une relation d’équivalence (réflexive, symétrique, transitive).
</div>

<div class="box answer">
<b>(1) Pour chaque <code>a ∈ A</code>, <code>a ∈ [a]</code></b><br>
Par définition, <code>[a] = { x ∈ A | (a,x) ∈ R }</code>. La réflexivité donne <code>(a,a) ∈ R</code>, donc <code>a ∈ [a]</code>. ✔️
</div>
<div class="box explain">
<b>Étape clé :</b> « équivalence ⇒ réflexive ». On n’utilise que la définition de <code>[a]</code> et la réflexivité.
</div>

<div class="box answer">
<b>(2) <code>[a] = [b]</code> ssi <code>(a,b) ∈ R</code></b><br>
<u>Sens « ⇒ »</u> : si <code>[a] = [b]</code>, alors comme <code>a ∈ [a]</code> (par (1)), on a <code>a ∈ [b]</code>, donc <code>(b,a) ∈ R</code>. Par symétrie, <code>(a,b) ∈ R</code>.<br>
<u>Sens « ⇐ »</u> : si <code>(a,b) ∈ R</code>, montrons <code>[a] ⊆ [b]</code> et <code>[b] ⊆ [a]</code>.  
• Soit <code>x ∈ [a]</code>, donc <code>(a,x) ∈ R</code>. De <code>(a,b) ∈ R</code> et symétrie/transitivité, on obtient <code>(b,x) ∈ R</code>, donc <code>x ∈ [b]</code>. Ainsi <code>[a] ⊆ [b]</code>.  
• Même raisonnement en échangeant <code>a</code>/<code>b</code> : <code>[b] ⊆ [a]</code>. Donc <code>[a] = [b]</code>. ✔️
</div>
<div class="box explain">
<b>Étapes clés :</b> (i) inclusion élément par élément ; (ii) usage de symétrie + transitivité pour « transporter » la relation de <code>a</code> vers <code>b</code>.
</div>

<div class="box answer">
<b>(3) Si <code>[a] ≠ [b]</code> alors <code>[a] ∩ [b] = ∅</code></b><br>
Par contraposée : supposons <code>[a] ∩ [b] ≠ ∅</code>. Alors il existe <code>x</code> tel que <code>(a,x) ∈ R</code> et <code>(b,x) ∈ R</code>.  
Par symétrie <code>(x,b) ∈ R</code>, puis par transitivité avec <code>(a,x) ∈ R</code> on obtient <code>(a,b) ∈ R</code>.  
Par (2) cela force <code>[a] = [b]</code>, contradiction. Donc l’intersection est vide. ✔️
</div>
<div class="box explain">
<b>Étapes clés :</b> point commun ⇒ chaînes <code>a ~ x</code> et <code>x ~ b</code> ⇒ <code>a ~ b</code> ⇒ égalité des classes (par (2)).
</div>

<div class="box answer">
<b>(4) Les classes d’équivalence forment une partition de <code>A</code></b><br>
Une partition exige : (i) non-vacuité de chaque bloc ; (ii) recouvrement ; (iii) disjonction deux à deux.<br>
• <u>Non-vacuité</u> : chaque <code>[a]</code> contient <code>a</code> par (1).  
• <u>Recouvrement</u> : pour tout <code>a ∈ A</code>, on a <code>a ∈ [a]</code>, donc <code>A = ⋃_{a∈A} [a]</code>.  
• <u>Disjonction</u> : par (3), deux classes distinctes sont disjointes.  
Donc <code>⟨[a]⟩_{a∈A}</code> est bien une partition de <code>A</code>. ✔️
</div>
<div class="box explain">
<b>Idée globale :</b> les classes sont des « paquets » d’éléments indiscernables à l’équivalence ; tout élément va exactement dans un paquet, et deux paquets sont soit identiques, soit sans recouvrement. 
</div>

<div class="box answer">
<b>Mini-exemple (≡ mod 3 sur ℕ)</b><br>
• <code>R</code> : <code>m R n</code> ssi <code>m ≡ n (mod 3)</code>.  
• Classes : <code>[0] = {0,3,6,…}</code>, <code>[1] = {1,4,7,…}</code>, <code>[2] = {2,5,8,…}</code>.  
(1) <code>4 ∈ [1]</code> car <code>4 ≡ 1</code>.  
(2) <code>[4] = [1]</code> car <code>4 ≡ 1</code>.  
(3) <code>[1] ∩ [2] = ∅</code>.  
(4) <code>{[0],[1],[2]}</code> partitionne ℕ (chaque entier tombe dans exactement une des trois classes).
</div>


### TD1 — Exercice 9 : Applications injectives, surjectives, bijectives — exemples

<small>Énoncé exact (copié du TD) :<br>

1. « Trouver un exemple d’application qui n’est ni injective, ni surjective. »<br>
2. « Les applications suivantes sont-elles injectives ? surjectives ? bijectives ? »
   (a) <code>f₁: ℕ → ℕ</code>, <code>f₁(x)=3x+1</code> et <code>f₂: ℚ → ℚ</code>, <code>f₂(x)=3x+1</code>
   (b) <code>f: ℕ → {0,1,2}</code>, <code>f(x)=x mod 3</code>
   (c) <code>f: ℕ² → ℕ</code>, <code>f(x,y)=x+y</code>
   (d) <code>f: ℕ → ℕ</code>, <code>f(n)=</code> <i>n+1 si n pair</i>, <i>n−1 si n impair</i>
   (e) <code>f: A^{*} → A^{*}</code>, <code>f(u)=u·b</code> avec <code>A={a,b}</code>
3. « Combien d’applications de <code>{a,b,c}</code> vers <code>{1,2}</code> ? Combien injectives / surjectives / bijectives ? » </small>

<div class="box question"><b>1) Un exemple qui n’est ni injectif ni surjectif</b></div>
<div class="box answer">
Exemple clair : <code>g: ℕ → ℕ</code> définie par <code>g(n)=0</code> pour tout <code>n</code>.<br>
• <b>Pas injective</b> : <code>g(0)=g(1)=0</code> alors que <code>0≠1</code>.<br>
• <b>Pas surjective</b> : il n’existe pas d’antécédent de <code>1,2,3,…</code>
</div>
<div class="box explain">
Astuce : une fonction <i>constante</i> vers un ensemble de taille ≥2 n’est ni injective ni surjective.
</div>

<hr>

<div class="box question"><b>2a) <code>f₁(x)=3x+1</code> sur ℕ &nbsp;/&nbsp; <code>f₂(x)=3x+1</code> sur ℚ</b></div>
<div class="box answer">
• <b><code>f₁: ℕ→ℕ</code></b> : <u>injective</u> (si <code>3x₁+1=3x₂+1</code> alors <code>x₁=x₂</code>) ; <u>non surjective</u> (l’image est l’ensemble des entiers <code>≡1 (mod 3)</code> : on n’atteint ni <code>0</code> ni <code>2 (mod 3)</code>). ⇒ <b>pas bijective</b>.<br>
• <b><code>f₂: ℚ→ℚ</code></b> : <u>injective</u> (même calcul) ; <u>surjective</u> : pour tout <code>y∈ℚ</code>, prendre <code>x=(y−1)/3 ∈ ℚ</code>. ⇒ <b>bijective</b>.
</div>
<div class="box explain">
Sur ℚ, l’affine <code>x↦3x+1</code> admet l’inverse <code>y↦(y−1)/3</code> ; sur ℕ, l’arithmétique mod 3 empêche la surjectivité. 
</div>

<hr>

<div class="box question"><b>2b) <code>f(x)=x mod 3</code> de ℕ vers <code>{0,1,2}</code></b></div>
<div class="box answer">
<u>Surjective</u> (on obtient 0, 1, 2 avec <code>x=0,1,2</code>, puis périodicité). <u>Non injective</u> (ex. <code>f(0)=f(3)=0</code>). ⇒ <b>pas bijective</b>.
</div>
<div class="box explain">
Chaque résidu modulo 3 a une infinité d’antécédents → collisions.
</div>

<hr>

<div class="box question"><b>2c) <code>f(x,y)=x+y</code> de ℕ² vers ℕ</b></div>
<div class="box answer">
<u>Surjective</u> : pour tout <code>n∈ℕ</code>, <code>f(n,0)=n</code>. <u>Non injective</u> : <code>f(1,2)=f(0,3)=3</code>. ⇒ <b>pas bijective</b>.
</div>
<div class="box explain">
Beaucoup de couples donnent la même somme → pas d’injectivité.
</div>

<hr>

<div class="box question"><b>2d) Pair/impair : <code>f(n)=n+1</code> si n pair, <code>f(n)=n−1</code> si n impair</b></div>
<div class="box answer">
<b>Bijective.</b> La fonction échange chaque paire voisine <code>(0,1), (2,3), (4,5), …</code><br>
• <u>Injective</u> : si <code>f(n₁)=f(n₂)</code>, alors <code>n₁</code> et <code>n₂</code> sont le même voisin dans leur paire ⇒ <code>n₁=n₂</code>.<br>
• <u>Surjective</u> : pour tout <code>k</code>, un antécédent existe (son voisin) : si <code>k</code> est pair, <code>f(k+1)=k</code> ; s’il est impair, <code>f(k−1)=k</code>.
</div>
<div class="box explain">
C’est une <i>involution</i> : <code>f(f(n))=n</code> ; toute involution sur un ensemble est bijective.
</div>

<hr>

<div class="box question"><b>2e) Mots : <code>f(u)=u·b</code> sur <code>A^{*}</code> avec <code>A={a,b}</code></b></div>
<div class="box answer">
<u>Injective</u> : si <code>u·b=v·b</code> alors <code>u=v</code> (on « enlève » le dernier <code>b</code>). <u>Non surjective</u> : aucun mot finissant par <code>a</code> n’est image. ⇒ <b>pas bijective</b>.
</div>
<div class="box explain">
« Ajouter un <code>b</code> à droite » code chaque mot de façon unique, mais ne couvre pas tout <code>A^{*}</code>.
</div>

<hr>

<div class="box question"><b>3) Combien d’applications <code>{a,b,c} → {1,2}</code> ? Injectives ? Surjectives ? Bijectives ?</b></div>
<div class="box answer">
• <b>Total</b> : chaque élément du domaine choisit 1 ou 2 ⇒ <code>2³ = 8</code>.<br>
• <b>Injectives</b> : <b>0</b> (impossible d’injecter 3 éléments distincts dans 2 valeurs).<br>
• <b>Surjectives</b> : <code>8 − 2 = 6</code> (on retire les deux fonctions constantes vers 1 et vers 2).<br>
• <b>Bijectives</b> : <b>0</b> (cardinaux différents).
</div>
<div class="box explain">
Comptage standard sur ensembles finis ; l’énoncé exact figure au TD.
</div>


<div class="box question">
<b>Exercice 10.</b><br>
Soient <b>A</b> et <b>B</b> deux ensembles <b>disjoints</b> (c.-à-d. <b>A ∩ B = ∅</b>). On définit
<pre><code>f : P(A) × P(B) → P(A ∪ B)
f(X, Y) = X ∪ Y
</code></pre>
Montrer que <b>f est une bijection</b>.
</div>

<div class="box answer">
<b>Idée générale.</b> Comme A et B ne se recouvrent pas, tout élément de A vient forcément de la partie dans A, et tout élément de B vient forcément de la partie dans B. Donc on peut toujours "retrouver" X et Y à partir de X ∪ Y. C’est ça qui donne l’injectivité. Pour la surjectivité, on coupe n’importe quel sous-ensemble de A ∪ B en “partie dans A” + “partie dans B”.
</div>

<div class="box explain">
<b>1) f est bien définie</b><br>
Si <code>X ⊆ A</code> et <code>Y ⊆ B</code>, alors <code>X ∪ Y ⊆ A ∪ B</code>. Donc <code>f(X,Y) ∈ P(A ∪ B)</code>.<br><br>

<b>2) f est injective</b><br>
Supposons

<pre><code>f(X₁, Y₁) = f(X₂, Y₂)
⇔ X₁ ∪ Y₁ = X₂ ∪ Y₂
</code></pre>

On intersecte avec A :

<pre><code>(X₁ ∪ Y₁) ∩ A = X₁
(X₂ ∪ Y₂) ∩ A = X₂
</code></pre>

(car <code>Y₁ ⊆ B</code> et <code>Y₂ ⊆ B</code>, donc rien dans A). Comme les deux unions sont égales, leurs intersections avec A sont égales, donc

<pre><code>X₁ = X₂
</code></pre>

Même chose avec B :

<pre><code>(X₁ ∪ Y₁) ∩ B = Y₁
(X₂ ∪ Y₂) ∩ B = Y₂
⇒ Y₁ = Y₂
</code></pre>

Donc

<pre><code>(X₁, Y₁) = (X₂, Y₂)
</code></pre>

⇒ f est <b>injective</b>.<br><br>

<b>3) f est surjective</b><br>
Soit <code>Z ⊆ A ∪ B</code>. On pose

<pre><code>X = Z ∩ A   (⊆ A)
Y = Z ∩ B   (⊆ B)
</code></pre>

Alors

<pre><code>X ∪ Y = (Z ∩ A) ∪ (Z ∩ B) = Z ∩ (A ∪ B) = Z
</code></pre>

Donc pour tout Z, on trouve (X,Y) tel que f(X,Y)=Z. f est donc <b>surjective</b>.<br><br>

<b>4) Conclusion</b><br>
f est à la fois injective et surjective ⇒ <b>f est une bijection</b>.<br>
⚠️ L’hypothèse <b>A ∩ B = ∅</b> est essentielle.

</div>

<br>

<div class="box question">
<b>Exercice 11.</b><br>
On définit, sur une famille d’ensembles, la relation suivante :
<pre><code>X ~ Y   ⇔   il existe une bijection de X vers Y
</code></pre>
1. Montrer que ~ est une <b>relation d’équivalence</b>. <br>
2. Décrire les <b>classes d’équivalence</b> dans le cas des ensembles finis.
</div>

<div class="box answer">
<b>Idée générale.</b> « Être en bijection » veut dire « avoir la même taille ». Une relation d’équivalence, c’est : chacun est en bijection avec lui-même (réflexive), si X est en bijection avec Y alors Y est en bijection avec X (symétrique), et si X est en bijection avec Y et Y avec Z, alors X est en bijection avec Z (transitive).
</div>

<div class="box explain">
<b>1) Réflexive</b><br>
Pour tout ensemble X, l’application identité
<pre><code>idₓ : X → X,   x ↦ x
</code></pre>
est une bijection. Donc <code>X ~ X</code>. ⇒ ~ est <b>réflexive</b>.<br><br>

<b>2) Symétrique</b><br>
Supposons <code>X ~ Y</code>. Alors il existe une bijection <code>f : X → Y</code>. Une bijection a un inverse <code>f⁻¹ : Y → X</code> qui est aussi une bijection. Donc <code>Y ~ X</code>. ⇒ ~ est <b>symétrique</b>.<br><br>

<b>3) Transitive</b><br>
Supposons

<pre><code>X ~ Y   et   Y ~ Z
</code></pre>

Donc il existe une bijection <code>f : X → Y</code> et une bijection <code>g : Y → Z</code>. La composée

<pre><code>g ∘ f : X → Z
</code></pre>

est encore une bijection. Donc <code>X ~ Z</code>. ⇒ ~ est <b>transitive</b>.<br><br>

<b>Conclusion partie 1</b><br>
La relation « il existe une bijection entre X et Y » est bien une <b>relation d’équivalence</b>.<br><br>

<b>4) Classes d’équivalence (ensembles finis)</b><br>
Si X et Y sont <b>finis</b>, alors :

<pre><code>X ~ Y   ⇔   |X| = |Y|
</code></pre>

Donc une classe d’équivalence est : « tous les ensembles qui ont le <b>même nombre d’éléments</b> ». <br>
Exemples :<br>
• classe de cardinal 0 : {∅}<br>
• classe de cardinal 1 : tous les ensembles à 1 élément : {1}, {a}, {●}, …<br>
• classe de cardinal 2 : {1,2}, {a,b}, {x,y}, …<br>
• etc.<br><br>

<b>Conclusion partie 2</b><br>
Dans le cas fini, les classes d’équivalence de ~ sont exactement les « niveaux de cardinal ». Autrement dit : <b>“être en bijection” = “avoir le même cardinal”</b>.

</div>





<div class="box explain">
  <strong>Explications générales sur le Thème 3 : Fonctions booléennes et formes normales</strong><br><br>

<strong>1. Objet du thème</strong><br>
Le thème 3 a pour but de montrer comment réécrire des formules logiques (avec ET, OU, NON) sous une forme standardisée. Les deux formes standard utilisées sont :<br>
• la <strong>forme normale disjonctive</strong> (FND) : une somme (OU) de produits (ET) de littéraux ;<br>
• la <strong>forme normale conjonctive</strong> (FNC) : un produit (ET) de sommes (OU) de littéraux.<br>
L’intérêt de ces formes est qu’elles permettent :<br>
– de comparer deux formules et de montrer qu’elles sont équivalentes ;<br>
– de passer facilement d’une table de vérité à une expression et inversement ;<br>
– d’exprimer simplement les cas “toujours vrai” (valide) et “toujours faux” (insatisfiable) ;<br>
– de préparer les méthodes de décision (SAT) qui exigent une formule en FNC.<br><br>

<strong>2. Vocabulaire utilisé dans le TD</strong><br>
• <em>Variable booléenne</em> : prend 0 ou 1.<br>
• <em>Littéral</em> : une variable ou sa négation (ex. <code>x</code>, <code>¬x</code>).<br>
• <em>Produit</em> : un ET de littéraux (ex. <code>x·y</code>, <code>¬x·y·z</code>).<br>
• <em>Somme</em> : un OU de littéraux (ex. <code>x+y</code>, <code>¬x+y+z</code>).<br>
• <em>Forme normale disjonctive (FND)</em> : expression de la forme

  <pre>(produit) + (produit) + (produit) + ...</pre>

c’est-à-dire “OU de ET”.<br>
• <em>Forme normale conjonctive (FNC)</em> : expression de la forme

  <pre>(somme) · (somme) · (somme) · ...</pre>

c’est-à-dire “ET de OU”.<br>
• <em>Forme canonique</em> (pas toujours exigée dans le TD) : chaque produit (en FND) ou chaque somme (en FNC) contient toutes les variables, soit en positif soit en négatif.<br><br>

<strong>3. Reconnaître FND / FNC (partie du TD où il faut dire “laquelle est en forme normale…”)</strong><br>
Pour reconnaître une FND :<br>

1. regarder l’opérateur principal (celui tout en haut). Si c’est un <code>+</code> → candidat FND ;<br>
2. vérifier que chaque terme séparé par ce <code>+</code> est un produit de littéraux uniquement (par ex. <code>x·y</code>, <code>¬x·z</code>, <code>x·¬y·z</code>) ;<br>
3. si c’est le cas pour tous les termes → c’est une FND.<br><br>
   Pour reconnaître une FNC :<br>
4. regarder l’opérateur principal. Si c’est un <code>·</code> → candidat FNC ;<br>
5. vérifier que chaque facteur séparé par ce <code>·</code> est une somme de littéraux uniquement (par ex. <code>x+y</code>, <code>x+¬y+z</code>) ;<br>
6. si c’est le cas pour tous les facteurs → c’est une FNC.<br><br>
   Cas particuliers importants :<br>
   • un seul littéral (<code>x</code>), une seule somme (<code>x+y</code>) ou un seul produit (<code>x·y</code>) sont acceptés comme formes normales ;<br>
   • dès qu’un morceau contient déjà un mélange non distribué (par ex. <code>y + y·z</code> ou <code>z·(y+z)</code>), l’expression n’est pas en forme normale telle qu’elle est écrite ;<br>
   • il est possible qu’une même petite expression soit à la fois FND et FNC (ex. <code>x</code>, <code>x+y</code>, <code>x·y</code>).<br><br>

<strong>4. Cas particuliers demandés dans le TD : formules valides et formules insatisfiables</strong><br>
Le TD demande d’écrire des exemples de formules :

  <ul>
    <li><strong>valides</strong> (toujours vraies, pour toutes les valeurs des variables),</li>
    <li><strong>insatisfiables</strong> (jamais vraies, pour aucune valeur des variables),</li>
    <li>et de les donner en FND et en FNC.</li>
  </ul>
  Les modèles à connaître sont les suivants :<br><br>
  • Formule toujours vraie en FNC (cas le plus simple) :
  <pre>(x + ¬x) · (y + ¬y) · (z + ¬z) · ...</pre>
  Chaque parenthèse est vraie quelle que soit la valeur de la variable, donc tout le produit est vrai. On peut en écrire autant qu’il y a de variables. Ce modèle répond à la question du TD “combien de sommes sont nécessaires ?” : on en met une par variable.<br><br>
  • Formule toujours vraie en FND (forme canonique) : on doit écrire un produit pour chaque ligne de la table de vérité. Pour 3 variables, il y a 8 lignes, donc :
  <pre>
(x · y · z)
+ (x · y · ¬z)
+ (x · ¬y · z)
+ (x · ¬y · ¬z)
+ (¬x · y · z)
+ (¬x · y · ¬z)
+ (¬x · ¬y · z)
+ (¬x · ¬y · ¬z)
  </pre>
  Ici, tous les cas possibles sont couverts → la formule est vraie partout.<br><br>
  • Formule jamais vraie (insatisfiable) en FNC :
  <pre>(x) · (¬x)</pre>
  Ce seul produit suffit à rendre la formule fausse. Si le TD impose “au moins 3 clauses”, on peut ajouter une tautologie pour faire nombre :
  <pre>(x) · (¬x) · (y + ¬y)</pre>
  • Formule jamais vraie en FND :
  <pre>(x · ¬x) + (y · ¬y) + (z · ¬z)</pre>
  Chaque produit vaut 0 → la somme vaut 0.<br><br>
  Ces 4 écritures sont les réponses-types attendues quand le TD parle de “valide” / “insatisfiable” sans table de vérité.
  <br><br>

<strong>5. Passage table de vérité → FND / FNC (partie du TD avec XOR et avec données de tableau)</strong><br>
Le TD montre la méthode classique pour reconstruire une formule à partir d’une table :<br><br>
• <u>Table → FND</u> :<br>

1. repérer les lignes où la fonction vaut 1 ;<br>
2. pour chaque ligne, écrire un produit qui fixe toutes les variables (si la variable vaut 1 dans la ligne → on l’écrit positive ; si elle vaut 0 → on l’écrit niée) ;<br>
3. faire le OU (+) de tous ces produits.<br>
   Exemple : XOR sur 2 variables est vrai sur (0,1) et (1,0) → donc

  <pre>(¬x · y) + (x · ¬y)</pre>

est la FND du XOR.<br><br>
• <u>Table → FNC</u> :<br>

1. repérer les lignes où la fonction vaut 0 ;<br>
2. pour chaque ligne, écrire une somme qui exclut cette ligne (si la variable vaut 0 → on l’écrit positive dans la somme, si elle vaut 1 → on l’écrit niée) ;<br>
3. faire le produit (·) de toutes ces sommes.<br>
   Pour XOR, la fonction vaut 0 sur (0,0) et (1,1) → donc

  <pre>(x + y) · (¬x + ¬y)</pre>

est la FNC du XOR.<br><br>
Cette partie du TD sert à montrer qu’à partir d’une table <em>on obtient toujours</em> une FND et une FNC. <br><br>

<strong>6. Passage forme normale → table de vérité (partie du TD où la formule est déjà sous forme normale)</strong><br>
Quand la formule est déjà donnée sous la forme :

  <pre>f(x,y,z) = x·y + y·z + x·y·z</pre>

ou

  <pre>g(x,y,z) = (x + y) · (y + z) · (x + y + z)</pre>

la méthode attendue est systématique :<br>

1. écrire les 8 lignes possibles de (x,y,z) ;<br>
2. calculer séparément chaque sous-terme (ex. x·y, y·z, x·y·z) ;<br>
3. faire le OU ou le ET final ;<br>
4. recopier le résultat dans la colonne finale.<br>
   Cette méthode est volontairement mécanique : elle évite les erreurs de tête et montre bien comment la forme normale “décrit” la fonction. <br><br>

<strong>7. Transformation d’une formule en FND / FNC (partie finale du TD)</strong><br>
Le TD demande de prendre une formule qui n’est pas écrite en forme normale, par exemple :

  <pre>F = (A ∧ (B ∨ C)) ∨ (¬A ∧ ¬B)</pre>

et de la mettre en FND puis en FNC sans faire de table.
Pour cela, deux règles de distributivité sont utilisées :

  <pre>
x·(y+z) = x·y + x·z          (pour aller vers FND : ET distribué sur OU)
x + (y·z) = (x+y)·(x+z)      (pour aller vers FNC : OU distribué sur ET)
  </pre>

Application vers la FND :<br>

  <pre>
F = (A ∧ (B ∨ C)) ∨ (¬A ∧ ¬B)
  = A·(B + C) + ¬A·¬B
  = (A·B) + (A·C) + (¬A·¬B)
  </pre>

On obtient une somme de produits → FND.<br><br>
Application vers la FNC (même formule) :<br>

  <pre>
F = (A ∧ (B ∨ C)) ∨ (¬A ∧ ¬B)
  = (A ∨ (¬A ∧ ¬B)) ∧ ((B ∨ C) ∨ (¬A ∧ ¬B))
  = (A ∨ ¬B) ∧ (¬A ∨ B ∨ C)
  </pre>

On obtient un produit de sommes → FNC.<br>
Ce passage montre ce qui est attendu dans la dernière partie du TD : savoir distribuer dans le bon sens jusqu’à obtenir la forme imposée. <br><br>

<strong>8. Lois utilisées dans toutes les solutions</strong><br>
Les mêmes lois reviennent tout le temps et doivent être utilisées sans justification longue :<br>
• <code>x + ¬x = 1</code> (tautologie)<br>
• <code>x · ¬x = 0</code> (contradiction)<br>
• <code>x + x·y = x</code> (absorption)<br>
• <code>x·(x + y) = x</code> (absorption)<br>
• <code>x·(y+z) = x·y + x·z</code> (vers FND)<br>
• <code>x + y·z = (x+y)·(x+z)</code> (vers FNC)<br>
Ces lois suffisent pour refaire toutes les étapes des exercices 9 à 13. <br><br>

<strong>9. Résumé opérationnel (ce qu’il faut savoir faire pour réussir le TD)</strong><br>

1. Savoir dire si une expression donnée est FND, FNC ou ni l’une ni l’autre (en regardant l’opérateur principal et la forme de chaque morceau).<br>
2. Savoir écrire une formule toujours vraie / jamais vraie en FND et en FNC en utilisant les modèles ci-dessus.<br>
3. Savoir construire une FND ou une FNC à partir d’une table de vérité (lignes = 1 → FND, lignes = 0 → FNC).<br>
4. Savoir faire la transformation d’une formule mélangée en FND ou en FNC à l’aide des deux règles de distributivité.<br>
5. Savoir simplifier une formule un peu longue avec les lois d’absorption et de complément.<br><br>

<strong>Conclusion</strong><br>
Ce thème est un thème de “mise en forme”. L’objectif n’est pas de trouver des raisonnements compliqués mais de savoir réécrire correctement. La solution d’un exercice de ce TD doit en général montrer : la forme visée (FND ou FNC), la ou les règles de distributivité utilisées, puis éventuellement une petite simplification avec les lois de base. En maîtrisant ces étapes, toutes les questions du TD sont accessibles.

</div>





### TD1 — Exercice 12 : Applications entre ensembles finis

<small>(d’après le TD — sans les marques bizarres) </small>

<div class="box question">
<b>Énoncé.</b><br>
Soient <b>E</b> et <b>F</b> deux ensembles finis non vides, avec  
• |E| = p  
• |F| = n  
1. Montrer que le nombre d’applications de E vers F est <code>n<sup>p</sup></code>.<br>
2. Combien d’applications de <code>{0,1}</code> vers <code>{0,1}</code> peut-on construire ? Montrer que, pour toute telle application f, on a :  
<code>f(f(f(x))) = f(x)</code>.
</div>

<div class="box answer">
<b>1. Compter les applications E → F.</b><br>
Unefonction <code>f : E → F</code> doit choisir, pour <b>chaque</b> élément de E, <b>une</b> valeur dans F.<br><br>
• E a <b>p</b> éléments → on doit faire <b>p choix</b>.<br>
• Pour chaque élément de E, on a <b>n</b> possibilités (les n éléments de F).<br>
• Les choix sont <b>indépendants</b> → on multiplie :  
<code>nombre de fonctions = n × n × … × n</code> (p fois)  
donc  
<pre><code>nombre d'applications E → F = n<sup>p</sup>.
</code></pre>
</div>

<div class="box explain">
<b>Pourquoi on multiplie ?</b><br>
Parce qu’une fonction est un <i>p-uplet</i> de choix : (image du 1er élément, image du 2e, …, image du p-ième).  
Un p-uplet avec n choix à chaque place → <code>n<sup>p</sup></code> possibilités.  
<b>Exemple rapide :</b> si E = {a,b,c} (donc p = 3) et F = {1,2} (donc n = 2), alors il y a <code>2<sup>3</sup> = 8</code> fonctions possibles (on le reverra à l’ex. 3 du TD aussi).
</div>

<br>

<div class="box answer">
<b>2. Cas particulier E = F = {0,1}.</b><br>
Ici p = 2 et n = 2 ⇒ nombre de fonctions = <code>2<sup>2</sup> = 4</code>.<br>
On peut donc <b>toutes</b> les lister.
</div>

<div class="box explain">
<b>On note f(0) et f(1).</b>  
Chaque valeur peut être 0 ou 1. Donc :  
1. f₁ : f(0)=0, f(1)=0  → fonction <b>constante 0</b>  
2. f₂ : f(0)=0, f(1)=1  → fonction <b>identité</b>  
3. f₃ : f(0)=1, f(1)=0  → fonction <b>négation</b>  
4. f₄ : f(0)=1, f(1)=1  → fonction <b>constante 1</b>  
On va vérifier sur ces 4 cas que <code>f(f(f(x))) = f(x)</code>.
</div>

<div class="box answer">
<b>Vérification 1 — f constante 0</b><br>
• f(x)=0 pour tout x.  
• f(f(x)) = f(0) = 0  
• f(f(f(x))) = f(0) = 0  
⇒ f(f(f(x))) = 0 = f(x).
</div>

<div class="box answer">
<b>Vérification 2 — f identité</b><br>
• f(x) = x  
• f(f(x)) = f(x) = x  
• f(f(f(x))) = f(x) = x  
⇒ f(f(f(x))) = f(x).
</div>

<div class="box answer">
<b>Vérification 3 — f négation</b> (f(0)=1, f(1)=0)<br>
Regardons les 2 valeurs :<br>
• x = 0 :  
&nbsp;&nbsp;f(0)=1  
&nbsp;&nbsp;f(f(0)) = f(1) = 0  
&nbsp;&nbsp;f(f(f(0))) = f(0) = 1  
&nbsp;&nbsp;⇒ f(f(f(0))) = 1 = f(0) ✅<br>
• x = 1 :  
&nbsp;&nbsp;f(1)=0  
&nbsp;&nbsp;f(f(1)) = f(0) = 1  
&nbsp;&nbsp;f(f(f(1))) = f(1) = 0  
&nbsp;&nbsp;⇒ f(f(f(1))) = 0 = f(1) ✅  
Donc pour la négation aussi, l’égalité tient.
</div>

<div class="box answer">
<b>Vérification 4 — f constante 1</b><br>
• f(x)=1 pour tout x  
• f(f(x)) = f(1)=1  
• f(f(f(x))) = f(1)=1  
⇒ f(f(f(x))) = 1 = f(x).
</div>

<div class="box explain">
<b>Conclusion du 2)</b>  
Comme on a listé <b>toutes</b> les fonctions possibles de {0,1} vers {0,1} et que, pour chacune, on a bien <code>f(f(f(x))) = f(x)</code>, l’énoncé est démontré.  
👉 L’idée cachée : quand le domaine est tout petit (2 points), on peut faire une preuve « par cas ».
</div>

---

### TD1 — Exercice 13 : Principe des tiroirs (pigeonhole)

<small>(version du TD) </small>

<div class="box question">
<b>Énoncé.</b><br>
On veut montrer :  
1. Si <code>n &lt; m</code>, il n’existe pas d’<b>injection</b> d’un ensemble à <code>m</code> éléments dans un ensemble à <code>n</code> éléments.  
2. (Forme “tiroirs”) : si on veut placer <code>m</code> chemises dans <code>n</code> tiroirs avec <code>m &gt; n</code>, alors <b>au moins un tiroir</b> contient <b>plusieurs</b> chemises.  
3. Plus précisément : montrer qu’un tiroir contiendra au moins un nombre entier  
<code>p ≥ m / n</code> chemises (en fait c’est <code>p ≥ ⌈m/n⌉</code>).
</div>

<div class="box answer">
<b>1. Pas d’injection si m &gt; n.</b><br>
Une injection de <code>M</code> (|M| = m) vers <code>N</code> (|N| = n) doit associer à <b>chaque</b> élément de M un élément <b>différent</b> de N.  
Mais N n’a que <code>n</code> places.  
Si <code>m &gt; n</code>, on a plus d’éléments à placer que de places disponibles → on est obligé de “réutiliser” une place → donc ce ne sera pas injectif.  
Donc : <b>si m &gt; n, aucune injection M → N n’existe.</b>
</div>

<div class="box explain">
C’est exactement le cœur du <b>principe des tiroirs</b> :  
• « objets » = chemises = m  
• « tiroirs » = boîtes = n  
• si objets &gt; tiroirs → au moins 1 tiroir aura ≥ 2 objets.
</div>

<br>

<div class="box answer">
<b>2. Forme imagée “chemises/tiroirs”.</b><br>
On met m chemises dans n tiroirs avec m &gt; n.  
S’il n’y avait <b>pas</b> de tiroir avec ≥2 chemises, alors <b>chaque</b> tiroir aurait ≤1 chemise → au total ≤ n chemises.  
Mais on en a m &gt; n → contradiction.  
Donc il existe au moins 1 tiroir avec ≥2 chemises.
</div>

<div class="box explain">
C’est juste la <b>contraposée</b> :  
si « tous ≤1 » ⇒ « total ≤ n ».  
Or on a « total &gt; n » ⇒ pas « tous ≤1 ».
</div>

<br>

<div class="box answer">
<b>3. Version plus précise.</b><br>
On veut montrer : au moins un tiroir contient  
<pre><code>p ≥ m / n
</code></pre>
chemises (en réalité l’entier <code>⌈m/n⌉</code>).  
<b>Idée :</b> on répartit le plus “équitablement” possible :  
• si on divise m par n, on obtient <code>m/n</code> → c’est la moyenne.  
• Si tout le monde avait ≤ ⌊m/n⌋ chemises, on aurait ≤ n × ⌊m/n⌋ &lt; m (quand m n’est pas multiple de n).  
Donc au moins un tiroir doit passer au-dessus de la moyenne → ≥ ⌈m/n⌉.
</div>

<div class="box explain">
<b>Démonstration rapide.</b><br>
Écrivons <code>m = q·n + r</code> avec <code>0 ≤ r &lt; n</code> (division euclidienne).  
• On peut mettre <code>q</code> chemises dans chaque tiroir → ça fait <code>q·n</code> chemises.  
• Il reste <code>r</code> chemises à placer.  
• On est obligé d’en mettre 1 de plus dans <code>r</code> tiroirs.  
Donc :  
• <code>r</code> tiroirs contiennent <code>q+1</code> chemises  
• <code>n−r</code> tiroirs contiennent <code>q</code> chemises  
Comme <code>q = ⌊m/n⌋</code> et <code>q+1 = ⌈m/n⌉</code>, on a bien : <b>au moins un tiroir contient ⌈m/n⌉ chemises.</b>
</div>

---



### TD1 — Exercice 14 : Applications injectives

<div class="box question">
<b>Énoncé.</b><br>
Soit <b>f : A → B</b> une application. Montrer que :
<br><br>
<center><b>f est injective ⇔ pour tous sous-ensembles X, Y ⊆ A, on a</b>  
<code>f(X ∩ Y) = f(X) ∩ f(Y)</code>.</center>
</div>

<div class="box answer">
On montre les deux sens.
<br><br>
<b>(⇒) Supposons f injective.</b><br>
• On a toujours, sans aucune hypothèse :  
<code>f(X ∩ Y) ⊆ f(X) ∩ f(Y)</code>  
car si <code>z ∈ X ∩ Y</code> alors <code>z ∈ X</code> et <code>z ∈ Y</code>, donc <code>f(z) ∈ f(X)</code> et <code>f(z) ∈ f(Y)</code>.<br><br>
• Il reste à montrer l’autre inclusion <code>f(X) ∩ f(Y) ⊆ f(X ∩ Y)</code>.<br>
  Prenons <code>b ∈ f(X) ∩ f(Y)</code>.  
  Alors il existe <code>x ∈ X</code> et <code>y ∈ Y</code> tels que
  <pre><code>f(x) = b  et  f(y) = b.
  </code></pre>
  Comme f est <b>injective</b>, de <code>f(x) = f(y)</code> on déduit <code>x = y</code>.  
  Donc cet élément commun <code>x = y</code> appartient à la fois à X et à Y, donc <code>x ∈ X ∩ Y</code>.  
  Alors <code>b = f(x) ∈ f(X ∩ Y)</code>.  
  Donc <code>f(X) ∩ f(Y) ⊆ f(X ∩ Y)</code>.<br><br>
Donc, si f est injective, on a bien  
<code>f(X ∩ Y) = f(X) ∩ f(Y)</code> pour tous X, Y.
<br><br>
<b>(⇐) Réciproquement, supposons :</b><br>
pour tous X, Y ⊆ A,  
<pre><code>f(X ∩ Y) = f(X) ∩ f(Y)   (★)
</code></pre>
Montrons que f est injective.
<br><br>
Prenons <code>a₁, a₂ ∈ A</code> tels que
<pre><code>f(a₁) = f(a₂).
</code></pre>
On veut prouver <code>a₁ = a₂</code>.  
Considérons les deux singletons :
<pre><code>X = {a₁}   et   Y = {a₂}.
</code></pre>
• Si <code>a₁ ≠ a₂</code>, alors <code>X ∩ Y = ∅</code> donc <code>f(X ∩ Y) = f(∅) = ∅</code>.<br>
• Mais <code>f(X) = {f(a₁)}</code> et <code>f(Y) = {f(a₂)}</code>.  
  Or on a supposé <code>f(a₁) = f(a₂)</code>, donc
  <pre><code>f(X) ∩ f(Y) = {f(a₁)} ∩ {f(a₂)} = {f(a₁)} ≠ ∅.
  </code></pre>
• On obtient alors
  <pre><code>f(X ∩ Y) = ∅    mais    f(X) ∩ f(Y) = {f(a₁)}.
  </code></pre>
  Ce qui contredit (★).  
Donc le cas <code>a₁ ≠ a₂</code> est impossible, il faut donc que <code>a₁ = a₂</code>.  
Donc f est <b>injective</b>.
</div>

<div class="box explain">
<b>À retenir.</b><br>
• L’inclusion <code>f(X ∩ Y) ⊆ f(X) ∩ f(Y)</code> est <u>toujours vraie</u>, même sans injectivité.<br>
• L’égalité complète <code>f(X ∩ Y) = f(X) ∩ f(Y)</code> pour <u>tous</u> X, Y est une façon de <b>caractériser l’injectivité</b>.<br><br>
<b>Mini-exemple.</b><br>
– f : ℕ → ℕ, f(n) = 2n (injection) → elle « ne colle » jamais deux éléments distincts ⇒ l’image de l’intersection reste l’intersection des images.<br>
– f : ℕ → ℕ, f(n) = 0 (pas injective) → si X={1}, Y={2} :  
&nbsp;&nbsp;X ∩ Y = ∅ ⇒ f(X ∩ Y)=∅  
&nbsp;&nbsp;f(X)={0}, f(Y)={0} ⇒ f(X) ∩ f(Y)={0} ≠ ∅  
⇒ l’égalité échoue.
</div>

<br><br>

---

### TD1 — Exercice 15 : Involutions

<div class="box question">
<b>Énoncé.</b><br>
On dit qu’une application <code>f : E → E</code> est une <b>involution</b> si, pour tout <code>x ∈ E</code>,
<pre><code>f(f(x)) = x.
</code></pre>
Montrer que si f est une involution alors f est <b>bijective</b>.
</div>

<div class="box answer">
On doit montrer : « involution ⇒ injective » et « involution ⇒ surjective ».
<br><br>
<b>1) f est injective.</b><br>
Supposons <code>f(x) = f(y)</code> pour deux éléments <code>x, y ∈ E</code>.  
Appliquons f des deux côtés :
<pre><code>f(f(x)) = f(f(y)).
</code></pre>
Comme f est une involution, <code>f(f(x)) = x</code> et <code>f(f(y)) = y</code>.  
Donc on obtient :
<pre><code>x = y.
</code></pre>
Donc <b>f est injective</b>.
<br><br>
<b>2) f est surjective.</b><br>
Soit <code>y ∈ E</code> quelconque.  
On veut trouver un <code>x ∈ E</code> tel que <code>f(x) = y</code>.  
Prenons simplement <code>x = f(y)</code> (on a le droit, car f va de E vers E).  
Alors
<pre><code>f(x) = f(f(y)) = y
</code></pre>
(définition d’une involution).  
Donc pour tout y, il existe un x avec f(x)=y ⇒ <b>f est surjective</b>.
<br><br>
<b>Conclusion.</b> f est injective et surjective ⇒ f est <b>bijective</b>.
</div>

<div class="box explain">
<b>Idée très simple.</b><br>
Une involution « revient en arrière » tout de suite : appliquer f deux fois te rend ton point de départ.  
Si tu peux toujours revenir en arrière, alors :  
• personne n’a été “fusionné” avec quelqu’un d’autre ⇒ injectif ;  
• tout le monde a un “prédécesseur” (son image par f) ⇒ surjectif.<br><br>

<b>Exemples d’involutions.</b><br>

1. Sur ℤ : <code>f(n) = −n</code>. Alors <code>f(f(n)) = −(−n) = n</code> ⇒ involution ⇒ bijection ℤ → ℤ.<br>
2. Sur un ensemble pair : <code>E = {1,2,3,4}</code>,
   définir <code>f(1)=2</code>, <code>f(2)=1</code>, <code>f(3)=4</code>, <code>f(4)=3</code>.
   Alors appliquer f deux fois renvoie le point de départ. On voit bien que c’est une permutation par « échanges de paires ».
3. Sur un espace de mots : « renverser deux fois » est une involution : <code>rev(rev(u)) = u</code>.

</div>

---



### TD1 — Exercice 16 : Composition d’applications

<div class="box question">
On se donne deux applications :  
• <b>f : A → B</b>  
• <b>g : B → C</b>  
et leur composition <b>g ∘ f : A → C</b> (définie par <code>(g ∘ f)(x) = g(f(x))</code>).<br><br>
<b>1.</b> Montrer que si <b>g ∘ f</b> est injective, alors <b>f</b> est injective.<br>
<b>2.</b> Montrer que si <b>g ∘ f</b> est surjective, alors <b>g</b> est surjective. :contentReference[oaicite:0]{index=0}
</div>

<div class="box answer">
<b>1. (g ∘ f) injective ⇒ f injective</b><br>
On suppose :  
<pre><code>pour tous x, y ∈ A,  (g ∘ f)(x) = (g ∘ f)(y)  ⇒  x = y.
</code></pre>
On veut montrer :  
<pre><code>pour tous x, y ∈ A,  f(x) = f(y)  ⇒  x = y.
</code></pre>
Soient donc <code>x, y ∈ A</code> tels que <code>f(x) = f(y)</code>.  
Alors en appliquant g aux deux côtés :
<pre><code>g(f(x)) = g(f(y))
⇔ (g ∘ f)(x) = (g ∘ f)(y)
</code></pre>
Or <code>g ∘ f</code> est injective, donc de cette égalité on déduit <code>x = y</code>.  
Donc <b>f est injective</b>.
</div>

<div class="box explain">
<b>Idée :</b> si la composition distingue déjà les éléments (injective), alors la première flèche <b>f</b> ne peut pas “coller” deux éléments différents, sinon la composition les confondrait.<br><br>
<b>Attention :</b> la réciproque est fausse : « f injective ⇒ g ∘ f injective » n’est pas toujours vrai (si g “écrase” les valeurs).
</div>

<br>

<div class="box answer">
<b>2. (g ∘ f) surjective ⇒ g surjective</b><br>
On suppose :  
<pre><code>pour tout z ∈ C, il existe x ∈ A tel que (g ∘ f)(x) = z.
</code></pre>
On veut montrer :  
<pre><code>pour tout z ∈ C, il existe b ∈ B tel que g(b) = z.
</code></pre>
Soit <code>z ∈ C</code>.  
Comme <code>g ∘ f</code> est surjective, il existe <code>x ∈ A</code> tel que
<pre><code>g(f(x)) = z.
</code></pre>
Posons alors <code>b = f(x)</code>. On a bien <code>b ∈ B</code> (puisque f va dans B) et
<pre><code>g(b) = g(f(x)) = z.
</code></pre>
Donc pour tout <code>z ∈ C</code> on a trouvé un <code>b ∈ B</code> avec <code>g(b)=z</code>.  
Donc <b>g est surjective</b>.
</div>

<div class="box explain">
<b>Idée :</b> si la composition “arrive” sur tout C, c’est que la deuxième appli <b>g</b> sait déjà atteindre tout C.  
<b>Mais</b> la réciproque est fausse : « g surjective ⇒ g ∘ f surjective » n’est pas vraie si f ne couvre pas tout B.
</div>

<br><hr><br>

### TD1 — Exercice 17 : Image et image réciproque

<div class="box question">
On rappelle que, pour une application <b>f : E → F</b>, pour une partie <b>A ⊆ E</b> et une partie <b>B ⊆ F</b>, on définit :  
• <b>image directe</b> :  
<pre><code>f(A) = { y ∈ F | ∃x ∈ A, y = f(x) }
</code></pre>
• <b>image réciproque</b> :  
<pre><code>f⁻¹(B) = { x ∈ E | f(x) ∈ B }
</code></pre>
Montrer que :  
<b>1.</b> pour toute partie A de E, on a <code>A ⊆ f⁻¹(f(A))</code> ;  
<b>2.</b> si f est injective, alors pour toute partie A de E, on a <code>f⁻¹(f(A)) ⊆ A</code> ;  
<b>3.</b> pour <code>E = {1,2,3}</code>, <code>F = {a,b}</code>, <code>f(1)=f(2)=a</code>, <code>f(3)=b</code>, <code>A = {1}</code>, calculer <code>f(A)</code> puis <code>f⁻¹(f(A))</code>. :contentReference[oaicite:1]{index=1}
</div>

<div class="box answer">
<b>1. Montrer A ⊆ f⁻¹(f(A))</b><br>
Soit <code>x ∈ A</code>.  
Alors <code>f(x) ∈ f(A)</code> par définition de l’image directe (puisque x est dans A).  
Donc, par définition de l’image réciproque,
<pre><code>x ∈ f⁻¹(f(A))
</code></pre>
puisque « f(x) est dans f(A) ».  
Donc tout élément de A est aussi dans <code>f⁻¹(f(A))</code> ⇒  
<pre><code>A ⊆ f⁻¹(f(A)).
</code></pre>
</div>

<div class="box explain">
<b>Lecture.</b> « Je pars de A, j’applique f → j’obtiens f(A). Puis je reviens en arrière avec f⁻¹. »  
Comme f⁻¹ de f(A) ramène <i>tous</i> les éléments qui avaient une image dans f(A), au minimum ça ramène les éléments de A.
</div>

<br>

<div class="box answer">
<b>2. Si f est injective, alors f⁻¹(f(A)) ⊆ A</b><br>
On suppose maintenant : <b>f est injective</b>.<br>
Soit <code>x ∈ f⁻¹(f(A))</code>.  
Cela veut dire :  
<pre><code>f(x) ∈ f(A)
</code></pre>
donc il existe <code>a ∈ A</code> tel que
<pre><code>f(x) = f(a).
</code></pre>
Or f est injective, donc de <code>f(x) = f(a)</code> on déduit <code>x = a</code>.  
Mais comme <code>a ∈ A</code>, on obtient <code>x ∈ A</code>.  
Donc tout élément de <code>f⁻¹(f(A))</code> appartient à A, d’où :
<pre><code>f⁻¹(f(A)) ⊆ A.
</code></pre>
</div>

<div class="box explain">
<b>Conclusion des 1. et 2.</b><br>
• Toujours : <code>A ⊆ f⁻¹(f(A))</code>  
• Si en plus f est injective : <code>f⁻¹(f(A)) ⊆ A</code>  
Donc, si f est injective :  
<pre><code>f⁻¹(f(A)) = A.
</code></pre>
Autrement dit : « revenir en arrière » après l’image ne rajoute rien si f ne mélange pas les éléments.
</div>

<br>

<div class="box answer">
<b>3. Exemple concret</b><br>
On a :
<pre><code>E = {1, 2, 3}
F = {a, b}
f(1) = a
f(2) = a
f(3) = b
A = {1}
</code></pre>
<b>Calcul de f(A).</b>  
A = {1} donc
<pre><code>f(A) = { f(1) } = { a }.
</code></pre>
<b>Calcul de f⁻¹(f(A)).</b>  
Ici f(A) = {a}.  
Donc
<pre><code>f⁻¹({a}) = { x ∈ E | f(x) ∈ {a} }.
</code></pre>
On regarde les valeurs de f :  
• f(1) = a → 1 est dedans  
• f(2) = a → 2 est dedans  
• f(3) = b → 3 n’est pas dedans  
Donc
<pre><code>f⁻¹(f(A)) = f⁻¹({a}) = {1, 2}.
</code></pre>
</div>

<div class="box explain">
<b>Ce que montre l’exemple.</b><br>
• On était parti de A = {1}.  
• On a fait f(A) = {a}.  
• Quand on revient en arrière, on obtient {1, 2}.  
<b>Pourquoi on a “gagné” le 2 ?</b> Parce que f n’est <u>pas</u> injective : 1 et 2 ont la même image (a). Donc quand on dit “ramène-moi tout ce qui envoie vers {a}”, on ramène 1 <b>et</b> 2.  
Donc ici :
<pre><code>A = {1}  ⊂  f⁻¹(f(A)) = {1, 2}.
</code></pre>
Ça illustre bien la partie 1.
</div>


### TD1 — Exercice 18 : Bijection réciproque

<div class="box question">
Soit <b>f : E → F</b> une application.
<ol>
  <li>Si <b>E ≠ ∅</b>, montrer que <b>f est injective</b> ⇔ il existe une application <b>r : F → E</b> telle que <code>r ∘ f = id<sub>E</sub></code>. On appelle <b>r</b> une <i>rétraction</i> de f.</li>
  <li>Montrer que <b>f est surjective</b> ⇔ il existe une application <b>s : F → E</b> telle que <code>f ∘ s = id<sub>F</sub></code>. On appelle <b>s</b> une <i>section</i> de f.</li>
  <li>Montrer que <b>f est bijective</b> ⇔ il existe une application <b>f<sup>−1</sup> : F → E</b> telle que <code>f ∘ f<sup>−1</sup> = id<sub>F</sub></code> et <code>f<sup>−1</sup> ∘ f = id<sub>E</sub></code>. :contentReference[oaicite:0]{index=0}
</div>

<div class="box answer">
<b>1) Cas “inverse à gauche” = rétraction.</b><br>
<b>(⇒)</b> Suppose que f est <b>injective</b> et que E ≠ ∅. On veut construire <b>r : F → E</b> telle que <code>r ∘ f = id<sub>E</sub></code>.
</div>

<div class="box explain">
Idée : comme f est injective, <u>deux éléments différents de E n’ont pas la même image</u>. Donc, pour chaque <code>y ∈ f(E)</code>, il existe un <u>unique</u> <code>x ∈ E</code> tel que <code>f(x) = y</code>.  
On définit alors :  
• pour <code>y ∈ f(E)</code> : <code>r(y) =</code> l’unique <code>x</code> tel que <code>f(x) = y</code> ;  
• pour <code>y ∉ f(E)</code> : comme <code>E ≠ ∅</code>, on choisit un élément fixe <code>e₀ ∈ E</code> et on pose <code>r(y) = e₀</code>.  
Ainsi, <code>r</code> est bien définie sur <b>tout</b> F.  
Alors, pour tout <code>x ∈ E</code> :
<pre><code>(r ∘ f)(x) = r(f(x)) = x
</code></pre>
puisque pour <code>y = f(x)</code>, on a défini <code>r(y)</code> comme l’unique antécédent de y.  
Donc <code>r ∘ f = id<sub>E</sub></code>.  
<br>
<b>(⇐)</b> Réciproque : suppose qu’il existe <code>r : F → E</code> telle que <code>r ∘ f = id<sub>E</sub></code>.  
Prenons <code>x, x' ∈ E</code> tels que <code>f(x) = f(x')</code>.  
En appliquant r :
<pre><code>r(f(x)) = r(f(x'))
⇔ (r ∘ f)(x) = (r ∘ f)(x')
⇔ id<sub>E</sub>(x) = id<sub>E</sub>(x')
⇔ x = x'
</code></pre>
Donc f est injective. ✅  
<b>Donc :</b> <code>f injective ⇔ ∃ r : F → E, r ∘ f = id<sub>E</sub></code>.
</div>

<div class="box answer">
<b>2) Cas “inverse à droite” = section.</b><br>
<b>(⇒)</b> Suppose que f est <b>surjective</b>.  
Comme f est surjective, pour tout <code>y ∈ F</code>, il existe au moins un <code>x ∈ E</code> tel que <code>f(x) = y</code>.  
On définit alors <code>s : F → E</code> en “choisissant” un tel antécédent :  
<pre><code>pour y ∈ F, choisir x ∈ E tel que f(x) = y et poser s(y) = x.
</code></pre>
Alors pour tout <code>y ∈ F</code> :
<pre><code>(f ∘ s)(y) = f(s(y)) = y
</code></pre>
donc <code>f ∘ s = id<sub>F</sub></code>.
</div>

<div class="box explain">
<b>(⇐)</b> Réciproque : si on a une application <code>s : F → E</code> telle que <code>f ∘ s = id<sub>F</sub></code>, alors pour tout <code>y ∈ F</code>,  
<pre><code>f(s(y)) = y
</code></pre>
donc chaque <code>y</code> a bien au moins un antécédent <code>s(y)</code>.  
Donc f est surjective. ✅  
<b>Donc :</b> <code>f surjective ⇔ ∃ s : F → E, f ∘ s = id<sub>F</sub></code>.
</div>

<div class="box answer">
<b>3) Cas bijectif.</b><br>
Si f est bijective, alors elle est injective <b>et</b> surjective.  
D’après 1) il existe une rétraction <code>r</code> telle que <code>r ∘ f = id<sub>E</sub></code>,  
et d’après 2) il existe une section <code>s</code> telle que <code>f ∘ s = id<sub>F</sub></code>.  
Comme f est bijective, ces deux inverses coïncident et on les note <code>f<sup>−1</sup></code>, avec :
<pre><code>f ∘ f<sup>−1</sup> = id<sub>F</sub>   et   f<sup>−1</sup> ∘ f = id<sub>E</sub>.
</code></pre>
</div>

<div class="box explain">
<b>Résumé.</b><br>
• injective ⇔ “inverse à gauche” existe (rétraction), E non vide ;<br>
• surjective ⇔ “inverse à droite” existe (section) ;<br>
• bijective ⇔ les deux → vrai inverse.  
C’est exactement la théorie des inverses <b>à gauche</b> / <b>à droite</b> en algèbre.
</div>

<br><hr><br>

### TD1 — Exercice 19 : Ensembles dénombrables

<div class="box question">
On dit qu’un ensemble <b>E</b> est <b>dénombrable</b> s’il existe une bijection entre E et ℕ.  
Montrer que <b>ℕ² = ℕ × ℕ</b> est dénombrable.  
(On pourra montrer que les deux fonctions suivantes sont des bijections de ℕ² dans ℕ :  
<code>f(x, y) = y + (0 + 1 + 2 + … + (x + y))</code> et <code>g(x, y) = 2<sup>y</sup>(2x + 1) − 1</code>.) :contentReference[oaicite:1]{index=1}
</div>

<div class="box answer">
Il y a plusieurs façons de montrer que ℕ² est dénombrable. On va en donner <b>2</b> très classiques :
<ol>
  <li>le <b>parcours en diagonale</b> (méthode visuelle)</li>
  <li>une <b>vraie formule</b> qui code chaque couple (x, y) en un seul entier</li>
</ol>
</div>

<div class="box explain">
<b>1) Méthode en diagonale (Cantor).</b><br>
On range tous les couples (x, y) avec x, y ∈ ℕ dans un tableau :
<pre>
(0,0)  (0,1)  (0,2)  (0,3)  ...
(1,0)  (1,1)  (1,2)  (1,3)  ...
(2,0)  (2,1)  (2,2)  (2,3)  ...
...
</pre>
On parcourt ce tableau <b>par diagonales croissantes</b> :
<pre>
diag 0 : (0,0)
diag 1 : (0,1), (1,0)
diag 2 : (0,2), (1,1), (2,0)
diag 3 : (0,3), (1,2), (2,1), (3,0)
...
</pre>
Ainsi, on obtient une <b>liste infinie</b> qui contient chaque couple <b>une fois</b>.  
Donc on a bien une bijection « position dans la liste » ↔ « couple (x, y) ».  
Donc ℕ² est dénombrable.
</div>

<div class="box answer">
<b>2) Méthode par formule : première fonction proposée.</b><br>
On pose :
<pre><code>f(x, y) = y + (0 + 1 + 2 + … + (x + y)).
</code></pre>
Remarque :  
<code>0 + 1 + 2 + … + n = n(n + 1) / 2</code>.  
Ici <code>n = x + y</code>, donc :
<pre><code>f(x, y) = y + (x + y)(x + y + 1) / 2.
</code></pre>
C’est exactement la <b>numérotation de Cantor</b>.
</div>

<div class="box explain">
<b>Pourquoi ça marche ?</b><br>
• Pour un couple (x, y), on regarde d’abord la “diagonale” d’indice <code>k = x + y</code>.  
• Tous les couples dont la somme vaut k sont sur la même diagonale.  
• On compte combien il y a d’éléments <b>avant</b> cette diagonale : c’est <code>0 + 1 + … + (k − 1)</code> = <code>k(k−1)/2</code>.  
• Puis on avance de <code>y</code> cases dans la diagonale k (qui est ordonnée du haut vers le bas : (0,k), (1,k−1), …, (y, x)).  
• On obtient une <b>position unique</b> dans ℕ.  
On peut montrer que cette fonction est :  
• <b>injective</b> : deux couples distincts ont soit une somme différente, soit un y différent dans la même diagonale → donc deux valeurs différentes ;  
• <b>surjective</b> : tout entier n s’écrit de manière unique sous la forme <code>y + (k(k+1))/2</code> avec k = x + y, donc on peut remonter au couple (x, y).  
Donc c’est une bijection ℕ² → ℕ.
</div>

<div class="box answer">
<b>3) Deuxième fonction proposée.</b><br>
On pose :
<pre><code>g(x, y) = 2<sup>y</sup> · (2x + 1) − 1.
</code></pre>
Ici on utilise le fait que tout entier admet une <b>décomposition unique</b> en puissance de 2 × impair.
</div>

<div class="box explain">
<b>Idée de la preuve pour g.</b><br>
• Tout entier naturel m+1 s’écrit <b>de façon unique</b> sous la forme <code>2<sup>y</sup> · (2x + 1)</code>  
&nbsp;&nbsp;– <code>2<sup>y</sup></code> = la plus grande puissance de 2 qui divise m+1  
&nbsp;&nbsp;– <code>(2x + 1)</code> = la partie impaire (> 0)<br>
• Donc, si on définit <code>g(x, y) = 2<sup>y</sup>(2x + 1) − 1</code>, alors <code>g</code> est <b>injective</b> : deux couples (x, y) ≠ (x', y') donnent deux décompositions 2-adique différentes → donc deux entiers différents.  
• Et g est <b>surjective</b> sur ℕ : pour tout n ∈ ℕ, on regarde n+1, on le décompose en <code>2<sup>y</sup> · t</code> avec t impair, on écrit t = 2x+1, on retrouve (x, y).  
Donc g est une bijection ℕ² ↔ ℕ.
</div>

<div class="box explain">
<b>Conclusion.</b><br>
Comme on vient de construire (au moins) une bijection de ℕ × ℕ vers ℕ, on a montré que :
<pre><code>ℕ² est dénombrable.
</code></pre>
Et comme ℕ² et ℕ ont “le même nombre d’éléments” (au sens de la bijection), on pourra plus tard en déduire que <b>toute union dénombrable de dénombrables</b> est encore dénombrable.
</div>


### TD1 — Exercice 20 : Les rationnels sont dénombrables 

<div class="box question">
<b>Énoncé.</b><br>
Montrer que l’ensemble des nombres rationnels <b>ℚ</b> est dénombrable.
<br><br>
(On rappelle qu’un ensemble est <b>dénombrable</b> s’il existe une bijection entre cet ensemble et <b>ℕ</b>.)
</div>

<div class="box answer">
<b>Idée générale.</b><br>
On va écrire tout nombre rationnel sous la forme <code>p/q</code> avec <code>p ∈ ℤ</code> et <code>q ∈ ℕ*</code> (donc <code>q ≥ 1</code>), puis on va montrer que :
<ol>
  <li>pour un dénominateur fixé <code>q</code>, il n’y a qu’un ensemble dénombrable de rationnels,</li>
  <li>ℚ est une <b>union dénombrable</b> de <b>dénombrables</b>,</li>
  <li>donc ℚ est dénombrable.</li>
</ol>
</div>

<div class="box explain">
On découpe la preuve en petits morceaux très lisibles.
</div>

<br>

<div class="box question">
<b>1.</b> Comment écrire proprement les rationnels ?
</div>

<div class="box answer">
On peut écrire
<pre><code>ℚ = { p/q  |  p ∈ ℤ, q ∈ ℕ*, q ≥ 1 }.
</code></pre>
Autrement dit : on prend tous les entiers en numérateur, et tous les entiers positifs en dénominateur.
</div>

<div class="box explain">
• On impose <code>q ≥ 1</code> pour éviter de compter aussi <code>p/(-q)</code> et de faire le même rationnel deux fois.<br>
• Si on veut vraiment une vraie bijection, on pourra plus tard imposer la <b>forme irréductible</b> (p et q premiers entre eux) et le signe uniquement au numérateur. Mais pour montrer « dénombrable », ce n’est pas grave d’avoir quelques doublons : on sait enlever les doublons ensuite.
</div>

<br>

<div class="box question">
<b>2.</b> Pourquoi “pour un dénominateur fixé” c’est dénombrable ?
</div>

<div class="box answer">
Fixons un dénominateur <code>q</code> (par exemple <code>q = 5</code>).  
Considérons l’ensemble :
<pre><code>X<sub>q</sub> = { p/q | p ∈ ℤ }.
</code></pre>
L’application
<pre><code>ℤ → X<sub>q</sub>,   p ↦ p/q
</code></pre>
est <b>bijective</b> : à chaque entier p correspond exactement un rationnel p/q, et inversement on retrouve p en multipliant par q.  
Donc <code>X<sub>q</sub></code> a le même “nombre d’éléments” que ℤ, donc <b>X<sub>q</sub> est dénombrable</b>.
</div>

<div class="box explain">
<b>Exemples.</b><br>
• pour q = 1 : <code>X₁ = { …, -2/1, -1/1, 0/1, 1/1, 2/1, … } = ℤ</code><br>
• pour q = 2 : <code>X₂ = { …, -3/2, -2/2, -1/2, 0, 1/2, 2/2, 3/2, … }</code><br>
• pour q = 3 : <code>X₃ = { …, -4/3, -3/3, -2/3, -1/3, 0, 1/3, 2/3, 3/3, 4/3, … }</code><br>
Chaque ligne est comme ℤ → dénombrable.
</div>

<br>

<div class="box question">
<b>3.</b> Écrire ℚ comme union de ces ensembles.
</div>

<div class="box answer">
On a
<pre><code>ℚ = ⋃<sub>q=1</sub><sup>+∞</sup> X<sub>q</sub>
    = X<sub>1</sub> ∪ X<sub>2</sub> ∪ X<sub>3</sub> ∪ ...
</code></pre>
c’est-à-dire : « tous les rationnels, c’est ceux de dénominateur 1, plus ceux de dénominateur 2, plus ceux de dénominateur 3, etc. »
</div>

<div class="box explain">
<b>Important :</b> on a écrit ℚ comme <b>union dénombrable</b> (indexée par q ∈ ℕ*) d’ensembles eux-mêmes dénombrables (les X<sub>q</sub>).  
Or on sait (résultat standard de dénombrabilité) :  
<b>union dénombrable de dénombrables ⇒ dénombrable</b>.  
Donc ℚ est dénombrable.
</div>

<br>

<div class="box question">
<b>4.</b> Comment “voir” la numérotation des rationnels ?
</div>

<div class="box answer">
On peut les ranger en tableau (numérateur sur l’axe vertical, dénominateur sur l’axe horizontal) et faire une <b>diagonale</b>, exactement comme pour ℕ × ℕ :
</div>

<div class="box explain">
<pre>
           q = 1     q = 2      q = 3      q = 4     ...
p = 0 →    0/1       0/2        0/3        0/4
p = 1 →    1/1       1/2        1/3        1/4
p = 2 →    2/1       2/2        2/3        2/4
p = 3 →    3/1       3/2        3/3        3/4
...
</pre>
On parcourt par diagonales :  
• diag 0 : 0/1  
• diag 1 : 1/1, 0/2  
• diag 2 : 2/1, 1/2, 0/3  
• diag 3 : 3/1, 2/2, 1/3, 0/4  
…  
et on enlève les doublons (ex. 2/2 = 1/1, 3/3 = 1/1, 4/2 = 2/1, etc.).  
On obtient une <b>liste infinie sans oubli</b> → donc on peut numéroter les rationnels.
</div>

<br>

<div class="box question">
<b>5.</b> Et les rationnels négatifs ? Et 0 ?
</div>

<div class="box answer">
On peut d’abord énumérer les rationnels positifs (q ≥ 1, p ≥ 0), puis intercaler les négatifs.  
Exemple de début de liste :
<pre><code>0,
1, -1,
1/2, -1/2,
2, -2,
2/3, -2/3,
3, -3,
1/3, -1/3,
...
</code></pre>
Chaque rationnel finit par apparaître quelque part → toujours dénombrable.
</div>

<div class="box explain">
Le fait d’intercaler positif / négatif / zéro ne casse jamais la dénombrabilité : on ne fait que réordonner une liste déjà infinie.
</div>

<br>

<div class="box answer">
<b>Conclusion.</b><br>
On a écrit ℚ comme union de familles dénombrables indexées par ℕ. Donc ℚ est dénombrable.
</div>

<div class="box explain">
<b>Ce qu’il faut retenir pour l’examen :</b><br>
1. Tout rationnel s’écrit p/q avec p ∈ ℤ, q ∈ ℕ*.<br>
2. Pour q fixé : {p/q | p ∈ ℤ} est dénombrable.<br>
3. ℚ = ⋃<sub>q≥1</sub> {p/q | p ∈ ℤ}.<br>
4. Union dénombrable de dénombrables → dénombrable.<br>
<b>Donc : ℚ est dénombrable.</b>
</div>



### TD1 — Exercice 21 : Cantor

<div class="box question">
<b>Exercice 21 — (Théorème de Cantor)</b><br>
Montrer qu’il n’existe pas de bijection entre un ensemble <b>E</b> et l’ensemble de ses parties <b>℘(E)</b>. Autrement dit : pour tout ensemble E, on ne peut pas construire d’application <code>f : E → ℘(E)</code> qui soit bijective. :contentReference[oaicite:0]{index=0}
</div>

<div class="box answer">
<b>Idée du résultat.</b><br>
Cantor dit : « l’ensemble de <i>toutes</i> les parties de E est <u>toujours plus grand</u> que E lui-même ».  
Donc, même si E est infini, <b>℘(E)</b> est encore “plus infini” → aucune bijection possible.
</div>

<div class="box explain">
On va faire la preuve classique par <b>diagonalisation</b> (ou “argument du sous-ensemble manquant”).
</div>
<br>

<div class="box question">
<b>1. On suppose qu’il existe une bijection.</b><br>
Supposons, <u>par l’absurde</u>, qu’il existe une application <code>f : E → ℘(E)</code> qui soit <b>surjective</b> (et donc bijective).  
Donc : pour toute partie <code>A ⊆ E</code>, il existe au moins un <code>x ∈ E</code> tel que <code>f(x) = A</code>.
</div>

<div class="box answer">
On va fabriquer une partie spéciale de E qui <b>ne peut pas</b> être dans l’image de f.  
Si on y arrive, on aura une contradiction → donc f ne peut pas être surjective → donc pas de bijection.
</div>

<div class="box explain">
<b>Pourquoi on vise la surjectivité ?</b><br>
Parce qu’une bijection = injective + surjective.  
Si on montre qu’<b>aucune</b> application <code>E → ℘(E)</code> ne peut être <b>surjective</b>, alors aucune ne peut être bijective.
</div>
<br>

<div class="box question">
<b>2. On construit l’ensemble “diagonal”</b><br>
On définit un sous-ensemble de E, appelé souvent <b>D</b>, par :
<pre><code>D = { x ∈ E | x ∉ f(x) }.
</code></pre>
C’est l’ensemble de <i>tous</i> les éléments de E qui <u>ne sont pas</u> dans leur propre image.
</div>

<div class="box answer">
<b>Remarque importante :</b>  
• pour chaque <code>x ∈ E</code>, on regarde la partie <code>f(x)</code> (qui est une partie de E),  
• si <code>x</code> n’est pas dedans, on met <code>x</code> dans D,  
• si <code>x</code> est dedans, on ne met pas <code>x</code> dans D.  
Donc D est bien une partie de E.
</div>

<div class="box explain">
C’est exactement la même idée que Cantor pour les suites : “je fabrique un objet qui est différent de tous les objets listés, au moins sur 1 point”.
</div>
<br>

<div class="box question">
<b>3. D est-il dans l’image de f ?</b><br>
Comme on a supposé que f est surjective, <b>toute</b> partie de E doit apparaître comme <code>f(x)</code> pour un certain <code>x</code>.  
Donc en particulier, il doit exister <code>a ∈ E</code> tel que :
<pre><code>f(a) = D.
</code></pre>
On va montrer que c’est impossible.
</div>

<div class="box answer">
Regardons l’élément <code>a</code> lui-même. Deux cas sont possibles :
<ol>
  <li><b>Cas 1 :</b> <code>a ∈ D</code></li>
  <li><b>Cas 2 :</b> <code>a ∉ D</code></li>
</ol>
On va voir que dans les deux cas, on tombe sur une contradiction.
</div>

<div class="box explain">
C’est le cœur de la preuve : on fait un raisonnement “si oui → non, si non → oui”.
</div>
<br>

<div class="box question">
<b>Cas 1 :</b> supposons que <code>a ∈ D</code>.
</div>

<div class="box answer">
Si <code>a ∈ D</code>, alors par définition de D :
<pre><code>a ∈ D  ⇒  a ∉ f(a)
</code></pre>
Mais on a supposé <code>f(a) = D</code>, donc
<pre><code>a ∈ D  ⇒  a ∉ D
</code></pre>
<b>Contradiction.</b>
</div>

<div class="box explain">
Donc le cas “<code>a</code> est dedans” ne peut pas arriver.
</div>
<br>

<div class="box question">
<b>Cas 2 :</b> supposons que <code>a ∉ D</code>.
</div>

<div class="box answer">
Si <code>a ∉ D</code>, alors par définition de D :
<pre><code>a ∉ D  ⇒  a ∈ f(a)
</code></pre>
Mais <code>f(a) = D</code>, donc
<pre><code>a ∉ D  ⇒  a ∈ D
</code></pre>
<b>Encore contradiction.</b>
</div>

<div class="box explain">
Dans les deux cas on obtient “a est dans D” et “a n’est pas dans D” en même temps → impossible.
</div>
<br>

<div class="box answer">
<b>Conclusion.</b><br>
Notre hypothèse “il existe une surjection <code>f : E → ℘(E)</code>” mène à une contradiction.  
Donc <b>il n’existe pas</b> de surjection de E vers ℘(E).  
Et donc, a fortiori, <b>il n’existe pas de bijection</b> entre E et ℘(E).
</div>

<div class="box explain">
<b>Ce qu’il faut retenir.</b><br>
• Pour tout ensemble E : <code>|E| &lt; |℘(E)|</code> (cardinal strictement plus grand).  
• C’est vrai même si E est infini (par ex. E = ℕ).  
• C’est pourquoi on dit qu’il y a “plus” de parties de ℕ que d’entiers naturels.
</div>

<br>

<div class="box question">
<b>Exemples pour bien voir</b>
</div>

<div class="box answer">
<b>1) E = {1,2}.</b><br>
Alors <code>℘(E) = { ∅, {1}, {2}, {1,2} }</code>.  
Ici on voit bien qu’il y a 2 éléments dans E et 4 dans ℘(E). Impossible de faire une bijection 2 ↔ 4.
</div>

<div class="box answer">
<b>2) E = ℕ.</b><br>
On pourrait essayer de “lister” toutes les parties de ℕ (les sous-ensembles de nombres naturels). Cantor montre que <b>quelle que soit</b> la liste, on en fabrique toujours une nouvelle qui n’est pas dans la liste → donc pas de bijection.
</div>

<div class="box explain">
<b>Important pour toi :</b> tu peux réutiliser ce schéma de preuve pour plein d’autres questions d’“impossibilité de lister”.
</div>



### Exercice 22 — Relations d’équivalence, applications 

<div class="box question">
Soient <b>E</b> et <b>F</b> deux ensembles, et <b>f : E → F</b> une application.<br>
On définit la relation <b>R<sub>f</sub> ⊆ E × E</b> par :
<br><code>x R<sub>f</sub> y</code> ⇔ <code>f(x) = f(y)</code>.
<br><br>
1. Montrer que <b>R<sub>f</sub></b> est une relation d’équivalence.<br>
2. Donner la définition de la classe d’équivalence de <code>x</code> par la relation <b>R<sub>f</sub></b>.<br>
3. Pour tout <code>x, y ∈ E</code>, si <code>x ∈ [y]<sub>R<sub>f</sub></sub></code>, montrer que <code>[x]<sub>R<sub>f</sub></sub> = [y]<sub>R<sub>f</sub></sub></code>.<br>
On suppose maintenant que <b>f n’est ni injective ni surjective</b>.<br>
On définit <b>S : E → E / R<sub>f</sub></b> par <code>S(x) = [x]<sub>R<sub>f</sub></sub></code> (ensemble des classes).<br>
4. S est-elle injective ? surjective ? bijective ? Justifier.<br>
On définit ensuite une relation<br>
<code>ĝ ⊆ (E / R<sub>f</sub>) × F</code> par : <code>(X, y) ∈ ĝ</code> s’il existe <code>x ∈ X</code> tel que <code>f(x) = y</code>.<br>
5. Montrer que <code>ĝ</code> est en fait une <b>application</b> de <code>E / R<sub>f</sub></code> vers <code>F</code>.<br>
6. Cette application est-elle injective ? surjective ? bijective ? Justifier.
</div>

<br>

<div class="box answer">
<b>1. R<sub>f</sub> est une relation d’équivalence</b><br>
On doit montrer : réflexive, symétrique, transitive.
</div>

<div class="box explain">
<b>Réflexive.</b> Pour tout <code>x ∈ E</code>, on a toujours <code>f(x) = f(x)</code>. Donc <code>x R<sub>f</sub> x</code>. ✅<br><br>
<b>Symétrique.</b> Supposons <code>x R<sub>f</sub> y</code>. Par définition, <code>f(x) = f(y)</code>. Alors forcément <code>f(y) = f(x)</code>. Donc <code>y R<sub>f</sub> x</code>. ✅<br><br>
<b>Transitive.</b> Supposons <code>x R<sub>f</sub> y</code> et <code>y R<sub>f</sub> z</code>. Ça veut dire <code>f(x) = f(y)</code> et <code>f(y) = f(z)</code>. En enchaînant, <code>f(x) = f(z)</code>. Donc <code>x R<sub>f</sub> z</code>. ✅<br><br>
Comme les 3 propriétés sont vraies, <b>R<sub>f</sub> est bien une relation d’équivalence</b>.
</div>

<br>

<div class="box answer">
<b>2. Classe d’équivalence de x</b><br>
La classe d’équivalence de <code>x</code> pour cette relation est :
<pre><code>[x]<sub>R<sub>f</sub></sub> = { y ∈ E | f(y) = f(x) }.
</code></pre>
C’est “tous les éléments de E qui ont la <b>même image</b> que x par f”.
</div>

<div class="box explain">
Tu peux la lire comme : « je regroupe dans le même sac tous les éléments que f envoie au même endroit ».
</div>

<br>

<div class="box answer">
<b>3. Si x ∈ [y]<sub>R<sub>f</sub></sub>, alors [x]<sub>R<sub>f</sub></sub> = [y]<sub>R<sub>f</sub></sub></b><br>
Hypothèse : <code>x ∈ [y]</code>.  
Ça veut dire : <code>f(x) = f(y)</code>.  
Or :
<pre><code>[x] = { u ∈ E | f(u) = f(x) }
[y] = { u ∈ E | f(u) = f(y) }
</code></pre>
Mais <code>f(x) = f(y)</code>, donc ces deux ensembles sont :
<pre><code>[x] = { u | f(u) = f(x) } = { u | f(u) = f(y) } = [y].
</code></pre>
Donc <b>les deux classes sont égales</b>.
</div>

<div class="box explain">
C’est la propriété classique des relations d’équivalence : “si deux éléments sont reliés, alors ils portent <i>exactement</i> la même classe”.
</div>

<br>

<div class="box answer">
<b>4. Étude de S : E → E / R<sub>f</sub>, S(x) = [x]</b><br>
On sait : f n’est <b>ni injective</b> ni <b>surjective</b>.
</div>

<div class="box explain">
<b>(a) S est-elle injective ?</b><br>
S(x) = S(y) ⇔ [x] = [y] ⇔ (par la question 3) ⇔ f(x) = f(y).  
Donc <code>S</code> est injective ⇔ <code>f</code> est injective.  
Mais on nous dit que <b>f n’est pas injective</b> → il existe <code>x ≠ y</code> avec <code>f(x) = f(y)</code>.  
Alors :
<pre><code>S(x) = [x] = [y] = S(y) avec x ≠ y
</code></pre>
Donc <b>S n’est pas injective</b>. ❌<br><br>

<b>(b) S est-elle surjective ?</b><br>
Par définition, <code>E / R<sub>f</sub></code> est l’ensemble de <b>toutes</b> les classes <code>[x]</code> pour x ∈ E.
Mais S envoie justement x sur <code>[x]</code>. Donc <b>toute classe est image d’au moins un x</b>.
Donc <b>S est surjective</b>. ✅<br><br>

<b>(c) S est-elle bijective ?</b><br>
Bijective = injective + surjective.
On a : surjective ✅ mais pas injective ❌ → donc <b>S n’est pas bijective</b>.

</div>

<br>

<div class="box answer">
<b>5. Définition de ĝ et preuve que c’est une application</b><br>
On définit :  
<pre><code>ĝ ⊆ (E / R<sub>f</sub>) × F
(X, y) ∈ ĝ   ⇔   ∃ x ∈ X tel que f(x) = y.
</code></pre>
On veut montrer : ça définit bien une <b>fonction</b> (application) <code>ĝ : E / R<sub>f</sub> → F</code>.
</div>

<div class="box explain">
Pour que ce soit une application, il faut 2 choses :  
1. <b>Totalité</b> : pour tout X ∈ E/R<sub>f</sub>, il existe un y tel que (X, y) ∈ ĝ.  
2. <b>Unicité</b> : pour un même X, on ne peut pas avoir deux y différents.
<br><br>
<b>Totalité.</b>  
Soit X ∈ E/R<sub>f</sub>. Par définition d’une classe, X = [x] pour un certain x ∈ E.  
Alors on prend ce x, on regarde y = f(x).  
Comme x ∈ X et f(x) = y, on a bien (X, y) ∈ ĝ.  
Donc c’est défini pour <b>toutes</b> les classes. ✅
<br><br>
<b>Unicité.</b>  
Soit X ∈ E/R<sub>f</sub>. Tous les éléments de X ont <b>la même image</b> par f (c’est exactement la définition de la classe).  
Donc si x₁, x₂ ∈ X, alors f(x₁) = f(x₂).  
Donc il ne peut pas y avoir (X, y₁) et (X, y₂) avec y₁ ≠ y₂.  
Autrement dit : <b>le y est unique</b>.
<br><br>
Donc ĝ est bien une application. On peut l’écrire plus joliment :
<pre><code>ĝ : E / R<sub>f</sub> → F
ĝ([x]) = f(x)
</code></pre>
et c’est bien défini car si [x] = [x′], alors f(x) = f(x′).
</div>

<br>

<div class="box answer">
<b>6. ĝ est-elle injective ? surjective ? bijective ?</b>
</div>

<div class="box explain">
<b>Injectivité de ĝ.</b><br>
Prenons deux classes X, Y ∈ E/R<sub>f</sub> telles que
<pre><code>ĝ(X) = ĝ(Y).
</code></pre>
Par définition, il existe x ∈ X, y ∈ Y tels que :
<pre><code>ĝ(X) = f(x),   ĝ(Y) = f(y).
</code></pre>
Donc
<pre><code>f(x) = f(y).
</code></pre>
Mais « avoir la même valeur par f » c’est justement « être dans la même classe » :  
<pre><code>f(x) = f(y)  ⇒  x R<sub>f</sub> y  ⇒  [x] = [y].
</code></pre>
Or X = [x] et Y = [y]. Donc X = Y.  
Donc <b>ĝ est injective</b>. ✅
<br><br>

<b>Surjectivité de ĝ.</b><br>
Pour que ĝ soit surjective, il faudrait que <b>tout</b> élément de F soit image d’une classe.
Mais ĝ([x]) = f(x). Donc <b>Im(ĝ) = Im(f)</b>.
Or on a supposé au début : <b>f n’est pas surjective</b> → son image est un vrai sous-ensemble de F.
Donc <b>ĝ n’est pas surjective</b>. ❌ <br><br>

<b>Bijectivité.</b><br>
Une application est bijective ssi elle est injective et surjective.
Ici : injective ✅ mais pas surjective ❌ → donc <b>ĝ n’est pas bijective</b>.

</div>

<br>

<div class="box explain">
<b>Bilan de tout l’exercice :</b><br>
• on part d’une application f qui identifie parfois plusieurs éléments (pas injective) et qui ne couvre pas tout F (pas surjective) ;<br>
• on construit la relation “avoir même image par f” → c’est une équivalence ;<br>
• on passe au quotient <code>E / R<sub>f</sub></code> : là, chaque élément est une “famille d’éléments de E qui avaient la même image” ;<br>
• l’application <code>S : E → E / R<sub>f</sub></code> est toujours surjective, mais injective seulement si f l’était ;<br>
• l’application <code>ĝ : E / R<sub>f</sub> → F</code> est toujours injective, mais surjective seulement si f l’était ;<br>
• on a le joli facteur :
<pre><code>f = ĝ ∘ S
</code></pre>
c’est le <b>“passage au quotient par les fibres de f”</b>.
</div>



### Exercice 23 — Monoïdes 

<div class="box question">
<b>Rappel (à connaître)</b><br>
Un <b>monoïde</b> est un triplet <code>(M, ⋆, e)</code> où :
<br>1. <b>Fermeture</b> : pour tous <code>x, y ∈ M</code>, <code>x ⋆ y ∈ M</code>.<br>
2. <b>Associativité</b> : pour tous <code>x, y, z ∈ M</code>, <code>(x ⋆ y) ⋆ z = x ⋆ (y ⋆ z)</code>.<br>
3. <b>Élément neutre</b> : il existe <code>e ∈ M</code> tel que pour tout <code>x ∈ M</code>, <code>e ⋆ x = x ⋆ e = x</code>.<br>
Si en plus <code>x ⋆ y = y ⋆ x</code> pour tous <code>x, y</code> → on dit que le monoïde est <b>commutatif</b>.
</div>

<br>

<div class="box question">
<b>1.</b> Montrer que <code>(ℕ, +, 0)</code> et <code>(℘(E), ∪, ∅)</code> sont des <b>monoïdes commutatifs</b>.
</div>

<div class="box answer">
<b>a) Pour (ℕ, +, 0)</b><br>
• <b>Ensemble</b> : <code>M = ℕ = {0,1,2,3,…}</code><br>
• <b>Opération</b> : <code>⋆ = +</code><br>
• <b>candidat neutre</b> : <code>0</code>
</div>

<div class="box explain">
<b>Fermeture.</b><br>
Pour <code>a, b ∈ ℕ</code>, on sait que <code>a + b ∈ ℕ</code>. Donc ℕ est fermé pour +. ✅<br><br>

<b>Associativité.</b><br>
Pour tous <code>a,b,c ∈ ℕ</code> :

<pre><code>(a + b) + c = a + (b + c)
</code></pre>

c’est la propriété classique de l’addition. ✅<br><br>

<b>Élément neutre.</b><br>
Pour tout <code>a ∈ ℕ</code> :

<pre><code>a + 0 = a   et   0 + a = a
</code></pre>

Donc <code>0</code> est bien neutre. ✅<br><br>

<b>Commutativité.</b><br>
Pour tout <code>a,b ∈ ℕ</code> :

<pre><code>a + b = b + a
</code></pre>

Donc le monoïde est commutatif. ✅<br><br>

<b>Conclusion :</b> <code>(ℕ, +, 0)</code> est un <b>monoïde commutatif</b>.

</div>

<br>

<div class="box answer">
<b>b) Pour (℘(E), ∪, ∅)</b><br>
• <b>Ensemble</b> : <code>M = ℘(E)</code> = ensemble de toutes les parties de E<br>
• <b>Opération</b> : <code>⋆ = ∪</code> (union d’ensembles)<br>
• <b>candidat neutre</b> : <code>∅</code>
</div>

<div class="box explain">
<b>Fermeture.</b><br>
Si <code>A, B ∈ ℘(E)</code>, alors <code>A ⊆ E</code> et <code>B ⊆ E</code>. Leur union est encore un sous-ensemble de E :
<pre><code>A ∪ B ⊆ E
</code></pre>
Donc <code>A ∪ B ∈ ℘(E)</code>. Fermeture ok. ✅<br><br>

<b>Associativité.</b><br>
Pour toutes parties <code>A,B,C ⊆ E</code> :

<pre><code>(A ∪ B) ∪ C = A ∪ (B ∪ C)
</code></pre>

(Propriété de base de l’union.) ✅<br><br>

<b>Élément neutre.</b><br>
Pour toute partie <code>A ⊆ E</code> :

<pre><code>A ∪ ∅ = A   et   ∅ ∪ A = A
</code></pre>

Donc <code>∅</code> est bien un neutre pour ∪. ✅<br><br>

<b>Commutativité.</b><br>
Pour toutes parties <code>A,B</code> :

<pre><code>A ∪ B = B ∪ A
</code></pre>

Donc c’est un <b>monoïde commutatif</b>. ✅<br><br>

<b>Conclusion :</b> <code>(℘(E), ∪, ∅)</code> est un <b>monoïde commutatif</b>.

</div>

<br><hr><br>

<div class="box question">
<b>2.</b> Soit <b>A</b> un alphabet. On note <code>A*</code> l’ensemble de <b>tous les mots finis</b> sur A (y compris le mot vide <code>ε</code>).  
On considère l’opération <b>concaténation</b> <code>·</code>.<br>
a) L’ensemble des mots de <b>longueur paire</b> est-il un monoïde pour la concaténation ?<br>
b) L’ensemble des mots de <b>longueur impaire</b> est-il un monoïde pour la concaténation ?
</div>

<div class="box answer">
<b>Rappel sur A*</b><br>
• <code>A*</code> avec la concaténation et le mot vide <code>ε</code) est un monoïde (classique).<br>
• <code>|u·v| = |u| + |v|</code> (longueur d’une concaténation = somme des longueurs).<br>
On va utiliser seulement ça.
</div>

<br>

<div class="box answer">
<b>a) Mots de longueur paire</b><br>
Notons :  
<pre><code>E = { u ∈ A*  |  |u| est pair }
</code></pre>
Question : <code>(E, ·)</code> est-il un monoïde ?
</div>

<div class="box explain">
<b>1. Fermeture.</b><br>
Prenons <code>u, v ∈ E</code>. Donc <code>|u| = 2k</code> et <code>|v| = 2ℓ</code> pour certains entiers k, ℓ.  
Alors
<pre><code>|u·v| = |u| + |v| = 2k + 2ℓ = 2(k + ℓ)
</code></pre>
→ c’est encore pair → <code>u·v ∈ E</code>. ✅ Fermeture ok.<br><br>

<b>2. Associativité.</b><br>
La concaténation est associative sur <code>A*</code> :

<pre><code>(u·v)·w = u·(v·w)
</code></pre>

Comme E ⊆ A*, l’associativité reste vraie. ✅<br><br>

<b>3. Élément neutre.</b><br>
Dans <code>A*</code>, le neutre est le mot vide <code>ε</code>.
Sa longueur est <code>|ε| = 0</code> → 0 est pair → donc <code>ε ∈ E</code>.
Et pour tout mot pair <code>u</code> :

<pre><code>ε·u = u   et   u·ε = u
</code></pre>

Donc <b>ε est bien neutre dans E</b>. ✅<br><br>

<b>Conclusion :</b> l’ensemble des mots de longueur pair est <b>un monoïde</b> pour la concaténation (et même sous-monoïde de <code>A*</code>).

</div>

<br>

<div class="box answer">
<b>b) Mots de longueur impaire</b><br>
Notons :
<pre><code>O = { u ∈ A*  |  |u| est impair }
</code></pre>
Question : <code>(O, ·)</code> est-il un monoïde ?
</div>

<div class="box explain">
<b>1. Fermeture ?</b><br>
Prenons <code>u, v ∈ O</code>. Donc <code>|u| = 2k + 1</code> et <code>|v| = 2ℓ + 1</code>.  
Alors
<pre><code>|u·v| = |u| + |v| = (2k + 1) + (2ℓ + 1) = 2(k + ℓ + 1)
</code></pre>
→ c’est <b>pair</b>, pas impair → <code>u·v ∉ O</code>.  
Donc <b>O n’est pas fermé</b> pour la concaténation. ❌  
Si pas de fermeture → pas de monoïde.  
On peut déjà s’arrêter là.
<br><br>

<b>2. Élément neutre ?</b><br>
Le seul neutre possible pour la concaténation, c’est <code>ε</code>.
Mais <code>|ε| = 0</code> → il n’est pas impair → <code>ε ∉ O</code>.
Donc même le neutre n’est pas dans O. ❌ <br><br>

<b>Conclusion :</b> l’ensemble des mots de longueur impaire <b>n’est pas</b> un monoïde (ni même un sous-monoïde).

</div>

<br>

<div class="box explain">
<b>Résumé exercice 23 :</b><br>
• <code>(ℕ, +, 0)</code> : monoïde commutatif.<br>
• <code>(℘(E), ∪, ∅)</code> : monoïde commutatif.<br>
• <b>Mots pairs</b> : oui, monoïde (neutre = ε, fermé, associatif).<br>
• <b>Mots impairs</b> : non, pas fermé, pas de neutre → pas monoïde.
</div>
