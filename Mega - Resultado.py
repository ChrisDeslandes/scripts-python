import numpy as np
import os

print("\n -- Conferência da Mega Sena --\n")

while 1:
    continua = False
    x = input("Digite os números sorteados separados por espaço: ").replace("-"," ")
    if x.replace(" ","").isdigit():
        numsSorteados = np.array(x.split(), dtype = "i")
        if len(numsSorteados) == 6:
            continua = True
            for i in range(6):
                if numsSorteados[i] < 1 or numsSorteados[i] > 60:
                    continua = False
    if continua:
        numsSorteados.sort()
        break
    else:
        print("Sua entrada deve conter 6 números inteiros, separados por espaço, do 1 ao 60. Os números não podem se repetir.\n")

print()

while 1:
    nome = input("Digite o nome do arquivo onde estão os números que deseja conferir (O arquivo deve estar em seu Desktop): ")
    if nome == "":
        print("O nome do arquivo não deve ser vazio!\n")
    else:
        arq = "C:\\Users\\user\\Desktop\\" + nome
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

arq = "C:\\Users\\user\\Desktop\\Resultado - " + nome

if os.path.exists(arq): os.remove(arq)

f = open(arq, "a")

f.write("Números sorteados: ")

f.write(" - ".join(str(n).zfill(2) for n in numsSorteados))
    
f.write("\n\n------------------------------------------------------------\n\n")

numSena = 0
numQuina = 0
numQuadra = 0

for i in range(len(lista)):
    frase = "Jogo " + str(i + 1).zfill(len(str(len(lista)))) + ":  "

    frase += " - ".join(str(n).zfill(2) for n in lista[i])

    numAcertos = 0
    for j in range(len(lista[i])):
        if lista[i][j] in numsSorteados:
            numAcertos += 1

    strGanhou = ""
    if numAcertos == 4: strGanhou = " ---> Ganhou a QUADRA!!"
    elif numAcertos == 5: strGanhou = " ---> Ganhou a QUINA!!"
    elif numAcertos == 6: strGanhou = " ---> Ganhou a SENA!!"

    frase += " --- Acertos: " + str(numAcertos) + "/6" + strGanhou

    if i != len(lista) - 1:
        frase += "\n\n"
    if numAcertos == 4:
        numQuadra += 1
    elif numAcertos == 5:
        numQuina += 1
    elif numAcertos == 6:
        numSena += 1
    f.write(frase)

f.close()

print("\n\n\nVocê ganhou:\n\n" +\
      str(numSena) + " senas;\n" +\
      str(numQuina) + " quinas;\n" +\
      str(numQuadra) + " quadras.")

print("\n\n\nFoi criado o arquivo 'Resultado - " + nome + " em seu desktop com o resultado de seus jogos! Obrigado por utilizar o app!")

print("\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
