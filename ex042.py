r1=float(input('Insira o comprimento da primeira reta: '))
r2=float(input('Insira o comprimento da segunda reta: '))
r3=float(input('Insira o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1!=r2!=r3!=r1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('As retas não podem formar um triângulo')
