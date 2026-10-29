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


<!-- ======================================================= -->

<!-- =============== CONCLUSION CLÉ (MÉTHODE) =============== -->

<div class="box answer">
  <h2>Conclusion clé — Comment résoudre (presque) toutes les questions du sujet</h2>

  <h3>1) Checklist universelle avant d’écrire</h3>
  <ol>
    <li><strong>Identifier l’objet</strong> : mot (A*), liste, arbre, paire (ℕ×ℕ), langage (Dyck), relation (préfixe/lexico), etc.</li>
    <li><strong>Choisir le bon type d’induction</strong> :
      <ul>
        <li><em>Sur les entiers</em> : induction simple/forte.</li>
        <li><em>Sur des objets construits</em> (mots, listes, arbres) : <strong>induction structurelle</strong>.</li>
        <li><em>Quand on diminue une mesure</em> (longueur, hauteur, ordre bien fondé) : <strong>induction bien fondée</strong>.</li>
      </ul>
    </li>
    <li><strong>Écrire la propriété P(·)</strong> précisément (avec notations exactes) <em>avant</em> la preuve.</li>
    <li><strong>Dérouler Base → Induction</strong> en suivant la <u>définition</u> de l’objet (cas du constructeur).</li>
    <li><strong>Conclure</strong> proprement (phrase finale = points faciles).</li>
  </ol>

  <h3>2) Patrons prêts à copier</h3>
  <pre><code>• Induction simple (n ∈ ℕ)
Base : montrer P(0) (ou P(1)).
H.I. : supposer P(n) vraie.
Pas : démontrer P(n+1) à partir de P(n). Conclure.

• Induction forte (n ∈ ℕ)
Base : montrer P(0).
H.I. : supposer P(k) vraie pour tous k ≤ n.
Pas : démontrer P(n+1) en utilisant {P(k)}<sub>k≤n</sub>. Conclure.

• Induction structurelle (mots/listes/arbres)
Base(s) : cas le(s) plus simple(s) (ε, nil, feuille/∅).
Pas : supposer la propriété vraie pour les sous-objets (u, x, g/d),
prouver pour l’objet construit (u·a, n|x, ⟨g,a,d⟩). Conclure.

• Induction bien fondée (mesure m < m(x))
Base : cas minimal(s).
Pas : supposer P(y) pour tous y < x (selon la mesure), démontrer P(x). Conclure.</code></pre>

</div>

<!-- ======================================================= -->

<!-- =============== RECETTES PAR THÈME ===================== -->

<div class="box explain">
  <h2>Recettes rapides par type d’exercice</h2>

  <h3>A) Mots (A*), longueurs et miroirs</h3>
  <ul>
    <li><strong>But fréquent</strong> : |uv|=|u|+|v|, |w|=∑|w|<sub>a</sub>, ~ (~w)=w, |~w|=|w|.</li>
    <li><strong>Méthode</strong> : <u>induction structurelle</u> sur le 2ᵉ argument (ou sur w).
      <br>Base ε. Pas u·a : réécrire la propriété en utilisant la définition (ajout d’une lettre).</li>
    <li><strong>Astuce</strong> : quand on colle une lettre, la longueur augmente de 1 et le compteur de cette lettre aussi.</li>
  </ul>

  <h3>B) Langage de Dyck (équilibres a/b)</h3>
  <ul>
    <li><strong>But fréquent</strong> : montrer l’équivalence “définition inductive” ⇔ “comptage + condition de préfixes”.</li>
    <li><strong>Direction inductive</strong> (E1→E2) : <u>induction structurelle</u> sur w = a·u·b·v.  
      Cas des préfixes : (avant a) / (entre a et b) / (après b) + I.H. sur u et v.</li>
    <li><strong>Direction inverse</strong> (E2→E1) : <u>induction bien fondée</u> sur |w|.  
      w≠ε ⇒ w commence par a et admet sa <em>première</em> fermeture b : écrire w = a·u·b·v, appliquer I.H. à u et v, reconstruire.</li>
    <li><strong>Astuce</strong> : pense “pile” (a = push, b = pop). Jamais de dette de b dans un préfixe.</li>
  </ul>

  <h3>C) Ordres sur A* : préfixe, lexicographique, bien-fondé</h3>
  <ul>
    <li><strong>Préfixe</strong> : u ≤ v ⇔ ∃w, v = u·w. <u>Partiel</u>, <u>bien fondé</u>.  
      Pour montrer l’équivalence avec la version “inductive”, fais une <u>double inclusion</u> par induction.</li>
    <li><strong>Lexicographique</strong> (A total) : <u>total</u> mais en général <u>pas bien fondé</u>.  
      Contre-exemple : b &gt; ab &gt; aab &gt; aaab &gt; …</li>
    <li><strong>Astuce</strong> : si l’énoncé parle de “minimal”, vérifie d’abord le bien-fondé.</li>
  </ul>

  <h3>D) Listes (nil, n|x), somme s, longueur ℓ, renversement rev</h3>
  <ul>
    <li><strong>But fréquent</strong> : s(x|y)=s(x)+s(y), ℓ(x|y)=ℓ(x)+ℓ(y), ℓ(rev x)=ℓ(x), rev(rev x)=x.</li>
    <li><strong>Méthode</strong> : <u>induction structurelle</u> sur la 1ʳᵉ liste ; base nil ; pas n|x.</li>
    <li><strong>Astuce</strong> : <code>rev(n|x) = rev(x) || n</code> (ajout en fin). Garde la définition sous les yeux.</li>
  </ul>

  <h3>E) Arbres binaires : h, n, f ; arbres stricts</h3>
  <ul>
    <li><strong>Formules</strong> :
      <ul>
        <li>h(∅)=0, h(•)=1, h(⟨g,a,d⟩)=1+max(h(g),h(d))</li>
        <li>n(∅)=0, n(•)=1, n(⟨g,a,d⟩)=1+n(g)+n(d)</li>
        <li>f(∅)=0, f(•)=1, f(⟨g,a,d⟩)=f(g)+f(d)</li>
      </ul>
    </li>
    <li><strong>Bornes</strong> : n(t) ≤ 2^{h(t)} − 1, f(t) ≤ 2^{h(t)-1}.  
        <u>Induction structurelle</u> : majore à gauche et droite, puis utilise H = 1 + max(…)</li>
    <li><strong>Arbre strict</strong> : n = ar + 1 et n = 2f − 1.  
        <u>Induction structurelle</u> : feuille (OK), puis ⟨g,a,d⟩ avec I.H. sur g et d.</li>
    <li><strong>Astuce</strong> : teste tes bornes sur les deux extrêmes — <em>chaîne</em> (très peu de nœuds) et <em>plein</em> (atteint la borne).</li>
  </ul>

  <h3>F) Relations inductives sur ℕ×ℕ (Inf1 / Inf2), ensemble D des multiples</h3>
  <ul>
    <li><strong>Idée</strong> : ces règles <em>encodent</em> souvent ≤ ou la divisibilité.  
        Prouve la propriété caractéristique (⇔) par double implication.</li>
    <li><strong>Inf1 / Inf2</strong> : montrer “appartient” ⇔ “n₁ ≤ n₂” avec un sens “règles ⇒ ≤” (lecture) + “≤ ⇒ règles” (construction par pas).</li>
    <li><strong>Multiples D</strong> : (n,0) base ; (n,n′) ⇒ (n,n+n′). Montrer (n,n′) ∈ D ⇔ ∃k, n′ = k·n par induction sur k (ou structurelle).</li>
    <li><strong>Astuce</strong> : <em>dessine</em> quelques premiers couples sur une grille, tu vois le motif.</li>
  </ul>
