x = int(input('Digite um número: '))
count=0
for c in range(1,x+1):
    if x%c==0:
        print('\033[32m',end='')
        count+=1
    else:
        print('\033[m', end='')
    print('{} '.format(c),end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(x,count),end='')
if count==2:
    print(',portanto ele é primo'.format(x))
else:
    print(',portanto ele não é primo'.format(x))

