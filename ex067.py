while True:
    x=int(input('Insira o número que você deseja ver a tabuada: '))
    c=0
    if x>=0:
        for c in range(0,11):
            print('{} x {} = {}'.format(x,c,x*c))
    else:
        break
print('FIM')