# idade em dias para anos, meses e dias
print('')
idade = int(input('Digite o valor da sua idade em dias: '))

anos = idade // 365
meses = idade % 365 // 30
dias = idade % 365 % 30

print('')
print('O valor digitado corresponde a:', anos, 'anos', meses, 'meses', dias, 'dias')