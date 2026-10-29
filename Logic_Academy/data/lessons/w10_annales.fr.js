Logic.reg("lesson:w10_annales:fr", {
  id: "w10_annales",
  lang: "fr",
  status: "complete",
  html: "\n<div class=\"box box-objectives\">\n  <div class=\"box-title\">Annales & Sujets Types — Semaine 10 (Résolution & Unification)</div>\n  <p>Les examens écrits finaux de Sorbonne Université se concentrent sur les thèmes 1 à 9, tandis que la résolution et Prolog sont évalués en contrôle continu (TME noté et devoirs surveillés). Voici les exercices types d'évaluation.</p>\n</div>\n\n<h2 id=\"w10-ann-ex1\">Exercice Type 1 — Unification de Robinson avec Occurs Check</h2>\n<div class=\"box box-enonce\">\n  <div class=\"box-title\">Énoncé</div>\n  <p>Appliquer l'algorithme de Robinson pour trouver le mgu du système :</p>\n  {{ \\{ f(x, g(y)) \\doteq f(h(z), x), \\quad y \\doteq a \\} }}\n</div>\n<div class=\"box box-solution\">\n  <div class=\"box-title\">Correction</div>\n  <p>1. Décomposition sur {{ f }} : {{ x \\doteq h(z) }} et {{ g(y) \\doteq x }}.</p>\n  <p>2. Remplacement de {{ x }} par {{ h(z) }} : {{ g(y) \\doteq h(z) }}.</p>\n  <p>3. Clash entre les symboles de fonction {{ g }} et {{ h }} : <strong>ÉCHEC d'unification !</strong></p>\n</div>\n"
});
