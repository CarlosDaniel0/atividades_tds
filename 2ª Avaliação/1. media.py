nota1 = float(input('Nota: '))
nota2 = float(input('Nota: '))
nota3 = float(input('Nota: '))
nota4 = float(input('Nota: '))

mediaAplicada = int(input('Média mínima: '))

media = (nota1 + nota2 + nota3 nota4) / 4

if media >= mediaAplicada:
    print('Aprovado')
else:
    print('Reprovado')