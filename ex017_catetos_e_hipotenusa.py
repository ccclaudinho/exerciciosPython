print('__________Programa gerador de Hipotenusa__________')
cateto_oposto = float(input('Qual o cumprimento do cateto oposto: '))
cateto_adjacente = float(input('Qual o cumprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto**2+cateto_adjacente**2)**(1/2)

print('a hipotenusa vai medir {:0.2f}'.format(hipotenusa))
