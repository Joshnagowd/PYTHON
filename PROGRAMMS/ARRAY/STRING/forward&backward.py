s = input("enter string:")

for i in s:
    print(i,end='')
print(":forward direction")
for i in s[::-1]:
    print(i,end='')
print(":Backward direction")
