from tabulate import tabulate
from colorama import init, Fore, Back, Style

init()  # PRECISA PRO COLORAMA

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print("\n-- COLORAMA --\n\n")
print(Fore.BLACK + Style.NORMAL + Back.YELLOW + "\nOi, eu sou preto com fundo amarelo!!!" + Back.RESET)
print(Fore.RED + "Já eu sou vermelho!!!")
print(Fore.GREEN + "Já eu sou verde!!!")
print(Fore.YELLOW + "Já eu sou amarelo!!!")
print(Fore.BLUE + "Já eu sou azul!!!")
print(Fore.MAGENTA + "Já eu sou magenta!!!")
print(Fore.CYAN + "Já eu sou ciano!!!" + Style.RESET_ALL)

print(Fore.BLACK + Style.BRIGHT + Back.YELLOW + "\nOi, eu sou preto com fundo amarelo e brilhante!!!" + Back.RESET)
print(Fore.RED + "Já eu sou vermelho e brilhante!!!")
print(Fore.GREEN + "Já eu sou verde e brilhante!!!")
print(Fore.YELLOW + "Já eu sou amarelo e brilhante!!!")
print(Fore.BLUE + "Já eu sou azul e brilhante!!!")
print(Fore.MAGENTA + "Já eu sou magenta e brilhante!!!")
print(Fore.CYAN + "Já eu sou ciano e brilhante!!!" + Style.RESET_ALL)

table = [["Christiano", 33], ["Daniel", 35], ["Joaquim", 67], ["Leslie", 64], ["Dedê", 89]]

# TESTE DE ARQUIVO TXT

headers = ["Nome", "Idade"]

f = open("C:/Users/user/Desktop/Tabulate - Teste.txt", "w")

f.write("plain:\n\n" + tabulate(table, headers, tablefmt="plain") + "\n\n\n\n" +
        "simple:\n\n" + tabulate(table, headers, tablefmt="simple") + "\n\n\n\n" +
        "github:\n\n" + tabulate(table, headers, tablefmt="github") + "\n\n\n\n" +
        "grid:\n\n" + tabulate(table, headers, tablefmt="grid", colalign=("center", "center")) + "\n\n\n\n" +
        "pipe:\n\n" + tabulate(table, headers, tablefmt="pipe") + "\n\n\n\n" +
        "orgtbl:\n\n" + tabulate(table, headers, tablefmt="orgtbl") + "\n\n\n\n" +
        "presto:\n\n" + tabulate(table, headers, tablefmt="presto") + "\n\n\n\n" +
        "pretty:\n\n" + tabulate(table, headers, tablefmt="pretty") + "\n\n\n\n" +
        "psql:\n\n" + tabulate(table, headers, tablefmt="psql") + "\n\n\n\n" +
        "rst:\n\n" + tabulate(table, headers, tablefmt="rst"))

f.close()

# MELHORES FORMATOS:

headers = [Style.BRIGHT + Fore.GREEN + "Nome" + Style.RESET_ALL, Style.BRIGHT + Fore.GREEN + "Idade" + Style.RESET_ALL]
print("\n\n\n-------------------------------------------------------------------------------------------------------------")
print("\n\n\n-- TABULATE --")
print("\n\n\nplain:\n\n" + tabulate(table, headers, tablefmt="plain") + "\n\n\n\n" +
      "simple:\n\n" + tabulate(table, headers, tablefmt="simple") + "\n\n\n\n" +
      "github:\n\n" + tabulate(table, headers, tablefmt="github") + "\n\n\n\n" +
      "grid:\n\n" + tabulate(table, headers, tablefmt="grid") + "\n\n\n\n" +
      "pipe:\n\n" + tabulate(table, headers, tablefmt="pipe") + "\n\n\n\n" +
      "orgtbl:\n\n" + tabulate(table, headers, tablefmt="orgtbl") + "\n\n\n\n" +
      "presto:\n\n" + tabulate(table, headers, tablefmt="presto") + "\n\n\n\n" +
      "pretty:\n\n" + tabulate(table, headers, tablefmt="pretty") + "\n\n\n\n" +
      "psql:\n\n" + tabulate(table, headers, tablefmt="psql") + "\n\n\n\n" +
      "rst:\n\n" + tabulate(table, headers, tablefmt="rst"))

input()
