from random import randint
from time import sleep

def saindo():
    print("Saindo em 3...")
    sleep(1)
    print("Saindo em 2..")
    sleep(1)
    print("Saindo em 1.")
    sleep(0.25)
    print("Até Mais!")


vidas = 3
pontos = 0


def acerte_numero():
    rnd_numero = randint(0, 200)
    print("Debug:",rnd_numero)
    resposta = input("Qual será o número que foi gerado? Responda: ")
    if int(resposta) == rnd_numero:
        global vidas
        global pontos
        vidas = vidas + 1
        pontos = pontos + 2
        if vidas <= 0:
            print("Você não possui mais tentativas.")
            exit
        else:
            pass
            tentar_novamente = input("Você acertou, está com {0} pontos e com {1} de vidas. Deseja tentar novamente? 1 - Sim | 2 - Não / Digite: ".format(pontos, vidas))
            if tentar_novamente in ["1", "Sim", "SIM", "sim"]:
                acerte_numero()
            elif tentar_novamente in ["2", "Não", "NÃO", "NAO", "Nao", "não", "nao"]:
                saindo()
            else:
                print("Opção inválida. Tente novamente!")
                menu()
    else:
        vidas = vidas - 1
        if vidas <= 0:
            print("Você não possui mais tentativas.")
            exit
        else:
            pass
            tentar_novamente = input("Você errou, está com {0} vidas. Deseja tentar novamente? 1 - Sim | 2 - Não / Digite: ".format(vidas))
            if tentar_novamente in ["1", "Sim", "SIM", "sim"]:
                acerte_numero()
            elif tentar_novamente in ["2", "Não", "NÃO", "NAO", "Nao", "não", "nao"]:
                saindo()
            else:
                print("Opção inválida. Tente novamente!")
                menu()

def menu():
    opcao = input('''
    Menu:
    1 - Acerte o numero
    Digite: ''')
    if opcao in ["1", "Acerte o Numero", "Acerte o numero", "ACERTE O NUMERO"]:
        acerte_numero()
    elif opcao == "2":
        print("segundo jogo")
    else:
        print("Opção inválida. Tente novamente!")
        menu()

menu()