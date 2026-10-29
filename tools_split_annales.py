#!/usr/bin/env python3
"""Split every annale into exercises (statement + official corrigé) -> /home/mnasimi/sorbonne/Logic_Academy/content/annales_src.json
Statement part = text before the first 'Corrigé'; corrigé part = text after. Exercises are split on 'Exercice N'."""
import re, json, glob, os, unicodedata
SRC = '/tmp/annales_txt'
out = {}
for p in sorted(glob.glob(SRC + '/*.txt')):
    name = os.path.basename(p)[:-4]
    t = open(p, encoding='utf-8').read()
    m = re.search(r'Corrig[ée]\s+de\s+l|Corrig[ée]', t)
    stmt, corr = (t[:m.start()], t[m.start():]) if m else (t, '')
    def split_ex(s, pat):
        parts = re.split(r'(?m)^\s*(?:I\s+|▶\s*)?(%s)\s*(\d+)' % pat, s)
        res = {}
        # parts: [pre, label, num, body, label, num, body...]
        for i in range(1, len(parts) - 2, 3):
            num = int(parts[i + 1]); res.setdefault(num, '')
            res[num] += parts[i + 2]
        return res
    se = split_ex(stmt, r'Exercice')
    ce = split_ex(corr, r'Corrig[ée] de l.exercice|Exercice')
    # header (first lines) for exam meta
    head = '\n'.join([l.strip() for l in stmt.splitlines() if l.strip()][:6])
    out[name] = {'header': head, 'exercises': {str(k): {'statement': re.sub(r'\n\s*\n+', '\n', v).strip(), 'corrige': re.sub(r'\n\s*\n+', '\n', ce.get(k, '')).strip()} for k, v in sorted(se.items())}}
json.dump(out, open('/home/mnasimi/sorbonne/Logic_Academy/content/annales_src.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v['exercises']) for v in out.values())
nocorr = sum(1 for v in out.values() for e in v['exercises'].values() if not e['corrige'])
print('exams', len(out), 'exercises', tot, 'without parsed corrigé', nocorr)

