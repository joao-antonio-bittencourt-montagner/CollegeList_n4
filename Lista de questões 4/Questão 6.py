# 6) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n
# vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.
import random
r = random.randint(5,20)
n1 = [random.randint(1,6)for i in range(r)]
d1 = d2 = d3 = d4 = d5 = d6 = 0
print(n1)
for i in range(r):
    if n1[i] == 1:
        d1 += 1
    elif n1[i] == 2:
        d2 += 1
    elif n1[i] == 3:
        d3 += 1
    elif n1[i] == 4:
        d4 += 1
    elif n1[i] == 5:
        d5 += 1
    elif n1[i] == 6:
        d6 += 1

print(f'O valor {1} aparece: {d1} vezes.')
print(f'O valor {2} aparece: {d2} vezes.')
print(f'O valor {3} aparece: {d3} vezes.')
print(f'O valor {4} aparece: {d4} vezes.')
print(f'O valor {5} aparece: {d5} vezes.')
print(f'O valor {6} aparece: {d6} vezes.')

