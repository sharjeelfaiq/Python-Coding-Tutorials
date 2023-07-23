# Python Numbers

# Integers (int)
num1 = 10
num2 = -25

# Floating-Point Numbers
num3 = 3.14
num4 = -0.5

# Complex Numbers
num5 = 2 + 3j
num6 = -2j

# Type Conversion

# Example 1: Integer to Float conversion
num_int = 10
num_float = float(num_int)
""" print(num_int)
print(num_float) """

# Example 2: Float to Integer conversion
num_float = 3.96
num_int = int(num_float)
""" print(num_float)
print(num_int) """

# Random Number Generation
import random

random_int = random.randint(1, 5)
# print(random_int)

random_float = random.random()
# print(random_float)

my_list = [1, 2, 3, 4, 5]
my_string = "Hello World"
random_element = random.choice(my_string)
print(random_element)