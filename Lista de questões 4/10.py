# 10) Lista Invertida: Crie um algoritmo que inverta uma lista de elementos.
import random
lista = [random.randint(1,15) for i in range(10)]
print(lista)
print(lista[::-1])
print()
print(sorted(lista))
print(sorted(lista,reverse=True))
