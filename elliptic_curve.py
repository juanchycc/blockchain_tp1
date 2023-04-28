from finite_field import FiniteField
#TODO: obtener cantidad de puntos. 
# Para el método (duplicar un punto p**2 veces) que pense necesitaría que el punto 
# sea un generador completo. Hay otros algorirmos: Schoof, atkin-morain, elkies-atkin
# revisar en video de clase
class EllipticCurve:
    
    def __init__( self,a ,b ,p ):
        self.a = a
        self.b = b
        self.finiteField = FiniteField(p)
    
    def is_in_curve( self, t ):
        if t == (None,None):
            return True
        # y^2 = x^3+ax+b
        left = self.finiteField.exponential( t[1], 2)
        
        c = self.finiteField.exponential( t[0], 3)
        m = self.finiteField.multiplication( self.a, t[0] )
        s1 = self.finiteField.addition( c, m )
        
        right = self.finiteField.addition( s1, self.b )
        
        return left == right

    def point_addition_differents( self, t1, t2 ):
        if not self.is_in_curve( t1 ) or not self.is_in_curve( t2 ):
            return 
        
        if t1 == (None,None) and t2 == (None,None):
            return (None,None)
        if t1 == (None,None):
            return t2
        if t2 == (None,None):
            return t1
        
        f = self.finiteField
        
        # s = ( y2 - y1 ) / ( x2 - x1 )
        a = f.subtraction( t2[1], t1[1] )
        b = f.subtraction( t2[0], t1[0] )
        s = f.division( a, b )
        if s == None:
            return (None,None)
        # x3 = s^2 - x1 - x2
        x = f.subtraction( f.subtraction( f.exponential(s,2), t1[0] ), t2[0] )
        # y3 = s( x1 - x3) - y1
        y = f.subtraction( f.multiplication( s, f.subtraction( t1[0], x ) ), t1[1] )
        
        return (x,y)
    
    def point_duplication( self, t ):
        
        if not self.is_in_curve( t ):
            return 
        
        f = self.finiteField
        
        # s = ( 3x1^2 + a) / ( 2y1 )
        p = f.multiplication( 3, f.exponential( t[0], 2 ) )
        s = f.division( f.addition( p, self.a ), f.multiplication( 2, t[1] ) )
        # x = s^2 - 2x1
        x = f.subtraction( f.exponential( s, 2 ), f.multiplication( 2, t[0] ) )
        # y = s( x1 - x ) - y1
        y = f.subtraction( f.multiplication( s, f.subtraction( t[0], x ) ) , t[1] )
        
        return (x,y)
    
    def scalar_multiplication( self, t, num ):
        resp = self.point_duplication( t )

        for _ in range( 1, num - 1 ):
            resp = self.point_addition_differents( resp, t )

        return resp