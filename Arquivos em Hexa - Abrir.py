import os

arq = input("Digite o endereço completo do arquivo a ser lido: ").replace("\\", "/")

x, extensao = os.path.splitext(arq)

pasta = arq[0:arq.rfind("/") + 1]
nome = arq[arq.rfind("/") + 1:]
arqtxt = pasta + "HEX - " + nome[0:len(nome) - len(extensao)] + ".txt"

f = open(arq, "rb")

data = f.read()

f.close()

if os.path.exists(arqtxt):
    os.remove(arqtxt)

f = open(arqtxt, "a")

texto = ""

for i in data:
    texto += hex(i)[2:].upper().zfill(2) + " "

f.write(texto[0:len(texto) - 1])

f.close()
