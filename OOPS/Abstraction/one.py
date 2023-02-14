from abc import *
class Emp(ABC):
    @abstractmethod
    def cal_Tax(self):
        pass
class PE(Emp):
    def cal_Tax(self):
        return 1800
e1 = PE()
print(e1.cal_Tax())