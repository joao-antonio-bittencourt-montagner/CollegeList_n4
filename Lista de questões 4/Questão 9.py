# 9) Média dos Elementos: Desenvolva um algoritmo que calcule e retorne a média dos elementos de uma
# lista de números.
import random
r = 0
lista = [random.randint(5,10) for i in range(10)]
print(lista)
for i in range(10):
    r += lista[i]
r = r/len(lista)
print(f'A média é {r}')