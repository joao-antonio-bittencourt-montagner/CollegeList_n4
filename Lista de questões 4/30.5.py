import random
lista1 = [random.randint(1,15)for i in range(10)]
lista2 = [random.randint(1,15)for i in range(10)]
lista3 = lista1 + lista2
lista4 = []
lista5 = []
c = 0
print(sorted(lista1))
print(sorted(lista2))

for i in range(20):
    if not lista3[i] in lista1:
        lista4.append(lista3[i])

    if not lista3[i] in lista2:
        lista4.append(lista3[i])

print()
print(sorted(lista4))
