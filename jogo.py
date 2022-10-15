import pygame

from pygame.locals import *
from sys import exit


pygame.init()

LARGURA = 600
ALTURA = 820


relogio = pygame.time.Clock()


buff = pygame.image.load('./assets/CoraçãoPixel.png')
nave = pygame.image.load("./assets/NavePixel.png")
imagemFundo = pygame.image.load('./assets/fundo.jpg')
gameIcon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(gameIcon)

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Asteroides")


while True:
    relogio.tick(35)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagemFundo, (0,0))

    pygame.display.update()