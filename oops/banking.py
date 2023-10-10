from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def fund_transfer(self):
        pass
    @abstractmethod
    def bal_enq(self):
        pass
    @abstractmethod
    def trans_history(self):
        pass

class Gpay(Bank):
    def fund_transfer(self):
        print("gpay fund transfer")
    def bal_enq(self):
        print("gpay balance enquiry")
    def trans_history(self):
        print("gpay transaction history")
    def gift_card(self):
        print("gift card")

obj=Gpay()
obj.fund_transfer()
obj.bal_enq()
obj.trans_history()
obj.gift_card()
