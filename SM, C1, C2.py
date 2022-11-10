import os

while True:
    nbits = input("Digite a quantidade de bits destinada ao número (4, 8 ou 16): ").strip()
    if nbits == "4" or nbits == "8" or nbits == "16":
        nbits = int(nbits)
        break
    else:
        print("Valor inválido!!\n")

print()

while True:
    dec = input("Digite o valor a ser convertido para binário (S/M, C1 e C2): ").strip()
    if dec.isdigit() or (dec[1:].isdigit() and (dec[0] == "-" or dec[0] == "+")):
        dec = int(dec)
        break
    else:
        print("Valor inválido!!\n")

sinal = ""

if dec < 0: sinal = "1"
else: sinal = "0"

bSM = sinal + bin(abs(dec))[2:].zfill(nbits - 1)

bC1 = bC2 = bin(abs(dec))[2:].zfill(nbits)

bnot = ""

if dec < 0:
    for i in bC1:
        if i == "1": bnot += "0"
        else: bnot += "1"
    bC1 = bnot
    bC2 = bin(int(bnot, 2) + 1)[2:]

resbinSM = ""
resbinC1 = ""
resbinC2 = ""

valmin = -(2**(nbits - 1) - 1)
valmax = 2**(nbits - 1) - 1

if valmin <= dec <= valmax:
    aux = 1
    for i in bSM:
        if aux%4 == 0 and aux != len(bSM):
            resbinSM += i + " "
        else:
            resbinSM += i
        aux += 1
    reshexSM = hex(int(resbinSM.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbinSM.replace(" ", ""))/4))
    for i in bC1:
        if aux%4 == 0 and aux != len(bC1):
            resbinC1 += i + " "
        else:
            resbinC1 += i
        aux += 1
    reshexC1 = hex(int(resbinC1.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbinC1.replace(" ", ""))/4))
elif dec > valmax:
    resbinSM = "Overflow"
    reshexSM = "Overflow"
    resbinC1 = "Overflow"
    reshexC1 = "Overflow"
else:
    resbinSM = "Underflow"
    reshexSM = "Underflow"
    resbinC1 = "Underflow"
    reshexC1 = "Underflow"
    
if valmin - 1 <= dec <= valmax:
    aux = 1
    for i in bC2:
        if aux%4 == 0 and aux != len(bC2):
            resbinC2 += i + " "
        else:
            resbinC2 += i
        aux += 1
    reshexC2 = hex(int(resbinC2.replace(" ", ""), 2))[2:].upper().zfill(int(len(resbinC2.replace(" ", ""))/4))
elif dec > valmax:
    resbinC2 = "Overflow"
    reshexC2 = "Overflow"
else:
    resbinC2 = "Underflow"
    reshexC2 = "Underflow"

if abs(dec) == 0:
    if nbits == 4:
        resbinSM = "0000 ou 1000"
        reshexSM = "0 ou 8"
        resbinC1 = "0000 ou 1111"
        reshexC1 = "0 ou F"
    elif nbits == 8:
        resbinSM = "0000 0000 ou 1000 0000"
        reshexSM = "00 ou 80"
        resbinC1 = "0000 0000 ou 1111 1111"
        reshexC1 = "00 ou FF"
    else:
        resbinSM = "0000 0000 0000 0000 ou 1000 0000 0000 0000"
        reshexSM = "0000 ou 8000"
        resbinC1 = "0000 0000 0000 0000 ou 1111 1111 1111 1111"
        reshexC1 = "0000 ou FFFF"

print("\n\nQuantidade de bits = " + str(nbits))
print("\nValor em decimal = " + str(dec))
print("\nValor em binário (S/M) = " + resbinSM + "\nValor em hexadecimal (S/M) = " + reshexSM)
print("\nValor em binário (Complemento de 1) = " + resbinC1 + "\nValor em hexadecimal (Complemento de 1) = " + reshexC1)
print("\nValor em binário (Complemento de 2) = " + resbinC2 + "\nValor em hexadecimal (Complemento de 2) = " + reshexC2)

print("\n\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
