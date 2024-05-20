import random
lista = [[random.randint(1,9)for i in range(5)]for i in range(5)]
for i in range(5):
    print(lista[i])
n = int(input('Digite um número para substituir todos os valores.'))
for i in range(5):
    for ii in range(5):
        lista[i][ii] = n

for i in range(5):
    print(lista[i])