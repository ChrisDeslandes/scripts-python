from numpy import random
from tqdm import tqdm
import os

print("\n -- Loto Fácil --\n")

while 1:
    nJogos = input("Digite quantas surpresinhas deseja jogar: ")
    print()
    nJogos.replace(" ","")
    if nJogos.isdigit():
        nJogos = int(nJogos)
        if nJogos > 0:
            break
        else:
            print("Digite um número inteiro e positivo!\n")
    else:
        print("Digite um número inteiro e positivo!\n")

print("\n\nGerando jogos...\n\n")

arq = "c:\\users\\user\\desktop\\Loto Fácil.txt"

f = open(arq, "w")

for i in tqdm(range(nJogos)):
    numeros = []
    n = 0
    while n < 15:
        while 1:
            aux = random.randint(1,26)
            if aux in numeros: # Se o número já existe no array
                continue
            else: # Se o número não existe no array
                numeros.append(aux) # Adiciona o numero na lista
                n += 1
                break
    numeros.sort()
    frase = "Jogo " + str(i + 1).zfill(len(str(nJogos))) + ":  "
    for j in range(14):
        frase += str(numeros[j]).zfill(2) + " - "
    frase += str(numeros[14]).zfill(2)
    if i != nJogos - 1:
        frase += "\n\n"
    f.write(frase)

f.close()

print("\n\n\nFoi criado o arquivo 'Loto Fácil.txt' em seu desktop com seus jogos! Obrigado por utilizar o app e boa sorte!")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
