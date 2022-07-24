x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))
op = 0
while op!=5:
    print('   [1] SOMAR\n   [2]MULTIPLICAR\n   [3]SABER QUAL É MAIOR'
                 '\n   [4]INSERIR NOVOS NÚMEROS\n   [5]SAIR DO PROGRAMA')
    op=int(input('O que você deseja fazer com estes números? '))
    if op==1:
        print('{} + {} = {}'.format(x,y,x+y))
    elif op==2:
        print('{} x {} = {}'.format(x, y, x * y))
    elif op==3:
        if x > y:
            print('{} é maior do que {}'.format(x,y))
        elif y > x:
            print('{} é maior do que {}'.format(y,x))
        elif x==y:
            print('Os números inseridos são iguais')
    elif op==4:
        print('Informe os números novamente:')
        x = int(input('Insira o primeiro número: '))
        y = int(input('Insira o segundo número: '))
    elif op==5:
        print('Tchau!')
    else:
        print('Opção inválida! Tente novamente...')
    print('='*30)
print('FIM')
