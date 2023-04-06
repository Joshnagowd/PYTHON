num = 5
sp =num-1
st = 1
for i in range(0,num):
    for j in range(0,sp):
        print('',end= "")
        for k in range(0,st):
            print('*',end="")
    print()
sp-=1
st+=1
    