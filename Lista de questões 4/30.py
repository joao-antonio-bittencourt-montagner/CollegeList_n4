import random

t = 10
m1 = [random.randint(0,15) for i in range(t)]
m2 = [random.randint(0,15) for i in range(t)]
m3 = m1 + m2
m4 = []

n = t * 2

for i in range (n):
    if not m3[i] in m1 and m3[i] in m2:
        m4.append(m3[i])
    if not m3[i] in m2 and m3[i] in m1:
        m4.append(m3[i])

print(sorted(m1))
print(sorted(m2))
print()
print(sorted(m4))