</div>

<!-- ======================================================= -->

<!-- ================== PIÈGES & RÉFLEXES ================== -->

<div class="box explain">
  <h2>Pièges fréquents & comment les éviter</h2>
  <ul>
    <li><strong>Oublier la base</strong> : toujours traiter ε / nil / ∅ / feuille.</li>
    <li><strong>Induction mal calée</strong> : suis exactement le <u>constructeur</u> de l’objet (u·a / n|x / ⟨g,a,d⟩).</li>
    <li><strong>Confondre ordre préfixe et lexico</strong> :  
      préfixe = partiel & bien fondé ; lexico = total & pas bien fondé (en général).</li>
    <li><strong>Dyck</strong> : vérifier <u>tous</u> les préfixes (pas seulement la fin). La première fermeture b est la clé de la décomposition.</li>
    <li><strong>Arbres</strong> : h = 1 + max(…) (pas somme), f = f(g)+f(d) (pas +1), n = 1 + n(g)+n(d).</li>
    <li><strong>Classes d’équivalence vs ordre</strong> : équivalence = réflexive + symétrique + transitive ; ordre = réflexive + antisymétrique + transitive.</li>
  </ul>
</div>

<!-- ======================================================= -->

<!-- =============== AUTO-CONTROLES FINAUX ================== -->

<div class="box explain">
  <h2>Auto-contrôles en 20 secondes</h2>
  <ul>
    <li><strong>Ai-je déclaré clairement P(·)</strong> juste avant la preuve ?</li>
    <li><strong>Base(s) écrite(s)</strong> ? (ε / nil / ∅ / feuille)</li>
    <li><strong>Hypothèse(s) d’induction</strong> bien posées (j’indique sur quoi porte l’I.H.) ?</li>
    <li><strong>Pas d’induction</strong> : j’applique mécaniquement la définition du constructeur.</li>
    <li><strong>Conclusion</strong> : phrase finale explicite (“Par (base) et (induction), P(·) est vraie pour tout …”).</li>
  </ul>
</div>

<!-- ======================================================= -->

<!-- ============== GABARITS DE RÉDACTION =================== -->

<div class="box explain">
  <h2>Gabarits de réponse (à coller / adapter)</h2>

  <h3>1) Induction structurelle (mots)</h3>
  <pre><code>On prouve la propriété P(w) par induction structurelle sur w ∈ A*.
Base : w = ε. (Détailler et conclure P(ε).)
Pas : supposer P(u) vraie et montrer P(u·a).
      (Utiliser la définition de la propriété et la construction u·a.)
Conclusion : par induction, P(w) vraie pour tout w ∈ A*.</code></pre>

  <h3>2) Induction structurelle (arbres)</h3>
  <pre><code>On prouve P(t) par induction structurelle.
Bases : t = ∅ et t = • (vérifications directes).
Pas : t = ⟨g,a,d⟩. Supposer P(g) et P(d) vraies (I.H.), déduire P(t) par les définitions (h, n, f, ...).
Conclusion.</code></pre>

  <h3>3) Dyck (sens “préfixes” → “inductif”)</h3>
  <pre><code>Induction bien fondée sur |w|.
Si w = ε, c’est ok. Sinon w commence par a. Soit b la première fermeture correspondante.
On écrit w = a u b v avec u, v plus courts.
Par I.H., u, v appartiennent au langage inductif.
Par règle (I), a u b v appartient. Conclusion.</code></pre>

  <h3>4) Égalité de deux définitions (ex. préfixe)</h3>
  <pre><code>Montrer D1 = D2 par deux inclusions.
(i) D2 ⇒ D1 : induction sur la dérivation de D2.
(ii) D1 ⇒ D2 : récurrence (souvent sur la longueur). Conclusion.</code></pre>
</div>

<!-- ======================================================= -->

<!-- =================== FIN — RÉSUMÉ ======================= -->

<div class="box answer">
  <h2>À retenir en une minute</h2>
  <ul>
    <li><strong>Choisis la bonne induction</strong> en lisant la <u>définition</u> de l’objet.</li>
    <li><strong>Écris P(·)</strong> proprement, puis déroule Base → Pas d’induction → Conclusion.</li>
    <li><strong>Pour Dyck</strong> : “première fermeture” + pile ; pour <strong>préfixe</strong> : deux définitions équivalentes ; pour <strong>lexico</strong> : total mais pas bien fondé ; pour <strong>arbres</strong> : h, n, f bien définies ; pour <strong>listes</strong> : s, ℓ, rev suivent la structure.</li>
    <li><strong>Finis par une phrase de conclusion</strong> (ça rapporte).</li>
  </ul>
  <p>Avec ces recettes, tu peux attaquer sereinement les variantes possibles de l’exam dans l’heure. Bonne réussite ! 💪</p>
</div>






<h1>Conclusion — Induction sur ℕ & Induction structurelle (version simple et claire)</h1>

<div class="box explain">
  <h2>1) Idées clés à retenir</h2>
  <ul>
    <li><strong>Induction simple sur ℕ</strong> : on prouve d’abord la <em>base</em> (souvent n=0 ou n=1), puis l’<em>hérédité</em> : P(n) ⇒ P(n+1). Si ces deux étapes sont vraies, alors P(n) est vraie pour tout n.</li>
    <li><strong>Induction forte</strong> : pour prouver P(n), on peut supposer vraies <em>toutes</em> les P(k) pour k &lt; n. Utile quand la preuve pour n dépend de plusieurs valeurs plus petites (ex : suites définies par plusieurs cas).</li>
    <li><strong>Induction structurelle</strong> : pour des objets construits par <em>règles</em> (mots, arbres), on prouve P sur <em>toutes les bases</em>, puis on montre que si P est vraie sur les sous-objets, alors P est vraie sur l’objet construit avec eux.</li>
  </ul>
</div>

<div class="box explain">
  <h2>2) Notations utilisées</h2>
  <ul>
    <li><strong>Mots sur A = {a,b}</strong> : A* est l’ensemble de tous les mots finis. <code>|w|<sub>a</sub></code> = nombre de « a » dans w ; <code>|w|<sub>b</sub></code> = nombre de « b » dans w. Un <em>préfixe</em> u de v signifie qu’il existe x tel que u·x = v. Un <em>préfixe propre</em> est un préfixe différent du mot entier.</li>
    <li><strong>Arbres binaires</strong> :
      <ul>
        <li>Base : ∅ (arbre vide) est un arbre.</li>
        <li>Construction : si g et d sont des arbres et a est une étiquette, alors (a, g, d) est un arbre.</li>
      </ul>
      Définitions usuelles (par récurrence structurelle) :
      <ul>
        <li>Hauteur h : h(∅)=0 ; h((a,g,d)) = 1 + max(h(g), h(d)).</li>
        <li>Nombre de nœuds n : n(∅)=0 ; n((a,g,d)) = 1 + n(g) + n(d).</li>
        <li>Nombre de feuilles f : f(∅)=0 ; f((a,∅,∅))=1 ; sinon f((a,g,d)) = f(g)+f(d).</li>
        <li>Arêtes ar : ar(∅)=0 ; ar((a,g,d)) = ar(g)+ar(d) + [g≠∅] + [d≠∅].</li>
      </ul>
      <em>Arbre binaire strict</em> : non vide et chaque nœud a soit 0 enfant (feuille) soit 2 enfants (jamais 1 seul).</li>
  </ul>
</div>

