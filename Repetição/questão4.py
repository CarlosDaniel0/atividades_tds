#primos entre limite inferior e superior
def principal():
    n = int(input('N: '))
    lInfer = int(input('Inferior: '))
    lSuper = int(input('Superior: '))

    #verifica a função e retorna um valor bool
    res = primo(n)

    while lInfer < lSuper:
        #trabalho
        if res == True:
            print(n)
        n -= 1
        lInfer += 1
        #atualiza a cada loop
        res = primo(n)

def primo(n):
    #verifica se alem de ser multiplo é o próprio número
    if ((n % 2 == 0) and not(n == 2)):
        pass
    elif ((n % 3 == 0) and not(n == 2)):
        pass
    elif ((n % 5 == 0) and not(n == 2)):
        pass
    elif ((n % 7 == 0) and not(n == 2)):
        pass
    else:
        return True

principal()