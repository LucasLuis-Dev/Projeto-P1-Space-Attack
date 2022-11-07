import pygame
from random import randint

class Asteroides():
    def __init__(self):
        self.nomeObjeto = 'Asteroide'
        self.imagem = pygame.image.load('./assets/AsteroidePixel.png')
        self.imagemExplosao = pygame.image.load("./assets/ExplosãoAsteroide.png")
        self.somExplosao = pygame.mixer.Sound('./Music/SomExplosaoAsteroide.wav')
        self.tocarSomExplosao = True
        self.explosao = False
        self.tempoExplosao = 40
        self.x = randint(0,500)
        self.y = -40
        self.altura = self.imagem.get_height()
        self.largura = self.imagem.get_width()

    # METODOS DA CLASSE

    def aparecerAsteroide(self, tela):
        """
            Mostra os asteroides na tela verficando se já percorreram todo o percurso e também mostra a sua animação de explosão
        """
        if self.explosao == False:
            if self.y < 830:
                tela.blit(self.imagem, (self.x, self.y))
                self.y += 4

            else:
                self.y = -40
                self.x = randint(0,500)

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
                self.tocarSomExplosao = True


    def recomecarJogo(self):
        """
            Reseta os atributos para recomeçar o jogo
        """
        self.x = randint(0,500)
        self.y = -40

    
    


