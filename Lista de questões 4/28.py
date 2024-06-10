import random
l = []
l1 = []
maior = menor = 0
c = 0
r = 10
while len(l) != r:
    c = (random.randint(0, 20))
    if c not in l:
        l.append(c)
print(sorted(l))
for ii in range(5):
    for i in range(len(l)):
        if i == 0:
            maior = menor = l[i]
        elif maior < l[i]:
            maior = l[i]
        elif menor > l[i]:
            menor = l[i]
    l1.append(maior)
    l1.append(menor)
    l.remove(maior)
    l.remove(menor)
print(l1)
