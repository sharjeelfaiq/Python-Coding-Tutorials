# Python - Slicing Strings

# Example: Slicing
my_string = "Data Science"
sliced_string = my_string[0:4]

# Example: Slice from the start
my_string = "Mathematics"
sliced_string = my_string[:4]

# Example: Slice to End
my_string = "Bio-Technology"
sliced_string = my_string[4:]

# Example: Type Conversion
my_string = "Python"
char_list = list(my_string)

# Example: Negative Indexing
my_string = "Milkshake"
sliced_string = my_string[-5:]

# Extracting dates from a messy date-time column
date_and_time = ["2022-07-15 08:30:46", "2023-05-20 13:15:00", "2021-12-01 09:00:00"]
formatted_dates = [date_and_time[2][:10], date_and_time[0][:10], date_and_time[1][:10]]

# Example: Extracting URLs
html_content = "<a href='https://www.example.com'>Click here</a>"
start_index = html_content.find("href='") + len("href='")
end_index = html_content.find("'", start_index)
url = html_content[start_index:end_index]
print(url)