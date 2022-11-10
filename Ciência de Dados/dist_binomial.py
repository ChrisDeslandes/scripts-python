from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
binom.pmf(3, 5, 0.5)

# Passar por 4 sinais de 4 tempos (1 aberto, 3 fechados),
# qual a probabilidade de pegar sinal verde 0, 1, 2, 3 e 4 vezes seguidas?
[binom.pmf(x, 4, 0.25) for x in range(0,5)] # array com resultados = [0 vezes, 1 vez, 2 vezes, 3 vezes, 4 vezes]

# E se forem 4 sinais de 2 tempos cada?
[binom.pmf(x, 4, 0.5) for x in range(0,5)]

# Em uma prova de 25 questões, CHUTANDO TODAS AS QUESTÕES,
# qual a probabilidade de acertar 10 questões? (cada questão tem 4 alternativas)
binom.pmf(10, 25, 0.25)

# PROBABILIDADE CUMULATIVA
# Se o primeiro parâmetro for 1, ele somará as probabilidades de 0 e 1
# Se o primeiro parâmetro for 2, ele somará as probabilidades de 0, 1 e 2, etc...
binom.cdf(2, 4, 0.25)
