#segundos em horas, minutos e segundos
print('')
s = int(input('Digite um valor em segundos: '))

horas = s // 3600
minutos = s % 3600 // 60
segundos = s // 1 % 10

print('')
print('Seu valor corresponde =', horas, ':', minutos, ':', segundos)