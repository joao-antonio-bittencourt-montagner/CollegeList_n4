import random
r = random.randint(5,25)
t1 = tuple(random.randint(0,9)for i in range(r))
t2 = tuple(random.randint(0,9)for i in range(r))
t3 = tuple(set(t1) | set(t2))
print(t1)
print(t2)
print(t3)
