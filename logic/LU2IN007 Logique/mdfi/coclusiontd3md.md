


# TD3 — Conclusion complète (Ordres avancés)

> **Objectif de cette conclusion.** Te donner **la vision d’ensemble** + **méthodes rapides** pour reconnaître, prouver, construire ou réfuter : ordre partiel, ordre total, ordre strict, bien‑fondé, produits/lexico/préfixe/sous‑mot, bornes, Hasse, (anti)symétrie, etc. Tu peux utiliser ce document comme **antisèche raisonnée** pour les contrôles/TD/exams.

---

## 1) Panorama express des notions (à savoir par cœur)

### 1.1. Triptyque “équivalence vs ordre”
- **Équivalence** : réflexive (∀x, xRx), **symétrique** (xRy ⇒ yRx), **transitive**. Classe, quotient, “mêmes propriétés”.  
- **Ordre partiel (≤)** : réflexive, **antisymétrique** (x≤y & y≤x ⇒ x=y), transitive.  
- **Ordre strict (≺)** : **irréflexif** (¬x≺x) et transitive. Souvent défini par `x≺y ⇔ (x≤y & x≠y)`.

> **Totalité** (comparabilité) : ∀x,y, x≤y **ou** y≤x. (Fait d’un ordre partiel un **ordre total**.)

### 1.2. Bien‑fondé (fondamental pour les preuves par induction/descente)
Deux critères équivalents (en général) :
- **A)** Pas de chaîne infinie strictement décroissante : x₀ ≻ x₁ ≻ x₂ ≻ …  
- **B)** Toute partie non vide admet un **élément minimal**.

### 1.3. Ordres classiques à reconnaître
- **⊆ sur ℘(E)** : partiel (réfl., anti‑sym., trans.), non total en général.  
- **Divisibilité ∣ sur ℕ** : partiel, non total (2 et 3 incomparables).  
- **Produit coordonné** (≤ sur X×Y par composantes) : partiel si chacune partiel. Rarement total.  
- **Lexicographique** : total si chaque composante est **totalement ordonnée**.  
- **Préfixe** (u ≤ v si u est préfixe de v) : partiel, non total.  
- **Sous‑mot / facteur** (u ≤ v si v = x u y) : partiel. Le bien‑fondé dépend de l’alphabet/exercice.  
- **Ordre par opération t** : `x≤y ⇔ x t y = y` : se prouve via axiomes de t.

---

## 2) Checklists & patrons de preuve (copiables en exam)

### 2.1. Prouver qu’une relation est **ordre partiel**
1) **Réflexive** : montrer ∀x, x≤x (souvent immédiat sur opérations/idempotence ; ou x⊆x).  
2) **Antisymétrique** : supposer x≤y et y≤x ; **extraire l’égalité** x=y (ex. inclusions réciproques de parties ⇒ égalité).  
3) **Transitive** : chaîner les hypothèses (ex. inclusions X⊆Y⊆Z ⇒ X⊆Z ; divisibilité a∣b & b∣c ⇒ a∣c).

**Anti‑modèle** (pour **refuser** l’antisymétrie) : trouver x≠y tels que xRy & yRx (alors R n’est pas un ordre).

### 2.2. Prouver qu’un ordre partiel est **total**
Montrer **comparabilité** : ∀x,y, x≤y ou y≤x.  
- **Lexico** : comparer première coordonnée où ça diffère.  
- **Nombres** (≤ usuel) : trichotomie (x<y, x=y, x>y).  
- **Contre‑exemple** produit coordonné : (0,1) et (1,0) **incomparables**.

### 2.3. Passer ordre partiel → **ordre strict**
Définir `x≺y ⇔ (x≤y & x≠y)` et prouver :
- **Irréflexive** : impossible d’avoir x≺x (car x≠x).  
- **Transitive** : utiliser transitivité + antisymétrie de ≤ (cas analysis : si x≺y et y≺z ⇒ x≺z).

### 2.4. **Bien‑fondé**
- Méthode **(A)** : montrer qu’aucune suite infinie strictement décroissante n’existe (ex. ℕ avec <).  
- Méthode **(B)** : prendre **une partie non vide** et fabriquer un minimal (ex. longueur minimale, norme, poids…).
- Astuces : **mesure** (longueur des mots, somme des composantes, valeur absolue…), **Noetherianité** (tout ensemble de parties de {1..n} ordonné par ⊆ est bien fondé).

### 2.5. **Produits & Lexico**
- **Produit coordonné** : prouver propriété **par composante**.  
- **Lexico** : prouver que la **première différence** décide l’ordre ; si chaque composante est totale, le lexicographique est total.

