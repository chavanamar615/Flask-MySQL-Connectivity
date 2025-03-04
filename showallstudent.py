import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sql="select * from student"
cursor.execute(sql)
records=cursor.fetchall()
print(records)      #o/p-[(2, 'pratik', 77.0, 19)] o/p in form of list
for stud in records:
    print(stud) #o/p-(2, 'pratik', 77.0, 19) o/p in form of tuple