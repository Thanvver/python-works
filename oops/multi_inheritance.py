# class P1:
#     def m1(self):
#         print("inside class p1 m1 method")

# class P2:
#     def m2(self):
#         print("inside method p2 m2 method")

# class Child(P2,P1):
#     def m3(self):
#         print("inside class child m3 method")

# obj=Child()
# obj.m3()
# obj.m2()
# obj.m1()

class P1:
    def m1(self):
        print("inside class p1 m1 method")

class P2:
    def m1(self):
        print("inside method p2 m1 method")

class Child(P2,P1):
    def m3(self):
        print("inside class child m3 method")

obj=Child()
obj.m1()

class Calculator:
    def add(self,n1,n2):
        print(n1+n2)

    def add(self,n1,n2,n3):
        print(n1+n2+n3)

obj=Calculator()
obj.add(10,20,4)
