#!/usr/bin/env python3
"""Authoring generator for TP Week 2 (Thème 2).
Exhaustive implementations and tutorials for:
- Exercice 4: is_satisfiable, is_valid, models, consequence_sem
- Exercice 5: decompose_simple, decompose (cas général avec équilibre des parenthèses), trouve_prochain_connec
"""
import os

W02 = '/home/mnasimi/sorbonne/Logic_Academy/content/w02'
os.makedirs(W02, exist_ok=True)

fr = r'''
<div class="lesson-header">
  <div class="badge">Sorbonne Université — L2 Informatique (UL2IN007)</div>
  <h1>TP Thème 2 : Satisfiabilité, Modèles et Décomposition de Formules</h1>
  <p class="lead">Travaux Pratiques officiels (2026-2027) : implémentation optimisée des prédicats sémantiques (satisfiabilité, validité, recherche de modèles, conséquence sémantique) et parseur complet avec équilibrage de parenthèses.</p>
</div>

<div class="toc-box">
  <h3>Sommaire du TP</h3>
  <ul>
    <li><a href="#tp2_ex4">1. Exercice 4 – Prédicats sémantiques efficaces sans table de vérité</a></li>
    <li><a href="#tp2_ex5">2. Exercice 5 – Parseur complet et analyse syntaxique robuste</a></li>
  </ul>
</div>

<!-- EXERCICE 4 -->
<h2 id="tp2_ex4">1. Exercice 4 – Prédicats sémantiques efficaces sans table de vérité</h2>

<div class="box info">
  <h4>Principe d'optimisation (Court-circuit / Early Exit)</h4>
  <p>L'énoncé de TP précise : <em>« Il est souvent inutile de calculer toutes les interprétations pour déterminer si une formule est satisfiable ou valide. »</em></p>
  <ul>
    <li>Pour la <strong>satisfiabilité</strong> : dès qu'une interprétation {{ I }} donne {{ [F]^I = 1 }}, on s'arrête immédiatement et on renvoie <code>True</code> sans explorer les autres lignes.</li>
    <li>Pour la <strong>validité</strong> : dès qu'une interprétation {{ I }} donne {{ [F]^I = 0 }} (contre-modèle), on s'arrête immédiatement et on renvoie <code>False</code>.</li>
  </ul>
</div>

<div class="q-card" id="tp2_q4_sat_val">
  <div class="q-header">
    <span class="q-num">Exercice 4 – Questions 1 &amp; 2</span>
    <span class="q-title">Fonctions is_satisfiable et is_valid avec arrêt anticipé</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Écrivez les fonctions suivantes :</p>
    <ul>
      <li><code>is_satisfiable(formule: str) -> bool</code> : renvoie <code>True</code> si la formule est satisfiable, <code>False</code> sinon.</li>
      <li><code>is_valid(formule: str) -> bool</code> : renvoie <code>True</code> si la formule est valide, <code>False</code> sinon.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Implémentations optimisées commentées</summary>
    <div class="box method">
      <pre><code>def is_satisfiable(formule: str) -> bool:
    """Détermine si formule admet au moins un modèle (arrêt dès le premier modèle)."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    for val in interpretations:
        if eval_formule(formule, val):
            return True  # Modèle trouvé : arrêt anticipé immédiat
            
    return False  # Aucun modèle trouvé : insatisfiable

def is_valid(formule: str) -> bool:
    """Détermine si formule est une tautologie (arrêt dès le premier contre-modèle)."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    for val in interpretations:
        if not eval_formule(formule, val):
            return False  # Contre-modèle trouvé : arrêt anticipé immédiat
            
    return True  # Vraie sous toutes les interprétations : valide</code></pre>
    </div>
  </details>
</div>

<div class="q-card" id="tp2_q4_models_entail">
  <div class="q-header">
    <span class="q-num">Exercice 4 – Questions 3 &amp; 4</span>
    <span class="q-title">Calcul des modèles et vérification de conséquence sémantique</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Écrivez les fonctions suivantes :</p>
    <ul>
      <li><code>models(formule: str) -> list[dict]</code> : renvoie la liste des interprétations pour lesquelles la formule s'interprète à <code>True</code>.
        <br/><em>Exemple :</em> <code>models("p OR q")</code> renvoie <code>[{'p': False, 'q': True}, {'p': True, 'q': False}, {'p': True, 'q': True}]</code>.
      </li>
      <li><code>consequence_sem(formule1: str, formule2: str) -> bool</code> : renvoie <code>True</code> si {{ F_2 }} est conséquence sémantique de {{ F_1 }} ({{ F_1 \models F_2 }}), <code>False</code> sinon.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Implémentations et analyse</summary>
    <div class="box method">
      <pre><code>def models(formule: str) -> list[dict[str, bool]]:
    """Construit la liste exhaustive de tous les modèles de la formule."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    liste_modeles = []
    for val in interpretations:
        if eval_formule(formule, val):
            liste_modeles.append(val)
            
    return liste_modeles

def consequence_sem(formule1: str, formule2: str) -> bool:
    """Vérifie si formule1 |= formule2 (tout modèle de F1 doit satisfaire F2)."""
    # L'ensemble des atomes doit couvrir les variables des deux formules
    tous_atomes = genere_fa(formule1) | genere_fa(formule2)
    interpretations = genere_interpretations(tous_atomes)
    
    for val in interpretations:
        # Si val est un modèle de F1, il doit obligatoirement rendre F2 vraie
        if eval_formule(formule1, val):
            if not eval_formule(formule2, val):
                return False  # Contre-modèle trouvé : [F1]^I = 1 et [F2]^I = 0
                
    return True</code></pre>
      <p><strong>Remarque sur le théorème de déduction :</strong> On aurait pu aussi écrire simplement :<br/>
      <code>return is_valid(f"({formule1}) IMPLIES ({formule2})")</code> ! Les deux approches sont sémantiquement équivalentes.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 5 -->
<h2 id="tp2_ex5">2. Exercice 5 – Parseur complet et analyse syntaxique robuste</h2>

<div class="q-card" id="tp2_q5_decompose_simple">
  <div class="q-header">
    <span class="q-num">Exercice 5 – Question 1</span>
    <span class="q-title">Décomposition sans parenthèses : decompose_simple(formule: str)</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Écrivez la fonction <code>decompose_simple(formule: str) -> tuple[str, list[str]]</code> qui s'applique aux formules sans parenthèses contenant au plus un connecteur.</p>
    <p>Exemples exigés :</p>
    <ul>
      <li><code>decompose_simple("p")</code> renvoie <code>('p', [])</code></li>
      <li><code>decompose_simple("NOT p")</code> renvoie <code>('NOT', ['p'])</code></li>
      <li><code>decompose_simple("p IMPLIES q")</code> renvoie <code>('IMPLIES', ['p', 'q'])</code></li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Implémentation robuste</summary>
    <div class="box method">
      <pre><code>def decompose_simple(formule: str) -> tuple[str, list[str]]:
    """Décompose une formule élémentaire sans parenthèses (au plus un connecteur)."""
    formule = formule.strip()
    
    # 1. Négation unaire NOT
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])
        
    # 2. Connecteurs binaires (IMPLIES, AND, OR)
    for op in ["IMPLIES", "AND", "OR"]:
        mot_cle = " " + op + " "
        if mot_cle in formule:
            parties = formule.split(mot_cle, 1)
            return (op, [parties[0].strip(), parties[1].strip()])
            
    # 3. Formule atomique simple ou constante
    return (formule, [])</code></pre>
    </div>
  </details>
</div>

<div class="q-card" id="tp2_q5_connec_and_full">
  <div class="q-header">
    <span class="q-num">Exercice 5 – Questions 2 &amp; 3</span>
    <span class="q-title">Analyse générale avec équilibre des parenthèses et recherche de connecteur</span>
  </div>
  <div class="box def">
    <h4>Énoncé officiel</h4>
    <p>Écrivez les fonctions :</p>
    <ul>
      <li><code>trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]</code> : renvoie le nom et la position du premier connecteur dont la position est supérieure ou égale à <code>index</code>.
        <br/><em>Exemple :</em> <code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> renvoie <code>('AND', 8)</code>.
      </li>
      <li><code>decompose(formule: str) -> tuple[str, list[str]] | None</code> : traite le cas général en vérifiant l'équilibre des parenthèses (renvoie <code>None</code> en cas d'erreur de parenthésage) et en supprimant les parenthèses superflues.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>Implémentation complète et commentée</summary>
    <div class="box method">
      <pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    """Trouve le premier connecteur apparaissant à partir de l'indice index."""
    sous_chaine = formule[index:]
    positions = []
    
    for op in ["IMPLIES", "AND", "OR", "NOT"]:
        pos = sous_chaine.find(op)
        if pos != -1:
            positions.append((pos + index, op))
            
    if not positions:
        return ("", -1)
        
    # On prend celui qui apparaît le plus tôt
    positions.sort(key=lambda x: x[0])
    pos_min, op_min = positions[0]
    return (op_min, pos_min)

def decompose(formule: str) -> tuple[str, list[str]] | None:
    """Analyse syntaxique complète d'une formule arbitraire."""
    formule = formule.strip()
    
    # 1. Vérification de l'équilibre des parenthèses
    ouvrantes = formule.count('(')
    fermantes = formule.count(')')
    if ouvrantes != fermantes:
        return None  # Formule mal parenthésée
        
    # Cas d'une formule sans aucune parenthèse
    if ouvrantes == 0:
        return decompose_simple(formule)
        
    # 2. Suppression des parenthèses externes inutiles englobant toute la formule
    # Attention : "(A) AND (B)" a '(' au début et ')' à la fin, mais ne forme pas un seul bloc !
    while formule.startswith('(') and formule.endswith(')'):
        # Vérifions si la parenthèse ouvrante initiale ne se ferme qu'au tout dernier caractère
        niveau = 0
        englobante = True
        for i in range(len(formule) - 1):
            if formule[i] == '(': niveau += 1
            elif formule[i] == ')': niveau -= 1
            if niveau == 0:
                englobante = False
                break
        if englobante:
            formule = formule[1:-1].strip()
        else:
            break
            
    # Cas de la négation NOT en début de formule
    if formule.startswith("NOT "):
        # Vérifier si NOT s'applique à toute la formule
        if formule.startswith("NOT ("):
            return ("NOT", [formule[4:].strip()])
            
    # 3. Recherche du connecteur principal au niveau 0 de parenthèses
    niveau = 0
    coupure = -1
    for i, c in enumerate(formule):
        if c == '(':
            niveau += 1
        elif c == ')':
            niveau -= 1
        elif niveau == 0 and c == ' ' and coupure == -1:
            coupure = i
            break
            
    if coupure != -1:
        op, pos = trouve_prochain_connec(formule, coupure)
        if pos != -1:
            gauche = formule[:pos].strip()
            droite = formule[pos + len(op):].strip()
            return (op, [gauche, droite])
            
    return decompose_simple(formule)</code></pre>
    </div>
  </details>
</div>
'''

