class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self,name,age,sal,id):
        super().__init__(name,age)

        self.sal=sal
        self.id=id
    def display(self):
        print("Employee name",self.name)
        print("Employee age", self.age)
        print("Employee sal", self.sal)
        print("Employee id", self.id)
a1= Employee("Joshna",22,40000,1)
a1.display()
a2=Employee("ram",23,43000,2)
a2.display()


