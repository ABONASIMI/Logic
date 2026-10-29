#!/usr/bin/env python3
"""Authoring generator for Week 7 Cours (Thème 7 : Syntaxe de la LPPO).
Covers:
- Limites du calcul propositionnel et passage au premier ordre
- Signature <X, F, P> et arités
- Définition inductive des termes T_0, T_k, T(X, F)
- Distinction fondamentale Termes (objets) vs Formules (valeurs de vérité)
- Portée des quantificateurs, occurrences libres/liées, Free(F), formules closes et clôture universelle
- Capture de variables et alpha-renommage sans capture
"""
import os

W07 = '/home/mnasimi/sorbonne/Logic/Logic_Academy/content/w07'
os.makedirs(W07, exist_ok=True)

fr = r"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>Thème 7 : Logique des Prédicats du Premier Ordre (LPPO) — Syntaxe</h1>
  <p class="lead">Du calcul propositionnel à la logique du premier ordre : signature {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }}, hiérarchie inductive des termes {{ \mathcal{T}_k }}, formules quantifiées, variables libres {{ \text{Free}(F) }}, clôture universelle et {{ \alpha }}-renommage sans capture.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du cours</h3>
  <ul>
    <li><a href="#sec1">1. Pourquoi dépasser le calcul propositionnel ?</a></li>
    <li><a href="#sec2">2. Signature du premier ordre {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} et arités</a></li>
    <li><a href="#sec3">3. Définition inductive des termes : {{ \mathcal{T}_0 }}, {{ \mathcal{T}_k }} et {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</a></li>
    <li><a href="#sec4">4. Formules de la LPPO et distinction Termes vs Formules</a></li>
    <li><a href="#sec5">5. Portée, variables libres {{ \text{Free}(F) }} et clôture universelle {{ \tilde{\forall} F }}</a></li>
    <li><a href="#sec6">6. Capture de variables et {{ \alpha }}-renommage canonique</a></li>
  </ul>
</div>

<h2 id="sec1">1. Pourquoi dépasser le calcul propositionnel ?</h2>

<div class="box info">
  <h4>Le syllogisme de Socrate et l'opacité des propositions atomiques</h4>
  <p>Considérons le célèbre raisonnement : <em>« Tous les hommes sont mortels ; or Socrate est un homme ; donc Socrate est mortel. »</em></p>
  <p>En logique propositionnelle (Thèmes 1 à 6), chaque phrase déclarative sans connecteur est traduite par une variable propositionnelle atomique distincte :</p>
  <ul>
    <li>{{ p }} : « Tous les hommes sont mortels »</li>
    <li>{{ q }} : « Socrate est un homme »</li>
    <li>{{ r }} : « Socrate est mortel »</li>
  </ul>
  <p>La formalisation propositionnelle donne le séquent {{ p, q \models r }}. Or ce séquent est <strong>faux</strong> en logique propositionnelle (il suffit de choisir l'interprétation {{ I(p) = 1 }}, {{ I(q) = 1 }} et {{ I(r) = 0 }}) ! Le calcul propositionnel est incapable de voir la structure interne des phrases : il ignore que « Socrate » est un individu particulier parmi « tous les hommes ».</p>
  <p>La <strong>Logique des Prédicats du Premier Ordre (LPPO)</strong> ouvre la boîte noire des propositions atomiques en distinguant les <strong>objets</strong> (individus, constantes, fonctions) et les <strong>propriétés ou relations</strong> (prédicats) portant sur ces objets, tout en quantifiant sur les individus grâce à {{ \forall }} (pour tout) et {{ \exists }} (il existe) :</p>
  <p style="text-align:center;">{{ \forall x \, (\text{homme}(x) \Rightarrow \text{mortel}(x)), \; \text{homme}(\text{socrate}) \models \text{mortel}(\text{socrate}) }}</p>
</div>

<h2 id="sec2">2. Signature du premier ordre {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} et arités</h2>

<div class="box def">
  <h4>Alphabet et Signature d'un langage du premier ordre (Cours 7, Slides 4–8)</h4>
  <p>Un langage du premier ordre est paramétré par un triplet {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} appelé <strong>signature</strong> (ou vocabulaire), composé de trois ensembles disjoints deux à deux :</p>
  <ol>
    <li><strong>L'ensemble des variables d'individu {{ \mathcal{X} }} :</strong> un ensemble infini dénombrable de symboles de variables {{ \{x, y, z, x_1, x_2, \dots\} }}. Chaque variable désigne un individu générique du domaine.</li>
    <li><strong>L'ensemble des symboles de fonction {{ \mathcal{F} = \bigcup_{n \in \mathbb{N}} \mathcal{F}_n }} :</strong> gradué selon l'<strong>arité</strong> {{ n \in \mathbb{N} }} (le nombre d'arguments) :
      <ul>
        <li>Pour {{ n = 0 }}, {{ \mathcal{F}_0 }} est l'ensemble des <strong>symboles de constante</strong> (ex : {{ a, b, c, 0, \text{socrate} }}). Une constante est une fonction d'arité {{ 0 }} qui s'écrit sans parenthèses.</li>
        <li>Pour {{ n \ge 1 }}, {{ \mathcal{F}_n }} est l'ensemble des symboles de fonction d'arité {{ n }} (ex : {{ s \in \mathcal{F}_1 }} pour le successeur {{ s(x) }}, {{ \text{plus} \in \mathcal{F}_2 }} pour {{ \text{plus}(x, y) }}).</li>
      </ul>
    </li>
    <li><strong>L'ensemble des symboles de prédicat (ou de relation) {{ \mathcal{P} = \bigcup_{n \in \mathbb{N}} \mathcal{P}_n }} :</strong> gradué selon l'arité {{ n \in \mathbb{N} }} :
      <ul>
        <li>Pour {{ n = 0 }}, {{ \mathcal{P}_0 }} est l'ensemble des variables propositionnelles (prédicats sans argument, retrouvant la logique propositionnelle comme cas particulier).</li>
        <li>Pour {{ n \ge 1 }}, {{ \mathcal{P}_n }} est l'ensemble des prédicats d'arité {{ n }} (ex : {{ \text{pair} \in \mathcal{P}_1 }}, {{ \text{inf} \in \mathcal{P}_2 }}, {{ \text{entre} \in \mathcal{P}_3 }}). En particulier, le symbole d'égalité {{ = }} est un prédicat binaire distingué {{ \text{egal} \in \mathcal{P}_2 }}.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box method">
  <h4>Méthode d'examen : Déterminer la nature et l'arité des symboles par inspection</h4>
  <p>Dans une formule bien formée {{ F }} (cf. TD Exercice 24), on identifie le rôle et l'arité de chaque symbole par sa position dans l'arbre syntaxique :</p>
  <ul>
    <li>Un symbole placé <strong>directement sous un connecteur logique</strong> ({{ \neg, \land, \lor, \Rightarrow, \Leftrightarrow }}) ou <strong>immédiatement comme corps d'un quantificateur</strong> ({{ \forall x \, \dots }}, {{ \exists x \, \dots }}) est obligatoirement un <strong>symbole de prédicat</strong> {{ p \in \mathcal{P}_n }}, où {{ n }} est le nombre d'arguments entre ses parenthèses.</li>
    <li>Un symbole placé <strong>à l'intérieur des arguments d'un prédicat ou d'une autre fonction</strong> est soit une variable {{ x \in \mathcal{X} }} (s'il est lié par un quantificateur ou listé dans {{ \mathcal{X} }}), soit une constante {{ c \in \mathcal{F}_0 }} (s'il n'a pas de parenthèses et n'est pas dans {{ \mathcal{X} }}), soit un <strong>symbole de fonction</strong> {{ f \in \mathcal{F}_n }} de {{ n \ge 1 }} arguments.</li>
  </ul>
</div>

<h2 id="sec3">3. Définition inductive des termes : {{ \mathcal{T}_0 }}, {{ \mathcal{T}_k }} et {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</h2>

<div class="box def">
  <h4>Hiérarchie des termes {{ \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }} et ensemble {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} (Cours 7, Slides 9–14)</h4>
  <p>Les <strong>termes</strong> sont les expressions syntaxiques qui désignent des objets (individus) du domaine. On définit d'abord par récurrence sur {{ k \in \mathbb{N} }} la famille des ensembles {{ \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }} des termes de profondeur (hauteur d'imbrication de fonctions) au plus {{ k }} :</p>
  <ul>
    <li><strong>Étape de base ({{ k = 0 }}, termes atomiques) :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}_0(\mathcal{X}, \mathcal{F}) = \mathcal{X} \cup \mathcal{F}_0 }}</div>
      Un terme de hauteur {{ 0 }} est uniquement une variable d'individu ou un symbole de constante.</li>
    <li><strong>Étape de récurrence ({{ k \to k+1 }}) :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}_{k+1}(\mathcal{X}, \mathcal{F}) = \mathcal{T}_k(\mathcal{X}, \mathcal{F}) \cup \left\{ f(t_1, \dots, t_n) \;\middle|\; n \ge 1, \, f \in \mathcal{F}_n \text{ et } t_1, \dots, t_n \in \mathcal{T}_k(\mathcal{X}, \mathcal{F}) \right\} }}</div>
    </li>
    <li><strong>Ensemble total des termes :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}(\mathcal{X}, \mathcal{F}) = \bigcup_{k \in \mathbb{N}} \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }}</div>
    </li>
  </ul>
  <p><strong>Définition inductive équivalente de {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} :</strong> {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} est le plus petit ensemble tel que :</p>
  <ol>
    <li><strong>Base :</strong> Toute variable {{ x \in \mathcal{X} }} est un terme ({{ x \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}) et toute constante {{ c \in \mathcal{F}_0 }} est un terme ({{ c \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}).</li>
    <li><strong>Induction :</strong> Si {{ f \in \mathcal{F}_n }} ({{ n \ge 1 }}) et {{ t_1, \dots, t_n \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}, alors {{ f(t_1, \dots, t_n) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}.</li>
  </ol>
  <p><strong>Terme clos (ou terme fermé / ground term) :</strong> Un terme sans aucune variable appartient à {{ \mathcal{T}(\emptyset, \mathcal{F}) }}, noté simplement {{ \mathcal{T}_0(\mathcal{F}) }} dans le polycopié de TD (attention : dans l'Exercice 22 du TD, {{ \mathcal{T}_0(\mathcal{F}) }} désigne l'ensemble de tous les termes clos construits sur {{ \mathcal{F} }} sans variables).</p>
</div>

<h2 id="sec4">4. Formules de la LPPO et distinction Termes vs Formules</h2>

<div class="box def">
  <h4>Définition inductive de l'ensemble des formules {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} (Cours 7, Slides 15–19)</h4>
  <p>L'ensemble {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} des formules de la logique des prédicats est le plus petit ensemble vérifiant :</p>
  <ol>
    <li><strong>Formules atomiques (Atomes) :</strong>
      <ul>
        <li> {{ \top \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} et {{ \bot \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} ;</li>
        <li> Si {{ p \in \mathcal{P}_0 }}, alors {{ p \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} ;</li>
        <li> Si {{ p \in \mathcal{P}_n }} ({{ n \ge 1 }}) et si {{ t_1, \dots, t_n \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} sont des <strong>termes</strong>, alors {{ p(t_1, \dots, t_n) \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }}.</li>
      </ul>
    </li>
    <li><strong>Connecteurs propositionnels :</strong> Si {{ F, G \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }}, alors {{ (\neg F) }}, {{ (F \land G) }}, {{ (F \lor G) }}, {{ (F \Rightarrow G) }} et {{ (F \Leftrightarrow G) }} appartiennent à {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }}.</li>
    <li><strong>Quantificateurs :</strong> Si {{ x \in \mathcal{X} }} est une <strong>variable</strong> et {{ F \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} est une formule, alors {{ (\forall x \, F) }} et {{ (\exists x \, F) }} appartiennent à {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }}.</li>
  </ol>
</div>

<div class="box warn">
  <h4>Frontière infranchissable : Termes (individus) vs Formules (vérité)</h4>
  <p>En LPPO, il est formellement interdit de mélanger les catégories grammaticales :</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>Catégorie</th>
        <th>Rôle sémantique</th>
        <th>Construit avec</th>
        <th>Exemples valides</th>
        <th>Erreurs graves (Syntaxiquement illégales)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Terme</strong> {{ t \in \mathcal{T} }}</td>
        <td>Désigne un <strong>objet</strong> du domaine {{ D }}</td>
        <td>Variables {{ \mathcal{X} }}, constantes {{ \mathcal{F}_0 }}, fonctions {{ f \in \mathcal{F}_n }}</td>
        <td>{{ x }}, {{ a }}, {{ s(s(a)) }}, {{ f(x, g(y)) }}</td>
        <td>{{ f(p(x)) }} <em>(prédicat dans fonction)</em>,<br/>{{ x \land y }} <em>(connecteur sur termes)</em></td>
      </tr>
      <tr>
        <td><strong>Formule</strong> {{ F \in \mathbb{F} }}</td>
        <td>Désigne une <strong>valeur de vérité</strong> {{ \{0, 1\} }}</td>
        <td>Prédicats {{ p(t_1,\dots,t_n) }}, connecteurs, {{ \forall x }}, {{ \exists x }}</td>
        <td>{{ p(f(x)) }}, {{ \forall x \, (p(x) \Rightarrow q(x, a)) }}</td>
        <td>{{ \forall f(x) \, p(x) }} <em>(quantifier un terme non-variable)</em>,<br/>{{ f(x) \Rightarrow p(x) }} <em>(terme sous {{ \Rightarrow }})</em></td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec5">5. Portée, variables libres {{ \text{Free}(F) }} et clôture universelle {{ \tilde{\forall} F }}</h2>

<div class="box def">
  <h4>Portée d'un quantificateur, occurrences libres et liées (Cours 7, Slides 21–27)</h4>
  <p>Dans une formule {{ Q x \, G }} (où {{ Q \in \{\forall, \exists\} }}), la sous-formule {{ G }} est appelée la <strong>portée</strong> (scope) du quantificateur {{ Q x }}. Dans l'arbre syntaxique de {{ F }}, la portée de {{ Q x }} correspond exactement au sous-arbre enraciné sous le nœud {{ Q x }}.</p>
  <ul>
    <li>Une occurrence d'une variable {{ x }} dans {{ F }} est dite <strong>liée</strong> (bound) si elle se situe dans la portée d'un quantificateur {{ \forall x }} ou {{ \exists x }} (elle est liée au quantificateur {{ Q x }} le plus proche en remontant vers la racine de l'arbre syntaxique).</li>
    <li>Une occurrence de {{ x }} qui n'est dans la portée d'aucun {{ \forall x }} ni {{ \exists x }} est dite <strong>libre</strong> (free).</li>
  </ul>
  <p><strong>Attention :</strong> Une même variable {{ x }} peut avoir <em>à la fois</em> des occurrences liées et des occurrences libres dans une même formule {{ F }} ! Par exemple, dans {{ F = (\forall x \, p(x)) \land q(x) }}, l'occurrence de {{ x }} dans {{ p(x) }} est liée par {{ \forall x }}, mais l'occurrence de {{ x }} dans {{ q(x) }} est <strong>libre</strong> car elle est en dehors de la portée de {{ \forall x }}. Ainsi {{ x \in \text{Free}(F) }}.</p>
</div>

<div class="box method">
  <h4>Calcul inductif de l'ensemble des variables libres {{ \text{Free}(F) }}</h4>
  <p>On note {{ \text{Var}(t) }} l'ensemble des variables apparaissant dans un terme {{ t }}, et {{ \text{Free}(F) }} l'ensemble des variables possédant <strong>au moins une occurrence libre</strong> dans {{ F }} :</p>
  <ul>
    <li>{{ \text{Free}(\top) = \text{Free}(\bot) = \emptyset }}, et pour {{ p \in \mathcal{P}_0 }}, {{ \text{Free}(p) = \emptyset }} ;</li>
    <li>Pour un atome {{ p(t_1, \dots, t_n) }} : {{ \text{Free}(p(t_1, \dots, t_n)) = \text{Var}(t_1) \cup \dots \cup \text{Var}(t_n) }} ;</li>
    <li>{{ \text{Free}(\neg F) = \text{Free}(F) }} ;</li>
    <li>Pour {{ \diamond \in \{\land, \lor, \Rightarrow, \Leftrightarrow\} }} : {{ \text{Free}(F_1 \diamond F_2) = \text{Free}(F_1) \cup \text{Free}(F_2) }} ;</li>
    <li><strong>Cas crucial des quantificateurs :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \text{Free}(\forall x \, G) = \text{Free}(G) \setminus \{x\} \qquad \text{et} \qquad \text{Free}(\exists x \, G) = \text{Free}(G) \setminus \{x\} }}</div>
    </li>
  </ul>
  <p><strong>Formule close (ou fermée) :</strong> Une formule {{ F }} est dite <strong>close</strong> si {{ \text{Free}(F) = \emptyset }}.</p>
  <p><strong>Clôture universelle {{ \tilde{\forall} F }} :</strong> Si {{ \text{Free}(F) = \{x_1, \dots, x_k\} }}, une <strong>clôture universelle</strong> de {{ F }} est la formule close obtenue en préfixant {{ F }} par des quantificateurs universels sur toutes ses variables libres : {{ \tilde{\forall} F = \forall x_1 \dots \forall x_k \, F }} (l'ordre des {{ \forall x_i }} n'a pas d'importance sémantique).</p>
</div>

<h2 id="sec6">6. Capture de variables et {{ \alpha }}-renommage canonique</h2>

<div class="box tip">
  <h4>Règle d'{{ \alpha }}-renommage sans capture et forme normale de variables (Cours 7, Slides 28–32)</h4>
  <p>Une variable liée par un quantificateur est une <em>variable muette</em> (comme l'indice {{ i }} dans {{ \sum_{i=1}^n i }}). On peut renommer la variable liée d'une sous-formule {{ Q x \, G }} en une nouvelle variable {{ y }} pour obtenir {{ Q y \, G[x \leftarrow y] }} (qui lui est logiquement équivalente) <strong>à la double condition impérative de non-capture</strong> :</p>
  <ol>
    <li><strong>Pas de capture d'une variable libre existante :</strong> {{ y \notin \text{Free}(G) }} (sinon les occurrences libres de {{ y }} dans {{ G }} seraient capturées par le nouveau quantificateur {{ Q y }}).</li>
    <li><strong>Pas de capture par un quantificateur interne :</strong> aucune occurrence libre de {{ x }} dans {{ G }} ne doit se trouver dans la portée d'un sous-quantificateur {{ \forall y }} ou {{ \exists y }} interne à {{ G }}.</li>
  </ol>
  <p><strong>Mise sous forme canonique (variables de quantification distinctes) :</strong> En examen (cf. TD Exercices 24 et 25), on demande souvent de renommer les variables liées d'une formule {{ F }} pour obtenir une formule équivalente {{ F' }} dans laquelle :</p>
  <ul>
    <li>deux quantificateurs distincts portent toujours sur des variables différentes ;</li>
    <li>aucune variable n'apparaît à la fois libre et liée dans {{ F' }}.</li>
  </ul>
  <p>Pour y parvenir sans jamais risquer de capture, il suffit de choisir pour chaque quantificateur {{ Q x }} à renommer une <strong>variable fraîche</strong> {{ x_i }} qui n'apparaît nulle part ailleurs dans la formule !</p>
</div>
"""

fa = r"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>فصل ۷: منطق محمولات مرتبه اول (LPPO) — نحو (Syntaxe)</h1>
  <p class="lead">گذر از منطق گزاره‌ای به منطق مرتبه اول: امضای زبان {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }}، سلسله‌مراتب استقرایی ترم‌ها {{ \mathcal{T}_k }}، فرمول‌های سوردار، متغیرهای آزاد {{ \text{Free}(F) }}، بستار کلی و {{ \alpha }}-تغییرنام بدون تله اسارت.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب درس</h3>
  <ul>
    <li><a href="#sec1">۱. چرا باید از منطق گزاره‌ای فراتر رفت؟</a></li>
    <li><a href="#sec2">۲. امضای مرتبه اول {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} و ظرفیت نمادها (Arité)</a></li>
    <li><a href="#sec3">۳. تعریف استقرایی ترم‌ها: {{ \mathcal{T}_0 }}، {{ \mathcal{T}_k }} و {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</a></li>
    <li><a href="#sec4">۴. فرمول‌های LPPO و مرز بنیادین میان ترم و فرمول</a></li>
    <li><a href="#sec5">۵. دامنه سور، متغیرهای آزاد {{ \text{Free}(F) }} و بستار کلی {{ \tilde{\forall} F }}</a></li>
    <li><a href="#sec6">۶. اسارت متغیرها و {{ \alpha }}-تغییرنام استاندارد</a></li>
  </ul>
</div>

<h2 id="sec1">1. Pourquoi dépasser le calcul propositionnel ?</h2>

<div class="box info">
  <h4>قیاس سقراط و محدودیت جعبه‌سیاه در گزاره‌های اتمی</h4>
  <p>استدلال کلاسیک زیر را در نظر بگیرید: <em>«هر انسانی فانی است؛ سقراط انسان است؛ پس سقراط فانی است.»</em></p>
  <p>در منطق گزاره‌ای (فصل‌های ۱ تا ۶)، هر جمله خبری ساده با یک متغیر گزاره‌ای مستقل مدل‌سازی می‌شود:</p>
  <ul>
    <li>{{ p }} : «هر انسانی فانی است»</li>
    <li>{{ q }} : «سقراط انسان است»</li>
    <li>{{ r }} : «سقراط فانی است»</li>
  </ul>
  <p>ترجمه گزاره‌ای این استدلال به صورت {{ p, q \models r }} خواهد بود. اما این استلزام در منطق گزاره‌ای <strong>نادرست</strong> است (کافی است تعبیر {{ I(p) = 1 }}، {{ I(q) = 1 }} و {{ I(r) = 0 }} را اختیار کنیم)! منطق گزاره‌ای قادر به دیدن ساختار درونی جملات نیست و نمی‌فهمد که «سقراط» مصداقی از «انسان‌ها» است.</p>
  <p><strong>منطق محمولات مرتبه اول (LPPO)</strong> جعبه سیاه اتم‌ها را می‌گشاید و میان <strong>اشیاء</strong> (افراد، ثابت‌ها، توابع) و <strong>ویژگی‌ها یا رابطه‌ها</strong> (محمول‌ها) تمایز می‌گذارد و امکان سوربندی با {{ \forall }} (به ازای هر) و {{ \exists }} (وجود دارد) را فراهم می‌سازد:</p>
  <p style="text-align:center;">{{ \forall x \, (\text{homme}(x) \Rightarrow \text{mortel}(x)), \; \text{homme}(\text{socrate}) \models \text{mortel}(\text{socrate}) }}</p>
</div>

<h2 id="sec2">2. Signature du premier ordre {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} et arités</h2>

<div class="box def">
  <h4>الفبا و امضای زبان مرتبه اول (درس ۷، اسلایدهای ۴ تا ۸)</h4>
  <p>هر زبان مرتبه اول با یک سه‌تایی {{ \langle \mathcal{X}, \mathcal{F}, \mathcal{P} \rangle }} به نام <strong>امضا</strong> (Signature) مشخص می‌شود که شامل سه مجموعه دوبه‌دو مجزا است:</p>
  <ol>
    <li><strong>مجموعه متغیرهای فردی {{ \mathcal{X} }} :</strong> مجموعه‌ای نامتناهی و شمارا از نمادهای متغیر {{ \{x, y, z, x_1, x_2, \dots\} }}. هر متغیر نماینده یک فرد یا شیء از دامنه است.</li>
    <li><strong>مجموعه نمادهای تابعی {{ \mathcal{F} = \bigcup_{n \in \mathbb{N}} \mathcal{F}_n }} :</strong> دسته‌بندی‌شده بر اساس <strong>ظرفیت یا تعداد آرگومان‌ها</strong> (Arité) {{ n \in \mathbb{N} }} :
      <ul>
        <li>برای {{ n = 0 }}، مجموعه {{ \mathcal{F}_0 }} شامل <strong>نمادهای ثابت</strong> است (مانند {{ a, b, c, 0, \text{socrate} }}). ثابت در واقع تابعی با ظرفیت {{ 0 }} است که بدون پرانتز نوشته می‌شود.</li>
        <li>برای {{ n \ge 1 }}، مجموعه {{ \mathcal{F}_n }} شامل نمادهای تابعی {{ n }}-آرگومانی است (مانند {{ s \in \mathcal{F}_1 }} برای تابع تالی {{ s(x) }}، و {{ \text{plus} \in \mathcal{F}_2 }} برای {{ \text{plus}(x, y) }}).</li>
      </ul>
    </li>
    <li><strong>مجموعه نمادهای محمول (یا رابطه) {{ \mathcal{P} = \bigcup_{n \in \mathbb{N}} \mathcal{P}_n }} :</strong> دسته‌بندی‌شده بر حسب ظرفیت {{ n \in \mathbb{N} }} :
      <ul>
        <li>برای {{ n = 0 }}، مجموعه {{ \mathcal{P}_0 }} همان متغیرهای گزاره‌ای بدون آرگومان است (که منطق گزاره‌ای را به عنوان حالت خاص در دل خود جای می‌دهد).</li>
        <li>برای {{ n \ge 1 }}، مجموعه {{ \mathcal{P}_n }} شامل محمول‌های {{ n }}-تایی است (مانند {{ \text{pair} \in \mathcal{P}_1 }}، {{ \text{inf} \in \mathcal{P}_2 }}، {{ \text{entre} \in \mathcal{P}_3 }}). به‌ویژه نماد تساوی {{ = }} یک محمول دوتایی ویژه {{ \text{egal} \in \mathcal{P}_2 }} است.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="box method">
  <h4>روش امتحانی: تشخیص نوع و ظرفیت (Arité) نمادها از روی ساختار فرمول</h4>
  <p>در یک فرمول خوش‌ساخت {{ F }} (مانند تمرین ۲۴ از سری تمرین‌های TD)، نقش و ظرفیت هر نماد را با بررسی جایگاه آن در درخت نحوی تعیین می‌کنیم:</p>
  <ul>
    <li>نمادی که <strong>مستقیماً زیر یک عملگر منطقی</strong> ({{ \neg, \land, \lor, \Rightarrow, \Leftrightarrow }}) یا <strong>بلافاصله به عنوان بدنه یک سور</strong> ({{ \forall x \, \dots }}، {{ \exists x \, \dots }}) قرار گرفته باشد، الزاماً یک <strong>نماد محمول</strong> {{ p \in \mathcal{P}_n }} است که {{ n }} تعداد آرگومان‌های درون پرانتز آن است.</li>
    <li>نمادی که <strong>درون پرانتزهای آرگومان یک محمول یا تابع دیگر</strong> ظاهر شده باشد، یا متغیر {{ x \in \mathcal{X} }} است، یا ثابت {{ c \in \mathcal{F}_0 }} (اگر پرانتز نداشته باشد و در {{ \mathcal{X} }} نباشد)، و یا یک <strong>نماد تابعی</strong> {{ f \in \mathcal{F}_n }} با {{ n \ge 1 }} آرگومان است.</li>
  </ul>
</div>

<h2 id="sec3">3. Définition inductive des termes : {{ \mathcal{T}_0 }}, {{ \mathcal{T}_k }} et {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }}</h2>

<div class="box def">
  <h4>سلسله‌مراتب ترم‌ها {{ \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }} و مجموعه کل ترم‌ها {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} (درس ۷، اسلایدهای ۹ تا ۱۴)</h4>
  <p><strong>ترم‌ها</strong> (Termes) عبارات نحوی‌ای هستند که به اشیاء (افراد) دامنه اشاره می‌کنند. ابتدا به صورت بازگشتی روی {{ k \in \mathbb{N} }} خانواده مجموعه‌های {{ \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }} شامل ترم‌هایی با عمق تودرتویی توابع حداکثر {{ k }} را تعریف می‌کنیم:</p>
  <ul>
    <li><strong>گام پایه ({{ k = 0 }}، ترم‌های اتمی) :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}_0(\mathcal{X}, \mathcal{F}) = \mathcal{X} \cup \mathcal{F}_0 }}</div>
      ترم با ارتفاع {{ 0 }} صرفاً یک متغیر فردی یا یک نماد ثابت است.</li>
    <li><strong>گام استقرایی ({{ k \to k+1 }}) :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}_{k+1}(\mathcal{X}, \mathcal{F}) = \mathcal{T}_k(\mathcal{X}, \mathcal{F}) \cup \left\{ f(t_1, \dots, t_n) \;\middle|\; n \ge 1, \, f \in \mathcal{F}_n \text{ et } t_1, \dots, t_n \in \mathcal{T}_k(\mathcal{X}, \mathcal{F}) \right\} }}</div>
    </li>
    <li><strong>مجموعه تمام ترم‌ها :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \mathcal{T}(\mathcal{X}, \mathcal{F}) = \bigcup_{k \in \mathbb{N}} \mathcal{T}_k(\mathcal{X}, \mathcal{F}) }}</div>
    </li>
  </ul>
  <p><strong>تعریف استقرایی معادل برای {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} :</strong> مجموعه {{ \mathcal{T}(\mathcal{X}, \mathcal{F}) }} کوچک‌ترین مجموعه‌ای است که:</p>
  <ol>
    <li><strong>پایه :</strong> هر متغیر {{ x \in \mathcal{X} }} یک ترم است ({{ x \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}) و هر ثابت {{ c \in \mathcal{F}_0 }} یک ترم است ({{ c \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }}).</li>
    <li><strong>گام استقرا :</strong> اگر {{ f \in \mathcal{F}_n }} ({{ n \ge 1 }}) و {{ t_1, \dots, t_n \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} باشند، آنگاه {{ f(t_1, \dots, t_n) \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} است.</li>
  </ol>
  <p><strong>ترم بسته (Terme clos / Ground term) :</strong> ترمی که هیچ متغیری در آن به کار نرفته باشد متعلق به {{ \mathcal{T}(\emptyset, \mathcal{F}) }} است که در جزوه تمرین‌های TD به اختصار با {{ \mathcal{T}_0(\mathcal{F}) }} نمایش داده می‌شود (دقت کنید: در تمرین ۲۲ جزوه TD، منظور از {{ \mathcal{T}_0(\mathcal{F}) }} مجموعه تمام ترم‌های بسته ساخته‌شده با {{ \mathcal{F} }} بدون متغیر است).</p>
</div>

<h2 id="sec4">4. Formules de la LPPO et distinction Termes vs Formules</h2>

<div class="box def">
  <h4>تعریف استقرایی مجموعه فرمول‌ها {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} (درس ۷، اسلایدهای ۱۵ تا ۱۹)</h4>
  <p>مجموعه {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} شامل فرمول‌های منطق محمولات، کوچک‌ترین مجموعه‌ای است که در اصول زیر صدق کند:</p>
  <ol>
    <li><strong>فرمول‌های اتمی (Atomes) :</strong>
      <ul>
        <li> {{ \top \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} و {{ \bot \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} ؛</li>
        <li> اگر {{ p \in \mathcal{P}_0 }} باشد، آنگاه {{ p \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} ؛</li>
        <li> اگر {{ p \in \mathcal{P}_n }} ({{ n \ge 1 }}) و {{ t_1, \dots, t_n \in \mathcal{T}(\mathcal{X}, \mathcal{F}) }} <strong>ترم</strong> باشند، آنگاه {{ p(t_1, \dots, t_n) \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }}.</li>
      </ul>
    </li>
    <li><strong>عملگرهای گزاره‌ای :</strong> اگر {{ F, G \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} باشند، آنگاه {{ (\neg F) }}، {{ (F \land G) }}، {{ (F \lor G) }}، {{ (F \Rightarrow G) }} و {{ (F \Leftrightarrow G) }} نیز متعلق به {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} هستند.</li>
    <li><strong>سورها (Quantificateurs) :</strong> اگر {{ x \in \mathcal{X} }} یک <strong>متغیر</strong> و {{ F \in \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} یک فرمول باشد، آنگاه {{ (\forall x \, F) }} و {{ (\exists x \, F) }} متعلق به {{ \mathbb{F}(\mathcal{X}, \mathcal{F}, \mathcal{P}) }} هستند.</li>
  </ol>
</div>

<div class="box warn">
  <h4>مرز عبورنشدنی: ترم‌ها (اشیاء دامنه) در برابر فرمول‌ها (ارزش درستی)</h4>
  <p>در منطق مرتبه اول، اختلاط مقولات دستوری میان ترم و فرمول خطای فاحش نحوی محسوب می‌شود:</p>
  <table class="logic-table" style="width:100%; margin:10px 0;">
    <thead>
      <tr>
        <th>مقوله نحوی</th>
        <th>نقش معنایی</th>
        <th>ساخته‌شده از</th>
        <th>نمونه‌های مجاز</th>
        <th>خطاهای فاحش (نحواً غیرمجاز)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>ترم</strong> {{ t \in \mathcal{T} }}</td>
        <td>اشاره به یک <strong>شیء</strong> در دامنه {{ D }}</td>
        <td>متغیرها {{ \mathcal{X} }}، ثابت‌ها {{ \mathcal{F}_0 }}، توابع {{ f \in \mathcal{F}_n }}</td>
        <td>{{ x }}, {{ a }}, {{ s(s(a)) }}, {{ f(x, g(y)) }}</td>
        <td>{{ f(p(x)) }} <em>(محمول درون تابع)</em>،<br/>{{ x \land y }} <em>(عملگر منطقی روی ترم)</em></td>
      </tr>
      <tr>
        <td><strong>فرمول</strong> {{ F \in \mathbb{F} }}</td>
        <td>دارای <strong>ارزش درستی</strong> در {{ \{0, 1\} }}</td>
        <td>محمول‌ها {{ p(t_1,\dots,t_n) }}، عملگرها، {{ \forall x }}، {{ \exists x }}</td>
        <td>{{ p(f(x)) }}, {{ \forall x \, (p(x) \Rightarrow q(x, a)) }}</td>
        <td>{{ \forall f(x) \, p(x) }} <em>(سور روی ترم غیرمتغیر)</em>،<br/>{{ f(x) \Rightarrow p(x) }} <em>(ترم زیر {{ \Rightarrow }})</em></td>
      </tr>
    </tbody>
  </table>
</div>

<h2 id="sec5">5. Portée, variables libres {{ \text{Free}(F) }} et clôture universelle {{ \tilde{\forall} F }}</h2>

<div class="box def">
  <h4>دامنه سور (Portée)، رخدادهای آزاد و مقید (درس ۷، اسلایدهای ۲۱ تا ۲۷)</h4>
  <p>در فرمول {{ Q x \, G }} (که در آن {{ Q \in \{\forall, \exists\} }})، زیرفرمول {{ G }} را <strong>دامنه اثر</strong> (Portée / Scope) سور {{ Q x }} می‌نامند. در درخت نحوی فرمول {{ F }}، دامنه سور {{ Q x }} دقیقاً برابر با زیردرختی است که ریشه آن گره {{ Q x }} است.</p>
  <ul>
    <li>هر رخداد متغیر {{ x }} در {{ F }} را <strong>مقید</strong> (Liée / Bound) گوییم هرگاه در دامنه یک سور {{ \forall x }} یا {{ \exists x }} قرار گرفته باشد (و به نزدیک‌ترین سور {{ Q x }} در مسیر صعود به سمت ریشه درخت نحوی مقید می‌شود).</li>
    <li>رخدادی از {{ x }} که در دامنه هیچ سور {{ \forall x }} یا {{ \exists x }} نباشد، <strong>آزاد</strong> (Libre / Free) نامیده می‌شود.</li>
  </ul>
  <p><strong>نکته بسیار مهم :</strong> یک متغیر واحد {{ x }} می‌تواند در یک فرمول {{ F }} <em>هم‌زمان</em> دارای رخدادهای مقید و رخدادهای آزاد باشد! برای نمونه در {{ F = (\forall x \, p(x)) \land q(x) }}، رخداد {{ x }} در {{ p(x) }} مقید به {{ \forall x }} است، اما رخداد {{ x }} در {{ q(x) }} بیرون از دامنه {{ \forall x }} بوده و <strong>آزاد</strong> است؛ بنابراین {{ x \in \text{Free}(F) }}.</p>
</div>

<div class="box method">
  <h4>محاسبه استقرایی مجموعه متغیرهای آزاد {{ \text{Free}(F) }}</h4>
  <p>مجموعه متغیرهای به‌کاررفته در ترم {{ t }} را با {{ \text{Var}(t) }} و مجموعه متغیرهایی را که <strong>حداقل یک رخداد آزاد</strong> در فرمول {{ F }} دارند با {{ \text{Free}(F) }} نمایش می‌دهیم:</p>
  <ul>
    <li>{{ \text{Free}(\top) = \text{Free}(\bot) = \emptyset }}، و برای {{ p \in \mathcal{P}_0 }} داریم {{ \text{Free}(p) = \emptyset }} ؛</li>
    <li>برای اتم {{ p(t_1, \dots, t_n) }} : {{ \text{Free}(p(t_1, \dots, t_n)) = \text{Var}(t_1) \cup \dots \cup \text{Var}(t_n) }} ؛</li>
    <li>{{ \text{Free}(\neg F) = \text{Free}(F) }} ؛</li>
    <li>برای عملگرهای دوتایی {{ \diamond \in \{\land, \lor, \Rightarrow, \Leftrightarrow\} }} : {{ \text{Free}(F_1 \diamond F_2) = \text{Free}(F_1) \cup \text{Free}(F_2) }} ؛</li>
    <li><strong>حالت کلیدی سورها :</strong>
      <div style="margin:6px 0; text-align:center;">{{ \text{Free}(\forall x \, G) = \text{Free}(G) \setminus \{x\} \qquad \text{et} \qquad \text{Free}(\exists x \, G) = \text{Free}(G) \setminus \{x\} }}</div>
    </li>
  </ul>
  <p><strong>فرمول بسته (Formule close) :</strong> فرمول {{ F }} را <strong>بسته</strong> می‌نامیم هرگاه {{ \text{Free}(F) = \emptyset }} باشد.</p>
  <p><strong>بستار کلی {{ \tilde{\forall} F }} (Clôture universelle) :</strong> اگر {{ \text{Free}(F) = \{x_1, \dots, x_k\} }} باشد، یک <strong>بستار کلی</strong> برای {{ F }} فرمول بسته‌ای است که با افزودن سورهای کلی برای تمام متغیرهای آزاد در ابتدای {{ F }} حاصل می‌شود: {{ \tilde{\forall} F = \forall x_1 \dots \forall x_k \, F }} (ترتیب سورهای {{ \forall x_i }} از نظر معنایی اهمیتی ندارد).</p>
</div>

<h2 id="sec6">6. Capture de variables et {{ \alpha }}-renommage canonique</h2>

<div class="box tip">
  <h4>قاعده {{ \alpha }}-تغییرنام بدون اسارت متغیر و فرم متعارف متغیرها (درس ۷، اسلایدهای ۲۸ تا ۳۲)</h4>
  <p>متغیر مقید به یک سور، یک <em>متغیر مجازی یا ساختگی</em> است (مشابه اندیس {{ i }} در {{ \sum_{i=1}^n i }}). می‌توان متغیر مقید در زیرفرمول {{ Q x \, G }} را به متغیر جدید {{ y }} تغییر نام داد و به {{ Q y \, G[x \leftarrow y] }} (که منطقاً هم‌ارز با آن است) رسید، <strong>مشروط به رعایت دو شرط اکید عدم اسارت (Non-capture)</strong>:</p>
  <ol>
    <li><strong>عدم اسارت متغیر آزاد موجود :</strong> {{ y \notin \text{Free}(G) }} (در غیر این صورت رخدادهای آزاد {{ y }} در {{ G }} توسط سور جدید {{ Q y }} به اسارت درمی‌آیند).</li>
    <li><strong>عدم اسارت توسط سور داخلی :</strong> هیچ رخداد آزادی از {{ x }} در {{ G }} نباید در دامنه یک سور داخلی {{ \forall y }} یا {{ \exists y }} درون {{ G }} قرار داشته باشد.</li>
  </ol>
  <p><strong>تبدیل به فرم متعارف (متمایزسازی متغیرهای سورها) :</strong> در امتحانات سوربن (ر.ک. تمرین‌های ۲۴ و ۲۵ جزوه TD)، غالباً خواسته می‌شود متغیرهای مقید فرمول {{ F }} را چنان تغییر نام دهید که در فرمول معادل {{ F' }} :</p>
  <ul>
    <li>هر دو سور متمایزی روی متغیرهای متفاوتی عمل کنند؛</li>
    <li>هیچ متغیری هم‌زمان هم رخداد آزاد و هم رخداد مقید در {{ F' }} نداشته باشد.</li>
  </ul>
  <p>برای انجام ایمن این کار بدون خطر اسارت، کافی است برای هر سور {{ Q x }} یک <strong>متغیر تازه (Fraîche)</strong> مانند {{ x_i }} انتخاب کنیم که در هیچ جای دیگر فرمول ظاهر نشده باشد!</p>
</div>
"""

open(os.path.join(W07, 'cours.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W07, 'cours.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("cours.fr.html and cours.fa.html written for w07.")
