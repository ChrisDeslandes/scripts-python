from Probabilidade import Probabilidade
c = Probabilidade.combinacao

brancas = int(input("Digite o número de meias brancas presentes na caixa: "))
pretas = int(input("Digite o número de meias pretas presentes na caixa: "))
azuis = int(input("Digite o número de meias azuis presentes na caixa: "))

nMeiasRetiradas = int(input("\nDigite o número de meias a serem sorteadas aleatoriamente: "))

total = brancas + pretas + azuis

possibilidades = []

totalPossibilidades = c(total,nMeiasRetiradas)

for nB in range(nMeiasRetiradas + 1 if nMeiasRetiradas < brancas else brancas + 1):
  for nP in range(nMeiasRetiradas + 1 if nMeiasRetiradas < pretas else pretas + 1):
    for nA in range(nMeiasRetiradas + 1 if nMeiasRetiradas < azuis else azuis + 1):
      possibilidades.append([nB, nP, nA])
	
for i in range(len(possibilidades) - 1, -1, -1):
  if sum(possibilidades[i]) != nMeiasRetiradas:
    possibilidades.pop(i)

print(f"\n\nPossibilidades ao serem sorteadas {nMeiasRetiradas} meias de um total de {brancas} meias brancas, {pretas} meias pretas e {azuis} meias azuis:\n")

for pos in possibilidades:
  valor = c(brancas, pos[0]) * c(pretas, pos[1]) * c(azuis, pos[2])
  print(str(pos[0]) + "B + " + str(pos[1]) + "P + " + str(pos[2]) + "A   =>   " + \
        "C(" + str(brancas) + "," + str(pos[0]) + ") * " + \
        "C(" + str(pretas) + "," + str(pos[1]) + ") * " + \
        "C(" + str(azuis) + "," + str(pos[2]) + ") = " + \
        f"{valor:,}".replace(",","."))

print(f"\nNúmero total de possibilidades = {totalPossibilidades:,}\n\n".replace(",","."))

print("Digite... (Você deve especificar todos os números possíveis. Se não for fixo, separe os números por vírgula)\n")

b = list(map(int, input("...o número desejado de meias brancas: ").split(",")))
p = list(map(int, input("...o número desejado de meias pretas: ").split(",")))
a = list(map(int, input("...o número desejado de meias azuis: ").split(",")))

for i in range(len(possibilidades) - 1, -1, -1):
  if (possibilidades[i][0] not in b) or (possibilidades[i][1] not in p) or (possibilidades[i][2] not in a):
    possibilidades.pop(i)

soma = 0

print("\nRespostas possíveis: ")
for pos in possibilidades:
  valor = c(brancas, pos[0]) * c(pretas, pos[1]) * c(azuis, pos[2])
  soma += valor
  print(str(pos[0]) + "B + " + str(pos[1]) + "P + " + str(pos[2]) + "A   =>   " + \
        "C(" + str(brancas) + "," + str(pos[0]) + ") * " + \
        "C(" + str(pretas) + "," + str(pos[1]) + ") * " + \
        "C(" + str(azuis) + "," + str(pos[2]) + ") = " + f"{valor:,}".replace(",","."))

print(f"\nSoma das respostas possíveis = {soma:,}".replace(",","."))
print(f"\nSoma de todas as possibilidades = {totalPossibilidades:,}".replace(",","."))

print (f"\n\nA probabilidade é de {soma:_} em {totalPossibilidades:_} = {100 * soma / totalPossibilidades:_.4f} %".replace(".",",").replace("_","."))

input()
