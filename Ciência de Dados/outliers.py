import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = pd.read_csv('C:/Chris/Python/Ciência de Dados/iris.csv')

plt.boxplot(iris.iloc[:,1]) # com outliers
plt.boxplot(iris.iloc[:,1], showfliers = False) # sem outliers

outliers = iris[(iris['sepal_width'] > 4) | (iris['sepal_width'] < 2.2)]


from pyod.models.knn import KNN

sepal_width = np.array(iris.iloc[:,1])
sepal_width = sepal_width.reshape(-1,1)
detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_

indices = [i for i in range(len(previsoes)) if previsoes[i] == 1]

resultados = [sepal_width[i] for i in indices]
