# Aula 008

from pygame import mixer

mixer.init()
mixer.music.load('021_musica.mp3')
mixer.music.play()

input('Tocou? ')