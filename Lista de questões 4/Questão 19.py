import random
n1 = []
r = r1 = 0
n1 = [random.randint(1,20) for i in range(10)]
np = []
ni = []
for i in range(10):
    r = n1[i]
    r1 = r % 2
    if r1 == 0:
       np.append(n1[i])
    else:
        ni.append(n1[i])
sorted(np)
sorted(ni)
print(n1)
print(np + ni)
