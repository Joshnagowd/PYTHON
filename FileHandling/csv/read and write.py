import csv
f1 = open("data.csv","r")
f2 = open("newData.csv","w")
reader =csv.reader(f1)
csvwriter=csv.writer(f2)
for line in reader:
    csvwriter.writerow(line)
f1.close()
f2.close()