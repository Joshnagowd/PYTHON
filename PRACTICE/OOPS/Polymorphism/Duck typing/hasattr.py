class Duck:
    def talk(self):
        print("Quack quack")

class Dog:
    def bark(self):
        print("Bow bow")
class Cat:
    def talk(self):
        print("meow meow")
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
d = Duck()
f1(d)
h=Dog()
f1(h)
g = Cat()
f1(g)
a1=[Duck(),Cat()]
for obj in a1:
    obj.talk()
a2=Dog()
a2.bark()
r=Dog()
f1(r)