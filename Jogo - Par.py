from classes.JogoPar import Par, Jogo
from numpy import random

lista = []
jogo = None

def sorteia():
    x = []
    for i in range(1, 17):
        while 1:
            loc1 = random.randint(32) + 1
            if not loc1 in x:
                x.append(loc1)
                break
        while 1:
            loc2 = random.randint(32) + 1
            if not loc2 in x:
                x.append(loc2)
                break
        lista.append(Par(i, loc1, loc2))
    global jogo
    jogo = Jogo(lista, "Tema Qualquer")

sorteia()

for i in jogo.pares:
    print(str(i.tag) + ":\n" + str(i.q1) + " - " + str(i.q2) + "\n")

input()
