import pygame
from random import randint

from pygame.locals import *
from sys import exit


pygame.init()

# Constantes do tamanho da plataforma do jogo

LARGURA = 600
ALTURA = 820


# Variavel para controlar os frames da tela

relogio = pygame.time.Clock()


# Variaveis responsaveis pela estetica

buffCoracao = pygame.image.load('./assets/CoraçãoPixel.png')
buffArmamento = pygame.image.load('./assets/ArmaPixel.png')
buffBonus = pygame.image.load('./assets/EstrelaPixel.png')
vidaJogador = pygame.image.load('./assets/VidaJogador.png')
bonusJogador = pygame.image.load("./assets/BuffPontos.png")
nave = pygame.image.load("./assets/NavePixel.png")
imagemFundo = pygame.image.load('./assets/fundo.jpg')
gameIcon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(gameIcon)

fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)




tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Space Invaders")


# Classe das naves com seus atributos e metodos

class Nave():
    def __init__(self):
        self.x = LARGURA/2 - 50
        self.y = ALTURA - 110
        self.h = altura_nave
        self.w = largura_nave

    def aparecer(self):
        tela.blit(nave, (self.x, self.y))

    def andarEsquerda(self):
        if self.x >= 0:
            self.x -= 10

    def andarDireita(self):
        if self.x <= 500:
            self.x += 10

# Varieaveis resposnaveis pela colisão

altura_imagem = buffBonus.get_height()
largura_imagem = buffBonus.get_width()

altura_nave = nave.get_height()
largura_nave = nave.get_width()

out_screen = -110


def colisao(a, b):
    return a.x + a.w > b.x and a.x < b.x + b.w and a.y + a.h > b.y and a.y < b.y + b.h

# Classe resposnsavel pelos buffs com seus atributos e metodos

class Buffs():
    def __init__(self):
        self.x = 0
        self.y = -100
        self.h = altura_imagem
        self.w = largura_imagem
        

    def descerBuffs(self):
        self.y += 3

    # Faz o buff descer por cima da tela novamente
    def ajuste(self):
        if self.y > 800 and self.x <= 470:
            self.y = -100
            self.x = randint(0,500)

    # Verifica se o buff já desceu por toda a tela
    def buffDesceu(self):
        if self.y > 800:
            return True
        
        else:
            return False


    def coracaoAparecer(self):
        tela.blit(buffCoracao, (self.x, self.y))


    def armaAparecer(self):
        tela.blit(buffArmamento, (self.x, self.y))


    def bonusAparecer(self):
        tela.blit(buffBonus, (self.x, self.y))


# Classe de gerenciamento do jogador com seus metodos e atributos

class VidaPersonagem():
    def __init__(self):
        self.x = 530
        self.y = 30
        self.quantVidas = 3


    def vidasJogador(self):
        if self.quantVidas == 3:
            tela.blit(vidaJogador, (self.x, self.y))
            tela.blit(vidaJogador, (self.x - 50, self.y))
            tela.blit(vidaJogador, (self.x - 100, self.y))

        elif self.quantVidas == 2:
            tela.blit(vidaJogador, (self.x, self.y))
            tela.blit(vidaJogador, (self.x - 50, self.y))

        elif self.quantVidas == 1:
            tela.blit(vidaJogador, (self.x, self.y))

    
    def capturaBuffVida(self):
        if self.quantVidas < 3:
            self.quantVidas += 1

    
    def capturaBuffBonus(self):
        tela.blit(bonusJogador, (30,70))
        tela.blit(textoFormatadoBuffs, (70,70))


# Variaveis que utilizam as classes

buffzinho = Buffs()
navezinha = Nave()
jogador = VidaPersonagem()

# Variaveis auxiliares dos buffs

contador = 0
contEstrela = 0
desceu = False
coracaoDescendo = False
armaDescendo = False
estrelaDescendo = False
pegouBuffEstrela = False


mensagemBuffs = "2x"
textoFormatadoBuffs = fonteTextoGame.render(mensagemBuffs, False, (255,255,255))
while True:
    buffzinho.ajuste()
    relogio.tick(60)

    # Mensagem dos pontos
    mensagemPontos = "Pontos: "
    textoFormatadoPontos = fonteTextoGame.render(mensagemPontos, False, (255,255,255))

    tela.blit(imagemFundo, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    # Funcionamento das teclas para mover a nave
    if pygame.key.get_pressed()[K_LEFT]:
        navezinha.andarEsquerda()
    
    elif pygame.key.get_pressed()[K_RIGHT]:
        navezinha.andarDireita()

    
    
    navezinha.aparecer()
    jogador.vidasJogador()

    # Condições para o caimento dos buffs

    if contador >= 500 and contador <= 800 and not desceu:
        buffzinho.armaAparecer()
        buffzinho.descerBuffs()
        armaDescendo = True

    elif contador >= 1000 and contador <= 1300 and not desceu:
        buffzinho.coracaoAparecer()
        buffzinho.descerBuffs()
        armaDescendo = False
        coracaoDescendo = True

    elif contador >= 1600 and contador <= 1900 and not desceu:
        buffzinho.bonusAparecer()
        buffzinho.descerBuffs()
        coracaoDescendo = False
        estrelaDescendo = True

    elif contador >= 2500:
        contador = 0

    
    if colisao(buffzinho, navezinha):
        buffzinho.x = out_screen


    buffzinho.ajuste()
    desceu = buffzinho.buffDesceu()
    
    # Condição de colisão
    if colisao(buffzinho, navezinha):
        buffzinho.y = out_screen
        desceu = True

        if coracaoDescendo:
            jogador.capturaBuffVida()

        elif estrelaDescendo:
            pegouBuffEstrela = True

    
    # Condição de duração do buff do bonus
    if pegouBuffEstrela:
        
        if contEstrela <= 300:
            jogador.capturaBuffBonus()

        else:
            contEstrela = 0
            pegouBuffEstrela = False

        contEstrela += 1
        
    contador += 1
    tela.blit(textoFormatadoPontos, (30, 30))
    pygame.display.update()