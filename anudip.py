n = int(input("Enter the limit:"))
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num += 1
    print()

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

#################################################

# n = int(input("Enter the limit:"))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end=" ") 
#     print()


# A 
# A B 
# A B C 
# A B C D 
# A B C D E

##############################################
# n = int(input("Enter the limit:"))
# for i in range(n):
#     # Print spaces
#     print(" " * (n - i - 1), end="")
#     # Print stars
#     print("*" * (2 * i + 1))

#     *
#    ***
#   *****
#  *******
# *********

##################################################

# n = int(input("Enter the limit:"))
# for i in range(n, 0, -1): 
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print() 

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
########################################3

# n = int(input("Enter the limit:"))
# for i in range(n):
#     print(" " * (2 * i), end="")
    
#     for j in range(n - i, 0, -1):
#         print(j, end=" ")
    
#     print()  

# 5 4 3 2 1 
#   4 3 2 1 
#     3 2 1 
#       2 1 
#         1 