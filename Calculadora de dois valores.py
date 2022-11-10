import datetime

while True:
    print()
    print(datetime.datetime.now().strftime("%d/%m/%Y - %H:%M\n"))

    while True:
        print("---------------------------------------------\n")
        print("Escolha uma opção:\n\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n")
        
        escolha = input("Digite a opção desejada (1, 2, 3 ou 4): ")    
        print()
    
        try:
            escolha = int(escolha)
            if (escolha <= 4 and escolha >= 1):
                break
            else:
                print("Opção não existente!\n")
        except ValueError:
            print("Opção não existente!\n")

    while True:
        try:
            global x, y
            x, y = input("Digite os dois números que deseja operar, separados por espaço, e depois tecle enter: ").split()
            try:
                x = float(x)
                y = float(y)
                break
            except ValueError:
                print("Somente dois NÚMEROS separados por espaço!\n")
        except ValueError:
            print("Somente dois NÚMEROS separados por espaço!\n")

    aux = str()
    if (escolha == 1):
        res = x + y
        aux = "x + y = "
    elif (escolha == 2):
        res = x - y
        aux = "x - y = "
    elif (escolha == 3):
        res = x * y
        aux = "x * y = "
    elif (escolha == 4):
        res = x / y
        aux = "x / y = "

    print("\n{}{:.3f}".format(aux, res))
    print("\n---------------------------------------------")
    continua = str()
    while True:
        continua = input("\nDeseja fazer outra operação? (S/N) ")
        if (continua == "N" or continua == "S" or continua == "n" or continua == "s"): break
        else: print("Por favor, somente 'S' ou 'N' como resposta.")
    if (continua == "N" or continua == "n"): break
    else: print("\n---------------------------------------------")
