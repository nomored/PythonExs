tipo = int(input('Digite 0 para somar valores inteiros ou 1 para somar valores decimais: '))


if tipo == 0:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    s = n1 + n2
    print('A soma dos valores {} e {} é igual a {}'.format(n1, n2, s))
elif tipo == 1:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    s = n1+n2
    print('A soma dos valores {} e {} é igual a {}'.format(n1,n2,s))

