qnt_corridas = int(input('Digite a quantidaded de corridas: '))
valor_total = 0

for i in range(qnt_corridas):
    valor_corrida = float(input('Digite um valor: '))
    valor_total = valor_total + valor_corrida

desconto = valor_total * 0.25
valor_motorista = valor_total * 0.75
restante = valor_motorista - desconto

print('')

print(f'Valor Total: {valor_total}')
print(f'Descontos: - {desconto}')
print(f'Total: {restante}')