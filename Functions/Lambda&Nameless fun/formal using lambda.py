a = int (input("enter first number-"))
b = int (input("enter second number-"))
maxValue = lambda a, b : a if a > b else b
print(maxValue(a,b))