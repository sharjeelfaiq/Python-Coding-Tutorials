# Variables in Python
x = 5
y = "Hello"

# Storing numerical data:
age = 30
height = 1.75
weight = 68.5

# Storing categorical data:
gender = "Female"
nationality = "Pakistani"
education_level = "Bachelor's Degree"

# Storing data in a list
temperatures = [23.5, 24.2, 22.8, 25.1, 24.9]
seasons = ["winter", "spring", "summer", "winter"]

# Storing data in a dictionary
student = {"name": "John", "age": 20, "grade":'A'}

# Casting from String to Integer
x = "5"
y = 5
sum = float(x)+y
# print(sum)

#Castin from Float to Integer
num_float = 3.14
num_int = int(num_float)
""" print(num_int)
print(type(num_int))
print(type(num_float)) """

# Variable Names
age = 25

# Snake Case
student_name = "John Doe"
num_data_points = 100
feature_name = 'age'
model_name = 'Random Forest Classifier'
column_name ='sales'
data_scientist_name = "Jane Smith"

# Camel Case
numDataPoints = 100
featureName = 'age'

# Pascal Case
NumDataPoints = 100
FeatureName = 'age'

# Multiple Assignment
x, y, z = 1, 2, 3
mean, std, max_value = 3.5, 1.2, 10.0
accuracy, precision, recall = 0.85, 0.78, 0.91
learning_rate, num_epochs, batch_size = 0.001, 50, 32
x_values, y_values, color = [1, 2, 3, 4], [5, 6, 7, 8], 'blue'
feature_1, feature_2, feature_3 = 'feature_1', 'feature_2', 'feature_3'
eng_dic, urdu_dic, spanish_dic =  {"1":"A", "2":"B", "3":"C"}, {"1":"D", "2":"E", "3":"F"}, {"1":"G", "2":"H", "3":"I"}
""" print(eng_dic)
print(feature_3)
print(x_values)
print(y_values)
print(color) """

x = 4
y = 2
""" print("The value of x is", x, "and the value of y is", y ) """

# Printing the resulf of a data analysis calculations
mean = 2.7
""" print("The mean is:", mean) """
accuracy = 0.85
precision = 0.78
recall = 0.91
""" print("Accuracy:", accuracy, "Precision:", precision, "Recall", recall) """

# Printing the results of a data visualization
X_values = [1, 2, 3, 4]
Y_values = [5, 6, 7, 8]
""" print("x_values:", X_values)
print("Y_values:", Y_values) """

# Printing the name and value of a feature in a dataset
feature_name = 'age'
feature_values = [25, 30, 28]
""" print("Feature:", feature_name)
print("Values:", feature_values) """

# Global Variables
var = 20

def function():
    print(var)
""" my_function() """

# using a global variable to store a dataset
global_dataset = {"country1":"Pakistan", "country2":"Bangladesh", "country3":"Nepal"}

def preprocess_data():
    print(global_dataset)
""" preprocess_data() """

# using a global variable to store the configuration settings for a machine learning model
global_config = {
    "learning_rate": 0.03,
    "num_epochs": 100,
    "batch_size": 32
}

def train_model():
    print(global_config)
""" train_model() """

# Example 1: Global Keyword
global_var = 10

def my_function():
    global global_var
    global_var += 5
    # print(global_var)

my_function()
# print(global_var)

# Example 2: Using a Global Variable
global_data = []

def add_item(item):
    global global_data
    global_data.append(item)

add_item(int(input("Enter a number: ")))
print(global_data)