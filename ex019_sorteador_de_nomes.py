import random

print('_______Sorteador de nomes do Craaaudiooo________')
p1 = input('primeiro nome:')
p2 = input('segundo nome:')
p3 = input('terceiro nome:')
p4 = input('quarto nome:')
lista = [p1, p2, p3, p4]
indice_aletorio = int((random.random() * 4))
print("O(a) sorturdo foi o(a) ", lista[indice_aletorio])
