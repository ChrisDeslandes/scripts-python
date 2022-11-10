import random

class CPF:

    def limparCPF(self, cpf):
        return cpf.replace(" ", "").replace(".", "").replace("-", "")

    def formatacaoCPF_Ok(self, cpf, nDig):
        cpf = self.limparCPF(cpf)
        if len(cpf) != nDig:
            return False
        if cpf[:9] in list(map(lambda n: n * 9, "0123456789")):
            return False
        for i in cpf:
            if i not in "0123456789":
                return False
        return True

    def formatacaoCPFSemCV_Ok(self, cpf):
        return self.formatacaoCPF_Ok(cpf, 9)

    def formatacaoCPFComCV_Ok(self, cpf):
        return self.formatacaoCPF_Ok(cpf, 11)

    def formatacaoCorretaCPF(self, cpf):
        if (self.formatacaoCPFComCV_Ok):
            cpf = self.limparCPF(cpf)
            return cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]
        else:
            return "CPF Inválido"

    def calcularDigVerif(self, cpf):
        cpf = self.limparCPF(cpf)[:9]
        if self.formatacaoCPFSemCV_Ok(cpf):
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (10 - i)
            pDig = 11 - (soma % 11)
            if pDig in [10, 11]:
                pDig = 0
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (11 - i)
            soma += pDig * 2
            sDig = 11 - (soma % 11)
            if sDig in [10, 11]:
                sDig = 0
            return str(pDig) + str(sDig)
        else:
            return "CPF Inválido"

    def determinarProcedenciaCPF(self, cpf):
        cpf = self.limparCPF(cpf)[:9]
        if self.formatacaoCPFSemCV_Ok(cpf):
            digEstado = int(cpf[8])
            estados = ""
            if digEstado == 0:
                estados = ["Rio Grande do Sul"]
            elif digEstado == 1:
                estados = ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul", "Tocantins"]
            elif digEstado == 2:
                estados = ["Amazonas", "Pará", "Roraima", "Amapá", "Acre", "Rondônia"]
            elif digEstado == 3:
                estados = ["Ceará", "Maranhão", "Piauí"]
            elif digEstado == 4:
                estados = ["Paraíba", "Pernambuco", "Alagoas", "Rio Grande do Norte"]
            elif digEstado == 5:
                estados = ["Bahia", "Sergipe"]
            elif digEstado == 6:
                estados = ["Minas Gerais"]
            elif digEstado == 7:
                estados = ["Rio de Janeiro", "Espírito Santo"]
            elif digEstado == 8:
                estados = ["São Paulo"]
            elif digEstado == 9:
                estados = ["Paraná", "Santa Catarina"]
            return estados
        else:
            return "CPF Inválido"

    def verificarCPF_Valido(self, cpf):
        cpf = self.limparCPF(cpf)
        if self.formatacaoCPFComCV_Ok(cpf):
            if self.calcularDigVerif(cpf[:9]) == cpf[9:11]:
                return True
        return False

    def gerarCPFAleatorio(self, siglaEstado):
        siglaEstado = siglaEstado.upper()

        digEstado = ""
        if siglaEstado in ["RS"]:
            digEstado += "0"
        elif siglaEstado in ["DF", "GO", "MT", "MS", "TO"]:
            digEstado += "1"
        elif siglaEstado in ["AM", "PA", "RR", "AP", "AC", "RO"]:
            digEstado += "2"
        elif siglaEstado in ["CE", "MA", "PI"]:
            digEstado += "3"
        elif siglaEstado in ["PB", "PE", "AL", "RN"]:
            digEstado += "4"
        elif siglaEstado in ["BA", "SE"]:
            digEstado += "5"
        elif siglaEstado in ["MG"]:
            digEstado += "6"
        elif siglaEstado in ["RJ", "ES"]:
            digEstado += "7"
        elif siglaEstado in ["SP"]:
            digEstado += "8"
        elif siglaEstado in ["PR", "SC"]:
            digEstado += "9"
        else:
            return False

        cpf = ""
        for _ in range(8):
            cpf += str(random.randint(0, 9))
        cpf += digEstado
        cpf += self.calcularDigVerif(cpf)

        return self.formatacaoCorretaCPF(cpf)
