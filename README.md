# Coleção de Jogos Clássicos em Python 🐍

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Este repositório contém uma coleção de jogos clássicos desenvolvidos em Python, como parte dos estudos iniciais na linguagem. O projeto foi estruturado de forma modular, permitindo que o usuário escolha qual jogo deseja jogar através de um menu principal.

---

## 🎮 Jogos Disponíveis

Atualmente, a coleção inclui os seguintes jogos:

### 1. Jogo da Forca (`forca.py`)
Um clássico jogo da forca em que o jogador deve adivinhar uma palavra secreta, letra por letra, antes que o boneco seja enforcado.

**Funcionalidades:**
-   A palavra secreta é escolhida aleatoriamente de um arquivo de texto.
-   Interface de linha de comando com arte ASCII para representar o enforcado.
-   Exibe as letras corretas e erradas já tentadas pelo jogador.
-   Mensagens de vitória ou derrota ao final do jogo.

### 2. Jogo de Adivinhação (`adivinhacao.py`)
O objetivo é adivinhar um número secreto gerado aleatoriamente dentro de um intervalo.

**Funcionalidades:**
-   **Níveis de Dificuldade**: O jogador pode escolher entre os níveis Fácil, Médio e Difícil, que determinam o número de tentativas disponíveis.
-   **Feedback ao Jogador**: O jogo informa se o chute foi maior ou menor que o número secreto.
-   **Sistema de Pontuação**: O jogador perde pontos a cada chute errado, incentivando a precisão.

---

## 🚀 Como Executar

Para rodar os jogos, você precisa ter o Python 3 instalado no seu computador.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd jogos
    ```

3.  **Execute o menu principal:**
    ```bash
    python jogos.py
    ```

4.  **Escolha o jogo**: O terminal exibirá um menu para você selecionar qual jogo deseja jogar.

---

## 📂 Estrutura do Projeto
.
├── jogos.py          # Script principal que executa o menu de jogos
├── forca.py          # Módulo do Jogo da Forca
├── adivinhacao.py    # Módulo do Jogo de Adivinhação
├── palavras.txt      # Arquivo com a lista de palavras para o Jogo da Forca
└── README.md         # Este arquivo
