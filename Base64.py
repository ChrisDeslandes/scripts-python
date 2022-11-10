import base64
import os

while True:
    escolha = input("Você deseja codificar ou decodificar o texto? (C para codificar e D para decodificar) ").upper().replace(" ", "")
    if escolha not in "CD" or escolha == "":
        print("\nDigite apenas C ou D...")
        continue
    else: break

s = input("\nDigite o texto a ser codificado/decodificado: ")

if escolha == "C":
    message_bytes = s.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("\nTexto codificado: " + base64_message)
else:
    base64_bytes = s.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("\nTexto decodificado: " + message)

print("\nPressione qualquer tecla para fechar...")
os.system("pause >nul")
