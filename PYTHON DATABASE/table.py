import mysql.connector
try:
    dbobject= mysql.connector.connect(host="localhost",user="root",password="Joshna@123",database="world")
    dbcursor=dbobject.cursor()
    dbcursor.execute("insert into emp(eid,ename ,esal) values(102,'joshi',50000)")
    dbobject.commit()
except mysql.connector.DatabaseError as e:
    dbobject.rollback()
    print(e)
finally:
    if dbcursor:
        dbcursor.close()
    if dbobject:
        dbobject.close()
