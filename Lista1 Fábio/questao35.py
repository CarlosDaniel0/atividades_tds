#soma dos numeros de valor de 4 digitos
print('')
numero = int(input('Digite um número de 4 digitos: '))

m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10

soma = m + c + d + u

print('')
print('O valor digitado corresponde:', soma)