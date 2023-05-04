from elliptic_curve import EllipticCurve
import random


class DiffieHellman:
    def __init__(self, G):
        a = 0
        b = 6
        self.p = 43
        self.curve = EllipticCurve(a, b, self.p)
        self.generator = G
        self.random = 0
        self.public = ()
        self.private = ()

    def check_order(self):
        return self.curve.get_group_order(self.generator)

    def generate_pub_key(self):

        while (self.public == (None, None) or self.public == ()):
            self.random = random.randrange(0, self.p - 1, 1)
            self.public = self.curve.scalar_multiplication(
                self.generator, self.random)
        return self.public

    def generate_priv_key(self, p):
        self.private = self.curve.scalar_multiplication(p, self.random)
        return self.private
