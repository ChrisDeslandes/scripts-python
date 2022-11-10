from Probabilidade import Probabilidade
c = Probabilidade.combinacao

separador = "\n------------------------------------------------------------------------------------------------\n"

while 1:
  while 1:
    respTotal = input(" Digite o número total de dezenas do jogo (ex.: Mega Sena = 60, Quina = 80): ")
    respAposta = input("\n Digite o número de dezenas de cada aposta (ex.: Mega Sena = 6, Quina = 5): ")
    try:
      total = int(respTotal)
      aposta = int(respAposta)
    except Exception as e:
      print("\n ERRO: Digite apenas números inteiros nos campos.")
      print(separador)
      continue
    if total < aposta:
      print("\n ERRO: O número de dezenas da aposta não pode ser maior que o número total de dezenas do jogo!")
      print(separador)
      continue
    break
  
  totalPossibilidades = c(total, aposta)

  print(f"\n\n >>> Total = {total} dezenas | Aposta = {aposta} dezenas <<<")

  print("\n\n Probabilidade de:")

  for acertos in range(aposta + 1):
    if total < 2 * aposta: possibilidades = 0
    possibilidades = c(aposta, acertos) * c(total - aposta, aposta - acertos)
    aux = "" if possibilidades in [0,1] else f" = 1 em {totalPossibilidades / possibilidades:_.4f}".replace(".",",").replace("_",".")
    print(f"\n    - Acertar {acertos} " + ("dezena" if acertos == 1 else "dezenas") + f":\n      {possibilidades:,} em {totalPossibilidades:,}".replace(",",".") + \
          aux + \
          f" = {100 * possibilidades / totalPossibilidades:.15f} %".replace(".",","))

  print(separador)
  resp = input(" Deseja fazer mais um cálculo (n para Não)? ").strip().lower()
  respsNegativas = ["n","não","nao","no"]
  if resp in respsNegativas: break
  print(separador)
