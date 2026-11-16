# Sprites

Todos os sprites são PNG e ficam em `sprites/`, divididos em dois grupos. Eles foram movidos da raiz (`sprites/*.png`) para estas pastas.

## `sprites/game/`: partida

| Pasta | Conteúdo |
|---|---|
| `ball/` | A bola |
| `court/` | A linha central da quadra |
| `digits/` | Dígitos de 0 a 9 do placar |
| `effects/` | Rastro da bola e efeito de impacto |
| `paddles/` | Raquetes: `paddle` (genérica), `paddle_p1` e `paddle_p2` |

## `sprites/ui/`: interface

| Pasta | Conteúdo |
|---|---|
| `avatars/` | Avatares do jogador |
| `buttons/` | Botões do menu |
| `cursor/` | Setas e cursor |
| `font/` | Fonte em pixel, um PNG por caractere |
| `headings/` | Títulos: `text_pausado`, `text_jogador1_venceu`, `text_jogador2_venceu` |
| `icons/` | Caixas de seleção, alto-falante, troféus |
| `input/` | Campo de nome e cursor de texto |
| `labels/` | Rótulos: `label_pontos`, `label_recorde`, `label_ranking`, `label_vidas`, `label_nome`, `label_avatar`, `label_opcoes` |
| `logo/` | Logo do jogo |
| `panel/` | Painel de fundo (`panel_9slice`) e linhas do ranking |

Os textos dos sprites de interface estão em português. Eles mostram as telas previstas: pausa, vitória de cada jogador, ranking e recorde, nome e avatar do jogador, opções.

## A fonte (`sprites/ui/font/`)

- Cada caractere tem 24 × 40 pixels, todos com a mesma largura.
- Arquivos: `char_A.png` a `char_Z.png`, e os símbolos `colon` (`:`), `comma` (`,`), `dash` (`-`), `exclaim` (`!`), `period` (`.`), `plus` (`+`), `question` (`?`).
- Não há sprite de espaço: o espaço é só um intervalo entre letras.
- Não há letras minúsculas, acentuadas nem `Ç`. Por isso o aviso de saque diz "ESPACO".
- No código, a classe `TextoSprite` monta um texto com esses arquivos.
