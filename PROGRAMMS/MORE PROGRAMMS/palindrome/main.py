n=int(input("enter numb:"))
reverse=0
sum=0
temp=n
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp//=10
if n ==reverse:
    print("palindrome")
else:
    print("not")