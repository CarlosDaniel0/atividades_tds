valor = float(input('Digite o valor do veículo: '))
taxa = float(input('Digite a taxa anual: '))
valorMensal = float(input('Valor Mensal: '))

taxaMensal = taxa / 12
c_meses = 0


while valorMensal < valor:
    c_meses += 1
    valorMensal = valorMensal + valorMensal * taxaMensal

anos = c_meses // 12
restante = c_meses % 12

if anos != 0:
    if restante == 1:
        print(f'{anos} anos e {restante} mês')
    else:
        print(f'{anos} anos e {restante} meses')
else:
    print(f'{c_meses} meses')