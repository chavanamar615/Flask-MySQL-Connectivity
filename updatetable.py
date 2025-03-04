import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sid=int(input("enter student id whose information you have to update:"))
sname=input("enter new student name:")
percentage=float(input("enter student percentage:"))
age=int(input("enter student age:"))
sql="update student set sname=%s,percentage=%s,age=%s where sid=%s"
val=(sname,percentage,age,sid) #give val within order
cursor.execute(sql,val)
con.commit()
 