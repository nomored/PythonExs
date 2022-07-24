from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    print('Faltam {} anos para você se alistar'.format(18-idade))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(idade-18))

