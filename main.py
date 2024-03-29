from finite_field import FiniteField
from elliptic_curve import EllipticCurve
from diffie_hellman import DiffieHellman
'''
# pto 2
a = -3
b = -3
p = 1021

t = (379, 1011)


ellipticCurve = EllipticCurve(a, b, p)

print(ellipticCurve.get_group_order(t))
'''
# pto 3

# Intercambio:
g = (13, 15)
alice = DiffieHellman(g)
bob = DiffieHellman(g)

alice_public = alice.generate_pub_key()
bob_public = bob.generate_pub_key()

alice_priv = alice.generate_priv_key(bob_public)
bob_priv = bob.generate_priv_key(alice_public)

print(alice_priv == bob_priv)
'''
#(13,15) es generador de un subgrupo => mucho más fácil de romper
dh1 = DiffieHellman((13, 15))
print(dh1.check_order())
print(dh1.generate_pub_key())
#(9,2) genera el grupo completo => más seguro, requiere
#más iteraciones de fuerza bruta para encontrar la clave privada
dh2 = DiffieHellman((9, 2))
print(dh2.check_order())
print(dh2.generate_pub_key())


# pto 4
a = 905
b = 100
p = 1021

t = (1006, 416)

ellipticCurve = EllipticCurve(a, b, p)

# kT = (612,827)

# 1. Ataque por fuerza bruta:

resp = ellipticCurve.point_duplication(t)
i = 2

while resp != (612, 827):
    resp = ellipticCurve.point_addition_differents(t, resp)
    i += 1
print("k: ",i)

print("check kP: ",ellipticCurve.scalar_multiplication(t, i))
'''
# 687
# (612, 827)
# print(ellipticCurve.get_group_order(t))
# 966
