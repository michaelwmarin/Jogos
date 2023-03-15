import random

def jogar():
    print("\n*********************************\n   Bem Vindo no jogo da forca!\n*********************************\n")

    lista_toda = []

    with open('G:\Meu Drive\Alura\Portifolio\Jogos\lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
    
    palavra_secreta = str(lista_toda)
    enforcou = False
    acertou = False
    letras_acertadas = []
    tamanho_palavra = len(palavra_secreta)
    letras_acer = len(letras_acertadas)

    for i in range(tamanho_palavra - 1):
        if(letras_acer < tamanho_palavra):
            letras_acertadas.append("_")
        continue

    while(not enforcou and not acertou):

        chute = input("\nQual letra? \n")
        chute = chute.strip()

        if(chute.upper() in letras_acertadas):
            print ('Você já falou essa letra.')
            continue

        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas.pop(index)
                letras_acertadas.insert(index, chute.upper())
            index = index + 1
            print("Encontrei a letra {}.".format(chute))
            print(letras_acertadas)
        
        print("jogando")       

if(__name__=="__main__"):
    jogar()