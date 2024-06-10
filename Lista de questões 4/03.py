import random
n1 = int(input('Digite a quantidade de colunas dessa matriz:'))
n = int(input('Digite o número de lados dessa matriz:'))
z = r = 0
lista = []
lista1 = []
for ii in range(n1):
    lista.append(random.randint(1, 9))
    r = r + lista[ii]

for i in range(n):
    lista1.append(lista[:])
    lista.clear()

    print(lista1[i])
    for iii in range(n1):
        lista.append(random.randint(1, 9))
        r = r + lista[iii]

z = r/len(lista1)
print(f'A média dos números na matriz é {z}')






