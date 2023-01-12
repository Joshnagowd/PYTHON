prices =[15, 200, 30, 45, 70, 500]
def belowhundred(n):
    if n < 100:
        return True
    else:
        return False
new_Prices=list(filter(belowhundred, prices))
print(prices)
print(new_Prices)