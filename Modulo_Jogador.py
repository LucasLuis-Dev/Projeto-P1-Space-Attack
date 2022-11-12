import pygame

class Jogador():
    def __init__(self):
        self.quantVidas = 3
        self.pontuacao = 0
        self.buffsColetados = []
        self.tempoBuffEstrela = 500
        self.tempoBuffArmamento = 500
        self.imagemVidas = pygame.image.load('./assets/VidaJogador.png')
        self.imagemVidasPerdidas = pygame.image.load('./assets/VidaPerdidaJogador.png')
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
            nave.colisao = [objeto.x, objeto.y]
            objeto.x = -110
            nave.naveAtingida = True
            
            if self.quantVidas > 0:
                self.quantVidas -= 1
         

    def colisaoDisparoJogador(self, disparoJogador, objeto):
        """
            Verifica se o  disparo efetuado pelo jogador colidiu com algum asteroide ou nave inimiga
        """
        if objeto.explosao == False and objeto.y > 5:
            if disparoJogador.x + disparoJogador.largura > objeto.x and disparoJogador.x < objeto.x + objeto.largura and disparoJogador.y + disparoJogador.altura > objeto.y and disparoJogador.y < objeto.y + objeto.altura:
                

                # Se o jogador estiver com o buff de Armamento o seu disparo recebe um bonus de destruição de itens na tela
                if disparoJogador.coletouBuffArmamento:
                    pass

                else:
                    disparoJogador.x = -110
                    disparoJogador.y = -10

                # Se o disparo do jogador colidir com  a nave inimiga ele receberá uma certa quantidade de pontos que pode ser duplicada caso ele estejá com o buff da estrela
                if objeto.nomeObjeto == 'Nave inimiga' and objeto.explosao == False:
                    if self.buffsColetados:
                        if self.buffsColetados[-1] == 'estrela' and self.tempoBuffEstrela > 0:
                            self.pontuacao += 100
                        else:
                            self.pontuacao += 50
                    else:
                        self.pontuacao += 50

                            
                # Se o disparo do jogador colidir com algum asteroide ele receberá uma certa quantidade de pontos que pode ser duplicada caso ele estejá com o buff da estrela
                elif objeto.nomeObjeto == 'Asteroide':
                    if disparoJogador.teclaApertada and objeto.explosao == False:
                        if self.buffsColetados:
                            if self.buffsColetados[-1] == 'estrela' and self.tempoBuffEstrela > 0:
                                self.pontuacao += 50
                            else:
                                self.pontuacao += 25
                        else:
                            self.pontuacao += 25

                objeto.explosao = True


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
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X - 100, self.posicaoVidas_y))

        elif self.quantVidas == 1:
            tela.blit(self.imagemVidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X - 100, self.posicaoVidas_y))

        elif self.quantVidas == 0:
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X, self.posicaoVidas_y))
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X - 50, self.posicaoVidas_y))
            tela.blit(self.imagemVidasPerdidas, (self.posicaoVidas_X - 100, self.posicaoVidas_y))

    
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
        tela.blit(textoFormatadoPontos, (120, 410))


    def recomecarJogo(self, nave):
        """
            Reseta os atributos para recomeçar o jogo
        """
        self.quantVidas = 3
        self.pontuacao = 0
        self.buffsColetados.clear()
        
        nave.tempoExplosao = 40
        nave.naveAtingida = False
        nave.tempoDanos = 30