### 2.6. **Préfixe / Sous‑mot**
- **Réflexive** : u est préfixe/facteur de u.  
- **Antisymétrique** : si u est préfixe de v et v préfixe de u ⇒ u=v (mêmes longueurs + inclusions).  
- **Transitive** : composer préfixes/facteurs.  
- **Pas total** : donner deux mots sans relation de préfixe/facteur mutuels.

---

## 3) “Trucs & astuces” (gagner du temps)

- **Égalités ⇒ symétrie immédiate** (équivalences, “même image”, produits en croix).  
- **Inclusions réciproques ⇒ égalité** (antisymétrie sur ℘(E)).  
- **Divisibilité** : a∣b et b∣a ⇒ a=b **sur ℕ** (car |a|=|b| et positifs).  
- **Produits coordonnés** : pense “par composantes”, mais **attention** à la **totalité** (souvent fausse).  
- **Lexico** : isomorphe à un **ordre total** des mots si alphabet total (A trié).  
- **Bien‑fondé** : cherche une **mesure décroissante** qui ne peut pas descendre à l’infini (longueur, somme, degré…).  
- **Hasse** : supprime arêtes déductibles par transitivité ; **conserve** uniquement les **couvertures**.  
- **Min/Max vs Inf/Sup** : min ∈ ensemble ; inf n’a pas besoin d’y être. Toujours **préciser** la différence.  
- **Comparabilité** : si tu bloques, tente un **contre‑exemple** (souvent demandé).

---

## 4) Pièges classiques (et comment les éviter)

1) **Confusion symétrie/antisymétrie** :  
   - Symétrie : xRy ⇒ yRx.  
   - **Anti**symétrie : xRy & yRx ⇒ x=y.  
   → Apprends un **exemple signature** : ⊆ est **antisymétrique** mais pas symétrique.

2) **Totalité supposée à tort** sur les produits coordonnés : (0,1) et (1,0) sont incomparables.

3) **Antisymétrie ratée** hors ℕ pour divisibilité : sur ℤ\{0}, a∣b & b∣a ⇒ a=±b (donc **pas** antisymétrique).  
   → Restreindre à ℕ ou “divisibilité up to units”.

4) **Bien‑fondé** confondu avec absence de cycles : l’absence de cycle **ne suffit pas** ; il faut **pas** de chaîne descendante infinie.

5) **Lexico mal appliqué** : la comparaison se fait à la **première position différente**, **pas** en additionnant.

6) **Préfixe vs facteur** : préfixe = “au début”, facteur = “quelque part”. Ne pas mélanger.

---

## 5) Modèles d’arguments prêts à coller

### 5.1. Antisymétrie sur ℘(E), ordre ⊆
> Suppose X⊆Y et Y⊆X. Alors tous les éléments de X sont dans Y et réciproquement ; donc X=Y. (∎)

### 5.2. Antisymétrie de la divisibilité sur ℕ
> Suppose a∣b et b∣a avec a,b∈ℕ. Il existe u,v∈ℕ tels que b=au et a=bv ⇒ a=auv ⇒ si a≠0, alors uv=1 ⇒ u=v=1 ⇒ a=b. (∎)

### 5.3. Transitivité “facteur”
> Si u est facteur de v (v = x u y) et v est facteur de w (w = x′ v y′), alors w = x′ x u y y′, donc u est facteur de w. (∎)

### 5.4. Bien‑fondé via longueur
> Toute partie non vide S⊆A* admet un mot de longueur **minimale** ℓ ; ce mot est **minimal** pour l’ordre “préfixe/facteur strict”. (∎)

### 5.5. Lexicographique total (si alphabet total)
> Soient u≠v ; à la première position où ils diffèrent, comparer leurs lettres (grâce à l’ordre total sur l’alphabet). On obtient u<lex v ou v<lex u. (∎)

---

## 6) Bornes, min/max, inf/sup (rappels rapides)

- **Majorant** de S : M tel que ∀x∈S, x≤M.  **Minorant** : m tel que m≤x.  
- **Plus grand élément (max)** : m∈S qui majore S. **Plus petit (min)** : m∈S qui minore S.  
- **Sup/Inf** (si existent) : plus petit des majorants / plus grand des minorants ; **peuvent ne pas appartenir** à S.  
- En **Hasse**, max/min = sommets **sans voisins au‑dessus/au‑dessous**.

---

## 7) Hasse (construction rapide)

1) Liste les **relations de couverture** (x≺y sans intermédiaire z).  
2) **Supprime** tous les arcs déductibles par **transitivité**.  
3) Oriente de **bas en haut** ; vrai pour ordres stricts ou partiels.  
4) Lis **minimaux** en bas, **maximaux** en haut ; **chaînes** = chemins montants ; **antichaînes** = sommets non comparables.

---

