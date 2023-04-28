import unittest
from finite_field import FiniteField

p = 523
a = 333
b = 70

finiteField = FiniteField( p )
        
class TestFiniteField(unittest.TestCase):
        
    def test_closed_property(self):
        add = finiteField.addition(a,b)
        self.assertEqual(finiteField.contains(add),True,"Additive Identity Failed")
        mult = finiteField.multiplication(a,b)
        self.assertEqual(finiteField.contains(mult),True,"Additive Identity Failed")
        
    def test_additive_indentity(self):
        add = finiteField.addition(a,0)
        self.assertEqual(add,a,"Additive Identity Failed")
        
    def test_multiplicative_identity(self):
        mult = finiteField.multiplication(a,1)
        self.assertEqual(mult,a,"Multiplicative Identity Failed")
        
    def test_additive_inverse(self):
        sub = finiteField.subtraction(0,a)
        self.assertEqual(finiteField.contains(sub),True,"Additive Inverse Failed") 
        add = finiteField.addition(a,sub)     
        self.assertEqual(0,add,"Additive Inverse Failed")
    
    def test_multiplicative_inverse(self):
        div = finiteField.division(1,a)
        self.assertEqual(finiteField.contains(div),True,"Multiplicative Inverse Failed") 
        mult = finiteField.multiplication(a,div)    
        self.assertEqual(1,mult,"Multiplicative Inverse Failed")
        
if __name__ == '__main__':
    unittest.main()