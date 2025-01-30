# write a program to find largest of three numbers by creating 4 types of user defined functions
a = int(input("Enter the first number: ")) # 10
b = int(input("Enter the Second number: ")) # 50
c = int(input("Enter the third number: ")) # 30
#using the arguments and return type
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(largest(a,b,c))

# using  the no arguments and no return type
def largest():
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest()

# using the arguments and no return type
def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest(a,b,c)

#using the no arguments and return type
def largest():
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(largest())