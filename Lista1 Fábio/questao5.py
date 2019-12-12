#Somar numero inteiro de 3 digitos
numero = int(input("Digite um valor com 3 digitos (ex: 100): "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10

print('A soma dos valores é:', u + d + c)