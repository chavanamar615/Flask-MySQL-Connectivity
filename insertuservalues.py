import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sname=input("enter student name:")
percentage=float(input("Enter student percentage:"))
age=int(input("enter stduent age:"))
sql="insert into student (sname,percentage,age) values(%s,%s,%s)"
val=(sname,percentage,age)
cursor.execute(sql,val)
con.commit()

