def animal(entrada, entrada2, entrada3):
    if entrada == 'vertebrado':
        if entrada2 == 'ave':
            if entrada3 == 'carnivoro':
                return 'aguia'
            elif entrada3 == 'onivoro':
                return 'pomba'
        elif entrada2 == 'mamifero':
            if entrada3 == 'onivoro':
                return 'homem'
            elif entrada3 == 'herbivoro':
                return 'vaca'
    elif entrada == 'invertebrado':
        if entrada2 == 'inseto':
            if entrada3 == 'hematofago':
                return 'pulga'
            elif entrada3 == 'herbivoro':
                return 'lagarta'
        elif entrada2 == 'anelideo':
            if entrada3 == 'ematofago':
                return 'sanguessuga'
            elif entrada3 == 'onivoro':
                return 'minhoca'

definicao1 = input('Tipo de animal: ')
definicao2 = input('Tipo de animal: ')
definicao3 = input('Tipo de animal: ')


tipo_de_animal = animal(definicao1, definicao2, definicao3)

print(tipo_de_animal)