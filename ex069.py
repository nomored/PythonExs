c_id18=c_id20m=c_sm=0
while True:
    id = int(input('Insira sua idade: '))
    sex=' '
    while sex not in 'FM':
        sex= str(input('Insira seu sexo [F/M]: ')).upper().strip()[0]
    if id>=18:
        c_id18+=1
    if sex=='M':
        c_sm+=1
    if sex=='F' and id<20:
        c_id20m+=1
    conti=' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if conti=='N':
        break
print(f'{c_id18} pessoas são maiores de idade')
print(f'{c_sm} pessoas são do sexo masculino')
print(f'{c_id20m} pessoas do sexo feminino possuem menos de 20 anos')
