from random import sample
from math import comb

class Loteria:

  def __init__(self, total, aposta):
    t = 0
    a = 0
    try:
      t = int(total)
      a = int(aposta)
    except:
      raise Exception("Digite apenas números inteiros nos campos!")
    if a < 1 or t < 1:
      raise Exception("Todos os valores devem ser positivos e não nulos!")
    if a > t:
      raise Exception("O número de dezenas da aposta não pode ser maior que o número total de dezenas do jogo!")
    self.total = t
    self.aposta = a
    self.numeros = list(range(1, t + 1))
    self.numsSorteados = []
    self.jaHouveSorteio = False

  def sortear(self):
    self.numsSorteados = sample(self.numeros, self.aposta)
    self.numsSorteados.sort()
    self.jaHouveSorteio = True

  def cancelarSorteio(self):
    self.numsSorteados = []
    self.jaHouveSorteio = False

  def quantosAcertei(self, tentativa):
    soma = 0
    for i in tentativa:
      if i in self.numsSorteados: soma += 1
    return soma
    
  def __str__(self):
    if self.jaHouveSorteio:
      sorteados = "Números sorteados: "
      for i in range(len(self.numsSorteados)):
        sorteados += str(self.numsSorteados[i])
        if not (i == len(self.numsSorteados) - 1): sorteados += " - "
        else:
          sorteados = "O sorteio ainda não foi realizado!"
          return f"Sorteio de {self.aposta} dezenas em um total de {self.total} dezenas!\n{sorteados}"

  def numTotalJogosPossiveis(self):
    return comb(self.total, self.aposta)

  def possibilidades(self, nAcertos):
    return comb(self.aposta, nAcertos) * comb(self.total - self.aposta, self.aposta - nAcertos)

  def probabilidade(self, nAcertos):
    return self.possibilidades(nAcertos) / self.numTotalJogosPossiveis()

  def probabilidadeInversa(self, nAcertos):
    return 1 / self.probabilidade(nAcertos)

  def surpresinha(self):
    numsSurpresinha = sample(self.numeros, self.aposta)
    numsSurpresinha.sort()
    return numsSurpresinha
