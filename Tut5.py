# Python Stirngs

# Assign string to a variable
name = "John Doe"
course = "Data Science"
email = 'john@example.com'

# Using Single and Double Quotes
single_quotes = 'Single quotes'
double_quotes = "Double quotes"

# Multiline Strings
description = '''Python is a programming language.
It is used to develop desktop, web and mobile applications.'''

text_with_breaks = """Line 1
Line 2
Line 3"""

# Strings are Arrays
my_string = "Hello, Data Science!"
first_character = my_string[0]
second_character = my_string[1]
fifth_character = my_string[4]
last_character = my_string[-1]
second_last_character = my_string[-2]
print(second_last_character)

# Example: Looping Through a String
my_string = "Python"
for i in my_string:
    print(i)

# Example: Counting Occurances of a Character
my_string = "Banana"
count = 0
target_character = "a"
for char in my_string:
    if char == target_character:
        count += 1
print(f"The character '{target_character}' appears {count} times.")

# String Length
my_string = "This is a car."
length = len(my_string)
print(length)

# Check String (in, not in)
# Example: Check String (Keyword 'in')
my_string = "Python is a great language for data science."
if "data" in my_string:
    print("Found 'data' keyword in the string.")

# Example: Check if NOT (Keyword 'not in')
my_string = "Python is a great language for data science."
if "cat" not in my_string:
    print("'cat' keyword is not in the string.")