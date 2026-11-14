from PPlay.window import Window

class Pong:
    def __init__(self):
        self.janela = Window(1200, 800, "Pong")

    def run(self):
        while True:
            self.janela.update()

Pong().run()