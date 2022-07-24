km=int(input('Digite a distância da viagem em km: '))

if km<=200:
    print('O preço da viagem é de {:.2f} reais'.format(km*0.5))
else:
    print('O preço da viagem é de {:.2f} reais'.format(km*0.45))
