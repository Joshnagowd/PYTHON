class Father:
    def m1(self):
        print("Father class m1() method")
    def m2(self):
         print("Father class m2() method")
class Mother:
    def m3(self):
        print("mother class m3() method")
class Child(Father,Mother):
    def m4(self):
        print("Child class m4() method")
c= Child()
c.m1()
c.m2()
c.m3()
c.m4()