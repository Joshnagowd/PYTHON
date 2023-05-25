import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='joshnadb', user='root', password='Joshna@123')
    cursor = con.cursor()
    cursor.execute("create table employees(sno int(5) primary key,name varchar(10),gender varchar(7),age(2))")
    print("Table Created")
    sql= "insert into employees(sno,name,gender,age) VALUES(%s,%s,%s,%s)"
    records = [(1, 'Ram', 'Male', '24'),
             (2, 'Sita', 'Female', '22'),
             (3, 'lucky', 'Male', '24')]

    cursor.executemany(sql, records)
    con.commit()
    print("Records inserted successfully")
    cursor.execute("select * from village")
    data=cursor.fetchall()
    for row in data:
        print("village sno:", row[0])
        print("village name:", row[1])
        print("village gender:", row[2])
        print("village age:", row[3])
        print()
        print()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("there is a problem in sql:", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


