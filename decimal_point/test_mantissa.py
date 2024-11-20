import calculate_mantissa

print("The minimum value of beta = 10; t = 3; and with exponent between [-5, 5] is:")
print(calculate_mantissa.min_val(10, 5))
print("And the maximum value is: ")
print(calculate_mantissa.max_val(10, 3, 5))
print("The number of possible positive mantissas is: ")
print(calculate_mantissa.num_max_mantissa_pos(10, 3))
print("The number of possible exponents is: ")
print(calculate_mantissa.num_max_exponent(5, -5))
print("The number of representable positive elements is: ")
print(calculate_mantissa.num_positive_elements(10, 3, 5, -5))
print("The number of representable total elements is: ")
print(calculate_mantissa.total_representable_elements(10, 3, 5, -5))