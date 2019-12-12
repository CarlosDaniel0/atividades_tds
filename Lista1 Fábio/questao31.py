# binarios para decimal

print('')
numero = int(input('Digite um valor de 4 digitos em binário: '))

#identifica cada digito
m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10

#transforma em binario
b1 = (2 ** 3) * m
b2 = (2 ** 2) * c
b3 = (2 ** 1) * d
b4 = (2 ** 0) * u

soma_binario = b1 + b2 + b3 + b4

print('')
print('O numero binario digitado corresponde a:', soma_binario)