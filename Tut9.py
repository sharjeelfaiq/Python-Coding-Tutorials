# Boolean Values
x = 5
y = 10
is_greater = x > y
is_equal = x == y
is_less = x < y
# print(is_less)

def is_true(value):
    if value:
        return bool(value)
    else:
        return bool(value)

# print(is_true(None))

def is_even(num):
    return num % 2 == 0

print(is_even(5))