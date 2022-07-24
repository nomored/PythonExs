from time import sleep
s_id = 0
count_m = 0
nome_maiorid = ''
maiorid_m = 0
for c in range(1,5):
    nome = str(input('Digite seu nome: ')).upper().strip()
    id = int(input('Digite sua idade: '))
    sex = str(input('Digite seu sexo (F/M): ')).upper().strip()
    print('='*30)
    sleep(0.5)
    s_id+=id
    if c==1 and sex=='M':
        maiorid_m = id
        nome_maiorid = nome
    if sex=='M' and id > maiorid_m:
        maiorid_m = id
        nome_maiorid = nome

    if sex == 'F' and id < 20:
        count_m += 1

print('A média de idades é igual a {:.0f}'.format(s_id/4))
print('{} é a pessoa de sexo masculino mais velha e tem {} anos'.format(nome_maiorid,maiorid_m))
print('{} pessoas de sexo feminino têm menos que 20 anos'.format(count_m))



