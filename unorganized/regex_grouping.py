import re

text = "Nominated for 1 Oscar. Another 6 wins & 10 nominations."
# text = "3 wins & 11 nominations."


r1 = re.compile(r"Nominated for (?P<n1>\d*)")

r2 = re.compile(r"(?P<n2>\d*) nominations.")

m1 = r1.findall(text)
m2 = r2.findall(text)

m1 = m1 + m2

if m1:
    print(m1)
else:
    print("no match")
