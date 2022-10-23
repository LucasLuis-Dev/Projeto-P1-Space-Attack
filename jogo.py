import pygame
from random import randint
import os
from Modulo_Jogador import Nave, jogador
from Modulo_Buffs import Buffs

from pygame.locals import *
from sys import exit


pygame.init()

# Constantes do tamanho da plataforma do jogo

LARGURA = 600
ALTURA = 820


# Variavel para controlar os frames da tela

relogio = pygame.time.Clock()


# Variaveis responsaveis pela estetica

imagemFundo = pygame.image.load('./assets/fundo_2.png')
gameIcon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(gameIcon)

fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)




tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Space Invaders")

nave = Nave()
player = jogador()
buffs = Buffs()



while True:
    
    relogio.tick(60)
    tela.blit(imagemFundo, (0,0))
    

    # Mensagem dos pontos
    mensagemPontos = "Pontos: "
    textoFormatadoPontos = fonteTextoGame.render(mensagemPontos, False, (255,255,255))
    tela.blit(textoFormatadoPontos, (30, 30))

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    # Funcionamento das teclas para mover a nave
    if pygame.key.get_pressed()[K_LEFT]:
        nave.andarEsquerda()    
    
    elif pygame.key.get_pressed()[K_RIGHT]:
        nave.andarDireita()


    nave.mostrarNave(tela)
    player.vidasJogador(tela)

   
    
    if buffs.contador():

        if buffs.verificaEscolhaBuff():
            pass
    
        else:
            elemento = buffs.escolhaBuff()


        buffs.aparecerBuff(tela, elemento)

        player.colisaoBuff(nave, buffs, elemento, player, tela)

    if player.buffEstrela():
        player.mostrarBuffEstrela(tela)

    


    pygame.display.update()