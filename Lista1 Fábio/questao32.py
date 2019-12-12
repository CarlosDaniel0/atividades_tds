#Diferença entre o número e seu inverso
print('')
numero = int(input('Digite um valor de 3 digitos: '))

c = (numero // 100 % 10)
d = (numero // 10 % 10) * 10
u = (numero // 1 % 10) * 100

inverso = u + d + c
soma = numero - inverso

print('')
print('O valor digitado corresponde a diferença com o inverso de:', soma)
