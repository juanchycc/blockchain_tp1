class FiniteField:

    def __init__(self, field_of_p):
        # TODO: chequear que el numero sea primo
        self.field_of_p = field_of_p
        self.set = self.get_set(field_of_p)

    def get_set(self, num):
        set = []
        for i in range(0, self.field_of_p):
            set.append(i)

        return set

    def contains(self, num):
        return num in self.set

    def addition(self, num_1, num_2):

        return (num_1 + num_2) % self.field_of_p

    def subtraction(self, num_1, num_2):

        neg_num = (-num_2) % self.field_of_p
        return self.addition(num_1, neg_num)

    def multiplication(self, num_1, num_2):
        # neutral element
        if num_1 == 0 or num_2 == 0:
            return 0

        mult = 0
        # TODO: iterar con el número más chico de los dos, como optimización
        for i in range(0, num_2):
            mult = self.addition(mult, num_1)
        return mult

    def division(self, num_1, num_2):

        if num_2 == 0:
            return None

        rng = self.field_of_p - 2

        multiplicative_inverse = self.exponential(num_2, rng)

        return self.multiplication(num_1, multiplicative_inverse)

    def exponential(self, num, exp):
        result = num
        for i in range(0, exp - 1):
            result = self.multiplication(result, num)
        return result
