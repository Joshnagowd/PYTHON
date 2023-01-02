x = int(input("First Number:"))
y =int(input("Second Number:"))
z  =int(input("Third Number:"))

if x<y and x<z:
    min = x
elif y<z:
    min = y
else:
    min = z
print(min)
