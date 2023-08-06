import Advinha
import Forca
def escolhe_jogo():
    print("***********************************")
    print("*********Escolha o seu Jogo********")
    print("***********************************")

    print("(1) Adivinhação \n(2) Forca")

    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        print('Iniciando Adivinhação...')
        Advinha.jogo_adv()

    if(jogo == 2):
        print('Iniciando Forca...')
        Forca.jogo_forca()

if (__name__ == "__main__"):
    escolhe_jogo()