#!/usr/bin/env python3
"""Extract every annale PDF to text (one file per PDF) into /tmp/annales_txt and print a page/size summary."""
import os, subprocess, glob, unicodedata
SRC = '/home/mnasimi/sorbonne/Logic/logic/LU2IN007 Logique/annales'
OUT = '/tmp/annales_txt'
os.makedirs(OUT, exist_ok=True)
for p in sorted(glob.glob(SRC + '/*.pdf')):
    name = os.path.basename(p)[:-4]
    txt = subprocess.run(['pdftotext', '-layout', p, '-'], capture_output=True).stdout.decode('utf-8', 'replace')
    txt = unicodedata.normalize('NFC', txt)
    open(os.path.join(OUT, name + '.txt'), 'w', encoding='utf-8').write(txt)
    info = subprocess.run(['pdfinfo', p], capture_output=True).stdout.decode()
    pages = [l for l in info.splitlines() if l.startswith('Pages')][0].split()[-1]
    print('%-40s pages=%s chars=%d' % (name, pages, len(txt)))

