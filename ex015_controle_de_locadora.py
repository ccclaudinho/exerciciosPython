print(' ____________Controle de cobrança de locadora____________')
dias = int(input('Quantos dias alugado?'))
km = int(input('Quantos Km rodados?'))

preco_por_dia = 60.00 * dias
preco_por_km = 0.15 * km
preco_total = preco_por_km + preco_por_dia

print(f'O total a pagar pelo aluguel é R$ {preco_total}')


