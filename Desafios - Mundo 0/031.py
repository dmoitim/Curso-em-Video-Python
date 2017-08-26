# Aula 010

num = float(input('Qual a distância da sua viagem? '))

if num <= 200:
    print('O preço da passagem será de R$ {:.2f}.'.format(num*0.50))
else:
    print('O preço da passagem será de R$ {:.2f}.'.format(num * 0.45))