# Python - Modify Strings

greeting = "Hello World!"

# Example 1: Uppercase
uppercase = greeting.upper()

# Example 2: Lowecase
lowercase = greeting.lower()

# Example 3: Stripped String
stripped_string = greeting.strip()

# Example 4: Replace String
replaced_string = greeting.replace("World", "Universe")

# Example 5: Split String
split_string = greeting.split()

# Python - String Concatenation
a = "Hello"
b = "World"
c = a + " " + b

# Python - Format Strings
age = 25
txt = "My name is Sharjeel, I'm {}."

quantity = 3
itemno = 630
price = 213.4
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))