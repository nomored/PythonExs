from datetime import date
count = 0
for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento: '))
    id = date.today().year - ano
    if id>=21:
        count+=1
print('{} pessoas atingiram a maioridade'.format(count))
print('{} pessoas não atingiram a maioridade'.format(7-count))
