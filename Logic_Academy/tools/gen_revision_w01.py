#!/usr/bin/env python3
"""Authoring generator for Revision Week 1 (Thème 1).
Contains:
- Fiche de synthèse express (formulaire clé)
- Radar des 6 pièges classiques de partiels
- Quiz interactif auto-corrigé avec w-quiz
"""
import os, json

W01 = '/home/mnasimi/sorbonne/Logic_Academy/content/w01'
os.makedirs(W01, exist_ok=True)

# Quiz specs for FR and FA
quiz_fr = {
    "questions": [
        {
            "q": "Selon la convention officielle de Sorbonne Université, comment parenthéser la formule {{ p \Rightarrow q \Rightarrow r }} ?",
            "options": [
                "{{ ((p \Rightarrow q) \Rightarrow r) }}",
                "{{ (p \Rightarrow (q \Rightarrow r)) }}",
                "Les deux parenthésages sont syntaxiquement équivalents"
            ],
            "answer": 1,
            "explain": "En cas d'opérateurs de même priorité, la règle du cours stipule impérativement : « sous-formule de droite prioritaire » (associativité à droite)."
        },
        {
            "q": "Quelle est la racine de l'AST de la formule {{ \neg p \land q \Rightarrow r }} ?",
            "options": [
                "Le connecteur {{ \neg }}",
                "Le connecteur {{ \land }}",
                "Le connecteur {{ \Rightarrow }}"
            ],
            "answer": 2,
            "explain": "L'ordre de priorité décroissant est ¬ > ∧ > ∨ > ⇒. Le connecteur de priorité la plus faible (ici ⇒) s'exécute en tout dernier lieu, il constitue donc la racine de l'arbre syntaxique."
        },
        {
            "q": "Laquelle de ces propositions traduit rigoureusement « Pour que A, il faut que B » ?",
            "options": [
                "{{ A \Rightarrow B }}",
                "{{ B \Rightarrow A }}",
                "{{ A \Leftrightarrow B }}"
            ],
            "answer": 0,
            "explain": "« Il faut B » exprime une condition nécessaire. Si A est réalisé, B a obligatoirement dû se réaliser, d'où A ⇒ B."
        },
        {
            "q": "Soit une formule F avec 4 variables atomiques distinctes. Combien de lignes comporte sa table de vérité ?",
            "options": [
                "8 lignes",
                "16 lignes",
                "32 lignes"
            ],
            "answer": 1,
            "explain": "Avec n variables booléennes indépendantes, le nombre d'interprétations possibles est 2^n. Pour n=4, on a 2^4 = 16 lignes."
        },
        {
            "q": "Si l'hypothèse A est fausse (I(A)=0), quelle est la valeur de l'implication {{ A \Rightarrow B }} ?",
            "options": [
                "Toujours 1 (Vrai), quelle que soit la valeur de B",
                "Toujours 0 (Faux)",
                "Indéterminée tant qu'on ne connaît pas B"
            ],
            "answer": 0,
            "explain": "Par le principe d'explosion (ex falso quodlibet), 0 ⇒ B vaut toujours 1. Une promesse dont la prémisse ne s'est pas réalisée n'est jamais rompue."
        }
    ]
}

