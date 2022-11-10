import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

base = pd.read_csv('C:\Chris\Python\Ciência de Dados\mtcars.csv')
# Deleta a coluna 'model' da base de dados:
base = base.drop(['model'], axis = 1)

# Passa os valores das colunas para arrays (x para matriz):
x = base.iloc[:,2].values
y = base.iloc[:,0].values

correlacao = np.corrcoef(x, y)

x = x.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(x,y)
modelo.intercept_
modelo.coef_

# R²:
modelo.score(x,y)

# R² ajustado:
previsoes = modelo.predict(x)
import statsmodels.formula.api as sm
modelo_ajustado = sm.ols('mpg ~ disp', data = base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(x,y)
plt.plot(x,previsoes, color = 'red')

modelo.predict([[200]])

x1 = base.iloc[:, 1:4].values

modelo2 = LinearRegression()
modelo2.fit(x1, y)

# R²:
modelo2.score(x1, y)
# R² ajustado:
modelo2_ajustado = sm.ols('mpg ~ cyl + disp + hp', data = base)
modelo2_treinado = modelo2_ajustado.fit()
modelo2_treinado.summary()

# Para prever consumo de um carro com 4 cilindros, 200 disp e 100 hp:
novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
modelo2.predict(novo)