<div class="box explain">
  <h2>3) Modèle de rédaction — Induction structurelle</h2>
  <ol>
    <li><strong>Rappeler la définition inductive</strong> (bases et règles de construction).</li>
    <li><strong>Énoncer clairement la propriété P(x)</strong> à montrer pour tout objet x.</li>
    <li><strong>Cas de base</strong> : prouver P pour chaque base.</li>
    <li><strong>Étape inductive</strong> : supposer P vraie pour les sous-objets (hypothèses d’induction), puis prouver P pour l’objet construit.</li>
    <li><strong>Conclusion</strong> : « donc, par induction structurelle, P est vraie pour tous les objets ». </li>
  </ol>
</div>

<hr/>

<div class="box question">
  <h2>4) Exemple guidé (mots) — Langage L sur A={a,b}</h2>
  <p><strong>Définition de L</strong> :</p>
  <pre>(B) b ∈ L
(I) si u ∈ L et v ∈ L alors a·u·v ∈ L</pre>
  <p><strong>À prouver</strong> :</p>
  <ol>
    <li>(1) Pour tout w∈L : <code>|w|<sub>b</sub> = |w|<sub>a</sub> + 1</code>.</li>
    <li>(2) Pour tout w∈L et tout préfixe propre w′ de w : <code>|w′|<sub>a</sub> ≥ |w′|<sub>b</sub></code>.</li>
  </ol>
</div>

<div class="box answer">
  <h3>Solution pas à pas (simple et complète)</h3>
  <p><strong>(1) Égalité globale sur chaque mot de L</strong></p>
  <ul>
    <li><em>Base</em> : w=b. Alors |w|<sub>a</sub>=0 et |w|<sub>b</sub>=1. Donc |w|<sub>b</sub> = |w|<sub>a</sub> + 1 (vrai).</li>
    <li><em>Induction</em> : supposons vrais pour u,v∈L :
      <br> |u|<sub>b</sub> = |u|<sub>a</sub> + 1 et |v|<sub>b</sub> = |v|<sub>a</sub> + 1.
      <br>Pour w = a·u·v :
      <div style="padding-left:10px">
        |w|<sub>a</sub> = 1 + |u|<sub>a</sub> + |v|<sub>a</sub><br/>
        |w|<sub>b</sub> = |u|<sub>b</sub> + |v|<sub>b</sub> = (|u|<sub>a</sub>+1) + (|v|<sub>a</sub>+1)
        = (1+|u|<sub>a</sub>+|v|<sub>a</sub>) + 1 = |w|<sub>a</sub> + 1.
      </div>
      Donc l’égalité est vraie pour a·u·v. </li>
  </ul>

  <p><strong>(2) Sécurité des préfixes</strong> : tout préfixe propre a au moins autant de « a » que de « b ».</p>
  <p>On prouve P(w) : « pour tout préfixe propre w′ de w, |w′|<sub>a</sub> ≥ |w′|<sub>b</sub> » par induction structurelle.</p>
  <ul>
    <li><em>Base</em> : w=b. Le seul préfixe propre est ε : |ε|<sub>a</sub>=|ε|<sub>b</sub>=0 ⇒ OK.</li>
    <li><em>Induction</em> : w=a·u·v. Supposons P(u) et P(v) vraies. Prenons un préfixe propre w′ de w. Quatre cas simples :
      <ol type="a">
        <li>w′=ε ⇒ 0≥0, OK.</li>
        <li>w′=a ⇒ 1≥0, OK.</li>
        <li>w′=a·x avec x préfixe propre de u.<br/>
            Par P(u), |x|<sub>a</sub> ≥ |x|<sub>b</sub>. Donc |w′|<sub>a</sub>=1+|x|<sub>a</sub> ≥ 1+|x|<sub>b</sub>=|w′|<sub>b</sub>. </li>
        <li>w′=a·u·y avec y préfixe propre de v.<br/>
            Par (1) sur u : |u|<sub>b</sub>=|u|<sub>a</sub>+1. Par P(v) sur y : |y|<sub>a</sub> ≥ |y|<sub>b</sub>.
            <div style="padding-left:10px">
              |w′|<sub>a</sub> = 1 + |u|<sub>a</sub> + |y|<sub>a</sub><br/>
              |w′|<sub>b</sub> = |u|<sub>b</sub> + |y|<sub>b</sub> = (|u|<sub>a</sub>+1) + |y|<sub>b</sub>
            </div>
            Donc |w′|<sub>a</sub> − |w′|<sub>b</sub> = (|y|<sub>a</sub> − |y|<sub>b</sub>) ≥ 0. </li>
      </ol>
      Tous les cas sont bons ⇒ P(w) est vraie.</li>
  </ul>

  <p><strong>Petit exemple concret pour « voir »</strong> :<br/>
    Prenons u=b et v=b. Alors w₁=a·b·b. Compte : |w₁|<sub>a</sub>=1, |w₁|<sub>b</sub>=2 (OK pour (1)).<br/>
    Reprenons u=w₁ et v=b : w₂=a·w₁·b = a a b b b. Compte : |w₂|<sub>a</sub>=2, |w₂|<sub>b</sub>=3. Tous les préfixes vérifient (2).
  </p>
</div>

<hr/>

<div class="box question">
  <h2>5) Exemple guidé (arbres) — Deux formules classiques</h2>
  <ol>
    <li><strong>Borne sur les nœuds</strong> : pour tout arbre t, <code>n(t) ≤ 2^{h(t)} − 1</code>.</li>
    <li><strong>Arbres stricts</strong> :
      <ul>
        <li>(a) <code>n(t) = ar(t) + 1</code></li>
        <li>(b) <code>n(t) = 2·f(t) − 1</code></li>
      </ul>
    </li>
  </ol>
</div>

<div class="box answer">
  <h3>Preuves courtes et claires</h3>

  <p><strong>(1) n(t) ≤ 2^{h(t)} − 1</strong></p>
  <ul>
    <li><em>Base</em> : t=∅. n=0, h=0 ⇒ 0 ≤ 1−1 = 0. OK.</li>
    <li><em>Induction</em> : t=(a,g,d). Par hypothèse d’induction :
      n(g) ≤ 2^{h(g)}−1 et n(d) ≤ 2^{h(d)}−1. Posons M=max(h(g),h(d)), alors h(t)=M+1.
      <div style="padding-left:10px">
        n(t)=1+n(g)+n(d) ≤ 1+(2^{h(g)}−1)+(2^{h(d)}−1) ≤ 2·2^M−1 = 2^{M+1}−1 = 2^{h(t)}−1.
      </div>
      Donc l’inégalité est vraie.</li>
  </ul>

  <p><strong>(2) Arbres stricts</strong></p>
  <p><em>(a) n(t) = ar(t) + 1</em></p>
  <ul>
    <li><em>Base (feuille)</em> : n=1, ar=0 ⇒ 1=0+1. OK.</li>
    <li><em>Induction</em> : t=(a,g,d) avec g≠∅ et d≠∅ (strict). Alors ar(t)=ar(g)+ar(d)+2.
      Par hypothèse d’induction : n(g)=ar(g)+1 et n(d)=ar(d)+1.
      <div style="padding-left:10px">
        n(t)=1+n(g)+n(d)=1+(ar(g)+1)+(ar(d)+1)=ar(g)+ar(d)+3=(ar(g)+ar(d)+2)+1=ar(t)+1.
      </div>
      C’est prouvé.</li>
  </ul>

  <p><em>(b) n(t) = 2·f(t) − 1</em></p>
  <ul>
    <li><em>Base (feuille)</em> : n=1, f=1 ⇒ 1 = 2·1 − 1. OK.</li>
    <li><em>Induction</em> : t=(a,g,d) strict interne, donc g,d≠∅. Par hypothèse :
      n(g)=2f(g)−1 et n(d)=2f(d)−1 ; et f(t)=f(g)+f(d).
      <div style="padding-left:10px">
        n(t)=1+n(g)+n(d)=1+(2f(g)−1)+(2f(d)−1)=2(f(g)+f(d))−1=2f(t)−1.
      </div>
      C’est prouvé.</li>
  </ul>
