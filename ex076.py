fones = ('Soundcore Q20',365,'Galaxy Buds 2',449,'Echo buds',749,'JBL Live 650BT',
         999,'Beats Studio Buds',1050,'Airpods Pro',1619)
print('Os melhores fones com cancelamento de ruído, segundo o site Techtudo: ')
for x in range(0,len(fones)):
    if x%2==0:
        print(f'{fones[x]} = ',end='')
    else:
        print(f'R${fones[x]:.2f}')
        