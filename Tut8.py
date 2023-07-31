# Example: Escape Character
quote = "He said, \"Hello!\""
# print(quote)

# Other escape characters
# 1. Single Quote
# print("This is a single quote: \\'")

# 2. New Line
# print("This is a \nnew line.")

# 3. Tab
# print("\tThis is a new line.")

# 4. Backslash
# print("This is a backslash: \\")

# 5. Carriage Return
# print("This is a carriage return: \rWorld")

# 6. Octal Value
# print("This is an octal value: \123")

# 7. Hex Value
# print("This is a hex value: \x50")

text = "Hello World"
# print(text.strip())
# print(text.upper())

sentence = "python is great"
# print(sentence.title())

data = "apple,banana,orange"
fruits = data.split(",")
# print(fruits)

text = "apple"
# print(text.replace("p", "b"))

# Python - Format Strings

# Using format() method with positional arguments
name = "Burhan"
age = 25
sentence = "My name is {}, and I am {} years old."
# print(sentence.format(name, age))

# Using f-strings
name = "Charlie"
age = 42
sentence = f"My name is {name}, and I am {age} years old."
print(sentence)