class Test:
    def __init__(self):
        self.a = 10
        self.b =20
        self.c = 30
    def m1(self):
        self.d=60
t1 = Test()
t2 =Test()
print(t1)
t1.m1()
print(t1.__dict__)
print(t2.__dict__)