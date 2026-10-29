#!/usr/bin/env python3
"""Authoring generator for Revision Week 2 (Thème 2).
Contains:
- Fiche de synthèse express (formulaire clé sans table de vérité)
- Radar des 5 pièges classiques de partiels
- Quiz interactif auto-corrigé avec w-quiz
"""
import os, json

W02 = '/home/mnasimi/sorbonne/Logic_Academy/content/w02'
os.makedirs(W02, exist_ok=True)

quiz_fr = {
    "questions": [
        {
            "q": "En algèbre de Boole, que vaut l'expression {{ a + (a \cdot b) }} ?",
            "options": [
                "{{ a \cdot b }}",
                "{{ a }}",
                "{{ a + b }}"
            ],
            "answer": 1,
            "explain": "Par la loi d'absorption de l'algèbre de Boole, a + (a · b) = a · 1 + a · b = a · (1 + b) = a · 1 = a."
        },
        {
            "q": "Soit F une formule insatisfiable et G une formule contingente quelconque. A-t-on {{ F \models G }} ?",
            "options": [
                "OUI, toujours",
                "NON, jamais",
                "Cela dépend de G"
            ],
            "answer": 0,
            "explain": "Par le principe d'explosion (ex falso quodlibet), il n'existe aucune interprétation satisfaisant F. Tout modèle de F satisfait donc trivialement G par vacuité."
        },
        {
            "q": "Quelle est l'équivalence exacte en algèbre de Boole pour {{ a + (b \cdot c) }} ?",
            "options": [
                "{{ (a + b) \cdot c }}",
                "{{ (a + b) \cdot (a + c) }}",
                "Cette distributivité est impossible en algèbre"
            ],
            "answer": 1,
            "explain": "Contrairement à l'algèbre sur les nombres réels, en algèbre de Boole la somme est distributive sur le produit : a + (b · c) = (a + b) · (a + c)."
        },
        {
            "q": "Pour prouver qu'une conséquence sémantique {{ \mathcal{H} \models F }} est FAUSSE, que suffit-il de faire ?",
            "options": [
                "Calculer l'intégralité de la table de vérité",
                "Exhiber une seule interprétation I qui satisfait toutes les hypothèses de H mais où [F]^I = 0",
                "Montrer que F est insatisfiable"
            ],
            "answer": 1,
            "explain": "Un contre-modèle unique (satisfaisant toutes les hypothèses mais rendant fausse la conclusion) suffit à anéantir l'implication universelle."
        },
        {
            "q": "Si une formule F est valide ({{ \models F }}), quelle propriété fondamentale possède sa négation {{ \neg F }} ?",
            "options": [
                "Elle est également valide",
                "Elle est satisfiable mais non valide",
                "Elle est insatisfiable (aucune interprétation ne la satisfait)"
            ],
            "answer": 2,
            "explain": "Par dualité fondamentale, F est vraie pour toute interprétation si et seulement si ¬F est fausse pour toute interprétation (insatisfiable)."
        }
    ]
}

