# -------Oops (Object Oriented Programming)-------

# To map with real world scenarios, we started using objected in code
# This is called Object Oriented Programming.

# ------ Object and class in Python-----
# class is a blueprint for creating objects.

# create class
# class Student:
#     name = "Karan Kumar"

# # create object (instance)
# s1=Student()
# print(s1.name)

# class car:
#     color = "Blue"
#     brand = "BMW"

# print(car.color)
# print(car.brand)

# ------- __init__ Function ------- (Constructor)

# All class have a function call __init__(), whichis always executed when
#  when the class is being initiated.

# # creating class
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# # create object
# s1 = Student("B.Kumar")
# print(s1.name)

# class Student:
#     # default constructors
#     def __init__(self):
#         pass
#     # parameterized constructors
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.mark = marks

# S1 = Student("B.Kumar", 93)
# print(S1.name, S1.mark)



# Class and Instance Attributes

# 1. Obj.att  2.class attr   (obj attr > class attr)

# class Student:
#     college_Name = "D.Y Patil"
#     # name = "anonymous" # class attributes

#     def __init__(self,name, marks):
#         self.name = name #obj attr > class attr
#         self.mark = marks
#         print("Adding new student")

# s1 = Student("karan", 56)
# print(s1.name, s1.mark)



# Methods
#  Methods are function that belong to objects.


# class Student:
#     college_Name = "D.Y Patil"

#     def __init__(self,name, marks):
#         self.name = name #obj attr > class attr
#         self.mark = marks
    
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.mark

# s1 = Student("karan", 56)
# s1.welcome()
# print(s1.get_marks())

# PQ = 

class Student:
    college_Name = "D.Y Patil"

    def __init__(self,subject, marks):
        self.subject = subject #obj attr > class attr
        self.mark = marks
    
    def welcome(self):
        print("welcome student,", self.subject)
    def get_marks(self):
        return self.mark

s1 = Student("Maths", 72)
s2 = Student("Physics", 85)
s3 = Student("Chemistry", 74)
print((s1.get_marks()+s2.get_marks() +s3.get_marks())/3)
