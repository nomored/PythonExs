a = int(input('Insira o primeiro termo da P.A.: '))
r = int(input('Insira a razão da P.A.: '))

print('Os 10 primeiros termos da P.A. são: ')
c=0
while c<10:
    print(a+r*c,end=' ')
    c+=1
print('\nFIM')
