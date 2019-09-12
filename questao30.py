#Minutos em dias horas e minutos
print('')
minutos = int(input('Digite um valor em minutos: '))

dias = minutos // 60 // 24
horas = minutos // 60 % 24
minutos_restantes = minutos % 60

print('')
print('O valor digitado corresponde a:', dias, 'dias e', horas, 'horas e', minutos_restantes, 'minutos' )