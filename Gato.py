from numpy import random
import os

nCaixas = 5
nJogos = 100000

def jogar(resposta):
    acertos = 0
    for i in range(nJogos):
        gato = random.randint(nCaixas) + 1
        for tentativa in resposta:
            if tentativa == gato:
                acertos += 1
                break
            if gato == 1:
                gato = 2
            elif gato == nCaixas:
                gato = nCaixas - 1
            else:
                gato = random.choice([gato - 1, gato + 1])
    print("Número de caixas: " + str(nCaixas))
    print("\nSequência de procura: " + str(resposta))
    print("\n\nNúmero de jogos: " + str(nJogos) + "\nNúmero de acertos: " + str(acertos) + "\nPorcentagem de acerto: " + str(100 * acertos / nJogos) + " %")

## RESPOSTA CORRETA INDEPENDENTE DO NÚMERO DE CAIXAS:
## --------------------------------------------------
##resposta = []
##for i in range(2, nCaixas):
##    resposta.append(i)
##for i in range(nCaixas - 1, 1, -1):
##    resposta.append(i)
## --------------------------------------------------

jogar([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])

print("\n\n")

jogar([2,3,4,4,3,2])

os.system("pause >nul")
