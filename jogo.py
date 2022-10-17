import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 600
altura = 700
x = 0


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space Invaders')
relogio = pygame.time.Clock()


while True:
    relogio.tick(40)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20 
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20


    pygame.draw.rect(tela, (0, 255, 0), (x, 600, 50, 50))

    
    pygame.display.update()


