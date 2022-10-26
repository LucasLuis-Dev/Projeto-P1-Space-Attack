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
imagemTelaInicial = pygame.image.load('./assets/TelaInicial.png')
imagemTelaFinal = pygame.image.load('./assets/TelaFinal.png')
gameIcon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(gameIcon)

fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)




tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Space Invaders")

nave = Nave()
player = jogador()
buffs = Buffs()


estadoAtual = "Tela inicial"


while True:

    if estadoAtual == 'Tela inicial':
        tela.blit(imagemTelaInicial, (0,0))



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:

                if event.key == K_SPACE:
                    estadoAtual = "Comecar jogo"

    elif estadoAtual == "Comecar jogo": 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()  

        relogio.tick(60)
        tela.blit(imagemFundo, (0,0))
        

        player.mostrarPontos(tela)


        if player.jogadorPerdeu():
            estadoAtual = "Tela final"

        
    
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

    elif estadoAtual == "Tela final":
        tela.blit(imagemTelaFinal, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:

                if event.key == K_SPACE:
                    estadoAtual = "Comecar jogo"


        


    pygame.display.update()