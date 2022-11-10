while True:
    x = input("Digite uma palavra ou frase: ")
    y = x[::-1]

    print()

    for i in range(len(x)):
        print(x[0:i+1] + " " * (2 * (len(x) - i) - 1) + y[len(y) - (i + 1):])

    for i in range(len(y)-1, -1, -1):
        print(x[0:i] + " " * (2 * (len(x) - i) + 1) + y[len(y)-i:])

    print("\n")
    resp = input("Deseja recomeçar ('s' para Sim)? ").lower()
    if resp != "s" and resp != "sim":
        print("\n*** FIM DO PROGRAMA ***")
        break
    else: print("\n")
