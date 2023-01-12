prices =[15, 200, 30, 400, 70, 500]
new_Prices=list(filter(lambda n : True if n<100 else False, prices))
print(prices)
print(new_Prices)