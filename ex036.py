casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salário mensal: '))
anos = int(input('Digite em quantos anos você quer pagar: '))

parc = casa/anos/12

if parc <= sal * 0.3:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
