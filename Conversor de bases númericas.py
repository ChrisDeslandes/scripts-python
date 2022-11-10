import datetime

hex = {"0": "0000",
       "1": "0001",
       "2": "0010",
       "3": "0011",
       "4": "0100",
       "5": "0101",
       "6": "0110",
       "7": "0111",
       "8": "1000",
       "9": "1001",
       "A": "1010",
       "B": "1011",
       "C": "1100",
       "D": "1101",
       "E": "1110",
       "F": "1111"}

oct = {"0": "000",
       "1": "001",
       "2": "010",
       "3": "011",
       "4": "100",
       "5": "101",
       "6": "110",
       "7": "111"}

while True:
    print()
    print("  " + datetime.datetime.now().strftime("%d/%m/%Y - %H:%M\n"))

    while True:
        print("  ------------------------------------------------------------------------------\n")
        print("  Você deseja converter um número de qual base numérica?\n\n  1 - Binária\n  2 - Octal\n  3 - Decimal\n  4 - Hexadecimal\n")        
        escolha = input("  Digite a opção desejada (1, 2, 3 ou 4): ")    
        print()
        if escolha.isnumeric():
            escolha = int(escolha)
            if (escolha >= 1 and escolha <= 4):
                break
            else:
                print("  Opção não existente!\n")
        else:
            print("  Opção não existente!\n")

    while True:
        num = input("  Digite o número que deseja converter, na base especificada: ").upper()
        correto = True
        for digito in num:
            if (escolha == 1):
                if not digito in "01":
                    correto = False
            elif (escolha == 2):
                if not digito in "01234567":
                    correto = False
            elif (escolha == 3):
                if not digito in "0123456789":
                    correto = False
            else:
                if not digito in "0123456789ABCDEF":
                    correto = False
        if correto == False:
            print("  O valor inserido não é um número inteiro compatível com a base especificada!\n")
        else:
            while (len(num) > 1 and num[0] == "0"):
                num = num[1:]
            break
        
    numd = ""
    numb = ""
    numo = ""
    numh = ""
    if (escolha == 1):
        numb = num        
    elif (escolha == 2):
        for i in num:
            numb += oct[i]
    elif (escolha == 3):
        n = int(num)
        while (n != 0):
            numb = str(n % 2) + numb
            n = int(n / 2)        
    else:
        for i in num:
            numb += hex[i]
    
    while (len(numb) > 1 and numb[0] == "0"):
        numb = numb[1:]
    
    if escolha != 3:
        aux = 0
        auxi = 0
        for i in range(len(numb) - 1, -1, -1):
            aux += int(numb[i]) * pow(2, auxi)
            auxi += 1
        numd = str(aux)
    else:
        numd = num

    if escolha != 2:
        aux = ""
        auxi = 0
        for i in range(len(numb) - 1, -1, -1):
            aux = numb[i] + aux
            auxi += 1
            if auxi == 3 or i == 0:
                auxi = 0
                aux = aux.zfill(3)
                numo = list(oct.keys())[list(oct.values()).index(aux)] + numo
                aux = ""
    else:
        numo = num
        
    if escolha != 4:
        aux = ""
        auxi = 0
        for i in range(len(numb) - 1, -1, -1):
            aux = numb[i] + aux
            auxi += 1
            if auxi == 4 or i == 0:
                auxi = 0
                aux = aux.zfill(4)
                numh = list(hex.keys())[list(hex.values()).index(aux)] + numh
                aux = ""
    else:
        numh = num
    
    print("\n\n  Binário = " + numb + "\n\n  Octal = " + numo + "\n\n  Decimal = " + numd + "\n\n  Hexadecimal = " + numh)
    print("\n  ------------------------------------------------------------------------------")
    while True:
        continua = input("\n  Deseja fazer outra operação? (S/N) ").upper()
        if (continua == "N" or continua == "S"): break
        else: print("  Por favor, somente 'S' ou 'N' como resposta.")
    if (continua == "N"): break
    else: print("\n  ==============================================================================")
