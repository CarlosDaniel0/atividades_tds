def estado(sigla):
    if sigla.upper() == 'RJ':
       return 'Carioca'
    elif sigla.upper() == 'SP':
        return 'Paulista'
    elif sigla.upper() == 'MG':
        return 'Mineiro'
    else:
        return 'Outros Estados'

def principal():
    print(estado('rj'))
    print(estado('sp'))
    print(estado('pi'))
    print(estado('mg'))

principal()

        
    