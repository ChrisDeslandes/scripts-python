import os

while True:
    nbits = input("Digite a quantidade de bits destinada ao número (4, 8 ou 16): ").strip()
    if nbits == "4" or nbits == "8" or nbits == "16":
        nbits = int(nbits)
        break
    else:
        print("Valor inválido!!\n")

valmin = -(2**(nbits - 1) - 1)
valmax = 2**(nbits - 1) - 1

print()

while True:
    dec = input("Digite o valor a ser convertido para binário (Complemento de 1) (de " + str(valmin) + " a " + str(valmax) + "): ").strip()
    if dec.isdigit() or (dec[1:].isdigit() and dec[0] == "-"):
        dec = int(dec)
        if valmin <= dec <= valmax:
            break
        else:
            print("Valor inválido!!\n")
    else:
        print("Valor inválido!!\n")

b = bin(abs(dec))[2:].zfill(nbits)

bnot = ""

if dec < 0:
    for i in b:
        if i == "1": bnot += "0"
        else: bnot += "1"
    b = bnot
    
resbin = ""
aux = 1

for i in b:
    if aux%4 == 0 and aux != len(b):
        resbin += i + " "
    else:
        resbin += i
    aux += 1

reshex = hex(int(resbin.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbin.replace(" ", ""))/4))

print("\n\nValor em binário (Complemento de 1) = " + resbin + "\nValor em hexadecimal (Complemento de 1) = " + reshex)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
