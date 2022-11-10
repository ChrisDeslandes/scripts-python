print("\n  ==============================================================================\n")

dicionario = {"A": ".-",
              "B": "-...",
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----"}

while True:
    frase = input("  Digite a frase a ser escrita em código Morse: ").upper()
    print()
    for i in frase:
        if i in dicionario:
            print("  " + i + ": " + dicionario[i])
    print("\n  ------------------------------------------------------------------------------")
    while True:
        continua = input("\n  Deseja fazer outra operação? (S/N) ").upper()
        if continua == "N" or continua == "S": break
        else: print("  Por favor, somente 'S' ou 'N' como resposta.")
    if continua == "N": break
    else: print("\n  ==============================================================================\n")
