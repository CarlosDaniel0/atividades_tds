#distancia entre 2 pontos no plano cartesiano
print('')
x1 = int(input('Digite o ponto x1: '))
x2 = int(input('Digite o ponto x2: '))

y1 = int(input('Digite o ponto y1: '))
y2 = int(input('Digite o ponto y2: '))

d = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 1/2

print('')
print('A distância entre dois pontos é:', d)