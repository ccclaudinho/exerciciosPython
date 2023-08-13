condicao = True
start = 0
x = 0
while condicao:
    num = int(input('Digite um número para ver sua tabuada:'))
    if num == 0:
        condicao = False
    else:
        for start in range(11):
            print(f'{num}x{start}={start * num}')



