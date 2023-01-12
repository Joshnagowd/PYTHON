a = int (input("enter first number-"))
b = int (input("enter second number-"))
def maxValue(a , b):
    if a > b :
        return a
    else:
        return b
print(maxValue(a,b))