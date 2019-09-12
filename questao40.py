#Quantidade de cigarros gasta por um fumante
print('')
anos = int(input('Digite a quantidade de anos que fuma: '))
cigarros = int(input('Digite a quantidade de cirgarros fumados por dia: '))
preco_carteira = float(input('Digite o preço da carteira de cigarro: '))

#converter anos em dias
dias = anos * 365

#calculo de carteiras
carteira = 20
quantidade_carteiras = cigarros // carteira
resto_carteira = cigarros % carteira

unidade_cigarro = preco_carteira / 20
valor_restante = resto_carteira * unidade_cigarro

print('')
dinheiro_gasto = quantidade_carteiras * preco_carteira * dias
print('O dinheiro gasto pelo fumante foi de: R$ ', dinheiro_gasto)