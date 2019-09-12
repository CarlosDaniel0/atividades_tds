#loja cálculo de prestações
print('')
valor = float(input('Valor do produto que deseja parcelar: '))

prestacoes = valor // 3
entrada = prestacoes + (valor % 3)


print('')
print('Sua entrada é de:', entrada)
print('Suas duas prestações são de:', prestacoes)