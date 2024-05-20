l1 = []
l2 = []
r1 = r2 = r3 = 0
while True:
    l1.append(int(input('Digite o valor tirado na prova:')))
    l2.append(int(input('Digite o peso dessa nota:')))
    r4 = int(input('Qual é a média dessa matéria?'))
    n = str(input('Deseja adicionar mais alguma nota? [S/N]'))
    if n =='n' or n == 'N':
        break
for i in range(len(l1)):
    r1 += l1[i]*l2[i]
    r2 += l2[i]
r3 = r1/10
if r2 <= 10:
    if r4<r3:
        print(f'O resultado  da média ponderada é {r3}, você passou.')
    else:
        print(f'O resultado da média ponderada é {r3}, você não passou.')