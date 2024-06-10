import random
z = 0
z1 = int(input('Digite o tamanho da matriz [1]:'))
z2 = int(input('Digite o tamanho da matriz [2]:'))


m1 = [[random.randint(1,6)for i in range(z1)] for i in range(z1)]
m2 = [[random.randint(1,6)for i in range(z2)] for i in range(z2)]

m3 = m1

for i in range(z1):
    print(m1[i])
print()
for i in range(z2):
    print(m2[i])
print()

if z1 == z2:
    for i in range(z2):
        for j in range(z2):
            m3[i][j] += m2[i][j]
    for i in range(z1):
        print(m3[i])
    print()
else:
    print('As tabelas não tem o mesmo tamanho.')


