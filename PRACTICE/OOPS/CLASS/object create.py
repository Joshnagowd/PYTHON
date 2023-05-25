class Computer:
    def config(self):
        print("Hello joshna")
comp1= Computer()
comp2=Computer()
comp1.config()
comp2.config()
Computer.config(comp1)
Computer.config(comp2)