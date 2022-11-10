print("\n  ==============================================================================\n")

dicionario = "AÁÂÃÀÄBCÇDEÉÊÈËFGHIÍÎÌÏJKLMNÑOÓÔÕÒÖPQRSTUÚÛÙÜVWXYZaáâãàäbcçdeéêèëfghiíîìïjklmnñoóôõòöpqrstuúûùüvwxyz0123456789 \\!?.,;:-*+/=_|@#$%&()[]{}<>ªº'\"¹²³£¢¬§"

matriz = []

for i in range(len(dicionario)):
    matriz.append(dicionario)
    dicionario = dicionario[1:] + dicionario[0]

while True:
    while True:
        opcao = input("  Você deseja cifrar ou decifrar uma frase? (C para cifrar, D para decifrar) ").upper().replace(" ", "")
        if (opcao != "") and (opcao in "CD"): break
        else: print("  Por favor, somente 'C' ou 'D' como resposta.\n")
    print()
    if opcao == "C":
        frase = input("  Digite a frase a ser cifrada: ")
        while True:
            codigo = input("\n  Digite a palavra/frase a ser usada como cifra: ")
            for i in codigo:
                if i not in dicionario:
                    i = ""
            if len(codigo) > len(frase): print("  A palavra usada como cifra não pode ter mais caracteres que a frase a ser cifrada!")
            else: break
        ind = 0
        for i in range(len(codigo), len(frase)):
            codigo += codigo[ind]
            ind += 1
            if ind > len(codigo) - 1: ind = 0
        print()
        resposta = "  A frase cifrada usando a Cifra de Vigenère é: "
        for i in range(len(frase)):
            if frase[i] in dicionario: resposta += matriz[dicionario.index(codigo[i])][dicionario.index(frase[i])]
    else:
        frase = input("  Digite a frase a ser decifrada: ")
        while True:
            codigo = input("\n  Digite a palavra a ser usada como cifra: ")
            for i in codigo:
                if i not in dicionario: i = ""
            if len(codigo) > len(frase): print("A palavra usada como cifra não pode ter mais caracteres que a frase a ser decifrada!")
            else: break
        ind = 0
        for i in range(len(codigo), len(frase)):
            codigo += codigo[ind]
            ind += 1
            if ind > len(codigo) - 1: ind = 0
        print()
        resposta = "  A frase decifrada usando a Cifra de Vigenère é: "
        for i in range(len(frase)):
            if frase[i] in dicionario: resposta += dicionario[matriz[dicionario.index(codigo[i])].index(frase[i])]
        
    print(resposta + "\n  ------------------------------------------------------------------------------")

    while True:
        continua = input("\n  Deseja fazer outra operação? (S/N) ").upper()
        if continua in "SN": break
        else: print("  Por favor, somente 'S' ou 'N' como resposta.")
    if continua == "N": break
    else: print("\n  ==============================================================================\n")
