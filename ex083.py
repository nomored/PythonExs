expr = str(input('Digite a expressão que deseja verificar: '))
par = []
for sp in expr:
    if sp =='(':
        par.append('(')
    elif sp==(')'):
        if len(par)>0:
            par.pop()
        else:
            par.append(')')
            break
if len(par)==0:
    print('Os parênteses estão fechados corretamente!')
else:
    print('Arrume os parênteses!')
