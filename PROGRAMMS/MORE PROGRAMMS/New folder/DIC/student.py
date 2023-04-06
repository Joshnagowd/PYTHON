rec={}
n=int(input("enter number of students:"))
i=1
while i<=n:
    name=input("enter name of student:")
    marks=input("enter marks of student:")
    rec[name]=marks
    i=i+1
print("name of student","\t","marks of students")
for x in rec:
    print("\t",x,"\t\t",rec[x])
    