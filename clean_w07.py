# -*- coding: utf-8 -*-
with open('Logic_Academy/data/lessons/w07_td.fr.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any occurrence of \\' with \'
# In Python string representation:
# A literal backslash-quote in the file is written as \'
# If the file contains two backslashes followed by quote, it is \\'
# We want ONE backslash followed by quote: \'
while "\\\\'" in text:
    text = text.replace("\\\\'", "\\'")

with open('Logic_Academy/data/lessons/w07_td.fr.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('Logic_Academy/data/lessons/w07_td.fa.js', 'r', encoding='utf-8') as f:
    text_fa = f.read()

while "\\\\'" in text_fa:
    text_fa = text_fa.replace("\\\\'", "\\'")

with open('Logic_Academy/data/lessons/w07_td.fa.js', 'w', encoding='utf-8') as f:
    f.write(text_fa)

print("w07_td files cleaned!")

