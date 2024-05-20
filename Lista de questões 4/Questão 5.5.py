import random
r = random.randint(1,10)
lista = [random.randint(1, 10) for i in range(r)]
print(f'A sequência em ordem fica:{sorted(lista)} ')
print(f'A sequêncai ao contrário fica:{sorted(lista,reverse=True)}')