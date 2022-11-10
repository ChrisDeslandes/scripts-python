print("\n  ==============================================================================\n")

dicionario = "AÁÂÃÀÄBCÇDEÉÊÈËFGHIÍÎÌÏJKLMNÑOÓÔÕÒÖPQRSTUÚÛÙÜVWXYZaáâãàäbcçdeéêèëfghiíîìïjklmnñoóôõòöpqrstuúûùüvwxyz0123456789 \\!?.,;-*+/=_|:@#$%&()[]{}<>ªº'\"¹²³£¢¬§"

while True:
    while True:
        opcao = input("  Você deseja cifrar ou decifrar uma frase? (C para cifrar, D para decifrar) ").upper().replace(" ","")
        if (opcao in "CD") and (opcao != ""): break
        else: print("  Por favor, somente 'C' ou 'D' como resposta.\n")
    print()
    if opcao == "C":
        frase = input("  Digite a frase a ser cifrada: ")
        print()
        resposta = "  A frase cifrada usando a Cifra de César é: "
        for i in frase:
            if i in dicionario:
                if dicionario.index(i) < len(dicionario) - 3:
                    resposta += dicionario[dicionario.index(i) + 3]
                else:
                    resposta += dicionario[dicionario.index(i) - len(dicionario) + 3]
    else:
        frase = input("  Digite a frase a ser decifrada: ")
        print()
        resposta = "  A frase decifrada usando a Cifra de César é: "
        for i in frase:
            if i in dicionario:
                if dicionario.index(i) >= 3:
                    resposta += dicionario[dicionario.index(i) - 3]
                else:
                    resposta += dicionario[dicionario.index(i) + len(dicionario) - 3]
                
    print(resposta)
        
    print("\n  ------------------------------------------------------------------------------")

    while True:
        continua = input("\n  Deseja fazer outra operação? (S/N) ").upper()
        if continua in "SN": break
        else: print("  Por favor, somente 'S' ou 'N' como resposta.")
    if (continua == "N"): break
    else: print("\n  ==============================================================================\n")
