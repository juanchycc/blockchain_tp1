from finite_field import FiniteField

number = 10

print("Building a finite field with p =", number)

finite_field = FiniteField(19)
finite_field.get_set()

'''print(finite_field.addition(20,30))
print(finite_field.addition(2,3))
print(finite_field.addition(5,7))
print(finite_field.subtraction(3,1))
print(finite_field.subtraction(5,8))
print(finite_field.multiplication(2,2))
print(finite_field.multiplication(7,3))
print(finite_field.multiplication(3,6))'''
print(finite_field.division(2,7))
print(finite_field.division(12,19))





