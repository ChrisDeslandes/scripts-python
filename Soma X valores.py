import numpy as np
import os

while 1:
    try:
        x = np.array(input("Digite os valores a serem somados separados por espaço: ").replace(",",".").split(), dtype='f')
        break        
    except ValueError: pass

print("\nSoma dos elementos = {:.3f}".format(x.sum()))

os.system("pause >nul")
