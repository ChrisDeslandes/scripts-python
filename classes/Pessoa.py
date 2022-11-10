class Pessoa:

    def __init__(self, nome, cpf, idade=""):
        self.__nome = str(nome)
        self.__cpf = str(cpf)
        self.__idade = str(idade)

    def getNome(self):
        return self.__nome

    def getCPF(self):
        return self.__cpf

    def getIdade(self):
        return self.__idade

    def setNome(self, nome):
        self.__nome = str(nome)

    def setCPF(self, cpf):
        self.__cpf = str(cpf)

    def setIdade(self, idade):
        self.__idade = str(idade)

    def cumprimentar(self):
        print("Olá, meu nome é " + self.getNome() + ("" if self.getIdade() == "" else " e tenho " + self.getIdade() + " anos de idade") + "!")

    def mostraDados(self):
        print(self.getNome() + ("" if self.getIdade() == "" else " (" + self.getIdade() + " anos)") + ": " + self.getCPF())
