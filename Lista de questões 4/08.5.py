import random

r = random.randint(1,15)
n = [random.randint(0,9) for i in range(r)]

print(max(int(n) for n in n))
print(min(int(n) for n in n))
