class Duck:
    def talk(self):
        print("Quack quack")

class Dog:
    def talk(self):
        print("Bow bow")
class Cat:
    def talk(self):
        print("meow meow")
def animal(obj):
    obj.talk()

l = [Duck(),Dog(),Cat()]
for obj in l:
    animal(obj)
