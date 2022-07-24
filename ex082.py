num = list()
count=0
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    ans=str((input('Quer adicionar outro? [S/N]'))).upper().strip()
    if ans=='N':
        break
    elif ans!='S':
        ans = str((input('Resposta inválida! Quer adicionar outro? [S/N]'))).upper().strip()
for i,v in enumerate(num):
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print((f'Os valores digitados foram: {num}'))
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {impar}')
