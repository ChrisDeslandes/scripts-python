import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')

# F9 para rodar só a linha atual ou a seleção

# A linha abaixo serve para forçar o python a sempre escolher os mesmos aleatórios.
# Se alterado o parâmetro do seed, o resultado será diferente
np.random.seed(100)

amostra = np.random.choice(a = [0,1], size = 150, replace = True, p = [0.5, 0.5])

len(amostra[amostra == 1])

amostra
