n = int(input('Digite a quantidade de colunas:'))
n1 = int(input('Digite a quantidade de lados:'))
r = n1 - 2
r1 = n1 -1
lista = ['*']*n1
lista1 = []
lista1.append(lista[:])
p = 1
for i in range(n+1):
    if i == 0:
        print(f'{lista}'
              f'')

    elif i == n1:
        print(lista1)

    elif i > 0 and i != (n-1):
        p = 1
        for ii in range(r):
            lista[p] = ('')
            p += 1
        print(lista)

