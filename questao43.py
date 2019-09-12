#ler a, b, c, d, e, f
print('')

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
d = int(input('Digite o valor de d: '))
e = int(input('Digite o valor de d: '))
f = int(input('Digite o valor de f: '))

x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

print('')
print('O valor de x é:', x)
print('O valor de y é:', y)