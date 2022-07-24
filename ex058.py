import random
print('Hmmm... Estou pensando em um número entre 0 e 10...')
n=random.randint(0,10)
acerto = False
palpite = 0
while not acerto:
    guess = int((input('Adivinha qual é: ')))
    palpite+=1
    if guess == n:
        acerto = True
    else:
        if guess<n:
            print('Mais...Tente novamente...')
        elif guess>n:
            print('Menos... Tente novamente...')

print('Parabéns, você acertou com {} palpites!'.format(palpite))
