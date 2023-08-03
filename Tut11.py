# Python Lists
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)

# Lists are mutable
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[0] = "pineapple"
fruits.append("grapes")
fruits.remove("kiwi")
# print(fruits)

cars = ["Ford", "Ford", "Volvo", "BMW"]
# print(cars)

# List Length
insects = ["ant", "bee", "caterpillar", "dragonfly", "earwig"]
# print(len(insects))

# Example: List with Different Data Types
mixed_list = [1, "apple", True, 3.14, ["a", "b", "c"]]
# print(len(mixed_list))

clouds = ["cirrus", "stratus", "cumulus", "cumulonimbus"]
# print(type(clouds))

# List Constructor to convert a string to a list
text = "Hello World"
text_list = list(text)
# print(text_list)

# List Constructor to convert a tuple to a list
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(my_list)