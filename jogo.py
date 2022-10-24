import pygame

from pygame.locals import *
from sys import exit


pygame.init()

#TELA DO JOGO
LARGURA = 600
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders")


relogio = pygame.time.Clock()

# CARACTERÍSTICAS DA NAVE
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('./naveimagens/1 (2).png'))
        self.sprites.append(pygame.image.load('./naveimagens/2.png'))
        self.sprites.append(pygame.image.load('./naveimagens/3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (369-200, 360-200))


        self.rect = self.image.get_rect()
        self.rect.topleft = LARGURA/2 - 85, ALTURA - 170

    def update(self):
        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (369-200, 360-200))

    def andarEsquerda(self):
        if self.x >= 0:
            self.x -= 20

    def andarDireita(self):
        if self.x <= 470:
            self.x += 20


todas_as_sprites = pygame.sprite.Group()   
imgnave = Nave()
todas_as_sprites.add(imgnave)
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

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.update()


