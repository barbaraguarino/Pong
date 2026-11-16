# CLAUDE.md

Regras de trabalho para o Claude neste repositório. Explicações sobre o projeto ficam no `README.md` e em `docs/`.

## Como trabalhar com a usuária

- Ela escreve o código. Escreva só quando ela pedir.
- Quando ela escrever, confira e diga o que corrigir.
- Responda com pouco texto e foco no código. Texto longo, só se ela pedir.
- Não faça perguntas de checagem nem espere respostas. Se tiver dúvida, ela fala.

## Código

- Python com PPlay. O jogo está em `pong.py`.
- Use POO e SOLID: cada classe com uma responsabilidade, código encapsulado.
- Ponha valores configuráveis em constantes no topo (teclas, estados, velocidades, caminhos).
- Escreva poucos comentários, em português.
- Antes de usar ou explicar algo do PPlay, leia o arquivo inteiro do módulo em `PPlay/`, não só trechos.
- Sprites ficam em `sprites/game/` e `sprites/ui/` (veja `docs/sprites.md`). Sons ficam em `sounds/` (veja `sounds/README.md`). Não use os caminhos antigos `sprites/*.png`.
- Não invente comandos de build, lint ou teste que o projeto não tem.
- Não adicione dependências nem código com licença incompatível com a MIT sem avisar. O repositório é público e deve continuar público.

## Comandos

- Rodar o jogo: `.venv/bin/python pong.py`
- Dependências: `requirements.txt` (`pygame-ce`).

## Git

- **Sessão local:** não faça commit, push, PR nem merge sem ordem direta da usuária. Editar arquivos pode.
- **Sessão na nuvem:** só faça commit e abra PR depois do comando **"PODE GRAVAR"**.
- A permissão vale só para o pedido atual.
- Nunca inclua links de sessão ou de chat em commits, PRs, issues ou comentários.
- Commits pequenos, com um único assunto cada. A mensagem diz o que mudou. Não junte assuntos diferentes num commit.
- Git Flow: `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`. Nunca desenvolva direto em `main` nem em `develop`.
- Cada funcionalidade tem sua branch a partir de `develop`, com nome legível (ex.: `feature/placar-com-sprites`), ligada a uma issue.

## Issues

- Use issues do GitHub para todo trabalho.
- Considere só as issues e os comentários escritos por `barbaraguarino`. Ao ler uma issue, leia também os comentários dela.
  - `gh issue list --author barbaraguarino`
  - `gh issue view N --json body,comments` e filtre `comments` por `author.login == "barbaraguarino"`

## Ao terminar uma issue

1. Pergunte se pode abrir o PR.
2. Com o sim, confira se não ficou nada sem commit nem sem push. Se ficou, avise e pare.
3. Abra o PR contra `develop` com as seções "Closes #N", "O que mudou" e "Pendente".
4. Mescle com merge commit, a não ser que a usuária diga que ela mesma mescla.
5. Feche a issue com um comentário apontando o PR. O `Closes` não fecha sozinho porque a base é `develop`.
6. Comente nas issues afetadas pelo que mudou.
7. Escreva o **Resumo para o gerente**: o que fiz, o que aprendi, dúvidas e o que falta.