quiz_fa = {
    "questions": [
        {
            "q": "بر طبق قرارداد رسمی دانشگاه سوربن، فرمول {{ p \Rightarrow q \Rightarrow r }} چگونه پرانتزگذاری می‌شود؟",
            "options": [
                "{{ ((p \Rightarrow q) \Rightarrow r) }}",
                "{{ (p \Rightarrow (q \Rightarrow r)) }}",
                "هر دو شیوه پرانتزگذاری از نظر نحوی یکسان هستند"
            ],
            "answer": 1,
            "explain": "در صورت تلاقی عملگرهای هم‌اولویت، قاعده اجباری درس سوربن اعلام می‌کند: «زیرفرمول سمت راست همیشه اولویت دارد» (شرکت‌پذیری از راست)."
        },
        {
            "q": "ریشه درخت نحو انتزاعی (AST) فرمول {{ \neg p \land q \Rightarrow r }} کدام عملگر است؟",
            "options": [
                "عملگر نقیض {{ \neg }}",
                "عملگر عطف {{ \land }}",
                "عملگر استلزام {{ \Rightarrow }}"
            ],
            "answer": 2,
            "explain": "ترتیب کاهشی اولویت‌ها عبارت است از ¬ > ∧ > ∨ > ⇒. ضعیف‌ترین عملگر (در اینجا ⇒) در آخرین گام اجرا شده و بنابراین در ریشه درخت قرار می‌گیرد."
        },
        {
            "q": "کدام‌یک از فرمول‌های زیر ترجمه دقیق «برای وقوع A، لازم است که B باشد» است؟",
            "options": [
                "{{ A \Rightarrow B }}",
                "{{ B \Rightarrow A }}",
                "{{ A \Leftrightarrow B }}"
            ],
            "answer": 0,
            "explain": "«لازم بودن B» بیانگر شرط لازم است. اگر A رخ داده باشد، الزاماً B نیز باید رخ داده باشد، بنابراین A ⇒ B."
        },
        {
            "q": "یک فرمول گزاره‌ای با ۴ متغیر اتمی مستقل، شامل چند سطر در جدول درستی خواهد بود؟",
            "options": [
                "۸ سطر",
                "۱۶ سطر",
                "۳۲ سطر"
            ],
            "answer": 1,
            "explain": "با n متغیر بولی مستقل، تعداد تعبیرهای ممکن ۲ به توان n است. برای ۴ متغیر داریم: ۲ به توان ۴ برابر با ۱۶ سطر."
        },
        {
            "q": "اگر مقدم A نادرست باشد (I(A)=0)، ارزش گزاره شرطی {{ A \Rightarrow B }} چقدر است؟",
            "options": [
                "همواره ۱ (درست)، فارغ از این‌که B چه ارزشی داشته باشد",
                "همواره ۰ (نادرست)",
                "نامشخص است تا زمانی که ارزش B مشخص نشود"
            ],
            "answer": 0,
            "explain": "طبق اصل انفجار منطقی (Ex falso quodlibet)، حاصل 0 ⇒ B همواره ۱ است. عهدی که پیش‌شرط آن اتفاق نیفتاده، هرگز شکسته نشده است."
        }
    ]
}

