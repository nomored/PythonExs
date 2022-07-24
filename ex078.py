lista = []
maior = menor = 0
for x in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {x}: ')))
    if x==0:
        maior = menor = lista[x]
    else:
        if lista[x]>maior:
            maior=lista[x]
        if lista[x]<menor:
            menor=lista[x]
print(f'Os valores digitados são: {lista}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
