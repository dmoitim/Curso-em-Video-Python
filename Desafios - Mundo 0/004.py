# Aula 006

var = input('Digite algo: ')

print('Tipo primitivo: '.format(type(var)))

print('Alfanumérico: {0}'.format(var.isalnum()))
print('Alfa: {0}'.format(var.isalpha()))
print('Numérico: {0}'.format(var.isnumeric()))
print('Decimal: {0}'.format(var.isdecimal()))
print('Dígito: {0}'.format(var.isdigit()))
print('Minúsculo: {0}'.format(var.islower()))
print('Impresso: {0}'.format(var.isprintable()))
print('Espaço: {0}'.format(var.isspace()))
print('Título: {0}'.format(var.istitle()))
print('Maiúsculo: {0}'.format(var.isupper()))
print('Identificador: {0}'.format(var.isidentifier()))