n = int(input('Quantos termos da sequência de Fibonacci você deseja? '))
a1=0
a2=1
print('{} | {}'.format(a1,a2),end='')
count=3
while count<=n:
    a3=a1+a2
    print(' | {}'.format(a3),end='')
    a1=a2
    a2=a3
    count+=1
print('\nFIM')