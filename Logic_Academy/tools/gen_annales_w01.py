#!/usr/bin/env python3
"""Authoring generator for Annales Week 1 (Thème 1).
Contains full official exam corrections for:
- Examen 1 (2015-2016) - Exercice 2 (9 points) : Énigme judiciaire Eva, Raoul et Scoubidou
- Examen 2 (2015-2016) - Exercice 2 (9 points) : Énigme judiciaire Conrad, Paul et Ursule
"""
import os

W01 = '/home/mnasimi/sorbonne/Logic_Academy/content/w01'
os.makedirs(W01, exist_ok=True)

fr = """
<div class="lesson-header">
  <div class="badge">Sorbonne Université — Annales Officielles Corrigées</div>
  <h1>Annales Thème 1 : Énigmes Judiciaires et Conséquence Sémantique</h1>
  <p class="lead">Sujets réels d'examens de la Sorbonne avec énoncés intégraux, grilles de points officielles, stratégies de résolution et corrigés détaillés basés sur les corrections de l'équipe pédagogique.</p>
</div>

<div class="toc-box">
  <h3>Sujets d'examen traités</h3>
  <ul>
    <li><a href="#annale_2015_ex1">1. Examen 1 (2015-2016) – Exercice 2 : Eva, Raoul et Scoubidou (9 points)</a></li>
    <li><a href="#annale_2015_ex2">2. Examen 2 (2015-2016) – Exercice 2 : Conrad, Paul et Ursule (9 points)</a></li>
  </ul>
</div>

<h2 id="annale_2015_ex1">1. Examen 1 (2015-2016) – Exercice 2 : Eva, Raoul et Scoubidou (9 points)</h2>

<div class="box info">
  <h4>Référence de l'épreuve</h4>
  <p><strong>Session :</strong> Examen 1 (Fin de semestre) 2015-2016 — Épreuve de Logique UL2IN007.<br/>
  <strong>Barème officiel :</strong> 9 points (3 + 3 + 3 points pour les trois questions).<br/>
  <strong>Notions requises :</strong> Formalisation propositionnelle, implication matérielle, table de vérité, conséquence sémantique.</p>
</div>

<div class="q-card" id="annale_1_q1">
  <div class="q-header">
    <span class="q-num">Question 1 (3 points)</span>
    <span class="q-title">Formalisation des déclarations des trois suspects</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Eva, Raoul et Scoubidou sont tous les trois accusés d'un crime et ils font les déclarations suivantes :</p>
    <ul>
      <li><strong>Eva :</strong> « Si Scoubidou est innocent, alors Raoul est coupable. »</li>
      <li><strong>Raoul :</strong> « Si Eva est coupable, alors je suis aussi coupable. »</li>
      <li><strong>Scoubidou :</strong> « Si Eva est innocente, alors Raoul est coupable. »</li>
    </ul>
    <p>À l'aide des trois propositions :</p>
    <ul>
      <li>{{ e }} : « Eva est coupable »</li>
      <li>{{ r }} : « Raoul est coupable »</li>
      <li>{{ s }} : « Scoubidou est coupable »</li>
    </ul>
    <p>formaliser les déclarations de Eva, Raoul et Scoubidou.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 1</summary>
    <div class="box method">
      <h4>Traductions formelles</h4>
      <ul>
        <li><strong>Déclaration d'Eva :</strong> Scoubidou est innocent se traduit par {{ \neg s }}. L'implication « si ... alors ... » donne directement :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_E = \neg s \Rightarrow r }}</p>
        </li>
        <li><strong>Déclaration de Raoul :</strong> Eva est coupable ({{ e }}) entraîne que Raoul est coupable ({{ r }}) :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_R = e \Rightarrow r }}</p>
        </li>
        <li><strong>Déclaration de Scoubidou :</strong> Eva est innocente se traduit par {{ \neg e }} :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_S = \neg e \Rightarrow r }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_1_q2">
  <div class="q-header">
    <span class="q-num">Question 2 (3 points)</span>
    <span class="q-title">Déduction de culpabilité par conséquence sémantique</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>On suppose que tous les trois disent la vérité. Que peut-on dire sur la culpabilité de Eva, de Raoul, de Scoubidou ? (Justifier vos réponses en utilisant la notion de conséquence sémantique).</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 2</summary>
    <div class="box method">
      <p>Construisons la table de vérité des trois formules sur les {{ 2^3 = 8 }} interprétations possibles :</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ I(e) }}</th>
            <th>{{ I(r) }}</th>
            <th>{{ I(s) }}</th>
            <th>{{ [\neg s \Rightarrow r]^I }}</th>
            <th>{{ [e \Rightarrow r]^I }}</th>
            <th>{{ [\neg e \Rightarrow r]^I }}</th>
            <th>Modèle simultané</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>Non</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>Non</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">Oui ({{ I_1 }})</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">Oui ({{ I_2 }})</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>Non ({{ I_0 }})</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>Non</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">Oui ({{ I_3 }})</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">Oui ({{ I_4 }})</strong></td></tr>
        </tbody>
      </table>

      <h4>Justification rigoureuse par conséquence sémantique</h4>
      <p>On constate qu'il existe exactement quatre interprétations {{ I_1, I_2, I_3 }} et {{ I_4 }} qui rendent simultanément vraies les formules {{ \neg s \Rightarrow r }}, {{ e \Rightarrow r }} et {{ \neg e \Rightarrow r }}.</p>
      <ul>
        <li>Puisque d'une part {{ I_2(e) = 0 }} et {{ I_3(e) = 1 }}, et d'autre part {{ I_1(s) = 0 }} et {{ I_2(s) = 1 }}, <strong>on ne peut rien déduire sur {{ e }} et {{ s }}</strong> (l'innocence ou la culpabilité d'Eva et de Scoubidou demeure indéterminée).</li>
        <li>Enfin, puisque dans tous les modèles sans exception on a :
          <p style="text-align:center; font-weight:bold;">{{ I_1(r) = I_2(r) = I_3(r) = I_4(r) = 1 }}</p>
          on en déduit formellement que <strong>Raoul est coupable</strong> ({{ \{F_E, F_R, F_S\} \models r }}).
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_1_q3">
  <div class="q-header">
    <span class="q-num">Question 3 (3 points)</span>
    <span class="q-title">Identification des menteurs sous l'interprétation réelle</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>L'enquête montre que Eva est coupable et que Raoul et Scoubidou sont innocents. Déterminer qui a menti et qui a dit la vérité.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 3</summary>
    <div class="box method">
      <p>La conclusion des enquêteurs correspond à l'interprétation réelle suivante :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ I_0 = \{e: 1, r: 0, s: 0\} }}</p>
      <p>Évaluons la valeur de vérité de chaque déclaration sous {{ I_0 }} :</p>
      <ul>
        <li><strong>Eva :</strong> {{ [\neg s \Rightarrow r]^{I_0} = [\neg 0 \Rightarrow 0] = [1 \Rightarrow 0] = 0 }}. <strong>Eva a menti.</strong></li>
        <li><strong>Raoul :</strong> {{ [e \Rightarrow r]^{I_0} = [1 \Rightarrow 0] = 0 }}. <strong>Raoul a menti.</strong></li>
        <li><strong>Scoubidou :</strong> {{ [\neg e \Rightarrow r]^{I_0} = [\neg 1 \Rightarrow 0] = [0 \Rightarrow 0] = 1 }}. <strong>Scoubidou a dit la vérité.</strong></li>
      </ul>
      <p><strong>Conclusion :</strong> Eva et Raoul ont menti, tandis que Scoubidou a dit la vérité.</p>
    </div>
  </details>
</div>

<h2 id="annale_2015_ex2">2. Examen 2 (2015-2016) – Exercice 2 : Conrad, Paul et Ursule (9 points)</h2>

<div class="box info">
  <h4>Référence de l'épreuve</h4>
  <p><strong>Session :</strong> Examen 2 (Session de rattrapage) 2015-2016 — Épreuve de Logique UL2IN007.<br/>
  <strong>Barème officiel :</strong> 9 points (3 + 3 + 3 points).<br/>
  <strong>Notions requises :</strong> Formalisation de « au moins deux », implications avec conclusions composées.</p>
</div>

<div class="q-card" id="annale_2_q1">
  <div class="q-header">
    <span class="q-num">Question 1 (3 points)</span>
    <span class="q-title">Formalisation des déclarations</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Conrad, Paul et Ursule sont tous les trois accusés d'un crime et font les déclarations suivantes :</p>
    <ul>
      <li><strong>Conrad :</strong> « Au moins deux d'entre nous sont coupables. »</li>
      <li><strong>Paul :</strong> « Si je suis coupable, alors Ursule est aussi coupable et Conrad est innocent. »</li>
      <li><strong>Ursule :</strong> « Si Conrad est coupable, alors Paul et moi sommes innocents. »</li>
    </ul>
    <p>Propositions : {{ p }} : « Conrad est coupable », {{ q }} : « Paul est coupable », {{ r }} : « Ursule est coupable ».</p>
    <p>Formaliser les déclarations des trois suspects.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 1</summary>
    <div class="box method">
      <ul>
        <li><strong>Conrad :</strong> « Au moins deux coupables » signifie (Conrad et Paul) ou (Conrad et Ursule) ou (Paul et Ursule) :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_C = (p \land q) \lor (p \land r) \lor (q \land r) }}</p>
        </li>
        <li><strong>Paul :</strong> Si Paul est coupable ({{ q }}), alors Ursule est coupable ({{ r }}) et Conrad est innocent ({{ \neg p }}) :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_P = q \Rightarrow (r \land \neg p) }}</p>
        </li>
        <li><strong>Ursule :</strong> Si Conrad est coupable ({{ p }}), alors Paul est innocent ({{ \neg q }}) et Ursule est innocente ({{ \neg r }}) :
          <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ F_U = p \Rightarrow (\neg q \land \neg r) }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_2_q2">
  <div class="q-header">
    <span class="q-num">Question 2 (3 points)</span>
    <span class="q-title">Résolution sous l'hypothèse de sincérité</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>On suppose que tous les trois disent la vérité. Que peut-on dire sur la culpabilité de Conrad, de Paul, de Ursule ?</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 2</summary>
    <div class="box method">
      <p>Construisons la table de vérité sur les 8 interprétations :</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ I(p) }}</th>
            <th>{{ I(q) }}</th>
            <th>{{ I(r) }}</th>
            <th>{{ [F_C]^I }}</th>
            <th>{{ [F_P]^I }}</th>
            <th>{{ [F_U]^I }}</th>
            <th>Modèle simultané</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>Non</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>Non</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>Non</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">Oui ({{ I_1 }})</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>Non</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>Non ({{ I_2 }})</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>Non</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>Non</td></tr>
        </tbody>
      </table>

      <h4>Conclusion officielle</h4>
      <p>On constate qu'il existe <strong>une unique interprétation {{ I_1 }}</strong> qui rend simultanément vraies les trois formules.</p>
      <p>Puisque dans cette interprétation {{ I_1(p) = 0 }} et {{ I_1(q) = I_1(r) = 1 }}, on en déduit de façon certaine que :</p>
      <ul>
        <li><strong>Conrad est innocent</strong> ({{ I_1(p) = 0 }}).</li>
        <li><strong>Paul et Ursule sont coupables</strong> ({{ I_1(q) = 1 }} et {{ I_1(r) = 1 }}).</li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_2_q3">
  <div class="q-header">
    <span class="q-num">Question 3 (3 points)</span>
    <span class="q-title">Analyse du cas réel</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>L'enquête montre que Conrad et Ursule sont coupables et que Paul est innocent. Déterminer qui a menti et qui a dit la vérité.</p>
  </div>

  <details class="sol" open>
    <summary>Corrigé officiel de la Question 3</summary>
    <div class="box method">
      <p>Cette situation correspond à l'interprétation :</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;">{{ I_2 = \{p: 1, q: 0, r: 1\} }}</p>
      <p>En observant la ligne {{ I_2 }} de la table de vérité :</p>
      <ul>
        <li>{{ [F_C]^{I_2} = 1 }} : <strong>Conrad a dit la vérité.</strong></li>
        <li>{{ [F_P]^{I_2} = 1 }} : <strong>Paul a dit la vérité.</strong> (Sa prémisse {{ q=0 }} étant fausse, son implication est automatiquement vraie).</li>
        <li>{{ [F_U]^{I_2} = 0 }} : <strong>Ursule a menti.</strong> (Conrad étant coupable {{ p=1 }}, sa conclusion attendue était que Paul et elle soient innocents {{ 0 \land 0 = 0 }}, donc {{ 1 \Rightarrow 0 = 0 }}).</li>
      </ul>
      <p><strong>Conclusion :</strong> Conrad et Paul ont dit la vérité, tandis qu'Ursule a menti.</p>
    </div>
  </details>
</div>
"""

