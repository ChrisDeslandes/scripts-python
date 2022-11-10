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
    dec = input("Digite o valor a ser convertido para binário (Sinal/Magnitude) (de " + str(valmin) + " a " + str(valmax) + "): ").strip()
    if dec.isdigit() or (dec[1:].isdigit() and (dec[0] == "-" or dec[0] == "+")):
        dec = int(dec)
        if valmin <= dec <= valmax:
            break
        else:
            print("Valor inválido!!\n")
    else:
        print("Valor inválido!!\n")

sinal = ""

if dec < 0:
    sinal = "1"
else:
    sinal = "0"

b = bin(abs(dec))[2:]

b = b.zfill(nbits - 1)

b = sinal + b

resbin = ""
aux = 1

for i in b:
    if aux%4 == 0 and aux != len(b):
        resbin += i + " "
    else:
        resbin += i
    aux += 1

reshex = hex(int(resbin.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbin.replace(" ", ""))/4))

if abs(dec) == 0:
    if nbits == 4:
        resbin = "0000 ou 1000"
        reshex = "0 ou 8"
    elif nbits == 8:
        resbin = "0000 0000 ou 1000 0000"
        reshex = "00 ou 80"
    else:
        resbin = "0000 0000 0000 0000 ou 1000 0000 0000 0000"
        reshex = "0000 ou 8000"

print("\n\nValor em binário (Sinal/Magnitude) = " + resbin + "\nValor em hexadecimal (Sinal/Magnitude) = " + reshex)

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
