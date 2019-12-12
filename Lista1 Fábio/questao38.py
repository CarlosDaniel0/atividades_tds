#Soma de frações.
numerador1 = int(input('Digite o númerador 1: '))
denominador1 = int(input('Digite o númerador 2: '))

numerador2 = int(input('Digite o númerador 2: '))
denominador2 = int(input('Digite o númerador 2: '))


denominador = denominador1 * denominador2
n1 = (denominador / denominador1) * numerador1
n2 = (denominador / denominador2) * numerador2
print('A soma das frações é: ')
print('', n1 + n2)
print('---')
print('', denominador)