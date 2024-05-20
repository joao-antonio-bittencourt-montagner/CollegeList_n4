# 7) Crie um algoritmo que receba uma lista de números e retorne a soma de todos os elementos.
import random
lista = []
r = 0
for i in range(5):
    lista.append(int(input('Digite um valor para ser colocado na lista:')))
    r += lista[i]
print(f'A soma de todos os elementos é {r}')