fr = f"""
<div class="lesson-header">
  <div class="badge">Sorbonne Université — Fiche de Révision &amp; Auto-évaluation</div>
  <h1>Révision Thème 1 : Les Incontournables de l'Examen</h1>
  <p class="lead">Synthèse ultra-rapide des notions clés du Thème 1, catalogue des pièges récurrents aux examens de Sorbonne Université et quiz d'auto-évaluation immédiate.</p>
</div>

<div class="toc-box">
  <h3>Sommaire de la fiche</h3>
  <ul>
    <li><a href="#rev_fiches">1. Fiche mémo express des 5 règles d'or</a></li>
    <li><a href="#rev_pieges">2. Radar des pièges d'examen classiques</a></li>
    <li><a href="#rev_quiz">3. Quiz interactif auto-corrigé</a></li>
  </ul>
</div>

<h2 id="rev_fiches">1. Fiche mémo express des 5 règles d'or</h2>

<div class="box tip">
  <h4>Les 5 règles absolues à graver dans votre mémoire</h4>
  <ol>
    <li><strong>Hiérarchie des priorités de la Sorbonne :</strong>
      <br/>{{ \neg \quad > \quad \land \quad > \quad \lor \quad > \quad \Rightarrow \quad > \quad \Leftrightarrow }}
      <br/>Le connecteur de plus faible priorité est la racine de l'AST.
    </li>
    <li><strong>Associativité à droite :</strong> En cas d'opérateurs identiques successifs, on regroupe TOUJOURS par la droite : {{ A \Rightarrow B \Rightarrow C \equiv A \Rightarrow (B \Rightarrow C) }}.</li>
    <li><strong>L'implication matérielle :</strong> {{ A \Rightarrow B \equiv \neg A \lor B }}. Fausse uniquement si {{ A=1 }} et {{ B=0 }}.</li>
    <li><strong>Condition nécessaire vs suffisante :</strong>
      <ul>
        <li>« Il suffit de A pour B » (condition suffisante) : {{ A \Rightarrow B }}.</li>
        <li>« Il faut A pour B » (condition nécessaire) : {{ B \Rightarrow A }}.</li>
      </ul>
    </li>
    <li><strong>Nombre de lignes de la table de vérité :</strong> Pour {{ n }} variables propositionnelles, la table comporte exactement {{ 2^n }} lignes.</li>
  </ol>
</div>

<h2 id="rev_pieges">2. Radar des pièges d'examen classiques</h2>

<div class="box warn">
  <h4>Les erreurs les plus pénalisées par les correcteurs de la Sorbonne</h4>
  <ul>
    <li><strong>Piège 1 — L'associativité à gauche par habitude du code :</strong> Écrire <code>((p &and; q) &and; r)</code> au lieu de <code>(p &and; (q &and; r))</code> fait perdre tous les points de syntaxe.</li>
    <li><strong>Piège 2 — Confondre « seulement si » et « si » :</strong> « A seulement si B » se formalise par {{ A \Rightarrow B }}, et NON par {{ B \Rightarrow A }}.</li>
    <li><strong>Piège 3 — Oublier que le faux implique tout :</strong> Penser que si {{ I(A)=0 }}, l'implication {{ A \Rightarrow B }} est fausse ou inconnue. Elle est <strong>vraie</strong> !</li>
    <li><strong>Piège 4 — Table de vérité dans le désordre :</strong> Ne pas respecter l'ordre binaire naturel ({{ 000, 001, 010, \dots }}) agace les correcteurs et entraîne souvent des oublis de lignes.</li>
    <li><strong>Piège 5 — Déduire sans vérifier tous les modèles :</strong> Dans une énigme, affirmer qu'une proposition est vraie alors qu'elle ne l'est que dans certains modèles mais pas dans tous. Pour qu'une affirmation soit déductible (conséquence sémantique {{ \mathcal{{T}} \models \varphi }}), elle doit valoir 1 dans <strong>100% des modèles</strong> de la théorie.</li>
  </ul>
</div>

<h2 id="rev_quiz">3. Quiz interactif auto-corrigé</h2>

<div class="w-quiz" data-id="w01-quiz">
  <script type="application/json">
{json.dumps(quiz_fr, indent=2)}
  </script>
</div>
"""

