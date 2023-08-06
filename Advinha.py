from random import randint
def jogo_adv():
    print("***********************************")
    print("Bem vindo no jogo de Advinhação!")
    print("***********************************")

    numero_secreto = randint(1,101)
    pontos = 500
    tentativas = 0

    dificultade = int(input(f"QUAL NIVEL DESEJA JOGAR? \n "
          f"(1) FACIL\n"
          f" (2) MÉDIO\n"
          f" (3) DIFICIL \n"))

    if(dificultade == 1):
        tentativas = 20

    elif(dificultade == 2):
        tentativas = 10

    else:
        tentativas = 5



    for rodadas in range(1,tentativas + 1):
        print("Tentativas {} de {}".format(rodadas,tentativas))
        chute = int(input("Digite o seu numero: "))
        print("Você digitou ", chute)
        print("***********************************")
        print("\n")

        if(chute < 1):
            print("Digite um número positivo maior q zero")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if numero_secreto == chute:
            print("*************PARABÉNS**************")
            print(f"Você Acertou, VOCÊ OBTEVE A PONTUAÇÃO DE {pontos}")
            print("Numero Secreto: ", numero_secreto)
            print("Seu Chute: ", chute)
            print("***********************************")
            break

        elif(maior):
            print("Você errou, jogou muito pra cima")

        elif(menor):
            print("Você errou, jogou muito pra baixo")

        pontos_perdidos = abs(numero_secreto-chute)
        pontos = pontos - pontos_perdidos



    print(f"O número era: {numero_secreto}")
    print("Fim de jogo")
if (__name__ == "__main__"):
    jogo_adv()