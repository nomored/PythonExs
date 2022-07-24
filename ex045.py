from random import randint
from time import sleep

print('Vamos jogar jokenpô?')
x=int(input('Digite 0 para escolher pedra, 1 para papel ou 2 para tesoura: '))
op = ('pedra','papel','tesoura')
y = randint(0,2)

if x>2 or x<0:
    print('JOGADA INVÁLIDA')
else:
    print('-' * 30)
    sleep(0.5)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(0.5)
    print('-'*30)
    print('Você escolheu {}'.format(op[x]))
    print('Eu escolhi {}'.format(op[y]))

    if x==y:
        print('Temos um empate!')
    elif y==0 and x==1 or y==1 and x==2 or y==2 and x==0:
        print('Parabéns, você ganhou!')
    else:
        print('Ganhei!')
