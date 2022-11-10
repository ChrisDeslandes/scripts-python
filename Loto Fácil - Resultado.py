import numpy as np
import os

print("\n -- Conferência da Loto Fácil --\n")

while 1:
    continua = False
    x = input("Digite os números sorteados separados por espaço: ").replace("-"," ")
    if x.replace(" ","").isdigit():
        numsSorteados = np.array(x.split(), dtype="i")
        if len(numsSorteados) == 15:
            continua = True
            for i in range(15):
                if numsSorteados[i] < 1 or numsSorteados[i] > 25:
                    continua = False
    if continua:
        numsSorteados.sort()
        break
    else:
        print("Sua entrada deve conter 15 números inteiros, separados por espaço, do 1 ao 25. Os números não podem se repetir.\n")

print()

while 1:
    nome = input("Digite o nome do arquivo onde estão os números que deseja conferir (O arquivo deve estar em seu Desktop): ")
    if nome == "":
        print("O nome do arquivo não deve ser vazio!\n")
    else:
        arq = "c:\\users\\user\\desktop\\" + nome
        if os.path.exists(arq):
            break
        else:
            print("Arquivo não encontrado!\n")

f = open(arq, "r")

indexLinha = 0

lista = []

print("\n\n\nLendo o arquivo " + arq + "...")

for i in f:
    if indexLinha % 2 == 0:
        nums = np.array(i[i.find(":") + 3:].replace("\n","").replace(" - "," ").split(), dtype="i")
        lista.append(nums)
    indexLinha += 1

f.close()

print("\n\n\nConferindo os jogos e gravando o arquivo de resultados...")

arq = "c:\\users\\user\\desktop\\Resultado - " + nome

if os.path.exists(arq): os.remove(arq)

f = open(arq, "a")

f.write("Números sorteados: ")

for i in range(len(numsSorteados)):
    if i == len(numsSorteados) - 1:
        f.write(str(numsSorteados[i]).zfill(2))
    else:
        f.write(str(numsSorteados[i]).zfill(2) + " - ")
    
f.write("\n\n----------------------------------------------------------------------------------------------------------\n\n")

num15 = 0
num14 = 0
num13 = 0
num12 = 0
num11 = 0

for i in range(len(lista)):
    frase = "Jogo " + str(i + 1).zfill(len(str(len(lista)))) + ":  "
    numAcertos = 0
    for j in range(len(lista[i])):
        if j != len(lista[i]) - 1:
            frase += str(lista[i][j]).zfill(2) + " - "
        else:
            frase += str(lista[i][14]).zfill(2)
        if lista[i][j] in numsSorteados:
            numAcertos += 1
    frase += " --- Acertos: " + str(numAcertos) + "/15"
    if i != len(lista) - 1:
        frase += "\n\n"
    if numAcertos == 11:
        num11 += 1
    elif numAcertos == 12:
        num12 += 1
    elif numAcertos == 13:
        num13 += 1
    elif numAcertos == 14:
        num14 += 1
    elif numAcertos == 15:
        num15 += 1
    f.write(frase)

f.close()

print("\n\n\nVocê ganhou:\n\n" +\
      str(num15) + " jogos com 15 acertos;\n" +\
      str(num14) + " jogos com 14 acertos;\n" +\
      str(num13) + " jogos com 13 acertos;\n" +\
      str(num12) + " jogos com 12 acertos;\n" +\
      str(num11) + " jogos com 11 acertos.")

print("\n\n\nFoi criado o arquivo 'Resultado - " + nome + " em seu desktop com o resultado de seus jogos! Obrigado por utilizar o app!")

print("\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
