import random

print('Hmmm... Estou pensando em um número entre 0 e 5...')
n=random.randint(0,5)
guess=int((input('Adivinha qual é: ')))

if guess==n:
    print('Parabéns, você acertou!')
else:
    print('Erroooou! Era o número {}'.format(n))
