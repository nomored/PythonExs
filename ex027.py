nome=str(input(('Insira seu nome completo: '))).strip().title()
dividido=nome.split()
print('Seu primeiro nome é {}'.format(dividido[0]))
#COMO VER O ÚLTIMO???????
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
