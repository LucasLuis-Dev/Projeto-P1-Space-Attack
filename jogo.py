import pygame
from random import randint
from Modulo_Jogador import Nave, jogador, DisparoNave
from Modulo_Buffs import Buffs
from Modulo_NaveInimiga import NaveInimiga, disparoNaveInimiga
from Modulo_Asteroides import Asteroides

from pygame.locals import *
from sys import exit


pygame.init()

# CONSTANTES DO TAMANHO DA TELA DO JOGO

LARGURA = 600
ALTURA = 820


# VARIAVEIS DE CONTROLE DO JOGO

relogio = pygame.time.Clock()
pygame.mixer.music.set_volume(50)
musicaFundo = pygame.mixer.music.load('./Music/MusicaFundo.mp3')
pygame.mixer.music.play(-1)


# VARIAVEIS RESPONSAVEIS PELA ESTÉTICA BÁSICA DO JOGO

IMAGEMFUNDO = pygame.image.load('./assets/fundo_2.png')
IMAGEMTELAINICIAL = pygame.image.load('./assets/TelaInicial.png')
IMAGEMTELAFINAL = pygame.image.load('./assets/TelaFinal.png')
ICONEJOGO = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(ICONEJOGO)


# DEFINIÇÃO DA TELA E NOME DO JOGO

TELA = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Space Invaders")

# CONSTANTES DAS CLASSES UTILIZADAS NO JOGO

NAVE = Nave()
PLAYER = jogador()
BUFFS = Buffs()
NAVEINIMIGA = NaveInimiga()
DISPAROINIMIGO = disparoNaveInimiga()
DISPAROPLAYER = DisparoNave()
ASTEROIDE_1 = Asteroides()
ASTEROIDE_2 = Asteroides()
ASTEROIDE_3 = Asteroides()
ASTEROIDE_4 = Asteroides()
ASTEROIDE_5 = Asteroides()
 

# VARIAVEL DA MAQUINA DE ESTADOS DO JOGO

estadoAtual = "Tela inicial"


# LOOPING DO JOGO
while True:

    if estadoAtual == 'Tela inicial':
        TELA.blit(IMAGEMTELAINICIAL, (0,0))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                
                # Verifica se o jogador quer iniciar o jogo e muda a maquina de estados
                if event.key == K_SPACE:
                    estadoAtual = "Comecar jogo"


    elif estadoAtual == "Comecar jogo": 

        relogio.tick(60)
        TELA.blit(IMAGEMFUNDO, (0,0))
        PLAYER.mostrarPontos(TELA)
        
        # Verifica se o jogador perdeu o jogo
        if PLAYER.jogadorPerdeu():
            estadoAtual = "Tela final"

        # MOSTRA OS OBJETOS NA TELA

        NAVE.mostrarNave(TELA)
        PLAYER.vidasJogador(TELA)
        ASTEROIDE_1.aparecerAsteroide(TELA)
        ASTEROIDE_2.aparecerAsteroide(TELA)
        ASTEROIDE_3.aparecerAsteroide(TELA)
        ASTEROIDE_4.aparecerAsteroide(TELA)
        ASTEROIDE_5.aparecerAsteroide(TELA)
        

        # Mostra a nave inimiga e seus disparos
        if NAVEINIMIGA.tempoSurgimento():
            NAVEINIMIGA.aparecerNaveInimiga(TELA)
 
            # Mostra os disparos da nave inimiga na tela
            if DISPAROINIMIGO.contadorDisparo(NAVEINIMIGA):
                DISPAROINIMIGO.disparar(TELA)  
               
                DISPAROINIMIGO.ajusteTrajetoria(NAVEINIMIGA)
                DISPAROINIMIGO.trajetoria()

        DISPAROINIMIGO.ajusteDisparo(NAVEINIMIGA)

        # Mostra os buffs na tela
        if BUFFS.contador():

            if BUFFS.verificaEscolhaBuff():
                pass
        
            else:
                elemento = BUFFS.escolhaBuff()

            BUFFS.aparecerBuff(TELA, elemento)

            PLAYER.colisaoBuff(NAVE, BUFFS, elemento, PLAYER, TELA)
        

        # MOVIMENTAÇÃO DA NAVE DO JOGADOR
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit() 

            elif event.type == KEYDOWN:
                # Verifica se o botão de disparo do jogador foi pressionado
                if event.key == K_SPACE:
                    DISPAROPLAYER.verificaTeclaApertada()

        # Funcionamento das teclas para mover a nave
        if pygame.key.get_pressed()[K_LEFT]:
            NAVE.andarEsquerda()    
            NAVEINIMIGA.moverNaveInimigaEsquerda()
        
        elif pygame.key.get_pressed()[K_RIGHT]:
            NAVE.andarDireita()
            NAVEINIMIGA.moverNaveInimigaDireita()


        # SISTEMAS DE COLISÃO DE OBJETOS

        PLAYER.colisaoNaveJogador(NAVE, DISPAROINIMIGO)
        PLAYER.colisaoNaveJogador(NAVE, ASTEROIDE_1)
        PLAYER.colisaoNaveJogador(NAVE, ASTEROIDE_2)
        PLAYER.colisaoNaveJogador(NAVE, ASTEROIDE_3)
        PLAYER.colisaoNaveJogador(NAVE, ASTEROIDE_4)
        PLAYER.colisaoNaveJogador(NAVE, ASTEROIDE_5)
        
        
        if DISPAROPLAYER.apertouTecla():
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, NAVEINIMIGA)
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, ASTEROIDE_1)
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, ASTEROIDE_2)
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, ASTEROIDE_3)
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, ASTEROIDE_4)
            PLAYER.colisaoDisparoJogador(DISPAROPLAYER, ASTEROIDE_5)
            
     
    
       # SISTEMA DE EXECUÇÃO DE PODERES DOS BUFFS


        if PLAYER.buffEstrela():
            PLAYER.mostrarBuffEstrela(TELA)


        if PLAYER.buffArmamento():
            DISPAROPLAYER.dispararComBuff(TELA)
            DISPAROPLAYER.ajusteDisparo()
            DISPAROPLAYER.ajusteTrajetoriaComBuff(NAVE)
            DISPAROPLAYER.trajetoria()

        else:           
            DISPAROPLAYER.disparar(TELA)
            DISPAROPLAYER.ajusteDisparo()
            DISPAROPLAYER.ajusteTrajetoria(NAVE)
            DISPAROPLAYER.trajetoria()



    elif estadoAtual == "Tela final":

        TELA.blit(IMAGEMTELAFINAL, (0,0))
        PLAYER.mostrarPontuacaoFinal(TELA)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                # Verifica se o jogador quer jogar novamente
                if event.key == K_SPACE:
                    estadoAtual = "Comecar jogo"
                    PLAYER.recomecarJogo()
                    NAVEINIMIGA.recomecarJogo()

                    ASTEROIDE_1.recomecarJogo()
                    ASTEROIDE_2.recomecarJogo()
                    ASTEROIDE_3.recomecarJogo()
                    ASTEROIDE_4.recomecarJogo()
                    ASTEROIDE_5.recomecarJogo()
                    
                    BUFFS.recomecarJogo()

    pygame.display.update()