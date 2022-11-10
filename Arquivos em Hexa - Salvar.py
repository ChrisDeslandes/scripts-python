import os

while 1:
    arqtxt = input("Digite o endereço completo do arquivo .txt contendo os bytes a serem salvos: ").replace("\\", "/")
    arq, e = os.path.splitext(arqtxt)
    if os.path.exists(arqtxt):
        if e == ".txt":
            break
        else:
            print("O arquivo especificado não é do tipo .txt!\n")
    else:
        print("O arquivo especificado não existe!\n")

f = open(arqtxt, "rt")

data = f.read()
data = data.replace(" ", "").replace("\n", "")

f.close()

if os.path.exists(arq):
    os.remove(arq)

f = open(arq, "wb")

b = bytes([int(data[i:i+2], 16) for i in range(0, len(data), 2)])

f.write(b)

f.close()
