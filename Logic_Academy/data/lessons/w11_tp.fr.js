Logic.reg("lesson:w11_tp:fr", {
  id: "w11_tp",
  lang: "fr",
  status: "complete",
  html: "\n<div class=\"box box-objectives\">\n  <div class=\"box-title\">TP Thème 11 — Listes et Applications Prolog (Exercices 19, 20 et 21)</div>\n  <p>Source : <code>main_tp-etudiants.pdf</code>, pages 19–24. Pratique avancée des listes en Prolog.</p>\n</div>\n\n<h2 id=\"w11-tp-ex20\">Exercice 20 — Manipulation de Listes</h2>\n<pre><code>% Deuxième élément\ndeuxieme([_, X | _], X).\n\n% Avant-dernier élément\navantDernier([X, _], X).\navantDernier([_ | Q], X) :- avantDernier(Q, X).\n\n% Inversion de liste (version avec accumulateur O(n))\ninverse(L, Res) :- inv_acc(L, [], Res).\ninv_acc([], Acc, Acc).\ninv_acc([T | Q], Acc, Res) :- inv_acc(Q, [T | Acc], Res).</code></pre>\n\n<h2 id=\"w11-tp-ex21\">Exercice 21 — Menus et Listes de Courses</h2>\n<pre><code>entree(salade). entree(avocat).\nplat(poulet). plat(saumon).\ndessert(pomme). dessert(yaourt).\n\nmenuValide([E, P, D]) :- entree(E), plat(P), dessert(D).</code></pre>\n"
});
