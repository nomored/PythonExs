s=0

for x in range(1,501):
    if x%2!=0 and x%3==0:
        s+=x
print('A soma dos valores é igual a {}'.format(s))
