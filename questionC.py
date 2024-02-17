from sympy import integrate, symbols

vx, vx0, t, k, m = symbols('vx vx0 t k m')

# Intégrale de la vitesse en x
v_x = integrate(1 / vx ** 2, (vx, vx0, vx))
print("-kt/m =", v_x)

# Intégrale de la position en x
x = (1 / vx0 + k * t / m) ** (-1)
x_integrale = integrate(x, (t, 0, t))

# Résultat
print("x =", x_integrale)
