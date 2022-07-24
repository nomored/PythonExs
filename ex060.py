x = int(input('Insira um número para calcular seu fatorial: '))
c = x
f = 1
print('{}! = '.format(x),end='')
while c>0:
    print('{}'.format(c),end='')
    if c>1:
        print('x',end='')
    else:
        print('=',end='')
    f*=c
    c-=1
print(f)
