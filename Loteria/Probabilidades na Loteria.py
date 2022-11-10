from loteria import Loteria
import matplotlib.pyplot as plt

loteria = None

def separador():
  print("\n------------------------------------------------------------------------------------------------\n")

def entrada():
  while True:
    respTotal = input(" Digite o número total de dezenas do jogo (ex.: Mega Sena = 60, Quina = 80): ")
    respAposta = input("\n Digite o número de dezenas de cada aposta (ex.: Mega Sena = 6, Quina = 5): ")
    try:
      global loteria
      loteria = Loteria(respTotal, respAposta)
    except Exception as ex:
      print(f"\n ERRO: {ex}")
      separador()
      continue
    break

def saida():
    global loteria
    print(f"\n\n >>> Total = {loteria.total} dezenas | Aposta = {loteria.aposta} dezenas <<<")
    print("\n\n Probabilidade de:")
    for acertos in range(loteria.aposta + 1):
      possibilidades = loteria.possibilidades(acertos)
      aux = "" if possibilidades in [0,1] else f" = 1 em {loteria.probabilidadeInversa(acertos):_.4f}".replace(".",",").replace("_",".")
      print(f"\n\t- Acertar {acertos} " + ("dezena:" if acertos == 1 else "dezenas:") + \
            f"\n\t\t{possibilidades:,} em {loteria.numTotalJogosPossiveis():,}".replace(",",".") + aux + \
            f" = {100 * loteria.probabilidade(acertos):.15f} %".replace(".",","))

# def plotar():
#     global loteria
#     x = list(range(0, loteria.aposta + 1))
#     y = []
#     for acertos in range(loteria.aposta + 1):
#         y.append(loteria.probabilidade(acertos))
#     plt.bar(x, y)
#     plt.title("Probabilidade de acertos na loteria")
#     plt.xlabel("Número de acertos")
#     plt.ylabel("Probabilidade")
#     plt.show()

def fechar():
  separador()
  resp = input(" Deseja fazer mais um cálculo (n para Não)? ").strip().lower()
  respsNegativas = ["n","não","nao","no"]
  if resp in respsNegativas: return True
  separador()
  return False

def app():
  while True:
    entrada()
    saida()
    # plotar()
    if fechar(): break

app()
