senha = input('Digite a senha: ')

n = '1234567890'
lMaiuscula = 0
lMinuscula = 0
numeros = 0

nContem1 = ''
nContem2 = ''
nContem3 = ''

if len(senha) >= 8:
    for letra in senha:
        if ord(letra) >= 65 and ord(letra) <= 90:
            lMaiuscula += 1
        elif ord(letra) >= 97 and ord(letra) <= 122:
            lMinuscula += 1
        elif letra in n:
            numeros += 1
        
    if lMinuscula != 0 and lMinuscula != 0 and numeros != 0:
        print('Senha Válida')
    else:
        if lMaiuscula < 1:
            nContem1 = 'Letra Maiuscula'
        if lMinuscula < 1:
            nContem2 = 'Letra Minuscula'
        if numeros < 1:
            nContem3 = 'Números'
        print('Senha Inválida')
        print(f'Não Contem: {nContem1} {nContem2} {nContem3}')   

else:
    print('Senha Inválida!')
    print(f'Não Contem: 8 caracteres')   
    


