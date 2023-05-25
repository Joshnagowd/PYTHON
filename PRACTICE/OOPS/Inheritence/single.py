class Student:
    def pen(self):
        print("pen is printed")
    def blue(self):
        print("blue pen")
class Teacher(Student):
    def chalk(self):
        print("chalk")
b = Student()
b.pen()
b.blue()
a = Teacher()
