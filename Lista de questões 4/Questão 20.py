import random
tupla = ()
tupla1 = ()
n1 = tuple(random.randint(0, 9) for i in range(10))
n2 = tuple(random.randint(0, 9) for i in range(10))
print(n1)
print(n2)

n3 = (set(n1) | set(n2))
n3 = tuple(n3_)
print(n3)