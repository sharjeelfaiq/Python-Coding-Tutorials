# Python Data Types
# Numberic Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set types: set, frozenset
# Boolean Type: bool
# String Type: str

# Getting the type of a variable
name = "John"
print(type(name))

num_int = 5
print(type(num_int))

num_float = 3.14
print(type(num_float))

numbers = [1, 2, 3, 4, 5]
print(type(numbers))

# Setting the Data Type Using The Constructor Functions
num_int = int(10)
num_float = float(3.14)
name = str("John")
my_list = list(range(1, 10))

print(type(num_int))
print(type(num_float))
print(type(name))
print(type(my_list))

# Setting the specific Data Types

# Example 1: Setting a Boolean Data Type
Is_valid = True
is_valid = bool(0)
true = bool(1)
false = bool(0)

print(type(Is_valid))
print(type(is_valid))
print(true)
print(false)

# Example 2: Setting a Tuple Data Type
person = ("John", 25, "USA", "john@example.com")
print(person)
print(type(person))

# Example 3: Setting a Set Data Type
setA = {1, 2, 3, 4, 5}
setB = set([6, 7, 8, 9, 10])

print(setA)
print(type(setA))

print(setB)
print(type(setB))

# Example 4: Setting a Dictionary Data Type
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"], "email": "abc@example.com"}
print(type(student))

# Example 5: Setting a Custom Data Type
# Importing the namedtuple function from the collections module
from collections import namedtuple

# Defining a namedtuple
Person = namedtuple("PersonA", ["name", "age", "country", "email"])

# Creating an instance of the named tuple
person = Person('John', 25, 'USA', 'john@example.con')

# Printing the named tuple
print(type(person))