</div>

<hr/>

<div class="box explain">
  <h2>6) Mini-fiche « comment rédiger vite et propre »</h2>
  <ul>
    <li><strong>Étape 1</strong> : écrire clairement la définition par cas (bases + règle(s)).</li>
    <li><strong>Étape 2</strong> : énoncer la propriété P avec les bonnes notations (|w|<sub>a</sub>, préfixe, h, n, f, ar…).</li>
    <li><strong>Étape 3</strong> : traiter <em>tous</em> les cas de base.</li>
    <li><strong>Étape 4</strong> : pour l’étape inductive, analyser <em>toutes</em> les formes possibles de l’objet construit (par ex. pour les préfixes de a·u·v : ε, a, a·(préfixe de u), a·u·(préfixe de v)).</li>
    <li><strong>Étape 5</strong> : utiliser l’hypothèse d’induction uniquement sur les sous-objets autorisés par la définition.</li>
    <li><strong>Étape 6</strong> : conclure explicitement par « induction » ou « induction structurelle ».</li>
  </ul>
</div>

<div class="box question">
  <h2>7) Exemple rapide (induction simple sur ℕ)</h2>
  <p>Montrer : pour tout n≥1, 1+2+…+n = n(n+1)/2.</p>
</div>

<div class="box answer">
  <h3>Preuve courte</h3>
  <ul>
    <li><em>Base</em> n=1 : 1 = 1·2/2 ⇒ vrai.</li>
    <li><em>Hérédité</em> : supposons vrai pour n. Alors pour n+1 :
      <div style="padding-left:10px">
        1+…+n+(n+1) = [n(n+1)/2] + (n+1) = (n+1)(n/2 + 1) = (n+1)(n+2)/2.
      </div>
      Donc la formule est vraie pour n+1. Conclusion par induction.</li>
  </ul>
</div>

<hr/>

<div class="box explain">
  <h2>8) Erreurs fréquentes (à éviter)</h2>
  <ul>
    <li>Oublier un cas de base.</li>
    <li>Utiliser l’hypothèse d’induction sur un objet qui n’est pas un « sous-objet » de la construction.</li>
    <li>Mélanger définitions (ex : confondre préfixe et sous-mot quelconque).</li>
    <li>Ne pas traiter toutes les formes possibles d’un préfixe ou d’un nœud.</li>
  </ul>
</div>

<div class="box question">
  <h2>9) Exercice d’entraînement (à faire seul, plan fourni)</h2>
  <p><strong>Ordre préfixe</strong> : On définit « u ≤<sub>pref</sub> v » par :
  <br>(B) ε ≤ v ; &nbsp; (I) si u ≤ v alors a·u ≤ a·v (pour toute lettre a).
  <br>Montrer que « u ≤<sub>pref</sub> v » est équivalent à « il existe w tel que v = u·w ».</p>
</div>

<div class="box answer">
  <h3>Plan très simple</h3>
  <ul>
    <li><em>Sens 1</em> (règles ⇒ existence de w) : induction structurelle sur la dérivation de « u ≤ v ». Traiter le cas base ε, puis le cas a·u ≤ a·v.</li>
    <li><em>Sens 2</em> (existence de w ⇒ règles) : induction sur la longueur de w. Cas w=ε puis w=a·x.</li>
  </ul>
</div>

<hr/>

<div class="box explain">
  <h2>10) Résumé express</h2>
  <ul>
    <li>Induction simple : base + hérédité n→n+1.</li>
    <li>Induction forte : on suppose vrai pour tous les k&lt;n.</li>
    <li>Induction structurelle : bases + « si vrai sur les morceaux, alors vrai sur l’assemblage ».</li>
    <li>Mots L : la règle a·u·v ajoute 1 « a » et conserve l’écart « b = a + 1 » ; les préfixes restent sûrs (|a| ≥ |b|).</li>
    <li>Arbres : toujours exprimer h, n, f, ar en fonction des sous-arbres et conclure par récurrence.</li>
  </ul>
</div>

<p><em>Si tu veux, je peux mettre tout ceci directement dans ton modèle exact (les mêmes &lt;div class="box question/answer/explain"&gt;) pour un TD prêt à imprimer, ou ajouter d’autres exemples détaillés (arbre strict, parcours préfixe, etc.).</em></p>
</div>


<h1>Exemple unique — Arbre binaire : notations + « comment trouver l’induction » + preuve guidée</h1>

<div class="box explain">
  <h2>1) Les notations (très simple)</h2>
  <ul>
    <li><strong>Définition inductive des arbres binaires</strong>
      <ul>
        <li>Base : ∅ (arbre vide) est un arbre.</li>
        <li>Construction : si <code>g</code> et <code>d</code> sont des arbres et <code>a</code> est une étiquette (lettre, nombre…), alors <code>(a, g, d)</code> est un arbre (a = racine, g = sous-arbre gauche, d = sous-arbre droit).</li>
      </ul>
    </li>
    <li><strong>Fonctions usuelles (définies elles aussi par récurrence)</strong>
      <ul>
        <li>Hauteur <code>h</code> : <code>h(∅)=0</code>, <code>h((a,g,d)) = 1 + max(h(g), h(d))</code>.</li>
        <li>Nombre de nœuds <code>n</code> : <code>n(∅)=0</code>, <code>n((a,g,d)) = 1 + n(g) + n(d)</code>.</li>
        <li>Nombre de feuilles <code>f</code> :
          <ul>
            <li><code>f(∅)=0</code>, <code>f((a,∅,∅))=1</code> (une feuille),</li>
            <li>sinon <code>f((a,g,d)) = f(g) + f(d)</code>.</li>
          </ul>
        </li>
        <li>Nombre d’arêtes <code>ar</code> : <code>ar(∅)=0</code>, <code>ar((a,g,d)) = ar(g)+ar(d) + [g≠∅] + [d≠∅]</code> (on ajoute 1 par enfant non vide).</li>
      </ul>
    </li>
    <li><strong>Arbre binaire strict</strong> : non vide, et chaque nœud a soit 0 enfant (feuille), soit 2 enfants (jamais exactement 1).</li>
  </ul>
</div>

<div class="box explain">
  <h2>2) Comment « trouver l’induction » (la bonne propriété P)</h2>
  <ol>
    <li><strong>Regarder la construction</strong> : vos objets naissent soit de <code>∅</code>, soit d’un collage <code>(a,g,d)</code>. Donc votre preuve doit traiter exactement ces deux formes.</li>
    <li><strong>Écrire la propriété P(t)</strong> en fonction de ce que modifie la construction. Exemple : des inégalités comme <code>n(t) ≤ 2^{h(t)} − 1</code> ou des identités comme <code>n(t)=ar(t)+1</code> ou, en strict, <code>n(t)=2f(t)−1</code>.</li>
    <li><strong>Cas de base</strong> : prouver P(∅) (et P(feuille) si nécessaire).</li>
    <li><strong>Étape inductive</strong> : supposer P(g) et P(d) vraies (hypothèses d’induction), puis démontrer P((a,g,d)). On <em>exprime tout</em> (h, n, f, ar…) par les mêmes choses sur g et d — c’est la clé.</li>
  </ol>
