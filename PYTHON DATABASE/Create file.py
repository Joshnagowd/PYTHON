import mysql.connector
try:
    dbobj= mysql.connector.connect(host="localhost",user="root",password="Joshna@123",database="world")
    if dbobj:
        print("connection succesfull")
    dbcursor=dbobj.cursor()
    dbcursor.execute('create table emp(eid int,ename varchar(30),esal double(10,2))')
    print("table created")
except mysql.connector.DatabaseError as e:
    print(e)
