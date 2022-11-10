import os

while True:
    nbits = input("Digite a quantidade de bits destinada ao número (4, 8 ou 16): ").strip()
    if nbits == "4" or nbits == "8" or nbits == "16":
        nbits = int(nbits)
        break
    else:
        print("Valor inválido!!\n")

valmin = -2**(nbits - 1)
valmax = 2**(nbits - 1) - 1

print()

for dec in range(valmin, valmax + 1):
    b = bin(abs(dec))[2:].zfill(nbits)
    bnot = ""
    if dec < 0:
        for i in b:
            if i == "1": bnot += "0"
            else: bnot += "1"
        b = bin(int(bnot, 2) + 1)[2:]
    resbin = ""
    aux = 1
    for i in b:
        if aux%4 == 0 and aux != len(b):
            resbin += i + " "
        else:
            resbin += i
        aux += 1
    reshex = hex(int(resbin.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbin.replace(" ", ""))/4))
    print("\n\nValor em decimal = " + str(dec) + "\nValor em binário (Complemento de 2) = " + resbin + "\nValor em hexadecimal (Complemento de 2) = " + reshex)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
