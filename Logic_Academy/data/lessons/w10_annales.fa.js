Logic.reg("lesson:w10_annales:fa", {
  id: "w10_annales",
  lang: "fa",
  status: "complete",
  html: "\n<div class=\"box box-objectives\">\n  <div class=\"box-title\">نمونه سؤالات امتحانی — هفته ۱۰ (تفکیک و یکسان‌سازی)</div>\n  <p>موضوعات تفکیک و پرولوگ در دانشگاه سوربن بیشتر در آزمون‌های کنترل مستمر و جلسات عملی کامپیوتر ارزیابی می‌شوند. در ادامه مسائل استاندارد امتحانی آورده شده است.</p>\n</div>\n\n<h2 id=\"w10-ann-ex1\">مسأله نمونه ۱ — یکسان‌سازی رابینسون همراه با Occurs Check</h2>\n<div class=\"box box-enonce\">\n  <div class=\"box-title\">صورت مسأله</div>\n  <p>محاسبه MGU به روش رابینسون برای سیستم معادلات زیر:</p>\n  {{ \\{ f(x, g(y)) \\doteq f(h(z), x), \\quad y \\doteq a \\} }}\n</div>\n<div class=\"box box-solution\">\n  <div class=\"box-title\">پاسخ تشریحی</div>\n  <p>پس از تجزیه تابع {{ f }} به معادلات {{ x \\doteq h(z) }} و {{ g(y) \\doteq x }}، با جایگذاری {{ x }} به معادله {{ g(y) \\doteq h(z) }} می‌رسیم. به دلیل تناقض در نماد تابع سربرگ ({{ g }} در برابر {{ h }})، الگوریتم فوراً با شکست مواجه می‌شود و هیچ یکسان‌سازی وجود ندارد.</p>\n</div>\n\n<span style=\"display:none\">{{ }}</span>"
});
