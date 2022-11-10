import random as rnd

sorte = [14, 20, 34, 45, 46, 53]
sorte.sort()

tentativas = 0
quadras = 0
quinas = 0

nums = list(range(1, 61))

while True:
    tentativas += 1
    n = 0
    tentativa = rnd.sample(nums, 6)
    tentativa.sort()
    
    acertos = 0
    for i in tentativa:
        if i in sorte:
            acertos += 1

    strGanhou = ""
    if acertos == 4:
        quadras += 1
        strGanhou = " --- QUADRA"
    elif acertos == 5:
        quinas += 1
        strGanhou = " --- QUINA"
    elif acertos == 6:
        strGanhou = " --- SENA"
    
    strTentativa = ' - '.join(str(i).zfill(2) for i in tentativa)
    print(f"Tentativa nº {tentativas:,}".replace(",",".") + ": " + strTentativa + strGanhou)

    if acertos == 6: break

print(f"\n\nFinalmente!! Depois de {tentativas:,}".replace(",",".") + f" tentativas, você ganhou na mega!\n\n" + \
      f"Jogo: {sorte}\n\n" + \
      f"Você acertou também {quadras:,} quadras e {quinas:,} quinas!".replace(",","."))

input()
