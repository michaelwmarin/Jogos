import random

def jogar():
    bem_vindo()

    palavra_secreta = carrega_palavras()
    letras_acertadas = iniciliza_letras_acertadas(palavra_secreta)
    letras_faladas = []
    acertou = False
    enforcou = False
    tamanho_palavra = len(palavra_secreta)

    numero_tentativas = nivel()

    while(not enforcou and not acertou):
        
        letras_fim = ("".join(letras_acertadas))
        tentativa = abs(tamanho_palavra+numero_tentativas)

        enforcou = tentativa == tamanho_palavra
        acertou = letras_fim == palavra_secreta

        if(acertou):
            imprime_mensagem_vencedor()
            break
        elif(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)
            break

        print("JOGANDO\n\nVOCÊ TEM {} TENTATIVAS.".format((tentativa-tamanho_palavra)))

        chute = pede_chute()

        if(chute in letras_faladas):
            ja_falo()
            numero_tentativas -= 1
            desenha_forca(numero_tentativas)
            continue
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas, letras_faladas)
        else:
            letras_faladas.append(chute)
            numero_tentativas -= 1
            desenha_forca(numero_tentativas)

        vez = palavra_secreta.count(chute)
        tem = vez > 0

        if(tem): 
            print("\nEncontrei a letra {} e {} vez.\n\n".format(chute, vez),"\n",letras_acertadas)
        else:
            print("\nNão tem essa letra.\n\n",letras_acertadas)
            

def ja_falo():
    print ('\nVocê já falou essa letra.\n')

def bem_vindo():
    print("\n*********************************\n    Bem Vindo no jogo da forca!\n*********************************\n")

def carrega_palavras():
     
    lista_toda = []

    with open('lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
        arq.close
    palavra_secreta = str(lista_toda).strip().upper()
    return palavra_secreta

def nivel():
    print("\nQual nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil\n")

    nivel = int(input("Define o nível: "))
    facil = nivel == 1
    medio = nivel == 2

    if(facil):
        numero_tentativas = 7
    elif(medio):
        numero_tentativas = 5
    else:
        numero_tentativas = 3
        
    return numero_tentativas

def iniciliza_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nQual letra? \n")
    chute = chute.strip().upper()

    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas, letras_faladas):
    letras_faladas.append(chute)
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas.pop(index)
            letras_acertadas.insert(index, chute)
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(numero_tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(numero_tentativas == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 6):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(numero_tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (numero_tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__=="__main__"):
    jogar()

