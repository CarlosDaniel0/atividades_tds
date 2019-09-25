nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

def programa(idade):
    if idade >= 18:
        print('Você é de maior')
    else:
        print('Você ainda é menor de idade')

programa(idade)