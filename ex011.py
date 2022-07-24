a = float(input('Digite a altura de sua parede: '))
l = float(input('Digite a largura de sua parede: '))
area = a*l
l_tinta = area/2
print('Será necessário utilizar {:.1f} litros de tinta para pintar sua parede'.format(l_tinta))
