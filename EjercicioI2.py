import math

#2.Escribir una función que calcule el mínimo común múltiplo entre dos números
def lcm(a, b):
    return (a*b) // math.gcd(a, b)