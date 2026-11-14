from PPlay.window import Window
from PPlay.sprite import Sprite

LARGURA = 1200
ALTURA = 800

class Bola:
    def __init__(self):
        self.bola = Sprite('sprites/game/ball/ball.png')
        self.bola.set_position(LARGURA/2 - self.bola.width/2, ALTURA/2 - self.bola.height/2)

    def draw(self):
        self.bola.draw()

class Pong:
    def __init__(self):
        self.janela = Window(LARGURA, ALTURA, "Pong")
        self.bola = Bola()

    def run(self):
        while True:
            self.bola.draw()

            self.janela.update()

Pong().run()