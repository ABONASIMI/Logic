Logic.reg("glossary", [
  {
    "id": "atome",
    "fr": "Formule atomique (Atome)",
    "fa": "فرمول اتمی (گزاره پایه)",
    "def_fr": "La plus petite unité syntaxique douée d'une valeur de vérité, ne contenant aucun connecteur ni quantificateur. En logique propositionnelle, c'est une variable propositionnelle (ex: p, q). En LPPO, c'est un prédicat appliqué à des termes (ex: P(t1, ..., tn)).",
    "def_fa": "کوچک‌ترین واحد نحوی دارای ارزش درستی که هیچ رابط یا سوری ندارد. در منطق گزاره‌ای یک متغیر گزاره‌ای است (مانند p) و در مرتبه اول، یک نماد محمول روی ترم‌هاست (مانند P(x, y)).",
    "why_fr": "Sert de brique élémentaire indissociable pour construire récursivement toutes les formules complexes.",
    "why_fa": "به عنوان بلوک بنیادین برای ساخت استقرایی فرمول‌های پیچیده‌تر به کار می‌رود."
  },
  {
    "id": "formule",
    "fr": "Formule bien formée (FBF)",
    "fa": "فرمول خوش‌ساخت",
    "def_fr": "Expression syntaxique construite inductivement à partir des atomes, des connecteurs (¬, ∧, ∨, ⇒, ⇔) et des parenthèses, respectant scrupuleusement la grammaire formelle.",
    "def_fa": "عبارت نحوی معتبری که بر اساس قواعد گرامر منطقی از اتم‌ها و رابط‌های منطقی ساخته شده است.",
    "why_fr": "Évite toute ambiguïté syntaxique et permet un traitement algorithmique uniforme par arbre de syntaxe abstraite.",
    "why_fa": "از هرگونه ابهام ساختاری جلوگیری کرده و امکان ارزیابی الگوریتمی را فراهم می‌کند."
  },
  {
    "id": "connecteur-principal",
    "fr": "Connecteur principal",
    "fa": "رابط اصلی",
    "def_fr": "Le connecteur logique dont la portée s'étend à l'ensemble de la formule. Dans l'arbre de syntaxe abstraite (AST), c'est l'étiquette de la racine. C'est la dernière opération exécutée lors de l'évaluation.",
    "def_fa": "رابط منطقی‌ای که دامنه اثر آن بر کل فرمول است و در درخت نحو انتزاعی در ریشه قرار می‌گیرد. این آخرین عملیاتی است که در محاسبه انجام می‌شود.",
    "why_fr": "Détermine la forme globale de la formule et guide le choix de la règle en déduction naturelle.",
    "why_fa": "شکل نهایی فرمول را تعیین کرده و قاعده اعمالی در استنتاج طبیعی را مشخص می‌کند."
  },
  {
    "id": "valuation",
    "fr": "Valuation (Interprétation propositionnelle)",
    "fa": "ارزش‌گذاری (تفسیر گزاره‌ای)",
    "def_fr": "Fonction v : V → {0, 1} qui attribue une valeur de vérité (Vrai/1 ou Faux/0) à chaque variable propositionnelle. Elle s'étend de manière unique à toute formule.",
    "def_fa": "تابعی که به هر متغیر گزاره‌ای یکی از مقادیر صفر یا یک را اختصاص می‌دهد.",
    "why_fr": "Définit le monde possible ou l'état de fait dans lequel la vérité d'une formule est calculée.",
    "why_fa": "جهان ممکن را برای ارزیابی صدق و کذب فرمول‌ها تعریف می‌کند."
  },
  {
    "id": "satisfiable",
    "fr": "Satisfiabilité",
    "fa": "صدق‌پذیری (سازگاری)",
    "def_fr": "Une formule F est satisfiable s'il existe au moins une valuation v telle que [F]_v = 1. Cette valuation est alors appelée un modèle de F.",
    "def_fa": "یک فرمول صدق‌پذیر است اگر حداقل یک ارزش‌گذاری وجود داشته باشد که آن را درست کند. به آن ارزش‌گذاری مدل فرمول می‌گویند.",
    "why_fr": "Notion centrale en informatique (problème SAT, résolution de contraintes).",
    "why_fa": "مفهوم محوری در علوم کامپیوتر (مسئله SAT و حل قیود)."
  },
  {
    "id": "valide",
    "fr": "Validité (Tautologie)",
    "fa": "اعتبار (تاتولوژی / راستگویی)",
    "def_fr": "Une formule F est valide (noté ⊨ F) si elle est vraie sous TOUTES les valuations possibles ([F]_v = 1 pour tout v).",
    "def_fa": "فرمول معتبر فرمولی است که تحت تمامی ارزش‌گذاری‌ها همواره مقدار یک (درست) داشته باشد.",
    "why_fr": "Représente les vérités logiques absolues indépendantes des faits du monde.",
    "why_fa": "بیانگر قوانین و حقایق بنیادین منطقی بدون وابستگی به شرایط دنیای خارج است."
  },
  {
    "id": "consequence-semantique",
    "fr": "Conséquence sémantique (⊨)",
    "fa": "پیامد معنایی (استلزام معنایی)",
    "def_fr": "G est conséquence sémantique de F (noté F ⊨ G) si tout modèle de F est aussi un modèle de G. Il est impossible que F soit vraie et G fausse.",
    "def_fa": "G پیامد معنایی F است اگر هر مدلی که F را درست کند، G را نیز الزاماً درست سازد.",
    "why_fr": "Définit la validité d'un raisonnement sémantique correct.",
    "why_fa": "تعریف‌کننده استدلال استنتاجی معتبر در علم منطق است."
  },
  {
    "id": "equivalence",
    "fr": "Équivalence logique (≡)",
    "fa": "هم‌ارزی منطقی",
    "def_fr": "Deux formules F et G sont équivalentes (F ≡ G) si elles ont exactement la même valeur de vérité sous toute valuation ([F]_v = [G]_v). Équivaut à ⊨ (F ⇔ G).",
    "def_fa": "دو فرمول هم‌ارزند اگر تحت هر ارزش‌گذاری، مقدار درستی یکسانی تولید کنند.",
    "why_fr": "Permet de remplacer une formule par une autre plus simple sans altérer sa signification.",
    "why_fa": "امکان ساده‌سازی فرمول‌ها را بدون تغییر در معنای آن‌ها فراهم می‌کند."
  },
  {
    "id": "fnc",
    "fr": "Forme Normale Conjonctive (FNC / CNF)",
    "fa": "فرم نرمال عطفی (FNC / CNF)",
    "def_fr": "Conjonction de clauses, où chaque clause est une disjonction de littéraux : ⋀_i ⋁_j l_{i,j}.",
    "def_fa": "عطف چند بند که هر بند خود فصلی از چند لیترال است.",
    "why_fr": "Format d'entrée universel des solveurs SAT modernes (Glucose, MiniSat) et de la méthode de résolution.",
    "why_fa": "ساختار ورودی استاندارد برای حل‌کننده‌های SAT و روش تحلیل و اثبات رابینسون."
  },
  {
    "id": "fnd",
    "fr": "Forme Normale Disjonctive (FND / DNF)",
    "fa": "فرم نرمال فصلی (FND / DNF)",
    "def_fr": "Disjonction de termes, où chaque terme est une conjonction de littéraux : ⋁_i ⋀_j l_{i,j}.",
    "def_fa": "فصل چند عبارت که هر عبارت خود عطفی از چند لیترال است.",
    "why_fr": "Facilite l'identification immédiate des modèles (chaque terme non contradictoire donne un modèle).",
    "why_fa": "یافتن مدل‌ها را آسان می‌کند زیرا هر ترم غیر متناقض یک مدل برای کل فرمول است."
  },
  {
    "id": "dpll",
    "fr": "Algorithme DPLL",
    "fa": "الگوریتم DPLL",
    "def_fr": "Algorithme de décision de la satisfiabilité d'un ensemble de clauses basé sur le retour sur trace (backtracking), la propagation unitaire et l'élimination des littéraux purs.",
    "def_fa": "الگوریتم پایه‌ای تصمیم‌گیری صدق‌پذیری برای فرم‌های FNC بر اساس پس‌گرد، قاعده تک‌عضوی و لیترال خالص.",
    "why_fr": "Le socle algorithmique de tous les solveurs SAT industriels actuels.",
    "why_fa": "پایه‌گذار اصلی تمامی حل‌کننده‌های صنعتی SAT در هوش مصنوعی و سخت‌افزار."
  },
  {
    "id": "deduction-naturelle",
    "fr": "Déduction Naturelle (⊢)",
    "fa": "استنتاج طبیعی",
    "def_fr": "Système formel de preuve mathématique inventé par Gentzen où chaque connecteur logique possède des règles d'introduction (I) et d'élimination (E).",
    "def_fa": "سیستم صوری اثبات که توسط گنتزن ابداع شد و برای هر رابط دو قاعده معرفی و حذف دارد.",
    "why_fr": "Formalise rigoureusement la démarche déductive des mathématiciens sans passer par des tables de vérité.",
    "why_fa": "روش استدلال ریاضی را بدون نیاز به جدول‌های درستی بزرگ به صورت صوری مدل می‌کند."
  },
  {
    "id": "intuitionniste-vs-classique",
    "fr": "Logique Intuitionniste vs Classique",
    "fa": "منطق شهودگرایانه در برابر کلاسیک",
    "def_fr": "La logique intuitionniste rejette le principe du tiers exclu (A ∨ ¬A) et la preuve par l'absurde classique (RAA) : pour prouver ∃x P(x), il faut construire explicitement un témoin. La logique classique accepte le tiers exclu.",
    "def_fa": "منطق شهودگرایانه اصل طرد شق ثالث و برهان خلف کلاسیک را نمی‌پذیرد و اثبات وجودی را نیازمند ساخت صریح می‌داند.",
    "why_fr": "Lien direct avec la théorie des types et la calculabilité (isomorphisme de Curry-Howard).",
    "why_fa": "ارتباط مستقیم با نظریه انواع و برنامه‌نویسی محاسباتی دارد (تطابق کوری-هاوارد)."
  },
  {
    "id": "terme",
    "fr": "Terme (LPPO)",
    "fa": "ترم (عبارت اسمی در مرتبه اول)",
    "def_fr": "Objet syntaxique désignant un élément du domaine de discours. Formé de constantes, variables et symboles de fonctions appliqués à des termes (ex: f(x, g(c))). Ne possède PAS de valeur de vérité.",
    "def_fa": "موجودیت نحوی برای اشاره به اشیاء جهان، ساخته‌شده از متغیرها، ثابت‌ها و توابع. ترم‌ها مقدار صدق و کذب ندارند.",
    "why_fr": "Permet de nommer et manipuler les individus d'un univers mathématique.",
    "why_fa": "امکان نام‌گذاری و دستکاری اشیاء درون دامنه سخن را فراهم می‌سازد."
  },
  {
    "id": "variable-libre-liee",
    "fr": "Variable libre vs liée",
    "fa": "متغیر آزاد در برابر مقید",
    "def_fr": "Une occurrence d'une variable x est liée si elle se trouve dans la portée d'un quantificateur (∀x ou ∃x) portant sur ce même symbole. Sinon, elle est libre.",
    "def_fa": "یک رخداد متغیر مقید است اگر در دامنه اثر سوری با همان متغیر قرار داشته باشد؛ در غیر این صورت آزاد است.",
    "why_fr": "Crucial pour éviter les captures de variables lors des substitutions mathématiques.",
    "why_fa": "برای جلوگیری از تله‌اندازی ناخواسته متغیرها هنگام جایگزینی در اثبات‌ها حیاتی است."
  },
  {
    "id": "unification",
    "fr": "Unification de Robinson",
    "fa": "یکسان‌سازی رابینسون",
    "def_fr": "Algorithme calculant le plus général unificateur (MGU) σ tel que deux termes ou atomes deviennent syntaxiquement identiques : t1 σ = t2 σ.",
    "def_fa": "الگوریتمی که کلی‌ترین جایگزینی (MGU) را برای یکسان کردن ساختار دو ترم یا اتم پیدا می‌کند.",
    "why_fr": "Cœur du moteur d'exécution de Prolog et de la résolution au premier ordre.",
    "why_fa": "هسته اصلی موتور اجرای پرولوگ و روش تحلیل در منطق مرتبه اول است."
  },
  {
    "id": "skolemisation",
    "fr": "Skolémisation",
    "fa": "اسکولم‌سازی",
    "def_fr": "Transformation éliminant les quantificateurs existentiels en remplaçant la variable quantifiée par une fonction (ou constante) de Skolem dépendant des quantificateurs universels englobants.",
    "def_fa": "فرآیند حذف سورهای وجودی با جایگزین کردن آن‌ها با توابع یا ثابت‌های اسکولم وابسته به سورهای کلی پیشین.",
    "why_fr": "Préserve l'équi-satisfiabilité et permet le passage à la forme clausale pour la résolution.",
    "why_fa": "صدق‌پذیری را حفظ کرده و فرمول را برای الگوریتم تحلیل آماده می‌سازد."
  }
]);
