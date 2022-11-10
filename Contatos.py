import pyodbc
import sys
from tabulate import tabulate
from colorama import init, Fore, Style    

def mostra():
    cursor.execute("SELECT * FROM Contatos;")
    num = 0
    for i in cursor:
        num += 1
    if num == 0:
        print("O banco de dados está vazio!")
    else:
        tabela = []
        for row in cursor.execute("SELECT * FROM Contatos;"):
            tabela.append([Fore.YELLOW + str(row.CPF) + Style.RESET_ALL,
                           Fore.YELLOW + str(row.__getattribute__("Primeiro Nome")) + Style.RESET_ALL,
                           Fore.YELLOW + str(row.__getattribute__("Último Nome")) + Style.RESET_ALL,
                           Fore.YELLOW + str(row.__getattribute__("Data de Nascimento")) + Style.RESET_ALL,
                           Fore.YELLOW + str(row.__getattribute__("Celular")) + Style.RESET_ALL,
                           Fore.YELLOW + str(row.__getattribute__("E-mail")) + Style.RESET_ALL])
        print()
        headers = [Fore.GREEN + Style.BRIGHT + "CPF" + Style.RESET_ALL,
                   Fore.GREEN + Style.BRIGHT + "Primeiro Nome" + Style.RESET_ALL,
                   Fore.GREEN + Style.BRIGHT + "Último Nome" + Style.RESET_ALL,
                   Fore.GREEN + Style.BRIGHT + "Data de Nascimento" + Style.RESET_ALL,
                   Fore.GREEN + Style.BRIGHT + "Celular" + Style.RESET_ALL,
                   Fore.GREEN + Style.BRIGHT + "E-mail" + Style.RESET_ALL]
        init()
        print(tabulate(tabela, headers, tablefmt="fancy_grid", colalign=("center", "center", "center", "center", "center", "center")))
    escolhe()

def escolhe():
    while 1:
        escolha = input("\n1 - Adicionar Contato\n2 - Excluir Contato\n3 - Atualizar Contato\n4 - Sair\n\nO que deseja fazer (1, 2, 3 ou 4)? ")
        if escolha.isdigit():
            escolha = int(escolha)
        else:
            continue
        separacao = "\n--------------------------------------------------------------------------------------------------------------------------\n"
        if escolha == 1:
            # Adiciona Contato
            while 1:
                incpf = input("\nDigite o CPF do novo contato (ou 'C' para cancelar): ")
                incpf = incpf.replace(" ", "")
                if incpf == "c" or incpf == "C":
                    print(separacao)
                    mostra()
                    return
                incpf = incpf.replace(".", "")
                incpf = incpf.replace("-", "")
                if len(incpf) == 11 and incpf.isdigit():
                    incpf = incpf[0:3] + "." + incpf[3:6] + "." + incpf[6:9] + "-" + incpf[9:11]
                    break
                else:
                    print("Formato de CPF inválido!")
            cursor.execute("SELECT * FROM Contatos WHERE CPF = ?;", incpf)
            num = 0
            for _ in cursor:
                num += 1
            if num > 0:
                print("\nCPF já cadastrado!")
            else:
                inpn = input("\nDigite o primeiro nome do novo contato: ")
                inun = input("\nDigite o último nome do novo contato: ")
                indn = input("\nDigite a data de nascimento do novo contato (dd/mm/aaaa): ")
                while 1:
                    incel = input("\nDigite o celular do contato no formato (99) 99999-9999: ")
                    incel = incel.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
                    if incel == "" or (len(incel) == 11 and incel.isdigit()):
                        incel = "(" + incel[0:2] + ") " + incel[2:7] + "-" + incel[7:11]
                        break
                    else:
                        print("Formato de celular inválido!")
                inem = input("\nDigite o e-mail do novo contato: ")
                query = "INSERT INTO Contatos ([CPF], [Primeiro Nome], [Último Nome], [Data de Nascimento], [Celular], [E-mail]) VALUES (?,?,?,?,?,?);"
                cursor.execute(query, incpf, inpn, inun, indn, incel, inem)
                print(separacao)
                mostra()
        elif escolha == 2:
            # Exclui Contato
            while 1:
                incpf = input("\nDigite o CPF do contato que deseja excluir (ou 'C' para cancelar): ")
                incpf = incpf.replace(" ", "")
                if incpf == "c" or incpf == "C":
                    print(separacao)
                    mostra()
                    return
                incpf = incpf.replace(".", "")
                incpf = incpf.replace("-", "")
                if len(incpf) == 11 and incpf.isdigit():
                    incpf = incpf[0:3] + "." + incpf[3:6] + "." + incpf[6:9] + "-" + incpf[9:11]
                    break
                else:
                    print("Formato de CPF inválido!")
            cursor.execute("SELECT * FROM Contatos WHERE CPF = ?;", incpf)
            num = 0
            for _ in cursor:
                num += 1
            if num == 0:
                print("\nO CPF informado não consta no banco de dados!")
            else:
                query = "DELETE FROM Contatos WHERE CPF = ?;"
                cursor.execute(query, incpf)
                print(separacao)
                mostra()
        elif escolha == 3:
            # Atualiza Contato
            while 1:
                incpf = input("\nDigite o CPF do contato que deseja atualizar (ou 'C' para cancelar): ")
                incpf = incpf.replace(" ", "")
                if incpf == "c" or incpf == "C":
                    print(separacao)
                    mostra()
                    return
                incpf = incpf.replace(".", "")
                incpf = incpf.replace("-", "")
                if len(incpf) == 11 and incpf.isdigit():
                    incpf = incpf[0:3] + "." + incpf[3:6] + "." + incpf[6:9] + "-" + incpf[9:11]
                    break
                else:
                    print("Formato de CPF inválido!")
            cursor.execute("SELECT * FROM Contatos WHERE CPF = ?;", incpf)
            num = 0
            for _ in cursor:
                num += 1
            if num == 0:
                print("\nO CPF informado não consta no banco de dados!")
            else:
                inpn = input("\nDigite o primeiro nome do contato: ")
                inun = input("\nDigite o último nome do contato: ")
                indn = input("\nDigite a data de nascimento do contato (dd/mm/aaaa): ")
                while 1:
                    incel = input("\nDigite o celular do contato no formato (99) 99999-9999: ")
                    incel = incel.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
                    if incel == "" or (len(incel) == 11 and incel.isdigit()):
                        incel = "(" + incel[0:2] + ") " + incel[2:7] + "-" + incel[7:11]
                        break
                    else:
                        print("Formato de celular inválido!")
                inem = input("\nDigite o e-mail do contato: ")
                query = "UPDATE Contatos SET [Primeiro Nome] = ?, [Último Nome] = ?, [Data de Nascimento] = ?, [Celular] = ?, [E-mail] = ? WHERE CPF = ?;"
                cursor.execute(query, inpn, inun, indn, incel, inem, incpf)
                print(separacao)
                mostra()
        elif escolha == 4:
            # Sai do programa
            conn.close()
            sys.exit()

conn = pyodbc.connect("Server=CHRISDESLANDES;Database=Agenda;Trusted_Connection=yes;", autocommit=True)
cursor = conn.cursor()
mostra()
