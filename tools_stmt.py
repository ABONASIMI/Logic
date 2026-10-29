#!/usr/bin/env python3
import sys, re
names = sys.argv[1:]
for n in names:
    t = open('/tmp/annales_txt/%s.txt' % n, encoding='utf-8').read()
    m = re.search(r'Corrig[ée]', t)
    stmt = t[:m.start()] if m else t
    # strip excessive blank lines
    stmt = re.sub(r'\n\s*\n+', '\n', stmt)
    print('=' * 20, n, '(statement chars: %d)' % len(stmt))
    print(stmt)

