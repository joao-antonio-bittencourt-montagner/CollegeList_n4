import random
lista = [[random.randint(1,9)for i in range(5)]for i in range(5)]
lista1 = []
lista2 = []
r = 0
for i in range(5):
    print(lista[i])

for l in range(5):
    for c in range(5):
        r += lista[l][c]
    lista1.append(r)
    r = 0
print()
print(f'A soma dos valores das linhas é: {lista1} respectivamente.')

for l in range(5):
    for c in range(5):
        r += lista[c][l]
    lista2.append(r)
    r = 0
print()
print(f'A soma do valor das colunas é: {lista2} respectivamente.')
