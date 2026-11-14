import random
from PPlay.window import Window
from PPlay.sprite import Sprite

DT_MAXIMO = 1/30

FPS_X = 10
FPS_Y = 10
FPS_TAMANHO = 20
FPS_COR = (255, 255, 0)

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

    def mover(self, dt):
        self.sprite.x += self.velocidade * self.dir_x * dt
        self.sprite.y += self.velocidade * self.dir_y * dt

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
    def __init__(self, raquete_png, lado):
        self.sprite = Sprite(raquete_png)
        self.lado = lado

        if lado == 1:
            x = MARGEM_RAQUETE
        else:
            x = LARGURA - MARGEM_RAQUETE - self.sprite.width

        self.sprite.set_position(x, ALTURA/2 - self.sprite.height/2)

    def mover(self, direcao, dt):
        self.sprite.y += VELOCIDADE_RAQUETE * direcao * dt
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

    def delta_time(self):
        return min(self.janela.delta_time(), DT_MAXIMO)

    def desenha_fps(self):
        fps = int(self.janela.get_fps())
        self.janela.draw_text(f"FPS: {fps}", FPS_X, FPS_Y, FPS_TAMANHO, FPS_COR)

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

            dt = self.delta_time()

            self.bola.mover(dt)
            self.raquete_1.mover(self.controle.direcao(TECLAS_P1), dt)
            self.raquete_2.mover(self.controle.direcao(TECLAS_P2), dt)

            self.bola.quica()
            self.bola.rebate(self.raquete_1)
            self.bola.rebate(self.raquete_2)

            self.desenha_fps()
            self.janela.update()

Pong().run()