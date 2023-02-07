class Parent():
    def m1(self):
        print("Parent class m1() method")
class ChildOne(Parent):
    def m2(self):
        print("Child class m2() method")
class ChildTwo(Parent):
    
    def m3(self):
        print("childTwo class m3() method")
c= ChildOne()
c.m1()
c.m2()
c= ChildTwo()
c.m1()
c.m3()