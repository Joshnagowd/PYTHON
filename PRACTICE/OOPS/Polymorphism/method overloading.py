class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1= Book(201)
b2=Book(22)
print("book pages:", b1+b2)
