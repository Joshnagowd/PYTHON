f=open("ramu.txt",'w') 
list=["sunny\n","bunny\n","vinny\n","chinny"] 
f.writelines(list) 
print("List of lines written to the file successfully") 
f.close()
