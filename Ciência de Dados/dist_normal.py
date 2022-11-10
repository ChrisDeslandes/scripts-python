from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt

# Conjunto de objetos com pesos normalmente distribuídos em uma cesta,
# com média = 8 e desvio padrão = 2.

# Qual a probabilidade de tirar um objeto cujo peso seja menor que 6kg?
norm.cdf(6, 8, 2)

# Qual a probabilidade de tirar um objeto cujo peso seja maior que 6kg?
norm.sf(6, 8, 2) # ou, no caso, 1 - norm.cdf(6, 8, 2)

# Qual a probabilidade de tirar um objeto cujo peso seja menor que 6kg ou maior que 10kg?
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# Qual a probabilidade de tirar um objeto cujo peso seja menor que 10kg e maior que 8kg?
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)


# Gerar dados normalmente distribuídos:
dados = norm.rvs(size = 1000)

stats.probplot(dados, plot = plt)

stats.shapiro(dados)
