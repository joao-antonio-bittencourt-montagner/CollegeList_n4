import random
t = int(input('Digite o tamanho da matriz:'))
m = [[random.randint(0,9) for i in range(t)]for i in range(t)]

for i in range (t):
    print(m[i])