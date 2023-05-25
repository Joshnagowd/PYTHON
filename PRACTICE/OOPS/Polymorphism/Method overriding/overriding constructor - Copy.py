class P:
    def __int__(self):
        print("parent constructor")
class C(P):
    def __int__(self):
        print("chhild class constructor")
a1=C()