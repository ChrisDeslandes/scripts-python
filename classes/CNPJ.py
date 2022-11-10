import random

class CNPJ:

    def limparCNPJ(self, cnpj):
        return cnpj.replace(" ", "").replace(".", "").replace("-", "").replace("/", "")

    def formatacaoCNPJSemCV_Ok(self, cnpj):
        cnpj = self.limparCNPJ(cnpj)
        if len(cnpj) != 12:
            return False
        if cnpj == "000000000000" or cnpj == "111111111111" or cnpj == "222222222222" or cnpj == "333333333333" or cnpj == "444444444444" or cnpj == "555555555555" or cnpj == "666666666666" or cnpj == "777777777777" or cnpj == "888888888888" or cnpj == "999999999999":
            return False
        for i in cnpj:
            if i not in "0123456789":
                return False
        return True

    def formatacaoCNPJComCV_Ok(self, cnpj):
        cnpj = self.limparCNPJ(cnpj)
        if len(cnpj) != 14:
            return False
        if cnpj[:12] == "000000000000" or cnpj[:12] == "111111111111" or cnpj[:12] == "222222222222" or cnpj[:12] == "333333333333" or cnpj[:12] == "444444444444" or cnpj[:12] == "555555555555" or cnpj[:12] == "666666666666" or cnpj[:12] == "777777777777" or cnpj[:12] == "888888888888" or cnpj[:12] == "999999999999":
            return False
        for i in cnpj:
            if i not in "0123456789":
                return False
        return True

    def formatacaoCorretaCNPJ(self, cnpj):
        if self.formatacaoCNPJComCV_Ok(cnpj):
            cnpj = self.limparCNPJ(cnpj)
            return cnpj[:2] + "." + cnpj[2:5] + "." + cnpj[5:8] + "/" + cnpj[8:12] + "-" + cnpj[12:14]
        else:
            return "CNPJ Inválido"

    def calcularDigVerif(self, cnpj):
        cnpj = self.limparCNPJ(cnpj)[:12]
        if self.formatacaoCNPJSemCV_Ok(cnpj):
            soma = 0
            for i in range(4):
                soma += int(cnpj[i]) * (5 - i)
            for i in range(8):
                soma += int(cnpj[i + 4]) * (9 - i)
            pDig = 11 - (soma % 11)
            if pDig == 10 or pDig == 11:
                pDig = 0
            soma = 0
            for i in range(5):
                soma += int(cnpj[i]) * (6 - i)
            for i in range(7):
                soma += int(cnpj[i + 5]) * (9 - i)
            soma += pDig * 2
            sDig = 11 - (soma % 11)
            if sDig == 10 or sDig == 11:
                sDig = 0
            return str(pDig) + str(sDig)
        else:
            return "CNPJ Inválido"

    def verificarCNPJ_Valido(self, cnpj):
        cnpj = self.limparCNPJ(cnpj)
        resp = False
        if self.formatacaoCNPJComCV_Ok(cnpj):
            if self.calcularDigVerif(cnpj[:12]) == cnpj[12:14]:
                resp = True
        return resp

    def gerarCNPJAleatorio(self):
        cnpj = ""
        for _ in range(8):
            cnpj += str(random.randint(0, 9))
        cnpj += "0001"
        cnpj += self.calcularDigVerif(cnpj)

        return self.formatacaoCorretaCNPJ(cnpj)
