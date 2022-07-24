#PAR OU ÍMPAR
from random import randint
count=0
while True:
    pl = int(input('Digite 0 para escolher par ou 1 para ímpar: '))
    pc = randint(0,1)
    if pl==pc:
        print('Acertou!',end='')
        count+=1
        if pl==pc==0:
            print(' Eu também escolhi par!')
        elif pl==pc==1:
            print(' Eu também escolhi ímpar!')
    elif pl!=0 and pl!=1:
        print('Jogada inválida! Tente novamente')
    else:
        print('Você perdeu!')
        print(f'Você teve {count} vitórias consecutivas!')
        break
