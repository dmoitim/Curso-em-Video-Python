# Aula 010

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))


if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Formam um triângulo.')
else:
    print('Não formam um triângulo.')