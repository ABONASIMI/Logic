#!/usr/bin/env python3
"""Authoring generator for Annales Week 2 (Thème 2).
Contains full official exam corrections for:
- Partiel 2017-2018 - Exercice 3 (20 points) : Validité équationnelle et conséquences sémantiques
- Partiel 2019-2020 L2 - Exercice 3 (8 points) : Preuve algébrique de validité et relations avec G quelconque
"""
import os

W02 = '/home/mnasimi/sorbonne/Logic_Academy/content/w02'
os.makedirs(W02, exist_ok=True)

fr = r'''
<div class="lesson-header">
  <div class="badge">Sorbonne Université — Annales Officielles Corrigées</div>
  <h1>Annales Thème 2 : Calcul Équationnel et Conséquence Sémantique</h1>
  <p class="lead">Sujets réels de partiels de la Sorbonne avec barème officiel détaillé, calculs sans tables de vérité, preuves équationnelles complètes et déductions sémantiques vérifiées.</p>
</div>

<div class="toc-box">
  <h3>Sujets d'examen traités</h3>
  <ul>
    <li><a href="#annale_partiel_2017">1. Partiel 2017-2018 – Exercice 3 : Validité et déductions formelles (20 points)</a></li>
    <li><a href="#annale_partiel_2019">2. Partiel 2019-2020 L2 – Exercice 3 : Preuve algébrique et relations avec G (8 points)</a></li>
  </ul>
</div>

<!-- SUJET 1 : PARTIEL 2017-2018 -->
<h2 id="annale_partiel_2017">1. Partiel 2017-2018 – Exercice 3 : Validité et déductions formelles (20 points)</h2>

<div class="box info">
  <h4>Référence de l'épreuve</h4>
  <p><strong>Épreuve :</strong> Évaluation de mi-semestre (Partiel) 2017-2018 — Logique UL2IN007.<br/>
  <strong>Barème officiel :</strong> 20 points (Question 1 : 2 pts ; Question 2 : 5 + 6 + 3 + 2 + 2 = 18 pts).<br/>
  <strong>Règle d'or :</strong> Aucune table de vérité n'est autorisée. Tous les calculs s'effectuent par l'algèbre de Boole.</p>
</div>

<div class="q-card" id="p17_q1">
  <div class="q-header">
    <span class="q-num">Question 1 (2 points)</span>
    <span class="q-title">Définition mathématique d'une formule valide</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Donner la définition d'une formule valide.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 1</summary>
    <div class="box method">
      <p>Une formule {{ F }} est <strong>valide</strong> si et seulement si pour toute interprétation (ou structure) {{ \mathcal{M} }}, on a :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;">{{ [F]^{\mathcal{M}} = 1 }}</p>
      <p><em>(Barème officiel : 2/2 si la quantification universelle « pour toute interprétation » est explicitement formulée).</em></p>
    </div>
  </details>
</div>

<div class="q-card" id="p17_q2_ab">
  <div class="q-header">
    <span class="q-num">Question 2 (a) &amp; (b) (11 points)</span>
    <span class="q-title">Traduction brute et preuve de validité par calcul équationnel</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Soit {{ F }} la formule {{ ((A \lor \neg B) \land B) \Rightarrow A }}.</p>
    <ul>
      <li><strong>(a) (5 points) :</strong> Étant donnée une structure {{ \mathcal{M} }}, calculer l'expression booléenne {{ [F]^{\mathcal{M}} }} en fonction de {{ I_{\mathcal{M}}(A) }} et {{ I_{\mathcal{M}}(B) }} (sans effectuer de simplification).</li>
      <li><strong>(b) (6 points) :</strong> En utilisant un raisonnement équationnel, montrer que {{ F }} est une formule valide (indiquer à chaque étape le nom de l'équivalence utilisée).</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel des Questions 2(a) et 2(b)</summary>
    <div class="box method">
      <h4>(a) Traduction inductive brute sans simplification (5 points)</h4>
      <p>Appliquons pas à pas la définition inductive de l'évaluation :</p>
      <div style="line-height:2em; font-size:1.05em;">
        {{ [F]^{\mathcal{M}} = [((A \lor \neg B) \land B) \Rightarrow A]^{\mathcal{M}} }}<br/>
        {{ = \overline{[ (A \lor \neg B) \land B ]^{\mathcal{M}}} + [A]^{\mathcal{M}} }} \quad <em>(Définition de l'implication)</em><br/>
        {{ = \overline{ [A \lor \neg B]^{\mathcal{M}} \cdot [B]^{\mathcal{M}} } + [A]^{\mathcal{M}} }} \quad <em>(Définition de la conjonction)</em><br/>
        {{ = \overline{ ([A]^{\mathcal{M}} + [\neg B]^{\mathcal{M}}) \cdot [B]^{\mathcal{M}} } + [A]^{\mathcal{M}} }} \quad <em>(Définition de la disjonction)</em><br/>
        {{ = \overline{ (I_{\mathcal{M}}(A) + \overline{I_{\mathcal{M}}(B)}) \cdot I_{\mathcal{M}}(B) } + I_{\mathcal{M}}(A) }} \quad <em>(Évaluation des atomes et de la négation)</em>
      </div>

      <h4>(b) Preuve de validité par raisonnement équationnel (6 points)</h4>
      <p>Posons pour alléger l'écriture {{ a = I_{\mathcal{M}}(A) }} et {{ b = I_{\mathcal{M}}(B) }} :</p>
      <div style="line-height:2.2em; font-size:1.05em;">
        {{ [F]^{\mathcal{M}} = \overline{ (a + \overline{b}) \cdot b } + a }}<br/>
        {{ \equiv (\overline{a + \overline{b}} + \overline{b}) + a }} \quad <em>(Loi de De Morgan sur la négation externe)</em><br/>
        {{ \equiv ( (\overline{a} \cdot \overline{\overline{b}}) + \overline{b} ) + a }} \quad <em>(Loi de De Morgan sur {{ \overline{a + \overline{b}} }})</em><br/>
        {{ \equiv ( (\overline{a} \cdot b) + \overline{b} ) + a }} \quad <em>(Involution : {{ \overline{\overline{b}} = b }})</em><br/>
        {{ \equiv ( (\overline{a} + \overline{b}) \cdot (b + \overline{b}) ) + a }} \quad <em>(Distributivité de + sur {{ \cdot }})</em><br/>
        {{ \equiv ( (\overline{a} + \overline{b}) \cdot 1 ) + a }} \quad <em>(Complémentarité : {{ b + \overline{b} = 1 }})</em><br/>
        {{ \equiv (\overline{a} + \overline{b}) + a }} \quad <em>(Élément neutre de {{ \cdot }})</em><br/>
        {{ \equiv (\overline{a} + a) + \overline{b} }} \quad <em>(Commutativité et associativité de +)</em><br/>
        {{ \equiv 1 + \overline{b} }} \quad <em>(Complémentarité : {{ \overline{a} + a = 1 }})</em><br/>
        {{ \equiv 1 }} \quad <em>(Élément absorbant : {{ 1 + x = 1 }})</em>
      </div>
      <p>Puisque {{ [F]^{\mathcal{M}} = 1 }} pour toute interprétation {{ \mathcal{M} }}, <strong>{{ F }} est une formule valide</strong>.</p>
    </div>
  </details>
</div>

<div class="q-card" id="p17_q2_cde">
  <div class="q-header">
    <span class="q-num">Question 2 (c), (d) &amp; (e) (7 points)</span>
    <span class="q-title">Déductions sémantiques et propriétés métamathématiques</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <ul>
      <li><strong>(c) (3 points) :</strong> A-t-on {{ (A \lor \neg B) \land B \models A }} ? (justifier).</li>
      <li><strong>(d) (2 points) :</strong> Soit {{ F_1 }} une formule quelconque. A-t-on {{ \neg F \models F_1 }} ? (justifier).</li>
      <li><strong>(e) (2 points) :</strong> Soit {{ F_2 }} une formule telle que {{ F \models F_2 }}. La formule {{ F_2 }} est-elle satisfiable ? valide ? (justifier).</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel des Questions 2(c), 2(d) et 2(e)</summary>
    <div class="box method">
      <h4>(c) Conséquence sémantique {{ (A \lor \neg B) \land B \models A }} (3 points)</h4>
      <p><strong>OUI.</strong> Par le théorème de déduction sémantique, on a l'équivalence fondamentale :</p>
      <p style="text-align:center; font-weight:bold;">{{ P \models Q \quad \iff \quad \models (P \Rightarrow Q) }}</p>
      <p>Comme on a prouvé à la question (b) que la formule {{ F = ((A \lor \neg B) \land B) \Rightarrow A }} est valide, on en déduit immédiatement que {{ (A \lor \neg B) \land B \models A }}.</p>

      <h4>(d) Conséquence sémantique avec la négation {{ \neg F \models F_1 }} (2 points)</h4>
      <p><strong>OUI.</strong> Puisque {{ F }} est une formule valide, sa négation {{ \neg F }} est <strong>insatisfiable</strong>. L'ensemble des structures satisfaisant {{ \neg F }} est donc <strong>vide</strong>. Dès lors, toute interprétation qui satisfait {{ \neg F }} satisfait trivialement {{ F_1 }} par vacuité (principe <em>ex falso quodlibet</em>). On a donc bien {{ \neg F \models F_1 }}.</p>

      <h4>(e) Nature de {{ F_2 }} si {{ F \models F_2 }} (2 points)</h4>
      <p>Puisque {{ F }} est valide, pour toute structure {{ \mathcal{M} }} on a {{ [F]^{\mathcal{M}} = 1 }}.</p>
      <p>Comme {{ F \models F_2 }}, toute structure qui satisfait {{ F }} doit satisfaire {{ F_2 }}. Or <em>toutes</em> les structures satisfont {{ F }}, donc <strong>toutes les structures satisfont obligatoirement {{ F_2 }}</strong> ({{ \forall \mathcal{M}, [F_2]^{\mathcal{M}} = 1 }}).</p>
      <p><strong>Conclusion :</strong> La formule {{ F_2 }} est donc <strong>valide</strong> (et donc également <strong>satisfiable</strong>).</p>
    </div>
  </details>
</div>

<!-- SUJET 2 : PARTIEL 2019-2020 L2 -->
<h2 id="annale_partiel_2019">2. Partiel 2019-2020 L2 – Exercice 3 : Preuve algébrique et relations avec G (8 points)</h2>

<div class="box info">
  <h4>Référence de l'épreuve</h4>
  <p><strong>Épreuve :</strong> Partiel L2 Informatique 2019-2020 — UE UL2IN007 Logique.<br/>
  <strong>Barème officiel :</strong> 8 points (1 pt + 1 pt + 2 pts + 4 pts).<br/>
  <strong>Formule étudiée :</strong> {{ F = (\neg A \Rightarrow (A \land \neg A)) \Rightarrow A }}.</p>
</div>

<div class="q-card" id="p19_q1_q2ab">
  <div class="q-header">
    <span class="q-num">Questions 1, 2(a) et 2(b) (4 points)</span>
    <span class="q-title">Traduction et preuve de validité de F</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <ol>
      <li>Donner la définition mathématique d'une formule {{ F }} valide.</li>
      <li>Soit {{ F = (\neg A \Rightarrow (A \land \neg A)) \Rightarrow A }} :
        <ul>
          <li><strong>(a) :</strong> Calculer l'expression booléenne {{ [F]^{\mathcal{M}} }} sans simplification.</li>
          <li><strong>(b) :</strong> Par un raisonnement équationnel, montrer que {{ F }} est valide.</li>
        </ul>
      </li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel pas-à-pas</summary>
    <div class="box method">
      <h4>1. Définition (1 point)</h4>
      <p>{{ F }} est valide ssi pour toute structure {{ \mathcal{M} }}, {{ [F]^{\mathcal{M}} = 1 }}.</p>

      <h4>2(a) Traduction brute sans simplification (1 point)</h4>
      <div style="line-height:2em; font-size:1.05em;">
        {{ [F]^{\mathcal{M}} = \overline{ [\neg A \Rightarrow (A \land \neg A)]^{\mathcal{M}} } + [A]^{\mathcal{M}} }}<br/>
        {{ = \overline{ \overline{[\neg A]^{\mathcal{M}}} + [A \land \neg A]^{\mathcal{M}} } + [A]^{\mathcal{M}} }}<br/>
        {{ = \overline{ \overline{\overline{I_{\mathcal{M}}(A)}} + (I_{\mathcal{M}}(A) \cdot \overline{I_{\mathcal{M}}(A)}) } + I_{\mathcal{M}}(A) }}
      </div>

      <h4>2(b) Raisonnement équationnel (2 points)</h4>
      <p>En posant {{ x = I_{\mathcal{M}}(A) }} :</p>
      <div style="line-height:2.2em; font-size:1.05em;">
        {{ [F]^{\mathcal{M}} \equiv \overline{ x + (x \cdot \overline{x}) } + x }} \quad <em>(Involution : {{ \overline{\overline{x}} = x }})</em><br/>
        {{ \equiv \overline{ x + 0 } + x }} \quad <em>(Complémentarité : {{ x \cdot \overline{x} = 0 }})</em><br/>
        {{ \equiv \overline{x} + x }} \quad <em>(Élément neutre : {{ x + 0 = x }})</em><br/>
        {{ \equiv 1 }} \quad <em>(Complémentarité : {{ \overline{x} + x = 1 }})</em>
      </div>
      <p>La formule {{ F }} est donc formellement valide.</p>
    </div>
  </details>
</div>

<div class="q-card" id="p19_q2c">
  <div class="q-header">
    <span class="q-num">Question 2(c) (4 points)</span>
    <span class="q-title">Analyse des 4 conséquences sémantiques avec G quelconque</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Soit {{ G }} une formule quelconque. A-t-on :</p>
    <ul>
      <li>(i) {{ G \models F }} ?</li>
      <li>(ii) {{ F \models G }} ?</li>
      <li>(iii) {{ G \models \neg F }} ?</li>
      <li>(iv) {{ \neg F \models G }} ?</li>
    </ul>
    <p>Justifier vos réponses.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel des 4 déductions</summary>
    <div class="box method">
      <ul>
        <li><strong>(i) A-t-on {{ G \models F }} ? &rarr; OUI (1 point)</strong>
          <br/>Toutes les structures qui satisfont {{ G }} satisfont nécessairement {{ F }}, puisque {{ F }} est <strong>valide</strong> et est donc satisfaite par <em>toutes</em> les structures sans exception.
        </li>
        <li><strong>(ii) A-t-on {{ F \models G }} ? &rarr; NON (1 point)</strong>
          <br/>Comme {{ G }} est une formule quelconque, elle peut par exemple être une formule non satisfaite par une certaine structure {{ \mathcal{M} }} (par exemple {{ G = \text{false} }}). Cette structure satisfait pourtant {{ F }} puisque {{ F }} est valide. C'est donc un contre-modèle.
        </li>
        <li><strong>(iii) A-t-on {{ G \models \neg F }} ? &rarr; NON (1 point)</strong>
          <br/>{{ G }} étant quelconque, elle peut être satisfaite par une certaine structure {{ \mathcal{M} }} (par exemple {{ G = \text{true} }}). Or {{ \neg F }} est insatisfiable (car {{ F }} est valide), donc aucune structure ne satisfait {{ \neg F }}.
        </li>
        <li><strong>(iv) A-t-on {{ \neg F \models G }} ? &rarr; OUI (1 point)</strong>
          <br/>Puisque {{ F }} est valide, {{ \neg F }} est <strong>insatisfiable</strong>. L'ensemble des structures qui satisfont {{ \neg F }} est donc vide, ce qui rend l'implication universellement vraie par vacuité.
        </li>
      </ul>
    </div>
  </details>
</div>
'''

