num = list()
ans = 'S'
while ans=='S':
    n=int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    else:
        n=int(input('Este número já está na lista. Digite outro: '))
    ans=str((input('Quer adicionar outro? [S/N]'))).upper().strip()
num.sort()
print('Finalizando...')
print(f'Os números inseridos foram: {num}')
