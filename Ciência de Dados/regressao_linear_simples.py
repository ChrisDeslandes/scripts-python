import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

base = pd.read_csv('C:\Chris\Python\Ciência de Dados\cars.csv')
# Deleta a coluna 'Unnamed: 0' da base de dados:
base = base.drop(['Unnamed: 0'], axis = 1)

# Passa os valores das colunas para arrays:
x = base.iloc[:,1].values
y = base.iloc[:,0].values

# Transforma os valores de pés para metros e de mi/h para km/h:
x = x * 0.3048
y = y * 1.6093

#Acha a matriz de correlação entre as variáveis:
correlacao = np.corrcoef(x,y)

# Cria o modelo de regressão linear:
modelo = LinearRegression()

# Para treinar o modelo, o array x deve ter o formato de matriz, logo:
x = x.reshape(-1,1)

# Treina o modelo com os valores de x e y
modelo.fit(x,y)

# Visualiza os coeficientes da linha de regressão criada:
modelo.intercept_
modelo.coef_

# Plota os valores (pontos):
plt.scatter(x,y)
# Plota a linha de regressão:
plt.plot(x, modelo.predict(x), color = 'red')

# Previsão manual da velocidade para 50m de distância de parada:
modelo.intercept_ + modelo.coef_ * 50
# Previsão 'automática da velocidade para 50m de distância de parada:
modelo.predict([[50]])

# Visualizar os residuais (no sklearn você só consegue um valor geral):
modelo._residues

# Visualizar os residuais (no yellowbrick você consegue ver detalhadamente):
from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(modelo)
visualizador.fit(x, y)
visualizador.poof()
