#Meses em anos e meses
print('')

meses = int(input('Digite um valor em meses: '))

anos = meses // 12
meses_restantes = meses % 12

print('')
print('O valor digitado corresponde a:', anos, 'anos e', meses_restantes, 'meses')