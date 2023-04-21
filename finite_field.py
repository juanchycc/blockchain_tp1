class FiniteField:
    
    def __init__(self, field_of_p):
        #TODO: chequear que el numero sea primo
        self.field_of_p = field_of_p


    def get_set( self ):
        set = []
        for i in range( 0, self.field_of_p ):
            set.append(i)
        print(set)

    def addition( self, num_1, num_2 ):
        if num_1 >= self.field_of_p or num_2 >= self.field_of_p :
            return "Invalid range, field number is: " + str(self.field_of_p)
         
        return ( num_1 + num_2 ) % self.field_of_p

    def subtraction( self, num_1, num_2 ):
        if num_1 >= self.field_of_p or num_2 >= self.field_of_p :
            return "Invalid range, field number is: " + str(self.field_of_p)

        neg_num = ( -num_2 ) % self.field_of_p
        return self.addition( num_1, neg_num )
    
    def multiplication( self, num_1, num_2 ):
        if num_1 >= self.field_of_p or num_2 >= self.field_of_p :
            return "Invalid range, field number is: " + str(self.field_of_p)
        #neutral element
        if num_1 == 0 or num_2 == 0:
            return 0

        mult = 0

        for i in range( 0,num_2 ):
            mult = self.addition( mult, num_1 )
        return mult
    
    def division( self, num_1, num_2 ):
        if num_1 >= self.field_of_p or num_2 >= self.field_of_p :
            return "Invalid range, field number is: " + str(self.field_of_p)
        
        rng = self.field_of_p - 2
        multiplicative_inverse = num_2

        for i in range(0, rng -1):
            multiplicative_inverse = self.multiplication( multiplicative_inverse, num_2 )

        return self.multiplication( num_1, multiplicative_inverse )
