p = float(input('Digite o preço do produto: '))
cp = int(input('Digite 1 para pagamento à vista no dinheiro/cheque\n'
               'Digite 2 para pagamento à vista no cartão\n'
               'Digite 3 para parcelar em até 2x no cartão\n'
               'Digite 4 para parcelar em 3x ou mais no cartão\n'
               'Sua escolha: '))

print('O preço normal é R${:.2f}'.format(p))

if cp==1:
    print('O preço à vista em dinheiro/cheque é R${:.2f}'.format(p*0.9))
elif cp==2:
    print('O preço à vista no cartão é R${:.2f}'.format(p*0.95))
elif cp==3:
    print('O preço em até 2x no cartão é R${:.2f}'.format(p))
elif cp==4:
    print('O preço em 3x ou mais no cartão é R${:.2f}'.format(p*1.2))
