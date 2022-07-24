peso = float(input('Insira seu peso em Kg: '))
alt = float(input(('Insira sua altura em m: ')))
imc = peso / (alt**2)
print('Seu IMC é {:.1f}'.format(imc))

if imc<18.5:
    print('Você está abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Você está no peso ideal')
elif imc>=25 and imc<30:
    print('Você está no sobrepeso')
elif imc>=30 and imc<=40:
    print('Vcocê está na obesidade')
elif imc>40:
    print('Você está na obesidade mórbida')

