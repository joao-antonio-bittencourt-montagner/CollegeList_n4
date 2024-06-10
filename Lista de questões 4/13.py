# 13) Ordenação: Escreva um programa que ordene uma lista de números em ordem crescente ou
# decrescente, dependendo do argumento passado para a função.
import random
n = int(input('Você deseja a lista em ordem crescente[1] ou decrescente[2]'))
lista = [random.randint(1,20) for i in range(15)]
if n == 1:
    print(sorted(lista))
elif n == 2:
    print(sorted(lista,reverse=True))
