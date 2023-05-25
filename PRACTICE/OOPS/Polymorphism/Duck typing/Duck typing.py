class pycharm:
    def execute(self):
        print("child")
        print("parent")
class myeditor:
    def execute(self):
        print("grand parent")
        print("grand son")
        print("child")
        print("parent")
class laptop:
    def code(obj):
        obj.execute()

l=[pycharm(),myeditor()]
for obj in l:
    laptop.code(obj)

