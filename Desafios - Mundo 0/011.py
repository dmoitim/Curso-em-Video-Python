# Aula 007

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

area = a * l
tinta = area / 2

print('Para pintar {:.2f} m², você precisará de {:.2f} litros de tinta.'.format(area, tinta))