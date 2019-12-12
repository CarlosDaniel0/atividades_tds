valor = float(input('Digite o valor do veiculo: '))
ano = int(input('Digite o ano de fabricação: '))

anos_veiculo = 2020 - ano
ipva = valor * 0.025
desconto = 0

if anos_veiculo >= 5 and anos_veiculo <= 10:
    desconto = ipva * 0.15
elif anos_veiculo >= 11 and anos_veiculo <=15:
    desconto = ipva * 0.20
elif anos_veiculo > 15:
    ipva = 0
else:
    ipva = ipva

valor = ipva - desconto
print(f'IPVA: {ipva}')
print(f'Valor de Descontos: {desconto}')
print(f'Valor a ser pago: {valor}')