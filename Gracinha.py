import os

while 1:
    palavra = input("Digite uma palavra/frase: ").upper()
    if len(palavra) > 0: break
    
print("\n\n")

print("  _" + " " * (2 * len(palavra) + 3) + "_")
print(" | \\" + " " * (2 * len(palavra) + 1) + "/ |")
print(" |  \\" + " " * (2 * len(palavra) - 1) + "/  |")

for i in range(len(palavra) - 1):
    print(" | " + palavra[:i+1] + " \\" + " " * (2 * len(palavra) - 3 - 2 * i) + "/ " + palavra[len(palavra) - i - 1:] + " |")
    
print(" | " + palavra + " | " + palavra + " |")

for i in range(1, len(palavra)):
    print(" | " + palavra[:len(palavra)-i] + " /" + " " * (2 * i - 1) + "\\ " + palavra[i:] + " |")
    
print(" |  /" + " " * (2 * len(palavra) - 1) + "\\  |")
print(" | /" + " " * (2 * len(palavra) + 1) + "\\ |")
print("  ̅" + " " * (2 * len(palavra) + 3) + "̅")

print("\n\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
