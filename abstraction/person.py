# class Person:
#     def __init__(self):
#      self.name="sukumar"

#     def bio(self):

#         self.adr="abc"
#         self.course="xyz"

# obj=Person()
# print(obj.name)

# class Student:
#     def __init__(self,name,course):
#       self.name=name
#       self.course=course

#     def get_student(self):
#        print("my name is",self.name,"and my course is",self.course)

# obj=Student("sukumar","python")
# obj.get_student()
# obj1=Student("abc","xyz")
# obj1.get_student()

# class Book:
#     def _init_(self):
#         self.id=int(input("enter the id"))
#         self.title=input("enter name")
#         self.author=input("enter author")
#         self.price=int(input("enter price"))
#     def getauthor(self):
#      print(self.author)
#     def gettitle(self):
#      print(self.title)
#     def setprice(self):
#      self.price=int(input("enter price"))
#     def settitle(self):
#      self.title=input("enter the title")

# b1=Book()
# b1.getauthor()
# b1.gettitle()


class Mobile:
     def mob(self):
         print("oneplus")
     def car(self):
         print("bmw")
     def bike(self):
         print("h2r")


class Child(Mobile):
    def bike(self):
        print("pulsar")

obj=Child()
obj.mob()
obj.car()
obj.bike()


