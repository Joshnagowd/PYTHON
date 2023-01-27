import csv
f = open("one.json","r")
reader = csv.reader(f)
for line in reader:
    
    for word in line:
        print(word)
    print()
    