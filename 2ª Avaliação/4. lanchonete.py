n = int(input('Digite: '))
valor = 0

while n != 0:
    if n == 1:
        valor += 4
    elif n == 2:
        valor += 4.50
    elif n == 3:
        valor += 5
    elif n == 4:
        valor += 2
    elif n == 5:
        valor += 1.50
    n = int(input('Digite: '))

taxa = valor * 0.10
valorPago = valor - taxa

print(f'Valor Total: {valor}')
print(f'Taxa de serviço: {taxa}')
print(f'Valor a ser pago: {valorPago}')

cliente = float(input('Valor: '))
troco = cliente - valorPago
if troco != 0:
    print('Troco: ',troco)
else:
    print('Sem troco')