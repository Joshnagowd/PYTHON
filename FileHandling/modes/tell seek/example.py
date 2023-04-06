data = "this is joshna"
f= open("hmm.txt","w")
f.write(data)
with open("hmm.txt","r+") as f:
    text=f.read()
    print(text)
    print("the current position:",f.tell())
    f.seek(15)
    print("the current position of:",f.tell())
    f.write(" Germs")
    f.seek(0)
    text=f.read()
    print("Data after modification:")
    print(text)
