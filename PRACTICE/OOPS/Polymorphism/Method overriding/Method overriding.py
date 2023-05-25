class P:
    def property(self):
        print("GOLDEN")
    def marry(self):
        print("SILVER")
class C(P):
    def marry(self):
        super().marry()
        print("COPPER")
a1=C()
a1.property()
a1.marry()