</div>

<div class="box question">
  <h2>3) Un seul exemple complet</h2>
  <p><strong>Arbre choisi :</strong></p>
  <pre>
            A
          /   \
         B     C
        / \   / \
       D  ∅  ∅  E
  </pre>
  <p>Forme inductive : <code>t = (A, (B, (D, ∅, ∅), ∅), (C, ∅, (E, ∅, ∅)))</code>.</p>
  <p><em>Note</em> : cet arbre n’est <strong>pas</strong> strict (B et C ont un seul enfant).</p>
</div>

<div class="box answer">
  <h3>Étape A — Calcul des notations sur l’exemple</h3>
  <ul>
    <li><strong>Hauteurs</strong>
      <ul>
        <li>h(D)=1, h(E)=1 (feuilles)</li>
        <li>h(B)=1+max(h(D),0)=2 ; h(C)=1+max(0,h(E))=2</li>
        <li>h(A)=1+max(h(B),h(C))=1+max(2,2)=3</li>
      </ul>
    </li>
    <li><strong>Nombre de nœuds</strong>
      <ul>
        <li>n(D)=1, n(E)=1</li>
        <li>n(B)=1+n(D)+0=2 ; n(C)=1+0+n(E)=2</li>
        <li>n(A)=1+n(B)+n(C)=1+2+2=5</li>
      </ul>
    </li>
    <li><strong>Nombre de feuilles</strong>
      <ul>
        <li>f(D)=1, f(E)=1</li>
        <li>f(B)=f(D)+f(∅)=1+0=1 ; f(C)=f(∅)+f(E)=0+1=1</li>
        <li>f(A)=f(B)+f(C)=1+1=2</li>
      </ul>
    </li>
    <li><strong>Nombre d’arêtes</strong>
      <ul>
        <li>ar(D)=0, ar(E)=0</li>
        <li>ar(B)=ar(D)+0 + [D≠∅]+[∅≠∅] = 0+0+1+0=1</li>
        <li>ar(C)=0+0 + 0+1 = 1</li>
        <li>ar(A)=ar(B)+ar(C) + 1 + 1 = 1+1+2=4</li>
      </ul>
    </li>
  </ul>
  <p><strong>Sanity check visuel</strong> : il y a 5 nœuds (A,B,C,D,E) et 4 arêtes (A–B, A–C, B–D, C–E). Tout colle.</p>
</div>

<div class="box explain">
  <h2>4) Preuve guidée n°1 — « Pour tout arbre t, n(t) ≤ 2^{h(t)} − 1 »</h2>
  <p><em>Pourquoi cette P(t) ?</em> Parce que quand on colle deux sous-arbres sous une racine, la hauteur prend un <code>max</code> et s’incrémente de 1, tandis que le nombre de nœuds s’additionne puis +1 : c’est parfait pour comparer avec une puissance de 2.</p>
  <h3>Rédaction (ultra claire)</h3>
  <ul>
    <li><strong>Propriété</strong> P(t) : <code>n(t) ≤ 2^{h(t)} − 1</code> pour tout arbre t.</li>
    <li><strong>Base</strong> : t=∅. Alors n=0 et h=0, donc <code>0 ≤ 2^0 − 1 = 0</code>. OK.</li>
    <li><strong>Induction</strong> : soit t=(a,g,d). On suppose P(g) et P(d) vraies :
      <br><code>n(g) ≤ 2^{h(g)} − 1</code> et <code>n(d) ≤ 2^{h(d)} − 1</code>.
      <br>Posons M = max(h(g), h(d)). Alors h(t)=M+1.
      <div style="padding-left:10px">
        n(t) = 1 + n(g) + n(d)
        ≤ 1 + (2^{h(g)} − 1) + (2^{h(d)} − 1)
        ≤ 1 + (2^{M} − 1) + (2^{M} − 1)
        = 2·2^{M} − 1
        = 2^{M+1} − 1
        = 2^{h(t)} − 1.
      </div>
      <strong>Conclusion</strong> : P(t) est vraie pour tous les arbres par induction structurelle.
    </li>
  </ul>
  <p><strong>Vérification sur notre exemple</strong> : h(t)=3 et n(t)=5, donc <code>5 ≤ 2^3−1 = 7</code>, correct.</p>
</div>

<div class="box explain">
  <h2>5) Preuve guidée n°2 (bonus) — Arbres stricts : « n(t) = 2·f(t) − 1 »</h2>
  <p><em>Pourquoi cette P(t) ?</em> En arbre strict, chaque nœud interne a 2 enfants ⇒ le « +1 » des nœuds se répartit exactement sur les feuilles. C’est une identité classique.</p>
  <h3>Rédaction courte</h3>
  <ul>
    <li><strong>Propriété</strong> P(t) : <code>n(t) = 2·f(t) − 1</code> pour tout arbre strict non vide.</li>
    <li><strong>Base</strong> (feuille) : n=1, f=1 ⇒ <code>1 = 2·1 − 1</code>, OK.</li>
    <li><strong>Induction</strong> : t=(a,g,d) strict interne, donc g≠∅ et d≠∅, et P(g), P(d) vraies :
      <br><code>n(g)=2f(g)−1</code>, <code>n(d)=2f(d)−1</code>, et <code>f(t)=f(g)+f(d)</code>.
      <div style="padding-left:10px">
        n(t) = 1 + n(g) + n(d)
             = 1 + (2f(g)−1) + (2f(d)−1)
             = 2(f(g)+f(d)) − 1
             = 2f(t) − 1.
      </div>
      <strong>Conclusion</strong> : identité vraie pour tout arbre binaire strict.
    </li>
  </ul>
  <p><em>Attention</em> : notre arbre d’exemple n’est pas strict, donc cette formule ne s’y applique pas (ici n=5, f=2 ⇒ 2f−1=3 ≠ 5).</p>
</div>

<div class="box answer">
  <h3>Résumé pratique (recette que tu peux réutiliser)</h3>
  <ol>
    <li><strong>Recopier la définition inductive</strong> (cas ∅ et cas (a,g,d)).</li>
    <li><strong>Choisir la propriété P(t)</strong> en observant comment h, n, f, ar se calculent à partir de g et d.</li>
    <li><strong>Base</strong> : prouver P(∅) (et P(feuille si besoin)).</li>
    <li><strong>Induction</strong> : supposer P(g) et P(d), puis exprimer tout sur (a,g,d) et conclure.</li>
    <li><strong>Vérifier sur 1–2 petits arbres</strong> pour « sentir » la propriété.</li>
  </ol>
</div>

<div class="box question">
  <h2>6) Exercice d’entraînement (facile, même méthode)</h2>
  <p>Montrer pour <em>tout</em> arbre (pas forcément strict) non vide : <code>ar(t) = n(t) − 1</code>.</p>
</div>

<div class="box explain">
  <h3>Indications</h3>
  <ul>
    <li>Base (feuille) : n=1 et ar=0 ⇒ OK.</li>
    <li>Induction : pour t=(a,g,d), écrire <code>n(t)=1+n(g)+n(d)</code> et <code>ar(t)=ar(g)+ar(d)+[g≠∅]+[d≠∅]</code>, puis utiliser les hypothèses d’induction sur g et d. Traiter les cas <code>g=∅</code> ou <code>d=∅</code> proprement (un seul enfant ⇒ on ajoute 1 seule arête).</li>
  </ul>
