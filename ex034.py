sal=float(input('Insira seu salário: '))

if sal<=1250:
    print('Seu novo salário é de R${:.2f}'.format(sal*1.15))
    print('Você recebeu um aumento de R${:.2f}'.format(sal * 0.15))
else:
    print(('Seu novo salário é de R${:.2f}'.format(sal*1.1)))
    print('Você recebeu um aumento de R${:.2f}'.format(sal * 0.1))
