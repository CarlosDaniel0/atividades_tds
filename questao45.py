#Caixa eletronico
print('')
valor = float(input('Digite o valor a ser sacado: '))

#Reconhecimento de cédulas
cem = valor // 100 % 10
cinquenta = valor % 100 // 50
vinte = valor % 100 % 50 // 20
dez = valor % 100 % 50 % 20 // 10
cinco = valor % 100 % 50 % 20 % 10 // 5
dois = valor % 100 % 50 % 20 % 10 % 5 // 2
um = valor % 100 % 50 % 20 % 10 % 5 % 2

print('')
print('Seu saque será em:')
print(cem, 'Notas de R$ 100,00')
print(cinquenta, 'Notas de R$ 50,00')
print(vinte, 'Notas de R$ 20,00')
print(dez, 'Notas de R$ 10,00')
print(cinco, 'Notas de R$ 5,00')
print(dois, 'Notas de R$ 2,00')
print(um, 'Notas de R$ 1,00')