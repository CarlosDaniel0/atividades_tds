#Calcular valor em dolar
dolar = float(input('Digite o valor da cotação do dolar: '))

produto = float(input('Digite o valor o valor do produto em dolar: '))

valor_real = round(dolar * produto, 2)

print('O valor do produto em reais é: ', valor_real)
