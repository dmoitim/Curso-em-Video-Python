# Aula 009

f = str(input('Digite seu nome completo: ')).strip()

print('Primeiro: {}'.format(f.split()[0]))
print('Último: {}.'.format(f.split()[-1]))