fa = """
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — پاسخ‌نامه رسمی امتحانات نهایی</div>
  <h1>امتحانات فصل ۱: معماهای قضایی و استلزام معنایی</h1>
  <p class="lead">مسائل واقعی امتحانات نهایی دانشگاه سوربن همراه با متن دست‌نخورده، بارم‌بندی رسمی، راهبردهای استنتاجی و پاسخ‌های تشریحی بر پایه تصحیح رسمی اساتید درس.</p>
</div>

<div class="toc-box">
  <h3>امتحانات مورد بررسی</h3>
  <ul>
    <li><a href="#annale_2015_ex1">۱. امتحان نهایی ۱ (سال ۲۰۱۵-۲۰۱۶) – تمرین ۲ : اوا، رائول و اسکوبیدو (۹ نمره)</a></li>
    <li><a href="#annale_2015_ex2">۲. امتحان نهایی ۲ (سال ۲۰۱۵-۲۰۱۶) – تمرین ۲ : کنراد، پل و اورسول (۹ نمره)</a></li>
  </ul>
</div>

<h2 id="annale_2015_ex1">1. Examen 1 (2015-2016) – Exercice 2 : Eva, Raoul et Scoubidou (9 points)</h2>

<div class="box info">
  <h4>مشخصات برگه امتحانی</h4>
  <p><strong>دوره آزمون:</strong> امتحان پایانی اول (پایان نیم‌سال) ۲۰۱۵-۲۰۱۶ — درس منطق UL2IN007.<br/>
  <strong>بارم رسمی:</strong> ۹ نمره (۳ سوال، هر سوال ۳ نمره).<br/>
  <strong>مفاهیم پیش‌نیاز:</strong> فرمول‌بندی گزاره‌ای، شرطی مادی، جدول درستی، نتیجه معنایی.</p>
</div>

<div class="q-card" id="annale_1_q1">
  <div class="q-header">
    <span class="q-num">سوال ۱ (۳ نمره)</span>
    <span class="q-title">فرمول‌بندی ادعاهای هر سه مظنون</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>اوا، رائول و اسکوبیدو متهم به یک فقره جرم هستند و اظهارات زیر را بیان می‌کنند:</p>
    <ul>
      <li><strong>اوا:</strong> «اگر اسکوبیدو بی‌گناه باشد، آنگاه رائول گناهکار است.»</li>
      <li><strong>رائول:</strong> «اگر اوا گناهکار باشد، آنگاه من هم گناهکارم.»</li>
      <li><strong>اسکوبیدو:</strong> «اگر اوا بی‌گناه باشد، آنگاه رائول گناهکار است.»</li>
    </ul>
    <p>با استفاده از گزاره‌های زیر:</p>
    <ul>
      <li>{{ e }}: «اوا گناهکار است»</li>
      <li>{{ r }}: «رائول گناهکار است»</li>
      <li>{{ s }}: «اسکوبیدو گناهکار است»</li>
    </ul>
    <p>اظهارات اوا، رائول و اسکوبیدو را فرمول‌بندی صوری کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۱</summary>
    <div class="box method">
      <h4>ترجمه صوری ادعاها</h4>
      <ul>
        <li><strong>اظهارات اوا:</strong> بی‌گناهی اسکوبیدو با {{ \neg s }} نمایش داده می‌شود. عبارت شرطی مستقیم حاصل می‌شود:
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_E = \neg s \Rightarrow r }}</p>
        </li>
        <li><strong>اظهارات رائول:</strong> گناهکاری اوا ({{ e }}) نتیجه می‌دهد که رائول گناهکار است ({{ r }}):
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_R = e \Rightarrow r }}</p>
        </li>
        <li><strong>اظهارات اسکوبیدو:</strong> بی‌گناهی اوا به صورت {{ \neg e }} بیان می‌شود:
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_S = \neg e \Rightarrow r }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_1_q2">
  <div class="q-header">
    <span class="q-num">سوال ۲ (۳ نمره)</span>
    <span class="q-title">استنتاج گناهکاری از طریق نتیجه معنایی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>فرض می‌کنیم هر سه نفر حقیقت را می‌گویند. درباره گناهکاری اوا، رائول و اسکوبیدو چه می‌توان گفت؟ (پاسخ‌های خود را با مفهوم نتیجه معنایی توجیه کنید).</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۲</summary>
    <div class="box method">
      <p>جدول درستی هر سه فرمول را بر روی تمام {{ 2^3 = 8 }} تعبیر ممکن تشکیل می‌دهیم:</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ I(e) }}</th>
            <th>{{ I(r) }}</th>
            <th>{{ I(s) }}</th>
            <th>{{ [\neg s \Rightarrow r]^I }}</th>
            <th>{{ [e \Rightarrow r]^I }}</th>
            <th>{{ [\neg e \Rightarrow r]^I }}</th>
            <th>مدل هم‌زمان</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>خیر</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>خیر</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">بله ({{ I_1 }})</strong></td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">بله ({{ I_2 }})</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>خیر ({{ I_0 }})</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>خیر</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">بله ({{ I_3 }})</strong></td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">بله ({{ I_4 }})</strong></td></tr>
        </tbody>
      </table>

      <h4>استدلال دقیق بر اساس نتیجه معنایی (Conséquence sémantique)</h4>
      <p>مشاهده می‌کنیم که دقیقاً چهار تعبیر {{ I_1, I_2, I_3 }} و {{ I_4 }} وجود دارند که هر سه فرمول {{ \neg s \Rightarrow r }} و {{ e \Rightarrow r }} و {{ \neg e \Rightarrow r }} را هم‌زمان صادق می‌کنند.</p>
      <ul>
        <li>از آنجا که از یک طرف {{ I_2(e) = 0 }} و {{ I_3(e) = 1 }}، و از طرف دیگر {{ I_1(s) = 0 }} و {{ I_2(s) = 1 }} است، <strong>هیچ نتیجه‌ای درباره {{ e }} و {{ s }} نمی‌توان گرفت</strong> (وضعیت اوا و اسکوبیدو نامشخص می‌ماند).</li>
        <li>اما در تمام مدل‌ها بدون هیچ استثنایی داریم:
          <p style="text-align:center; font-weight:bold;" dir="ltr">{{ I_1(r) = I_2(r) = I_3(r) = I_4(r) = 1 }}</p>
          بنابراین نتیجه صوری به دست می‌آید که <strong>رائول قطعاً گناهکار است</strong> ({{ \{F_E, F_R, F_S\} \models r }}).
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_1_q3">
  <div class="q-header">
    <span class="q-num">سوال ۳ (۳ نمره)</span>
    <span class="q-title">شناسایی دروغگویان بر پایه حقیقت بازپرسی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>تحقیقات نهایی بازپرس نشان می‌دهد که اوا گناهکار است و رائول و اسکوبیدو بی‌گناه هستند. مشخص کنید چه کسی دروغ گفته و چه کسی راست گفته است.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۳</summary>
    <div class="box method">
      <p>یافته‌های پلیس دقیقاً متناظر با تعبیر واقعی زیر است:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ I_0 = \{e: 1, r: 0, s: 0\} }}</p>
      <p>ارزش درستی ادعای هر فرد را تحت {{ I_0 }} محاسبه می‌کنیم:</p>
      <ul>
        <li><strong>اوا:</strong> {{ [\neg s \Rightarrow r]^{I_0} = [\neg 0 \Rightarrow 0] = [1 \Rightarrow 0] = 0 }}. <strong>اوا دروغ گفته است.</strong></li>
        <li><strong>رائول:</strong> {{ [e \Rightarrow r]^{I_0} = [1 \Rightarrow 0] = 0 }}. <strong>رائول دروغ گفته است.</strong></li>
        <li><strong>اسکوبیدو:</strong> {{ [\neg e \Rightarrow r]^{I_0} = [\neg 1 \Rightarrow 0] = [0 \Rightarrow 0] = 1 }}. <strong>اسکوبیدو راست گفته است.</strong></li>
      </ul>
      <p><strong>نتیجه نهایی:</strong> اوا و رائول دروغ گفته‌اند، و اسکوبیدو راست گفته است.</p>
    </div>
  </details>
</div>

<h2 id="annale_2015_ex2">2. Examen 2 (2015-2016) – Exercice 2 : Conrad, Paul et Ursule (9 points)</h2>

<div class="box info">
  <h4>مشخصات برگه امتحانی</h4>
  <p><strong>دوره آزمون:</strong> امتحان پایانی دوم (نوبت جبرانی) ۲۰۱۵-۲۰۱۶ — درس منطق UL2IN007.<br/>
  <strong>بارم رسمی:</strong> ۹ نمره (۳ سوال، هر سوال ۳ نمره).<br/>
  <strong>مفاهیم پیش‌نیاز:</strong> فرمول‌بندی «حداقل دو نفر»، جملات شرطی با نتیجه‌های عطفی ترکیبی.</p>
</div>

<div class="q-card" id="annale_2_q1">
  <div class="q-header">
    <span class="q-num">سوال ۱ (۳ نمره)</span>
    <span class="q-title">فرمول‌بندی ادعاهای مظنونین</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>کنراد، پل و اورسول متهم به یک جرم هستند و ادعاهای زیر را بیان می‌کنند:</p>
    <ul>
      <li><strong>کنراد:</strong> «حداقل دو نفر از ما گناهکار هستند.»</li>
      <li><strong>پل:</strong> «اگر من گناهکار باشم، آنگاه اورسول هم گناهکار است و کنراد بی‌گناه است.»</li>
      <li><strong>اورسول:</strong> «اگر کنراد گناهکار باشد، آنگاه من و پل بی‌گناهیم.»</li>
    </ul>
    <p>گزاره‌ها: {{ p }}: «کنراد گناهکار است»، {{ q }}: «پل گناهکار است»، {{ r }}: «اورسول گناهکار است».</p>
    <p>ادعاهای هر سه نفر را فرمول‌بندی کنید.</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۱</summary>
    <div class="box method">
      <ul>
        <li><strong>کنراد:</strong> «حداقل دو گناهکار» یعنی (کنراد و پل) یا (کنراد و اورسول) یا (پل و اورسول):
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_C = (p \land q) \lor (p \land r) \lor (q \land r) }}</p>
        </li>
        <li><strong>پل:</strong> اگر پل گناهکار باشد ({{ q }})، آنگاه اورسول گناهکار است ({{ r }}) و کنراد بی‌گناه است ({{ \neg p }}):
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_P = q \Rightarrow (r \land \neg p) }}</p>
        </li>
        <li><strong>اورسول:</strong> اگر کنراد گناهکار باشد ({{ p }})، آنگاه پل بی‌گناه است ({{ \neg q }}) و اورسول نیز بی‌گناه است ({{ \neg r }}):
          <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ F_U = p \Rightarrow (\neg q \land \neg r) }}</p>
        </li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_2_q2">
  <div class="q-header">
    <span class="q-num">سوال ۲ (۳ نمره)</span>
    <span class="q-title">یافتن مجرمین در فرض صداقت همگانی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>فرض می‌کنیم هر سه نفر راست می‌گویند. درباره گناهکاری کنراد، پل و اورسول چه نتیجه‌ای می‌توان گرفت؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۲</summary>
    <div class="box method">
      <p>جدول درستی را روی ۸ تعبیر ممکن رسم می‌کنیم:</p>
      <table class="logic-table" style="width:100%;">
        <thead>
          <tr>
            <th>{{ I(p) }}</th>
            <th>{{ I(q) }}</th>
            <th>{{ I(r) }}</th>
            <th>{{ [F_C]^I }}</th>
            <th>{{ [F_P]^I }}</th>
            <th>{{ [F_U]^I }}</th>
            <th>مدل هم‌زمان</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>خیر</td></tr>
          <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>خیر</td></tr>
          <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>خیر</td></tr>
          <tr><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td><strong style="color:#27ae60;">بله ({{ I_1 }})</strong></td></tr>
          <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>خیر</td></tr>
          <tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>خیر ({{ I_2 }})</td></tr>
          <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>خیر</td></tr>
          <tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>خیر</td></tr>
        </tbody>
      </table>

      <h4>نتیجه‌گیری قطعی طبق برگه اساتید</h4>
      <p>مشاهده می‌شود که <strong>تنها یک تعبیر یکتای {{ I_1 }}</strong> وجود دارد که هر سه فرمول را هم‌زمان برقرار می‌کند.</p>
      <p>در این تعبیر مشخص است که {{ I_1(p) = 0 }} و {{ I_1(q) = I_1(r) = 1 }}. بنابراین با قطعیت نتیجه می‌گیریم که:</p>
      <ul>
        <li><strong>کنراد بی‌گناه است</strong> ({{ I_1(p) = 0 }}).</li>
        <li><strong>پل و اورسول گناهکار هستند</strong> ({{ I_1(q) = 1 }} و {{ I_1(r) = 1 }}).</li>
      </ul>
    </div>
  </details>
</div>

<div class="q-card" id="annale_2_q3">
  <div class="q-header">
    <span class="q-num">سوال ۳ (۳ نمره)</span>
    <span class="q-title">تحلیل وضعیت واقعی بازپرسی</span>
  </div>
  <div class="box def">
    <h4>متن اصلی صورت مسئله امتحان</h4>
    <p>تحقیقات نشان می‌دهد کنراد و اورسول گناهکارند و پل بی‌گناه است. چه کسی راست گفته و چه کسی دروغ؟</p>
  </div>

  <details class="sol" open>
    <summary>پاسخ‌نامه رسمی سوال ۳</summary>
    <div class="box method">
      <p>این وضعیت معادل با تعبیر زیر است:</p>
      <p style="text-align:center; font-weight:bold; font-size:1.1em;" dir="ltr">{{ I_2 = \{p: 1, q: 0, r: 1\} }}</p>
      <p>با ارزیابی سطر متناظر با {{ I_2 }} در جدول درستی داریم:</p>
      <ul>
        <li>{{ [F_C]^{I_2} = 1 }}: <strong>کنراد راست گفته است.</strong></li>
        <li>{{ [F_P]^{I_2} = 1 }}: <strong>پل راست گفته است.</strong> (زیرا فرض {{ q=0 }} نادرست بوده و استلزام به طور خودکار درست است).</li>
        <li>{{ [F_U]^{I_2} = 0 }}: <strong>اورسول دروغ گفته است.</strong> (زیرا کنراد گناهکار است {{ p=1 }} اما نتیجه بی‌گناهی هر دو نفر غلط بود {{ 0 \land 0 = 0 }}، لذا {{ 1 \Rightarrow 0 = 0 }}).</li>
      </ul>
      <p><strong>نتیجه نهایی:</strong> کنراد و پل راست گفته‌اند، و اورسول دروغ گفته است.</p>
    </div>
  </details>
</div>
"""

open(os.path.join(W01, 'annales.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W01, 'annales.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("annales.fr.html and annales.fa.html written.")

