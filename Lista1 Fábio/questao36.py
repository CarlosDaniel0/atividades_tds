#Idade em anos, meses e dias transforma em dias
print('')
anos = int(input('Digite o valor correspondente aos anos de idade: '))
meses = int(input('Digite o valor correspondente aos meses de idade: '))
dias = int(input('Digite o valor correspondente aos dias de idade: '))

idade = (anos * 365) + (meses * 30) + dias

print('')
print('O valor digitados corresponde a:', idade, 'dias')