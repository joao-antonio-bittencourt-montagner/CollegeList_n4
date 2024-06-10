# 15) Escreva um algoritmo que receba duas matrizes como entrada e retorne a soma dessas matrizes, desde
# que tenham as mesmas dimensões.
import random
print('Dê o tamanho de duas matrizes! Se ambas tiverem a mesma dimensão daremos a soma delas.')
n = int(input('Dê o valor da coluna da matriz [1]:'))
n1 = int(input('Dê o valor do lado da matriz [2]:'))
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
m6 = []
s = 0
m = n * n1
for i in range(n):
    m1.append(random.randint(1, 9))
for ii in range(n1):
    m2.append(m1[:])
    m1.clear()
    print(m2[ii])
    for iii in range(n):
        m1.append(random.randint(1, 9))
print(m2)

n2 = int(input('Dê o valor da coluna da matriz [3]:'))
n3 = int(input('Dê o valor do lado da matriz [4]:'))
mm = n2 * n3
for i in range(n3):
    m3.append(random.randint(1, 9))
for ii in range(n3):
    m4.append(m3[:])
    m3.clear()
    print(m4[ii])
    for iii in range(n3):
        m3.append(random.randint(1, 9))
print(m4)

if m == mm:
    for i in range(n1):
        for ii in range(n):
            a = aa = 0
            a = m2[i][ii]
            aa = m4[i][ii]
            r = a + aa
            m5.append(r)

        for iii in range(n1):
            m6.append(m5[:])
            m5.clear()
        print(m6)


