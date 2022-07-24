p1 = float(input('Insira sua nota da primeira prova: '))
p2 = float(input('Insira sua nota da segunda prova: '))
med = (p1 + p2)/2

print('Sua média é: {:.1f}'.format(med))

if med < 5:
    print('Você foi reprovado :(')
elif 7 > med >= 5:
    print('Você está de recuperação :|')
elif med >=  7:
    print('Você foi aprovado :)')
