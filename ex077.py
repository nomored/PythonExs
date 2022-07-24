tupla = ('pasta','arvore','abacaxi','mineral','chapeu','videogame','gato')

for x in tupla:
    print(f'\nEm {x} tem as vogais: ',end='')
    for letra in x:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

