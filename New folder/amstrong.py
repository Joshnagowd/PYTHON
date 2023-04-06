num = int(input("enter number:"))
sum = 0
temp=num
order=len(str(num))
while temp>0:
    digit=temp%10
    sum = sum + digit **order
    temp=temp//10
if num==sum:
    print(num,"Amstrong")
else:
    print(num,"not Amstrong")
