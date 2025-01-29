my_list = [10, 20, 30, 40, 50]

# Access the first element.
print(my_list[0])

# Access the last element using negative indexing
print(my_list[-1])

# Access the third element.
print(my_list[2])

# Create a list of 5 strings (e.g., names of fruits
li = ["Apple","Banana","Cherry","Grape","Mango"]

# Print the second and fourth elements
print(f'second = {li[1]} and fourth = {li[3]}')

# Replace the third element with a new string.
li.insert(2,"Orange")
print(li)

###############
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the first 5 elements using slicing.
print(num[:5])

# Print every alternate element starting from the second element.
print(num[1:9:2])

# Reverse the list using slicing.
print(num[::-1])

# Create a list of the first 10 letters of the alphabet
al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Extract the first 5 letters.
print(al[:5])

# Extract the last 5 letters.
print(al[:4:-1])

# Extract every second letter from the list.
print(al[1:10:2])

##############################################
col = ['red', 'blue', 'green']

# Insert 'yellow' at the second position.
col.insert(1,"yellow")
print(col)

# Append 'purple' to the end of the list.
col.append("purple")
print(col)

# Add 'orange' at the beginning of the list.
col.insert(0,"orange")
print(col)



######################################
li_n = [10, 20, 30, 40, 50, 60]

# Remove the third element.
del li_n[2]
print(li_n)

# Delete the last element.
li_n.pop()
print(li_n)

# Clear the entire list.
li_n.clear()
print(li_n)


############# empty list ###############
em = []
# Insert the numbers 1 to 5 at the beginning of the list one by one using a loop.
n = 5
for i in range(n):
    em.append(int(input(f"enter the {i} number:")))
print(em)

# Insert the string 'middle' at index 2.
em.insert(2,"string")
print(em)

################################
my_list = []

n = int(input("Enter the number of elements you want in the list(it must be <5): "))
print("Enter the elements:")

for i in range(n):
    element = input()
    my_list.append(element)

print(my_list)

# Delete the first element
del my_list[0]
print(my_list)

# Delete the last element
del my_list[-1]
print(my_list)

# Remove the element at index 3 using pop()
my_list.pop(2)
print(my_list)

#################################
# Create a list of numbers from 1 to 10.
li3 = list((range(1,11)))
print(li3)

# Extract a sublist from index 2 to 7.
print(li3[1:7])

# Insert the number 99 after the fifth element.
li3.insert(5,99)
print(li3)

##########################################
alp =  ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Extract the sublist ['b', 'c', 'd'] using slicing.
print(alp[1:4])
# Replace the element 'd' with 'x'.
alp[3] = 'x'
print(alp)

# Remove the element 'g' and append 'z' to the list.
alp.remove('g')
alp.append('z')
print(alp)