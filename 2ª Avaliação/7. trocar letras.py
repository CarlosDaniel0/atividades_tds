def num(numero):
    numeros = '1234567890'
    if numero in numeros:
        return True

def remover(caractere):
    numeros = '1234567890'
    if ord(caractere) >= 65 and ord(caractere) <= 90:
        return True
    elif ord(caractere) >= 97 and ord(caractere) <= 122:
        return True
    elif caractere in numeros:
        return True
    else:
        return False

def vogais(vogal):
    vogais = 'aeiouAEIOU'
    if vogal in vogais:
        return True

frase = input('Digite uma frase: ')
novaFrase = ''

for letra in frase:
    if not(remover(letra)):
        letra = ''
    elif vogais(letra):
        letra = letra.upper()
    elif num(letra):
        letra = '@'

    novaFrase = novaFrase + letra

print(novaFrase)