nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
nome=(nome.strip())
dividido = nome.split()
print('Seu nome completo possui {} letras'.format(len(''.join(dividido))))
primeiro_nome=dividido[0]
print('Seu primeiro nome possui {} letras'.format(len(primeiro_nome)))
