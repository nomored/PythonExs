from datetime import date

ano = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc

if idade<=9:
    print('Sua categoria é MIRIM')
elif idade<=14:
    print('Sua categoria é INFANTIL')
elif idade<=19:
    print('Sua categoria é JÚNIOR')
elif idade<=25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
