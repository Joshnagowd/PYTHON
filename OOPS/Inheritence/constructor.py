class Account:
    def __init__(self,amount):
        self.amount = amount

class SA(Account):
    def __init__(self,id,name,amount):
        self.id = id
        self.name = name
        

a1 = SA(101,"Rahul", 50000)
a2 = Account(40000)
print(a1.__dict__)