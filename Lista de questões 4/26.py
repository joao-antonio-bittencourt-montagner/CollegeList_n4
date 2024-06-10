import random
lista = [[random.randint(0,1)for i in range(5)]for i in range(5)]
c = 0
for i in range(5):
    print(lista[i])
for i in range(5):
    for ii in range(5):
        if lista[i][ii] == 0:
            c += 1
if c >= 13:
    print('A matriz é esparsa!')
else:
    print('A matriz não é esparsa!')


