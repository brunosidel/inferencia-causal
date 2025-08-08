import numpy as np


n_jugadas = 1000
prob_cara = 0.5
capital = 100


for _ in range(n_jugadas):
    sale_cara = np.random.rand() < prob_cara
    if sale_cara:
        capital = 0.5 * capital * 3
    else:
        capital = 0.5 * capital * 1.2

print(f"Capital final después de {n_jugadas} jugadas: {capital:.8f}")
