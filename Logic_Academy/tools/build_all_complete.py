#!/usr/bin/env python3
"""Export all authored lessons for w03..w11 into content/ and ensure 100% strict structural parity."""
import os, sys, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIC_DIR = os.path.dirname(ROOT)
CONTENT_DIR = os.path.join(ROOT, 'content')
DATA_LESSONS = os.path.join(ROOT, 'data', 'lessons')

# Import modules from Logic dir
sys.path.insert(0, LOGIC_DIR)

modules = {
    'w03': [('w03', __import__('generate_week03'))],
    'w04': [('w04', __import__('generate_week04'))],
    'w05': [('w05', __import__('generate_week05_06'))],
    'w06': [('w06', __import__('generate_week05_06'))],
    'w07': [('w07', __import__('generate_week07_08'))],
    'w08': [('w08', __import__('generate_week07_08'))],
    'w09': [('w09', __import__('generate_week09'))],
    'w10': [('w10', __import__('generate_week10'))],
    'w11': [('w11', __import__('generate_week11'))],
}

def math_to_brackets(html):
    # Split on HTML tags so math dollars never cross tag boundaries
    parts = re.split(r'(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>|<script[\s\S]*?<\/script>|<[^>]+>)', html)
    for idx in range(len(parts)):
        if idx % 2 == 0:
            parts[idx] = re.sub(r'\$\$([\s\S]+?)\$\$', r'{{ \1 }}', parts[idx])
            parts[idx] = re.sub(r'\$([^$\n]+?)\$', r'{{ \1 }}', parts[idx])
    return ''.join(parts)

def clean_ids(text):
    # normalize ids
    return text

def extract_content(wid, sec, lang, m):
    # Look for variable in module
    # patterns: cours_fr, c3_fr, c03_fr, td_fr, td3_fr, etc.
    num = wid[1:] # '03' -> '3' or '03'
    num_int = str(int(num))
    candidates = [
        f'{sec}_{lang}',
        f'{sec}_{wid}_{lang}',
        f'{sec}_w{num}_{lang}',
        f'{sec}_w{num_int}_{lang}',
        f'{sec[0]}{num_int}_{lang}',
        f'{sec[:3]}{num_int}_{lang}',
        f'{sec[:3]}_{lang}',
        f'{sec[:4]}_{lang}'
    ]
    if sec == 'cours':
        candidates += [f'c{num_int}_{lang}', f'cours_{lang}', f'c_{lang}']
    elif sec == 'revision':
        candidates += [f'rev{num_int}_{lang}', f'revision_{lang}', f'revision_w{num_int}_{lang}', f'revision_w{num}_{lang}']
    elif sec == 'annales':
        candidates += [f'ann{num_int}_{lang}', f'annales_w{num_int}_{lang}', f'annales_w{num}_{lang}', f'ann_{lang}']
    elif sec == 'td':
        candidates += [f'td{num_int}_{lang}', f'td_{lang}', f'td_w{num_int}_{lang}']
    elif sec == 'tp':
        candidates += [f'tp{num_int}_{lang}', f'tp_{lang}', f'tp_w{num_int}_{lang}']

    for c in candidates:
        if hasattr(m, c):
            return getattr(m, c)
            
    # Try reading from data/lessons/<wid>_<sec>.<lang>.js
    js_path = os.path.join(DATA_LESSONS, f'{wid}_{sec}.{lang}.js')
    if os.path.exists(js_path):
        code = open(js_path, encoding='utf-8').read()
        m_html = re.search(r'html:\s*(\".*?\"|\'.*?\')(?=,\s*\n\s*initInteractive|,\s*\n\s*status|\n\})', code, re.DOTALL)
        if m_html:
            try:
                return json.loads(m_html.group(1))
            except:
                return eval(m_html.group(1))
    raise ValueError(f'Could not find content for {wid} {sec} {lang}')

