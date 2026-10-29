#!/usr/bin/env python3
"""Build lesson bundles from authored HTML fragments.

content/<wXX>/<section>.<lang>.html   (section = cours | td | tp | annales | revision; lang = fr | fa)
  -> data/lessons/<wXX>_<section>.<lang>.js   (Logic.reg bundle, JSON-escaped: no quoting problems)
content/status.json  : {"w01_cours": "complete", ...}  ->  data/status.js   (honest status shown as a banner in the UI)

Also runs structural FR/FA parity checks (same ids, same number of boxes, widgets, math spans, solutions).
Usage: python3 tools/build_lessons.py
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
OUT = os.path.join(ROOT, 'data', 'lessons')
os.makedirs(OUT, exist_ok=True)


def bundle(lid, lang, html, status):
    return ('Logic.reg(%s, {\n  id: %s,\n  lang: %s,\n  status: %s,\n  html: %s\n});\n' % (
        json.dumps('lesson:%s:%s' % (lid, lang)), json.dumps(lid), json.dumps(lang), json.dumps(status),
        json.dumps(html, ensure_ascii=False)))


def parity(fr, fa):
    """Return list of human-readable parity problems between FR and FA fragments."""
    problems = []
    def ids(s): return re.findall(r'\sid="([^"]+)"', s)
    def count(pat, s): return len(re.findall(pat, s))
    if ids(fr) != ids(fa):
        problems.append('ids differ: FR-only=%s FA-only=%s' % (sorted(set(ids(fr)) - set(ids(fa)))[:6], sorted(set(ids(fa)) - set(ids(fr)))[:6]))
    for name, pat in [('box', r'class="box '), ('details.sol', r'<details class="sol'), ('widgets', r'class="w-[a-z]+'),
                      ('math', r'\{\{'), ('h2', r'<h2'), ('h3', r'<h3'), ('q-card', r'class="q-card'), ('pre', r'<pre')]:
        a, b = count(pat, fr), count(pat, fa)
        if a != b:
            problems.append('%s count FR=%d FA=%d' % (name, a, b))
    return problems


def main():
    status_path = os.path.join(CONTENT, 'status.json')
    status = json.load(open(status_path, encoding='utf-8')) if os.path.exists(status_path) else {}
    built, bad = 0, 0
    for wdir in sorted(glob.glob(os.path.join(CONTENT, 'w[0-9][0-9]'))):
        wid = os.path.basename(wdir)
        secs = sorted({os.path.basename(p).split('.')[0] for p in glob.glob(os.path.join(wdir, '*.html'))})
        for sec in secs:
            lid = '%s_%s' % (wid, sec)
            frp, fap = [os.path.join(wdir, '%s.%s.html' % (sec, l)) for l in ('fr', 'fa')]
            if not (os.path.exists(frp) and os.path.exists(fap)):
                print('!! %s: missing language file' % lid); bad += 1; continue
            fr, fa = open(frp, encoding='utf-8').read(), open(fap, encoding='utf-8').read()
            for p in parity(fr, fa):
                print('!! parity %s: %s' % (lid, p)); bad += 1
            st = status.get(lid, 'partial')
            for lang, html in (('fr', fr), ('fa', fa)):
                open(os.path.join(OUT, '%s.%s.js' % (lid, lang)), 'w', encoding='utf-8').write(bundle(lid, lang, html, st))
            built += 1
    open(os.path.join(ROOT, 'data', 'status.js'), 'w', encoding='utf-8').write('Logic.reg("status", %s);\n' % json.dumps(status, indent=1))
    print('built %d lesson pairs, %d problems' % (built, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())

