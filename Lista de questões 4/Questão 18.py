listap = []
n1 = z = 0
v1 = [0, 0, 0, 0, 0]
o = []
v = ['a', 'e', 'i', 'o', 'u']
while True:
    listap.append(str(input('Digite uma palavra:')))
    n = str(input('Deseja continuar digitando palavras?: [S/N]'))
    n1 += 1
    if n == 'n' or n == 'N':
        break
for i in range(n1):
    for ii in range(len(listap[i])):
        for z in range(5):
            if listap[i][ii] == v[z]:
                v1[z] += 1
for i in range(5):
    print(f'A palavra possui {v1[i]} letras {v[i]}')
