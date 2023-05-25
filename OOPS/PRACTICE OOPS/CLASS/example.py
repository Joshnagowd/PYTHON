class Student:
//overloading
     def int __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def  string __init__(self,name,roo,class):
        self.name=name

class school extends student:
    def  string __init__(self,name,roo,class):
        self.name=name

student2=Student("sa",23)

print(student2.name,student2.roll)
