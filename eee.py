import re

key = r"mat yat uat aat"
p1 = r"[^y]at"
print(re.findall(p1, key))
