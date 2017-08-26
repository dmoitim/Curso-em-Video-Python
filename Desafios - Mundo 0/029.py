# Aula 010

num = float(input('Qual a velocidade atual do carro? '))

if num > 80.0:
    multa = (num - 80.0) * 7
    print('Você foi multado em R$ {:.2f}.'.format(multa))

print('Bom dia! Dirija com segurança.')