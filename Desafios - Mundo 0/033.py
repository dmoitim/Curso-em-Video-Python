# Aula 010

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

if num1 < num2 and num1 < num3:
    menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

if num1 > num2 and num1 > num3:
    maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O menor número digitado foi {}.'.format(menor))
print('O maior número digitado foi {}.'.format(maior))