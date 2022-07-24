x = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')))
print(f'Os valores digitados foram: {x}')
print(f'O número 9 apareceu {x.count(9)} vezes')
if 3 in x:
     print(f'O número 3 apareceu na {x.index(3)+1}ª posição')
else:
     print('Você não digitou o número 3')
print('Os valores pares são: ',end='')
for n in x:
     if n%2==0:
          print(n,end=' ')

