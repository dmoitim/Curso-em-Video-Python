# Aula 008

from math import hypot

n1 = float(input('Digite o cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(hypot(n1, n2)))