fa = f"""
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — برگه مرور سریع و خودآزمایی</div>
  <h1>مرور جامع فصل ۱: نکات طلایی و سرنوشت‌ساز آزمون</h1>
  <p class="lead">خلاصه سریع و ساختاریافته از مفاهیم کلیدی فصل ۱، فهرست تله‌های رایج در امتحانات دانشگاه سوربن و کوئیز تعاملی با تصحیح و تحلیل بلادرنگ.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب برگه مرور</h3>
  <ul>
    <li><a href="#rev_fiches">۱. برگه یادداشت ۵ قاعده طلایی</a></li>
    <li><a href="#rev_pieges">۲. رادار تله‌های پرتکرار امتحانات سوربن</a></li>
    <li><a href="#rev_quiz">۳. آزمون تعاملی با تصحیح آنی</a></li>
  </ul>
</div>

<h2 id="rev_fiches">1. Fiche mémo express des 5 règles d'or</h2>

<div class="box tip">
  <h4>۵ قاعده اساسی که باید در ذهن تثبیت شوند</h4>
  <ol>
    <li><strong>سلسله‌مراتب اولویت عملگرها در سوربن:</strong>
      <br/><span dir="ltr">{{ \neg \quad > \quad \land \quad > \quad \lor \quad > \quad \Rightarrow \quad > \quad \Leftrightarrow }}</span>
      <br/>عملگری که کمترین اولویت را دارد، ریشه درخت AST خواهد بود.
    </li>
    <li><strong>شرکت‌پذیری از راست:</strong> در صورت تکرار عملگرهای هم‌ارز، دسته‌بندی همواره از راست انجام می‌شود: {{ A \Rightarrow B \Rightarrow C \equiv A \Rightarrow (B \Rightarrow C) }}.</li>
    <li><strong>استلزام مادی:</strong> {{ A \Rightarrow B \equiv \neg A \lor B }}. تنها در صورتی نادرست است که {{ A=1 }} و {{ B=0 }} باشد.</li>
    <li><strong>شرط لازم در برابر شرط کافی:</strong>
      <ul>
        <li>«کافی است A باشد تا B شود» (شرط کافی): {{ A \Rightarrow B }}.</li>
        <li>«لازم است A باشد تا B شود» (شرط لازم): {{ B \Rightarrow A }}.</li>
      </ul>
    </li>
    <li><strong>تعداد سطرهای جدول درستی:</strong> برای {{ n }} متغیر گزاره‌ای، جدول دقیقاً شامل {{ 2^n }} سطر است.</li>
  </ol>
</div>

<h2 id="rev_pieges">2. Radar des pièges d'examen classiques</h2>

<div class="box warn">
  <h4>رایج‌ترین اشتباهاتی که دانشجویان در تصحیح سوربن نمره از دست می‌دهند</h4>
  <ul>
    <li><strong>تله ۱ — شرکت‌پذیری از چپ ناشی از عادت برنامه‌نویسی:</strong> نوشتن <code>((p &and; q) &and; r)</code> به جای <code>(p &and; (q &and; r))</code> تمام نمره بخش نحو را صفر می‌کند.</li>
    <li><strong>تله ۲ — اشتباه گرفتن «تنها اگر» با «اگر»:</strong> عبارت «A تنها اگر B» با فرمول {{ A \Rightarrow B }} نمایش می‌یابد و نه با {{ B \Rightarrow A }}.</li>
    <li><strong>تله ۳ — فراموشی این‌که فرض باطل هر چیزی را نتیجه می‌دهد:</strong> تصور این‌که اگر {{ I(A)=0 }} باشد، شرطی {{ A \Rightarrow B }} نادرست یا مبهم است. در حالی که قطعاً <strong>درست</strong> است!</li>
    <li><strong>تله ۴ — بی‌نظمی در پر کردن جدول درستی:</strong> عدم رعایت نظم طبیعی باینری ({{ 000, 001, 010, \dots }}) باعث سردرگمی مصحح و جا افتادن برخی سطرها می‌شود.</li>
    <li><strong>تله ۵ — نتیجه‌گیری شتاب‌زده بدون بررسی همه مدل‌ها:</strong> در یک معما، ادعای این‌که فلان گزاره درست است در حالی که فقط در برخی مدل‌ها درست بوده و در مدل دیگری صفر است. برای استلزام منطقی {{ \mathcal{{T}} \models \varphi }}، باید فرمول در <strong>۱۰۰٪ مدل‌های نظریه</strong> مقدار ۱ داشته باشد.</li>
  </ul>
</div>

<h2 id="rev_quiz">3. Quiz interactif auto-corrigé</h2>

<div class="w-quiz" data-id="w01-quiz">
  <script type="application/json">
{json.dumps(quiz_fa, ensure_ascii=False, indent=2)}
  </script>
</div>
"""

open(os.path.join(W01, 'revision.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W01, 'revision.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("revision.fr.html and revision.fa.html written.")

