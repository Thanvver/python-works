class Car:
    def start(self):
        print("key start")
    def break_type(self):
        print("drum breaks")
    def transmission(self):
        print("manual")
    
class Ambassador(Car):
    pass

class swift(Car):
    def break_type(self):
        print("disk break")

obj=swift()
obj.start()
obj.break_type()
obj.transmission()

