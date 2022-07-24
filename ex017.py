import math
co=float(input('Digite o comprimento do cateto oposto: '))
ca=float(input('Digite o comprimento do cateto adjacente: '))
hi= math.hypot(co,ca)
print('O comprimento da hipotenusa é de {:.2f}'.format(hi))
