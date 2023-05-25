class student:

    def pen(self):
        print("elder")
    def pencil(self):
        print("younger")
class Teacher(student):
    def pen(self):
        super().pen()
        print("Teacher")
    def chalk(self):
        print("board")
c1=Teacher()
c1.pen()
c1.pencil()