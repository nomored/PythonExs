lista = []
for x in range(0,5):
    num=int(input('Digite um número: '))
    if x==0 or num>lista[-1]:
        lista.append(num)
    else:
        pos=0
        while pos<len(lista):
            if num<=lista[pos]:
                lista.insert(pos,num)
                break
            pos+=1
print(f'A lista dos valores digitados em ordem é:{lista}')
