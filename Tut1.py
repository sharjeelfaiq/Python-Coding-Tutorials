# Python Quickstart Example
print("Welcome to Tut1.py")

# Python Syntax Example
x = 5;
y = -10;
sum = x + y;
Sum = x + 2;
print("The sum of", x, "and", y, "is", sum);
print("The sum of", x, "and", 2, "is", Sum);

result = 21 + 9 * 12 / 2;

print(result);

# Python Indentation Example
x = 5;
if x == "5":
    print("Positive Number");
else:
    print("Non-positve number");

if 5 > 2:
    print("Five is greater than two!")
    if 5 > 0:
        print("Five is a positive integer.")

x = -10;
y = 5;

if x > y:
    print("x is greater than y")
    if x > 0:
        print("x is a positive number")
    else:
        print("x is a negative number")
else:
    print("x is less than or equal to y")


# Python Variables Example
x = 5;
name = "John";
is_student = True;

# Casting Example
x = 5;
y = str(x);
z = float(y);

print(type(x));
print(type(y));
print(type(z));

# Single or Double Quotes Example
name1 = 'John';
name2 = "Jane";
print("Hello " + name1);

# Area and Perimeter of a Rectangle
length = float(input("Enter the length of the rectangle: "));
width = float(input("Enter the width of the rectangle: "));

area = length * width;
perimeter = 2 * (length + width);

print("The are of the rectangle is: ", area);
print("The perimeter of the rectangle is: ", perimeter);