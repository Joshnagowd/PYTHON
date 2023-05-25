class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self, a,b):
        s3= a+b
        return s3
s1=Student(22,33)

print(s1.sum(5,5))