def programa():
    print('')
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    print('')

    if idade >= 18:
        print('Parabéns', nome,'Você é de maior')
    else:
        print(nome, 'Você ainda é menor de idade')

programa()
