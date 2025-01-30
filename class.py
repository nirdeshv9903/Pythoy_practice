# create a class student with student name, rollnumber and 3 subjects marks as attributes. 
# create a method to accept the attributes create 
# another method to calculate the total average of student marks and display the final result of the student. 
# create three objects and display the object details.

class student:
    def __init__(self,name,rollnumber,marks1,marks2,marks3):
        self.name = name
        self.rollnumber = rollnumber
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def display(self):
        print("Name: ",self.name)
        print("Rollnumber: ",self.rollnumber)
        print("Marks1: ",self.marks1)
        print("Marks2: ",self.marks2)
        print("Marks3: ",self.marks3)
    def total(self):
        total = self.marks1 + self.marks2 + self.marks3
        avg = total/3
        print("Total: ",total)
        print("Average: ",avg)
s1 = student("Nine",101,90,80,70)
s1.display()
s1.total()