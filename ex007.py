n1 = float(input('Digite sua nota da P1: '))
n2 = float(input('Digite sua nota da P2: '))
x = (n1+n2)/2
print('Sua média é {}'.format(x))

if x>=6:
    print('Você passou!')
else:
    print('Você está de recuperação!')