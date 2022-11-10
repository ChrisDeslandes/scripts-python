import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig1 = plt.figure("Gráficos de Equações")
fig1.suptitle("Gráficos de Equações", fontsize=22)

graf1 = fig1.add_axes([0.1, 0.55, 0.35, 0.35])
graf2 = fig1.add_axes([0.55, 0.55, 0.35, 0.35])
graf3 = fig1.add_axes([0.1, 0.1, 0.35, 0.35])
graf4 = fig1.add_axes([0.55, 0.1, 0.35, 0.35])

i = np.linspace(-10, 10, 201)

w = -4/7*i + 4
wLabel = "w = -4i/7 + 4"
x = i**2
xLabel = "x = i²"
y = i**3
yLabel = "y = i³"
z = i**4
zLabel = "z = i^4"

graf1.plot(i, w, "r--", label = wLabel)
graf1.set_title("Equação de 1º grau")
graf1.set_xlabel("i")
graf1.set_ylabel("w")
graf1.grid(True)
graf1.legend()

graf2.plot(i, x, "b", label = xLabel)
graf2.set_title("Equação de 2º grau")
graf2.set_xlabel("i")
graf2.set_ylabel("x")
graf2.grid(True)
graf2.legend()

graf3.plot(i, y, "g--", label = yLabel)
graf3.set_title("Equação de 3º grau")
graf3.set_xlabel("i")
graf3.set_ylabel("y")
graf3.grid(True)
graf3.legend()

graf4.plot(i, z, "k-.", label = zLabel)
graf4.set_title("Equação de 4º grau")
graf4.set_xlabel("i")
graf4.set_ylabel("z")
graf4.grid(True)
graf4.legend()

manager = plt.get_current_fig_manager()
manager.window.state('zoomed')  # janela maximizada

fig2 = plt.figure("Gráficos de Seno e Cosseno")
fig2.suptitle("Gráficos de Seno e Cosseno", fontsize=22)

graf = fig2.add_axes([0.1, 0.1, 0.8, 0.8])

graus = np.linspace(-360, 360, 49)
t = np.sin(graus * np.pi / 180)
u = np.cos(graus * np.pi / 180)

graf.plot(graus, t, "b", label="t = sen(x)")
graf.plot(graus, u, "r", label="u = cos(x)")
graf.set_xlabel("x (Graus)")
graf.grid(which="both")
graf.legend(prop={'size': 16})
graf.set_xlim(-360, 360)
graf.xaxis.set_major_locator(MultipleLocator(90))
graf.xaxis.set_minor_locator(MultipleLocator(30))

manager = plt.get_current_fig_manager()
manager.window.state('zoomed') # janela maximizada

plt.show()
