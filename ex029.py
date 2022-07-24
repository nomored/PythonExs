vel=int(input('Digite a velocidade do veículo: '))
multa = (vel-80)*7

if vel>80:
    print('Você deverá pagar uma multa de {} reais '.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade')
