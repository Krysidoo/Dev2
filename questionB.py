import numpy as np
from scipy.optimize import fsolve

def equation(t):
    m = 1
    g = 9.81
    k = 0.0228
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))

# Estimation initiale
guess = 1

# Résolution
t_solution = fsolve(equation, guess)

# Résultat (t)
print("La valeur de t est :", round(t_solution[0], 3), 's')
