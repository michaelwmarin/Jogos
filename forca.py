import random

def jogar():
    print("\n*********************************\n   Bem Vindo no jogo da forca!\n*********************************\n")

    lista_toda = []

    with open('G:\Meu Drive\Alura\Portifolio\Jogos\lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
    
    palavra_secreta = str(lista_toda)
    palavra = lista_toda
    tentativa = len(palavra)
    enforcou = False
    acertou = False
    letras_acertadas = []
    tamanho_palavra = len(palavra_secreta)
    letras_acer = len(letras_acertadas)
    letras_faladas = []

    for i in range(tamanho_palavra - 1):
        if(letras_acer < tamanho_palavra):
            letras_acertadas.append("_")
        continue

    while(not enforcou and not acertou):

        letras_fim = ("".join(letras_acertadas))

        chute = input("\nQual letra? \n")
        chute = chute.strip()

        if(chute.upper() in letras_faladas):
            print ('Você já falou essa letra.')
            continue

        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas.pop(index)
                letras_acertadas.insert(index, chute.upper())
                letras_faladas.append(chute.upper())
            else:
                letras_faladas.append(chute.upper())
            index = index + 1

        letra_h = chute.upper()
        vez = palavra_secreta.count(chute)
        tem = vez > 0

        if(tem): 
            print("Encontrei a letra {} e {} vez.".format(letra_h, vez),"\n",letras_acertadas)
        else:
            print("Não tem essa letra.\n",letras_acertadas)

        if(palavra.upper() == letras_fim):
            print("\nFIM\n")
            break

        print("jogando")  

    acertou = palavra == palavra_secreta
    enforcou = tentativa == len(letras_faladas)


if(__name__=="__main__"):
    jogar()