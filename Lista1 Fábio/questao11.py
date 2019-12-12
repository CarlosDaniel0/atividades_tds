#Mostra digitos ao contrário
numero = int(input("Digite um número de 3 digitos: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10

print('Seu núemro ao contrário é:', u , d, c)