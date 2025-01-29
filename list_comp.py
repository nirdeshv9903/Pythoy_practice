import math

# Filter Divisible Numbers:
# Create a list of numbers between 1 and 50 that are divisible by 5.
li = [i for i in range(1, 51) if i % 5 == 0]
print(li)
# Given a string: "comprehension", create a list of all the vowels in the string.
li1 = [i for i in "comprehension" if i in "aeiou"]
print(li1)
# Write a list comprehension to generate all prime numbers less than 50.
li2 = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]
print(li2)

# Given a list of numbers:
numbers = [1, 2, 3, 4, 5]
# Create a list of their factorials using list comprehension using in build funtion.
li3 = [math.factorial(i) for i in numbers]
print(li3)