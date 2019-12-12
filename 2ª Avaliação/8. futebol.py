partidas = int(input('Digite a quantidade de partidas: '))
pontuacao = 0

for i in range(partidas):
    resultado = input('Digite v - Vitória ou e - Empate: ')
    if resultado == 'v':
        pontuacao = pontuacao + 3
    elif resultado == 'e':
        pontuacao = pontuacao + 1
    else:
        print('valor inválido')
    
print('')

print(f'Seu time acumulou: {pontuacao} pontos')