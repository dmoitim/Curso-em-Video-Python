# Aula 010

sal = float(input('Qual é o salário do funcionário? R$ '))

if sal <= 1250:
    salnovo = sal * 1.15
else:
    salnovo = sal * 1.10

print('Quem ganhava R$ {:.2f} passará a ganhar R$ {:.2f}.'.format(sal, salnovo))