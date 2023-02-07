class Bank:
    a = 10
    def m1(self):
        self.amount= 5000
        id = 101
b1 = Bank()
b1.m1()
print(id)
print(b1.__dict__)
print(Bank.__dict__)