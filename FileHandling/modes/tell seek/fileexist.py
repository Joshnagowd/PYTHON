import os,sys
fname=input("enter file name:")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
else:
    print("file does not exist:",fname)
    sys.exit(0)
print("the content of file is:")
data= f.read()
print(data)
