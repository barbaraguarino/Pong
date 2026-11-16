# Pong

Implementação do clássico jogo **Pong** em **Python**, usando a biblioteca **[PPlay](https://www2.ic.uff.br/pplay/)** (uma abstração simplificada construída sobre o **Pygame**) e escrita com **Programação Orientada a Objetos (POO)**.

Este é um projeto de estudo: todo o código é escrito pela autora, como preparação para a prova.

> **Status:** em desenvolvimento. Os sprites e os sons já estão no repositório; o código-fonte está sendo escrito aos poucos (veja o [Roteiro](#roteiro)).

## Funcionalidades previstas

- **Menu gráfico** com os botões Jogar, Dificuldade, Ranking e Sair
- **1 jogador** contra o computador (IA que acompanha e prevê a bola)
- **2 jogadores no mesmo teclado**
- **Dificuldade** em 3 níveis (fácil, médio, difícil)
- **Placar** desenhado com sprites, pausa e telas de vitória
- **Bola** que acelera a cada batida, com movimento baseado em *delta time*
- **Ranking em página própria**, no estilo dos fliperamas antigos: o jogador escolhe o nome (iniciais) com o teclado e a pontuação é gravada em arquivo (nome, pontos e data)
- **Música e efeitos sonoros** originais, e efeitos visuais (rastro da bola e impacto)

## Controles

| Ação | Jogador 1 | Jogador 2 |
|---|---|---|
| Subir | `W` | `↑` |
| Descer | `S` | `↓` |

| Tecla | Função |
|---|---|
| `ESPAÇO` | Sacar (no início e depois de cada gol) |
| `ESC` | Fechar o jogo (no futuro: voltar ao menu / pausar) |

## Tecnologias

- Python 3
- [PPlay](https://www2.ic.uff.br/pplay/): biblioteca usada na disciplina, já incluída na pasta `PPlay/`
- [pygame-ce](https://pyga.me/): usado internamente pelo PPlay

## Como instalar e rodar

1. Clone o repositório (ele é público).
2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências (o PPlay usa o `pygame-ce`):
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o jogo:
   ```bash
   python pong.py
   ```

## Estrutura do projeto

```
pong/
├── pong.py       o jogo
├── PPlay/        biblioteca PPlay
├── sprites/
│   ├── game/     quadra, bola, raquetes, dígitos do placar, efeitos
│   └── ui/       avatares, botões, cursor, fonte, títulos, ícones, campo de nome, painéis, logo
├── sounds/
│   ├── music/    músicas em loop e vinhetas (jingles)
│   └── sfx/      efeitos sonoros do jogo e da interface
├── docs/         documentação (arquitetura do código, sprites)
├── CLAUDE.md     regras de trabalho para o Claude
└── LICENSE
```

O código segue a POO, com uma classe para cada parte do jogo. A divisão atual está em [`docs/arquitetura.md`](docs/arquitetura.md), e a descrição dos sprites em [`docs/sprites.md`](docs/sprites.md).

Os sons estão documentados em [`sounds/README.md`](sounds/README.md), com a indicação de quando tocar cada um.

## Fluxo de trabalho (Git Flow)

O projeto segue o **Git Flow**:

| Branch | Uso |
|---|---|
| `main` | Produção: só recebe versões prontas |
| `develop` | Integração das funcionalidades |
| `feature/*` | Uma branch por funcionalidade, criada a partir de `develop` (ex.: `feature/movimento-das-raquetes`) |
| `release/*` | Preparação de uma versão |
| `hotfix/*` | Correções urgentes a partir de `main` |

Cada funcionalidade tem uma **issue** no GitHub ligada à sua branch, e os commits são pequenos, com uma única mudança cada.

## Roteiro

1. **Pong base:** janela, bola, colisões, barras, delta time, placar e reinício com `ESPAÇO`
2. **Dois jogadores** no mesmo teclado
3. **Menu e telas:** menu gráfico, escolha de 1 ou 2 jogadores, dificuldade, `ESC` e pausa
4. **Inteligência:** o computador segue a bola, depois prevê onde ela chega, com dificuldade ajustável
5. **Fim de jogo e ranking:** tela de vitória e ranking estilo fliperama em arquivo
6. **Sons e efeitos:** músicas, efeitos sonoros, rastro da bola e impacto
7. **Acabamento:** revisão e documentação

## Licença

Projeto público, sob a licença **MIT**. Veja o arquivo [`LICENSE`](LICENSE).
