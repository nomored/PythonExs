x=0
count=0
s=0
while x!=999:
    x = int(input('Digite um número (ou digite 999 para encerrar): '))
    if x!=999:
        count+=1
        s+=x
print('A soma dos {} números digitados é igual a {}'.format(count,s))
print('FIM')
