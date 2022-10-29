import pygame
from random import randint

class Asteroides():
    def __init__(self):
        self.nomeObjeto = 'Asteroide'
        self.imagem = pygame.image.load('./assets/AsteroidePixel.png')
        self.x = randint(0,500)
        self.y = -40
        self.altura = self.imagem.get_height()
        self.largura = self.imagem.get_width()

    # METODOS DA CLASSE

    def aparecerAsteroide(self, tela):
        """
            Mostra os asteroides na tela verficando se já percorreram todo o percurso
        """
        if self.y < 850:
            tela.blit(self.imagem, (self.x, self.y))
            self.y += 3

        else:
            self.y = -40
            self.x = randint(0,500)

    def recomecarJogo(self):
        """
            Reseta os atributos para recomeçar o jogo
        """
        self.x = randint(0,500)
        self.y = -40


