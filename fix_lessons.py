import re

# 1. Fix w04_td.fr.js and w04_td.fa.js
for path in ['Logic_Academy/data/lessons/w04_td.fr.js', 'Logic_Academy/data/lessons/w04_td.fa.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace \Sigma' with \Sigma^\prime
    content = content.replace(r"\Sigma'", r"\Sigma^\prime")
    content = content.replace(r"C_3'", r"C_3^\prime")
    content = content.replace(r"C_4'", r"C_4^\prime")
    content = content.replace(r"C_5'", r"C_5^\prime")
    content = content.replace(r"C_1'", r"C_1^\prime")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {path}')

# 2. Fix w07_td.fr.js and w07_td.fa.js
for path in ['Logic_Academy/data/lessons/w07_td.fr.js', 'Logic_Academy/data/lessons/w07_td.fa.js']:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Let's fix line by line inside initInteractive
    new_lines = []
    in_interactive = False
    for line in lines:
        if 'initInteractive' in line:
            in_interactive = True
        if in_interactive:
            # Look for words like d'une, l'occurrence, d'arité, n'est, d'examen, s'arrête that are not escaped
            # Replace single quotes inside french contractions if preceded by letter and followed by letter
            line = re.sub(r"([a-zA-Z])'([a-zA-Z])", r"\1\\'\2", line)
        new_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f'Fixed {path}')

