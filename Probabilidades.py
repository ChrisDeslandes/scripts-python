from numpy import random
import os
from tqdm import tqdm
from colorama import init, Fore, Style

os.system("cls")

while 1:
    while 1:
        nJogadores = input("Digite o número de jogadores: ")
        print()
        nJogadores = nJogadores.replace(" ","")
        if nJogadores.isdigit() and nJogadores != "0":
            nJogadores = int(nJogadores)
            break
        else:
            print("Digite um número válido!\n")

    while 1:
        nJogosNaQueda = input("Digite o número de jogos em cada queda: ")
        print()
        nJogosNaQueda = nJogosNaQueda.replace(" ","")
        if nJogosNaQueda.isdigit() and nJogosNaQueda != "0":
            nJogosNaQueda = int(nJogosNaQueda)
            break
        else:
            print("Digite um número válido!\n")

    while 1:
        nQuedas = input("Digite o número de quedas: ")
        print()
        nQuedas = nQuedas.replace(" ","")
        if nQuedas.isdigit() and nQuedas != "0":
            nQuedas = int(nQuedas)
            break
        else:
            print("Digite um número válido!\n")

    numDeJogosGanheiTodas = 0
    for n in tqdm(range(nQuedas)):
        i = 0
        Jogador1 = 0
        for i in range(nJogosNaQueda):
            x = random.randint(nJogadores)
            if x == 0:
                Jogador1 += 1
            i += 1
        if Jogador1 == nJogosNaQueda:
            numDeJogosGanheiTodas += 1
    
    os.system("cls")

    init()
    
    print("Número de jogadores = " + str(nJogadores)\
          + "\n\nNúmero de jogos em cada queda = " + str(nJogosNaQueda)\
          + "\n\nNúmero de quedas = " + str(nQuedas)\
          + "\n\nNúmero de jogos em que o Jogador 1 ganhou todas = " + str(numDeJogosGanheiTodas)\
          + "\n\n\nPorcentagem = " + Fore.GREEN + Style.BRIGHT + str("%.2f" % ((numDeJogosGanheiTodas * 100) / nQuedas)) + " %" + Style.RESET_ALL \
          + "\n\n------------------------------------------------------\n")
    
    resp = input("Deseja rodar o programa de novo? (S/N) ")
    if (resp == "N" or resp == "n"):
        print()
        break
    else:
        os.system("cls")
