import pygame
import os
import time
import random
pygame.init()


nave_inimiga = pygame.image.load(os.path.join('nave_inimiga.png'))

laser = pygame.image.load(os.path.join('laser.png'))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def mover(self, vel):
        self.y += vel

    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)

    def colisao(self, obj):
        return colidir(self, obj)


class Nave:
    tempo = 30

    def __init__(self, x, y, vida=100):
        self.x = x
        self.y = y
        self.vida = vida
        self.nave_inimiga_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.nave_inimiga_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def mover_lasers(self, vel, obj):
        self.tempo()
        for laser in self.lasers:
            laser.mover(vel)
            if laser.fora_da_tela(ALTURA):
                self.lasers.remover(laser)
            elif laser.colisao(obj):
                obj.vida -= 10
                self.lasers.remover(laser)

    def tempo(self):
        if self.cool_down_counter >= self.tempo:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def tiro(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
           

    def obter_largura(self):
        return self.nave_inimiga_img.obter_largura()
    
    def obter_altura(self):
        return self.nave_inimiga_img.obter_altura()
