import pygame

class jogador():
    def __init__(self):
        self.quantVidas = 3
        self.pontuacao = 0
        self.buffsColetados = []
        self.tempoBuffEstrela = 500
        self.tempoBuffArmamento = 500
        self.imagemVidas = pygame.image.load('./assets/VidaJogador.png')
        self.imagemBonus = pygame.image.load("./assets/BuffPontos.png")
        self.posicaoVidas_X = 530
        self.posicaoVidas_y = 30
        
    # METODOS DA CLASSE

    def mostrarPontos(self, tela):
        """
            Mostra a quantidade de pontos do jogador
        """
        fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)
        mensagemPontos = f"Pontos: {self.pontuacao}"
        textoFormatadoPontos = fonteTextoGame.render(mensagemPontos, False, (255,255,255))
        tela.blit(textoFormatadoPontos, (30, 30))


    def colisaoBuff(self, nave, buffs, nomeObjeto, player, tela):
        """
            Verifica se o jogador colidiu com algum buff para que possa ser beneficiado pelo mesmo
        """
        if nave.x + nave.largura > buffs.x and nave.x < buffs.x + buffs.largura and nave.y + nave.altura > buffs.y and nave.y < buffs.y + buffs.altura:
            buffs.x = -110

            if nomeObjeto == "coracao":
                if self.quantVidas < 3:
                    self.quantVidas += 1
                    self.buffsColetados.append(nomeObjeto)

            elif nomeObjeto == "estrela":
                self.tempoBuffEstrela = 500
                self.buffsColetados.append(nomeObjeto)

            
            elif nomeObjeto == "armamento":
                self.tempoBuffArmamento = 500
                self.buffsColetados.append(nomeObjeto)
            

    def colisaoNaveJogador(self, nave, objeto):
        """
            Verifica se o jogador colidiu com algum asteroide ou disparo inimigo e penaliza o mesmo
        """

        if nave.x + nave.largura > objeto.x and nave.x < objeto.x + objeto.largura and nave.y + nave.altura > objeto.y and nave.y < objeto.y + objeto.altura:
            objeto.x = -110
            if self.quantVidas > 0:
                self.quantVidas -= 1
         


    def colisaoDisparoJogador(self, disparoJogador, objeto):
        """
            Verifica se o  disparo efetuado pelo jogador colidiu com algum asteroide ou nave inimiga
        """

        if disparoJogador.x + disparoJogador.largura > objeto.x and disparoJogador.x < objeto.x + objeto.largura and disparoJogador.y + disparoJogador.altura > objeto.y and disparoJogador.y < objeto.y + objeto.altura:
            objeto.y = -120

            # Se o jogador estiver com o buff de Armamento o seu disparo recebe um bonus de destruição de itens na tela
            if disparoJogador.coletouBuffArmamento:
                pass

            else:
                disparoJogador.x = -110
                disparoJogador.y = -10

            # Se o disparo do jogador colidir com  a nave inimiga ele receberá uma certa quantidade de pontos que pode ser duplicada caso ele estejá com o buff da estrela
            if objeto.nomeObjeto == 'Nave inimiga':

                if self.buffsColetados:
                    if self.buffsColetados[-1] == 'estrela' and self.tempoBuffEstrela > 0:
                        self.pontuacao += 100
                    else:
                        self.pontuacao += 50
                else:
                    self.pontuacao += 50

                        
            # Se o disparo do jogador colidir com algum asteroide ele receberá uma certa quantidade de pontos que pode ser duplicada caso ele estejá com o buff da estrela
            elif objeto.nomeObjeto == 'Asteroide':
                if disparoJogador.teclaApertada:
                    if self.buffsColetados:
                        if self.buffsColetados[-1] == 'estrela' and self.tempoBuffEstrela > 0:
                            self.pontuacao += 50
                        else:
                            self.pontuacao += 25
                    else:
                        self.pontuacao += 25


    def buffEstrela(self):
        """
            Verifica o tempo em que o jogador passará buffado com a estrela se esgotou ou não
        """
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
        """
            Mostra ao jogador que ele está buffado com a estrela
        """
        fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)
        mensagemBuffs = "2x"
        textoFormatadoBuffs = fonteTextoGame.render(mensagemBuffs, False, (255,255,255))
        tela.blit(self.imagemBonus, (30,70))
        tela.blit(textoFormatadoBuffs, (70,70))


    def buffArmamento(self):
        """
            Verifica o tempo em que o jogador passará buffado com o armamento se esgotou ou não
        """
        if len(self.buffsColetados) > 0:
            if self.buffsColetados[-1] == 'armamento':
                if self.tempoBuffArmamento != 0:
                    self.tempoBuffArmamento -= 1
                    return True
                else:
                    return False
        else:
            pass
    

    def vidasJogador(self, tela):
        """
            Mostra a quantidade de vidas que o jogador possui
        """
        if self.quantVidas == 3:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 100, self.posicaoVidas_y))

        elif self.quantVidas == 2:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))

        elif self.quantVidas == 1:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))

    
    def jogadorPerdeu(self):
        """
            Verifica se o jogador perdeu o jogo ou não
        """
        if self.quantVidas == 0:
            return True


    def mostrarPontuacaoFinal(self,tela):
        """
            Mostra a quantidade de pontos do jogador quando ele perde o jogo
        """
        fonteTextoGame = pygame.font.SysFont('arial', 30 , True, False)
        mensagemPontos = f"Pontuação alcançada: {self.pontuacao}"
        textoFormatadoPontos = fonteTextoGame.render(mensagemPontos, False, (255,255,255))
        tela.blit(textoFormatadoPontos, (120, 310))


    def recomecarJogo(self):
        """
            Reseta os atributos para recomeçar o jogo
        """
        self.quantVidas = 3
        self.pontuacao = 0
        self.buffsColetados.clear()



