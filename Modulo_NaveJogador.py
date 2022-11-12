import pygame
from random import randint

class Nave():
    def __init__(self):
        self.imagem = pygame.image.load("./assets/NavePixel.png")
        self.imagemExplosao = pygame.image.load("./assets/ExplosãoNave.png")
        self.imagemDanos = pygame.image.load("./assets/DanosNaveJogador.png")
        self.somExplosao = pygame.mixer.Sound('./Music/SomMorteJogador.wav')
        self.somDanos = pygame.mixer.Sound('./Music/SomExplosaoAsteroide.wav')
        self.colisao = []
        self.naveAtingida = False
        self.tocarSomDanos = True
        self.tocarSomExplosao = True
        self.tempoExplosao = 40
        self.tempoDanos = 30
        self.x = 250
        self.y = 670
        self.altura = self.imagem.get_height()
        self.largura = self.imagem.get_width()


    # METODOS DA CLASSE

    def mostrarNave(self, tela, player):
        """
            Mostra a nave controlada pelo jogador na tela
        """
        if player.quantVidas != 0:
            tela.blit(self.imagem, (self.x, self.y ))

        else:
            tela.blit(self.imagemExplosao, (self.x, self.y))


    def andarEsquerda(self, player):
        """
            Movimenta a nave para a esquerda
        """
        if player.quantVidas != 0:
            if self.x > 0:
                self.x -= 7


    def andarDireita(self,player):
        """
            Movimenta a nave para a direita
        """
        if player.quantVidas != 0:
            if self.x <= 510:
                self.x += 7

    def explosaoNave(self):
        '''
            Reproduz o som de explosão da nave e contabiliza o tempo da sua animação de destruição
        '''
        if self.tempoExplosao != 0:
            if self.tocarSomExplosao:
                self.somExplosao.play()
                self.tocarSomExplosao = False
            self.tempoExplosao -= 1
            return False
        
        else:
            self.tocarSomExplosao = True
            return True

    
    def naveDanificada(self, tela):
        '''
            Exibi a animação de dano quando a nave do jogador é atingida
        '''
        if self.naveAtingida and self.tempoExplosao == 40:
            posicaoAcerto = randint(self.x, self.x + 55)
            if self.tempoDanos != 0:
                tela.blit(self.imagemDanos, (posicaoAcerto, self.colisao[1] + 35))
                self.tempoDanos -= 1
                if self.tocarSomDanos:
                    self.somDanos.play()
                    self.tocarSomDanos = False

            else:
                self.naveAtingida = False
                self.tocarSomDanos = True
                self.tempoDanos = 30
                self.colisao.clear()


class DisparoNave():
    def __init__(self):
        self.imagemDisparo = pygame.image.load('./assets/DisparoNave.png')
        self.imagemDisparoBuffado = pygame.image.load('./assets/DisparoNaveBuffada.png')
        self.somDisparo = pygame.mixer.Sound('./Music/SomDisparo.wav')
        self.tocarSom = True
        self.teclaApertada = False
        self.coletouBuffArmamento = False
        self.x = 283 
        self.y = 630
        self.velocidade = 9
        self.largura = self.imagemDisparo.get_width()
        self.altura = self.imagemDisparo.get_height()

    # METODOS DA CLASSE

    def verificaTeclaApertada(self):
        """
            Verifica se a tecla de disparo foi pressionada
        """
        self.teclaApertada = True
        

    def apertouTecla(self):
        """
            Verifica se a tecla de disparo foi apertada retornando sua condição para um IF
        """
        if self.teclaApertada:
            return True

        else:
            return False


    def trajetoria(self):
        """
            Faz o disparo feito pelo jogador percorrer a tela de baixo para cima
        """
        if self.teclaApertada:
            self.y = self.y - self.velocidade


    def disparar(self, tela, player):
        """
            Mostra o disparo efetuado pelo jogador sem estar buffado, e reproduz o som do disparo
        """
        if player.quantVidas > 0:
            if self.teclaApertada:
                self.coletouBuffArmamento = False
                self.largura = self.imagemDisparo.get_width()
                self.altura = self.imagemDisparo.get_height()
                tela.blit(self.imagemDisparo, (self.x, self.y))
                if self.tocarSom:
                    self.somDisparo.play()
                    self.tocarSom = False


    def dispararComBuff(self, tela, player):
        """
            Mostra o disparo efetuado pelo jogador estando buffado, e reproduz o som do disparo
        """
        if player.quantVidas > 0:
            if self.teclaApertada:
                self.coletouBuffArmamento = True
                self.largura = self.imagemDisparoBuffado.get_width()
                self.altura = self.imagemDisparoBuffado.get_height()
                tela.blit(self.imagemDisparoBuffado, (self.x - 10, self.y - 95))
                if self.tocarSom:
                    self.somDisparo.play()
                    self.tocarSom = False
            

    def ajusteDisparo(self):
        """
           Ajusta a posição do disparo para que outro possa ser efetuado
        """
        if self.y < 0:
            self.y = 630
            self.teclaApertada = False
            self.tocarSom = True


    def ajusteTrajetoria(self, nave):
        """
            Ajusta a trajetoria do disparo para que ela não se mova junto com a nave do jogador
        """
        if self.y != 630:
            pass
        else:
            self.x = nave.x + 33


    def ajusteTrajetoriaComBuff(self, nave):
        """
            Ajusta a trajetoria do disparo buffado para que ela não se mova junto com a nave do jogador
        """
        if self.y != 630:
            pass
        else:
            self.x = nave.x + 23