import random
from PPlay.window import Window
from PPlay.sprite import Sprite

LARGURA = 1200
ALTURA = 800

VELOCIDADE_INICIAL = 100
AUMENTO_POR_BATIDA = 20
VELOCIDADE_MAXIMA = 400

BOLA_PNG = 'sprites/game/ball/ball.png'
RAQUETE_P1_PNG = 'sprites/game/paddles/paddle_p1.png'
RAQUETE_P2_PNG = 'sprites/game/paddles/paddle_p2.png'
LINHA_CENTRAL_PNG = 'sprites/game/court/center_line.png'

MARGEM_RAQUETE = 40
VELOCIDADE_RAQUETE = 400

TECLAS_P1 = ('w', 's')
TECLAS_P2 = ('up', 'down')

class Quadra:
    def __init__(self):
        self.linha = Sprite(LINHA_CENTRAL_PNG)
        self.linha.set_position(LARGURA/2 - self.linha.width/2, ALTURA/2 - self.linha.height/2)

    def desenha(self):
        self.linha.draw()

class Controle:
    def __init__(self, teclado):
        self.teclado = teclado

    def fechar(self):
        return self.teclado.key_pressed("ESC")

    def direcao(self, teclas):
        cima, baixo = teclas
        if self.teclado.key_pressed(cima):
            return -1
        if self.teclado.key_pressed(baixo):
            return 1
        return 0

class Bola:

    def __init__(self):
        self.sprite = Sprite(BOLA_PNG)
        self.sprite.set_position(LARGURA/2 - self.sprite.width/2, ALTURA/2 - self.sprite.height/2)

        self.velocidade = VELOCIDADE_INICIAL
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])

    def mover(self):
        self.sprite.move_x(self.velocidade * self.dir_x)
        self.sprite.move_y(self.velocidade * self.dir_y)

    def aumenta_velocidade(self):
        self.velocidade += AUMENTO_POR_BATIDA
        if self.velocidade > VELOCIDADE_MAXIMA:
            self.velocidade = VELOCIDADE_MAXIMA

    def quica(self):
        if self.sprite.x <= 0:
            self.dir_x = 1
            self.aumenta_velocidade()
        if self.sprite.x + self.sprite.width >= LARGURA:
            self.dir_x = -1
            self.aumenta_velocidade()

        if self.sprite.y <= 0:
            self.dir_y = 1
            self.aumenta_velocidade()
        if self.sprite.y + self.sprite.height >= ALTURA:
            self.dir_y = -1
            self.aumenta_velocidade()

    def rebate(self, raquete):
        if self.sprite.collided(raquete.sprite) and self.dir_x != raquete.lado:
            self.dir_x = raquete.lado
            self.aumenta_velocidade()


    def desenha(self):
        self.sprite.draw()

class Raquete:
    def __init__(self, sprite, lado):
        self.sprite = Sprite(sprite)
        self.lado = lado

        if lado == 1:
            x = MARGEM_RAQUETE
        else:
            x = LARGURA - MARGEM_RAQUETE - self.sprite.width

        self.sprite.set_position(x, ALTURA/2 - self.sprite.height/2)

    def mover(self, direcao):
        self.sprite.move_y(VELOCIDADE_RAQUETE * direcao)
        if self.sprite.y < 0:
            self.sprite.y = 0
        if self.sprite.y + self.sprite.height > ALTURA:
            self.sprite.y = ALTURA - self.sprite.height

    def desenha(self):
        self.sprite.draw()

class Pong:
    def __init__(self):
        self.janela = Window(LARGURA, ALTURA, "Pong")
        self.quadra = Quadra()
        self.bola = Bola()
        self.raquete_1 = Raquete(RAQUETE_P1_PNG, 1)
        self.raquete_2 = Raquete(RAQUETE_P2_PNG, -1)
        self.controle = Controle(self.janela.keyboard)

    def fechar(self):
        if self.controle.fechar():
            self.janela.close()

    def run(self):
        while True:
            self.fechar()

            self.quadra.desenha()
            self.raquete_1.desenha()
            self.raquete_2.desenha()
            self.bola.desenha()

            self.bola.mover()
            self.raquete_1.mover(self.controle.direcao(TECLAS_P1))
            self.raquete_2.mover(self.controle.direcao(TECLAS_P2))

            self.bola.quica()
            self.bola.rebate(self.raquete_1)
            self.bola.rebate(self.raquete_2)

            self.janela.update()

Pong().run()