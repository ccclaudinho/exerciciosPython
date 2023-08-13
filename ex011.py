print("___________Medidor de Consumo de tinta______________")
largura = float(input("Informe a largura da parede em metros quadrados: "))
altura = float(input("Informe a altura da parede em metros quadrados: "))
area = largura * altura
print(f'sua parede tem a dimensão de {largura}x{altura}  sua área é {area}')
print(f'Para pintar essa parede, você precisará de {area/2}L de tinta')
