import pygame
from random import randint

from pygame.locals import *
from sys import exit


pygame.init()

LARGURA = 600
ALTURA = 820

relogio = pygame.time.Clock()

out_screen = -100

buffCoracao = pygame.image.load('./assets/CoraçãoPixel.png')
buffArmamento = pygame.image.load('./assets/ArmaPixel.png')
buffBonus = pygame.image.load('./assets/EstrelaPixel.png')
nave = pygame.image.load("./assets/NavePixel.png")
imagemFundo = pygame.image.load('./assets/fundo.jpg')
gameIcon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(gameIcon)

altura_imagem = buffBonus.get_height()
largura_imagem = buffBonus.get_width()

altura_nave = nave.get_height()
largura_nave = nave.get_width()

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Space Invaders")


class Nave():
    def __init__(self):
        self.x = LARGURA/2 - 50
        self.y = ALTURA - 150
        self.h = altura_nave
        self.w = largura_nave

    def aparecer(self):
        tela.blit(nave, (self.x, self.y))

    def andarEsquerda(self):
        if self.x >= 0:
            self.x -= 20

    def andarDireita(self):
        if self.x <= 470:
            self.x += 20



class Buffs():
    def __init__(self):
        self.x = 0
        self.y = -100
        self.h = altura_imagem
        self.w = largura_imagem
        

    def descer(self):
        self.y += 3


    def ajuste(self):
        if self.y >= ALTURA and self.x <= 470:
            self.y = -100
            self.x = randint(0,470)


    def coracao(self):
        tela.blit(buffCoracao, (self.x, self.y))


    def arma(self):
        tela.blit(buffArmamento, (self.x, self.y))


    def bonus(self):
        tela.blit(buffBonus, (self.x, self.y))


def colisao(a, b):
    return a.x + a.w > b.x and a.x < b.x + b.w and a.y + a.h > b.y and a.y < b.y + b.h


buffzinho = Buffs()
navezinha = Nave()
contador = 0

while True:
    relogio.tick(60)
    tela.blit(imagemFundo, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if pygame.key.get_pressed()[K_a]:
        navezinha.andarEsquerda()
    
    elif pygame.key.get_pressed()[K_d]:
        navezinha.andarDireita()

    
    
    navezinha.aparecer()

    if contador <= 300:
        buffzinho.arma()
        buffzinho.descer()

    elif contador >= 900 and contador <= 1230:
        buffzinho.coracao()
        buffzinho.descer()

    
    elif contador >= 1600 and contador <= 1900:
        buffzinho.bonus()
        buffzinho.descer()

    elif contador >= 2400:
        contador = 0

    if colisao(buffzinho, navezinha):
        buffzinho.x = out_screen

    contador += 1
    buffzinho.ajuste()

    pygame.display.update()