</div>


<h1>Exemple unique — Arbre binaire (version aérée + lisible)</h1>

<div class="box explain">
  <h2>1) Notations (claires et courtes)</h2>

  <p><strong>Arbres binaires — Définition inductive</strong></p>
  <ul>
    <li><em>Base</em> : ∅ est un arbre.</li>
    <li><em>Construction</em> : si <code>g</code> et <code>d</code> sont des arbres et <code>a</code> est une étiquette, alors <code>(a, g, d)</code> est un arbre (racine <code>a</code>, sous-arbre gauche <code>g</code>, sous-arbre droit <code>d</code>).</li>
  </ul>

  <br/>

  <p><strong>Fonctions standards (définies aussi par récurrence)</strong></p>
  <ul>
    <li>Hauteur : <code>h(∅)=0</code>, &nbsp; <code>h((a,g,d)) = 1 + max(h(g), h(d))</code>.</li>
    <li>Nombre de nœuds : <code>n(∅)=0</code>, &nbsp; <code>n((a,g,d)) = 1 + n(g) + n(d)</code>.</li>
    <li>Nombre de feuilles :
      <ul>
        <li><code>f(∅)=0</code>, &nbsp; <code>f((a,∅,∅))=1</code> (une feuille),</li>
        <li>sinon <code>f((a,g,d)) = f(g) + f(d)</code>.</li>
      </ul>
    </li>
    <li>Nombre d’arêtes : <code>ar(∅)=0</code>, &nbsp; <code>ar((a,g,d)) = ar(g)+ar(d) + [g≠∅] + [d≠∅]</code> (on ajoute 1 par enfant non vide).</li>
  </ul>

  <br/>

  <p><strong>Arbre binaire strict</strong> : non vide, et chaque nœud a soit 0 enfant, soit 2 enfants (jamais exactement 1).</p>
</div>

<hr/>

<div class="box explain">
  <h2>2) Choisir la « bonne » récurrence (recette rapide)</h2>

  <ol>
    <li><strong>Regarde la construction</strong> : tous les objets sont soit <code>∅</code>, soit <code>(a,g,d)</code> ⇒ ta preuve aura exactement ces deux cas.</li>
    <li><strong>Écris la propriété P(t)</strong> en termes de <code>g</code> et <code>d</code>.
      <br/>Exemples utiles :
      <ul>
        <li><code>n(t) ≤ 2<sup>h(t)</sup> − 1</code> (inégalité « puissance de 2 »),</li>
        <li><code>ar(t) = n(t) − 1</code> (identité structurelle),</li>
        <li><em>(strict)</em> <code>n(t) = 2·f(t) − 1</code> (lien nœuds ↔ feuilles).</li>
      </ul>
    </li>
    <li><strong>Base(s)</strong> : prouve P(∅) (et P(feuille) si nécessaire).</li>
    <li><strong>Étape</strong> : suppose P(g) et P(d), exprime tout pour <code>(a,g,d)</code>, puis conclue.</li>
  </ol>
</div>

<hr/>

<div class="box question">
  <h2>3) Un arbre d’exemple (on calcule tout)</h2>

  <pre>
            A
          /   \
         B     C
        / \   / \
       D  ∅  ∅  E
  </pre>

  <p>Forme inductive : <code>t = (A, (B, (D, ∅, ∅), ∅), (C, ∅, (E, ∅, ∅)))</code>.</p>

  <p><em>Remarque</em> : cet arbre n’est <strong>pas</strong> strict (B et C ont un seul enfant).</p>
</div>

<hr/>

<div class="box answer">
  <h2>4) Calcul pas à pas des notations sur cet arbre</h2>

  <p><strong>Hauteur</strong></p>
  <ul>
    <li>Feuilles : <code>h(D)=1</code>, <code>h(E)=1</code>.</li>
    <li><code>h(B)=1+max(h(D),0)=1+max(1,0)=2</code>.</li>
    <li><code>h(C)=1+max(0,h(E))=1+max(0,1)=2</code>.</li>
    <li><code>h(A)=1+max(h(B),h(C))=1+max(2,2)=3</code>.</li>
  </ul>

  <br/>

  <p><strong>Nombre de nœuds</strong></p>
  <ul>
    <li>Feuilles : <code>n(D)=1</code>, <code>n(E)=1</code>.</li>
    <li><code>n(B)=1+n(D)+0=2</code>, &nbsp; <code>n(C)=1+0+n(E)=2</code>.</li>
    <li><code>n(A)=1+n(B)+n(C)=1+2+2=5</code>.</li>
  </ul>

  <br/>

  <p><strong>Nombre de feuilles</strong></p>
  <ul>
    <li>Feuilles : <code>f(D)=1</code>, <code>f(E)=1</code>.</li>
    <li><code>f(B)=f(D)+f(∅)=1+0=1</code>, &nbsp; <code>f(C)=f(∅)+f(E)=0+1=1</code>.</li>
    <li><code>f(A)=f(B)+f(C)=1+1=2</code>.</li>
  </ul>

  <br/>

  <p><strong>Nombre d’arêtes</strong></p>
  <ul>
    <li>Feuilles : <code>ar(D)=0</code>, <code>ar(E)=0</code>.</li>
    <li><code>ar(B)=ar(D)+ar(∅)+[D≠∅]+[∅≠∅]=0+0+1+0=1</code>.</li>
    <li><code>ar(C)=ar(∅)+ar(E)+[∅≠∅]+[E≠∅]=0+0+0+1=1</code>.</li>
    <li><code>ar(A)=ar(B)+ar(C)+[B≠∅]+[C≠∅]=1+1+1+1=4</code>.</li>
  </ul>

  <br/>

  <p><strong>Vérification visuelle</strong> : 5 nœuds (A,B,C,D,E) et 4 arêtes (A–B, A–C, B–D, C–E) — cohérent.</p>
</div>

<hr/>

<div class="box explain">
  <h2>5) Preuve guidée — <code>n(t) ≤ 2<sup>h(t)</sup> − 1</code> (tous arbres)</h2>

  <p><em>Idée</em> : ajouter une racine au-dessus de <code>g</code> et <code>d</code> fait
    <code>h(t)=1+max(h(g),h(d))</code> et <code>n(t)=1+n(g)+n(d)</code>. Cette structure « colle » naturellement avec une borne en <code>2<sup>h</sup></code>.
  </p>

  <p><strong>Propriété</strong> P(t) : <code>n(t) ≤ 2<sup>h(t)</sup> − 1</code>.</p>

  <p><strong>Base</strong> : t=∅. <code>n=0</code>, <code>h=0</code> ⇒ <code>0 ≤ 2<sup>0</sup> − 1 = 0</code>.</p>

  <p><strong>Étape</strong> : t = (a,g,d).</p>
  <ul>
    <li>Hypothèses d’induction : <code>n(g) ≤ 2<sup>h(g)</sup> − 1</code> et <code>n(d) ≤ 2<sup>h(d)</sup> − 1</code>.</li>
    <li>Posons <code>M = max(h(g), h(d))</code> ⇒ <code>h(t) = M + 1</code>.</li>
    <li>Calcul :
      <div style="padding-left:12px; line-height:1.75;">
        <code>n(t) = 1 + n(g) + n(d)</code><br/>
        <code>≤ 1 + (2<sup>h(g)</sup> − 1) + (2<sup>h(d)</sup> − 1)</code><br/>
        <code>≤ 1 + (2<sup>M</sup> − 1) + (2<sup>M</sup> − 1)</code><br/>
        <code>= 2 · 2<sup>M</sup> − 1 = 2<sup>M+1</sup> − 1 = 2<sup>h(t)</sup> − 1</code>.
      </div>
    </li>
  </ul>

  <p><strong>Conclusion</strong> : P(t) est vraie pour tous les arbres par récurrence structurelle.</p>

  <p><strong>Test sur notre arbre</strong> : <code>h(t)=3</code>, <code>n(t)=5</code> ⇒ <code>5 ≤ 2<sup>3</sup> − 1 = 7</code> ✔</p>
