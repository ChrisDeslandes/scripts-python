from datetime import datetime as dt

def qtosSegundos(td):
    return td.days * 24 * 60 * 60 + td.seconds

def qtosMinutos(td):
    return td.days * 24 * 60 + int(td.seconds / 60)

def qtasHoras(td):
    return int(td.days * 24 + int(td.seconds / 3600))

def qtosDias(td):
    return td.days

def qtasSemanas(td):
    return int(td.days / 7)

sep = "\n------------------------------------------------------------------------------------\n"

while 1:
    while 1:
        try:
            resp = input("Digite a data e a hora em que nasceu no formato \"dd/mm/aaaa HH:MM\": ")
            fmt = "%d/%m/%Y %H:%M"
            nasceu = dt.strptime(resp, fmt)
        except:
            print("\nPor favor, insira as informações no formato pedido...")
            print(sep)
        else:
            break

    agora = dt.now()

    dif = agora - nasceu

    print(sep)

    print(f"Você tem {qtasSemanas(dif):,} semanas completas de vida!".replace(",","."))

    print(sep)

    print(f"Você tem {qtosDias(dif):,} dias completos de vida!".replace(",","."))

    print(sep)

    print(f"Você tem {qtasHoras(dif):,} horas completas de vida!".replace(",","."))

    print(sep)

    print(f"Você tem {qtosMinutos(dif):,} minutos completos de vida!".replace(",","."))

    print(sep)

    print(f"Você tem {qtosSegundos(dif):,} segundos completos de vida!".replace(",","."))

    print(sep)

    sair = input("Você deseja sair do programa (\"s\" para Sim)? ").lower()
    if sair == "s": break
    else: print(sep)
