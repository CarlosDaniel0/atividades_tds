def numero():
    n = int(input('Digite um número inteiro: '))

    centenas = n // 100

    if centenas % 2 == 0:
        print('Par')
    else:
        print('impar')

numero()