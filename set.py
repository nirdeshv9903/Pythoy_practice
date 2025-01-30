# Write a program to check if 'apple' is present in the set {'apple', 'banana', 'cherry'}.
fruits = {'apple', 'banana', 'cherry'}
print('apple' in fruits)

# 5.Length of a Set:
# Find the length of the set numbers = {10, 20, 30, 40, 50}.
numbers = {10, 20, 30, 40, 50}
print(len(numbers))

# 6.Remove Duplicates from a List:
# Write a program to remove duplicates from the list [1, 2, 2, 3, 4, 4, 5] using a set.
numbers = [1, 2, 2, 3, 4, 4, 5]
uni_num = set(numbers)
print(uni_num)

# 7.Find Common Elements:
# Given two lists:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# Find the common elements using a set.
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)
print(common_elements)

# 8.Unique Characters in a String:
# Write a program to find all unique characters in the string "programming" using a set.
string = "programming"
unique_chars = set(string)
print(unique_chars)

# 9.Union of Sets:
# Find the union of the sets:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# 10. Intersection of Sets:
# Find the intersection of the sets:
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
intersection_set = A.intersection(B)
print(intersection_set)

# 11. Difference of Sets:
# Find the difference of the sets:
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
diff_set = X.difference(Y)
print(diff_set)