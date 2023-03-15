import random

def jogar():

    print("*********************************\nBem Vindo no jogo de Adivinhação!\n*********************************")

    numero_secreto = random.randrange(1, 10)
    numero_tentativas = 0
    pontos = 30

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

    for rodada in range(1, numero_tentativas + 1):

        print("\nTentativa {} de {} \n".format(rodada, numero_tentativas))
        chute = int(input("Escreva o número de 1 a 10 = "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos_ganhados = abs(numero_secreto + chute)

        if ((chute < 1) or (chute > 10)):
            print("Escreva o número de 1 até 10!\nTentativa {} de {}".format(rodada, numero_tentativas))
            continue

        if(acertou):
            pontos = pontos + pontos_ganhados
            print("\nSeu pontos são {}\nCERTO!! Seu número foi {}\nNúmero secreto é {}".format(pontos, chute, numero_secreto))
            break
        else:
            if (menor):
                print("\n********************************\nTentativa {} de {}\nERRADO!! Seu número foi {}\nVocê chutou abaixo".format(rodada, numero_tentativas, chute))
                rodada = rodada + 1
                pontos = pontos - pontos_perdidos
                print("Seu pontos são {}\n******* FIM DA TENTATIVA *******".format(pontos)) 
            elif (maior):
                print("\n********************************\nTentativa {} de {}\nERRADO!! Seu número foi {}\nVocê chutou para acima".format(rodada, numero_tentativas, chute))
                rodada = rodada + 1
                pontos = pontos - pontos_perdidos
                print("Seu pontos são {}\n******* FIM DA TENTATIVA *******".format(pontos))       

    print("\nSeu pontos são {}\nNúmero certo era {}\nFIM DO JOGO\n".format(pontos, numero_secreto))

if(__name__=="__main__"):
    jogar()