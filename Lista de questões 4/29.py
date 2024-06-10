import random
lista = [[random.randint(0,9)for j in range(5)]for j in range(5)]
r1 = []
r = 0

for j in range(5):
    print(lista[j])

for i in range(5):
    for ii in range(5):
        r += lista[ii][i]
    r1.append(r/5)
    r = 0
print()
print(f'A média da soma dos valores das colunas é {r1}, respectivamente.')
