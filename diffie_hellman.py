from elliptic_curve import EllipticCurve
import random


class DiffieHellman:
    def __init__(self, G):
        a = 0
        b = 6
        p = 43
        self.curve = EllipticCurve(a, b, p)
        self.generator = G
        # TODO: numero primo?
        self.private = random.randrange(0, p-1, 1)

    def check_order(self):
        return self.curve.get_group_order(self.generator)

    def generate_pub_key(self):
        return self.curve.scalar_multiplication(self.generator, self.private)
