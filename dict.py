# Basic Dictionary Operations
# Create a Dictionary:
d = {'name': 'Nine', 'age': 22, 'grade': 'A'}
print(d)
d1 = dict(name='Nine', age=22, grade='A')
print(d1)
# Create a dictionary with keys as numbers from 1 to 5 and values as their cubes.
d2 = {key: key**3 for key in range(1, 6)}
print(d1)


# Access and Modify a Dictionary:
d["name"] = 'Nero'
for key in d:
    print(key, d[key])

# Given a dictionary student = {'name': 'John', 'age': 22, 'grade': 'A'}, do the following:
student = {'name': 'Nine', 'age': 22, 'grade': 'A'}
# Access and print the student’s name.
print(student['name'])
# Update the student’s grade to 'A+'.
student['grade'] = 'A+'
# Add and Remove Key-Value Pairs:
student["roll"] = 101
print(student)
del student["roll"]
print(student)

# Create a dictionary inventory = {'apples': 10, 'bananas': 5}.
inventory = {'apples': 10, 'bananas': 5}
# Add a new item oranges with a quantity of 7.
inventory['oranges'] = 7
print(inventory)
# Remove the item bananas from the dictionary.
del inventory['bananas']
print(inventory)


# Check for Key Presence:

# Given a dictionary scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}, check if 'David' is a key in the dictionary.
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}
print('David' in scores)

# Iterate Over a Dictionary:
# Write a program to iterate through a dictionary and print each key and its corresponding value.
for key, value in scores.items():
    print(key, value)


# Merge Two Dictionaries:

# Merge these two dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
new_dict = {**dict1, **dict2}
# Print the resulting dictionary.
print(new_dict)

# Dictionary Comprehension
# Squares of Numbers:
d4 = {i: i**2 for i in range(1, 11)}
print(d4)
# Create a dictionary with numbers from 1 to 10 as keys and their squares as values using dictionary comprehension.
d5 = {i: i**2 for i in range(1, 11)}
print(d5)

# Filter Even Numbers:

# Create a dictionary using dictionary comprehension where the keys are numbers from 1 to 10, and the values are their squares, but include only the even numbers.
d6 = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(d6)

# Reverse a Dictionary:
original_dict = {'a': 1, 'b': 2, 'c': 3}
# Reverse the keys and values of this dictionary using dictionary comprehension:
reversed_dict = {value: key for key, value in original_dict.items()}
print(reversed_dict)

# Count Character Frequency:

# Write a dictionary comprehension to count the frequency of each character in the string "programming".
string = "programming"
char_frequency = {char: string.count(char) for char in string}
print(char_frequency)

# Nested Dictionary:

# Use dictionary comprehension to create a nested dictionary where the keys are numbers from 1 to 3, and the values are dictionaries that map numbers from 1 to 3 to their products.
nested_dict = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(nested_dict)
# Example: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}


# Zip Two Lists into a Dictionary:
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
# Use dictionary comprehension to create a dictionary from these two lists:
d7 = {key: value for key, value in zip(keys, values)}
print(d7)

# Filter Dictionary by Value:

# Given a dictionary marks = {'Alice': 85, 'Bob': 65, 'Charlie': 90, 'David': 72}, create a new dictionary containing only students who scored more than 80.
marks = {'Alice': 85, 'Bob': 65, 'Charlie': 90, 'David': 72}
top_students = {key: value for key, value in marks.items() if value > 80}
print(top_students)

# Multiplication Table:

# Create a dictionary comprehension to generate a multiplication table for the number 5 (from 1 to 10).
multiplication_table = {i: i*5 for i in range(1, 11)}
print(multiplication_table)
# Example: {1: 5, 2: 10, 3: 15, ..., 10: 50}

# Convert List to Dictionary:
# Given a list of tuples data = [('a', 10), ('b', 20), ('c', 30)], convert it into a dictionary using dictionary comprehension.
data = [('a', 10), ('b', 20), ('c', 30)]
data_dict = {key: value for key, value in data}
print(data_dict)