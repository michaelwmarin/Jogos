import random

def jogar():
    print("\n*********************************\n   Bem Vindo no jogo da forca!\n*********************************\n")

    lista_toda = []

    with open('G:\Meu Drive\Alura\Portifolio\Jogos\lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
    
    palavra_secreta = str(lista_toda).strip().upper()
    letras_acertadas = []
    letras_faladas = []
    acertou = False
    enforcou = False
    tamanho_palavra = len(palavra_secreta)
    letras_acer = len(letras_acertadas)
    numero_tentativas = 0

    for i in range(tamanho_palavra):
        if(letras_acer < tamanho_palavra):
            letras_acertadas.append("_")
        continue
    
    print("\nQual nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil\n")

    nivel = int(input("Define o nível: "))
    facil = nivel == 1
    medio = nivel == 2

    if(facil):
        numero_tentativas = 5
    elif(medio):
        numero_tentativas = 3
    else:
        numero_tentativas = 2

    while(not enforcou and not acertou):

        letras_fim = ("".join(letras_acertadas))
        tentativa = abs(tamanho_palavra+numero_tentativas)

        enforcou = tentativa == tamanho_palavra
        acertou = letras_fim == palavra_secreta

        if(acertou):
            print("\nFIM\nVocê acertou a palavra\nPARABÉNS!!!!")
            break
        elif(enforcou):
            print("\nFIM\nVocê pedeu não acertou.\nSuas tentativa acabaram\n")
            break

        print("JOGANDO\n\nVOCÊ TEM {} TENTATIVAS.".format(tentativa-tamanho_palavra))

        chute = input("\nQual letra? \n")
        chute = chute.strip().upper()

        if(chute in letras_faladas):
            print ('\nVocê já falou essa letra.\n')
            numero_tentativas -= 1 
            continue
        
        if(chute in palavra_secreta):
            letras_faladas.append(chute)
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas.pop(index)
                    letras_acertadas.insert(index, chute)
                index += 1
        else:
            letras_faladas.append(chute)

        vez = palavra_secreta.count(chute)
        tem = vez > 0

        if(tem): 
            print("\nEncontrei a letra {} e {} vez.\n\n".format(chute, vez),"\n",letras_acertadas)
        else:
            print("\nNão tem essa letra.\n\n",letras_acertadas)
            numero_tentativas -= 1

if(__name__=="__main__"):
    jogar()