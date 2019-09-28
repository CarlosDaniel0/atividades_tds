def e_par(n):
    return n % 2 == 0

def impar_par(n):
    if e_par(n):
        return 'Par'
    else:
        return 'Impar'

print(impar_par(4))
print(impar_par(5))