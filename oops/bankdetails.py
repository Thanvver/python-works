class Bank_details:

    acc_no:int
    name:str
    ifsc_code:int
    branch:str
    acc_type:str
    balance:int
    bank_name:str

    def create(self,acc_no,name,ifsc_code,branch,acc_type,balance,bank_name):
        self.acc_no=acc_no
        self.name=name
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.acc_type=acc_type
        self.balance=balance
        self.bank_name=bank_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name}")

    


    


        