def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello how are you")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("good morning")

wish("krish")
wish("ram")
wish("sunny")