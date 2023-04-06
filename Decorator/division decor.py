def divison():
    def inner(a,b):
        print("we are dividing",a,"with",b)
        if b==0:
            print("oops")
        else:
            return func(a,b)
        return inner
@divison
def division(a,b):
    return a/b
print(division(20,2))

