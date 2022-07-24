dias=int(input('Insira a quantidade de dias pelos quais o carro foi alugado: '))
km=float(input('Insira a quantidade de Km rodados: '))
p=60*dias+0.15*km
print('O valor a ser pago é de R${:.2f}'.format(p))
