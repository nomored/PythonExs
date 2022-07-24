frase=str(input('Insira uma frase: ')).lower().strip()
print('Seu nome possui {} letras a'.format(frase.count('a')))
print('A primeira letra a aparece na posição {}'.format(frase.find('a')+1))
print('A última letra a aparece na posição {}'.format(frase.rfind('a')+1))
