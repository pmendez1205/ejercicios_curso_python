# Dado un número complejo Z = a + bi, calcular su módulo:

import math

# Pedir valores al usuario
a = float(input("Introduce la parte real (a): "))
b = float(input("Introduce la parte imaginaria (b): "))

# Calcular el módulo
modulo = math.sqrt(a**2 + b**2)

print(f"El módulo de Z = {a} + {b}i es: {modulo}")
