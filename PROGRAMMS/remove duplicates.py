list = [12, 36, 56, 36, 36, 50, 56, 12] 
  
x = [] 
[x.append(y)
 for y in list
 if y not in x] 
    
print (x)
