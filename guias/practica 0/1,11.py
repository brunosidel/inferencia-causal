import numpy as np

n_jugadas = 1000
prob_cara = 0.5
proporciones = np.arange(0.1, 1.01, 0.1)  # 0.1, 0.2, ..., 1.0

for f_cara in proporciones:
    capital = 100.0
    for _ in range(n_jugadas):
        sale_cara = np.random.rand() < prob_cara
        if sale_cara:
            capital = f_cara * capital * 3
        else:
            capital = (1 - f_cara) * capital * 1.2
        if capital == 0:
            break
    print(f"Fracción a Cara {f_cara:.1f} -> Capital final: {capital:.8f}")
