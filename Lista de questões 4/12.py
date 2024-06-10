import random
lista = [random.randint(1,15)for i in range(10)]
a =[]
for i in range(len(lista)):
    if not lista[i] in a:
        a.append(lista[i])
print(sorted(lista))
print(sorted(a))
