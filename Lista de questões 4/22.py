import random
n = tuple(random.randint(1, 9)for i in range(5))
n1 = tuple()
print(n)
c = 0
for i in range(5):
    for ii in range(5):
        if n[i] == n[ii]:
            c+=1
    if c == 1:
        n1 += (n[i],)
    c = 0
print(n1)
