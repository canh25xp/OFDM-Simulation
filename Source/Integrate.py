import math
from scipy.integrate import quad
from sympy import Symbol, integrate, sin

# def fx(x):
#     return x**2

# integrand = quad(fx, 0, 1)

# print(integrand)

x = Symbol('x')

fx = integrate(sin(x),x)

print(fx)