class Account:
    def open_Account(self):
        print("Account openend")
    def depositAccount(self,amount):
        self.accAmount = amount
        print("Account is closed")
t = Account()
t.open_Account()
t.depositAccount(500)
print(Account.__dict__)
print(t.__dict__)
