class computer:
    def __init__(self):
        self.name="joshi"
        self.age= 25
    def update(self):
        self.age=22
com1=computer()
com2=computer()

com1.name="krish"
com1.age=23
#com1.update()
com2.update()
print(com1.name)
print(com1.age)

print(com2.name)
print(com2.age)