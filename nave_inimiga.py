import pygame

class NaveInimiga():
    def __init__(self):
        self.nomeObjeto = 'Nave inimiga'
        self.imagemNave = pygame.image.load('./assets/NaveInimiga.png')
        self.x = 250
        self.y = -10
        self.tempoAparecimento = 500
        self.largura = self.imagemNave.get_width()
        self.altura = self.imagemNave.get_height()

     # METODOS DA CLASSE

    def recomecarJogo(self):
        """
            Reinicia os principais atributos de jogabilidade da Classe
        """
        self.tempoAparecimento = 500
        self.x = 250
        self.y = -10


    def tempoSurgimento(self):
        """
            Cálcula o tempo certo para a nave inimiga surgir na tela
        """
        if self.tempoAparecimento != 0:
            self.tempoAparecimento -= 1
            return False

        else:
            return True


    def aparecerNaveInimiga(self,tela):
        """
            Mostra a nave inimiga na tela 
        """
        # se a nave inimiga estiver acima da ela este if a faz descer dando uma animação a mais ao jogo
        if self.y < 80:
            self.y += 2
            tela.blit(self.imagemNave, (self.x, self.y))

        else:
            tela.blit(self.imagemNave, (self.x, self.y))


    def moverNaveInimigaEsquerda(self):
        """
            Move a nave inimiga para a esquerda
        """
        if self.x > 0:
            self.x -= 5

    def moverNaveInimigaDireita(self):
        """
            Move a nave inimiga para a direita
        """
        if self.x <= 510:
            self.x += 5 


    

class disparoNaveInimiga():
    def __init__(self):
        self.ImagemDisparo = pygame.image.load('./assets/DisparoNaveInimiga.png')
        self.velocidade = 7
        self.y = 125
        self.x = 265
        self.somDisparo = pygame.mixer.Sound('./Music/SomDisparo.wav')
        self.tocarSom = True
        self.tempoDisparo = 0
        self.largura = self.ImagemDisparo.get_width()
        self.altura = self.ImagemDisparo.get_height()

    # METODOS DA CLASSE
    
    def trajetoria(self):
        """
            Faz o disparo percorrer a tela na direção de cima para baixo
        """
        self.y = self.y + self.velocidade


    def disparar(self, tela):
        """
            Mostra o disparo da nave inimiga na tela e também reproduz o som do disparo
        """
        tela.blit(self.ImagemDisparo, (self.x, self.y))
        if self.tocarSom:
            self.somDisparo.play()
            self.tocarSom = False


    def contadorDisparo(self, naveInimiga):
        """
            Cálcula o momento de intervalo entre cada disparo da nave inimiga
        """
        if naveInimiga.y == 80:
            if self.tempoDisparo != 0:
                self.tempoDisparo -= 1
                self.x = naveInimiga.x + 15
                return False

            else:
                return True
            
            
    def ajusteDisparo(self, naveInimiga):
        """
            Reseta os atributos para possibilitar a nave inimiga disparar novamente
        """
        if self.y > 900:
            self.y = 125
            self.tempoDisparo = 30
            self.tocarSom = True

        if naveInimiga.y < 80:
            self.tocarSom = True
            self.y = 125


    def ajusteTrajetoria(self, naveInimiga):
        """
            Impossibilita o diparo de se movimentar para os lados quando a nave se movimenta
        """
        if self.y != 125:
            pass
        else:
            self.x = naveInimiga.x + 15


    def recomecarJogo(self):
        """
            Reseta os atributos da classe para recomeçar o jogo
        """
        self.velocidade = 7
        self.y = 125
        self.x = 265
        self.tempoDisparo = 0
