import random

def palavra():

    lista_toda = []

    with open('G:\Meu Drive\Alura\Portifolio\Jogos\lista_toda.txt','r') as arq:
        conteudo = arq.readlines()
        p = random.randrange(0, 245366)
        lista_toda = (conteudo[p])
    print(lista_toda)

if(__name__=="__main__"):
    palavra()