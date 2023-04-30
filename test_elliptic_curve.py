import unittest
from elliptic_curve import EllipticCurve

a = -3
b = -3
p = 1021

t = (379,1011)
k = 655

ellipticCurve = EllipticCurve( a, b, p )
        
class TestEllipticCurve(unittest.TestCase):

    def test_is_in_curve(self):
        self.assertEqual(ellipticCurve.is_in_curve( t ),True,"Is in Curve Failed")
    
    def test_duplication(self):
        dup = ellipticCurve.point_duplication( t )
        self.assertEqual(ellipticCurve.is_in_curve( dup ),True,"Duplication Point Failed")
        
    def test_point_addition(self):
        dup = ellipticCurve.point_duplication( t )
        add = ellipticCurve.point_addition_differents( dup, t )
        self.assertEqual(ellipticCurve.is_in_curve( add ),True,"Point Addittion Failed")
        
    def test_scalar_multiplication(self):
        mult = ellipticCurve.scalar_multiplication( t,k )
        print(mult)
        self.assertEqual(ellipticCurve.is_in_curve( mult ),True,"Scalar Multiplication Failed")

