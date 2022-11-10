import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from yahooquery import Ticker
import datetime

def mostraAcao(acao):
    t = Ticker(acao)
    t = t.history(period="1d",  interval = "1m")
    minimo = maximo = t.close[0]
    for i in t.close:
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i
    x = []
    for i in t.index:
        x.append(i[1])
    fig = plt.figure(acao)
    fig.suptitle(acao, fontsize=22)
    graf = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    graf.set_xlabel("Data")
    graf.set_ylabel("Valor")
    graf.grid(which="both")
    graf.set_ylim(minimo - (maximo - minimo)/4 , maximo + (maximo - minimo)/4)
    graf.yaxis.set_minor_locator(MultipleLocator(1))
    graf.plot(x,t.close,"b", marker=".")
    print(acao + "\n\nÚltima atualização:\nData / Hora: " + str(t.index[len(t.index) - 1][1].strftime("%d/%m/%Y / %H:%M:%S")) + "\nValor: R$" + str("%.2f" % t.close[len(t.close) - 1]))

mostraAcao("PETR4.SA")
print("\n\n")
mostraAcao("VALE3.SA")
plt.show()
