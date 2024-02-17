from sympy import symbols

vx0, t, k, m = symbols('vx0 t k m')

values = {vx0: 15, t: 1.483, k: 0.0228, m: 1}
x_max = x_integrale.subs(values)

# Résultat
print("La valeur de x après intégration est :", round(x_max, 3), 'm')