class Nave():
    def __init__(self):
        self.imagem = pygame.image.load("./assets/NavePixel.png")
        self.mask = pygame.mask.from_surface(self.imagem)
        self.x = 250
        self.y = 710
        self.altura = self.imagem.get_height()
        self.largura = self.imagem.get_width()


    # METODOS DA CLASSE

    def mostrarNave(self, tela):
        """
            Mostra a nave controlada pelo jogador na tela
        """
        tela.blit(self.imagem, (self.x, self.y ))


    def andarEsquerda(self):
        """
            Movimenta a nave para a esquerda
        """
        if self.x > 0:
            self.x -= 7


    def andarDireita(self):
        """
            Movimenta a nave para a direita
        """
        if self.x <= 510:
            self.x += 7



class DisparoNave():
    def __init__(self):
        self.imagemDisparo = pygame.image.load('./assets/DisparoNave.png')
        self.imagemDisparoBuffado = pygame.image.load('./assets/DisparoNaveBuffada.png')
        self.somDisparo = pygame.mixer.Sound('./Music/SomDisparo.wav')
        self.tocarSom = True
        self.teclaApertada = False
        self.coletouBuffArmamento = False
        self.x = 283 
        self.y = 680 
        self.velocidade = 7
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


    def disparar(self, tela):
        """
            Mostra o disparo efetuado pelo jogador sem estar buffado, e reproduz o som do disparo
        """
        if self.teclaApertada:
            self.coletouBuffArmamento = False
            self.largura = self.imagemDisparo.get_width()
            self.altura = self.imagemDisparo.get_height()
            tela.blit(self.imagemDisparo, (self.x, self.y))
            if self.tocarSom:
                self.somDisparo.play()
                self.tocarSom = False


    def dispararComBuff(self, tela):
        """
            Mostra o disparo efetuado pelo jogador estando buffado, e reproduz o som do disparo
        """
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
            self.y = 680
            self.teclaApertada = False
            self.tocarSom = True


    def ajusteTrajetoria(self, nave):
        """
            Ajusta a trajetoria do disparo para que ela não se mova junto com a nave do jogador
        """
        if self.y != 680:
            pass
        else:
            self.x = nave.x + 33


    def ajusteTrajetoriaComBuff(self, nave):
        """
            Ajusta a trajetoria do disparo buffado para que ela não se mova junto com a nave do jogador
        """
        if self.y != 680:
            pass
        else:
            self.x = nave.x + 23