quiz_fa = {
    "questions": [
        {
            "q": "در جبر بولی، مقدار عبارت {{ a + (a \cdot b) }} برابر با چیست؟",
            "options": [
                "{{ a \cdot b }}",
                "{{ a }}",
                "{{ a + b }}"
            ],
            "answer": 1,
            "explain": "طبق قانون جذب جبر بولی داریم: a + (a · b) = a · 1 + a · b = a · (1 + b) = a · 1 = a."
        },
        {
            "q": "اگر F فرمولی ناسازگار (تناقض) و G گزاره‌ای محتمل باشد، آیا رابطه {{ F \models G }} برقرار است؟",
            "options": [
                "بله، همواره برقرار است",
                "خیر، هرگز برقرار نیست",
                "بستگی به ساختار فرمول G دارد"
            ],
            "answer": 0,
            "explain": "طبق اصل انفجار منطقی (Ex falso quodlibet)، هیچ تعبیری فرضیه F را ارضا نمی‌کند؛ بنابراین به دلیل انتفای مقدم، استلزام برای هر G دلخواهی همواره صادق است."
        },
        {
            "q": "هم‌ارزی دقیق عبارت {{ a + (b \cdot c) }} در جبر بولی کدام است؟",
            "options": [
                "{{ (a + b) \cdot c }}",
                "{{ (a + b) \cdot (a + c) }}",
                "چنین توزیع‌پذیری در جبر غیرممکن است"
            ],
            "answer": 1,
            "explain": "برخلاف جبر اعداد حقیقی، در جبر بولی عمل جمع بر روی ضرب توزیع‌پذیر است: a + (b · c) = (a + b) · (a + c)."
        },
        {
            "q": "برای ابطال و رد یک ادعای استلزام معنایی ({{ \mathcal{H} \models F }})، انجام چه کاری کافی است؟",
            "options": [
                "کشیدن تمام جدول درستی",
                "ارائه تنها یک تعبیر I که تمام فرضیات H را صادق کند اما [F]^I = 0 باشد",
                "اثبات این‌که F ناسازگار است"
            ],
            "answer": 1,
            "explain": "وجود یک پادمدل منفرد (تعبیری که تمام فرضیات را درست اما نتیجه را نادرست نماید) ادعای استلزام کلی را فوراً باطل می‌سازد."
        },
        {
            "q": "اگر فرمول F معتبر (توتولوژی با نماد {{ \models F }}) باشد، نقیض آن {{ \neg F }} چه خاصیت قطعی دارد؟",
            "options": [
                "آن هم معتبر است",
                "صدق‌پذیر ولی غیرمعتبر است",
                "ناسازگار (تناقض) است و هیچ مدلی ندارد"
            ],
            "answer": 2,
            "explain": "بنا بر اصل دوگانگی اساسی، فرمول F تحت تمام تعبیرها درست است اگر و تنها اگر نقیض آن تحت تمام تعبیرها نادرست باشد (ناسازگار)."
        }
    ]
}

