# 14) Elementos Únicos: Crie um algoritmo que retorne uma lista com os elementos que aparecem em apenas
# uma das duas listas passadas como argumento
import random
n = [random.randint(1,15)for i in range(15)]
n1 = [random.randint(1,15)for i in range(15)]
n2 = []
for i in range (15):
    if not n[i] in n1:
        n2.append(n[i])
print(n)
print()
print(n1)
print()
print(n2)