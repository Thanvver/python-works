class Parent:

    phone="iphone11pro"
    bike="ntorq125"

    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class Child(Parent):
    pass

obj=Child()
obj.mobile()