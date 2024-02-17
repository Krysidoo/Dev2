import matplotlib.pyplot as plt
import numpy as np

valeur_t = np.linspace(0, 3)
m = 1
g = 9.81
k = 0.0228
vx0 = 1

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
