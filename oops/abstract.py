from abc import ABC,abstractmethod

class Bike:

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class hunter(Bike):

    def start(self):
        print("hunter start")
    def accelarate(self):
        print("hunter accelartes")
    def stop(self):
        print("hunter stops")

obj=hunter()
obj.start()
obj.accelarate()
obj.stop()