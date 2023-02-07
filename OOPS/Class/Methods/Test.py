class Test:
    a = 10
    def __init__(self):
        self.a = 20
        self.b = 30
        self.c = 40
    def m1(self):
        self.d = 50
        self.e = 70
t1 = Test()
t2 = Test()
print(Test.__dict__)
print(t1)
t1.m1()
print(t1.__dict__)
print(t2.__dict__)