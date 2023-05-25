import mysql.connector
mydb = mysql.connector.connect(host='localhost',user="root",password='Joshna@123')
mycursor = mydb.cursor()
mycursor.execute('select * from python')
result= mycursor.fetchall()
for i in result:
    print(i)