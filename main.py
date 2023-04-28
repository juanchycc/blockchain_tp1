from finite_field import FiniteField
from elliptic_curve import EllipticCurve

'''a = -3
b = -3
p = 1021

t = (379,1011)'''
a = -3
b = -3
p = 11

t = (4,4)

ellipticCurve = EllipticCurve( a, b, p )

# g^n = I => un punto generador, elevado a la cantidad de elementos de la curva es igual al punto infinito
# por lo tanto si multiplo un punto generador hasta encontrar el punto inifinito encuentro n
# por Lagrange si n es primo, todos los puntos son generadores
p = ()
i = 0
while p != (None,None):
    i +=1
    p = ellipticCurve.scalar_multiplication(t,i)

print(i)