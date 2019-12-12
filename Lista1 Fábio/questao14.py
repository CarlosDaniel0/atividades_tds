#Calcular média ponderada
print('')
nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a nota do aluno: '))
nota3 = float(input('Digite a nota do aluno: '))
print('')

peso1 = int(input('Digite o peso da nota: '))
peso2 = int(input('Digite o peso da nota: '))
peso3 = int(input('Digite o peso da nota: '))
print('')

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3))/(peso1 + peso2 + peso3)

print('A nota do aluno com peso é:', media_ponderada)
