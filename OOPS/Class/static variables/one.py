class Test:
    a = 10
    def __init__(self):    #constructor
        Test.b = 20
    def m1(self):          #instance
        Test.c = 30
    @classmethod
    def m2(cls):           #class
        cls.d = 40
        Test.e = 50
    @staticmethod
    def m3():
        Test.f = 60
t = Test()
t.m1()
Test.m2()
t.m2()
print(t.a)
print(t.b)
print(t.c)

print(t.__dict__)
print(Test.__dict__)
