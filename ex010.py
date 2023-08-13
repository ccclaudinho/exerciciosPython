class Conversora:

    #Conversor de moedas
    print("__________Conversor de moedas___________")
    reais = float(input("Quantos reais você tem? "))
    cotacao = float(input("qual a cotação do câmbio BRL/USD?"))

    print(f'com a cotação de R${cotacao} por dolár, você pode comprar ${reais/cotacao} dólares')

