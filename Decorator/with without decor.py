def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello how are you")
        else:
            func(name)
    return inner

def wish(name):
    print("good morning")
decorator=decor(wish)

wish("krish")
wish("ram")
wish("sunny")
decorator("sunny")