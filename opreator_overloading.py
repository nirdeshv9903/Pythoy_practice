# Create a Time class with hours and minutes.
# Overload the + operator to add two Time objects correctly.
class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    def display(self):
        print("Hours: ",self.hours)
        print("Minutes: ",self.minutes)
    def __add__(self,other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        return Time(hours,minutes)
t1 = Time(2,30)
t2 = Time(3,45)
t3 = t1 + t2
t3.display()

# Create a Distance class with attributes feet and inches.
# Overload the * operator to multiply the distance by a scalar value.(any numeric value)
class Distance:
    def __init__(self,feet,inches):
        self.feet = feet
        self.inches = inches
    def display(self):
        print("Feet: ",self.feet)
        print("Inches: ",self.inches)
    def __mul__(self,other):
        feet = self.feet * other
        inches = self.inches * other
        return Distance(feet,inches)
d1 = Distance(5,6)
d2 = d1 * 2
d2.display()

# Create a Rectangle class with length and width.
# Overload the == operator to compare the area of two rectangles.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def display(self):
        print("Length: ",self.length)
        print("Width: ",self.width)
    def __eq__(self,other):
        area1 = self.length * self.width
        area2 = other.length * other.width
        if area1 == area2:
            return True
        else:
            return False
r1 = Rectangle(2,3)
r2 = Rectangle(3,2)
if r1 == r2:
    print("Areas are equal")
else:
    print("Areas are not equal")