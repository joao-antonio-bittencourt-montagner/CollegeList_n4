# 11) Remover Elemento Específico: Escreva um algoritmo que remova todas as ocorrências de um
# elemento específico de uma lista. Portanto, o usuário deverá digitar qual elemento ele gostaria de retirar
# da lista, e o algoritmo deverá substituir cada ocorrência deste número por um asterisco “*”.
import random
lista = [random.randint(1,15) for i in range(15)]
print(lista)
n = int(input('Diga um número para ser eliminado da lista:'))
for i in range (len(lista)):
    if lista[i] == n:
        lista[i] = '*'
print(lista)