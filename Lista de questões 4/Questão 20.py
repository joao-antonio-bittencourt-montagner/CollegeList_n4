import random
d = 10
c = 0
l1 = [random.randint(0,15)for i in range(d)]
l2 = [random.randint(0,15)for i in range(d)]
l3 = l1 + l2
l4 = []
print(l1)
print(l2)
print()
print(l3)
for i in range(len(l3)):
    if not l3[i] in l4:
        l4.append(l3[i])
print()
print(sorted(l4))
