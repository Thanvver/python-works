class Employee:
    id:int
    name:str
    gender:str
    department:str
    salary:int

    def create(self,id,name,gender,dept,salary):
        self.id=id
        self.name=name
        self.gender=gender
        self.department=dept
        self.salary=salary

    def get(self):
        print(self.id,self.name,self.department,self.salary)

emp1=Employee()
emp1.create(1001,"ravi","male","it",56000)
emp2=Employee()
emp2.create(1002,"hari","male","hr",34000)

emp1.get()
emp2.get()
