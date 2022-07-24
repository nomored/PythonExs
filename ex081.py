num = list()
count=0
while True:
    num.append(int(input('Digite um número: ')))
    ans=str((input('Quer adicionar outro? [S/N]'))).upper().strip()
    if ans=='N':
        break
    elif ans!='S':
        ans = str((input('Resposta inválida! Quer adicionar outro? [S/N]'))).upper().strip()
print(f'Foram digitados {len(num)} valores')
num.sort(reverse=True)
print((f'Os valores, em ordem decrescente, são: {num}'))
if 5 in num:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
