import random
from PPlay.window import Window
from PPlay.sprite import Sprite

DT_MAXIMO = 1/30

FPS_X = 10
FPS_Y = 10
FPS_TAMANHO = 20
FPS_COR = (255, 255, 0)

FONTE_PASTA = 'sprites/ui/font'
FONTE_SIMBOLOS = {':': 'colon', ',': 'comma', '-': 'dash', '!': 'exclaim',
                  '.': 'period', '+': 'plus', '?': 'question'}
FONTE_ESPACAMENTO = 4

AVISO_TEXTO = 'APERTE ESPACO PARA SACAR'
AVISO_MARGEM_SUPERIOR = 30
AVISO_PISCA = 0.5

LARGURA = 1200
ALTURA = 800

ESQUERDA = -1
DIREITA = 1

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
TECLA_SAQUE = 'SPACE'
TECLA_FECHAR = 'ESC'

ESPERANDO = 'esperando'
JOGANDO = 'jogando'


def centraliza(sprite):
    sprite.set_position(LARGURA/2 - sprite.width/2, ALTURA/2 - sprite.height/2)


class Quadra:
    def __init__(self):
        self.linha = Sprite(LINHA_CENTRAL_PNG)
        centraliza(self.linha)

    def desenha(self):
        self.linha.draw()


def caminho_da_letra(letra):
    nome = FONTE_SIMBOLOS.get(letra, letra)
    return f'{FONTE_PASTA}/char_{nome}.png'


class TextoSprite:
    def __init__(self, texto):
        texto = texto.upper()
        self.letras = {}
        for i, letra in enumerate(texto):
            if letra != ' ':
                self.letras[i] = Sprite(caminho_da_letra(letra))

        primeira = next(iter(self.letras.values()))
        self.passo = primeira.width + FONTE_ESPACAMENTO
        self.largura = len(texto) * self.passo - FONTE_ESPACAMENTO

    def set_position(self, x, y):
        for i, letra in self.letras.items():
            letra.set_position(x + i * self.passo, y)

    def desenha(self):
        for letra in self.letras.values():
            letra.draw()


class Aviso:
    def __init__(self):
        self.texto = TextoSprite(AVISO_TEXTO)
        self.texto.set_position(LARGURA/2 - self.texto.largura/2, AVISO_MARGEM_SUPERIOR)
        self.tempo = 0

    def atualiza(self, dt):
        self.tempo = (self.tempo + dt) % (2 * AVISO_PISCA)

    def desenha(self):
        if self.tempo < AVISO_PISCA:
            self.texto.desenha()


class Controle:
    def __init__(self, teclado):
        self.teclado = teclado

    def sacar(self):
        return self.teclado.key_down(TECLA_SAQUE)

    def fechar(self):
        return self.teclado.key_pressed(TECLA_FECHAR)

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
        self.velocidade = VELOCIDADE_INICIAL
        self.dir_x = random.choice([ESQUERDA, DIREITA])
        self.dir_y = random.choice([-1, 1])
        self.centralizar(self.dir_x)

    def centralizar(self, dir_x):
        centraliza(self.sprite)
        self.velocidade = VELOCIDADE_INICIAL
        self.dir_x = dir_x
        self.dir_y = random.choice([-1, 1])

    def mover(self, dt):
        self.sprite.x += self.velocidade * self.dir_x * dt
        self.sprite.y += self.velocidade * self.dir_y * dt

    def aumenta_velocidade(self):
        self.velocidade = min(self.velocidade + AUMENTO_POR_BATIDA, VELOCIDADE_MAXIMA)

    def quica(self):
        if self.sprite.y <= 0:
            self.dir_y = 1
            self.aumenta_velocidade()
        if self.sprite.y + self.sprite.height >= ALTURA:
            self.dir_y = -1
            self.aumenta_velocidade()

    def rebate(self, raquete):
        if self.sprite.collided(raquete.sprite) and self.dir_x == raquete.lado:
            self.dir_x = -raquete.lado
            self.aumenta_velocidade()

    def saida(self):
        if self.sprite.x <= 0:
            return ESQUERDA
        if self.sprite.x + self.sprite.width >= LARGURA:
            return DIREITA
        return None

    def desenha(self):
        self.sprite.draw()


class Raquete:
    def __init__(self, raquete_png, lado):
        self.sprite = Sprite(raquete_png)
        self.lado = lado

        if lado == ESQUERDA:
            x = MARGEM_RAQUETE
        else:
            x = LARGURA - MARGEM_RAQUETE - self.sprite.width

        self.sprite.set_position(x, ALTURA/2 - self.sprite.height/2)

    def mover(self, direcao, dt):
        self.sprite.y += VELOCIDADE_RAQUETE * direcao * dt
        self.sprite.y = max(0, min(self.sprite.y, ALTURA - self.sprite.height))

    def desenha(self):
        self.sprite.draw()


class Jogador:
    def __init__(self, raquete_png, teclas, lado):
        self.raquete = Raquete(raquete_png, lado)
        self.teclas = teclas
        self.lado = lado
        self.pontos = 0

    def mover(self, controle, dt):
        self.raquete.mover(controle.direcao(self.teclas), dt)

    def marca_ponto(self):
        self.pontos += 1

    def desenha(self):
        self.raquete.desenha()


class Partida:
    def __init__(self, controle):
        self.controle = controle
        self.quadra = Quadra()
        self.bola = Bola()
        self.jogadores = {
            ESQUERDA: Jogador(RAQUETE_P1_PNG, TECLAS_P1, ESQUERDA),
            DIREITA: Jogador(RAQUETE_P2_PNG, TECLAS_P2, DIREITA),
        }
        self.estado = ESPERANDO

    def atualiza(self, dt):
        for jogador in self.jogadores.values():
            jogador.mover(self.controle, dt)

        if self.estado == ESPERANDO:
            self.espera_saque()
        elif self.estado == JOGANDO:
            self.joga(dt)

    def esperando_saque(self):
        return self.estado == ESPERANDO

    def espera_saque(self):
        if self.controle.sacar():
            self.estado = JOGANDO

    def joga(self, dt):
        self.bola.mover(dt)
        self.bola.quica()
        for jogador in self.jogadores.values():
            self.bola.rebate(jogador.raquete)
        self.confere_gol()

    def confere_gol(self):
        lado = self.bola.saida()
        if lado is None:
            return
        self.adversario_de(lado).marca_ponto()
        self.bola.centralizar(self.direcao_do_saque(lado))
        self.estado = ESPERANDO

    def adversario_de(self, lado):
        return self.jogadores[-lado]

    @staticmethod
    def direcao_do_saque(lado_do_gol):
        return lado_do_gol

    def desenha(self):
        self.quadra.desenha()
        for jogador in self.jogadores.values():
            jogador.desenha()
        self.bola.desenha()


class Pong:
    def __init__(self):
        self.janela = Window(LARGURA, ALTURA, "Pong")
        self.controle = Controle(self.janela.keyboard)
        self.partida = Partida(self.controle)
        self.aviso = Aviso()

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
            dt = self.delta_time()
            self.partida.desenha()
            if self.partida.esperando_saque():
                self.aviso.atualiza(dt)
                self.aviso.desenha()
            self.partida.atualiza(dt)
            self.desenha_fps()
            self.janela.update()


Pong().run()
