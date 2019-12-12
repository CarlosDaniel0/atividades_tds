n = int(input('Quantidade de registros: '))
qnt_s = 0
qnt_r = 0
qnt_c = 0
total = 0

for i in range(n):
    amostra = input('Digite a amostra: ')
    amostra = amostra.split()

    if amostra[1] == 'R':
        qnt_r += int(amostra[0])
        total += int(amostra[0])
    elif amostra[1] == 'S':
        qnt_s += int(amostra[0])
        total += int(amostra[0])
    elif amostra[1] == 'C':
        qnt_c += int(amostra[0])
        total += int(amostra[0])

print('')
print(f'Total: {total} cobaias')
print(f'Total de Coelhos: {qnt_c}')
print(f'Total de Ratos: {qnt_r}')
print(f'Total de Sapos: {qnt_s}')
perc_s = (qnt_s / total) * 100
perc_r = (qnt_r / total) * 100
perc_c = (qnt_c / total) * 100

print(f'Percentual de coelhos: {perc_c} %')
print(f'Percentual de Ratos: {perc_r} %')
print(f'Percentual de Sapos: {perc_s} %')