# Aula 010

from random import randint
from time import sleep

num = int(input('Pensei em um número de 0 a 5, veja se você adivinha em qual foi: '))
pc = randint(0, 5)

print('Processando...')
sleep(3)

if pc == num:
    print('Parabéns, você ganhou!')
else:
    print('Eu ganhei! Eu pensei no número {} e você digitou {}.'.format(pc, num))