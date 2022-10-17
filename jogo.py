import pygame

from pygame.locals import *
from sys import exit


pygame.init()

#TELA DO JOGO
LARGURA = 600
ALTURA = 700
x = 0

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders")


relogio = pygame.time.Clock()

nave = pygame.Surface((50, 50))
nave.fill((255, 0, 0))

tela.blit(nave, (50, 50))

# CARACTERÍSTICAS DA NAVE
class Nave():
    def __init__(self):
        self.x = 275
        self.y = 600

    def aparecer(self):
        tela.blit(nave, (self.x, self.y))

    def andarEsquerda(self):
        if self.x >= 0:
            self.x -= 20

    def andarDireita(self):
        if self.x <= 470:
            self.x += 20


navezinha = Nave()


#LOOP DO JOGO
while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        navezinha.andarEsquerda()

    elif pygame.key.get_pressed()[K_RIGHT]:
        navezinha.andarDireita()

    navezinha.aparecer()


    pygame.display.update()


