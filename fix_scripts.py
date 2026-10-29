import re

# 1. Fix generate_week04.py
with open('generate_week04.py', 'r', encoding='utf-8') as f:
    c4 = f.read()

# Replace any occurrence of C_3\' or C_4\' etc.
c4_fixed = c4.replace("C_3\\'", "C_3^{(1)}")
c4_fixed = c4_fixed.replace("C_4\\'", "C_4^{(1)}")
c4_fixed = c4_fixed.replace("C_5\\'", "C_5^{(1)}")
c4_fixed = c4_fixed.replace("C_1\\'", "C_1^{(1)}")

with open('generate_week04.py', 'w', encoding='utf-8') as f:
    f.write(c4_fixed)
print("Updated generate_week04.py")

# 2. Fix generate_week07_08.py
with open('generate_week07_08.py', 'r', encoding='utf-8') as f:
    c7 = f.read()

p1 = c7.find('td7_interactive = """')
p2 = c7.find('"""', p1 + 25)
td7_code = c7[p1:p2]

# In td7_code, replace \' with \\\'
td7_fixed = td7_code.replace(r"\'", r"\\\'")
c7_fixed = c7[:p1] + td7_fixed + c7[p2:]

with open('generate_week07_08.py', 'w', encoding='utf-8') as f:
    f.write(c7_fixed)
print("Updated generate_week07_08.py")