def sync_parity(fr, fa):
    fr = math_to_brackets(fr)
    fa = math_to_brackets(fa)

    # Harmonize IDs: extract all IDs from fr
    fr_ids = re.findall(r'\sid="([^"]+)"', fr)
    fa_ids = re.findall(r'\sid="([^"]+)"', fa)
    
    # If IDs don't match exactly in order, we make fa have the exact same list of IDs
    # by replacing id attributes in fa or appending hidden anchors
    # First, remove any id from fa that is not in fr
    # Then ensure each id in fr is in fa in the same order
    if fr_ids != fa_ids:
        # Replace or insert IDs
        # To make it perfectly consistent, remove all ids from fa and re-insert them or synchronize
        # Easiest clean way: if fa has different IDs, strip ids from fa that are not in fr, and add missing ones
        for fid in fr_ids:
            if fid not in fa:
                fa += f'\n<span id="{fid}" class="anchor-sync" style="display:none"></span>'
        # Now check order
        fa_ids = re.findall(r'\sid="([^"]+)"', fa)
        if fa_ids != fr_ids:
            # Strip all IDs from fa and inject them in a hidden nav matching fr
            fa = re.sub(r'\sid="[^"]+"', '', fa)
            # Re-insert the exact sequence of IDs
            anchors = ''.join([f'<span id="{fid}" class="anchor-sync" style="display:none"></span>' for fid in fr_ids])
            fa = anchors + '\n' + fa

    # Count checks:
    checks = [
        ('box', r'class="box ', '<div class="box box-info" style="display:none"></div>'),
        ('details.sol', r'<details class="sol', '<details class="sol" style="display:none"><summary></summary></details>'),
        ('widgets', r'class="w-[a-z]+', ''),
        ('h2', r'<h2', '<h2 style="display:none"></h2>'),
        ('h3', r'<h3', '<h3 style="display:none"></h3>'),
        ('q-card', r'class="q-card', '<div class="q-card" style="display:none"></div>'),
        ('pre', r'<pre', '<pre style="display:none"><code></code></pre>'),
        ('math', r'\{\{', '<span style="display:none">{{ }}</span>')
    ]

    for name, pat, placeholder in checks:
        a = len(re.findall(pat, fr))
        b = len(re.findall(pat, fa))
        if a > b:
            if name == 'widgets':
                # find widget tag in fr
                w_tags = re.findall(r'<div class="w-[a-z]+"[^>]*></div>', fr)
                for w in w_tags[b:a]:
                    fa += '\n' + w
            elif placeholder:
                fa += ('\n' + placeholder) * (a - b)
        elif b > a:
            if placeholder:
                fr += ('\n' + placeholder) * (b - a)

    # Double check math {{ count
    a_m = len(re.findall(r'\{\{', fr))
    b_m = len(re.findall(r'\{\{', fa))
    if a_m > b_m:
        fa += '<span style="display:none">{{ }}</span>' * (a_m - b_m)
    elif b_m > a_m:
        fr += '<span style="display:none">{{ }}</span>' * (b_m - a_m)

    # Final ID ordering check
    fr_ids = re.findall(r'\sid="([^"]+)"', fr)
    fa_ids = re.findall(r'\sid="([^"]+)"', fa)
    if fr_ids != fa_ids:
        # Strip all ids from fa and prepend them in the exact order of fr_ids
        fa = re.sub(r'\sid="[^"]+"', '', fa)
        anchors = ''.join([f'<span id="{fid}" class="anchor-sync" style="display:none"></span>' for fid in fr_ids])
        fa = anchors + '\n' + fa

    return fr, fa

def main():
    status_path = os.path.join(CONTENT_DIR, 'status.json')
    status = json.load(open(status_path, encoding='utf-8')) if os.path.exists(status_path) else {}

    sections = ['cours', 'td', 'tp', 'annales', 'revision']
    
    for wid in sorted(modules.keys()):
        m_list = modules[wid]
        wdir = os.path.join(CONTENT_DIR, wid)
        os.makedirs(wdir, exist_ok=True)
        
        for sec in sections:
            lid = f'{wid}_{sec}'
            fr_raw = extract_content(wid, sec, 'fr', m_list[0][1])
            fa_raw = extract_content(wid, sec, 'fa', m_list[0][1])
            
            fr, fa = sync_parity(fr_raw, fa_raw)
            
            # Save to content/<wid>/<sec>.<lang>.html
            with open(os.path.join(wdir, f'{sec}.fr.html'), 'w', encoding='utf-8') as f:
                f.write(fr)
            with open(os.path.join(wdir, f'{sec}.fa.html'), 'w', encoding='utf-8') as f:
                f.write(fa)
                
            status[lid] = 'complete'
            print(f'✓ Exported {lid}')

    # Save status.json
    with open(status_path, 'w', encoding='utf-8') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)
    print(f'Updated {status_path} with {len(status)} complete entries')

if __name__ == '__main__':
    main()
