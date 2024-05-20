n = int(input('Digite a quantidade de colunas:'))
n1 = int(input('Digite a quantidade de lados:'))
n2 = n1 - 4
if n1 <= 2:
    for i in range(n1):
        print('*'*n1)

else:
    for i in range(n):
        if i == 0 or i == (n1-1):
            print('*'*n1)

        elif i > 0 and i != (n-1):
            print('*',' '*n2,'*')
