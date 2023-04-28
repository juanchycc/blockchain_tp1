from finite_field import FiniteField
from elliptic_curve import EllipticCurve

'''a = -3
b = -3
p = 1021

t = (379,1011)'''
a = -3
b = -3
p = 47

t = (17,21)

ellipticCurve = EllipticCurve( a, b, p )

points = set()
points.add(t)
for i in range( 1, p**2 - 1  ):
    r = ellipticCurve.scalar_multiplication(t,i)
    points.add(ellipticCurve.scalar_multiplication(t,i))
print(len(points))