</div>

<hr/>

<div class="box explain">
  <h2>6) Bonus — Arbres stricts : <code>n(t) = 2·f(t) − 1</code></h2>

  <p><em>Idée</em> : chaque nœud interne strict a 2 enfants — l’« équilibre » nœuds/feuilles donne l’identité.</p>

  <p><strong>Base</strong> (feuille) : <code>n=1</code>, <code>f=1</code> ⇒ <code>1 = 2·1 − 1</code>.</p>

  <p><strong>Étape</strong> : t=(a,g,d) strict interne (donc <code>g≠∅</code> et <code>d≠∅</code>).</p>
  <ul>
    <li>HI : <code>n(g)=2f(g)−1</code>, &nbsp; <code>n(d)=2f(d)−1</code>.</li>
    <li>Comme <code>f(t)=f(g)+f(d)</code> :
      <div style="padding-left:12px; line-height:1.75;">
        <code>n(t)=1+n(g)+n(d)</code><br/>
        <code>= 1 + (2f(g)−1) + (2f(d)−1)</code><br/>
        <code>= 2(f(g)+f(d)) − 1 = 2f(t) − 1</code>.
      </div>
    </li>
  </ul>

  <p><em>Attention</em> : notre arbre d’exemple n’est pas strict — cette formule ne s’y applique pas.</p>
</div>

<hr/>

<div class="box question">
  <h2>7) Exercice d’entraînement — <code>ar(t) = n(t) − 1</code> (arbres non vides)</h2>
</div>

<div class="box explain">
  <h3>Indications très courtes</h3>

  <p><strong>Base</strong> (feuille) : <code>n=1</code>, <code>ar=0</code> ⇒ <code>ar = n − 1</code>.</p>

  <p><strong>Étape</strong> : t=(a,g,d).</p>
  <ul>
    <li>Écris <code>n(t)=1+n(g)+n(d)</code>.</li>
    <li>Écris <code>ar(t)=ar(g)+ar(d)+[g≠∅]+[d≠∅]</code>.</li>
    <li>Applique l’HI à <code>g</code> et <code>d</code>, puis discute les cas « un seul enfant » vs « deux enfants » pour bien retomber sur <code>ar = n − 1</code>.</li>
  </ul>
</div>

<hr/>

<div class="box answer">
  <h2>8) Résumé-utilisateur (à répliquer à l’examen)</h2>

  <ol>
    <li>Je recopie la <strong>définition inductive</strong> (∅ et (a,g,d)).</li>
    <li>Je choisis une <strong>propriété P(t)</strong> exprimée via <code>g</code> et <code>d</code> (ex. <code>n(t) ≤ 2<sup>h(t)</sup> − 1</code>).</li>
    <li><strong>Bases</strong> : je prouve P(∅) (et P(feuille si besoin).</li>
    <li><strong>Étape</strong> : j’assume P(g), P(d), je traduis <code>n,h,f,ar</code> de <code>(a,g,d)</code> en fonction de <code>g,d</code>, j’aligne les calculs, je conclus.</li>
    <li>Je <strong>vérifie</strong> sur un petit arbre (comme ci-dessus) pour un « sanity check » rapide.</li>
  </ol>
</div>




---

<div class="box answer">
  <h2>Conclusion clé — Méthode unique pour 90% des questions</h2>
  <ol>
    <li><strong>Identifier l’objet</strong> : entier, mot (A*), liste, arbre, relation inductive, langage (Dyck), ordre (préfixe/lexico)…</li>
    <li><strong>Choisir la bonne induction</strong> :
      <ul>
        <li><em>ℕ</em> : simple (n→n+1) ou forte (tous k≤n).</li>
        <li><em>Objets construits</em> : <strong>induction structurelle</strong> (bases + constructeurs).</li>
        <li><em>Mesure qui diminue</em> (longueur, hauteur, etc.) : <strong>induction bien fondée</strong>.</li>
      </ul>
    </li>
    <li><strong>Écrire clairement la propriété P(·)</strong> avant la preuve (avec les notations exactes).</li>
    <li><strong>Dérouler</strong> : Bases → Pas d’induction (en suivant la <u>définition</u> de l’objet).</li>
    <li><strong>Conclure</strong> : une phrase explicite (“Donc, par induction, …”).</li>
  </ol>
</div>

<div class="box explain">
  <h2>Patrons très courts (à copier/coller)</h2>
  <pre><code>• ℕ (induction simple)
Base : P(0) (ou P(1)).
H.I. : P(n) vraie.
Pas : P(n) ⇒ P(n+1). Conclusion.

• ℕ (induction forte)
Base : P(0).
H.I. : P(k) vraie pour tous k ≤ n.
Pas : {P(k)} ⇒ P(n+1). Conclusion.

• Induction structurelle (mots/listes/arbres)
Bases : cas minimaux (ε, nil, feuille/∅).
Pas : IH sur sous-objets ⇒ propriété sur l’objet construit.

• Induction bien fondée (mesure m)
Base(s) : cas minimal(s).
Pas : IH pour tout y avec m(y) < m(x) ⇒ P(x). Conclusion.</code></pre>

</div>

<div class="box explain">
  <h2>Recettes par thème (ultra-concis)</h2>
  <h3>A) Mots (A*)</h3>
  <ul>
    <li>Classiques : |uv| = |u| + |v| ; ~ (~w) = w ; |~w| = |w| ; décomptes |w|<sub>a</sub>, |w|<sub>b</sub>.</li>
    <li><u>Induction structurelle</u> sur w : Base ε ; Pas u·a (on “ajoute 1 lettre”).</li>
  </ul>

  <h3>B) Langage de Dyck</h3>
  <ul>
    <li>Équivalence “définition inductive” ⇔ “comptage + tous les préfixes non négatifs”.</li>
    <li>Sens inductif : structurelle sur w = a·u·b·v.</li>
    <li>Sens inverse : bien fondée sur |w| en découpant au premier b qui ferme le a initial.</li>
  </ul>

  <h3>C) Ordres sur A*</h3>
  <ul>
    <li><strong>Préfixe</strong> : partiel et bien fondé. Définition “inductive” ⇔ “v = u·w”.</li>
    <li><strong>Lexicographique</strong> (alphabet total) : total mais en général pas bien fondé.</li>
  </ul>

  <h3>D) Listes</h3>
  <ul>
    <li>s(x|y) = s(x)+s(y) ; ℓ(x|y) = ℓ(x)+ℓ(y) ; ℓ(rev x)=ℓ(x) ; rev(rev x)=x.</li>
    <li>Induction structurelle sur la première liste (Base nil ; Pas n|x).</li>
  </ul>

  <h3>E) Arbres binaires</h3>
  <ul>
    <li>Hauteur : h(∅)=0 ; h(⟨g,a,d⟩)=1+max(h(g),h(d))</li>
    <li>Nœuds : n(∅)=0 ; n(⟨g,a,d⟩)=1+n(g)+n(d)</li>
    <li>Feuilles : f(∅)=0 ; f(•)=1 ; sinon f(⟨g,a,d⟩)=f(g)+f(d)</li>
    <li>Borne : n(t) ≤ 2<sup>h(t)</sup> − 1 ; (strict) n(t) = 2·f(t) − 1.</li>
  </ul>

  <h3>F) Relations inductives sur ℕ×ℕ (type Inf1/Inf2)</h3>
  <ul>
    <li>Idée : ces règles codent souvent “≤”. Prouver “règles ⇒ ≤” (lecture) et “≤ ⇒ règles” (construction).</li>
  </ul>
