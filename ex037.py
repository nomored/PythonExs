x = int(input('Insira um número inteiro: '))
base = int (input('Digite 1 para convertê-lo em binário, 2 para octal ou 3 para hexadecimal: '))

if base == 1:
    print('O número {} em binário é: {}'.format(x,bin(x)))
elif base == 2:
    print('O número {} em octal é: {}'.format(x, oct(x)))
elif base == 3:
        print('O número {} em hexadecimal é: {}'.format(x, hex(x)))
