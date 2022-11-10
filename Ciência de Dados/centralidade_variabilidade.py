import numpy as np
from scipy import stats

time = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

np.mean(time)
np.median(time)

np.quantile(time, [0, 0.25, 0.5, 0.75, 1])
np.std(time) # Diferente do R pois no Python se usa o ddof como 0, no R se usa ddof como 1.
np.std(time, ddof = 1) # Igual ao R

stats.describe(time)
