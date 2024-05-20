import random
lista = [[random.randint(0,1)for i in range(5)]for i in range(5)]
r = 0
r1 =0
d = 4
for i in range(5):
    print(lista[i])
print()
for i in range(5):
    r += lista[i][i]
print(f'O valor da soma da diagonal principal é {r}')
print()

for i in range(5):
    r1 += lista[i][d]
    d -= 1
print(f'O valor da soma da diagonal secundária é {r1}')