from loteria import Loteria

loteria = None
aposta = 0
numJogos = 0

def separador():
  print("\n------------------------------------------------------------------------------------------------\n")

def entrada():
  global acertos, aposta, numJogos
  while True:
    respTotal = input(" Digite o número total de dezenas do jogo (ex.: Mega Sena = 60, Quina = 80): ")
    respAposta = input("\n Digite o número de dezenas de cada aposta (ex.: Mega Sena = 6, Quina = 5): ")
    respNumJogos = input("\n Digite o número de jogos que o programa deve rodar (Quanto maior o número, menor o erro da probabilidade, porém o tempo para o programa rodar aumenta): ")
    try:
      numJogos = int(respNumJogos)
    except Exception:
      print("\n ERRO: Digite apenas números inteiros nos campos.")
      separador()
      continue
    if numJogos < 1:
      print("\n ERRO: O número de jogos que o programa deve rodar deve ser inteiro, positivo e não nulo.")
      separador()
      continue
    try:
      global loteria
      loteria = Loteria(respTotal, respAposta)
    except Exception as ex:
      print(f"\n ERRO: {ex}")
      separador()
      continue
    aposta = int(respAposta)
    break

def sair():
  separador()
  resp = input(" Deseja fazer mais um cálculo (n para Não)? ").strip().lower()
  respsNegativas = ["n", "não", "nao", "no"]
  if resp in respsNegativas: return True
  separador()
  return False

def app():
  while True:
    entrada()
    global loteria, numJogos, aposta
    soma = [0] * (aposta + 1)
    for _ in range(numJogos):
      loteria.sortear()
      soma[loteria.quantosAcertei(loteria.surpresinha())] += 1
    nums = ""
    print(f"\n\n RESULTADO:\n")
    for i in range(len(soma)):
      print(f"\n De {numJogos:,} jogos".replace(",",".") + ", " + f"{soma[i]:,} jogos resultaram em {i} acerto(s) e {loteria.aposta - i} erro(s).".replace(",","."))
      print(f"\tProbabilidade: {100 * soma[i] / numJogos:.15f} %".replace(".",","))
    if sair(): break

app()
