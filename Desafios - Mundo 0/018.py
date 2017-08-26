# Aula 008

from math import sin, cos, tan, radians

n = float(input('Digite o ângulo: '))
r = radians(n)

print('O ângulo {} tem o seno {:.2f}.'.format(n, sin(r)))
print('O ângulo {} tem o coseno {:.2f}.'.format(n, cos(r)))
print('O ângulo {} tem a tangente {:.2f}.'.format(n, tan(r)))