x=int(input('Insira o primeiro número: '))
y=int(input('Insira o segundo numero: '))
z=int(input('Insira o terceiro número: '))

#Menor:
if x<y and x<z:
    menor=x
elif y<x and y<z:
    menor=y
elif z<x and z<y:
    menor=z
print('O menor valor é {}'.format(menor))

#Maior:
if x>y and x>z:
    maior=x
elif y>x and y>z:
    maior=y
elif z>x and z>y:
    maior=z
print('O maior valor é {}'.format(maior))
