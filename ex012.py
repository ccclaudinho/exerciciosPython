print("_____Gerador de descontos ________")

preco_original = float(input("Qual o preço do produto? "))
desconto = int(input("Quantos % de desconto? "))

print(f'O produto que custava R${preco_original}, na promoção com {desconto}% de desconto, vai custar {(100-desconto)/100*preco_original}')

