#n, Limite superior, limite inferior

n = int(input('Digite o valor de: '))
lInfer = int(input('Digite o valor do Limite Infeior: '))
lSuper = int(input('Digite o valor do Limite Superior: ')) 


while lInfer <= lSuper:
    if lInfer % n == 0:
        print(lInfer)
    lInfer += 1