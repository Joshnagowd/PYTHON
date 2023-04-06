num=int(input("enter number:"))
reverse=int(str(num)[::-1])
if num==reverse:
    print("palindrome")
else:
    print("not palindrome")