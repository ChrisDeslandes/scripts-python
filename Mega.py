import random as rnd
from tqdm import tqdm
import os

print("\n -- Mega Sena --\n")

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

arq = "c:\\users\\user\\desktop\\Mega.txt"

f = open(arq, "w")

for i in tqdm(range(nJogos)):
    numeros = rnd.sample(list(range(1,61)), 6)
    numeros.sort()
    frase = "Jogo " + str(i + 1).zfill(len(str(nJogos))) + ":  "
    frase += " - ".join(str(n).zfill(2) for n in numeros)
    if i != nJogos - 1:
        frase += "\n\n"
    f.write(frase)

f.close()

print("\n\n\nFoi criado o arquivo Mega.txt em seu desktop com seus jogos! Obrigado por utilizar o app e boa sorte!")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
