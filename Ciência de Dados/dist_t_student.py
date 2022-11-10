from scipy.stats import t

# Média de salários = 75 por hora
# Amostra = 9 funcionários
# Desvio padrão = 10

# Qual a probabilidade de selecionar um
# funcionário com salário menor que 80 por hora?
t.cdf(1.5, 8) # 8 é o grau de liberdade = n - 1

# Qual a probabilidade do salário ser maior que 80?
t.sf(1.5, 8) # ou 1 - t.cdf(1.5, 8)