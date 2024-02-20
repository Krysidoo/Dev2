import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve
from sympy import solve, integrate, symbols

# Question A
def valeur_k(C, rho, r):
    return round(0.5 * C * rho * math.pi * r ** 2, 4)

# Variables
C = 0.5
rho = 1.293
r = 0.15

# Résultat (k)
print("QUESTION A : La valeur de k est :", valeur_k(C, rho, r))

# Question B
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
print("QUESTION B : La valeur de t est :", round(t_solution[0], 3), 's')

# Question C

vx, vx0, t, k, m = symbols('vx vx0 t k m')

# Intégrale de la vitesse en x
v_x = integrate(1 / vx ** 2, (vx, vx0, vx))
print("POUR LA QUESTION C :")
print("-kt/m =", v_x)

# Intégrale de la position en x
x = (1 / vx0 + k * t / m) ** (-1)
x_integrale = integrate(x, (t, 0, t))

# Résultat
print("x =", x_integrale)

# Question D
values = {vx0: 15, t: 1.483, k: 0.0228, m: 1}
x_max = x_integrale.subs(values)

# Résultat
print("QUESTION D : La valeur de x après l'intégration est :", round(x_max, 3), 'm')

# Question E
valeur_t = np.linspace(0, 3)
m = 1
g = 9.81
k = 0.0228
vx0 = 15

def xair(t):
    return -m * np.log(m) / k + m * np.log(k * vx0 * t + m) / k

def yair(t):
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))

def xvide(t):
    return vx0 * t

def yvide(t):
    return 10 - 0.5 * g * t ** 2

valeur_xair = xair(valeur_t)
valeur_yair = yair(valeur_t)
valeur_xvide = xvide(valeur_t)
valeur_yvide = yvide(valeur_t)

plt.figure(figsize=(8, 6))
plt.plot(valeur_xair, valeur_yair, label='Dans l\'air')
plt.plot(valeur_xvide, valeur_yvide, label='Dans le vide')
plt.title('Graphique paramétrique de y en fonction de x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
