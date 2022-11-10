alf = "0123456789ABCDEF"

while True:
    ok = True
    x = input("Digite o valor em binário a ser convertido para hexadecimal: ").strip()
    for i in x:
        if not i in "01":
            print("Você introduziu um valor inválido!\n")
            ok = False
            break
    if ok: break

hexa = ""

while x != "":
    if len(x) >= 4:
        aux = x[len(x) - 4:]
        x = x[:len(x) - 4]
    else:
        aux = x
        x = ""
    r = 0
    for i in range(len(aux)):
        r += int(aux[len(aux) - 1 - i]) * (2 ** i)
    hexa = alf[r] + hexa

hexa = hexa.lstrip("0")

print("\nValor em hexadecimal:", hexa)

input()
