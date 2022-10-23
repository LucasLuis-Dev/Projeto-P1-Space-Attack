import pygame

class jogador():
    def __init__(self):
        self.quantVidas = 1
        self.objetosColidiveis = ['Buffs', 'Asteroides']
        self.buffsColetados = []
        self.tempoBuffEstrela = 350
        self.imagemVidas = pygame.image.load('./assets/VidaJogador.png')
        self.imagemBonus = pygame.image.load("./assets/BuffPontos.png")
        self.posicaoVidas_X = 530
        self.posicaoVidas_y = 30
        

    def colisaoBuff(self, nave, objeto, nomeObjeto, player, tela):
        if nave.x + nave.larguraNave > objeto.x and nave.x < objeto.x + objeto.larguraBuffs and nave.y + nave.alturaNave > objeto.y and nave.y < objeto.y + objeto.alturaBuffs:
            objeto.x = -110

            if nomeObjeto == "coracao":
                if self.quantVidas < 3:
                    self.quantVidas += 1
                    self.buffsColetados.append(nomeObjeto)

            elif nomeObjeto == "estrela":
                self.tempoBuffEstrela = 350
                self.buffsColetados.append(nomeObjeto)
                

         
   

    def buffEstrela(self):
        if len(self.buffsColetados) > 0:
            if self.buffsColetados[-1] == 'estrela':
                if self.tempoBuffEstrela != 0:
                    self.tempoBuffEstrela -= 1
                    return True

                else:
                    return False

        else:
            pass
                

    def mostrarBuffEstrela(self, tela):
        fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)
        mensagemBuffs = "2x"
        textoFormatadoBuffs = fonteTextoGame.render(mensagemBuffs, False, (255,255,255))
        tela.blit(self.imagemBonus, (30,70))
        tela.blit(textoFormatadoBuffs, (70,70))

        

    def vidasJogador(self, tela):
        if self.quantVidas == 3:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 100, self.posicaoVidas_y))

        elif self.quantVidas == 2:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))

        elif self.quantVidas == 1:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))

    
    def capturaBuffVida(self):
        if self.quantVidas < 3:
            self.quantVidas += 1

    
    #def capturaBuffBonus(self):
        #tela.blit(bonusJogador, (30,70))
        #tela.blit(textoFormatadoBuffs, (70,70))



class Nave(jogador):
    def __init__(self):
        self.imagem = pygame.image.load("./assets/NavePixel.png")
        self.x = 250
        self.y = 710
        self.alturaNave = self.imagem.get_height()
        self.larguraNave = self.imagem.get_width()


    def mostrarNave(self, tela):
        tela.blit(self.imagem, (self.x, self.y ))

    def andarEsquerda(self):
        if self.x >= 0:
            self.x -= 10

    def andarDireita(self):
        if self.x <= 500:
            self.x += 10