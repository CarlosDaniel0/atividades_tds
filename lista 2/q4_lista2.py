'''
Questão 4
'''
from random import randint

l = list(range(15))

for i in range(15):
    l[i] = randint(0,60)

maior = l[0]
menor = l[0]
p_1 = 0
p_2 = 0
for i in range(len(l)):
    #a)
    if l[i] > maior:
        maior = l[i]
        p_1 = i
    #b)
    elif l[i] < menor:
        menor = l[i]
        p_2 = i
        
print("Lista l: ", l)
print("O maior número da lista é: {} e está na posição: {}".format(maior, p_1))
print("O menor número da lista é: {} e está na posição: {}".format(menor, p_2))