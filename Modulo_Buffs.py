from math import radians
import pygame
from random import randint, choice


class Buffs():


    def __init__(self):
        self.y = -50
        self.x = randint(0,500)
        self.tempoAparecimento = 0
        self.quedaBuff = False
        self.buffEscolhido = False
        self.nomesBuffs = ['armamento','estrela','coracao']
        self.buffCoracao = pygame.image.load('./assets/CoraçãoPixel.png')
        self.buffArmamento = pygame.image.load('./assets/ArmaPixel.png')
        self.buffEstrela = pygame.image.load('./assets/EstrelaPixel.png')
        self.larguraBuffs = self.buffCoracao.get_width()
        self.alturaBuffs = self.buffCoracao.get_height()


    def aparecerBuff(self,tela, elemento):
        if self.y < 900 and self.quedaBuff == False:
            
            if elemento == 'coracao':
                tela.blit(self.buffCoracao, (self.x, self.y))
                self.y += 4

            elif elemento == 'armamento':
                tela.blit(self.buffArmamento, (self.x, self.y))
                self.y += 4
            
            elif elemento == 'estrela':
                tela.blit(self.buffEstrela, (self.x, self.y))
                self.y += 4

        else:
            self.quedaBuff = True
            self.x = randint(0,500)
            self.tempoAparecimento = 0
            self.buffEscolhido = False
            self.y = -50



    def contador(self):
        if self.tempoAparecimento != 400:
            self.tempoAparecimento += 1
            return False
        
        else:
            self.quedaBuff = False
            return True
    
    def escolhaBuff(self):
        escolha = self.nomesBuffs[randint(0,2)]
        self.buffEscolhido = escolha
        return escolha

    
    def verificaEscolhaBuff(self):
        if self.buffEscolhido:
            return True

        else:
            return False
        




        