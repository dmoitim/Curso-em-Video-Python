# Aula 009

f = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase.'.format(f.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(f.find('A') + 1))
print('A letra A aparece pela última vez na posição {}.'.format(f.rfind('A')))