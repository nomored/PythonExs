f = str(input('Digite uma frase para ver se é um palíndromo: ')).strip().upper()
divid = f.split()
junto = ''.join(divid)
inv = ''
for l in range(len(junto)-1,-1,-1):
    inv += junto[l]
print('O inverso de {} é {}'.format(junto,inv))
if inv==junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')

#Outra opção é utilizar inv = junto[::-1] para inverter a frase

