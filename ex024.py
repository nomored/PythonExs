cid=str(input('Insira o nome da sua cidade: '))
cid=cid.upper()
dividido=cid.split()
if dividido[0]=='SANTO':
    print('O nome de sua cidade começa com "Santo"')
else:
    print('O nome de sua cidade não começa com "Santo"')
