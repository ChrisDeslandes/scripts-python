from classes.CPF import CPF

def entrada(c):
    while True:
        cpf = input("Digite os 9 primeiros dígitos do CPF: ")
        if c.formatacaoCPFSemCV_Ok(cpf):
            cpf = c.limparCPF(cpf)
            return cpf
        else:
            print("\nEntrada Inválida!\n")

def saida(c, estados):
    print("\nO CPF válido é: " + c)
    print("\nPossíveis locais de cadastramento deste CPF:")
    for i in estados:
        print("  - " + i)

def main():
    resp = "s"
    while resp != "n":
        c = CPF()
        cpf = entrada(c)
        cv = c.calcularDigVerif(cpf)
        saida(c.formatacaoCorretaCPF(cpf + cv), c.determinarProcedenciaCPF(cpf))

        resp = input("\n\nDeseja conferir outro CPF (\"s\" para Sim e \"n\" para Não)? ")
        if resp != "":
            resp = resp[0].lower()
        if resp == "n":
            print("\n--- FIM DO PROGRAMA ---")
        else:
            print("\n----------------------------------------------------------\n")

main()
