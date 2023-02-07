class Account:
    min_Bal = 500
    def __init__(self):
        print("Constructor will execute")
        self.a = 10
        self.b = 20
    def Open_Account(self):
        self.c = 30
        self.d = 40
        Account.amount= 5000
    @classmethod
    def info_Account(cls):
        pass
    @staticmethod
    def calc(a,b):
        pass
a1 = Account()
a2 = Account()
a1.Open_Account()
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)