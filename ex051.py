a = int(input('Insira o primeiro termo da P.A.: '))
r = int(input('Insira a razão da P.A.: '))

print('Os 10 primeiros termos da P.A. são:')
for c in range(0,10):
    print(a+r*c)
print('FIM')
