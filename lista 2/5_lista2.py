'''
Questão 5
'''
from random import randint

l1 = list(range(10))
l2 = list(range(10))
l3 = []

for i in range(len(l1)):
    l1[i] = randint(0,10)
    l3.append(l1[i])
    l2[i] = randint(10, 20)
    l3.append(l2[i])

    
print(l1)
print(l2)
print(l3)