fr = r'''
<div class="lesson-header">
  <div class="badge">Sorbonne Université — Fiche de Révision &amp; Auto-évaluation</div>
  <h1>Révision Thème 2 : Mémo Algébrique et Conséquences</h1>
  <p class="lead">Synthèse ultra-rapide des notions clés du Thème 2, radar des 5 pièges de partiels et quiz d'auto-évaluation immédiate.</p>
</div>

<div class="toc-box">
  <h3>Sommaire de la fiche</h3>
  <ul>
    <li><a href="#rev2_fiches">1. Fiche mémo express des 5 règles d'or</a></li>
    <li><a href="#rev2_pieges">2. Radar des pièges d'examen classiques</a></li>
    <li><a href="#rev2_quiz">3. Quiz interactif auto-corrigé</a></li>
  </ul>
</div>

<h2 id="rev2_fiches">1. Fiche mémo express des 5 règles d'or</h2>

<div class="box tip">
  <h4>Les 5 règles absolues à graver dans votre mémoire</h4>
  <ol>
    <li><strong>Traduction brute sans simplification :</strong>
      <br/>Quand l'examen demande de calculer {{ [F]^{\mathcal{M}} }}, écrivez d'abord l'arbre complet avec les barres et les produits sans jamais simplifier au préalable (5 points au partiel !).
    </li>
    <li><strong>Distributivité croisée en algèbre de Boole :</strong>
      <br/>{{ a + (b \cdot c) = (a + b) \cdot (a + c) }} et {{ a \cdot (b + c) = (a \cdot b) + (a \cdot c) }}.
    </li>
    <li><strong>Théorème de déduction sémantique :</strong>
      <br/>{{ \mathcal{H} \cup \{A\} \models B \quad \iff \quad \mathcal{H} \models (A \Rightarrow B) }}. En particulier, {{ A \models B \iff \models (A \Rightarrow B) }}.
    </li>
    <li><strong>Dualité validité / insatisfiabilité :</strong>
      <br/>{{ F }} est valide ssi {{ \neg F }} est insatisfiable.
    </li>
    <li><strong>Principe de réfutation par contre-modèle :</strong>
      <br/>Pour infirmer {{ \mathcal{H} \models F }}, il suffit de fournir UNE seule interprétation {{ I }} telle que {{ [H]^I = 1 }} pour tout {{ H \in \mathcal{H} }} et {{ [F]^I = 0 }}.
    </li>
  </ol>
</div>

<h2 id="rev2_pieges">2. Radar des pièges d'examen classiques</h2>

<div class="box warn">
  <h4>Les erreurs les plus pénalisées par les correcteurs de la Sorbonne</h4>
  <ul>
    <li><strong>Piège 1 — Utiliser une table de vérité :</strong> La consigne interdit formellement les tables au Thème 2. Tout tableau de vérité entraîne la note 0 à l'exercice.</li>
    <li><strong>Piège 2 — Oublier de nommer les équivalences :</strong> Dans une preuve équationnelle, omettre d'écrire « loi de De Morgan », « élément neutre » ou « complémentarité » coûte la moitié des points de la question.</li>
    <li><strong>Piège 3 — Confondre {{ \models }} et {{ \Rightarrow }} :</strong> {{ \models }} est une relation métamathématique de déduction, tandis que {{ \Rightarrow }} est un symbole syntaxique de la formule.</li>
    <li><strong>Piège 4 — Oublier que le faux implique tout :</strong> Si {{ F }} est insatisfiable, alors {{ F \models G }} est <strong>VRAIE</strong> pour n'importe quelle formule {{ G }} !</li>
    <li><strong>Piège 5 — Déduire la validité de la conclusion :</strong> Si {{ F \models G }} et {{ G }} est valide, on ne peut RIEN en déduire sur {{ F }} (elle peut être contingente ou fausse). En revanche, si {{ F }} est valide et {{ F \models G }}, alors {{ G }} est obligatoirement valide !</li>
  </ul>
</div>

<h2 id="rev2_quiz">3. Quiz interactif auto-corrigé</h2>

<div class="w-quiz" data-id="w02-quiz">
  <script type="application/json">
%%QUIZ_FR%%
  </script>
</div>
'''

