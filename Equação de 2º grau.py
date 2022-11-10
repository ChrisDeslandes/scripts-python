while 1:
    while 1:
        try:
            a = float(input("Digite o valor de 'a': "))
            b = float(input("Digite o valor de 'b': "))
            c = float(input("Digite o valor de 'c': "))
            break
        except ValueError:
            print("\nValor em formatação incorreta!\nEntre com os valores certos...\n")

    auxa = "- " + str(-1 * a) if a < 0 else str(a)
    auxb = " - " + str(-1 * b) if b < 0 else " + " + str(b)
    auxc = " - " + str(-1 * c) if c < 0 else " + " + str(c)

    eq = "y = {}x²{}x{}".format(auxa,auxb,auxc)
    
    print()
    print(eq)

    x1 = (-1 * b + ((b ** 2 - (4 * a * c)) ** 0.5)) / (2 * a)
    x2 = (-1 * b - ((b ** 2 - (4 * a * c)) ** 0.5)) / (2 * a)

    print("\nx1 = {:.3f}\nx2 = {:.3f}".format(x1,x2))

    resp = input("\nDeseja fazer outra operação? (S/N) ")
    if resp == "N" or resp == "n": break
    else: print()
