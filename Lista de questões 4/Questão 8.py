# 8) Escreva um algoritmo que encontre e retorne o maior elemento em uma lista de números.
import random
lista = [random.randint(1,15)for i in range(10)]
maior = 0
menor = 0
print(lista)
for i in range(10):
    if i == 0:
        menor = maior = lista[i]

    elif lista [i] > maior:
        maior = lista[i]

    elif lista [i] < menor:
        menor = lista [i]


print(f'O maoir valor é {maior} e o menor é {menor}')