number = int(input("enter any number:"))
if number >1:
    for i in range(2,number):
        if(number% i)== 0:
            print(number,"number is not a prime number")
            break
    else:
            print(number,"is prime")