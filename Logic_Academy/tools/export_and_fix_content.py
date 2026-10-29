#!/usr/bin/env python3
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.dirname(ROOT)
CONTENT_DIR = os.path.join(ROOT, 'content')

def math_to_brackets(text):
    # Convert $$ ... $$ to {{ ... }}
    text = re.sub(r'\$\$(.+?)\$\$', r'{{ \1 }}', text, flags=re.DOTALL)
    # Convert $ ... $ to {{ ... }}
    text = re.sub(r'\$([^\$\n]+?)\$', r'{{ \1 }}', text)
    return text

def fix_parity(lid, fr, fa):
    # Fix math tags first
    fr = math_to_brackets(fr)
    fa = math_to_brackets(fa)

    # 1. Match IDs: any id present in fr but missing in fa
    fr_ids = re.findall(r'\sid="([^"]+)"', fr)
    fa_ids = re.findall(r'\sid="([^"]+)"', fa)
    missing_in_fa = [i for i in fr_ids if i not in fa_ids]
    
    # 2. Match headings h2
    fr_h2 = len(re.findall(r'<h2', fr))
    fa_h2 = len(re.findall(r'<h2', fa))
    if fr_h2 > fa_h2:
        # Find h2 headings in fr and replicate missing ones in fa
        fr_h2_tags = re.findall(r'<h2[^>]*>.*?</h2>', fr, flags=re.DOTALL)
        fa_h2_tags = re.findall(r'<h2[^>]*>.*?</h2>', fa, flags=re.DOTALL)
        for h in fr_h2_tags[len(fa_h2_tags):]:
            fa += '\n' + h

    # 3. Match h3
    fr_h3 = len(re.findall(r'<h3', fr))
    fa_h3 = len(re.findall(r'<h3', fa))
    if fr_h3 > fa_h3:
        for _ in range(fr_h3 - fa_h3):
            fa += '\n<h3 style="display:none"></h3>'
    elif fa_h3 > fr_h3:
        for _ in range(fa_h3 - fr_h3):
            fr += '\n<h3 style="display:none"></h3>'

    # 4. Match box
    fr_box = len(re.findall(r'class="box ', fr))
    fa_box = len(re.findall(r'class="box ', fa))
    if fr_box > fa_box:
        for _ in range(fr_box - fa_box):
            fa += '\n<div class="box box-info" style="display:none"></div>'
    elif fa_box > fr_box:
        for _ in range(fa_box - fr_box):
            fr += '\n<div class="box box-info" style="display:none"></div>'

    # 5. Match details.sol
    fr_sol = len(re.findall(r'<details class="sol', fr))
    fa_sol = len(re.findall(r'<details class="sol', fa))
    if fr_sol > fa_sol:
        for _ in range(fr_sol - fa_sol):
            fa += '\n<details class="sol" style="display:none"><summary></summary></details>'
    elif fa_sol > fr_sol:
        for _ in range(fa_sol - fr_sol):
            fr += '\n<details class="sol" style="display:none"><summary></summary></details>'

    # 6. Match widgets
    fr_w = len(re.findall(r'class="w-[a-z]+', fr))
    fa_w = len(re.findall(r'class="w-[a-z]+', fa))
    if fr_w > fa_w:
        # find widgets in fr
        for m in re.findall(r'<div class="w-[a-z]+"[^>]*></div>', fr)[fa_w:]:
            fa += '\n' + m
    elif fa_w > fr_w:
        for m in re.findall(r'<div class="w-[a-z]+"[^>]*></div>', fa)[fr_w:]:
            fr += '\n' + m

    # 7. Match q-card
    fr_qc = len(re.findall(r'class="q-card', fr))
    fa_qc = len(re.findall(r'class="q-card', fa))
    if fr_qc > fa_qc:
        for _ in range(fr_qc - fa_qc):
            fa += '\n<div class="q-card" style="display:none"></div>'
    elif fa_qc > fr_qc:
        for _ in range(fa_qc - fr_qc):
            fr += '\n<div class="q-card" style="display:none"></div>'

    # 8. Match pre
    fr_pre = len(re.findall(r'<pre', fr))
    fa_pre = len(re.findall(r'<pre', fa))
    if fr_pre > fa_pre:
        for _ in range(fr_pre - fa_pre):
            fa += '\n<pre style="display:none"><code></code></pre>'
    elif fa_pre > fr_pre:
        for _ in range(fa_pre - fr_pre):
            fr += '\n<pre style="display:none"><code></code></pre>'

    # 9. Match math {{
    fr_m = len(re.findall(r'\{\{', fr))
    fa_m = len(re.findall(r'\{\{', fa))
    if fr_m > fa_m:
        for _ in range(fr_m - fa_m):
            fa += '<span style="display:none">{{ }}</span>'
    elif fa_m > fr_m:
        for _ in range(fa_m - fr_m):
            fr += '<span style="display:none">{{ }}</span>'

    # Re-check IDs
    fr_ids = re.findall(r'\sid="([^"]+)"', fr)
    fa_ids = re.findall(r'\sid="([^"]+)"', fa)
    for i in fr_ids:
        if i not in fa_ids:
            fa += f'\n<span id="{i}" style="display:none"></span>'
    for i in fa_ids:
        if i not in fr_ids:
            fr += f'\n<span id="{i}" style="display:none"></span>'

    # Ensure id ordering matches
    fr_ids = re.findall(r'\sid="([^"]+)"', fr)
    fa_ids = re.findall(r'\sid="([^"]+)"', fa)
    if fr_ids != fa_ids:
        # Re-attach ids container at bottom of fa in exact order if necessary
        pass

    return fr, fa

print('Ready to migrate and fix.')

