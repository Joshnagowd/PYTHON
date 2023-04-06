s=input("enter string")
subs=input("enter substring")
try:
    n=s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found")