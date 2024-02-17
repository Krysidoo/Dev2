import math

def valeur_k(C, rho, r):
    return round(0.5 * C * rho * math.pi * r ** 2, 4)

# Variables
C = 0.5
rho = 1.293
r = 0.15

# Résultat (k)
print("La valeur de k est :", valeur_k(C, rho, r))
