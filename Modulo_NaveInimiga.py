import pygame

class NaveInimiga():
    def __init__(self):
        self.nomeObjeto = 'Nave inimiga'
        self.imagemNave = pygame.image.load('./assets/NaveInimiga.png')
        self.imagemExplosao = pygame.image.load("./assets/ExplosãoNave.png")
        self.somExplosao = pygame.mixer.Sound('./Music/SomExplosaoNaveInimiga.wav')
        self.tocarSomExplosao = True
        self.explosao = False
        self.x = 250
        self.y = -10
        self.tempoAparecimento = 500
        self.tempoExplosao = 40
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
        self.tempoExplosao = 40


    def tempoSurgimento(self):
        """
            Cálcula o tempo certo para a nave inimiga surgir na tela
        """
        if self.tempoAparecimento != 0:
            self.tempoAparecimento -= 1
            return False

        else:
            return True


    def aparecerNaveInimiga(self,tela, nave):
        """
            Mostra a nave inimiga na tela e também mostra a sua animação de explosao caso a mesma seja atingida
        """
        # se a nave inimiga estiver acima da ela este if a faz descer dando uma animação a mais ao jogo
        if self.explosao == False:
            if self.y < 64:
                self.y += 2
            
            tela.blit(self.imagemNave, (self.x, self.y))

        else:
            if self.tempoExplosao != 0:
                tela.blit(self.imagemExplosao, (self.x, self.y))
                self.tempoExplosao -= 1
                if self.tocarSomExplosao:
                    self.somExplosao.play()
                    self.tocarSomExplosao = False

            else:
                self.explosao = False
                self.tempoExplosao = 40
                self.y = -120
                self.x = nave.x
                self.tocarSomExplosao = True


    def posicaoNave(self, naveJogador):
        """
            Fornece a posição da Nave do jogador possibilitando o espelhamento
        """
        if self.explosao == False:
            self.x = naveJogador.x
    

class disparoNaveInimiga():
    def __init__(self, naveInimiga):
        self.ImagemDisparo = pygame.image.load('./assets/DisparoNaveInimiga.png')
        self.velocidade = 10
        self.y = 125
        self.x = naveInimiga.x + 15
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
        if naveInimiga.y == 64 and naveInimiga.explosao == False:
            if self.tempoDisparo != 0:
                self.tempoDisparo -= 1
                self.x = naveInimiga.x + 15
                return False

            else:
                return True

        elif self.y > 125:
            return True
            
            
    def ajusteDisparo(self):
        """
            Reseta os atributos para possibilitar a nave inimiga disparar novamente
        """
        if self.y > 900:
            self.y = 125
            self.tempoDisparo = 10
            self.tocarSom = True

    
    def ajusteTrajetoria(self, naveInimiga):
        """
            Impossibilita o diparo de se movimentar para os lados quando a nave se movimenta
        """
        if self.y != 125:
            pass
        else:
            self.x = naveInimiga.x + 15


    def recomecarJogo(self, naveInimiga):
        """
            Reseta os atributos da classe para recomeçar o jogo
        """
        self.y = 125
        self.x =  naveInimiga.x + 15
        self.tempoDisparo = 0
        self.tocarSom = True


