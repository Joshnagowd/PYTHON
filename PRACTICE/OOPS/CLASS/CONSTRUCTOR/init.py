class computer:
    def __init__(self,name,age):
        self.computer_name=name
        self.computer_age=age

    def config(self):
        print("hello gm",self.computer_name,self.computer_age)

t1=computer("joshna",92)
t1.config()
print(t1.__dict__)


