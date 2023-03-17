import random

def jogar():
    print("\n*********************************\n   Bem Vindo no jogo da forca!\n*********************************\n")

    lista_toda = []

    with open('G:\Meu Drive\Alura\Portifolio\Jogos\lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
    
    palavra_secreta = str(lista_toda).strip()
    letras_acertadas = []
    letras_faladas = []
    acertou = False
    enforcou = False
    tamanho_palavra = len(palavra_secreta)
    letras_acer = len(letras_acertadas)


    for i in range(tamanho_palavra):
        if(letras_acer < tamanho_palavra):
            letras_acertadas.append("_")
        continue

    while(not enforcou and not acertou):

        letras_fim = ("".join(letras_acertadas))
        palavra_fim = palavra_secreta.upper()
        tentativa = len(letras_faladas)
        print("JOGANDO\nVOCÊ TEM {} TENTATIVAS.".format(tamanho_palavra-tentativa))

        enforcou = tentativa == tamanho_palavra
        acertou = letras_fim == palavra_fim

        if(acertou):
            print("\nFIM\nVocê acertou a palavra\nPARABÉNS!!!!")
            break
        elif(enforcou):
            print("\nFIM\nVocê pedeu não acertou.\nSuas tentativa acabaram\n")
            break

        chute = input("\nQual letra? \n")
        chute = chute.strip().lower()

        if(chute.upper() in letras_faladas):
            print ('Você já falou essa letra.')
            continue
        
        if(chute in palavra_secreta):
            letras_faladas.append(chute.upper())
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas.pop(index)
                    letras_acertadas.insert(index, chute.upper())
                index += 1
        else:
            letras_faladas.append(chute.upper())

        letra_h = chute.upper()
        vez = palavra_secreta.count(chute)
        tem = vez > 0

        if(tem): 
            print("Encontrei a letra {} e {} vez.".format(letra_h, vez),"\n",letras_acertadas)
        else:
            print("Não tem essa letra.\n",letras_acertadas)

if(__name__=="__main__"):
    jogar()