</div>

<hr/>

<div class="box question">
  <h2>Exemple 1 — Mots (langage L sur A={a,b})</h2>
  <p><strong>Définition de L</strong> : (B) b ∈ L. (I) si u∈L et v∈L, alors a·u·v ∈ L.</p>
  <ol>
    <li>Montrer : pour tout w∈L, <code>|w|<sub>b</sub> = |w|<sub>a</sub> + 1</code>.</li>
    <li>Montrer (sécurité des préfixes) : pour tout préfixe propre w′ de w, <code>|w′|<sub>a</sub> ≥ |w′|<sub>b</sub></code>.</li>
  </ol>
</div>

<div class="box answer">
  <h3>Solution guidée</h3>
  <p><strong>(1) Égalité globale</strong> — Induction structurelle.</p>
  <ul>
    <li><em>Base</em> : w=b ⇒ |a|=0, |b|=1 ⇒ OK.</li>
    <li><em>Pas</em> : w=a·u·v. IH : |u|<sub>b</sub>=|u|<sub>a</sub>+1 et |v|<sub>b</sub>=|v|<sub>a</sub>+1.
      <br/>Alors |w|<sub>a</sub>=1+|u|<sub>a</sub>+|v|<sub>a</sub>, et |w|<sub>b</sub>=|u|<sub>b</sub>+|v|<sub>b</sub> = (|u|<sub>a</sub>+1)+(|v|<sub>a</sub>+1) = |w|<sub>a</sub>+1.</li>
  </ul>

  <p><strong>(2) Préfixes non négatifs</strong> — Induction structurelle sur w.</p>
  <ul>
    <li><em>Base</em> : w=b. Préfixe propre seul : ε ⇒ 0≥0.</li>
    <li><em>Pas</em> : w=a·u·v. Un préfixe propre w′ est soit ε, soit “a”, soit “a·x” (x préfixe propre de u), soit “a·u·y” (y préfixe propre de v).
      <ul>
        <li>ε : 0≥0. “a” : 1≥0.</li>
        <li>a·x : |a| − |b| = 1 + (|x|<sub>a</sub> − |x|<sub>b</sub>) ≥ 1 + 0.</li>
        <li>a·u·y : (1 + |u|<sub>a</sub> + |y|<sub>a</sub>) − (|u|<sub>b</sub> + |y|<sub>b</sub>) = (|y|<sub>a</sub> − |y|<sub>b</sub>) ≥ 0 (car IH sur y et (1)).</li>
      </ul>
    </li>
  </ul>

  <p><strong>Exemple</strong> : u=b, v=b ⇒ w=a·b·b : |a|=1, |b|=2 et tous les préfixes respectent (2).</p>
</div>

<hr/>

<div class="box question">
  <h2>Exemple 2 — Dyck (deux sens)</h2>
  <p><strong>But</strong> : “Définition inductive” ⇔ “compte |·|<sub>a</sub>=|·|<sub>b</sub> et tous les préfixes vérifient |·|<sub>a</sub> ≥ |·|<sub>b</sub>”.</p>
</div>

<div class="box answer">
  <h3>Plan court</h3>
  <ul>
    <li><strong>Sens inductif → conditions</strong> (structurelle) : Base ε : OK. Pas w=a·u·b·v : additionner les comptes ; pour les préfixes, séparer en “avant a”, “dans u”, “après b”, et appliquer les IH sur u et v.</li>
    <li><strong>Conditions → sens inductif</strong> (bien fondée) : si w≠ε, il commence par a et a un premier b qui ferme ce a : écrire w=a·u·b·v ; les conditions se transmettent à u et v (plus courts) ⇒ IH ⇒ reconstruire par la règle inductive.</li>
  </ul>
</div>

<hr/>

<div class="box question">
  <h2>Exemple 3 — Ordre préfixe : deux définitions équivalentes</h2>
  <p><strong>D1</strong> (inductive) : ε ≤ v ; si u ≤ v alors a·u ≤ a·v. &nbsp;&nbsp;
     <strong>D2</strong> (concaténation) : u ≤ v ⇔ ∃w, v = u·w.</p>
</div>

<div class="box answer">
  <h3>Preuve en deux sens (très guidée)</h3>
  <ul>
    <li><strong>D2 ⇒ D1</strong> : si v = u·w, on fait une induction sur la <em>dérivation</em> induite par D1 : Base ε ≤ v (prendre w=v). Pas : si a·u ≤ a·v et v = u·w, alors a·v = (a·u)·w ⇒ la règle inductive est satisfaite.</li>
    <li><strong>D1 ⇒ D2</strong> : récurrence sur |w| tel que v = u·w. Base w=ε ⇒ v=u. Pas w=a·x ⇒ v=u·a·x ; appliquer la règle inductive “remonte” la lettre a, puis IH sur x.</li>
  </ul>
</div>

<hr/>

<div class="box question">
  <h2>Exemple 4 — Arbres binaires</h2>
  <p><strong>Propriété</strong> : pour tout arbre t, <code>n(t) ≤ 2<sup>h(t)</sup> − 1</code>.</p>
</div>

<div class="box answer">
  <h3>Preuve ultra claire</h3>
  <ul>
    <li><strong>Bases</strong> : t=∅ ⇒ n=0, h=0 ⇒ 0 ≤ 2<sup>0</sup>−1=0.</li>
    <li><strong>Pas</strong> : t=⟨g,a,d⟩. IH : n(g) ≤ 2<sup>h(g)</sup>−1 et n(d) ≤ 2<sup>h(d)</sup>−1.
      <br/>Poser M=max(h(g),h(d)) ⇒ h(t)=M+1.
      <div style="padding-left:10px">
        n(t)=1+n(g)+n(d) ≤ 1+(2<sup>h(g)</sup>−1)+(2<sup>h(d)</sup>−1) ≤ 2·2<sup>M</sup>−1 = 2<sup>M+1</sup>−1 = 2<sup>h(t)</sup>−1.
      </div>
    </li>
  </ul>
</div>

<hr/>

<div class="box explain">
  <h2>Auto-contrôle express (20 s)</h2>
  <ul>
    <li>P(·) bien écrite ? (avec |·|, h, n, f, etc.).</li>
    <li>Tous les cas de base traités (ε / nil / ∅ / feuille) ?</li>
    <li>Pas : j’utilise <u>exactement</u> les constructeurs (u·a / n|x / ⟨g,a,d⟩).</li>
    <li>Conclusion écrite clairement (“par induction …”).</li>
  </ul>
</div>

<div class="box answer">
  <h2>Résumé en 5 lignes</h2>
  <ul>
    <li>Choisis l’induction adaptée (ℕ / structurelle / bien fondée).</li>
    <li>Écris P(·) avant de commencer.</li>
    <li>Suis la définition : bases puis constructeurs.</li>
    <li>Pour Dyck : “première fermeture” ; pour préfixe : D1⇔D2 ; pour arbres : h via max, n via addition.</li>
    <li>Conclue toujours par une phrase de fin.</li>
  </ul>
</div>