fa = r'''
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — برگه مرور سریع و خودآزمایی</div>
  <h1>مرور جامع فصل ۲: چکیده جبری و قواعد استنتاج</h1>
  <p class="lead">خلاصه سریع و ساختاریافته از مفاهیم کلیدی فصل ۲، فهرست ۵ تله مهلک در امتحانات میان‌ترم و آزمون تعاملی با تصحیح و تحلیل بلادرنگ.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب برگه مرور</h3>
  <ul>
    <li><a href="#rev2_fiches">۱. برگه یادداشت ۵ قاعده طلایی</a></li>
    <li><a href="#rev2_pieges">۲. رادار تله‌های پرتکرار امتحانات میان‌ترم</a></li>
    <li><a href="#rev2_quiz">۳. آزمون تعاملی با تصحیح آنی</a></li>
  </ul>
</div>

<h2 id="rev2_fiches">1. Fiche mémo express des 5 règles d'or</h2>

<div class="box tip">
  <h4>۵ قاعده اساسی که باید در ذهن تثبیت شوند</h4>
  <ol>
    <li><strong>ترجمه خام استقرایی بدون ساده‌سازی:</strong>
      <br/>هنگامی که امتحان مقدار {{ [F]^{\mathcal{M}} }} را می‌خواهد، ابتدا درخت کامل را با خطوط متمم بنویسید بدون این‌که کوچک‌ترین ساده‌سازی پیش‌رس انجام دهید (۵ نمره میان‌ترم!).
    </li>
    <li><strong>توزیع‌پذیری متقابل در جبر بولی:</strong>
      <br/><span dir="ltr">{{ a + (b \cdot c) = (a + b) \cdot (a + c) }}</span> و <span dir="ltr">{{ a \cdot (b + c) = (a \cdot b) + (a \cdot c) }}</span>.
    </li>
    <li><strong>قضیه بنیادین استنتاج معنایی:</strong>
      <br/><span dir="ltr">{{ \mathcal{H} \cup \{A\} \models B \quad \iff \quad \mathcal{H} \models (A \Rightarrow B) }}</span>. به ویژه <span dir="ltr">{{ A \models B \iff \models (A \Rightarrow B) }}</span>.
    </li>
    <li><strong>اصل دوگانگی اعتبار / ناسازگاری:</strong>
      <br/>فرمول {{ F }} معتبر است اگر و فقط اگر {{ \neg F }} ناسازگار باشد.
    </li>
    <li><strong>اصل ابطال با پادمدل:</strong>
      <br/>برای رد ادعای {{ \mathcal{H} \models F }}، ارائه تنها یک تعبیر {{ I }} که در آن {{ [H]^I = 1 }} برای تمام {{ H \in \mathcal{H} }} و {{ [F]^I = 0 }} باشد کفایت می‌کند.
    </li>
  </ol>
</div>

<h2 id="rev2_pieges">2. Radar des pièges d'examen classiques</h2>

<div class="box warn">
  <h4>رایج‌ترین اشتباهاتی که دانشجویان در تصحیح سوربن نمره از دست می‌دهند</h4>
  <ul>
    <li><strong>تله ۱ — استفاده از جدول درستی:</strong> صورت مسئله اکیداً جدول را ممنوع کرده است؛ رسم جدول نمره صفر را به همراه دارد.</li>
    <li><strong>تله ۲ — ننوشتن نام قواعد جبری:</strong> در اثبات معادلاتی، ننوشتن عناوینی چون «قانون دمرگان»، «عنصر خنثی» یا «قانون متمم» نیمی از نمره را کسر می‌کند.</li>
    <li><strong>تله ۳ — خلط نماد {{ \models }} با {{ \Rightarrow }}:</strong> نماد {{ \models }} یک رابطه فرامنطقی در جهان تعبیرهاست در حالی که {{ \Rightarrow }} عملگری متنی درون خود فرمول است.</li>
    <li><strong>تله ۴ — فراموشی اصل انفجار:</strong> اگر {{ F }} ناسازگار باشد، رابطه {{ F \models G }} برای هر فرمول دلخواهی چون {{ G }} <strong>درست</strong> است!</li>
    <li><strong>تله ۵ — نتیجه‌گیری شتاب‌زده درباره اعتبار:</strong> اگر {{ F \models G }} باشد و {{ G }} معتبر باشد، هیچ نتیجه‌ای درباره اعتبار {{ F }} نمی‌توان گرفت. اما اگر {{ F }} معتبر باشد و {{ F \models G }}، آنگاه {{ G }} قطعاً معتبر است!</li>
  </ul>
</div>

<h2 id="rev2_quiz">3. Quiz interactif auto-corrigé</h2>

<div class="w-quiz" data-id="w02-quiz">
  <script type="application/json">
%%QUIZ_FA%%
  </script>
</div>
'''

open(os.path.join(W02, 'revision.fr.html'), 'w', encoding='utf-8').write(fr.replace('%%QUIZ_FR%%', json.dumps(quiz_fr, indent=2)).strip())
open(os.path.join(W02, 'revision.fa.html'), 'w', encoding='utf-8').write(fa.replace('%%QUIZ_FA%%', json.dumps(quiz_fa, ensure_ascii=False, indent=2)).strip())
print("revision.fr.html and revision.fa.html written.")
