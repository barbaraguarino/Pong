# Arquitetura do código

O jogo está em `pong.py`. As constantes ficam no topo e as classes vêm depois. Cada classe cuida de uma coisa só.

| Classe | Responsabilidade |
|---|---|
| `Pong` | A janela: o laço principal, o `delta_time` limitado por `DT_MAXIMO`, o FPS, fechar com `ESC` e mostrar o aviso de saque. |
| `Partida` | As regras: o estado (`ESPERANDO`, `JOGANDO` ou `FIM_DA_PARTIDA`), o saque, o gol, quem pontua, o vencedor ao chegar a `PONTOS_PARA_VENCER` e o reinício com `ESPAÇO`. |
| `Jogador` | Raquete, teclas, lado (`ESQUERDA` ou `DIREITA`) e pontos (`marca_ponto`, `zera`). |
| `Raquete` | Move a raquete sem sair da tela. |
| `Bola` | Move, quica no topo e na base, rebate nas raquetes (só elas aceleram a bola) e informa por qual lado saiu (`saida()`). Não sabe nada de jogadores. |
| `Controle` | Lê o teclado: a direção de cada jogador, o saque e fechar. |
| `Quadra` | Desenha a linha central. |
| `TextoSprite` | Escreve um texto com sprites, um por caractere. Por padrão usa as letras de `sprites/ui/font/`; recebe outra função de caminho para os dígitos. |
| `Placar` | Mostra os pontos de cada jogador com os dígitos de `sprites/game/digits/`, um número de cada lado da quadra. |
| `Aviso` | O aviso piscando "APERTE ESPACO PARA SACAR". |
| `AvisoVencedor` | Desenha o heading de quem venceu (`sprites/ui/headings/`). Só desenha; a regra fica na `Partida`. |

## Decisões

- **Lados:** `ESQUERDA = -1` e `DIREITA = 1` seguem o eixo x da tela. Os jogadores ficam num dicionário por lado, então o adversário é `jogadores[-lado]`.
- **Saque:** depois de um gol, a bola volta ao centro com `VELOCIDADE_INICIAL` e sai na direção de quem sofreu o gol (`Partida.direcao_do_saque`).
- **Teclas de um toque:** o saque usa `key_down`, que só vale no quadro em que a tecla foi apertada. O movimento das raquetes usa `key_pressed`, que vale enquanto a tecla está segurada.
- **Delta time:** a bola e as raquetes andam em pixels por segundo. O `dt` é lido uma vez por quadro em `Pong.run()` e limitado a `DT_MAXIMO` (1/30 s). Sem esse limite, o tempo que a abertura do PPlay leva seria contado no 2º quadro e a bola daria um salto.
