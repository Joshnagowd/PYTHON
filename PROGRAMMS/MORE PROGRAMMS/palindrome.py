num = 122


temp = num
reverse=0
while temp>0:
    digit = temp%10
    reverse=(reverse*10)+digit
    temp//=10
if (num==reverse):
    print("Palindrome")
else:
    print("not Palindrome")