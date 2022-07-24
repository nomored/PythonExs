x=0
count=0
s=med=maior=menor=0
user='S'
while user=='S':
    x = int(input('Digite um número: '))
    count+=1
    s+=x
    if count==1:
        maior = menor = x
    else:
        if x>maior:
            maior = x
        if x<menor:
            menor = x
    user=str(input('Deseja digitar outro? [S/N] ')).upper().strip()[0]
    if user!='S' and user!='N':
        user = str(input('Opção inválida! Digite S ou N:  ')).upper().strip()[0]
med = (s / count)
print('A média dos {} números digitados é igual a {:.2f}'.format(count,med))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
print('FIM')
