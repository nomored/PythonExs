sac = int(input('Que valor você deseja sacar? '))
tot = sac
nota = 50
t_nota=0
while True:
    if tot>=nota:
        tot-=nota
        t_nota+=1
    else:
        if t_nota>0:
            print(f'{t_nota} cédulas de R${nota:.2f}')
        if nota==50:
            nota=20
        elif nota==20:
            nota=10
        elif nota==10:
            nota=1
        t_nota=0
        if tot==0:
            break




