import random
n1 = tuple(random.randint(1,20)for i in range(20))
n2 = 0
np = tuple()
ni = tuple()
print(n1)
for i in range(20):
    n2 = n1[i] % 2
    if n2 == 0:
        np += (n1[i],)
    else:
        ni += (n1[i],)
print(np)
print(ni)