## 8) Micro‑exemples instant (flash drill)

1) Sur ℘({1,2,3}), **⊆** : partiel (OK), **non total** : {1} et {2} incomparables.  
2) Sur ℕ, **∣** : partiel ; **non total** : 2∤3 et 3∤2.  
3) Sur A* avec **préfixe** : partiel ; **bien fondé** pour ordre strict par longueur.  
4) Produit coordonné (ℕ×ℕ, ≤×≤) : partiel ; **pas total** : (0,1) vs (1,0).  
5) **Lexico** sur A* (alphabet A totalement ordonné) : **total**.  
6) Ordre strict `x≺y ⇔ x≤y & x≠y` : irréflexif + transitif (hérité de ≤).  
7) **Contre‑exemple antisymétrie** hors ℕ (divisibilité) : 2∣−2 et −2∣2 mais 2≠−2.

---

## 9) Méthodo “en 5 minutes” pour toute question d’ordre

1) **Identifier** la nature : équivalence ? ordre partiel ? strict ? total ?  
2) **Prouver** les axiomes minimaux (réflexive/irréflexive, antisym., trans.).  
3) **Tester** la **totalité** (comparabilité) par preuve ou contre‑exemple.  
4) **Étudier** min/max, bornes, inf/sup, éléments minimaux/maximaux si demandé.  
5) **(Si requis)** bien‑fondé : choisir critère A ou B et une **mesure** utile.

---

## 10) Grille de correction mentale (auto‑check)

- Ai‑je **défini** clairement la relation (dommaine + condition) ?  
- Ai‑je prouvé les **trois** propriétés (ou irr., trans. pour strict) **sans trous** ?  
- Ai‑je **donné** un **contre‑exemple** quand une propriété est fausse ?  
- Ai‑je séparé **min/max** de **inf/sup** correctement ?  
- Mon **Hasse** ne contient‑il **pas** d’arêtes transitives ?  
- Ai‑je justifié la **totalité** (ou son échec) ?  
- Ai‑je utilisé une **mesure** pour bien‑fondé si nécessaire ?

---

## 11) Mini‑banque d’exercices de conclusion (avec idées de solution)

1) Montrer que `(X,⊆)` est un ordre partiel et décrire **tous** les éléments minimaux d’une famille donnée.  
   *Idée* : minimaux = ensembles sans sous‑ensemble strict dans la famille.

2) Sur ℕ×ℕ, comparer (a,b) et (c,d) en **lexico** vs **produit coordonné**.  
   *Idée* : lexico est total ; produit ne l’est pas.

3) Donner un exemple d’ordre partiel **non total** et tracer son **Hasse**.  
   *Idée* : ⊆ sur ℘({1,2,3}).

4) Prouver qu’il **n’existe pas** de chaîne infinie strictement décroissante pour la **longueur** des mots.  
   *Idée* : la longueur est une mesure dans ℕ.

5) Sur A* facteur, décider si l’ordre strict est bien fondé.  
   *Idée* : oui via longueur (on ne peut pas raccourcir indéfiniment en retirant des lettres si on exige une stricte décroissance).

6) Sur ℤ\{0}, expliquer pourquoi la **divisibilité** n’est pas **antisymétrique**.  
   *Idée* : unités ±1.

7) Construire deux mots **incomparables** pour l’ordre **préfixe**.  
   *Idée* : “ab” et “ba”.

8) Montrer que le **produit** de deux ordres partiels est un **ordre partiel**.  
   *Idée* : propriétés héritées composante par composante.

9) Décider si l’ordre **lexico** sur `{0,1}^*` est **bien fondé**.  
   *Idée* : **non** en général (ex. 1 >lex 01 >lex 001 >lex … si l’on prend un ordre inversé sur l’alphabet). Il faut préciser le sens ; avec ordre **croissant** classique et stricte sur longueurs, on peut fabriquer des descentes en préfixant.

10) Distinguer **maximal** vs **plus grand élément** sur un poset donné.  
    *Idée* : plusieurs maximaux possibles sans plus grand élément.

---

## 12) Dernier mot (stratégie d’exam)

- **Écris d’abord la définition** de la relation ET de l’espace (dom.) — ça “bétonne” la copie.  
- **Enchaîne les axiomes** demandés (titres en marge : Réfl., Anti‑sym., Trans.).  
- **Compare** (totalité ?) par un mini‑argument/contre‑exemple.  
- **Schématise** (Hasse) si pertinent : ça vaut des points.  
- **Conclusion** en une ligne : “Donc (E,≤) est un ordre partiel/total ; l’ordre strict associé est… ; bien‑fondé : …”.

Bonne révision — garde ce document comme guide rapide pour tout exercice d’ordres. ✨






