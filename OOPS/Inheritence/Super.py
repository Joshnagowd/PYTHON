class Account:
    def __init__(self,id,name):
        pass
class SA(Account):
    def __init__(self,id,name,amount):
        super().__init__(id,name)
        self.amount = amount
        
a1 = SA(101,"Joshi",50000)
print(a1.__dict__)
