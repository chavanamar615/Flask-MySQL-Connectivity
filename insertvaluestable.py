import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sql="insert into student(sname,percentage,age) values ('pratik',89,23)"
cursor.execute(sql)
con.commit()