fa = r'''
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — پاسخ‌نامه رسمی امتحانات میان‌ترم</div>
  <h1>امتحانات فصل ۲: محاسبات معادلاتی و استلزام معنایی</h1>
  <p class="lead">مسائل واقعی آزمون‌های میان‌ترم (Partiel) دانشگاه سوربن با بارم‌بندی دقیق، محاسبات بدون جدول درستی، اثبات‌های معادلاتی و استنتاج‌های صوری تاییدشده.</p>
</div>

<div class="toc-box">
  <h3>امتحانات مورد بررسی</h3>
  <ul>
    <li><a href="#annale_partiel_2017">۱. میان‌ترم ۲۰۱۷-۲۰۱۸ – تمرین ۳ : اعتبار و استنتاج‌های صوری (۲۰ نمره)</a></li>
    <li><a href="#annale_partiel_2019">۲. میان‌ترم ۲۰۱۹-۲۰۲۰ دوره کارشناسی – تمرین ۳ : اثبات جبری و روابط با فرمول دلخواه G (۸ نمره)</a></li>
  </ul>
</div>

<!-- SUJET 1 : PARTIEL 2017-2018 -->
<h2 id="annale_partiel_2017">1. Partiel 2017-2018 – Exercice 3 : Validité et déductions formelles (20 points)</h2>

<div class="box info">
  <h4>مشخصات برگه امتحانی</h4>
  <p><strong>آزمون:</strong> امتحان میان‌ترم (Partiel) ۲۰۱۷-۲۰۱۸ — درس منطق UL2IN007.<br/>
  <strong>بارم رسمی:</strong> ۲۰ نمره (سوال ۱: ۲ نمره ؛ سوال ۲: ۵ + ۶ + ۳ + ۲ + ۲ = ۱۸ نمره).<br/>
  <strong>قانون طلایی:</strong> کشیدن جدول درستی اکیداً ممنوع بوده و تمام محاسبات باید با جبر بولی انجام پذیرد.</p>
</div>

<div class="q-card" id="p17_q1">
  <div class="q-header">
    <span class="q-num">سوال ۱ (۲ نمره)</span>
    <span class="q-title">تعریف ریاضی فرمول معتبر (توتولوژی)</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>تعریف فرمول معتبر را بنویسید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۱</summary>
    <div class="box method">
      <p>فرمول {{ F }} <strong>معتبر</strong> است اگر و تنها اگر تحت هر تعبیر (یا ساختار) دلخواه {{ \mathcal{M} }} داشته باشیم:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.15em;" dir="ltr">{{ [F]^{\mathcal{M}} = 1 }}</p>
      <p><em>(ضابطه تصحیح: ۲ نمره کامل در صورتی داده می‌شود که قید «به ازای هر تعبیر» صراحتاً قید شده باشد).</em></p>
    </div>
  </details>
</div>

<div class="q-card" id="p17_q2_ab">
  <div class="q-header">
    <span class="q-num">سوال ۲ (الف) و (ب) (۱۱ نمره)</span>
    <span class="q-title">ترجمه خام و اثبات اعتبار با استدلال معادلاتی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرض کنید {{ F }} فرمول {{ ((A \lor \neg B) \land B) \Rightarrow A }} باشد.</p>
    <ul>
      <li><strong>(الف) (۵ نمره) :</strong> تحت ساختار {{ \mathcal{M} }}، عبارت بولی {{ [F]^{\mathcal{M}} }} را بر حسب {{ I_{\mathcal{M}}(A) }} و {{ I_{\mathcal{M}}(B) }} بدون هیچ‌گونه ساده‌سازی بنویسید.</li>
      <li><strong>(ب) (۶ نمره) :</strong> با استفاده از استدلال معادلاتی نشان دهید فرمول {{ F }} معتبر است (در هر گام نام قاعده جبری را ذکر کنید).</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوالات ۲(الف) و ۲(ب)</summary>
    <div class="box method">
      <h4>(الف) ترجمه خام استقرایی بدون ساده‌سازی (۵ نمره)</h4>
      <p>قواعد تبدیل استقرایی را گام‌به‌گام پیاده می‌کنیم:</p>
      <div style="line-height:2em; font-size:1.05em;" dir="ltr">
        {{ [F]^{\mathcal{M}} = [((A \lor \neg B) \land B) \Rightarrow A]^{\mathcal{M}} }}<br/>
        {{ = \overline{[ (A \lor \neg B) \land B ]^{\mathcal{M}}} + [A]^{\mathcal{M}} }} \quad <em>(تعریف شرطی)</em><br/>
        {{ = \overline{ [A \lor \neg B]^{\mathcal{M}} \cdot [B]^{\mathcal{M}} } + [A]^{\mathcal{M}} }} \quad <em>(تعریف عطف)</em><br/>
        {{ = \overline{ ([A]^{\mathcal{M}} + [\neg B]^{\mathcal{M}}) \cdot [B]^{\mathcal{M}} } + [A]^{\mathcal{M}} }} \quad <em>(تعریف فصل)</em><br/>
        {{ = \overline{ (I_{\mathcal{M}}(A) + \overline{I_{\mathcal{M}}(B)}) \cdot I_{\mathcal{M}}(B) } + I_{\mathcal{M}}(A) }} \quad <em>(ارزیابی اتم‌ها و نقیض)</em>
      </div>

      <h4>(ب) اثبات اعتبار با استدلال معادلاتی (۶ نمره)</h4>
      <p>برای اختصار می‌نویسیم {{ a = I_{\mathcal{M}}(A) }} و {{ b = I_{\mathcal{M}}(B) }} :</p>
      <div style="line-height:2.2em; font-size:1.05em;" dir="ltr">
        {{ [F]^{\mathcal{M}} = \overline{ (a + \overline{b}) \cdot b } + a }}<br/>
        {{ \equiv (\overline{a + \overline{b}} + \overline{b}) + a }} \quad <em>(قانون دمرگان روی نقیض کلی)</em><br/>
        {{ \equiv ( (\overline{a} \cdot \overline{\overline{b}}) + \overline{b} ) + a }} \quad <em>(قانون دمرگان روی عبارت داخلی {{ \overline{a + \overline{b}} }})</em><br/>
        {{ \equiv ( (\overline{a} \cdot b) + \overline{b} ) + a }} \quad <em>(نفی مضاعف : {{ \overline{\overline{b}} = b }})</em><br/>
        {{ \equiv ( (\overline{a} + \overline{b}) \cdot (b + \overline{b}) ) + a }} \quad <em>(توزیع‌پذیری جمع روی ضرب {{ \cdot }})</em><br/>
        {{ \equiv ( (\overline{a} + \overline{b}) \cdot 1 ) + a }} \quad <em>(قانون متمم : {{ b + \overline{b} = 1 }})</em><br/>
        {{ \equiv (\overline{a} + \overline{b}) + a }} \quad <em>(عنصر همانی ضرب {{ \cdot }})</em><br/>
        {{ \equiv (\overline{a} + a) + \overline{b} }} \quad <em>(جابجایی و شرکت‌پذیری جمع)</em><br/>
        {{ \equiv 1 + \overline{b} }} \quad <em>(قانون متمم : {{ \overline{a} + a = 1 }})</em><br/>
        {{ \equiv 1 }} \quad <em>(عنصر جاذب : {{ 1 + x = 1 }})</em>
      </div>
      <p>از آنجا که {{ [F]^{\mathcal{M}} = 1 }} تحت هر تعبیر {{ \mathcal{M} }} برقرار است، <strong>فرمول {{ F }} معتبر است</strong>.</p>
    </div>
  </details>
</div>

<div class="q-card" id="p17_q2_cde">
  <div class="q-header">
    <span class="q-num">سوال ۲ (ج)، (د) و (هـ) (۷ نمره)</span>
    <span class="q-title">استنتاج‌های معنایی و خواص فرامنطقی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <ul>
      <li><strong>(ج) (۳ نمره) :</strong> آیا رابطه {{ (A \lor \neg B) \land B \models A }} برقرار است؟ (توجیه کنید).</li>
      <li><strong>(د) (۲ نمره) :</strong> فرض کنید {{ F_1 }} یک فرمول دلخواه باشد. آیا {{ \neg F \models F_1 }} برقرار است؟ (توجیه کنید).</li>
      <li><strong>(هـ) (۲ نمره) :</strong> فرض کنید {{ F_2 }} فرمولی باشد به طوری که {{ F \models F_2 }}. آیا {{ F_2 }} صدق‌پذیر است؟ آیا معتبر است؟ (توجیه کنید).</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوالات ۲(ج)، ۲(د) و ۲(هـ)</summary>
    <div class="box method">
      <h4>(ج) استلزام معنایی {{ (A \lor \neg B) \land B \models A }} (۳ نمره)</h4>
      <p><strong>بله.</strong> طبق قضیه بنیادین استنتاج معنایی، هم‌ارزی زیر برقرار است:</p>
      <p style="text-align:center; font-weight:bold;" dir="ltr">{{ P \models Q \quad \iff \quad \models (P \Rightarrow Q) }}</p>
      <p>از آنجا که در بخش (ب) اثبات شد فرمول {{ F = ((A \lor \neg B) \land B) \Rightarrow A }} معتبر است، بلافاصله نتیجه می‌گیریم که {{ (A \lor \neg B) \land B \models A }}.</p>

      <h4>(د) استلزام با نقیض فرمول معتبر {{ \neg F \models F_1 }} (۲ نمره)</h4>
      <p><strong>بله.</strong> از آنجا که {{ F }} معتبر است، نقیض آن {{ \neg F }} <strong>ناسازگار (تناقض)</strong> است. بنابراین مجموعه ساختارهایی که {{ \neg F }} را برآورده کنند <strong>تهی</strong> است. در نتیجه هر ساختاری که {{ \neg F }} را صادق کند، به طور بدیهی فرضیه را به انتفای مقدم برآورده ساخته و {{ F_1 }} را نتیجه می‌دهد. پس {{ \neg F \models F_1 }} صادق است.</p>

      <h4>(هـ) ماهیت فرمول {{ F_2 }} در صورت {{ F \models F_2 }} (۲ نمره)</h4>
      <p>چون فرمول {{ F }} معتبر است، تحت تمامی ساختارها {{ \mathcal{M} }}، مقدار {{ [F]^{\mathcal{M}} = 1 }} است.</p>
      <p>از طرفی رابطه {{ F \models F_2 }} بیان می‌کند هر مدلی از {{ F }} باید مدلی برای {{ F_2 }} باشد. از آنجا که <em>تمام</em> ساختارهای جهان مدل {{ F }} هستند، نتیجه می‌شود که <strong>تمام ساختارها مدل فرمول {{ F_2 }} خواهند بود</strong> ({{ \forall \mathcal{M}, [F_2]^{\mathcal{M}} = 1 }}).</p>
      <p><strong>نتیجه نهایی:</strong> بنابراین فرمول {{ F_2 }} الزاماً <strong>معتبر (توتولوژی)</strong> است (و در نتیجه <strong>صدق‌پذیر</strong> نیز می‌باشد).</p>
    </div>
  </details>
</div>

<!-- SUJET 2 : PARTIEL 2019-2020 L2 -->
<h2 id="annale_partiel_2019">2. Partiel 2019-2020 L2 – Exercice 3 : Preuve algébrique et relations avec G (8 points)</h2>

<div class="box info">
  <h4>مشخصات برگه امتحانی</h4>
  <p><strong>آزمون:</strong> میان‌ترم کارشناسی ۲۰۱۹-۲۰۲۰ — درس منطق UL2IN007.<br/>
  <strong>بارم رسمی:</strong> ۸ نمره (۱ نمره + ۱ نمره + ۲ نمره + ۴ نمره).<br/>
  <strong>فرمول مورد بررسی:</strong> {{ F = (\neg A \Rightarrow (A \land \neg A)) \Rightarrow A }}.</p>
</div>

<div class="q-card" id="p19_q1_q2ab">
  <div class="q-header">
    <span class="q-num">سوالات ۱، ۲(الف) و ۲(ب) (۴ نمره)</span>
    <span class="q-title">ترجمه و اثبات اعتبار جبری فرمول F</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <ol>
      <li>تعریف ریاضی فرمول معتبر {{ F }} را بنویسید.</li>
      <li>فرمول {{ F = (\neg A \Rightarrow (A \land \neg A)) \Rightarrow A }} را در نظر بگیرید:
        <ul>
          <li><strong>(الف) :</strong> عبارت بولی {{ [F]^{\mathcal{M}} }} را بدون ساده‌سازی بنویسید.</li>
          <li><strong>(ب) :</strong> با استدلال معادلاتی نشان دهید {{ F }} معتبر است.</li>
        </ul>
      </li>
    </ol>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی تشریحی</summary>
    <div class="box method">
      <h4>۱. تعریف صوری (۱ نمره)</h4>
      <p>فرمول {{ F }} معتبر است اگر و تنها اگر برای هر ساختار {{ \mathcal{M} }} داشته باشیم: {{ [F]^{\mathcal{M}} = 1 }}.</p>

      <h4>۲(الف) ترجمه خام بدون ساده‌سازی (۱ نمره)</h4>
      <div style="line-height:2em; font-size:1.05em;" dir="ltr">
        {{ [F]^{\mathcal{M}} = \overline{ [\neg A \Rightarrow (A \land \neg A)]^{\mathcal{M}} } + [A]^{\mathcal{M}} }}<br/>
        {{ = \overline{ \overline{[\neg A]^{\mathcal{M}}} + [A \land \neg A]^{\mathcal{M}} } + [A]^{\mathcal{M}} }}<br/>
        {{ = \overline{ \overline{\overline{I_{\mathcal{M}}(A)}} + (I_{\mathcal{M}}(A) \cdot \overline{I_{\mathcal{M}}(A)}) } + I_{\mathcal{M}}(A) }}
      </div>

      <h4>۲(ب) استدلال معادلاتی (۲ نمره)</h4>
      <p>با تعریف متغیر {{ x = I_{\mathcal{M}}(A) }} داریم:</p>
      <div style="line-height:2.2em; font-size:1.05em;" dir="ltr">
        {{ [F]^{\mathcal{M}} \equiv \overline{ x + (x \cdot \overline{x}) } + x }} \quad <em>(نفی مضاعف : {{ \overline{\overline{x}} = x }})</em><br/>
        {{ \equiv \overline{ x + 0 } + x }} \quad <em>(قانون متمم : {{ x \cdot \overline{x} = 0 }})</em><br/>
        {{ \equiv \overline{x} + x }} \quad <em>(عنصر همانی : {{ x + 0 = x }})</em><br/>
        {{ \equiv 1 }} \quad <em>(قانون متمم : {{ \overline{x} + x = 1 }})</em>
      </div>
      <p>بنابراین فرمول {{ F }} یک توتولوژی صوری و معتبر است.</p>
    </div>
  </details>
</div>

<div class="q-card" id="p19_q2c">
  <div class="q-header">
    <span class="q-num">سوال ۲(ج) (۴ نمره)</span>
    <span class="q-title">تحلیل ۴ استلزام با فرمول دلخواه G</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله</h4>
    <p>فرض کنید {{ G }} فرمولی دلخواه باشد. آیا روابط زیر برقرارند؟</p>
    <ul>
      <li>(i) آیا {{ G \models F }} برقرار است؟</li>
      <li>(ii) آیا {{ F \models G }} برقرار است؟</li>
      <li>(iii) آیا {{ G \models \neg F }} برقرار است؟</li>
      <li>(iv) آیا {{ \neg F \models G }} برقرار است؟</li>
    </ul>
    <p>پاسخ‌های خود را توجیه نمایید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی هر ۴ حالت</summary>
    <div class="box method">
      <ul>
        <li><strong>(i) آیا {{ G \models F }} برقرار است؟ &larr; بله (۱ نمره)</strong>
          <br/>تمامی ساختارهایی که {{ G }} را برآورده می‌سازند اجباراً {{ F }} را نیز برآورده می‌کنند، چرا که {{ F }} <strong>معتبر</strong> بوده و در تمامی ساختارهای ممکن مقدار ۱ دارد.
        </li>
        <li><strong>(ii) آیا {{ F \models G }} برقرار است؟ &larr; خیر (۱ نمره)</strong>
          <br/>چون {{ G }} فرمولی دلخواه است، می‌تواند گزاره‌ای باشد که در ساختاری خاص {{ \mathcal{M} }} مقدار صفر بگیرد (مثلاً {{ G = \text{false} }}). با این حال آن ساختار، {{ F }} را صادق می‌نماید چون {{ F }} معتبر است. پس یک پادمدل وجود دارد.
        </li>
        <li><strong>(iii) آیا {{ G \models \neg F }} برقرار است؟ &larr; خیر (۱ نمره)</strong>
          <br/>فرمول دلخواه {{ G }} می‌تواند توسط یک ساختار {{ \mathcal{M} }} برآورده شود (مثلاً {{ G = \text{true} }}). اما فرمول {{ \neg F }} ناسازگار است (چون {{ F }} معتبر است) و بنابراین هیچ ساختاری {{ \neg F }} را برآورده نمی‌کند.
        </li>
        <li><strong>(iv) آیا {{ \neg F \models G }} برقرار است؟ &larr; بله (۱ نمره)</strong>
          <br/>از آنجا که {{ F }} معتبر است، فرمول {{ \neg F }} <strong>ناسازگار</strong> است و مجموعه ساختارهایی که {{ \neg F }} را صادق کنند تهی است، که استلزام را به طور بدیهی درست می‌گرداند.
        </li>
      </ul>
    </div>
  </details>
</div>
'''

open(os.path.join(W02, 'annales.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W02, 'annales.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("annales.fr.html and annales.fa.html written.")
