# Aula 009

n = int(input('Digite um número entre 0 e 9999: '))
n = str(n).rjust(4, '0')

print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))