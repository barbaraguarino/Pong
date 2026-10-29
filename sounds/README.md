# Sons do Pong

Todos os sons são **originais**, sintetizados por código (estilo 8-bit), sem nenhum arquivo baixado da internet. Formato: WAV 44,1 kHz, 16 bits (músicas em estéreo, efeitos em mono), que o Pygame/PPlay toca sem conversão.

Padrão de nomes: `music_*` toca em loop, `jingle_*` toca uma vez, `sfx_*` é efeito sonoro. A divisão `game/` e `ui/` segue a mesma da pasta `sprites/`.

## `music/`

| Arquivo | Tipo | Quando tocar |
|---|---|---|
| `music_menu.wav` | loop (16 s) | Menu principal e telas do menu (1 ou 2 jogadores, Novo jogador, Opções, Ranking) |
| `music_partida.wav` | loop (26 s) | Durante a partida (duas melodias se respondem da esquerda para a direita) |
| `jingle_inicio_partida.wav` | 1 vez (2,5 s) | Antes do primeiro saque |
| `jingle_vitoria.wav` | 1 vez (4,2 s) | Vitória (`text_jogador1_venceu`, `text_jogador2_venceu`) |
| `jingle_derrota.wav` | 1 vez (5,5 s) | Modo 1 jogador: perdeu para o computador / acabaram as vidas (`label_vidas`) |
| `jingle_novo_recorde.wav` | 1 vez (3,6 s) | Novo recorde no ranking (`label_recorde`, `trophy_*`) |

Ao tocar um jingle, pare (ou abaixe) a música que estiver em loop.

## `sfx/game/` — partida

| Arquivo | Quando tocar | Sprite relacionado |
|---|---|---|
| `sfx_raquete.wav` | A bola bate numa raquete | `paddles/*`, `effects/hit_effect_*` |
| `sfx_parede.wav` | A bola bate na parede de cima ou de baixo | `ball/ball` |
| `sfx_saque.wav` | A bola é lançada | `ball/ball`, `effects/ball_trail_*` |
| `sfx_ponto_marcado.wav` | Você (ou o jogador da vez) marca ponto | `digits/*` |
| `sfx_ponto_sofrido.wav` | O adversário marca ponto / no modo 1 jogador, perde uma vida | `digits/*`, `label_vidas` |
| `sfx_contagem.wav` | Cada número da contagem regressiva (3, 2, 1) | `digits/*` |
| `sfx_contagem_vai.wav` | Fim da contagem: "vai!" | — |

### `sfx/ui/` — interface (igual nos dois jogos)

| Arquivo | Quando tocar | Sprite relacionado |
|---|---|---|
| `sfx_navegar.wav` | Cursor muda de botão no menu | `cursor/arrow_up`, `arrow_down` |
| `sfx_confirmar.wav` | Botão confirmado (Jogar, Confirmar, Opções...) | `buttons/btn_*_selected` |
| `sfx_voltar.wav` | Botão Voltar / sair de uma tela | `buttons/btn_voltar` |
| `sfx_digitar.wav` | Letra digitada no campo de nome | `input/input_field_focus`, `caret` |
| `sfx_apagar.wav` | Letra apagada (Backspace) no campo de nome | `input/caret` |
| `sfx_erro.wav` | Ação inválida (ex.: confirmar nome vazio) | `input/input_field` |
| `sfx_trocar_avatar.wav` | Setas esquerda/direita na escolha de avatar | `cursor/cursor_left`, `cursor_right`, `avatars/*` |
| `sfx_ligar.wav` | Opção ligada (checkbox, som ligado) | `icons/checkbox_on`, `speaker_on` |
| `sfx_desligar.wav` | Opção desligada | `icons/checkbox_off`, `speaker_off` |
| `sfx_pausar.wav` | Jogo pausado | `headings/text_pausado` |
| `sfx_retomar.wav` | Jogo retomado após a pausa | `headings/text_pausado` |
