import random
from PPlay.window import Window
from PPlay.sprite import Sprite

LARGURA = 1200
ALTURA = 800

VELOCIDADE_INICIAL = 100
AUMENTO_POR_BATIDA = 20
VELOCIDADE_MAXIMA = 400

BOLA_PNG = 'sprites/game/ball/ball.png'

class Controle:
    def __init__(self, teclado):
        self.teclado = teclado

    def fechar(self):
        return self.teclado.key_pressed("ESC")

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


    def draw(self):
        self.sprite.draw()

class Pong:
    def __init__(self):
        self.janela = Window(LARGURA, ALTURA, "Pong")
        self.bola = Bola()
        self.controle = Controle(self.janela.keyboard)

    def fechar(self):
        if self.controle.fechar():
            self.janela.close()

    def run(self):
        while True:
            self.fechar()
            self.bola.draw()
            self.bola.mover()
            self.bola.quica()
            self.janela.update()

Pong().run()