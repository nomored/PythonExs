sex = str(input('Digite seu sexo (F/M): ')).upper().strip()[0]
while sex not in 'FM':
    sex = str(input('Resposta inválida! Digite seu sexo (F/M) novamente: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sex))
