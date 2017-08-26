# Aula 007

d = int(input('Quantos dias alugados? '))
k = float(input('Quantos m rodados? '))

t = (60 * d) + (0.15 * k)

print('O valor a pagar é de R$ {:.2f}.'.format(t))