fa = r'''
<div class="lesson-header">
  <div class="badge">دانشگاه سوربن — دوره کارشناسی علوم کامپیوتر (UL2IN007)</div>
  <h1>کارگاه عملی فصل ۲: صدق‌پذیری، مدل‌ها و تجزیه ساختاری فرمول‌ها</h1>
  <p class="lead">تکلیف کارگاهی رسمی (سال تحصیلی ۲۰۲۶-۲۰۲۷): پیاده‌سازی بهینه‌شده گزاره‌های معنایی (صدق‌پذیری، اعتبار، استخراج مدل‌ها، استلزام معنایی) و پارسر کامل همراه با تحلیل توازن پرانتزها.</p>
</div>

<div class="toc-box">
  <h3>فهرست مطالب کارگاه</h3>
  <ul>
    <li><a href="#tp2_ex4">۱. تمرین ۴ – توابع معنایی بهینه بدون جدول درستی</a></li>
    <li><a href="#tp2_ex5">۲. تمرین ۵ – پارسر کامل و تحلیل ساختاری نحوی</a></li>
  </ul>
</div>

<!-- EXERCICE 4 -->
<h2 id="tp2_ex4">1. Exercice 4 – Prédicats sémantiques efficaces sans table de vérité</h2>

<div class="box info">
  <h4>اصل بهینه‌سازی محاسباتی (خروج زودهنگام / Early Exit)</h4>
  <p>دستور کارگاه دانشگاه سوربن تصریح می‌کند: <em>«برای تعیین صدق‌پذیری یا اعتبار یک فرمول، اغلب نیازی به محاسبه تمام تعبیرها نیست.»</em></p>
  <ul>
    <li>برای <strong>صدق‌پذیری</strong>: به محض یافتن نخستین تعبیر {{ I }} که در آن {{ [F]^I = 1 }} شود، بررسی فوراً متوقف شده و مقدار <code>True</code> برگشت داده می‌شود.</li>
    <li>برای <strong>اعتبار</strong>: به محض یافتن نخستین تعبیر {{ I }} که در آن {{ [F]^I = 0 }} شود (پادمدل)، اجرای برنامه متوقف شده و مقدار <code>False</code> برگشت داده می‌شود.</li>
  </ul>
</div>

<div class="q-card" id="tp2_q4_sat_val">
  <div class="q-header">
    <span class="q-num">تمرین ۴ – سوالات ۱ و ۲</span>
    <span class="q-title">توابع is_satisfiable و is_valid با توقف زودهنگام</span>
  </div>
  <div class="box def">
    <h4>متن صورت مسئله رسمی</h4>
    <p>توابع زیر را پیاده‌سازی کنید:</p>
    <ul>
      <li><code>is_satisfiable(formule: str) -> bool</code> : در صورتی که فرمول صدق‌پذیر باشد مقدار <code>True</code> و در غیر این صورت <code>False</code> برگرداند.</li>
      <li><code>is_valid(formule: str) -> bool</code> : در صورتی که فرمول معتبر باشد مقدار <code>True</code> و در غیر این صورت <code>False</code> برگرداند.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پیاده‌سازی بهینه و توضیحات کد</summary>
    <div class="box method">
      <pre><code>def is_satisfiable(formule: str) -> bool:
    """Détermine si formule admet au moins un modèle (arrêt dès le premier modèle)."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    for val in interpretations:
        if eval_formule(formule, val):
            return True  # Modèle trouvé : arrêt anticipé immédiat
            
    return False  # Aucun modèle trouvé : insatisfiable

def is_valid(formule: str) -> bool:
    """Détermine si formule est une tautologie (arrêt dès le premier contre-modèle)."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    for val in interpretations:
        if not eval_formule(formule, val):
            return False  # Contre-modèle trouvé : arrêt anticipé immédiat
            
    return True  # Vraie sous toutes les interprétations : valide</code></pre>
    </div>
  </details>
</div>

<div class="q-card" id="tp2_q4_models_entail">
  <div class="q-header">
    <span class="q-num">تمرین ۴ – سوالات ۳ و ۴</span>
    <span class="q-title">یافتن مدل‌ها و بررسی استلزام معنایی</span>
  </div>
  <div class="box def">
    <h4>متن صورت مسئله رسمی</h4>
    <p>توابع زیر را پیاده‌سازی کنید:</p>
    <ul>
      <li><code>models(formule: str) -> list[dict]</code> : لیست تمام تعبیرهایی که فرمول در آن‌ها مقدار <code>True</code> می‌گیرد را تولید کند.
        <br/><em>نمونه:</em> عبارت <code>models("p OR q")</code> این لیست را برمی‌گرداند: <code>[{'p': False, 'q': True}, {'p': True, 'q': False}, {'p': True, 'q': True}]</code>.
      </li>
      <li><code>consequence_sem(formule1: str, formule2: str) -> bool</code> : اگر {{ F_2 }} نتیجه معنایی فرمول {{ F_1 }} باشد ({{ F_1 \models F_2 }}) مقدار <code>True</code> وگرنه <code>False</code> برگرداند.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پیاده‌سازی و تحلیل منطقی</summary>
    <div class="box method">
      <pre><code>def models(formule: str) -> list[dict[str, bool]]:
    """Construit la liste exhaustive de tous les modèles de la formule."""
    atomes = genere_fa(formule)
    interpretations = genere_interpretations(atomes)
    
    liste_modeles = []
    for val in interpretations:
        if eval_formule(formule, val):
            liste_modeles.append(val)
            
    return liste_modeles

def consequence_sem(formule1: str, formule2: str) -> bool:
    """Vérifie si formule1 |= formule2 (tout modèle de F1 doit satisfaire F2)."""
    # L'ensemble des atomes doit couvrir les variables des deux formules
    tous_atomes = genere_fa(formule1) | genere_fa(formule2)
    interpretations = genere_interpretations(tous_atomes)
    
    for val in interpretations:
        # Si val est un modèle de F1, il doit obligatoirement rendre F2 vraie
        if eval_formule(formule1, val):
            if not eval_formule(formule2, val):
                return False  # Contre-modèle trouvé : [F1]^I = 1 et [F2]^I = 0
                
    return True</code></pre>
      <p><strong>نکته مهم بر پایه قضیه استنتاج:</strong> می‌توانستیم این تابع را به شکل زیر نیز بنویسیم:<br/>
      <code>return is_valid(f"({formule1}) IMPLIES ({formule2})")</code> ! هر دو روش از نظر معنایی کاملاً هم‌ارز هستند.</p>
    </div>
  </details>
</div>

<!-- EXERCICE 5 -->
<h2 id="tp2_ex5">2. Exercice 5 – Parseur complet et analyse syntaxique robuste</h2>

<div class="q-card" id="tp2_q5_decompose_simple">
  <div class="q-header">
    <span class="q-num">تمرین ۵ – سوال ۱</span>
    <span class="q-title">تجزیه فرمول‌های بدون پرانتز: decompose_simple(formule: str)</span>
  </div>
  <div class="box def">
    <h4>متن صورت مسئله رسمی</h4>
    <p>تابع <code>decompose_simple(formule: str) -> tuple[str, list[str]]</code> را برای فرمول‌های فاقد پرانتز که حداکثر یک عملگر دارند بنویسید.</p>
    <p>نمونه‌های الزامی:</p>
    <ul>
      <li>عبارت <code>decompose_simple("p")</code> زوج مرتب <code>('p', [])</code> را برمی‌گرداند.</li>
      <li>عبارت <code>decompose_simple("NOT p")</code> زوج مرتب <code>('NOT', ['p'])</code> را برمی‌گرداند.</li>
      <li>عبارت <code>decompose_simple("p IMPLIES q")</code> زوج مرتب <code>('IMPLIES', ['p', 'q'])</code> را برمی‌گرداند.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پیاده‌سازی تمیز و ماژولار</summary>
    <div class="box method">
      <pre><code>def decompose_simple(formule: str) -> tuple[str, list[str]]:
    """Décompose une formule élémentaire sans parenthèses (au plus un connecteur)."""
    formule = formule.strip()
    
    # 1. Négation unaire NOT
    if formule.startswith("NOT "):
        return ("NOT", [formule[4:].strip()])
        
    # 2. Connecteurs binaires (IMPLIES, AND, OR)
    for op in ["IMPLIES", "AND", "OR"]:
        mot_cle = " " + op + " "
        if mot_cle in formule:
            parties = formule.split(mot_cle, 1)
            return (op, [parties[0].strip(), parties[1].strip()])
            
    # 3. Formule atomique simple ou constante
    return (formule, [])</code></pre>
    </div>
  </details>
</div>

<div class="q-card" id="tp2_q5_connec_and_full">
  <div class="q-header">
    <span class="q-num">تمرین ۵ – سوالات ۲ و ۳</span>
    <span class="q-title">تحلیل جامع با توازن پرانتزها و جستجوی عملگرها</span>
  </div>
  <div class="box def">
    <h4>متن صورت مسئله رسمی</h4>
    <p>توابع زیر را پیاده‌سازی کنید:</p>
    <ul>
      <li><code>trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]</code> : نام و اندیس نخستین عملگری که بعد از موقعیت <code>index</code> ظاهر می‌شود را بازگرداند.
        <br/><em>نمونه:</em> عبارت <code>trouve_prochain_connec("(NOT b) AND (q OR r)", 2)</code> مقدار <code>('AND', 8)</code> را برمی‌گرداند.
      </li>
      <li><code>decompose(formule: str) -> tuple[str, list[str]] | None</code> : حالت عمومی را با بررسی توازن پرانتزها بررسی کند (در صورت عدم توازن <code>None</code> دهد) و پرانتزهای خارجی اضافه را حذف نماید.</li>
    </ul>
  </div>

  <details class="sol" open>
    <summary>پیاده‌سازی کامل به همراه توضیحات تفصیلی</summary>
    <div class="box method">
      <pre><code>def trouve_prochain_connec(formule: str, index: int) -> tuple[str, int]:
    """Trouve le premier connecteur apparaissant à partir de l'indice index."""
    sous_chaine = formule[index:]
    positions = []
    
    for op in ["IMPLIES", "AND", "OR", "NOT"]:
        pos = sous_chaine.find(op)
        if pos != -1:
            positions.append((pos + index, op))
            
    if not positions:
        return ("", -1)
        
    # On prend celui qui apparaît le plus tôt
    positions.sort(key=lambda x: x[0])
    pos_min, op_min = positions[0]
    return (op_min, pos_min)

def decompose(formule: str) -> tuple[str, list[str]] | None:
    """Analyse syntaxique complète d'une formule arbitraire."""
    formule = formule.strip()
    
    # 1. Vérification de l'équilibre des parenthèses
    ouvrantes = formule.count('(')
    fermantes = formule.count(')')
    if ouvrantes != fermantes:
        return None  # Formule mal parenthésée
        
    # Cas d'une formule sans aucune parenthèse
    if ouvrantes == 0:
        return decompose_simple(formule)
        
    # 2. Suppression des parenthèses externes inutiles englobant toute la formule
    # Attention : "(A) AND (B)" a '(' au début et ')' à la fin, mais ne forme pas un seul bloc !
    while formule.startswith('(') and formule.endswith(')'):
        # Vérifions si la parenthèse ouvrante initiale ne se ferme qu'au tout dernier caractère
        niveau = 0
        englobante = True
        for i in range(len(formule) - 1):
            if formule[i] == '(': niveau += 1
            elif formule[i] == ')': niveau -= 1
            if niveau == 0:
                englobante = False
                break
        if englobante:
            formule = formule[1:-1].strip()
        else:
            break
            
    # Cas de la négation NOT en début de formule
    if formule.startswith("NOT "):
        # Vérifier si NOT s'applique à toute la formule
        if formule.startswith("NOT ("):
            return ("NOT", [formule[4:].strip()])
            
    # 3. Recherche du connecteur principal au niveau 0 de parenthèses
    niveau = 0
    coupure = -1
    for i, c in enumerate(formule):
        if c == '(':
            niveau += 1
        elif c == ')':
            niveau -= 1
        elif niveau == 0 and c == ' ' and coupure == -1:
            coupure = i
            break
            
    if coupure != -1:
        op, pos = trouve_prochain_connec(formule, coupure)
        if pos != -1:
            gauche = formule[:pos].strip()
            droite = formule[pos + len(op):].strip()
            return (op, [gauche, droite])
            
    return decompose_simple(formule)</code></pre>
    </div>
  </details>
</div>
'''

open(os.path.join(W02, 'tp.fr.html'), 'w', encoding='utf-8').write(fr.strip())
open(os.path.join(W02, 'tp.fa.html'), 'w', encoding='utf-8').write(fa.strip())
print("tp.fr.html and tp.fa.html written.")
