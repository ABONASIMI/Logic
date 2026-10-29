Logic.reg("lesson:w04_revision:fr", {
  id: "w04_revision",
  lang: "fr",
  status: "complete",
  html: "\n<div class=\"box box-objectives\">\n  <div class=\"box-title\">Fiche de Révision Express — Semaine 4 (SAT & DPLL)</div>\n  <p>Rappels essentiels pour l'examen sur DPLL.</p>\n</div>\n\n<h2 id=\"w04-rev-dpll\">Points Clés de l'Algorithme DPLL</h2>\n<ul>\n  <li><strong>Propagation unitaire prioritaire :</strong> Toujours exécuter TOUTES les propagations unitaires possibles avant de faire le moindre branchement.</li>\n  <li><strong>Clause vide {{ \\Box }} = Backtracking :</strong> Dès qu'une clause devient vide, la branche échoue immédiatement.</li>\n  <li><strong>Ensemble vide {{ \\emptyset }} = SAT :</strong> Dès que toutes les clauses ont disparu, la formule est satisfiable.</li>\n</ul>\n"
});
