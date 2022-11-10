from numpy import random as rnd
import pandas as pd
from math import ceil

# O código possui erros!
# No caso descrito abaixo, por exemplo, os índices 10, 11, 12 e 13 nunca serão "sorteados"!
# No vídeo da aula, pode ocorrer erro de índice fora dos limites da tabela!

pop = 150
amostra = 11
k = ceil(pop / amostra)
acumuladorMax = pop - 1 - k * (amostra - 1)

acumulador = rnd.randint(0, acumuladorMax + 1)

sorteados = range(acumulador, pop, k)

base = pd.read_csv('C:\Chris\Python\Ciência de Dados\iris.csv')

base_final = base.loc[sorteados]
