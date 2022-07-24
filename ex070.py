s=c_1k=men_p=count=0
men_n=' '
while True:
    n = str(input('Insira o nome do produto: ')).upper().strip()
    p = float(input('Insira o preço do produto: '))
    s+=p
    count+=1
    if p>1000:
        c_1k+=1
    if count==1:
        men_p=p
        men_n=n
    else:
        if p<men_p:
            men_p=p
            men_n=n
    conti=' '
    while conti not in 'SN':
        conti=str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if conti == 'N':
            break
print(f'O total gasto na compra é de R${s:.2f}')
print(f'{c_1k} produtos custam mais de R$1000.00')
print((f'{men_n} custa R${men_p:.2f} e é o produto mais barato'))
