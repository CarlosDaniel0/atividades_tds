from random import randint

l = list(range(5))
for i in range(5):
    l[i] = randint(1, 60)

l2 = l[:]

#a)
print("Lista normal:", l)

#b)
l2.reverse()
print("Lista invertida:", l2)