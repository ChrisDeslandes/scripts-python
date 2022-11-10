from random import sample
import matplotlib.pyplot as plt

dado = [1, 2, 3, 4, 5, 6]

resultados = [0] * 26

for i in range(1000000):
    soma = 0
    for j in range(5):
        soma += sample(dado, 1)[0]
    resultados[soma - 5] += 1

plt.bar(list(range(5,31)), resultados)
plt.title("Soma de 5 dados (1.000.000 de vezes)")
plt.xlabel("Soma")
plt.ylabel("Nº de vezes")
plt.show()

input()
