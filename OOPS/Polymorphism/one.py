class Emp:
    def cal_Tax(self):
        print("Employee tax")
class PE:
    def cal_Tax(self):
        print("Permanent Employee tax")
class CE:
    def cal_Tax(self):
        print("Contract Employee tax")
    
def exec(obj):
    obj.cal_Tax()
exec(Emp())
exec(PE())
exec(CE())