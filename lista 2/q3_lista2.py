from random import randint

l = list(range(5))
for i in range(5):
    l[i] = randint(1, 60)

l2 = l[:]
i = 4

#a)
print(l)

#b)
l2.reverse()
print(l2)