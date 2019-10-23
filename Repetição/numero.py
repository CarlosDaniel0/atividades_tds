def programa():
    n = int(input('Digite um valor: '))
    atual = 0

    while atual <= n:
        if atual % 2 == 0:
            print(atual)
        atual += 1

print('')
programa()
print('FIM')