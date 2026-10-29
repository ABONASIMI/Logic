Logic.reg("lesson:w11_tp:fa", {
  id: "w11_tp",
  lang: "fa",
  status: "complete",
  html: "\n<div class=\"box box-objectives\">\n  <div class=\"box-title\">کار عملی موضوع ۱۱ — برنامه‌های کاربردی لیست‌ها در پرولوگ (تمرین‌های ۱۹، ۲۰ و ۲۱)</div>\n  <p>منبع رسمی: <code>main_tp-etudiants.pdf</code>، صفحات ۱۹ تا ۲۴.</p>\n</div>\n\n<h2 id=\"w11-tp-ex20\">تمرین ۲۰ — دستکاری و معکوس کردن لیست</h2>\n<pre><code>% عنصر دوم\ndeuxieme([_, X | _], X).\n\n% عنصر یکی مانده به آخر\navantDernier([X, _], X).\navantDernier([_ | Q], X) :- avantDernier(Q, X).\n\n% معکوس کردن بهینه با انباشت‌گر (O(n))\ninverse(L, Res) :- inv_acc(L, [], Res).\ninv_acc([], Acc, Acc).\ninv_acc([T | Q], Acc, Res) :- inv_acc(Q, [T | Acc], Res).</code></pre>\n\n<span id=\"w11-tp-ex21\" class=\"anchor-sync\" style=\"display:none\"></span>\n<h2 style=\"display:none\"></h2>\n<pre style=\"display:none\"><code></code></pre>"
});
