import pygame
import time

# 1. Inicializa o reprodutor de áudio
pygame.mixer.init()

# 2. Carrega a música de teste que você baixou
pygame.mixer.music.load('teste.mp3')

# 3. Dá o comando de Play
pygame.mixer.music.play()

print('Tocando o áudio direto do Python! 🎶')

# 4. Segura o programa aberto por 30 segundos para dar tempo de ouvir
time.sleep(30)
