class Parent:

    props=["discover","wagnor"]
    def get_properties(self):
        return self.props
    
class Child(Parent):
    def get_properties(self):
        self.p=super().get_properties()
        self.p.append("ducatti")
        return self.p
    
ch=Child()
print(ch.get_properties())

