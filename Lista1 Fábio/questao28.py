#Horas em semanas, dias e horas
print('')
horas = int(input('Digite um valor em horas: '))

semanas = horas // 24 // 7
dias = horas // 24 % 7
horas_restantes = horas % 24

print('')
print('O valor digitado corresponde a:', semanas , 'semanas ,', dias, 'dias e' , horas_restantes, 'horas')