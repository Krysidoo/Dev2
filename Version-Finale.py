import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve
from sympy import integrate, symbols

# Question A

# On commence par définir les variables
C = 0.5
rho = 1.293
r = 0.15

# On trouve la valeur de k avec cette equation
# (on n'oublie pas de laisser 4 chiffres apres la virgule)
def valeur_k(C, rho, r):
    return round(0.5 * C * rho * math.pi * r ** 2, 4)

# Résultat (k)
print("QUESTION A : La valeur de k est :", valeur_k(C, rho, r))
print() # Je fait un print vide pour que ce soit plus beau dans la console

# Question B

# On commence par définir les variables
m = 1
g = 9.81
k = 0.0228

# l'équation pour trouver t
def equation(t):
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))

# On donne une estimation initiale
# (l'équation de newton a besoin d'une estimation initiale)
# dans notre  cas on peut estimer entre 0.5 et 1 
# On va estimer à 0.5
guess = 0.5

# Résolution de l'équation pour t
t_solution = fsolve(equation, guess)

# Résultat (t)
# On va arrondir à 3 chiffres apres la virgule
print("QUESTION B : La valeur de t est :", round(t_solution[0], 3), 's')
print() # Je fait un print vide pour que ce soit plus beau dans la console

# Question C

# 1er print Utile à moi-meme
print("POUR LA QUESTION C :")

# On commence par définir les symboles
# Nous n'utuliserons pas de valeurs pour cette question
vx, vx0, t, k, m = symbols('vx vx0 t k m')

# Intégrale de la vitesse en x
v_x = integrate(1 / vx ** 2, (vx, vx0, vx))

print() # Je fait un print vide pour que ce soit plus beau dans la console

print("-kt/m =", v_x)

print() # Je fait un print vide pour que ce soit plus beau dans la console

# Intégrale de la position en x
x = (1 / vx0 + k * t / m) ** (-1)
x_integrale = integrate(x, (t, 0, t))

# Résultat x(t)
print("x =", x_integrale)
print() # Je fait un print vide pour que ce soit plus beau dans la console

# Question D

# Ici contrairement à la question précédente:
# je vais devoir donner une valeur aux variables
valeurs = {vx0: 15, t: 1.483, k: 0.0228, m: 1}
# Je résouds l'intégrale précedente mais avec des valeurs
x_max = x_integrale.subs(valeurs)

# Résultat Xmax
# ici on va arrondir le résultat à 3 chiffres apres la virgule
print("QUESTION D : La valeur de x après l'intégration est :", round(x_max, 3), 'm')
print() # Je fait un print vide pour que ce soit plus beau dans la console

# Question E

# Définir les valeurs possible (ici j'en ai générer 100)
valeur_t = np.linspace(0, 2, 100)
# Je défini encore les variables avec des valeurs
m = 1
g = 9.81
k = 0.0228
vx0 = 15

# Equation pour l'air

def xair(t):  # X
    return -m*np.log(m)/k + m*np.log(k*t*vx0 + m)/k

def yair(t):  # Y
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))

# Equation pour le vide

def xvide(t):        # X
    return vx0 * t

def yvide(t):        # Y
    return 10 - 0.5 * g * t ** 2

# On donne les valeurs correspondantes de x et y pour chaque t
valeur_xair = xair(valeur_t)
valeur_yair = yair(valeur_t)
valeur_xvide = xvide(valeur_t)
valeur_yvide = yvide(valeur_t)

# On utilise matplotlib pour tracer le graphique
plt.figure(figsize=(8, 6))
plt.plot(valeur_xair, valeur_yair, label='Dans l\'air')
plt.plot(valeur_xvide, valeur_yvide, label='Dans le vide')
plt.title('Graphique paramétrique de y en fonction de x')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 25)  # Définir les limites de x de 0 à 20
plt.ylim(0, 10)  # Définir les limites de y de 0 à 10
plt.grid(True)
plt.legend()
plt.show()
print("QUESTION E : ")
print("Une page avec le graphique paramétrique de y en fonction de x s'est ouvert")
