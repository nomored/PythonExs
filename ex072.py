
y = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
     'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
     x = int(input('Digite um número entre 0 e 20: '))
     if 0<=x<=20:
          break
     print('Tente novamente!')
print(f'Você escolheu o número {y[x]}')

