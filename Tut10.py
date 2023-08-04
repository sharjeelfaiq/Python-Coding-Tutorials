# Python Arithmetic Operators
""" x = 10
y = 2
result = x ** y
print(result) """

# Python Assignment Operators
""" x = 10
x **= 3
print(x) """

# Python Comparison Operators
""" x = 10
y = 5
print(x <= y) """

# Python Logical Operators
# 1. Logical AND
# 2. Logical OR
# 3. Logical NOT
""" x = 10
y = 7
z = 8
logical_and = x > y and y < z
logical_or = x < y or y > z or y < z 
logical_not = not(x < y) // True
print(logical_not) """

# Python Identity Operators
""" x = [1, 2, 3]
y = x
z = [1, 2, 3]
is_same_object = x is not y
print(is_same_object) """

# Python Membership Operators Operators
""" x = [1, 2.5, 3, 4, 5]
y = 2.5 in x
print(y) """

# Python Bitwise Operators
a = 5 # 0101 in binary
b = 3 # 0011 in binary

bitwise_and = a & b # 0001 in binary
bitwise_or = a | b # 0111 in binary
bitwise_xor = a ^ b # 0110 in binary
bitwise_not = ~a # 1010 in binary
print(bitwise_not)