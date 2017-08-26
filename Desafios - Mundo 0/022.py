# Aula 009

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras no primeiro nome: {}'.format(len(nome.split()[0])))