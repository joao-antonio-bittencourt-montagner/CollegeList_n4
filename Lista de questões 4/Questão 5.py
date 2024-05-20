import random
lista = []
for i in range(5):
    lista.append(random.randint(1,9))
print(sorted(lista))
print(sorted(lista, reverse=True))